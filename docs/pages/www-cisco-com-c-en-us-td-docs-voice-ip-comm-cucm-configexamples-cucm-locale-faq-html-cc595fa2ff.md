---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-configexamples-cucm-locale-faq-html-cc595fa2ff
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/configExamples/CUCM-Locale-FAQ.html
retrieved_at: 2026-08-21T13:59:24.316713+00:00
---

Cisco Unified Communications Manager Locale Installer FAQs

# Cisco Unified Communications Manager Locale Installer FAQs

### Download Options

Updated: June 16, 2021

Cisco Unified Communications Locale Installer Frequently Asked Questions (FAQ)

# Locale Types

Cisco Unified Communications Product

Locale

Cisco Unified Communication Manager (CUCM)

User Locale, Network Locale

Cisco IP Phone Only

Phone-Only Locale

Cisco Unified Communications Manager IM & Presence

User Locale

## User Locale

Includes localized user interfaces for applications, devices, services, and localized spoken prompts. Every CUCM User locale also include the Network Locale for the country of the user locale. A user locale is comprised of localized graphical user interface, telephone user interface and annunciators (audio prompts) that can be heard via a telephone. User locales are produced individually and are specific to a language and country combination.

## (Combined) Network Locale

Includes localized telephone and gateway tones. Network Locale and Combined Network Locale are synonymous. Combined Network Locales include network locales for all countries that are supported. A network locale covers the specific localization needs of a country, these include telephone dial and ringing tones and those that are required by a gateway to generate local tones on the network (whether it is for IP networks or Time Division Multiplexing networks on the Public Switched Telephone Network) and network annunciators that are played via a gateway.

Network locales are generally produced as a single package intended to cover all supported countries.

## Phone Only Locale

Includes localized device user interfaces and tones.

# Locale Installer (LI) Releases

There is Locale Installer (LI) release for every CUCM and CUCM IMP (previous name: CUP) major and minor release. Standard version numbering is Major.Minor. Examples include: 10.5 and 12.0. Usually, there might not be LI releases for CUCM and CUPS maintenance or service releases (ex: 8.0(3a)su1, 8.0(3a)su2) when the maintenance or service release has no updates on localization.

## What Version of Locale Installer should I apply when I upgrade my CUCM?

General rule: Apply the latest Locale Installer release that matches the major.minor version of CUCM. Released locale installers are available on cisco.com. Locate the latest LI with a major.minor number that matches your CUCM or CUCM IM&P major.minor version. For example, the latest locale installer for CUCM 11.5.1.x is LI 11.5.1.10000-1 (as of June 2021).

## What type of Locale do I need to install?

You will need: CUCM User Locale for every CUCM server, CUCM IM&P (previous name: CUP) user locale for every IMP server. If you need network tones for countries which we have no supported User Locale yet, you will need to apply the Combined Network Locale Installer on every CUCM server. User locales are produced individually and are specific to a language and country combination. Network locales are generally produced as a single package intended to cover all supported countries. Network locales may be referred to as combined network locales.

## Do locales need to be installed on every Node?

Yes, Cisco Unified Communications Locale Installer MUST be applied to each and every Cisco Unified Communications Manager server in a cluster, starting with the publisher. After installation has completed, it is essential to reboot each and every platform in order for all user and network locale changes to become fully activated.

Starting Version 12.5, there is option to install all locale installer on all nodes at the same time. ( https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/214134-upgrade-enhancements-in-cisco-unified-c.html )

## How to install locales?

Locale can be installed either from Network drive or from CD/DVD drive. Option A: Install locale from network drive:

1. Put the locale installer (*.cop.sgn or *.cop.sha512 ) file on an FTP or SFTP server which is accessible from your CUCM/CUP server.

2. Log into Cisco Unified Communications Operating System Administration.

3. Navigate to Software Upgrades > Install/Upgrade. The Software Installation/Upgrade window displays.

4. Choose Remote Filesystem from the Source list.

