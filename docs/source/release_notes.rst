.. ...........................................................................
.. © Copyright IBM Corporation 2023                                          .
.. ...........................................................................

========
Releases
========

Version 1.6.0
=============

Notes
-----

* Added new roles to the z/OSMF Software Management Collection
* 7 new roles have been added.
* 6 aimed at managing the software update process. 1 aimed at managing system holds.
* Software update roles have been added, aimed at enabling automation.
* Fixed bug where zmf_port wasn't always registered properly.
* Updated all z/OSMF Software Management roles to encode the characters in the request URLs

* New roles
  
  * `zmf_swmgmt_holds_for_reason`_
  * `zmf_swupdate_cancel`_
  * `zmf_swupdate_copy`_
  * `zmf_swupdate_resume`_
  * `zmf_swupdate_retrieve`_
  * `zmf_swupdate_retrieve_all`_
  * `zmf_swupdate_start`_

Availability
------------

* `Automation Hub`_
* `Galaxy`_
* `GitHub`_

Version 1.5.0
=============

Notes
-----

* Added new roles for z/OSMF Software Management
* Updated the z/OSMF Software Management roles from a previous release to support UUID

* New roles

  * `zmf_swmgmt_csi_query`_
  * `zmf_swmgmt_system_uuid`_

Availability
------------

* `Automation Hub`_
* `Galaxy`_
* `GitHub`_


.. .............................................................................
.. Global Links
.. .............................................................................

.. _zmf_authenticate:
   modules/zmf_authenticate.html

.. _zmf_workflow:
   modules/zmf_workflow.html

.. _zmf_sca:
   modules/zmf_sca.html

.. _zmf_workflow_complete:
   roles/zmf_workflow_complete.html

.. _zmf_cpm_manage_software_instance:
   roles/zmf_cpm_manage_software_instance.html

.. _zmf_cpm_provision_software_service:
   roles/zmf_cpm_provision_software_service.html

.. _zmf_cpm_remove_software_instance:
   roles/zmf_cpm_remove_software_instance.html

.. _zmf_cpm_list_software_templates:
   roles/zmf_cpm_list_software_templates.html

.. _zmf_cpm_create_software_instance:
   roles/zmf_cpm_create_software_instance.html

.. _zmf_cpm_get_software_instance:
   roles/zmf_cpm_get_software_instance.html

.. _zmf_swmgmt_identify_missing_critical_updates:
   roles/zmf_swmgmt_identify_missing_critical_updates.html

.. _zmf_swmgmt_identify_missing_fixcat_updates:
   roles/zmf_swmgmt_identify_missing_fixcat_updates.html

.. _zmf_swmgmt_search_software_updates:
   roles/zmf_swmgmt_search_software_updates.html

.. _zmf_zmsc_run_management_service:
   roles/zmf_zmsc_run_management_service.html

.. _zmf_swmgmt_csi_query:
   roles/zmf_swmgmt_csi_query.html

.. _zmf_swmgmt_system_uuid:
   roles/zmf_swmgmt_system_uuid.html

.. _zmf_swmgmt_holds_for_reason:
   roles/zmf_swmgmt_holds_for_reason.html

.. _zmf_swupdate_cancel:
   roles/zmf_swupdate_cancel.html

.. _zmf_swupdate_copy:
   roles/zmf_swupdate_copy.html

.. _zmf_swupdate_resume:
   roles/zmf_swupdate_resume.html

.. _zmf_swupdate_retrieve:
   roles/zmf_swupdate_retrieve.html

.. _zmf_swupdate_retrieve_all:
   roles/zmf_swupdate_retrieve_all.html

.. _zmf_swupdate_start:
   roles/zmf_swupdate_start.html

.. _Automation Hub:
   https://www.ansible.com/products/automation-hub

.. _Galaxy:
   https://galaxy.ansible.com/ui/repo/published/ibm/ibm_zosmf

.. _GitHub:
   https://github.com/IBM/ibm_zosmf

.. _z/OS V2R3:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3/en/homepage.html

.. _z/OS Management Facility:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3.izua300/abstract.html

.. _documentation site:
   https://ibm.github.io/z_ansible_collections_doc/ibm_zosmf/docs/ansible_content.html

.. _samples repository:
   https://github.com/IBM/z_ansible_collections_samples/tree/master/zos_management

.. _z/OSMF SCA Configuration:
   https://www.ibm.com/docs/en/zos/2.4.0?topic=services-configure-security-configuration-assistant-service

.. _SCA demo:
   https://mediacenter.ibm.com/media/Use+z+OSMF+to+validate+security+of+DFSMS/1_17jzrqtg/101043781

.. _SCA blog:
   https://community.ibm.com/community/user/ibmz-and-linuxone/blogs/river-jia/2021/07/25/zosmf-security-configuration-assistant