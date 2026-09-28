---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-configuration-guide-f1d330bc74
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/configuration/guide/ccvp_b_1501-configuration-guide-for-cisco-customer-voice-portal-release/sip_devices_configuration.html
retrieved_at: 2026-08-21T12:06:44.387690+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: December 12, 2025

Chapter: SIP Devices Configuration

## Chapter: SIP Devices Configuration

# SIP Devices Configuration

## Set Up Ingress Gateway to Use Redundant Proxy Servers

```
ip domain name <your domain name>
                                ip name-server <your DNS server>
                                sip-ua
                                sip-server dns:<your SRV cluster domain name>
                                dial-peer voice 1000 voip
                                session target sip-server
```

## Set Up Call Server with Redundant Proxy Servers

See the Operations Console User's Guide for Cisco Unified Customer Voice Portal on how to configure local based SRV records.

## Local SRV File Configuration Example for SIP Messaging Redundancy

## Load-Balancing SIP
                        	 Calls

SIP calls can be
                           		load balanced across destinations in several different ways as outlined below:

Using the CUSP server, define several static routes with the same route pattern, priorities, and weights.

Using DNS,
                                 			 configure SRV records with priorities and weights. Both the DNS client and the
                                 			 server settings must be configured and operating successfully for DNS "A" and
                                 			 "SRV" type queries to work. Configure SRV queries to be used wherever outbound
                                 			 SIP calls are made, such as on the IOS Ingress gateway, on the Call Server
                                 			 itself, and on Unified CM .

## Cisco Unified SIP Proxy ( CUSP ) Configuration

The following configuration shows a CUSP proxy in Unified CVP. The highlighted lines are specific to a Unified CVP solution. For additional configuration details,
                           refer to the Configuring Cisco Unified SIP Proxy Server guide.

Configuration Example:

```
server-group sip global-load-balance call-id
                            server-group sip retry-after 0
                            server-group sip element-retries udp 1
                            server-group sip element-retries tls 1
                            server-group sip element-retries tcp 1
                            sip dns-srv
                            no enable
                            no naptr
                            end dns
                        !
                        no sip header-compaction
                        no sip logging
                        !
                        sip max-forwards 70
                        sip network netA noicmp
                        non-invite-provisional 200
                        allow-connections
                        retransmit-count invite-server-transaction 9
                        retransmit-count non-invite-client-transaction 9
                        retransmit-count invite-client-transaction 2
                        retransmit-timer T4 5000
                        retransmit-timer T2 4000
                        retransmit-timer T1 500
                        retransmit-timer TU2 32000
                        retransmit-timer TU1 5000
                        retransmit-timer clientTn 64000
                        retransmit-timer serverTn 64000
                        end network
                        !
                        no sip peg-counting
                        !
                        sip privacy service
                        sip queue message
                        drop-policy head
                        low-threshold 80
                        size 2000
                        thread-count 20
                        end queue
                        !
                        sip queue radius
                        drop-policy head
                        low-threshold 80
                        size 2000
                        thread-count 20
                        end queue
                        !
                        sip queue request
                        drop-policy head
                        low-threshold 80
                        size 2000
                        thread-count 20
                        end queue
                        !
                        sip queue response
                        drop-policy head
                        low-threshold 80
                        size 2000
                        thread-count 20
                        end queue
                        !
                        sip queue st-callback
                        drop-policy head
                        low-threshold 80
                        size 2000
                        thread-count 10
                        end queue
                        !
                        sip queue timer
                        drop-policy none
                        low-threshold 80
                        size 2500
                        thread-count 8
                        end queue
                        !
                        sip queue xcl
                        drop-policy head
                        low-threshold 80
                        size 2000
                        thread-count 2
                        end queue
                        !
                        route recursion
                        !
                        sip tcp connection-timeout 240
                        sip tcp max-connections 256
                        !
                        no sip tls
                        !
                        trigger condition in-netA
                            sequence 1
                            in-network netA
                            end sequence
                            end trigger condition
                            !
                            trigger condition mid-dialog
                            sequence 1
                            mid-dialog
                            end sequence
                            end trigger condition
                            !
                            trigger condition out-netA
                            sequence 1
                            out-network netA
                            end sequence
                            end trigger condition
                        !
                        accounting
                        no enable
                        no client-side
                        no server-side
                        end accounting
                        !
                        server-group sip group cucm-cluster.cisco.com netA
                         element ip-address 10.86.129.219 5060 udp q-value 1.0 weight 10
                         element ip-address 10.86.129.62 5060 udp q-value 1.0 weight 10
                         element ip-address 10.86.129.63 5060 udp q-value 1.0 weight 10
                         failover-resp-codes 503
                         lbtype global
                         ping
                         end server-group
                         !
                         server-group sip group cvp-call-servers.cisco.com netA
                         element ip-address 10.86.129.220 5060 udp q-value 1.0 weight 10
                         element ip-address 10.86.129.224 5060 udp q-value 0.9 weight 10
                         failover-resp-codes 503
                         lbtype global
                         ping
                         end server-group
                         !
                         server-group sip group vxml-gws.cisco.com netA
                         element ip-address 10.86.129.229 5060 udp q-value 1.0 weight 10
                         element ip-address 10.86.129.228 5060 udp q-value 1.0 weight 10
                         failover-resp-codes 503
                         lbtype global
                         ping
                         end server-group
                         !
                         route table cvp-route-table
                         key 9 target-destination vxml-gws.cisco.com netA
                         key 8 target-destination cvp-call-servers.cisco.com netA
                         key 7 target-destination vxml-gws.cisco.com netA
                         key 700699 target-destination cvp-call-servers.cisco.com netA
                         key 2 target-destination cucm-cluster.cisco.com netA
                         key 1 target-destination cucm-cluster.cisco.com netA
                         key 7000 target-destination 172.19.151.41 netA
                         key 777333 target-destination cvp-call-servers.cisco.com netA
                         key 1004 target-destination 10.86.139.84 netA
                         key 7105 target-destination dialer-gws netA
                         end route table
                         !
                         policy lookup cvp-policy
                         sequence 1 cvp-route-table request-uri uri-component user
                         rule prefix
                         end sequence
                         end policy
                         !
                         trigger routing sequence 1 by-pass condition mid-dialog
                         trigger routing sequence 10 policy cvp-policy condition in-netA
                         !
                         server-group sip ping-options netA 10.86.129.200 5038
                         method OPTIONS
                         ping-type adaptive 5000 10000
                         timeout 500
                         end ping
                         !
                         server-group sip global-ping
                         sip listen netA udp 10.86.129.200 5060
                        !
                        end
```

