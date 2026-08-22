---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg410-software-configuration-vg410-software-config-guide-configuring-secure-85d9f6d667
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg410/software-configuration/vg410-software-config-guide/configuring-secure-sip-signaling.html
retrieved_at: 2026-08-22T01:18:18.107849+00:00
---

Cisco VG410 Voice Gateway Software Configuration Guide

# Cisco VG410 Voice Gateway Software Configuration Guide

Updated: August 27, 2024

Chapter: Configuring Secure SIP Signaling

## Chapter: Configuring Secure SIP Signaling

# Configuring Secure SIP Signaling

You can enable secure SIP line using transport layer security (TLS) to enhance FXS analog SIP endpoints, as well as support
                                    for some additional supplementary services such as enhanced auto-configuration, failover and fallback, forward to voicemail,
                                    hunt group login/logout, toggle between calls and callback features.

## Overview

A SIP line refers to a virtual phone line that uses Session Initiation Protocol (SIP) to transmit voice calls using an internet
                           connection. Features of a SIP line include call hold, call transfer, call forward, etc. To enable and use the SIP line features,
                           IP phones need to be registered to a communication manager like CUCM. FXS ports also need to be registered as a SIP endpoints
                           so that analog phones can have similar functionalities with IP phones. By enabling this feature, the analog endpoints connected
                           to the FXS ports can support basic SIP call features such as Call Waiting, Call Transfer, Call Park, Call Forward, etc. If
                           FXS ports are not registered as SIP endpoints, even basic calls cannot go through.

To register your FXS ports to CUCM as SIP endpoints, from Cisco IOS XE 16.12.1a, the SIP line functionality is available.

With all these call features, securing the signaling and media communication is vital to prevent the signaling line from being
                           disrupted, or the media stream being hacked or listened to.

From Cisco IOS XE 17.15.1a, support for secure SIP line connections is available. You can enable secure SIP line using transport layer security (TLS) to enhance FXS analog
                           SIP endpoints, as well as support some additional supplementary services such as enhanced auto-configuration, failover and
                           fallback, forward to voicemail, hunt group login/logout, toggle between calls and callback features.

The sections in this chapter provide information on how to enable secure SIP line features. You can choose to follow these
                           tasks to secure SIP line signaling and media communication by using the Cisco IOS XE 17.15.1a version or use the SIP line
                           features that are available from Cisco IOS XE 16.12.1 release.

## Prerequisites

Auto configuration and SIP line features are supported on CUCM version 15 and later only.

## Restrictions

You cannot rollback to a software version before IOS XE 17.15.1a and continue to use the secure SIP line features. If you
                                 need to rollback to an older release, it is recommended that you save the older working configuration before you upgrade to
                                 Cisco IOS XE 17.15.1a or a later version.

SIP line features with SIP trunk are not supported.

## Platforms Supported

This list specifies all the platforms that support secure SIP Line features:

VG400 Series Voice Gateways

VG410 Series Voice Gateways

VG420 Series Voice Gateways

Cisco Catalyst 8300 Series Routers

Cisco Catalyst 8200 Series Routers

ISR 4000 Series Routers (ISR4461 only)

## Configure Secure SIP Signaling

To configure secure SIP signaling from the device, perform the trustpoint configurations to generate the certificate for TLS
                           handshaking. Create a PKI trustpoint and then associate the trustpoint under sip-ua. You can achieve this in many ways, which
                           also includes creating a PKI trustpoint, providing a URL of the CA server, and associating the trustpoint under sip-ua. This
                           method is covered in the tasks under this section.

To know more about how to set the trustpoint and configuring SIP TLS, see SIP TLS Support .

### Create a Trustpoint

Perform these steps to create a trustpoint, which acts as a container for CA information.

### SUMMARY STEPS

- enable

- configure terminal

- crypto pki trustpoint

- enrollment url <URL>

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device > enable
```

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters the global configuration mode.

Step 3

crypto pki trustpoint

#### Example:

```
Device (config)# crypto pki trustpoint
```

Enters ca-trustpoint configuration mode.

Step 4

enrollment url <URL>

#### Example:

```
Device (ca-trustpoint)# enrollment url http://172.19.156.173:80
```

Specifies the URL where the device can enroll for certificates from the CA. Here, <URL> is the URL you need to specify.

#### Sample Configuration

```
Device (config)# crypto pki trustpoint
 enrollment url http://172.19.156.173:80
 serial-number none
 fqdn none
 ip-address none
 subject-name cn=6c:dd:30:9d:d7:61 --> MAC address of the gateway
 subject-alt-name s-sip analog --> Same as security profile in CUCM
 revocation-check none
 rsakeypair rsa_4k
 hash sha256
```

This configuration generates the certificate used in TLS handshaking. Here, a PKI trustpoint named ”sipline_rsa_4K” is created.
                                 The subject-name here is set to the MAC Address of the gateway and the subject-alternative-name is the secure SIP profile
                                 name. Both these entities should match with what is configured on the call manager.

### Associate the Trustpoint to the sip-ua

### SUMMARY STEPS

- voice class tls-profile <profile name>

- trustpoint <sipline_rsa_4k>

- sip-ua

- crypto signaling default tls-profile <profile name>

### DETAILED STEPS

Step 1

voice class tls-profile <profile name>

#### Example:

```
Device (config)# voice class tls-profile 123
```

Creates a voice class for the tls-profile. In this example, the tls-profile is named 123.

Step 2

trustpoint <sipline_rsa_4k>

Adds the sipline_rsa_4k trustpoint.

Step 3

sip-ua

#### Example:

```
Device (config)# sip-ua
```

Enters the SIP user-agent configuration mode.

Step 4

crypto signaling default tls-profile <profile name>

#### Example:

```
Device (config-sip-ua)# crypto signaling default tls-profile 123
```

Associates the trustpoint under sip-ua.

#### Example

```
Device > enable
Device# configure terminal
Device(config)# voice class tls-profile 123
    trustpoint sipline_rsa_4k
