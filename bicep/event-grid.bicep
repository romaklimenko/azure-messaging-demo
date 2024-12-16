param name string
param principalId string

resource eventGridNamespace 'Microsoft.EventGrid/namespaces@2024-06-01-preview' = {
  name: name
  location: resourceGroup().location
  sku: {
    name: 'Standard'
  }
}

resource namespaceTopic 'Microsoft.EventGrid/namespaces/topics@2024-06-01-preview' = {
  parent: eventGridNamespace
  name: 'eventGridTopic1'
}

resource subscription 'Microsoft.EventGrid/namespaces/topics/eventSubscriptions@2024-06-01-preview' = {
  parent: namespaceTopic
  name: 'eventGridSubscription1'
  properties: {
    deliveryConfiguration: {
      deliveryMode: 'Queue'
    }
  }
}

resource roleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(eventGridNamespace.id, 'EventGridDataContributor', principalId)
  scope: eventGridNamespace
  properties: {
    roleDefinitionId: subscriptionResourceId(
      'Microsoft.Authorization/roleDefinitions',
      '1d8c3fe3-8864-474b-8749-01e3783e8157'
    )
    principalId: principalId
  }
}

output eventGridHostName string = eventGridNamespace.properties.topicsConfiguration.hostname
output eventGridTopicName string = namespaceTopic.name
