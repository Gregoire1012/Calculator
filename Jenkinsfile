pipeline {
    agent any

    stages {

        stage('Clone GitHub') {
            steps {
                echo 'Téléchargement du projet...'

                git branch: 'main',
                url: 'https://github.com/Gregoire1012/Calculator.git'

                echo 'Contenu du projet :'
                sh 'ls -l'
            }
        }

    }
}
