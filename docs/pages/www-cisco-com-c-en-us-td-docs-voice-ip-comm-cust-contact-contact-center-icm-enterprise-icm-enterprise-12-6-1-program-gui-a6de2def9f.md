---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-program-gui-a6de2def9f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/program/guide/ucce_b_cisco-ucce_developer_guide-12_6_1/ucce_b_cisco-ucce_developer_guide-12_6_1_chapter_010000.html
retrieved_at: 2026-08-16T20:22:36.792401+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

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
    <registrationStatus>Registered</registrationStatus> <dataGenerationEnabled>
        <changeStamp>310</changeStamp>
        <analyserIntegrated>true</analyserIntegrated>
    </dataGenerationEnabled>
    <dataSource>
        <sideA>
            <address>
                <refURL>/unifiedconfig/config/machineinventory/9939</refURL>
                <name>ABC</name>
            </address>
            <userName>Cisco</userName>
            <password>Cisco</password>
        </sideA>
        <sideB>
            <address>
                <refURL>/unifiedconfig/config/machineinventory/9940</refURL>
                <name>XYZ</name>
            </address>
            <userName>Cisco123</userName>
            <password>Cisco</password>
        </sideB>
    </dataSource> <proxyAddress>http://10.10.10.10:80</proxyAddress> <streamerEnabled>true</streamerEnabled> <deploymentID>9de8bdfe-d513-4ab9-a021-2b729efa9c63</deploymentID>
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
    <registrationStatus>Registered</registrationStatus> <dataGenerationEnabled>
        <changeStamp>310</changeStamp>
        <analyserIntegrated>true</analyserIntegrated>
    </dataGenerationEnabled>
    <dataSource>
        <sideA>
            <address>
                <refURL>/unifiedconfig/config/machineinventory/9939</refURL>
                <name>ABC</name>
            </address>
            <userName>Cisco</userName>
        </sideA>
        <sideB>
            <address>
                <refURL>/unifiedconfig/config/machineinventory/9940</refURL>
                <name>XYZ</name>
            </address>
            <userName>Cisco123</userName>
        </sideB>
    </dataSource> <proxyAddress>http://10.10.10.10:80</proxyAddress> <streamerEnabled>true</streamerEnabled> <deploymentID>9de8bdfe-d513-4ab9-a021-2b729efa9c63</deploymentID>
    <deploymentName>CloudConnectSettings</deploymentName>
    <changeStamp>6</changeStamp>
</CloudConnectSettings>
```