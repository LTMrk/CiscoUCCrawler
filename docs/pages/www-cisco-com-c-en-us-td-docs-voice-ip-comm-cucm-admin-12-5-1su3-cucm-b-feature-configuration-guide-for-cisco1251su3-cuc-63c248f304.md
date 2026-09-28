---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-cucm-b-feature-configuration-guide-for-cisco1251su3-cuc-63c248f304
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/cucm_b_feature-configuration-guide-for-cisco1251su3/cucm_m_licensing.html
retrieved_at: 2026-08-16T17:05:04.364240+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: July 31, 2025

Chapter: Licensing

## Chapter: Licensing

# Licensing

## Licensing

Cisco Unified Communications Manager licensing is part of the overall commercial offer of Cisco Unified Communications Licensing.

User Connect Licensing (Essential)

User Connect Licensing (Basic)

User Connect Licensing (Enhanced/ Enhanced

Plus)

Unified Workspace Licensing

Cisco Unified CM Features

Mobile Connect (SNR)

Not Available

Included

Included

Included

Device Support

Number of Devices

1

1

1/2

10

Device Type Support

Analog/Voice (for details, see the User and Device table)

Voice (for details, see the User and Device table)

Voice (for details, see the User and Device table)

Voice (for details, see the User and Device table)

Number of User Profiles

1

1

1

1

Clients

Jabber Mobile

Not Available

Included

Included

Jabber Desktop

Not Available

Included

Included

Jabber IM/Presence

Included

Included

Included

Included

Application

Add-on

Add-on

Included

Webex Social

Add-on

Add-on

Included

Add-on

Included

Cisco Unified CM

Included

Included

Included

Included

Licensing for the Cisco Unified Communications Manager is determined by the total number of users, user features, and devices
                              configured. Cisco Unified Communications Manager calculates its license usage based upon the total number of users (with user
                              features and associated devices) and devices configured on the system. Cisco Unified Communications Manager reports the total
                              license usage (per publisher) to the Cisco Smart Software Manager and gets back the license compliance or non-compliance status.

## Unified Communications Manager Licensing

Cisco Unified Workspace Licensing (UWL) allows organizations to access a wide range of Cisco Collaboration applications and
                              services in a cost-effective, simple package. It includes soft clients, application server software, and licensing on a per
                              user basis.

Cisco User Connect Licensing (UCL) is a user-based license for individual Cisco Unified Communications products. It includes
                              a soft client, application server software licensing, and basic unified communications applications. Depending on your needs
                              and device of choice, UCL is available in Essential, Basic, Enhanced, or Enhanced Plus.

The following are the license types for the Unified Communications Manager:

UC Manager Essential

Essential User Connect License - supports one device providing basic voice or analog device (phone or fax). (For example:
                                          analog phone, ATA 186, ATA 187, Cisco 3905, Cisco 6901)

UC Manager Basic

Basic User Connect License - supports one device, including all Essential devices, plus basic (voice and video) call control
                                          features. (For example: Cisco 6911, Cisco 6921)

UC Manager Enhanced

Enhanced User Connect License - supports one device, including all Basic devices, plus advanced (voice and video) call control
                                          features including desktop, mobile clients. (For example: Cisco 3911, Cisco 3951, Cisco 6941, Cisco 6945, Cisco 6961, Cisco
                                          79xx, Cisco 89xx, Cisco 99xx, Cisco E20, Cisco TelePresence EX60, Cisco TelePresence EX90, third party SIP)

UC Manager Enhanced Plus

Enhanced Plus User Connect License - supports up to two devices, and including all Enhanced devices.

UC Manager CUWL

Supports advanced (voice and video) call control features including desktop and mobile, professional collaboration workspace
                                          application features with a maximum of ten devices per user.

UC Manager TelePresence Room

TelePresence Room license - supports room based immersive and multipurpose Cisco TelePresence System endpoints and Spark Room.
                                          (For example: Cisco TelePresence System Series 3200, 3000, 1300; Cisco TelePresence MX Series; Cisco TelePresence TX Series;
                                          Cisco TelePresence System Profile Series)

