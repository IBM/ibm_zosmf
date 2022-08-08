
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_workflow_complete

.. _zmf_workflow_complete_module:


zmf_workflow_complete -- Role completes a z/OS workflow
=======================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Complete a z/OS workflow, either forcibly or idempotently.
- This role runs z/OSMF workflows that are located on the target z/OS managed node. The workflows must be z/OSMF XML workflows and be located in a z/OS UNIX System Services (z/OS UNIX) filesystem.



Dependencies
------------

The below requirements are needed on the host that executes this role.

- Module :ref:`zmf_workflow <zmf_workflow_module>`





Variables
---------


 

zmf_host
  Hostname of the z/OSMF server, specified in the inventory file or vars file.


  | **required**: True
  | **type**: str


 

zmf_port
  Port number of the z/OSMF server, specified in the inventory file or vars file.


  | **required**: False
  | **type**: int


 

zmf_user
  User name to be used for authenticating with the z/OSMF server.

  This variable can be specified in the inventory file or vars file, or prompted when playbook is run.


  Required when *zmf_crt* and *zmf_key* are not supplied.

  If *zmf_crt* and *zmf_key* are supplied, *zmf_user* and *zmf_password* are ignored.


  | **required**: False
  | **type**: str


 

zmf_password
  Password to be used for authenticating with z/OSMF server.

  This variable can be specified in the inventory file or vars file, or prompted when playbook is run.


  Required when *zmf_crt* and *zmf_key* are not supplied.

  If *zmf_crt* and *zmf_key* are supplied, *zmf_user* and *zmf_password* are ignored.


  | **required**: False
  | **type**: str


 

zmf_crt
  Location of the PEM-formatted certificate chain file to be used for HTTPS client authentication.


  This variable can be specified in the inventory file or vars file, or prompted when playbook is run.


  Required when *zmf_user* and *zmf_password* are not supplied.

  | **required**: False
  | **type**: str


 

zmf_key
  Location of the PEM-formatted file with your private key to be used for HTTPS client authentication.


  This variable can be specified in the inventory file or vars file, or prompted when playbook is run.


  Required when *zmf_user* and *zmf_password* are not supplied.

  | **required**: False
  | **type**: str


 

workflow_name
  Descriptive name of the workflow.

  The workflow name is not case-sensitive, for example, ``MyWorkflow`` and ``MYWORKFLOW`` are the same workflow.


  | **required**: True
  | **type**: str


 

workflow_file
  Location of the workflow definition file.

  | **required**: False
  | **type**: str


 

workflow_owner
  User name of the workflow owner.

  If this value is omitted, *zmf_user* is used as workflow owner.

  | **required**: False
  | **type**: str


 

workflow_file_system
  Nickname of the system on which the specified workflow definition file resides, along with any related files.


  | **required**: False
  | **type**: str


 

workflow_vars_file
  Location of the optional properties file to be used to pre-specify the values of one or more variables in the workflow definition file.


  | **required**: False
  | **type**: str


 

workflow_vars
  Values of one or more workflow variables in JSON format.

  For example, ``{"user_to_list":"DEBUG1", "tsocmd_to_issue":"TIME"}``


  | **required**: False
  | **type**: dict


 

workflow_resolve_global_conflict_by_using
  Version of the variable to be used if the supplied workflow variable conflicts with an existing global variable in z/OSMF Workflows task.


  | **required**: False
  | **type**: str
  | **default**: global
  | **choices**: global, input


 

workflow_comments
  User-specified information to be associated with the workflow at creation time.


  | **required**: False
  | **type**: str


 

workflow_assign_to_owner
  Specifies whether the workflow steps are assigned to the workflow owner when the workflow is created.


  | **required**: False
  | **type**: bool
  | **default**: True


 

workflow_access_type
  Access type for the workflow when the workflow is created.

  | **required**: False
  | **type**: str
  | **default**: Public
  | **choices**: Public, Restricted, Private


 

workflow_account_info
  For a workflow that submits a batch job, this variable specifies the account information for the JCL JOB statement.


  | **required**: False
  | **type**: str


 

workflow_job_statement
  For a workflow that submits a batch job, this variable specifies the JOB statement JCL for the job.


  | **required**: False
  | **type**: str


 

workflow_delete_completed_jobs
  For a workflow that submits a batch job, this variable specifies whether the job is deleted from the JES spool after it completes.


  | **required**: False
  | **type**: bool
  | **default**: False


 

workflow_resolve_conflict_by_using
  Specifies how to handle variable conflicts, if any are detected at workflow creation time.


  Such conflicts can be found when the z/OSMF Workflows task reads the output file from a step that runs a REXX exec or UNIX shell script.


  | **required**: False
  | **type**: str
  | **default**: outputFileValue
  | **choices**: outputFileValue, existingValue, leaveConflict


 

workflow_step_name
  Name of the workflow step at which automation processing is to begin when the workflow is started.


  | **required**: False
  | **type**: str


 

workflow_perform_subsequent
  Specifies whether the subsequent automated steps are performed when the workflow is started.


  | **required**: False
  | **type**: bool
  | **default**: True


 

workflow_notification_url
  URL to be used for receiving notifications when the workflow is started.


  | **required**: False
  | **type**: str


 

force_complete
  Specify whether to complete the workflow instance forcibly or idempotently.


  If *force_complete=true* (Forcibly), this role will delete the workflow instance if it exists in the z/OSMF server, create a new workflow instance and start it on each target z/OS system, and periodically check the workflow status and return the final result when the workflow completes.


  If *force_complete=false* (Idempotently),
    - If the workflow does not exist, this role will create the workflow instance.
    -
      If the workflow exists but has different content(such as same workflow definition, same
      varaible values, etc.), this role will delete the existing workflow and create a new workflow instance.
    -
      If the workflow exists and has consistent content(such as same workflow definition, same
      varaible values, etc.), this workflow will be used.


  Then this role will start the workflow on each target z/OS system, and periodically check the workflow status and return the final result when the workflow completes.


  | **required**: False
  | **type**: bool
  | **default**: False


 

complete_check_times
  The maximum number of checks that can be made of the workflow status.


  | **required**: False
  | **type**: int
  | **default**: 10


 

complete_check_delay
  The interval time (in seconds) between periodic checks of the workflow status.


  | **required**: False
  | **type**: int
  | **default**: 5




Examples
--------

.. code-block:: yaml+jinja

   
   - name: sample of completing a z/OS workflow
     include_role :
       name: zmf_workflow_complete
     vars:
       workflow_name: "ansible_sample_workflow_{{ inventory_hostname }}"
       workflow_file: "/var/zosmf/workflow_def/workflow_sample_automation_steps.xml"
       force_complete: False
       complete_check_times: 10
       complete_check_delay: 5



Notes
-----

.. note::
   - Submitting a z/OSMF workflow found on Ansible control node is currently not supported.


   - Only automated steps are supported when starting a z/OSMF workflow.




See Also
--------

.. seealso::
   - :ref:`zmf_workflow_module`





