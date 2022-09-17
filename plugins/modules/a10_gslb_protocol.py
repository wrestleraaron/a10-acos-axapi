#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2021 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


DOCUMENTATION = r'''
module: a10_gslb_protocol
description:
    - Specify GSLB Message Protocol parameters
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
    auto_detect:
        description:
        - "Automatically detect SLB Config"
        type: bool
        required: False
    use_mgmt_port:
        description:
        - "Use management port for connections in Shared Partition"
        type: bool
        required: False
    use_mgmt_port_for_all_partitions:
        description:
        - "Use management port for connections in all L3v Partitions"
        type: bool
        required: False
    status_interval:
        description:
        - "Specify GSLB Message Protocol update period (The GSLB Protocol update interval
          (seconds), default is 30)"
        type: int
        required: False
    ping_site:
        description:
        - "name of site or ip address to ping"
        type: str
        required: False
    msg_format_acos_2x:
        description:
        - "Run GSLB Protocol in compatible mode with a ACOS 2.x GSLB peer"
        type: bool
        required: False
    uuid:
        description:
        - "uuid of the object"
        type: str
        required: False
    enable_list:
        description:
        - "Field enable_list"
        type: list
        required: False
        suboptions:
            ntype:
                description:
                - "'controller'= Enable/Disable GSLB protocol as GSLB controller; 'device'=
          Enable/Disable GSLB protocol as site device;"
                type: str
            uuid:
                description:
                - "uuid of the object"
                type: str
    limit:
        description:
        - "Field limit"
        type: dict
        required: False
        suboptions:
            ardt_query:
                description:
                - "Query Messages of Active RDT, default is 200 (Number)"
                type: int
            ardt_response:
                description:
                - "Response Messages of Active RDT, default is 1000 (Number)"
                type: int
            ardt_session:
                description:
                - "Sessions of Active RDT, default is 32768 (Number)"
                type: int
            conn_response:
                description:
                - "Response Messages of Connection Load, default is no limit (Number)"
                type: int
            response:
                description:
                - "Amount of Response Messages, default is 3600 (Number)"
                type: int
            message:
                description:
                - "Amount of Messages, default is 10000 (Number)"
                type: int
            uuid:
                description:
                - "uuid of the object"
                type: str
    secure:
        description:
        - "Field secure"
        type: dict
        required: False
        suboptions:
            action:
                description:
                - "'enable'= Enable Secure; 'disable'= Disable Secure (default); 'enable-
          fallback'= Fall back to non-secure if fail;"
                type: str
            uuid:
                description:
                - "uuid of the object"
                type: str
    oper:
        description:
        - "Field oper"
        type: dict
        required: False
        suboptions:
            session_list:
                description:
                - "Field session_list"
                type: list

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

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.a10.acos_axapi.plugins.module_utils import \
    errors as a10_ex
from ansible_collections.a10.acos_axapi.plugins.module_utils import \
    wrapper as api_client
from ansible_collections.a10.acos_axapi.plugins.module_utils import \
    utils
from ansible_collections.a10.acos_axapi.plugins.module_utils.client import \
    client_factory
from ansible_collections.a10.acos_axapi.plugins.module_utils.kwbl import \
    KW_OUT, translate_blacklist as translateBlacklist


# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["auto_detect", "enable_list", "limit", "msg_format_acos_2x", "oper", "ping_site", "secure", "status_interval", "use_mgmt_port", "use_mgmt_port_for_all_partitions", "uuid", ]


def get_default_argspec():
    return dict(
        ansible_host=dict(type='str', required=True),
        ansible_username=dict(type='str', required=True),
        ansible_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str', default="present", choices=['noop', 'present', 'absent']),
        ansible_port=dict(type='int', choices=[80, 443], required=True),
        a10_partition=dict(type='str', required=False, ),
        a10_device_context_id=dict(type='int', choices=[1, 2, 3, 4, 5, 6, 7, 8], required=False, ),
        get_type=dict(type='str', choices=["single", "list", "oper", "stats"]),
    )


def get_argspec():
    rv = get_default_argspec()
    rv.update({'auto_detect': {'type': 'bool', },
        'use_mgmt_port': {'type': 'bool', },
        'use_mgmt_port_for_all_partitions': {'type': 'bool', },
        'status_interval': {'type': 'int', },
        'ping_site': {'type': 'str', },
        'msg_format_acos_2x': {'type': 'bool', },
        'uuid': {'type': 'str', },
        'enable_list': {'type': 'list', 'ntype': {'type': 'str', 'required': True, 'choices': ['controller', 'device']}, 'uuid': {'type': 'str', }},
        'limit': {'type': 'dict', 'ardt_query': {'type': 'int', }, 'ardt_response': {'type': 'int', }, 'ardt_session': {'type': 'int', }, 'conn_response': {'type': 'int', }, 'response': {'type': 'int', }, 'message': {'type': 'int', }, 'uuid': {'type': 'str', }},
        'secure': {'type': 'dict', 'action': {'type': 'str', 'choices': ['enable', 'disable', 'enable-fallback']}, 'uuid': {'type': 'str', }},
        'oper': {'type': 'dict', 'session_list': {'type': 'list', 'protocol_info': {'type': 'str', }, 'state': {'type': 'str', }, 'session_id': {'type': 'int', }, 'connection_succeeded': {'type': 'int', }, 'connection_failed': {'type': 'int', }, 'open_packet_sent': {'type': 'int', }, 'open_packet_received': {'type': 'int', }, 'open_session_succeeded': {'type': 'int', }, 'open_session_failed': {'type': 'int', }, 'sessions_dropped': {'type': 'int', }, 'retry': {'type': 'int', }, 'update_packet_sent': {'type': 'int', }, 'update_packet_received': {'type': 'int', }, 'keepalive_packet_sent': {'type': 'int', }, 'keepalive_packet_received': {'type': 'int', }, 'notify_packet_sent': {'type': 'int', }, 'notify_packet_received': {'type': 'int', }, 'message_header_error': {'type': 'int', }, 'secure_negotiation_success': {'type': 'int', }, 'secure_negotiation_fail': {'type': 'int', }, 'ssl_handshake_success': {'type': 'int', }, 'ssl_handshake_fail': {'type': 'int', }, 'secure_state': {'type': 'str', }, 'secure_config': {'type': 'str', }}}
    })
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb/protocol"

    f_dict = {}

    return url_base.format(**f_dict)


def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb/protocol"

    f_dict = {}

    return url_base.format(**f_dict)


def report_changes(module, result, existing_config, payload):
    change_results = copy.deepcopy(result)
    if not existing_config:
        change_results["modified_values"].update(**payload)
        return change_results

    config_changes = copy.deepcopy(existing_config)
    for k, v in payload["protocol"].items():
        v = 1 if str(v).lower() == "true" else v
        v = 0 if str(v).lower() == "false" else v

        if config_changes["protocol"].get(k) != v:
            change_results["changed"] = True
            config_changes["protocol"][k] = v

    change_results["modified_values"].update(**config_changes)
    return change_results


def create(module, result, payload={}):
    call_result = api_client.post(module.client, new_url(module), payload)
    result["axapi_calls"].append(call_result)
    result["modified_values"].update(
        **call_result["response_body"])
    result["changed"] = True
    return result


def update(module, result, existing_config, payload={}):
    call_result = api_client.post(module.client, existing_url(module), payload)
    result["axapi_calls"].append(call_result)
    if call_result["response_body"] == existing_config:
        result["changed"] = False
    else:
        result["modified_values"].update(
            **call_result["response_body"])
        result["changed"] = True
    return result


def present(module, result, existing_config):
    payload = utils.build_json("protocol", module.params, AVAILABLE_PROPERTIES)
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
        call_result = api_client.delete(module.client, existing_url(module))
        result["axapi_calls"].append(call_result)
        result["changed"] = True
    except a10_ex.NotFound:
        result["changed"] = False
    return result


def absent(module, result, existing_config):
    if not existing_config:
        result["changed"] = False
        return result

    if module.check_mode:
        result["changed"] = True
        return result

    return delete(module, result)


def run_command(module):
    result = dict(
        changed=False,
        messages="",
        modified_values={},
        axapi_calls=[],
        ansible_facts={},
        acos_info={}
    )

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

    module.client = client_factory(ansible_host, ansible_port,
                                   protocol, ansible_username,
                                   ansible_password)

    valid = True

    run_errors = []
    if state == 'present':
        requires_one_of = sorted([])
        valid, validation_errors = utils.validate(module.params, requires_one_of)
        for ve in validation_errors:
            run_errors.append(ve)

    if not valid:
        err_msg = "\n".join(run_errors)
        result["messages"] = "Validation failure: " + str(run_errors)
        module.fail_json(msg=err_msg, **result)


    try:
        if a10_partition:
            result["axapi_calls"].append(
                api_client.active_partition(module.client, a10_partition))

        if a10_device_context_id:
             result["axapi_calls"].append(
                api_client.switch_device_context(module.client, a10_device_context_id))

        existing_config = api_client.get(module.client, existing_url(module))
        result["axapi_calls"].append(existing_config)
        if existing_config['response_body'] != 'NotFound':
            existing_config = existing_config["response_body"]
        else:
            existing_config = None

        if state == 'present':
            result = present(module, result, existing_config)

        if state == 'absent':
            result = absent(module, result, existing_config)

        if state == 'noop':
            if module.params.get("get_type") == "single":
                get_result = api_client.get(module.client, existing_url(module))
                result["axapi_calls"].append(get_result)
                info = get_result["response_body"]
                result["acos_info"] = info["protocol"] if info != "NotFound" else info
            elif module.params.get("get_type") == "list":
                get_list_result = api_client.get_list(module.client, existing_url(module))
                result["axapi_calls"].append(get_list_result)

                info = get_list_result["response_body"]
                result["acos_info"] = info["protocol-list"] if info != "NotFound" else info
            elif module.params.get("get_type") == "oper":
                get_oper_result = api_client.get_oper(module.client, existing_url(module),
                                                      params=module.params)
                result["axapi_calls"].append(get_oper_result)
                info = get_oper_result["response_body"]
                result["acos_info"] = info["protocol"]["oper"] if info != "NotFound" else info
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    finally:
        if module.client.auth_session.session_id:
            module.client.auth_session.close()

    return result


def main():
    module = AnsibleModule(argument_spec=get_argspec(), supports_check_mode=True)
    result = run_command(module)
    module.exit_json(**result)

if __name__ == '__main__':
    main()
