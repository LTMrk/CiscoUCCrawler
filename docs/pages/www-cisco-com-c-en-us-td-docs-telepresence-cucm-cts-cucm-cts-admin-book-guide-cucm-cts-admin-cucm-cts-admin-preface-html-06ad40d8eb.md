---
doc_id: www-cisco-com-c-en-us-td-docs-telepresence-cucm-cts-cucm-cts-admin-book-guide-cucm-cts-admin-cucm-cts-admin-preface-html-06ad40d8eb
source_url: https://www.cisco.com/c/en/us/td/docs/telepresence/cucm_cts/cucm_cts_admin_book/guide/cucm_cts_admin/cucm_cts_admin_preface.html
retrieved_at: 2026-08-17T00:09:45.894009+00:00
---

Cisco Unified Communications Manager Configuration Guide for the Cisco TelePresence System

# Cisco Unified Communications Manager Configuration Guide for the Cisco TelePresence System

Updated: April 15, 2014

Chapter: What's in This Guide

## Chapter: What's in This Guide

# What’s in This Guide

Revised: June 9, 2015, OL-21851-01

## How to Use This Guide

The Cisco Unified Communications Manager Configuration Guide for the Cisco TelePresence System provides information to help you use the Cisco Unified Communications Manager (Unified CM) Administration interface to configure the following Cisco TelePresence System (CTS) products:

- TelePresence Immersive Endpoints

– Cisco TelePresence System TX9200 Series

– Cisco TelePresence System TX9000 Series

– Cisco TelePresence System 3200 Series

– Cisco TelePresence System 3000 Series

– Cisco TelePresence System TX1300 Series

– Cisco TelePresence System 1300 Series

- TelePresence Personal Endpoints > TelePresence Office

– Cisco TelePresence System 1100

– Cisco TelePresence System 1000

– Cisco TelePresence System 500 Series

Note The entries that are recommended or required in the configuration fields in this guide are for configuring the Unified CM for Cisco TelePresence specifically. While some configuration fields in the administration interface offer a variety of choices, Cisco recommends that you follow the guidelines presented in this document to set up your Cisco TelePresence configuration successfully.

## Before You Begin

Before beginning the tasks in this guide, verify the following:

### Web Browser Support

Cisco administration interfaces are supported on Internet Explorer (IE) versions 6, 7, 8 and 9 and Firefox version 3.6, 5 and 9.

### CTS Software Download

Make sure you have downloaded supported CTS software. Navigate to your CTS device on Cisco.com.

1. Navigate to your device:

- Product Support > TelePresence > TelePresence Immersive Endpoints

– Cisco TelePresence System TX9200 Series

– Cisco TelePresence System TX9000 Series

– Cisco TelePresence System 3200 Series

– Cisco TelePresence System 3000 Series

– Cisco TelePresence System TX1300 Series

– Cisco TelePresence System 1300 Series

- Products > TelePresence > TelePresence Personal Endpoints > TelePresence Office

– Cisco TelePresence System 1100

– Cisco TelePresence System 1000

– Cisco TelePresence System 500 Series

For example:

Products > TelePresence > TelePresence Endpoints - Immersive > Cisco TelePresence TX9200 Series > Cisco TelePresence TX9200 > TelePresence Software-1.9.3(44)

2. Select software and choose whether to download now or add it to your cart.

### DHCP Connectivity

Provide a Dynamic Host Configuration Protocol (DHCP) server to achieve connectivity. CTS uses DHCP by default. If no DHCP server is available, refer to your system assembly guide’s First Time Setup chapter, in the section that instructs how to use a static IP network address.

- For CTS 500-32, 1300-47, 1310-65, and TX9x00 systems: Refer to your system assembly guide’s First Time Setup chapter.

- For CTS 500-37, 1x00, 1300-65, 30x0, and 32x0 systems: Refer to Configuring a Static IP Address for Networks That Do Not Use DHCP .

### COP (Loads) File Download

