# Microsoft Graph

---

<br>

[Microsoft Graph](https://docs.microsoft.com/graph/overview) is the gateway to data and intelligence in Microsoft 365. It provides a unified programmability model that you can use to access the tremendous amount of data in Microsoft 365, Windows 10, and Enterprise Mobility + Security. Use the wealth of data in Microsoft Graph to build apps for organizations and consumers that interact with millions of users.

<br>

## Requests

### Get my notebooks 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/onenote/notebooks
```

<br>

### Get my notebook sections 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/onenote/sections
```

<br>

### Get my notebook pages 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/onenote/pages
```

<br>

### Create notebook 

---
> Request

```
POST https://graph.microsoft.com/v1.0/me/onenote/notebooks
```


> Body

```json
{
  "displayName": "Postman Notebook 1"
}
```

<br>

### Create section 

---
> Request

```
POST https://graph.microsoft.com/v1.0/me/onenote/notebooks/{{NotebookId}}/sections
```


> Body

```json
{
  "displayName": "Section 1"
}
```

<br>

### Get my organization's default site collection 

---
> Request

```
GET https://graph.microsoft.com/v1.0/sites/root
```

<br>

### Get the doc libs in root site 

---
> Request

```
GET https://graph.microsoft.com/v1.0/sites/root/drives
```

<br>

### Search for site by name 

---
> Request

```
GET https://graph.microsoft.com/v1.0/sites?search=contoso
```

> Query parameters

**`search`**

<br>

### Get subsites of site 

---
> Request

```
GET https://graph.microsoft.com/v1.0/sites/root/sites
```

<br>

### Get site columns 

---
> Request

```
GET https://graph.microsoft.com/v1.0/sites/root/columns
```

<br>

### Get site content types 

---
> Request

```
GET https://graph.microsoft.com/v1.0/sites/root/contentTypes
```

<br>

### Get site lists 

---
> Request

```
GET https://graph.microsoft.com/v1.0/sites/root/lists
```

<br>

### Get list columns 

---
> Request

```
GET https://graph.microsoft.com/v1.0/sites/root/lists/{{ListId}}/columns
```

<br>

### Get list content types 

---
> Request

```
GET https://graph.microsoft.com/v1.0/sites/root/lists/{{ListId}}/contentTypes
```

<br>

### Get list items 

---
> Request

```
GET https://graph.microsoft.com/v1.0/sites/root/lists/{{ListId}}/items
```

<br>

### Get list items titled "Contoso Home" 

---
> Request

```
GET https://graph.microsoft.com/v1.0/sites/root/lists/{{ListId}}/items?$filter=fields/Title eq 'Contoso Home'
```

> Query parameters

**`$filter`**

<br>

### Get applications 

---
> Request

```
GET https://graph.microsoft.com/v1.0/applications
```

<br>

### Create an application 

---
> Request

```
POST https://graph.microsoft.com/v1.0/applications
```


> Body

```json
{
  "displayName": "My App"
}
```

<br>

### Get application 

---
> Request

```
GET https://graph.microsoft.com/v1.0/applications/{{ApplicationId}}
```

<br>

### Get application owners 

---
> Request

```
GET https://graph.microsoft.com/v1.0/applications/{{ApplicationId}}/owners
```

<br>

### Update application 

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/applications/{{ApplicationId}}
```


> Body

```json
{
  "signInAudience": "AzureADMyOrg"
}
```

<br>

### Delete application 

---
> Request

```
DELETE https://graph.microsoft.com/beta/applications/{{ApplicationId}}
```

<br>

### Get subscriptions 

---
> Request

```
GET https://graph.microsoft.com/v1.0/subscriptions
```

<br>

### Create subjectRightsRequest 

---
> Request

```
POST https://graph.microsoft.com/v1.0/privacy/subjectRightsRequests
```


> Body

```json
{
    "type": "access",
    "dataSubjectType": "currentEmployee",
    "regulations": ["Test Regulation"],
    "displayName": "{{createRequestDisplayName}}",
    "description": "{{createRequestDescription}}",
    "internalDueDateTime": "{{internalDueDateTime}}",
    "dataSubject": {
        "firstName": "{{firstName}}",
        "lastName": "{{lastName}}",
        "email": "{{email}}",
        "residency": "5000 148th Ave NE, Redmond, WA 98052",
        "phoneNumber": "(425) 867-6537",
        "SSN": "555-55-5555"
    }
}
```

<br>

### List subjectRightsRequests 

---
> Request

```
GET https://graph.microsoft.com/v1.0/privacy/subjectRightsRequests
```

<br>

### Get subjectRightsRequest 

---
> Request

```
GET https://graph.microsoft.com/v1.0/privacy/subjectRightsRequests/{{subjectRightsRequestId}}
```

<br>

### subjectRightsRequest: getFinalReport 

---
> Request

```
GET https://graph.microsoft.com/v1.0/privacy/subjectRightsRequests/{{subjectRightsRequestId}}/getFinalReport
```

<br>

### subjectRightsRequest: getFinalAttachment 

---
> Request

```
GET https://graph.microsoft.com/v1.0/privacy/subjectRightsRequests/{{subjectRightsRequestId}}/getFinalAttachment
```

<br>

### Create authoredNote 

---
> Request

```
POST https://graph.microsoft.com/v1.0/privacy/subjectRightsRequests/{{subjectRightsRequestId}}/notes
```


> Body

```json
{
"content": 
  {
    "content": "This is a Microsoft Graph note!",
    "contentType": "text"
  }
}
```

<br>

### List notes 

---
> Request

```
GET https://graph.microsoft.com/v1.0/privacy/subjectRightsRequests/{{subjectRightsRequestId}}/notes
```

<br>

### List retentionLabels 

---
> Request

```
GET https://graph.microsoft.com/beta/security/labels/retentionLabels
```

<br>

### Create retentionLabel 

---
> Request

```
POST https://graph.microsoft.com/beta/security/labels/retentionLabels
```


> Body

```json
{
  "displayName": "{{labelDisplayName}}",
  "behaviorDuringRetentionPeriod": "retain",
  "actionAfterRetentionPeriod": "none",
  "retentionTrigger": "dateLabeled",
  "retentionDuration": {
    "@odata.type": "microsoft.graph.security.retentionDurationInDays",
    "days": "2555"
  },
  "descriptionForAdmins": "{{labelDescriptionForAdmins}}",
  "descriptionForUsers": "{{labelDescriptionForUsers}}"
}
```

<br>

### Get retentionLabel 

---
> Request

```
GET https://graph.microsoft.com/beta/security/labels/retentionLabels/{{retentionLabelId}}
```

<br>

### Update retentionLabel 

---
> Request

```
PATCH https://graph.microsoft.com/beta/security/labels/retentionLabels/{{retentionLabelId}}
```


> Body

```json
{
    "descriptionForAdmins": "Updated description for Admins"
}
```

<br>

### Delete rentionionLabel 

---
> Request

```
DELETE https://graph.microsoft.com/beta/security/labels/retentionLabels/{{retentionLabelId}}
```

<br>

### List retentionEventTypes 

---
> Request

```
GET https://graph.microsoft.com/beta/security/triggerTypes/retentionEventTypes
```

<br>

### Get retentionEventType 

---
> Request

```
GET https://graph.microsoft.com/beta/security/triggerTypes/retentionEventTypes/{{retentionEventTypeId}}
```

<br>

### Create retentionEvent 

---
> Request

```
POST https://graph.microsoft.com/beta/security/triggers/retentionEvents
```


> Body

```json
{
    "displayName": "{{eventDisplayName}}",
    "description": "{{eventDescription}}",
    "eventQueries": [
        {
            "queryType": "files",
            "query": "12345"
        },
        {
            "queryType": "messages",
            "query": "test"
        }
    ],
    "eventTriggerDateTime": "2022-09-14T00:00:00Z",
    "retentionEventType@odata.bind": "https://graph.microsoft.com/beta/security/triggerTypes/retentionEventTypes/{{retentionEventTypeId}}" 
}
```

<br>

### Get retentionEvent 

---
> Request

```
GET https://graph.microsoft.com/beta/security/triggers/retentionEvents/{{retentionEventId}}
```

<br>

### List retentionEvents 

---
> Request

```
GET https://graph.microsoft.com/beta/security/triggers/retentionEvents
```

<br>

### Get an open extension ![auth](https://img.shields.io/badge/auth-token-brightgreen)

---
> Request

```
GET https://graph.microsoft.com/v1.0/me?$select=id,displayName,mail,mobilePhone&$expand=extensions
```

> Query parameters

**`$select`**

**`$expand`**

<br>

### Create an open extension ![auth](https://img.shields.io/badge/auth-token-brightgreen)

---
> Request

```
POST https://graph.microsoft.com/v1.0/me/extensions
```


> Body

```json
{
  "@odata.type": "microsoft.graph.openTypeExtension",
  "extensionName": "com.contoso.roamingSettings",
  "theme": "dark",
  "color": "purple",
  "lang": "Japanese"
}
```

<br>

### Update an open extension ![auth](https://img.shields.io/badge/auth-token-brightgreen)

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/me/extensions/{{ExtensionId}}
```


> Body

```json
{
  "theme": "light",
  "color": "red",
  "lang": "Swahili"
}
```

<br>

### Get avaiable schema extensions ![auth](https://img.shields.io/badge/auth-token-brightgreen)

---
> Request

```
GET https://graph.microsoft.com/v1.0/schemaExtensions
```

<br>

### Create a group with extension ![auth](https://img.shields.io/badge/auth-token-brightgreen)

---
> Request

```
POST https://graph.microsoft.com/v1.0/groups
```


> Body

```json
{
  "displayName": "Extensions sample group",
  "description": "Extensions sample group",
  "groupTypes": [
    "Unified"
  ],
  "mailEnabled": true,
  "mailNickname": "extSample123",
  "securityEnabled": false,
  "adatumisv_courses": {
    "id": "123",
    "name": "New Managers",
    "type": "Online"
  }
}
```

<br>

### Filter groups by extensions ![auth](https://img.shields.io/badge/auth-token-brightgreen)

---
> Request

```
GET https://graph.microsoft.com/v1.0/groups?$filter=adatumisv_courses/id eq '123'&$select=id,displayName,adatumisv_courses
```

> Query parameters

**`$filter`**

**`$select`**

<br>

### Update a group with extension ![auth](https://img.shields.io/badge/auth-token-brightgreen)

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/groups/{{GroupId}}
```


> Body

```json
{
  "adatumisv_courses": {
    "id": "123",
    "name": "More Managers",
    "type": "Online"
  }
}
```

<br>

### Perform parallel GETS 

---
> Request

```
POST https://graph.microsoft.com/v1.0/$batch
```


> Body

```json
{
  "requests": [
    {
      "url": "/me?$select=displayName,jobTitle,userPrincipalName",
      "method": "GET",
      "id": "1"
    },
    {
      "url": "/me/messages?$filter=importance eq 'high'&$select=from,subject,receivedDateTime,bodyPreview",
      "method": "GET",
      "id": "2"
    },
    {
      "url": "/me/events",
      "method": "GET",
      "id": "3"
    }
  ]
}
```

<br>

### Combine a POST and a GET 

---
> Request

```
POST https://graph.microsoft.com/v1.0/$batch
```


> Body

```json
{
  "requests": [
    {
      "url": "/me/drive/root/children",
      "method": "POST",
      "id": "1",
      "body": {
        "name": "TestBatchingFolder",
        "folder": {}
      },
      "headers": {
        "Content-Type": "application/json"
      }
    },
    {
      "url": "/me/drive/root/children/TestBatchingFolder ",
      "method": "GET",
      "id": "2",
      "DependsOn": [
        "1"
      ]
    }
  ]
}
```

<br>

### List ediscoveryCases 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases
```

<br>

### Create ediscoveryCase 

---
> Request

```
POST https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases
```


> Body

```json
{
    "displayName": "{{displayName}}",
    "description": "{{description}}",
    "externalId": "{{externalId}}"
}
```

<br>

### Get ediscoveryCase 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}
```

<br>

### Update ediscoveryCase 

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}
```


> Body

```json
{
    "externalId": "Updated external case value 12345"
}
```

<br>

### Create Custodians 

---
> Request

```
POST https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/custodians
```


> Body

```json
{
    "email":"{{custodianEmail}}"
}
```

<br>

### List ediscoveryCustodian 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/custodians
```

