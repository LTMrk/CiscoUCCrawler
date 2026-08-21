---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-800-series-firmware-1-5-0-w800-b-wireless-rln-150-html-21320a72d3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/800-series/firmware/1-5-0/w800_b_wireless_rln_150.html
retrieved_at: 2026-08-21T23:36:03.371919+00:00
---

Webex Wireless Phone 840 and 860 Release Notes for Firmware Release 1.5(0)

# Webex Wireless Phone 840 and 860 Release Notes for Firmware Release 1.5(0)

### Download Options

Updated: April 20, 2022

First Published: April 18, 2022

# Webex Wireless Phone 840 and 860 release notes for firmware release 1.5(0)

These release notes support the Webex Wireless Phone 840 and 860 software release 1.5(0). These wireless smartphones require:

Cisco Unified
                        				Communications Manager ( Unified Communications Manager ):

Minimum: 11.5(1)

Recommended: 12.5(1), 14.0(1), or higher

Supported Wi-Fi access point.

See the Cisco Webex Wireless Phone 840 and 860 Wireless LAN Deployment Guide for supported access point options.

## New and Changed
               	 Features

The following sections describe the features that are new or have
                  		changed in this release.

### New Webex Wireless Phone Configuration Management tool to deploy and configure multiple phones

You can use our new Webex Wireless Phone Configuration Management tool to deploy and configure multiple Webex Wireless Phones without an Enterprise Mobility Management (EMM) application . You can also use this tool to restrict apps and settings that you don't want users to access.

When you use the new Webex Wireless Phone Configuration Management tool to set up phones, the phones display the apps on a Smart Launcher screen. The Smart Launcher can have:

A single app —There's only one app on the phone. When you turn on the phone, the app is open.

Multiple apps —There are multiple apps on the phone.

You access the Webex Wireless Phone Configuration Management tool at this url: https://configure.cisco.com/ . To see how to use the tool to enroll and configure your phones, see the Webex Wireless Phone Configuration Management tool workflow .

#### Where to find more information

Webex Wireless Phone 840 and 860 user guide

Webex Wireless Phone quick reference guides

Webex Wireless Phone 840 and 860 administration guide for Cisco Unified Communications Manager

Webex Wireless Phone 840 and 860 Wireless LAN Deployment Guide

### Date and time set from local network

You can now define a server in DHCP option 42 to provide Network Time Protocol (NTP) service in case the NTP server isn't
                        available. By default, the phones get their time source from the NTP server set in the NTP Server Address field of the Custom Settings app. If the NTP server isn't available, for example there's no internet, the phones get their time source from the server
                        that you define in DHCP option 42.

#### Where to find more information

Webex Wireless Phone 840 and 860 administration guide for Cisco Unified Communications Manager

Webex Wireless Phone 840 and 860 Wireless LAN Deployment Guide

## Related
               	 Documentation

Use the following sections to obtain related information.

### Webex Wireless Phone 840 and 860 documentation

Find documentation specific to your phone model and language on the product support page for the Webex Wireless Phone . From this page, you can also find the Deployment Guide .

### Cisco Unified
                     				Communications Manager Documentation

See the Cisco Unified
                              				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                           				Communications Manager release on the product support page.

## Installation

### Download the COP files for release 1.5(0)

Download the correct device enabler QED installer and software Cisco Options Package (COP) files for your phone and Cisco Unified
                           				Communications Manager version, so that you can install them on the Cisco Unified
                           				Communications Manager servers in the cluster.

Go to the Software Download page for the phones.

From Webex Wireless Phone , choose the phone model.

Choose Latest Releases > QED Installer , and then click either Download or Add to Cart for the required device enabler QED installer COP file.

Device Enabler QED Installer COP file for 840 : cmterm-840-installer.1-5-0.k4.cop.sha512

Device Enabler QED Installer COP file for 860 : cmterm-860-installer.1-5-0.k4.cop.sha512

To access more details about the COP files, such as the Checksum details and a link to the Readme file, hover the mouse pointer over the filename.

If you chose to click Download , follow the prompts.

Choose Latest Releases > 1.5(0) , and then click either the Download or Add to Cart button for the required software COP file.

