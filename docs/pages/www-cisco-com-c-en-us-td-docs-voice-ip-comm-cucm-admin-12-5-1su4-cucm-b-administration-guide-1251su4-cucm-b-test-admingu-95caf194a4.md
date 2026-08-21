---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-cucm-b-administration-guide-1251su4-cucm-b-test-admingu-95caf194a4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/cucm_b_administration-guide-1251su4/cucm_b_test-adminguide_chapter_010101.html
retrieved_at: 2026-08-21T16:01:12.250026+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: April 8, 2025

Chapter: Call Home

## Chapter: Call Home

# Call Home

## Call Home

This chapter provides an overview of the Unified Communications Manager Call Home service and describes how to configure the
                           Unified Communications Manager Call Home feature. The Call Home feature allows to communicate and send the diagnostic alerts,
                           inventory, and other messages to the Smart Call Home back-end server.

### Smart Call Home

Smart Call Home provides proactive diagnostics, real-time alerts, and remediation on a range of Cisco devices for higher network
                                 availability and increased operational efficiency. It accomplishes the same by receiving and analyzing the diagnostic alerts,
                                 inventory, and other messages from Smart Call Home enabled Unified Communications Manager. This particular capability of Unified
                                 Communications Manager is called as Unified Communications Manager Call Home.

Smart Call Home offers:

Higher network availability through proactive, fast issue resolution by:

Identifying issues quickly with continuous monitoring, real-time, proactive alerts, and detailed diagnostics.

Making you aware of potential problems by providing alerts that are specific to only those types of devices in the network.
                                             Resolving critical problems faster with direct, automatic access to experts at Cisco Technical Assistance Center (TAC).

Increased operational efficiency by providing customers the ability to:

Use staff resources more efficiently by reducing troubleshooting time.

Fast, web-based access to needed information that provides customers the ability to:

Review all Call Home messages, diagnostics, and recommendations in one place.

Check Service Request status quickly.

View the most up-to-date inventory and configuration information for all Call Home devices.

Smart Call Home contains modules that perform the following tasks:

Notify Customer of Call Home messages.

Provide impact analysis and remediation steps.

For more information about Smart Call Home, see the Smart Call Home page at this location:

http://www.cisco.com/en/US/products/ps7334/serv_home.html

#### Information for Smart Call Home Certificates Renewal

From Cisco Release 10.5(2) onwards, administrators have to manually upload the new certificates for any renewal request to
                                 continue support for Smart Call Home feature. You can upload certificates through Cisco Unified Operating System Administration
                                 web GUI. Go to Security > Certificate Management > Upload Certificate/Certificate chain . Choose tomcat-trust as the Certificate Purpose, and upload the certificate from the saved destination.

The following certificate with extension .PEM should be uploaded to tomcat-trust.

Ensure that the administrator copy the entire string and include -----BEGIN CERTIFICATE----- and -----END CERTIFICATE-----,
                                             paste it into a text file, and save it with the extension .PEM.

-----BEGIN CERTIFICATE-----

MIIFtzCCA5+gAwIBAgICBQkwDQYJKoZIhvcNAQEFBQAwRTELMAkGA1UEBhMCQk0x

GTAXBgNVBAoTEFF1b1ZhZGlzIExpbWl0ZWQxGzAZBgNVBAMTElF1b1ZhZGlzIFJv

b3QgQ0EgMjAeFw0wNjExMjQxODI3MDBaFw0zMTExMjQxODIzMzNaMEUxCzAJBgNV

BAYTAkJNMRkwFwYDVQQKExBRdW9WYWRpcyBMaW1pdGVkMRswGQYDVQQDExJRdW9

WYWRpcyBSb290IENBIDIwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQCa

GMpLlA0ALa8DKYrwD4HIrkwZhR0In6spRIXzL4GtMh6QRr+jhiYaHv5+HBg6XJxg

Fyo6dIMzMH1hVBHL7avg5tKifvVrbxi3Cgst/ek+7wrGsxDp3MJGF/hd/aTa/55J

WpzmM+Yklvc/ulsrHHo1wtZn/qtmUIttKGAr79dgw8eTvI02kfN/+NsRE8Scd3bB