The Cisco Options Package (COP) file is a mechanism for installing files on a Unified CM in a secure manner. See Chapter 3, “Loading Cisco Options Package (COP) Files on the Cisco TelePresence System” for complete information.

### Call Control Device Requirements

All new Cisco TelePresence Systems which use the Cisco TelePresence Touch 12 for call control take 6 units of the Unified CM unit license:

- 0 units for the Cisco TelePresence Touch device

- 6 units for the Cisco TelePresence unit

All existing Cisco TelePresence Systems which use the IP Phone for call control take 11 units of the Unified CM unit license:

- 5 units for the Cisco Unified IP Phone 7970/7975

- 6 units for the Cisco TelePresence unit

You can configure the system and the Cisco Unified IP Phone as a shared line in Cisco Unified CM.

Note When using the IP Phone, please note the following: For all SCCP and SIP firmware upgrades from firmware release versions earlier than 8.3(3) to version 8.5(3) or a later release, you must first upgrade your firmware to version 8.5(2). Once you have upgraded to version 8.5(2), you can upgrade your Cisco Unified IP Phone to version 8.5(3) or a later release. See the Installation Notes section of the Cisco Unified IP Phone Release Notes for Firmware Release 8.5(3) (SCCP and SIP) for download instructions.

### MAC Address

Make sure the MAC address of the device you are installing is known or available:

- The MAC address comprises a unique 12-character hexadecimal number that identifies a Cisco Unified IP phone or other hardware device.

- Locate the MAC address number on a label on the back of the Cisco TelePresence system primary codec (for example, 000B6A409C405). Unified CM makes the MAC address a required field for Cisco Unified IP phone device configuration.

The MAC address is also displayed on the CTS main display screen during boot-up.

Note When entering the MAC address in Unified CM fields, do not use spaces or dashes, and do not include any other characters that may precede the MAC address on the label.

### Unified Communications Manager and MIDlets Download

Note This section pertains only to systems that uses a Cisco Unified IP phone for call control. If your system uses a Cisco Touch device for call control, skip this section.

Make sure that Unified CM is running and is using supported software for your release. For complete Cisco TelePresence software compatibility information, see the software support matrix on the Cisco TelePresence Administration Software page at the following URL:

http://www.cisco.com/en/US/products/ps8332/products_device_support_tables_list.html

You must download and configure MIDlets to enable all available features on your CTS Cisco Unified IP phone. The supported MIDlet version is embedded in the software files that are available when you click Download Software on the Cisco Unified Communications Manager Support page at the following URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/tsd_products_support_series_home.html

Or navigate to Products > Voice and Unified Communications > IP Telephony > Call Control > Cisco Unified Communications Manager (CallManager) > Cisco Unified Communications Manager Version x.x > Unified Communications Manager/CallManager Device Packages.

Check the following:

- The Cisco TelePresence device name in Unified CM follows the following format: The characters “SEP” followed by the device MAC address. Assign the hostname so that it is resolvable by Domain Name System (DNS), for example:”

MAC address: “ 000DD12345A1 ”

Cisco TelePresence Host Name: “ SEP000DD12345A1 ”

Note DNS (domain) is optional.

## Additional System Information

For more information, see the following sections:

### Adding or Removing a Presentation Codec

When you add or remove a CTS presentation codec in the system configuration, you must also do so from the Unified CM administration interface. After the configuration change is complete, click Reset to sync this configuration change with the CTS codec.

### Call Control Device Features for Cisco TelePresence

There are additional features that can be configured on standard Cisco TelePresence call control devices. The settings described in this document are provided specifically to configure a Touch 12 as a Cisco TelePresence device.

For complete Cisco TelePresence user options on the Touch 12, refer to the Cisco TelePresence System User Guide on cisco.com that corresponds with your system’s software release.

Many of the settings also apply to the Cisco Unified IP Phone call control device. See Chapter 5, “Configuring and Managing the Cisco Unified IP Phone” for specifics.

Note Features that are not mentioned in this or other guides are assumed to be un-supported at this time.

### Software Compatibility