Software COP file for 840 : cmterm-840-sip.1-5-0-1252-42517.k4.cop.sha512

Software COP file for 860 : cmterm-860-sip.1-5-0-1676-42517.k4.cop.sha512

If you chose to download the file, follow the prompts.

If you chose to add the files to your cart, click the Cart when you are ready to download all the files.

### Load the COP files to Cisco Unified
                     				Communications Manager

You must install the Webex Wireless Phone 840 and 860 device enabler QED installer and phone software Cisco Options Package (COP) files into each Cisco Unified
                           				Communications Manager ( Unified Communications Manager ) in the cluster.

These COP files are signed with the sha512 checksum. Cisco Unified
                                       				Communications Manager versions before version 14 don't automatically include support for sha512.

For the first installation, install the device enabler QED installer file first and then the software file.

For future software updates, there is not always a corresponding device enabler QED installer update. When a software update is available, check the latest version of the device enabler QED installer file to see whether you also must update it.

With each new software release, the Cisco apps are also updated in the Play Store. However, if you manage the phones through
                                    an Enterprise Mobility Management (EMM) application , we recommend that you update the firmware on the phones to minimize any risk of app incompatibility.

Before you begin

#### Before you begin

Download the device enabler QED installer and phone software COP files from the Software Download site.

If you want to use the Webex Wireless Phone Configuration Management tool to configure your phones, install release 1.5(0) files or newer.

If you have Unified Communications Manager version 11.5 or 12.5 and don't already have sha512 checksum support enabled, install ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn.

Choose an appropriate time to perform this task. As part of this task you must restart each Unified Communications Manager in the cluster after you install a device enabler QED installer COP file, unless your version of Unified Communications Manager offers an alternate process that does not require a reboot.

See the Manage Device Firmware section of the Administration Guide for Cisco Unified Communications Manager for your Unified Communications Manager version, to see if it allows an installation process that does not require a reboot.

In each Unified Communications Manager in the cluster, select Cisco Unified OS Administration > Software Upgrades > Install/Upgrade .

Enter the Software Location data.

Click Next .

Select the COP (.cop.sha512) file.

If the COP file doesn't appear in the available files list, ensure that you enable sha512 checksum support.

Click Next to download the COP file to Unified Communications Manager .

Check that the file checksum details are correct.

Click Next to install the COP file on Unified Communications Manager .

Click Install Another and repeat steps 2–7 to install another COP file.

Perform the following actions based on the COP files that you installed.

If you installed a device enabler QED installer COP file:

For 11.5(1)SU4 and lower :

Reboot all Unified Communications Manager nodes through Cisco Unified OS Administration > Settings > Version > Restart .

For 11.5(1)SU5 and higher or 12.5(1) and higher :

Restart the Cisco Tomcat service on all Unified Communications Manager nodes.

If running the Unified Communications Manager service on the publisher node, restart the service on the publisher node only. You do not need to restart the Cisco Call
                                                      Manager Service on subscriber nodes.

If you installed a software COP file, restart the Cisco TFTP service for all nodes running the Cisco TFTP service.

### Install manufacturing CA certificates

The phones use a new manufacturing certificate authority (CA). Until Cisco Unified
                           				Communications Manager ( Unified Communications Manager ) includes these new certificates, you must manually add the new root and intermediate certificates to the certificate chain
                        to trust the new Manufacturing Installed Certificates (MIC). After you add the new certificates to the trust chain, the MICs
                        can be used for trust services such as SIP TLS, Configuration File Encryption, and LSC Certificate distribution.

Download the missing root and intermediate certificates from the externally available Cisco PKI website. The missing certificates to complete the trust chain up to and including the root for the new MICs are:

Cisco Manufacturing CA III (cmca3) - Intermediate

Cisco Basic Assurance Root CA 2099 (cbarc2099) - Root for Cisco Manufacturing CA III

From your web browser, log in to the Cisco Unified Operating System Administration web page.

Under the Security menu, select Certificate Management .

Select Upload Certificate/Certificate Chain .

Select CallManager-trust for the Certificate Purpose , browse to the certificate, then select Upload .

Repeat this step for all certificates on the Unified Communications Manager Publisher only as the certificate replicates to all other Unified Communications Manager nodes.

