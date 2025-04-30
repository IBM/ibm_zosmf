def pythonVersionList = ["python3.11", "python3.12"]
def ansibleVersionList = ["11.3.0"] // (ansible-core) ["2.18.3"]
def venvDir = "/home/connect-ansible-build-server/venv"

pipeline {
	agent {
        label "zmf-ansible-agent"
    }
	options {
		// Skip checking out code from source control by default in the agent directive
		// skipDefaultCheckout()
		// Disallow concurrent executions of the Pipeline
		// disableConcurrentBuilds()
		// only keep 15 builds to prevent disk usage from growing out of control
		buildDiscarder(
			logRotator(
				daysToKeepStr: '180',
				numToKeepStr: '50',
			)
		)
	}
    
	stages {
        stage('Validating Tools are Installed') {
            steps {
                sh('./tests/scripts/check-environment.sh')   
            }
        }
        stage('Checking Python Levels') {
            steps {
                sh('./tests/scripts/check-python-levels.sh')
            }
        }
        stage('Cleaning Up Virtual Environment') {
            steps {
                sh('./tests/scripts/cleanup-virtual-environment.sh ${venvDir}')
            }
        }
        stage('Build and Install Ansible Collection') {
            steps {
                def remoteWorkspace = env.WORKSPACE
                sh('./tests/scripts/build-and-install-ansible-collection.sh ${remoteWorkspace}')
            }
        }
        
        stage('Test Valid Python Versions') {
            steps {
                parallel {
                    stage("Testing with Python 3.11") {
                        steps {
                            def pythonVersion = 'python3.11'
                            sh('./tests/scripts/python-version-test.sh ${pythonVersion} ${venvDir} ${remoteWorkspace}')
                        }
                    }
                    stage("Testing with Python 3.12") {
                        steps {
                            def pythonVersion = 'python3.12'
                            sh('./tests/scripts/python-version-test.sh ${pythonVersion} ${venvDir} ${remoteWorkspace}')
                        }
                    }
                }
            }
        }
    }
}