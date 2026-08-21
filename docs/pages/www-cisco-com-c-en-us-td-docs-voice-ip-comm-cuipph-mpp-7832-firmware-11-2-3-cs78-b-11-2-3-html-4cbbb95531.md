---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7832-firmware-11-2-3-cs78-b-11-2-3-html-4cbbb95531
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7832/firmware/11-2-3/cs78_b_11_2_3.html
retrieved_at: 2026-08-21T23:18:15.445346+00:00
---

Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 11.2(3)

# Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 11.2(3)

### Download Options

Updated: January 30, 2019

First Published: January 30, 2019

# Release Notes

Use these release notes with the Cisco IP Conference Phone 7832 Multiplatform Phones running SIP Firmware Release 11.2(3).

The following table describes the individual phone requirements.

Phone

Support Server

BroadSoft BroadWorks 22.0

MetaSphere CFS version 9.4

Asterisk 11.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Conference Phone 7832 Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                        following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/index.html

New and Changed Features

## Catalan Language Support

You and your user can set the phones to display text in Catalan. On the phone administration web page,  the Locale field in Voice > Regional contains the new ca-ES option.

### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

Cisco IP Phone 7800 Series Multiplatform Phones Provisioning Guide

## Control of Phone Configuration Reporting

You can control when the phone reports its configuration to the provisioning server. This is in addition to the standard report
                     upload that happens as part of the phone shutdown or restart.

Use the new Report to Server drop-down list on the phone administration web page, in Voice > Provisioning > Upload Configuration Options . When you choose On Local Change , the phone reports its configuration when any configuration parameter changes by an action on the phone or on the phone administration
                     web page. The phone waits for a few seconds after a change is made, and then reports the configuration. This wait time is
                     defined in the Upload Delay On Local Change field. Specify a value in number of seconds (10 minimum, 60 default, 900 maximum). This delay ensures that changes are reported
                     to the web server in batches, rather than reporting a single change at a time.

Alternately, the phone can report its configuration at regular intervals. Choose Periodically in the Report to Server drop-down list. Then, in the Periodic Upload to Server field, specify an interval in number of seconds (600 minimum, 3600 default, 2592000 (30 days) maximum).

In all cases, the report rule that you specify defines the configuration report that the phone sends. Two report upload destination
                     URLs are supported in the Report Rule field which provide flexibility in both destination and content of the uploaded report.

This feature has no user impact.

### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

Cisco IP Phone 7800 Series Multiplatform Phones Provisioning Guide

## Device Identifier in Uploaded Syslog Messages

You can now choose to include a device identifier for the phone in syslog messages that are uploaded to the syslog server.
                     While the IP address of a phone may change over time, the device identifier does not change. This can ease the process of
                     identifying the source of each message in a stream of incoming messages from multiple phones. The device identifier appears
                     after the timestamp in each message.

On the phone administration web page, you will see a new field named Syslog Identifier in Voice > System > Optional Network Configuration . You can also configure this setting in the XML configuration file. You can choose the type of device identifier to include:

none

the MAC address of the phone, in the standard colon-separated format, or as continuous upper case or lower case letters and
                           digits

the product serial number of the phone

This feature has no user impact.

### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

Cisco IP Phone 7800 Series Multiplatform Phones Provisioning Guide

## DND and Call Forwarding Sync Between the Phone and the Server

Besides Feature Key Synchronization (FKS), you can also enable the do not disturb (DND) and call forwarding synchronization
                     between the phone and the server through the XSI service. When both FKS and XSI Synchronization are enabled, FKS takes precedent
                     over XSI Synchronization.

You use the new fields DND Enable and CFWD Enable on the phone administration web page to enable or disable this feature. When enabled, the settings of DND and call forwarding
                     on the server are synchronized to the phone. The status changes made on the phone will also be synchronized to the server.

The fields are located in the XSI Line Service section from Voice > Ext (n) .

### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

