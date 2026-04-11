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

                echo 'Contenu du projet :'
                sh 'ls -l'
            }
        }

        stage('Installation des dépendances') {
            steps {
                echo "Création de l'environnement Python et installation..."

                sh '''
                    ${PYTHON} -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip

                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        echo "Pas de requirements.txt trouvé"
                    fi
                '''
            }
        }

    }
}
