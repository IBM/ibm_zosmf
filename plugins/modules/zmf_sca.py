#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) IBM Corporation 2021
# Apache License, Version 2.0 (see https://opensource.org/licenses/Apache-2.0)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: zmf_sca

short_description: Automate z/OS security validation

version_added: "1.0.0"

author:
    - Xiao Ming Liu (@EricLiuAtIbm)

description:
    - >
      This module supports automatically validating security requirements/configuration based
      on the security descriptor JSON file.
    - This module drives z/OSMF Security Configuration Assistant REST API undercover.

options:
    target_userid:
        description:
            - >
              User ID or group ID to be validated for the security requirements documented by the security descriptor
              JSON file which is specified by parameter path_of_security_requirements.
            - >
              If this parameter is not specified, the current logon user ID will be used to be validated.
        required: false
        type: str

    location:
        description: The location of path_of_security_requirements.
        required: false
        type: str
        default: 'zos'
        choices:
            - zos
            - local

    path_of_security_requirements:
        description:
            - >
              Absolute path of the security descriptor JSON file which contains the security requirements
              to be validated.
        required: true
        type: str

    expected_result:
        description:
            - Expected validation result of security requirements.
            - >
                For all-passed, the module returns success when all security requirements are satisfied.
                If any requirement is failed or can not be determined, this module will be failed.
            - >
                For all-failed, the module returns success when all security requirements are failed.
                If any requirement is satisfied or can not be determined, this module will be failed.
            - >
              The value "all-passed" can be used in security validation use case.
              The value "all-failed" may be used in security auditing use case to check if any over permission exists.
        required: false
        default: 'all-passed'
        type: str
        choices:
            - all-failed
            - all-passed

    state:
        description:
            - The desired final state.
            - >
              If I(state=check), this module performs security validation for the security requirements
              specified in path_of_security_requirements.
        required: false
        type: str
        default: check
        choices:
            - check

    zmf_credential:
        description:
            - >
              Authentication credentials, returned by module
              M(zmf_authenticate), for successful authentication with the
              z/OSMF server.
            - >
              If I(zmf_credential) is supplied, I(zmf_host), I(zmf_port),
              I(zmf_user), I(zmf_password), I(zmf_crt) and I(zmf_key) are
              ignored.
        required: False
        type: dict
        default: null
        suboptions:
            ltpa_token_2:
                description:
                    - >
                      The value of the Lightweight Third Party Access (LTPA)
                      token, which supports strong encryption.
                    - >
                      If I(jwt_token) is not supplied, I(ltpa_token_2) is
                      required.
                required: False
                type: str
                default: null
            jwt_token:
                description:
                    - >
                      The value of the JSON web token, which supports strong
                      encryption.
                    - >
                      If I(ltpa_token_2) is not supplied, I(jwt_token) is
                      required.
                required: False
                type: str
                default: null
            zmf_host:
                description: Hostname of the z/OSMF server.
                required: True
                type: str
            zmf_port:
                description: Port number of the z/OSMF server.
                required: False
                type: int
                default: null
    zmf_host:
        description:
            - Hostname of the z/OSMF server.
            - If I(zmf_credential) is supplied, I(zmf_host) is ignored.
            - If I(zmf_credential) is not supplied, I(zmf_host) is required.
        required: False
        type: str
        default: null
    zmf_port:
        description:
            - Port number of the z/OSMF server.
            - If I(zmf_credential) is supplied, I(zmf_port) is ignored.
        required: False
        type: int
        default: null
    zmf_user:
        description:
            - User name to be used for authenticating with z/OSMF server.
            - If I(zmf_credential) is supplied, I(zmf_user) is ignored.
            - >
              If I(zmf_credential) is not supplied, I(zmf_user) is required
              when I(zmf_crt) and I(zmf_key) are not supplied.
            - >
              If I(zmf_credential) is not supplied and I(zmf_crt) and
              I(zmf_key) are supplied, I(zmf_user) and I(zmf_password) are
              ignored.
        required: False
        type: str
        default: null
    zmf_password:
        description:
            - Password to be used for authenticating with z/OSMF server.
            - If I(zmf_credential) is supplied, I(zmf_password) is ignored.
            - >
              If I(zmf_credential) is not supplied, I(zmf_password) is required
              when I(zmf_crt) and I(zmf_key) are not supplied.
            - >
              If I(zmf_credential) is not supplied and I(zmf_crt) and
              I(zmf_key) are supplied, I(zmf_user) and I(zmf_password) are
              ignored.
        required: False
        type: str
        default: null
    zmf_crt:
        description:
            - >
              Location of the PEM-formatted certificate chain file to be used
              for HTTPS client authentication.
            - >
              If I(zmf_credential) is supplied, I(zmf_crt) is ignored.
            - >
              If I(zmf_credential) is not supplied, I(zmf_crt) is required when
              I(zmf_user) and I(zmf_password) are not supplied.
        required: False
        type: str
        default: null
    zmf_key:
        description:
            - >
              Location of the PEM-formatted file with your private key to be
              used for HTTPS client authentication.
            - If I(zmf_credential) is supplied, I(zmf_key) is ignored.
            - >
              If I(zmf_credential) is not supplied, I(zmf_key) is required when
              I(zmf_user) and I(zmf_password) are not supplied.
        required: False
        type: str
        default: null

