---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-configurationguid-ab56a52d15
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/ConfigurationGuideCVP12_6/guide/ccvp_b_1261-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp_m_1252-unified-cm-sme-configuration.html
retrieved_at: 2026-08-21T06:53:13.433615+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: June 11, 2024

Chapter: Unified CM SME Configuration

## Chapter: Unified CM SME Configuration

# Unified CM SME Configuration

## Enable Session
                        	 Refresh

Periodic session refresh helps to determine the downlink status and
                              		  to trigger clear sessions from the gateway to release Unified CVP call server
                              		  ports in case of Unified CM SME failures.

Perform the following steps to enable SIP session refresh globally.

Step 1

Use putty or telnet to log
                                       			 in to the IOS gateway.

Step 2

From the command prompt, run the following command:

```
>enable
>configure terminal 
>voice service voip 
>sip 
>session refresh
```

## Enable Session
                        	 Timer

To enable SIP
                              		  session timer globally, set the min-se command in SIP configuration mode using the
                              		  following steps.

Step 1

Use putty or
                                       			 telnet to log in to the IOS gateway.

Step 2

From the
                                       			 command prompt, run the following command:

```
>enable 
>configure terminal 
>voice service voip
>sip 
>min-se <seconds> session-expires <seconds>
```

Step 3

Check the
                                       			 min-se set value by typing the following command: show sip-ua min-se .

## Configure Media
                        	 Inactivity Timer in Cisco IOS Gateway

During Unified SME
                              		  failure, the IOS(Cisco UBE or PSTN Gateway) does not receive a BYE message for
                              		  any type of call flow. To avoid this scenario, you must use the following
                              		  procedure to configure Media Inactivity Timer in the IOS Gateway.

Step 1

Use Putty or
                                       			 Telnet to log in to the IOS gateway.

Step 2

From the
                                       			 command prompt, run the following command:

```
ip rtcp report interval <timer_value in msecs>
gateway
media-inactivity-criteria all
 timer receive-rtcp <timer_value in secs>
 timer receive-rtp <timer_value in secs>
```

## Configure SIP
                        	 Trunk from SME to Unified CM Leaf Cluster

For more information about configuring SIP trunk from SME to Unified
                              		  CM Leaf Cluster, see Cisco Collaboration System Solution Reference Network Designs
                                 			 (SRND) available at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/design/guides/UCgoList.html .

## Configure SIP
                        	 Trunk from Unified CM Leaf Cluster to SME

For more information about configuring SIP trunk from Unified CM Leaf
                              		  Cluster to SME, see Cisco Collaboration System Solution Reference Network Designs
                                 			 (SRND) available at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/design/guides/UCgoList.html .

| Step 1 | Use putty or telnet to log
                                       			 in to the IOS gateway. |
|---|---|
| Step 2 | From the command prompt, run the following command: >enable
>configure terminal 
>voice service voip 
>sip 
>session refresh |

| Step 1 | Use putty or
                                       			 telnet to log in to the IOS gateway. |
|---|---|
| Step 2 | From the
                                       			 command prompt, run the following command: >enable 
>configure terminal 
>voice service voip
>sip 
>min-se <seconds> session-expires <seconds> |
| Step 3 | Check the
                                       			 min-se set value by typing the following command: show sip-ua min-se . |

| Step 1 | Use Putty or
                                       			 Telnet to log in to the IOS gateway. |
|---|---|
| Step 2 | From the
                                       			 command prompt, run the following command: ip rtcp report interval <timer_value in msecs>
gateway
media-inactivity-criteria all
 timer receive-rtcp <timer_value in secs>
 timer receive-rtp <timer_value in secs> |