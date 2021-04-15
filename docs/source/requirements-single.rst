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

Control node
============
The controller is where the Ansible engine that runs the playbook is installed.
Refer to RedHat Ansible Certified Content documentation for more on the
`controllers dependencies`_.

.. _controllers dependencies:
   https://ibm.github.io/z_ansible_collections_doc/requirements/requirements.html#control-node
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

Specific Requirements
---------------------

.. toctree::
   :maxdepth: 1
   :glob:

   requirements_workflow
   requirements_cpm


.. _z/OS:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3/en/homepage.html
.. _z/OS Management Facility:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3.izua300/abstract.html