#!/bin/zsh

echo "Build and install Ansible collection:"

ansibleCollection="/home/connect-ansible-build-server/.ansible"
echo "Ansible collection is: $ansibleCollection"

cd $ansibleCollection

pwd
rm -rf *

remoteWorkspace=$1
echo "Remote workspace is: ${remoteWorkspace}"

cd ${remoteWorkspace}

pwd

if [ -e "${remoteWorkspace}/ibm-ibm_zosmf-*.tar.gz" ]; then
    rm ${remoteWorkspace}/ibm-ibm_zosmf-*.tar.gz
fi

ansible-galaxy collection build --force
ansible-galaxy collection install ibm-ibm_zosmf-*.tar.gz --force

