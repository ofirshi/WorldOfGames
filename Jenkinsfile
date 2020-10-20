pipeline {
    environment {
        url_ip = "127.0.0.1"
        port_id = "8777"
    }
      options {
    buildDiscarder(logRotator(numToKeepStr: '2'))
  }
  agent {
        node {
            label 'windows'
        }
    }
   stages {
        stage('Checkout') {
            steps {
            deleteDir()
            checkout scm
            bat 'docker system prune -af'
            }
        }
        stage('Build') {
            steps {
                bat 'docker build . -f Dockerfile --no-cache --pull --force-rm -t ofirsh11/worldoffames '
            }
        }
        stage('Run') {
            steps {
                bat 'echo 8 > tests/Scores.txt'
                bat 'icacls * /reset /t /c /q '
                bat 'docker run --name flask_server -d -it -p 8777:8777 --mount type=bind,source=%WORKSPACE%/Scores.txt,target=/app/Scores.txt  ofirsh11/worldoffames'
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
            withCredentials([usernamePassword(credentialsId: 'docker-hub', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
               bat 'docker stop flask_server'
               bat 'docker login -u %USER% -p %PASS%'
               bat 'docker tag ofirsh11/worldoffames ofirsh11/worldoffames:latest'
               bat 'docker push ofirsh11/worldoffames'
               bat 'docker-clear.bat'
        }
        }
	}
   }
}