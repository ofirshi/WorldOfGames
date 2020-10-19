pipeline {
  agent any
   stages {
        stage('Checkout') {
            steps {
               git 'https://github.com/ofirshi/WorldOfGames'
               bat 'docker system prune -af'
            }
        }
        stage('Build') {
            steps {
                bat 'docker-compose pull'
                bat 'docker-compose build'
            }
        }
        stage('Run') {
            steps {
                bat 'docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                script {
            try {
                bat "python3 tests\e2e.py"
            } catch (err) {
                            currentBuild.result='FAILURE'
                        }

            }
        }
	}
            stage('Test') {
            steps {
               bat 'docker tag ofirsh11/worldoffames ofirsh11/worldoffames:latest'
               bat 'docker push ofirsh11/worldoffames'
               //sh 'docker stop $(docker ps -aq)'
               //bat 'FOR /f "tokens=*" %i IN ('docker ps -q') DO docker stop %i'
               //sh 'docker rm $(docker ps -aq)'
               //sh 'docker rmi $(docker images -q)'
               bat 'docker-clear.bat'
               bat 'docker system prune -af'
        }
	}
}