---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-program-gui-422580dd0a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/program/guide/ucce_b_cisco-ucce_developer_guide-12_6_1/ucce_b_cisco-ucce_developer_guide-12_6_1_chapter_010101.html
retrieved_at: 2026-08-16T20:23:02.575812+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

Updated: August 21, 2023

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