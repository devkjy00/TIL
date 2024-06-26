[github](https://github.com/eclipse-che/che)
[[Minikube]]
[chectl](https://eclipse.dev/che/docs/stable/administration-guide/installing-the-chectl-management-tool/)
[kubectl](https://kubernetes.io/docs/tasks/tools/)

- TypeScript, JavaScript

### Window 설치
``` 
// chocolatey 설치
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

// minikube 설치
choco install minikube

// kubectl 설치
choco install kubernetes-cli
minikube kubectl -- get pods -A
minikube addons enable metrics-server

// chectl 설치
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://che-incubator.github.io/chectl/install.ps1'))

minikube start --addons=ingress,dashboard --vm=true --memory=10240 --cpus=4 --disk-size=50GB --kubernetes-version=v1.23.9
chectl server:deploy --platform minikube
chectl dashboard:open

```

### Mac 설치
```
brew install minikube kuberetes-cli
// che 설치
bash <(curl -sL  https://che-incubator.github.io/chectl/install.sh)
```