## License Compliance

When first installed, the Unified Communications Manager is fully operational in demonstration mode for an evaluation period
                              of 90 days, until it has successfully registered with the Cisco Smart Software Manager. After registration, the Unified Communications
                              Manager communicates with Cisco Smart Software Manager periodically. The Unified Communications Manager reports the total
                              license requirements by license type to the Cisco Smart Software Manager and then gets back the license status.

Licenses in the non-compliant state for Unified Communications Manager are enforced after a 90-day overage period. At the
                              conclusion of the grace period, Unified Communications Manager enforces non-compliance with the following service degradation:

Devices and Users cannot be provisioned. Changing the configuration of a user that affects licensing (For example: the Enable/Disable
                              IM and Presence and the Enable/Disable Mobility check boxes) is not allowed.

For information about smart licensing operations, see the System Configuration Guide for Cisco Unified Communications Manager

## User Only Licensing

If a user is configured on the system and is not associated with a device, that user does not own any devices and is a "User
                              Only." A user is associated with a device or owns the device if that user's user ID is entered in the OwnerUserID field of
                              the device. The licensing for a "User Only" is shown in the User and Device Support table, for the user not associated with
                              any devices.

Simply adding a user to the system does not consume a license if that user does not own any devices or does not use a licensed
                              user feature. If, however, the user is configured with a licensed user feature, or that user does own a device, then the user
                              does consume a license. The only licensed feature currently is Mobile Connect (also known as Mobility or Single Number Reach
                              or SNR).

Mobile Connect (or Mobility or Single Number Reach) for a user is configured when a Remote Destination Profile (RDP) has been
                              created with the end-user set as the Device owner (User ID field).

## Device Only

If a device is added to Cisco Unified Communications Manager and does not have an entry for OwnerUserID field in its Device
                              Configuration window, then the device is not assigned or not associated to a user and called "Device Only". The licensing
                              for "Device Only" devices is listed in the Cisco Unified Communications Manager Licensing - User and Device Support table.
                              If a device is added to Cisco Unified Communications Manager and does not have an entry for OwnerUserID, then the device would
                              require the minimum license type determined by device type, as shown in the Licensing - User and Device Support table.

## User and Device

Once a device is assigned or associated with a user, by entering a user ID in the OwnerUserID field of the device, the licensing
                              requirements for that user and device are determined by the type of device and the number of devices assigned to the user.
                              For a user that owns one device, if the user ID of that user is added as OwnerUserID to one Essential device (such as a 3905,
                              6901, or analog device), then the User and Device minimum license that is required is an Essential license. This means that
                              the one Essential license supports both the user and the device. If instead, that user ID of that user is added as OwnerUserID
                              to one Basic device (such as 6911 or 6921), then the user and device minimum license that is required is one Basic icense.
                              If the user ID of a user is added as OwnerUserID to one Enhanced device, the user and device minimum license that is required
                              is an Enhanced license.

For users that own more than one device, the minimum licensing is determined by the number of devices that are owned by the
                              user. Cisco Unified Communications Manager Licensing table shows the maximum number of devices per user license that is supported.
                              A user that owns two devices requires an Enhanced Plus license at a minimum. A user that owns more than two devices requires
                              a CUWL license at a minimum.

Cisco Unified Communications Manager Licensing - User and Device Support table summarizes Cisco Unified Communications Manager
                              Licensing for User Only, Device Only, and User and Device.

License Type

Device Only

User and Device

User Only

UC Manager Essential

Cisco Unified SIP Phone 3905

Cisco Unified IP Phone 6901

Analog devices

A user with 1 Essential device.

N/A

UC Manager Basic

Cisco Unified IP Phone 6911 and 6921 models

OR

Any device from UC Manager Essential license type.

A user with 1 Basic device.

OR

A user and associated device from the UC Manager Essential license type.

A user with Single Number Reach (Mobile Connect).

OR

A user with an UC Manager Essential license type.