5. Enter the path to the directory that contains the local installer file on the remote system in the Directory field. (If the upgrade file is located on a Linux or Unix server, you must enter a forward slash at the beginning of the directory path. For example, if the upgrade file is in the "patches" directory, you must enter "/patches". If the upgrade file is located on a Windows server, check with your system administrator for the correct directory path.)

6. In the Server field, enter the server name or IP address.

7. In the User Name field, enter your user name on the remote server.

8. In the User Password field, enter your password on the remote server.

9. Select the SFTP protocol from the Transfer Protocol field.

10. To continue the upgrade process, click Next .

11. Choose the upgrade version that you want to install and click Next .

12. In the next window, monitor the progress of the download.

13. When the download completes, verify the checksum value against the checksum (if available) or the file you that downloaded that is shown on Cisco.com.

14. Restart the CUCM or CUP server after any new locale installs. For Phone Only locale, restart TFTP service is an alternative way.

Option B: Install locale from CD/DVD:

1. Burn the locale installer file into a CD/DVD.

2. Follow the steps in "Install locale from network drive" except "Choose CD/DVD from the Source list" instead of "Choose Remote Filesystem from the Source list."

## What is a Phone-Only locale installer (POLI) and when should it be used?

Cisco Unified Communications Locale Installer for Cisco Unified IP Phones ensures localized phones are kept up to date with the latest UI localization updates after the firmware is upgraded. The full Cisco Unified Communications Locale Installer for Cisco Unified Communications Manager must be installed prior to installation of a Phone Only locale installer. For example, with CUCM 10.5 and Firmware 12.8, CUCM LI 10.5.x need to be installed first, then install Phone Only LI 12.8 for firmware updates.

## Do I need to install a new Phone Only locale every time after I upgrade my IP phone firmware?

There isn’t a “Yes” or “No” answer for this question. Cisco only releases Phone Only Locales for FW with changes to phone UI or internationalization. In other words, we do not have Phone Only Locale Installer release for every FW release when it is not necessary. When a customer upgrades the firmware without upgrading their CUCM, they should install the latest Phone Only locale with the same major.minor number with the new FW. For example, if you upgrade from FW 12.1 (with POLI 12.1) to FW 12.8, you will need to install POLI 12.8.

Phone Only Locale Installer (PO LI) is a subset of the CUCM LI. PO LI is used for customers who upgrade IP phone firmware without upgrading CUCM. Future CUCM images may include later versions of IP Phone firmware. Please make sure you have installed the latest phone-only locale installer that matches the firmware's major.minor version number.

Here is the version mapping between CUCM LI and PO LI:

CUCM LI Version (matches CUCM major.minor version)

PO LI version (matches IP phone firmware major.minor version)

CUCM LI 14.0

PO LI 14.0

CUCM LI 12.5/SU3/SU4

PO LI 12.8

CUCM LI 12.0

PO LI 12.0

CUCM LI 11.5/SU10

PO LI 14.0

CUCM LI 11.5/SU8/SU9

PO LI 12.8

CUCM LI 11.0

PO LI 10.3.1 (provides localization support for both FW 10.3.1)

CUCM LI 10.5.1

PO LI 10.2.1 (provides localization support for both FW 10.2.1 and FW 9.4.2)

CUCM LI 10.0.x

PO LI 10.1.1 (provides localization support for both FW 10.1 and FW 9.4.1)

CUCM LI 9.1.x

PO LI 9.3.2

CUCM LI 9.0.x

PO LI 9.3.1

CUCM LI 8.6.x

PO LI 9.2.x

CUCM LI 8.5.x

PO LI 9.1.x

CUCM LI 8.0.x

PO LI 9.0.x

CUCM LI 7.1.x

PO LI 8.5.x

CUCM LI 7.0.x

PO LI 8.4.x

CUCM LI 6.1.x

PO LI 8.3.x

CUCM LI 10.5.1

PO LI 10.2.1 (provides localization support for both FW 10.2.1 and FW 9.4.2)

CUCM LI 10.0.x

PO LI 10.1.1 (provides localization support for both FW 10.1 and FW 9.4.1)

CUCM LI 9.1.x

PO LI 9.3.2

CUCM LI 9.0.x

