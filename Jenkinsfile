#!/usr/bin/env groovy

node('robxtask-jenkins-slave') {

    // -----------------------------------------------
    // --------------- Staging Branch ----------------
    // -----------------------------------------------
    if (env.BRANCH_NAME == 'staging') {

        stage('Clone and Update') {
            git(url: 'https://github.com/ROBxTASK/simple-registration-service.git', branch: env.BRANCH_NAME)
        }

        stage('Build Docker') {
            sh 'docker build . -t robxtask/simple-registration-service:staging'
        }

        stage('Push Docker - staging') {
            withCredentials([usernamePassword(credentialsId: 'docker-login-credentials', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                sh 'docker login --username $USER --password $PASS'
                sh 'docker push robxtask/simple-registration-service:staging'
            }
        }

        stage('Deploy') {
            sh 'ssh staging "cd /srv/docker-setup/staging/ && ./run-staging.sh restart-single simple-registration-service"'
        }
    }
}