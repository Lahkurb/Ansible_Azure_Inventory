# Ansible_Azure_Inventory
This repository contains examples and best practices for building Ansible Playbooks for Azure Inventory.
Prerequisites

    Azure Account. If you don't have one, get a free one.

    To authenticate with Azure, generate service principal and expose them as environment variables or store them as a file.

    Install Ansible

    Install Azure dependencies package

    pip install ansible[azure]

    Install azure_preview_modules role.

    Install azure_preview_module role's dependencies packages.

    pip install -r ~/.ansible/roles/Azure.azure_preview_modules/files/requirements-azure.txt

How to run

To run samples in your local environment,

    git clone https://github.com/Azure-Samples/ansible-playbooks.git
    cd ansible-playbooks
    modify playbook to replace variables with yours, such as resource group name.
    add Azure credential info by using one of the following options.

First option, set the following environment variables:

AZURE_CLIENT_ID=<service_principal_client_id>
AZURE_SECRET=<service_principal_password>
AZURE_SUBSCRIPTION_ID=<azure_subscription_id>
AZURE_TENANT=<azure_tenant_id>

Second option, add the following content to the file $HOME/.azure/credentials:

[default]
subscription_id=xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
client_id=xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
secret=xxxxxxxxxxxxxxxxx
tenant=xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

Third option, do a az login:

az login
