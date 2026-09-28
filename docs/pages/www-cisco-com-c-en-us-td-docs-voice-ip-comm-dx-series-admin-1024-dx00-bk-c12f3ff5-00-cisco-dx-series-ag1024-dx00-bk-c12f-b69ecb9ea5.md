---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-dx-series-admin-1024-dx00-bk-c12f3ff5-00-cisco-dx-series-ag1024-dx00-bk-c12f-b69ecb9ea5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/dx/series/admin/1024/DX00_BK_C12F3FF5_00_cisco-dx-series-ag1024/DX00_BK_C12F3FF5_00_cisco-dx-series-ag1024_chapter_0110.html
retrieved_at: 2026-08-21T04:58:12.438185+00:00
---

Cisco DX Series Administration Guide, Release 10.2(4)

# Cisco DX Series Administration Guide, Release 10.2(4)

Updated: June 25, 2015

Chapter: Contacts

## Chapter: Contacts

Contents

# Contacts

## Contacts and Directories by Operating Mode

Contact Source

Public Mode

Simple Mode

Enhanced Mode

Created on device

Yes

Yes

Yes

Imported from Bluetooth

Yes

Yes

Yes

Cisco User Data Services (UDS)

Yes

Yes

Yes

Jabber

No

No

Yes

Exchange Global Address List

No

No

Yes

Google

No

No

Yes

Third-party apps

No

No

Yes

## Local Contacts

Local contacts are the contacts that a user creates on their DX device. Local contacts can also include contacts imported from a mobile phone via Bluetooth.

In Enhanced Mode, local contacts can also include contacts synced from Jabber, an Exchange account, a Google account, or third party applications.

Local contacts with a phone number are available on the Contacts tab in the Call application. All local contacts are available in the People application.

## Corporate Directory

The Corporate Directory allows a user to look up contact information
for coworkers. To support this feature, you must configure
a corporate directory.

Cisco Unified Communications Manager uses a Lightweight Directory Access Protocol (LDAP)
directory to store information
about users of Cisco Unified Communications Manager , and to sync to Active Directory (AD).

Cisco DX Series devices use Cisco User Data Services (UDS) to query Cisco Unified Communications Manager for corporate directory information.

Cisco DX Series devices do not support traditional XML directories, including custom directories.

For more information about setting up LDAP, see the Cisco Unified Communications Manager Administration Guide .

- Set Company Photo Directory

### Set Company Photo Directory

Set this parameter to show directory photos when a user searches the corporate directory using UDS, and for directory search results that the user adds as a local contact.

Device > Phone

Device > Device
						  Settings > Common Phone Profile

System > Enterprise
						  Phone

If you configure the parameter in multiple windows, the precedence
				order is:

Device > Phone

Device > Device
						  Settings > Common Phone Profile

System > Enterprise
						  Phone

## Contacts Search

Cisco DX Series users can search their locally stored contacts, Recents and corporate directory (UDS).
Users operating DX Series devices in Enhanced Mode can also search Jabber contacts and online directories such as Exchange.

First name

Last name

Phone number

Username

Users can search their corporate directory on the Directory tab. Corporate directory searches show a maximum of 25 results.

Search results will show a photo (if available), first and last name, and a URI or phone number. If the search result includes both a URI and a phone number, the URI is shown.

- Optimize Search Results

### Optimize Search Results

By default, the user can search for local contacts on the Calls tab, but not directories. Follow this procedure to show corporate directory results while  searching on the Calls tab. Directory results will show up below local contacts in the search results, and will be sorted by directory type.

## Application Dial Rules

Application Dial Rules are used to convert numbers for shared mobile contacts to network dialable numbers.  Application Dial Rules do not apply when the user is dialing a number manually, or if the number is edited before the user places the call.

Application Dial Rules are set in Cisco Unified Communications Manager . For more information, see the "Dial Rules Overview" chapter of the Cisco Unified Communications Manager System Guide .

- Configure Application Dial Rules

### Configure Application Dial Rules

- Name This field comprises a unique name for the dial rule that can contain up to 20 alphanumeric characters and any combination of spaces, periods (.), hyphens (-), and underscore characters (_).

- Description This field comprises a brief description that you enter for the dial rule.

- Number Begins With This field comprises the initial digits of the directory numbers to which you want to apply this application dial rule.

- Number of Digits This required field comprises the initial digits of the directory numbers to which you want to apply this application dial rule.