<br>

### Create custodian userSource 

---
> Request

```
POST https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/custodians/{{custodianId}}/userSources
```


> Body

```json
{
    "email": "{{custodianEmail}}",
    "includedSources": "mailbox, site"
}
```

<br>

### ediscoveryCustodian: applyHold 

---
> Request

```
POST https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/custodians/applyHold
```


> Body

```json
{
  "ids": [
    "{{custodianId}}"
  ]
}
```

<br>

### List userSources 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/custodians/{{custodianId}}/userSources
```

<br>

### Create ediscoveryNoncustodialDataSources 

---
> Request

```
POST https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/noncustodialDataSources
```


> Body

```json
{
    "dataSource": {
        "@odata.type": "microsoft.graph.security.userSource",
        "email": "{{noncustodialEmail}}"
    }
}
```

<br>

### ediscoveryNoncustodialDataSource: applyHold 

---
> Request

```
POST https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/noncustodialDataSources/applyHold
```


> Body

```json
{
  "ids": [
    "{{noncustodialId}}"
  ]
}
```

<br>

### List ediscoveryNoncustodialDataSources 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/noncustodialDataSources
```

<br>

### Create searches 

---
> Request

```
POST https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/searches
```


> Body

```json
{
    "displayName": "Microsoft Graph Search",
    "description": "This is an eDiscovery Premium search using Microsoft Graph",
    "contentQuery": "HasAttachment=true",
    "custodianSources@odata.bind": [
        "https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/custodians/{{custodianId}}/userSources/{{custodianUserSource}}"
    ],
    "noncustodialSources@odata.bind": [
        "https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/noncustodialdatasources/{{noncustodialDataSource}}"
    ]
}
```

<br>

### List searches 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/searches
```

<br>

### ediscoverySearch: estimate Statistics 

---
> Request

```
POST https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/searches/{{ediscoverySearchId}}/estimateStatistics
```

<br>

### List lastEstimateStatisticsOperation 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/searches/{{ediscoverySearchId}}/lastEstimateStatisticsOperation
```

<br>

### Create reviewSets 

---
> Request

```
POST https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/reviewSets
```


> Body

```json
{
    "displayName": "My Microsoft Graph Review Set"
}
```

<br>

### List reviewSets 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/reviewSets
```

<br>

### ediscoveryReviewSet: addToReviewSet 

---
> Request

```
POST https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/reviewSets/{{ediscoveryReviewSetId}}/addToReviewSet
```


> Body

```json
{
    "search": {
        "id": "{{ediscoverySearchId}}"
    },
    "additionalDataOptions": "linkedFiles"
}
```

<br>

### Create ediscoveryReviewSetQuery 

---
> Request

```
POST https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/reviewSets/{{ediscoveryReviewSetId}}/queries
```


> Body

```json
{
    "displayName": "Microsoft Graph Query",
    "contentQuery": "(Author=\"edison\")"
}
```

<br>

### Update ediscoveryReviewSetQuery 

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/reviewSets/{{ediscoveryReviewSetId}}/queries/{{ediscoveryReviewSetQueryId}}
```


> Body

```json
{
    "displayName": "Microsoft Graph Query (Update)",
    "contentQuery": "(ContentType=document)"
}
```

<br>

