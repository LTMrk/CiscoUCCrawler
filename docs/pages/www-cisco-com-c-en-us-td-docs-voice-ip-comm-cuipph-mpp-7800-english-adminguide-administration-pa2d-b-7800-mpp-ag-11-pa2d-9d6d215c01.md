---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-english-adminguide-administration-pa2d-b-7800-mpp-ag-11-pa2d-9d6d215c01
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/english/adminguide/administration/pa2d_b_7800-mpp-ag-11/pa2d_b_7800-mpp-ag-11_chapter_0100.html
retrieved_at: 2026-09-01T15:41:14.458099+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

# Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Updated: April 29, 2019

Chapter: Third-Party Call Control Setup

## Chapter: Third-Party Call Control Setup

# Third-Party Call Control Setup

## Determine the Phone MAC Address

To add phones to the Third-Party Call Control system, determine the MAC address of a Cisco IP Phone.

Perform one of the following actions:

On the phone, press Applications > Status > Product Information , and look at the MAC address field.

Look at the MAC label on the back of the phone.

Display the web page for the phone and select Info > Status > Product Information .

## Network Configuration

The Cisco IP Phone is used as a part of a SIP network, because the phone supports Session Initiation Protocol (SIP). The Cisco
                           IP Phone is compatible with other SIP IP PBX call control systems, such as BroadSoft, MetaSwitch, and Asterisk.

Configuration of these systems is not described in this document. For more information, see the documentation for the SIP
                           PBX system to which you are connecting the Cisco IP Phone.

This document describes some common network configurations; however, your configuration can vary, depending on the type of
                           equipment that your service provider uses.

## Provisioning

Phones can be provisioned to download configuration profiles or updated firmware from a remote server when they are connected
                           to a network, when they are powered up, and at set intervals. Provisioning is typically part of high-volume, Voice-over-IP
                           (VoIP) deployments and is limited to service providers. Configuration profiles or updated firmware are transferred to the
                           device through use of TFTP, HTTP, or HTTPS.

The Cisco IP Phone 7800 Series Multiplatform Phones Provisioning Guide describes provisioning in detail.

## Report Current Phone Configuration to the Provisioning Server

You can configure the phone to report its full configuration, delta changes in the configuration, or the status data to the
                              server. You can add up to two URLs in the Report Rule field to specify the destination for the report, and include an optional encryption key.

When requesting delta configuration and status reports at once, separate report rules with a space . Include a destination upload-URL in each of the report rules. You can optionally precede the report rule by one or more
                              content arguments that are enclosed in square brackets [ ] .

When a report upload is attempted, the HTTP Report Method field specifies whether the HTTP Request that the phone sends should be an HTTP PUT or an HTTP POST . Choose:

PUT Method –To create a new report or overwrite an existing report at a known location on the server. For example, you may want to keep
                                    overwriting each report that you send and only store the most current configuration on the server.

POST Method –To send the report data to the server for processing, such as, by a PHP script. This approach provides more flexibility for
                                    storing the configuration information. For example, you may want to send a series of phone status reports and store all the reports on the server.

Use the following content arguments in the Report Rule field to send specific configuration reports:

Content Argument

Report Content

Full Configuration report

[--delta]

Configuration report containing only the latest changed fields

Report 1 contains ABC changes.

Report 2 contains XYZ changes ( not ABC and XYZ).

[--status]

Full Phone Status report

The preceding arguments can be combined with other arguments, such as, --key , --uid , and --pwd . These arguments control upload authentication and encryption, and are documented in the Profile Rule field.

When you specify the [--key <encryption key>] argument in the Report Rule , the phone applies AES-256-CBC encryption to the file (configuration, status, or delta), with the specified encryption key.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Provisioning > Upload Configuration Options .

Set the parameter for each of the five fields as described in Upload Configuration Options .

Click Submit All Changes .

Example of user inputs and the resulting actions of the phone and provisioning server for the Report Rule :

