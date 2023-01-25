
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_swmgmt_identify_missing_fixcat_updates

.. _zmf_swmgmt_identify_missing_fixcat_updates_module:


zmf_swmgmt_identify_missing_fixcat_updates -- Identify Missing Fixcat Software Updates for a Software Instance
==============================================================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The **IBM z/OSMF collection** provides an Ansible role, referred to as **zmf_swmgmt_identify_missing_fixcat_updates**, to determine if a software instance is missing updates for fix categories that might be applicable to the software instance.  It also helps you identify the SYSMODs that resolve the missing updates.







Variables
---------


 

zmf_host
  Hostname of the z/OSMF server, specified in the inventory file or as an argument on the playbook command.


  | **required**: True
  | **type**: str


 

zmf_port
  Port number of the z/OSMF server. If z/OSMF is not using the default port, you need to specify value for this parameter in the inventory file or as an argument on the playbook command.


  | **required**: False
  | **type**: str
  | **default**: 443


 

zmf_user
  User name to be used for authenticating with the z/OSMF server.

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

  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: True
  | **type**: str


 

system_nickname
  Nickname of the z/OSMF host system that has access to the volumes and data sets where the software instance resides.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: True
  | **type**: str


 

missing_fixcat_updates_response_file
  The path to the file that will contain the results from the missing fixcat updates operation.

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

   
   - name: sample of identifying missing fixcat software updates for a software instance
     hosts: sampleHost
     gather_facts: no
     collections:
       - ibm.ibm_zosmf

     tasks:
       - include_role :
           name: zmf_swmgmt_identify_missing_fixcat_updates




Notes
-----

.. note::
   - The given example assumes you have an inventory file *inventory.yml* that contains the values for the variables described above, such as z/OSMF host server, userid, password, software instance name and system, and response file name.


   - When the role is executed, a message shown in following example is displayed, ``"msg": "Output filename= /tmp/xxx/missing_fixcat_updates_response.json"``. This message includes a file path and file name where the missing fixcat updates report for the requested software instance is returned.