### List queries 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/reviewSets/{{ediscoveryReviewSetId}}/queries
```

<br>

### Delete ediscoveryReviewSetQuery 

---
> Request

```
DELETE https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/reviewSets/{{ediscoveryReviewSetId}}/queries/{{ediscoveryReviewSetQueryId}}
```

<br>

### List caseOperations 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/cases/ediscoveryCases/{{ediscoveryCaseId}}/operations
```

<br>

### Get alerts 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/alerts
```

<br>

### Get alerts with high severity 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/alerts?$filter=Severity eq 'High'&$top=5
```

> Query parameters

**`$filter`**

**`$top`**

<br>

### Get alerts from Azure Security Center 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/alerts?$filter=vendorInformation/provider eq 'ASC'&$top=5
```

> Query parameters

**`$filter`**

**`$top`**

<br>

### Get alerts filtered by category 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/alerts?$filter=Category eq 'ransomware'&$top=5
```

> Query parameters

**`$filter`**

**`$top`**

<br>

### Get alerts filtered by destination 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/alerts?$filter=networkConnections/any(d:d/destinationAddress eq '{destination-address}')
```

> Query parameters

**`$filter`**

<br>

### Get alerts filtered by status 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/alerts?$filter=Status eq 'NewAlert'&$top=1
```

> Query parameters

**`$filter`**

**`$top`**

<br>

### Get secure scores 

---
> Request

```
GET https://graph.microsoft.com/v1.0/security/secureScores?$top=5
```

> Query parameters

**`$top`**

<br>

### Get secure scores control profiles 

---
> Request

```
GET https://graph.microsoft.com/beta/security/secureScoreControlProfiles?$top=5
```

> Query parameters

**`$top`**

<br>

### Get TI indicators 

---
> Request

```
GET https://graph.microsoft.com/beta/security/tiIndicators
```

<br>

### Get TI indicator by id 

---
> Request

```
GET https://graph.microsoft.com/beta/security/tiIndicators/{{TIIndicatorId}}
```

<br>

### Get security actions 

---
> Request

```
GET https://graph.microsoft.com/beta/security/securityActions
```

<br>

### Get security action by id 

---
> Request

```
GET https://graph.microsoft.com/beta/security/securityActions/{{SecurityActionsId}}
```

<br>

### List retention labels 

---
> Request

```
GET https://graph.microsoft.com/beta/security/labels/retentionLabels
```

<br>

### List catalog entries 

---
> Request

```
GET https://graph.microsoft.com/beta/admin/windows/updates/catalog/entries
```

<br>

### List members 

---
> Request

```
GET https://graph.microsoft.com/beta/admin/windows/updates/deployments/{{DeploymentId}}/audience/members
```

<br>

### List exclusions 

---
> Request

```
GET https://graph.microsoft.com/beta/admin/windows/updates/deployments/{{DeploymentId}}/audience/exclusions
```

<br>

### Update audience (add members) 

---
> Request

```
POST https://graph.microsoft.com/beta/admin/windows/updates/deployments/{{DeploymentId}}/audience/updateAudience
```


> Body

```json
{
    "addMembers": [
        {
            "@odata.type": "#microsoft.graph.windowsUpdates.azureADDevice",
            "id": "{{AzureAdDeviceId}}" // deadbeef-cad1-4da9-b357-3ee3cde5d50a
        }
    ]
}
```

<br>

### Update audience (add exclusions) 

---
> Request

```
POST https://graph.microsoft.com/beta/admin/windows/updates/deployments/{{DeploymentId}}/audience/updateAudience
```


> Body

```json
{
    "addExclusions": [
        {
            "@odata.type": "#microsoft.graph.windowsUpdates.azureADDevice",
            "id": "{{AzureAdDeviceId}}" // deadbeef-cad1-4da9-b357-3ee3cde5d50a
        }
    ]
}
```

<br>

### Update audience (remove members) 

---
> Request

```
POST https://graph.microsoft.com/beta/admin/windows/updates/deployments/{{DeploymentId}}/audience/updateAudience
```


> Body

```json
{
    "removeMembers": [
        {
            "@odata.type": "#microsoft.graph.windowsUpdates.azureADDevice",
            "id": "{{AzureAdDeviceId}}" // deadbeef-cad1-4da9-b357-3ee3cde5d50a
        }
    ]
}
```

<br>

### Update audience (remove exclusions) 

---
> Request

```
POST https://graph.microsoft.com/beta/admin/windows/updates/deployments/{{DeploymentId}}/audience/updateAudience
```


> Body

```json
{
    "removeExclusions": [
        {
            "@odata.type": "#microsoft.graph.windowsUpdates.azureADDevice",
            "id": "{{AzureAdDeviceId}}" // deadbeef-cad1-4da9-b357-3ee3cde5d50a
        }
    ]
}
```

<br>

### Create deployment (feature update) 

---
> Request

```
POST https://graph.microsoft.com/beta/admin/windows/updates/deployments
```


> Body

```json
{
    "content": {
        "@odata.type": "#microsoft.graph.windowsUpdates.featureUpdateReference",
        "version": "{{FeatureUpdateVersion}}"
    }
}
```

<br>

### Create deployment (expedited security update) 

---
> Request

```
POST https://graph.microsoft.com/beta/admin/windows/updates/deployments
```


> Body

```json
{
    "content": {
        "@odata.type": "microsoft.graph.windowsUpdates.expeditedQualityUpdateReference",
        "releaseDate": "{{QualityUpdateReleaseDate}}"
    }
}
```

<br>

### Create deployment (rate-based gradual rollout) 

---
> Request

```
POST https://graph.microsoft.com/beta/admin/windows/updates/deployments
```


> Body

```json
{
    "content": {
        "@odata.type": "#microsoft.graph.windowsUpdates.featureUpdateReference",
        "version": "{{FeatureUpdateVersion}}"
    },
    "settings": {
        "@odata.type": "microsoft.graph.windowsUpdates.windowsDeploymentSettings",
        "rollout": {
            "devicesPerOffer": 100,
            "durationBetweenOffers": "P7D"
        },
        "monitoring": {
            "monitoringRules": [
                {
                    "@odata.type": "#microsoft.graph.windowsUpdates.monitoringRule",
                    "signal": "rollback",
                    "threshold": 5,
                    "action": "pauseDeployment"
                }
            ]
        }
    }
}
```

<br>

### Create deployment (date-based gradual rollout) 

---
> Request

```
POST https://graph.microsoft.com/beta/admin/windows/updates/deployments
```


> Body

```json
{
    "content": {
        "@odata.type": "#microsoft.graph.windowsUpdates.featureUpdateReference",
        "version": "{{FeatureUpdateVersion}}"
    },
    "settings": {
        "@odata.type": "microsoft.graph.windowsUpdates.windowsDeploymentSettings",
        "rollout": {
            "startDateTime": "{{DeploymentStartDateTime}}",
            "endDateTime": "{{DeploymentEndDateTime}}",
            "durationBetweenOffers": "P7D"
        },
        "monitoring": {
            "monitoringRules": [
                {
                    "@odata.type": "#microsoft.graph.windowsUpdates.monitoringRule",
                    "signal": "rollback",
                    "threshold": 5,
                    "action": "pauseDeployment"
                }
            ]
        }
    }
}
```

<br>

### List deployments 

---
> Request

```
GET https://graph.microsoft.com/beta/admin/windows/updates/deployments
```

<br>

### Get deployment 

---
> Request

```
GET https://graph.microsoft.com/beta/admin/windows/updates/deployments/{{DeploymentId}}
```

<br>

### Update deployment (replace monitoring rules) 

---
> Request

```
PATCH https://graph.microsoft.com/beta/admin/windows/updates/deployments/{{DeploymentId}}
```


> Body

```json
{
    "settings": {
        "@odata.type": "microsoft.graph.windowsUpdates.windowsDeploymentSettings",
        "monitoring": {
            "monitoringRules": [
                {
                    "signal": "rollback",
                    "threshold": 5,
                    "action": "pauseDeployment"
                }
            ]
        }
    }
}
```

<br>

### Update deployment (request paused state) 

