---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-213406-test-directory-attribute-mapping-for-jab-html-5d9fc51359
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/213406-test-directory-attribute-mapping-for-jab.html
retrieved_at: 2026-08-21T07:05:28.761667+00:00
---

Test Directory Attribute Mapping for Jabber in Isolation

# Test Directory Attribute Mapping for Jabber in Isolation

### Download Options

Updated: September 28, 2018

Document ID: 213406

Contents

## Contents

## Introduction

This document describes how to map a directory attribute for use in Jabber and then test it without impact to any other user.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of:

- Cisco Jabber

- Cisco Unified Communication Manager (CUCM)

### Components Used

The information in this document is based on these software versions:

- Cisco Jabber for Windows 12.0

- Cisco Unified Communications Manager 12.0

## Configure

It is useful to have a test group configuration file on the Trivial File Transfer Protocol (TFTP) servers that can be assigned to a single user to test new configurations before you deploy them to the global jabber-config.xml file.

The first time this file is uploaded to the TFTP server, the TFTP service needs to be restarted.

In this example, you can see how to map the Other phone number on Jabber to the ipPhone Lightweight Directory Access Protocol (LDAP) attribute.

Steps to create the test configuration file:

Step 1. Using your favourite text editor, create a new file with the following content and save it as jabber-config-test.xml.

```
<?xml version="1.0" encoding="utf-8"?>
<config version="1.0">
 <Directory>
  <OtherPhone>ipPhone</OtherPhone>
 </Directory>
</config>
```

Note : the value ipPhone is case sensitive and needs to match the directory attribute name

Step 2. Upload the jabber-config-test.xml file to all TFTP servers in the cluster.

Step 3. Restart the TFTP service on all nodes in the cluster.

Step 4. Check that the new configuration file can be displayed in a web browser by navigating to one of the following URLs:

http://<TFTP_server>:6970/jabber-config-test.xml

OR

https://<TFTP_server>:6972/jabber-config-test.xml

Step 5. Assign the new configuration file to the test user on the Cisco Support Field on the Cisco Services Framework (CSF) device as ConfigurationFile=jabber-config-test.xml .

Step 6. Reset the Jabber client for that user to force fresh configuration download.

## Verify

On Jabber, click on the Call button for a user that has ipPhone attribute populated in LDAP and confirm the number is displayed in the Other field

## Troubleshoot

- Check that the new configuration file is displayed successfully in the web browser.

- Check the attribute on LDAP to ensure it is populated.

- Jabber logs show the test configuration file is retrieved correctly and that the value for OtherPhone is ipPhone.

```
DEBUG [0x00000dd0] [ents\ecc\src\config\PhoneConfig.cpp(861)] [csf.ecc] [csf::ecc::SoftphoneConfig::parseOutConfigurationFileName] - Detected that the "Cisco Support Field" has the following content: ConfigurationFile=jabber-config-test.xml DEBUG [0x00001bc8] [pters\config\ConfigStoreManager.cpp(169)] [ConfigService-ConfigStoreManager] [CSFUnified::ConfigStoreManager::getValue] - key : [otherphone] skipLocal : [0]  value: [ipPhone] success: [true] configStoreName: [TftpConfigStore]
```

- Check that packet capture displays the ipPhone value returned successfully.

### Contributed by Cisco Engineers

Domhnall MacCormac

Cisco TAC

### This Document Applies to These Products

- Jabber

- Unified Communications Manager (CallManager)