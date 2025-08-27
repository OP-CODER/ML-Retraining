pipeline {
    agent any

    environment {
        VENV_PATH = "C:\\Jenkins\\venvs\\retraining_venv"
        PYTHON_EXE = "${VENV_PATH}\\Scripts\\python.exe"
        REQUIREMENTS = "C:/Users/mohda/Desktop/Retraining/data/requirements.txt"
        PIPELINE_SCRIPT = "C:/Users/mohda/Desktop/Retraining/pipeline.py"
    }

    stages {
        stage('Setup Virtual Environment') {
            steps {
                script {
                    // Check if venv exists; create if missing
                    if (!fileExists("${VENV_PATH}\\Scripts\\python.exe")) {
                        bat "python -m venv ${VENV_PATH}"
                        bat "${PYTHON_EXE} -m pip install --upgrade pip"
                        bat "${PYTHON_EXE} -m pip install -r ${REQUIREMENTS}"
                    } else {
                        echo "Virtual environment exists. Skipping installation."
                    }
                }
            }
        }

        stage('Run Retraining Pipeline') {
            steps {
                bat "${PYTHON_EXE} pipeline.py"
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
