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
				daysToKeepStr: '180',
				numToKeepStr: '50',
			)
		)
	}

	stages {
        stage('CICD') {
            matrix {
                // 22 - local (python=3.9.18, ansible-core=2.15.11)
                axes {
                    axis {
                        name 'SSH_PORT'
                        values '22'
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
                            echo "****************************************************************************\n****************************************************************************"
                            echo "Check local env:"
                            sh "pwd"
                            sh '/bin/bash -c -l "python --version"'
                            sh '/bin/bash -c -l "which python"'
                            sh '/bin/bash -c -l "ansible --version"'
                            sh '/bin/bash -c -l "which ansible"'
                            
                            echo "Check installed python:"
                            sh '/bin/bash -c -l "python3.9 --version"'
                            sh '/bin/bash -c -l "which python3.9"'
                            sh '/bin/bash -c -l "python3.10 --version"'
                            sh '/bin/bash -c -l "which python3.10"'
                            sh '/bin/bash -c -l "python3.11 --version"'
                            sh '/bin/bash -c -l "which python3.11"'
                            
                            // echo "****************************************************************************\n****************************************************************************"
                            // echo "Build and install ansible collection:"
                            // checkout scm
                            
                            // script {
                            //     ansibleCollection = "/home/test/.ansible"
                            //     echo "Ansible collection is: ${ansibleCollection}"
                            //     dir("${ansibleCollection}") {
                            //         sh "pwd"
                            //         sh "rm -rf *"
                            //     }
                                
                            //     remoteWorkspace = env.WORKSPACE
                            //     echo "Remote workspace is: ${remoteWorkspace}"
                            //     dir("${remoteWorkspace}") {
                            //         sh "pwd"
                            //         sh '/bin/bash -c -l "ansible-galaxy collection build --force"'
                            //         sh '/bin/bash -c -l "ansible-galaxy collection install ibm-ibm_zosmf-*.tar.gz --force"'
                            //     }
                            // }
                        }
                    }
                    
                    stage('Test-python3.11') {
                        steps {
                            echo "****************************************************************************\n****************************************************************************"
                            echo "Test:"
                            
                            script {
                                echo "****************************************************************************"
                                echo "Setup venv:"
                                
                                pythonVersion = "python3.11"
                                venvPath = "/home/test/venv/${pythonVersion}"
                                echo "Venv is: ${venvPath}"
                                sh """#!/bin/bash
                                    ${pythonVersion} -m venv ${venvPath}
                                    source ${venvPath}/bin/activate
                                """
                                
                                echo "Install:"
                                sh '/bin/bash -c -l "pip install --upgrade pip"'
                                sh '/bin/bash -c -l "pip install ansible"'
                                sh '/bin/bash -c -l "pip install ansible-lint"'
                                sh '/bin/bash -c -l "pip install flake8"'
                                sh '/bin/bash -c -l "pip install pylint"'
                                sh '/bin/bash -c -l "pip install voluptuous"'
                                sh '/bin/bash -c -l "pip install yamllint"'
                                sh '/bin/bash -c -l "pip install rstcheck"'
                                sh '/bin/bash -c -l "pip install bandit"'
                                
                                echo "Check:"
                                sh '/bin/bash -c -l "python --version"'
                                sh '/bin/bash -c -l "which python"'
                                sh '/bin/bash -c -l "ansible --version"'
                                sh '/bin/bash -c -l "which ansible"'
                                
                                echo "****************************************************************************"
                                echo "Install ansible collection:"
                                ansiblePath = "${venvPath}/.ansible"
                                dir("${remoteWorkspace}") {
                                    sh "pwd"
                                    sh """#!/bin/bash
                                        ${venvPath}/bin/ansible-galaxy collection build --force
                                        ${venvPath}/bin/ansible-galaxy collection install ibm-ibm_zosmf-*.tar.gz -p ${ansiblePath}/collections --force
                                    """
                                }
                                
                                echo "****************************************************************************"
                                echo "Run sanity test:"
                                dir("${ansiblePath}/collections/ansible_collections/ibm/ibm_zosmf") {
                                    sh "pwd"
                                    sh """#!/bin/bash
                                        ${venvPath}/bin/ansible-test --version
                                        ${venvPath}/bin/ansible-test sanity
                                    """
                                }
                                
                                echo "****************************************************************************"
                                echo "Run ansible-lint:"
                                dir("${ansiblePath}/collections/ansible_collections/ibm/ibm_zosmf") {
                                    sh "pwd"
                                    sh """#!/bin/bash
                                        ${venvPath}/bin/ansible-lint --version
                                        ${venvPath}/bin/ansible-lint plugins
                                        ${venvPath}/bin/ansible-lint roles
                                        ${venvPath}/bin/ansible-lint --profile production
                                    """
                                }
                                
                                echo "****************************************************************************"
                                echo "Run bandit scan:"
                                dir("${ansiblePath}/collections/ansible_collections/ibm/ibm_zosmf") {
                                    sh "pwd"
                                    sh """#!/bin/bash
                                        ${venvPath}/bin/bandit --version
                                        ${venvPath}/bin/bandit -r plugins
                                    """
                                }
                                
                                echo "****************************************************************************"
                                echo "Run BVT:"
                            }
                        }
                    }
                }
            }
        }
    }
}