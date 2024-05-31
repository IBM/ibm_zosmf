# IBM® z/OSMF collection

The **IBM z/OSMF collection** supports automation tasks such as configuration management, application deployment, and provisioning on z/OS.

### Description

The **IBM z/OSMF collection**, also represented as **ibm_zosmf** in this document, is part of the **Red Hat® Ansible Certified Content for IBM Z®** offering that brings Ansible automation to IBM Z®. This collection supports automation tasks such as operating z/OS workflows, provisioning and managing z/OS middlewares/softwares, via z/OSMF RESTful services.

## Requirements

The **IBM z/OSMF collection** requires both a control node and managed node be configured with a minimum set of requirements.

### Ansible Controller

This release of the collection requires **ansible-core >=2.15** (Ansible >=8.x), for additional requirements such as Python, review the [support matrix](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix).

### Managed Node

The managed node has dependencies that are specific to each release of the collection, review [here](https://ibm.github.io/z_ansible_collections_doc/ibm_zosmf/docs/source/requirements_managed.html) for the details of the dependencies.

## Installation

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:

```
ansible-galaxy collection install ibm.ibm_zosmf
```

You can also include it in a requirements.yml file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```
collections:
  - name: ibm.ibm_zosmf
```

Note that if you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the Ansible package.
To upgrade the collection to the latest available version, run the following command:

```
ansible-galaxy collection install ibm.ibm_zosmf --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version 1.0.0:

```
ansible-galaxy collection install ibm.ibm_zosmf:1.0.0
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

## Use Cases

* Use Case Name: Work with z/OSMF workflows
    * Actors:
        * System Programmer
    * Description:
        * An system programmer can perform various operations with z/OSMF workflows on the target z/OS systems, and complete a z/OSMF workflow forcibly or idempotently on the target z/OS systems.
    * Flow:
        * Check whether a workflow instance with the given name exists.
        * Delete the workflow instance if it exists in the z/OSMF server.
        * Create a new workflow instance and start it on each target z/OS system.
        * Periodically check the workflow status and return the final result when the workflow completes.
    * Sample: [Invoking z/OSMF Workflows](https://github.com/IBM/z_ansible_collections_samples/tree/main/zos_management/zosmf_workflows)

* Use Case Name: Provision and manage z/OS middlewares/softwares
    * Actors:
        * Provisioning Administrator
    * Description:
        * The provisioning administrator can provision and manage z/OS middlewares/softwares, such as CICS, Db2, MQ, z/OS Connect, and WebSphere Liberty, on the target z/OS systems using templates published in the z/OSMF Software Services Catalog.
    * Flow:
        * Provision a z/OS middleware/software.
        * Perform various actions to manage a provisioned software service instance.
        * Remove a deprovisioned software service instance.
    * Sample: [z/OSMF Cloud Provisioning and Management](https://github.com/IBM/z_ansible_collections_samples/tree/main/zos_management/zosmf_cloud_provisioning_and_management)

* Use Case Name: Validate and provision security requirements
    * Actors:
        * Security Administrator
    * Description:
        * The security administrator can validate and provision security requirements on target z/OS systems by leveraging z/OSMF Security Configuration Assistant (SCA).
    * Flow:
        * Perform the security validation.
        * Perform the security audit.
        * Perform the security provision.
    * Sample: [z/OSMF Security Configuration Assistant](https://github.com/IBM/z_ansible_collections_samples/tree/main/zos_management/zosmf_security_configuration_assistant)

## Testing

All releases will meet the following test criteria:

* 100% success for [Functional](https://github.com/IBM/ibm_zosmf/tree/main/tests/CICD/playbooks) tests.
* 100% success for [Sanity](https://docs.ansible.com/ansible/latest/dev_guide/testing/sanity/index.html#all-sanity-tests) tests as part of [ansible-test](https://docs.ansible.com/ansible/latest/dev_guide/testing.html#run-sanity-tests).
* 100% success for [ansible-lint](https://ansible.readthedocs.io/projects/lint/) allowing only false positives.

This release of the collection was tested with following dependencies:

* ansible-core v2.15.x, v2.16.x
* Python 3.10.x, 3.11.x
* z/OS 3.1

Review the [release notes](https://ibm.github.io/z_ansible_collections_doc/ibm_zosmf/docs/source/release_notes.html) for the details of this release.

## Contributing

We are not currently accepting community contributions. However, we encourage you to open [git issues](https://github.com/IBM/ibm_zosmf/issues) for bugs, comments or feature requests. Review this content periodically to learn when and how to make contributions in the future.

## Support

As Red Hat Ansible [Certified Content](https://catalog.redhat.com/software/search?target_platforms=Red%20Hat%20Ansible%20Automation%20Platform), this collection is entitled to [support](https://access.redhat.com/support/) through [Ansible Automation Platform](https://www.redhat.com/en/technologies/management/ansible) (AAP). After creating a Red Hat support case, if it is determined the issue belongs to IBM, Red Hat will instruct you to create an [IBM support case](https://www.ibm.com/mysupport/s/createrecord/NewCase) and share the case number with Red Hat so that a collaboration can begin between Red Hat and IBM.

The current supported versions of this collection can be found listed under the [release section](https://ibm.github.io/z_ansible_collections_doc/ibm_zosmf/docs/source/release_notes.html).

## Release Notes and Roadmap

The collection's cumulative release notes can be reviewed [here](https://ibm.github.io/z_ansible_collections_doc/ibm_zosmf/docs/source/release_notes.html). Note, some collections release before an ansible-core version reaches End of Life (EOL), thus the version of ansible-core that is supported must be a version that is currently supported.

For AAP users, to see the supported ansible-core versions, review the [AAP Life Cycle](https://access.redhat.com/support/policy/updates/ansible-automation-platform).

For Galaxy and GitHub users, to see the supported ansible-core versions, review the [ansible-core support matrix](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix).

## Related Information

Example playbooks and use cases can be be found in the [z/OS playbook repository](https://github.com/IBM/z_ansible_collections_samples).
Supplemental content on getting started with Ansible, architecture and use cases is available [here](https://ibm.github.io/z_ansible_collections_doc/reference/helpful_links.html).

## License Information

This collection is licensed under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).