pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'apt install python3 -y'
        bat 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        bat 'python3 tuv_rheinland_termin_buchen.py'
      }
    }
  }
}