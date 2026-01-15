
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_swmgmt_holds_for_reason

.. _zmf_swmgmt_holds_for_reason_module:


zmf_swmgmt_holds_for_reason -- Collect ++HOLDs for selected REASON IDs
======================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The \ :strong:`IBM z/OSMF collection`\  provides an Ansible role, referred to as \ :strong:`zmf\_swmgmt\_holds\_for\_reason`\ , to separate SYSTEM HOLDs by REASON and prepare to query the CSI associated with a software instance. The SYSTEM HOLDs are gathered from the retrieve software update response and then the HOLDDATA text is gathered from the CSI query response.







Variables
---------


 

software_instance_uuid
  A UUID of a software instance. A UUID is assigned to every software instance and can be obtained using the "List the software instances defined to z/OSMF" REST API.


  A UUID can also be obtained using the zmf\_swmgmt\_zos\_system\_uuid Ansible role which retrieves the UUID for the software instance that represents the installed software for the specified z/OSMF host system.


  A software instance UUID name must be specified.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: True
  | **type**: str


 

hold_reason
  The HOLD REASON ID for which to get the HOLDDATA text.


  A HOLD REASON ID must be 1-7 characters long and is accepted in mixed case and is folded to uppercase automatically. It may consist of alphabetic, numeric, and national characters (@ \\# $).


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: True
  | **type**: str


 

holds_for_reason_dir
  The directory that will contain the HOLDDATA text file. The directory specified must have valid UNIX directory name syntax. It must start and end with a slash ('/') and can be up to 1023 characters long.


  One file will be written in this directory with the HOLDDATA text pertaining to the specified HOLD REASON each time this role is invoked. The file written will follow this naming convention where the file name will be the HOLD REASON: \ :literal:`YourHoldReason-HOLDDATA.txt`\ 


  The directory must already exist otherwise there will be an error writing the results to the file. If files with the same name already exist in the directory, they will be overwritten by the new response when the playbook is executed. If files don't exist in the directory, they will be created.


  This variable can be specified in the inventory file or as an argument on the playbook command.


  | **required**: True
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: sample of separating HOLDs by REASON
     hosts: sampleHost
     gather_facts: no
     collections:
       - ibm.ibm_zosmf

     tasks:
       - include_role :
           name: zmf_swmgmt_holds_for_reason




Notes
-----

.. note::
   - The given example assumes you have an inventory file \ :emphasis:`inventory.yml`\  that contains the values for the two variables described above: software instance UUID and the HOLD REASON.


   - Command syntax to call a playbook using an inventory file: \ :literal:`ansible-playbook -i inventory software\_management\_holds\_for\_reason\_CICDtest1.yml`\ 


   - Command syntax to call a playbook using command arguments: \ :literal:`ansible-playbook software\_management\_holds\_for\_reason\_CICDtest1.yml -e software\_instance\_uuid=cccccc...444444 -e hold\_reason=ACTION -e holds\_for\_reason\_file=/Users/yourUser/AnsibleOutputDir/`\ 


   - When the role is executed, a message shown in following example is displayed, \ :literal:`"msg": "Output filename= /tmp/xxx/ACTION-HOLDDATA.txt"`\ . This message includes a file path and file name where the HOLDDATA text for the requested HOLD REASON is returned.








