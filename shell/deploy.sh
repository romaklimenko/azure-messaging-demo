#!/bin/bash

if ! az account show > /dev/null 2>&1; then
    az login
fi

RESOURCE_GROUP=$(jq -r '.parameters.resourceGroupName.value' ./bicep/resource-group.parameters.json)
LOCATION=$(jq -r '.parameters.location.value' ./bicep/resource-group.parameters.json)

PRINCIPAL_ID=$(az ad signed-in-user show --query id -o tsv)

az group create \
    --name $RESOURCE_GROUP \
    --location $LOCATION \
    --tags "purpose=demo"

az deployment group create \
    --resource-group $RESOURCE_GROUP \
    --template-file ./bicep/main.bicep \
    --parameters ./bicep/main.parameters.json \
    --parameters principalId=$PRINCIPAL_ID

STORAGE_ACCOUNT_DEPLOYMENT_OUTPUT=$(az deployment group show \
    --resource-group $RESOURCE_GROUP \
    --name storageAccountDeployment \
    --query properties.outputs)

SERVICE_BUS_DEPLOYMENT_OUTPUT=$(az deployment group show \
    --resource-group $RESOURCE_GROUP \
    --name serviceBusDeployment \
    --query properties.outputs)

EVENT_HUB_DEPLOYMENT_OUTPUT=$(az deployment group show \
    --resource-group $RESOURCE_GROUP \
    --name eventHubDeployment \
    --query properties.outputs)

echo "STORAGE_ACCOUNT=$(jq -r '.storageAccountName.value' <<< $STORAGE_ACCOUNT_DEPLOYMENT_OUTPUT)" > .env
echo "SERVICE_BUS_NAMESPACE=$(jq -r '.serviceBusNamespaceName.value' <<< $SERVICE_BUS_DEPLOYMENT_OUTPUT)" >> .env
echo "EVENT_HUB_NAMESPACE=$(jq -r '.eventHubNamespaceName.value' <<< $EVENT_HUB_DEPLOYMENT_OUTPUT)" >> .env
echo "EVENT_HUB=$(jq -r '.eventHubName.value' <<< $EVENT_HUB_DEPLOYMENT_OUTPUT)" >> .env