PO LI 9.3.1

CUCM LI 8.6.x

PO LI 9.2.x

CUCM LI 8.5.x

PO LI 9.1.x

CUCM LI 8.0.x

PO LI 9.0.x

CUCM LI 7.1.x

PO LI 8.5.x

CUCM LI 7.0.x

PO LI 8.4.x

CUCM LI 6.1.x

PO LI 8.3.x

## Does the Locale Installer register with the DRS for backup and restore?

Locale Installers, from version 5.1.1.1-1 onwards, no longer register with the DRS for backup and restore. Locales must be re-installed separately after a rebuild and before a restore.

# CUCM User Locale and Network Locale Support

### List of user and network locales for CUCM 11.5, 12.0, 12.5, 14:

CUCM Selfcare Portal language localization support:

Arabic(Algeria), Arabic (Bahrain), Arabic (Egypt), Arabic (Iraq), Arabic (Jordan), Arabic (Kuwait), Arabic (Lebanon), Arabic (Morocco), Arabic (Oman), Arabic (Qatar), Arabic (Saudi Arabia), Arabic (Tunisia), Arabic (United Arab Emirates), Arabic (Yemen), Bulgarian (Bulgaria), Catalan (Spain), Chinese (Hong Kong), Chinese (China), Chinese (Taiwan), Croatian (Croatia), Czech (Czech Republic), Danish (Denmark), Dutch (Netherlands), English (United Kingdom), Estonian (Estonia), Finnish (Finland), French (France), French (Canada), French (Switzerland), German, (Austria), German (Germany), German (Switzerland), Greek (Greece), Hebrew (Israel), Hungarian (Hungary), Italian (Italy), Italian (Switzerland), Japanese (Japan), Korean (Korea Republic), Latvian (Latvia), Lithuanian (Lithuania), Norwegian (Norway), Polish (Poland), Portuguese (Brazil), Portuguese (Portugal), Romanian (Romania), Russian (Russian Federation), Serbian (Republic of Montenegro), Serbian (Republic of Serbia), Slovak (Slovakia), Slovenian (Slovenia), Spanish (Argentina), Spanish (Colombia), Spanish (Spain), Swedish (Sweden), Thai (Thailand), and Turkish (Turkey), Ukrainian (Ukraine).

CUCM Administration pages localization support

Cisco Unified Communications Manager Administration Components localization support

[X] Cisco Unified Communications Manager Administration (General) [ ] Cisco Unified Serviceability

[X] Cisco Unified Communications Operating System Administration [ ] Cisco Unified Reports

[ ] Cisco Unified Disaster Recovery System

## Cisco Unified Communications Manager Administration languages localization support:

· Chinese (China)

· Chinese (Taiwan) (Supported from CUCM 12.5 and upwards)

· Japanese (Japan)

· Korean (Korea Republic).

## CUCM Network Locales support:

Algeria, Argentina, Australia, Austria, Bahrain, Belgium, Brazil, Bulgaria, Canada, Chile, China, Colombia, Croatia, Cyprus, Czech Republic, Denmark, Egypt, Estonia, Finland, France, Germany, Ghana, Greece, Hong Kong, Hungary, Iceland, India, Indonesia, Iraq, Ireland, Israel, Italy, Japan, Jordan, Kenya, Korea Republic, Kuwait, Latvia, Lebanon, Lithuania, Luxembourg, Malaysia, Mauritania, Mexico, Morocco, Nepal, Netherlands, New Zealand, Nigeria, Norway, Oman, Pakistan, Panama, Peru, Philippines, Poland, Portugal, Qatar, Romania, Republic of Montenegro, Republic of Serbia, Russian Federation, Saudi Arabia, Singapore, Slovakia, Slovenia, South Africa, Spain, Sudan, Sweden, Switzerland, Taiwan, Thailand, Tunisia, Turkey, Ukraine, United Arab Emirates, United Kingdom, Venezuela, Vietnam, Yemen, Zimbabwe.

## List of user and network locales for CUCM 11.0, 10.0:

