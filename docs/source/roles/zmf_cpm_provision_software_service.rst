# Copyright (c) IBM Corporation 2021

:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_cpm_provision_software_service

.. _zmf_cpm_provision_software_service:

zmf_cpm_provision_software_service
==================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Provision a z/OS middleware or software service using Cloud Provisioning & Management (CP&M) template.
- Template referenced by playbook must be published in z/OSMF Software Services Catalog.



Variables
---------

zmf_host
  z/OSMF host name, specified via inventory file.

  | **required**: True
  | **type**: str

zmf_port
  z/OSMF port number, specified via inventory file.

  | **required**: True
  | **type**: str

zmf_user
  z/OSMF username. Value for this variable can be specified in host specific variables file in *host_vars* directory or 
  playbook can prompt user to provide value.

  | **required**: True
  | **type**: str

zmf_password
  z/OSMF user password  Value for this variable can be specified in host specific variables file in *host_vars* directory or 
  playbook can prompt user to provide value.

  | **required**: True
  | **type**: str

instance_record_dir
  Path of the directory that provision role will use to capture various information about provisioned instance in json format. 
  
  Value for this variable is specified in host specific variables file in *host_vars* directory.

  | **required**: True
  | **type**: str
  | **default**: default value set in host_vars file is /tmp

instance_info_json_path
  Path to the file that holds provisioned instance information, `zmf_cpm_provision_software_service`_ role  
  will automatically generate this variable in the format of ``<instance_record_dir>/<template_name>-<instance external_name>.json``

  | **required**: False
  | **type**: str

cpm_template_name
  Template name, i.e. software service to be provisioned.

  | **required**: True
  | **type**: str

domain_name
  Cloud domain name associated with the template.

  | **required**: True
  | **type**: str

tenant_name
  Identifies the CP&M Tenant name associated with the user that is driving this role. 
  
  This variable is required if *zmf_user* is associated with multiple CP&M tenants.

  | **required**: True
  | **type**: str

systems_nicknames
  System nick name as identified in z/OSMF. 
  
  If this variable is not specified, provisioning will take place on a system where z/OSMF is currently running.

  | **required**: False
  | **type**: str

input_vars
  Input variable names and values for the software service to be provisioned 
  
  This variable is required if software service expects specific inputs from user. This is a dictionary variable and needs to be in following format.

  [{ "name":"VAR1","value":"VAR1_VALUE"},{..},...]

  | **required**: False
  | **type**: dict

zmf_body
  Instead of specifying **domain-name**, **tenant-name**, **system-nicknames** and **input-variable**
  individually, this parameter can be used to pass them as a dictionary variable. This variable needs to
  be in following format.

  {"domain-name":"{{ domain_name }}","tenant-name":"{{ tenant_name }}",
      "systems-nicknames":["{{ systems_nicknames }}"],"input-variables":{{ input_vars }}}

  | **required**: False
  | **type**: dict

api_polling_retry_count
  Total retries number before role exit with failure waiting on instance action to complete. 
  
  This variable is specified in host specific variables file in *host_vars* directory.

  | **required**: True
  | **type**: int
  | **default**: default value set in host_vars file is 50

api_polling_interval_seconds
  Interval time for each polling request in seconds. 
  
  This variable is specified in host specific variables file in *host_vars* directory.

  | **required**: True
  | **type**: int
  | **default**: default value set in host_vars file is 10

Dependencies
------------

None

Requirements
------------

See the section `Requirements`_.

Examples
--------

.. code-block:: yaml+jinja

   
   - name: test role for zmf_cpm_provision_software_service
     hosts: cpmHost1 # need to match host nick name specified in hosts inventory file
     gather_facts: no
     collections:
       - ibm.ibm_zosmf
     vars:
       - name: instance_info_json_path  
    tasks:
      - include_role:
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
   - When playbooks completes, a message shown in following example is displayed. This message includes  
     a file path and file name where instance specific information is returned. This file is required for
     `zmf_cpm_manage_software_service`_ and `zmf_cpm_remove_software_service`_ roles.

      TASK [ibm.ibm_zos_zosmf.zmf_cpm_provision_software_service : Display instance record file path] ********************************************************************
        ok: [xxx] => {
            "msg": "Instance record saved at: /tmp/xxx.json"
            }

# Roles don't return anything, this RETURN block must be defined and remain
# empty for doc extraction tooling to avoid an error.
RETURN = r"""
 """