Cisco IP Phone 7800 Series Multiplatform Phones Provisioning Guide

## Profile Account Authentication

Profile account authentication enables the phone to resynchronize the provisioning profile. You can specify a profile authentication
                     type for phone users to use.

The new field Profile Authentication Type replaces the Profile Account Enable field on the phone administration web page. The available options are: Disabled, Basic HTTP Authentication, and XSI Authentication.

When you disable this feature, the phone user can't enter the authentication account on the phone screen. When you specify
                     an authentication type, the phone user can use the provided credentials to resynchronize the provisioning profile either when
                     prompted or through the Profile account setup menu on the phone screen.

If XSI Authentication is specified as the authentication type, you can use either XSI login credentials or SIP credentials to resynchronize the
                     provisioning profile. Logging into XSI server with SIP credentials requires Broadsoft Broadworks 20.0 or later versions.

To use SIP credentials, set XSI Host Server , XSI Authentication Type (as SIP Credentials ), SIP Auth ID , and SIP Password in the XSI Phone Service section from the Voice > Phone tab on the phone administration web page.

### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 7832 Multiplatform Phones User Guide

## RFC 8188-Based HTTP Content Encryption for Configuration Files

The phone now supports RFC 8188-based HTTP content encryption with AES-128-GCM ciphering for configuration files. With this
                     encryption method, any entity can read the HTTP message headers. However, only the entities that know the Input Keying Material
                     (IKM) can read the payload. When the phone is provisioned with the IKM, the phone and the provisioning server can exchange
                     configuration files securely, while allowing third-party network elements to use the message headers for analytic and monitoring
                     purposes.

The new XML configuration parameter IKM_HTTP_Encrypt_Content holds the IKM on the phone. For security reasons, this parameter is not accessible on the phone administration web page.
                     It is also not visible in the phone's configuration file, which you can access from the phone's IP address or from the phone's
                     configuration reports sent to the provisioning server.

The phone continues to support the AES-256-CBC encryption method. As in the previous release, you specify the AES-256-CBC
                                 key with the --key keyword in profile rules and report rules. Which of the two encryption and decryption methods the phone applies depends on
                                 the inputs that you provide.

If you want to use the RFC 8188-based encryption, ensure the following:

Provision the phone with the IKM by specifying the IKM with the new XML parameter IKM_HTTP_Encrypt_Content in the configuration file that is sent from the provisioning server to the phone.

If this encryption is applied to the configuration files sent from the provisioning server to the phone, ensure that the Content-Encoding HTTP header in the configuration file has "aes128gcm" .

In the absence of this header, the AES-256-CBC method is given precedence. The phone applies AES-256-CBC decryption if a AES-256-CBC
                           key is present in a profile rule, regardless of IKM.

If you want the phone to apply this encryption to the configuration reports that it sends to the provisioning server, ensure
                           that there is no AES-256-CBC key specified in the report rule.

This feature has no user impact.

### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Provisioning Guide

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

## Remotely Initiated Problem Reports

You can initiate a phone problem report remotely. To do this, initiate a SIP-NOTIFY message from the server to the phone, with the Event specified as prt-gen . The phone generates a problem report using the Cisco Problem Report Tool (PRT), with the problem description "Remote PRT Trigger" . If you have configured an upload rule for problem reports, the phone also uploads the problem report according to the upload
                     rule.

You can see the status of the most recent problem report initiation on the phone administration web page > Info > Status . A new section called PRT Status shows the location of initiation and the status of the report generation, and the status of the report upload.

You can access a remotely-initiated problem report from the same location as locally-initiated problem reports on the phone
                     administration web page.

This feature has no user impact.

### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

## Support for Early Media and Preconditions

Your phone now supports early media negotiation and precondition signaling.

For an outgoing call, a SIP message from the phone includes the P-Early-Media header, which contains the status of the early
                     media stream. If the status in the header is not indicating that the network is blocking the early media stream, the phone
                     plays the early media instead of the ringback tone while waiting for the call to be connected.

