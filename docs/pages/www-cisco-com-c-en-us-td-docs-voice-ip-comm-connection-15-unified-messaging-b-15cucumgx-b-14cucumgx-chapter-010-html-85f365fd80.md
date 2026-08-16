---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-unified-messaging-b-15cucumgx-b-14cucumgx-chapter-010-html-85f365fd80
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/unified_messaging/b_15cucumgx/b_14cucumgx_chapter_010.html
retrieved_at: 2026-08-16T18:34:41.379063+00:00
---

Unified Messaging Guide for Cisco Unity Connection Release 15

# Unified Messaging Guide for Cisco Unity Connection Release 15

Updated: December 18, 2023

Chapter: Configuring Text-to-Speech

## Chapter: Configuring Text-to-Speech

# Configuring Text-to-Speech

Configuring Text-to-Speech

## Overview

The Text-to-Speech (TTS) feature allows the unified messaging users to listen to their emails when they sign in to Unity Connection
                           using phone. For more information on text-to-speech, see the Text-to-Speech, page 1-10 section.

## Task List for Configuring Text-to-Speech

With text-to-speech feature enabled in Unity Connection, you can play the emails through phone that are accessible either
                           through Exchange or Office 365.

### Configuring the
                           	 Text-to-Speech Feature

Step 1

Follow the steps depending on the version of Exchange server
                                          			 accessed by unified messaging users:

Configuring TTS on Office 365, Exchange 2019, Exchange 2016 .

Step 2

Enable
                                          			 text-to-speech in Unity Connection on an existing or a new unified messaging
                                          			 service. Configure a unified messaging service following the steps as mentioned
                                          			 in the Creating a Unified Messaging
                                             				Service to Access Mail Server, page 2-27 section.

### Configuring TTS on Office 365, Exchange 2019 or Exchange 2016

Create and install an SSL certificate on each Exchange server
                              		that unified messaging users want to access following the given steps:

Open the Exchange Management Shell on the Exchange server.

Enter the following command:

new-exchangecertificate -generaterequest -domainname < Exchange server > - friendlyname < friendly name > -path c:\csr.txt

where < Exchange server > is the IP address or host name of the
                                    			 Exchange server and < friendly name > is the friendly name that you select for
                                    			 the Exchange server

The domain name for the Exchange server must be the IP address
                                    			 or the fully qualified DNS name (recommended) so that the Unity Connection
                                    			 server can successfully ping the Exchange server. Otherwise, users may not be
                                    			 able to access their emails in the external message store.

Press the Enter key
                                    			 and a Certificate Signing Request (CSR) file with the name Csr.txt is
                                    			 created in the root directory.

Send the CSR file to a Certification Authority (CA) that
                                    			 generates and sends back a new certificate.

Enter the following command:

import-exchangecertificate -path < path >

where < path > is the location of the directory where the CA saves
                                    			 the new server certificate

Press the Enter key
                                    			 and enter the following command:

dir cert:\localmachine\my |
                                       				fl

Press the Enter key and highlight the “thumbprint” property and copy it to the
                                    			 clipboard.

Perform either of the following actions:

If the class of service for unified messaging users is
                                          				  configured to access email and use calendar data from an external email server
                                          				  using IMAP, enter the following command:

enable-exchangecertificate
                                             					 -thumbprint <thumbprint> -services "IIS,IMAP"

If the class of service for unified messaging users is not
                                          				  configured to access calendar data from external email server using IMAP, enter
                                          				  the following command:

enable-exchangecertificate
                                             					 -thumbprint <thumbprint> -services "IIS"

Press the Enter key.

| Step 1 | Follow the steps depending on the version of Exchange server
                                          			 accessed by unified messaging users: Configuring TTS on Office 365, Exchange 2019, Exchange 2016 . |
|---|---|
| Step 2 | Enable
                                          			 text-to-speech in Unity Connection on an existing or a new unified messaging
                                          			 service. Configure a unified messaging service following the steps as mentioned
                                          			 in the Creating a Unified Messaging
                                             				Service to Access Mail Server, page 2-27 section. Note Make sure the Access Exchange Email Using Text-to-Speech (TTS)
                                                      				check box under Service Capabilities is checked. | Note | Make sure the Access Exchange Email Using Text-to-Speech (TTS)
                                                      				check box under Service Capabilities is checked. |
| Note | Make sure the Access Exchange Email Using Text-to-Speech (TTS)
                                                      				check box under Service Capabilities is checked. |

| Note | Make sure the Access Exchange Email Using Text-to-Speech (TTS)
                                                      				check box under Service Capabilities is checked. |
|---|---|

| Note | You must have a copy of the CA public root certificate or public root certificate chain. This certificate is needed for configuring
                                                Unity Connection to trust the Exchange 2019 or Exchange 2016 server. |
|---|---|

| Note | To use
                                                   				  TTS over Office 365, you are not required to do any specific configuration. |
|---|---|