CUCM Admin user interface supports only Chinese (China), Japanese (Japan), and Korean (Korea Republic).

CUCM Self Care Portal user interface supports the following user locales (languages and prompts): Arabic(Algeria), Arabic (Bahrain), Arabic (Egypt), Arabic (Iraq), Arabic (Jordan), Arabic (Kuwait), Arabic (Lebanon), Arabic (Morocco), Arabic (Oman), Arabic (Qatar), Arabic (Saudi Arabia), Arabic (Tunisia), Arabic (United Arab Emirates), Arabic (Yemen), Bulgarian (Bulgaria), Catalan (Spain), Chinese (Hong Kong), Chinese (China), Chinese (Taiwan), Croatian (Croatia), Czech (Czech Republic), Danish (Denmark), Dutch (Netherlands), English (United Kingdom), Estonian (Estonia), Finnish (Finland), French (France), French (Canada) * , German (Germany), Greek (Greece), Hebrew (Israel), Hungarian (Hungary), Italian (Italy), Japanese (Japan), Korean (Korea Republic), Latvian (Latvia), Lithuanian (Lithuania), Norwegian (Norway), Polish (Poland), Portuguese (Brazil), Portuguese (Portugal), Romanian (Romania), Russian (Russian Federation), Serbian (Republic of Montenegro), Serbian (Republic of Serbia), Slovak (Slovakia), Slovenian (Slovenia), Spanish (Colombia), Spanish (Spain), Swedish (Sweden), Thai (Thailand), and Turkish (Turkey).

* French (Canada) locale has now been updated linguistically since 10.0 release.

CUCM supports the following network locales (phone and gateway tones) : Algeria, Argentina, Australia, Austria, Bahrain, Belgium, Brazil, Bulgaria, Canada, Chile, China, Colombia, Croatia, Cyprus, Czech Republic, Denmark, Egypt, Estonia, Finland, France, Germany, Ghana, Greece, Hong Kong, Hungary, Iceland, India, Indonesia, Iraq, Ireland, Israel, Italy, Japan, Jordan, Kenya, Korea Republic, Kuwait, Latvia, Lebanon, Lithuania, Luxembourg, Malaysia, Mauritania, Mexico, Morocco, Nepal, Netherlands, New Zealand, Nigeria, Norway, Oman, Pakistan, Panama, Peru, Philippines, Poland, Portugal, Qatar, Romania, Republic of Montenegro, Republic of Serbia, Russian Federation, Saudi Arabia, Singapore, Slovakia, Slovenia, South Africa, Spain, Sudan, Sweden, Switzerland, Taiwan, Thailand, Tunisia, Turkey, United Arab Emirates, United Kingdom, Venezuela, Vietnam, Yemen, Zimbabwe.

## List of user and network locales for CUCM 9.1, 9.0:

CUCM Admin user interface supports only Chinese (China), Japanese (Japan), and Korean (Korea Republic).

CUCM Self Care Portal user interface supports the following user locales (languages and prompts): Arabic(Algeria), Arabic (Bahrain), Arabic (Egypt), Arabic (Iraq), Arabic (Jordan), Arabic (Kuwait), Arabic (Lebanon), Arabic (Morocco), Arabic (Oman), Arabic (Qatar), Arabic (Saudi Arabia), Arabic (Tunisia), Arabic (United Arab Emirates), Arabic (Yemen), Bulgarian (Bulgaria), Catalan (Spain), Chinese (Hong Kong), Chinese (China), Chinese (Taiwan), Croatian (Croatia), Czech (Czech Republic), Danish (Denmark), Dutch (Netherlands), English (United Kingdom), Estonian (Estonia), Finnish (Finland), French (France), German (Germany), Greek (Greece), Hebrew (Israel), Hungarian (Hungary), Italian (Italy), Japanese (Japan), Korean (Korea Republic), Latvian (Latvia), Lithuanian (Lithuania), Norwegian (Norway), Polish (Poland), Portuguese (Brazil), Portuguese (Portugal), Romanian (Romania), Russian (Russian Federation), Serbian (Republic of Montenegro), Serbian (Republic of Serbia), Slovak (Slovakia), Slovenian (Slovenia), Spanish (Colombia), Spanish (Spain), Swedish (Sweden), Thai (Thailand), and Turkish (Turkey).