For complete information about software and firmware compatibility for the CTS, see the Cisco TelePresence Administration Software Compatibility Matrix on Cisco.com.

### Cisco TelePresence Bandwidth Requirements

For information about Cisco TelePresence service level requirements including bandwidth, latency (delay), jitter (variations in delay), and packet loss, see the “Understanding How Endpoints Determine fps and Video Quality” section of the Administration Guide for Cisco TelePresence TX Software Release 6.0 on Cisco.com.

### Device and Cluster Security Modes

During a call, the Media is Encrypted icon (closed lock) is displayed on the screen only when the Device Security mode is set to encrypted and cluster security mode is set to 1 ( mixed mode ). While configuring your system, check the following settings:

- Device Security Mode should be set to Encrypted in the SIP Phone Security Profile Information field. See the “SIP Phone Security Profile Information” section for configuration information.

- Cluster Security Mode field is set to 1 ( mixed mode ) in the Configuration Settings for CTL Client in Cisco Unified CM Administration > System > Enterprise Parameters . To configure and verify cluster security mode, see the Verifying the Cisco Unified Communications Manager Security Mode section of the Cisco TelePresence Security Solutions Guide .

### Supported Unified CM Characters and Digits for the CTS Device Page

Use the information in Table 1 as a guide for supported Unified CM characters and digits that are used to configure and maintain the Cisco TelePresence system. For general Unified CM support documentation, see the Unified CM documentation roadmaps for your release on Cisco.com:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_documentation_roadmaps_list.html

Note Unified CM no longer the ‘$’ (currency symbol) in system passwords.

Table 1 Supported Unified CM Characters and Digits for Cisco TelePresence Device Configurations

- Digits 0 through 9

- * (Asterisk)

- # (Number sign or hash)

- + (Plus sign, escape symbol)

The number that you want the system to dial when the user presses the speed-dial button.

Note The speed-dial function does not allow you to configure pauses or waits.

- Speed Dial and Abbreviated Dial Configuration window, Number field.

- Multilevel precedence and preemption MLPP Alternate Party Settings , Target (Destination) field.

See Chapter1, “Configuring Cisco Unified Communications Manager for the Cisco TelePresence System”

## Related Documentation

Cisco command-line interface (CLI) information for configuring the Cisco TelePresence System.

- Cisco TelePresence System Command-Line Interface Reference Guide .

Cisco Jabber Video for TelePresence (previously called Movi) home page.

- Cisco Jabber Video for TelePresence

Cisco Multipoint Control Unit (MCU) 4500 Series home page.

- Cisco TelePresence MCU 4500 Series

Cisco switch support information.

- Product Support > Switches

Cisco TelePresence support information.

- Product Support > TelePresence (Video Conferencing)

Cisco TelePresence administration software download page.

- Download Software Select a Product page on Cisco.com:

http://www.cisco.com/cisco/software/navigator.html

Cisco TelePresence Manager documentation home page.

- Cisco TelePresence Manager home page on Cisco.com

Cisco TelePresence Recording Server information.

- Cisco TelePresence Recording Server home page on Cisco.com

Cisco TelePresence System Codec home page.

- Cisco Telepresence System Integrator C Series

Cisco TelePresence System compatibility information.

- Software Compatibility Information for the Cisco TelePresence System

Cisco TelePresence System EX Series home page.

- Cisco TelePresence System EX Series

Cisco TelePresence System MXP Series home page.

- Cisco TelePresence System MXP Series

Cisco TelePresence Video Communication Server (VCS) home page.

- Cisco TelePresence Video Communication Server (VCS)

Cisco TelePresence Video Communication Server (VCS) support documentation

Cisco Unified Communications Manager Support page.

- Cisco Unified Communications Manager Support

Cisco Unified IP Phone 8900 Series home page.

- Cisco Unified IP Phone 8900 Series

Cisco Unified IP Phone 9900 Series home page.

- Cisco Unified IP Phones 9900 Series

Cisco Unified IP Phone firmware download instructions in the Installation Notes section.

