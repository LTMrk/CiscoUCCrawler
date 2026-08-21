---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-212104-configure-and-troubleshoot-uds-contact-p-htm-966f92068c
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/212104-Configure-and-Troubleshoot-UDS-Contact-P.html
retrieved_at: 2026-08-21T07:05:32.902870+00:00
---

Configure and Troubleshoot UDS Contact Photos Resolution through MRA/Expressway

# Configure and Troubleshoot UDS Contact Photos Resolution through MRA/Expressway

Updated: June 28, 2018

Document ID: 212104

Contents

## Contents

## Introduction

This document describes the procedure to configure and troubleshoot contact photo resolution via User Discovery Service (UDS) when Jabber is registered over Mobile Remote Access (MRA).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of the contact photo resolution over UDS requirements:

- The images must be hosted somewhere. You need to have a separate webserver to host the images.

- The images must be in "jpg" format and be sized 128 x128 pixels.

- Jabber must have access to that location. The webserver's Fully Qualified Domain Name (FQDN) or IP address must be completely resolvable and reachable from the inside even if the webserver is located outside of the network.

- Each image file must have the naming scheme as "uid.jpg" where "uid" is the user id of each Jabber user. This will work in tandom with the configuration code in the configuration file.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

Jabber administrators configure photo contact resolution via Lightweight Directory Access Protocol (LDAP) internally before they deploy Mobile Remote Access (MRA) via Cisco Expressway. When LDAP is used for contact photo resolution when you log in externally via MRA, your contact photos will not resolve because MRA uses User Discovery Service (UDS) by default. Administrators need to configure contact photo resolution via UDS for this to work over MRA. This way when Jabber connects externally, it automatically switches to UDS as the directory source and is able to pull contact photos for each user.

If an administrator already uses UDS prominently rather than LDAP and has contact photo resolution already configured, the administrator only needs to configure the Expressway and can skip the other steps.

## Configure

### The jabber-config.xml File

If you use custom jabber-config files, you will need to make sure that these files do not write over the global configuration file. In other words, the configuration you will add to the global configuration file to make this work must take precedence.

The configuration needs to be added in the <Directory></Directory> tags. It can be added in addition to any directory configuration already present.

```
<Directory>
<DirectoryServerType>UDS</DirectoryServerType>
<PhotoUriWithToken>http://webserverFQDNorIP/images/%%uid%%.jpg</PhotoUriWithToken>
<UdsPhotoUriWithToken>http://webserverFQDNorIP/images/%%uid%%.jpg</UdsPhotoUriWithToken>
<UdsServer>CallManager IP or FQDN</UdsServer>
<MinimumCharacterQuery>3</MinimumCharacterQuery>
</Directory>
```

Note : The "%%uid%%.jpg" portion of the URL tells Jabber to substitute the word "uid" with the user ID of each user. It is very important for Jabber to know where to find the image and whom it maps it to.

### UID Parameter Mapping in LDAP

Jabber needs to be able to map the image to the user. If you have an LDAP server, then you will need to configure the UID parameter for each user. The UID parameter will be the user ID for that user.

Step 1. Locate the users.

Step 2. Choose View > Advanced Features .

Step 3. Click the Attribute Editor tab.

Step 4. Configure the UID parameter for each user as its user ID.

Note : This needs to be done for every user. Once you complete this you need to perform a full sync in the LDAP Directory configuration in CallManager.

### Configure the Expressway-Core / Video Communications Manager (VCS) Control

Since Jabber will connect externally and communicate with all of the servers on the inside through the Expressway-Core (Expressway-C) / VCS Control, you need to configure the Expressway-C in order to allow Jabber to access the webserver that hosts the images.

Step 1. Log in to the VCS Control.

Step 2. Choose Configuration > Unified Communications > Configuration .

Step 3. Click Configure HTTP server allow list .

Step 3. Click New .

Step 4. Configure the IP address or FQDN of the webserver. Click Create entry .

## Verify

Use this section in order to confirm that your configuration works properly.

You should now be able to exit Jabber, delete the cache, and log back in externally. Contact photo resolution should work.

## Troubleshoot

This section provides information you can use to troubleshoot your configuration.

If contact photos do not work, complete these steps in order to troubleshoot the issue:

Step 1. Check the Jabber configuration file. There should be no missed tag brackets and the photo URl should be correct.

Step 2. The Jabber client should download the new configuration file. There must not be a custom configuration file that takes precedence.

Step 3. Check the LDAP server, the UID parameter needs to be correct for the users.

Step 4. If you use FQDNs , they will need to resolve from the Personal Computer (PC) that you use with Jabber. An nslookup will help confirm if this is a problem. Enter the URL for a user's image in the browser and see if it loads. If all of this works, the next step is to pull the Jabber problem report.

Step 5. The Expressway-C should be configured correctly to allow the server.

If all of the previous items have been checked, pull a Jabber problem report and get a packet capture from the PC. The problem report will show the modified photo URL for each user as it tries to resolve the image. If it says that it is unable to find the image, it might be a webserver or network issue.

Problem Report Keywords for Contact Issues

```
*Photos, Contacts, and Directory Search*
 
[csf.person.adsource] – Component level resource for directory and contact information.  Shows results of searches performed in Jabber.
 
[csf.person] – Component level information specifically about contacts in Jabber (and those searched) along with photo information
 
“BuddyListEventListener” – Keyword that shows up when Adding and Removing contacts
 
"onPhotoDownloadComplete" - When Jabber attempts to download contact photos, it will be noted by this keyword along with success or failure information.
 
“sendGetRequest” – URI Substitution for Photos will inclue this keyword in the URL request to the Web Server
 
“HttpClientImpl” – Keyword shows HTTP data and requests for photos, CURL, and WebEx Meetings
 
PersonResolutionHandler – This keyword is good for discovering where Jabber attempts to resolve contacts through AD and Outlook. May not be available in sub 9.6 versions.
 
“searchString” – This displays the letters a user types in the Jabber search or call field.
 
“string2search” – This keyword is the result of the searchString user entered information. It’s what Jabber will actually use to search in local cache, Outlook Address Book, and Active Directory
 
“getRecordWithPhoto” – When using AD as the source for photo downloads, this keyword provides the point at which Jabber downloads the photo from AD.
 
"ContactCard" – (11.x) The Contact Card feature used when hovering over a contact uses this keyword
```

### Contributed by Cisco Engineers

Fareed Warrad

Cisco TAC Engineer

Edited by Ishan Sambhi

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber