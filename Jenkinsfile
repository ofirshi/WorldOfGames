pipeline {
   agent any

   stages {
        stage('clone') {
            steps {
                sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
                sh 'python3 get-pip.py'
                sh 'rm -rf get-pip.py'
                sh 'python3 -m pip install --upgrade pip --force  --no-warn-script-location'
                sh '${JENKINS_HOME}/.local/bin/pip install --no-cache-dir -r ./requirements.txt --no-warn-script-location'
                sh 'python3 ./tests/e2e.py '
            }
        }
	
	}
}