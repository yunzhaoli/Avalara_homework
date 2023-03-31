pipeline {
    agent any

    stages {
        stage('Clone repository') {
            when { branch 'main' }
            steps {
                git 'https://github.com/yunzhaoli/Avalara_homework.git'
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t yunzhaoli/homework-python .'
            }
        }

        stage('Run tests') {
            steps {
                sh 'docker run --rm --name test_container yunzhaoli/homework-python python -m unittest discover -v'
                script {
                    def exitCode = sh script: 'docker inspect --format=\'{{.State.ExitCode}}\' test_container', returnStatus: true
                    if (exitCode == 0) {
                        currentBuild.result = 'SUCCESS'
                    } else {
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }

        // TODO: Add the stage logic to push the Docker image to repository  
        stage('Push Docker image') {
            steps {
                sh 'echo "Pushed Docker image to repository"'
            }
        }
    }
}
