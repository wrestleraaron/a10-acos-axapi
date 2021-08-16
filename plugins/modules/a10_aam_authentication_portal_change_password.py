#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2021 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_aam_authentication_portal_change_password
description:
    - Change password page configuration
author: A10 Networks 2021
options:
    state:
        description:
        - State of the object to be created.
        choices:
          - noop
          - present
          - absent
        type: str
        required: True
    ansible_host:
        description:
        - Host for AXAPI authentication
        type: str
        required: True
    ansible_username:
        description:
        - Username for AXAPI authentication
        type: str
        required: True
    ansible_password:
        description:
        - Password for AXAPI authentication
        type: str
        required: True
    ansible_port:
        description:
        - Port for AXAPI authentication
        type: int
        required: True
    a10_device_context_id:
        description:
        - Device ID for aVCS configuration
        choices: [1-8]
        type: int
        required: False
    a10_partition:
        description:
        - Destination/target partition for object/command
        type: str
        required: False
    portal_name:
        description:
        - Key to identify parent object
        type: str
        required: True
    background:
        description:
        - "Field background"
        type: dict
        required: False
        suboptions:
            bgfile:
                description:
                - "Specify background image filename"
                type: str
            bgstyle:
                description:
                - "'tile'= Tile; 'stretch'= Stretch; 'fit'= Fit;"
                type: str
            bgcolor_name:
                description:
                - "'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray;
          'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive;
          'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal;
          'white'= white; 'yellow'= yellow;"
                type: str
            bgcolor_value:
                description:
                - "Specify 6-digit HEX color value"
                type: str
    title_cfg:
        description:
        - "Field title_cfg"
        type: dict
        required: False
        suboptions:
            title:
                description:
                - "Configure title in default change password page"
                type: bool
            title_text:
                description:
                - "Specify title (Default= Please Change Your Password)"
                type: str
            title_font:
                description:
                - "Sepcify font (Default= Arial)"
                type: bool
            title_face:
                description:
                - "'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia;
          'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;"
                type: str
            title_font_custom:
                description:
                - "Specify custom font"
                type: str
            title_size:
                description:
                - "Specify font size (Default= 5)"
                type: int
            title_color:
                description:
                - "Specify font color (Default= black)"
                type: bool
            title_color_name:
                description:
                - "'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray;
          'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive;
          'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal;
          'white'= white; 'yellow'= yellow;"
                type: str
            title_color_value:
                description:
                - "Specify 6-digit HEX color value"
                type: str
    action_url:
        description:
        - "Specify form action URL in default change password page (Default= /change.fo)"
        type: str
        required: False
    username_cfg:
        description:
        - "Field username_cfg"
        type: dict
        required: False
        suboptions:
            username:
                description:
                - "Configure username text in default change password page"
                type: bool
            user_text:
                description:
                - "Specify username text (Default= Username)"
                type: str
            user_font:
                description:
                - "Sepcify font (Default= Arial)"
                type: bool
            user_face:
                description:
                - "'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia;
          'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;"
                type: str
            user_font_custom:
                description:
                - "Specify custom font"
                type: str
            user_size:
                description:
                - "Specify font size (Default= 3)"
                type: int
            user_color:
                description:
                - "Specify font color (Default= black)"
                type: bool
            user_color_name:
                description:
                - "'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray;
          'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive;
          'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal;
          'white'= white; 'yellow'= yellow;"
                type: str
            user_color_value:
                description:
                - "Specify 6-digit HEX color value"
                type: str
    username_var:
        description:
        - "Specify username variable name in default change password page (Default=
          cp_usr)"
        type: str
        required: False
    old_pwd_cfg:
        description:
        - "Field old_pwd_cfg"
        type: dict
        required: False
        suboptions:
            old_password:
                description:
                - "Configure old password text in default change password page"
                type: bool
            old_text:
                description:
                - "Specify old password text (Default= Old Password)"
                type: str
            old_font:
                description:
                - "Sepcify font (Default= Arial)"
                type: bool
            old_face:
                description:
                - "'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia;
          'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;"
                type: str
            old_font_custom:
                description:
                - "Specify custom font"
                type: str
            old_size:
                description:
                - "Specify font size (Default= 3)"
                type: int
            old_color:
                description:
                - "Specify font color (Default= black)"
                type: bool
            old_color_name:
                description:
                - "'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray;
          'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive;
          'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal;
          'white'= white; 'yellow'= yellow;"
                type: str
            old_color_value:
                description:
                - "Specify 6-digit HEX color value"
                type: str
    old_password_var:
        description:
        - "Specify old password variable name in default change password page (Default=
          cp_old_pwd)"
        type: str
        required: False
    new_pwd_cfg:
        description:
        - "Field new_pwd_cfg"
        type: dict
        required: False
        suboptions:
            new_password:
                description:
                - "Configure new password text in default change password page"
                type: bool
            new_text:
                description:
                - "Specify new password text (Default= New Password)"
                type: str
            new_font:
                description:
                - "Sepcify font (Default= Arial)"
                type: bool
            new_face:
                description:
                - "'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia;
          'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;"
                type: str
            new_font_custom:
                description:
                - "Specify custom font"
                type: str
            new_size:
                description:
                - "Specify font size (Default= 3)"
                type: int
            new_color:
                description:
                - "Specify font color (Default= black)"
                type: bool
            new_color_name:
                description:
                - "'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray;
          'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive;
          'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal;
          'white'= white; 'yellow'= yellow;"
                type: str
            new_color_value:
                description:
                - "Specify 6-digit HEX color value"
                type: str
    new_password_var:
        description:
        - "Specify new password variable name in default change password page (Default=
          cp_new_pwd)"
        type: str
        required: False
    cfm_pwd_cfg:
        description:
        - "Field cfm_pwd_cfg"
        type: dict
        required: False
        suboptions:
            confirm_password:
                description:
                - "Configure confirm password text in default change password page"
                type: bool
            cfm_text:
                description:
                - "Specify confirm password text (Default= Confirm New Password)"
                type: str
            cfm_font:
                description:
                - "Sepcify font (Default= Arial)"
                type: bool
            cfm_face:
                description:
                - "'Arial'= Arial; 'Courier_New'= Courier New; 'Georgia'= Georgia;
          'Times_New_Roman'= Times New Roman; 'Verdana'= Verdana;"
                type: str
            cfm_font_custom:
                description:
                - "Specify custom font"
                type: str
            cfm_size:
                description:
                - "Specify font size (Default= 3)"
                type: int
            cfm_color:
                description:
                - "Specify font color (Default= black)"
                type: bool
            cfm_color_name:
                description:
                - "'aqua'= aqua; 'black'= black; 'blue'= blue; 'fuchsia'= fuchsia; 'gray'= gray;
          'green'= green; 'lime'= lime; 'maroon'= maroon; 'navy'= navy; 'olive'= olive;
          'orange'= orange; 'purple'= purple; 'red'= red; 'silver'= silver; 'teal'= teal;
          'white'= white; 'yellow'= yellow;"
                type: str
            cfm_color_value:
                description:
                - "Specify 6-digit HEX color value"
                type: str
    confirm_password_var:
        description:
        - "Specify confirm password variable name in default change password page
          (Default= cp_cfm_pwd)"
        type: str
        required: False
    submit_text:
        description:
        - "Specify submit button text in default change password page (Default= Submit)"
        type: str
        required: False
    reset_text:
        description:
        - "Specify reset button text in default change password page (Default= Reset)"
        type: str
        required: False
    uuid:
        description:
        - "uuid of the object"
        type: str
        required: False

