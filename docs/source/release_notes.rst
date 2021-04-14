.. ...........................................................................
.. © Copyright IBM Corporation 2021                                          .
.. ...........................................................................

========
Releases
========

Version 1.0.0
=============

Notes
-----

* Initial beta release of IBM zOS Management Facility collection, referred to as ibm_zosmf
  which is part of the broader offering
  Red Hat® Ansible Certified Content for IBM Z.

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
  * Supported by `z/OS Management Facility`_ V2R3 and later.
  * Module zmf_authenticate is supported by z/OSMF APAR PH12143 (PTF UI66511 for V2R3, PTF UI66512 for V2R4).

.. .............................................................................
.. Global Links
.. .............................................................................

.. _zmf_authenticate:
   modules/zmf_authenticate.html

.. _zmf_workflow:
   modules/zmf_workflow.html

.. _zmf_workflow_complete:
   roles/zmf_workflow_complete.html

.. _zmf_cpm_manage_software_instance:
   roles/zmf_cpm_manage_software_instance.html

.. _zmf_cpm_provision_software_service:
   roles/zmf_cpm_provision_software_service.html

.. _zmf_cpm_remove_software_instance:
   roles/zmf_cpm_remove_software_instance.html

.. _Automation Hub:
   https://www.ansible.com/products/automation-hub

.. _Galaxy:
   https://galaxy.ansible.com/ibm/ibm_zosmf

.. _GitHub:
   https://github.com/IBM/ibm_zosmf

.. _z/OS V2R3:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3/en/homepage.html

.. _z/OS Management Facility:
   https://www.ibm.com/support/knowledgecenter/SSLTBW_2.3.0/com.ibm.zos.v2r3.izua300/abstract.html

.. _playbook repository:
   https://github.com/IBM/z_ansible_collections_samples/blob/master/README.md

.. _FAQs:
   https://ibm.github.io/z_ansible_collections_doc/faqs/faqs.html

.. _playbook configuration:
   https://github.com/IBM/z_ansible_collections_samples/blob/master/docs/share/configuration_guide.md