CUCM supports the following network locales (phone and gateway tones) : Algeria, Argentina, Australia, Austria, Bahrain, Belgium, Brazil, Bulgaria, Canada, Chile, China, Colombia, Croatia, Cyprus, Czech Republic, Denmark, Egypt, Estonia, Finland, France, Germany, Ghana, Greece, Hong Kong, Hungary, Iceland, India, Indonesia, Iraq, Ireland, Israel, Italy, Japan, Jordan, Kenya, Korea Republic, Kuwait, Latvia, Lebanon, Lithuania, Luxembourg, Malaysia, Mauritania, Mexico, Morocco, Nepal, Netherlands, New Zealand, Nigeria, Norway, Oman, Pakistan, Panama, Peru, Philippines, Poland, Portugal, Qatar, Romania, Republic of Montenegro, Republic of Serbia, Russian Federation, Saudi Arabia, Singapore, Slovakia, Slovenia, South Africa, Spain, Sudan, Sweden, Switzerland, Taiwan, Thailand, Tunisia, Turkey, United Arab Emirates, United Kingdom, Venezuela, Vietnam, Yemen, Zimbabwe.

## List of user and network locales for CUCM 8.6 :

CUCM Admin user interface supports only Chinese (China), Japanese (Japan), and Korean (Korea Republic).

CUCM Self Care Portal user interface supports the following user locales (languages and prompts): Arabic(Algeria), Arabic (Bahrain), Arabic (Egypt), Arabic (Iraq), Arabic (Jordan), Arabic (Kuwait), Arabic (Lebanon), Arabic (Morocco), Arabic (Oman), Arabic (Qatar), Arabic (Saudi Arabia), Arabic (Tunisia), Arabic (United Arab Emirates), Arabic (Yemen), Bulgarian (Bulgaria), Catalan (Spain), Chinese (Hong Kong), Chinese (China), Chinese (Taiwan), Croatian (Croatia), Czech (Czech Republic), Danish (Denmark), Dutch (Netherlands), English (United Kingdom) * , Estonian (Estonia), Finnish (Finland), French (France), German (Germany), Greek (Greece), Hebrew (Israel), Hungarian (Hungary), Italian (Italy), Japanese (Japan), Korean (Korea Republic), Latvian (Latvia), Lithuanian (Lithuania), Norwegian (Norway), Polish (Poland), Portuguese (Brazil), Portuguese (Portugal), Romanian (Romania), Russian (Russian Federation), Serbian (Republic of Montenegro), Serbian (Republic of Serbia), Slovak (Slovakia), Slovenian (Slovenia), Spanish (Colombia), Spanish (Spain), Swedish (Sweden), Thai (Thailand), and Turkish (Turkey).

* English (United Kingdom) locale has now been updated linguistically.

CUCM supports the following network locales (phone and gateway tones) : Algeria, Argentina, Australia, Austria, Bahrain, Belgium, Brazil, Bulgaria, Canada, Chile, China, Colombia, Croatia, Cyprus, Czech Republic, Denmark, Egypt, Estonia, Finland, France, Germany, Ghana, Greece, Hong Kong, Hungary, Iceland, India, Indonesia, Iraq, Ireland, Israel, Italy, Japan, Jordan, Kenya, Korea Republic, Kuwait, Latvia, Lebanon, Lithuania, Luxembourg, Malaysia, Mauritania, Mexico, Morocco, Nepal, Netherlands, New Zealand, Nigeria, Norway, Oman, Pakistan, Panama, Peru, Philippines, Poland, Portugal, Qatar, Romania, Republic of Montenegro, Republic of Serbia, Russian Federation, Saudi Arabia, Singapore, Slovakia, Slovenia, South Africa, Spain, Sudan, Sweden, Switzerland, Taiwan, Thailand, Tunisia, Turkey, United Arab Emirates, United Kingdom, Venezuela, Vietnam, Yemen, Zimbabwe.

