param principalId string

module storage 'storage-account.bicep' = {
  name: 'storageAccountDeployment'
  scope: resourceGroup()
  params: {
    name: toLower(substring('storage${uniqueString(resourceGroup().id)}', 0, 20))
    principalId: principalId
  }
}
