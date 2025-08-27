pipeline {
    agent any

    environment {
        VENV_PATH = "${WORKSPACE}\\venv"
        PYTHON_EXE = "${VENV_PATH}\\Scripts\\python.exe"
        REQUIREMENTS = "${WORKSPACE}\\data\\requirements.txt"
        PIPELINE_SCRIPT = "${WORKSPACE}\\pipeline.py"
    }

    stages {
        stage('Setup Virtual Environment') {
            steps {
                script {
                    if (!fileExists("${PYTHON_EXE}")) {
                        bat "python -m venv ${VENV_PATH}"
                        echo "Virtual environment created."
                    } else {
                        echo "Virtual environment exists."
                    }

                    bat "${PYTHON_EXE} -m pip install --upgrade pip"
                    bat "${PYTHON_EXE} -m pip install -r ${REQUIREMENTS} --upgrade --quiet"
                }
            }
        }

        stage('Run Retraining Pipeline') {
            steps {
                bat "${PYTHON_EXE} ${PIPELINE_SCRIPT}"
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
