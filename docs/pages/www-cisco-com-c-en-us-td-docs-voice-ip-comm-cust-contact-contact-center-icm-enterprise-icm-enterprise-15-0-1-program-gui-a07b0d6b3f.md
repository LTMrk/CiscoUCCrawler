---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-a07b0d6b3f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_inventory-auto-discovery-api_1501.html
retrieved_at: 2026-08-21T16:47:09.048855+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Inventory Auto Discovery API

## Chapter: Inventory Auto Discovery API

- Inventory Auto Discovery API

- Inventory Auto Discovery API

# Inventory Auto Discovery API

## Inventory Auto Discovery API

Use the Inventory Auto Discovery API to set and retrieve the status of auto discovery.

### Operations

create : Sets the status of auto discovery, using the URL:

https://<server>:<serverport>/unifiedconfig/config/systemmgmt/inventoryautodiscovery

get : Returns the status of auto discovery in the inventory, using the URL:

https://<server>:<serverport>/unifiedconfig/config/systemmgmt/inventoryautodiscovery

### Response Parameters for get

disabled : Indicates the status of auto discovery. Values are True or False .

### Payload for Create

disabled : The status of auto discovery. You must disable auto discovery in the virtual machine before updating the IP address or hostname
                              and enable it once the inventory update is complete. During Technology Refresh upgrade, auto discovery is disabled by default
                              till upgrade completion. Supported values are:

True : set this value to disable auto discovery.

False : set this value to enable auto discovery.

If you do not enable auto discovery, it gets enabled automatically after three days of disabling.

| Note | If you do not enable auto discovery, it gets enabled automatically after three days of disabling. |
|---|---|