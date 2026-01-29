
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_swupdate_retrieve

.. _zmf_swupdate_retrieve_module:


zmf_swupdate_retrieve -- Retrieve the Status of a Software Update Process
=========================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The **IBM z/OSMF collection** provides an Ansible role, referred to as **zmf_swupdate_retrieve**, retrieves the most recent software update process on a software instance.







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
  Name of the software instance for which the status of the most recent software update process is retrieved.


  A software instance name must be specified when a software instance UUID or a software update process ID are not specified. If a software update process ID is specified in addition to a software instance name and system nickname, then the software update process ID is used by default.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: False
  | **type**: str


 

system_nickname
  Nickname of the z/OSMF host system that has access to the volumes and data sets where the software instance resides.


  A system nickname must be specified when a software instance UUID or a software update process ID are not specified. If a software update process ID is specified in addition to a software instance name and system nickname, then the software update process ID is used by default.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: False
  | **type**: str


 

software_instance_uuid
  A UUID of a software instance for which the status of the most recent software update process is retrieved. A UUID is assigned to every software instance and can be obtained using the "List the software instances defined to z/OSMF" REST API.


  A UUID can also be obtained using the zmf_swmgmt_zos_system_uuid Ansible role which retrieves the UUID for the software instance that represents the installed software for the specified z/OSMF host system.


  A software instance UUID must be specified when a software instance name or a software update process ID are not specified. If a software update process ID is specified in addition to a software instance UUID, then the software update process ID is used by default.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: False
  | **type**: str


 

swupdate_process_id
  A software update process ID indicating the software update process to be retrieved.


  The process ID value is set as a variable in both the **zmf_swupdate_start** and **zmf_swupdate_resume** roles to identify the started or resumed software update process.


  A software update process ID must be specified when a software instance name or a software instance UUID are not specified. If a process ID is specified in addition to a software instance name or UUID, then the process ID is used by default.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: False
  | **type**: str


 

swupdate_retrieve_response_file
  The path to the file that will contain the results from the retrieve software update operation. The results will be in JSON format and will contain status information about the sofware update process.


  The directory must already exist otherwise there will be an error writing the results to the file. If the file exists in the directory already, it will be overwritten by the new response when the playbook is executed. If the file doesn't exist in the directory, it will be created.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: True
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: sample of retrieving the status of a software update
     hosts: sampleHost
     gather_facts: no
     collections:
       - ibm.ibm_zosmf

     tasks:
       - include_role :
           name: zmf_swupdate_retrieve
       - set_fact :
           zmf_user: 'ibmuser'
           zmf_password: 'ibmuser'
           software_instance_name: 'YourSwiName'
           system_nickname: 'YourSystemName'
           swupdate_retrieve_response_file: '/Users/yourUser/YourSwiNameRetrieve.json'




Notes
-----

.. note::
   - The given example assumes you have an inventory file *inventory.yml* that contains the values for the variables described above, such as z/OSMF host server, userid, password, software instance name and system, and software update process ID.


   - Command syntax to call a playbook using an inventory file: ``ansible-playbook -i inventory software_management_swu_start_CICDtest1.yml``


   - Command syntax to call a playbook using command arguments: ``ansible-playbook software_management_swu_start_CICDtest1.yml -e zmf_user=ibmuser -e zmf_password=ibmuser -e software_instance_name=YourSwiName -e system_nickname=YourSystemName -e swupdate_retrieve_response_file=/Users/yourUser/YourSwiNameRetrieve.json``








