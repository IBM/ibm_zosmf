.. ...........................................................................
.. © Copyright IBM Corporation 2020, 2025
..
.. This is an orphaned page because its not included in any toctree
.. 'orphan' if set, warnings about this file not being included in any toctree
..  will be suppressed.
.. ...........................................................................

:orphan:

=============
Configuration
=============

After installing the IBM z/OSMF collection, usage of the collection should be fairly simple. You will need to be sure that users attempting to utilize the collection have access to z/OSMF on the managed node (LPARs).

Step 1: Directory Structure
===========================

.. dropdown:: The following section discusses configuring the collection ... (expand for more)
    :color: primary
    :icon: info

    The following section discusses configuring the collection,
    it is best to begin by creating the directory structure that will combine
    the various elements; playbooks, inventory, variables (group_vars & host_vars)
    as well as environment variables.

    In this example, we are using the alternative directory layout that places
    inventory with ``group_vars`` and ``host_vars`` which is particularly useful
    if the variables contained in ``groups_vars`` and ``host_vars`` don't have
    much in common with other systems, eg Linux, Windows, etc.

    This directory structure complete with playbook and configurations is
    available in `Ansible Z Playbook Repository`_.

    The directory structure should be created on the control node, that is
    where Ansible is running.

    .. code-block:: sh

        /playbooks/
                ├── my_playbook.yml       # A playbook
                ├── another_playbook.yml  # Another playbook
                ├── ansible.cfg           # Custom Ansible configuration
                ├── inventories/
                    └── host_vars/        # Assign variables to particular systems
                        └── zos_host.yml
                    └── group_vars/       # Assign variables to particular groups
                        └── all.yml
                    └── inventory.yml     # Inventory file for production systems


    The following commands will also create this directory structure in the `/tmp`
    directory.

    .. code-block:: sh

        mkdir -p /tmp/playbooks;
        touch /tmp/playbooks/my_playbook.yml;
        touch /tmp/playbooks/another_playbook.yml;
        touch /tmp/playbooks/ansible.cfg;
        mkdir -p /tmp/playbooks/inventories;
        mkdir -p /tmp/playbooks/inventories/host_vars;
        touch /tmp/playbooks/inventories/host_vars/zos_host.yml;
        mkdir -p /tmp/playbooks/inventories/group_vars;
        touch /tmp/playbooks/inventories/group_vars/all.yml;
        touch /tmp/playbooks/inventories/inventory.yml;


Step 2: Inventory
==================

.. dropdown:: The following section discusses how Ansible interacts with managed node ... (expand for more)
    :color: primary
    :icon: file-code

    The following section discusses how Ansible interacts with managed
    nodes (hosts) using a list known as `inventory`_. It is a configuration file that
    specifies the hosts and group of hosts on which Ansible commands, modules, and playbooks
    will operate. It also defines variables and connection details for those hosts, such as
    IP address. For more information, see `Building Ansible inventories`_.

    The following inventory is explained.

    - **systems** is a group that contains one managed host, **zos1**.
    - **zos1** is the name chosen for managed node, you can choose any name. \
    - **ansible_host** is an ansible reserved keyword that is the hostname ansible
      will connect to and run automated tasks on, it can be an LPAR, ZVM, etc.
    - **ansible_user** is an ansible reserved keyword that is the user Ansible will
      use to connect to the managed node, generally and OMVS segment.

    Edit the file ``inventory.yml`` located at ``/tmp/playbooks/inventories/inventory.yml``
    and paste the following below. You will need to update the properties
    **ansible_host** and **ansible_user**.

    .. code-block:: sh

        systems:
            hosts:
                zos1:
                ansible_host: zos_managed_node_host_name_or_ip
                ansible_user: zos_managed_node_ssh_user

Step 3: User
============

