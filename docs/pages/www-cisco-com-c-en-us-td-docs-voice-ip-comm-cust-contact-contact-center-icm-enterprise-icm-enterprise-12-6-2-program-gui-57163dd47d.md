---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-program-gui-57163dd47d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/program/guide/ucce_b_cisco-ucce_developer_guide-12-6-2-/ucce_m_cloud_connect_device_config-12_6_1.html
retrieved_at: 2026-08-16T20:20:14.668791+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

Updated: August 21, 2023

Chapter: Cloud Connect Device Configuration

## Chapter: Cloud Connect Device Configuration

- Cloud Connect Device Configuration

- Cloud Connect Configuration

# Cloud Connect Device Configuration

## Cloud Connect Configuration

This is global API for cloudconnector (same configuration will be applicable for all the cloud connect present in the system).

The Cloud Connect API is applicable for the following deployments only:

Unified CCE 2000 Agents.

PCCE 2000 Agents and

PCCE LabOnly

### URL

### Operations

Gets the configuration information of the cloud connect https://<server>/unifiedconfig/config/cloudconnectsettings

Updates the proxy server and media type mapping to cloud connect. https://<server>/unifiedconfig/config/cloudconnectsettings

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><CloudConnectSettings>
    <registrationStatus>Registered</registrationStatus>
    
    <proxyAddress>http://10.10.10.10:80</proxyAddress>
    
    <deploymentID>9de8bdfe-d513-4ab9-a021-2b729efa9c63</deploymentID>
    <deploymentName>CloudConnectSettings</deploymentName>
    <changeStamp>6</changeStamp>
</CloudConnectSettings>
```

### Parameters

dataGenerationEnabled: Enables data generation for Cloud Connect.

dataSourceAddress: DataSource address for Cloud Connect.

dataSourceUserName: DataSource user name for Cloud Connect.

dataSourcePassword: DataSource password for Cloud Connect.

proxyAddress: Proxy address or hostname for the Cloud Connect to connecct to the Control Hub.

streamerEnabled: Enables the data flow between Cloud Connect and Control Hub.

### Example Get Response

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><CloudConnectSettings>
    <registrationStatus>Registered</registrationStatus>
    
    <proxyAddress>http://10.10.10.10:80</proxyAddress>
    
    <deploymentID>9de8bdfe-d513-4ab9-a021-2b729efa9c63</deploymentID>
    <deploymentName>CloudConnectSettings</deploymentName>
    <changeStamp>6</changeStamp>
</CloudConnectSettings>
```