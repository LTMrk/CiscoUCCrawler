---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-e73592142f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_cloud-connect-configuration_1501.html
retrieved_at: 2026-08-21T16:45:53.739598+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Cloud Connect Device Configuration

## Chapter: Cloud Connect Device Configuration

- Cloud Connect Device Configuration

- Cloud Connect Configuration

# Cloud Connect Device Configuration

## Cloud Connect Configuration

This is the global API to configure Cloud Connect settings.

### URL

### Operations

Gets the current configuration information from the cloud connect.

Updates the configuration information to cloud connect.

### Parameters

proxyAddress: IP address or hostname of the proxy server that is used by Cloud Connect Publisher.

subscriberProxyAddress: IP address or hostname of the proxy server that is used by Cloud Connect Subscriber.

registrationStatus: Read-only field that displays the Cloud Connect registration status of Control Hub.

publisherHost: A readonly field that returns the hostname of the Cloud Connect Publisher machine.

subscriberHost: A readonly field that returns the hostname of the Cloud Connect Subscriber machine.

lastUpdatedTimestamp: Timestamp of the last successful proxy update operation. The latest value for this field must be supplied
                                    during PUT operation.

warnings: Warnings returned from the unifiedconfig service in response to GET / PUT operations. It may return one or both
                                    of the following warnings:

cce.cdn.cloudConnectNotUpgraded: This warning indicates that the Cloud Connect machines are of an older version that do not
                                          support separate proxy configuration for Publisher and Subscriber. In this case, the contents of subscriberProxyAddress field will be disregarded.

ccmgmtServiceDownErrorMsg: This warning indicates that the configuration service on the Cloud Connect servers are not reachable.
                                          This means that the response returned for the GET operation might be outdated.

### Example Get Response

```
{
    "lastUpdatedTimestamp": 1768335193101,
    "proxyAddress": "http://proxy.example.com:80",
    "registrationStatus": "Registered",
    "subscriberProxyAddress": "http://proxy.example.com:80",
    "publisherHost": "ccPublisher.example.com",
    "subscriberHost": "ccSubscriber.example.com",
    "warnings": ["cce.cdn.cloudConnectNotUpgraded", "ccmgmtServiceDownErrorMsg"]
    }
```