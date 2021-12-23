
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_cpm_list_software_templates

.. _zmf_cpm_list_software_templates_module:


zmf_cpm_list_software_templates -- Role lists all published z/OS software templates
===================================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The **IBM z/OSMF collection** provides an Ansible role, referred to as **zmf_cpm_list_software_templates**, to obtain list of all the published templates that can be used to provision z/OS middleware such as  IBM Customer Information Control System (CICS®), IBM Db2®, IBM MQ, and IBM WebSphere Application Server or any other software service from **IBM Cloud Provisioning and Management (CP&M**) catalog.







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


 

instance_record_dir
  Directory path that the provisioning role uses to capture list of published templates (in JSON format).


  On many system default value ``"/tmp"`` used for this variable may not be acceptable because ``"/tmp"`` directory can be transient on the system. In such cases it is recommended to specify non-default value for this variable. This variable can be specified in the inventory file or vars file.


  | **required**: False
  | **type**: str
  | **default**: /tmp




Examples
--------

.. code-block:: yaml+jinja

   
   - name: list published provisioning templates
     hosts: sampleHost
     gather_facts: no
     collections: 
       - ibm.ibm_zosmf
     tasks: 
       - include_module:
           name: zmf_cpm_list_software_templates
         



Notes
-----

.. note::
   - The given example assumes that you have an inventory file *inventory.yml* and host vars *sampleHost.yml* with appropriate values to identify the target z/OSMF server end point.


   - When playbooks completes, a message shown in following example is displayed, ``"msg": "Published Template List saved at: /tmp/xxx.json"``. This message includes a file path and file name where the list of published template is returned.








