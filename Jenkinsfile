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
            // 22 - ansible2.12 + python3.8
            // 3335 - ansible2.9 + python2.7
            // 3339 - ansible2.13.1 + python3.9.13
            // 3338 - ansible2.14.2 + python3.9.16
                axes {
                    axis {
                        name 'SSH_PORT'
                        values '3338' //'22', '3335', '3339', '3338'
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
                            sh "whoami"

                            checkout scm

                            sh '/bin/bash -c -l "ansible --version"'
                            dir("/home/test/.ansible") {
                                sh "pwd"
                                sh "rm -rf *"
                            }



                            script {
                                remoteWorkspace = env.WORKSPACE

                                echo "Remote workspace is ${remoteWorkspace} on ${SSH_PORT}"

                                dir("${remoteWorkspace}") {
                                        if (fileExists('ibm-ibm_zosmf-1.4.1.tar.gz')) {
                                                echo "ibm-ibm_zosmf-1.4.1.tar.gz existed on ${SSH_PORT}"
                                                sh 'rm ibm-ibm_zosmf-1.4.1.tar.gz'
                                                sh '/bin/bash -c -l "ansible-galaxy collection build --force"'
                                        } else {
                                                sh '/bin/bash -c -l "ansible-galaxy collection build --force"'
                                        }
                                        sh "pwd"
                                        sh '/bin/bash -c -l "ansible-galaxy collection install ibm-ibm_zosmf-1.4.1.tar.gz --force"'
                                }
                            }
                        }
                    }

                    stage('Test') {
                        steps {
                            echo "sanity test on ${SSH_PORT}"
                            // dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf") {
                            //     sh "pwd"
                            //     sh '/bin/bash -c -l "ansible-test sanity"'
                            //     sh '/bin/bash -c -l "ansible-lint plugins"'
                            //     sh '/bin/bash -c -l "ansible-lint roles"'
                            //     sh '/bin/bash -c -l "ansible-lint --profile production"'
                            //     sh '/bin/bash -c -l "bandit -r /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/plugins/"'
                            // }
                            dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/host_vars") {
                                sh "cp -p /home/test/ansible-tmp/P00.yml /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/host_vars/P00.yml"
                                sh "cp -p /home/test/ansible-tmp/P01.yml /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/host_vars/P01.yml"
                                sh "cp -p /home/test/ansible-tmp/hosts /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/"
                            }
                            dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/group_vars") {
                                sh "cp ${remoteWorkspace}/tests/CICD/playbooks/*.json /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/"
                                sh "cp ${remoteWorkspace}/tests/CICD/playbooks/*.yml /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/"
                                sh "cp ${remoteWorkspace}/tests/CICD/playbooks/group_vars/*.yml /home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks/group_vars/"
                            }
                            echo "SCA BVT on ${SSH_PORT}"
                            dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks") {
                                sh '/bin/bash -c -l "ansible-playbook sca_CICDtest1.yml"'
                            }
                            echo "Workflow BVT on ${SSH_PORT}"
                            dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks") {
                                sh '/bin/bash -c -l "ansible-playbook workflow_complete_CICDtest1.yml"'
                            }
                            echo "CPM BVT on ${SSH_PORT}"
                            dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks") {
                                sh '/bin/bash -c -l "ansible-playbook cpm_complete_CICDtest1.yml"'
                            }
                            echo "SM BVT on ${SSH_PORT}"
                            dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks") {
                                sh '/bin/bash -c -l "ansible-playbook software_management_reports_CICDtest1.yml"'
                            }
                            echo "ZMSC BVT on ${SSH_PORT}"
                            dir("/home/test/.ansible/collections/ansible_collections/ibm/ibm_zosmf/tests/CICD/playbooks") {
                                sh '/bin/bash -c -l "ansible-playbook zmsc_run_mgmt_service_CICDTest1.yml"'
                            }
                            echo "CICD test successfully on ${SSH_PORT}"
                        }
                    }
                }
            }
        }
    }
}