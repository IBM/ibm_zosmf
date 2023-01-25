
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_swmgmt_search_software_updates

.. _zmf_swmgmt_search_software_updates_module:


zmf_swmgmt_search_software_updates -- Search a Software Instance for Software Updates
=====================================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The **IBM z/OSMF collection** provides an Ansible role, referred to as **zmf_swmgmt_search_software_updates**, to search a software instance for one or more software updates to determine which updates are installed or updates that need to be installed.







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


 

search_software_updates_response_file
  The path to the file that will contain the results from the search software updates operation.

  The directory must already exist otherwise there will be an error writing the results to the file. If the file exists in the directory already, it will be overwritten by the new response when the playbook is executed. If the file doesn't exist in the directory, it will be created.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: True
  | **type**: str


 

updates
  The list of software update (SYSMOD) IDs to be searched in the subject software instance.


  | **required**: True
  | **type**: arr


 

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

   
   - name: sample of searching a software instance for software updates
     hosts: sampleHost
     gather_facts: no
     collections:
       - ibm.ibm_zosmf

     tasks:
       - include_role :
           name: zmf_swmgmt_search_software_updates




Notes
-----

.. note::
   - The given example assumes you have an inventory file *inventory.yml* that contains the values for the variables described above, such as z/OSMF host server, userid, password, software instance name and system, and response file name.


   - When the role is executed, a message shown in following example is displayed, ``"msg": "Output filename= /tmp/xxx/search_software_updates_response.json"``. This message includes a file path and file name where the search software updates report for the requested software instance is returned.








