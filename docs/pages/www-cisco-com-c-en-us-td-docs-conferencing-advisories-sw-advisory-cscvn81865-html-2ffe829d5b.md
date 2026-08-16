---
doc_id: www-cisco-com-c-en-us-td-docs-conferencing-advisories-sw-advisory-cscvn81865-html-2ffe829d5b
source_url: https://www.cisco.com/c/en/us/td/docs/conferencing/Advisories/SW_Advisory_CSCvn81865.html
retrieved_at: 2026-08-16T19:01:40.668998+00:00
---

Cisco Software Advisory Notices for CSCvn81865

# Cisco Software Advisory Notices for CSCvn81865

### Download Options

Updated: January 14, 2019

Dear Cisco Customer,

Cisco engineering has identified that WebRTC calls using the latest version of Google Chrome (72) will not connect to meetings with specific versions of Cisco Meeting Server. Please review the Software Advisory notice here to determine if the issues apply to your environment. Customers with active support contracts can proceed to download updated software to resolve the issue described.

For more comprehensive information about what is included in this software, refer to the Cisco software Release Notes, available from the Product Selector tool . From this page, select the product you are interested in. Release Notes are under "General Information" on the product page.

Affected Software and Replacement Solution for CSCvn81865

Software Type

Software Affected

Software Solution

Cisco Meeting Server

Version:

2.0 – All versions

2.1 – All versions

2.2 - All versions 2.3 - All versions earlier than 2.3.10 2.4 - All versions earlier than 2.4.3 2.5 - Version 2.5.0

Version:

2.3.10

2.4.3

2.5.1

All versions prior to 2.3 have reached end of software maintenance, customers are advised to update to one of the versions as listed above under “Software Solution”. More information is available here: Cisco Meeting Server end of maintenance and support policy

Reason for Advisory:

This software advisory addresses the following software issue.

CSCvn81865

Fix joining calls on Chrome from version 72 onwards

Affected Platforms:

Cisco Meeting Server when used with Google Chrome 72.

```
Symptom :
```

```
WebRTC calls on Cisco Meeting Server using Chrome will cease working after updating Chrome to Version 72 or above. This Chrome release is expected to be released by Google on or about January 29th, 2019. Users of Chrome might see the following error within the Chrome Developer Console when attempting to connect to a Meeting Server software version affected by this change:
```

```
[Deprecation] "Complex" Plan B SDP detected!
```

```
Conditions:
```

```
Unable to join Cisco Meeting Server call with Chrome WebRTC. Error printed in Chrome Developer Console as: [Deprecation] "Complex" Plan B SDP detected!
```

```
Workaround:
```

```
Do not upgrade Chrome beyond Version 71. Alternatively, upgrade Cisco Meeting Server to a version which contains the solution to this issue.
```

| Affected Software and Replacement Solution for CSCvn81865 |
|---|
| Software Type | Software Affected | Software Solution |
| Cisco Meeting Server | Version: 2.0 – All versions 2.1 – All versions 2.2 - All versions 2.3 - All versions earlier than 2.3.10 2.4 - All versions earlier than 2.4.3 2.5 - Version 2.5.0 | Version: 2.3.10 2.4.3 2.5.1 |