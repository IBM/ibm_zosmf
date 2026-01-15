.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module:

.. Anchors: short name for ansible.builtin

.. Title

ibm.ibm_zosmf.zmf_workflow module -- Operate z/OS workflows
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `ibm.ibm_zosmf collection <https://galaxy.ansible.com/ui/repo/published/ibm/ibm_zosmf/>`_ (version 1.5.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install ibm.ibm\_zosmf`.

    To use it in a playbook, specify: :code:`ibm.ibm_zosmf.zmf_workflow`.

.. version_added

.. rst-class:: ansible-version-added

New in ibm.ibm\_zosmf 1.0.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Operate z/OS workflows through the use of z/OSMF workflow REST services.
- This module supports to compare, start, delete, and check the status of a workflow.


.. Aliases


.. Requirements






.. Options

Parameters
----------

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The desired final state for the specified workflow.

      If :emphasis:`state=existed`\ , checks whether a workflow instance exists or not.
      \- If only :emphasis:`workflow\_name` is specified, the module looks for a workflow instance with same name.
      \- If :emphasis:`workflow\_file`\ , :emphasis:`workflow\_vars`\ , :emphasis:`workflow\_vars\_file` are also specified,
      the module not only looks for workflow instance with same name,
      but also validates if content of workflow definition and variables are consistent.

      If :emphasis:`state=started`\ , starts the workflow instance.
      \- If :emphasis:`workflow\_key` is specified, finds the workflow instance and starts it.
      \- If :emphasis:`workflow\_key` is not specified, checks if workflow exists by :emphasis:`workflow\_name`\ :
      \- If exists, starts the workflow instance.
      \- If not exist, creates a new workflow instance and starts it.

      If :emphasis:`state=deleted`\ , delete a workflow instance if it exists.
      \- If :emphasis:`workflow\_key` is specified, delete the workflow instance.
      \- If :emphasis:`workflow\_key` is not specified, checks if workflow exists by :emphasis:`workflow\_name`
      and delete the workflow instance if it exists.

      If :emphasis:`state=check`\ , check the status of a workflow.
      \- If the status of the workflow is 'automation\-in\-progress', return message:
      \- Workflow instance with key:{} is still in progress. Current step is: {}. Percent complete is xx%.
      \- If the status of the workflow is 'complete', return message:
      \- Workflow instance with key:{} is is completed.
      \- If the status of the workflow is not 'automation\-in\-progress' or 'complete', return message:
      \- Workflow instance with key:{} is not completed. No step is started.
      \- Workflow instance with key:{} is not completed. Failed step is: {}.
      You can manually complete this step in z/OSMF Workflows task,
      and start this workflow instance again with next step name: {}
      specified in argument: workflow\_step\_name.
      \- Workflow instance with key:{} is not completed.
      Failed step is: {}. While one or more steps may be skipped.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"existed"`
      - :ansible-option-choices-entry:`"started"`
      - :ansible-option-choices-entry:`"deleted"`
      - :ansible-option-choices-entry:`"check"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_access_type"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_access_type:

      .. rst-class:: ansible-option-title

      **workflow_access_type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_access_type" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Access type for the workflow when the workflow is created.

      The access type determines which users can view the workflow steps and edit the step notes.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"Public"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"Restricted"`
      - :ansible-option-choices-entry:`"Private"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_account_info"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_account_info:

      .. rst-class:: ansible-option-title

      **workflow_account_info**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_account_info" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      For a workflow step that submits a batch job, this variable specifies the account information for the JCL JOB statement.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_assign_to_owner"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_assign_to_owner:

      .. rst-class:: ansible-option-title

      **workflow_assign_to_owner**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_assign_to_owner" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specifies whether the workflow steps are assigned to the workflow owner when the workflow is created.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_category"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_category:

      .. rst-class:: ansible-option-title

      **workflow_category**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_category" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Category of the workflow, which is general or configuration.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"general"`
      - :ansible-option-choices-entry:`"configuration"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_comments"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_comments:

      .. rst-class:: ansible-option-title

      **workflow_comments**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_comments" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User\-specified information to be associated with the workflow at creation time.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_delete_completed_jobs"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_delete_completed_jobs:

      .. rst-class:: ansible-option-title

      **workflow_delete_completed_jobs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_delete_completed_jobs" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      For a workflow that submits a batch job, this variable specifies whether the job is deleted from the JES spool after it completes.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_file"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_file:

      .. rst-class:: ansible-option-title

      **workflow_file**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_file" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Location of the workflow definition file.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_file_system"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_file_system:

      .. rst-class:: ansible-option-title

      **workflow_file_system**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_file_system" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Nickname of the system on which the specified workflow definition file and any related files reside.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_host"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_host:

      .. rst-class:: ansible-option-title

      **workflow_host**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_host" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Nickname of the target z/OS system on which the workflow is to be performed.

      This variable should be specified as :literal:`{{ inventory\_hostname }}`. Its value should be specified in the inventory file as a managed node.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_job_statement"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_job_statement:

      .. rst-class:: ansible-option-title

      **workflow_job_statement**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_job_statement" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      For a workflow that submits a batch job, this variable specifies the JOB statement JCL for the job.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_key"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_key:

      .. rst-class:: ansible-option-title

      **workflow_key**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_key" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A string value, generated by z/OSMF to uniquely identify the workflow instance.

      Either :emphasis:`workflow\_name` or :emphasis:`workflow\_key` is required when :emphasis:`state=started/deleted/check`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_name"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_name:

      .. rst-class:: ansible-option-title

      **workflow_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Descriptive name of the workflow.

      The workflow name is case insensitive, for example, :literal:`MyWorkflow` and :literal:`MYWORKFLOW` are the same workflow.

      It is recommended that you use the naming rule :literal:`ansible\_workflowName\_{{ workflow\_host }}` when :emphasis:`state=started`.

      Required when :emphasis:`state=existed`.

      Either :emphasis:`workflow\_name` or :emphasis:`workflow\_key` is required when :emphasis:`state=started/deleted/check`.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_notification_url"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_notification_url:

      .. rst-class:: ansible-option-title

      **workflow_notification_url**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_notification_url" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      URL to be used for receiving notifications when the workflow is started.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_owner"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_owner:

      .. rst-class:: ansible-option-title

      **workflow_owner**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_owner" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User name of the workflow owner.

      If this value is omitted, :emphasis:`zmf\_user` is used as workflow owner.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_perform_subsequent"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_perform_subsequent:

      .. rst-class:: ansible-option-title

      **workflow_perform_subsequent**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_perform_subsequent" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specifies whether the subsequent automated steps are performed when the workflow is started.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry-default:`true` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_resolve_conflict_by_using"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_resolve_conflict_by_using:

      .. rst-class:: ansible-option-title

      **workflow_resolve_conflict_by_using**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_resolve_conflict_by_using" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Specifies how to handle variable conflicts if any are detected at workflow creation time.

      Such conflicts can be found when z/OSMF Workflows task reads the output file from a step that runs a REXX exec or UNIX shell script.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"outputFileValue"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"existingValue"`
      - :ansible-option-choices-entry:`"leaveConflict"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_resolve_global_conflict_by_using"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_resolve_global_conflict_by_using:

      .. rst-class:: ansible-option-title

      **workflow_resolve_global_conflict_by_using**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_resolve_global_conflict_by_using" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Version of the variable to be used if the supplied workflow variable conflicts with an existing global variable in z/OSMF Workflows task.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"global"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"input"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_step_name"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_step_name:

      .. rst-class:: ansible-option-title

      **workflow_step_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_step_name" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the workflow step at which automation processing is to begin when the workflow is started.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_vars"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_vars:

      .. rst-class:: ansible-option-title

      **workflow_vars**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_vars" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Values of one or more workflow variables in JSON format.

      For example, :literal:`{"user\_to\_list": "DEBUG1", "tsocmd\_to\_issue": "TIME"}`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_vars_file"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_vars_file:

      .. rst-class:: ansible-option-title

      **workflow_vars_file**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_vars_file" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Location of the optional properties file to be used to pre\-specify the values of one or more variables that are defined in workflow definition file.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-workflow_vendor"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-workflow_vendor:

      .. rst-class:: ansible-option-title

      **workflow_vendor**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-workflow_vendor" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Name of the vendor that provided the workflow definition file.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_credential"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-zmf_credential:

      .. rst-class:: ansible-option-title

      **zmf_credential**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-zmf_credential" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Authentication credentials, returned by module :strong:`zmf\_authenticate`\ , for successful authentication with the z/OSMF server.

      If :emphasis:`zmf\_credential` is supplied, :emphasis:`zmf\_host`\ , :emphasis:`zmf\_port`\ , :emphasis:`zmf\_user`\ , :emphasis:`zmf\_password`\ , :emphasis:`zmf\_crt` and :emphasis:`zmf\_key` are ignored.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_credential/jwt_token"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-zmf_credential/jwt_token:

      .. rst-class:: ansible-option-title

      **jwt_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-zmf_credential/jwt_token" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The value of the JSON web token, which supports strong encryption.

      If :emphasis:`ltpa\_token\_2` is not supplied, :emphasis:`jwt\_token` is required.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_credential/ltpa_token_2"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-zmf_credential/ltpa_token_2:

      .. rst-class:: ansible-option-title

      **ltpa_token_2**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-zmf_credential/ltpa_token_2" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The value of the Lightweight Third Party Access (LTPA) token, which supports strong encryption.

      If :emphasis:`jwt\_token` is not supplied, :emphasis:`ltpa\_token\_2` is required.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_credential/zmf_host"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-zmf_credential/zmf_host:

      .. rst-class:: ansible-option-title

      **zmf_host**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-zmf_credential/zmf_host" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Hostname of the z/OSMF server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_credential/zmf_port"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-zmf_credential/zmf_port:

      .. rst-class:: ansible-option-title

      **zmf_port**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-zmf_credential/zmf_port" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Port number of the z/OSMF server.


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_crt"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-zmf_crt:

      .. rst-class:: ansible-option-title

      **zmf_crt**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-zmf_crt" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Location of the PEM\-formatted certificate chain file to be used for HTTPS client authentication.

      If :emphasis:`zmf\_credential` is supplied, :emphasis:`zmf\_crt` is ignored.

      If :emphasis:`zmf\_credential` is not supplied, :emphasis:`zmf\_crt` is required when :emphasis:`zmf\_user` and :emphasis:`zmf\_password` are not supplied.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_host"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-zmf_host:

      .. rst-class:: ansible-option-title

      **zmf_host**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-zmf_host" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Hostname of the z/OSMF server.

      If :emphasis:`zmf\_credential` is supplied, :emphasis:`zmf\_host` is ignored.

      If :emphasis:`zmf\_credential` is not supplied, :emphasis:`zmf\_host` is required.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_key"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-zmf_key:

      .. rst-class:: ansible-option-title

      **zmf_key**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-zmf_key" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Location of the PEM\-formatted file with your private key to be used for HTTPS client authentication.

      If :emphasis:`zmf\_credential` is supplied, :emphasis:`zmf\_key` is ignored.

      If :emphasis:`zmf\_credential` is not supplied, :emphasis:`zmf\_key` is required when :emphasis:`zmf\_user` and :emphasis:`zmf\_password` are not supplied.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_password"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-zmf_password:

      .. rst-class:: ansible-option-title

      **zmf_password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-zmf_password" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Password to be used for authenticating with z/OSMF server.

      If :emphasis:`zmf\_credential` is supplied, :emphasis:`zmf\_password` is ignored.

      If :emphasis:`zmf\_credential` is not supplied, :emphasis:`zmf\_password` is required when :emphasis:`zmf\_crt` and :emphasis:`zmf\_key` are not supplied.

      If :emphasis:`zmf\_credential` is not supplied and :emphasis:`zmf\_crt` and :emphasis:`zmf\_key` are supplied, :emphasis:`zmf\_user` and :emphasis:`zmf\_password` are ignored.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_port"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-zmf_port:

      .. rst-class:: ansible-option-title

      **zmf_port**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-zmf_port" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Port number of the z/OSMF server.

      If :emphasis:`zmf\_credential` is supplied, :emphasis:`zmf\_port` is ignored.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_user"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__parameter-zmf_user:

      .. rst-class:: ansible-option-title

      **zmf_user**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-zmf_user" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User name to be used for authenticating with z/OSMF server.

      If :emphasis:`zmf\_credential` is supplied, :emphasis:`zmf\_user` is ignored.

      If :emphasis:`zmf\_credential` is not supplied, :emphasis:`zmf\_user` is required when :emphasis:`zmf\_crt` and :emphasis:`zmf\_key` are not supplied.

      If :emphasis:`zmf\_credential` is not supplied and :emphasis:`zmf\_crt` and :emphasis:`zmf\_key` are supplied, :emphasis:`zmf\_user` and :emphasis:`zmf\_password` are ignored.


      .. raw:: html

        </div>


.. Attributes


.. Notes

Notes
-----

.. note::
   - Submitting a z/OSMF workflow found on Ansible control node is currently not supported.
   - Only automated steps are supported when starting a z/OSMF workflow.
   - This module is considered to be "weakly" idempotent. That is, this module achieves an idempotent result for the final state of the workflow instance, rather than for the target z/OS systems. A strong idempotent result for the final state of the target z/OS systems depends on the idempotency of the workflow instance steps.
   - This module does not support check mode.

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    - name: Authenticate with z/OSMF server by username/password, and register the result for later use.
      zmf_authenticate:
        zmf_host: "{{ zmf_host }}"
        zmf_port: "{{ zmf_port }}"
        zmf_user: "{{ zmf_user }}"
        zmf_password: "{{ zmf_password }}"
      register: result_auth

    - name: Compare whether a workflow with the given name already exists
      ibm.ibm_zosmf.zmf_workflow:
        state: "existed"
        zmf_credential: "{{ result_auth }}"
        workflow_name: "ansible_sample_workflow_SY1"
        workflow_file: "/zosmf/workflow_def/workflow_sample_automation_steps.xml"
        workflow_host: "SY1"

    - name: Create a workflow if it does not exist, and start it
      ibm.ibm_zosmf.zmf_workflow:
        state: "started"
        zmf_credential: "{{ result_auth }}"
        workflow_name: "ansible_sample_workflow_{{ inventory_hostname }}"
        workflow_file: "/zosmf/workflow_def/workflow_sample_automation_steps.xml"
        workflow_host: "{{ inventory_hostname }}"

    - name: Start the existing workflow from the specified step `workflow_step_name`
      ibm.ibm_zosmf.zmf_workflow:
        state: "started"
        zmf_credential: "{{ result_auth }}"
        workflow_name: "ansible_sample_workflow_{{ inventory_hostname }}"
        workflow_step_name: "StepName"

    - name: Delete a workflow if it exists
      ibm.ibm_zosmf.zmf_workflow:
        state: "deleted"
        zmf_credential: "{{ result_auth }}"
        workflow_name: "ansible_sample_workflow_SY1"

    - name: Check the status of a workflow
      ibm.ibm_zosmf.zmf_workflow:
        state: "check"
        zmf_credential: "{{ result_auth }}"
        workflow_name: "ansible_sample_workflow_SY1"



.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. tabularcolumns:: \X{1}{3}\X{2}{3}

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1
  :class: longtable ansible-option-table

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-changed"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__return-changed:

      .. rst-class:: ansible-option-title

      **changed**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-changed" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indicates if any change is made during the module operation.

      If \`state=existed/check\`, always return false.

      If \`state=started\` and the workflow is started, return true.

      If \`state=deleted\` and the workflow is deleted, return true.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-deleted"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__return-deleted:

      .. rst-class:: ansible-option-title

      **deleted**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-deleted" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indicate whether the workflow is deleted.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success when \`state=deleted\`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-message"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__return-message:

      .. rst-class:: ansible-option-title

      **message**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-message" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The output message generated by the module.

      If \`state=existed\`, indicate whether a workflow with the given name does not exist, or exists with same or different definition file, variables and properties.

      If \`state=started\`, indicate whether the workflow is started.

      If \`state=deleted\`, indicate whether the workflow to be deleted does not exist or is deleted.

      If \`state=check\`, indicate whether the workflow is completed, is not completed, or is still in progress.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"{'sample1': 'Workflow instance named: ansible\_sample\_workflow\_SY1 with same definition file, variables and properties is found.', 'sample10': 'Workflow instance named: ansible\_sample\_workflow\_SY1 is deleted.', 'sample11': 'Workflow instance named: ansible\_sample\_workflow\_SY1 does not exist.', 'sample2': 'Workflow instance named: ansible\_sample\_workflow\_SY1 with different definition file is found.', 'sample3': 'Workflow instance named: ansible\_sample\_workflow\_SY1 is found. While it could not be compared since the argument: workflow\_file is required, and please supply variables by the argument: workflow\_vars rather than the argument:  workflow\_vars\_file.\\"', 'sample4': 'Workflow instance named: ansible\_sample\_workflow\_SY1 is started, you can use state=check to check its final status.', 'sample5': 'Workflow instance named: ansible\_sample\_workflow\_SY1 is still in progress. Current step is: 1.2 Step title. Percent complete is 28%.', 'sample6': 'Workflow instance named: ansible\_sample\_workflow\_SY1 is completed.', 'sample7': 'Workflow instance named: ansible\_sample\_workflow\_SY1 is not completed. No step is started.', 'sample8': 'Workflow instance named: ansible\_sample\_workflow\_SY1 is not completed. Failed step is: 1.2 Step title. IZUWF0145E: Automation processing for the workflow \`ansible\_sample\_workflow\_SY1\` stopped at step \`Step title\`. This step cannot be performed automatically. You can manually complete this step in z/OSMF Workflows task, and start this workflow instance again with next step name: subStep3 specified in argument: workflow\_step\_name.', 'sample9': 'Workflow instance named: ansible\_sample\_workflow\_SY1 is not completed. Failed step is: 1.2 Step title. IZUWF0162I: Automation processing for workflow \`ansible\_sample\_workflow\_SY1\` is complete. While one or more steps may be skipped.'}"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-same_workflow_instance"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__return-same_workflow_instance:

      .. rst-class:: ansible-option-title

      **same_workflow_instance**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-same_workflow_instance" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indicate whether the existing workflow has the same or different definition file, variables and properties.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success when \`state=existed\`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-workflow_completed"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__return-workflow_completed:

      .. rst-class:: ansible-option-title

      **workflow_completed**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-workflow_completed" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indicate whether the workflow is completed. Return True if the status of the workflow is 'complete'. Otherwise, return False.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success when \`state=existed/check\`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-workflow_failed_step"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__return-workflow_failed_step:

      .. rst-class:: ansible-option-title

      **workflow_failed_step**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-workflow_failed_step" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indicate what the failed step is if the workflow is not completed, including the step number, step name and step title.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success when \`state=check\`

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"step\_name": "createInstanceDirectory", "step\_number": "1.2", "step\_title": "Create a new instance directory"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-workflow_key"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__return-workflow_key:

      .. rst-class:: ansible-option-title

      **workflow_key**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-workflow_key" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Generated key to uniquely identify the existing or started workflow.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success when \`state=existed/started/check/deleted\`

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"2535b19e\-a8c3\-4a52\-9d77\-e30bb920f912"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-workflow_name"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__return-workflow_name:

      .. rst-class:: ansible-option-title

      **workflow_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-workflow_name" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Descriptive name of the workflow.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success when \`state=existed/started/check/deleted\`

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"ansible\_sample\_workflow\_SY1"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-workflow_waiting"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_workflow_module__return-workflow_waiting:

      .. rst-class:: ansible-option-title

      **workflow_waiting**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-workflow_waiting" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Indicate whether it needs to wait and check again because the workflow is still in progress. Return True if the status of the workflow is 'automation\-in\-progress'. Otherwise (the workflow is either completed or paused/failed at some step), return False.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success when \`state=check\`


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Yang Cao (@zosmf-Young)
- Yun Juan Yang (@zosmf-Robyn)


.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. ansible-links::

  - title: "Issue Tracker"
    url: "https://github.com/IBM/ibm_zosmf/issues"
    external: true
  - title: "Repository (Sources)"
    url: "https://github.com/IBM/ibm_zosmf"
    external: true


.. Parsing errors