'''

RETURN = r'''
modified_values:
    description:
    - Values modified (or potential changes if using check_mode) as a result of task operation
    returned: changed
    type: dict
axapi_calls:
    description: Sequential list of AXAPI calls made by the task
    returned: always
    type: list
    elements: dict
    contains:
        endpoint:
            description: The AXAPI endpoint being accessed.
            type: str
            sample:
                - /axapi/v3/slb/virtual_server
                - /axapi/v3/file/ssl-cert
        http_method:
            description:
            - HTTP method being used by the primary task to interact with the AXAPI endpoint.
            type: str
            sample:
                - POST
                - GET
        request_body:
            description: Params used to query the AXAPI
            type: complex
        response_body:
            description: Response from the AXAPI
            type: complex
'''

EXAMPLES = """
"""

import copy

# standard ansible module imports
from ansible.module_utils.basic import AnsibleModule

from ansible_collections.a10.acos_axapi.plugins.module_utils import \
    errors as a10_ex
from ansible_collections.a10.acos_axapi.plugins.module_utils.axapi_http import \
    client_factory
from ansible_collections.a10.acos_axapi.plugins.module_utils.kwbl import \
    KW_OUT, translate_blacklist as translateBlacklist

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'supported_by': 'community',
    'status': ['preview']
}

# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = [
    "action_url",
    "background",
    "cfm_pwd_cfg",
    "confirm_password_var",
    "new_password_var",
    "new_pwd_cfg",
    "old_password_var",
    "old_pwd_cfg",
    "reset_text",
    "submit_text",
    "title_cfg",
    "username_cfg",
    "username_var",
    "uuid",
]


def get_default_argspec():
    return dict(
        ansible_host=dict(type='str', required=True),
        ansible_username=dict(type='str', required=True),
        ansible_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str',
                   default="present",
                   choices=['noop', 'present', 'absent']),
        ansible_port=dict(type='int', choices=[80, 443], required=True),
        a10_partition=dict(
            type='str',
            required=False,
        ),
        a10_device_context_id=dict(
            type='int',
            choices=[1, 2, 3, 4, 5, 6, 7, 8],
            required=False,
        ),
        get_type=dict(type='str', choices=["single", "list", "oper", "stats"]),
    )


def get_argspec():
    rv = get_default_argspec()
    rv.update({
        'background': {
            'type': 'dict',
            'bgfile': {
                'type': 'str',
            },
            'bgstyle': {
                'type': 'str',
                'choices': ['tile', 'stretch', 'fit']
            },
            'bgcolor_name': {
                'type':
                'str',
                'choices': [
                    'aqua', 'black', 'blue', 'fuchsia', 'gray', 'green',
                    'lime', 'maroon', 'navy', 'olive', 'orange', 'purple',
                    'red', 'silver', 'teal', 'white', 'yellow'
                ]
            },
            'bgcolor_value': {
                'type': 'str',
            }
        },
        'title_cfg': {
            'type': 'dict',
            'title': {
                'type': 'bool',
            },
            'title_text': {
                'type': 'str',
            },
            'title_font': {
                'type': 'bool',
            },
            'title_face': {
                'type':
                'str',
                'choices': [
                    'Arial', 'Courier_New', 'Georgia', 'Times_New_Roman',
                    'Verdana'
                ]
            },
            'title_font_custom': {
                'type': 'str',
            },
            'title_size': {
                'type': 'int',
            },
            'title_color': {
                'type': 'bool',
            },
            'title_color_name': {
                'type':
                'str',
                'choices': [
                    'aqua', 'black', 'blue', 'fuchsia', 'gray', 'green',
                    'lime', 'maroon', 'navy', 'olive', 'orange', 'purple',
                    'red', 'silver', 'teal', 'white', 'yellow'
                ]
            },
            'title_color_value': {
                'type': 'str',
            }
        },
        'action_url': {
            'type': 'str',
        },
        'username_cfg': {
            'type': 'dict',
            'username': {
                'type': 'bool',
            },
            'user_text': {
                'type': 'str',
            },
            'user_font': {
                'type': 'bool',
            },
            'user_face': {
                'type':
                'str',
                'choices': [
                    'Arial', 'Courier_New', 'Georgia', 'Times_New_Roman',
                    'Verdana'
                ]
            },
            'user_font_custom': {
                'type': 'str',
            },
            'user_size': {
                'type': 'int',
            },
            'user_color': {
                'type': 'bool',
            },
            'user_color_name': {
                'type':
                'str',
                'choices': [
                    'aqua', 'black', 'blue', 'fuchsia', 'gray', 'green',
                    'lime', 'maroon', 'navy', 'olive', 'orange', 'purple',
                    'red', 'silver', 'teal', 'white', 'yellow'
                ]
            },
            'user_color_value': {
                'type': 'str',
            }
        },
        'username_var': {
            'type': 'str',
        },
        'old_pwd_cfg': {
            'type': 'dict',
            'old_password': {
                'type': 'bool',
            },
            'old_text': {
                'type': 'str',
            },
            'old_font': {
                'type': 'bool',
            },
            'old_face': {
                'type':
                'str',
                'choices': [
                    'Arial', 'Courier_New', 'Georgia', 'Times_New_Roman',
                    'Verdana'
                ]
            },
            'old_font_custom': {
                'type': 'str',
            },
            'old_size': {
                'type': 'int',
            },
            'old_color': {
                'type': 'bool',
            },
            'old_color_name': {
                'type':
                'str',
                'choices': [
                    'aqua', 'black', 'blue', 'fuchsia', 'gray', 'green',
                    'lime', 'maroon', 'navy', 'olive', 'orange', 'purple',
                    'red', 'silver', 'teal', 'white', 'yellow'
                ]
            },
            'old_color_value': {
                'type': 'str',
            }
        },
        'old_password_var': {
            'type': 'str',
        },
        'new_pwd_cfg': {
            'type': 'dict',
            'new_password': {
                'type': 'bool',
            },
            'new_text': {
                'type': 'str',
            },
            'new_font': {
                'type': 'bool',
            },
            'new_face': {
                'type':
                'str',
                'choices': [
                    'Arial', 'Courier_New', 'Georgia', 'Times_New_Roman',
                    'Verdana'
                ]
            },
            'new_font_custom': {
                'type': 'str',
            },
            'new_size': {
                'type': 'int',
            },
            'new_color': {
                'type': 'bool',
            },
            'new_color_name': {
                'type':
                'str',
                'choices': [
                    'aqua', 'black', 'blue', 'fuchsia', 'gray', 'green',
                    'lime', 'maroon', 'navy', 'olive', 'orange', 'purple',
                    'red', 'silver', 'teal', 'white', 'yellow'
                ]
            },
            'new_color_value': {
                'type': 'str',
            }
        },
        'new_password_var': {
            'type': 'str',
        },
        'cfm_pwd_cfg': {
            'type': 'dict',
            'confirm_password': {
                'type': 'bool',
            },
            'cfm_text': {
                'type': 'str',
            },
            'cfm_font': {
                'type': 'bool',
            },
            'cfm_face': {
                'type':
                'str',
                'choices': [
                    'Arial', 'Courier_New', 'Georgia', 'Times_New_Roman',
                    'Verdana'
                ]
            },
            'cfm_font_custom': {
                'type': 'str',
            },
            'cfm_size': {
                'type': 'int',
            },
            'cfm_color': {
                'type': 'bool',
            },
            'cfm_color_name': {
                'type':
                'str',
                'choices': [
                    'aqua', 'black', 'blue', 'fuchsia', 'gray', 'green',
                    'lime', 'maroon', 'navy', 'olive', 'orange', 'purple',
                    'red', 'silver', 'teal', 'white', 'yellow'
                ]
            },
            'cfm_color_value': {
                'type': 'str',
            }
        },
        'confirm_password_var': {
            'type': 'str',
        },
        'submit_text': {
            'type': 'str',
        },
        'reset_text': {
            'type': 'str',
        },
        'uuid': {
            'type': 'str',
        }
    })
    # Parent keys
    rv.update(dict(portal_name=dict(type='str', required=True), ))
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/aam/authentication/portal/{portal_name}/change-password"

    f_dict = {}
    f_dict["portal_name"] = module.params["portal_name"]

    return url_base.format(**f_dict)


def list_url(module):
    """Return the URL for a list of resources"""
    ret = existing_url(module)
    return ret[0:ret.rfind('/')]


def _get(module, url, params={}):

    resp = None
    try:
        resp = module.client.get(url, params=params)
    except a10_ex.NotFound:
        resp = "Not Found"

    call_result = {
        "endpoint": url,
        "http_method": "GET",
        "request_body": params,
        "response_body": resp,
    }
    return call_result


def _post(module, url, params={}, file_content=None, file_name=None):
    resp = module.client.post(url, params=params)
    resp = resp if resp else {}
    call_result = {
        "endpoint": url,
        "http_method": "POST",
        "request_body": params,
        "response_body": resp,
    }
    return call_result


def _delete(module, url):
    call_result = {
        "endpoint": url,
        "http_method": "DELETE",
        "request_body": {},
        "response_body": module.client.delete(url),
    }
    return call_result


def _switch_device_context(module, device_id):
    call_result = {
        "endpoint": "/axapi/v3/device-context",
        "http_method": "POST",
        "request_body": {
            "device-id": device_id
        },
        "response_body": module.client.change_context(device_id)
    }
    return call_result


def _active_partition(module, a10_partition):
    call_result = {
        "endpoint": "/axapi/v3/active-partition",
        "http_method": "POST",
        "request_body": {
            "curr_part_name": a10_partition
        },
        "response_body": module.client.activate_partition(a10_partition)
    }
    return call_result


def get(module):
    return _get(module, existing_url(module))


def get_list(module):
    return _get(module, list_url(module))


def _to_axapi(key):
    return translateBlacklist(key, KW_OUT).replace("_", "-")


def _build_dict_from_param(param):
    rv = {}

    for k, v in param.items():
        hk = _to_axapi(k)
        if isinstance(v, dict):
            v_dict = _build_dict_from_param(v)
            rv[hk] = v_dict
        elif isinstance(v, list):
            nv = [_build_dict_from_param(x) for x in v]
            rv[hk] = nv
        else:
            rv[hk] = v

    return rv


def build_envelope(title, data):
    return {title: data}


def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/aam/authentication/portal/{portal_name}/change-password"

    f_dict = {}
    f_dict["portal_name"] = module.params["portal_name"]

    return url_base.format(**f_dict)


def validate(params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([
        x for x in requires_one_of if x in params and params.get(x) is not None
    ])

    errors = []
    marg = []

    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc, msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc, msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc, msg = REQUIRED_VALID

    if not rc:
        errors.append(msg.format(", ".join(marg)))

    return rc, errors


def build_json(title, module):
    rv = {}

    for x in AVAILABLE_PROPERTIES:
        v = module.params.get(x)
        if v is not None:
            rx = _to_axapi(x)

            if isinstance(v, dict):
                nv = _build_dict_from_param(v)
                rv[rx] = nv
            elif isinstance(v, list):
                nv = [_build_dict_from_param(x) for x in v]
                rv[rx] = nv
            else:
                rv[rx] = module.params[x]

    return build_envelope(title, rv)


def report_changes(module, result, existing_config, payload):
    change_results = copy.deepcopy(result)
    if not existing_config:
        change_results["modified_values"].update(**payload)
        return change_results

    config_changes = copy.deepcopy(existing_config)
    for k, v in payload["change-password"].items():
        v = 1 if str(v).lower() == "true" else v
        v = 0 if str(v).lower() == "false" else v

        if config_changes["change-password"].get(k) != v:
            change_results["changed"] = True
            config_changes["change-password"][k] = v

    change_results["modified_values"].update(**config_changes)
    return change_results


def create(module, result, payload):
    try:
        call_result = _post(module, new_url(module), payload)
        result["axapi_calls"].append(call_result)
        result["modified_values"].update(**call_result["response_body"])
        result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result


def update(module, result, existing_config, payload):
    try:
        call_result = _post(module, existing_url(module), payload)
        result["axapi_calls"].append(call_result)
        if call_result["response_body"] == existing_config:
            result["changed"] = False
        else:
            result["modified_values"].update(**call_result["response_body"])
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result


def present(module, result, existing_config):
    payload = build_json("change-password", module)
    change_results = report_changes(module, result, existing_config, payload)
    if module.check_mode:
        return change_results
    elif not existing_config:
        return create(module, result, payload)
    elif existing_config and change_results.get('changed'):
        return update(module, result, existing_config, payload)
    return result


def delete(module, result):
    try:
        call_result = _delete(module, existing_url(module))
        result["axapi_calls"].append(call_result)
        result["changed"] = True
    except a10_ex.NotFound:
        result["changed"] = False
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result


def absent(module, result, existing_config):
    if not existing_config:
        result["changed"] = False
        return result

    if module.check_mode:
        result["changed"] = True
        return result

    return delete(module, result)


def replace(module, result, existing_config, payload):
    try:
        post_result = module.client.put(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result


def run_command(module):
    result = dict(changed=False,
                  messages="",
                  modified_values={},
                  axapi_calls=[])

    state = module.params["state"]
    ansible_host = module.params["ansible_host"]
    ansible_username = module.params["ansible_username"]
    ansible_password = module.params["ansible_password"]
    ansible_port = module.params["ansible_port"]
    a10_partition = module.params["a10_partition"]
    a10_device_context_id = module.params["a10_device_context_id"]

    if ansible_port == 80:
        protocol = "http"
    elif ansible_port == 443:
        protocol = "https"

    valid = True

    run_errors = []
    if state == 'present':
        valid, validation_errors = validate(module.params)
        for ve in validation_errors:
            run_errors.append(ve)

    if not valid:
        err_msg = "\n".join(run_errors)
        result["messages"] = "Validation failure: " + str(run_errors)
        module.fail_json(msg=err_msg, **result)

    module.client = client_factory(ansible_host, ansible_port, protocol,
                                   ansible_username, ansible_password)

    if a10_partition:
        result["axapi_calls"].append(_active_partition(module, a10_partition))

    if a10_device_context_id:
        result["axapi_calls"].append(
            _switch_device_context(module, a10_device_context_id))

    existing_config = get(module)
    result["axapi_calls"].append(existing_config)
    if existing_config['response_body'] != 'Not Found':
        existing_config = existing_config["response_body"]
    else:
        existing_config = None

    if state == 'present':
        result = present(module, result, existing_config)

    if state == 'absent':
        result = absent(module, result, existing_config)

    if state == 'noop':
        if module.params.get("get_type") == "single":
            result["axapi_calls"].append(get(module))
        elif module.params.get("get_type") == "list":
            result["axapi_calls"].append(get_list(module))
    module.client.session.close()
    return result


def main():
    module = AnsibleModule(argument_spec=get_argspec(),
                           supports_check_mode=True)
    result = run_command(module)
    module.exit_json(**result)


if __name__ == '__main__':
    main()
