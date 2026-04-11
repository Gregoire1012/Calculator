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


    
    stages {

        stage('Installation des dépendances') {
            steps {
                echo "Création de l'environnement Python et installation..."

                sh '''
                    # Créer environnement virtuel
                    ${PYTHON} -m venv ${VENV}

                    # Activer environnement
                    . ${VENV}/bin/activate

                    # Mettre à jour pip
                    pip install --upgrade pip

                    # Installer dépendances si fichier existe
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
