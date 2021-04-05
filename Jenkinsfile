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
        [allure ./reports/* config=/data/allure-2.13.9/config]
      }
    }
  }
  environment {
    allure = '/data/allure-2.13.9/bin'
  }
}
