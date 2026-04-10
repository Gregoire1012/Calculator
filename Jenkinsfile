pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Gregoire1012/Calculator.git'
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Installation des dépendances...'
                sh 'python3 --version'
                // Si requirements.txt existe :
                // sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run App / Test') {
            steps {
                echo 'Exécution du projet Python...'
                // Exemple :
                // sh 'python3 app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Déploiement (simple)...'
                // Exemple :
                // copier vers serveur ou lancer app
            }
        }
    }
}
