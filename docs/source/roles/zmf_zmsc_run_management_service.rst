
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_zmsc_run_management_service

.. _zmf_zmsc_run_management_service_module:


zmf_zmsc_run_management_service -- Role runs a z/OS management service
======================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The **IBM z/OSMF collection** provides an Ansible role, referred to as **zmf_zmsc_run_management_service**, to run a z/OS management service published in **z/OS Management Services Catalog**.

- Management Service referenced by playbook must be published in *z/OS Management Services Catalog*.

- This role will generate a unique JSON file that holds service instance information. The file location is in following format, ``<instance_record_dir>/<catalog_service_name>-<instance objectId>.json``







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
  Directory path that the run management service role uses to capture various information (in JSON format) about the service instance.


  On many system default value ``"/tmp"`` used for this variable may not be acceptable because ``"/tmp"`` directory can be transient on the system. In such cases it is recommended to specify non-default value for this variable. This variable can be specified in the inventory file or vars file.


  | **required**: False
  | **type**: str
  | **default**: /tmp


 

catalog_service_name
  Service name of the management service to be run.

  | **required**: True
  | **type**: str


 

category_name
  Category name associated with the management service to be run. If there after are multiple managment services with same name, this parameter is required to uniquely identify management service to be run.

  | **required**: False
  | **type**: str


 

change_record_number
  Change record number associated with the change being performed by management service. This information is required when z/OS Management Service Catalog is configured to require change record number to run any management service.


  | **required**: False
  | **type**: str


 

job_statement
  Job statement to be used when running a management service.


  | **required**: False
  | **type**: str


 

system_nickname
  System nickname as specified in the z/OSMF Systems table.

  If this variable is not specified, management service will run on the system where z/OSMF is currently running.


  | **required**: False
  | **type**: str


 

input_vars
  Input variable names and values for the management service to be run.


  This variable is required if management service expects specific inputs from user. This is a json variable and needs to be in following format, ``{ "var1":"value1","var2":"value2",...}``


  | **required**: False
  | **type**: json


 

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

   
   - name: Run z/OS Management Service
     hosts: sampleHost
     gather_facts: no
     collections: 
       - ibm.ibm_zosmf
     tasks: 
       - include_module:
           name: zmf_zmsc_run_management_service
         vars:
           catalog_service_namme: "<fill-me-service-name>"
           category_name: "<optional-category-name>"
           change_record_number: "<optional-change_record_number>"
           job_statement: "<optional-job_statement>"
           systems_name: "<optional-system-name>"
           input_vars: "<optional-input-vars>"
           



Notes
-----

.. note::
   - The given example assumes that you have an inventory file *inventory.yml* and host vars *sampleHost.yml* with appropriate values to identify the target z/OSMF server end point.


   - When playbooks completes, a message shown in following example is displayed, ``"msg": "Instance record saved at: /tmp/xxx/xxx.json"``. This message includes a file path and file name where instance specific information is returned.