- Cisco Unified IP Phone Release Notes for Firmware Release 8.5(3) (SCCP and SIP)

Cisco Unified IP Phones 7900 Series documentation.

- Cisco Unified IP Phones 7900 Series Maintain and Operate Guides

Cisco Unified Mobility documentation.

- Cisco Unified Mobility

Cisco Validated Design Program. Systems and solutions designed, tested, and documented to facilitate faster, more reliable, and more predictable customer deployments.

- Cisco TelePresence Network Systems 2.0 Design Guide

Complete software and firmware compatibility.

- Cisco TelePresence Administration Software Compatibility Matrix

Configuring CTS administration software features.

- Cisco TelePresence System Administration Guide

CTS Administration and User Guides: Configuration, maintenance, and monitoring tasks using Cisco TelePresence administration software.

- Products > TelePresence > TelePresence Immersive Endpoints > TelePresence System > Cisco TelePresence Administration Software

http://www.cisco.com/en/US/products/ps8332/tsd_products_ support_series_home.html

Documentation resources for administering the Cisco Unified Communications Manager system.

- Cisco Unified Communications Manager Documentation Guide for Release 8.0(1)

Features supported on the Touch 12 device.

- Cisco TelePresence System User Guide

How to configure and manage security on the Cisco TelePresence System.

- Cisco TelePresence Security Solutions Configuration Guide

How to configure Cisco WebEx OneTouch for Cisco TelePresence.

- Cisco WebEx OneTouch for Cisco TelePresence Configuration Guide

How to navigate to Cisco TelePresence System (CTS) hardware and software documentation, including information about CTS devices.

- Cisco.com Products > TelePresence

Information about the Cisco TelePresence Multipoint Switch (CTMS).

- Cisco TelePresence Multipoint Switch home page on Cisco.com

Install and use the Cisco TelePresence Touch 12.

Overview of the features available on your Cisco IP Phone 7970 Series.

- Cisco Unified IP Phone 7970 Series Phone Guide for Cisco Unified Communications Manager 7.0 (SCCP and SIP)

Reference and procedural guide for system and phone administrators who plan to configure call security features for Cisco Unified Communications Manager.

- Cisco Unified Communications Manager Security Guide, Release 7.1(2)

Session Initiation Protocol (SIP) page.

- Session Initiation Protocol (SIP)

Troubleshooting the CTS and Cisco Unified CM Administration interfaces and related hardware components.

- Cisco TelePresence System Troubleshooting Guide

Unified CM documentation types and locations.

- Cisco Unified Communications Manager (CallManager) Documentation Roadmaps

Unified CM install and upgrade guides.

- Cisco Unified Communications Manager (CallManager) Install and Upgrade Guides

## Obtaining Documentation and Submitting a Service Request

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at the following URL:

http://www.cisco.com/en/US/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently RSS version 2.0.

| Character or Digit | Description | Where Used |
|---|---|---|
| Digits 0 through 9 * (Asterisk) # (Number sign or hash) + (Plus sign, escape symbol) | The number that you want the system to dial when the user presses the speed-dial button. Note The speed-dial function does not allow you to configure pauses or waits. | Speed Dial and Abbreviated Dial Configuration window, Number field. Multilevel precedence and preemption MLPP Alternate Party Settings , Target (Destination) field. See Chapter1, “Configuring Cisco Unified Communications Manager for the Cisco TelePresence System” |

