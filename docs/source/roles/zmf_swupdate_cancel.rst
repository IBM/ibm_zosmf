
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_swupdate_cancel

.. _zmf_swupdate_cancel_module:


zmf_swupdate_cancel -- Cancel a Software Update Process
=======================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The \ :strong:`IBM z/OSMF collection`\  provides an Ansible role, referred to as \ :strong:`zmf\_swupdate\_cancel`\ , cancels a software update process that is in progress on a software instance.







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
  Name of the software instance for which the currently in progress software update process is cancelled.


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
  A UUID of a software instance for which the currently in progress software update process is cancelled. A UUID is assigned to every software instance and can be obtained using the "List the software instances defined to z/OSMF" REST API.


  A UUID can also be obtained using the zmf\_swmgmt\_zos\_system\_uuid Ansible role which retrieves the UUID for the software instance that represents the installed software for the specified z/OSMF host system.


  A software instance UUID must be specified when a software instance name or a software update process ID are not specified. If a software update process ID is specified in addition to a software instance UUID, then the software update process ID is used by default.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: False
  | **type**: str


 

swupdate_process_id
  A software update process ID indicating the software update process to be canceled.


  A software update process ID must be specified when a software instance name or a software instance UUID are not specified. If a process ID is specified in addition to a software instance name or UUID, then the process ID is used by default.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: sample of canceling a software update
     hosts: sampleHost
     gather_facts: no
     collections:
       - ibm.ibm_zosmf

     tasks:
       - include_role :
           name: zmf_swupdate_cancel
       - set_fact :
           zmf_user: 'ibmuser'
           zmf_password: 'ibmuser'
           software_instance_name: 'YourSwiName'
           system_nickname: 'YourSystemName'




Notes
-----

.. note::
   - The given example assumes you have an inventory file \ :emphasis:`inventory.yml`\  that contains the values for the variables described above, such as z/OSMF host server, userid, password, software instance name and system, and software update process ID.


   - Command syntax to call a playbook using an inventory file: \ :literal:`ansible-playbook -i inventory software\_management\_swu\_cancel\_CICDtest1.yml`\ 


   - Command syntax to call a playbook using command arguments: \ :literal:`ansible-playbook software\_management\_swu\_cancel\_CICDtest1.yml -e zmf\_user=ibmuser -e zmf\_password=ibmuser -e software\_instance\_name=YourSwiName -e system\_nickname=YourSystemName`\ 








