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
        always() {
          script {
            allure includeProperties: false, jdk: '', report: 'report', results: [[path: 'reports/*.xml']]
          }

        }

      }
    }

  }
  environment {
    allure = '/data/allure-2.13.9/bin'
  }
}