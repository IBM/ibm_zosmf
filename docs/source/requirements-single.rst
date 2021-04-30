.. ...........................................................................
.. Auto generated restructured text                                          .
.. ...........................................................................
.. ...........................................................................
.. Auto generated restructured text                                          .
.. ...........................................................................
.. ...........................................................................
.. © Copyright IBM Corporation 2021                                          .
.. ...........................................................................

============
Requirements
============

The **IBM z/OSMF collection** requires both a **control node** and
**managed node** be configured with a minimum set of requirements.
The control node is often referred to as the **controller** and the managed
node as the **host** or **target**.

Refer to RedHat Ansible Certified Content documentation for more on the
`controllers dependencies`_.

.. _controllers dependencies:
   https://ibm.github.io/z_ansible_collections_doc/requirements/requirements.html#control-node
.. ...........................................................................
.. © Copyright IBM Corporation 2021                                          .
.. ...........................................................................

Control node
============

A control node is any machine with Ansible® installed.
From the control node, you can run commands and playbooks from a laptop,
desktop, or server.
However, Windows® is not a supported controller for Ansible collections
managing a z/OS node.

All IBM z/OS collections require these versions of software:

* `Ansible`_: 2.9 or later
* `Python`_: 2.7 or later

Specific Requirements - Operate z/OS Workflows
----------------------------------------------

Interacting with **z/OSMF Workflows** in your playbook requires that you
meet the software requirements.
Besides meeting the requirements above, you must ensure that the required
software is installed on the control node, as follows:

* `Requests library for Python`_: 2.23 or later

   It is required when using:

   * module: `zmf_workflow`_
   * role: `zmf_workflow_complete`_


.. _Ansible:
   https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
.. _Python:
   https://www.python.org
.. _Requests library for Python:
   https://requests.readthedocs.io/en/latest/
.. _zmf_workflow:
   modules/zmf_workflow.html
.. _zmf_workflow_complete:
   roles/zmf_workflow_complete.html
.. ...........................................................................
.. © Copyright IBM Corporation 2021                                          .
.. ...........................................................................

Managed node
============

The managed z/OS node is the host that is managed by Ansible, as identified in
the Ansible inventory.
The managed node has dependencies that are specific to each release of the
**IBM z/OSMF collection**.
Review the details of the dependencies before you proceed to install the
**IBM z/OSMF collection**.

* `z/OS`_: V2R3 or later

   The target z/OS systems should be configured as the target hosts
   (managed nodes) in your playbook.
   It is not necessary to set up an SSH connection and install Python on the
   target z/OS systems.
   Instead, the modules and roles in this collection will create HTTPS
   connections with the z/OSMF server.
   Therefore ``delegate_to: localhost`` statement is required for using the
   modules in your playbook task.
   This statement is hard-coded within the roles.

* `z/OS Management Facility`_: V2R3 or later

   The z/OSMF server must be installed and active on **at least one** z/OS
   system in the same sysplex.
   Information about the z/OSMF server must be configured in the inventory
   file or in the ``vars`` file, such as the hostname, port number, and
   authentication info.
   The authentication info to connect to the z/OSMF server is provided when
   running playbook or it will be prompted during playbook run.

Specific Requirements - Provision and Manage z/OS Software Instances
--------------------------------------------------------------------

Interacting with **Cloud Provisioning & Management (CP&M)** in your playbook
requires that you meet the software requirements.
Besides meeting the requirements above, you must ensure that the required
software is installed on the managed nodes, as follows:

* `z/OS Management Facility`_: V2R3 or later

   The z/OSMF server must be installed and active on **each** managed z/OS
   system.

   It is required for using the following roles:

   * role: `zmf_cpm_provision_software_service`_
   * role: `zmf_cpm_manage_software_instance`_
   * role: `zmf_cpm_remove_software_instance`_

* `Cloud Provisioning and Management`_:

   It is required for using the following roles:

   * role: `zmf_cpm_provision_software_service`_
   * role: `zmf_cpm_manage_software_instance`_
   * role: `zmf_cpm_remove_software_instance`_


.. _z/OS:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3/en/homepage.html
.. _z/OS Management Facility:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3.izua300/abstract.html
.. _Cloud Provisioning and Management:
   https://www.ibm.com/support/z-content-solutions/cloud-provisioning
.. _zmf_cpm_provision_software_service:
   roles/zmf_cpm_provision_software_service.html
.. _zmf_cpm_manage_software_instance:
   roles/zmf_cpm_manage_software_instance.html
.. _zmf_cpm_remove_software_instance:
   roles/zmf_cpm_remove_software_instance.html