
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/roles/zmf_workflow_complete

.. _zmf_workflow_complete_role:


zmf_workflow_complete -- complete a z/OS workflow
=================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Complete a z/OS workflow, either forcibly or idempotently, by executing z/OSMF workflows that are located on z/OS system.

- The workflows must be z/OSMF XML workflows and located on UNIX System Services (USS).







Variables
---------


 

zmf_host
  Hostname of the z/OSMF server.

  If *zmf_credential* is supplied, *zmf_host* is ignored.

  If *zmf_credential* is not supplied, *zmf_host* is required.

  | **required**: False
  | **type**: str


 

zmf_port
  Port number of the z/OSMF server.

  If *zmf_credential* is supplied, *zmf_port* is ignored.

  | **required**: False
  | **type**: int


 

zmf_user
  User name to be used for authenticating with z/OSMF server.

  If *zmf_credential* is supplied, *zmf_user* is ignored.


  If *zmf_credential* is not supplied, *zmf_user* is required when *zmf_crt* and *zmf_key* are not supplied.


  If *zmf_credential* is not supplied and *zmf_crt* and *zmf_key* are supplied, *zmf_user* and *zmf_password* are ignored.


  | **required**: False
  | **type**: str


 

zmf_password
  Password to be used for authenticating with z/OSMF server.

  If *zmf_credential* is supplied, *zmf_password* is ignored.


  If *zmf_credential* is not supplied, *zmf_password* is required when *zmf_crt* and *zmf_key* are not supplied.


  If *zmf_credential* is not supplied and *zmf_crt* and *zmf_key* are supplied, *zmf_user* and *zmf_password* are ignored.


  | **required**: False
  | **type**: str


 

zmf_crt
  Location of the PEM-formatted certificate chain file to be used for HTTPS client authentication.


  If *zmf_credential* is supplied, *zmf_crt* is ignored.


  If *zmf_credential* is not supplied, *zmf_crt* is required when *zmf_user* and *zmf_password* are not supplied.


  | **required**: False
  | **type**: str


 

zmf_key
  Location of the PEM-formatted file with your private key to be used for HTTPS client authentication.


  If *zmf_credential* is supplied, *zmf_key* is ignored.


  If *zmf_credential* is not supplied, *zmf_key* is required when *zmf_user* and *zmf_password* are not supplied.


  | **required**: False
  | **type**: str


 

workflow_name
  Descriptive name of the workflow.

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
  Nickname of the system on which the specified workflow definition file and any related files reside.


  | **required**: False
  | **type**: str


 

workflow_vars_file
  Location of the optional properties file to be used to pre-specify the values of one or more variables that are defined in workflow definition file.


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
  Specifies how to handle variable conflicts if any are detected at workflow creation time.


  Such conflicts can be found when z/OSMF Workflows task reads the output file from a step that runs a REXX exec or UNIX shell script.


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
  URL to be used for notification when the workflow is started.

  | **required**: False
  | **type**: str


 

force_complete
  Specify whether to complete the workflow instance forcibly or idempotently.


  If *force_complete=true* (Forcibly), the role will delete the workflow instance if it exists in the z/OSMF server, then create a new workflow instance and start it on z/OS systems, periodically check the workflow status and return the final result when the workflow stops running.


  If *force_complete=false* (Idempotently), the role will create the workflow instance if it does not exist in the z/OSMF server, start the workflow on z/OS systems, and periodically check the workflow status and return the final result when the workflow stops running.


  | **required**: False
  | **type**: bool
  | **default**: False


 

complete_check_times
  The maximum number of time that is used for periodic checks of the workflow status.


  | **required**: False
  | **type**: int
  | **default**: 10


 

complete_check_delay
  The interval time (seconds) between periodic checks of the workflow status.


  | **required**: False
  | **type**: int
  | **default**: 5




Examples
--------

.. code-block:: yaml+jinja

   
   - name: sample of completing a z/OS workflow
     include_module:
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
   - Completing a z/OS workflow found on Ansible control node is currently not supported.





See Also
--------

.. seealso::
   - :ref:`zmf_workflow_module`