rrcCaoF6qUWD4gXmuVbBlDePSHFjIuwXZQeVikvfj8ZaCuWw419eaxGrDPmF60Tp

+ARz8un+XJiM9XOva7R+zdRcAitMOeGylZUtQofX1bOQQ7dsE/He3fbE+Ik/0XX1

ksOR1YqI0JDs3G3eicJlcZaLDQP9nL9bFqyS2+r+eXyt66/3FsvbzSUr5R/7mp/i

Ucw6UwxI5g69ybR2BlLmEROFcmMDBOAENisgGQLodKcftslWZvB1JdxnwQ5hYIiz

PtGo/KPaHbDRsSNU30R2be1B2MGyIrZTHN81Hdyhdyox5C315eXbyOD/5YDXC2Og

/zOhD7osFRXql7PSorW+8oyWHhqPHWykYTe5hnMz15eWniN9gqRMgeKh0bpnX5UH

oycR7hYQe7xFSkyyBNKr79X9DFHOUGoIMfmR2gyPZFwDwzqLID9ujWc9Otb+fVuI

yV77zGHcizN300QyNQliBJIWENieJ0f7OyHj+OsdWwIDAQABo4GwMIGtMA8GA1Ud

EwEB/wQFMAMBAf8wCwYDVR0PBAQDAgEGMB0GA1UdDgQWBBQahGK8SEwzJQTU7tD2

A8QZRtGUazBuBgNVHSMEZzBlgBQahGK8SEwzJQTU7tD2A8QZRtGUa6FJpEcwRTEL

MAkGA1UEBhMCQk0xGTAXBgNVBAoTEFF1b1ZhZGlzIExpbWl0ZWQxGzAZBgNVBAMT

ElF1b1ZhZGlzIFJvb3QgQ0EgMoICBQkwDQYJKoZIhvcNAQEFBQADggIBAD4KFk2f

BluornFdLwUvZ+YTRYPENvbzwCYMDbVHZF34tHLJRqUDGCdViXh9duqWNIAXINzn

g/iN/Ae42l9NLmeyhP3ZRPx3UIHmfLTJDQtyU/h2BwdBR5YM++CCJpNVjP4iH2Bl

fF/nJrP3MpCYUNQ3cVX2kiF495V5+vgtJodmVjB3pjd4M1IQWK4/YY7yarHvGH5K

WWPKjaJW1acvvFYfzznB4vsKqBUsfU16Y8Zsl0Q80m/DShcK+JDSV6IZUaUtl0Ha

B0+pUNqQjZRG4T7wlP0QADj1O+hA4bRuVhogzG9Yje0uRY/W6ZM/57Es3zrWIozc

hLsib9D45MY56QSIPMO661V6bYCZJPVsAfv4l7CUW+v90m/xd2gNNWQjrLhVoQPR

TUIZ3Ph1WVaj+ahJefivDrkRoHy3au000LYmYjgahwz46P0u05B/B5EqHdZ+XIWD

mbA4CD/pXvk1B+TJYm5Xf6dQlfe6yJvmjqIBxdZmv3lh8zwc4bmCXF2gw+nYSL0Z

ohEUGW6yhhtoPkg3Goi3XZZenMfvJ2II4pEZXNLxId26F0KCl3GBUzGpn/Z9Yr9y

4aOTHcyKJloJONDO1w2AFrR4pTqHTI2KpdVGl/IsELm8VCLAAVBpQ570su9t+Oza

8eOx79+Rj1QqCyXBJhnEUhAFZdWCEOrCMc0u

-----END CERTIFICATE-----

### Anonymous Call Home

The Anonymous Call Home feature is a sub-feature of the Smart Call Home feature that
                                 allows Cisco to anonymously receive inventory and telemetry
                                 messages. Enable this feature to keep your identification anonymous.

The Unified Communications Manager sends only inventory and telemetry messages and not diagnostic and configuration information
                                          to Smart Call Home back-end.

It
                                          will not send any user related information (for example, registered devices and
                                          upgrade history).

Anonymous call home option does not require
                                          registration or entitlement for Smart Call Home feature with
                                          Cisco.

The
                                          inventory and telemetry messages are sent periodically (first day of every month) to the
                                          Call Home back-end.