---
> Request

```
PATCH https://graph.microsoft.com/beta/admin/windows/updates/deployments/{{DeploymentId}}
```


> Body

```json
{
    "state": {
        "@odata.type": "#microsoft.graph.windowsUpdates.deploymentState",
        "requestedValue": "paused"
    }
}
```

<br>

### Update deployment (clear requested state) 

---
> Request

```
PATCH https://graph.microsoft.com/beta/admin/windows/updates/deployments/{{DeploymentId}}
```


> Body

```json
{
    "state": {
        "@odata.type": "#microsoft.graph.windowsUpdates.deploymentState",
        "requestedValue": "none"
    }
}
```

<br>

### Delete deployment 

---
> Request

```
DELETE https://graph.microsoft.com/beta/admin/windows/updates/deployments/{{DeploymentId}}
```

<br>

### List Azure AD devices 

---
> Request

```
GET https://graph.microsoft.com/beta/admin/windows/updates/updatableAssets/?$filter=isof('microsoft.graph.windowsUpdates.azureADDevice')
```

> Query parameters

**`$filter`**

<br>

### Get Azure AD device 

---
> Request

```
GET https://graph.microsoft.com/beta/admin/windows/updates/updatableAssets/{{UpdatableAssetId}}
```

<br>

### Delete Azure AD device 

---
> Request

```
DELETE https://graph.microsoft.com/beta/admin/windows/updates/deployments/{{UpdatableAssetId}}
```

<br>

### Enroll in feature update management 

---
> Request

```
POST https://graph.microsoft.com/beta/admin/windows/updates/updatableAssets/enrollAssets
```


> Body

```json
{
    "updateCategory": "feature",
    "assets": [
        {
            "@odata.type": "#microsoft.graph.windowsUpdates.azureADDevice",
            "id": "{{AzureAdDeviceId}}"
        }
    ]
}
```

<br>

### Unenroll from feature update management 

---
> Request

```
POST https://graph.microsoft.com/beta/admin/windows/updates/updatableAssets/unenrollAssets
```


> Body

```json
{
    "updateCategory": "feature",
    "assets": [
        {
            "@odata.type": "#microsoft.graph.windowsUpdates.azureADDevice",
            "id": "{{AzureAdDeviceId}}"
        }
    ]
}
```

<br>

### List updatable assets 

---
> Request

```
GET https://graph.microsoft.com/beta/admin/windows/updates/updatableAssets
```

<br>

### Get updatable asset 

---
> Request

```
GET https://graph.microsoft.com/beta/admin/windows/updates/updatableAssets/{{UpdatableAssetId}}
```

<br>

### Delete updatable asset 

---
> Request

```
DELETE https://graph.microsoft.com/beta/admin/windows/updates/deployments/{{UpdatableAssetId}}
```

<br>

### Get groups 

---
> Request

```
GET https://graph.microsoft.com/v1.0/groups
```

<br>

### Get items trending around me 

---
> Request

```
GET https://graph.microsoft.com/beta/me/insights/trending
```

<br>

### Get people I'm working with 

---
> Request

```
GET https://graph.microsoft.com/beta/me/workingWith
```

<br>

### Get rooms 

---
> Request

```
GET https://graph.microsoft.com/beta/me/findRooms
```

<br>

### Get my events for next week 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/calendarview?startdatetime={{Today}}&enddatetime={{NextWeek}}
```

> Query parameters

**`startdatetime`**

**`enddatetime`**

<br>

### Get my calendars 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/calendars
```

<br>

### Add Microsoft Graph community call event 

---
> Request

```
POST https://graph.microsoft.com/v1.0/me/events
```


> Body

```json
{
  "subject": "Microsoft Graph community call",
  "body": {
    "contentType": "HTML",
    "content": "Call link: https://aka.ms/mmkv1b Submit a question: https://aka.ms/ybuw2i"
  },
  "start": {
    "dateTime": "2018-09-04T08:00:00",
    "timeZone": "Pacific Standard Time"
  },
  "end": {
    "dateTime": "2018-09-04T09:00:00",
    "timeZone": "Pacific Standard Time"
  },
  "location": {
    "displayName": "Skype for Business"
  },
  "recurrence": {
    "pattern": {
      "type": "relativeMonthly",
      "interval": 1,
      "daysOfWeek": [
        "Tuesday"
      ],
      "index": "first"
    },
    "range": {
      "type": "noEnd",
      "startDate": "2017-08-29"
    }
  }
}
```

<br>

### Get my Microsoft Graph community call events 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/events?$filter=subject eq 'Microsoft Graph community call'
```

> Query parameters

**`$filter`**

<br>

### Get my messages 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/messages
```

<br>

### Get my important messages 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/messages?$filter=importance eq 'high'
```

> Query parameters

**`$filter`**

<br>

### Get my messages from an address 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/messages?$filter=(from/emailAddress/address) eq '{{UserName}}'
```

> Query parameters

**`$filter`**

<br>

### Search my messages for "Weekly Digest" 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/messages?$search="Weekly Digest"
```

> Query parameters

**`$search`**

<br>

### Get my messages I'm at mentioned in 

---
> Request

```
GET https://graph.microsoft.com/beta/me/messages?$filter=mentionsPreview/isMentioned eq true&$select=subject,sender,receivedDateTime
```

> Query parameters

**`$filter`**

**`$select`**

<br>

### Get a message 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/messages/{{MessageId}}
```

<br>

### Get my mailbox rules 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messagerules
```

<br>

### Get my categories 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/outlook/masterCategories
```

<br>

### Get email headers 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/messages?$select=internetMessageHeaders&$top=1
```

> Query parameters

**`$select`**

**`$top`**

<br>

### Send mail 

---
> Request

```
POST https://graph.microsoft.com/v1.0/me/sendMail
```


> Body

```json
{
  "message": {
    "subject": "Meet for lunch?",
    "body": {
      "contentType": "Text",
      "content": "The new cafeteria is open."
    },
    "toRecipients": [
      {
        "emailAddress": {
          "address": "{{UserName}}"
        }
      }
    ],
    "ccRecipients": [
      {
        "emailAddress": {
          "address": "{{UserName}}"
        }
      }
    ]
  },
  "saveToSentItems": "false"
}
```

<br>

### Get mailbox settings 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/mailboxSettings
```

<br>

### Set automatic replies 

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/me/mailboxSettings
```


> Body

```json
{
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#Me/mailboxSettings",
"automaticRepliesSetting": {
        "status": "scheduled",
        "externalAudience": "contactsOnly",
        "internalReplyMessage": "<html>\n<body>\n<div>I'm on vacation!</div>\n<div><br>\n</div>\n<div>Kindly regards</div>\n<div></div>\n</body>\n</html>\n",
        "externalReplyMessage": "<html>\n<body>\n<div></div>\n<div>I'm on vacation.</div>\n<div><br>\n</div>\n<div>Kindly regards</div>\n</body>\n</html>\n",
        "scheduledStartDateTime": {
            "dateTime": "2019-07-15T08:00:00.0000000",
            "timeZone": "Europe/Berlin"
        },
        "scheduledEndDateTime": {
            "dateTime": "2019-08-09T16:00:00.0000000",
            "timeZone": "Europe/Berlin"
        }
    }
}
```

<br>

### Search messages 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "message"
            ],
            "query": {
                "queryString": "contoso"
            }
        }
    ]
}
```

<br>

### Search file and connector interleaving Results 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "listItem",
                "externalItem"
            ],
            "contentSources": [
                "/external/connections/*"
            ],
            "query": {
                "queryString": "test"
            },
            "from": 0,
            "size": 15
        }
    ]
}
```

<br>

### Search teams messages 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "chatMessage"
            ],
            "query": {
                "queryString": "contoso"
            }
        }
    ]
}
```

<br>

### Search messages top results 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "message"
            ],
            "query": {
                "queryString": "contoso"
            },
            "enableTopResults": true
        }
    ]
}
```

<br>

### Search events 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "event"
            ],
            "query": {
                "queryString": "contoso"
            }
        }
    ]
}
```

