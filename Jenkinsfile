pipeline {
   agent any

   stages {
        stage('clone') {
            steps {
                  sh 'python3 -m pip install --upgrade pip --force --user '
                  sh 'pip install --no-cache-dir -r ./requirements.txt --user'
                  sh 'python3 ./tests/e2e.py '
            }
        }
	
	}
}