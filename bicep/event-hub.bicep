param name string
param principalId string

resource eventHubNamespace 'Microsoft.EventHub/namespaces@2024-01-01' = {
  name: name
  location: resourceGroup().location
  sku: {
    name: 'Standard'
    tier: 'Standard'
  }
}

resource eventHub 'Microsoft.EventHub/namespaces/eventHubs@2024-01-01' = {
  parent: eventHubNamespace
  name: 'eventHub1'
}

resource roleAssignmentEventHubDataOwner 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(eventHub.id, 'EventHubDataOwner', principalId)
  scope: eventHub
  properties: {
    roleDefinitionId: subscriptionResourceId(
      'Microsoft.Authorization/roleDefinitions',
      // (https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/analytics#azure-event-hubs-data-owner)
      'f526a384-b230-433a-b45c-95f59c4a2dec'
    )
    principalId: principalId
  }
}

output eventHubNamespaceName string = eventHubNamespace.name
output eventHubName string = eventHub.name
