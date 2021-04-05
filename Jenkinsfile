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
        sh 'allure generate -c reports/ -o reports/html'
      }
    }
    stage('tomcat-report') {
      steps {
        sh 'cp -r reports/html/* /data/apache-tomcat-8.5.64/webapps/tomcat_allure/'
      }
    }
  }
  environment {
    allure = '/data/allure-2.13.9/bin'
  }
}
