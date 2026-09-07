---
doc_id: developer-cisco-com-site-paws-documents-api-reference-7db07208f4
source_url: https://developer.cisco.com/site/paws/documents/api-reference/
retrieved_at: 2026-09-07T14:17:40.603918+00:00
---

About this Document

Title: PAWS API Reference

Version: V11.0

Publisher: DevNet, Cisco's Developer Program

Publisher Address: Cisco Systems, Inc., 150 W Tasman Dr, San Jose, CA 95134,
                        USA

Comments: DevNet Slate is based upon the open source project called Slate

Published Date: November 23, 2015

# Introduction

The Platform Administrative Web Service (PAWS) is a XML/SOAP based interface that allows applications to
                initiate and monitor upgrades on multiple Unified Communications clusters from a single management
                client.

# Authentication

See Authentication .

# Developer Guide

The Cisco Platform Administrative Web Services Developer
                Guide contains information about how to gather logs and traces, troubleshooting tips and more
                information about using PAWS.

# Base URL

All PAWS requests should be sent via HTTP POST to the base URL below, where {service} is the name of the PAWS sub-service, for example APIVersionService :

https://{paws_host}/platform-services/services/{service}

# Web Service Addressing

PAWS supports both synchronous and asynchronous operations by using the Web Service Addressing (WSA)
                standard to allow the application to provide a destination URL in the <wsa:ReplyTo> request SOAP header, to which asynchronous responses should be sent. Synchronous requests should use the
                WSA ‘Anonymous URL’ in the <wsa:ReplyTo> header:

http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous

Example synchronous PAWS request with WSA header

```
<soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser= "http://services.api.platform.vos.cisco.com" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:getAPIVersion </wsa:Action> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:MessageID> uuid:26634481-3273-4a70-b537-ab4b874e4d6b </wsa:MessageID> <wsa:To/> </soapenv:Header> <soapenv:Body> <ser:getAPIVersion/> </soapenv:Body> </soapenv:Envelope>
```

- Asynchronous requests: the response destination URL

- Synchronous requests: the WSA Anonymous URL

Note that all PAWS requests must include these WSA headers, including synchronous requests.

# Response RemoteMessages

Many PAWS API responses include a <remoteMessages> element, which
                provides brief messages about the operation from the PAWS service.

Example remoteMessages element

```
... <ax285:remoteMessages xsi:type= "ax285:RemoteMessage" > <ax286:error> true </ax286:error> <ax286:info> false </ax286:info> <ax286:messageKey> error.validation.invalid </ax286:messageKey> <ax286:messageType> internal.message.error </ax286:messageType> <ax286:warning> false </ax286:warning> <ax285:messageParams> node.host </ax285:messageParams> </ax285:remoteMessages> ...
```

If xsi:nil=“true” , then there are no remote messages. Otherwise:

- true - an error occurred

- false - no error

- true - this is an info-level message

- false - not an info message

- messageKey - A result code such as internal.request.denied.lock if such an error occurred

- messageType - The type of error, such as internal.message.error

- true - this is a warning

- false - not a warning

- messageParams - Information about the message (there can be more than one
                    messageParam)

# APIVersionService

## getAPIVersion

The getAPIVersion method returns the API version of PAWS.

### getAPIVersion Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:getAPIVersion </wsa:Action> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:MessageID> uuid:26634481-3273-4a70-b537-ab4b874e4d6b </wsa:MessageID> </soapenv:Header> <soapenv:Body /> </soapenv:Envelope>
```

None.

### getAPIVersion Response Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:getAPIVersionResponse </wsa:Action> <wsa:RelatesTo> uuid:26634481-3273-4a70-b537-ab4b874e4d6b </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getAPIVersionResponse xmlns:ns= "http://server_url" > <ns:return xmlns:ax25= "http://server_url/xsd" xmlns:ax26= "http://server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax25:APIVersionResponse" > <ax25:result> internal.request.complete </ax25:result> <ax25:APIVersion> 5.0.2.0 </ax25:APIVersion> </ns:return> </ns:getAPIVersionResponse> </soapenv:Body> </soapenv:Envelope>
```

Return element children:

# CancelUpgradeService

## cancelUpgrade

The cancelUpgrade method cancels an upgrade or COP file installation previously started via the startUpgrade method. This call should always be made asynchronously.

Use UpgradeStageService to check the status of the upgrade.

### cancelUpgrade Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:cancelUpgrade </wsa:Action> <wsa:MessageID> uuid:e08a0e1f-1a36-414c-b8e5-4cbff27c036a </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/ CancelUpgradeService.CancelUpgradeServiceHttpSoap11Endpoint </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <cancelUpgrade xmlns= "http://server_url" /> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

None.

### cancelUpgrade Response Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:FE6356947E20FE3BD91297893141096 </wsa:MessageID> <wsa:Action> urn:cancelUpgradeResponse </wsa:Action> <wsa:RelatesTo> uuid:45c4d6e3-6c04-4115-8fcc-4bc8fe90940b </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:cancelUpgradeResponse xmlns:ns= "http://server_url" > <ns:return xmlns:ax251= "http://server_url/xsd" xmlns:ax252= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax251:CancelUpgradeResponse" > <ax251:result> internal.request.complete </ax251:result> <ax251:upgradeCancelled> true </ax251:upgradeCancelled> </ns:return> </ns:cancelUpgradeResponse> </soapenv:Body> </soapenv:Envelope>
```

Return element children:

- true if upgrade is canceled

- false otherwise

# ClusterNodesService

## getClusterNodes

The getClusterNodes method is deprecated. Use the getClusterStatus request.

## getClusterStatus

This method returns all cluster node information including each node’s cluster authentication
                status.

### getClusterStatus Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getClusterStatus </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <getClusterStatus xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### getClusterStatus Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:98240059-2dc0-4024-aa91-0b93a3ede219 </wsa:MessageID> <wsa:Action> urn:getClusterStatusResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getClusterStatusResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax217= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax218= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax217:ClusterNodeStatusResponse" > <ax217:result> internal.request.complete </ax217:result> <ax217:clusterNodeStatus xsi:type= "ax217:ClusterNodeStatus" > <ax217:address> 10.106.3.82 </ax217:address> <ax217:alias></ax217:alias> <ax217:hostname> rwerer </ax217:hostname> <ax217:primaryNode> 10.106.3.82 </ax217:primaryNode> <ax217:type> cluster.node.type.primary </ax217:type> <ax217:dbRole> cluster.node.type.primary </ax217:dbRole> <ax217:role> 1 </ax217:role> <ax217:status> cluster.node.status.online </ax217:status> </ax217:clusterNodeStatus> </ns:return> </ns:getClusterStatusResponse> </soapenv:Body> </soapenv:Envelope>
```

- address - IP address of the node

- alias - an alpha-numeric identifier for the node

- hostname - the URL of the node’s host server

- primaryNode - IP address of the primary node associated with this node,
                                if node is primary, same as address ClusterNodes element

- type - cluster.node.type.primary if primary node and cluster.node.type.secondary if secondary node

- dbRole - cluster.node.type.primary if primary node and cluster.node.type.secondary if secondary node

- role - The number of the role

- status - cluster.node.status.online if online

## getMyClusterNode

The getMyClusterNode method retrieves information for the node (server) in the cluster that was
                contacted.

### getMyClusterNode Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getMyClusterNode </wsa:Action> <wsa:MessageID> uuid:cd3169b4-9595-4b60-bbfa-ae768423dbea </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/ClusterNodesService.ClusterNodesServiceHttpSoap11Endpoint/ </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <getMyClusterNode xmlns= "http://server_url" /> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

None.

### getMyClusterNode Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:8109AEDEE509351D941299799673199 </wsa:MessageID> <wsa:Action> urn:getMyClusterNodeResponse </wsa:Action> <wsa:RelatesTo> uuid:feb14e8c-ca0a-448a-bf91-447effb66eb1 </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getMyClusterNodeResponse xmlns:ns= "http://server_url" > <ns:return xmlns:ax213= "http://server_url/xsd" xmlns:ax214= "http://server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax213:ClusterNodesResponse" > <ax213:result> internal.request.complete </ax213:result> <ax213:clusterNodes xsi:type= "ax213:ClusterNode" > <ax213:address> server </ax213:address> <ax213:alias> bldr-vcm238 </ax213:alias> <ax213:hostname> server_address </ax213:hostname> <ax213:primary> true </ax213:primary> <ax213:primaryNode> server </ax213:primaryNode> <ax213:secondary> false </ax213:secondary> <ax213:type> cluster.node.type.primary </ax213:type> </ax213:clusterNodes> </ns:return> </ns:getMyClusterNodeResponse> </soapenv:Body> </soapenv:Envelope>
```

- address - IP address of the node

- alias - an alpha-numeric identifier for the node

- hostname - the URL of the node’s host server

- true if primary node

- false otherwise

- primaryNode - IP address of the primary node associated with this node,
                                if node is primary, same as address ClusterNodes element

- true if secondary node

- false otherwise

- type - cluster.node.type.primary if primary node and cluster.node.type.secondary if secondary node

## isClusterReplicationOK

The isClusterReplicationOK method checks if the replication status of the cluster is OK.

### isClusterReplicationOK Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:isClusterReplicationOK </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <isClusterReplicationOK xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### isClusterReplicationOK Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:277fd3ae-533f-48ce-ad0a-c05d5d9b44a0 </wsa:MessageID> <wsa:Action> urn:isClusterReplicationOKResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:isClusterReplicationOKResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax217= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax218= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax217:ClusterReplicationStatusResponse" > <ax217:result> internal.request.complete </ax217:result> <ax217:clusterReplicationStatusOK> true </ax217:clusterReplicationStatusOK> </ns:return> </ns:isClusterReplicationOKResponse> </soapenv:Body> </soapenv:Envelope>
```

- true if status is ok

- false if status is not ok

## isNodeReplicationOK

The isNodeReplicationOK method checks if the replication status of the cluster node is OK..

### isNodeReplicationOK Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:isNodeReplicationOK </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <isNodeReplicationOK xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### isNodeReplicationOK Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:51ac89c6-6725-40af-b54e-aa21dfdee8b9 </wsa:MessageID> <wsa:Action> urn:isNodeReplicationOKResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:isNodeReplicationOKResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax217= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax218= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax217:NodeReplicationStatusResponse" > <ax217:result> internal.request.complete </ax217:result> <ax217:nodeReplicationStatusOK> true </ax217:nodeReplicationStatusOK> </ns:return> </ns:isNodeReplicationOKResponse> </soapenv:Body> </soapenv:Envelope>
```

- true if status is ok

- false if status is not ok

# DataExportService

## dataExport

The dataExport method begins an export of the database to an external FTP server.

### dataExport Request Parameters

```
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:ser="http://services.api.platform.vos.cisco.com">
<soap:Header xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing">
    <wsa:Action>urn:dataExport</wsa:Action>
    <wsa:MessageID>1</wsa:MessageID>
    <wsa:ReplyTo>
        <wsa:Address>http://www.w3.org/2005/08/addressing/anonymous</wsa:Address>
    </wsa:ReplyTo>
    <wsa:To></wsa:To>
</soap:Header>
<soap:Body>
    <ser:dataExport>
        <ser:args0>10.99.58.23</ser:args0>
        <ser:args1>22</ser:args1>
        <ser:args2>Administrator</ser:args2>
        <ser:args3>password</ser:args3>
        <ser:args4>/home/ftp/files</ser:args4>
    </ser:dataExport>
</soap:Body>
</soap:Envelope>
```

### dataExport Response Parameters

Return element children:

This example shows that an error occurred.

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:a0541e26-939a-490b-a3eb-c43ff752d2e0 </wsa:MessageID> <wsa:Action> urn:dataExportResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:dataExportResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax2105= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax2106= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax2105:DataExportResponse" > <ax2105:remoteMessages xsi:type= "ax2105:RemoteMessage" > <ax2106:error> true </ax2106:error> <ax2106:info> false </ax2106:info> <ax2106:messageKey> internal.request.denied.lock </ax2106:messageKey> <ax2106:messageType> internal.message.error </ax2106:messageType> <ax2106:warning> false </ax2106:warning> <ax2105:messageParams> platform.api.network.address </ax2105:messageParams> <ax2105:messageParams> 27543@rwerer </ax2105:messageParams> <ax2105:messageParams> CreateUffDbImportExportThread-211 </ax2105:messageParams> </ax2105:remoteMessages> <ax2105:result> internal.request.failed </ax2105:result> <ax2105:dataExportResult> error.undetermined.result </ax2105:dataExportResult> </ns:return> </ns:dataExportResponse> </soapenv:Body> </soapenv:Envelope>
```

# DataExportStatusService

## dataExportStatus

The dataExportStatus method shows the status of a request made by the dataExport method.

### dataExportStatus Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:dataExportStatus </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <dataExportStatus xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### dataExportStatus Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:0a144548-81c9-42f0-a302-19c7c37a09e6 </wsa:MessageID> <wsa:Action> urn:dataExportStatusResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:dataExportStatusResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax2109= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax2110= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax2109:DataExportStatusResponse" > <ax2109:result> internal.request.complete </ax2109:result> <ax2109:dataExportStatus> data.export.status.none </ax2109:dataExportStatus> </ns:return> </ns:dataExportStatusResponse> </soapenv:Body> </soapenv:Envelope>
```

# DeploymentModeService

## getDeploymentMode

The getDeploymentMode method returns the deployment mode which reflects the licensing model of the
                product. The deployment mode returned will be either Enterprise , HCS (Hosted Collaboration Service), or HCS-LE (Hosted Collaboration Service - Large Enterprise). Note: Unified Communications Manager release 14(1)SU1 and 12.5(1)SU7 does not support HCS-LE Deployment mode

### getDeploymentMode Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:getDeploymentMode </wsa:Action> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:MessageID> uuid:26634481-3273-4a70-b537-ab4b874e4d6b </wsa:MessageID> </soapenv:Header> <soapenv:Body /> </soapenv:Envelope>
```

None.

### getDeploymentMode Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:getDeploymentModeResponse </wsa:Action> <wsa:RelatesTo> uuid:26634481-3273-4a70-b537-ab4b874e4d6b </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getDeploymentModeResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax273= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax274= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax273:DeploymentModeResponse" > <ax273:result> internal.request.complete </ax273:result> <ax273:deploymentMode> Enterprise </ax273:deploymentMode> </ns:return> </ns:getDeploymentModeResponse> </soapenv:Body> </soapenv:Envelope>
```

- Enterprise - The server is used as part of a standard enterprise
                                deployment.

- HCS - The server is hosted by a service provider using the Hosted
                                Collaboration Solution (HCS) end-to-end system.

- HCS-LE - The server is hosted by a service provider using the Hosted
                                Collaboration Solution (HCS) end-to-end system with centralized management of services
                                and licensing to multiple business units.

## setDeploymentMode

The setDeploymentMode method allows you to set the deployment mode which reflects the licensing model of
                the product. The deployment mode can be set to either Enterprise , HCS (Hosted Collaboration Service), or HCS-LE (Hosted Collaboration Service - Large Enterprise). Once the deployment mode is set, it will be verified
                against the license that is in use. Note: Unified Communications Manager release 14(1)SU1 and 12.5(1)SU7 does not support HCS-LE Deployment mode

### setDeploymentMode Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soap:Envelope xmlns:soap= "http://www.w3.org/2003/05/soap-envelope" xmlns:ser= "http://services.api.platform.vos.cisco.com" > <soap:Header /> <soap:Body> <ser:setDeploymentMode> <ser:args0> Enterprise </ser:args0> </ser:setDeploymentMode> </soap:Body> </soap:Envelope>
```

- Enterprise - The server is used as part of a standard enterprise
                                deployment.

- HCS - The server is hosted by a service provider using the Hosted
                                Collaboration Solution (HCS) end-to-end system.

- HCS-LE - The server is hosted by a service provider using the Hosted
                                Collaboration Solution (HCS) end-to-end system with centralized management of services
                                and licensing to multiple business units.

