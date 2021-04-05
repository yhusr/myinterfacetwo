pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'python run.py'
      }
    }

    stage('生成测试报告') {
      steps {
        allure(commandline: 'allure', results: [[path: 'reports']])
      }
    }

  }
  environment {
    allure = '/data/allure-2.13.9/bin'
  }
}