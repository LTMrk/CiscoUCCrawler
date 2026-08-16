---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-telepresence-system-ex-series-221630-configure-telepresence-e-b89001e895
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/telepresence-system-ex-series/221630-configure-telepresence-endpoint-sip-regi.html
retrieved_at: 2026-08-16T22:18:28.728108+00:00
---

Configure Telepresence Endpoint SIP Registration to Expressway

# Configure Telepresence Endpoint SIP Registration to Expressway

### Download Options

Updated: February 5, 2024

Document ID: 221630

Contents

## Contents

## Introduction

This document describes the basic configuration steps to register telepresence devices to the Expressway.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Expressway series.

- Telepresence endpoints.

- SIP protocol.

### Components Used

The information in this document is based on these software and hardware versions:

- Telepresence endpoints running software version RoomOS 11.9.

- Expressway series server running software version X14.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Expressway can act as the registrar and call control server for telepresence endpoints over the SIP and H.323 protocols. Both Expressway-C and Expressway-E can be configured as a registrar, however the most common approach is to register telepresence endpoints to Expressway-C, since this is the server that sits on the internal corporate network.

### Enable the registrar service on Expressway

The registrar service can be enabled from the Expressway GUI, by running the Service setup from the link available at General > Overview > Run service setup :

This setup can be executed during the initial configuration of the server, or at any other time if services need to enabled in the future. If the Service setup has been executed before, the Overview page displays a Return to service setup link instead:

To enable the service, from the Select Services check list, choose Registrar .

Note : The Service setup always starts up with all options unchecked, regardless of whether the services have been previously activated or not.

Click Continue and complete the remaining steps of the Service setup for the changes to take effect.

### Licensing requirements

The correct license types must be available in order for Expressway to accept registrations. The amount of licenses available determines the amount of telepresence endpoints that are able to register to the Expressway. There are two types of registration licenses available:

TelePresence Room System License

Desktop System License

The SIP devices in this list register as desktop systems; all other devices are considered room systems:

Cisco TelePresence EX60

Cisco TelePresence EX90

Cisco Webex DX70

Cisco Webex DX80

Tip : The Webex Desk and Webex Desk Pro series are not in this list, and do not register as a desktop system. They consume a TelePresence Room System License.

More detailed information about licensing can be found in the Cisco Expressway Administrator Guide .

Caution : This document uses the basic registration settings, resulting in a non-secure registration. With this setup, the SIP signaling can be inspected in clear text in a packet capture. Refer to the telepresence endpoint and Expressway administrator guides for more information about configuring TLS to set up secure registrations with encrypted SIP signaling.

### 1. Configure the Expressway

1. Log in to the web GUI of Expressway. If a cluster is in place, log in to the primary server.

2. Navigate to Configuration > Domains > New.

3. Enter the name of your registration domain under Domain name .

4. Ensure that SIP registrations and provisioning on Expressway is set to On .

5. Leave all other settings with their default value. Click Create domain .

6. Navigate to Configuration > Registration > Configuration , set Restriction policy to Allow List . Click Save .

Note : If the Registration menu is not available under Configuration , ensure that the registrar service has been enabled as described in the Background Information section.

7. At the bottom of the page, click Configure the registration Allow List , and click New .

8. Enter a description for your rule (optional).

9. From the Pattern type drop-down menu, select Regex .

10. In the Pattern string field, enter the expression .*@ and append the domain name you entered in step 3.

11. Click Add Allow List pattern .

### 2. Configure the Telepresence Endpoint

- Log in to the web GUI of your telepresence endpoint.

- Navigate to Settings > Configurations > NetworkServices and ensure that the SIP protocol is enabled by setting SIP Mode to On .

- Navigate to Settings > Configurations > SIP .

- Set ANAT to Off . This feature is not supported by Expressway.

- Enter the FQDN or IP address of your Expressway(s) in the Proxy [n] Address fields . You can enter the addresses of up to 4 Expressway cluster peers, to provide redundancy.

- Set TlsVerify to Off and DefaultTransport to TCP .

- Set Type to Standard .

- In the URI field, enter the URI that your device uses to identify itself. This is the URI that must be dialed in order to call the device. This must be in the host@domain format, where the host part is an alphanumeric string, and the domain part is the domain previously configured on Expressway.

- Click Save .

This image provides example settings used in a lab environment:

## Verify

After saving the configuration, the registration status can be verified from Settings > Statuses > SIP > Registration. As shown in this image, the registration is successful in this example:

In case of a failure to register, this section displays a reason for the failure. In this example, the reason field shows that a 403 Forbidden was returned by Expressway in response to the SIP REGISTER request, suggesting that the registration policy rules need to be reviewed.

Registrations can also be verified on the Expressway by navigating to Status > Registrations . A list of registrations can be displayed by device, by URI or as a historical report. This image displays an example of a registration report by device name:

## Related Information

SIP settings configuration from the RoomOS Administrator Guide .

Registration Control chapter from the Expressway Administrator Guide version X14 .

### Revision History

1.0

06-Feb-2024

Initial Release

### Contributed by Cisco Engineers

Fabio Achi

Technical Consulting Engineer

### This Document Applies to These Products

- TelePresence System EX Series

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 06-Feb-2024 | Initial Release |