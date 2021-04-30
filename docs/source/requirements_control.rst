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

Operate z/OS Workflows
----------------------

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