Include Trace logs and Diagnostic Information option is disabled if Cisco Unified Communications Manager is configured to use Anonymous Call Home.

Inventory messages contains information about the cluster, nodes,
                                 				and license.

The following table lists the inventory messages for Smart Call Home and Anonymous Call Home.

Inventory messages

Smart Call Home

Anonymous Call Home

Contact Email

Applicable

Not Applicable

Contact Phone number

Applicable

Not Applicable

Street Address

Applicable

Not Applicable

Server Name

Applicable

Not Applicable

Server IP Address

Applicable

Not Applicable

Licence Server

Applicable

Not Applicable

OS Version

Applicable

Applicable

Model

Applicable

Applicable

Serial Number

Applicable

Applicable

CPU Speed

Applicable

Applicable

RAM

Applicable

Applicable

Storage Partition

Applicable

Applicable

Firmware version

Applicable

Applicable

BIOS Version

Applicable

Applicable

BIOS Information

Applicable

Applicable

Raid Configuration

Applicable

Applicable

Active Services

Applicable

Applicable

Publisher Name

Applicable

Not Applicable

Publisher IP

Applicable

Not Applicable

Product ID

Applicable

Applicable

Active Version

Applicable

Applicable

Inactive Version

Applicable

Applicable

Product Short name

Applicable

Applicable

Telemetry messages contain information about the number of devices (IP phones, gateways, conference bridge, and so on) for
                                 each device type that is available on a Unified Communications Manager cluster. The telemetry data contains the device count
                                 for the entire cluster.

The following table lists the telemetry messages for Smart Call Home and Anonymous Call Home.

Telemetry messages

Smart Call Home

Anonymous Call Home

Contact Email

Applicable

Not Applicable

Contact Phone number

Applicable

Not Applicable

Street Address

Applicable

Not Applicable

Server name

Applicable

Not Applicable

CM User Count

Applicable

Not Applicable

Serial Number

Applicable

Applicable

Publisher name

Applicable

Not Applicable

Device count and Model

Applicable

Applicable

Phone User Count

Applicable

Applicable

CM Call Activity

Applicable

Applicable

Registered Device count

Applicable

Not Applicable

Upgrade history

Applicable

Not Applicable

System Status

Applicable for Host name, Date, Locale, Product Version, OS
                                             Version, Licence MAC, Up Time, MP Stat, Memory Used, Disk Usage, Active and
                                             Inactive partition used, and DNS

Applicable for Date, Locale, Product Version, OS Version, Licence MAC, Up Time, Memory Used, Disk Usage, and Active and Inactive
                                             partition used

Configuration messages contain information about the row count
                                 				for each database table that is related to a configuration. The configuration
                                 				data consists of table name and row count for each table across the cluster.

### Smart Call Home Interaction

If you have a service contract directly with Cisco Systems, you can register Unified Communications Manager for the Cisco
                                 Smart Call Home service. Smart Call Home provides fast resolution of system problems by analyzing Call Home messages that
                                 are sent from Unified Communications Manager and providing background information and recommendations.

The Unified Communications Manager Call Home feature delivers the following messages to the Smart Call Home back-end server:

Alerts - Contain alert information for various conditions related to environment, hardware failure, and system performance.
                                       The alerts may be generated from any node within the Unified Communications Manager cluster. The alert details contain the
                                       node and other information required for troubleshooting purposes, depending on the alert type. See topics related to Smart
                                       call home interaction for alerts that are sent to the Smart Call Home back-end server.

The following are the alerts for Smart Call Home.

Important

The collected information is deleted from the primary AMC server after 48 years. By default, Unified Communications Manager
                                                publisher is the primary AMC server.

CallProcessingNodeCPUPegging

CodeYellow

CPUPegging

LowActivePartitionAvailableDiskSpace

LowAvailableVirtualMemory

LowSwapPartitionAvailableDiskSpace

Database - Related Alerts

DBReplicationFailure

Failed Calls Alerts

MediaListExhausted

RouteListExhausted

Crash - Related Alerts

Coredumpfilefound

CriticalServiceDown

The configuration, inventory, and telemetry messages are sent periodically (first day of every month) to the Call Home back-end.
                                 The information in these messages enables TAC to provide timely and proactive service to help customers manage and maintain
                                 their network.