.. dropdown:: The following section discusses how the collection connects to the managed node over SSH ... (expand for more)
    :color: primary
    :icon: command-palette

    The following section discusses how the collection connects to the
    managed node using the z/OSMF Web APIs via the zOSMF user defined in inventory or optionally from
    the command line, thus requiring access to z/OS Management Facility (z/OSMF) as well as access to the additional resources you're trying to access.
    
    From a security perspective, the collection will require TSO segment in the users profile. It's recommended to have an OMVS segment as well.

    With the RACF **ADDGROUP** command you can:

    - Define a new group to RACF.
    - Add a profile for the new group to the RACF database.
    - Specify z/OS UNIX System Services information for the group being defined to RACF.
    - specify that RACF is to automatically assign an unused GID value to the group.

    With the RACF **ADDUSER** command you can:

    - Define a new user to RACF.
    - Add a profile for the new user to the RACF database.
    - Create a connect profile that connects the user to the default group.
    - Create an OMVS segment.
    - Create a TSO segment.

    When issuing RACF commands, you might require sufficient authority to the proper
    resources. It is recommended you review the `RACF language reference`_.

    You can define a new group to RACF with command:

    .. code-block:: sh

       ADDGROUP gggggggg OMVS(AUTOGID)

    You can add a new user with RACF command:

    .. code-block:: sh

       ADDUSER uuuuuuuu DFLTGRP(gggggggg) OWNER(nnnnnnnn) PASSWORD(pppppppp) TSO(ACCTNUM(aaaaaaaa) PROC(pppppppp)) OMVS(HOME(/u/uuuuuuuu) PROGRAM('/bin/sh')) AUTOUID

    To learn more about creating users with RACF, see `RACF command syntax`_.

    .. dropdown:: The following section explains the RACF operands ... (expand for more)
        :color: info
        :icon: file-code

        The following section explains the RACF operands used in the above RACF commands.

        uuuuuuuu
            - Specifies the user to be defined to RACF. 1 - 8 alphanumeric characters. A
              user id can contain any of the supported symbols A-Z, 0-9, #, $, or @.
        gggggggg
            - Specifies the name of a RACF-defined group to be used as the default
              group for the user. If you do not specify a group, RACF uses your current connect
              group as the default. 1 - 8 alphanumeric characters, beginning with an alphabetic
              character. A group name can contain any of the supported symbols A-Z, 0-9, #, $, or @.
        nnnnnnnn
            - Specifies a RACF-defined user or group to be assigned as the owner of the
              new group. If you do not specify an owner, you are defined as the owner of the group.
        pppppppp
            - Specifies the user's initial logon password. This password is always set
              expired, thus requiring the user to change the password at initial logon.
        aaaaaaaa
            - Specifies the user's default TSO account number. The account number you
              specify must be protected by a profile in the ACCTNUM general resource class, and
              the user must be granted READ access to the profile.

.. Step 6: Security
.. ================

.. .. dropdown:: The following section discusses how the collection secures interaction using RACF ... (expand for more)
..     :color: primary
..     :icon: command-palette

..     The following section discusses how the collection secures interaction using RACF.
..     Some of the modules in the collection will perform operations that require the
..     playbook user to have appropriate authority with various RACF resource classes.
..     Each module documents which access is needed in the **notes** section. A user
..     is described as the remote SSH user executing playbook tasks, who can also
..     obtain escalated privileges to execute as another user.

..     In RACF, a *class* refers to a collection of resources that share similar
..     characteristics, while a *resource class profile* is a set of access controls
..     belonging a class. In other words, a class is a group of related things, and a
..     resource class profile are rules managing access to those things within that group.

..     .. dropdown:: Enabling RACF resource classes for module *zos_apf* ... (expand for more)
..         :color: info
..         :icon: command-palette

..         Enabling RACF resource classes for module ``zos_apf`` requires that
..         library *libname*, you have **UPDATE** authority to the RACF **FACILITY**
..         resource class entity **CSVAPF.libname**, or there must be no **FACILITY**
..         class profile that protects that entity. Once access for **CSVAPF.libname**
..         has been determined:

..         .. dropdown:: To control who can make the APF list dynamic ... (expand for more)
..             :icon: command-palette

..             To control who can make the **APF list dynamic** using module ``zos_apf``,
..             the RACF security administrator can:

..             Establish a profile for the following FACILITY class with command:

..             .. code-block:: sh

..                 RDEFINE FACILITY CSVAPF.MVS.SETPROG.FORMAT.DYNAMIC UACC(NONE)

..             Then permit the RACF-defined user or group profile *iiiiiiii* to use the class
..             with command:

..             .. code-block:: sh

..                 PERMIT CSVAPF.MVS.SETPROG.FORMAT.DYNAMIC CLASS(FACILITY) ID(iiiiiiii) ACCESS(UPDATE)


..             If the FACILITY class is not active, issue the command:

..             .. code-block:: sh

..                 SETROPTS CLASSACT(FACILITY)


..             To verify the FACILITY class is active, issue command:

..             .. code-block:: sh

..                 SETROPTS LIST

..             To refresh the FACILITY resource class, issue command:

..             .. code-block:: sh

..                 SETROPTS RACLIST(FACILITY) REFRESH

..         .. dropdown:: To control who can make the APF list static ... (expand for more)
..             :icon: command-palette

..             To control who can make the **APF list dynamic** using module ``zos_apf``,
..             the RACF security administrator can:

..             Establish a profile for the following FACILITY class with command:

..             .. code-block:: sh

..                 RDEFINE FACILITY CSVAPF.MVS.SETPROG.FORMAT.STATIC UACC(NONE)

..             Then permit the RACF-defined user or group profile *iiiiiiii* to use the class
..             with command:

..             .. code-block:: sh

