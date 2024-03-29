
:github_url: https://github.com/IBM/ibm_zosmf/tree/master/plugins/modules/zmf_authenticate.py

.. _zmf_authenticate_module:


zmf_authenticate -- Authenticate with z/OSMF server
===================================================


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Authenticate with z/OSMF server by either username/password or HTTPS client authenticate.

- Return the authentication credentials for successful authentication.
- The credential can be then used for succeeding Ansible tasks which call z/OSMF Ansible module or role.





Parameters
----------


 

zmf_host
  Hostname of the z/OSMF server.

  | **required**: True
  | **type**: str


 

zmf_port
  Port number of the z/OSMF server.

  | **required**: False
  | **type**: int


 

zmf_user
  User name to be used for authenticating with z/OSMF server.

  Required when *zmf_crt* and *zmf_key* are not supplied.

  If *zmf_crt* and *zmf_key* are supplied, *zmf_user* and *zmf_password* are ignored.


  | **required**: False
  | **type**: str


 

zmf_password
  Password to be used for authenticating with z/OSMF server.

  Required when *zmf_crt* and *zmf_key* are not supplied.

  If *zmf_crt* and *zmf_key* are supplied, *zmf_user* and *zmf_password* are ignored.


  | **required**: False
  | **type**: str


 

zmf_crt
  Location of the PEM-formatted certificate chain file to be used for HTTPS client authentication.


  Required when *zmf_user* and *zmf_password* are not supplied.

  | **required**: False
  | **type**: str


 

zmf_key
  Location of the PEM-formatted file with your private key to be used for HTTPS client authentication.


  Required when *zmf_user* and *zmf_password* are not supplied.

  | **required**: False
  | **type**: str




Examples
--------

.. code-block:: yaml+jinja

   
   - name: Authenticate with z/OSMF server by username/password
     zmf_authenticate:
       zmf_host: "sample.ibm.com"
       zmf_user: "your_username"
       zmf_password: "your_password"

   - name: Authenticate with z/OSMF server by HTTPS client authenticate
     zmf_authenticate:
       zmf_host: "sample.ibm.com"
       zmf_crt: "/file_with_your_certificate_chain.crt"
       zmf_key: "/file_with_your_private_key.key"

   - name: Authenticate with z/OSMF server by prompting to input username/password
     vars_prompt:
       - name: zmf_user
         prompt: "Enter your zOSMF username"
         private: false
       - name: zmf_password
         prompt: "Enter your zOSMF password"
         private: true
     tasks:
       - zmf_authenticate:
           zmf_host: "{{ zmf_host }}"
           zmf_port: "{{ zmf_port }}"
           zmf_user: "{{ zmf_user }}"
           zmf_password: "{{ zmf_password }}"









Return Values
-------------


      changed
        Indicates if any change is made during the module operation.

        | **returned**: always
        | **type**: bool

      ltpa_token_2
        The value of Lightweight Third Party Access (LTPA) token, which supports strong encryption.


        | **returned**: on success
        | **type**: str
        | **sample**: yDS7uJxqrd3h8v5WXq9pf1yPtztQ4JzroZN3XQKF26ZicXgHc7mdzgycMCa......


      jwt_token
        The value of JSON Web token, which supports strong encryption.

        | **returned**: on success
        | **type**: str
        | **sample**: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0b2tlmVhcmVyIiwicie......


      zmf_host
        Hostname of the z/OSMF server.

        | **returned**: on success
        | **type**: str

      zmf_port
        Port number of the z/OSMF server.

        | **returned**: on success
        | **type**: int

