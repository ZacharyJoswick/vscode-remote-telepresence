# Example of VsCode Remote Development with telepresence
This repository is an example of using the [visual studio code remote development tools](https://code.visualstudio.com/docs/remote/containers) with [telepresence](https://www.telepresence.io/)

Using this environment gives the developer an isolated and reproducible environment for rapid development of kubernetes services. This example can be modified and reused for virtually any development environment. 

## Setup
To use this environment you must have the following installed on your local machine
- [Docker](https://docs.docker.com/install/)
- [Visual studio code](https://code.visualstudio.com/)
- [Visual studio code remote development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

Additionally, you must replace the ```config``` file in the ```.devcontainer``` folder with a valid kubernetes configuration file. I have not tested alternative methods of authentication or with minikube clusters, but as long as the cluster is accessible from your local environment over the network, it should work in the container.

## Use
Once all prerequisites are satisfied you must checkout this repository and open the folder with vscode

```
git checkout https://github.com/ZacharyJoswick/vscode-remote-telepresence.git
code vscode-remote-telepresence
```

Once opened, a prompt should appear in the bottom right to open the folder in a remote container. If it does not you can trigger this manually by doing the following:

```
press: ctr+shift+p
type: Remote-Containers: open Folder in Container...
press: enter
```

The containerized environment should now start. This may take a few moments the first time depending on the speed of your machine.

Once the environment is started you should be able to perform all steps in the telepresence [Rapid development with Kubernetes](https://www.telepresence.io/tutorials/kubernetes-rapid) page