### setDeploymentMode Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://www.w3.org/2003/05/soap-envelope" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:setDeploymentModeResponse </wsa:Action> <wsa:RelatesTo> uuid:d864e7c5-c517-48f2-8957-b26e18806cbd </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:setDeploymentModeResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax277= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax278= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax277:DeploymentModeResponse" > <ax277:result> internal.request.complete </ax277:result> <ax277:deploymentMode xsi:nil= "true" /> </ns:return> </ns:setDeploymentModeResponse> </soapenv:Body> </soapenv:Envelope>
```

# HardwareInformationService

## getHardwareInformation

The getHardwareInformation method returns detailed hardware information, including everything from the HardwareModelService , as well as CPU/Memory information.

### getHardwareInformation Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getHardwareInformation </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <getHardwareInformation xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### getHardwareInformation Response Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:c0afa34a-410a-4788-852b-d28850abfb2b </wsa:MessageID> <wsa:Action> urn:getHardwareInformationResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getHardwareInformationResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax293= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax294= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax293:HardwareInformationResponse" > <ax293:result> internal.request.complete </ax293:result> <ax293:hardwareInformation xsi:type= "ax293:HardwareInformation" > <ax293:diskCount> 1 </ax293:diskCount> <ax293:diskInformation> <ax293:number> 1 </ax293:number> <ax293:size> 80 </ax293:size> <ax293:total> 1 </ax293:total> </ax293:diskInformation> <ax293:hasMotorizedDriveTray> false </ax293:hasMotorizedDriveTray> <ax293:isServerHeadless> false </ax293:isServerHeadless> <ax293:memory> 4096 </ax293:memory> <ax293:memoryAvailable> 120800 </ax293:memoryAvailable> <ax293:memoryUsed> 3804920 </ax293:memoryUsed> <ax293:model> VMware </ax293:model> <ax293:objectId> 1.3.6.1.4.1.9.1.1348 </ax293:objectId> <ax293:oemModel /> <ax293:opticalDrives> <ax293:driveTray> opticaldrive.drivetray.nonmotorized </ax293:driveTray> </ax293:opticalDrives> <ax293:partitions> <ax293:available> 1805760 </ax293:available> <ax293:name> / </ax293:name> <ax293:total> 14643056 </ax293:total> <ax293:unrestricted> partition.unrestricted.false </ax293:unrestricted> <ax293:used> 12688532 </ax293:used> </ax293:partitions> <ax293:partitions> <ax293:available> 13731912 </ax293:available> <ax293:name> /partB </ax293:name> <ax293:total> 14643120 </ax293:total> <ax293:unrestricted> partition.unrestricted.false </ax293:unrestricted> <ax293:used> 167376 </ax293:used> </ax293:partitions> <ax293:partitions> <ax293:available> 33281580 </ax293:available> <ax293:name> /common </ax293:name> <ax293:total> 50989088 </ax293:total> <ax293:unrestricted> partition.unrestricted.notsupported </ax293:unrestricted> <ax293:used> 15117332 </ax293:used> </ax293:partitions> <ax293:processorCount> 2 </ax293:processorCount> <ax293:processorSpeed> 2400 </ax293:processorSpeed> <ax293:processorType> Intel(R) Xeon(R) CPU E7- 2870 @ 2.40GHz </ax293:processorType> <ax293:raidStatus> No RAID information is available ----------------------------------------------------------------------- Physical device information ----------------------------------------------------------------------- Number of Disks : 1 Hard Disk #1 Size (in GB) : 80 </ax293:raidStatus> <ax293:serialNumber> VMware-42 09 cb 44 ba 75 bc a1-35 6b 51 bb 9e 9a dd 02 </ax293:serialNumber> <ax293:supportedHardware> true </ax293:supportedHardware> <ax293:virtualMachine> true </ax293:virtualMachine> </ax293:hardwareInformation> </ns:return> </ns:getHardwareInformationResponse> </soapenv:Body> </soapenv:Envelope>
```

- diskCount - The number of disks.

- number - Number of disks.

- size - Size in gigabytes.

- total - Total number of disks.

- hasMotorizedDriveTray - Does the drive have a motorized drive tray?

- isServerHeadless - Is the server headless (no monitor).

- memory - Memory installed.

- memoryAvailable - How much of that memory is available.

- memoryUsed - How much of that memory is in use.

- model - The model of the hardware (or virtual machine).

- objectId - The object ID.

- oemModel - The OEM model, if available.

- driveTray - Is the optical drive tray motorized?

- 0 - First partition.

- available - Available space.

- name - The name or mount point of the partition.

- total - Total space on the partition.

- unrestricted - Whether or not the partition is
                                            unrestricted.

- used - How much space on the partition is used.

- 1 - Second partition.

- available - Available space.

- name - The name or mount point of the partition.

- total - Total space on the partition.

- unrestricted - Whether or not the partition is unrestricted.

- used - How much space on the partition is used.

- 2 - Third partition.

- available - Available space.

- name - The name or mount point of the partition.

- total - Total space on the partition.

- unrestricted - Whether or not the partition is unrestricted.

- used - How much space on the partition is used.

- processorCount

- processorSpeed

- processorType

- raidStatus - Information about RAID if available.

- serialNumber - Serial number of the machine or virtual machine.

- true if hardware is supported

- false if not

- true if this is a virtual machine

- false if not

# HardwareModelService

## getHardwareModel

The getHardwareModel method returns hardware information such as model and serial number.

### getHardwareModel Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getHardwareModel </wsa:Action> <wsa:MessageID> uuid:09b18f4c-e212-42dd-be44-c31a9ef0b123 </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/HardwareModelService.HardwareModelServiceHttpSoap11Endpoint </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <getHardwareModel xmlns= "server_url" /> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

None.

### getHardwareModel Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:4F8DCF8A8A3428F84D1297118157136 </wsa:MessageID> <wsa:Action> urn:getHardwareModelResponse </wsa:Action> <wsa:RelatesTo> uuid:7a3e94dc-bcae-4e0f-9cde-950c9dcc9e5b </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getHardwareModelResponse xmlns:ns= "http://server_url" > <ns:return xmlns:ax221= "server_url/xsd" xmlns:ax222= "http://server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax221:HardwareModelResponse" > <ax221:result> internal.request.complete </ax221:result> <ax221:hardwareModel xsi:type= "ax221:HardwareModel" > <ax221:model> VMware </ax221:model> <ax221:objectId> 1.3.6.1.4.1.9.1.1348 </ax221:objectId> <ax221:oemModel /> <ax221:serialNumber> VMware-42 2e 9d 42 65 80 ac a4-49 39 ca f9 82 de b8 a5 </ax221:serialNumber> <ax221:supportedHardware> true </ax221:supportedHardware> <ax221:virtualMachine> true </ax221:virtualMachine> </ax221:hardwareModel> </ns:return> </ns:getHardwareModelResponse> </soapenv:Body> </soapenv:Envelope>
```

- model - Model name of the hardware

- objectId - Numerical ID for the model

- oemModel - OEM name of the model, if it exists

- serialNumber - Serial number

- true if hardware is supported

- false if not

- true if hardware is actually a virtual machine

- false if not

# MaintenanceService

## scheduleBackup

The scheduleBackup method updates an already scheduled DRS backup which is to be run some time in the
                future. In general, there should be a default scheduled backup named all-maint-activities. This method
                provides a way to override the default schedule by passing the schedule name and a time to run the
                backup.

### scheduleBackup Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soap:Envelope xmlns:soap= "http://www.w3.org/2003/05/soap-envelope" xmlns:ser= "server_url" > <soap:Header /> <soap:Body> <ser:scheduleBackup> <ser:args0> all-maint-activities </ser:args0> <ser:args1> 2012-12-28T15:50:00.000-05:00 </ser:args1> <ser:args2> true </ser:args2> </ser:scheduleBackup> </soap:Body> </soap:Envelope>
```

- true enables scheduled backup

- false disables scheduled backup

### scheduleBackup Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://www.w3.org/2003/05/soap-envelope" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:scheduleBackupResponse </wsa:Action> <wsa:RelatesTo> uuid:cd65cd4f-8589-4126-ad88-833a71979fda </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:scheduleBackupResponse xmlns:ns= "server_url" > <ns:return xmlns:ax213= "server_url/xsd" xmlns:ax214= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax213:MaintenanceResponse" > <ax213:remoteMessages xsi:nil= "true" /> <ax213:result> internal.request.complete </ax213:result> <ax213:backupProgressResult xsi:nil= "true" /> <ax213:startBackupResult xsi:nil= "true" /> <ax213:updateScheduleResult> Update successful </ax213:updateScheduleResult> </ns:return> </ns:scheduleBackupResponse> </soapenv:Body> </soapenv:Envelope>
```

## startBackup

The startBackup method starts a previously scheduled backup immediately. It requires the scheduleID of
                the previously scheduled backup as an input.

### startBackup Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soap:Envelope xmlns:soap= "http://www.w3.org/2003/05/soap-envelope" xmlns:ser= "server_url" > <soap:Header /> <soap:Body> <ser:startBackup> <ser:args0> test </ser:args0> </ser:startBackup> </soap:Body> </soap:Envelope>
```

### startBackup Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://www.w3.org/2003/05/soap-envelope" > <soapenv:Body> <ns:startBackupResponse xmlns:ns= "server_url" > <ns:return xmlns:ax213= "server_url/xsd" xmlns:ax214= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax213:MaintenanceResponse" > <ax213:remoteMessages xsi:nil= "true" /> <ax213:result> internal.request.complete </ax213:result> <ax213:backupProgressResult xsi:nil= "true" /> <ax213:startBackupResult xsi:nil= "true" /> <ax213:updateScheduleResult> Update successful </ax213:updateScheduleResult> </ns:return> </ns:startBackupResponse> </soapenv:Body> </soapenv:Envelope>
```

## getBackupProgress

The getBackupProgress method retrieves the progress of the current backup.

### getBackupProgress Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soap:Envelope xmlns:soap= "http://www.w3.org/2003/05/soap-envelope" xmlns:ser= "server_url" > <soap:Header /> <soap:Body> <ser:getBackupProgress xmlns:ns= "server_url" /> </soap:Body> </soap:Envelope>
```

None.

### getBackupProgress Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://www.w3.org/2003/05/soap-envelope" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:getBackupProgressResponse </wsa:Action> <wsa:RelatesTo> uuid:bbe33389-675c-44ff-b7ba-43e85244fb8f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getBackupProgressResponse xmlns:ns= "server_url" > <ns:return xmlns:ax213= "server_url/xsd" xmlns:ax214= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax213:MaintenanceResponse" > <ax213:remoteMessages xsi:nil= "true" /> <ax213:result> internal.request.complete </ax213:result> <ax213:backupProgressResult> Status: Backup operation in progress for server [CSEVDIR79], please wait... Tar Filename: 2012-01-17-10-11-23.tar Storage Location: NETWORK Operation: BACKUP Percentage Complete: 91 UCM CSEVDIR79 PLATFORM SUCCESS Tue Jan 17 10:11:24 IST 2012 activelog/platform/drf/log/2012-01-17-10-11-23_b_csevdir79_ucm_platform.log UCM CSEVDIR79 CLM SUCCESS Tue Jan 17 10:11:29 IST 2012 activelog/platform/drf/log/2012-01-17-10-11-23_b_csevdir79_ucm_clm.log UCM CSEVDIR79 CDPAGT SUCCESS Tue Jan 17 10:11:29 IST 2012 activelog/platform/drf/log/2012-01-17-10-11-23_b_csevdir79_ucm_cdpagt.log UCM CSEVDIR79 SYSLOGAGT SUCCESS Tue Jan 17 10:11:29 IST 2012 activelog/platform/drf/log/2012-01-17-10-11-23_b_csevdir79_ucm_syslogagt.log UCM CSEVDIR79 TCT SUCCESS Tue Jan 17 10:11:30 IST 2012 activelog/platform/drf/log/2012-01-17-10-11-23_b_csevdir79_ucm_tct.log UCM CSEVDIR79 CCMDB SUCCESS Tue Jan 17 10:11:30 IST 2012 activelog/platform/drf/log/2012-01-17-10-11-23_b_csevdir79_ucm_ccmdb.log UCM CSEVDIR79 CCMPREFS SUCCESS Tue Jan 17 10:11:50 IST 2012 activelog/platform/drf/log/2012-01-17-10-11-23_b_csevdir79_ucm_ccmprefs.log UCM CSEVDIR79 ANN SUCCESS Tue Jan 17 10:11:52 IST 2012 activelog/platform/drf/log/2012-01-17-10-11-23_b_csevdir79_ucm_ann.log UCM CSEVDIR79 CEF SUCCESS Tue Jan 17 10:11:52 IST 2012 activelog/platform/drf/log/2012-01-17-10-11-23_b_csevdir79_ucm_cef.log UCM CSEVDIR79 BAT SUCCESS Tue Jan 17 10:11:53 IST 2012 activelog/platform/drf/log/2012-01-17-10-11-23_b_csevdir79_ucm_bat.log UCM CSEVDIR79 MOH SUCCESS Tue Jan 17 10:11:54 IST 2012 activelog/platform/drf/log/2012-01-17-10-11-23_b_csevdir79_ucm_moh.log UCM CSEVDIR79 TFTP Active Tue Jan 17 10:11:58 IST 2012 </ax213:backupProgressResult> <ax213:startBackupResult xsi:nil= "true" /> <ax213:updateScheduleResult xsi:nil= "true" /> </ns:return> </ns:getBackupProgressResponse> </soapenv:Body> </soapenv:Envelope>
```

# NetworkService

## checkNetworkChangeStatus

Use the checkNetworkChangeStatus method to determine when the NetworkService setXXX services have
                completed. Calling this service will set the returned NetworkResponse.networkChangeSuccessful flag appropriately.

### checkNetworkChangeStatus Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:checkNetworkChangeStatus </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <checkNetworkChangeStatus xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### checkNetworkChangeStatus Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:9f02e36b-5e61-4fd1-8542-e27f36f4c3d9 </wsa:MessageID> <wsa:Action> urn:checkNetworkChangeStatusResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:checkNetworkChangeStatusResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax285= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax286= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax285:NetworkResponse" > <ax285:remoteMessages xsi:nil= "true" /> <ax285:result> internal.request.complete </ax285:result> <ax285:DHCPEnabled> false </ax285:DHCPEnabled> <ax285:GW /> <ax285:IP /> <ax285:IPMask /> <ax285:networkChangeStatus /> </ns:return> </ns:checkNetworkChangeStatusResponse> </soapenv:Body> </soapenv:Envelope>
```

## setHostname

This method sets the hostname to a different value.

Use NetworkService checkNetworkChangeStatus to check the status
                of your change.

It is highly recommended that you call NetworkDiagnosticService
                checkNetworkStatus and isClusterReplicationOK along with
                checking the node status returned by getClusterStatus . It should be set
                to cluster.node.status.online before attempting changes to the network settings.

### setHostname Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser= "http://services.api.platform.vos.cisco.com" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:setIpAddress </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <setIpAddress xmlns= "http://services.api.platform.vos.cisco.com" > <ser:args0> infyvoscm28-lnx.cisco.com. </ser:args0> </setIpAddress> </soapenv:Body> </soapenv:Envelope>
```

### setHostname Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:c611810e-49a3-4232-bc8a-7e92ca81dc37 </wsa:MessageID> <wsa:Action> urn:setHostnameResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:setHostnameResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax285= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax286= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax285:NetworkResponse" > <ax285:remoteMessages xsi:type= "ax285:RemoteMessage" > <ax286:error> true </ax286:error> <ax286:info> false </ax286:info> <ax286:messageKey> internal.request.denied.lock </ax286:messageKey> <ax286:messageType> internal.message.error </ax286:messageType> <ax286:warning> false </ax286:warning> <ax285:messageParams> platform.api.network.address </ax285:messageParams> <ax285:messageParams> 27543@rwerer </ax285:messageParams> <ax285:messageParams> CreateUffDbImportExportThread-211 </ax285:messageParams> </ax285:remoteMessages> <ax285:result> internal.request.failed </ax285:result> <ax285:DHCPEnabled> false </ax285:DHCPEnabled> <ax285:GW></ax285:GW> <ax285:IP></ax285:IP> <ax285:IPMask></ax285:IPMask> <ax285:networkChangeStatus></ax285:networkChangeStatus> </ns:return> </ns:setHostnameResponse> </soapenv:Body> </soapenv:Envelope>
```

This example returns an error internal.request.denied.lock , with other details in
                remoteMessages.

## setIpAddress

This method sets the IP address to a different value.

Use NetworkService checkNetworkChangeStatus to check the status
                of your change.

