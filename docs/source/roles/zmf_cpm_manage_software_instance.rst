
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_cpm_manage_software_instance

.. _zmf_cpm_manage_software_instance_module:


zmf_cpm_manage_software_instance -- Manage a z/OS software instance
===================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Manage a provisioned instance of z/OS middleware or software.
- Depending on actions supported by z/OS middleware or software, various management such as starting or stopping the instance can be performed by using this role.

- When software service instance is not required any more, it can be deprovisioned by using this role.







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


 

instance_action_name
  Action to be performed on a provisioned software instance, for example, ``Deprovision``.


  Actions that can be performed on a provisioned instance are described in local record file that is associated with the provisioned instance. The *name* variable in *actions* array under *registry-info* identifies the various actions that can be performed on the instance.


  | **required**: True
  | **type**: str


 

instance_info_json_path
  Directory path for the JSON file that holds provisioned instance information.


  Specify the file name that was generated when the :ref:`zmf_cpm_provision_software_service <zmf_cpm_provision_software_service_module>` role was performed.


  | **required**: True
  | **type**: str


 

input_vars
  Input variable names and values for the action to be performed on the provisioned instance.


  This variable is required if the action processing expects specific inputs from user. This is a dictionary variable and needs to be in following format, ``[{ "name":"VAR1","value":"VAR1_VALUE"},{..},...]``


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

   
   - name: test role for zmf_cpm_manage_software_instance
     include_role :
       name: zmf_cpm_manage_software_instance
     vars:
       instance_action_name: "<action-name>"
       instance_info_json_path: "<full-instance-json-file-path>"
       input_vars: '<optional-fill-me-input-vars>'