'''

EXAMPLES = r'''
- name: Authenticate with z/OSMF server by username/password, and register the result for later use.
  zmf_authenticate:
    zmf_host: "{{ zmf_host }}"
    zmf_port: "{{ zmf_port }}"
    zmf_user: "{{ zmf_user }}"
    zmf_password: "{{ zmf_password }}"
  register: result_auth
  
- name: Validate resources defined in a z/OS security descriptor file and expect all requirements are satisfied.
  ibm.ibm_zosmf.zmf_sca:
    zmf_credential: "{{ result_auth }}"
    target_userid: IBMUSER
    path_of_security_requirements: /global/zosmf/sample/configuration/security/descriptor.json

- name: Validate resources defined in a local security descriptor file and expect no access to any items.
  ibm.ibm_zosmf.zmf_sca:
    zmf_credential: "{{ result_auth }}"
    target_userid: IBMUSER
    path_of_security_requirements: /home/user/descriptor.json
    location: local
    expected_result: all-failed

'''

RETURN = r'''
changed:
    description:
        - Indicates if any change is made during the module operation.
    returned: always
    type: bool

msg:
    description: Error message.
    returned: always on error
    type: str

resourceItems:
    description: Array of security resources do not match with expected result.
    type: list
    elements: dict
    returned: always on fail
    contains:
        itemId:
            description: Item ID.
            type: str
            sample: '5695DF18658I10001000'
        itemType:
            description: Item type.
            type: str
            sample: 'PROGRAMMABLE'
        itemCategory:
            description: Item category.
            type: str
            sample: 'CHANGEDATASET VX'
        itemDescription:
            description: Item description.
            type: str
            sample: 'DFSMSrmm inventory management CHANGEDATASET VX command protection.'
        resourceProfile:
            description:
                - Name of security resource profile.
                - At current stage,
                -   Variable in the name is not supported.
                -   Generic resource name is not supported.
            type: str
            returned: always
            sample: 'STGADMIN.EDG.CD.VX'
        resourceClass:
            description: SAF resource class.
            type: str
            returned: always
            sample: 'FACILITY'
        access:
            description:
                - Level of access that is required to the security resource for the specified user ID or group ID.
                - Value can be the following
            type: str
            returned: always
            sample:
                - READ
                - UPDATE
                - CONTROL
                - ALTER
        action:
            description: For validate action, the return value will be 'validate'.
            type: str
            returned: always
            sample: 'validate'
        actionObjectId:
            description:
                - The object ID of this action. For validation action, this ID is the same as validatedId below.
                - This field can also be used for other action in further versions.
            type: str
            returned: always
            sample: ''
        validatedId:
            description: User ID or group ID that is used to validate for the resource.
            type: str
            returned: always
            sample: ''
        status:
            description:
                - Validation result
            type: str
            returned: always
            sample:
                - Passed
                - Failed
                - Unknown
        additionalInfo:
            description: Additional info.
            type: str
            sample: ''
        whoNeedsAccess:
            description:
                - Users (security groups) who require access to this resource.
                - The Security Configuration Assistant does not verify that security groups are defined;
                - your security administrator must verify that the groups exist.
            type: str
            sample: '<Inventory Management>'
        messageId:
            description: Message Id.
            type: str
            sample: ''
        messageText:
            description: Message text.
            type: str
            sample: ''
        httpStatus:
            description: http status code if error.
            type: str
            returned: on error
            sample: ''
        requestMethod:
            description: http request method if error.
            type: str
            returned: on error
            sample: ''
        requestUri:
            description: Request uri if error.
            type: str
            returned: on error
            sample: ''
