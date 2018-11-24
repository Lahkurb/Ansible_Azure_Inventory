!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: azure_inventory_module

short_description: dump resource on azure into an excel

version_added: "beta"

description:
    - "Develop new Ansible module for particular functions for playbook. Which can output Azure Inventory. Module should be in Python. "

options:
    name:
        description:
            - N/A
        required: true
    new:
        description:
            - Control to demo if the result of this module is changed or not
        required: false

extends_documentation_fragment:
    - azure

author:
    - Wenbin Chen
'''

import os
import json
import sys

from azure.common.credentials import UserPassCredentials
from azure.mgmt.resource.resources import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient

# Create azure inventory folder if not exist
Directory = 'c:\AzureInventory'
if not os.path.isdir(Directory):
    try:
        os.mkdir(Directory)
    except OSError:
        pass

# User authentication
user = 'kyle@live.com'
password = 'xxx***xxx'
credentials = UserPassCredentials(user,password)
subscription_id='9c9de358-2a52-4640-a82f-bd656255abb7'

# Write content to file
def writeCSV(name,content):
    try:
        file = open(str("%s\%s.csv"%(Directory,name)),'w')
        file.write(content)
        file.close
    except OSError:
        pass
    
#---------------------------------------------------
#   Resource Groups
#---------------------------------------------------
csvResourceGroup=""
client=ResourceManagementClient(credentials,subscription_id)
for item in client.resource_groups.list():
    oResourceGroupName = item.name
    oResourceGroupLocation = item.location
    csvResourceGroup += str("%s,%s\n"%(oResourceGroupName,oResourceGroupLocation))
# Write to file
writeCSV('ResouceGroup',csvResourceGroup)



#---------------------------------------------------
#   Network
#---------------------------------------------------
csvNetwork=""
network_client=NetworkManagementClient(credentials,subscription_id)

for virtualNetwork in network_client.virtual_networks.list_all():
    for subnet in virtualNetwork.subnets:        
        for virtualNICS in subnet.NetworkSecurityGroup.networkInterfaces:
            oVirtualNetwork=virtualNetwork.name
            oNetworkSecurityGroup=subnet.NetworkSecurityGroup.name            
            oSubnetName=subnet.name
            oSubnetAddressprefix=subnet.AddressPrefix
            oSubnetNetworkSecurityGroup=subnet.NetworkSecurityGroup.name
            oSubnetRouteTable=subnet.routeTable.name
            oVnicName=virtualNICS.name
            oVnicPrivateIpAddress=virtualNICS.IpConfigurations.privateIPAddress
            oVnicPrivateIpAllocationMethod=virtualNICS.IpConfigurations.PrivateIpAllocationMethod
            csvNetwork += str("%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(\
                oVirtualNetwork,\
                oNetworkSecurityGroup,\
                oSubnetName,\
                oSubnetAddressprefix,\
                oSubnetNetworkSecurityGroup,\
                oSubnetRouteTable,\
                oVnicName,\
                oVnicPrivateIpAddress,\
                oVnicPrivateIpAllocationMethod))
writeCSV('Network',csvNetwork)
                              

#---------------------------------------------------
#   Virutal Machines
#---------------------------------------------------
csvVirtualMachines = ""
compute_client = ComputeManagementClient(credentials, subscription_id)
virtual_machines = compute_client.virtual_machine_images
for virtual_machine in virtual_machines:
    vmName = virtual_machine.name
    vmLocation = virtual_machine.location
    vmHardwareProfile = virtual_machine.hardwareProfile.vmSize
    vmOSDisk = virtual_machine.StorageProfile.osDisk.vhd.uri
    csvVirtualMachines += str("%s,%s,%s,%s\n"%(vmName,vmLocation,vmHardwareProfile,vmOSDisk))
writeCSV('VirtualMachines',csvVirtualMachines)

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=True),
        new=dict(type='bool', required=False, default=False)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        return result

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    result['original_message'] = module.params['name']
    result['message'] = 'goodbye'

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    if module.params['new']:
        result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['name'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
