### 1. Basit bir jenkins-script.sh dosyasını localde çalıştırma.

```
kubectl get pods
```

```
kubectl cp ./jenkins-script.sh <jenkins-pod-name>:/var/jenkins_home/
```

```
kubectl exec -it <jenkins-pod-name> -- /bin/bash
```

```
sh /var/jenkins_home/jenkins-script.sh
```
### 2. Basit bir script.sh dosyasını jenkins browserda çalıştırma.

- Jenkins pod'una giriş yap:

```
kubectl exec -it <jenkins-pod-name> -- /bin/bash
```
- Çalıştırma İzni Verme

```
chmod +x /var/jenkins_home/jenkins-script.sh
```

### 3. Jenkins Pipeline Script kısmına yazacağımız kod. Bu kodu "jenkinsfile" adında dosyada tutabiliriz.

```
pipeline {
    agent any

    triggers {
        githubPush()  // GitHub'dan gelen push'ları dinler
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/KuserOguzHan/githup_jenkins_1.git'
            }
        }

        stage('Build and Run') {
            steps {
                sh 'chmod +x jenkins-script.sh'
                sh './jenkins-script.sh'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

```
- jenkins-script.sh dosyası
```
sleep 5
echo "####################################"
sleep 5
echo "Jenkis bağlantsı başarlı !!!"
sleep 5
echo "####################################"
sleep 3
```
### 4.FastApi 1.Adım

```
uvicorn main:app --host 0.0.0.0 --port 8001
```
```
pipeline {
    agent any

    triggers {
        githubPush()  // GitHub'dan gelen push'ları dinler
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/KuserOguzHan/githup_jenkins_1.git'
            }
        }

        stage('Virtualenv and Requirements') {
            steps {
                script {
                    echo 'Setting up Python virtual environment and installing requirements...'
                    sh '''#!/bin/bash
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
                echo 'Python environment is set up and requirements are installed'
            }
        }

        stage('Run FastAPI Application') {
            steps {
                script {
                    echo 'Starting FastAPI application with Uvicorn...'
                    sh '''#!/bin/bash
                    source venv/bin/activate
                    uvicorn main:app --host 0.0.0.0 --port 8002
                    '''
                }
                echo 'Uvicorn is running'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
```

### 5. Eklendi