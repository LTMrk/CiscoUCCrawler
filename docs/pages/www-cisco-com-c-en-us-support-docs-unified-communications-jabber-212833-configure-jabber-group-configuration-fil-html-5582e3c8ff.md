---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-212833-configure-jabber-group-configuration-fil-html-5582e3c8ff
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/212833-configure-jabber-group-configuration-fil.html
retrieved_at: 2026-08-21T07:05:37.058648+00:00
---

Configure Jabber Group Configuration File in Non-Telephony Deployment

# Configure Jabber Group Configuration File in Non-Telephony Deployment

### Download Options

Updated: February 27, 2018

Document ID: 212833

Contents

## Contents

## Introduction

This document describes how to provide a group configuration file to the Jabber desktop clients in the absence of a Client Services Framework (CSF) device.

## Prerequisites

### Requirements

Cisco recommends that you have the knowledge of these topics:

- Cisco Jabber Windows

- Cisco CallManager

### Components Used

- Cisco Jabber Windows 10.x and 11.x

- Cisco CallManager Version 10.x and above

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any configuration change.

## Configure

A group configuration file is typically used in order to test a configuration change before it is applied to the global XML file. The test file is attached to the Cisco Support Field file of the CSF device under Product Specific Configuration section and then the file is uploaded to the TFTP server. But for Jabber IM-Only or Deskphone mode deployments, the use of a group configuration is not possible due to the absence of the Cisco Support Field. In such scenarios, bootstrap.properties file can be used to attach the group configuration file.

Note : The Cisco TFTP service must be restarted each time a new XML file is uploaded in order to ensure that it will be downloaded by the Jabber client.

In order to link the group configuration file to the bootstrap.properties file:

- Navigate to C:\ProgramData\Cisco Systems\Cisco Jabber and open the bootstrap.properties file.

- Add ConfigurationFile:group-jabber-config.xml at the bottom and save it.

- Upload the new xml file to all the TFTP servers in the cluster.

- Restart the TFTP server.

- Reset the Jabber client and login again.

Tip : In order to confirm whether the new file is available on the TFTP server, enter http://<IP or FQDN of the server>:6970/group-jabber-config.xml or https://<IP or FQDN of the server>:6972/group-jabber-config.xml and hit Enter . The file content is displayed if it is available. If it is not displayed, then the possibilities are that either the file has a syntax error or the TFTP service restart is not done properly.

## Verify

Use this section in order to confirm that your configuration works properly.

In order to confirm that the Jabber client downloaded the xml file:

- Login into the Jabber client and collect a problem report. Navigate to Help > Report Problem .

- Extract the report and look for these lines in the jabber.log file.

```
DEBUG [0x000010f0] [pters\config\ConfigStoreManager.cpp(165)] [ConfigService-ConfigStoreManager] [CSFUnified::ConfigStoreManager::getValue] - key : [ConfigurationFile] skipLocal : [0]  value: [group-jabber-config.xml] success: [true] configStoreName: [BootstrapConfigStore] INFO  [0x00000d78] [adapters\config\TftpConfigStore.cpp(492)] [ConfigService-TftpConfigStore] [CSFUnified::TftpConfigStore::attemptTftpFileDownload] - *-----* Downloading file from: https://10.106.92.196:6972/group-jabber-config.xml with a timeout of 10 seconds.
```

This line is an indication of a successful download of the file.

```
INFO  [0x00000d78] [ls\src\http\BasicHttpClientImpl.cpp(452)] [csf.httpclient] [csf::http::executeImpl] - *-----* HTTP response code 200 for request #12 to https://10.106.92.196:6972/group-jabber-config.xml
```

3. Another way to confirm the availability of the file is to check C:\Users\<username>\AppData\Roaming\Cisco\Unified Communications\Jabber\CSF\Config\Cache location for the cachedTFTPConfigStore.xml file. Open this file with a text editor to see that the content is accurate.

Note : Jabber client uses port number 6972 and https for the download request if CUCM version is 11 and above. For CUCM versions 10 and below, it sends a http request to port 6970. So, the download URL varies in the logs based on the CUCM version.

## Troubleshoot

This section provides information you can use in order  to troubleshoot your configuration.

Ensure that the configuration file is free of syntax errors before you upload it to the TFTP servers. There are multiple ways to do it and one of the easiest ways is to upload the content of the file to https://www.w3schools.com/xml/xml_validator.asp . Alternatively, use the procedure given as Tip in order to confirm this. If the file has syntax errors, then Jabber client will not be able to parse it though it downloads successfully. In this case, the cachedTFTPConfigStore.xml file is not seen in the path that is mentioned.

### Contributed by Cisco Engineers

Gangabhavani Sankar Voleti

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber