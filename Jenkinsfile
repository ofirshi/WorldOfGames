pipeline {
  environment {
  //https://medium.com/@gustavo.guss/jenkins-building-docker-image-and-sending-to-registry-64b84ea45ee9
    registry = "ofirsh11/worldoffames"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }

   agent any
   stages {
        stage('Checkout') {
            steps {
               git 'https://github.com/ofirshi/WorldOfGames'
               sh 'docker system prune -af'
            }
        }
        stage('Build') {
            steps {
                sh 'docker-compose pull'
                sh 'docker-compose build'
            }
        }
        stage('Run') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                script {
            try {
                sh "python3 tests/e2e.py"
            } catch (err) {
                            currentBuild.result='FAILURE'
                        }

            }
        }
	}
            stage('Test') {
            steps {
               sh 'docker tag ofirsh11/worldoffames ofirsh11/worldoffames:latest'
               sh 'docker push ofirsh11/worldoffames'
               sh 'docker stop $(docker ps -aq)'
               sh 'docker rm $(docker ps -aq)'
               sh 'docker rmi $(docker images -q)'
               sh 'docker system prune -af'
        }
	}
}