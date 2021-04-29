.. ...........................................................................
.. © Copyright IBM Corporation 2021                                          .
.. ...........................................................................

Provision and Manage z/OS Software Instances
============================================

Interacting with **Cloud Provisioning & Management (CP&M)** in your playbook
requires that you meet the software requirements.
Besides meeting the `Overall Requirements`_, you must ensure that the required
software is installed on the nodes, as follows:

**Managed Node**:

* `z/OS Management Facility`_: V02.03.00 or later

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


.. _Overall Requirements:
   requirements-single.html
.. _zmf_cpm_provision_software_service:
   roles/zmf_cpm_provision_software_service.html
.. _zmf_cpm_manage_software_instance:
   roles/zmf_cpm_manage_software_instance.html
.. _zmf_cpm_remove_software_instance:
   roles/zmf_cpm_remove_software_instance.html
.. _z/OS Management Facility:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3.izua300/abstract.html
.. _Cloud Provisioning and Management:
   https://www.ibm.com/support/z-content-solutions/cloud-provisioning