UC Manager Enhanced

Cisco Unified IP Phone 3911, 3941, 3951

Cisco Unified IP Phone 6941, 6945, and 6961 models

Cisco Unified IP Phone 7900 Series (7900G, 7911G, 7912G, 7931G, 794xG, 796xG, and 7975G models)

Cisco Unified IP Phone 8900 Series (8941, 8945, and 8961 models)

Cisco Unified IP Phone 9900 Series (9951 and 9971 models) with or without a camera

Cisco Unified Wireless IP Phones Series (792xG and 7925G-EX models)

Cisco Unified IP Conference Stations (7936G and 7937G stations)

Cisco Unified Softphones (Cisco Unified Personal Communicator, Cisco UC Integration for Lync, Cisco UC Integration for Connect,
                                                and Cisco IP Communicator)

Jabber clients (Jabber for Mac, Jabber for Windows, Jabber for iPhone, Jabber for Android, Jabber for iPad, and Jabber SDK)

Cisco Virtual Experience Clients (VXC) with voice and video firmware

Cisco IP Video Phone E20

Cisco TelePresence System EX Series (EX60 and EX90)

Third-party SIP devices

Cisco Desktop Collaboration Experience DX600 Series

Transnova S3

Cisco Spark Room Device

IMS

OR

Any device from the UC Manager Essential or UC Manager Basic license type.

A user with 1 Enhanced device.

OR

A user and associated device with UC Manager Essential or UC Manager Basic license type.

N/A

UC Manager Enhanced Plus

N/A

A user with 2 devices.

OR

A user and associated devices with UC Manager Essential, UC Manager Basic, UC Manager Enhanced , or UC Manager Enhanced Plus license type.

N/A

UC Manager TelePresence Room License

Cisco TelePresence System 500 Series

Cisco TelePresence System 1100

Cisco TelePresence System 1300 Series

Cisco TelePresence System 3000 Series

Cisco TelePresence System 3200 Series

Cisco TelePresence TX9000 Series (TX9000, TX9200)

Cisco TelePresence TX1300 Series

Cisco TelePresence System Profile Series (42-inch 6000 MXP, 52- inch MXP, 52- inch Dual MXP, 65-inch, and 65- inch Dual)

Cisco TelePresence System Codecs C90/C60/C40

Cisco TelePresence System Quick Set C20

Cisco TelePresence MX Series (MX300 and MX200)

Cisco TelePresence 1000

Cisco TelePresence SX series

Cisco Webex devices

Generic Desktop Video Endpoint

Generic Multiple Screen Room System

Generic Single Screen Room System

A user with 1 UC Manager TelePresence Room device associated.

N/A

Device Only means a device configured in Cisco Unified Communications Manager that does not have a user association, where the OwnerUserID
                              field is blank.

User and Device means a device configured in Cisco Unified Communications Manager that has a user associated, the OwnerUserID field has a
                              registered userid.

User Only means a user configured in Cisco Unified Communications Manager that does not have any devices associated with the user -
                              whose user id is not found as OwnerUserID for any Cisco Unified Communications Manager devices.

Bold text in the above table indicates that a device is supported through license substitution where an available license of the license
                              type listed may be used to meet lower-level license requirements. This is done in Cisco Smart Software Manager.

MGCP FXS ports do not require any license because they are not considered analog phones.

## Maximum Number of Devices Per User

The Essential, Basic, and Enhanced licenses support users with one associated device, where the user's id is entered in the
                              OwnerUserId field of one device. The Enhanced Plus license supports users with two associated devices. UWL supports users
                              with three and up to ten associated devices.

## TelePresence Room License

Multi-purpose and immersive TelePresence devices are licensed under a separate device license type that is called the TelePresence
                              Room license. The TelePresence Room license covers both the TelePresence device and phone that is registered to Cisco Unified
                              Communications Manager, only if the same userid is entered as the OwnerUserID field for the TelePresence device and the phone.
                              If the same userid is not entered as OwnerUserID for both the TelePresense device and the phone, then the devices are not
                              associated and two licenses are required: one TelePresence Room license for the device and one Enhanced for the phone. The
                              TelePresence touch device does not register to the Cisco Unified Communications Manager, and therefore does not require a
                              separate license or the OwnerUserID association.

