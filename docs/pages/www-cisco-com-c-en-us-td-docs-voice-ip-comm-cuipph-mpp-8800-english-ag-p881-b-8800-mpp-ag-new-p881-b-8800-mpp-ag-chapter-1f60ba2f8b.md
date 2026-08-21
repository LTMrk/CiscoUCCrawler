---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8800-english-ag-p881-b-8800-mpp-ag-new-p881-b-8800-mpp-ag-chapter-1f60ba2f8b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8800/english/AG/p881_b_8800-mpp-ag_new/p881_b_8800-mpp-ag_chapter_0110.html
retrieved_at: 2026-08-21T09:56:46.075150+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phone Administration Guide for Release 11.3(1) and Later

# Cisco IP Phone 8800 Series Multiplatform Phone Administration Guide for Release 11.3(1) and Later

Updated: November 21, 2019

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

Configuration report contains only the latest changed fields

For example,

Report 1 contains ABC changes.

Report 2 contains XYZ changes ( not ABC and XYZ).

[--status]

Full Phone Status report

The preceding arguments can be combined with other arguments, such as, --key , --uid , and --pwd . These arguments control upload authentication and encryption, and are documented in the Profile Rule field.

When you specify the [--key <encryption key>] argument in the Report Rule , the phone applies AES-256-CBC encryption to the file (configuration, status, or delta), with the specified encryption key.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Provisioning > Upload Configuration Options .

Set the parameter for each of the five fields as described in Parameters for Reporting the Phone Configuration to the Server .

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

### Parameters for Reporting the Phone Configuration to the Server

Specifies how the phone reports its current internal configuration to the provisioning server. The URLs in this field specify
                                             the destination for a report and can include an encryption key.

You can use the following keywords, encryption key, and file locations and names to control how you store the phone configuration
                                             information:

No keywords and only an XML file reports the entire configuration data to server.

[--status] keyword reports the status data to server.

[--delta] keyword reports the changed configuration to server.

[--key <encryption key>] keyword tells the phone to apply AES-256-CBC encryption with the specified encryption key to the configuration report, before
                                                   sending it to the server.

