
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_swupdate_resume

.. _zmf_swupdate_resume_module:


zmf_swupdate_resume -- Resume a Software Update Process
=======================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- The :strong:`IBM z/OSMF collection` provides an Ansible role, referred to as :strong:`zmf\_swupdate\_resume`\ , to resume a currently suspended software update process for a specified software instance. The process ID associated with the software update process that gets resumed is saved in a variable to be referenced by subsequent roles in the playbook.






Variables
---------


 

zmf_host
  Hostname of the z/OSMF server, specified in the inventory file or as an argument on the playbook command.

  | **required**: True
  | **type**: str


 

zmf_port
  Port number of the z/OSMF server. If z/OSMF is not using the default port, you need to specify a value for this parameter in the inventory file or as an argument on the playbook command.

  | **required**: False
  | **type**: str
  | **default**: 443


 

zmf_user
  User ID for authenticating with the z/OSMF server.

  This variable can be specified in the inventory file or as an argument on the playbook command.

  | **required**: True
  | **type**: str


 

zmf_password
  Password to be used for authenticating with z/OSMF server.

  This variable can be specified in the inventory file or as an argument on the playbook command.

  | **required**: True
  | **type**: str


 

software_instance_name
  Name of the software instance whose suspended software update process is resumed.

  A software instance name must be specified when a software instance UUID or a software update process ID are not specified. If a software update process ID is specified in addition to a software instance name and system nickname, then the software update process ID is used by default.

  This variable can be specified in the inventory file or as an argument on the playbook command.

  | **required**: False
  | **type**: str


 

system_nickname
  Nickname of the z/OSMF host system that has access to the volumes and data sets where the software instance resides.

  A system nickname must be specified when a software instance UUID or a software update process ID are not specified. If a software update process ID is specified in addition to a software instance name and system nickname, then the software update process ID is used by default.

  This variable can be specified in the inventory file or as an argument on the playbook command.

  | **required**: False
  | **type**: str


 

software_instance_uuid
  A UUID of a software instance whose suspended software update process is resumed. A UUID is assigned to every software instance and can be obtained using the "List the software instances defined to z/OSMF" REST API.

  A UUID can also be obtained using the zmf\_swmgmt\_zos\_system\_uuid Ansible role which retrieves the UUID for the software instance that represents the installed software for the specified z/OSMF host system.

  A software instance UUID must be specified when a software instance name or a software update process ID are not specified. If a software update process ID is specified in addition to a software instance UUID, then the software update process ID is used by default.

  This variable can be specified in the inventory file or as an argument on the playbook command.

  | **required**: False
  | **type**: str


 

swupdate_process_id
  A software update process ID indicating the software update process to be resumed.

  A software update process ID must be specified when a software instance name or a software instance UUID are not specified. If a process ID is specified in addition to a software instance name or UUID, then the process ID is used by default.

  This variable can be specified in the inventory file or as an argument on the playbook command.

  | **required**: False
  | **type**: str


 

suspend_steps
  The RESOLVE\_HOLDS and PRE\_INSTALLATION\_SUMMARY steps may be specified on the suspend-steps property to allow for review or interaction of the update process. A software update process has 6 steps:

  PREPARING\_UPDATES: z/OSMF is performing an APPLY CHECK to identify HOLDs for review and ensure no missing requisites.

  RESOLVE\_HOLDS: User reviews and resolves each HOLD, either bypass the HOLD or exclude the update.

  VERIFYING\_UPDATES: z/OSMF performs APPLY CHECK to validate the HOLD resolution choices.

  PRE\_INSTALLATION\_SUMMARY: User reviews the list of updates that will be installed.

  INSTALLATION: z/OSMF performs the APPLY.

  COMPLETE: The installation is complete. User should review any HOLDs that need ACTION after the APPLY.

  The suspend-steps array needs to be in the following format: :literal:`'"SUSPEND-STEP1","SUSPEND-STEP2"'`

  This variable can be specified in the inventory file or as an argument on the playbook command.

  | **required**: False
  | **type**: arr


 

