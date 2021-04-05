pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'python run.py'
      }
    }

    stage('report') {
      steps {
        sh 'allure generate -c reports/ -o reports/'
      }
    }

  }
  environment {
    allure = '/data/allure-2.13.9/bin'
  }
}
