.. ...........................................................................
.. © Copyright IBM Corporation 2025
.. This files (collections-requirements.rxt) contents should be contributed by
.. all collections discussing their particular requirements. For the most part,
.. I have kept this general but each team will need to identify their
.. collection versions, control & managed node dependencies and create a unique
.. reference, for example the reference I am using is `ibm-zosmf-dependency-matrix`
..
.. This is an orphaned page because its not included in any toctree
.. 'orphan' if set, warnings about this file not being included in any toctree
..  will be suppressed.
.. ...........................................................................

:orphan:

=======================
Collection Requirements
=======================

The **dependency matrix** lists the minimum required component versions for each
version of the collection when they became generally available (GA) for both,
the control node and managed node.

The minimum required component versions can reach end of life (EOL) before
the collection reaches EOL, when this happens, you must update the
component to a supported version.

For example, if a collection is released that minimally requires
**ansible-core** version **2.15.0** (Ansible 8.0) and later reaches EOL,
a newer supported version of **ansible-core** must be installed.

.. _ibm-zosmf-collection-requirements-control-node:

Control Node
------------

.. dropdown:: When you install an Ansible version, review the ... (expand for more)
   :color: primary
   :icon: info

   When you install an Ansible (`ansible-core`_) version, review the communities
   `ansible-core support matrix`_ to select the appropriate dependencies.
   Different releases of **ansible-core** can require different dependencies
   such as is the case with Python.

   Optionally, you can upgrade the **ansible-core** version, review the
   `installing Ansible`_ guide and select the appropriate option.

   If the control node is Ansible Automation Platform (AAP), review the
   `Red Hat Ansible Automation Platform Life Cycle`_ to select a supported
   AAP version.

.. _ibm-zosmf-collection-requirements-managed-node:

Managed Node
------------

.. dropdown:: The managed requires the following to be installed ... (expand for more)
   :color: primary
   :icon: info

   The :term:`managed node<Managed node>` requires the following be installed and
   configured:

      - `z/OS Management Facility`_

.. _ibm-zosmf-collection-requirements-dependency-matrix:

Dependency Matrix
-----------------

.. dropdown:: The dependency matrix lists the dependencies for both, the control node and managed node ... (expand for more)
   :color: primary
   :icon: info

   The dependency matrix lists the dependencies for both, the :term:`control node<Control node>`
   and :term:`managed node<Managed node>`.

   Over time, dependencies will reach EOL, for IBM product lifecycle information,
   you can search for products using the product's name, version or ID on
   the `IBM Support product lifecycle`_ page.

   +---------+----------------------------+-----------------------------------------------------+
   | Version | Control Node               | Managed Node                                        |
   +=========+============================+=====================================================+
   | 1.6.x   |- `ansible-core`_ >=2.15.x  |- `z/OS`_ V2R5 - V3Rx                                |
   |         |- `Ansible`_ >=8.0.x        |- `z/OS Management Facility`_                        |
   |         |- `AAP`_ >=2.4              |                                                     |
   |         |                            |                                                     |
   +---------+----------------------------+-----------------------------------------------------+
   | 1.5.x   |- `ansible-core`_ >=2.15.x  |- `z/OS`_ V2R5 - V3Rx                                |
   |         |- `Ansible`_ >=8.0.x        |- `z/OS Management Facility`_                        |
   |         |- `AAP`_ >=2.4              |                                                     |
   |         |                            |                                                     |
   +---------+----------------------------+-----------------------------------------------------+
   | 1.4.x   |- `ansible-core`_ >=2.15.x  |- `z/OS`_ V2R5 - V3Rx                                |
   |         |- `Ansible`_ >=8.0.x        |- `z/OS Management Facility`_                        |
   |         |- `AAP`_ >=2.4              |                                                     |
   |         |                            |                                                     |
   +---------+----------------------------+-----------------------------------------------------+
   | 1.3.x   |- `ansible-core`_ >=2.15.x  |- `z/OS`_ V2R4 - V2Rx                                |
   |         |- `Ansible`_ >=8.0.x        |- `z/OS Management Facility`_                        |
   |         |- `AAP`_ >=2.4              |                                                     |
   |         |                            |                                                     |
   +---------+----------------------------+-----------------------------------------------------+

.. .............................................................................
.. Global Links
.. .............................................................................
.. _ansible-core support matrix:
   https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix
.. _Red Hat Ansible Automation Platform Life Cycle:
   https://access.redhat.com/support/policy/updates/ansible-automation-platform
.. _IBM Support product lifecycle:
    https://www.ibm.com/support/pages/lifecycle/search/
.. _5655-PYT:
   https://www.ibm.com/support/pages/lifecycle/search?q=5655-PYT
.. _5698-PA1:
   https://www.ibm.com/support/pages/lifecycle/search?q=5698-PA1
.. _AAP:
   https://access.redhat.com/support/policy/updates/ansible-automation-platform
.. _Automation Hub:
   https://www.ansible.com/products/automation-hub
.. _Open Enterprise SDK for Python:
   https://www.ibm.com/products/open-enterprise-python-zos
.. _Z Open Automation Utilities:
   https://www.ibm.com/docs/en/zoau/latest
.. _z/OS Management Facility:
   https://www.ibm.com/products/zos/management-facility
.. _z/OS shell:
   https://www.ibm.com/support/knowledgecenter/en/SSLTBW_2.4.0/com.ibm.zos.v2r4.bpxa400/part1.htm
.. _z/OS OpenSSH:
   https://www.ibm.com/docs/en/zos/latest?topic=zbed-zos-openssh
.. _z/OS:
   https://www.ibm.com/docs/en/zos
.. _Open Enterprise SDK for Python lifecycle:
   https://www.ibm.com/support/pages/lifecycle/search?q=5655-PYT
.. _Z Open Automation Utilities lifecycle:
   https://www.ibm.com/support/pages/lifecycle/search?q=5698-PA1
.. _ansible-core:
   https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix
.. _Ansible:
   https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix
.. _installing Ansible:
   https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible