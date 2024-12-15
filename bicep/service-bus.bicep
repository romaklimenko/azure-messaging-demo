param name string
param location string = resourceGroup().location
param principalId string

resource serviceBusNamespace 'Microsoft.ServiceBus/namespaces@2024-01-01' = {
  name: name
  location: location
  sku: {
    name: 'Standard'
    tier: 'Standard'
  }
}

resource topic 'Microsoft.ServiceBus/namespaces/topics@2024-01-01' = {
  parent: serviceBusNamespace
  name: 'topic1'
}

resource subscription1 'Microsoft.ServiceBus/namespaces/topics/subscriptions@2024-01-01' = {
  parent: topic
  name: 'subscription1'
}

resource subscription2 'Microsoft.ServiceBus/namespaces/topics/subscriptions@2024-01-01' = {
  parent: topic
  name: 'subscription2'
}

resource roleAssignment1 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(serviceBusNamespace.id, 'ServiceBusDataSender', principalId)
  scope: serviceBusNamespace
  properties: {
    roleDefinitionId: subscriptionResourceId(
      'Microsoft.Authorization/roleDefinitions',
      // (https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#service-bus-data-owner)
      '090c5cfd-751d-490a-894a-3ce6f1109419'
    )
    principalId: principalId
  }
}

output serviceBusNamespaceName string = serviceBusNamespace.name
