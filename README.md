# Azure Messaging Demo

This repository contains a demo of Azure messaging services.

- `/bicep` - contains Bicep templates to deploy Azure resources.
- `/python` - contains Python scripts to interact with Azure messaging services.

## How to use

The following steps assume you run the repository in GitHub Codespaces or devcontainer.

First, open the repository in a GitHub Codespace by clicking the button below:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/romaklimenko/azure-messaging-demo)

Or, clone the repository and open it in a [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers).

Next, deploy the Azure resources:

```bash
make deploy
```

You will be prompted to login to your Azure account and select a subscription.

NB: The script creates a new resource group called `messaging` in `westeurope` and deploys all resources to it. If you want to deploy resources to a different location or resource group, modify the `resource-group.parameters.json` accordingly.

After the deployment is complete, run the Python scripts directly or using the Makefile:

### Azure Storage Queue

```bash
make sa_pub # Publish messages to the queue
make sa_sub # Receive messages
```

### Azure Service Bus

```bash
make sb_pub # Publish messages to the topic
make sb_sub1 # Receive messages from the subscription1
make sb_sub2 # Receive messages from the subscription1
```

### Azure Event Hubs

```bash
make eh_pub # Publish messages to the event hub
make eh_sub # Receive messages
```

### Azure Event Grid

```bash
make eg_pub # Publish events to the event grid
make eg_sub # Receive events
```

## Clean up

To delete all Azure resources, run:

```bash
make undeploy
```
