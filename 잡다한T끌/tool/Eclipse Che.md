- TypeScript, JavaScript
- Eclipse Public License 2.0

[che repo](https://github.com/eclipse-che/che/blob/main/CONTRIBUTING.md#other-che-repositories)
- che, che-server, chectl, che-code, dashboard .....

[[Minikube]]
[kubectl](https://kubernetes.io/docs/tasks/tools/)
[chectl](https://eclipse.dev/che/docs/stable/administration-guide/installing-the-chectl-management-tool/)
### Window 설치
```  // chocolatey 설치
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

// minikube 설치
choco install minikube

// kubectl 설치
choco install kubernetes-cli

// chectl 설치
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://che-incubator.github.io/chectl/install.ps1'))

minikube start --addons=ingress,dashboard --vm=true --memory=10240 --cpus=4 --disk-size=50GB --kubernetes-version=v1.23.9
chectl server:deploy --platform minikube
chectl dashboard:open
```

- issue
```
X Exiting due to PR_HYPERV_MODULE_NOT_INSTALLED: Failed to start host: creating host: create: precreate: Hyper-V PowerShell Module is not available

* 권장: Run: 'Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Tools-All -All'
* 문서: https://www.altaro.com/hyper-v/install-hyper-v-powershell-module/
* 관련 이슈: https://github.com/kubernetes/minikube/issues/9040
```

### Mac 설치
```
brew install minikube kuberetes-cli
// che 설치
bash <(curl -sL  https://che-incubator.github.io/chectl/install.sh)
```
