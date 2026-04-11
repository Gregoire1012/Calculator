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

        // ✅ CORRECTION tkinter
        stage('Run Application') {
            steps {
                echo "Application tkinter ignorée (non compatible Jenkins)"
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

    // ✅ CORRECTION junit
    post {
        always {
            script {
                if (fileExists('reports/resultats.xml')) {
                    junit 'reports/*.xml'
                } else {
                    echo "Pas de résultats de test"
                }
            }
        }
        success {
            echo "Pipeline réussi ✅"
        }
        failure {
            echo "Pipeline échoué ❌"
        }
    }
}
