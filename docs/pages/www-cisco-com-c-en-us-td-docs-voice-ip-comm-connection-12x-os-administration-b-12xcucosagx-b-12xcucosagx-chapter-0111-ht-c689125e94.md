---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-os-administration-b-12xcucosagx-b-12xcucosagx-chapter-0111-ht-c689125e94
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/os_administration/b_12xcucosagx/b_12xcucosagx_chapter_0111.html
retrieved_at: 2026-08-17T03:40:09.346793+00:00
---

Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 12.x

# Cisco Unified Communications Operating System Administration Guide for Cisco Unity Connection Release 12.x

Updated: August 7, 2017

Chapter: Services

## Chapter: Services

# Services

## Services

### Overview

This chapter describes the utility functions that are available on the operating system, which include pinging another system
                              and setting up remote support.

### Ping

The Ping Utility window enables you to ping another server in
                                 		  the network.

To ping another system, follow this procedure:

From the Cisco Unified Communications Operating System
                                          			 Administration window, navigate to Services > Ping .

The Ping Remote window displays.

Enter the IP address or network name for the system that you
                                          			 want to ping.

Enter the ping interval in seconds.

Enter the packet size.

Enter the ping count, the number of times that you want to ping
                                          			 the system.

When you specify multiple pings, the ping command does not
                                                         				  display the ping date and time in real time. Be aware that the Ping command
                                                         				  displays the data after the number of pings that you specified completes.

Select whether you want to validate IPSec.

Click Ping .

The Ping Remote window displays the ping statistics.

### Setting Up Remote
                           	 Support

From the Remote Account Support window, you can set up a remote
                                 		  account that Cisco support personnel can use to access the system for a
                                 		  specified time.

The remote support process works like this:

The customer sets up a remote support account. This account
                                          			 includes a time limit on how long Cisco personnel can access it. This time
                                          			 limit can be configured to various values.

When the remote support account is set up, a pass phrase gets
                                          			 generated.

The customer calls Cisco support and provides the remote support
                                          			 account name and pass phrase.

Cisco support enters the pass phrase into a decoder program that
                                          			 generates a password from the pass phrase.

Cisco support logs into the remote support account on the
                                          			 customer system with the decoded password.

When the account time limit expires, Cisco support can no longer
                                          			 access the remote support account.

To set up remote support, follow this procedure:

From the Cisco Unified Communications Operating System
                                          			 Administration window, navigate to Services > Remote
                                                				  Support .

The Remote Access Configuration window displays.

Enter an account name for the remote account in the Account Name field.

The account name must comprise at least six-characters that are
                                             				all lowercase, alphabetic characters.

Enter the account duration, in days, in the Account Duration field.

The default account duration specifies 30 days.

Click Save .

The Remote Support Status window displays. For descriptions of
                                             				fields on the Remote Support Status window, see Table 8-1 .

To access the system with the generated pass phrase, contact
                                          			 your Cisco personnel.

To delete the remote access support account, click the Delete button.

Field

Description

Decode version

Indicates the version of the decoder in use.

Account name

Displays the name of the remote support account.

Expiration

Displays the date and time when access to the remote account
                                                         						  expires.

Pass phrase

Displays the generated pass phrase.

| Step 1 | From the Cisco Unified Communications Operating System
                                          			 Administration window, navigate to Services > Ping . The Ping Remote window displays. |
|---|---|
| Step 2 | Enter the IP address or network name for the system that you
                                          			 want to ping. |
| Step 3 | Enter the ping interval in seconds. |
| Step 4 | Enter the packet size. |
| Step 5 | Enter the ping count, the number of times that you want to ping
                                          			 the system. Note When you specify multiple pings, the ping command does not
                                                         				  display the ping date and time in real time. Be aware that the Ping command
                                                         				  displays the data after the number of pings that you specified completes. | Note | When you specify multiple pings, the ping command does not
                                                         				  display the ping date and time in real time. Be aware that the Ping command
                                                         				  displays the data after the number of pings that you specified completes. |
| Note | When you specify multiple pings, the ping command does not
                                                         				  display the ping date and time in real time. Be aware that the Ping command
                                                         				  displays the data after the number of pings that you specified completes. |
| Step 6 | Select whether you want to validate IPSec. |
| Step 7 | Click Ping . The Ping Remote window displays the ping statistics. |

| Note | When you specify multiple pings, the ping command does not
                                                         				  display the ping date and time in real time. Be aware that the Ping command
                                                         				  displays the data after the number of pings that you specified completes. |
|---|---|

| Step 1 | The customer sets up a remote support account. This account
                                          			 includes a time limit on how long Cisco personnel can access it. This time
                                          			 limit can be configured to various values. |
|---|---|
| Step 2 | When the remote support account is set up, a pass phrase gets
                                          			 generated. |
| Step 3 | The customer calls Cisco support and provides the remote support
                                          			 account name and pass phrase. |
| Step 4 | Cisco support enters the pass phrase into a decoder program that
                                          			 generates a password from the pass phrase. |
| Step 5 | Cisco support logs into the remote support account on the
                                          			 customer system with the decoded password. |
| Step 6 | When the account time limit expires, Cisco support can no longer
                                          			 access the remote support account. To set up remote support, follow this procedure: |
| Step 7 | From the Cisco Unified Communications Operating System
                                          			 Administration window, navigate to Services > Remote
                                                				  Support . The Remote Access Configuration window displays. |
| Step 8 | Enter an account name for the remote account in the Account Name field. The account name must comprise at least six-characters that are
                                             				all lowercase, alphabetic characters. |
| Step 9 | Enter the account duration, in days, in the Account Duration field. The default account duration specifies 30 days. |
| Step 10 | Click Save . The Remote Support Status window displays. For descriptions of
                                             				fields on the Remote Support Status window, see Table 8-1 . |
| Step 11 | To access the system with the generated pass phrase, contact
                                          			 your Cisco personnel. |
| Step 12 | To delete the remote access support account, click the Delete button. Table 1. Remote Support Status Fields and
                                                      				  Descriptions Field Description Decode version Indicates the version of the decoder in use. Account name Displays the name of the remote support account. Expiration Displays the date and time when access to the remote account
                                                         						  expires. Pass phrase Displays the generated pass phrase. | Field | Description | Decode version | Indicates the version of the decoder in use. | Account name | Displays the name of the remote support account. | Expiration | Displays the date and time when access to the remote account
                                                         						  expires. | Pass phrase | Displays the generated pass phrase. |
| Field | Description |
| Decode version | Indicates the version of the decoder in use. |
| Account name | Displays the name of the remote support account. |
| Expiration | Displays the date and time when access to the remote account
                                                         						  expires. |
| Pass phrase | Displays the generated pass phrase. |

| Field | Description |
|---|---|
| Decode version | Indicates the version of the decoder in use. |
| Account name | Displays the name of the remote support account. |
| Expiration | Displays the date and time when access to the remote account
                                                         						  expires. |
| Pass phrase | Displays the generated pass phrase. |