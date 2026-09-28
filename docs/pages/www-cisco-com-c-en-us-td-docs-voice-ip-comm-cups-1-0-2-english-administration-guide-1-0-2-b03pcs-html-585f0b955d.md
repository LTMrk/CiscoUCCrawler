---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b03pcs-html-585f0b955d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b03pcs.html
retrieved_at: 2026-08-21T16:11:11.802209+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Proxy Server Settings

## Chapter: Proxy Server Settings

## Proxy Server Settings

Use proxy server settings to configure settings for the SIP proxy server.

## Configuring Proxy Server Settings

This section describes how to configure proxy server settings for the Cisco Unified Presence Server.

Step 1 Choose Unified Presence Server > Proxy Server > Settings .

The Proxy Configuration Settings window displays.

Step 2 For the Method/Event Routing Status, choose On or Off .

Step 3 Choose the appropriate Preferred Proxy Listener, as described in Table 8-1 .

Step 4 To save your settings, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## Proxy Server Configuration Settings

Table 8-1 describes the proxy server configuration settings. For related procedures, see the "Related Topics" section .

Table 8-1 Proxy Server Configuration Settings

Method/Event Routing Status

This parameter specifies whether the method/event routing module is enabled or disabled in the SIP proxy server.

Preferred Proxy Listener

This parameter specifies which SIP proxy listener is considered the preferred listener. The dropdown list contains SIP proxy server listeners that you defined in the Transport Listeners window.

## Restart Proxy Services

Some changes you make in Cisco Unified Presence Server Administration require that you restart SIP proxy services before the change takes effect. Changes that require you to restart SIP proxy services include:

• Adding, deleting, or modifying the system server

• Modifying the SIP proxy server settings

• Adding, deleting, or modifying transport listeners

• Adding, deleting, or modifying TLS context and TLS peer subjects

To restart proxy services, use the following procedure:

Warning While the proxy services are restarting, the Cisco Enterprise SIP proxy services drop any existing transactions and do not accept any new requests.

Step 1 Choose Unified Presence Server > Proxy Server > Settings .

The Proxy Configuration Settings window displays.

Step 2 Click Restart All Proxy Services .

Step 3 When the confirmation window displays, click OK .

## Related Topics

• Configuring Proxy Server Settings

• Proxy Server Configuration Settings

| Field | Description |
|---|---|
| Method/Event Routing Status | This parameter specifies whether the method/event routing module is enabled or disabled in the SIP proxy server. |
| Preferred Proxy Listener | This parameter specifies which SIP proxy listener is considered the preferred listener. The dropdown list contains SIP proxy server listeners that you defined in the Transport Listeners window. |