It is highly recommended that you call NetworkDiagnosticService
                checkNetworkStatus and isClusterReplicationOK along with
                checking the node status returned by getClusterStatus . It should be set
                to cluster.node.status.online before attempting changes to the network settings.

### setIpAddress Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser= "http://services.api.platform.vos.cisco.com" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:setIpAddress </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <setIpAddress xmlns= "http://services.api.platform.vos.cisco.com" > <ser:args0> 10.106.3.82 </ser:args0> </setIpAddress> </soapenv:Body> </soapenv:Envelope>
```

### setIpAddress Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:48fab7bd-dcd0-4e57-85ab-f108526d4d53 </wsa:MessageID> <wsa:Action> urn:setIpAddressResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:setIpAddressResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax285= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax286= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax285:NetworkResponse" > <ax285:remoteMessages xsi:type= "ax285:RemoteMessage" > <ax286:error> true </ax286:error> <ax286:info> false </ax286:info> <ax286:messageKey> internal.request.denied.lock </ax286:messageKey> <ax286:messageType> internal.message.error </ax286:messageType> <ax286:warning> false </ax286:warning> <ax285:messageParams> platform.api.network.address </ax285:messageParams> <ax285:messageParams> 27543@rwerer </ax285:messageParams> <ax285:messageParams> CreateUffDbImportExportThread-211 </ax285:messageParams> </ax285:remoteMessages> <ax285:result> internal.request.failed </ax285:result> <ax285:DHCPEnabled> false </ax285:DHCPEnabled> <ax285:GW></ax285:GW> <ax285:IP></ax285:IP> <ax285:IPMask></ax285:IPMask> <ax285:networkChangeStatus></ax285:networkChangeStatus> </ns:return> </ns:setIpAddressResponse> </soapenv:Body> </soapenv:Envelope>
```

This example returns an error internal.request.denied.lock , with other details in
                remoteMessages.

## setNetworkInfo

This method sets the hostname, IP address, IP address mask, and default gateway to different values.

Use NetworkService checkNetworkChangeStatus to check the status
                of your change.

It is highly recommended that you call NetworkDiagnosticService
                checkNetworkStatus and isClusterReplicationOK along with
                checking the node status returned by getClusterStatus . It should be set
                to cluster.node.status.online before attempting changes to the network settings.

### setNetworkInfo Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xmlns:ser= "http://services.api.platform.vos.cisco.com" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:setNetworkInfo </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <setNetworkInfo xmlns= "http://services.api.platform.vos.cisco.com" > <ser:args0> 10.106.3.82 </ser:args0> <ser:args1> infyvoscm28-lnx.cisco.com. </ser:args1> </setNetworkInfo ></soapenv:Body> </soapenv:Envelope>
```

### setNetworkInfo Response Parameters

Return element children:

```
<?xml version='1.0' encoding='UTF-8'?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:e03d6a9e-00af-46d0-822b-23e131413770 </wsa:MessageID> <wsa:Action> urn:setNetworkInfoResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:setNetworkInfoResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax285= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xmlns:ax286= "http://api.platform.vos.cisco.com/xsd" xsi:type= "ax285:NetworkResponse" > <ax285:remoteMessages xsi:type= "ax285:RemoteMessage" > <ax286:error> true </ax286:error> <ax286:info> false </ax286:info> <ax286:messageKey> error.validation.invalid </ax286:messageKey> <ax286:messageType> internal.message.error </ax286:messageType> <ax286:warning> false </ax286:warning> <ax285:messageParams> node.host </ax285:messageParams> </ax285:remoteMessages> <ax285:result> internal.request.failed </ax285:result> <ax285:DHCPEnabled> false </ax285:DHCPEnabled> <ax285:GW></ax285:GW> <ax285:IP></ax285:IP> <ax285:IPMask></ax285:IPMask> <ax285:networkChangeStatus></ax285:networkChangeStatus> </ns:return> </ns:setNetworkInfoResponse> </soapenv:Body> </soapenv:Envelope>
```

This example returns an error internal.request.failed , with other details, such as error.validation.invald in remoteMessages.

## getNetworkInfo

The getNetworkInfo method retrieves information for the node (server) in the cluster that was
                contacted.

### getNetworkInfo Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getNetworkInfo </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <getNetworkInfo xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### getNetworkInfo Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:f0953a43-2376-4038-9526-d31c602432d8 </wsa:MessageID> <wsa:Action> urn:getNetworkInfoResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getNetworkInfoResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax285= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax286= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax285:NetworkResponse" > <ax285:result> internal.request.complete </ax285:result> <ax285:DHCPEnabled> false </ax285:DHCPEnabled> <ax285:GW> 10.106.3.1 </ax285:GW> <ax285:IP> 10.106.3.82 </ax285:IP> <ax285:IPMask> 255.255.255.000 </ax285:IPMask> <ax285:networkChangeStatus></ax285:networkChangeStatus> </ns:return> </ns:getNetworkInfoResponse> </soapenv:Body> </soapenv:Envelope>
```

# NetworkDiagnosticService

## checkNetworkStatus

This checkNetworkStatus method will check the network connectivity status of a node.

### checkNetworkStatus Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:checkNetworkStatus </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <checkNetworkStatus xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### checkNetworkStatus Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:6ab33a16-29e6-4d6f-8e9f-bce39cab66b3 </wsa:MessageID> <wsa:Action> urn:checkNetworkStatusResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:checkNetworkStatusResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax289= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax290= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax289:NetworkDiagnosticResponse" > <ax289:result> internal.request.complete </ax289:result> <ax289:status> true </ax289:status> </ns:return> </ns:checkNetworkStatusResponse> </soapenv:Body> </soapenv:Envelope>
```

- true if ok

- false if not

# Options Service

## getActiveOptions

The getActiveOptions method returns the options installed on the active partition.

### getActiveOptions Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:getActiveOptions </wsa:Action> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:MessageID> uuid:50e3c2ac-fc4e-45ab-9f98-58907619649b </wsa:MessageID> </soapenv:Header> <soapenv:Body/> </soapenv:Envelope>
```

None.

### getActiveOptions Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:4F8DCF8A8A3428F84D1297118397075 </wsa:MessageID> <wsa:Action> urn:getActiveOptionsResponse </wsa:Action> <wsa:RelatesTo> uuid:6a81599c-5813-4465-a777-c6b83c69ad11 </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getActiveOptionsResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax210= "http://api.platform.vos.cisco.com/xsd" xmlns:ax29= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax29:OptionsResponse" > <ax29:remoteMessages xsi:nil= "true" /> <ax29:result> internal.request.complete </ax29:result> <ax29:options xsi:nil= "true" /> </ns:return> </ns:getActiveOptionsResponse> </soapenv:Body> </soapenv:Envelope>
```

## getInactiveOptions

The getInactiveOptions method returns options installed on the inactive partition.

### getInactiveOptions Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:getInactiveOptions </wsa:Action> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:MessageID> uuid:af4f0eb9-44bb-4fb9-8f8d-fa8001e7dab3 </wsa:MessageID> </soapenv:Header> <soapenv:Body /> </soapenv:Envelope>
```

None.

### getInactiveOptions Response Parameters

Return element children:

This result shows there are no options installed on the inactive partition.

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:getInactiveOptionsResponse </wsa:Action> <wsa:RelatesTo> uuid:af4f0eb9-44bb-4fb9-8f8d-fa8001e7dab3 </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getInactiveOptionsResponse xmlns:ns= "server_url.com" > <ns:return xmlns:ax210= "server_url/xsd" xmlns:ax29= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax29:OptionsResponse" > <ax29:remoteMessages xsi:nil= "true" /> <ax29:result> internal.request.complete </ax29:result> <ax29:options xsi:nil= "true" /> </ns:return> </ns:getInactiveOptionsResponse> </soapenv:Body> </soapenv:Envelope>
```

# PlatformConfigExportService

## platformConfigExport

The PlatformConfigExport method begins an export of the node’s platformConfig.xml file to a remote
                FTP server.

### platformConfigExport Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser= "http://services.api.platform.vos.cisco.com" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:platformConfigExport </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To /> </soapenv:Header> <soapenv:Body> <platformConfigExport xmlns= "http://services.api.platform.vos.cisco.com" > <ser:args0> infyvoscm28-lnx.cisco.com. </ser:args0> <ser:args1> 22 </ser:args1> <ser:args2> root </ser:args2> <ser:args3> cisco123 </ser:args3> <ser:args4> /home/rvurimi/ </ser:args4> </platformConfigExport> </soapenv:Body> </soapenv:Envelope>
```

### platformConfigExport Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:df1b570c-62ee-4449-a132-f62963beb54a </wsa:MessageID> <wsa:Action> urn:platformConfigExportResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:platformConfigExportResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax297= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax298= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax297:PlatformConfigExportResponse" > <ax297:result> internal.request.complete </ax297:result> <ax297:platformConfigExportStatus> platform.config.export.failed </ax297:platformConfigExportStatus> </ns:return> </ns:platformConfigExportResponse> </soapenv:Body> </soapenv:Envelope>
```

# PrepareRemoteUpgradeService

## prepareRemoteUpgrade

The prepareRemoteUpgrade method downloads and prepares an upgrade or Cisco Option Package (COP) file for
                installation. This call should always be made asynchronously.

### prepareRemoteUpgrade Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:prepareRemoteUpgrade </wsa:Action> <wsa:MessageID> uuid:88042ed4-0c17-4aba-acfe-f6c68c1c6f0c </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/PrepareRemoteUpgradeService.PrepareRemoteUpgradeServiceHttpSoap11Endpoint </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <prepareRemoteUpgrade xmlns= "http://services.api.platform.vos.cisco.com" > <args0> <ns1:errorMessages xmlns:ns1= "http://server_url/xsd" xsi:nil= "true" /> <ns2:infoMessages xmlns:ns2= "http://server_url/xsd" xsi:nil= "true" /> <ns3:status xmlns:ns3= "http://server_url/xsd" xsi:nil= "true" /> <ns4:validationMessages xmlns:ns4= "http://server_url/xsd" xsi:nil= "true" /> <ns5:warningMessages xmlns:ns5= "http://server_url/xsd" xsi:nil= "true" /> <ns6:completePath xmlns:ns6= "http://server_url/xsd" xsi:nil= "true" /> <ns7:name xmlns:ns7= "http://server_url/xsd" > UCSInstall_UCOS_8.6.0.98000-9015.iso </ns7:name> <ns8:path xmlns:ns8= "http://server_url/xsd" > /ws/jschmaus-rcd/jschmaus-cc_mainline-cct-ccm/iso </ns8:path> <ns9:checksum xmlns:ns9= "http://server_url/xsd" xsi:nil= "true" /> <ns10:essuTimestamp xmlns:ns10= "http://server_url/xsd" xsi:nil= "true" /> <ns11:internalUpgradeType xmlns:ns11= "http://server_url/xsd" xsi:nil= "true" /> <ns12:password xmlns:ns12= "server_url/xsd" > ftpuser </ns12:password> <ns13:postValidatedCompletePath xmlns:ns13= "http://server_url/xsd" xsi:nil= "true" /> <ns14:postValidatedFilename xmlns:ns14= "http://server_url/xsd" xsi:nil= "true" /> <ns15:rejectCode xmlns:ns15= "http://server_url/xs" xsi:nil= "true" /> <ns16:server xmlns:ns16= "http://server_url/xsd" > bcodev1 </ns16:server> <ns17:systemUpgradeLocation xmlns:ns17= "http://=server_url/xsd" xsi:nil= "true" /> <ns18:upgradeLocation xmlns:ns18= "http//server_url/xsd" > upgradefile.location.remote.sftp </ns18:upgradeLocation> <ns19:upgradeType xmlns:ns19= "http?://server_url/xsd" > patch </ns19:upgradeType> <ns20:user xmlns:ns20= "http://server_url/xsd" > ftpuser </ns20:user> <ns21:version xmlns:ns21= "http://server_url/xsd" xsi:nil= "true" /> </args0> <args1> pm238 </args1> <args2> false </args2> </prepareRemoteUpgrade> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

- name - The name of the upgrade file

- path - The path/directory containing the upgrade file

- password - The S/FTP file server password

- server - The S/FTP file server hostname or IP address

- upgradefile.location.remote.sftp - indicating the upgrade is
                                        located on an SFTP server

- upgradefile.location.remote.ftp - indicating the upgrade is
                                        located on a FTP server

- upgradeType - Currently always patch .
                                More types may be supported in the future.

- user - The S/FTP file server user

### prepareRemoteUpgrade Response Parameters

Return element children:

This result shows that the upgrade was canceled.

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:A76367D3A705D7D5591299705914148 </wsa:MessageID> <wsa:Action> urn:prepareRemoteUpgradeResponse </wsa:Action> <wsa:RelatesTo> uuid:19896bfb-dbb4-4f2a-8c84-a34c13b42ac5 </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:prepareRemoteUpgradeResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax241= "server_url/xsd" xmlns:ax243= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax244= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax243:PrepareRemoteUpgradeResponse" > <ax243:remoteMessages xsi:type= "ax243:RemoteMessage" > <ax244:error> true </ax244:error> <ax244:info> false </ax244:info> <ax244:messageKey> error.upgrade.canceled </ax244:messageKey> <ax244:messageType> internal.message.error </ax244:messageType> <ax244:warning> false </ax244:warning> </ax243:remoteMessages> <ax243:result> internal.request.failed </ax243:result> <ax243:upgradeFile xsi:type= "ax243:UpgradeFile" > <ax243:checksum /> <ax243:essuTimestamp /> <ax243:name> UCSInstall_UCOS_8.6.0.98000-9009.iso </ax243:name> <ax243:path> /common/download/ </ax243:path> <ax243:postValidatedFilename> UCSInstall_UCOS_8.6.0.98000-9009.iso </ax243:postValidatedFilename> <ax243:rebootRequired> false </ax243:rebootRequired> <ax243:rejectCode /> <ax243:server /> <ax243:signed> false </ax243:signed> <ax243:unrestrictedVersion> false </ax243:unrestrictedVersion> <ax243:upgradeLocation /> <ax243:upgradeType> upgradefile.type.patch </ax243:upgradeType> <ax243:user /> <ax243:validated> false </ax243:validated> <ax243:version> 8.6.0.98000-9009 </ax243:version> </ax243:upgradeFile> </ns:return> </ns:prepareRemoteUpgradeResponse> </soapenv:Body> </soapenv:Envelope>
```

- name - upgrade or COP file name

- password - the passsword for the server that contains the upgrade file

- path - upgrade file path

- server - the name of the server that provided the upgrade file

- upgradeLocation - url of upgrade serve

- upgradeType - upgradefile.type.patch

- user - user name on upgrade server

# ProductService

## getInstalledProducts

The getInstalledProducts method returns the deployed products.

### getInstalledProducts Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getInstalledProducts </wsa:Action> <wsa:MessageID> uuid:2fe9a853-08b2-4390-9929-317711651d61 </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/ProductService. ProductServiceHttpSoap11Endpoint/ </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <getInstalledProducts xmlns= "server_url" /> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

None.

### getInstalledProducts Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:4F8DCF8A8A3428F84D1297119470696 </wsa:MessageID> <wsa:Action> urn:getInstalledProductsResponse </wsa:Action> <wsa:RelatesTo> uuid:c1e22940-cd4e-4afe-9ef7-dee5fc5e135d </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getInstalledProductsResponse xmlns:ns= "server_url" > <ns:return xmlns:ax267= "server_url/xsd" xmlns:ax268= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax267:ProductResponse" > <ax267:remoteMessages xsi:nil= "true" /> <ax267:result> internal.request.complete </ax267:result> <ax267:installedProducts xsi:type= "ax267:InstalledProduct" > <ax267:displayName> Cisco Unified Communications Manager </ax267:displayName> <ax267:name /> <ax267:version> 8.6.0.96000-9006 </ax267:version> <ax267:adminUrl> ccmadmin/showHome.do </ax267:adminUrl> <ax267:id> CallManager </ax267:id> </ax267:installedProducts> </ns:return> </ns:getInstalledProductsResponse> </soapenv:Body> </soapenv:Envelope>
```

- displayName - The name of the product as displayed

- name - The name of the product if different from the display name.

- version - The product’s version number.

- adminUrl - URL of the product’s admin GUI

- id - the product ID

## getProductName

The getProductName method returns the overall product name.

### getProductName Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:getProductName </wsa:Action> <wsa:ReplyTo> <wsa:Address> http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:MessageID> uuid:5eda82c3-eb40-4b8d-87b4-f7407bb2fb14 </wsa:MessageID> </soapenv:Header> <soapenv:Body /> </soapenv:Envelope>
```

