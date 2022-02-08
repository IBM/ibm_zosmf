.. ...........................................................................
.. © Copyright IBM Corporation 2021                                          .
.. ...........................................................................

Modules
=======

Modules can be used from the command line or in a playbook task.
Ansible executes each module, usually on the remote target node, and collects
return values.
While different modules perform different tasks, their interfaces and
responses follow similar patterns.

You can also access the documentation of each module from the command line by
using the `ansible-doc`_ command:

.. code-block:: sh

   $ ansible-doc ibm.ibm_zosmf.zmf_workflow
   $ ansible-doc ibm.ibm_zosmf.zmf_sca

The **IBM z/OSMF collection** provides several modules.
Reference material for each module contains documentation on what parameters
certain modules accept, what values they expect those parameters to be, and
what will returned.

.. toctree::
   :maxdepth: 1
   :glob:

   modules/*


.. _ansible-doc:
   https://docs.ansible.com/ansible/latest/cli/ansible-doc.html#ansible-doc