## License Substitution

The Cisco Smart Software Manager (CSSM) allows for tiered license substitution of available licenses to enable compliance.
                              The available higher-level licenses are substituted or loaned to meet lower level license requirements. For example, if a
                              customer has 100 UC Manager CUWL licenses installed, however Cisco Unified Communications Manager is reporting back license
                              requirements for 10 CUWL licenses and 50 UC Manager Enhanced Plus licenses, CSSM will calculate that there are 100-10 or 90
                              UC Manager CUWL license available to be loaned to lower tiers. Of the 90 UC Manager CUWL available licenses 50 CUWL would
                              then be used to meet the requirements for the 50 Enhanced Plus licenses. CSSM will show 40 UC Manager CUWL licenses as available.

When Cisco Smart Software Manager On-Prem (Cisco SSM On-Prem) or Smart Software Manager satellite is used in Unified Communications
                                          Manager for licensing, there is a difference in the way the license Hierarchy Substitution breakdown is displayed in CSSM,
                                          when compared to Cisco SSM On-Prem. See the Cisco SSM On-Prem user interface for details on the insufficient license information
                                          if the license authorization status of Unified CM is Out of Compliance. Refer CSCwf47221 for more details.

If the Virtual account is already used by Product Instance using direct communication and license reserved for Specific License
                                          Reservation, the available license quantities are shown incorrectly. Refer CSCwf47223 for more details.

## Licensing Scenarios

The following licensing scenarios will walk through the configuration changes on the Cisco Unified Communications Manager
                              Administration that result in licensing requirements.

## Adding Users

When a new user (UserA) is first added to Cisco Unified Communications Manager Administration through the End User configuration
                              or through the Bulk Administration tool, if the user does not have remote device profiles under Enable Mobility, then the
                              new user does not require a license.

If a new user (UserB) is first added to Cisco Unified Communications Manager with remote destination profiles configured under
                              Enable Mobility, then the new user, UserB, requires a Basic license.

UserID

Licensed User Feature

License Required

UserA

None

None

With no assigned devices

UserB

Mobility

Basic

With no assigned devices

## Adding Unassociated Devices

If a new device is registered to Cisco Unified Communications Manager and there is no user id entered in the OwnerUserID field
                              for the device, then the device is unassociated to a user, and requires the license per device type for unassociated devices,
                              as indicated in Cisco Unified Communications Manager Licensing - User and Device Support table. For example, Device6901 is
                              added and it requires an Essential license. Device6921 is added and it requires a Basic license. DeviceEX60 is added and it
                              requires an Enhanced device.

There are currently no devices that require an Enhanced Plus, CUWL Standard, or CUWL Professional license. So you will not
                              see a requirement in Cisco Unified Communications Manager for an unassociated device that requires an Enhanced Plus or above
                              license.

Device

License Required

Device6901

UC Manager Essential

With no OwnerUserID

Device6921

UC Manager Basic

With no OwnerUserID

DeviceEX60

UC Manager Enhanced

With no OwnerUserID

## Adding Users with Associated Devices

When a device is added, if the device is associated with a user, then the user and device share a license. For one device
                              per user, the license that is required is the greater of the user license or device license required. The following scenarios
                              review the different combinations of device and user associations for one device per user.

### Essential Device Associated to User

If Device6901 (an Essential device) is assigned to UserA, by entering OwnerUserID = UserA, then both the device and user are
                              supported by one Essential license.

If however, Device6901 (an Essential device) is assigned to UserB (a Basic user), by entering OwnerUserID = UserB then both
                              device and user are supported by one Basic License.

### Basic Device Associated to User