## Configure Custom Streaming Ringtones

You can configure custom ringtone patterns that enable you to
                              play an audio stream to a caller in place of the usual ringtone. Customized
                              streaming ringtones are based on the dialed number destination and, when
                              configured, play an in-progress broadcast stream to the caller while the call
                              is transferred an agent.

Step 1

Configure Helix for
                                       streaming audio.

The default installation and
                                          configuration of the Helix server is all that is required for use with Unified CVP.
                                          See the Helix Server Administration Guide for
                                          information about installing and configuring the Helix Server.

Step 2

In the Operations Console, perform the following steps to
                                       configure custom streaming ringtones:

Select System > Dialed Number
                                                   Pattern .

Click Add
                                                New .

Complete the following fields
                                             to assoicate a dialed number pattern with a custom ringtone.

Property

Description

Default

Value

General Configuration

Dialed Number Pattern

The actual Dialed Number Pattern.

None

Must be unique

Maximum
                                                            length of 24 characters

Can contain alphanumeric characters, wildcard characters such as exclamation point (!) or asterisk (*), single digit matches
                                                            such as the letter X (not x) or period (.)

Can end with an optional
                                                            greater than (>) wildcard character

Description

Information about the Dialed Number
                                                            Pattern.

None

Maximum
                                                            length of 1024 characters

Enable Custom
                                                               Ringtone

Enables customized ring tone.

Ringtone media filename - Enter the name of the file
                                                                  that is to be played for the respective dialed number pattern. Provide the URL
                                                                  for the stream name in the following format: rtsp://<streaming
                                                                     server IP
                                                                     address>:<port>/<directory>/<filename>.rm

Disabled

none

Maximum
                                                            length of 256 characters

Cannot contain whitespace
                                                            characters

Click Save to save the Dialed Number
                                             Pattern.

You are returned to the Dialed Number
                                                   Pattern page. To deploy the Dialed Number Pattern configuration, click Deploy to deploy the configuration to all Unified CVP Call
                                                Server devices.

Step 3

Add a Send to
                                       VRU node in your ICM script before any Queue node.

The
                                          explicit Send to VRU node is used to establish the VRU leg before the transfer
                                          to the agent; this is required to play streaming audio ringtones to a
                                          caller.

| Note | Refer to DNS Zone File Configuration for Comprehensive Call Flow Model for information
                                    		about load balancing and failover without a Proxy Server. Only the DNS SRV
                                    		method is supported for load balancing and failover without a Proxy Server. |
|---|---|

| Step 1 | Configure Helix for
                                       streaming audio. The default installation and
                                          configuration of the Helix server is all that is required for use with Unified CVP.
                                          See the Helix Server Administration Guide for
                                          information about installing and configuring the Helix Server. |
