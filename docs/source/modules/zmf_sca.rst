
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/modules/zmf_sca.py

.. _zmf_sca_module:


zmf_sca -- Automate z/OS security requirements validation and provision
=======================================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module supports automatically validating and provisioning security requirements/configuration based on the security descriptor JSON file.

- This module drives z/OSMF Security Configuration Assistant REST API undercover.




Parameters
----------


 

state
  The desired final state.

  If *state=check*, this module performs security validation for the security requirements specified in path_of_security_requirements.


  If *state=provisioned*, this module performs security provision for the security requirements specified in path_of_security_requirements.


  | **required**: False
  | **type**: str
  | **default**: check
  | **choices**: check, provisioned


 

target_userid
  User ID or group ID to be validated or provisioned for the security requirements documented by the security descriptor JSON file that is specified by the parameter path_of_security_requirements.


  If this parameter is not specified, the current logon user ID is used for validation or provision.


  | **required**: False
  | **type**: str


 

location
  The location of path_of_security_requirements.

  | **required**: False
  | **type**: str
  | **default**: remote
  | **choices**: remote, local


 

path_of_security_requirements
  Absolute path of the security descriptor JSON file that contains the security requirements to be validated or provisioned.


  | **required**: True
  | **type**: str


 

expected_result
  Expected validation result of the security requirements.

  This parameter is ignored when *state=provisioned*

  For all-passed, the module returns success when all security requirements are satisfied. If any requirement is not met or can not be determined, this module fails.


  For all-failed, the module returns success when all security requirements have failed. If any requirement is satisfied or can not be determined, this module fails.


  The value "all-passed" can be used in security validation use cases. The value "all-failed" may be used in security auditing use cases to check if any over permission exists.


  | **required**: False
  | **type**: str
  | **default**: all-passed
  | **choices**: all-failed, all-passed


 

zmf_credential
  Authentication credentials, returned by module **zmf_authenticate**, for successful authentication with the z/OSMF server.


  If *zmf_credential* is supplied, *zmf_host*, *zmf_port*, *zmf_user*, *zmf_password*, *zmf_crt* and *zmf_key* are ignored.


  | **required**: False
  | **type**: dict


 

  ltpa_token_2
    The value of the Lightweight Third Party Access (LTPA) token, which supports strong encryption.


    If *jwt_token* is not supplied, *ltpa_token_2* is required.


    | **required**: False
    | **type**: str


 

  jwt_token
    The value of the JSON web token, which supports strong encryption.


    If *ltpa_token_2* is not supplied, *jwt_token* is required.


    | **required**: False
    | **type**: str


 

  zmf_host
    Hostname of the z/OSMF server.

    | **required**: True
    | **type**: str


 

  zmf_port
    Port number of the z/OSMF server.

    | **required**: False
    | **type**: int



 

zmf_host
  Hostname of the z/OSMF server.

  If *zmf_credential* is supplied, *zmf_host* is ignored.

  If *zmf_credential* is not supplied, *zmf_host* is required.

  | **required**: False
  | **type**: str


 

zmf_port
  Port number of the z/OSMF server.

  If *zmf_credential* is supplied, *zmf_port* is ignored.

  | **required**: False
  | **type**: int


 

zmf_user
  User name to be used for authenticating with z/OSMF server.

  If *zmf_credential* is supplied, *zmf_user* is ignored.

  If *zmf_credential* is not supplied, *zmf_user* is required when *zmf_crt* and *zmf_key* are not supplied.


  If *zmf_credential* is not supplied and *zmf_crt* and *zmf_key* are supplied, *zmf_user* and *zmf_password* are ignored.


  | **required**: False
  | **type**: str


 

zmf_password
  Password to be used for authentication with z/OSMF server.

  If *zmf_credential* is supplied, *zmf_password* is ignored.

  If *zmf_credential* is not supplied, *zmf_password* is required when *zmf_crt* and *zmf_key* are not supplied.


  If *zmf_credential* is not supplied and *zmf_crt* and *zmf_key* are supplied, *zmf_user* and *zmf_password* are ignored.


  | **required**: False
  | **type**: str


 

zmf_crt
  Location of the PEM-formatted certificate chain file to be used for HTTPS client authentication.


  If *zmf_credential* is supplied, *zmf_crt* is ignored.


  If *zmf_credential* is not supplied, *zmf_crt* is required when *zmf_user* and *zmf_password* are not supplied.


  | **required**: False
  | **type**: str


 

