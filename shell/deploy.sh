RESOURCE_GROUP=$(jq -r '.parameters.resourceGroupName.value' ./bicep/resource-group.parameters.json)
LOCATION=$(jq -r '.parameters.location.value' ./bicep/resource-group.parameters.json)

PRINCIPAL_ID=$(az ad signed-in-user show --query id -o tsv)

az group create \
    --name $RESOURCE_GROUP \
    --location $LOCATION

az deployment group create \
    --resource-group $RESOURCE_GROUP \
    --template-file ./bicep/main.bicep \
    --parameters ./bicep/main.parameters.json \
    --parameters principalId=$PRINCIPAL_ID

# print Bicep outputs
STORAGE_ACCOUNT_DEPLOYMENT_OUTPUT=$(az deployment group show \
    --resource-group $RESOURCE_GROUP \
    --name storageAccountDeployment \
    --query properties.outputs)

echo "STORAGE_ACCOUNT_NAME=$(jq -r '.storageAccountName.value' <<< $STORAGE_ACCOUNT_DEPLOYMENT_OUTPUT)" > .env
