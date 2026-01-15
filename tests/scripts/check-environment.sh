#!/bin/bash -eu
echo "Validating the tools in the local environment:"

echo 'Checking the working directory:'
pwd

echo 'Checking the Python version:'
python --version

echo 'Checking the Python location:'
which python

echo 'Checking the Ansible version:'
ansible --version

echo 'Checking the Ansible location:'
which ansible