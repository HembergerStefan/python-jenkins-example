pipeline {
    agent agent1_V1

    stages {
        stage('Build') {
            steps {
                echo "Building ..."
                sh '''
                pip3 install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing ..."
                sh '''
                python3 main.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo "Deliver ..."
            }
        }
    }
}