Select CAPF-trust for the Certificate Purpose, browse to the certificate, then select Upload .

Repeat this step for all certificates on all Unified Communications Manager nodes as the certificate will not replicate to all other Unified Communications Manager nodes automatically.

## Limitations and Restrictions

## Caveats

### View bugs

You can search for bugs using the Cisco Bug Search Tool.

Known bugs are graded according to severity level, and can be either open or resolved.

For more information about how to use the Bug Search Tool, see Bug Search Tool Help .

Before you begin

#### Before you begin

To view bugs, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

### SUMMARY STEPS

- Click the following links to view bugs for the 1.5(0) release of the Webex Wireless Phone 840 and 860 :

- When prompted, log in with your Cisco.com user ID and password.

- (Optional) Enter the bug ID number in the Search For field, then press Enter .

### DETAILED STEPS

Click the following links to view bugs for the 1.5(0) release of the Webex Wireless Phone 840 and 860 :

View all bugs .

View all open bugs .

View all resolved bugs .

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search For field, then press Enter .

### Open bugs

The following list contains a snapshot of severity 1, 2, and 3 bugs that were open at the time of the Webex Wireless Phone 840 and 860 software release 1.5(0).

For an updated view of open bugs or to view more information about specific bugs, access the Bug Search Tool as described in View bugs .

CSCwa01438 840/860 logs out of EMCC when the phone is restarted

CSCwb11302 When using EMMA the EAP Phase 2 auth options for PEAP should only be MSCHAPV2 and GTC

CSCwb31325 860 phone displays the wrong number after transfer

### Resolved bugs

The following list contains a snapshot of severity 1, 2, and 3 bugs that were resolved at the time of the Webex Wireless Phone 840 and 860 software release 1.5(0).

For an updated view of resolved bugs or to view more information about specific bugs, access the Bug Search Tool as described in View bugs .

CSCvz70007 840 phone continues to play call waiting tone periodically after the call has ended

CSCvz81223 840/860 is not refreshing the Personal Directory list every 2 hours as expected

CSCvz93775  Battery Percentage option in the Custom Settings app is not managing the Settings option correctly

CSCvz93791 Auto-rotate Screen option is missing if Disabled in Custom Settings app then set to User Controlled

CSCvz93805  Auto-rotate Screen option in the Custom Settings app is not managing the Settings option correctly

| Step 1 | Go to the Software Download page for the phones. |
|---|---|
| Step 2 | From Webex Wireless Phone , choose the phone model. |
| Step 3 | Choose Latest Releases > QED Installer , and then click either Download or Add to Cart for the required device enabler QED installer COP file. Device Enabler QED Installer COP file for 840 : cmterm-840-installer.1-5-0.k4.cop.sha512 Device Enabler QED Installer COP file for 860 : cmterm-860-installer.1-5-0.k4.cop.sha512 Note To access more details about the COP files, such as the Checksum details and a link to the Readme file, hover the mouse pointer over the filename. Note If you chose to click Download , follow the prompts. | Note | To access more details about the COP files, such as the Checksum details and a link to the Readme file, hover the mouse pointer over the filename. | Note | If you chose to click Download , follow the prompts. |
| Note | To access more details about the COP files, such as the Checksum details and a link to the Readme file, hover the mouse pointer over the filename. |
| Note | If you chose to click Download , follow the prompts. |
| Step 4 | Choose Latest Releases > 1.5(0) , and then click either the Download or Add to Cart button for the required software COP file. Software COP file for 840 : cmterm-840-sip.1-5-0-1252-42517.k4.cop.sha512 Software COP file for 860 : cmterm-860-sip.1-5-0-1676-42517.k4.cop.sha512 Note If you chose to download the file, follow the prompts. If you chose to add the files to your cart, click the Cart when you are ready to download all the files. | Note | If you chose to download the file, follow the prompts. If you chose to add the files to your cart, click the Cart when you are ready to download all the files. |
| Note | If you chose to download the file, follow the prompts. If you chose to add the files to your cart, click the Cart when you are ready to download all the files. |

