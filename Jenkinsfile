pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/TON_USERNAME/Calculator.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python3 -m venv $VENV'
                sh '. $VENV/bin/activate && pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '. $VENV/bin/activate && pip install flask'
            }
        }

        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
                sh 'python3 --version'
            }
        }

        stage('Run Application') {
            steps {
                sh '. $VENV/bin/activate && python3 app.py &'
            }
        }
    }

    post {
        success {
            echo '✅ Déploiement réussi !'
        }
        failure {
            echo '❌ Erreur dans le pipeline !'
        }
    }
}