|---|---|
| Step 2 | In the Operations Console, perform the following steps to
                                       configure custom streaming ringtones: Select System > Dialed Number
                                                   Pattern . Click Add
                                                New . Complete the following fields
                                             to assoicate a dialed number pattern with a custom ringtone. Table 1. Dialed Number Pattern Configuration Settings Property Description Default Value General Configuration Dialed Number Pattern The actual Dialed Number Pattern. None Must be unique Maximum
                                                            length of 24 characters Can contain alphanumeric characters, wildcard characters such as exclamation point (!) or asterisk (*), single digit matches
                                                            such as the letter X (not x) or period (.) Can end with an optional
                                                            greater than (>) wildcard character Description Information about the Dialed Number
                                                            Pattern. None Maximum
                                                            length of 1024 characters Enable Custom
                                                               Ringtone Enables customized ring tone. Ringtone media filename - Enter the name of the file
                                                                  that is to be played for the respective dialed number pattern. Provide the URL
                                                                  for the stream name in the following format: rtsp://<streaming
                                                                     server IP
                                                                     address>:<port>/<directory>/<filename>.rm Disabled none Maximum
                                                            length of 256 characters Cannot contain whitespace
                                                            characters Click Save to save the Dialed Number
                                             Pattern. You are returned to the Dialed Number
                                                   Pattern page. To deploy the Dialed Number Pattern configuration, click Deploy to deploy the configuration to all Unified CVP Call
                                                Server devices. | Property | Description | Default | Value | General Configuration | Dialed Number Pattern | The actual Dialed Number Pattern. | None | Must be unique Maximum
                                                            length of 24 characters Can contain alphanumeric characters, wildcard characters such as exclamation point (!) or asterisk (*), single digit matches
                                                            such as the letter X (not x) or period (.) Can end with an optional
                                                            greater than (>) wildcard character | Description | Information about the Dialed Number
                                                            Pattern. | None | Maximum
                                                            length of 1024 characters | Enable Custom
                                                               Ringtone | Enables customized ring tone. Ringtone media filename - Enter the name of the file
                                                                  that is to be played for the respective dialed number pattern. Provide the URL
                                                                  for the stream name in the following format: rtsp://<streaming
                                                                     server IP
                                                                     address>:<port>/<directory>/<filename>.rm | Disabled none | Maximum
                                                            length of 256 characters Cannot contain whitespace
                                                            characters |
| Property | Description | Default | Value |
| General Configuration |
| Dialed Number Pattern | The actual Dialed Number Pattern. | None | Must be unique Maximum
                                                            length of 24 characters Can contain alphanumeric characters, wildcard characters such as exclamation point (!) or asterisk (*), single digit matches
                                                            such as the letter X (not x) or period (.) Can end with an optional
                                                            greater than (>) wildcard character |
| Description | Information about the Dialed Number
                                                            Pattern. | None | Maximum
                                                            length of 1024 characters |
| Enable Custom
                                                               Ringtone | Enables customized ring tone. Ringtone media filename - Enter the name of the file
                                                                  that is to be played for the respective dialed number pattern. Provide the URL
                                                                  for the stream name in the following format: rtsp://<streaming
                                                                     server IP
                                                                     address>:<port>/<directory>/<filename>.rm | Disabled none | Maximum
                                                            length of 256 characters Cannot contain whitespace
                                                            characters |
| Step 3 | Add a Send to
                                       VRU node in your ICM script before any Queue node. The
                                          explicit Send to VRU node is used to establish the VRU leg before the transfer
                                          to the agent; this is required to play streaming audio ringtones to a
                                          caller. |

| Property | Description | Default | Value |
|---|---|---|---|
| General Configuration |
| Dialed Number Pattern | The actual Dialed Number Pattern. | None | Must be unique Maximum
                                                            length of 24 characters Can contain alphanumeric characters, wildcard characters such as exclamation point (!) or asterisk (*), single digit matches
                                                            such as the letter X (not x) or period (.) Can end with an optional
                                                            greater than (>) wildcard character |
| Description | Information about the Dialed Number
                                                            Pattern. | None | Maximum
                                                            length of 1024 characters |
| Enable Custom
                                                               Ringtone | Enables customized ring tone. Ringtone media filename - Enter the name of the file
                                                                  that is to be played for the respective dialed number pattern. Provide the URL
                                                                  for the stream name in the following format: rtsp://<streaming
                                                                     server IP
                                                                     address>:<port>/<directory>/<filename>.rm | Disabled none | Maximum
                                                            length of 256 characters Cannot contain whitespace
                                                            characters |