None.

### getProductName Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:getProductNameResponse </wsa:Action> <wsa:RelatesTo> uuid:5eda82c3-eb40-4b8d-87b4-f7407bb2fb14 </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getProductNameResponse xmlns:ns= "server_url" > <ns:return xmlns:ax269= "server_url/xsd" xmlns:ax270= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax269:ProductNameResponse" > <ax269:remoteMessages xsi:nil= "true" /> <ax269:result> internal.request.complete </ax269:result> <ax269:productName> Cisco Unified Communications Manager </ax269:productName> </ns:return> </ns:getProductNameResponse> </soapenv:Body> </soapenv:Envelope>
```

# RestartSystemService

## restartSystem

The restartSystem method reboots the system without switching partitions. This service does not return a
                response when successful, since the reboot occurs before the final response can be returned.

Use RestartSystemStatusService to check the status of the
                reboot.

### restartSystem Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:restartSystem </wsa:Action> <wsa:MessageID> uuid:0b23619d-f88e-43cb-a6f2-e3752827dddd </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/RestartSystemService .RestartSystemServiceHttpSoap11Endpoint/ </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <restartSystem xmlns= "server_url" /> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

None.

### restartSystem Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:131F8296C8AB838D9D1299260560238 </wsa:MessageID> <wsa:Action> urn:restartSystemResponse </wsa:Action> <wsa:RelatesTo> uuid:98335f43-35ea-4a4b-bb6c-1843bf340850 </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:restartSystemResponse xmlns:ns= "server_url" > <ns:return xmlns:ax263= "server_url/xsd" xmlns:ax264= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax263:RestartSystemResponse" > <ax263:remoteMessages xsi:type= "ax263:RemoteMessage" > <ax264:error> true </ax264:error> <ax264:info> false </ax264:info> <ax264:messageKey> error.file.notdeleted </ax264:messageKey> <ax264:messageType> internal.message.error </ax264:messageType> <ax264:warning> false </ax264:warning> <ax263:messageParams> /var/log/install/gui-restart-result.xml </ax263:messageParams> </ax263:remoteMessages> <ax263:result> internal.request.failed </ax263:result> </ns:return> </ns:restartSystemResponse> </soapenv:Body> </soapenv:Envelope>
```

This result shows that /var/log/install/gui-restart-result.xml could not be deleted and the restart
                failed. In this case, review the logs to determine the root cause.

# RestartSystemStatusService

## getRestartSystemStatus

The getRestartSystemStatus method returns the status of the last restartSystem method call.

### getRestartSystemStatus Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getRestartSystemStatus </wsa:Action> <wsa:MessageID> uuid:d31cbc57-639c-4b90-b34c-ee235dede2f1 </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/RestartSystemStatusService. RestartSystemStatusServiceHttpSoap11Endpoint/ </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <getRestartSystemStatus xmlns= "server_url" /> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

None.

### getRestartSystemStatus Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:2E42FE5EA44715D2481297190589523 </wsa:MessageID> <wsa:Action> urn:getRestartSystemStatusResponse </wsa:Action> <wsa:RelatesTo> uuid:b09d02c6-1591-4e4f-a8f0-91b29ef9322d </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getRestartSystemStatusResponse xmlns:ns= "server_url" > <ns:return xmlns:ax267= "server_url/xsd" xmlns:ax268= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax267:RestartSystemStatusResponse" > <ax267:result> internal.request.complete </ax267:result> <ax267:restartSystemStatus> internal.request.processing </ax267:restartSystemStatus> </ns:return> </ns:getRestartSystemStatusResponse> </soapenv:Body> </soapenv:Envelope>
```

This result indicates the restart is still processing which means the system reboot has initiated.

- internal.request.processing - The restart is still in progress

- internal.request.complete - The restart has completed

# SSOService

## getStatus

The getStatus method tells you if Single Sign-On (SSO) is enabled or not.

### getStatus Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getStatus </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <getStatus xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### getStatus Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:d78253b6-ff29-48ab-9870-ef821750458e </wsa:MessageID> <wsa:Action> urn:getStatusResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getStatusResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax21= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax22= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax21:SSOResponse" > <ax21:remoteMessages xsi:nil= "true" /> <ax21:result> internal.request.complete </ax21:result> <ax21:SSOCertificate xsi:nil= "true" /> <ax21:idpMetadataUploadTime> 0 </ax21:idpMetadataUploadTime> <ax21:samlTestSuccess> false </ax21:samlTestSuccess> <ax21:samlTestTime> 0 </ax21:samlTestTime> <ax21:serverMetadataDownloadTime> 0 </ax21:serverMetadataDownloadTime> <ax21:ssoResult> true </ax21:ssoResult> <ax21:ssoResultDescription /> <ax21:status> 0 </ax21:status> <ax21:vanityURLStatus> true </ax21:vanityURLStatus> </ns:return> </ns:getStatusResponse> </soapenv:Body> </soapenv:Envelope>
```

## enableSSO

The enableSSO method allows you to enable or disable SSO.

### enableSSO Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser= "http://services.api.platform.vos.cisco.com" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:enableSSO </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <enableSSO xmlns= "http://services.api.platform.vos.cisco.com" > <ser:args0> false </ser:args0> </enableSSO> </soapenv:Body> </soapenv:Envelope>
```

- true if you want to enable SSO

- false if you want to disable SSO

### enableSSO Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:b959d987-b655-4f1d-8579-6b3ac19b5efd </wsa:MessageID> <wsa:Action> urn:enableSSOResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:enableSSOResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax21= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax22= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax21:SSOResponse" > <ax21:remoteMessages xsi:nil= "true" /> <ax21:result> internal.request.complete </ax21:result> <ax21:SSOCertificate xsi:nil= "true" /> <ax21:idpMetadataUploadTime> 0 </ax21:idpMetadataUploadTime> <ax21:samlTestSuccess> false </ax21:samlTestSuccess> <ax21:samlTestTime> 0 </ax21:samlTestTime> <ax21:serverMetadataDownloadTime> 0 </ax21:serverMetadataDownloadTime> <ax21:ssoResult> false </ax21:ssoResult> <ax21:ssoResultDescription> SSO disable operation failed. SAML SSO is already disabled. </ax21:ssoResultDescription> <ax21:status> 0 </ax21:status> <ax21:vanityURLStatus> false </ax21:vanityURLStatus> </ns:return> </ns:enableSSOResponse> </soapenv:Body> </soapenv:Envelope>
```

## clearTestStatus

The clearTestStatus method clears the test status bit from an SSO test (this test is initiated by another
                API).

### clearTestStatus Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:clearTestStatus </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <clearTestStatus xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### clearTestStatus Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:c9626e0c-bb1b-4f45-962d-c1eb88123be6 </wsa:MessageID> <wsa:Action> urn:clearTestStatusResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:clearTestStatusResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax21= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax22= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax21:SSOResponse" > <ax21:remoteMessages xsi:nil= "true" /> <ax21:result> internal.request.complete </ax21:result> <ax21:SSOCertificate xsi:nil= "true" /> <ax21:idpMetadataUploadTime> 0 </ax21:idpMetadataUploadTime> <ax21:samlTestSuccess> false </ax21:samlTestSuccess> <ax21:samlTestTime> 0 </ax21:samlTestTime> <ax21:serverMetadataDownloadTime> 0 </ax21:serverMetadataDownloadTime> <ax21:ssoResult> true </ax21:ssoResult> <ax21:ssoResultDescription /> <ax21:status> 0 </ax21:status> <ax21:vanityURLStatus> false </ax21:vanityURLStatus> </ns:return> </ns:clearTestStatusResponse> </soapenv:Body> </soapenv:Envelope>
```

## uploadIdPMetadata

Use the uploadIdPMetadata method to upload the XML content of an Identify Provider metadata file.

### uploadIdPMetadata Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser= "http://services.api.platform.vos.cisco.com" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:uploadIdPMetadata </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <uploadIdPMetadata xmlns= "http://services.api.platform.vos.cisco.com" > <ser:args0> &lt; ?xml version="1.0" encoding="UTF-8" standalone="no"? &gt; &lt; EntityDescriptor xmlns="urn:oasis:names:tc:SAML:2.0:metadata" ID="_d1bb3b70-80f5-43f8-add1-998f9939fa73" entityID="http://DS-SSO-ADFS.ds-adfs.sso.com/adfs/services/trust" &gt; &lt; SPSSODescriptor WantAssertionsSigned="true" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol" &gt; &lt; KeyDescriptor use="encryption" &gt; &lt; KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#" &gt; &lt; X509Data &gt; [...] &lt; /EntityDescriptor &gt; </ser:args0> </uploadIdPMetadata> </soapenv:Body> </soapenv:Envelope>
```

### uploadIdPMetadata Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:1a794df4-df77-4e99-af23-a7c6f6480a46 </wsa:MessageID> <wsa:Action> urn:uploadIdPMetadataResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:uploadIdPMetadataResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax21= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax22= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax21:SSOResponse" > <ax21:remoteMessages xsi:nil= "true" /> <ax21:result> internal.request.complete </ax21:result> <ax21:SSOCertificate xsi:nil= "true" /> <ax21:idpMetadataUploadTime> 0 </ax21:idpMetadataUploadTime> <ax21:samlTestSuccess> false </ax21:samlTestSuccess> <ax21:samlTestTime> 0 </ax21:samlTestTime> <ax21:serverMetadataDownloadTime> 0 </ax21:serverMetadataDownloadTime> <ax21:ssoResult> false </ax21:ssoResult> <ax21:ssoResultDescription> Exception in removing un supported tags. </ax21:ssoResultDescription> <ax21:status> 0 </ax21:status> <ax21:vanityURLStatus> false </ax21:vanityURLStatus> </ns:return> </ns:uploadIdPMetadataResponse> </soapenv:Body> </soapenv:Envelope>
```

## downloadIdPMetadata

Use the downloadIdPMetadata method to download an IdP certificate. A SAML metadata file must be generated
                for the specified server. You must then upload this metatdata file to the Identity Provider (IdP)
                server.

### downloadIdPMetadata Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:downloadIdPMetadata </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <downloadIdPMetadata xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### downloadIdPMetadata Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:0fcd5238-ee03-407c-be3e-a93ae2603dc1 </wsa:MessageID> <wsa:Action> urn:downloadIdPMetadataResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:downloadIdPMetadataResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax21= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax22= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax21:SSOResponse" > <ax21:remoteMessages xsi:nil= "true" /> <ax21:result> internal.request.complete </ax21:result> <ax21:SSOCertificate xsi:nil= "true" /> <ax21:idpMetadataUploadTime> 0 </ax21:idpMetadataUploadTime> <ax21:samlTestSuccess> false </ax21:samlTestSuccess> <ax21:samlTestTime> 0 </ax21:samlTestTime> <ax21:serverMetadataDownloadTime> 0 </ax21:serverMetadataDownloadTime> <ax21:ssoResult> false </ax21:ssoResult> <ax21:ssoResultDescription> Error in downloading metadata. File not present </ax21:ssoResultDescription> <ax21:status> 0 </ax21:status> <ax21:vanityURLStatus> false </ax21:vanityURLStatus> </ns:return> </ns:downloadIdPMetadataResponse> </soapenv:Body> </soapenv:Envelope>
```

## downloadSPMetadata

Use the downloadSPMetadata method to download SP metadata.

### downloadSPMetadata Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:downloadSPExtendedMetadata </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <downloadSPExtendedMetadata xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### downloadSPMetadata Response Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:08a2c8b4-db45-4dd8-92f2-0d51fe01a5a8 </wsa:MessageID> <wsa:Action> urn:downloadSPMetadataResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:downloadSPMetadataResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax21= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax22= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax21:SSOResponse" > <ax21:remoteMessages xsi:nil= "true" /> <ax21:result> internal.request.complete </ax21:result> <ax21:SSOCertificate> [XML encoded SSO certificate ommitted] </ax21:SSOCertificate> <ax21:idpMetadataUploadTime> 0 </ax21:idpMetadataUploadTime> <ax21:samlTestSuccess> false </ax21:samlTestSuccess> <ax21:samlTestTime> 0 </ax21:samlTestTime> <ax21:serverMetadataDownloadTime> 0 </ax21:serverMetadataDownloadTime> <ax21:ssoResult> true </ax21:ssoResult> <ax21:ssoResultDescription /> <ax21:status> 0 </ax21:status> <ax21:vanityURLStatus> false </ax21:vanityURLStatus> </ns:return> </ns:downloadSPMetadataResponse> </soapenv:Body> </soapenv:Envelope>
```

- 0 - There can be multiple KeyDescriptor sections. This is the first in
                                the example.

- 1 - There can be multiple KeyDescriptor sections. This is the second in
                                the example.

## downloadSPExtendedMetadata

Use the downloadSPExtendedMetadata method to download SP extended metadata.

### downloadSPExtendedMetadata Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:downloadSPExtendedMetadata </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <downloadSPExtendedMetadata xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### downloadSPExtendedMetadata Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:4890b50f-9ad9-43cd-9058-3132f3a35cd0 </wsa:MessageID> <wsa:Action> urn:downloadSPExtendedMetadataResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:downloadSPExtendedMetadataResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax21= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax22= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax21:SSOResponse" > <ax21:remoteMessages xsi:nil= "true" /> <ax21:result> internal.request.complete </ax21:result> <ax21:SSOCertificate> <EntityConfig xmlns= "urn:sun:fm:SAML:2.0:entityconfig" xmlns:fm= "urn:sun:fm:SAML:2.0:entityconfig" entityID= "rwerer" hosted= "1" > <SPSSOConfig metaAlias= "/sp1" > <Attribute name= "transientUser" > <Value> anonymous </Value> </Attribute> <Attribute name= "signingCertAlias" > <Value> tomcat </Value> </Attribute> <Attribute name= "encryptionCertAlias" > <Value> tomcat </Value> </Attribute> <Attribute name= "fedletAdapter" > <Value> com.sun.identity.saml2.plugins.DefaultFedletAdapter </Value> </Attribute> <Attribute name= "spAccountMapper" > <Value> com.sun.identity.saml2.plugins.DefaultLibrarySPAccountMapper </Value> </Attribute> <Attribute name= "useNameIDAsSPUserID" > <Value> false </Value> </Attribute> <Attribute name= "spAttributeMapper" > <Value> com.sun.identity.saml2.plugins.DefaultSPAttributeMapper </Value> </Attribute> <Attribute name= "attributeMap" > <Value> *=* </Value> </Attribute> <Attribute name= "assertionTimeSkew" > <Value> 300 </Value> </Attribute> <Attribute name= "cotlist" > <Value> ssospcot </Value> </Attribute> </SPSSOConfig> </EntityConfig> </ax21:SSOCertificate> <ax21:idpMetadataUploadTime> 0 </ax21:idpMetadataUploadTime> <ax21:samlTestSuccess> false </ax21:samlTestSuccess> <ax21:samlTestTime> 0 </ax21:samlTestTime> <ax21:serverMetadataDownloadTime> 0 </ax21:serverMetadataDownloadTime> <ax21:ssoResult> true </ax21:ssoResult> <ax21:ssoResultDescription /> <ax21:status> 0 </ax21:status> <ax21:vanityURLStatus> false </ax21:vanityURLStatus> </ns:return> </ns:downloadSPExtendedMetadataResponse> </soapenv:Body> </soapenv:Envelope>
```

## isMultiServerCert

The isMultiServerCert method checks whether the certificate used by the SSO SP is a multi-server
                certificate.

