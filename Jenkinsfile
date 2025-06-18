pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest pytest-rerunfailures'
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