..                 PERMIT CSVAPF.MVS.SETPROG.FORMAT.STATIC CLASS(FACILITY) ID(iiiiiiii) ACCESS(UPDATE)


..             If the FACILITY class is not active, issue the command:

..             .. code-block:: sh

..                 SETROPTS CLASSACT(FACILITY)


..             To verify the FACILITY class is active, issue command:

..             .. code-block:: sh

..                 SETROPTS LIST

..             To refresh the FACILITY resource class, issue command:

..             .. code-block:: sh

..                 SETROPTS RACLIST(FACILITY) REFRESH


..         To learn more about enabling users APF dynamic and static access, see
..         controlling `static and dynamic access`_.

..     .. dropdown:: Enabling RACF resource class for module *zos_backup_restore* ... (expand for more)
..         :color: info
..         :icon: command-palette

..         Enabling RACF resource class for module ``zos_backup_restore`` requires that
..         library **STGADMIN.ADR.DUMP.TOLERATE.ENQF** have **READ** authority or there
..         must be no **FACILITY** class profile that protects that entity to use the
..         module option recover=true.

..         Establish a profile for the following FACILITY class with command:

..         .. code-block:: sh

..             RDEFINE FACILITY STGADMIN.ADR.DUMP.TOLERATE.ENQF UACC(NONE)

..         Then permit the RACF-defined user or group profile *iiiiiiii* to use the class
..         with command:

..         .. code-block:: sh

..             PERMIT STGADMIN.ADR.DUMP.TOLERATE.ENQF CLASS(FACILITY) ID(iiiiiiii) ACCESS(READ)

..         If the FACILITY class is not active, issue the command:

..         .. code-block:: sh

..             SETROPTS CLASSACT(FACILITY)

..         To verify the FACILITY class is active, issue command:

..         .. code-block:: sh

..             SETROPTS LIST

..         To refresh the FACILITY resource class, issue command:

..         .. code-block:: sh

..             SETROPTS RACLIST(FACILITY) REFRESH

..     .. dropdown:: Enabling RACF resource class for module *zos_copy* ... (expand for more)
..         :color: info
..         :icon: command-palette

..         Enabling RACF resource class for module ``zos_copy`` requires that library
..         **MVS.MCSOPER.ZOAU** have **READ** authority or there must be no **OPERCMDS**
..         class profile that protects that entity to use the module.

..         Establish a profile for the following OPERCMDS class with command:

..         .. code-block:: sh

..             RDEFINE OPERCMDS MVS.MCSOPER.ZOAU UACC(NONE)

..         Then permit the RACF-defined user or group profile *iiiiiiii* to use the class
..         with command:

..         .. code-block:: sh

..             PERMIT MVS.MCSOPER.ZOAU CLASS(OPERCMDS) ID(iiiiiiii) ACCESS(READ)

..         If the OPERCMDS class is not active, issue the command:

..         .. code-block:: sh

..             SETROPTS CLASSACT(OPERCMDS)

..         To verify the OPERCMDS class is active, issue command:

..         .. code-block:: sh

..             SETROPTS LIST

..         To refresh the OPERCMDS resource class, issue command:

..         .. code-block:: sh

..             SETROPTS RACLIST(OPERCMDS) REFRESH

..     .. dropdown:: Enabling RACF resource class for module *zos_volume_init* ... (expand for more)
..         :color: info
..         :icon: command-palette

..         Enabling RACF resource class for module ``zos_volume_init`` requires
..         that library **STGADMIN.ICK.INIT** have **READ** authority or there must
..         be no **FACILITY** class profile that protects that entity to use the module.

..         Establish a profile for the following FACILITY class with command:

..         .. code-block:: sh

..             RDEFINE FACILITY STGADMIN.ICK.INIT UACC(NONE)

..         Then permit the RACF-defined user or group profile *iiiiiiii* to use the class
..         with command:

..         .. code-block:: sh

..             PERMIT STGADMIN.ICK.INIT CLASS(FACILITY) ID(iiiiiiii) ACCESS(READ)

..         If the FACILITY class is not active, issue the command:

..         .. code-block:: sh

..             SETROPTS CLASSACT(FACILITY)

..         To verify the FACILITY class is active, issue command:

..         .. code-block:: sh

..             SETROPTS LIST

..         To refresh the FACILITY resource class, issue command:

..         .. code-block:: sh

..             SETROPTS RACLIST(FACILITY) REFRESH


..     .. dropdown:: Use the RLIST command to display information on resources ... (expand for more)
..         :color: success
..         :icon: info

..         Use the RLIST command to display information on resources belonging to RACF classes.

..         To see information on class OPERCMDS, resource class profile MVS.MCSOPER.ZOAU,
..         issue command:

..         .. code-block:: sh

..             RLIST OPERCMDS MVS.MCSOPER.ZOAU

..         RLIST command result:

..         .. code-block:: sh