- Total Digits to be Removed This required field comprises the number of digits that you want Cisco Unified Communications Manager to remove from directory numbers that apply to this dial rule.

- Prefix With Pattern This required field comprises the pattern to prepend to directory numbers that apply to this application dial rule.

- Application Dial Rule Priority This field displays when you enter the Prefix With Pattern information. The field allows you to set the priority order of the application dial rules.

# Contacts

## Contacts and Directories by Operating Mode

Contact Source

Public Mode

Simple Mode

Enhanced Mode

Created on device

Yes

Yes

Yes

Imported from Bluetooth

Yes

Yes

Yes

Cisco User Data Services (UDS)

Yes

Yes

Yes

Jabber

No

No

Yes

Exchange Global Address List

No

No

Yes

Google

No

No

Yes

Third-party apps

No

No

Yes

## Local Contacts

Local contacts are the contacts that a user creates on their DX device. Local contacts can also include contacts imported from a mobile phone via Bluetooth.

In Enhanced Mode, local contacts can also include contacts synced from Jabber, an Exchange account, a Google account, or third party applications.

Local contacts with a phone number are available on the Contacts tab in the Call application. All local contacts are available in the People application.

## Corporate Directory

The Corporate Directory allows a user to look up contact information
for coworkers. To support this feature, you must configure
a corporate directory.

Cisco Unified Communications Manager uses a Lightweight Directory Access Protocol (LDAP)
directory to store information
about users of Cisco Unified Communications Manager , and to sync to Active Directory (AD).

Cisco DX Series devices use Cisco User Data Services (UDS) to query Cisco Unified Communications Manager for corporate directory information.

Cisco DX Series devices do not support traditional XML directories, including custom directories.

For more information about setting up LDAP, see the Cisco Unified Communications Manager Administration Guide .

- Set Company Photo Directory

### Set Company Photo Directory

Set this parameter to show directory photos when a user searches the corporate directory using UDS, and for directory search results that the user adds as a local contact.

Device > Phone

Device > Device
						  Settings > Common Phone Profile

System > Enterprise
						  Phone

If you configure the parameter in multiple windows, the precedence
				order is:

Device > Phone

Device > Device
						  Settings > Common Phone Profile

System > Enterprise
						  Phone

## Contacts Search

Cisco DX Series users can search their locally stored contacts, Recents and corporate directory (UDS).
Users operating DX Series devices in Enhanced Mode can also search Jabber contacts and online directories such as Exchange.

First name

Last name

Phone number

Username

Users can search their corporate directory on the Directory tab. Corporate directory searches show a maximum of 25 results.

Search results will show a photo (if available), first and last name, and a URI or phone number. If the search result includes both a URI and a phone number, the URI is shown.

- Optimize Search Results

### Optimize Search Results

By default, the user can search for local contacts on the Calls tab, but not directories. Follow this procedure to show corporate directory results while  searching on the Calls tab. Directory results will show up below local contacts in the search results, and will be sorted by directory type.

## Application Dial Rules

Application Dial Rules are used to convert numbers for shared mobile contacts to network dialable numbers.  Application Dial Rules do not apply when the user is dialing a number manually, or if the number is edited before the user places the call.

Application Dial Rules are set in Cisco Unified Communications Manager . For more information, see the "Dial Rules Overview" chapter of the Cisco Unified Communications Manager System Guide .

- Configure Application Dial Rules

### Configure Application Dial Rules

- Name This field comprises a unique name for the dial rule that can contain up to 20 alphanumeric characters and any combination of spaces, periods (.), hyphens (-), and underscore characters (_).

- Description This field comprises a brief description that you enter for the dial rule.

- Number Begins With This field comprises the initial digits of the directory numbers to which you want to apply this application dial rule.

- Number of Digits This required field comprises the initial digits of the directory numbers to which you want to apply this application dial rule.

- Total Digits to be Removed This required field comprises the number of digits that you want Cisco Unified Communications Manager to remove from directory numbers that apply to this dial rule.

- Prefix With Pattern This required field comprises the pattern to prepend to directory numbers that apply to this application dial rule.

- Application Dial Rule Priority This field displays when you enter the Prefix With Pattern information. The field allows you to set the priority order of the application dial rules.

