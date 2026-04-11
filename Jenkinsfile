pipeline {
    agent any

    environment {
        PYTHON = 'python3'
        VENV = 'venv'
    }

    stages {

        stage('Clone GitHub') {
            steps {
                echo 'Téléchargement du projet...'

                git branch: 'main',
                url: 'https://github.com/Gregoire1012/Calculator.git'

                sh 'ls -l'
            }
        }

        stage('Installation des dépendances') {
            steps {
                echo "Installation Python..."

                sh '''
                    ${PYTHON} -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip

                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        echo "Pas de requirements.txt"
                    fi
                '''
            }
        }

    }
}
