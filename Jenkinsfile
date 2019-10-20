#!/usr/bin/env groovy

/**
 * <name>: Jenkinsfile
 *
 *    The Continuous Delivery pipeline Jenkinsfile.
 *
 */

/** Note-1: Pay attention to the following comment for OS Path Separators adjustments
 *      <check-path-separator>
 */

/** Note-2: Pay attention to the following comment for OS CLI Interpreter adjustments
 *      <check-cli-interpreter>
 */

pipeline {
    agent any
    
    options {
        buildDiscarder(logRotator(numToKeepStr:'15'))  // Keep latest 15 builds
    }

    environment {
        VIRTUAL_ENV = "${env.WORKSPACE}\\venv\\Scripts"  // Windows
        // VIRTUAL_ENV = "${env.WORKSPACE}/venv/bin"  // Linux
    }

    stages {
        /** stage ('Declarative: Checkout SCM') { return } */

        stage ('Bootstrap') {
            environment {
                /** Add and modify the following line if python / pip are not recognized by Jenkins */
                // PATH = "<path/to/python>:<path/to/pip>:${env.PATH}"  // Use ':' for Linux, ';' for Windows as PATH Separators
                PATH = "C:\\Users\\uid33194\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\;C:\\Users\\uid33194\\AppData\\Local\\Programs\\Python\\Python37-32\\;${env.PATH}"         
            }
            steps {
                echo "PATH=${env.PATH}"
                /** <check-cli-interpreter> */
                bat """
                    python --version
                    pip --version
                """
                bat """
                    pip install virtualenv
                """
                script {
                    dir ('venv') {
                        deleteDir()
                    }
                }
                /** <check-cli-interpreter> */
                bat """
                    virtualenv venv
                """
            }
        }

        stage ('Set-up') {
            environment {
                PATH = "${env.VIRTUAL_ENV};${env.PATH}" // Use ':' for Linux, ';' for Windows as PATH Separators
            }
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
            environment {
                PATH = "${env.VIRTUAL_ENV};${env.PATH}" // Use ':' for Linux, ';' for Windows as PATH Separators
            }
            /** <check-cli-interpreter> */
            steps {
                bat """
                    pylint project
                """
            }
        }
    }
}
