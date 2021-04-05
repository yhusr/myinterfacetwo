pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'python run.py'
      }
    }
    stage('生成测试报告'){
        steps{
        allure commandline: 'allure', includeProperties: false, jdk: '', results: [[path: 'reports']]
        }
    }


  }
}