exclude_updates
  List of software update names to exclude from the installation.

  Update names must be 7 characters long and are accepted in mixed case and are folded to uppercase automatically. They may consist of alphabetic, numeric, and national characters (@,#,$).

  The exclude-updates array needs to be in the following format: :literal:`'"UPDATE1","UPDATE2"'`

  This variable can be specified in the inventory file or as an argument on the playbook command.

  | **required**: False
  | **type**: arr


 

resolve_holds
  List of resolve-options to resolve HOLDs. If resolve-options are not provided, or there are other HOLDs to be resolved, the software update process will suspend at the RESOLVE\_HOLDS step and cannot proceed until all HOLDs have been resolved.

  The resolve-holds array needs to be in the following format: :literal:`'[{"type":"TYPE1","reason":"REASON1","names":["UPDATE1"]}, {"type":"TYPE2","reason":"REASON2","names":["UPDATE2"]}]'`

  Below are the descriptions of the resolve-hold object properties:

  type: The hold type of the hold. This property is required if resolve-holds is specified. Valid hold types are "SYSTEM", "ERROR", "FIXCAT", and "USER". For more information about hold types see https://www.ibm.com/docs/en/zos/3.1.0?topic=statements-hold-mcs in z/OS SMP/E Reference.

  reason: The reason value for the hold. The hold reason must be 1-7 characters long and is accepted in mixed case and is folded to uppercase automatically. It may consist of alphabetic, numeric, and national characters (@,#,$). If a hold-reason is not provided, all holds of the specified hold-type will be resolved.

  names: List of update names for which to resolve the specified hold-type and hold-reason. This property is only allowed for the SYSTEM hold-type. If a list of update names is not provided, all holds of the specified hold-type, and hold-reason if specifed, will be resolved.

  This variable can be specified in the inventory file or as an argument on the playbook command.

  | **required**: False
  | **type**: arr


 

smpe_userid
  The user ID used to run SMP/E operations instead of your z/OSMF user ID.

  Your z/OSMF user ID acts as a surrogate user to run SMP/E on behalf of the specified user.

  If an SMP/E user ID is not specified in the request content, but an SMP/E user ID is specified in the Software Update UI Settings Page, for the logged-in user and selected system, that SMP/E user ID will be used to start the TSO address space and perform the SMP/E operations.

  This variable can be specified in the inventory file or as an argument on the playbook command.

  | **required**: False
  | **type**: str


 

notes
  Notes about the software update process. The maximum length for the notes property is 140 characters.

  This variable can be specified in the inventory file or as an argument on the playbook command.

  | **required**: False
  | **type**: str


 

remote_zmf_user
  User ID for authenticating with a remote z/OSMF server.  Used only if the software instance resides on a remote z/OSMF server.

  | **required**: False
  | **type**: str


 

remote_zmf_password
  Password for authenticating with a remote z/OSMF server.

  | **required**: False
  | **type**: str


 

proxy_zmf_user
  User ID for authenticating with an HTTP proxy server.

  | **required**: False
  | **type**: str


 

proxy_zmf_password
  Password for authenticating with an HTTP proxy server.

  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: sample of resuming a software update on a software instance
     hosts: sampleHost
     gather_facts: no
     collections:
       - ibm.ibm_zosmf

     tasks:
       - include_role :
           name: zmf_swupdate_resume
       - set_fact :
           zmf_user: 'ibmuser'
           zmf_password: 'ibmuser'
           software_instance_name: 'YourSwiName'
           system_nickname: 'YourSystemName'
           resolve_holds: '[{"type":"SYSTEM"}]'




Notes
-----

.. note::
   - The given example assumes you have an inventory file :emphasis:`inventory.yml` that contains the values for the variables described above, such as z/OSMF host server, userid, password, software instance name and system, software update process ID, and request content variables.

   - Command syntax to call a playbook using an inventory file: :literal:`ansible-playbook -i inventory software\_management\_swu\_resume\_CICDtest1.yml`

   - Command syntax to call a playbook using command arguments: :literal:`ansible-playbook software\_management\_swu\_resume\_CICDtest1.yml -e zmf\_user=ibmuser -e zmf\_password=ibmuser -e software\_instance\_name=YourSwiName -e system\_nickname=YourSystemName -e resolve\_holds='[{"type":"SYSTEM"}]' -e smpe\_userid=smpuser -e notes='Resuming a SWU on YourSwiName from Ansible' -e swupdate\_retrieve\_response\_file=/Users/yourUser/AnsibleOutputDir/YourSwiNameRetrieve.json`