### isMultiServerCert Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser= "http://services.api.platform.vos.cisco.com" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header> <wsa:Action xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > urn:isMultiServerCert </wsa:Action> <wsa:MessageID xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" /> </soapenv:Header> <soapenv:Body> <isMultiServerCert xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### isMultiServerCert Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:ef6ed2e8-0df0-48b0-81e4-056ef988c816 </wsa:MessageID> <wsa:Action> urn:isMultiServerCertResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:isMultiServerCertResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax21= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax22= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax21:SSOResponse" > <ax21:remoteMessages xsi:nil= "true" /> <ax21:result> internal.request.complete </ax21:result> <ax21:SAMLMetaData xsi:nil= "true" /> <ax21:SSOCertificate xsi:nil= "true" /> <ax21:hostName xsi:nil= "true" /> <ax21:idpMetadataUploadTime> 0 </ax21:idpMetadataUploadTime> <ax21:multiServerCert> true </ax21:multiServerCert> <ax21:samlTestSuccess> false </ax21:samlTestSuccess> <ax21:samlTestTime> 0 </ax21:samlTestTime> <ax21:serialNumber> 44C58C8F000000000040 </ax21:serialNumber> <ax21:serverMetadataDownloadTime> 0 </ax21:serverMetadataDownloadTime> <ax21:ssoResult> true </ax21:ssoResult> <ax21:ssoResultDescription /> <ax21:status> 0 </ax21:status> <ax21:vanityURLStatus> false </ax21:vanityURLStatus> </ns:return> </ns:isMultiServerCertResponse> </soapenv:Body> </soapenv:Envelope>
```

## generateClusterWideSPMetadata

The generateClusterWideSPMetadata method generates clusterwide SP metadata XML in the node from where it
                is called.

### generateClusterWideSPMetadata Request
                Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser= "http://services.api.platform.vos.cisco.com" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header> <wsa:Action xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > urn:generateClusterWideSPMetadata </wsa:Action> <wsa:MessageID xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" /> </soapenv:Header> <soapenv:Body> <generateClusterWideSPMetadata xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### generateClusterWideSPMetadata Response
                Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:91c2f262-7aa7-43e0-a326-625bf3e747bb </wsa:MessageID> <wsa:Action> urn:generateClusterWideSPMetadataResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:generateClusterWideSPMetadataResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax21= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax22= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax21:SSOResponse" > <ax21:remoteMessages xsi:nil= "true" /> <ax21:result> internal.request.complete </ax21:result> <ax21:SAMLMetaData> [XML encoded SAML meta data ommitted] </ax21:SAMLMetaData> <ax21:SSOCertificate> [XML encoded SSO certificate data ommitted] </ax21:SSOCertificate> <ax21:hostName xsi:nil= "true" /> <ax21:idpMetadataUploadTime> 0 </ax21:idpMetadataUploadTime> <ax21:multiServerCert> false </ax21:multiServerCert> <ax21:samlTestSuccess> false </ax21:samlTestSuccess> <ax21:samlTestTime> 0 </ax21:samlTestTime> <ax21:serialNumber xsi:nil= "true" /> <ax21:serverMetadataDownloadTime> 0 </ax21:serverMetadataDownloadTime> <ax21:ssoResult> true </ax21:ssoResult> <ax21:ssoResultDescription /> <ax21:status> 0 </ax21:status> <ax21:vanityURLStatus> false </ax21:vanityURLStatus> </ns:return> </ns:generateClusterWideSPMetadataResponse> </soapenv:Body> </soapenv:Envelope>
```

## downloadClusterWideSPMetadata

The downloadClusterWideSPMetadata method downloads the cluster-wide SP metadata.xml.

### downloadClusterWideSPMetadata Request
                Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header> <wsa:Action xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > urn:
downloadClusterWideSPMetadata </wsa:Action> <wsa:MessageID xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" /> </soapenv:Header> <soapenv:Body> <downloadClusterWideSPMetadata xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### downloadClusterWideSPMetadata Response
                Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:dc4e6409-1bbb-4780-897a-6dc9912d678a </wsa:MessageID> <wsa:Action> urn:downloadClusterWideSPMetadataResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:downloadClusterWideSPMetadataResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax21= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax22= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax21:SSOResponse" > <ax21:remoteMessages xsi:nil= "true" /> <ax21:result> internal.request.complete </ax21:result> <ax21:SAMLMetaData> [XML encoded SAML meta data ommitted] </ax21:SAMLMetaData> <ax21:SSOCertificate> [XML encoded SSO certificate data ommitted] </ax21:SSOCertificate> <ax21:hostName xsi:nil= "true" /> <ax21:idpMetadataUploadTime> 0 </ax21:idpMetadataUploadTime> <ax21:multiServerCert> false </ax21:multiServerCert> <ax21:samlTestSuccess> false </ax21:samlTestSuccess> <ax21:samlTestTime> 0 </ax21:samlTestTime> <ax21:serialNumber xsi:nil= "true" /> <ax21:serverMetadataDownloadTime> 0 </ax21:serverMetadataDownloadTime> <ax21:ssoResult> true </ax21:ssoResult> <ax21:ssoResultDescription /> <ax21:status> 0 </ax21:status> <ax21:vanityURLStatus> false </ax21:vanityURLStatus> </ns:return> </ns:downloadClusterWideSPMetadataResponse> </soapenv:Body> </soapenv:Envelope>
```

## uploadClusterWideSPMetadata

The uploadClusterWideSPMetadata method uploads the cluster-wide SP metadata xml to the particular node
                from where it has been called. Customer would have to use this API on every node and upload the same
                metadata on all the nodes for it to be unique.

### uploadClusterWideSPMetadata Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser= "http://services.api.platform.vos.cisco.com" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header> <wsa:Action xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > urn:uploadClusterWideSPMetadata </wsa:Action> <wsa:MessageID xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" /> </soapenv:Header> <soapenv:Body> <uploadClusterWideSPMetadata xmlns= "http://services.api.platform.vos.cisco.com" > <ser:args0> [XML encoded SP meta data ommitted] </ser:args0> </uploadClusterWideSPMetadata> </soapenv:Body> </soapenv:Envelope>
```

### uploadClusterWideSPMetadata Response
                Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:fe739500-26e3-4994-9006-0f59035383c8 </wsa:MessageID> <wsa:Action> urn:uploadClusterWideSPMetadataResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:uploadClusterWideSPMetadataResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax21= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax22= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax21:SSOResponse" > <ax21:remoteMessages xsi:nil= "true" /> <ax21:result> internal.request.complete </ax21:result> <ax21:SAMLMetaData xsi:nil= "true" /> <ax21:SSOCertificate xsi:nil= "true" /> <ax21:hostName xsi:nil= "true" /> <ax21:idpMetadataUploadTime> 0 </ax21:idpMetadataUploadTime> <ax21:multiServerCert> false </ax21:multiServerCert> <ax21:samlTestSuccess> false </ax21:samlTestSuccess> <ax21:samlTestTime> 0 </ax21:samlTestTime> <ax21:serialNumber xsi:nil= "true" /> <ax21:serverMetadataDownloadTime> 0 </ax21:serverMetadataDownloadTime> <ax21:ssoResult> true </ax21:ssoResult> <ax21:ssoResultDescription/> <ax21:status> 0 </ax21:status> <ax21:vanityURLStatus> false </ax21:vanityURLStatus> </ns:return> </ns:uploadClusterWideSPMetadataResponse> </soapenv:Body> </soapenv:Envelope>
```

# StartUpgradeService

## startUpgrade

The startUpgrade method starts the upgrade or COP file installation previously prepared via prepareRemoteUpgrade This method returns a response:

- As soon as the upgrade is complete for normal upgrades, and before booting the new partition if a
                    reboot was requested.

- Before rebooting if a refresh upgrade is being performed.

For refresh upgrades, the upgrade is not complete when the response is received. Refresh upgrades do not
                have platform services running after the first reboot, so Platform Administrative Web Services are
                unavailable. In particular, UpgradeStageService and UpgradeProgressStageService are not available for
                monitoring the upgrade progress after performing a refresh upgrade.

This call should always be made asynchronously.

### startUpgrade Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:startUpgrade </wsa:Action> <wsa:MessageID> uuid:b4d705b2-eb27-4f63-8ca7-1421e5e11535 </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/StartUpgradeService. StartUpgradeServiceHttpSoap11Endpoint </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <startUpgrade xmlns= "server_url" > <args0> pm238 </args0> <args1> false </args1> <args2> false </args2> </startUpgrade> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

### startUpgrade Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:95C57A73325A726E721299707179251 </wsa:MessageID> <wsa:Action> urn:startUpgradeResponse </wsa:Action> <wsa:RelatesTo> uuid:b6bcfda4-e62c-43d6-8f52-3770286b8ccb </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:startUpgradeResponse xmlns:ns= "server_url" > <ns:return xmlns:ax247= "server_url/xsd" xmlns:ax248= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax247:StartUpgradeResponse" > <ax247:remoteMessages xsi:type= "ax247:RemoteMessage" > <ax248:error> true </ax248:error> <ax248:info> false </ax248:info> <ax248:messageKey> error.upgrade.canceled </ax248:messageKey> <ax248:messageType> internal.message.error </ax248:messageType> <ax248:warning> false </ax248:warning> </ax247:remoteMessages> <ax247:result> internal.request.failed </ax247:result> </ns:return> </ns:startUpgradeResponse> </soapenv:Body> </soapenv:Envelope>
```

This result occurs if the upgrade is cancelled.

# SwitchVersionService

## SwitchVersions

The switchVersions method switches the running software version to the upgrade version. It activates and
                boots the inactive partition.

### SwitchVersions Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:switchVersions </wsa:Action> <wsa:MessageID> uuid:b04cfe9e-2f77-4eed-b150-805e3ba6980d </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/SwitchVersionService.SwitchVersionServiceHttpSoap11Endpoint </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <switchVersions xmlns= "server_url" /> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

None.

### SwitchVersions Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:BAFCD8D75A4A7146AE1299252260996 </wsa:MessageID> <wsa:Action> urn:switchVersionsResponse </wsa:Action> <wsa:RelatesTo> uuid:66ab1659-7644-4baa-bf9d-381511f03dc4 </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:switchVersionsResponse xmlns:ns= "server_url" > <ns:return xmlns:ax255= "server_url/xsd" xmlns:ax256= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax255:SwitchVersionResponse" > <ax255:remoteMessages xsi:type= "ax255:RemoteMessage" > <ax256:error> true </ax256:error> <ax256:info> false </ax256:info> <ax256:messageKey> error.version.inactive.notavailable </ax256:messageKey> <ax256:messageType> internal.message.error </ax256:messageType> <ax256:warning> false </ax256:warning> </ax255:remoteMessages> <ax255:result> internal.request.failed </ax255:result> </ns:return> </ns:switchVersionsResponse> </soapenv:Body> </soapenv:Envelope>
```

This result indicates there is no inactive version.

# SwitchVersionStatusService

## getSwitchVersionStatus

The getSwitchVersionStatus method returns the status of the last switchVersions method call. It works exactly like getRestartSystemStatus . This getSwitchVersion service call causes
                the server to reboot, it is possible that the reboot takes place before the server can respond to the
                call, making the response for this call unreliable.

### getSwitchVersionStatus Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getSwitchVersionStatus </wsa:Action> <wsa:MessageID> uuid:48f27b57-628b-48b2-9bb3-5b696149ba85 </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/SwitchVersionStatusService.SwitchVersionStatusServiceHttpSoap11Endpoint </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <getSwitchVersionStatus xmlns= "server_url" /> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

None.

### getSwitchVersionStatus Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:7AE2E8A25ED9B04B3B1299542867309 </wsa:MessageID> <wsa:Action> urn:getSwitchVersionStatusResponse </wsa:Action> <wsa:RelatesTo> uuid:3e4b6b55-dce4-4232-a4e0-70a064b20bf7 </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getSwitchVersionStatusResponse xmlns:ns= "server_url" > <ns:return xmlns:ax259= "server_url/xsd" xmlns:ax260= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax259:SwitchVersionStatusResponse" > <ax259:result> internal.request.complete </ax259:result> <ax259:switchVersionStatus> internal.request.complete </ax259:switchVersionStatus> </ns:return> </ns:getSwitchVersionStatusResponse> </soapenv:Body> </soapenv:Envelope>
```

- internal.request.processing - The switch version is still in progress

- internal.request.complete - The switch version has completed

# UffDbImportExportService

## UffDbImportExport

The uffDbImportExport method imports or exports uff db data files from a node and uploads them a remote
                server.

### UffDbImportExport Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser= "http://services.api.platform.vos.cisco.com" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:uffDbImportExport </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <uffDbImportExport xmlns= "http://services.api.platform.vos.cisco.com" > <ser:args0> infyvoscm28-lnx.cisco.com. </ser:args0> <ser:args1> 22 </ser:args1> <ser:args2> root </ser:args2> <ser:args3> cisco123 </ser:args3> <ser:args4> /home/rvurimi/ </ser:args4> <ser:args5> /home/rvurimi/ </ser:args5> <ser:args6> export </ser:args6> </uffDbImportExport> </soapenv:Body> </soapenv:Envelope>
```

### UffDbImportExport Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:9c1fbf48-3909-4049-987f-3426429a75f6 </wsa:MessageID> <wsa:Action> urn:uffDbImportExportResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:uffDbImportExportResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax2113= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax2114= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax2113:UffDbImportExportResponse" > <ax2113:remoteMessages xsi:type= "ax2113:RemoteMessage" > <ax2114:error> true </ax2114:error> <ax2114:info> false </ax2114:info> <ax2114:messageKey> internal.request.denied.lock </ax2114:messageKey> <ax2114:messageType> internal.message.error </ax2114:messageType> <ax2114:warning> false </ax2114:warning> <ax2113:messageParams> platform.api.network.address </ax2113:messageParams> <ax2113:messageParams> 27543@rwerer </ax2113:messageParams> <ax2113:messageParams> CreateUffDbImportExportThread-211 </ax2113:messageParams> </ax2113:remoteMessages> <ax2113:result> internal.request.failed </ax2113:result> <ax2113:uffDbStatus> error.undetermined.result </ax2113:uffDbStatus> </ns:return> </ns:uffDbImportExportResponse> </soapenv:Body> </soapenv:Envelope>
```

# UpgradeFilterService

## upgradeFilter

The upgradeFilter method returns a list of valid files from the provided list of files. Use this method
                to locate valid files in a particular SFTP or FTP directory. This call should always be made
                asynchronously.

### upgradeFilter Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:upgradeFilter </wsa:Action> <wsa:MessageID> uuid:2057d520-f1c9-4821-a6a5-e859c37e9076 </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/UpgradeFilterService .UpgradeFilterServiceHttpSoap11Endpoint/ </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <upgradeFilter xmlns= "server_url" > <args0> patch </args0> <args1> UCSInstall_UCOS_8.6.0.98000-9002.iso </args1> <args1> UCSInstall_UCOS_8.6.0.98000-9012.iso </args1> <args1> UCSInstall_UCOS_8.6.0.98000-9020.iso </args1> </upgradeFilter> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

### upgradeFilter Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:4F8DCF8A8A3428F84D1297115377730 </wsa:MessageID> <wsa:Action> urn:upgradeFilterResponse </wsa:Action> <wsa:RelatesTo> uuid:473ab189-5161-4ef4-ac30-a8cdad3a9158 </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:upgradeFilterResponse xmlns:ns= "server_url" > <ns:return xmlns:ax233= "server_url/xsd" xmlns:ax234= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax233:UpgradeFilterResponse" > <ax233:remoteMessages xsi:type= "ax233:RemoteMessage" > <ax234:error> false </ax234:error> <ax234:info> false </ax234:info> <ax234:messageKey> warning.upgrade.noupgrades </ax234:messageKey> <ax234:messageType> internal.message.warning </ax234:messageType> <ax234:warning> true </ax234:warning> </ax233:remoteMessages> <ax233:result> internal.request.complete.message </ax233:result> <ax233:upgradeFiles xsi:nil= "true" /> </ns:return> </ns:upgradeFilterResponse> </soapenv:Body> </soapenv:Envelope>
```

This result indicates that the upgrade filter detected a bad file.

# UpgradeProgressStageService

## getCurrentUpgradeProgressStage

The getCurrentUpgradeProgressStage method returns detailed progress information for an upgrade or COP
                file installation that is in progress. Before you can use this method, you need to have initiated a StartUpgradeService call. This call should always be made
                asynchronously.

### getCurrentUpgradeProgressStage Request
                Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getCurrentUpgradeProgressStage </wsa:Action> <wsa:MessageID> uuid:75eb75b0-de1f-4179-8413-8a9c487cd749 </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server_url/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server_url/platform-services/services/UpgradeProgressStageService.UpgradeProgressStageServiceHttpSoap11Endpoint </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <getCurrentUpgradeProgressStage xmlns= "server_url" /> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

None.

### getCurrentUpgradeProgressStage Response
                Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous </wsa:To> <wsa:MessageID> urn:uuid:4A13792C1511BDDB981297716605720 </wsa:MessageID> <wsa:Action> urn:getCurrentUpgradeProgressStageResponse </wsa:Action> <wsa:RelatesTo> uuid:9edecbfe-215b-4ee9-b681-79b3096f8f1c </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getCurrentUpgradeProgressStageResponse xmlns:ns= "server_url" > <ns:return xmlns:ax229= "server_url/xsd" xmlns:ax230= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax229:UpgradeStageResponse" > <ax229:result> internal.request.complete </ax229:result> <ax229:upgradeStage> upgrade.progress.application.installation </ax229:upgradeStage> </ns:return> </ns:getCurrentUpgradeProgressStageResponse> </soapenv:Body> </soapenv:Envelope>
```

