
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_cpm_get_software_instance

.. _zmf_cpm_get_software_instance_module:


zmf_cpm_get_software_instance -- Role retrieves a z/OS software instance
=========================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The **IBM z/OSMF collection** provides an Ansible role, referred to as **zmf_cpm_get_software_instance**, to get a software instance from **IBM Cloud Provisioning and Management (CP&M)** registry.







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

external_software_name
  The external name associated with the software instance that was created in z/OSMF CP&M Registry before.


  | **required**: True
  | **type**: str

instance_record_dir
  Directory path that the CP&M roles use to capture various information (in JSON format) about the software instance.
  On many system default value ``"/tmp"`` used for this variable may not be acceptable because ``"/tmp"`` directory
  can be transient on the system. In such cases it is recommended to specify non-default value for this variable. This
  variable can be specified in the inventory file or vars file.


  | **required**: False
  | **type**: str
  | **default**: /tmp


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
           name: zmf_cpm_get_software_instance
         vars:
            external_software_name: "{{ external_name }}"



Notes
-----

.. note::
   - The given example assumes that you have an inventory file *inventory.yml* and host vars *sampleHost.yml* with appropriate values to identify the target z/OSMF server end point.