<br>

### Search files and folders 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "driveItem"
            ],
            "query": {
                "queryString": "contoso"
                //"queryString": "contoso filetype:pdf OR filetype:docx"
                //"queryString": "contoso path:\"https://contoso.sharepoint.com/sites/Team Site/Documents/\\""                              
            }
        }
    ]
}
```

<br>

### Search lists 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "list"
            ],
            "query": {
                "queryString": "*"
            }
        }
    ]
}
```

<br>

### Search list items 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "listItem"
            ],
            "query": {
                "queryString": "contoso"
            }
        }
    ]
}
```

<br>

### Search with XRANK 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "listItem"
            ],
            "query": {
                "queryString": "cat XRANK(cb=100) dog"
            }
        }
    ]
}
```

<br>

### Search list items with property selection 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "listItem"
            ],
            "query": {
                "queryString": "issue"
            },
            "fields": [
                "id",
                "name",                
                "contentclass",
                "title",
                "fooCustomProperty"
            ]
        }
    ]
}
```

<br>

### Search sites 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "site"
            ],
            "query": {
                "queryString": "contoso"
            }
        }
    ]
}
```

<br>

### Search drives 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "drive"
            ],
            "query": {
                "queryString": "*"
                //Note that personal OneDrive is not returned in this query
            }
        }
    ]
}
```

<br>

### Search acronym 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "acronym"
            ],
            "query": {
                "queryString": "define KQL"
            }
        }
    ]
}
```

<br>

### Search bookmark 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "bookmark"
            ],
            "query": {
                "queryString": "yammer"
            }
        }
    ]
}
```

<br>

### Search qna 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "bookmark"
            ],
            "query": {
                "queryString": "yammer"
            }
        }
    ]
}
```

<br>

### Search result template 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "externalItem"
            ],
            "contentSources": [
                "/external/connections/sampleConnectionId"
            ],
            "query": {
                "queryString": "sample"
            },
            "resultTemplateOptions": {
                "enableResultTemplate": true
            }
        }
    ]
}
```

<br>

### Search external items 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "externalItem"
            ],
            "contentSources": [
                "/external/connections/sampleConnectionId"
            ],
            "query": {
                "queryString": "sample"
            },
            "fields": [
                "title",
                "iconurl",
                "lastModifiedDate"
            ]
        }
    ]
}
```

<br>

### Page search results 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "driveItem"
            ],
            "query": {
                "queryString": "contoso"
            },
            "from": 0,
            "size": 15
        }
    ]
}
```

<br>

### Sort search results 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "driveItem"
            ],
            "query": {
                "queryString": "contoso"
            },
            "sortProperties": [
                {
                    "name": "lastModifiedDateTime",
                    "isDescending": "true" // default is false
                }
            ]
        }
    ]
}
```

<br>

### Request spelling correction 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
  "requests": [
    {
      "entityTypes": [
        "message"
      ],
      "query": {
        "queryString": "informatino"
      },
      "from": 0,
      "size": 5
    }
  ],
  "queryAlterationOptions": {
    "enableSuggestion": true,
    "enableModification": true
  }
}
```

<br>

### Refine results with string aggregations 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "listItem"
            ],
            "query": {
                "queryString": "contoso"
            },
            "aggregations": [
                {
                    "field": "FileType",
                    "size": 20,
                    "bucketDefinition": {
                        "sortBy": "count",
                        "isDescending": "true",
                        "minimumCount": 0
                    }
                },
                {
                    "field": "contentclass",
                    "size": 20,
                    "bucketDefinition": {
                        "sortBy": "keyAsString",
                        "isDescending": "true",
                        "minimumCount": 0
                    }
                }
            ]
        }
    ]
}
```

<br>

### Refine results with numeric aggregations 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "Requests": [
        {
            "entityTypes": [
                "listItem"
            ],
            "query": {
                "queryString": "contoso"
            },
            "aggregations": [
                {
                    "field": "Size",
                    "size": 15,
                    "bucketDefinition": {
                        "sortBy": "keyAsNumber",
                        "isDescending": "true",
                        "minimumCount": 0,
                        "ranges": [
                            {
                                "to": "100"
                            },
                            {
                                "from": "100",
                                "to": "1000"
                            },
                            {
                                "from": "1000"
                            }
                        ]
                    }
                }
            ]
        }
    ]
}
```

<br>

### Apply refined query passing the aggregationToken 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "Requests": [
        {
            "entityTypes": [
                "driveItem"
            ],
            "query": {
                "queryString": "contoso"
            },
            "aggregationFilters": [
                "contentclass:\"ǂǂ5354535f4c6973744974656d5f446f63756d656e744c696272617279\"",
                "FileType:\"ǂǂ646f6378\""                
            ],
            "aggregations": [
                {
                    "field": "FileType",
                    "size": 20,
                    "bucketDefinition": {
                        "sortBy": "count",
                        "isDescending": "true",
                        "minimumCount": 0
                    }
                },
                {
                    "field": "contentclass",
                    "size": 15,
                    "bucketDefinition": {
                        "sortBy": "keyAsString",
                        "isDescending": "true",
                        "minimumCount": 0
                    }
                }
            ]
        }
    ]
}
```

<br>

### Trim duplicated SharePoint search results 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "driveItem"
            ],
            "query": {
                "queryString": "contoso"
            },
            "trimDuplicate": true
        }
    ]
}
```

<br>

### Search with queryTemplate 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "driveItem"
            ],
            "query": {
                "queryString": "contoso",
                "queryTemplate": "({searchTerms})"
            }
        }
    ]
}
```

<br>

### Search with basic collapse 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "listItem"
            ],
            "query": {
                "queryString": "test"
            },
            "fields": [
                "title"
            ],
            "collapseProperties": [
                {
                    "fields": [
                        "title"
                    ],
                    "limit": 3
                }
            ]
        }
    ]
}
```

<br>

### Search with compound collapse 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "listItem"
            ],
            "query": {
                "queryString": "cat"
            },
            "fields": [
                "title",
                "createdBy"
            ],
            "collapseProperties": [
                {
                    "fields": [
                        "title",
                        "createdBy"
                    ],
                    "limit": 3
                }
            ]
        }
    ]
}
```

<br>

### Search with multi-level collapse 

---
> Request

```
POST https://graph.microsoft.com/beta/search/query
```


> Body

```json
{
    "requests": [
        {
            "entityTypes": [
                "listItem"
            ],
            "query": {
                "queryString": "cat"
            },
            "fields": [
                "title",
                "createdBy"
            ],
            "collapseProperties": [
                {
                    "fields": [
                        "title"
                    ],
                    "limit": 3
                },
                {
                    "fields": [
                        "createdBy"
                    ],
                    "limit": 2
                }
            ]
        }
    ]
}
```

<br>

### Get Planner tasks 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/planner/tasks
```

<br>

### Get Planner tasks for a user 

---
> Request

```
GET https://graph.microsoft.com/v1.0/users/{{UserName}}/planner/tasks
```

<br>

### Get Planner plans associated with group 

---
> Request

```
GET https://graph.microsoft.com/v1.0/groups/{{GroupId}}/planner/plans
```

<br>

### Get plan 

---
> Request

```
GET https://graph.microsoft.com/v1.0/planner/plans/{{PlanId}}
```

<br>

### Update plan 

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/planner/plans/{{PlanId}}
```


> Body

```json
{
  "title": "Updated plan title"
}
```

<br>

### Get plan buckets 

---
> Request

```
GET https://graph.microsoft.com/v1.0/planner/plans/{{PlanId}}/buckets
```

<br>

### Create a bucket in a plan 

---
> Request

```
POST https://graph.microsoft.com/v1.0/planner/buckets
```


> Body

```json
{
  "name": "New bucket",
  "planId": "{{PlanId}}",
  "orderHint": " !"
}
```