If Device6921 (a Basic device) is assigned to UserA by entering OwnerUserID = UserA, then both the device and user are supported
                              by one Basic license. Similarly, if Device6921 (a Basic device) is assigned to UserB (a Basic user) by entering OwnerUserID
                              = UserB, then both the device and user are supported by one Basic license.

### Enhanced Device Associated to User

Most physical phones, soft clients, and desktop video devices such as the EX60 and EX90 are included in the Enhanced device
                              level. If Device EX60 (an Enhanced device) is assigned to UserA by entering OwnerUserID = UserA, then both the device and
                              user is supported by one Enhanced license. Similarly, if DeviceEX60 (an Enhanced device) is assigned to UserB (a Basic user)
                              by entering OwnerUserID = UserB, then both the device and user are supported by one Enhanced license.

Device

OwnerUserID

Licensed User Feature

License Required

Device6901

UserA

None

UC Manager Essential

UserB

Mobility

UC Manager Basic

Device6921

UserA

None

UC Manager Basic

UserB

Mobility

UC Manager Basic

DeviceEX60

UserA

None

UC Manager Enhanced

UserB

Mobility

UC Manager Enhanced

## Number of Devices Per User

The above examples for Users and Devices apply only when a user is associated with one device - where their userid is found
                              in only one device configuration OwnerUserID field. When a user is associated with more than one device, then higher level
                              licenses are required independent of device type.

If UserA is assigned to OwnerUserID for one device then the scenarios above apply. If, however, UserA is assigned OwnerUserID
                              for two devices, then one Enhanced Plus license is required for both the user and the two associated devices. If UserA is
                              assigned OwnerUserID for more than two devices, then one UWL Standard license is required. UserA can be assigned up to ten
                              devices with one UWL Standard license. If more than ten devices are assigned to one user, then the user requires one UWL Standard
                              license and also requires an additional license for the additional device.

## License Usage Report

Usage details are available by license type, users, and unassigned devices. Usage information is updated once every six hours
                              and maybe updated manually by clicking on Update Usage Details. Clicking Update Usage Details is a resource-intensive process
                              and may take a few minutes depending on the size of your system. There is a link provided to review the Unified Communications
                              licensing information in View all license type descriptions and device classifications.

The Status message displays if there is an alarm or licensing alert (license non-compliance). See Alarms alerts and license status notifications
                              for further information on status messages. See License Compliance for further information on license compliance and non-compliance.

The License Requirements by Type table shows the current system license requirements. It shows current license usage (number of licenses required) by license
                              type and summarizes the number of users and unassigned devices that are requiring licenses by license type. The Report links
                              by license type are provided by (number of) Users or (number of) Unassigned devices and allow drill-down links. For the User
                              report, the user id link provides details on user configuration per the user id. The view details link provides license requirements
                              per user id. For the Unassigned Devices report, the Device Type and License Type that is required is displayed for each unassigned
                              device.

License Usage Reports are also available summarized by Users and Unassigned devices. The Users row lists the total number
                              of users configured on the system. View Usage Report for the users provides a report for all users configured on the system
                              and their corresponding license requirements. View Usage Report for the Unassigned Devices shows the total number of unassigned
                              devices (devices with no associated user).

Assigning a user ID to a device using Cisco Unified Communications Administration moves the device from "Unassigned Devices"
                                          to "Users" in the License Usage Report. However, adding a device to the list of controlled devices for an end-user does not
                                          modify the "License Usage Report" results for the device.

## Cisco Unified Reporting

The following reports are available from the Cisco Unified Reporting console for Cisco Unified Communications Solutions.

From Cisco Unified Communications Manager Administration login page Navigation bar, click Cisco Unified Reporting.

Choose System Reports.

Choose Unified CM Device Counts Summary.

The generated report will summarize, per cluster, the device counts by model.

From Cisco Unified Communications Manager Administration login page Navigation bar, click Cisco Unified Reporting.

Choose System Reports.

Choose Unified CM User Device Count.

The generated report will summarize, per cluster, the phone to user relationship the number of phones with no users, users
                              with one phone, and users with more than one phone.

