
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_swupdate_retrieve_all

.. _zmf_swupdate_retrieve_all_module:


zmf_swupdate_retrieve_all -- Retrieve the Status of all Software Update Processes
=================================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The **IBM z/OSMF collection** provides an Ansible role, referred to as **zmf_swupdate_retrieve_all**, retrieves all software update processes on a software instance.







Variables
---------


 

zmf_host
  Hostname of the z/OSMF server, specified in the inventory file or as an argument on the playbook command.


  | **required**: True
  | **type**: str


 

zmf_port
  Port number of the z/OSMF server. If z/OSMF is not using the default port, you need to specify a value for this parameter in the inventory file or as an argument on the playbook command.


  | **required**: False
  | **type**: str
  | **default**: 443


 

zmf_user
  User ID for authenticating with the z/OSMF server.

  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: True
  | **type**: str


 

zmf_password
  Password to be used for authenticating with z/OSMF server.

  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: True
  | **type**: str


 

software_instance_name
  Name of the software instance for which the status of all software update processes are retrieved.


  A software instance name must be specified when a software instance UUID is not specified. If a software instance UUID is specified in addition to a software instance name and system nickname, then the software instance UUID is used by default.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: False
  | **type**: str


 

system_nickname
  Nickname of the z/OSMF host system that has access to the volumes and data sets where the software instance resides.


  A system nickname must be specified when a software instance UUID is not specified. If a software instance UUID is specified in addition to a software instance name and system nickname, then the software instance UUID is used by default.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: False
  | **type**: str


 

software_instance_uuid
  A UUID of a software instance for which the status of all software update processes are retrieved. A UUID is assigned to every software instance and can be obtained using the "List the software instances defined to z/OSMF" REST API.


  A UUID can also be obtained using the zmf_swmgmt_zos_system_uuid Ansible role which retrieves the UUID for the software instance that represents the installed software for the specified z/OSMF host system.


  A software instance UUID must be specified when a software instance name is not specified. If both a software instance UUID and name are specified, then the software instance UUID is used by default.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: False
  | **type**: str


 

swupdate_retrieve_all_response_file
  The path to the file that will contain the results from the retrieve all software updates operation. The results will be in JSON format and will contain information about each of the sofware update processes.


  The directory must already exist otherwise there will be an error writing the results to the file. If the file exists in the directory already, it will be overwritten by the new response when the playbook is executed. If the file doesn't exist in the directory, it will be created.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: True
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: sample of retrieving the status of all software updates
     hosts: sampleHost
     gather_facts: no
     collections:
       - ibm.ibm_zosmf

     tasks:
       - include_role :
           name: zmf_swupdate_retrieve_all
       - set_fact :
           zmf_user: 'ibmuser'
           zmf_password: 'ibmuser'
           software_instance_name: 'YourSwiName'
           system_nickname: 'YourSystemName'
           swupdate_retrieve_all_response_file: '/Users/yourUser/YourSwiNameRetrieveAll.json'




Notes
-----

.. note::
   - The given example assumes you have an inventory file *inventory.yml* that contains the values for the variables described above, such as z/OSMF host server, userid, password, software instance name, and system.


   - Command syntax to call a playbook using an inventory file: ``ansible-playbook -i inventory software_management_swu_retrieve_all_CICDtest1.yml``


   - Command syntax to call a playbook using command arguments: ``ansible-playbook software_management_swu_retrieve_all_CICDtest1.yml -e zmf_user=ibmuser -e zmf_password=ibmuser -e software_instance_name=YourSwiName -e system_nickname=YourSystemName -e swupdate_retrieve_all_response_file=/Users/yourUser/YourSwiNameRetrieveAll.json``








