# echo "*** Test in the venv for ${pythonVersionList[i]}:"
pythonVersion = $1
venvDir = $2
remoteWorkspace = $3
echo "Test Collection with ${pythonVersion}:"

venvPath = "${venvDir}/${pythonVersion}"

echo "Setup venv: ${venvPath}"

echo 'Creating Virtual Environment:'
echo '==> ${pythonVersion} -m venv ${venvPath}'
${pythonVersion} -m venv ${venvPath}

echo '*** activate:'
echo '==> source ${venvPath}/bin/activate'
source ${venvPath}/bin/activate

pip install -r requirements.txt

echo 'Checking for Proper Python Version and Location'
python --version
which python

echo 'Checking for Proper Ansible Version and Location'
ansible --version
which ansible

echo 'Confirming Ansible Collection was Installed Correctly'
cd ${ansibleCollection}/collections/ansible_collections/ibm/ibm_zosmf
echo '==> pwd'
pwd


echo "Running Ansible Sanity Test:"
${venvPath}/bin/ansible-test --version
${venvPath}/bin/ansible-test sanity

echo "Running Ansible Lint:"
# echo '==> ${venvPath}/bin/ansible-lint --version'
${venvPath}/bin/ansible-lint --version
# echo '==> ${venvPath}/bin/ansible-lint plugins'
${venvPath}/bin/ansible-lint plugins
# echo '==> ${venvPath}/bin/ansible-lint roles'
${venvPath}/bin/ansible-lint roles
# echo '==> ${venvPath}/bin/ansible-lint --profile production'
${venvPath}/bin/ansible-lint --profile production

echo "Running Bandit Scan:"

# echo '==> ${venvPath}/bin/bandit --version'
${venvPath}/bin/bandit --version
# echo '==> ${venvPath}/bin/bandit -r plugins'
${venvPath}/bin/bandit -r plugins

echo "*** Run BVT:"
echo '==> mkdir'
mkdir tests/CICD
mkdir tests/CICD/playbooks
mkdir tests/CICD/playbooks/group_vars
mkdir tests/CICD/playbooks/host_vars
echo '==> cp'
cp ${remoteWorkspace}/tests/CICD/playbooks/*.yml tests/CICD/playbooks/
cp ${remoteWorkspace}/tests/CICD/playbooks/*.json tests/CICD/playbooks/
cp ${remoteWorkspace}/tests/CICD/playbooks/hosts tests/CICD/playbooks/
cp ${remoteWorkspace}/tests/CICD/playbooks/ansible.cfg tests/CICD/playbooks/
cp ${remoteWorkspace}/tests/CICD/playbooks/group_vars/*.yml tests/CICD/playbooks/group_vars/
// cp -p /home/connect-ansible-build-server/ansible-tmp/P00.yml tests/CICD/playbooks/host_vars/P00.yml
// cp -p /home/connect-ansible-build-server/ansible-tmp/P01.yml tests/CICD/playbooks/host_vars/P01.yml
cd tests/CICD/playbooks
echo '==> pwd'
pwd

// echo '*** Workflow BVT:'
// ${venvPath}/bin/ansible-playbook workflow_complete_CICDtest1.yml
// echo '*** CPM BVT:'
// ${venvPath}/bin/ansible-playbook cpm_complete_CICDtest1.yml
// echo '*** SCA BVT:'
// ${venvPath}/bin/ansible-playbook sca_CICDtest1.yml
// echo '*** ZMSC BVT:'
// ${venvPath}/bin/ansible-playbook zmsc_run_mgmt_service_CICDTest1.yml
echo '*** SM BVT:'
${venvPath}/bin/ansible-playbook software_management_reports_CICDtest1.yml
${venvPath}/bin/ansible-playbook software_management_system_uuid_CICDtest1.yml
${venvPath}/bin/ansible-playbook software_management_csi_query_CICDtest1.yml
${venvPath}/bin/ansible-playbook software_management_swu_start_and_resolve_all_system_holds_CICDtest1.yml
${venvPath}/bin/ansible-playbook software_management_swu_start_CICDtest1.yml
${venvPath}/bin/ansible-playbook software_management_swu_resume_CICDtest1.yml
${venvPath}/bin/ansible-playbook software_management_swu_retrieve_all_CICDtest1.yml
${venvPath}/bin/ansible-playbook software_management_swu_cancel_CICDtest1.yml

echo 'Test Completed Deactivating and Cleaning up Virtual Environment:'
echo '==> deactivate'
deactivate
rm -rf ${venvPath}