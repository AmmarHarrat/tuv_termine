pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'apt install python3 -y'
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 tuv_rheinland_termin_buchen.py'
      }
    }
  }
}