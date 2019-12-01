#!/bin/bash

sed -i 's/all_trials/jenkinsIntegration/g' plotbot/config.yml

sudo apt update
sudo apt install -y python3
sudo apt install -y python3-pip
sudo apt install -y ansible
pip3 install ansible
cd AnsibleScripts/
sudo ansible-playbook -i inventory provision.yaml --vault-password-file ~/keys/vaultPass
cd ../

source ~/keys/exportKeys.sh
cd plotbot/puppeteer
sudo npm install
sudo apt install -y chromium-browser
npm test
