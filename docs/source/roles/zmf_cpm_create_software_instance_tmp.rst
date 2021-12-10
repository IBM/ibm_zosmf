
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_cpm_create_software_instance

.. _zmf_cpm_create_software_instance_module:


zmf_cpm_create_software_instance -- Role creates a z/OS software instance
=========================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The **IBM z/OSMF collection** provides an Ansible role, referred to as **zmf_cpm_create_software_instance**, to directly create a software instance of z/OS Software such as IBM Customer Information Control System (CICS®), IBM Db2®, IBM Information Management System (IMS™), IBM MQ, and IBM WebSphere Application Server or any other z/OS software in **IBM Cloud Provisioning and Management (CP&M**) registry.







Variables
---------


 

zmf_host
  Hostname of the z/OSMF server, specified in the inventory file or vars file.


  | **required**: True
  | **type**: str


 

zmf_port
  Port number of the z/OSMF server. If z/OSMF is not using the default port, you need to specify value for this parameter in the inventory file or vars file.


  | **required**: False
  | **type**: str
  | **default**: 443


 

zmf_user
  User name to be used for authenticating with the z/OSMF server.

  This variable can be specified in the inventory file or vars file, or prompted when playbook is run.


  | **required**: True
  | **type**: str


 

zmf_password
  Password to be used for authenticating with z/OSMF server.

  This variable can be specified in the inventory file or vars file, or prompted when playbook is run.


  | **required**: True
  | **type**: str

systems_name
  The name of the system where the software is currently manullay provisioned

  | **required**: True
  | **type**: str

sysplex_name
  The name of the sysplex where the software is currently manullay provisioned


  | **required**: True
  | **type**: str

external_name
  The external name associated with the manually provisioned software instance


  | **required**: True
  | **type**: str

vendor_name
  The vendor who proivded the software


  | **required**: True
  | **type**: str

software_type
  The software type of the provisioned software 

  | **required**: True
  | **type**: str


product_version
  The software product version of the provisioned software 

  | **required**: True
  | **type**: str

instance_description
  Description for the software instance


  | **required**: True
  | **type**: str

instance_provider
  User who provided the software instance information


  | **required**: True
  | **type**: str

instance_owner
  Owner of the software instance. Software instance can be removed only by this user


  | **required**: True
  | **type**: str

instance_var_json_path
  Directory path for the JSON file that holds variables associated with software instance.
  Specify the file name that includes variables associated with softare instace e.g. /tmp/myVar.json.
  File contains json array of variables with name, value and visibility format where name identifies
  variable name, value identifies variable value and visibility identifies whether variable is "public"
  or "private". For example,
  ``[``
      ``{``
      `` "name": "VAR1",``
      `` "value": "VAR1_VALUE",``
      `` "visibility": "public" ``
      ``},``
      ``{``
      `` "name": "VAR2",``
      `` "value": "VAR2_VALUE",``
      `` "visibility": "public" ``
      ``},``
      ....
  ``]``


  | **required**: True
  | **type**: str

instance_record_dir
  Directory path that the provisioning role uses to capture various information (in JSON format) about the provisioned instance.
  On many system default value ``"/tmp"`` used for this variable may not be acceptable because ``"/tmp"`` directory
  can be transient on the system. In such cases it is recommended to specify non-default value for this variable. This
  variable can be specified in the inventory file or vars file.


  | **required**: False
  | **type**: str
  | **default**: /tmp

 

zmf_body
  Instead of specifying *system-name*, *sysplex-name*, *external_name*, *vendor_name*, *product_version*, *instance_description*,
  *instance_owner*, *instance_provider*, and *instance_var_json_path* individually, this parameter
  can be used to pass them as a dictionary variable. This variable needs to be in following format,


  ``{``

  ``"system-name":"{{ system_name }}",``

  ``"sysplex-name":"{{ sysplex_name }}",``

  ``"registry-type":"general",``

  ``"external-name":"{{ external_name }}",``

  ``"vendor":"{{ vendor_name }}",``

  ``"version":"{{ product_version }}",``

  ``"description":"{{ instance_description }}",``

  ``"owner":"{{ instance_owner }}",``

  ``"provider":"{{ instance_provider }}",``

  ``"state": "provisioned",``

  ``"actions": [ {"name" : "deprovision", "type" : "instructions",
      "instructions" : "perform this action to deprovision"} ],``


  ``"variables": {{ instance_variable_record }} ``

  ``}``

  Note: *instance_variable_record* is a dictionary object and needs to be in following format
  ``[``
      ``{``
      `` "name": "VAR1",``
      `` "value": "VAR1_VALUE",``
      `` "visibility": "public" ``
      ``},``
      ``{``
      `` "name": "VAR2",``
      `` "value": "VAR2_VALUE",``
      `` "visibility": "public" ``
      ``},``
      ....
  ``]``

  | **required**: False
  | **type**: dict



Examples
--------

.. code-block:: yaml+jinja

   
   - name: Create software instance of manually provisioned z/OS Middleware or z/OS software
     hosts: sampleHost
     gather_facts: no
     collections: 
       - ibm.ibm_zosmf
     tasks: 
       - include_module:
           name: zmf_cpm_create_software_instance
         vars:
           systems_name: "<system-name>"
           sysplex_name: "<sysplex-name>"
           external_name: "<external-name>"
           vendor_name: "<vendor-name>"
           product_version: "<product-version>"
           instance_description: "<instance-description>"
           instance_owner: "<instance-owner>"
           instance_provider: "<instance-provider>"
           instance_var_json_path: "<variables-json-file-path>"



Notes
-----

.. note::
   - The given example assumes that you have an inventory file *inventory.yml* and host vars *sampleHost.yml* with appropriate values to identify the target z/OSMF server end point.








