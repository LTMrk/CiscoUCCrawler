---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-200119-configure-cu-b3085ee57f
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200119-Configure-CUCM-TFTP-for-Jabber-Automatic.html
retrieved_at: 2026-08-21T13:54:22.719271+00:00
---

Configure CUCM TFTP for Jabber Automatic Update

# Configure CUCM TFTP for Jabber Automatic Update

### Download Options

Updated: September 14, 2018

Document ID: 200119

Contents

## Contents

## Introduction

This document describes how to host XML files on Cisco Unified Communications Manager (CUCM) TFTP server for Jabber's Automatic Update feature.

Since CUCM 8.5, all files uploaded to the TFTP server can also be made available via HTTP on TCP Port 6970.

Note : The built in HTTP server is designed for static content only, dynamic content is not supported. It can be used to host files so that a separate web server is not needed to be deployed in the cluster. Files can only be uploaded via the OS Administration TFTP File Management page which means it might not be scalable for hosting photos (for use with Jabber Uniform Resource Identifier (URI) Substitution Photo Retrieval).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- OS Administration TFTP File Management page

- Cisco TFTP Service

### Components Used

The information in this document is based on CUCM version 8.5 and later.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Configure

### Jabber Automatic Update Configuration File

This example illustrates an XML file that is used for Jabber's Automatic Update feature.

```
<?xml version="1.0" encoding="UTF-8"?> <JabberUpdate> <LatestBuildNum>55781</LatestBuildNum> <LatestVersion>10.6.1</LatestVersion> <Message> <![CDATA[<h3 class="topictitle3">New and Changed Features in Release 10.6(1)</h3> <p><strong>Certificate Validation for CTI Connections</strong></p> <p>Cisco Jabber for Windows no longer uses CTI server certificate validation.</p> <p><strong>Call with Edit</strong></p> <p>A new&nbsp;<strong>Call with Edit</strong>&nbsp;menu option is available from the hub window by right-clicking over a contact's name. Users can edit the number they are calling prior to making the call. When users select a number from this menu option, the call number is copied into the&nbsp;<strong>Search or Call</strong>&nbsp;field with the cursor automatically placed at the front of the number. Users can edit the call number prior to making the call.</p> <p>No configuration is required to enable this feature.</p> <p><strong>Show Contact Pictures in Hub</strong></p> <p>The Cisco Jabber client has renamed the&nbsp;<strong>Show Contact Pictures</strong>&nbsp;option as&nbsp;<strong>Show Contact Pictures in Hub</strong>. This option is available in the client under the&nbsp;<strong>Options</strong>&nbsp;&gt;&nbsp;<strong>View</strong>&nbsp;menu.</p> <p>Only the name of the option has changed, the behavior has not; selecting it displays users' contact photos in the hub window on the&nbsp;<strong>Contacts</strong>,&nbsp;<strong>Recents</strong>, and&nbsp;<strong>Voice Messages</strong>&nbsp;tabs.</p>]]> </Message> <DownloadURL>http://ucmpub.domain.com:6970/CiscoJabberSetup.msi</DownloadURL> </JabberUpdate>
```

As you can see, the DownloadURL is pointed to http://ucmpub.domain.com:6970/CiscoJabberSetup.msi .

Note : It is important to use port 6970 in the URL.

The next step is to refer this URL in the jabber-config.xml file:

```
<?xml version="1.0" encoding="utf-8"?>
<config version="1.0">
 <Client>
   <UpdateUrl>http://ucmpub.domain.com:6970/jabber-update.xml</UpdateUrl>
 </Client>
</config>
```

This jabber-config.xml file then gets uploaded to CUCM OS Administration TFTP File Management as normal. Next, upload the jabber-update.xml file and the Jabber executable file as shown in these images.

Finally, restart Cisco TFTP service from Cisco Unified Serviceability.

## Verify

Use this section in order to confirm that your configuration works properly.

In order to verify that the file is available via HTTP, point your browser to http://<CUCM IP or FQDN>:6970/jabber-update.xml as shown in this image.

In Wireshark, the HTTP protocol requests jabber-update.xml via TCP port 6970 as shown in this image.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.