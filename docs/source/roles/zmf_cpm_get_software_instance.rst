
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_cpm_get_software_instance

.. _zmf_cpm_get_software_instance_module:


zmf_cpm_get_software_instance -- Role get specific z/OS software instance
=========================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The **IBM z/OSMF collection** provides an Ansible role, referred to as **zmf_cpm_get_software_instance**, to obtain a specific software instance defined in the **IBM Cloud Provisioning and Management (CP&M**) software instances registry.







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
  Directory path that the provisioning role uses to record the software instance and associated data (in JSON format).


  On many system default value ``"/tmp"`` used for this variable may not be acceptable because ``"/tmp"`` directory can be transient on the system. In such cases it is recommended to specify non-default value for this variable. This variable can be specified in the inventory file or vars file.


  | **required**: False
  | **type**: str
  | **default**: /tmp


 

external_name
  The external name associated with the previously created software instance in Cloud Provisioning and Management software registry.


  | **required**: True
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: sample of retrieving software instance from registry
     hosts: sampleHost
     gather_facts: no
     collections: 
       - ibm.ibm_zosmf

     vars:
       - name: instance_info_json_path
       
     tasks: 
       - include_module:
           name: zmf_cpm_get_software_instance
         vars:
           external_software_name: "<fill-me>"

       - name: Obtain Variable Value
         vars:
              instance_info_json: "{{lookup('file', instance_info_json_path)}}"

         set_fact:
       
            VAR1: "{{ instance_info_json['registry-info'] | json_query('variables[?name == `<fill-me>`]') | join(' ') }}"

       - name: Display VAR1 value
         debug:
             msg: "VAR1 Value is : {{ VAR1.value }}"




Notes
-----

.. note::
   - The given example assumes that you have an inventory file *inventory.yml* and host vars *sampleHost.yml* with appropriate values to identify the target z/OSMF server end point.


   - When playbooks completes, a message shown in following example is displayed, ``"msg": "Instance record saved at: /tmp/xxx/xxx.json"``. This message includes a file path and file name where the instance specific data of of requested software instance is returned. User can obtain specific property from this file using json_query.








