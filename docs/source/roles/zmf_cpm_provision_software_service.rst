
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_cpm_provision_software_service

.. _zmf_cpm_provision_software_service_module:


zmf_cpm_provision_software_service -- provision a z/OS software service
=======================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Provision a z/OS middleware or software service by using an IBM Cloud Provisioning and Management (CP&M) template.

- Template referenced by playbook must be published in z/OSMF Software Services Catalog.







Variables
---------


 

zmf_host
  Hostname of the z/OSMF server, specified in the inventory file or vars file.


  | **required**: True
  | **type**: str


 

zmf_port
  Port number of the z/OSMF server, specified in the inventory file or vars file.


  | **required**: True
  | **type**: str


 

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


  This variable can be specified in the inventory file or vars file.


  | **required**: True
  | **type**: str


 

instance_info_json_path
  Directory path for the JSON file that holds provisioned instance information.


  This role will automatically generate this variable in following format, ``<instance_record_dir>/<template_name>-<instance external_name>.json``


  | **required**: False
  | **type**: str


 

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


  | **required**: True
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
  Instead of specifying *domain-name*, *tenant-name*, *system-nicknames* and *input-variable* individually, this parameter can be used to pass them as a dictionary variable. This variable needs to be in following format,


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


  | **required**: True
  | **type**: int


 

api_polling_interval_seconds
  Interval time (in seconds) for each polling request.


  This variable can be specified in the inventory file or vars file.


  | **required**: True
  | **type**: int




Examples
--------

.. code-block:: yaml+jinja

   
   - name: test role for zmf_cpm_provision_software_service
     include_role :
       name: zmf_cpm_provision_software_service
     vars:
       cpm_template_name: "<fill-me-template-name>"
       domain_name: "<domain-name>"
       tenant_name: "<tenant-name>"
       systems_nicknames: "<system-name>"
       input_vars: "<input-vars>"



Notes
-----

.. note::
   - When playbooks completes, a message shown in following example is displayed. This message includes a file path and file name where instance specific information is returned. This file is required for :ref:`zmf_cpm_manage_software_instance <zmf_cpm_manage_software_instance_module>` and :ref:`zmf_cpm_remove_software_instance <zmf_cpm_remove_software_instance_module>` roles.








