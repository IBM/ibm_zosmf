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


.. _Requests library for Python:
   https://requests.readthedocs.io/en/latest/
.. _zmf_workflow:
   modules/zmf_workflow.html
.. _zmf_workflow_complete:
   roles/zmf_workflow_complete.html

