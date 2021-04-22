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
		sh '/usr/local/bin/ansible --version'
		dir("/Users/strangepear2019/.ansible") {
			sh "pwd"
			sh "rm -rf *"
		}	
		
		checkout scm
		
		script {
			    remoteWorkspace = env.WORKSPACE
			
			    echo "Remote workspace is ${remoteWorkspace}"
			
			    dir("${remoteWorkspace}") {
					    sh "rm -rf *"
				        if (fileExists('ibm-ibm_zosmf-1.0.0.tar.gz')) {
					            echo "ibm-ibm_zosmf-1.0.0.tar.gz existed"
					            sh 'rm ibm-ibm_zosmf-1.0.0.tar.gz'
					            sh '/usr/local/bin/ansible-galaxy collection build'
				        } else {
					            sh '/usr/local/bin/ansible-galaxy collection build'
				        }
				        sh "pwd"
				        sh '/usr/local/bin/ansible-galaxy collection install ibm-ibm_zosmf-1.0.0.tar.gz'
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
		    dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zosmf") {
                sh "pwd"
			    sh '/usr/local/bin/ansible-test sanity'
			    sh '/usr/local/bin/ansible-lint roles/zmf_workflow_complete'
			    sh '/usr/local/bin/ansible-lint roles/zmf_cpm_manage_software_instance'
			    sh '/usr/local/bin/ansible-lint roles/zmf_cpm_provision_software_service'
			    sh '/usr/local/bin/ansible-lint roles/zmf_cpm_remove_software_instance'
				sh '/usr/local/bin/bandit -r /Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zosmf'
         	    }
		    dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/host_vars") {
			    sh "cp -p /Users/strangepear2019/ansible-tmp/p00.yml /Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/host_vars/p00.yml"
			    sh "cp -p /Users/strangepear2019/ansible-tmp/hosts /Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/hosts"
		    }
		    echo 'Workflow BVT'
		    dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks") {
		    	sh '/usr/local/bin/ansible-playbook workflow_complete_CICDtest1.yml'
		    }
			echo 'CPM BVT'
			dir("/Users/strangepear2019/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks") {
		    	sh '/usr/local/bin/ansible-playbook cpm_complete_CICDtest1.yml'
		    }
		    echo 'CICD test successfully!'
            }
        }
    }
}