| Contact Source | Public Mode | Simple Mode | Enhanced Mode |
|---|---|---|---|
| Created on device | Yes | Yes | Yes |
| Imported from Bluetooth | Yes | Yes | Yes |
| Cisco User Data Services (UDS) | Yes | Yes | Yes |
| Jabber | No | No | Yes |
| Exchange Global Address List | No | No | Yes |
| Google | No | No | Yes |
| Third-party apps | No | No | Yes |

| Step 1 | In Cisco Unified Communications Manager Administration, select one
			 of the following windows: Device > Phone Device > Device
						  Settings > Common Phone Profile System > Enterprise
						  Phone If you configure the parameter in multiple windows, the precedence
				order is: Device > Phone Device > Device
						  Settings > Common Phone Profile System > Enterprise
						  Phone |
|---|---|
| Step 2 | Set Company Photo Directory to http://<servername>/<path>/%%uid%%.<image file
extension> . |
| Step 3 | Check Override Common Settings . |

| Step 1 | Tap . |
|---|---|
| Step 2 | Tap Settings . |
| Step 3 | Check Directory results . |

| Step 1 | In Cisco Unified Communications Manager Administration, go to Call Routing > Dial Rules > Application Dial Rules . |
|---|---|
| Step 2 | Choose Add New to create a new application dial rule, or choose an existing application dial rule to edit it. |
| Step 3 | Fill in the following fields: Name This field comprises a unique name for the dial rule that can contain up to 20 alphanumeric characters and any combination of spaces, periods (.), hyphens (-), and underscore characters (_). Description This field comprises a brief description that you enter for the dial rule. Number Begins With This field comprises the initial digits of the directory numbers to which you want to apply this application dial rule. Number of Digits This required field comprises the initial digits of the directory numbers to which you want to apply this application dial rule. Total Digits to be Removed This required field comprises the number of digits that you want Cisco Unified Communications Manager to remove from directory numbers that apply to this dial rule. Prefix With Pattern This required field comprises the pattern to prepend to directory numbers that apply to this application dial rule. Application Dial Rule Priority This field displays when you enter the Prefix With Pattern information. The field allows you to set the priority order of the application dial rules. |
| Step 4 | Restart Cisco Unified Communications Manager . |

| Contact Source | Public Mode | Simple Mode | Enhanced Mode |
|---|---|---|---|
| Created on device | Yes | Yes | Yes |
| Imported from Bluetooth | Yes | Yes | Yes |
| Cisco User Data Services (UDS) | Yes | Yes | Yes |
| Jabber | No | No | Yes |
| Exchange Global Address List | No | No | Yes |
| Google | No | No | Yes |
| Third-party apps | No | No | Yes |

| Step 1 | In Cisco Unified Communications Manager Administration, select one
			 of the following windows: Device > Phone Device > Device
						  Settings > Common Phone Profile System > Enterprise
						  Phone If you configure the parameter in multiple windows, the precedence
				order is: Device > Phone Device > Device
						  Settings > Common Phone Profile System > Enterprise
						  Phone |
|---|---|
| Step 2 | Set Company Photo Directory to http://<servername>/<path>/%%uid%%.<image file
extension> . |
| Step 3 | Check Override Common Settings . |

| Step 1 | Tap . |
|---|---|
| Step 2 | Tap Settings . |
| Step 3 | Check Directory results . |

| Step 1 | In Cisco Unified Communications Manager Administration, go to Call Routing > Dial Rules > Application Dial Rules . |
|---|---|
| Step 2 | Choose Add New to create a new application dial rule, or choose an existing application dial rule to edit it. |
| Step 3 | Fill in the following fields: Name This field comprises a unique name for the dial rule that can contain up to 20 alphanumeric characters and any combination of spaces, periods (.), hyphens (-), and underscore characters (_). Description This field comprises a brief description that you enter for the dial rule. Number Begins With This field comprises the initial digits of the directory numbers to which you want to apply this application dial rule. Number of Digits This required field comprises the initial digits of the directory numbers to which you want to apply this application dial rule. Total Digits to be Removed This required field comprises the number of digits that you want Cisco Unified Communications Manager to remove from directory numbers that apply to this dial rule. Prefix With Pattern This required field comprises the pattern to prepend to directory numbers that apply to this application dial rule. Application Dial Rule Priority This field displays when you enter the Prefix With Pattern information. The field allows you to set the priority order of the application dial rules. |
| Step 4 | Restart Cisco Unified Communications Manager . |