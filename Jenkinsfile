pipeline {
    agent any
    stages {
        stage("Stage 1") {
            steps {
                sh """
                    pwd
                    ls -l
                    touch test.py
                """
            }
        }
        stage("Stage 2") {
            steps {
                sh "ifconfig"
                sh "netstat -ln"
                sh "ps aux"
                build job: "freestyle1"
            }
        }
    }
}