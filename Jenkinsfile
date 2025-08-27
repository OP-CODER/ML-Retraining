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
                    def matcher = output =~ /Evaluation accuracy: ([0-9]*\\.?[0-9]+)/
                    if (matcher) {
                        env.MODEL_ACCURACY = matcher[0][1]
                        echo "Model Accuracy: ${env.MODEL_ACCURACY}"
                    } else {
                        error("Could not parse model accuracy from pipeline output.")
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                bat '''
                kubectl apply -f k8s-deployment.yaml
                kubectl rollout restart deployment/ml-model-deployment
                '''
            }
        }
        stage('Archive Metrics') {
            steps {
                script {
                    def metricsPath = "/shared-volume/accuracy.txt"
                    writeFile file: metricsPath, text: "Model accuracy: ${env.MODEL_ACCURACY}"
                    archiveArtifacts artifacts: metricsPath
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
