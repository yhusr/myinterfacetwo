pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'python run.py'
      }
    }

    stage('Results') {
      steps{
        [allure reports/allure.xml]
      }
    }
  }
  environment {
    allure = '/data/allure-2.13.9/bin'
  }
}
