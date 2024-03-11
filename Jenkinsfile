pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building ..."
                sh '''
                sudo apt update
                sudo apt install python3
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