<br>

### Update a bucket 

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/planner/buckets/{{BucketId}}
```


> Body

```json
{
  "name": "Updated bucket name"
}
```

<br>

### Get Planner tasks for a plan 

---
> Request

```
GET https://graph.microsoft.com/v1.0/planner/plans/{{PlanId}}/tasks
```

<br>

### Get Planner task by id 

---
> Request

```
GET https://graph.microsoft.com/v1.0/planner/tasks/{{TaskId}}
```

<br>

### Create a Planner task 

---
> Request

```
POST https://graph.microsoft.com/v1.0/planner/tasks
```


> Body

```json
{
  "planId": "{{PlanId}}",
  "title": "New Task",
  "assignments": {}
}
```

<br>

### Update a Planner task 

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/planner/tasks/{{TaskId}}
```


> Body

```json
{
  "title": "Updated task title"
}
```

<br>

### Get Planner task details 

---
> Request

```
GET https://graph.microsoft.com/v1.0/planner/tasks/{{TaskId}}/details
```

<br>

### Get my profile 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me
```

<br>

### Get my about me 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/aboutMe
```

<br>

### Get my skills 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/?$select=displayName,skills
```

> Query parameters

**`$select`**

<br>

### Get my manager 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/manager
```

<br>

### Get my direct reports 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/directReports
```

<br>

### Get my groups 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/memberOf
```

<br>

### Get my photo 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/photo/$value
```

<br>

### Get users 

---
> Request

```
GET https://graph.microsoft.com/v1.0/users
```

<br>

### Get users $filter 

---
> Request

```
GET https://graph.microsoft.com/v1.0/users?$filter=Department eq 'Finance'
```

> Query parameters

**`$filter`**

<br>

### Get user's profile by email 

---
> Request

```
GET https://graph.microsoft.com/v1.0/users/{{UserName}}
```

<br>

### Get a user's profile by id 

---
> Request

```
GET https://graph.microsoft.com/v1.0/users/{{UserId}}
```

<br>

### Get a user's photo 

---
> Request

```
GET https://graph.microsoft.com/v1.0/users/{{UserId}}/photo/$value
```

<br>

### Invite a guest user 

---
> Request

```
POST https://graph.microsoft.com/v1.0/invitations
```


> Body

```json
{ 
    "invitedUserDisplayName": "<Display Name of Invited User>", 
    "invitedUserEmailAddress": "<Email Address of Invited User>", 
    "invitedUserMessageInfo": {
        "messageLanguage": "en-US",
        "ccRecipients": [
             {
                "emailAddress": {
                    "name": "<Optional CC for Invitation>",
                    "address": "<Optional CC Email Address for Invitation>"
                 }
             }
        ],
        "customizedMessageBody": "Hi, you have just been invited to Azure AD with Postman using Microsoft Graph!"
     },
    "sendInvitationMessage": true, 
    "inviteRedirectUrl": "https://myapps.microsoft.com" 
} 
```

<br>

### Get my files 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/drive/root/children
```

<br>

### Get my recent files 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/drive/recent
```

<br>

### Get files shared with me 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/drive/sharedWithMe
```

<br>

### Search my OneDrive 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/drive/root/search(q='finance')?select=name,id,webUrl
```

> Query parameters

**`select`**

<br>

### Create a folder 

---
> Request

```
POST https://graph.microsoft.com/v1.0/me/drive/root/children
```


> Body

```json
{
  "name": "New Folder",
  "folder": {}
}
```

<br>

### Get my To Do lists 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/todo/lists
```

<br>

### Get my To Do list 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/todo/lists/{{TaskListId}}
```

<br>

### Create a To Do list 

---
> Request

```
POST https://graph.microsoft.com/v1.0/me/todo/lists/
```


> Body

```json
{
  "displayName": "Postman created list"
}
```

<br>

### Update a To Do list 

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/me/todo/lists/{{TaskListId}}
```


> Body

```json
{
  "displayName": "Postman created items"
}
```

<br>

### Delete a To Do list 

---
> Request

```
DELETE https://graph.microsoft.com/v1.0/me/todo/lists/{{TaskListId}}
```

<br>

### Get my To Do list tasks 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/todo/lists/{{TaskListId}}/tasks
```

<br>

### Create a To Do task in a list 

---
> Request

```
POST https://graph.microsoft.com/v1.0/me/todo/lists/{{TaskListId}}/tasks
```


> Body

```json
{
   "title":"Postman created Task",
   "linkedResources":[
      {
         "webUrl":"http://microsoft.com",
         "applicationName":"Microsoft",
         "displayName":"Microsoft"
      }
   ]
}
```

<br>

### Update a To Do task in a list 

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/me/todo/lists/{{TaskListId}}/tasks/{{TaskId}}
```


> Body

```json
{
   "dueDateTime":{
      "dateTime":"2021-04-19T00:00:00",
      "timeZone":"Eastern Standard Time"
   }
}
```

<br>

### Delete a To Do task in a list 

---
> Request

```
DELETE https://graph.microsoft.com/v1.0/me/todo/lists/{{TaskListId}}/tasks/{{TaskId}}
```

<br>

### Get my joined teams 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/joinedTeams
```

<br>

### Get members of a team 

---
> Request

```
GET https://graph.microsoft.com/v1.0/groups/{{TeamId}}/members
```

<br>

### Get channels of a team 

---
> Request

```
GET https://graph.microsoft.com/v1.0/teams/{{TeamId}}/channels
```

<br>

### Get channel info 

---
> Request

```
GET https://graph.microsoft.com/v1.0/teams/{{TeamId}}/channels/{{ChannelId}}
```

<br>

### Create team 

---
> Request

```
POST https://graph.microsoft.com/v1.0/teams
```


> Body

```json
{
  "template@odata.bind": "https://graph.microsoft.com/v1.0/teamsTemplates('standard')",
  "displayName": "My Sample Team",
  "description": "My Sample Team’s Description"
}
```

<br>

### Create channel 

---
> Request

```
POST https://graph.microsoft.com/v1.0/teams/{{TeamId}}/channels
```


> Body

```json
{
  "displayName": "Architecture Discussion",
  "description": "This channel is where we debate all future architecture plans"
}
```

<br>

### Get apps in a team 

---
> Request

```
GET https://graph.microsoft.com/v1.0/teams/{{TeamId}}/installedApps?$expand=teamsAppDefinition
```

> Query parameters

**`$expand`**

<br>

### Get tabs in a channel 

---
> Request

```
GET https://graph.microsoft.com/v1.0/teams/{{TeamId}}/channels/{{ChannelId}}/tabs?$expand=teamsApp
```

> Query parameters

**`$expand`**

<br>

### Get items in a team drive 

---
> Request

```
GET https://graph.microsoft.com/v1.0/groups/{{TeamId}}/drive/root/children
```

<br>

### Get messages (without replies) in a channel (beta) 

---
> Request

```
GET https://graph.microsoft.com/beta/teams/{{TeamId}}/channels/{{ChannelId}}/messages
```

<br>

### Get a message in a channel (beta) 

---
> Request

```
GET https://graph.microsoft.com/beta/teams/{{TeamId}}/channels/{{ChannelId}}/messages/{{MessageId}}
```

<br>

### Get replies to a message in a channel (beta) 

---
> Request

```
GET https://graph.microsoft.com/beta/teams/{{TeamId}}/channels/{{ChannelId}}/messages/{{MessageId}}/replies
```

<br>

### Get a reply of a message (beta) 

---
> Request

```
GET https://graph.microsoft.com/beta/teams/{{TeamId}}/channels/{{ChannelId}}/messages/{{MessageId}}/replies/{{ReplyId}}
```

<br>

### Create a plain text chat thread (beta) 

---
> Request

```
POST https://graph.microsoft.com/beta/teams/{{TeamId}}/channels/{{ChannelId}}/messages
```


> Body

```json
{
  "body": {
    "content": "Hello World!"
  }
}
```

<br>

### Create an HTML chat thread (beta) 

---
> Request

```
POST https://graph.microsoft.com/beta/teams/{{TeamId}}/channels/{{ChannelId}}/messages
```


> Body

```json
{
  "body": {
    "contentType": "html",
    "content": "<div><div>\n<div><img alt=\"GIF Image\" height=\"250\" src=\"https://media3.giphy.com/media/f5xmRWRu4zxxh2mE5v/giphy.gif?cid=de9bf95eevnce0lknjlbneccchvdkn991jea1gtmw2zmvdke&amp;rid=giphy.gif\" width=\"250\" style=\"max-height:250px; width:250px; height:250px\"></div>\n\n\n</div>\n</div>"
  }
}
```

<br>

### Get people 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/people
```

