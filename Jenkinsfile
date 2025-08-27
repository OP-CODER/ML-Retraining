pipeline {
    agent any
    environment {
        PYTHON_ENV = "${WORKSPACE}/venv"
        DATA_PATH = "training_data.csv"
        MODEL_DIR = "${WORKSPACE}/models"
        MODEL_ACCURACY = ''
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                bat '''
                python -m venv venv
                call venv/Scripts/activate
                venv\\Scripts\\python.exe -m pip install --upgrade pip
                venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }
        stage('Train Model') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                python training.py
                '''
            }
        }
        stage('Run Pipeline and Extract Metrics') {
            steps {
                script {
                    def output = bat(script: '''
                        call venv\\Scripts\\activate
                        python pipeline.py
                    ''', returnStdout: true).trim()
                    echo "Pipeline output:\\n${output}"

                    def accuracyLine = output.readLines().find { it.contains('Evaluation accuracy:') }
                    if (accuracyLine != null) {
                        def matcher = (accuracyLine =~ /Evaluation accuracy: ([0-9]+\.?[0-9]*)/)
                        if (matcher && matcher.size() > 0) {
                            env.MODEL_ACCURACY = matcher[0][1]
                            echo "Model Accuracy: ${env.MODEL_ACCURACY}"
                        } else {
                            error("Accuracy parsing failed in accuracyLine.")
                        }
                    } else {
                        error("No 'Evaluation accuracy' line found in output.")
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                bat '''
                kubectl apply -f k8s-deployment.yml
                kubectl rollout restart deployment/ml-model-deployment
                '''
            }
        }
        stage('Archive Metrics') {
            steps {
                script {
                    def metricsPath = "/shared-volume/accuracy.txt"
                    writeFile file: metricsPath, text: "Model accuracy: ${env.MODEL_ACCURACY}"
                    archiveArtifacts artifacts: 'accuracy.txt', fingerprint: true                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
