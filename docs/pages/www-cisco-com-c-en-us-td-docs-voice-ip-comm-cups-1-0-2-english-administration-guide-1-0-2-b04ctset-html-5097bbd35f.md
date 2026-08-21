---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b04ctset-html-5097bbd35f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b04ctset.html
retrieved_at: 2026-08-21T16:13:00.919597+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: CTI Gateway Settings

## Chapter: CTI Gateway Settings

- Configuring CTI Gateway Settings

- Related Topics

## CTI Gateway Settings

Use Computer Telephony Interface (CTI) gateway settings to configure the settings that apply to the CTI gateway.

## Configuring CTI Gateway Settings

Follow this procedure to configure the CTI gateway settings.

Step 1 Choose Application > CTI Gateway > Settings .

The CTI Gateway Settings window displays.

Step 2 Enter the appropriate settings as described in Table 34-1 .

Step 3 To save the data, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Table 34-1 IP Phone Messenger Configuration Settings

Application Status

From the drop-down list, choose On or Off to turn the CTI gateway application on or off.

Application Username

This parameter specifies the CTI gateway application user name.

Note This user name must match the application user name that you configured on the Cisco Unified CallManager cluster.

Application Password

This parameter specifies the CTI gateway application password.

Note This password must match the application password that you configured on the Cisco Unified CallManager cluster.

CTI Address

This parameter specifies the IP address or fully qualified domain name of the CTI gateway.

CTI Address (Failover)

This parameter specifies the IP address or fully qualified domain name of the failover CTI gateway.

Note Ensure the failover CTI address is not the same as the primary CTI address.

Heartbeat Interval (seconds)

This parameter specifes the heartbeat interval in seconds.

Range: 5-20 seconds

Default: 8 seconds

Session Timer (seconds)

This parameter specifies the value of the session time in seconds.

Range: 1810-2000 seconds

Default: 1810 seconds

## Related Topics

Configuring CTI Gateway Settings

| Field | Description |
|---|---|
| Application Status | From the drop-down list, choose On or Off to turn the CTI gateway application on or off. |
| Application Username | This parameter specifies the CTI gateway application user name. Note This user name must match the application user name that you configured on the Cisco Unified CallManager cluster. |
| Application Password | This parameter specifies the CTI gateway application password. Note This password must match the application password that you configured on the Cisco Unified CallManager cluster. |
| CTI Address | This parameter specifies the IP address or fully qualified domain name of the CTI gateway. |
| CTI Address (Failover) | This parameter specifies the IP address or fully qualified domain name of the failover CTI gateway. Note Ensure the failover CTI address is not the same as the primary CTI address. |
| Heartbeat Interval (seconds) | This parameter specifes the heartbeat interval in seconds. Range: 5-20 seconds Default: 8 seconds |
| Session Timer (seconds) | This parameter specifies the value of the session time in seconds. Range: 1810-2000 seconds Default: 1810 seconds |