pipeline {
   agent any

   stages {
        stage('clone') {
            steps {
                sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                sh 'python get-pip.py'
                sh 'rm -rf get-pip.py'
                  sh 'python3 -m pip install --upgrade pip --force --user'
                  sh 'pip install --no-cache-dir -r ./requirements.txt --user'
                  sh 'python3 ./tests/e2e.py '
            }
        }
	
	}
}