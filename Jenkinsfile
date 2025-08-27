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
                    // Create venv if it doesn't exist
                    if (!fileExists("${PYTHON_EXE}")) {
                        bat "python -m venv ${VENV_PATH}"
                        echo "Virtual environment created."
                    } else {
                        echo "Virtual environment exists."
                    }

                    // Upgrade pip
                    bat "${PYTHON_EXE} -m pip install --upgrade pip"

                    // Install only missing packages
                    bat """
                    for /f "delims=" %%i in ('type ${REQUIREMENTS}') do (
                        ${PYTHON_EXE} -m pip show %%i >nul 2>&1 || ${PYTHON_EXE} -m pip install %%i
                    )
                    """
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
