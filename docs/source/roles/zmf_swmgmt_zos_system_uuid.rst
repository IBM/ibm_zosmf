
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_swmgmt_zos_system_uuid

.. _zmf_swmgmt_zos_system_uuid_module:


zmf_swmgmt_zos_system_uuid -- Retrieve the z/OS system UUID
===========================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The \ :strong:`IBM z/OSMF collection`\  provides an Ansible role, referred to as \ :strong:`zmf\_swmgmt\_zos\_system\_uuid`\ , to retrieve the z/OS system UUID for the specified system nickname. The UUID identifies the software instance object that corresponds to the installed software for the specified z/OSMF host system.  The UUID can be used to uniquely identify a software instance object to be acted upon by other Ansible roles.







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


 

system_nickname
  Nickname of the z/OSMF host system.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: True
  | **type**: str


 

remote_zmf_user
  User ID for authenticating with a remote z/OSMF server.  Used only to retrieve the UUID of a remote z/OSMF server.


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

   
   - name: sample of retrieving the z/OS system UUID
     hosts: sampleHost
     gather_facts: no
     collections:
       - ibm.ibm_zosmf

     tasks:
       - include_role :
           name: zmf_swmgmt_zos_system_uuid




Notes
-----

.. note::
   - The given example assumes you have an inventory file \ :emphasis:`inventory.yml`\  that contains the values for the variables described above, such as z/OSMF host server, userid, password, system, and response file name.


   - Command syntax to call a playbook using an inventory file: \ :literal:`ansible-playbook -i inventory software\_management\_system\_uuid\_CICDtest1.yml`\ 


   - Command syntax to call a playbook using command arguments: \ :literal:`ansible-playbook software\_management\_system\_uuid\_CICDtest1.yml -e zmf\_user=zosmf\*\* -e zmf\_password=zosmf\*\*`\ 


   - When the role is executed, a message shown in following example is displayed, \ :literal:`"msg": "Output filename= /tmp/xxx/zos\_system\_uuid\_response.json"`\ . This message includes a file path and file name where the z/OS system UUID is saved.


   - Refer to https://www.ibm.com/docs/en/zos/3.1.0?topic=services-retrieve-zos-system-uuid for more information on the REST API's request and response JSON.








