---
doc_id: www-cisco-com-c-en-us-td-docs-conferencing-advisories-sw-advisory-cscvo51143-html-8473efec4c
source_url: https://www.cisco.com/c/en/us/td/docs/conferencing/Advisories/SW_Advisory_CSCvo51143.html
retrieved_at: 2026-08-16T19:01:36.738143+00:00
---

Cisco Software Advisory Notices for CSCvo51143

# Cisco Software Advisory Notices for CSCvo51143

### Download Options

Updated: March 6, 2019

Dear Cisco Customer,

Cisco engineering has identified that WebRTC calls using the latest version of Google Chrome (73) will not connect to meetings with specific versions of Cisco Meeting Server. Please review the Software Advisory notice here to determine if the issues apply to your environment. Customers with active support contracts can proceed to download updated software to resolve the issue described.

For more comprehensive information about what is included in this software, refer to the Cisco software Release Notes, available from the Product Selector tool . From this page, select the product you are interested in. Release Notes are under "General Information" on the product page.

Affected Software and Replacement Solution for CSCvo51143

Software Type

Software Affected

Software Solution

Cisco Meeting Server

Version:

2.0 – All versions

2.1 – All versions

2.2 - All versions 2.3 - All versions earlier than 2.3.11 2.4 - All versions earlier than 2.4.4 2.5 - All versions earlier than 2.5.2

Version:

2.3.11

2.4.4

2.5.2

All versions prior to 2.3 have reached end of software maintenance, customers are advised to update to one of the versions as listed above under “Software Solution”. More information is available here: Cisco Meeting Server end of maintenance and support policy

Reason for Advisory:

This software advisory addresses the following software issue.

CSCvo51143

Google Chrome 73 onwards may send mDNS instead of IP addresses in ICE host candidates

Affected Platforms:

Cisco Meeting Server when used with Google Chrome 73.

```
Symptom :
```

```
Sharing presentation on WebRTC calls on Cisco Meeting Server using Google Chrome (as described in Conditions ) will cease working after updating Chrome to Version 73 or above if the camera permission is not granted. This Chrome release is expected to be released by Google on or about March 12th, 2019.
```

```
Conditions:
```

```
1. Google Chrome version 73 or above is used for a Cisco Meeting App WebRTC call, and
```

```
2. Camera permission is not granted by the user to Chrome or "Management and Presentation" mode is used to join a call.
```

```
Workarounds:
```

```
· Have the browser user grant Camera and Microphone permissions to the Cisco Meeting App WebRTC site. This permission can be prompted by having the user attempt to join a meeting with the ' Continue with browser ' option. This prompts the user to accept the permission and the permission will be saved in the browser for future uses. If a user has explicitly blocked the site, this block can be removed in Chrome's Settings under Content Settings -> Camera , or
```

```
· Do not upgrade Google Chrome beyond version 72 (Google provides individual and enterprise tools for controlling auto-upgrade of releases), or
```

```
· On an individual basis, use of mDNS by Chrome can be disabled by setting the flag Anonymize local IPs exposed by WebRTC to Disabled in the chrome://flags page (requires a relaunch of Chrome to take effect, this change is permanent), or
```

```
· Upgrade Cisco Meeting Server to a version that contains the solution to this issue.
```

| Affected Software and Replacement Solution for CSCvo51143 |
|---|
| Software Type | Software Affected | Software Solution |
| Cisco Meeting Server | Version: 2.0 – All versions 2.1 – All versions 2.2 - All versions 2.3 - All versions earlier than 2.3.11 2.4 - All versions earlier than 2.4.4 2.5 - All versions earlier than 2.5.2 | Version: 2.3.11 2.4.4 2.5.2 |