From Cisco Unified Communications Manager Administration login page Navigation bar, click Cisco Unified Reporting.

Choose System Reports.

Choose Unified CM User Device Count.

The generated report will summarize, per cluster, the phone to user relationship the number of phones with no users, users
                              with one phone, and users with more than one phone.

|  |  | User Connect Licensing (Essential) | User Connect Licensing (Basic) | User Connect Licensing (Enhanced/ Enhanced Plus) | Unified Workspace Licensing |
|---|---|---|---|---|---|
| Cisco Unified CM Features | Mobile Connect (SNR) | Not Available | Included | Included | Included |
| Device Support | Number of Devices | 1 | 1 | 1/2 | 10 |
| Device Type Support | Analog/Voice (for details, see the User and Device table) | Voice (for details, see the User and Device table) | Voice (for details, see the User and Device table) | Voice (for details, see the User and Device table) |
| Number of User Profiles | 1 | 1 | 1 | 1 |
| Clients | Jabber Mobile | Not Available | Not Available | Included | Included |
| Jabber Desktop | Not Available | Not Available | Included | Included |
| Jabber IM/Presence | Included | Included | Included | Included |
| Application | Webex Meetings | Add-on | Add-on | Add-on | Included |
| Webex Social | Add-on | Add-on | Add-on | Included |
| Unity Connection | Add-on | Add-on | Add-on | Included |
| Cisco Unified CM | Included | Included | Included | Included |

| UC Manager Essential | Essential User Connect License - supports one device providing basic voice or analog device (phone or fax). (For example:
                                          analog phone, ATA 186, ATA 187, Cisco 3905, Cisco 6901) |
|---|---|
| UC Manager Basic | Basic User Connect License - supports one device, including all Essential devices, plus basic (voice and video) call control
                                          features. (For example: Cisco 6911, Cisco 6921) |
| UC Manager Enhanced | Enhanced User Connect License - supports one device, including all Basic devices, plus advanced (voice and video) call control
                                          features including desktop, mobile clients. (For example: Cisco 3911, Cisco 3951, Cisco 6941, Cisco 6945, Cisco 6961, Cisco
                                          79xx, Cisco 89xx, Cisco 99xx, Cisco E20, Cisco TelePresence EX60, Cisco TelePresence EX90, third party SIP) |
| UC Manager Enhanced Plus | Enhanced Plus User Connect License - supports up to two devices, and including all Enhanced devices. |
| UC Manager CUWL | Supports advanced (voice and video) call control features including desktop and mobile, professional collaboration workspace
                                          application features with a maximum of ten devices per user. |
| UC Manager TelePresence Room | TelePresence Room license - supports room based immersive and multipurpose Cisco TelePresence System endpoints and Spark Room.
                                          (For example: Cisco TelePresence System Series 3200, 3000, 1300; Cisco TelePresence MX Series; Cisco TelePresence TX Series;
                                          Cisco TelePresence System Profile Series) |

| License Type | Device Only | User and Device | User Only |
|---|---|---|---|
| UC Manager Essential | Cisco Unified SIP Phone 3905 Cisco Unified IP Phone 6901 Analog devices | A user with 1 Essential device. | N/A |
| UC Manager Basic | Cisco Unified IP Phone 6911 and 6921 models OR Any device from UC Manager Essential license type. | A user with 1 Basic device. OR A user and associated device from the UC Manager Essential license type. | A user with Single Number Reach (Mobile Connect). OR A user with an UC Manager Essential license type. |
| UC Manager Enhanced | Cisco Unified IP Phone 3911, 3941, 3951 Cisco Unified IP Phone 6941, 6945, and 6961 models Cisco Unified IP Phone 7900 Series (7900G, 7911G, 7912G, 7931G, 794xG, 796xG, and 7975G models) Cisco Unified IP Phone 8900 Series (8941, 8945, and 8961 models) Cisco Unified IP Phone 9900 Series (9951 and 9971 models) with or without a camera Cisco Unified Wireless IP Phones Series (792xG and 7925G-EX models) Cisco Unified IP Conference Stations (7936G and 7937G stations) Cisco Unified Softphones (Cisco Unified Personal Communicator, Cisco UC Integration for Lync, Cisco UC Integration for Connect,
                                                and Cisco IP Communicator) Jabber clients (Jabber for Mac, Jabber for Windows, Jabber for iPhone, Jabber for Android, Jabber for iPad, and Jabber SDK) Cisco Virtual Experience Clients (VXC) with voice and video firmware Cisco IP Video Phone E20 Cisco TelePresence System EX Series (EX60 and EX90) Third-party SIP devices Cisco Desktop Collaboration Experience DX600 Series Transnova S3 Cisco Spark Room Device IMS OR Any device from the UC Manager Essential or UC Manager Basic license type. | A user with 1 Enhanced device. OR A user and associated device with UC Manager Essential or UC Manager Basic license type. | N/A |
