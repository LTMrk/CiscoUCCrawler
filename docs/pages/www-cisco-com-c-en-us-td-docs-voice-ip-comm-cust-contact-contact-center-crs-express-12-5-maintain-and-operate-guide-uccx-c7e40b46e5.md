---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-maintain-and-operate-guide-uccx-c7e40b46e5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/maintain_and_operate/guide/uccx_b_unified-ccx-operating-system-1251su3/uccx_m_1251su3_utility-functions.html
retrieved_at: 2026-08-16T21:30:48.008466+00:00
---

Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR, Release 12.5(1) SU3

# Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR, Release 12.5(1) SU3

Updated: July 10, 2023

Chapter: Utility Functions

## Chapter: Utility Functions

- Utility Functions

- Ping

- Remote Account                              	 Support

# Utility Functions

This chapter describes the utility functions that are available
                        		on the operating system: pinging another system and setting up
                        		remote support.

## Ping

Use the Ping Utility window to ping another
                              		  server in the network.

To ping another system, follow this procedure:

Step 1

From the Cisco Unified Operating System Administration window, navigate to Services > Ping .

Step 2

Enter the IP address or network name for the system that you want
                                       			 to ping.

Step 3

Enter the ping interval in seconds.

Step 4

Enter the packet size.

Step 5

Enter the ping count (the number of times that you want to ping
                                       			 the system).

When you specify multiple pings, the ping command does not
                                                      				  display the ping date and time immediately. Be aware that the Ping command
                                                      				  displays the data after it completes the number of pings that you specified.

Step 6

Choose whether you want to validate IPSec.

Step 7

Click Ping .

The Ping Remote window displays the ping
                                          				statistics.

## Remote Account
                        	 Support

From the Remote
                                 			 Access Configuration window, you can set up a remote account that
                              		  Cisco support personnel can use to access the system for a specified time.

- The customer sets up a remote
                                    			 support account. This account includes a time limit on how long Cisco personnel
                                    			 can access it. This time limit can be configured to various values.

- When the remote support
                                    			 account is set up, a pass phrase gets generated.

- The customer calls Cisco
                                    			 support and provides the remote support account name and pass phrase.

- Cisco support enters the pass
                                    			 phrase into a decoder program that generates a password from the pass phrase.

- Cisco support logs into the
                                    			 remote support account on the customer system by using the decoded password.

- When the account time limit
                                    			 expires, Cisco support can no longer access the remote support account.

To set up remote
                              		  support, follow this procedure:

Step 1

From the Cisco Unified Operating System Administration window, navigate to Services > Remote Support .

Step 2

Enter an account
                                       			 name for the remote account in the Account
                                          				Name field.

The account name
                                          				must comprise at least six-characters that are all lowercase, alphabetic
                                          				characters.

Caution

Avoid creating remote account
                                                      				  names starting with "uccx" or "UCCX" because such user names may conflict with system account names used internally
                                                      				  within Unified CCX server.

Step 3

Enter the
                                       			 account duration, in days, in the Account
                                          				Duration field.

The default
                                          				account duration specifies 30 days.

Step 4

Click Save .

Step 5

To access the
                                       			 system by using the generated pass phrase, contact your Cisco personnel.

Step 6

To delete the
                                       			 remote access support account, click Delete .

| Step 1 | From the Cisco Unified Operating System Administration window, navigate to Services > Ping . The Ping Remote window appears. |
|---|---|
| Step 2 | Enter the IP address or network name for the system that you want
                                       			 to ping. |
| Step 3 | Enter the ping interval in seconds. |
| Step 4 | Enter the packet size. |
| Step 5 | Enter the ping count (the number of times that you want to ping
                                       			 the system). Note When you specify multiple pings, the ping command does not
                                                      				  display the ping date and time immediately. Be aware that the Ping command
                                                      				  displays the data after it completes the number of pings that you specified. | Note | When you specify multiple pings, the ping command does not
                                                      				  display the ping date and time immediately. Be aware that the Ping command
                                                      				  displays the data after it completes the number of pings that you specified. |
| Note | When you specify multiple pings, the ping command does not
                                                      				  display the ping date and time immediately. Be aware that the Ping command
                                                      				  displays the data after it completes the number of pings that you specified. |
| Step 6 | Choose whether you want to validate IPSec. |
| Step 7 | Click Ping . The Ping Remote window displays the ping
                                          				statistics. |

| Note | When you specify multiple pings, the ping command does not
                                                      				  display the ping date and time immediately. Be aware that the Ping command
                                                      				  displays the data after it completes the number of pings that you specified. |
|---|---|

| Step 1 | From the Cisco Unified Operating System Administration window, navigate to Services > Remote Support . The Remote Access Configuration window appears. |
|---|---|
| Step 2 | Enter an account
                                       			 name for the remote account in the Account
                                          				Name field. The account name
                                          				must comprise at least six-characters that are all lowercase, alphabetic
                                          				characters. Caution Avoid creating remote account
                                                      				  names starting with "uccx" or "UCCX" because such user names may conflict with system account names used internally
                                                      				  within Unified CCX server. | Caution | Avoid creating remote account
                                                      				  names starting with "uccx" or "UCCX" because such user names may conflict with system account names used internally
                                                      				  within Unified CCX server. |
| Caution | Avoid creating remote account
                                                      				  names starting with "uccx" or "UCCX" because such user names may conflict with system account names used internally
                                                      				  within Unified CCX server. |
| Step 3 | Enter the
                                       			 account duration, in days, in the Account
                                          				Duration field. The default
                                          				account duration specifies 30 days. |
| Step 4 | Click Save . The fields in
                                          				the following table appears in the Remote Access Account Information area: Table 1. Remote
                                                   				Access Account Information Fields and Descriptions Field Description Account name Displays the name of the remote support account. Expiration Displays the date and time when access to the remote account
                                                      						expires. Passphrase Displays the generated pass phrase. Decode version Indicates the version of the decoder in use. | Field | Description | Account name | Displays the name of the remote support account. | Expiration | Displays the date and time when access to the remote account
                                                      						expires. | Passphrase | Displays the generated pass phrase. | Decode version | Indicates the version of the decoder in use. |
| Field | Description |
| Account name | Displays the name of the remote support account. |
| Expiration | Displays the date and time when access to the remote account
                                                      						expires. |
| Passphrase | Displays the generated pass phrase. |
| Decode version | Indicates the version of the decoder in use. |
| Step 5 | To access the
                                       			 system by using the generated pass phrase, contact your Cisco personnel. |
| Step 6 | To delete the
                                       			 remote access support account, click Delete . |

| Caution | Avoid creating remote account
                                                      				  names starting with "uccx" or "UCCX" because such user names may conflict with system account names used internally
                                                      				  within Unified CCX server. |
|---|---|

| Field | Description |
|---|---|
| Account name | Displays the name of the remote support account. |
| Expiration | Displays the date and time when access to the remote account
                                                      						expires. |
| Passphrase | Displays the generated pass phrase. |
| Decode version | Indicates the version of the decoder in use. |