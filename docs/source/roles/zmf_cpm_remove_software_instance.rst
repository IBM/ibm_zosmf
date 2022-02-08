
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_cpm_remove_software_instance

.. _zmf_cpm_remove_software_instance_module:


zmf_cpm_remove_software_instance -- Role removes a z/OS software instance
=========================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The **IBM z/OSMF collection** provides an Ansible role, referred to as **zmf_cpm_remove_software_instance**, to remove a deprovisioned instance of z/OS middleware such as IBM Customer Information Control System (CICS®), IBM Db2®, IBM Information Management System (IMS™), IBM MQ, and IBM WebSphere Application Server or any other software service from **IBM Cloud Provisioning and Management (CP&M**) registry.







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


 

instance_info_json_path
  Directory path for the JSON file that holds provisioned instance information.


  Specify the file name that was generated when the :ref:`zmf_cpm_provision_software_service <zmf_cpm_provision_software_service_module>` role was performed.


  | **required**: True
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Remove deprovisioned instance of z/OS Middleware
     hosts: sampleHost
     gather_facts: no
     collections: 
       - ibm.ibm_zosmf
     tasks: 
       - include_module:
           name: zmf_cpm_remove_software_instance
         vars:
           instance_info_json_path: "<full-instance-json-file-path>"



Notes
-----

.. note::
   - The given example assumes that you have an inventory file *inventory.yml* and host vars *sampleHost.yml* with appropriate values to identify the target z/OSMF server end point.