HTTP PUT ALL configuration:

If the HTTP report method is PUT, you enter the URL for the report rule in this format:

Then the phone will report the configuration data to http://my_http_server/config-mpp.xml .

HTTP PUT Changed Configuration

If the HTTP report method is PUT, you enter the URL for the report rule in this format:

Then the phone will report changed configuration to http://my_http_server/config-mpp-delta.xml .

HTTP PUT Encrypted Delta Configuration

If the HTTP report method is PUT, you enter the URL for the report rule in this format:

The phone will report status data to http://my_http_server/config-mpp-delta.enc.xml

On the report server side, the file can be decrypted like this: # openssl enc -d -aes-256-cbc -k test123 - in config-mpp-delta.enc-delta.enc -out cfg.xml

HTTP PUT Status Data

If the HTTP report method is PUT, you enter the URL for the report rule in this format:

The phone will report status data to http://my_http_server/config-mpp-status.xml

HTTP PUT Changed Configuration and Status

If the HTTP report method is PUT, you enter the URL for the report rule in this format:

The phone will report status data to http://my_http_server/config-mpp-status.xml and http://my_http_server/config-mpp-delta.xml

HTTP POST Changed Configuration

If the report method is POST, you enter the URL for the report rule in this format:

The report upload file format"

```
// report_upload.php content
<?php
$filename = “report_cfg.xml”;  // report file name
// where to put the file
$file = “/path/to/file”.$filename;
// get data from http post
$report_data = file_get_contents(‘php://input');
// save the post data to file
$file_put_contents($file, $report_data);
?>
```

The phone will upload changed data to http://my_http_server/report_cfg.xml

## Web-Based Configuration Utility

Your phone system administrator can allow you to view the phone statistics and modify some or all the parameters. This section
                              describes the features of the phone that you can modify with the phone web user interface.

### Access the Phone Web Page

Access the phone web page from a web browser on a computer that can reach the phone on the subnetwork.

If your service provider has disabled access to the configuration utility, contact the service provider before proceeding.

Ensure that the computer can communicate with the phone. No VPN in use.

Start a web browser.

Enter the IP address of the phone in your web browser address bar.

- User Access: http://<ip address>/user

- Admin Access: http://<ip address>/admin/advanced

- Admin Access: http://<ip address> , click Admin Login and click advanced

For example, http://10.64.84.147/admin

### Allow Web Access to the Cisco IP Phone

To view the phone parameters, enable the configuration profile. To make changes to any of the parameters, you must be able
                                 to change the configuration profile. Your system administrator might have disabled the phone option to make the phone web
                                 user interface viewable or writable.

For more information, see the Cisco IP Phone 7800 Series Multiplatform Phones Provisioning Guide .

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Click Voice > System .

In the System Configuration section, set Enable Web Server to Yes .

To update the configuration profile, click Submit All Changes after you modify the fields in the phone web user interface.

The phone reboots and the changes are applied.

To clear all changes that you made during the current session (or after you last clicked Submit All Changes ), click Undo All Changes . Values return to their previous settings.

### Determine the IP Address of the Phone

A DHCP server assigns the IP address, so the phone must be booted up and connected to the subnetwork.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Info > Status .

Scroll to IPv4 Information . Current IP displays the IP address.

Scroll to IPv6 Information . Current IP displays the IP address.

### View Download Status

You can view download status from the phone web page when your user has difficulties with phone registration.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Info > Download Status .

View firmware upgrade, provisioning, and custom CA status details as described in the Firmware Upgrade Status , , and .

### Web Administration
                           	 Tabs

Each tab contains parameters that are related to a particular
                                 		  feature. Some tasks require that you set multiple parameters in different tabs.

Info briefly describes each parameter that is available on
                                 		  the phone web user interface.

## Administrator and User Accounts

