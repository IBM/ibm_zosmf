.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. meta::
  :antsibull-docs: 2.24.0

.. Anchors

.. _ansible_collections.ibm.ibm_zosmf.zmf_authenticate_module:

.. Anchors: short name for ansible.builtin

.. Title

ibm.ibm_zosmf.zmf_authenticate module -- Authenticate with z/OSMF server
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `ibm.ibm_zosmf collection <https://galaxy.ansible.com/ui/repo/published/ibm/ibm_zosmf/>`_ (version 1.5.0).

    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible\-galaxy collection install ibm.ibm\_zosmf`.

    To use it in a playbook, specify: :code:`ibm.ibm_zosmf.zmf_authenticate`.

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

- Authenticate with z/OSMF server by either username/password or HTTPS client authenticate.
- Return the authentication credentials for successful authentication.
- The credential can be then used for succeeding Ansible tasks which call z/OSMF Ansible module or role.


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
        <div class="ansibleOptionAnchor" id="parameter-zmf_crt"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_authenticate_module__parameter-zmf_crt:

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

      Required when :emphasis:`zmf\_user` and :emphasis:`zmf\_password` are not supplied.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_host"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_authenticate_module__parameter-zmf_host:

      .. rst-class:: ansible-option-title

      **zmf_host**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-zmf_host" title="Permalink to this option"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Hostname of the z/OSMF server.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_key"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_authenticate_module__parameter-zmf_key:

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

      Required when :emphasis:`zmf\_user` and :emphasis:`zmf\_password` are not supplied.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_password"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_authenticate_module__parameter-zmf_password:

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

      Required when :emphasis:`zmf\_crt` and :emphasis:`zmf\_key` are not supplied.

      If :emphasis:`zmf\_crt` and :emphasis:`zmf\_key` are supplied, :emphasis:`zmf\_user` and :emphasis:`zmf\_password` are ignored.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_port"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_authenticate_module__parameter-zmf_port:

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


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zmf_user"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_authenticate_module__parameter-zmf_user:

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

      Required when :emphasis:`zmf\_crt` and :emphasis:`zmf\_key` are not supplied.

      If :emphasis:`zmf\_crt` and :emphasis:`zmf\_key` are supplied, :emphasis:`zmf\_user` and :emphasis:`zmf\_password` are ignored.


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    - name: Authenticate with z/OSMF server by username/password
      zmf_authenticate:
        zmf_host: "sample.ibm.com"
        zmf_user: "your_username"
        zmf_password: "your_password"

    - name: Authenticate with z/OSMF server by HTTPS client authenticate
      zmf_authenticate:
        zmf_host: "sample.ibm.com"
        zmf_crt: "/file_with_your_certificate_chain.crt"
        zmf_key: "/file_with_your_private_key.key"

    - name: Authenticate with z/OSMF server by prompting to input username/password
      vars_prompt:
        - name: zmf_user
          prompt: "Enter your zOSMF username"
          private: false
        - name: zmf_password
          prompt: "Enter your zOSMF password"
          private: true
      tasks:
        - zmf_authenticate:
            zmf_host: "{{ zmf_host }}"
            zmf_port: "{{ zmf_port }}"
            zmf_user: "{{ zmf_user }}"
            zmf_password: "{{ zmf_password }}"



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

      .. _ansible_collections.ibm.ibm_zosmf.zmf_authenticate_module__return-changed:

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


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-jwt_token"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_authenticate_module__return-jwt_token:

      .. rst-class:: ansible-option-title

      **jwt_token**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-jwt_token" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The value of JSON Web token, which supports strong encryption.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlmVhcmVyIiwicie......"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-ltpa_token_2"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_authenticate_module__return-ltpa_token_2:

      .. rst-class:: ansible-option-title

      **ltpa_token_2**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-ltpa_token_2" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The value of Lightweight Third Party Access (LTPA) token, which supports strong encryption.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"yDS7uJxqrd3h8v5WXq9pf1yPtztQ4JzroZN3XQKF26ZicXgHc7mdzgycMCa......"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-zmf_host"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_authenticate_module__return-zmf_host:

      .. rst-class:: ansible-option-title

      **zmf_host**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-zmf_host" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Hostname of the z/OSMF server.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-zmf_port"></div>

      .. _ansible_collections.ibm.ibm_zosmf.zmf_authenticate_module__return-zmf_port:

      .. rst-class:: ansible-option-title

      **zmf_port**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-zmf_port" title="Permalink to this return value"></a>

      .. ansible-option-type-line::

        :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Port number of the z/OSMF server.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` on success


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
