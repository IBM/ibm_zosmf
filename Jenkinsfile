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
        stage('BuildAndTest') {
            matrix {
                axes {
                    axis {
                        name 'SSH_PORT'
                        values '22', '3335', '3339'
                    }
                }
                agent {
                    node {
                        label "zmf-ansible-configuration-ssh-${SSH_PORT}"
                        customWorkspace "workspace/${env.BRANCH_NAME}"
                    }
                }
                stages {
                    stage('Build') {
                        steps {
                            echo "Hello, build on ${SSH_PORT}"
                            sh "pwd"
                            sh 'ansible --version'
                            dir("/home/test/.ansible") {
                                sh "pwd"
                                sh "rm -rf *"
                            }

                            checkout scm

                            script {
                                remoteWorkspace = env.WORKSPACE

                                echo "Remote workspace is ${remoteWorkspace} on ${SSH_PORT}"

                                dir("${remoteWorkspace}") {
                                        if (fileExists('ibm-ibm_zosmf-1.2.0.tar.gz')) {
                                                echo "ibm-ibm_zosmf-1.2.0.tar.gz existed on ${SSH_PORT}"
                                                sh 'rm ibm-ibm_zosmf-1.2.0.tar.gz'
                                                sh 'ansible-galaxy collection build --force'
                                        } else {
                                                sh 'ansible-galaxy collection build --force'
                                        }
                                        sh "pwd"
                                        sh 'ansible-galaxy collection install ibm-ibm_zosmf-1.2.0.tar.gz --force'
                                }
                            }
                        }
                    }

                    stage('Test') {
                        steps {
                            echo "sanity test on ${SSH_PORT}"
                            dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf") {
                                sh "pwd"
                                sh 'ansible-test sanity'
                                sh 'ansible-lint roles/zmf_workflow_complete'
                                sh 'ansible-lint roles/zmf_cpm_manage_software_instance'
                                sh 'ansible-lint roles/zmf_cpm_provision_software_service'
                                sh 'ansible-lint roles/zmf_cpm_remove_software_instance'
                                sh '/usr/bin/bandit -r /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/plugins/'
                                }
                            dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/host_vars") {
                                sh "cp -p /home/test/ansible-tmp/P00.yml /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/host_vars/P00.yml"
                                sh "cp -p /home/test/ansible-tmp/P01.yml /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/host_vars/P01.yml"
                                sh "cp -p /home/test/ansible-tmp/hosts /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/hosts"
                            }
                            echo "SCA BVT on ${SSH_PORT}"
                            dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks") {
                                sh 'ansible-playbook sca_CICDtest1.yml'
                            }
                            echo "Workflow BVT on ${SSH_PORT}"
                            dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks") {
                                sh 'ansible-playbook workflow_complete_CICDtest1.yml'
                            }
                            echo "CPM BVT on ${SSH_PORT}"
                            dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks") {
                                sh 'ansible-playbook cpm_complete_CICDtest1.yml'
                            }
                            echo "CICD test successfully on ${SSH_PORT}"
                        }
                    }
                }
            }
        }
    }
}
