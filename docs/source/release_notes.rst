.. ...........................................................................
.. © Copyright IBM Corporation 2023                                          .
.. ...........................................................................

========
Releases
========

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

Version 1.4.2
=============

Notes
-----

* The README has been updated with a new template.
* Fixed role `zmf_workflow_complete` which previously failed to return final_result.

Availability
------------

* `Automation Hub`_
* `Galaxy`_
* `GitHub`_

Version 1.4.1
=============

Notes
-----

* Documentation updates
* Fixed ansible-lint issues

Availability
------------

* `Automation Hub`_
* `Galaxy`_
* `GitHub`_

Version 1.4.0
=============

Notes
-----

* Added a new z/OSMF Management Services Catalog role `zmf_zmsc_run_management_service`_ to run a z/OS management service
  published in B(z/OS Management Services Catalog).
* Updated module `zmf_workflow` to return the failed step if the workflow is not completed.

* New roles

  * `zmf_zmsc_run_management_service`_

Availability
------------

* `Automation Hub`_
* `Galaxy`_
* `GitHub`_

Reference
---------

* The new z/OS Management Services Catalog role `zmf_zmsc_run_management_service`_ works with z/OSMF V2R4
  and above with the APAR PH52813 installed.

Version 1.3.0
=============

Notes
-----

* Added a new z/OSMF Software Management role `zmf_swmgmt_identify_missing_critical_updates`_ to determine if a software
  instance is missing software updates to resolve PE PTFs, HIPER fixes, or other exception SYSMODs identified by ERROR
  HOLDDATA.  It also helps you identify the SYSMODs that resolve those exceptions.
* Added a new z/OSMF Software Management role `zmf_swmgmt_identify_missing_fixcat_updates`_ to determine if a software
  instance is missing updates for fix categories that might be applicable to the software instance.  It also helps you
  identify the SYSMODs that resolve the missing updates.
* Added a new z/OSMF Software Management role `zmf_swmgmt_search_software_updates`_ to search a software instance for one
  or more software updates  to determine which updates are installed or updates that need to be installed.

* New roles

  * `zmf_swmgmt_identify_missing_critical_updates`_
  * `zmf_swmgmt_identify_missing_fixcat_updates`_
  * `zmf_swmgmt_search_software_updates`_

Availability
------------

* `Automation Hub`_
* `Galaxy`_
* `GitHub`_

Reference
---------

* The new software management roles only work with z/OSMF V2R5 and above with the APAR PH47050 installed.
* The new software management roles require proper input values and users who will use these roles should be provided
  appropriate access on z/OS system.

Version 1.2.1
=============

Notes
-----

* Removed dependency on Requests library for Python on the control node.

Availability
------------

* `Automation Hub`_
* `Galaxy`_
* `GitHub`_

Version 1.2.0
=============

Notes
-----

* Updated module `zmf_sca`_ for SAF based z/OS security automation, which adds support for provisioning security requirements.
* The updated module `zmf_sca`_ is based on the REST API of the z/OSMF Security Configuration Assistant (SCA) with APAR PH47746.
  SCA supports the json format of the security descriptor file. This file can be used to document security requirements
  by function or by product. With the security descriptor file that is easy to create,
  SCA is able to display and automatically provision security requirements in a flexible granularity,
  either by individual requirement, by function or by product. SCA is based on the SAF interface,
  therefore it supports all SAF based security products in most cases. To learn more about z/OSMF SCA, please refer to
  `SCA blog`_ and the `SCA demo`_ in IBM MediaCenter.

Availability
------------

* `Automation Hub`_
* `Galaxy`_
* `GitHub`_

Reference
---------

* The updated module `zmf_sca`_ requires that z/OSMF SCA is configured properly.
  For the required configuration of z/OSMF SCA, please refer to `z/OSMF SCA Configuration`_
* The updated module `zmf_sca`_ only works with z/OSMF V2R4 and above with the APAR PH47746 installed.

Version 1.1.0
=============

Notes
-----

* Added a new module `zmf_sca`_ for SAF based z/OS security automation, which starts with the security validation.
* The new module `zmf_sca`_ is based on the REST API of the z/OSMF Security Configuration Assistant (SCA).
  SCA supports the json format of the security descriptor file. This file can be used to document security requirements
  by function or by product. With the security descriptor file that is easy to create,
  SCA is able to display and automatically validate security requirements in a flexible granularity,
  either by individual requirement, by function or by product. SCA is based on the SAF interface,
  therefore it supports all SAF based security products in most cases. To learn more about z/OSMF SCA, please refer to
  `SCA blog`_ and the `SCA demo`_ in IBM MediaCenter.
* The new module `zmf_sca`_ can be used in use cases like security validation, security audit, etc.
* Added a new cloud provisioning and management (CP&M) role `zmf_cpm_list_software_templates`_ to obtain list of published
  software templates that can be provisioned by user who is requesting to obtain the list.
  List of templates is saved in a file system and contains detailed information about each software template.
* Added a new CP&M role `zmf_cpm_create_software_instance`_ to create a software
  instance in z/OSMF CP&M software instance registry. A json file with various properties for the instance can
  be provided to save instance specific properties in the registry.
* Added a new CP&M role `zmf_cpm_get_software_instance`_ to obtain a specific software instance from the z/OSMF CP&M
  software instance registry. Retrieved software instance along with associated properties is saved in a file system.

* New modules

  * `zmf_sca`_

* New roles

  * `zmf_cpm_list_software_templates`_ 
  * `zmf_cpm_create_software_instance`_ 
  * `zmf_cpm_get_software_instance`_ 

Availability
------------

* `Automation Hub`_
* `Galaxy`_
* `GitHub`_

Reference
---------

* The new module `zmf_sca`_ requires that z/OSMF SCA is configured properly.
  For the required configuration of z/OSMF SCA, please refer to `z/OSMF SCA Configuration`_
* The new module `zmf_sca`_ only works with z/OSMF V2R4 and above with the APAR PH41248 installed.
* The new cloud provisioning and management roles requires z/OSMF cloud provisioning and management
  configured properly and users who will use these roles should be provided appropriate access on
  z/OS system.

Version 1.0.1
=============

Notes
-----

* Initial release of IBM z/OS Management Facility (z/OSMF) collection,
  referred to as ibm_zosmf, which is part of the broader offering
  Red Hat® Ansible Certified Content for IBM Z.
* Generic documentation is available at the `documentation site`_, covering
  guidance on installation, modules, roles and other references.
* Sample playbooks are available at the `samples repository`_.
  Each playbook contains a README file that explains which configurations are needed to run a sample playbook.

* New modules

  * `zmf_authenticate`_
  * `zmf_workflow`_

* New roles

  * `zmf_workflow_complete`_
  * `zmf_cpm_manage_software_instance`_ 
  * `zmf_cpm_provision_software_service`_ 
  * `zmf_cpm_remove_software_instance`_ 

Availability
------------

* `Automation Hub`_
* `Galaxy`_
* `GitHub`_

Reference
---------

* Supported by `z/OS V2R3`_ or later.
* Supported by `z/OS Management Facility`_ V2R3 or later.
* Module `zmf_authenticate`_ is supported by z/OSMF APAR PH12143 (PTF UI66511 for V2R3, PTF UI66512 for V2R4).

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