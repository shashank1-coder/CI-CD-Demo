pipeline {
    agent none
    stages {
        stage('Test Matrix') {
            matrix {
                axes {
                    axis {
                        name 'PYTHON_VERSION'
                        values '3.8', '3.9', '3.10'
                    }
                }
                agent {
                    docker {
                        image "python:${PYTHON_VERSION}"
                        args '-v $PWD:/app -w /app'
                    }
                }
                stages {
                    stage('Install Dependencies') {
                        steps {
                            sh 'pip install -r requirements.txt'
                            sh 'pip install pytest-rerunfailures'
                        }
                    }
                    stage('Run Tests') {
                        steps {
                            sh 'pytest tests/ --reruns 1 --junitxml=report.xml'
                        }
                        post {
                            always {
                                junit 'report.xml'
                                archiveArtifacts artifacts: 'report.xml', allowEmptyArchive: true
                            }
                        }
                    }
                }
            }
        }
        
    }
}
