---
doc_id: developer-cisco-com-docs-contact-center-express-configuration-information-masks-56a4a71528
source_url: https://developer.cisco.com/docs/contact-center-express/configuration-information-masks/
retrieved_at: 2026-09-07T14:05:31.781307+00:00
---

# Configuration-Information Masks

The Configuration-Information masks specify the
		  configuration event messages that the client requests.

Mask name

Description

Value

CONFIG_AGENT_MASK

Set when the client wishes to receive agent configuration update messages.

0x00000001

CONFIG_CSQ_MASK

Set when the client wishes to receive skill group configuration update messages.

0x00000002

CONFIG_APPLICATION_MASK

Set when the client wishes to receive service configuration update messages.

0x00000004

CONFIG_DEVICE_MASK

Set when the client wishes to receive device configuration update messages.

0x00000008

CONFIG_TERMINAL_MASK

(Version 18 and later)

Set when the client wishes to receive terminal configuration update messages.

0x00000010

| Mask name | Description | Value |
|---|---|---|
| CONFIG_AGENT_MASK | Set when the client wishes to receive agent configuration update messages. | 0x00000001 |
| CONFIG_CSQ_MASK | Set when the client wishes to receive skill group configuration update messages. | 0x00000002 |
| CONFIG_APPLICATION_MASK | Set when the client wishes to receive service configuration update messages. | 0x00000004 |
| CONFIG_DEVICE_MASK | Set when the client wishes to receive device configuration update messages. | 0x00000008 |
| CONFIG_TERMINAL_MASK (Version 18 and later) | Set when the client wishes to receive terminal configuration update messages. | 0x00000010 |