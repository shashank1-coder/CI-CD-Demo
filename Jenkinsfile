pipeline {
    agent any
    stages {
        stage('Setup and Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pip install pytest pytest-rerunfailures
                    pytest tests/ --reruns 1 --junitxml=report.xml
                '''
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