### Prerequisites for Call Home

To support the Unified Communications Manager Call Home service, you require the following:

A Cisco.com user ID associated with a corresponding Unified Communications Manager service contract.

It is highly recommended that both the Domain Name System (DNS) and Simple Mail Transfer Protocol (SMTP) servers are setup
                                    for the Unified Communications Manager Call Home feature.

DNS setup is required to send the Call Home messages using Secure Web (HTTPS).

SMTP setup is required to send the Call Home messages to Cisco TAC or to send a copy of the messages to a list of recipients
                                          through email.

### Access Call Home

To access Unified Communications Manager Call Home, go to Cisco Unified Serviceability Administration and choose CallHome ( Cisco Unified Serviceability > CallHome > Call Home Configuration ).

### Call Home Settings

The following table lists the default Unified Communications Manager Call Home settings.

Parameter

Default

Call Home

Enabled

Send Data to Cisco Technical Assistance Center (TAC) using

Secure Web (HTTPS)

If default Smart Call Home configuration is changed during
                                 installation, then the same settings reflect in the Call Home user
                                 interface.

### Call Home Configuration

In Cisco Unified Serviceability, choose Call Home > Call Home
                                       				Configuration .

The Call Home Configuration window appears.

You can also configure the Cisco Smart Call Home while installing the Unified Communications Manager.

The Smart Call Home feature is enabled if you configure Smart Call Home option during installation. If you select None , a reminder message is displayed, when you log in to Cisco Unified Communications Manager Administration. Instructions to
                                 configure Smart Call Home or disable the reminder using Cisco Unified Serviceability is provided.

The following table describes the settings to configure the Unified Communications Manager Call Home.

Field Name

Description

Call Home Message Schedule

Displays the date and time of the last Call Home
                                             					 messages that were sent and the next message that is  scheduled.

Call Home*

Select this option if you want to enable or disable the Call Home. A reminder message appears Smart Call Home is not configured. To configure Smart Call Home or disable the reminder, please go to Cisco Unified Serviceability
                                                         > Call Home or click here on the administrator  page.

- Disabled :  Select
                                                   this option if you want to disable Call Home.

- Enabled (Smart Call Home) :  This option is enabled, if you have selected Smart Call Home during installation. When you select this option, all the
                                                   fields under Customer Contact Details are enabled. With the same configuration, the options in Send Data are also enabled.

If you enable Anonymous Call Home, the server sends usage statistics to Cisco systems from the server. This information helps
                                                                  Cisco to understand user experience about the product and to drive product direction.

Customer Contact Details

Email Address*

Enter the contact email address of the customer.
                                             					 This is a mandatory field.

Company

(Optional) Enter the name of the company. You can
                                             					 enter up to 255 characters.

Contact Name

(Optional) Enter the contact name of the customer.
                                             					 You can enter up to 128 characters.

The contact name can contain alphanumeric characters
                                             					 and some special characters like dot (.), underscore (_) and, hyphen (-).

Address

(Optional) Enter the address of the customer. You
                                             					 can enter up to 1024 characters.

Phone

(Optional) Enter the phone number of the customer.

Send Data

Send Data to Cisco Technical  Assistance Center (TAC) using

This is a Mandatory field. From the drop-down list, select one of the
                                             following options to send Call Home
                                             messages to Cisco TAC:

- Secure Web (HTTPS) : Select this option if you want to send the data to Cisco TAC
                                                   using secure web.

- HTTPS Proxy IP/Hostname* : Enter the proxy IP/Hostname.

- HTTPS Proxy Port* : Enter the proxy port number to
                                                         communicate.

Send a copy to the following email addresses
                                             				  (separate multiple addresses with comma)

Check this check box to send a copy of the Call Home
                                             					 messages to the specified email addresses.
                                             				  You can enter up to a maximum of 1024 characters.

Include Trace logs and Diagnostic Information

Check this check box to activate the Unified Communications Manager to collect logs and diagnostics information.

This option is active only if the Smart Call Home  is enabled.

The message contains diagnostic information collected at the time of alert along with trace message. If the trace size is
                                                         less than 3 MB, then the traces will be encoded and sent as part of alert message and if the  traces are more than 3 MB then
                                                         the path of the trace location is displayed in the alert message.

