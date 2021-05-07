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