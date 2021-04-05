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
        allure commandline: 'allure2.29.0', includeProperties: false, jdk: '', results: [[path: 'reports']]
        }
    }


  }
}