Precondition signaling defers incoming call notifications until the phone receives the message that preconditions are satisfied
                     to establish the call.

### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

## Contact Search in Multiple Directories

You can now search for contacts by name in multiple directories simultaneously. The new All menu item in the Directories menu provides this function. The phone searches for the name in the following locations if Broadsoft directories are configured:

All Broadsoft directories

Enterprise directory

Group directory (included in the Enterprise directory)

Enterprise Common directory

Group Common directory

Personal directory

The LDAP directory, if configured

The personal address book on the phone

The search function behaves in a similar manner to the name-search function within individual directories. The search results
                     show both full and partial name matches. You can select a contact in the search results and then view contact details, add
                     the contact to the personal address book, and call the contact. You can also edit the number before making the call.

### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones User Guide

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

## Upgrade the Firmware

Use the information in this section to upgrade the firmware on Cisco IP Conference Phone 7832 Multiplatform Phones .

The Cisco IP Phone 7811, 7821, 7841, and 7861 Multiplatform Phones have a different firmware image. For more information,
                     see the Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 11.2(3), at this location:

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

Click this link:

https://software.cisco.com/download/home/286311381

On the Software Download web page that is displayed, ensure that IP Phone 7800 Series with Multiplatform Firmware is selected in the middle pane.

Select IP Conference Phone 7832 with Multiplatform Firmware in the right pane.

On the next page that is displayed, select Multiplatform Firmware .

On the next page that is displayed, select 11.2.3 in the All Releases > MPPv11 folder.

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Download the cmterm-7832.11-2-3MPP-398_REL.zip file.

Click Accept License Agreement .

Unzip the file and place the files in the appropriate location on your upgrade server.

The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade.

Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade .

In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Example:

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Example:

https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip7832.11-2-3MPP-398.loads

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing
                        impaired.

Caveats

## View Caveats

You can search for caveats (bugs) with the Cisco Bug Search tool.

Known caveats are graded according to severity level, and are either open or resolved.

Before you begin

### Before you begin

Click one of the following links:

To view all caveats that affect this release:

To view open caveats that affect this release:

To view resolved caveats that affect this release:

When prompted, log in with your Cisco.com user ID and password.

(Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

## Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Conference Phone 7832 Multiplatform Phones that use Firmware Release 11.2(3).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in the View Caveats .

CSCvo01547 When phone set ignore incoming call , current ringer volume is not right

## Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 7832 Multiplatform Phones that use Firmware Release 11.2(3).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in the View Caveats .

CSCvm70118 From missed call screen there is no way to go back

CSCvm04591 When two phones are in a dial-up connection, there is no call status in the Web GUI

CSCvm95087 Syslog is missing bootup logs and PRT is missing older log archives

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Server |
|---|---|
| Cisco IP Conference Phone 7832 Multiplatform Phones | BroadSoft BroadWorks 22.0 MetaSphere CFS version 9.4 Asterisk 11.0 |

| Note | The phone continues to support the AES-256-CBC encryption method. As in the previous release, you specify the AES-256-CBC
                                 key with the --key keyword in profile rules and report rules. Which of the two encryption and decryption methods the phone applies depends on
                                 the inputs that you provide. |
|---|---|

| Step 1 | Click this link: https://software.cisco.com/download/home/286311381 On the Software Download web page that is displayed, ensure that IP Phone 7800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select IP Conference Phone 7832 with Multiplatform Firmware in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | On the next page that is displayed, select 11.2.3 in the All Releases > MPPv11 folder. |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the cmterm-7832.11-2-3MPP-398_REL.zip file. |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.73.10.223/firmware/sip7832.11-2-3MPP-398.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip7832.11-2-3MPP-398.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319849&rls=11.2(3)&sb=anfr&bt=custV To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319849&rls=11.2(3)&sb=anfr&sts=open&bt=custV To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319849&rls=11.2(3)&sb=anfr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |