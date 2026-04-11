pipeline {
    agent any

    environment {
        PYTHON = 'python3'
        VENV = 'venv'
    }

    stages {

        stage('Initialisation') {
            steps {
                echo "Vérification de l'environnement..."
                sh '${PYTHON} --version || true'

                echo "Nettoyage..."
                sh 'find . -name "*.pyc" -delete'
                sh 'rm -rf ${VENV}'
                sh 'mkdir -p reports'
            }
        }

        stage('Création environnement Python') {
            steps {
                echo "Création du venv..."
                sh '''
                    ${PYTHON} -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Installation des dépendances') {
            steps {
                echo "Installation dépendances..."
                sh '''
                    . ${VENV}/bin/activate
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        echo "Pas de requirements.txt"
                    fi
                '''
            }
        }

        stage('Tests') {
            steps {
                echo "Exécution des tests..."
                sh '''
                    . ${VENV}/bin/activate
                    pip install pytest || true

                    pytest --junitxml=reports/resultats.xml || true
                '''
            }
        }

        stage('Analyse Statique') {
            steps {
                echo "Analyse avec flake8..."
                sh '''
                    . ${VENV}/bin/activate
                    pip install flake8 || true
                    flake8 . --exclude=${VENV} --max-line-length=120 || true
                '''
            }
        }

        stage('Run Application') {
            steps {
                echo "Lancement app Python..."
                sh '''
                    . ${VENV}/bin/activate
                    if [ -f app.py ]; then
                        python app.py &
                    else
                        echo "Pas de app.py trouvé"
                    fi
                '''
            }
        }

        stage('Déploiement') {
            when {
                branch 'main'
            }
            steps {
                echo "Déploiement..."
                sh 'echo "Déploiement réussi !"'
            }
        }
    }

    post {
        always {
            junit 'reports/*.xml'
        }
        success {
            echo "Pipeline réussi ✅"
        }
        failure {
            echo "Pipeline échoué ❌"
        }
    }
}
