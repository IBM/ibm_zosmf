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

When using the **IBM z/OS Management Facility (z/OSMF) collection**, there
could be additional requirements for the control node.
Please see details of dependency below:

* `Requests library for Python`_: 2.23 or later (Optional)
   
   This dependency is only required for using the following roles or modules:

   * module: `zmf_workflow`_
   * role: `zmf_workflow_complete`_
   * module: `zmf_sca`_


.. _Requests library for Python:
   https://requests.readthedocs.io/en/latest/
.. _zmf_workflow:
   modules/zmf_workflow.html
.. _zmf_workflow_complete:
   roles/zmf_workflow_complete.html
.. _zmf_sca:
   modules/zmf_sca.html
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
   The z/OSMF collection drives z/OSMF REST APIs remotely by default.
   This is done by specifying ``delegate_to: localhost`` statement in your
   playbook or roles in this collection.
   With this remote approach, it is not necessary to set up SSH and install
   Python on the target z/OS systems. 

* `z/OSMF server`_

   The z/OSMF server must be installed and active on **at least one** z/OS
   system in the same sysplex.
   Information about the z/OSMF server must be configured in the inventory
   file or in the ``vars`` file, such as the hostname, port number, and
   authentication info.
   The authentication info to connect to the z/OSMF server is provided when
   running playbook or it will be prompted during playbook run.
   You can specify the same z/OSMF server for multiple z/OS managed nodes in
   the same sysplex.

* `z/OSMF Workflow`_
   
   z/OSMF Workflow is a plugin of z/OSMF which provides a framework to
   streamline z/OS tasks.
   To interact with z/OSMF Workflow in your playbook, it requires you to
   setup z/OSMF Workflow properly in z/OS managed nodes.
   Typically, you setup z/OSMF Workflow as a plugin of one z/OSMF server in
   each sysplex. 

   This dependency is only required for using the following roles or modules:

   * module: `zmf_workflow`_
   * role: `zmf_workflow_complete`_
   * role: `zmf_cpm_provision_software_service`_
   * role: `zmf_cpm_manage_software_instance`_
   * role: `zmf_cpm_remove_software_instance`_

* `Cloud Provisioning and Management`_ (Optional)

   Cloud Provisioning and Management (CP&M) can be used to provision and
   Manage z/OS Software Instances.
   To interact with CP&M in your playbook, it requires you to set up CP&M
   properly in z/OS managed nodes.
   Typically, you setup CP&M as a plugin of one z/OSMF server in each sysplex.
   
   This dependency is only required for using the following roles or modules:

   * role: `zmf_cpm_provision_software_service`_
   * role: `zmf_cpm_manage_software_instance`_
   * role: `zmf_cpm_remove_software_instance`_

* `z/OSMF SCA`_

   z/OSMF SCA is a plugin of z/OSMF which supports json format of security descriptor file.
   This file can be used to document security requirements by function or product.
   With the security descriptor file which is easy to create,
   SCA is able to display and automatically validate security requirements in a flexible granularity,
   either by individual requirement, by function or by product. SCA is based on SAF interface,
   therefore, supports all SAF based security products in most cases.

   To interact with z/OSMF SCA in your playbook, it requires you to
   setup z/OSMF SCA properly in z/OS managed nodes.

   This dependency is only required for using the following module:

   * module: `zmf_sca`_

.. _z/OS:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3/en/homepage.html
.. _z/OSMF server:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3.izua300/abstract.html
.. _z/OSMF Workflow:
   https://www.ibm.com/docs/en/zos/2.4.0?topic=services-configure-zosmf-workflows-task
.. _Cloud Provisioning and Management:
   https://www.ibm.com/support/z-content-solutions/cloud-provisioning
.. _zmf_workflow:
   modules/zmf_workflow.html
.. _zmf_workflow_complete:
   roles/zmf_workflow_complete.html
.. _zmf_cpm_provision_software_service:
   roles/zmf_cpm_provision_software_service.html
.. _zmf_cpm_manage_software_instance:
   roles/zmf_cpm_manage_software_instance.html
.. _zmf_cpm_remove_software_instance:
   roles/zmf_cpm_remove_software_instance.html
.. _z/OSMF SCA:
   https://www.ibm.com/docs/en/zos/2.4.0?topic=services-configure-zosmf-workflows-task
.. _zmf_sca:
   modules/zmf_sca.html