This result indicates that an application installation is in progress.

# UpgradeStageService

## getUpgradeStage

The getUpgradeStage method returns the current overall upgrade or COP file installation stage such as
                downloading, validating, or in progress.

### getUpgradeStage Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getUpgradeStage </wsa:Action> <wsa:MessageID> uuid:746e0b0f-d0b6-4e30-ad5e-ba0bc0c13347 </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/UpgradeStageService .UpgradeStageServiceHttpSoap11Endpoint </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <getUpgradeStage xmlns= "server_url" /> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

None.

### getUpgradeStage Response Parameters

Return element children Validated:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:371332A0B549A964C21298940705128 </wsa:MessageID> <wsa:Action> urn:getUpgradeStageResponse </wsa:Action> <wsa:RelatesTo> uuid:93816fa1-1614-46e3-b884-5a7919140c4f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getUpgradeStageResponse xmlns:ns= "server_url" > <ns:return xmlns:ax225= "server_url/xsd" xmlns:ax226= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax225:UpgradeStageResponse" > <ax225:remoteMessages xsi:nil= "true" /> <ax225:result> internal.request.complete </ax225:result> <ax225:upgradeStage> upgrade.stage.validated </ax225:upgradeStage> </ns:return> </ns:getUpgradeStageResponse> </soapenv:Body> </soapenv:Envelope>
```

This result indicates the upgrade stage is validated.

# UpgradeTypeService

## getUpgradeType

The getUpgradeType method returns the type of the current upgrade.

### getUpgradeType Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:getUpgradeType </wsa:Action> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:MessageID> uuid:26634481-3273-4a70-b537-ab4b874e4d6b </wsa:MessageID> </soapenv:Header> <soapenv:Body /> </soapenv:Envelope>
```

None.

### getUpgradeType Response Parameters

Return element children Validated:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://www.w3.org/2003/05/soap-envelope" > <soapenv:Header xmlns:wsa= "http://www.w3.org/2005/08/addressing" > <wsa:Action> urn:getUpgradeTypeResponse </wsa:Action> <wsa:RelatesTo> uuid:a8804cc2-0e60-4e44-9cab-6acb1c3f3fc9 </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getUpgradeTypeResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax229= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax230= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax229:UpgradeTypeResponse" > <ax229:remoteMessages xsi:nil= "true" /> <ax229:result> internal.request.complete </ax229:result> <ax229:upgradeType> L2 </ax229:upgradeType> </ns:return> </ns:getUpgradeTypeResponse> </soapenv:Body> </soapenv:Envelope>
```

- L2 - Standard UC Application upgrade

- RU - Refresh upgrade required for certain major OS changes (for
                                example, migrating from a 32 bit to a 64 bit OS)

# UpgradeValidService

## isUpgradeValid

The isUpgradeValid method determines if the specified upgrade file is valid.

### isUpgradeValid Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:isUpgradeValid </wsa:Action> <wsa:MessageID> uuid:1bbffcbe-e779-4277-9cfc-db285fc52a1f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/UpgradeValidService .UpgradeValidServiceHttpSoap11Endpoint/ </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <isUpgradeValid xmlns= "server_url" > <args0> UCSInstall_UCOS_8.6.0.98000-9020.iso </args0> </isUpgradeValid> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

### isUpgradeValid Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:A42DDA286381C7F5DF1300917556810 </wsa:MessageID> <wsa:Action> urn:isUpgradeValidResponse </wsa:Action> <wsa:RelatesTo> uuid:1431a298-33c5-4885-88e0-a35e9d2d98e3 </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:isUpgradeValidResponse xmlns:ns= "server_url" > <ns:return xmlns:ax237= "server_url/xsd" xmlns:ax238= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax237:UpgradeValidResponse" > <ax237:result> internal.request.complete </ax237:result> <ax237:upgradeValid> true </ax237:upgradeValid> </ns:return> </ns:isUpgradeValidResponse> </soapenv:Body> </soapenv:Envelope>
```

- true if specified file is valid

- false otherwise

# VersionService

## getActiveVersion

The getActiveVersion method returns the active product version.

### getActiveVersion Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getActiveVersion </wsa:Action> <wsa:MessageID> uuid:c37f60b9-92eb-4c1a-8de7-873b60adce19 </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/VersionService .VersionServiceHttpSoap11Endpoint </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <getActiveVersion xmlns= "server_url" /> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

None.

### getActiveVersion Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:B8E556B192135F3CC31298997621402 </wsa:MessageID> <wsa:Action> urn:getActiveVersionResponse </wsa:Action> <wsa:RelatesTo> uuid:455bc1c3-8267-4902-9e7e-8f47b6200ad1 </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getActiveVersionResponse xmlns:ns= "server_url" > <ns:return xmlns:ax217= "server_url/xsd" xmlns:ax218= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax217:VersionResponse" > <ax217:remoteMessages xsi:nil= "true" /> <ax217:result> internal.request.complete </ax217:result> <ax217:version> 8.6.0.98000-9005 </ax217:version> </ns:return> </ns:getActiveVersionResponse> </soapenv:Body> </soapenv:Envelope>
```

The result in the following case shows that the service is throttling.

PAWS permits a maximum of three concurrent threads running. Certain services are denied access based on the Platform API lock, before throttling can occur. Throttled services wait for up to 60 seconds for the throttling semaphore. If the timeout elapses, the service returns a result of internal.request.failed with a
                messageKey error.remote.throttled . If too many Platform Administrative Web Services arrive at once, Platform Administrative Web Services
                throttle.

## getActiveVersion Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <SOAP-ENV:Envelope xmlns:SOAP-ENV= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <SOAP-ENV:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getActiveVersion </wsa:Action> <wsa:MessageID> uuid:c37f60b9-92eb-4c1a-8de7-873b60adce19 </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://server/servlet/WSACallBackHandler </wsa:Address> <wsa:PortType xmlns:ns1= "http://example.org" > ns1:LocalPart </wsa:PortType> </wsa:ReplyTo> <wsa:To> https://server/platform-services/services/VersionService .VersionServiceHttpSoap11Endpoint </wsa:To> </SOAP-ENV:Header> <SOAP-ENV:Body> <getActiveVersion xmlns= "server_url" /> </SOAP-ENV:Body> </SOAP-ENV:Envelope>
```

None.

## getActiveVersion Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://server/servlet/WSACallBackHandler </wsa:To> <wsa:MessageID> urn:uuid:E4F05C2A76D78B5EEB1301499080974 </wsa:MessageID> <wsa:Action> urn:getActiveVersionResponse </wsa:Action> <wsa:RelatesTo> uuid:ec12b570-6066-41d1-a0ff-506401a3302f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getActiveVersionResponse xmlns:ns= "server_url" > <ns:return xmlns:ax217= "server_url/xsd" xmlns:ax218= "server_url/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax217:VersionResponse" > <ax217:remoteMessages xsi:type= "ax217:RemoteMessage" > <ax218:error> true </ax218:error> <ax218:info> false </ax218:info> <ax218:messageKey> error.remote.throttled </ax218:messageKey> <ax218:messageType> internal.message.error </ax218:messageType> <ax218:warning> false </ax218:warning> </ax217:remoteMessages> <ax217:result> internal.request.failed </ax217:result> <ax217:version xsi:nil= "true" /> </ns:return> </ns:getActiveVersionResponse> </soapenv:Body> </soapenv:Envelope>
```

## getInactiveVersion

The getInActiveVersion method returns the inactive product version.

### getInactiveVersion Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getInactiveVersion </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <getInactiveVersion xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### getInactiveVersion Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:1f248579-20e4-452f-ac40-a4e2cfea5fb7 </wsa:MessageID> <wsa:Action> urn:getInactiveVersionResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getInactiveVersionResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax221= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax222= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax221:VersionResponse" > <ax221:remoteMessages xsi:nil= "true" /> <ax221:result> internal.request.complete </ax221:result> <ax221:version></ax221:version> </ns:return> </ns:getInactiveVersionResponse> </soapenv:Body> </soapenv:Envelope>
```

# M2DataExportService

## m2DataExport

The m2DataExport method begins an export of the Node's data to an external FTP server.

### m2 dataExport Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:m2DataExport </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <m2DataExport xmlns= "http://services.api.platform.vos.cisco.com" /> <arg0> The remote SFTP directory where the exported data gets copied to </arg0> <arg1> The remote IP Address of  SFTP Directory </arg1> <arg2> The remote SFTP username for logging in to the FTP server </arg2> <arg3> The remote SFTP password for logging in to the FTP server. </arg3> <arg4> The Destination Hostname </arg4> <arg5> The Destination IpAddress </arg5> </soapenv:Body> </soapenv:Envelope>
```

### m2dataExport Response Parameters

Return element children:

This example shows that an error occurred.

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:a0541e26-939a-490b-a3eb-c43ff752d2e0 </wsa:MessageID> <wsa:Action> urn:m2DataExportResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:m2DataExportResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax2105= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax2106= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax2105:M2DataExportResponse" > <ax2105:remoteMessages xsi:type= "ax2105:RemoteMessage" > <ax2106:error> true </ax2106:error> <ax2106:info> false </ax2106:info> <ax2106:messageKey> internal.request.denied.lock </ax2106:messageKey> <ax2106:messageType> internal.message.error </ax2106:messageType> <ax2106:warning> false </ax2106:warning> <ax2105:messageParams> platform.api.network.address </ax2105:messageParams> <ax2105:messageParams> 27543@rwerer </ax2105:messageParams> <ax2105:messageParams> CreateUffDbImportExportThread-211 </ax2105:messageParams> </ax2105:remoteMessages> <ax2105:result> internal.request.failed </ax2105:result> <ax2105:m2DataExportResult> error.undetermined.result </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.invalid.cmd.args </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.multiple.instance.notallowed </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.create.pid </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.remove.pid </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.acquireLock </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.releaseLock </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.require.abosulte.sftpPath </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.sftp.not.reachable </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.invalid.sftp.password </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.createClusterInfo </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.setPermissions.ClusterInfo </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.create.nodedirectory </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.currNode.auth.failed </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.export.util.failed </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.component.install.failed </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.copy.ucplatform.failed </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.delete.oldexportdata </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.create.rootdir </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.get.activeVer </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.copy.remoteserver </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.dataExport.start </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.incorrect.format </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.delete.sftp </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.publisher.export.notfound </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.create.exportDirectory </ax2105:m2DataExportResult> <ax2105:m2DataExportResult> error.dynamic.export.failed </ax2105:m2DataExportResult> </ns:return> </ns:m2DataExportResponse> </soapenv:Body> </soapenv:Envelope>
```

- A status code such as error.undetermined.result indicating, if possible, the
                        result of the dataExport.

- A status code such as error.invalid.cmd.args if invalid command line args detected..

- A status code such as error.multiple.instance.notallowed if multiple concurrent instance of this program is forbidden.

- A status code such as error.create.pid if failed to create PID file.

- A status code such as error.remove.pid if failed to remove the PID file.

- A status code such as error.acquireLock if failed to acquire the LOCK file.

- A status code such as error.releaseLock if failed to remove the LOCK file.

- A status code such as error.require.abosulte.sftpPath if SFTP directory path is not an absolute path.

- A status code such as error.sftp.not.reachable if server failed validation or is unreachable.

- A status code such as error.invalid.sftp.password if SFTP password provided is null.

- A status code such as error.createClusterInfo if failed to create the cluster info xml file.

- A status code such as error.setPermissions.ClusterInfo if failed to set permissions of cluster info xml file.

- A status code such as error.create.nodedirectory if failed to create node directory..

- A status code such as error.currNode.auth.failed if the current node is not authenticated.

- A status code such as error.export.util.failed if export util failed.

- A status code such as error.component.install.failed if component install failed..

- A status code such as error.copy.ucplatform.failed if copying uc platform post failed.

- A status code such as error.delete.oldexportdata if failed to delete the data of the previous data export operation in the SFTP server.

- A status code such as error.create.rootdir if failed to create root directory.

- A status code such as error.get.activeVer if failed to fetch the active version.

- A status code such as error.copy.remoteserver if failed to copy the export data to remote server.

- A status code such as error.dataExport.start if user selected not to start the data export.

- A status code such as error.incorrect.format if not in correct format.

- A status code such as error.delete.sftp if failed to delete the existing cluster folder in the given sftp location.

- A status code such as error.publisher.export.notfound if publisher's export did not run.

- A status code such as error.create.exportDirectory if failed to create dataexport directory..

- A status code such as error.dynamic.export.failed if dynamic data export failed.

# M2DataExportStatusService

## m2DataExportStatus

The m2DataExportStatus method shows the status of a request made by the m2DataExport method.

### m2dataExportStatus Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:m2dataExportStatus </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <m2DataExportStatus xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### m2dataExportStatus Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:0a144548-81c9-42f0-a302-19c7c37a09e6 </wsa:MessageID> <wsa:Action> urn:m2dataExportStatusResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:m2DataExportStatusResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax2109= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax2110= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax2109:M2DataExportStatusResponse" > <ax2109:result> data.export.succeeded </ax2109:result> <ax2105:m2DataExportStatusResult> error.undetermined.result </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.invalid.cmd.args </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.multiple.instance.notallowed </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.create.pid </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.remove.pid </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.acquireLock </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.releaseLock </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.require.abosulte.sftpPath </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.sftp.not.reachable </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.invalid.sftp.password </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.createClusterInfo </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.setPermissions.ClusterInfo </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.create.nodedirectory </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.currNode.auth.failed </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.export.util.failed </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.component.install.failed </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.copy.ucplatform.failed </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.delete.oldexportdata </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.create.rootdir </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.get.activeVer </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.copy.remoteserver </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.dataExport.start </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.incorrect.format </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.delete.sftp </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.publisher.export.notfound </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.create.exportDirectory </ax2105:m2DataExportStatusResult> <ax2105:m2DataExportStatusResult> error.dynamic.export.failed </ax2105:m2DataExportStatusResult> </ns:return> </ns:m2DataExportStatusResponse> </soapenv:Body> </soapenv:Envelope>
```

- A status code such as error.undetermined.result indicating, if possible, the
                       			 result of the dataExport.

- A status code such as error.invalid.cmd.args if invalid command line args detected..

- A status code such as error.multiple.instance.notallowed if multiple concurrent instance of this program is forbidden.

- A status code such as error.create.pid if failed to create PID file.

- A status code such as error.remove.pid if failed to remove the PID file.

- A status code such as error.acquireLock if failed to acquire the LOCK file.

- A status code such as error.releaseLock if failed to remove the LOCK file.

- A status code such as error.require.abosulte.sftpPath if SFTP directory path is not an absolute path.

- A status code such as error.sftp.not.reachable if server failed validation or is unreachable.

- A status code such as error.invalid.sftp.password if SFTP password provided is null.

- A status code such as error.createClusterInfo if failed to create the cluster info xml file.

- A status code such as error.setPermissions.ClusterInfo if failed to set permissions of cluster info xml file.

- A status code such as error.create.nodedirectory if failed to create node directory..

- A status code such as error.currNode.auth.failed if the current node is not authenticated.

- A status code such as error.export.util.failed if export util failed.

- A status code such as error.component.install.failed if component install failed..

- A status code such as error.copy.ucplatform.failed if copying uc platform post failed.

- A status code such as error.delete.oldexportdata if failed to delete the data of the previous data export operation in the SFTP server.

- A status code such as error.create.rootdir if failed to create root directory.

- A status code such as error.get.activeVer if failed to fetch the active version.

- A status code such as error.copy.remoteserver if failed to copy the export data to remote server.

- A status code such as error.dataExport.start if user selected not to start the data export.

- A status code such as error.incorrect.format if not in correct format.

- A status code such as error.delete.sftp if failed to delete the existing cluster folder in the given sftp location.

- A status code such as error.publisher.export.notfound if publisher's export did not run.

- A status code such as error.create.exportDirectory if failed to create dataexport directory..

- A status code such as error.dynamic.export.failed if dynamic data export failed.

# M2DataExportCancelService

## m2DataExportCancel

The m2DataExportCancel method shows the cancel status of a request made by the m2DataExport method.

### m2dataExportCancel Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:m2dataExportCancel </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <m2DataExportCancel xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### m2DataExportCancel Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:0a144548-81c9-42f0-a302-19c7c37a09e6 </wsa:MessageID> <wsa:Action> urn:m2DataExportCancelResponse </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:m2DataExportCancelResponse xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax2109= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax2110= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax2109:M2DataExportCancelResponse" > <ax2109:result> data.export.terminated </ax2109:result> <ax2105:m2DataExportCancel> error.undetermined.result </ax2105:m2DataExportCancel> <ax2105:m2DataExportCancel> data.export.termination.not.required </ax2105:m2DataExportCancel> <ax2105:m2DataExportCancel> dynamic.export.inProgress.cannotCancel </ax2105:m2DataExportCancel> <ax2105:m2DataExportCancel> export.termination.failed </ax2105:m2DataExportCancel> </ns:return> </ns:m2DataExportCancelResponse> </soapenv:Body> </soapenv:Envelope>
```

