# Copyright (c) IBM Corporation 2021

:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_cpm_manage_software_instance

.. _zmf_cpm_manage_software_instance:

zmf_cpm_manage_software_instance
=================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------
Manage a provisioned instance of z/OS middleware or software. Depending on actions supported by z/OS middleware or software, 
various management such as starting or stopping the instance can be performed using this role. When software service instance is 
not required any more, it can be deprovisioned using this role.

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

instance_action_name
  Action to be performed on a provisioned software instance, for example: Deprovision.
  
  Actions that can be performed on a provisioned instance are described in local record file associated with the provisioned instance. The *name* variable in *actions* array under *registry-info* identifies various actions that can be performed on the instance.

  | **required**: True
  | **type**: str

instance_info_json_path
  Path to the json file that holds provisioned instance information. 
  
  Specify the file name that is generated when `zmf_cpm_provision_software_service`_ role was performed.

  | **required**: True
  | **type**: str

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

   
   - name: test role for zmf_cpm_manage_software_instance
     hosts: cpmHost1 # need to match host nick name specified in hosts inventory file
     gather_facts: no
     collections:
       - ibm.ibm_zosmf
     vars_prompt:
       - name: zmf_user
         prompt: "Enter your zOSMF username"
         private: no

       - name: zmf_password
         prompt: "Enter your zOSMF password"
         private: yes  
     tasks:
       - include_role:
           name: zmf_cpm_manage_software_instance
         vars:
           instance_action_name: "<action-name>"
           instance_info_json_path: "<full-instance-json-file-path>"

Return
------
None          

# Roles don't return anything, this RETURN block must be defined and remain
# empty for doc extraction tooling to avoid an error.
RETURN = r"""
 """