Save

Saves your Call Home configuration.

After you save your Call Home Configuration, an End User
                                                         						License Agreement (EULA) message appears. If you are configuring for the first
                                                         						time, you must accept the license agreement.

Tip

To deactivate the Call Home service that you activated, select the Disabled option from the drop-down list and click Save .

Reset

Resets to last saved configuration.

Save and Call Home Now

Saves and sends the Call Home messages.

A message appears Call Home Configuration saved and all Call Home Messages sent successfully if the messages are sent successfully.

### Limitations

The following limitations apply when Unified Communications Manager or Cisco Unified Presence server is down or unreachable:

Smart Call Home fails to capture the date and time of the last Call Home messages
                                    			 sent and the next message scheduled, until the server is reachable.

Smart Call Home does not send the Call Home messages, until the server is reachable.

Smart Call Home will be unable to capture license information in
                                    the inventory mail when the publisher is down.

The following limitations are due to Alert Manager and Collector
                              (AMC):

If an alert occurs on node A and the primary AMC
                                       server (by default, publisher) is restarted, and if the same alert
                                       occurs within a span of 24 hours on the same node, Smart Call Home
                                       resends the alert data from node A. Smart Call Home cannot recognize the alert that has already occurred because the  primary
                                       AMC was restarted.

If an alert occurs on node A and if you change
                                       the primary AMC server to another node, and if the same alert
                                       occurs within a span of 24 hours on the same node, Smart Call Home
                                       recognizes it as a fresh alert on node A and sends the alert
                                       data.

The traces that are collected on the primary AMC
                                       server may reside on the primary AMC server for a maximum of 60
                                       hours in few scenarios.

The following are the limitations in the mixed cluster (Unified Communications Manager and IM and Presence ) scenario:

- Alerts like CallProcessingNodeCpuPegging , Media
                                       List Exhausted , Route List Exhausted are
                                    not applicable to IM
                                    and Presence.

- If the user changes primary AMC server to IM
                                    and Presence, then Smart Call Home cannot generate Custer Overview
                                    reports for Media List Exhausted and Route List Exhausted.

If the user changes primary AMC server to IM
                                       and Presence, then Smart Call Home cannot generate Overview reports for DB Replication alert.

### References for Call Home

For more information about Smart Call Home, refer the following URL:

Smart Call Home Service Introduction

http://www.cisco.com/en/US/products/ps7334/serv_home.html

| Note | Ensure that the administrator copy the entire string and include -----BEGIN CERTIFICATE----- and -----END CERTIFICATE-----,
                                             paste it into a text file, and save it with the extension .PEM. |
|---|---|

| Inventory messages | Smart Call Home | Anonymous Call Home |
|---|---|---|
| Contact Email | Applicable | Not Applicable |
| Contact Phone number | Applicable | Not Applicable |
| Street Address | Applicable | Not Applicable |
| Server Name | Applicable | Not Applicable |
| Server IP Address | Applicable | Not Applicable |
| Licence Server | Applicable | Not Applicable |
| OS Version | Applicable | Applicable |
| Model | Applicable | Applicable |
| Serial Number | Applicable | Applicable |
| CPU Speed | Applicable | Applicable |
| RAM | Applicable | Applicable |
| Storage Partition | Applicable | Applicable |
| Firmware version | Applicable | Applicable |
| BIOS Version | Applicable | Applicable |
| BIOS Information | Applicable | Applicable |
| Raid Configuration | Applicable | Applicable |
| Active Services | Applicable | Applicable |
| Publisher Name | Applicable | Not Applicable |
| Publisher IP | Applicable | Not Applicable |
| Product ID | Applicable | Applicable |
| Active Version | Applicable | Applicable |
| Inactive Version | Applicable | Applicable |
| Product Short name | Applicable | Applicable |

