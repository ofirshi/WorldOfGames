pipeline {
    environment {
        url_ip = "127.0.0.1"
        port_id = "8777"
    }

  agent {
        node any
    }
   stages {
        stage('Checkout') {
            steps {
             git credentialsId: 'c8238df7-eca5-48ea-a075-eb5aa5ec78dc', url: 'https://github.com/ofirshi/WorldOfGames.git'
             //git 'https://github.com/ofirshi/WorldOfGames'
               bat 'docker system prune -af'
            }
        }
        stage('Build') {
            steps {
                bat 'docker-compose pull'
                bat 'docker-compose build'
                //waitUntilServicesReady
            }
        }
        stage('Run') {
            steps {
                bat 'docker-compose up -d'
                //waitUntilServicesReady
            }
        }
        stage('Test') {
            steps {
                script {
            try {
                bat "python tests\\e2e.py ${env.url_ip} ${env.port_id}"
            } catch (err) {
                            currentBuild.result='FAILURE'
                        }

            }
        }
        }
    stage('cleanup') {
            steps {
            withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'PASSWORD', usernameVariable: 'USERNAME')]) {
               bat 'docker login -u ${USERNAME} -p ${PASSWORD}'
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
   }
}