<br>

### Get people $top $skip 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/people?$top=10&$skip=10
```

> Query parameters

**`$top`**

**`$skip`**

<br>

### Get people $orderby 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/people/?$orderby=DisplayName
```

> Query parameters

**`$orderby`**

<br>

### Get people $filter 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/people/?$select=DisplayName,scoredEmailAddresses&$filter=DisplayName eq 'New Hires'
```

> Query parameters

**`$select`**

**`$filter`**

<br>

### Get people $search 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/people/?$search=j
```

> Query parameters

**`$search`**

<br>

### Get people $search topic 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/people/?$search="ma topic: feature planning"
```

> Query parameters

**`$search`**

<br>

### Get people $search fuzzy 

---
> Request

```
GET https://graph.microsoft.com/v1.0/me/people/?$search="John"
```

> Query parameters

**`$search`**

<br>

### Get a user's related people 

---
> Request

```
GET https://graph.microsoft.com/v1.0/users('{{UserName}}')/people/
```

<br>

### Get all connections 

---
> Request

```
GET https://graph.microsoft.com/v1.0/external/connections
```

<br>

### Create connection 

---
> Request

```
POST https://graph.microsoft.com/v1.0/external/connections
```


> Body

```json
{
    "id": "sampleConnectionId",
    "name": "Sample connection",
    "description": "Sample connection description"
}
```

<br>

### Get connection 

---
> Request

```
GET https://graph.microsoft.com/v1.0/external/connections/sampleConnectionId
```

<br>

### Delete connection 

---
> Request

```
DELETE https://graph.microsoft.com/v1.0/external/connections/sampleConnectionId
```

<br>

### Register schema 

---
> Request

```
POST https://graph.microsoft.com/v1.0/external/connections/sampleConnectionId/schema
```


> Body

```json
{
    "baseType": "microsoft.graph.externalItem",
    "properties": [
        {
            "name": "id",
            "type": "string",
            "isSearchable": false,
            "isRetrievable": true,
            "isQueryable": false,
            "labels": [],
            "aliases": []
        },
        {
            "name": "title",
            "type": "string",
            "isSearchable": true,
            "isRetrievable": true,
            "isQueryable": true,
            "labels": [
                "title"
            ],
            "aliases": []
        },
        {
            "name": "extension",
            "type": "string",
            "isSearchable": true,
            "isRetrievable": true,
            "isQueryable": true,
            "labels": [],
            "aliases": []
        },
        {
            "name": "createdBy",
            "type": "string",
            "isSearchable": true,
            "isRetrievable": true,
            "isQueryable": true,
            "labels": [
                "createdBy"
            ],
            "aliases": []
        },
        {
            "name": "createdDateTime",
            "type": "dateTime",
            "isSearchable": false,
            "isRetrievable": true,
            "isQueryable": true,
            "labels": [
                "createdDateTime"
            ],
            "aliases": []
        },
        {
            "name": "lastModifiedBy",
            "type": "string",
            "isSearchable": false,
            "isRetrievable": true,
            "isQueryable": true,
            "labels": [],
            "aliases": []
        },
        {
            "name": "lastModifiedDate",
            "type": "dateTime",
            "isSearchable": false,
            "isRetrievable": true,
            "isQueryable": true,
            "labels": [
                "lastModifiedDateTime"
            ],
            "aliases": []
        },
        {
            "name": "url",
            "type": "string",
            "isSearchable": false,
            "isRetrievable": true,
            "isQueryable": false,
            "labels": [
                "url"
            ],
            "aliases": []
        },
        {
            "name": "description",
            "type": "string",
            "isSearchable": false,
            "isRetrievable": true,
            "isQueryable": false,
            "labels": [],
            "aliases": []
        },
        {
            "name": "authors",
            "type": "stringCollection",
            "isSearchable": false,
            "isRetrievable": true,
            "isQueryable": false,
            "labels": [
                "authors"
            ],
            "aliases": []
        }
    ]
}
```

<br>

### Get schema 

---
> Request

```
GET https://graph.microsoft.com/v1.0/external/connections/sampleConnectionId/schema
```

<br>

### Get connection operation status 

---
> Request

```
GET {{OperationUrl}}
```

<br>

### Put item 

---
> Request

```
PUT https://graph.microsoft.com/v1.0/external/connections/sampleConnectionId/items/sampleItemId
```


> Body

```json
{
    "acl": [
        {
            "type": "everyone",
            "value": "c5f19b2d-0a77-454a-9b43-abf298c3b34e",
            "accessType": "grant"
        }
    ],
    "properties": {
        "title": "Sample item title",
        "extension": "docx",
        "createdBy": "John Doe",
        "createdDateTime": "2021-04-27T11:04:00Z",
        "iconUrl": "https://contentdepot.blob.core.windows.net/filedepot/sampleIconUrl.png",
        "authors": [
            "John Doe"
        ],
        "authors@odata.type": "Collection(String)",
        "lastModifiedDate": "2021-04-27T11:04:00Z",
        "url": "https://sampleItemUrl.com",
        "containerName": "Sample container name",
        "containerUrl": "https://sampleContainerUrl.com"
    },
    "content": {
        "type": "text",
        "value": "Empower customers and partners to be more productive by enabling them to bring content and activity information and allow external content to participate in Microsoft Search and OfficeHub experiences so that they find relevant and actionable information across all their applications."
    }
}
```

<br>

### Get item 

---
> Request

```
GET https://graph.microsoft.com/v1.0/external/connections/sampleConnectionId/items/sampleItemId
```

<br>

### Delete item 

---
> Request

```
DELETE https://graph.microsoft.com/v1.0/external/connections/sampleConnectionId/items/sampleItemId
```

<br>

### Create group 

---
> Request

```
POST https://graph.microsoft.com/v1.0/external/connections/sampleConnectionId/groups
```


> Body

```json
{
   "id":"graphConnectorGroupId",
   "displayName":"Display name of group sampleExternalGroupId"
}
```

<br>

### Get group 

---
> Request

```
GET https://graph.microsoft.com/v1.0/external/connections/sampleConnectionId/groups/graphConnectorGroupId
```

<br>

### Add AAD user as member 

---
> Request

```
POST https://graph.microsoft.com/v1.0/external/connections/sampleConnectionId/groups/graphConnectorGroupId/members/
```


> Body

```json
{
   "id":"e42f427c-f33f-4389-afd8-db432ff6a338",
   "type":"user"
}
```

<br>

### Add AAD group as member 

---
> Request

```
POST https://graph.microsoft.com/v1.0/external/connections/sampleConnectionId/groups/graphConnectorGroupId/members/
```


> Body

```json
{
   "id":"e42f427c-f33f-4389-afd8-db432ff6a338",
   "type":"group"
}
```

<br>

### Add connector group as member 

---
> Request

```
POST https://graph.microsoft.com/v1.0/external/connections/sampleConnectionId/groups/graphConnectorGroupId/members/
```


> Body

```json
{
   "id":"childGraphConnectorGroupId",
   "type":"externalGroup"
}
```

<br>

### Remove member 

---
> Request

```
DELETE https://graph.microsoft.com/v1.0/external/connections/sampleConnectionId/groups/graphConnectorGroupId/members/childGraphConnectorGroupId
```

<br>

### Delete group 

---
> Request

```
DELETE https://graph.microsoft.com/v1.0/external/connections/sampleConnectionId/groups/graphConnectorGroupId
```

<br>

### Get a user's messages 

---
> Request

```
GET https://graph.microsoft.com/v1.0/users/{{UserId}}/messages
```

<br>

### Get a user's message 

---
> Request

```
GET https://graph.microsoft.com/v1.0/users/{{UserId}}/messages/{{MessageId}}
```

<br>

### Get sites 

---
> Request

```
GET https://graph.microsoft.com/v1.0/sites
```

<br>

### Get drives 

---
> Request

```
GET https://graph.microsoft.com/v1.0/sites/{{SiteID}}/drives
```

<br>

### Get subscriptions 

---
> Request

```
GET https://graph.microsoft.com/v1.0/subscriptions
```

<br>

### Update subscription 

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/subscriptions/{{SubscriptionId}}
```


