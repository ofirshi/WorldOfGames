node{
        stage('clone') {
            steps {
                  checkout scm
                  sh 'python3 -m pip install --upgrade pip --force --user --no-warn-script-location --no-cache-dir'
                  sh 'pip install --no-cache-dir -r ./requirements.txt --user --no-warn-script-location --use-feature=2020-resolver'
                  sh 'python3 ./tests/e2e.py '
            }
        }
	
	}