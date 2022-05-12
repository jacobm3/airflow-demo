#!/bin/bash

hostnamectl set-hostname airflow

export DEBIAN_FRONTEND=noninteractive

# add hashi stuff
curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add -
apt-add-repository "deb [arch=$(dpkg --print-architecture)] https://apt.releases.hashicorp.com $(lsb_release -cs) main"

apt-get update
apt-get upgrade -y
apt-get install -y nmap bzip2 netcat net-tools git htop sysstat iotop vim-nox docker-compose docker.io python3-pip terraform vault unzip

pip install -q boto3 hvac bpytop

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o /tmp/awscliv2.zip
cd /tmp && unzip awscliv2.zip && ./aws/install

curl https://goreleaserdev.blob.core.windows.net/goreleaser-test-container/releases/v1.5.0/cloud-cli_1.5.0_Linux_x86_64.tar.gz \
  -o astrocloudcli.tar.gz && tar xzf astrocloudcli.tar.gz && mv astrocloud /usr/local/bin
rm README.md astrocloudcli.tar.gz

# add ubuntu user to docker group
usermod -a -G docker ubuntu

HM=/home/ubuntu


# add environment
cd $HM
git clone https://github.com/jacobm3/gbin.git
chmod +x gbin/*

echo '. ~/gbin/jacobrc'  >> ${HM}/.bashrc

sudo chown -R $USER:$USER $HM

cd ${HM}/gbin && sudo cp pg ng /usr/local/bin

./vim.sh 

chown -R ubuntu $HM
