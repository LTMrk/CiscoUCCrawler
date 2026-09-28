---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-1000-218117-configure-and-troubleshoot-meetingapps-f-html-82f951feaa
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server-1000/218117-configure-and-troubleshoot-meetingapps-f.html
retrieved_at: 2026-08-18T23:48:08.754237+00:00
---

Configure and Troubleshoot MeetingApps for File Sharing

# Configure and Troubleshoot MeetingApps for File Sharing

### Download Options

Updated: August 30, 2022

Document ID: 218117

Contents

## Contents

## Introduction

This document describes the step-by-step process to configure and troubleshoot MeetingApp for File sharing on Cisco Meeting Server (CMS).

Contributed by Vikas Kumar, Sateesh Katukam, Aviral Pal, Cisco TAC Engineers.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Understanding of CMS API for meetingapps configuration

- Cisco Meeting Server version 3.5 and later

### Components Used

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

- MeetingApp service has been introduced to support file sharing from version 3.5 Web App ,meeting participants can share files in the meeting.

- MeetingApps service must be configured in stand alone Meeting Server node and no other services must be running on this node,MeetingApps can be configured on DMZ network for external users and internal also depending upon the requirement.

- MeetingApps service must be deployed in the DMZ network for external users to share files and must be assigned public IP and firewall ports must be opened on DMZ for public access. The MeetingApps service can be configured on a Meeting Server 1000 or Meeting Server on VM deployments.

- Only a signed-in web app user with appropriate permissions can share files in a meeting.

- File sharing supports a maximum of 5 files with a size limit of 10MB each at a time.

- The shared file is available for download only during the meeting. Participants joining after a meeting has started can only view or download the files that are shared after they joined the meeting.

- exe files cannot be shared.

- MeetingApps services cannot be configured on a Meeting Server 2000.

- File share feature does not work if your cluster has a Meeting Server 2000 deployment.

### Network Diagram

Web Bridges in your environment must be configured to talk to MeetingApps in order to upload or download the files shared in the meeting.

## Configure

Follow these steps to configure:

1. SSH into the MMP and log in.

2. Configure the interface and port used by MeetingApps to communicate using the command

meetingapps https listen <interface> <port>

3. Configure the certificate key pair for the MeetingApps using the command

meetingapps https certs <key-file> <crt-fullchain-file>

4. Generate the secret key using the command: meetingapps gensecret

Copy the generated key to later configure the Web Bridge (at Step 7). Everytime the command is executed, a new secret key is generated and Web Bridge must be configured with the new key.

5. Enable the MeetingApps service using the command meetingapps enable

6. Before configuring the Web Bridge to connect to MeetingApps, all the Web Bridges must be disabled using the command

webbridge3 disable

7. All the Web Bridges in your setup need to communicate with the MeetingApps to upload or download files shared in the meeting. Configure the Web Bridge to connect to the MeetingApps using the command

webbridge3 meetingapps add  <hostname> <port> <secretkey>

8. Enable all the Web Bridges using the command webbridge3 enable

9. Sharing files in a meeting : API parameter fileReceiveAllowed ( true|false ) has been introduced to enable or disable the file share at the callProfile level or Call level.

Set fileReceivedAllowed to true in callProfile and assign to cospace or system level.

10. File Upload Allowed : API parameter fileUploadAllowed ( true|false ) has been introduced to enable user to allow share file or not in the callLegProfile

Set fileUploadAllowed to true in callLegProfile and assign to cospace or system level.

## Verify

Verify the configuration by entering command : webbridge3

## Troubleshoot

To troubleshoot the reachability of the MeetingApps, you can use the API https://hostname/IP address:port/api/ping

### File sharing Icon is not visible

Ensure meetingapps and webbridge3 is configured correctly and both the services are running in the CMS , under calls fileReceiveAllowed API parameter is set to true at the call level OR callprofiles API.

Enable fileReceiveAllowed : At call level

After enable we can see option file share visible.

At callProfiles level : A callProfile can be assigned at a cospace or at the system level.

### Add files and share buttons are not visibile to the users

Add files and share buttons won’t be visible to users until fileUploadAllowed is set to true for a participant to share files in a meeting. fileUploadAllowed supported on the callLegProfiles or callLegs methods

callLegProfiles can be assigned at the cospace or at system level.

After performing this change we can see file Add File and Share button is enabled:

### File Upload failed

This issue is because of a communication issue between client and server or an issue between meetingapps and Webbridge configuration. Finally, after resolving the issue we can see the file upload successfully:

### Revision History

1.0

31-Aug-2022

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 31-Aug-2022 | Initial Release |