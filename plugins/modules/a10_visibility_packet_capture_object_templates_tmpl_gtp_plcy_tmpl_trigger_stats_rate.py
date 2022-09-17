#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2021 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


DOCUMENTATION = r'''
module: a10_visibility_packet_capture_object_templates_tmpl_gtp_plcy_tmpl_trigger_stats_rate
description:
    - Configure stats to triggers packet capture on increment
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
    tmpl_gtp_plcy_tmpl_name:
        description:
        - Key to identify parent object
        type: str
        required: True
    threshold_exceeded_by:
        description:
        - "Set the threshold to the number of times greater than the previous duration to
          start the capture, default is 5"
        type: int
        required: False
    duration:
        description:
        - "Time in seconds to look for the anomaly, default is 60"
        type: int
        required: False
    drop_vld_gtp_ie_repeat_count_exceed:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTP repeated IE count
          exceeded"
        type: bool
        required: False
    drop_vld_reserved_field_set:
        description:
        - "Enable automatic packet-capture for Validation Drop= Reserved Header Field Set"
        type: bool
        required: False
    drop_vld_tunnel_id_flag:
        description:
        - "Enable automatic packet-capture for Validation Drop= Tunnel Header Flag Not Set"
        type: bool
        required: False
    drop_vld_invalid_flow_label_v0:
        description:
        - "Enable automatic packet-capture for Validation Drop= Invalid Flow Label in
          GTPv0-C Header"
        type: bool
        required: False
    drop_vld_invalid_teid:
        description:
        - "Enable automatic packet-capture for Validation Drop= Invalid TEID Value"
        type: bool
        required: False
    drop_vld_out_of_state:
        description:
        - "Enable automatic packet-capture for Validation Drop= Out Of State GTP Message"
        type: bool
        required: False
    drop_vld_mandatory_information_element:
        description:
        - "Enable automatic packet-capture for Validation Drop= Mandatory IE Not Present"
        type: bool
        required: False
    drop_vld_mandatory_ie_in_grouped_ie:
        description:
        - "Enable automatic packet-capture for Validation Drop= Mandatory IE in Grouped IE
          Not Present"
        type: bool
        required: False
    drop_vld_out_of_order_ie:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTPv1-C Message Out of
          Order IE"
        type: bool
        required: False
    drop_vld_out_of_state_ie:
        description:
        - "Enable automatic packet-capture for Validation Drop= Unexpected IE Present in
          Message"
        type: bool
        required: False
    drop_vld_reserved_information_element:
        description:
        - "Enable automatic packet-capture for Validation Drop= Reserved IE Field Present"
        type: bool
        required: False
    drop_vld_version_not_supported:
        description:
        - "Enable automatic packet-capture for Validation Drop= Invalid GTP version"
        type: bool
        required: False
    drop_vld_message_length:
        description:
        - "Enable automatic packet-capture for Validation Drop= Message Length Exceeded"
        type: bool
        required: False
    drop_vld_cross_layer_correlation:
        description:
        - "Enable automatic packet-capture for Validation Drop= Cross Layer IP Address
          Mismatch"
        type: bool
        required: False
    drop_vld_country_code_mismatch:
        description:
        - "Enable automatic packet-capture for Validation Drop= Country Code Mismatch in
          IMSI and MSISDN"
        type: bool
        required: False
    drop_vld_gtp_u_spoofed_source_address:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTP-U IP Address Spoofed"
        type: bool
        required: False
    drop_vld_gtp_bearer_count_exceed:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTP Bearer count exceeded
          max (11)"
        type: bool
        required: False
    drop_vld_gtp_v2_wrong_lbi_create_bearer:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTPV2-C Wrong LBI in
          Create Bearer Request"
        type: bool
        required: False
    drop_vld_gtp_c_handover_in_progress:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTP-C Drop Since Handover
          In Progress"
        type: bool
        required: False
    drop_vld_v0_reserved_message_drop:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTPv0-C Reserved Message
          Drop"
        type: bool
        required: False
    drop_vld_v1_reserved_message_drop:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTPv1-C Reserved Message
          Drop"
        type: bool
        required: False
    drop_vld_v2_reserved_message_drop:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTPv2-C Reserved Message
          Drop"
        type: bool
        required: False
    drop_vld_invalid_pkt_len_piggyback:
        description:
        - "Enable automatic packet-capture for Validation Drop= Piggyback message invalid
          packet length"
        type: bool
        required: False
    drop_vld_sanity_failed_piggyback:
        description:
        - "Enable automatic packet-capture for Validation Drop= piggyback message anomaly
          failed"
        type: bool
        required: False
    drop_vld_sequence_num_correlation:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTP-C Sequence number
          Mismatch"
        type: bool
        required: False
    drop_vld_gtpv0_seqnum_buffer_full:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTPV0-C conn Sequence
          number Buffer Full"
        type: bool
        required: False
    drop_vld_gtpv1_seqnum_buffer_full:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTPV1-C conn Sequence
          number Buffer Full"
        type: bool
        required: False
    drop_vld_gtpv2_seqnum_buffer_full:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTPV2-C conn Sequence
          number Buffer Full"
        type: bool
        required: False
    drop_vld_gtp_invalid_imsi_len_drop:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTP-C Invalid IMSI Length
          Drop"
        type: bool
        required: False
    drop_vld_gtp_invalid_apn_len_drop:
        description:
        - "Enable automatic packet-capture for Validation Drop= GTP-C Invalid APN Length
          Drop"
        type: bool
        required: False
    drop_vld_protocol_flag_unset:
        description:
        - "Enable automatic packet-capture for Validation Drop= Protocol flag in Header
          Field not Set"
        type: bool
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
AVAILABLE_PROPERTIES = ["drop_vld_country_code_mismatch", "drop_vld_cross_layer_correlation", "drop_vld_gtp_bearer_count_exceed", "drop_vld_gtp_c_handover_in_progress", "drop_vld_gtp_ie_repeat_count_exceed", "drop_vld_gtp_invalid_apn_len_drop", "drop_vld_gtp_invalid_imsi_len_drop", "drop_vld_gtp_u_spoofed_source_address", "drop_vld_gtp_v2_wrong_lbi_create_bearer", "drop_vld_gtpv0_seqnum_buffer_full", "drop_vld_gtpv1_seqnum_buffer_full", "drop_vld_gtpv2_seqnum_buffer_full", "drop_vld_invalid_flow_label_v0", "drop_vld_invalid_pkt_len_piggyback", "drop_vld_invalid_teid", "drop_vld_mandatory_ie_in_grouped_ie", "drop_vld_mandatory_information_element", "drop_vld_message_length", "drop_vld_out_of_order_ie", "drop_vld_out_of_state", "drop_vld_out_of_state_ie", "drop_vld_protocol_flag_unset", "drop_vld_reserved_field_set", "drop_vld_reserved_information_element", "drop_vld_sanity_failed_piggyback", "drop_vld_sequence_num_correlation", "drop_vld_tunnel_id_flag", "drop_vld_v0_reserved_message_drop", "drop_vld_v1_reserved_message_drop", "drop_vld_v2_reserved_message_drop", "drop_vld_version_not_supported", "duration", "threshold_exceeded_by", "uuid", ]


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
    rv.update({'threshold_exceeded_by': {'type': 'int', },
        'duration': {'type': 'int', },
        'drop_vld_gtp_ie_repeat_count_exceed': {'type': 'bool', },
        'drop_vld_reserved_field_set': {'type': 'bool', },
        'drop_vld_tunnel_id_flag': {'type': 'bool', },
        'drop_vld_invalid_flow_label_v0': {'type': 'bool', },
        'drop_vld_invalid_teid': {'type': 'bool', },
        'drop_vld_out_of_state': {'type': 'bool', },
        'drop_vld_mandatory_information_element': {'type': 'bool', },
        'drop_vld_mandatory_ie_in_grouped_ie': {'type': 'bool', },
        'drop_vld_out_of_order_ie': {'type': 'bool', },
        'drop_vld_out_of_state_ie': {'type': 'bool', },
        'drop_vld_reserved_information_element': {'type': 'bool', },
        'drop_vld_version_not_supported': {'type': 'bool', },
        'drop_vld_message_length': {'type': 'bool', },
        'drop_vld_cross_layer_correlation': {'type': 'bool', },
        'drop_vld_country_code_mismatch': {'type': 'bool', },
        'drop_vld_gtp_u_spoofed_source_address': {'type': 'bool', },
        'drop_vld_gtp_bearer_count_exceed': {'type': 'bool', },
        'drop_vld_gtp_v2_wrong_lbi_create_bearer': {'type': 'bool', },
        'drop_vld_gtp_c_handover_in_progress': {'type': 'bool', },
        'drop_vld_v0_reserved_message_drop': {'type': 'bool', },
        'drop_vld_v1_reserved_message_drop': {'type': 'bool', },
        'drop_vld_v2_reserved_message_drop': {'type': 'bool', },
        'drop_vld_invalid_pkt_len_piggyback': {'type': 'bool', },
        'drop_vld_sanity_failed_piggyback': {'type': 'bool', },
        'drop_vld_sequence_num_correlation': {'type': 'bool', },
        'drop_vld_gtpv0_seqnum_buffer_full': {'type': 'bool', },
        'drop_vld_gtpv1_seqnum_buffer_full': {'type': 'bool', },
        'drop_vld_gtpv2_seqnum_buffer_full': {'type': 'bool', },
        'drop_vld_gtp_invalid_imsi_len_drop': {'type': 'bool', },
        'drop_vld_gtp_invalid_apn_len_drop': {'type': 'bool', },
        'drop_vld_protocol_flag_unset': {'type': 'bool', },
        'uuid': {'type': 'str', }
    })
    # Parent keys
    rv.update(dict(
        tmpl_gtp_plcy_tmpl_name=dict(type='str', required=True),
    ))
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/visibility/packet-capture/object-templates/tmpl-gtp-plcy-tmpl/{tmpl_gtp_plcy_tmpl_name}/trigger-stats-rate"

    f_dict = {}
    if '/' in module.params["tmpl_gtp_plcy_tmpl_name"]:
        f_dict["tmpl_gtp_plcy_tmpl_name"] = module.params["tmpl_gtp_plcy_tmpl_name"].replace("/","%2F")
    else:
        f_dict["tmpl_gtp_plcy_tmpl_name"] = module.params["tmpl_gtp_plcy_tmpl_name"]

    return url_base.format(**f_dict)


def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/visibility/packet-capture/object-templates/tmpl-gtp-plcy-tmpl/{tmpl_gtp_plcy_tmpl_name}/trigger-stats-rate"

    f_dict = {}
    f_dict["tmpl_gtp_plcy_tmpl_name"] = module.params["tmpl_gtp_plcy_tmpl_name"]

    return url_base.format(**f_dict)


def report_changes(module, result, existing_config, payload):
    change_results = copy.deepcopy(result)
    if not existing_config:
        change_results["modified_values"].update(**payload)
        return change_results

    config_changes = copy.deepcopy(existing_config)
    for k, v in payload["trigger-stats-rate"].items():
        v = 1 if str(v).lower() == "true" else v
        v = 0 if str(v).lower() == "false" else v

        if config_changes["trigger-stats-rate"].get(k) != v:
            change_results["changed"] = True
            config_changes["trigger-stats-rate"][k] = v

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
    payload = utils.build_json("trigger-stats-rate", module.params, AVAILABLE_PROPERTIES)
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
                result["acos_info"] = info["trigger-stats-rate"] if info != "NotFound" else info
            elif module.params.get("get_type") == "list":
                get_list_result = api_client.get_list(module.client, existing_url(module))
                result["axapi_calls"].append(get_list_result)

                info = get_list_result["response_body"]
                result["acos_info"] = info["trigger-stats-rate-list"] if info != "NotFound" else info
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
