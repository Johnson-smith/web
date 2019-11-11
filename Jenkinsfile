pipeline {
  agent {
    node {
      label 'master'
    }

  }
  stages {
    stage('Source') {
      steps {
        git(url: 'git@github.com:Johnson-smith/web.git', branch: 'master')
      }
    }

  }
  environment {
    COMPLETED_MSG = 'Build done !'
  }
}