| Telemetry messages | Smart Call Home | Anonymous Call Home |
|---|---|---|
| Contact Email | Applicable | Not Applicable |
| Contact Phone number | Applicable | Not Applicable |
| Street Address | Applicable | Not Applicable |
| Server name | Applicable | Not Applicable |
| CM User Count | Applicable | Not Applicable |
| Serial Number | Applicable | Applicable |
| Publisher name | Applicable | Not Applicable |
| Device count and Model | Applicable | Applicable |
| Phone User Count | Applicable | Applicable |
| CM Call Activity | Applicable | Applicable |
| Registered Device count | Applicable | Not Applicable |
| Upgrade history | Applicable | Not Applicable |
| System Status | Applicable for Host name, Date, Locale, Product Version, OS
                                             Version, Licence MAC, Up Time, MP Stat, Memory Used, Disk Usage, Active and
                                             Inactive partition used, and DNS | Applicable for Date, Locale, Product Version, OS Version, Licence MAC, Up Time, Memory Used, Disk Usage, and Active and Inactive
                                             partition used |

| Important | The collected information is deleted from the primary AMC server after 48 years. By default, Unified Communications Manager
                                                publisher is the primary AMC server. |
|---|---|

| Parameter | Default |
|---|---|
| Call Home | Enabled |
| Send Data to Cisco Technical Assistance Center (TAC) using | Secure Web (HTTPS) |

| Note | You must need to have a SMTP setup if you choose Email as the transport method and SMTP setup is not a required for Secure Web (HTTPS) option. |
|---|---|

| Note | You can also configure the Cisco Smart Call Home while installing the Unified Communications Manager. |
|---|---|

| Field Name | Description |
|---|---|
| Call Home Message Schedule | Displays the date and time of the last Call Home
                                             					 messages that were sent and the next message that is  scheduled. |
| Call Home* | From the drop-down list, select one of the
                                             following options: None : Select this option if you want to enable or disable the Call Home. A reminder message appears Smart Call Home is not configured. To configure Smart Call Home or disable the reminder, please go to Cisco Unified Serviceability
                                                         > Call Home or click here on the administrator  page. Disabled :  Select
                                                   this option if you want to disable Call Home. Enabled (Smart Call Home) :  This option is enabled, if you have selected Smart Call Home during installation. When you select this option, all the
                                                   fields under Customer Contact Details are enabled. With the same configuration, the options in Send Data are also enabled. Enabled (Anonymous Call Home) : Select this option  if you want to use Call Home in anonymous mode. When you select this option, all the fields under Customer Contact Details is disabled. With the same configuration, the Send a copy
                                                   to the following email addresses (separate multiple addresses with
                                                   comma) field in Send Data is enabled, and Include Trace logs and
                                                   Diagnostics Information is disabled on Call Home page. Note If you enable Anonymous Call Home, the server sends usage statistics to Cisco systems from the server. This information helps
                                                                  Cisco to understand user experience about the product and to drive product direction. | Note | If you enable Anonymous Call Home, the server sends usage statistics to Cisco systems from the server. This information helps
                                                                  Cisco to understand user experience about the product and to drive product direction. |
| Note | If you enable Anonymous Call Home, the server sends usage statistics to Cisco systems from the server. This information helps
                                                                  Cisco to understand user experience about the product and to drive product direction. |
| Customer Contact Details |
| Email Address* | Enter the contact email address of the customer.
                                             					 This is a mandatory field. |
| Company | (Optional) Enter the name of the company. You can
                                             					 enter up to 255 characters. |
| Contact Name | (Optional) Enter the contact name of the customer.
                                             					 You can enter up to 128 characters. The contact name can contain alphanumeric characters
                                             					 and some special characters like dot (.), underscore (_) and, hyphen (-). |
| Address | (Optional) Enter the address of the customer. You
                                             					 can enter up to 1024 characters. |
| Phone | (Optional) Enter the phone number of the customer. |
| Send Data |
| Send Data to Cisco Technical  Assistance Center (TAC) using | This is a Mandatory field. From the drop-down list, select one of the
                                             following options to send Call Home
                                             messages to Cisco TAC: Secure Web (HTTPS) : Select this option if you want to send the data to Cisco TAC
                                                   using secure web. Email : Select
                                                   this option if you want to send the data to Cisco TAC using email. For
                                                   email, the SMTP server must be configured. You can see the
                                                   Host name or IP address of the SMTP server that is  configured. Note A warning
                                                               message displays if you have not configured the SMTP
                                                               server. Secure
                                                      Web
                                                      (HTTPS) through Proxy : Select this
                                                   option if you want to send the data to Cisco TAC through
                                                   proxy. Currently, we do not support Authentication at the proxy level. The following fields appear on configuring this
                                                   option: HTTPS Proxy IP/Hostname* : Enter the proxy IP/Hostname. HTTPS Proxy Port* : Enter the proxy port number to
                                                         communicate. | Note | A warning
                                                               message displays if you have not configured the SMTP
                                                               server. |
