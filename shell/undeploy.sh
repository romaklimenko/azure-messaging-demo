#!/bin/bash

if ! az account show > /dev/null 2>&1; then
    az login
fi

RESOURCE_GROUP=$(jq -r '.parameters.resourceGroupName.value' ./bicep/resource-group.parameters.json)

if $(az group exists --name "$RESOURCE_GROUP"); then
    az group delete \
        --name "$RESOURCE_GROUP" \
        --yes
fi
