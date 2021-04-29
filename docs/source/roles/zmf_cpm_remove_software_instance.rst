
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_cpm_remove_software_instance

.. _zmf_cpm_remove_software_instance_module:


zmf_cpm_remove_software_instance -- Remove a z/OS software instance
===================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Remove a deprovisioned instance of z/OS middleware or software service.






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


 

instance_info_json_path
  Directory path for the JSON file that holds provisioned instance information.


  Specify the file name that was generated when the :ref:`zmf_cpm_provision_software_service <zmf_cpm_provision_software_service_module>` role was performed.


  | **required**: True
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: test role for zmf_cpm_remove_software_instance
     include_role :
       name: zmf_cpm_remove_software_instance
     vars:
       instance_info_json_path: "<full-instance-json-file-path>"








