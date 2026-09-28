---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-5cee3d4c13
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce_m_internet-script-editor-api_1501.html
retrieved_at: 2026-08-16T20:18:07.291303+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

Chapter: Internet Script Editor API

## Chapter: Internet Script Editor API

- Internet Script Editor API

- Internet Script Editor API

# Internet Script Editor API

## Internet Script Editor API

The Internet Script Editor API indicates whether Internet Script Editor is enabled. If Internet Script Editor is enabled in
                           Web Setup, the API displays the download link in the format https://<server>/install/iScriptEditor.exe.

### URL

### Operations

get :
                                    				Returns whether Internet Script Editor is enabled and a download link.

### Parameters

enabled: Indicates whether Internet Script Editor is enabled in Web Setup. True or false.

downloadLink: The download link for Internet Script Editor. This link appears only when the enabled parameter is true.

### Example Get Response

```
<internetScriptEditor>
    <enabled>true</enabled>
    <downloadLink>https://10.10.10.207/install/iScriptEditor.exe</downloadLink>
</internetScriptEditor>
```