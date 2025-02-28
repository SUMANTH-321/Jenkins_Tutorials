pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
               git branch: 'main', url: 'https://github.com/SUMANTH-321/Jenkins_Tutorials.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Building the application..."'
            }
        }

        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploying the application..."'
            }
        }
    }
}