..             CLASS      NAME
..             -----      ----
..             OPERCMDS   MVS.MCSOPER.ZOAU

..             LEVEL  OWNER      UNIVERSAL ACCESS  YOUR ACCESS  WARNING
..             -----  --------   ----------------  -----------  -------
..             00     RACEC      READ              READ         NO

Step 4: Run a playbook
======================

.. dropdown:: The following section discusses how to run an run an Ansible playbook ... (expand for more)
    :color: primary
    :icon: command-palette

    The following section discusses how to use the IBM z/OS Core collection in an Ansible playbook.
    An `Ansible playbook`_ consists of organized instructions that define work for a managed
    node (host) to be managed with Ansible.

    If you have completed steps 1 - 6 above, then you are ready to run a playbook. In the
    folllowing playbook, there are two tasks, the first one will perform a simple ping
    operation using `ibm_zos_core.zos_ping`_ and the following operation will use the
    `ibm_zos_core.zos_operator`_ command to display the local time of day and the date.

    .. code-block:: sh

        ---
        - hosts: all
          environment: "{{ environment_vars }}"

          tasks:
            - name: Ping host - {{ inventory_hostname }}
              ibm.ibm_zos_core.zos_ping:
              register: result
            - name: Response
              debug:
                msg: "{{ result.ping }}"

            - name: Display system limits
            zos_operator:
                cmd: 'D OMVS,LIMITS'
            register: result
            tags: sys_limit_info

            - name: Result display system limits
            debug:
                msg: "{{result}}"
            tags: sys_limit_info


    Copy the above playbook into a file, call it **sample.yml** and to run it,
    use he Ansible command ``ansible-playbook`` with the inventory you definewd
    in step 4 along with a reqeust for a password using opiton ``--ask-pass``.

    The command syntax is ``ansible-playbook -i <inventory> <playbook> --ask-pass``,
    for example;

    .. code-block:: sh

        ansible-playbook -i inventory sample.yaml

    You can avoid a password prompt by configuring SSH keys, see `setting up SSH keys`_.

    For further reading, review `run your first command and playbook`_ and follow up
    with `Ansible playbooks`_.


    .. dropdown:: Optionally, you can configure the console logging verbosity ... (expand for more)
        :color: success
        :icon: info

        Optionally, you can configure the console logging verbosity during playbook
        execution. This is helpful in situations where communication is failing and
        you want to obtain more details. To adjust the logging verbosity, append more
        letter ``v``'s; for example, ``-v``, ``-vv``, ``-vvv``, or ``-vvvv``. Each letter
        ``v`` increases logging verbosity similar to traditional logging levels **INFO**,
        **WARN**, **ERROR**, **DEBUG**.

        Using the previous example, the following will set the highest level of
        verbosity.

        .. code-block:: sh

            ansible-playbook -i inventory sample.yaml -vvvv

.. ...........................................................................
.. External links
.. ...........................................................................
.. _Ansible Z Playbook Repository:
   https://github.com/IBM/z_ansible_collections_samples
.. _How to put environment variables in a playbook:
   https://github.com/ansible-collections/ibm_zos_core/discussions/657
.. _Open Enterprise SDK for Python:
   https://www.ibm.com/products/open-enterprise-python-zos
.. _Z Open Automation Utilities:
   https://www.ibm.com/docs/en/zoau/latest
.. _inventory:
   https://ibm.github.io/z_ansible_collections_doc/welcome/basic-concepts.html#term-Inventory
.. _Building Ansible inventories:
   https://docs.ansible.com/ansible/latest/inventory_guide/index.html#
.. _RACF command syntax:
   https://www.ibm.com/docs/en/zos/3.1.0?topic=syntax-addgroup-add-group-profile
.. _RACF language reference:
   https://www.ibm.com/docs/en/zos/3.1.0?topic=racf-zos-security-server-command-language-reference
.. _static and dynamic access:
   https://www.ibm.com/docs/en/zos/3.1.0?topic=lists-controlling-how-change-apf-list-format
.. _Ansible playbook:
   https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#playbooks-intro
.. _ibm_zos_core.zos_ping:
    https://ibm.github.io/z_ansible_collections_doc/ibm_zos_core/docs/source/modules/zos_ping.html
.. _ibm_zos_core.zos_operator:
   https://ibm.github.io/z_ansible_collections_doc/ibm_zos_core/docs/source/modules/zos_operator.html
.. _setting up SSH keys:
   https://docs.ansible.com/ansible/latest/inventory_guide/connection_details.html#setting-up-ssh-keys
.. _Ansible playbooks:
   https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#about-playbooks
.. _run your first command and playbook:
   https://docs.ansible.com/ansible/latest/network/getting_started/first_playbook.html#run-your-first-command-and-playbook
.. _managed node requirements:
   collection-requirements.html#control-node