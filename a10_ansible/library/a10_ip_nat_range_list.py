#!/usr/bin/python
REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = """
module: a10_range-list
description:
    - 
author: A10 Networks 2018 
version_added: 1.8

options:
    
    name:
        description:
            - Name for this Static List
    
    local-start-ipv4-addr:
        description:
            - Local Start IPv4 Address of this list
    
    local-netmaskv4:
        description:
            - Mask for this Address range
    
    global-start-ipv4-addr:
        description:
            - Global Start IPv4 Address of this list
    
    global-netmaskv4:
        description:
            - Mask for this Address range
    
    v4-count:
        description:
            - Number of addresses to be translated in this range
    
    v4-acl-id:
        description:
            - Access list ID
    
    v4-acl-name:
        description:
            - Access list name
    
    v4-vrid:
        description:
            - VRRP-A vrid (Specify ha VRRP-A vrid)
    
    local-start-ipv6-addr:
        description:
            - Local Start IPv6 Address of this list
    
    global-start-ipv6-addr:
        description:
            - Global Start IPv6 Address of this list
    
    v6-count:
        description:
            - Number of addresses to be translated in this range
    
    v6-acl-name:
        description:
            - Access list name
    
    v6-vrid:
        description:
            - VRRP-A vrid (Specify ha VRRP-A vrid)
    
    uuid:
        description:
            - uuid of the object
    

"""

EXAMPLES = """
"""

ANSIBLE_METADATA = """
"""

# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = {"global_netmaskv4","global_start_ipv4_addr","global_start_ipv6_addr","local_netmaskv4","local_start_ipv4_addr","local_start_ipv6_addr","name","uuid","v4_acl_id","v4_acl_name","v4_count","v4_vrid","v6_acl_name","v6_count","v6_vrid",}

# our imports go at the top so we fail fast.
from a10_ansible.axapi_http import client_factory
from a10_ansible import errors as a10_ex

def get_default_argspec():
    return dict(
        a10_host=dict(type='str', required=True),
        a10_username=dict(type='str', required=True),
        a10_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str', default="present", choices=["present", "absent"])
    )

def get_argspec():
    rv = get_default_argspec()
    rv.update(dict(
        
        global_netmaskv4=dict(
            type='str' 
        ),
        global_start_ipv4_addr=dict(
            type='str' 
        ),
        global_start_ipv6_addr=dict(
            type='str' 
        ),
        local_netmaskv4=dict(
            type='str' 
        ),
        local_start_ipv4_addr=dict(
            type='str' 
        ),
        local_start_ipv6_addr=dict(
            type='str' 
        ),
        name=dict(
            type='str' , required=True
        ),
        uuid=dict(
            type='str' 
        ),
        v4_acl_id=dict(
            type='str' 
        ),
        v4_acl_name=dict(
            type='str' 
        ),
        v4_count=dict(
            type='str' 
        ),
        v4_vrid=dict(
            type='str' 
        ),
        v6_acl_name=dict(
            type='str' 
        ),
        v6_count=dict(
            type='str' 
        ),
        v6_vrid=dict(
            type='str' 
        ), 
    ))
    return rv

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/ip/nat/range-list/{name}"
    f_dict = {}
    
    f_dict["name"] = ""

    return url_base.format(**f_dict)

def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/ip/nat/range-list/{name}"
    f_dict = {}
    
    f_dict["name"] = module.params["name"]

    return url_base.format(**f_dict)


def build_envelope(title, data):
    return {
        title: data
    }

def build_json(title, module):
    rv = {}
    for x in AVAILABLE_PROPERTIES:
        v = module.params.get(x)
        if v:
            rx = x.replace("_", "-")
            rv[rx] = module.params[x]

    return build_envelope(title, rv)

def validate(params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([x for x in requires_one_of if params.get(x)])
    
    errors = []
    marg = []
    
    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc,msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc,msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc,msg = REQUIRED_VALID
    
    if not rc:
        errors.append(msg.format(", ".join(marg)))
    
    return rc,errors

def exists(module):
    try:
        module.client.get(existing_url(module))
        return True
    except a10_ex.NotFound:
        return False

def create(module, result):
    payload = build_json("range-list", module)
    try:
        post_result = module.client.post(new_url(module), payload)
        result.update(**post_result)
        result["changed"] = True
    except a10_ex.Exists:
        result["changed"] = False
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def delete(module, result):
    try:
        module.client.delete(existing_url(module))
        result["changed"] = True
    except a10_ex.NotFound:
        result["changed"] = False
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def update(module, result):
    payload = build_json("range-list", module)
    try:
        post_result = module.client.put(existing_url(module), payload)
        result.update(**post_result)
        result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def present(module, result):
    if not exists(module):
        return create(module, result)
    else:
        return update(module, result)

def absent(module, result):
    return delete(module, result)



def run_command(module):
    run_errors = []

    result = dict(
        changed=False,
        original_message="",
        message=""
    )

    state = module.params["state"]
    a10_host = module.params["a10_host"]
    a10_username = module.params["a10_username"]
    a10_password = module.params["a10_password"]
    # TODO(remove hardcoded port #)
    a10_port = 443
    a10_protocol = "https"

    valid, validation_errors = validate(module.params)
    map(run_errors.append, validation_errors)
    
    if not valid:
        result["messages"] = "Validation failure"
        err_msg = "\n".join(run_errors)
        module.fail_json(msg=err_msg, **result)

    module.client = client_factory(a10_host, a10_port, a10_protocol, a10_username, a10_password)

    if state == 'present':
        result = present(module, result)
    elif state == 'absent':
        result = absent(module, result)
    return result

def main():
    module = AnsibleModule(argument_spec=get_argspec())
    result = run_command(module)
    module.exit_json(**result)

# standard ansible module imports
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

if __name__ == '__main__':
    main()