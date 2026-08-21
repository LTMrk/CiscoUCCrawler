---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-118750-technote-jabber-00-html-160d121d9f
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/118750-technote-jabber-00.html
retrieved_at: 2026-08-21T06:59:41.988195+00:00
---

Troubleshoot Microsoft Outlook Integrated with Cisco Jabber when Shows No Presence Status/Presence Bubble

# Troubleshoot Microsoft Outlook Integrated with Cisco Jabber when Shows No Presence Status/Presence Bubble

### Download Options

Updated: October 8, 2021

Document ID: 118750

Contents

## Contents

## Introduction

This document describes a problem encountered where there is no presence status or presence bubble in Microsoft Outlook Integrated with Cisco Jabber and proposes steps in order to troubleshoot this issue.

## Prerequisites

### Requirement

Cisco recommends that you have knowledge of these topics:

- Cisco Jabber for Windows

- Microsoft Outlook Integration

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Unified Communications Manager (CUCM) Version 10.5

- Cisco Instant Messaging (IM) and Presence (IM and P) Version 10.5

- Cisco Jabber for Windows Version 10.5

- Microsoft Outlook Professional Plus 2010

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Cisco Jabber for Windows supports availability status in Microsoft Outlook. If the presence integration is successful, then users can share their availability in Microsoft Outlook. With Microsoft Outlook, you can use the Microsoft contact card click-to-communicate icons directly from within the application in order to save time and streamline workflows because you can view user availability and initiate communications such as personal and group voice, video, and chat sessions without the need to switch between applications.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Problem

The Jabber client can be integrated with Microsoft Outlook with the Messaging Application Program Interface (MAPI) protocol so that the users can share their availability in Microsoft Outlook. Sometimes, the Microsoft Outlook integration is successful but you might not see the users' presence status/presence bubble in Microsoft Outlook.

## Troubleshoot

In order to troubleshoot this problem, verify these points:

- Ensure that there is no other Extensible Messaging and Presence Protocol  (XMPP) / Session Initiation Protocol (SIP) application integrated with Microsoft Outlook that provides presence (Lync, Windows Live Messenger, Office Communicator, Windows Messenger, Cisco Unified Communication Integration with Microsoft Lync 2010 (CUCILync), Cisco Unified Communication Integration with Microsoft Office Communicator (CUCIMOC), Cisco Unified Personal Communicator (CUPC), and WebEx Connect).

```
HKEY_CURRENT_User\Software\Microsoft\Office\14.0\Common\PersonaMenu
```

```
HKEY_CURRENT_USER\Software\IM Providers\Cisco Jabber\UpAndRunning
```

If Jabber runs and the key UpAndRunning is not set to two, change the UpAndRunning data to two and then restart the Microsoft Outlook and Jabber client.

- Verify that the Jabber IM address and proxyaddress are the same. If they are different, specify SIP:user@cupdomain as the value of the proxyAddresses attribute in Microsoft Active Directory. The requirement to share availability in Microsoft Outlook is to keep the Session Initiation Protocol (SIP) proxy and the IM address the same.

Caution : If it does not have the proxyaddress the same as the IM address is completely unsupported by both Microsoft and Cisco.

7. Presence only updates when Use Cached Exchange Mode is disabled.

8. Fix/Repair the Outlook Registry keys.

Warning : The next steps require to be followed by a Windows Administrator engineer who understands how the Regedit works. Follow the steps in this section carefully. Serious problems might occur if you modify the registry incorrectly. Before you modify it, back up the registry for restoration in case of problems occur.

Remove the Outlook registry key and then repair your Outlook to check the result. . Step 1. Click Start , and then click Run . Step 2. Type regedit in the blank box, and then press ENTER . Step 3. In the Registry Editor , locate the next subkey in the registry: HKEY_LOCAL_MACHINE\Software\Clients\Mail\Microsoft Outlook.

Step 4. Select the subkey , and then press DELETE . Click Yes . Step 5. Exit the Registry Editor.

Step 6. Start Outlook . Step 6. Navigate to Start > Control Panel > Programs and Features. Step 7. Select your Microsoft Office suite and then click the Change button . Next, click Repair and then click Continue . Step 8. Follow the instructions on the screen to complete the repair.

Tip : If these steps do not help/resolve the issue, gather a problem report from the Jabber client and contact the Cisco Technical Assistance Center (TAC).

## Related Information

- Deployment and Installation Guide for Cisco JabberRelease 10.5

Feature Configuration for Cisco Jabber 11.7

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

08-Oct-2021

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 08-Oct-2021 | Initial Release |