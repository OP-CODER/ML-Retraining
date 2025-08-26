pipeline {
    agent any

    environment {
        PYTHON_ENV = "${WORKSPACE}/venv"
        DATA_PATH = "training_data.csv"  // dataset path relative to workspace
        MODEL_DIR = "${WORKSPACE}/models"
    }

    stages {
        stage('Checkout') {
            steps {
                // Get code from Git repo
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python -m venv venv
                source venv/Scripts/activate
                pip install --upgrade pip
                pip install pandas scikit-learn joblib
                '''
            }
        }

        stage('Run Retraining Pipeline') {
            steps {
                script {
                    // Run pipeline.py and capture output
                    def output = sh(returnStdout: true, script: '''
                        source venv/Scripts/activate
                        python pipeline.py
                    ''').trim()

                    // Parse accuracy from output line "Evaluation accuracy: X.Y"
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

        stage('Kubernetes Deployment') {
            steps {
                sh '''
                # Apply/update Kubernetes deployment (ensure kubectl and kubeconfig are configured)
                kubectl apply -f k8s-deployment.yaml

                # Restart deployment pods to reload new model files
                kubectl rollout restart deployment/ml-model-deployment
                '''
            }
        }

        stage('Archive Metrics') {
            steps {
                // Save accuracy metric for Jenkins UI
                echo "Model accuracy: ${env.MODEL_ACCURACY}" > accuracy.txt
                archiveArtifacts artifacts: 'accuracy.txt'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
