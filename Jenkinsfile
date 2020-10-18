    environment {
            URL_ADDR = '127.0.0.1'
            PORT_NUMBER = '8777'
    }
node{
    stages {
        stage('clone') {
            steps {
                //git url: 'https://github.com/ofirshi/WorldOfGames.git'
                checkout scm
            }
        }
		 stage('build') {
            steps {
						 sh 'python3 -m pip install --upgrade pip --force --user --no-warn-script-location --no-cache-dir'
						 sh 'pip install --no-cache-dir -r ./requirements.txt --user --no-warn-script-location --use-feature=2020-resolver'
					} 
            }
		stage('test') {
            steps {

						sh 'python3 tests/e2e.py ${URL_ADDR} ${PORT_NUMBER}'
					}
						}
	}

    }
}