| UC Manager Enhanced Plus | N/A | A user with 2 devices. OR A user and associated devices with UC Manager Essential, UC Manager Basic, UC Manager Enhanced , or UC Manager Enhanced Plus license type. | N/A |
| UC Manager TelePresence Room License | Cisco TelePresence System 500 Series Cisco TelePresence System 1100 Cisco TelePresence System 1300 Series Cisco TelePresence System 3000 Series Cisco TelePresence System 3200 Series Cisco TelePresence TX9000 Series (TX9000, TX9200) Cisco TelePresence TX1300 Series Cisco TelePresence System Profile Series (42-inch 6000 MXP, 52- inch MXP, 52- inch Dual MXP, 65-inch, and 65- inch Dual) Cisco TelePresence System Codecs C90/C60/C40 Cisco TelePresence System Quick Set C20 Cisco TelePresence MX Series (MX300 and MX200) Cisco TelePresence 1000 Cisco TelePresence SX series Cisco Webex devices Generic Desktop Video Endpoint Generic Multiple Screen Room System Generic Single Screen Room System | A user with 1 UC Manager TelePresence Room device associated. | N/A |

| Note | MGCP FXS ports do not require any license because they are not considered analog phones. |
|---|---|

| Note | When Cisco Smart Software Manager On-Prem (Cisco SSM On-Prem) or Smart Software Manager satellite is used in Unified Communications
                                          Manager for licensing, there is a difference in the way the license Hierarchy Substitution breakdown is displayed in CSSM,
                                          when compared to Cisco SSM On-Prem. See the Cisco SSM On-Prem user interface for details on the insufficient license information
                                          if the license authorization status of Unified CM is Out of Compliance. Refer CSCwf47221 for more details. |
|---|---|

| Note | If the Virtual account is already used by Product Instance using direct communication and license reserved for Specific License
                                          Reservation, the available license quantities are shown incorrectly. Refer CSCwf47223 for more details. |
|---|---|

| UserID | Licensed User Feature | License Required | Note |
|---|---|---|---|
| UserA | None | None | With no assigned devices |
| UserB | Mobility | Basic | With no assigned devices |

| Device | License Required | Note |
|---|---|---|
| Device6901 | UC Manager Essential | With no OwnerUserID |
| Device6921 | UC Manager Basic | With no OwnerUserID |
| DeviceEX60 | UC Manager Enhanced | With no OwnerUserID |

| Device | OwnerUserID | Licensed User Feature | License Required |
|---|---|---|---|
| Device6901 | UserA | None | UC Manager Essential |
| UserB | Mobility | UC Manager Basic |
| Device6921 | UserA | None | UC Manager Basic |
| UserB | Mobility | UC Manager Basic |
| DeviceEX60 | UserA | None | UC Manager Enhanced |
| UserB | Mobility | UC Manager Enhanced |

| Note | Assigning a user ID to a device using Cisco Unified Communications Administration moves the device from "Unassigned Devices"
                                          to "Users" in the License Usage Report. However, adding a device to the list of controlled devices for an end-user does not
                                          modify the "License Usage Report" results for the device. |
|---|---|