zmf_key
  Location of the PEM-formatted file with your private key to be used for HTTPS client authentication.


  If *zmf_credential* is supplied, *zmf_key* is ignored.

  If *zmf_credential* is not supplied, *zmf_key* is required when *zmf_user* and *zmf_password* are not supplied.


  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Authenticate with the z/OSMF server by username/password, and register the result for later use.
     zmf_authenticate:
       zmf_host: "{{ zmf_host }}"
       zmf_port: "{{ zmf_port }}"
       zmf_user: "{{ zmf_user }}"
       zmf_password: "{{ zmf_password }}"
     register: result_auth

   - name: Validate security requirements defined in a z/OS security descriptor file and \
           expect all requirements are satisfied.
     ibm.ibm_zosmf.zmf_sca:
       zmf_credential: "{{ result_auth }}"
       target_userid: IBMUSER
       path_of_security_requirements: /global/zosmf/sample/configuration/security/descriptor.json

   - name: Validate security requirements defined in a local (Ansible control node) security descriptor file\
           and expect no access to any items.
     ibm.ibm_zosmf.zmf_sca:
       zmf_credential: "{{ result_auth }}"
       target_userid: IBMUSER
       path_of_security_requirements: /home/user/descriptor.json
       location: local
       expected_result: all-failed

   - name: Provision security requirements defined in a z/OS security descriptor file and \
           expect all requirements are satisfied.
     ibm.ibm_zosmf.zmf_sca:
       zmf_credential: "{{ result_auth }}"
       state: provisioned
       target_userid: IBMUSER
       path_of_security_requirements: /global/zosmf/sample/configuration/security/descriptor.json

   - name: Provision resources defined in a local (Ansible control node) security descriptor file and \
           expect all requirements are satisfied.
     ibm.ibm_zosmf.zmf_sca:
       zmf_credential: "{{ result_auth }}"
       state: provisioned
       target_userid: IBMUSER
       path_of_security_requirements: /home/user/descriptor.json
       location: local









Return Values
-------------


      changed
        Indicates whether any change is made during the module operation.

        | **returned**: always
        | **type**: bool

      msg
        Error message.

        | **returned**: always on error
        | **type**: str

      resourceItems
        Array of security requirements that need attention.

        If `state=check`, indicate security requirements which do not match with the expected result.

        If `state=provisioned`, indicate security requirements that are failed to provision.

        | **returned**: always on fail
        | **type**: list
        | **elements**: dict

        itemId
          Item ID.

          | **type**: str
          | **sample**: 5695DF18658I10001000


        itemType
          Item type.

          | **type**: str
          | **sample**: PROGRAMMABLE


        itemCategory
          Item category.

          | **type**: str
          | **sample**: CHANGEDATASET VX


        itemDescription
          Item description.

          | **type**: str
          | **sample**: DFSMSrmm inventory management CHANGEDATASET VX command protection.


        resourceProfile
          Name of the security resource profile.

          At current stage,

          Variable in the name is not supported.

          Generic resource name is not supported.

          | **returned**: always
          | **type**: str
          | **sample**: STGADMIN.EDG.CD.VX


        resourceClass
          SAF resource class.

          | **returned**: always
          | **type**: str
          | **sample**: FACILITY


        access
          Level of access that is required for the security resource for the specified user ID or group ID.

          Value can be the following

          | **returned**: always
          | **type**: str
          | **sample**: ['READ', 'UPDATE', 'CONTROL', 'ALTER']


        action
          \"validate\" will be returned if SCA only did validation for this security requirement.

          \"provision\" will be returned if SCA provisioned the security requirement.

          | **returned**: always
          | **type**: str
          | **sample**: ['validate', 'provision']


        actionObjectId
          The object ID of this action. For validation action, this ID is the same as validatedId below.

          This field can also be used for other actions in future versions.

          | **returned**: always
          | **type**: str

        validatedId
          User ID or group ID that is used for resource validation.

          | **returned**: always
          | **type**: str

        status
          Validation result

          | **returned**: always
          | **type**: str
          | **sample**: ['Passed', 'Failed', 'Unknown']


        additionalInfo
          Additional info.

          | **type**: str

        whoNeedsAccess
          Users (security groups) who require access to this resource.

          The Security Configuration Assistant does not verify that security groups are defined;

          your security administrator must verify that the groups exist.

          | **type**: str
          | **sample**: <Inventory Management>


        messageId
          Message Id.

          | **type**: str

        messageText
          Message text.

          | **type**: str

        httpStatus
          http status code if error.

          | **returned**: on error
          | **type**: str

        requestMethod
          http request method if error.

          | **returned**: on error
          | **type**: str

        requestUri
          Request uri if error.

          | **returned**: on error
          | **type**: str


