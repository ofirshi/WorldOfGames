node{
    stages {
        stage('clone') {
            steps {
                 git credentialsId: 'c8238df7-eca5-48ea-a075-eb5aa5ec78dc', url: 'https://github.com/ofirshi/WorldOfGames.git'
                  sh 'python3 -m pip install --upgrade pip --force --user --no-warn-script-location --no-cache-dir'
                  sh 'pip install --no-cache-dir -r ./requirements.txt --user --no-warn-script-location --use-feature=2020-resolver'
                  sh 'python3 ./tests/e2e.py '
            }
        }
	
	}
}