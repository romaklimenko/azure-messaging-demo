param principalId string

module storage 'storage-account.bicep' = {
  name: 'storageAccountDeployment'
  scope: resourceGroup()
  params: {
    name: toLower(substring('storage${uniqueString(resourceGroup().id)}', 0, 20))
    principalId: principalId
  }
}

module serviceBus 'service-bus.bicep' = {
  name: 'serviceBusDeployment'
  scope: resourceGroup()
  params: {
    name: toLower(substring('servicebus${uniqueString(resourceGroup().id)}', 0, 20))
    principalId: principalId
  }
}

module eventHub 'event-hub.bicep' = {
  name: 'eventHubDeployment'
  scope: resourceGroup()
  params: {
    name: toLower(substring('eventhub${uniqueString(resourceGroup().id)}', 0, 20))
    principalId: principalId
  }
}