# Translated Documentation

### User Documentation:

CUCM Admin, Self Care, SRND, and IM and Presence Documentation: http://www.cisco.com/c/en/us/support/unified-communications/unified-communications- manager-callmanager/tsd-products-support-translated-end-user-guides-list.html

### Cisco IP Phone Documentation:

Cisco IP Phone 3905 Quick Start Guide: http://www.cisco.com/en/US/products/ps7193/tsd_products_support_translated_end_user_guides

_list.html

Cisco IP Phone 6901 User Guide and Quick Start Guide: http://www.cisco.com/en/US/products/ps10326/tsd_products_support_translated_end_user_guid es_list.html

Cisco IP Phone 7800 series User Guide and Quick Start guide: Cisco IP Phone 7800 Series - Translated End-User Guides - Cisco

Cisco IP Phone 7900 series User Guide and Quick Start Guide: http://www.cisco.com/en/US/products/hw/phones/ps379/tsd_products_support_translated_end_u ser_guides_list.html

Cisco IP Phone 8800 series User Guide and Quick Start Guide: http://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/tsd- products-support-translated-end-user-guides-list.html

Cisco IP Phone 9951/9971 Firmware User Guide and Quick Start Guide: http://www.cisco.com/en/US/products/ps10453/tsd_products_support_translated_end_user_guid es_list.html

Cisco DX series Documentation: DX650, DX70, DX80: http://www.cisco.com/c/en/us/support/collaboration-endpoints/desktop-collaboration-experience- dx600-series/tsd-products-support-translated-end-user-guides-list.html

| Cisco Unified Communications Product | Locale |
|---|---|
| Cisco Unified Communication Manager (CUCM) | User Locale, Network Locale |
| Cisco IP Phone Only | Phone-Only Locale |
| Cisco Unified Communications Manager IM & Presence | User Locale |

| CUCM LI Version (matches CUCM major.minor version) | PO LI version (matches IP phone firmware major.minor version) |
|---|---|
| CUCM LI 14.0 | PO LI 14.0 |
| CUCM LI 12.5/SU3/SU4 | PO LI 12.8 |
| CUCM LI 12.0 | PO LI 12.0 |
| CUCM LI 11.5/SU10 | PO LI 14.0 |
| CUCM LI 11.5/SU8/SU9 | PO LI 12.8 |
| CUCM LI 11.0 | PO LI 10.3.1 (provides localization support for both FW 10.3.1) |
| CUCM LI 10.5.1 | PO LI 10.2.1 (provides localization support for both FW 10.2.1 and FW 9.4.2) |
| CUCM LI 10.0.x | PO LI 10.1.1 (provides localization support for both FW 10.1 and FW 9.4.1) |
| CUCM LI 9.1.x | PO LI 9.3.2 |
| CUCM LI 9.0.x | PO LI 9.3.1 |
| CUCM LI 8.6.x | PO LI 9.2.x |
| CUCM LI 8.5.x | PO LI 9.1.x |
| CUCM LI 8.0.x | PO LI 9.0.x |
| CUCM LI 7.1.x | PO LI 8.5.x |
| CUCM LI 7.0.x | PO LI 8.4.x |
| CUCM LI 6.1.x | PO LI 8.3.x |
| CUCM LI 10.5.1 | PO LI 10.2.1 (provides localization support for both FW 10.2.1 and FW 9.4.2) |
| CUCM LI 10.0.x | PO LI 10.1.1 (provides localization support for both FW 10.1 and FW 9.4.1) |
| CUCM LI 9.1.x | PO LI 9.3.2 |
| CUCM LI 9.0.x | PO LI 9.3.1 |
| CUCM LI 8.6.x | PO LI 9.2.x |
| CUCM LI 8.5.x | PO LI 9.1.x |
| CUCM LI 8.0.x | PO LI 9.0.x |
| CUCM LI 7.1.x | PO LI 8.5.x |
| CUCM LI 7.0.x | PO LI 8.4.x |
| CUCM LI 6.1.x | PO LI 8.3.x |