Device(config)# sip-ua
    Device(config-sip-ua)# crypto signaling default tls-profile 123
```

### Configure Secure SIP Signaling on CUCM

After you create a trustpoint and associate the trustpoint to the sip-ua, perform these steps on the CUCM user interface to
                                 complete the secure SIP line signaling configuration.

Step 1

Log in to the CUCM user interface and choose Gateway from the Device drop-down list on top.

Step 2

On the Find and List Gateway window, click Add New .

Step 3

From the Gateway Type drop-down list, choose the gateway, for example, VG410. Click Next .

Step 4

From the Protocol drop-down list, choose SIP , and click Next .

Step 5

On the Gateway Configuration window, configure the following fields:

MAC Address : Enter the MAC Address of the gateway.

Description : Provide a description for this gateway, if required.

Cisco Unified Communications Manager Group : From this drop-down list, select the required CUCM group.

Step 6

In the Configured Slots, VICs, and Endpoints area, click the FXS Port icon for the port that you want to configure.

Step 7

From the Port Type drop-down list, choose the type of connection that you want to configure.

The Port Configuration window displays the configuration for the port interface with analog access as the device protocol.

Step 8

From the Device Pool drop-down list, select a device pool.

Step 9

Complete the remaining fields in the Port Configuration window and click Save .

Step 10

Add a phone number and associate the phone number with the port.

Step 11

Once a phone line is associated with the port, you will see the associated phones on the left side of the window.

Step 12

Click on the phone line to go to the Directory Number Configuration window. You can configure the settings for your call features from this page. For example, you can configure the settings
                                          for Call Forward from the Call Forward and Call Pickup Settings area. Similary, for Call Waiting, you can configure the settings from the Multiple Call/Call Waiting Settings on Device area.

Step 13

Click Save to save your settings.

For more and in-depth information on Voice Gateway configuration on CUCM, see Configure Gateways .

| Feature or Enhancement | IOS XE Release | Feature Description |
|---|---|---|
| Analog SIP Line features | Cisco IOS XE 16.12.1a and later | From Cisco IOS XE 16.12.1a, your Voice Gateway allows you to register your FXS ports to CUCM as SIP endpoints. The analog
                                 endpoints connected to these FXS ports could support basic SIP call features, such as Call Waiting, Call Transfer, Call Park,
                                 Call Forward, etc. |
| Secure Analog SIP Line features | Cisco IOS XE 17.15.1a and later | You can enable secure SIP line using transport layer security (TLS) to enhance FXS analog SIP endpoints, as well as support
                                    for some additional supplementary services such as enhanced auto-configuration, failover and fallback, forward to voicemail,
                                    hunt group login/logout, toggle between calls and callback features. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device > enable |  |
| Step 2 | configure terminal Example: Device# configure terminal | Enters the global configuration mode. |
| Step 3 | crypto pki trustpoint Example: Device (config)# crypto pki trustpoint | Enters ca-trustpoint configuration mode. |
| Step 4 | enrollment url <URL> Example: Device (ca-trustpoint)# enrollment url http://172.19.156.173:80 | Specifies the URL where the device can enroll for certificates from the CA. Here, <URL> is the URL you need to specify. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | voice class tls-profile <profile name> Example: Device (config)# voice class tls-profile 123 | Creates a voice class for the tls-profile. In this example, the tls-profile is named 123. |
| Step 2 | trustpoint <sipline_rsa_4k> | Adds the sipline_rsa_4k trustpoint. |
| Step 3 | sip-ua Example: Device (config)# sip-ua | Enters the SIP user-agent configuration mode. |
| Step 4 | crypto signaling default tls-profile <profile name> Example: Device (config-sip-ua)# crypto signaling default tls-profile 123 | Associates the trustpoint under sip-ua. |

| Step 1 | Log in to the CUCM user interface and choose Gateway from the Device drop-down list on top. |
|---|---|
| Step 2 | On the Find and List Gateway window, click Add New . |
| Step 3 | From the Gateway Type drop-down list, choose the gateway, for example, VG410. Click Next . |
| Step 4 | From the Protocol drop-down list, choose SIP , and click Next . |
| Step 5 | On the Gateway Configuration window, configure the following fields: MAC Address : Enter the MAC Address of the gateway. Description : Provide a description for this gateway, if required. Cisco Unified Communications Manager Group : From this drop-down list, select the required CUCM group. |
| Step 6 | In the Configured Slots, VICs, and Endpoints area, click the FXS Port icon for the port that you want to configure. |
| Step 7 | From the Port Type drop-down list, choose the type of connection that you want to configure. The Port Configuration window displays the configuration for the port interface with analog access as the device protocol. |
| Step 8 | From the Device Pool drop-down list, select a device pool. |
| Step 9 | Complete the remaining fields in the Port Configuration window and click Save . |
| Step 10 | Add a phone number and associate the phone number with the port. |
| Step 11 | Once a phone line is associated with the port, you will see the associated phones on the left side of the window. |
| Step 12 | Click on the phone line to go to the Directory Number Configuration window. You can configure the settings for your call features from this page. For example, you can configure the settings
                                          for Call Forward from the Call Forward and Call Pickup Settings area. Similary, for Call Waiting, you can configure the settings from the Multiple Call/Call Waiting Settings on Device area. |
| Step 13 | Click Save to save your settings. For more and in-depth information on Voice Gateway configuration on CUCM, see Configure Gateways . |