You can enclose the encryption key in double-quotes (") optionally.

Two rules used together as:

```
[--delta]http://my_http_server/config-mpp-delta.xml 
[--status]http://my_http_server/config-mpp-status.xml
```

Perform one of the following:

```
<Profile_Rule ua="na">
[--delta]http://my_http_server/config-mpp-delta.xml 
[--status]http://my_http_server/config-mpp-status.xml
</Profile_Rule>
```

In the phone web interface, enter the profile rule in this field.

HTTP Report method:

Specifies whether the HTTP Request that the phone sends should be an PUT or an POST .

PUT –To create a new report or overwrite an existing report at a known location on the server. For example, you may want to keep
                                                   overwriting each report that you send and only store the most current configuration on the server.

POST –To send the report data to the server for processing, such as, by a PHP script. This approach provides more flexibility for
                                                   storing the configuration information. For example, you may want to send a series of phone status reports and store all the reports on the server.

Perform one of the following:

```
<HTTP_Report_Method ua="na">PUT</HTTP_Report_Method>
```

In the phone web interface, select an HTTP report method.

Allowed values: PUT|POST

Default: POST

Defines when the phone reports its configuration to the provisioning servers.

On Request : The phone reports its configuration only when an administrator sends a sip notify event, or the phone restarts.

On Local Change : The phone reports its configuration when any configuration parameter changes by an action on the phone or on the phone administration
                                                   web page. The phone waits for a few seconds after a change is made, and then reports the configuration. This delay ensures
                                                   that changes are reported to the web server in batches, rather than reporting a single change at a time.

Periodically : The phone reports its configuration at regular intervals. The interval is expressed in seconds.

Perform one of the following:

```
<Report_to_Server ua="na">Periodically</Report_to_Server>
```

In the phone web interface, select an option from the list.

Allowed values: On Request|On Local Change|Periodically

Default: On Request

Defines the interval (in seconds) that the phone reports its configuration to the provisioning servers.

This field is used only when Report to Server is set to Periodically .

Perform one of the following:

```
<periodic_upload_to_server ua="na">3600</periodic_upload_to_server>
```

In the phone web interface, specify the interval in seconds.

Allowed values: An integer ranging between 600 and 259200

Default: 3600

Upload Delay On Local Change:

Defines the delay (in seconds) that the phone waits after a change is made, and then reports the configuration.

This field is used only when Report to Server is set to On Local Change .

Perform one of the following:

```
<Upload_Delay_On_Local_Change ua="na">60</Upload_Delay_On_Local_Change>
```

In the phone web interface, specify the delay in seconds.

Allowed values: An integer ranging between 10 and 900

Default: 60

| Perform one of the following actions: On the phone, press Applications > Status > Product Information , and look at the MAC address field. Look at the MAC label on the back of the phone. Display the web page for the phone and select Info > Status > Product Information . |
|---|

| Content Argument | Report Content |
|---|---|
| Default: Blank | Full Configuration report |
| [--delta] | Configuration report contains only the latest changed fields For example, Report 1 contains ABC changes. Report 2 contains XYZ changes ( not ABC and XYZ). |
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
| Step 2 | Set the parameter for each of the five fields as described in Parameters for Reporting the Phone Configuration to the Server . |
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

| Field | Description |
|---|---|
| Report Rule | Specifies how the phone reports its current internal configuration to the provisioning server. The URLs in this field specify
                                             the destination for a report and can include an encryption key. You can use the following keywords, encryption key, and file locations and names to control how you store the phone configuration
                                             information: No keywords and only an XML file reports the entire configuration data to server. [--status] keyword reports the status data to server. [--delta] keyword reports the changed configuration to server. [--key <encryption key>] keyword tells the phone to apply AES-256-CBC encryption with the specified encryption key to the configuration report, before
                                                   sending it to the server. You can enclose the encryption key in double-quotes (") optionally. Note If you have provisioned the phone with Input Keying Material (IKM) and want the phone to apply RFC 8188-based encryption to
                                                            the file, do not specify a AES-256-CBC encryption key. Two rules used together as: [--delta]http://my_http_server/config-mpp-delta.xml 
[--status]http://my_http_server/config-mpp-status.xml Caution If you need to use the [--delta]xml-delta file rule and the [--status]xml-status file rule together, you must separate the
                                                      two rules with a space . Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Profile_Rule ua="na">
[--delta]http://my_http_server/config-mpp-delta.xml 
[--status]http://my_http_server/config-mpp-status.xml
</Profile_Rule> In the phone web interface, enter the profile rule in this field. | Note | If you have provisioned the phone with Input Keying Material (IKM) and want the phone to apply RFC 8188-based encryption to
                                                            the file, do not specify a AES-256-CBC encryption key. | Caution | If you need to use the [--delta]xml-delta file rule and the [--status]xml-status file rule together, you must separate the
                                                      two rules with a space . |
| Note | If you have provisioned the phone with Input Keying Material (IKM) and want the phone to apply RFC 8188-based encryption to
                                                            the file, do not specify a AES-256-CBC encryption key. |
| Caution | If you need to use the [--delta]xml-delta file rule and the [--status]xml-status file rule together, you must separate the
                                                      two rules with a space . |
| HTTP Report method: | Specifies whether the HTTP Request that the phone sends should be an PUT or an POST . PUT –To create a new report or overwrite an existing report at a known location on the server. For example, you may want to keep
                                                   overwriting each report that you send and only store the most current configuration on the server. POST –To send the report data to the server for processing, such as, by a PHP script. This approach provides more flexibility for
                                                   storing the configuration information. For example, you may want to send a series of phone status reports and store all the reports on the server. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <HTTP_Report_Method ua="na">PUT</HTTP_Report_Method> In the phone web interface, select an HTTP report method. Allowed values: PUT\|POST Default: POST |
| Report to Server: | Defines when the phone reports its configuration to the provisioning servers. On Request : The phone reports its configuration only when an administrator sends a sip notify event, or the phone restarts. On Local Change : The phone reports its configuration when any configuration parameter changes by an action on the phone or on the phone administration
                                                   web page. The phone waits for a few seconds after a change is made, and then reports the configuration. This delay ensures
                                                   that changes are reported to the web server in batches, rather than reporting a single change at a time. Periodically : The phone reports its configuration at regular intervals. The interval is expressed in seconds. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Report_to_Server ua="na">Periodically</Report_to_Server> In the phone web interface, select an option from the list. Allowed values: On Request\|On Local Change\|Periodically Default: On Request |
| Periodic Upload to Server: | Defines the interval (in seconds) that the phone reports its configuration to the provisioning servers. This field is used only when Report to Server is set to Periodically . Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <periodic_upload_to_server ua="na">3600</periodic_upload_to_server> In the phone web interface, specify the interval in seconds. Allowed values: An integer ranging between 600 and 259200 Default: 3600 |
| Upload Delay On Local Change: | Defines the delay (in seconds) that the phone waits after a change is made, and then reports the configuration. This field is used only when Report to Server is set to On Local Change . Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Upload_Delay_On_Local_Change ua="na">60</Upload_Delay_On_Local_Change> In the phone web interface, specify the delay in seconds. Allowed values: An integer ranging between 10 and 900 Default: 60 |

| Note | If you have provisioned the phone with Input Keying Material (IKM) and want the phone to apply RFC 8188-based encryption to
                                                            the file, do not specify a AES-256-CBC encryption key. |
|---|---|

| Caution | If you need to use the [--delta]xml-delta file rule and the [--status]xml-status file rule together, you must separate the
                                                      two rules with a space . |
|---|---|