def pythonVersionList = ["python3.9", "python3.10", "python3.11"]
def ansibleVersionList = []

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
        stage('CICD-Build') {
            agent {
                node {
                    label "zmf-ansible-configuration-agent"
                    customWorkspace "workspace/${env.BRANCH_NAME}"
                }
            }
            
            steps {
                echo "****************************************************************************\n****************************************************************************"
                echo "Check local env:"

                script {
                    sh(script: """#!/bin/bash
                        echo '==> pwd'
                        pwd
                        
                        echo '==> python --version'
                        python --version
                        
                        echo '==> which python'
                        which python
                        
                        echo '==> ansible --version'
                        ansible --version
                        
                        echo '==> which ansible'
                        which ansible
                    """)
                    
                    echo "Check installed python:"
                    sh(script: """#!/bin/bash
                        for pythonVersion in ${pythonVersionList}
                        do 
                            echo '==> ${pythonVersion} --version'
                            ${pythonVersion} --version
                            
                            echo '==> which ${pythonVersion}'
                            which ${pythonVersion}
                        done
                    """)
                    
                    echo "Cleanup venv dir:"
                    venvDir = "/home/test/venv"
                    dir("${venvDir}") {
                        sh "pwd"
                        sh "rm -rf *"
                    }
                }
                
                echo "****************************************************************************\n****************************************************************************"
                echo "Build and install ansible collection:"
                checkout scm
                
                script {
                    ansibleCollection = "/home/test/.ansible"
                    echo "Ansible collection is: ${ansibleCollection}"
                    dir("${ansibleCollection}") {
                        sh "pwd"
                        sh "rm -rf *"
                    }
                    
                    remoteWorkspace = env.WORKSPACE
                    echo "Remote workspace is: ${remoteWorkspace}"
                    dir("${remoteWorkspace}") {
                        sh "pwd"
                        sh '/bin/bash -c -l "ansible-galaxy collection build --force"'
                        sh '/bin/bash -c -l "ansible-galaxy collection install ibm-ibm_zosmf-*.tar.gz --force"'
                    }
                }
            }
        }
        
        stage('CICD-Test') {
            agent {
                node {
                    label "zmf-ansible-configuration-agent"
                    customWorkspace "workspace/${env.BRANCH_NAME}"
                }
            }
            
            steps {
                script {
                    for(int i=0; i<pythonVersionList.size(); i++) {
                        stage('Test-' + pythonVersionList[i]) {
                            steps {
                                echo "****************************************************************************\n****************************************************************************"
                                echo "Test on venv ${pythonVersionList[i]}:"
                                
                                script {
                                    pythonVersion = pythonVersionList[i]
                                    venvPath = "${venvDir}/${pythonVersion}"
                                    sh(script: """#!/bin/bash
                                        echo "****************************************************************************"
                                        echo "Setup venv: ${venvPath}"
                                        
                                        echo '==> create'
                                        ${pythonVersion} -m venv ${venvPath}
                                        
                                        echo '==> activate'
                                        source ${venvPath}/bin/activate
                                        
                                        echo '==> install'
                                        pip install --upgrade pip
                                        pip install ansible
                                        pip install ansible-lint
                                        pip install flake8
                                        pip install pylint
                                        pip install voluptuous
                                        pip install yamllint
                                        pip install rstcheck
                                        pip install bandit
                                        
                                        echo '==> check'
                                        python --version
                                        which python
                                        ansible --version
                                        which ansible
                                        cd ${ansibleCollection}/collections/ansible_collections/ibm/ibm_zosmf
                                        pwd
                                        
                                        echo "****************************************************************************"
                                        echo "Run sanity test:"
                                        
                                        ${venvPath}/bin/ansible-test --version
                                        ${venvPath}/bin/ansible-test sanity
                                        
                                        echo "****************************************************************************"
                                        echo "Run ansible-lint:"
                                        
                                        ${venvPath}/bin/ansible-lint --version
                                        ${venvPath}/bin/ansible-lint plugins
                                        ${venvPath}/bin/ansible-lint roles
                                        ${venvPath}/bin/ansible-lint --profile production
                                        
                                        echo "****************************************************************************"
                                        echo "Run bandit scan:"
                                        
                                        ${venvPath}/bin/bandit --version
                                        ${venvPath}/bin/bandit -r plugins
                                        
                                        echo "****************************************************************************"
                                        echo "Run BVT:"
                                    """)
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}