| Note | A warning
                                                               message displays if you have not configured the SMTP
                                                               server. |
| Send a copy to the following email addresses
                                             				  (separate multiple addresses with comma) | Check this check box to send a copy of the Call Home
                                             					 messages to the specified email addresses.
                                             				  You can enter up to a maximum of 1024 characters. |
| Include Trace logs and Diagnostic Information | Check this check box to activate the Unified Communications Manager to collect logs and diagnostics information. Note This option is active only if the Smart Call Home  is enabled. The message contains diagnostic information collected at the time of alert along with trace message. If the trace size is
                                                         less than 3 MB, then the traces will be encoded and sent as part of alert message and if the  traces are more than 3 MB then
                                                         the path of the trace location is displayed in the alert message. | Note | This option is active only if the Smart Call Home  is enabled. The message contains diagnostic information collected at the time of alert along with trace message. If the trace size is
                                                         less than 3 MB, then the traces will be encoded and sent as part of alert message and if the  traces are more than 3 MB then
                                                         the path of the trace location is displayed in the alert message. |
| Note | This option is active only if the Smart Call Home  is enabled. The message contains diagnostic information collected at the time of alert along with trace message. If the trace size is
                                                         less than 3 MB, then the traces will be encoded and sent as part of alert message and if the  traces are more than 3 MB then
                                                         the path of the trace location is displayed in the alert message. |
| Save | Saves your Call Home configuration. Note After you save your Call Home Configuration, an End User
                                                         						License Agreement (EULA) message appears. If you are configuring for the first
                                                         						time, you must accept the license agreement. Tip To deactivate the Call Home service that you activated, select the Disabled option from the drop-down list and click Save . | Note | After you save your Call Home Configuration, an End User
                                                         						License Agreement (EULA) message appears. If you are configuring for the first
                                                         						time, you must accept the license agreement. | Tip | To deactivate the Call Home service that you activated, select the Disabled option from the drop-down list and click Save . |
| Note | After you save your Call Home Configuration, an End User
                                                         						License Agreement (EULA) message appears. If you are configuring for the first
                                                         						time, you must accept the license agreement. |
| Tip | To deactivate the Call Home service that you activated, select the Disabled option from the drop-down list and click Save . |
| Reset | Resets to last saved configuration. |
| Save and Call Home Now | Saves and sends the Call Home messages. Note A message appears Call Home Configuration saved and all Call Home Messages sent successfully if the messages are sent successfully. | Note | A message appears Call Home Configuration saved and all Call Home Messages sent successfully if the messages are sent successfully. |
| Note | A message appears Call Home Configuration saved and all Call Home Messages sent successfully if the messages are sent successfully. |

| Note | If you enable Anonymous Call Home, the server sends usage statistics to Cisco systems from the server. This information helps
                                                                  Cisco to understand user experience about the product and to drive product direction. |
|---|---|

| Note | A warning
                                                               message displays if you have not configured the SMTP
                                                               server. |
|---|---|

| Note | This option is active only if the Smart Call Home  is enabled. The message contains diagnostic information collected at the time of alert along with trace message. If the trace size is
                                                         less than 3 MB, then the traces will be encoded and sent as part of alert message and if the  traces are more than 3 MB then
                                                         the path of the trace location is displayed in the alert message. |
|---|---|

| Note | After you save your Call Home Configuration, an End User
                                                         						License Agreement (EULA) message appears. If you are configuring for the first
                                                         						time, you must accept the license agreement. |
|---|---|

| Tip | To deactivate the Call Home service that you activated, select the Disabled option from the drop-down list and click Save . |
|---|---|

| Note | A message appears Call Home Configuration saved and all Call Home Messages sent successfully if the messages are sent successfully. |
|---|---|