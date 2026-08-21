---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-85923d6f03
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_version-api_1501.html
retrieved_at: 2026-08-21T16:49:02.644388+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Version API

## Chapter: Version API

- Version API

- Version                              	 API

# Version API

## Version
                        	 API

The Version API is
                           		used to get the Unified Contact Center Enterprise version information from the
                           		system.

### URL

### Parameters

ucceVersion:
                                    				Information about the UCCE version installed on the system, including
                                    				maintenance releases, engineering specials, and the schema version.

### Operations

- get :
                                 			 Returns UCCE version information using the URL https://<server>/unifiedconfig/config/version .

### Example Get
                              		  Response

```
<versionInfo>
    <ucceVersion>
        <majorVersion>11</majorVersion>
        <minorVersion>0</minorVersion>
        <maintenanceVersion>1</maintenanceVersion>
        <srVersion>0</srVersion>
        <esVersion>0</esVersion>
        <buildVersion>3086</buildVersion>
        <versionString>11.0.1.0.0.3086</versionString>
        <schemaVersion>
            <major>181</major>
            <ccMinor>3</ccMinor>
            <awMinor>3</awMinor>
            <cceMinor>0</cceMinor>
        </schemaVersion>
    </ucceVersion>
</versionInfo>
```