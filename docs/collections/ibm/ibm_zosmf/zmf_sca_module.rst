.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module:

.. Anchors: short name for ansible.builtin

.. Title

ibm.ibm_zosmf.zmf_sca module -- Automate z/OS security requirements validation and provision
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `ibm.ibm_zosmf collection <https://galaxy.ansible.com/ui/repo/published/ibm/ibm_zosmf/>`_ (version 1.5.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install ibm.ibm\_zosmf`.

    To use it in a playbook, specify: :code:`ibm.ibm_zosmf.zmf_sca`.

.. version_added

.. rst-class:: ansible-version-added

New in ibm.ibm\_zosmf 1.1.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module supports automatically validating and provisioning security requirements/configuration based on the security descriptor JSON file.
- This module drives z/OSMF Security Configuration Assistant REST API undercover.


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
        <div class="ansibleOptionAnchor" id="parameter-expected_result"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-expected_result:

      .. rst-class:: ansible-option-title

      **expected_result**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-expected_result" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expected validation result of the security requirements.

      This parameter is ignored when :emphasis:`state=provisioned`

      For all\-passed, the module returns success when all security requirements are satisfied. If any requirement is not met or can not be determined, this module fails.

      For all\-failed, the module returns success when all security requirements have failed. If any requirement is satisfied or can not be determined, this module fails.

      The value "all\-passed" can be used in security validation use cases. The value "all\-failed" may be used in security auditing use cases to check if any over permission exists.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`"all\-failed"`
      - :ansible-option-choices-entry-default:`"all\-passed"` :ansible-option-choices-default-mark:`← (default)`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-location"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-location:

      .. rst-class:: ansible-option-title

      **location**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-location" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The location of path\_of\_security\_requirements.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"remote"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"local"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-path_of_security_requirements"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-path_of_security_requirements:

      .. rst-class:: ansible-option-title

      **path_of_security_requirements**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-path_of_security_requirements" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Absolute path of the security descriptor JSON file that contains the security requirements to be validated or provisioned.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-state"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-state:

      .. rst-class:: ansible-option-title

      **state**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The desired final state.

      If :emphasis:`state=check`\ , this module performs security validation for the security requirements specified in path\_of\_security\_requirements.

      If :emphasis:`state=provisioned`\ , this module performs security provision for the security requirements specified in path\_of\_security\_requirements.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"check"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"provisioned"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-target_userid"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-target_userid:

      .. rst-class:: ansible-option-title

      **target_userid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-target_userid" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      User ID or group ID to be validated or provisioned for the security requirements documented by the security descriptor JSON file that is specified by the parameter path\_of\_security\_requirements.

      If this parameter is not specified, the current logon user ID is used for validation or provision.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_credential"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-zmf_credential:

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

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-zmf_credential/jwt_token:

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

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-zmf_credential/ltpa_token_2:

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

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-zmf_credential/zmf_host:

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

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-zmf_credential/zmf_port:

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

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-zmf_crt:

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

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-zmf_host:

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

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-zmf_key:

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

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-zmf_password:

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

      Password to be used for authentication with z/OSMF server.

      If :emphasis:`zmf\_credential` is supplied, :emphasis:`zmf\_password` is ignored.

      If :emphasis:`zmf\_credential` is not supplied, :emphasis:`zmf\_password` is required when :emphasis:`zmf\_crt` and :emphasis:`zmf\_key` are not supplied.

      If :emphasis:`zmf\_credential` is not supplied and :emphasis:`zmf\_crt` and :emphasis:`zmf\_key` are supplied, :emphasis:`zmf\_user` and :emphasis:`zmf\_password` are ignored.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_port"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-zmf_port:

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

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__parameter-zmf_user:

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


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    - name: Authenticate with the z/OSMF server by username/password, and register the result for later use.
      zmf_authenticate:
        zmf_host: "{{ zmf_host }}"
        zmf_port: "{{ zmf_port }}"
        zmf_user: "{{ zmf_user }}"
        zmf_password: "{{ zmf_password }}"
      register: result_auth

    - name: Validate security requirements defined in a z/OS security descriptor file and \
            expect all requirements are satisfied.
      ibm.ibm_zosmf.zmf_sca:
        zmf_credential: "{{ result_auth }}"
        target_userid: IBMUSER
        path_of_security_requirements: /global/zosmf/sample/configuration/security/descriptor.json

    - name: Validate security requirements defined in a local (Ansible control node) security descriptor file\
            and expect no access to any items.
      ibm.ibm_zosmf.zmf_sca:
        zmf_credential: "{{ result_auth }}"
        target_userid: IBMUSER
        path_of_security_requirements: /home/user/descriptor.json
        location: local
        expected_result: all-failed

    - name: Provision security requirements defined in a z/OS security descriptor file and \
            expect all requirements are satisfied.
      ibm.ibm_zosmf.zmf_sca:
        zmf_credential: "{{ result_auth }}"
        state: provisioned
        target_userid: IBMUSER
        path_of_security_requirements: /global/zosmf/sample/configuration/security/descriptor.json

    - name: Provision resources defined in a local (Ansible control node) security descriptor file and \
            expect all requirements are satisfied.
      ibm.ibm_zosmf.zmf_sca:
        zmf_credential: "{{ result_auth }}"
        state: provisioned
        target_userid: IBMUSER
        path_of_security_requirements: /home/user/descriptor.json
        location: local



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

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-changed:

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

      Indicates whether any change is made during the module operation.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-msg"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-msg" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Error message.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always on error


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems:

      .. rst-class:: ansible-option-title

      **resourceItems**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Array of security requirements that need attention.

      If \`state=check\`, indicate security requirements which do not match with the expected result.

      If \`state=provisioned\`, indicate security requirements that are failed to provision.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always on fail


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/access"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/access:

      .. rst-class:: ansible-option-title

      **access**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/access" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Level of access that is required for the security resource for the specified user ID or group ID.

      Value can be the following


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"['READ', 'UPDATE', 'CONTROL', 'ALTER']"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/action"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/action:

      .. rst-class:: ansible-option-title

      **action**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/action" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      \\"validate\\" will be returned if SCA only did validation for this security requirement.

      \\"provision\\" will be returned if SCA provisioned the security requirement.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"['validate', 'provision']"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/actionObjectId"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/actionobjectid:

      .. rst-class:: ansible-option-title

      **actionObjectId**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/actionObjectId" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The object ID of this action. For validation action, this ID is the same as validatedId below.

      This field can also be used for other actions in future versions.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`""`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/additionalInfo"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/additionalinfo:

      .. rst-class:: ansible-option-title

      **additionalInfo**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/additionalInfo" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Additional info.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`""`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/httpStatus"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/httpstatus:

      .. rst-class:: ansible-option-title

      **httpStatus**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/httpStatus" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      http status code if error.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on error

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`""`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/itemCategory"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/itemcategory:

      .. rst-class:: ansible-option-title

      **itemCategory**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/itemCategory" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Item category.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"CHANGEDATASET VX"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/itemDescription"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/itemdescription:

      .. rst-class:: ansible-option-title

      **itemDescription**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/itemDescription" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Item description.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"DFSMSrmm inventory management CHANGEDATASET VX command protection."`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/itemId"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/itemid:

      .. rst-class:: ansible-option-title

      **itemId**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/itemId" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Item ID.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"5695DF18658I10001000"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/itemType"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/itemtype:

      .. rst-class:: ansible-option-title

      **itemType**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/itemType" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Item type.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"PROGRAMMABLE"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/messageId"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/messageid:

      .. rst-class:: ansible-option-title

      **messageId**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/messageId" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Message Id.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`""`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/messageText"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/messagetext:

      .. rst-class:: ansible-option-title

      **messageText**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/messageText" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Message text.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`""`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/requestMethod"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/requestmethod:

      .. rst-class:: ansible-option-title

      **requestMethod**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/requestMethod" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      http request method if error.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on error

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`""`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/requestUri"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/requesturi:

      .. rst-class:: ansible-option-title

      **requestUri**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/requestUri" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Request uri if error.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on error

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`""`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/resourceClass"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/resourceclass:

      .. rst-class:: ansible-option-title

      **resourceClass**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/resourceClass" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      SAF resource class.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"FACILITY"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/resourceProfile"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/resourceprofile:

      .. rst-class:: ansible-option-title

      **resourceProfile**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/resourceProfile" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Name of the security resource profile.

      At current stage,

      Variable in the name is not supported.

      Generic resource name is not supported.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"STGADMIN.EDG.CD.VX"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/status"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/status:

      .. rst-class:: ansible-option-title

      **status**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/status" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Validation result


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"['Passed', 'Failed', 'Unknown']"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/validatedId"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/validatedid:

      .. rst-class:: ansible-option-title

      **validatedId**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/validatedId" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      User ID or group ID that is used for resource validation.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`""`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-resourceItems/whoNeedsAccess"></div>

      .. raw:: latex

        \hspace{0.02\textwidth}\begin{minipage}[t]{0.3\textwidth}

      .. _ansible_collections.ibm.ibm_zosmf.zmf_sca_module__return-resourceitems/whoneedsaccess:

      .. rst-class:: ansible-option-title

      **whoNeedsAccess**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-resourceItems/whoNeedsAccess" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

      .. raw:: latex

        \end{minipage}

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Users (security groups) who require access to this resource.

      The Security Configuration Assistant does not verify that security groups are defined;

      your security administrator must verify that the groups exist.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"\<Inventory Management\>"`


      .. raw:: html

        </div>




..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Xiao Ming Liu (@EricLiuAtIbm)
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