'''

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.ibm.ibm_zosmf.plugins.module_utils.zmf_util import (
    get_connect_argument_spec,
    get_connect_session,
    cmp_list
)
from ansible_collections.ibm.ibm_zosmf.plugins.module_utils.zmf_sca_api \
    import (
    get_request_argument_spec,
    call_sca_api
)
import io


def validate_descriptor(module):
    # create session
    session = get_connect_session(module)
    # step1 - find workflow instance by name
    # path = module.params['path_of_security_requirements']

    response = call_sca_api(module, session, 'validateDescriptor')

    process_response(response, module)

    # import epdb
    # epdb.serve()


def validate_resource(module):
    path = module.params['path_of_security_requirements']
    body = None
    try:
        with io.open(path, 'r', encoding='utf8') as f_read:
            body = f_read.read()
    except OSError as ex:
        module.fail_json(msg='Failed to read local security requirements: ' + path + ' ---- OS error: ' + str(ex))
    if f_read is not None:
        f_read.close()
    # create session
    session = get_connect_session(module)
    # step1 - find workflow instance by name
    # import epdb
    # epdb.serve()
    response = call_sca_api(module, session, 'validateResource', body)

    process_response(response, module)


def process_response(response, module):
    if isinstance(response, dict):
        unexpected = []
        expected_result = module.params['expected_result'][4:]
        for item in response['resourceItems']:
            if item['status'].lower() != expected_result:
                unexpected.append(item)
        res = {}
        if len(unexpected) > 0:
            res['resourceItems'] = unexpected
            module.fail_json('Security validation does not match with expected_result.', **res)
        else:
            module.exit_json(**res)
    else:
        prefix = 'Failed to validate security requirements:'
        # not found, msg: path of security requirements not found
        if '400' in response and 'not found' in response:
            prefix = 'Path of security requirements not found.'
        module.fail_json(
            msg=prefix + ' ---- ' + response
        )


def run_module():
    # define available arguments/parameters a user can pass to the module
    argument_spec = {}
    connect_argument_spec = get_connect_argument_spec()

    (argument_spec_mapping, request_argument_spec) = \
        get_request_argument_spec()
    argument_spec.update(connect_argument_spec)
    argument_spec.update(request_argument_spec)

    argument_spec.update(
        target_userid=dict(type='str', required=False),
        path_of_security_requirements=dict(type='str', required=True),
        location=dict(type='str', required=False, choices=['zos', 'local'], default='zos'),
        expected_result=dict(type='str', required=False, choices=['all-passed', 'all-failed'], default='all-passed'),
        state=dict(type='str', required=False, choices=['check'], default='check'),

    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)
    # import epdb
    # epdb.serve()
    response = {}
    if module.params['location'] == 'zos':
        validate_descriptor(module)
    else:
        validate_resource(module)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
