#!/usr/bin/env groovy

/**
 * <name>: Jenkinsfile
 *
 *    The Continuous Delivery pipeline Jenkinsfile.
 *
 */

/** Note: Pay attention to the following comment for OS CLI Interpreter adjustments
 *      <check-cli-interpreter>
 */

pipeline {
    agent any
    
    options {
        buildDiscarder(logRotator(numToKeepStr:'15'))  // Keep latest 15 builds
    }

    environment {
        PATH = "${env.WORKSPACE}\\venv\\Scripts;${env.PATH}" // Use ':' for Linux, ';' for Windows as PATH Separators
    }

    stages {
        /** stage ('Declarative: Checkout SCM') { return } */

        stage ('Bootstrap') {
            steps {
                echo "PATH=${env.PATH}"
                script {
                    dir ('venv') {
                        deleteDir()
                    }
                }
                /** <check-cli-interpreter> */
                bat """
                    python --version
                    pip --version
                """
                bat """
                    pip install virtualenv
                """
                bat """
                    virtualenv venv
                """
            }
        }

        stage ('Set-up') {
            steps {
                bat """
                    pip install --upgrade pip
                    pip install -r requirements.txt -r dev-requirements.txt
                """
            }
        }

        stage ('Build') {
            steps {
                echo "This is a Python project. Skipping.."
            }
        }

        stage ('Static Code Analysis') {
            /** <check-cli-interpreter> */
            steps {
                bat """
                    pylint project
                """
            }
        }
    }
}
