def pythonVersionList = ["python3.11", "python3.12"]
def ansibleVersionList = ["11.3.0"] // (ansible-core) ["2.18.3"]

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
                    label "zmf-ansible-agent"
                    customWorkspace "workspace/${env.BRANCH_NAME}"
                }
            }
            
            steps {
                echo "****************************************************************************\n****************************************************************************"
                echo "*** Check local env:"
                
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
                    
                    echo "****************************************************************************"
                    echo "*** Check installed python:"
                    for(int i=0; i<pythonVersionList.size(); i++) {
                        pythonVersion = pythonVersionList[i]
                        sh(script: """#!/bin/bash
                            echo '==> ${pythonVersion} --version'
                            ${pythonVersion} --version
                            
                            echo '==> which ${pythonVersion}'
                            which ${pythonVersion}
                        """)
                    }
                    
                    echo "****************************************************************************"
                    echo "Cleanup venv dir:"
                    venvDir = "/home/test/venv"
                    dir("${venvDir}") {
                        sh "pwd"
                        sh "rm -rf *"
                    }
                }
                
                echo "****************************************************************************\n****************************************************************************"
                echo "*** Build and install ansible collection:"
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
                        sh(script: """
                            if [ -e "${remoteWorkspace}/ibm-ibm_zosmf-*.tar.gz" ]; then
                                rm ${remoteWorkspace}/ibm-ibm_zosmf-*.tar.gz
                            fi
                        """)
                        sh '/bin/bash -c -l "ansible-galaxy collection build --force"'
                        sh '/bin/bash -c -l "ansible-galaxy collection install ibm-ibm_zosmf-*.tar.gz --force"'
                    }
                }
            }
        }
        
        stage('CICD-Test') {
            agent {
                node {
                    label "zmf-ansible-agent"
                    customWorkspace "workspace/${env.BRANCH_NAME}"
                }
            }
            
            steps {
                script {
                    for(int i=0; i<pythonVersionList.size(); i++) {
                        stage('Test-' + pythonVersionList[i]) {
                            echo "****************************************************************************\n****************************************************************************"
                            echo "*** Test on venv ${pythonVersionList[i]}:"
                            
                            script {
                                pythonVersion = pythonVersionList[i]
                                ansibleVersion = ansibleVersionList[i]
                                venvPath = "${venvDir}/${pythonVersion}"
                                sh(script: """#!/bin/bash
                                    echo "****************************************************************************"
                                    echo "*** Setup venv: ${venvPath}"
                                    
                                    echo '*** create:'
                                    echo '==> ${pythonVersion} -m venv ${venvPath}'
                                    ${pythonVersion} -m venv ${venvPath}
                                    
                                    echo '*** activate:'
                                    echo '==> source ${venvPath}/bin/activate'
                                    source ${venvPath}/bin/activate
                                    
                                    echo '*** install:'
                                    echo '==> pip install --upgrade pip'
                                    pip install --upgrade pip
                                    echo '==> pip install ansible==${ansibleVersion}'
                                    pip install ansible==${ansibleVersion}
                                    echo '==> pip install ansible-lint'
                                    pip install ansible-lint
                                    echo '==> pip install flake8'
                                    pip install flake8
                                    echo '==> pip install pylint'
                                    pip install pylint
                                    echo '==> pip install voluptuous'
                                    pip install voluptuous
                                    echo '==> pip install yamllint'
                                    pip install yamllint
                                    echo '==> pip install rstcheck'
                                    pip install rstcheck
                                    echo '==> pip install bandit'
                                    pip install bandit
                                    
                                    echo '*** check:'
                                    echo '==> python --version'
                                    python --version
                                    echo '==> which python'
                                    which python
                                    echo '==> ansible --version'
                                    ansible --version
                                    echo '==> which ansible'
                                    which ansible
                                    cd ${ansibleCollection}/collections/ansible_collections/ibm/ibm_zosmf
                                    echo '==> pwd'
                                    pwd
                                    
                                    echo "****************************************************************************"
                                    echo "*** Run sanity test:"
                                    
                                    echo '==> ${venvPath}/bin/ansible-test --version'
                                    ${venvPath}/bin/ansible-test --version
                                    echo '==> ${venvPath}/bin/ansible-test sanity'
                                    ${venvPath}/bin/ansible-test sanity
                                    
                                    echo "****************************************************************************"
                                    echo "*** Run ansible-lint:"
                                    
                                    echo '==> ${venvPath}/bin/ansible-lint --version'
                                    ${venvPath}/bin/ansible-lint --version
                                    echo '==> ${venvPath}/bin/ansible-lint plugins'
                                    ${venvPath}/bin/ansible-lint plugins
                                    echo '==> ${venvPath}/bin/ansible-lint roles'
                                    ${venvPath}/bin/ansible-lint roles
                                    echo '==> ${venvPath}/bin/ansible-lint --profile production'
                                    ${venvPath}/bin/ansible-lint --profile production
                                    
                                    echo "****************************************************************************"
                                    echo "*** Run bandit scan:"
                                    
                                    echo '==> ${venvPath}/bin/bandit --version'
                                    ${venvPath}/bin/bandit --version
                                    echo '==> ${venvPath}/bin/bandit -r plugins'
                                    ${venvPath}/bin/bandit -r plugins
                                    
                                    echo "****************************************************************************"
                                    echo "*** Run BVT:"
                                    
                                    echo '==> mkdir'
                                    mkdir tests/CICD
                                    mkdir tests/CICD/playbooks
                                    mkdir tests/CICD/playbooks/group_vars
                                    mkdir tests/CICD/playbooks/host_vars
                                    echo '==> cp'
                                    cp ${remoteWorkspace}/tests/CICD/playbooks/*.yml tests/CICD/playbooks/
                                    cp ${remoteWorkspace}/tests/CICD/playbooks/*.json tests/CICD/playbooks/
                                    cp ${remoteWorkspace}/tests/CICD/playbooks/hosts tests/CICD/playbooks/
                                    cp ${remoteWorkspace}/tests/CICD/playbooks/ansible.cfg tests/CICD/playbooks/
                                    cp ${remoteWorkspace}/tests/CICD/playbooks/group_vars/*.yml tests/CICD/playbooks/group_vars/
                                    cp -p /home/test/ansible-tmp/P00.yml tests/CICD/playbooks/host_vars/P00.yml
                                    cp -p /home/test/ansible-tmp/P01.yml tests/CICD/playbooks/host_vars/P01.yml
                                    cd tests/CICD/playbooks
                                    echo '==> pwd'
                                    pwd
                                    
                                    echo '*** Workflow BVT:'
                                    ${venvPath}/bin/ansible-playbook workflow_complete_CICDtest1.yml
                                    echo '*** CPM BVT:'
                                    ${venvPath}/bin/ansible-playbook cpm_complete_CICDtest1.yml
                                    echo '*** SCA BVT:'
                                    ${venvPath}/bin/ansible-playbook sca_CICDtest1.yml
                                    echo '*** ZMSC BVT:'
                                    ${venvPath}/bin/ansible-playbook zmsc_run_mgmt_service_CICDTest1.yml
                                    echo '*** SM BVT:'
                                    ${venvPath}/bin/ansible-playbook software_management_reports_CICDtest1.yml
                                    ${venvPath}/bin/ansible-playbook software_management_system_uuid_CICDtest1.yml
                                    ${venvPath}/bin/ansible-playbook software_management_csi_query_CICDtest1.yml
                                    
                                    echo "****************************************************************************"
                                    echo '*** Test done:'
                                    echo '==> deactivate'
                                    deactivate
                                """) 
                            }
                        }
                    }
                }
            }
        }
    }
}