The Cisco IP Phone firmware provides specific administrator and user accounts. These accounts provide specific login privileges.
                           The administrator account name is admin ; the user account name is user . These account names cannot be changed.

The admin account gives the service provider or Value-added Reseller (VAR) configuration access to the Cisco IP phone. The user account gives limited and configurable control to the device end user.

The user and admin accounts can be password protected independently. If the service provider sets an administrator account password, you are
                           prompted for it when you click Admin Login . If the password does not yet exist, the screen refreshes and displays the administration parameters. No default passwords
                           are assigned to either the administrator or the user account. Only the administrator account can assign or change passwords.

The administrator account can view and modify all web profile parameters, including web parameters, that are available to
                           the user login. The Cisco IP Phone system administrator can further restrict the parameters that a user account can view and
                           modify through  use of  a provisioning profile.

Configuration parameters that are available to the user account are configurable on the Cisco IP Phone. User access to the
                           phone web user interface can be disabled.

### Enable User Access to the Phone Interface Menus

Use the admin account to enable or disable access to the phone web user interface by the user account. If the user account has access, users can set parameters through the phone web user interface.

Use phone profile provisioning to restrict the ability to configure individual parameters. Take Connection_Type parameter
                                             for example, when Phone-UI-User-Mode is set to Yes and, in the Resync file, the "ua" attribute can be:

Connection_Type ua= "rw" , you can read and change the information on the user phone web and phone screen.

Connection_Type ua= "ro" , you can only read, not change, the information on the user phone web and phone screen.

Connection_Type ua= "na" , you can not access the information on the user phone web or phone screen.

For more information on provisioning, see the Cisco IP Phone 7800 Series Multiplatform Phones Provisioning Guide .

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > System .

Under System Configuration in the Phone-UI-User-Mode field, choose Yes .

Click Submit All Changes .

### Access Administrative Options by Login

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

If prompted, enter the Admin Password .

### Access Administrative Options by IP Address

Enter the IP address of the Cisco IP Phone in a web browser and include the admin/ extension.

For example: http://10.64.84.147/admin/

| Perform one of the following actions: On the phone, press Applications > Status > Product Information , and look at the MAC address field. Look at the MAC label on the back of the phone. Display the web page for the phone and select Info > Status > Product Information . |
|---|

| Content Argument | Report Content |
|---|---|
| Default: Blank | Full Configuration report |
| [--delta] | Configuration report containing only the latest changed fields For example, Report 1 contains ABC changes. Report 2 contains XYZ changes ( not ABC and XYZ). |
| [--status] | Full Phone Status report |
| Note The preceding arguments can be combined with other arguments, such as, --key , --uid , and --pwd . These arguments control upload authentication and encryption, and are documented in the Profile Rule field. | Note | The preceding arguments can be combined with other arguments, such as, --key , --uid , and --pwd . These arguments control upload authentication and encryption, and are documented in the Profile Rule field. |
| Note | The preceding arguments can be combined with other arguments, such as, --key , --uid , and --pwd . These arguments control upload authentication and encryption, and are documented in the Profile Rule field. |

| Note | The preceding arguments can be combined with other arguments, such as, --key , --uid , and --pwd . These arguments control upload authentication and encryption, and are documented in the Profile Rule field. |
|---|---|

| Note | If you have provisioned the phone with Input Keying Material (IKM) and want the phone to apply RFC 8188-based encryption to
                                             the file, do not specify the --key argument. |
|---|---|

