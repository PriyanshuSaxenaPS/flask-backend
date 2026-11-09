
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'venv/bin/pytest -v'
            }
        }

        stage('Deploy Flask') {
            steps {
                sh '''
                    sudo /usr/local/bin/deploy-flask "$WORKSPACE"
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    sleep 3
                    curl --fail http://127.0.0.1:5000/health
                '''
            }
        }
    }

    post {
        success {
            echo 'Flask CI/CD completed successfully!'
        }

        failure {
            echo 'Flask CI/CD failed!'
        }
    }
}
