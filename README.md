[![Travis CI](https://travis-ci.org/Azure-Samples/ansible-playbooks.svg?branch=full-ci)](https://travis-ci.org/Azure-Samples/ansible-playbooks)

# Ansible Playbooks for Azure Inventory

This repository contains examples and best practices for building Ansible Playbooks for Azure Inventory.

## Prerequisites

- Azure Account. If you don't have one, get a [free one](https://azure.microsoft.com/en-us/free/).

  To authenticate with Azure, generate [service principal](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal) and expose them as environment variables or store them as a file.

- Install [Ansible]((http://docs.ansible.com/ansible/latest/intro_installation.html))
- Install Azure dependencies package

  ```sh
  pip install ansible[azure]
  ```

- Install [azure_preview_modules](https://galaxy.ansible.com/Azure/azure_preview_modules/) role.
- Install azure_preview_module role's dependencies packages.

  ```sh
  pip install -r ~/.ansible/roles/Azure.azure_preview_modules/files/requirements-azure.txt
  ```

## How to run

To run samples in your local environment,

- `git clone https://github.com/Azure-Samples/ansible-playbooks.git`
- `cd ansible-playbooks`
- modify playbook to replace variables with yours, such as resource group name.
- [add Azure credential info](http://docs.ansible.com/ansible/latest/scenario_guides/guide_azure.html) by using one of the following options.

First option, set the following environment variables:

```ini
AZURE_CLIENT_ID=<service_principal_client_id>
AZURE_SECRET=<service_principal_password>
AZURE_SUBSCRIPTION_ID=<azure_subscription_id>
AZURE_TENANT=<azure_tenant_id>
```

Second option, add the following content to the file `$HOME/.azure/credentials`:

```ini
[default]
subscription_id=xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
client_id=xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
secret=xxxxxxxxxxxxxxxxx
tenant=xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

Third option, do a az login:

```sh
az login
```

- `ansible-playbook sample.yml`


## Resources

[Ansible on Azure](https://docs.microsoft.com/en-us/azure/ansible/ansible-overview)

[Get Started with Azure](http://docs.ansible.com/ansible/latest/guide_azure.html)

[Ansible Playbook](http://docs.ansible.com/ansible/latest/playbooks.html)

[Ansible role azure_preview_modules](https://galaxy.ansible.com/Azure/azure_preview_modules/)

[Ansible Galaxy](http://galaxy.ansible.com) for example roles from the Ansible community for deploying many popular applications. 

