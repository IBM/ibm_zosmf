def remoteWorkspace = ''

pipeline {
	agent none
	
	options {
		// Skip checking out code from source control by default in the agent directive
		skipDefaultCheckout()
		// Disallow concurrent executions of the Pipeline
		disableConcurrentBuilds()
		// only keep 15 builds to prevent disk usage from growing out of control
		buildDiscarder(
			logRotator(
				daysToKeepStr: '15',
				numToKeepStr: '15',
			)
		)
   
	}
	
	stages {
		stage('Build') {
			agent {
				node {
					label 'zmf-ansible-configuration'
					customWorkspace "workspace/${env.BRANCH_NAME}"
				}
			}
			steps {
				echo 'Hello, build'
				sh "pwd"
				sh '/usr/bin/ansible --version'
				dir("/home/test/.ansible") {
					sh "pwd"
					sh "rm -rf *"
				}	
				
				checkout scm
				
				script {
					remoteWorkspace = env.WORKSPACE
				
					echo "Remote workspace is ${remoteWorkspace}"
				
					dir("${remoteWorkspace}") {
							if (fileExists('ibm-ibm_zosmf-1.1.0.tar.gz')) {
									echo "ibm-ibm_zosmf-1.1.0.tar.gz existed"
									sh 'rm ibm-ibm_zosmf-1.1.0.tar.gz'
									sh '/usr/bin/ansible-galaxy collection build --force'
							} else {
									sh '/usr/bin/ansible-galaxy collection build --force'
							}
							sh "pwd"
							sh '/usr/bin/ansible-galaxy collection install ibm-ibm_zosmf-1.1.0.tar.gz --force'
					}
				}
            }
		}

		stage('Test') {
			agent {
				node {
					label 'zmf-ansible-configuration'
					customWorkspace "workspace/${env.BRANCH_NAME}"
				}
			}

			steps {
				echo 'sanity test'
				dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf") {
					sh "pwd"
					sh '/usr/bin/ansible-test sanity'
					sh '/usr/bin/ansible-lint roles/zmf_workflow_complete'
					sh '/usr/bin/ansible-lint roles/zmf_cpm_manage_software_instance'
					sh '/usr/bin/ansible-lint roles/zmf_cpm_provision_software_service'
					sh '/usr/bin/ansible-lint roles/zmf_cpm_remove_software_instance'
					sh '/usr/bin/bandit -r /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/plugins/'
					}
				dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/host_vars") {
					sh "cp -p /home/test/ansible-tmp/P00.yml /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/host_vars/P00.yml"
					sh "cp -p /home/test/ansible-tmp/P01.yml /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/host_vars/P01.yml"
					sh "cp -p /home/test/ansible-tmp/hosts /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/hosts"
				}
				echo 'SCA BVT'
				dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks") {
					sh '/usr/bin/ansible-playbook sca_CICDtest1.yml'
				}
				echo 'Workflow BVT'
				dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks") {
					sh '/usr/bin/ansible-playbook workflow_complete_CICDtest1.yml'
				}
				echo 'CPM BVT'
				dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks") {
					sh '/usr/bin/ansible-playbook cpm_complete_CICDtest1.yml'
				}
				echo 'CICD test successfully!'
			}
		}
    }
}