| Related Topic | Document Title |
|---|---|
| Cisco command-line interface (CLI) information for configuring the Cisco TelePresence System. | Cisco TelePresence System Command-Line Interface Reference Guide . |
| Cisco Jabber Video for TelePresence (previously called Movi) home page. | Cisco Jabber Video for TelePresence |
| Cisco Multipoint Control Unit (MCU) 4500 Series home page. | Cisco TelePresence MCU 4500 Series |
| Cisco switch support information. | Product Support > Switches |
| Cisco TelePresence support information. | Product Support > TelePresence (Video Conferencing) |
| Cisco TelePresence administration software download page. | Download Software Select a Product page on Cisco.com: http://www.cisco.com/cisco/software/navigator.html |
| Cisco TelePresence Manager documentation home page. | Cisco TelePresence Manager home page on Cisco.com |
| Cisco TelePresence Recording Server information. | Cisco TelePresence Recording Server home page on Cisco.com |
| Cisco TelePresence System Codec home page. | Cisco Telepresence System Integrator C Series |
| Cisco TelePresence System compatibility information. | Software Compatibility Information for the Cisco TelePresence System |
| Cisco TelePresence System EX Series home page. | Cisco TelePresence System EX Series |
| Cisco TelePresence System MXP Series home page. | Cisco TelePresence System MXP Series |
| Cisco TelePresence Video Communication Server (VCS) home page. | Cisco TelePresence Video Communication Server (VCS) |
| Cisco TelePresence Video Communication Server (VCS) support documentation |  |
| Cisco Unified Communications Manager Support page. | Cisco Unified Communications Manager Support |
| Cisco Unified IP Phone 8900 Series home page. | Cisco Unified IP Phone 8900 Series |
| Cisco Unified IP Phone 9900 Series home page. | Cisco Unified IP Phones 9900 Series |
| Cisco Unified IP Phone firmware download instructions in the Installation Notes section. | Cisco Unified IP Phone Release Notes for Firmware Release 8.5(3) (SCCP and SIP) |
| Cisco Unified IP Phones 7900 Series documentation. | Cisco Unified IP Phones 7900 Series Maintain and Operate Guides |
| Cisco Unified Mobility documentation. | Cisco Unified Mobility |
| Cisco Validated Design Program. Systems and solutions designed, tested, and documented to facilitate faster, more reliable, and more predictable customer deployments. | Cisco TelePresence Network Systems 2.0 Design Guide |
| Complete software and firmware compatibility. | Cisco TelePresence Administration Software Compatibility Matrix |
| Configuring CTS administration software features. | Cisco TelePresence System Administration Guide |
| CTS Administration and User Guides: Configuration, maintenance, and monitoring tasks using Cisco TelePresence administration software. | Products > TelePresence > TelePresence Immersive Endpoints > TelePresence System > Cisco TelePresence Administration Software http://www.cisco.com/en/US/products/ps8332/tsd_products_ support_series_home.html |
| Documentation resources for administering the Cisco Unified Communications Manager system. | Cisco Unified Communications Manager Documentation Guide for Release 8.0(1) |
| Features supported on the Touch 12 device. | Cisco TelePresence System User Guide |
| How to configure and manage security on the Cisco TelePresence System. | Cisco TelePresence Security Solutions Configuration Guide |
| How to configure Cisco WebEx OneTouch for Cisco TelePresence. | Cisco WebEx OneTouch for Cisco TelePresence Configuration Guide |
| How to navigate to Cisco TelePresence System (CTS) hardware and software documentation, including information about CTS devices. | Cisco.com Products > TelePresence |
| Information about the Cisco TelePresence Multipoint Switch (CTMS). | Cisco TelePresence Multipoint Switch home page on Cisco.com |
| Install and use the Cisco TelePresence Touch 12. |  |
| Overview of the features available on your Cisco IP Phone 7970 Series. | Cisco Unified IP Phone 7970 Series Phone Guide for Cisco Unified Communications Manager 7.0 (SCCP and SIP) |
| Reference and procedural guide for system and phone administrators who plan to configure call security features for Cisco Unified Communications Manager. | Cisco Unified Communications Manager Security Guide, Release 7.1(2) |
| Session Initiation Protocol (SIP) page. | Session Initiation Protocol (SIP) |
| Troubleshooting the CTS and Cisco Unified CM Administration interfaces and related hardware components. | Cisco TelePresence System Troubleshooting Guide |
| Unified CM documentation types and locations. | Cisco Unified Communications Manager (CallManager) Documentation Roadmaps |
| Unified CM install and upgrade guides. | Cisco Unified Communications Manager (CallManager) Install and Upgrade Guides |