| Note | To access more details about the COP files, such as the Checksum details and a link to the Readme file, hover the mouse pointer over the filename. |
|---|---|

| Note | If you chose to click Download , follow the prompts. |
|---|---|

| Note | If you chose to download the file, follow the prompts. If you chose to add the files to your cart, click the Cart when you are ready to download all the files. |
|---|---|

| Note | These COP files are signed with the sha512 checksum. Cisco Unified
                                       				Communications Manager versions before version 14 don't automatically include support for sha512. |
|---|---|

| Note | With each new software release, the Cisco apps are also updated in the Play Store. However, if you manage the phones through
                                    an Enterprise Mobility Management (EMM) application , we recommend that you update the firmware on the phones to minimize any risk of app incompatibility. |
|---|---|

| Note | If you want to use the Webex Wireless Phone Configuration Management tool to configure your phones, install release 1.5(0) files or newer. |
|---|---|

| Caution | Choose an appropriate time to perform this task. As part of this task you must restart each Unified Communications Manager in the cluster after you install a device enabler QED installer COP file, unless your version of Unified Communications Manager offers an alternate process that does not require a reboot. See the Manage Device Firmware section of the Administration Guide for Cisco Unified Communications Manager for your Unified Communications Manager version, to see if it allows an installation process that does not require a reboot. |
|---|---|

| Step 1 | In each Unified Communications Manager in the cluster, select Cisco Unified OS Administration > Software Upgrades > Install/Upgrade . |
|---|---|
| Step 2 | Enter the Software Location data. |
| Step 3 | Click Next . |
| Step 4 | Select the COP (.cop.sha512) file. Note If the COP file doesn't appear in the available files list, ensure that you enable sha512 checksum support. | Note | If the COP file doesn't appear in the available files list, ensure that you enable sha512 checksum support. |
| Note | If the COP file doesn't appear in the available files list, ensure that you enable sha512 checksum support. |
| Step 5 | Click Next to download the COP file to Unified Communications Manager . |
| Step 6 | Check that the file checksum details are correct. |
| Step 7 | Click Next to install the COP file on Unified Communications Manager . |
| Step 8 | Click Install Another and repeat steps 2–7 to install another COP file. |
| Step 9 | Perform the following actions based on the COP files that you installed. If you installed a device enabler QED installer COP file: For 11.5(1)SU4 and lower : Reboot all Unified Communications Manager nodes through Cisco Unified OS Administration > Settings > Version > Restart . For 11.5(1)SU5 and higher or 12.5(1) and higher : Restart the Cisco Tomcat service on all Unified Communications Manager nodes. If running the Unified Communications Manager service on the publisher node, restart the service on the publisher node only. You do not need to restart the Cisco Call
                                                      Manager Service on subscriber nodes. If you installed a software COP file, restart the Cisco TFTP service for all nodes running the Cisco TFTP service. |

| Note | If the COP file doesn't appear in the available files list, ensure that you enable sha512 checksum support. |
|---|---|

| Step 1 | Download the missing root and intermediate certificates from the externally available Cisco PKI website. The missing certificates to complete the trust chain up to and including the root for the new MICs are: Cisco Manufacturing CA III (cmca3) - Intermediate Cisco Basic Assurance Root CA 2099 (cbarc2099) - Root for Cisco Manufacturing CA III |
|---|---|
| Step 2 | From your web browser, log in to the Cisco Unified Operating System Administration web page. |
| Step 3 | Under the Security menu, select Certificate Management . |
| Step 4 | Select Upload Certificate/Certificate Chain . |
| Step 5 | Select CallManager-trust for the Certificate Purpose , browse to the certificate, then select Upload . Repeat this step for all certificates on the Unified Communications Manager Publisher only as the certificate replicates to all other Unified Communications Manager nodes. |
| Step 6 | Select CAPF-trust for the Certificate Purpose, browse to the certificate, then select Upload . Repeat this step for all certificates on all Unified Communications Manager nodes as the certificate will not replicate to all other Unified Communications Manager nodes automatically. |

| Step 1 | Click the following links to view bugs for the 1.5(0) release of the Webex Wireless Phone 840 and 860 : View all bugs . View all open bugs . View all resolved bugs . |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search For field, then press Enter . |