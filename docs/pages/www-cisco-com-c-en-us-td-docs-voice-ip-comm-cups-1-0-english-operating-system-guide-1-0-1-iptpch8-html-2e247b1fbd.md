---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-english-operating-system-guide-1-0-1-iptpch8-html-2e247b1fbd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0/english/operating_system/guide/1_0_1/iptpch8.html
retrieved_at: 2026-08-21T02:47:23.754523+00:00
---

Cisco Unified Communications Operating System Administration Guide, Release 1.0(1)

# Cisco Unified Communications Operating System Administration Guide, Release 1.0(1)

Updated: July 17, 2006

Chapter: Services

## Chapter: Services

- Ping

- Remote Support

## Services

This chapter describes the utility functions that are available on the operating system, which include pinging another system and setting up remote support.

## Ping

The Ping Utility window enables you to ping another server in the network.

To ping another system, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Services>Ping .

The Ping Remote window displays.

Step 2 Enter the IP address or network name for the system that you want to ping.

Step 3 Enter the ping interval in seconds.

Step 4 Enter the packet size.

Step 5 Enter the ping count, the number of times that you want to ping the system.

Note When you specify multiple pings, the ping command does not display the ping date and time in real time. Be aware that the Ping command displays the data after the number of pings that you specified complete.

Step 6 Choose whether you want to validate IPSec.

Step 7 Click Ping .

The Ping Remote window displays the ping statistics.

## Remote Support

From the Remote Account Support window, you can set up a remote account that Cisco support personnel can use to access the system for a specified period of time.

The remote support process works like this:

1. The customer sets up a remote support account. This account includes a configurable time limit on how long Cisco personnel can access it.

2. When the remote support account is set up, a pass phrase gets generated.

3. The customer calls Cisco support and provides the remote support account name and pass phrase.

4. Cisco support enters the pass phrase into a decoder program that generates a password from the pass phrase.

5. Cisco support logs into the remote support account on the customer system by using the decoded password.

6. When the account time limit expires, Cisco support can no longer access the remote support account.

To set up remote support, follow this procedure:

Step 1 From the Cisco Unified Communications Operating System Administration window, navigate to Services>Remote Support .

The Remote Support Window displays.

Step 2 If no remote support account is configured, click Add .

Step 3 Enter an account name for the remote account and the account life in days.

Note The account name must be at least six-characters long and all lowercase, alphabetic characters.

Step 4 Click Save .

The Remote Support Status window displays. For descriptions of fields on the Remote Support Status window, see Table 8-1 .

Step 5 To access the system by using the generated pass phrase, contact your Cisco personnel.

Table 8-1 Remote Support Status Fields and Descriptions

Decoder version

Indicates the version of the decoder in use.

Account name

Displays the name of the remote support account.

Expires

Displays the date and time when access to the remote account expires.

Pass phrase

Displays the generated pass phrase.

| Field | Description |
|---|---|
| Decoder version | Indicates the version of the decoder in use. |
| Account name | Displays the name of the remote support account. |
| Expires | Displays the date and time when access to the remote account expires. |
| Pass phrase | Displays the generated pass phrase. |