pipeline {
    agent any
    environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub-token')
  }
    stages {
        stage('Git clone') {
            steps {
                sh 'rm -rf test-Docker_hub'
                sh 'git clone https://github.com/Palachev/test-Docker_hub.git'
                echo 'Git Clone Completed'
            }
        }
        stage('Build Docker Images') {
            steps {
                sh 'ls'
                sh 'docker build -t pl43ch/my-app . '
                echo 'Build Dockerfile Completed'
            }
        }
        stage('Login to Docker.hub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                echo 'Login Completed'
            }
        }
        stage('Push Image to Docker Hub') {
            steps {
                sh 'docker push pl43ch/my-app'
            }
        }
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}
