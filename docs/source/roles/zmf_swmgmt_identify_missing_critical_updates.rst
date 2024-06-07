
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_swmgmt_identify_missing_critical_updates

.. _zmf_swmgmt_identify_missing_critical_updates_module:


zmf_swmgmt_identify_missing_critical_updates -- Identify Missing Critical Software Updates for a Software Instance
==================================================================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The \ :strong:`IBM z/OSMF collection`\  provides an Ansible role, referred to as \ :strong:`zmf\_swmgmt\_identify\_missing\_critical\_updates`\ , to determine if a software instance is missing software updates to resolve PE PTFs, HIPER fixes, or other exception SYSMODs identified by ERROR HOLDDATA.  It also helps you identify the SYSMODs that resolve those exceptions.







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
  Name of the software instance.

  A software instance name must be specified when a software instance UUID is not specified. If both a software instance name and UUID are specified, then the software instance UUID is used by default.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: False
  | **type**: str


 

system_nickname
  Nickname of the z/OSMF host system that has access to the volumes and data sets where the software instance resides.


  A system nickname must be specified when a software instance UUID is not specified. If a software instance UUID is specified in  addition to a software instance and system nickname, then the software instance UUID is used by default.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: False
  | **type**: str


 

software_instance_uuid
  A UUID of a software instance. A UUID is assigned to every software instance and  can be obtained using the "List the software instances defined to z/OSMF" REST API.


  A UUID can also be obtained using the zmf\_swmgmt\_zos\_system\_uuid Ansible role which retrieves the UUID for the software instance that represents the installed software for the specified z/OSMF host system.


  A software instance UUID must be specified when a software instance name is not specified. If both a software instance UUID and name are specified, then the software instance UUID is used by default.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: False
  | **type**: str


 

missing_critical_updates_response_file
  The path to the file that will contain the results from the missing critical updates operation.

  The directory must already exist otherwise there will be an error writing the results to the file. If the file exists in the directory already, it will be overwritten by the new response when the playbook is executed. If the file doesn't exist in the directory, it will be created.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: True
  | **type**: str


 

remote_zmf_user
  User ID for authenticating with a remote z/OSMF server.  Used only if the software instance resides on a remote z/OSMF server.


  | **required**: False
  | **type**: str


 

remote_zmf_password
  Password for authenticating with a remote z/OSMF server.

  | **required**: False
  | **type**: str


 

proxy_zmf_user
  User ID for authenticating with an HTTP proxy server.

  | **required**: False
  | **type**: str


 

proxy_zmf_password
  Password for authenticating with an HTTP proxy server.

  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: sample of identifying missing critical software updates for a software instance
     hosts: sampleHost
     gather_facts: no
     collections:
       - ibm.ibm_zosmf

     tasks:
       - include_role :
           name: zmf_swmgmt_identify_missing_critical_updates




Notes
-----

.. note::
   - The given example assumes you have an inventory file \ :emphasis:`inventory.yml`\  that contains the values for the variables described above, such as z/OSMF host server, userid, password, software instance name and system, and response file name.


   - Command syntax to call a playbook using an inventory file: \ :literal:`ansible-playbook -i inventory software\_management\_reports\_CICDtest1.yml`\ 


   - Command syntax to call a playbook using command arguments: \ :literal:`ansible-playbook software\_management\_reports\_CICDtest1.yml -e zmf\_user=zosmf\*\* -e zmf\_password=zosmf\*\*`\ 


   - When the role is executed, a message shown in following example is displayed, \ :literal:`"msg": "Output filename= /tmp/xxx/missing\_critical\_updates\_response.json"`\ . This message includes a file path and file name where the missing critical updates report for the requested software instance is returned.


   - Refer to https://www.ibm.com/docs/en/zos/3.1.0?topic=services-missing-critical-updates for more information on the REST API's request and response JSON.