| Step 1 | Select Voice > Provisioning > Upload Configuration Options . |
|---|---|
| Step 2 | Set the parameter for each of the five fields as described in Upload Configuration Options . |
| Step 3 | Click Submit All Changes . Example of user inputs and the resulting actions of the phone and provisioning server for the Report Rule : HTTP PUT ALL configuration: If the HTTP report method is PUT, you enter the URL for the report rule in this format: http://my_http_server/config-mpp.xml Then the phone will report the configuration data to http://my_http_server/config-mpp.xml . HTTP PUT Changed Configuration If the HTTP report method is PUT, you enter the URL for the report rule in this format: [--delta]http://my_http_server/config-mpp-delta.xml; Then the phone will report changed configuration to http://my_http_server/config-mpp-delta.xml . HTTP PUT Encrypted Delta Configuration If the HTTP report method is PUT, you enter the URL for the report rule in this format: [--delta --key test123]http://my_http_server/config-mpp-delta.enc.xml; The phone will report status data to http://my_http_server/config-mpp-delta.enc.xml On the report server side, the file can be decrypted like this: # openssl enc -d -aes-256-cbc -k test123 - in config-mpp-delta.enc-delta.enc -out cfg.xml HTTP PUT Status Data If the HTTP report method is PUT, you enter the URL for the report rule in this format: [--status]http://my_http_server/config-mpp-status.xml; The phone will report status data to http://my_http_server/config-mpp-status.xml HTTP PUT Changed Configuration and Status If the HTTP report method is PUT, you enter the URL for the report rule in this format: [--status]http://my_http_server/config-mpp-status.xml [--delta]http://my_http_server/config-mpp-delta.xml The phone will report status data to http://my_http_server/config-mpp-status.xml and http://my_http_server/config-mpp-delta.xml HTTP POST Changed Configuration If the report method is POST, you enter the URL for the report rule in this format: [--delta]http://my_http_server/report_upload.php The report upload file format" // report_upload.php content
<?php
$filename = “report_cfg.xml”;  // report file name
// where to put the file
$file = “/path/to/file”.$filename;
// get data from http post
$report_data = file_get_contents(‘php://input');
// save the post data to file
$file_put_contents($file, $report_data);
?> The phone will upload changed data to http://my_http_server/report_cfg.xml |

| Step 1 | Ensure that the computer can communicate with the phone. No VPN in use. |
|---|---|
| Step 2 | Start a web browser. |
| Step 3 | Enter the IP address of the phone in your web browser address bar. User Access: http://<ip address>/user Admin Access: http://<ip address>/admin/advanced Admin Access: http://<ip address> , click Admin Login and click advanced For example, http://10.64.84.147/admin |

| Step 1 | Click Voice > System . |
|---|---|
| Step 2 | In the System Configuration section, set Enable Web Server to Yes . |
| Step 3 | To update the configuration profile, click Submit All Changes after you modify the fields in the phone web user interface. The phone reboots and the changes are applied. |
| Step 4 | To clear all changes that you made during the current session (or after you last clicked Submit All Changes ), click Undo All Changes . Values return to their previous settings. |

| Step 1 | Select Info > Status . |
|---|---|
| Step 2 | Scroll to IPv4 Information . Current IP displays the IP address. |
| Step 3 | Scroll to IPv6 Information . Current IP displays the IP address. |

| Step 1 | Select Info > Download Status . |
|---|---|
| Step 2 | View firmware upgrade, provisioning, and custom CA status details as described in the Firmware Upgrade Status , , and . |

| Note | Use phone profile provisioning to restrict the ability to configure individual parameters. Take Connection_Type parameter
                                             for example, when Phone-UI-User-Mode is set to Yes and, in the Resync file, the "ua" attribute can be: Connection_Type ua= "rw" , you can read and change the information on the user phone web and phone screen. Connection_Type ua= "ro" , you can only read, not change, the information on the user phone web and phone screen. Connection_Type ua= "na" , you can not access the information on the user phone web or phone screen. |
|---|---|

| Step 1 | Select Voice > System . |
|---|---|
| Step 2 | Under System Configuration in the Phone-UI-User-Mode field, choose Yes . |
| Step 3 | Click Submit All Changes . |

| If prompted, enter the Admin Password . |
|---|

| Enter the IP address of the Cisco IP Phone in a web browser and include the admin/ extension. For example: http://10.64.84.147/admin/ |
|---|