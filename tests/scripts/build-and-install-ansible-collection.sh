#!/bin/bash -eu

echo "Building the Ansible Collection"
ansible-galaxy collection build --force

echo "Installing the Ansible Collection"
ansible-galaxy collection install ibm-ibm_zosmf-*.tar.gz --force