- A status code such as error.undetermined.result if there is undetermined result.

- A status code such as data.export.termination.not.required if DataExport not running and nothing to cancel.

- A status code such as dynamic.export.inProgress.cannotCancel if Dynamic DataExport in progress and it cannot be cancelled.

- A status code such as export.termination.failed if failed to cancel the M2DataExportcancelService.

# SpaceCalculationService

## getSpaceCalculation

The getSpaceCalculation method shows the space calculation status of a request made by the getSpaceCalculation method.

### spaceCalculation Request Parameters

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd= "http://www.w3.org/2001/XMLSchema" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:Action> urn:getSpaceCalculation </wsa:Action> <wsa:MessageID> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:MessageID> <wsa:ReplyTo> <wsa:Address> http://www.w3.org/2005/08/addressing/anonymous </wsa:Address> </wsa:ReplyTo> <wsa:To></wsa:To> </soapenv:Header> <soapenv:Body> <getSpaceCalculation xmlns= "http://services.api.platform.vos.cisco.com" /> </soapenv:Body> </soapenv:Envelope>
```

None.

### spaceCalculation Response Parameters

Return element children:

```
<?xml version="1.0" encoding="UTF-8"?> <soapenv:Envelope xmlns:soapenv= "http://schemas.xmlsoap.org/soap/envelope/" > <soapenv:Header xmlns:wsa= "http://schemas.xmlsoap.org/ws/2004/08/addressing" > <wsa:To> http://www.w3.org/2005/08/addressing/anonymous </wsa:To> <wsa:MessageID> urn:uuid:0a144548-81c9-42f0-a302-19c7c37a09e6 </wsa:MessageID> <wsa:Action> urn:getSpaceCalculation </wsa:Action> <wsa:RelatesTo> uuid:63e5d8ca-dcac-40af-916b-d32ec3382d0f </wsa:RelatesTo> </soapenv:Header> <soapenv:Body> <ns:getSpaceCalculation xmlns:ns= "http://services.api.platform.vos.cisco.com" > <ns:return xmlns:ax2109= "http://element.services.api.platform.vos.cisco.com/xsd" xmlns:ax2110= "http://api.platform.vos.cisco.com/xsd" xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance" xsi:type= "ax2109:getSpaceCalculation" > <ax2109:result> internal.request.complete </ax2109:result> <ax2109:getSpaceCalculation> internal.request.complete </ax2109:getSpaceCalculation> <ax2109:getSpaceCalculation> error.soap.internal </ax2109:getSpaceCalculation> </ns:return> </ns:getSpaceCalculation> </soapenv:Body> </soapenv:Envelope>
```

| WSA Header | Type | Value |
|---|---|---|
| Action | urn | Contains the PAWS request name |
| ReplyTo | <wsa:Address> | Asynchronous requests: the response destination URL Synchronous requests: the WSA Anonymous URL |
| MessageID | uuid | A unique string (for example a UUID) which is returned in the response |
| To | urn | The address of the intended receiver (may be nil) |
| RelatesTo | uuid | (Responses only) The MessageID provided in the original asynchronous request |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| APIVersion | The API version in use. |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| upgradeCancelled | Boolean: true if upgrade is canceled false otherwise |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| clusterNodeStatus | address - IP address of the node alias - an alpha-numeric identifier for the node hostname - the URL of the node’s host server primaryNode - IP address of the primary node associated with this node,
                                if node is primary, same as address ClusterNodes element type - cluster.node.type.primary if primary node and cluster.node.type.secondary if secondary node dbRole - cluster.node.type.primary if primary node and cluster.node.type.secondary if secondary node role - The number of the role status - cluster.node.status.online if online |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| clusterNodes | address - IP address of the node alias - an alpha-numeric identifier for the node hostname - the URL of the node’s host server primary - Boolean: true if primary node false otherwise primaryNode - IP address of the primary node associated with this node,
                                if node is primary, same as address ClusterNodes element secondary - Boolean: true if secondary node false otherwise type - cluster.node.type.primary if primary node and cluster.node.type.secondary if secondary node |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| clusterReplicationStatusOK | Boolean: true if status is ok false if status is not ok |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| nodeReplicationStatusOK | Boolean: true if status is ok false if status is not ok |

| Parameter | Description |
|---|---|
| args0 | The IP address of the FTP server where you plan to send the file. |
| args1 | The port you want to use for FTP (usually 22). |
| args2 | The username for logging in to the FTP server. |
| args3 | The password for logging in to the FTP server. |
| args4 | The remote directory. |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| dataExportResult | A status code such as error.undetermined.result indicating, if possible, the
                        result of the dataExport. |
| remoteMessages | see Response RemoteMessages |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| dataExportStatus | Returns a status code such as data.export.status.none if there is no status to
                        report. |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| deploymentMode | Deployment mode as follows: Enterprise - The server is used as part of a standard enterprise
                                deployment. HCS - The server is hosted by a service provider using the Hosted
                                Collaboration Solution (HCS) end-to-end system. HCS-LE - The server is hosted by a service provider using the Hosted
                                Collaboration Solution (HCS) end-to-end system with centralized management of services
                                and licensing to multiple business units. |

| Parameter | Description |
|---|---|
| args0 | Enterprise - The server is used as part of a standard enterprise
                                deployment. HCS - The server is hosted by a service provider using the Hosted
                                Collaboration Solution (HCS) end-to-end system. HCS-LE - The server is hosted by a service provider using the Hosted
                                Collaboration Solution (HCS) end-to-end system with centralized management of services
                                and licensing to multiple business units. |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| deploymentMode | xsi:nil=“true” if there are no deployment mode messages |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| hardwareInformation | Some of the following parameters are self-explanatory: diskCount - The number of disks. diskInformation number - Number of disks. size - Size in gigabytes. total - Total number of disks. hasMotorizedDriveTray - Does the drive have a motorized drive tray? isServerHeadless - Is the server headless (no monitor). memory - Memory installed. memoryAvailable - How much of that memory is available. memoryUsed - How much of that memory is in use. model - The model of the hardware (or virtual machine). objectId - The object ID. oemModel - The OEM model, if available. opticalDrives driveTray - Is the optical drive tray motorized? partitions - There may be multiple partitions. There are three in this
                                sample case. 0 - First partition. available - Available space. name - The name or mount point of the partition. total - Total space on the partition. unrestricted - Whether or not the partition is
                                            unrestricted. used - How much space on the partition is used. 1 - Second partition. available - Available space. name - The name or mount point of the partition. total - Total space on the partition. unrestricted - Whether or not the partition is unrestricted. used - How much space on the partition is used. 2 - Third partition. available - Available space. name - The name or mount point of the partition. total - Total space on the partition. unrestricted - Whether or not the partition is unrestricted. used - How much space on the partition is used. processorCount processorSpeed processorType raidStatus - Information about RAID if available. serialNumber - Serial number of the machine or virtual machine. supportedHardware: true if hardware is supported false if not virtualMachine: true if this is a virtual machine false if not |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| hardwareModel | model - Model name of the hardware objectId - Numerical ID for the model oemModel - OEM name of the model, if it exists serialNumber - Serial number supportedHardware - Boolean: true if hardware is supported false if not virtualMachine - Boolean: true if hardware is actually a virtual machine false if not |

| Parameter | Description |
|---|---|
| args0 | The backup name. |
| args1 | The time when this backup should be run in yyyymmddThhmmsss-offset format. |
| args2 | Boolean: true enables scheduled backup false disables scheduled backup |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| backupProgressResult | xsi:nil=“true” - There are no backupProgressResult messages, or
                        progress result messages |
| startBackupResult | xsi:nil=“true” - There are no startBackupResult messsages, or
                        backup result messsages |
| updateScheduleResult | Message relating successs or failure of scheduling backup |

| Parameter | Description |
|---|---|
| args0 | Schedule name |
| args1 | scheduleID |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| backupProgressResult | xsi:nil=true - There are no backupProgressResult messages, or progress result
                        messages |
| startBackupResult | xsi:nil=true - There are no startBackupResult messsages, or backup result
                        messsages |
| updateScheduleResult | Message relating successs or failure of update schedule |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| backupProgressResult | xsi:nil=“true” - There are no backupProgressResult messages, or
                        progress result messages |
| startBackupResult | xsi:nil=“true” - There are no startBackupResult messsages, or
                        backup result messsages |
| updateScheduleResult | Message relating successs or failure of update |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| DHCPEnabled | Boolean, true if DHCP is enabled. |
| GW | The default gateway. |
| IP | The IP address for the host. |
| IPMask | The IP subnet mask. |
| networkChangeStatus | A change status, if available. |

| Parameter | Description |
|---|---|
| args0 | string - The new hostname |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| DHCPEnabled | Boolean, true if DHCP is enabled. |
| GW | The default gateway. |
| IP | The IP address for the host. |
| IPMask | The IP subnet mask. |
| networkChangeStatus | A change status, if available. |

| Parameter | Description |
|---|---|
| args0 | string - The new IP address |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details |
| remoteMessages | see Response RemoteMessages |
| DHCPEnabled | Boolean, true if DHCP is enabled. |
| GW | The default gateway. |
| IP | The IP address for the host. |
| IPMask | The IP subnet mask. |
| networkChangeStatus | A change status, if available. |

| Parameter | Description |
|---|---|
| args0 | string - The new hostname |
| args1 | string - The new IP address |
| args2 | string - The IP subnet address mask |
| args3 | string - The default gateway |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| DHCPEnabled | Boolean, true if DHCP is enabled. |
| GW | The default gateway. |
| IP | The IP address for the host. |
| IPMask | The IP subnet mask. |
| networkChangeStatus | A change status, if available. |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| DHCPEnabled | Boolean, true if DHCP is enabled. |
| GW | The default gateway. |
| IP | The IP address for the host. |
| IPMask | The IP subnet mask. |
| networkChangeStatus | A change status, if available. |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| status | The status of the Network check: boolean true if ok false if not |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| options | xsi:nil=“true” true if no
                        options are installed, false if options are installed. |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| options | xsi:nil=“true” true if no
                        options are installed, false if options are installed |

| Parameter | Description |
|---|---|
| args0 | The FTP server where you plan to send the file. |
| args1 | The port you want to use for FTP (usually 22). |
| args2 | The username for logging in to the FTP server. |
| args3 | The password for logging in to the FTP server. |
| args4 | The location of the platform configuration file. |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| platformConfigExportStatus | Returns platform.config.export.failed if the file transfer was unsuccessful. |

| Parameter | Description |
|---|---|
| args0 | name - The name of the upgrade file path - The path/directory containing the upgrade file password - The S/FTP file server password server - The S/FTP file server hostname or IP address upgradeLocation - One of two values: upgradefile.location.remote.sftp - indicating the upgrade is
                                        located on an SFTP server upgradefile.location.remote.ftp - indicating the upgrade is
                                        located on a FTP server upgradeType - Currently always patch .
                                More types may be supported in the future. user - The S/FTP file server user |
| args1 | A unique session ID provided by the client. When the prepare service starts, this session ID is
                        associated with the upgrade. Subsequent calls to the start upgrade service should provide the
                        same session ID, otherwise an error.upgrade.anotheruser is generated. This
                        allows the services to differentiate between multiple clients and prevent accidental
                        overrides/interruptions. pm238 - sample sessionID |
| args2 | Boolean - true or false Set
                        this parameter to false initially. If the value is true , allows
                        the session ID to be overridden. This is useful when one client decides to take over the upgrade
                        from another client which can happen when the first client crashed and a second client instance
                        is used to start the upgrade. The admin who prepared the upgrade hands it off to a coworker, and
                        so on. If the SOAP request returns with an error.upgrade.anotheruser message,
                        then the SOAP client should prompt the user if they would like to override the session ID. If
                        the user says yes, then submit the request again with arg2= true . |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| upgradeFile | name - upgrade or COP file name password - the passsword for the server that contains the upgrade file path - upgrade file path server - the name of the server that provided the upgrade file upgradeLocation - url of upgrade serve upgradeType - upgradefile.type.patch user - user name on upgrade server |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| installedProducts | displayName - The name of the product as displayed name - The name of the product if different from the display name. version - The product’s version number. adminUrl - URL of the product’s admin GUI id - the product ID |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| productName | The overall product name |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| restartSystemStatus | The current restart status in this form: internal.request. status The
                        status is either of these: internal.request.processing - The restart is still in progress internal.request.complete - The restart has completed |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| SSOCertificate | The Single Sign On (SSO) Certificate |
| idpMetadataUploadTime | The Identity Provider (IdP) Metadata upload time |
| samlTestSuccess | The status of the Security Assertion Markup Language (SAML) Test |
| samlTestTime | The Security Assertion Markup Language (SAML) test time |
| serverMetadataDownloadTime | The Server Metadata Download Time |
| ssoResult | The Single Sign On (SSO) result |
| ssoResultDescription | A description of the Single Sign On (SSO) result |
| status | The status |
| vanityURLStatus | The vanity URL status |

| Parameter | Description |
|---|---|
| args0 | Boolean: true if you want to enable SSO false if you want to disable SSO |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| SSOCertificate | The Single Sign On (SSO) Certificate |
| idpMetadataUploadTime | The Identity Provider (IdP) Metadata upload time |
| samlTestSuccess | The status of the Security Assertion Markup Language (SAML) Test |
| samlTestTime | The Security Assertion Markup Language (SAML) test time |
| serverMetadataDownloadTime | The Server Metadata Download Time |
| ssoResult | The Single Sign On (SSO) result |
| ssoResultDescription | A description of the Single Sign On (SSO) result |
| status | The status |
| vanityURLStatus | The vanity URL status |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| SSOCertificate | The Single Sign On (SSO) Certificate |
| idpMetadataUploadTime | The Identity Provider (IdP) Metadata upload time |
| samlTestSuccess | The status of the Security Assertion Markup Language (SAML) Test |
| samlTestTime | The Security Assertion Markup Language (SAML) test time |
| serverMetadataDownloadTime | The Server Metadata Download Time |
| ssoResult | The Single Sign On (SSO) result |
| ssoResultDescription | A description of the Single Sign On (SSO) result |
| status | The status |
| vanityURLStatus | The vanity URL status |

| Parameter | Description |
|---|---|
| args0 | The IdP metadata content to be uploaded. This is the complete XML content of the IdP metadata
                        file. Note the XML data must be escaped/encoded or enclosed in a CDATA section . |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| SSOCertificate | The Single Sign On (SSO) Certificate |
| idpMetadataUploadTime | The Identity Provider (IdP) Metadata upload time |
| samlTestSuccess | The status of the Security Assertion Markup Language (SAML) Test |
| samlTestTime | The Security Assertion Markup Language (SAML) test time |
| serverMetadataDownloadTime | The Server Metadata Download Time |
| ssoResult | The Single Sign On (SSO) result |
| ssoResultDescription | A description of the Single Sign On (SSO) result |
| status | The status |
| vanityURLStatus | The vanity URL status |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| SSOCertificate | The Single Sign On (SSO) Certificate |
| idpMetadataUploadTime | The Identity Provider (IdP) Metadata upload time |
| samlTestSuccess | The status of the Security Assertion Markup Language (SAML) Test |
| samlTestTime | The Security Assertion Markup Language (SAML) test time |
| serverMetadataDownloadTime | The Server Metadata Download Time |
| ssoResult | The Single Sign On (SSO) result |
| ssoResultDescription | A description of the Single Sign On (SSO) result |
| status | The status |
| vanityURLStatus | The vanity URL status |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| SSOCertificate | The Single Sign On (SSO) Certificate EntityDescriptor - The following is a
                        breakdown of the SSO
                        Certificate: SPSSODescriptor KeyDescriptor 0 - There can be multiple KeyDescriptor sections. This is the first in
                                the example. KeyInfo X509Data X509Certificate 1 - There can be multiple KeyDescriptor sections. This is the second in
                                the example. KeyInfo X509Data X509Certificate NameIDFormat AssertionConsumerService Binding Location index |
| idpMetadataUploadTime | The Identity Provider (IdP) Metadata upload time |
| samlTestSuccess | The status of the Security Assertion Markup Language (SAML) Test |
| samlTestTime | The Security Assertion Markup Language (SAML) test time |
| serverMetadataDownloadTime | The Server Metadata Download Time |
| ssoResult | The Single Sign On (SSO) result |
| ssoResultDescription | A description of the Single Sign On (SSO) result |
| status | The status |
| vanityURLStatus | The vanity URL status |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| SSOCertificate | The Single Sign On (SSO) Certificate EntityConfig - Information about the
                        SSO Certificate Extended
                        Metadata: SPSSOConfig Attribute transientUser signingCertAlias encryptionCertAlias fedletAdapter spAccountMapper useNameIDAsSPUserID spAttributeMapper attributeMap assertionTimeSkew cotlist |
| idpMetadataUploadTime | The Identity Provider (IdP) Metadata upload time |
| samlTestSuccess | The status of the Security Assertion Markup Language (SAML) Test |
| samlTestTime | The Security Assertion Markup Language (SAML) test time |
| serverMetadataDownloadTime | The Server Metadata Download Time |
| ssoResult | The Single Sign On (SSO) result |
| ssoResultDescription | A description of the Single Sign On (SSO) result |
| status | The status |
| vanityURLStatus | The vanity URL status |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| SAMLMetaData | Nil |
| SSOCertificate | Nil |
| idpMetadataUploadTime | Zero |
| multiServerCert | Whether the node has a multi-server certificate - Boolean |
| samlTestSuccess | false |
| samlTestTime | Zero |
| serverMetadataDownloadTime | Zero |
| ssoResult | true |
| ssoResultDescription | Nil |
| status | Zero |
| vanityURLStatus | false |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| SAMLMetaData | Contains the generated clusterwide metadata in XML encoded format |
| SSOCertificate | The Single Sign On (SSO) Certificate in XML encoded format EntityConfig -
                        Information about the SSO Certificate Extended Metadata: SPSSOConfig Attribute transientUser signingCertAlias encryptionCertAlias fedletAdapter spAccountMapper useNameIDAsSPUserID spAttributeMapper attributeMap assertionTimeSkew cotlist |
| idpMetadataUploadTime | The Identity Provider (IdP) Metadata upload time |
| samlTestSuccess | The status of the Security Assertion Markup Language (SAML) Test |
| samlTestTime | The Security Assertion Markup Language (SAML) test time |
| serverMetadataDownloadTime | The Server Metadata Download Time |
| ssoResult | The Single Sign On (SSO) result |
| ssoResultDescription | A description of the Single Sign On (SSO) result |
| status | The status |
| vanityURLStatus | The vanity URL status |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| SAMLMetaData | Contains the generated clusterwide metadata in XML encoded format |
| SSOCertificate | The Single Sign On (SSO) Certificate in XML encoded format EntityConfig -
                        Information about the SSO Certificate Extended Metadata: SPSSOConfig Attribute transientUser signingCertAlias encryptionCertAlias fedletAdapter spAccountMapper useNameIDAsSPUserID spAttributeMapper attributeMap assertionTimeSkew cotlist |
| idpMetadataUploadTime | The Identity Provider (IdP) Metadata upload time |
| multiServerCert | Whether the node has a multi-server certificate |
| samlTestSuccess | The status of the Security Assertion Markup Language (SAML) Test |
| samlTestTime | The Security Assertion Markup Language (SAML) test time |
| serverMetadataDownloadTime | The Server Metadata Download Time |
| ssoResult | The Single Sign On (SSO) result |
| ssoResultDescription | A description of the Single Sign On (SSO) result |
| status | The status |
| vanityURLStatus | The vanity URL status |

| Parameter | Description |
|---|---|
| args0 | The SP metadata content to be uploaded. This is the complete XML content of the SP metadata
                        file. Note the XML data must be escaped/encoded or enclosed in a CDATA section |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| remoteMessages | see Response RemoteMessages |
| SAMLMetaData | Contains the generated clusterwide metadata in XML encoded format |
| SSOCertificate | The Single Sign On (SSO) Certificate in XML encoded format EntityConfig -
                        Information about the SSO Certificate Extended Metadata: SPSSOConfig Attribute transientUser signingCertAlias encryptionCertAlias fedletAdapter spAccountMapper useNameIDAsSPUserID spAttributeMapper attributeMap assertionTimeSkew cotlist |
| idpMetadataUploadTime | The Identity Provider (IdP) Metadata upload time |
| multiServerCert | Whether the node has a multi-server certificate |
| samlTestSuccess | The status of the Security Assertion Markup Language (SAML) Test |
| samlTestTime | The Security Assertion Markup Language (SAML) test time |
| serverMetadataDownloadTime | The Server Metadata Download Time |
| ssoResult | The Single Sign On (SSO) result |
| ssoResultDescription | A description of the Single Sign On (SSO) result |
| status | The status |
| vanityURLStatus | The vanity URL status |

| Parameter | Description |
|---|---|
| args0 | string - The session ID A unique session ID provided by the client. When the prepare
                        service starts, this session ID is associated with the upgrade. Subsequent calls to the start
                        upgrade service should provide the same session ID, otherwise an error.upgrade.anotheruser is generated. This allows the services to differentiate between multiple clients and prevent
                        accidental overrides/interruptions. |
| args1 | Boolean - true or false Set
                        this parameter to false initially. If the value is true , allows the session ID to be overridden. This is
                        useful when one client decides to take over the upgrade from another client which can happen
                        when the first client crashed and a second client instance is used to start the upgrade. The
                        admin who prepared the upgrade hands it off to a coworker, and so on. |
| args2 | Boolean - true or false true if the server
                        should automatically switch to the new version if the upgrade completes successfully. |

| Parameter | Description |
|---|---|
| remoteMessages | see Response RemoteMessages |
| result | A message such as internal.request.failed - request call failed. See messageKey child of remoteMessages for cause of failure. |

| Parameter | Description |
|---|---|
| remoteMessages | see Response RemoteMessages |
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. If internal.request.failed ,
                        see messageKey child of remoteMessages for cause of failure. |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| switchVersionStatus | The current restart status in this form: internal.request. status The
                        status can be either: internal.request.processing - The switch version is still in progress internal.request.complete - The switch version has completed |

| Parameter | Description |
|---|---|
| args0 | The IP address for the FTP server where you plan to send the file. |
| args1 | The port you want to use for FTP (usually 22). |
| args2 | The username for logging in to the FTP server. |
| args3 | The password for logging in to the FTP server. |
| args4 | The remote directory for the import/export. |
| args5 | The local directory for the import/export. |
| args6 | The desired action, import or export. |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Application Layer Messages and Status & Types in the Developer
                            Guide for details. |
| remoteMessages | see Response RemoteMessages |
| uffDbStatus | A status code such as error.undetermined.result may occur if the result cannot
                        be determined. See Error Codes in the Developer
                            Guide for details. |

| Parameter | Description |
|---|---|
| args0 | The upgrade type, for example patch |
| args1 | The file name of an upgrade file (you can have multiple upgrade files such as args2 and args3) |
| args2 | The file name of an upgrade file |
| args3 | The file name of an upgrade file |

| Parameter | Description |
|---|---|
| remoteMessages | see Response RemoteMessages |
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| upgradeFiles | Boolean for the nil attribute value, true if the upgrade file
                        does not exist or is bad, or upgrade file exists otherwise. |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| upgradeStage | Current progress of the upgrade installation as follows: upgrade.progress.populating.archives - Populating archives upgrade.progress.populating.os.rpms - Populating OS
                        RPMs upgrade.progress.populating.hw.rpms - Populating HW RPMs upgrade.progress.populating.deployment.rpms - Populating Deployment RPMs upgrade.progress.os.installation - OS
                        Installation upgrade.progress.platform.preinstall - Platform Pre Install upgrade.progress.os.rpms.installation - OS RPMs Installation upgrade.progress.platform.postinstall - Platform Post
                        Install upgrade.progress.platform.postinstall.nochroot - Platform Post
                        Install - nochroot upgrade.progress.create.special.accounts - Creating
                        important user accounts/groups upgrade.progress.tomcat.config - Setting up
                        Tomcat configuration upgrade.progress.disable.keys.functions - Disabling
                        various keys and functions upgrade.progress.create.ccm.accounts - Creating
                        CCM Account upgrade.progress.hw.based.install - HW RPMs
                        installation upgrade.progress.updating.rc.local - Updating
                        rc.local upgrade.progress.application.installation - Application
                        Installation upgrade.progress.finalization - Finalization |

| Parameter | Description |
|---|---|
| remoteMessages | see Response RemoteMessages |
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| upgradeStage | Current stage of the upgrade installation as
                        follows: upgrade.stage.cancelled - Canceled upgrade.stage.checksumming - Calculating File Checksum upgrade.stage.completed - Completed upgrade.stage.configuring - Configuring (only set if someone is using the OS Admin or CLI to install an upgrade or COP
                        file) upgrade.stage.determining.files - Determining Valid Files (only set if
                        someone is using the OS Admin or CLI to install an upgrade or COP file upgrade.stage.downloading - Downloading File upgrade.stage.error - Error (indicates
                        failure) upgrade.stage.installing - Installing File upgrade.stage.none - None upgrade.stage.validating - Validating File upgrade.stage.validated - File Validated |

| Parameter | Description |
|---|---|
| remoteMessages | see Response RemoteMessages |
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| upgradeType | Type of the current upgrade as follows: L2 - Standard UC Application upgrade RU - Refresh upgrade required for certain major OS changes (for
                                example, migrating from a 32 bit to a 64 bit OS) |

| Parameter | Description |
|---|---|
| arg0 | The upgrade file name |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| upgradeValid | Boolean: true if specified file is valid false otherwise |

| Parameter | Description |
|---|---|
| remoteMessages | see Response RemoteMessages |
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| version | The product version number. |

| Parameter | Description |
|---|---|
| remoteMessages | see Response RemoteMessages |
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| version | Boolean for the nil attribute value, true if no version number
                        could be determined, or the version number. |

| Parameter | Description |
|---|---|
| remoteMessages | see Response RemoteMessages |
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| version | The inactive product version number. |

| Parameter | Description |
|---|---|
| args0 | The remote SFTP directory where the exported data gets copied to |
| args1 | The remote IP Address of  SFTP Directory |
| args2 | The remote SFTP username for logging in to the FTP server. |
| args3 | The remote SFTP password for logging in to the FTP server. |
| args4 | The Destination Hostname |
| args5 | The Destination IpAddress |

| Parameter | Description |
|---|---|
| result | A result code such as data.export.succeeded that describes the result. See
                        Error Codes in the Developer Guide for details. |
| m2DataExportResult | A status code such as error.undetermined.result indicating, if possible, the
                        result of the dataExport. A status code such as error.invalid.cmd.args if invalid command line args detected.. A status code such as error.multiple.instance.notallowed if multiple concurrent instance of this program is forbidden. A status code such as error.create.pid if failed to create PID file. A status code such as error.remove.pid if failed to remove the PID file. A status code such as error.acquireLock if failed to acquire the LOCK file. A status code such as error.releaseLock if failed to remove the LOCK file. A status code such as error.require.abosulte.sftpPath if SFTP directory path is not an absolute path. A status code such as error.sftp.not.reachable if server failed validation or is unreachable. A status code such as error.invalid.sftp.password if SFTP password provided is null. A status code such as error.createClusterInfo if failed to create the cluster info xml file. A status code such as error.setPermissions.ClusterInfo if failed to set permissions of cluster info xml file. A status code such as error.create.nodedirectory if failed to create node directory.. A status code such as error.currNode.auth.failed if the current node is not authenticated. A status code such as error.export.util.failed if export util failed. A status code such as error.component.install.failed if component install failed.. A status code such as error.copy.ucplatform.failed if copying uc platform post failed. A status code such as error.delete.oldexportdata if failed to delete the data of the previous data export operation in the SFTP server. A status code such as error.create.rootdir if failed to create root directory. A status code such as error.get.activeVer if failed to fetch the active version. A status code such as error.copy.remoteserver if failed to copy the export data to remote server. A status code such as error.dataExport.start if user selected not to start the data export. A status code such as error.incorrect.format if not in correct format. A status code such as error.delete.sftp if failed to delete the existing cluster folder in the given sftp location. A status code such as error.publisher.export.notfound if publisher's export did not run. A status code such as error.create.exportDirectory if failed to create dataexport directory.. A status code such as error.dynamic.export.failed if dynamic data export failed. |
| remoteMessages | see Response RemoteMessages |

| Parameter | Description |
|---|---|
| result | A result code such as data.export.succeeded that describes the result. See
                        Error Codes in the Developer Guide for details. |
| m2DataExportStatus | A status code such as error.undetermined.result indicating, if possible, the
                       			 result of the dataExport. A status code such as error.invalid.cmd.args if invalid command line args detected.. A status code such as error.multiple.instance.notallowed if multiple concurrent instance of this program is forbidden. A status code such as error.create.pid if failed to create PID file. A status code such as error.remove.pid if failed to remove the PID file. A status code such as error.acquireLock if failed to acquire the LOCK file. A status code such as error.releaseLock if failed to remove the LOCK file. A status code such as error.require.abosulte.sftpPath if SFTP directory path is not an absolute path. A status code such as error.sftp.not.reachable if server failed validation or is unreachable. A status code such as error.invalid.sftp.password if SFTP password provided is null. A status code such as error.createClusterInfo if failed to create the cluster info xml file. A status code such as error.setPermissions.ClusterInfo if failed to set permissions of cluster info xml file. A status code such as error.create.nodedirectory if failed to create node directory.. A status code such as error.currNode.auth.failed if the current node is not authenticated. A status code such as error.export.util.failed if export util failed. A status code such as error.component.install.failed if component install failed.. A status code such as error.copy.ucplatform.failed if copying uc platform post failed. A status code such as error.delete.oldexportdata if failed to delete the data of the previous data export operation in the SFTP server. A status code such as error.create.rootdir if failed to create root directory. A status code such as error.get.activeVer if failed to fetch the active version. A status code such as error.copy.remoteserver if failed to copy the export data to remote server. A status code such as error.dataExport.start if user selected not to start the data export. A status code such as error.incorrect.format if not in correct format. A status code such as error.delete.sftp if failed to delete the existing cluster folder in the given sftp location. A status code such as error.publisher.export.notfound if publisher's export did not run. A status code such as error.create.exportDirectory if failed to create dataexport directory.. A status code such as error.dynamic.export.failed if dynamic data export failed. |

| Parameter | Description |
|---|---|
| result | A result code such as data.export.terminated that describes the result. See
                        Error Codes in the Developer Guide for details. |
| dataExportCancel | A status code such as error.undetermined.result if there is undetermined result. A status code such as data.export.termination.not.required if DataExport not running and nothing to cancel. A status code such as dynamic.export.inProgress.cannotCancel if Dynamic DataExport in progress and it cannot be cancelled. A status code such as export.termination.failed if failed to cancel the M2DataExportcancelService. |

| Parameter | Description |
|---|---|
| result | A result code such as internal.request.complete that describes the result. See
                        Error Codes in the Developer Guide for details. |
| spaceCalculation | A status code such as error.soap.internal if there is undetermined result. |