> Body

```json
{
   "expirationDateTime":"2019-05-19T12:41:53.2962802Z"
}
```

<br>

### Create subscription 

---
> Request

```
POST https://graph.microsoft.com/beta/subscriptions
```


> Body

```json
{
  "changeType": "created,updated",
  "notificationUrl": "{{notificationUrl}}",
  "resource": "{{resourcePath}}",
  "expirationDateTime": "{{expirationDateTime}}",
  "clientState": "secretClientState"
}
```

<br>

### Get team members 

---
> Request

```
GET https://graph.microsoft.com/v1.0/teams/{{GroupId}}/members
```

<br>

### Get single team member 

---
> Request

```
GET https://graph.microsoft.com/v1.0/teams/{{GroupId}}/members/{{UserId}}
```

<br>

### Get channel members 

---
> Request

```
GET https://graph.microsoft.com/v1.0/teams/{{GroupId}}/channels/{{ChannelId}}/members
```

<br>

### Add channel member 

---
> Request

```
POST https://graph.microsoft.com/v1.0/teams/{{TeamId}}/channels/{{ChannelId}}/members
```


> Body

```json
{
    "@odata.type": "#microsoft.graph.aadUserConversationMember",
    "roles": ["owner"],
    "user@odata.bind": "https://graph.microsoft.com/v1.0/users/8b081ef6-4792-4def-b2c9-c363a1bf41d5"
}
```

<br>

### Remove team member 

---
> Request

```
DELETE https://graph.microsoft.com/v1.0/teams/{{TeamId}}/members/{{UserId}}
```

<br>

### Remove channel member 

---
> Request

```
DELETE https://graph.microsoft.com/v1.0/teams/{{TeamId}}/channels/{{ChannelId}}members/{{UserId}}
```

<br>

### Update team member 

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/teams/{{GroupId}}/members/{{UserId}}
```


> Body

```json
{
  "@odata.type":"#microsoft.graph.aadUserConversationMember",
  "roles": ["owner"]
}
```

<br>

### Update channel member 

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/teams/{{GroupId}}/channels/{{ChannelId}}/members/{{UserId}}
```


> Body

```json
{
  "@odata.type":"#microsoft.graph.aadUserConversationMember",
  "roles": ["owner"]
}
```

<br>

### Add team member 

---
> Request

```
POST https://graph.microsoft.com/v1.0/teams/{{GroupId}}/members
```


> Body

```json
{
    "@odata.type": "#microsoft.graph.aadUserConversationMember",
    "roles": ["owner"],
    "user@odata.bind": "https://graph.microsoft.com/v1.0/users/a82083e7-cc7c-48a4-9ed1-ce70e42f7453"
}
```

<br>

### Get user's joined teams 

---
> Request

```
GET https://graph.microsoft.com/v1.0/users/{{UserId}}/joinedTeams
```

<br>

### Get primary channel 

---
> Request

```
GET https://graph.microsoft.com/v1.0/teams/{{GroupId}}/primaryChannel
```

<br>

### Get team channels 

---
> Request

```
GET https://graph.microsoft.com/v1.0/teams/{{GroupId}}/channels
```

<br>

### Get team 

---
> Request

```
GET https://graph.microsoft.com/v1.0/teams/{{TeamId}}
```

<br>

### Delete team 

---
> Request

```
DELETE https://graph.microsoft.com/v1.0/groups/{{GroupId}}
```

<br>

### Create team from group 

---
> Request

```
PUT https://graph.microsoft.com/v1.0/groups/{{GroupId}}/team
```


> Body

```json
{  
  "memberSettings": {
    "allowCreatePrivateChannels": true,
    "allowCreateUpdateChannels": true
  },
  "messagingSettings": {
    "allowUserEditMessages": true,
    "allowUserDeleteMessages": true
  },
  "funSettings": {
    "allowGiphy": true,
    "giphyContentRating": "strict"
  }
}
```

<br>

### Update team 

---
> Request

```
PATCH https://graph.microsoft.com/v1.0/teams/{{TeamId}}
```


> Body

```json
{  
  "memberSettings": {
    "allowCreateUpdateChannels": true
  },
  "messagingSettings": {
    "allowUserEditMessages": true,
    "allowUserDeleteMessages": true
  },
  "funSettings": {
    "allowGiphy": true,
    "giphyContentRating": "strict"
  }
}
```

<br>

### Create team 

---
> Request

```
POST https://graph.microsoft.com/v1.0/teams/{{TeamId}}/channels/{{ChannelId}}/members
```


> Body

```json
{
  "template@odata.bind": "https://graph.microsoft.com/v1.0/teamsTemplates('standard')",
  "displayName": "My Sample Team",
  "description": "My Sample Team’s Description"
}
```

<br>

### Archive team 

---
> Request

```
POST https://graph.microsoft.com/v1.0/teams/{{TeamId}}/archive
```


> Body

```json
{
    "shouldSetSpoSiteReadOnlyForMembers": true
}
```

<br>

### Clone team 

---
> Request

```
POST https://graph.microsoft.com/v1.0/teams/{{TeamId}}/clone
```


> Body

```json
{  
     "displayName": "Library Assist",
     "description": "Self help community for library",
     "mailNickname": "libassist",
     "partsToClone": "apps,tabs,settings,channels,members",
     "visibility": "public"
}
```

<br>

### Unarchive team 

---
> Request

```
POST https://graph.microsoft.com/v1.0/teams/{{TeamId}}/unarchive
```

<br>

### Get users 

---
> Request

```
GET https://graph.microsoft.com/v1.0/users
```

<br>

### Invite guest user 

---
> Request

```
POST https://graph.microsoft.com/v1.0/invitations
```


> Body

```json
{ 
    "invitedUserDisplayName": "<Display Name of Invited User>", 
    "invitedUserEmailAddress": "<Email Address of Invited User>, 
    "invitedUserMessageInfo": {
        "messageLanguage": "en-US",
        "ccRecipients": [
             {
                "emailAddress": {
                    "name": "<Optional CC for Invitation>",
                    "address": "<Optional CC Email Address for Invitation>"
                 }
             }
        ],
        "customizedMessageBody": "Hi, you have just been invited to Azure AD with Postman using Microsoft Graph!"
     },
    "sendInvitationMessage": true, 
    "inviteRedirectUrl": "https://myapps.microsoft.com" 
} 
```

<br>

### List retention labels 

---
> Request

```
GET https://graph.microsoft.com/beta/security/labels/retentionLabels
```

<br>

### Subscription validation 

---
> Request

```
POST http://localhost:5000/api/notification?validationToken=something
```

> Query parameters

**`validationToken`**

random validation token passed by the Microsoft Graph when validating the notificationURL

<br>

### v1.0 $metadata 

---
> Request

```
GET https://graph.microsoft.com/v1.0/$metadata
```

<br>

### beta $metadata 

---
> Request

```
GET https://graph.microsoft.com/beta/$metadata
```

<br>

Generated with [Palourde](https://github.com/bagabool/palourde)