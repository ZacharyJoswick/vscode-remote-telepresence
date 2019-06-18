# Simple vscode devcontainer example for using telepresence
FROM ubuntu:16.04

# Configure apt
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils 2>&1

# Install git, process tools, lsb-release (common in install instructions for CLIs)
# Also dependencies for telepresence
RUN apt-get -y install git procps lsb-release sudo iptables

# Install kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/bin/kubectl

# Copy in kubectl config file and set environment variables
COPY config /kube/config
ENV KUBECONFIG=/kube/config

# Install Telepresence
RUN curl -s https://packagecloud.io/install/repositories/datawireio/telepresence/script.deb.sh | bash
RUN apt install -y --no-install-recommends telepresence 

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

# Set the default shell to bash instead of sh
ENV SHELL /bin/bash

# Create a worksapce folder
RUN mkdir /workspace
WORKDIR /workspace