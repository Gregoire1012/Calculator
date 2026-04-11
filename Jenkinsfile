pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo "Code déjà cloné par Jenkins"
            }
        }

        stage('Build') {
            steps {
                sh 'echo "building the app"'
            }
        }

        stage('Test') {
            steps {
                sh 'echo "Running tests"'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "deploying"'
            }
        }
    }

    post {
        success {
            sh 'echo "build successful"'
        }
        failure {
            sh 'echo "build failed"'
        }
    }
}
