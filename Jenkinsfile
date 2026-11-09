
pipeline {
    agent any

    environment {
        APP_DIR = '/opt/flask-app'
        VENV = '/opt/flask-app/venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/flask-backend.git'
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
                sh '''
                    venv/bin/pytest -v
                '''
            }
        }

        stage('Deploy Flask') {
            steps {
                sh '''
                    sudo /usr/local/bin/deploy-flask
                '''
            }
        }
    }

    post {
        success {
            echo 'Flask deployment successful!'
        }

        failure {
            echo 'Flask pipeline failed!'
        }
    }
}
