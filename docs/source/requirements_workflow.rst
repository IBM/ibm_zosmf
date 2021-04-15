.. ...........................................................................
.. © Copyright IBM Corporation 2021                                          .
.. ...........................................................................

Requirements - Operate z/OS Workflows
=====================================

Interacting with **z/OSMF Workflows** in your playbook requires that you meet
the software requirements.
Besides meeting the `Overall Requirements`_, you must ensure that the required
software is installed on the nodes, as follows:

**Control Node**:

* `Requests library for Python`_: 2.23 or later

   It is required when using:

   * module: `zmf_workflow`_
   * role: `zmf_workflow_complete`_


.. _Overall Requirements:
   requirements-single.html
.. _Requests library for Python:
   https://requests.readthedocs.io/en/latest/
.. _zmf_workflow:
   modules/zmf_workflow.html
.. _zmf_workflow_complete:
   roles/zmf_workflow_complete.html