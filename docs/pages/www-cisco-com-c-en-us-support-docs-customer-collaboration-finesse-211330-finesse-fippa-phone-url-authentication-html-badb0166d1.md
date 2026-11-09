---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-finesse-211330-finesse-fippa-phone-url-authentication-html-badb0166d1
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/finesse/211330-Finesse-FIPPA-Phone-URL-Authentication.html
retrieved_at: 2026-11-09T13:02:22.142223+00:00
---

Finesse IPPA "Phone URL Authentication" Error Generated After Call Termination

# Finesse IPPA "Phone URL Authentication" Error Generated After Call Termination

Updated: June 8, 2017

Document ID: 211330

Contents

## Contents

## Introduction

This document describes a problem when Finesse IP Phone Agent (IPPA) agent gets an error "Phone URL authentication username or password is incorrect in the IP Phone Agent settings. Contact your administrator." after normal call termination.

## FIPPA URL Authentication Troubleshooting

### Collect Information

Check the user configured in Finesse Administration web page for IPPA settings.

Get basic information about the phone that has FIPPA service configured. To troubleshoot, it is good to have MAC address, IP address and extension of the phone.

### Troubleshoot

Most of the troubleshooting for this feature is done from Cisco Unified Communications Manager (CUCM) perspective.

Therefore administration should have some experience with CUCM.

Ensure that the user configured in Finesse Administration IPPA settings has the phone in its list of controlled devices. In order to do that, use this SQL query. Replace the pguser name in the query with the one you have configured.

```
admin: run sql SELECT m.pkid,ap.name appuser,d.name device FROM ApplicationUserDeviceMap m INNER JOIN device AS d ON d.pkid==m.fkdevice INNER JOIN applicationuser ap ON ap.pkid==m.fkapplicationuser WHERE ap.name LIKE 'pguser' pkid appuser device ==================================== ======= ==================== ea92949a-c8e4-4818-ad42-80ed5ba65135 pguser SEP0050569902C1 fb5af549-d1ae-423b-afa0-f28b32e4426d pguser SEP005056996F7E 1fe71268-328b-4810-9e55-5683647a82d1 pguser SEPC80084AA8721
```

In the example pguser has phone with mac address C80084AA8721 in its list of controlled devices.

If Extenstion Mobility (EM) service is used CTI Controlled Device Profile must be associated as well with pguser.

Use this link to ensure that the phone can be controlled remotely. Replace IP address with the one that your FIPPA phone has and provide pguser credentials after the prompt.

http://10.62.153.22/CGI/Screenshot

Note : Close the browser if you want to use the link to test again.

If the configuration is correct, similar picture will be displayed.

In case there is some problem with configuration such message might be displayed.

```
<CiscoIPPhoneError Number="4" />
```

The error code "4" means an authentication issue.

From FIPPA log file you will see similar messages.

```
0000001737: 10.48.47.140: Jun 08 2017 08:52:14.036 +0200: %CCBU_pool-148-thread-1-6-HTTP_RESPONSE: %[FIPPA_USER_ID=HttpClient-pushToPhone-24-15c86799425] [HTTP_BODY=<CiscoIPPhoneError Number="4" />] [HTTP_METHOD=POST][HTTP_REQUESTID=null][HTTP_RESPONSE_MESSAGE=OK][HTTP_RESPONSE_STATUS=200][HTTP_URL=http://10.62.153.22/CGI/Execute]: Received HTTP Response 0000001738: 10.48.47.140: Jun 08 2017 08:52:14.039 +0200: %CCBU_pool-148-thread-1-3-FIPPA_ERROR: %[ERROR_DESCRIPTION=get invalid Response from phone: <CiscoIPPhoneError Number="4" /> CiscoIPPhoneError: number=4][FIPPA_SOURCE=HttpPushClient-24-15c86799425]: An error was encountered
```

Note : To troubleshoot the problem ensure to enable Web Server in the phone Product Specific Configuration Layout.

Ensure that you have correct resolvable URL Authentication link specified in CUCM Enterprise Parameters.

In some cases, when you remove the Secure Authentication URL, it helps fix the problem.

If the problem persists, try one of these options:

- remove ITL/CTL file from the phone

- remove the phone's association with pguser and associate the phone back

- restart CTIManager process on the node to which the phone is registered (10.48.47.136 in the example)

### Revision History

1.0

08-Jun-2017

Initial Release

### Contributed by Cisco Engineers

Alexander Levichev

Cisco TAC Engineer

### This Document Applies to These Products

- Finesse

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 08-Jun-2017 | Initial Release |

## Figuras

![211330-Finesse-FIPPA-Phone-URL-Authentication-00.jpeg](https://www.cisco.com/c/dam/en/us/support/docs/customer-collaboration/finesse/211330-Finesse-FIPPA-Phone-URL-Authentication-00.jpeg)

![211330-Finesse-FIPPA-Phone-URL-Authentication-01.jpeg](https://www.cisco.com/c/dam/en/us/support/docs/customer-collaboration/finesse/211330-Finesse-FIPPA-Phone-URL-Authentication-01.jpeg)

![211330-Finesse-FIPPA-Phone-URL-Authentication-02.jpeg](https://www.cisco.com/c/dam/en/us/support/docs/customer-collaboration/finesse/211330-Finesse-FIPPA-Phone-URL-Authentication-02.jpeg)

![211330-Finesse-FIPPA-Phone-URL-Authentication-03.jpeg](https://www.cisco.com/c/dam/en/us/support/docs/customer-collaboration/finesse/211330-Finesse-FIPPA-Phone-URL-Authentication-03.jpeg)

![211330-Finesse-FIPPA-Phone-URL-Authentication-04.jpeg](https://www.cisco.com/c/dam/en/us/support/docs/customer-collaboration/finesse/211330-Finesse-FIPPA-Phone-URL-Authentication-04.jpeg)

![TAC Authored](https://www.cisco.com/etc/designs/cdc/fw/i/TAC_lg-icon.png)

![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)