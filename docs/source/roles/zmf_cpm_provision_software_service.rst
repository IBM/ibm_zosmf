
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_cpm_provision_software_service

.. _zmf_cpm_provision_software_service_module:


zmf_cpm_provision_software_service -- Role provisions a z/OS software service
=============================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The **IBM z/OSMF collection** provides an Ansible role, referred to as **zmf_cpm_provision_software_service**, to provision a z/OS middleware such as IBM Customer Information Control System (CICS®), IBM Db2®, IBM Information Management System (IMS™), IBM MQ, and IBM WebSphere Application Server or any other software service by using an **IBM Cloud Provisioning and Management (CP&M**) template.

- Template referenced by playbook must be published in *z/OSMF Software Services Catalog*.

- This role will generate a unique JSON file that holds provisioned instance information. The file location is in following format, ``<instance_record_dir>/<cpm_template_name>-<instance external_name>.json``







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
  Directory path that the provisioning role uses to capture various information (in JSON format) about the provisioned instance.


  On many system default value ``"/tmp"`` used for this variable may not be acceptable because ``"/tmp"`` directory can be transient on the system. In such cases it is recommended to specify non-default value for this variable. This variable can be specified in the inventory file or vars file.


  | **required**: False
  | **type**: str
  | **default**: /tmp


 

cpm_template_name
  Template name for the software service to be provisioned.

  | **required**: True
  | **type**: str


 

domain_name
  Cloud domain name that is associated with the template.

  | **required**: True
  | **type**: str


 

tenant_name
  CP&M Tenant name that is associated with the user who is performing this role.


  This variable is required if *zmf_user* is associated with multiple CP&M tenants.


  | **required**: False
  | **type**: str


 

systems_nicknames
  System nickname as specified in the z/OSMF Systems table.

  If this variable is not specified, provisioning is performed on the system where z/OSMF is currently running.


  | **required**: False
  | **type**: str


 

input_vars
  Input variable names and values for the software service to be provisioned.


  This variable is required if software service expects specific inputs from user. This is a dictionary variable and needs to be in following format, ``[{ "name":"VAR1","value":"VAR1_VALUE"},{..},...]``


  | **required**: False
  | **type**: dict


 

zmf_body
  Instead of specifying *domain_name*, *tenant_name*, *system_nicknames* and *input_variable* individually, this parameter can be used to pass them as a dictionary variable. This variable needs to be in following format,


  ``{``

  ``"domain-name":"{{ domain_name }}",``

  ``"domain-name":"{{ domain_name }}",``

  ``"systems-nicknames":["{{ systems_nicknames }}"],``

  ``"input-variables":"{{ input_vars }}"``

  ``}``

  | **required**: False
  | **type**: dict


 

api_polling_retry_count
  Total retry attempts allowed before the role exits with failure, waiting on the instance action to complete.


  This variable can be specified in the inventory file or vars file.


  | **required**: False
  | **type**: int
  | **default**: 50


 

api_polling_interval_seconds
  Interval time (in seconds) for each polling request.


  This variable can be specified in the inventory file or vars file.


  | **required**: False
  | **type**: int
  | **default**: 10




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Provision a z/OS Middleware service
     hosts: sampleHost
     gather_facts: no
     collections: 
       - ibm.ibm_zosmf
     tasks: 
       - include_module:
           name: zmf_cpm_provision_software_service
         vars:
           cpm_template_name: "<fill-me-template-name>"
           domain_name: "<domain-name>"
           tenant_name: "<optional-tenant-name>"
           systems_nicknames: "<optional-system-name>"
           input_vars: "<optional-input-vars>"
           



Notes
-----

.. note::
   - The given example assumes that you have an inventory file *inventory.yml* and host vars *sampleHost.yml* with appropriate values to identify the target z/OSMF server end point.


   - When playbooks completes, a message shown in following example is displayed, ``"msg": "Instance record saved at: /tmp/xxx.json"``. This message includes a file path and file name where instance specific information is returned. This file is required for :ref:`zmf_cpm_manage_software_instance <zmf_cpm_manage_software_instance_module>` and :ref:`zmf_cpm_remove_software_instance <zmf_cpm_remove_software_instance_module>` roles.








