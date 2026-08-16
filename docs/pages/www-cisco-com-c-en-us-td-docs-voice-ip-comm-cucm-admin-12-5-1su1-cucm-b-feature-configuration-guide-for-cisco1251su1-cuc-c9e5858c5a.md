---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-cucm-b-feature-configuration-guide-for-cisco1251su1-cuc-c9e5858c5a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/cucm_b_feature-configuration-guide-for-cisco1251SU1/cucm_m_headset-management.html
retrieved_at: 2026-08-16T17:20:28.853064+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: July 31, 2025

Chapter: Headset Management

## Chapter: Headset Management

# Headset Management

## Headset Management Overview

Headset Management enhances your Cisco headset deployment, letting administrators manage headset serviceability from Cisco
                              Unified Communications Manager. From Cisco Unified CM Administration, administrators can:

Remotely configure headset settings such as wireless power range, audio bandwidth, and Bluetooth on/off.

Define and control the headset firmware.

Get a detailed inventory of all the headsets in your deployment.

Diagnose and troubleshoot headsets with Remote PRT, headset metrics in Call Management Records (CMR), and alarms.

## Feature Compatibility for Headset Management

Cisco Headset Management is supported in Unified Communications Manager from the following releases:

Release 11.5(1)SU7 for 11.x releases

Release 12.5(1)SU1 for 12.x releases

Along with the Unified Communications Manager version, feature support is dependent on the firmware versions of Cisco Headsets,
                              Cisco IP Phone and Cisco Jabber. The following table lists the available headset management features depending on the headset,
                              phone, and Unified Communications Manager versions you use.

New Serviceability Feature

Unified CM 12.5(1) or earlier + Phone Firmware 12.1(1) or earlier

Unified CM 12.5(1)SU1 and above** + Phone Firmware 12.1(1) or earlier

Unified CM 12.5(1) or earlier + Phone Firmware 12.5(1)

Unified CM 12.5(1)SU1 and above** + Phone Firmware 12.5(1)

Unified CM 12.5(1) or earlier + Phone Firmware 12.5(1)SR3

Unified CM 12.5(1)SU1 and above** + Phone Firmware 12.5(1)SR3

COP file installation required

X

X

X

X

X

—

Manual remote configuration

—

—

X

N/A

X

—

Headset firmware management on Unified CM

—

—

—

—

—

X

Remote headset configuration through Unified CM

—

—

—

—

—

X

Headset inventory on Unified CM

—

—

—

—

—

X*

Configuration Reset on the phone UI

—

—

—

—

X

X

Headset Call Management Records (CMR)

—

—

—

—

—

X*

* This feature is only available on headsets with Headset Firmware 1.5 or later.

**This feature is not supported in the 12.0.x and 12.5(1) releases.

N/A When you upgrade to Unified CM 11.5(1)SU7 or higher from an earlier version, most Cisco IP Phones will upgrade automatically
                                    to Phone Firmware 12.5(1)SR3 or higher versions.

New Serviceability Feature

Unified CM 12.5(1) or earlier + Jabber version 12.5(1) or earlier

Unified CM 12.5(1)SU1 and above** + Jabber version 12.5(1) or earlier

Unified CM 12.5(1) or earlier + Jabber version 12.6(1)

Unified CM 12.5(1)SU1 and above** + Jabber version 12.6(1)

Unified CM 12.5(1) or earlier + Jabber version 12.6(1)MR

Unified CM 12.5(1)SU1 and above** + Jabber version 12.6(1)MR

COP file installation required

X

X

X

X

X

X

Headset firmware management through Unified CM

—

—

—

—

—

X

Remote headset configuration through Unified CM

—

—

—

X

—

X

Headset inventory on Unified CM

—

—

—

X*

—

X*

Local configuration reset

—

—

—

—

X

X

Local UI configuration

—

—

X

X

X

X

Local headset version display

—

—

—

—

X

X

* This feature can only detect headsets with Headset Firmware 1.5 or later.

**This feature is not supported in the 12.0.x and 12.5(1) releases.

### Third-Party Headset Support

If you are deploying third-party headsets, Cisco Unified Communications Manager supports headset inventory management with
                                 limited information for the third-party headsets right from the Cisco Unified CM Administration interface. Cisco Unified Communications
                                 Manager does not support headset configuration templates, firmware, diagnostics, and headset CMRs for third-party headsets.

## Workflow: Configure Headset Serviceability

After you complete this workflow, you can configure headset settings, maintain headset latest firmware loads, headset association
                              to users, enable headset-based Extension Mobility, and maintain inventory.

Step 1

Activate Cisco Headset Service

Turn on Cisco Headset Service in Cisco Unified Serviceability.

Step 2

Prepare Your Headset COP Files

Make sure you install and upgrade the latest headset firmware using a COP file.

Step 3

Configure User Profiles for Headset Users

If you haven't yet configured User Profiles, use this procedure to set up profiles for your users. If all User Profiles are
                                          configured, you can skip this task.

Step 4

Apply User Profiles to End Users

Assign User Profiles to your end users. If you've already assigned User Profiles, you can skip this task.

Step 5

Configure a Headset Template

Configure default settings and firmware for a Cisco headset template. Associate User Profiles to the template such that users
                                          whom use that User Profile are assigned to this headset template.

Step 6

View Headset Inventory

Check that you can see your deployed headset inventory through the Cisco Unified CM interface.

### Activate Cisco Headset Service

Cisco Headset service should be activated on all the Unified Communications Manager nodes wherever Cisco CallManager service
                                             is already running. Ensure that you activate the Cisco Headset service on the Unified Communications Manager nodes where you
                                             want to administer headsets  using the Cisco Unified CM Administration interface. The Cisco CallManager service will be automatically
                                             activated when you enable the Cisco Headset service. Deactivate the Cisco CallManager service if you do not need it.

Step 1

From Cisco Unified CM Administration, navigate to Cisco Unified Serviceability and click Go .

Step 2

Select Tools > Service Activation .

Step 3

Check the Cisco Headset Service check box from the CM Services section and select Save .

#### What to do next

### Prepare Your Headset COP Files

You can install and upgrade the latest headset firmware using a COP file. A headset COP file contains all the firmware versions
                              of different headset  models along with their configuration data.

Ensure that the Cisco Headset service is up and running before the COP file is installed.

Ensure that the headset COP file is installed on all nodes of Unified Communications Manager.

Install or upgrade the COP file to the Unified Communications Manager system before you can start using your Cisco headsets
                                    .

When you connect your headset  to the endpoints, the headset  template configuration changes are applied. If you make any
                              updates to the headset  template configurations on Unified Communications Manager, the endpoints apply these configuration
                              updates on the connected headsets .

All configuration updates depend on the version of the headset  template in the COP file. If the headset  template version
                              is higher in the latest COP file, the configuration file on Unified Communications Manager is updated. If the configuration
                              file in the COP file is upgraded, the headset  template version in Unified Communications Manager is updated irrespective
                              of the version of the template and vice versa. The following list shows the various template version update scenarios after
                              a COP file upgrade:

If the Unified Communications Manager is currently installed with the headset  template version 1-10 and you upgrade your
                                    Unified Communications Manager server that has headset  template version 1-12, then the chosen headset  template version is
                                    1-12. Unified Communications Manager opts for the higher headset  template version.

If the Unified Communications Manager is currently installed with the headset  template version 1-10 and you upgrade your
                                    Unified Communications Manager server that has headset  template version 1-9, then the chosen headset  template version is
                                    1-10. Unified Communications Manager opts for the higher headset  template version.

If the Unified Communications Manager is currently installed with the headset  template version 1-10 and you install a COP
                                    file that has headset  template version 1-12, then the chosen headset  template version is 1-12. Headset  template installed
                                    with the COP files is the preferred option.

If the Unified Communications Manager is currently installed with the headset  template version 1-10 and you install a COP
                                    file that has headset  template version 1-9, then the chosen headset  template version is 1-9. Headset  template installed
                                    with the COP files is the preferred option.

If you had a COP file installed that has headset  template version 1-12 and you upgrade your Unified Communications Manager
                                    server having headset  template version 1-10, then the chosen headset  template version is 1-12. Unified Communications Manager
                                    opts for the higher headset  template version.

### Configure User Profiles for Headset Users

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > User Profile .

Step 2

Click Add New .

Step 3

Enter a Name and Description for the user profile.

Step 4

Assign a Universal Device Template to apply to users' Desk Phones , Mobile and Desktop Devices , and Remote Destination/Device Profiles .

Step 5

Assign a Universal Line Template to apply to the phone lines for users in this user profile.

Step 6

If you want the users in this user profile to be able to use the self-provisioning feature to provision their own phones,
                                          do the following:

Check the Allow End User to Provision their own phones check box.

In the Limit Provisioning once End User has this many phones field, enter a maximum number of phones the user is allowed to provision. The maximum is 20.

Step 7

If you want Cisco Jabber users associated with this user profile to be able to use the Mobile and Remote Access  feature,
                                          check the Enable Mobile and Remote Access check box.

Step 8

Assign the Jabber policies for this user profile. From the Jabber Desktop Client Policy , and Jabber Mobile Client Policy drop-down list, choose one of the following options:

- No Service—This policy disables access to all Cisco Jabber services.

- IM & Presence only—This policy enables only instant messaging and presence capabilities.

- IM & Presence, Voice and Video calls—This policy enables instant messaging, presence, voicemail, and conferencing capabilities
                                             for all users with audio or video devices. This is the default option.

Step 9

If you want the users in this user profile to set the maximum login time for Extension Mobility or Extension Mobility Cross
                                          Cluster through the Cisco Unified Communications Self Care Portal, check the Allow End User to set their Extension Mobility maximum login time check box.

Step 10

Click Save .

### Apply User Profiles to End Users

Step 1

To add a new end user to the Unified Communications Manager database manually, perform the following:

In Cisco Unified CM Administration, choose User Management > End User .

Click Add New .

Enter the User ID and Last name .

Choose the User Rank from the drop-down list.

Complete the fields in the End User Configuration window. For field descriptions, see the online help.

Click Save .

Step 2

To associate the end user with the device, perform the following:

In Cisco Unified CM Administration, choose Device > Phone .

Select the Cisco IP Phone or device.

Under Device Information, select User as the Owner and select the Owner User ID .

Click Save and Apply Config for the configuration changes to take effect.

## Headset Template Management

You can assign headset templates to user profiles in Cisco Unified Communications Manager to configure default headset settings
                              for your users. The headset template provides the option to associate User Profiles. Unified Communications Manager supports
                              the following types of headset templates:

### Standard Default Headset Configuration Template

This is the system default template that contains the factory default settings for all headset model series. This template
                              contains the headset settings supported by the latest headset firmware installed on your system for all your headset model
                              series. You cannot edit the default settings though you can change the profile configuration setting.

The Standard Default Headset Configuration template is created only when the Cisco Headset Service is activated in the Cisco Unified Serviceability user interface.

By default, all User Profiles are associated to the standard headset template unless the administrator associates these user
                              profiles to any of the custom defined headset templates. You can make copies of the standard default headset template to create
                              custom template with customized values of the parameters including the headset firmware version.

### System Generated Custom Headset Template

For some earlier releases that did not support the full Cisco Headset Serviceability feature, administrators could configure
                              and deploy headset templates manually via the defaultheadsetconfig.json configuration file and TFTP. If you used this method on a previous release, and then upgrade to this release, the config
                              file is converted to the System Generated Custom Headset Template and displays in the Headset Template Configuration window. Following the upgrade, users and devices that used the config file are associated to this custom template.

### Custom Headset Configuration Template

From Cisco Unified CM Administration, use the Device > Headset > Headset Template window to customize headset templates as per your deployment needs. You can assign different headset parameters to different
                              models in the same template. You can also assign different firmware loads to different headset models. The custom headset
                              settings can be assigned to specific sets of users by associating the User Profile(s) to the Custom Headset Template.

Field

Description

Headset Template Configuration

Name

Enter a unique name to identify the headset template.

Description

Enter a description that identifies use of the template.

Model and Firmware Settings

Choose Model Series

Choose any supported headset model that offers reliable, high-quality sound for your device.

Add

For a standard template, you can view the default pre-defined firmware versions and settings of the headset models. You cannot
                                          edit the default values.

For customized templates, click Add to add a new headset model and corresponding settings. You cannot add another existing headset model in the same template.
                                          You can add different headset models in a customized template; however, you can only use one firmware per headset model. For
                                          more information on headset parameters, see the "Headset Configuration Parameters" table below.

For Standard Default Headset Template Configuration, you can only edit settings by installing a headset COP file.

Firmware

Select the required firmware version.

Remain on current version—Choose this option if you want the headset to remain on the existing firmware version (that is,
                                                the headset firmware version is not upgraded to the latest firmware version on the system).

Latest—Choose this option if you want to upgrade the headset firmware version to the latest firmware version on the system.

Delete

For customized templates, click Delete to remove the headset model from the headset template.

Profile Configuration

Available User Profiles

Lists the configured User Profiles that are available to use with this headset template.

To associate a User Profile to this template, select the profile and click the down arrow to move the template to Assigned
                                          User Profiles.

By default, all User Profiles get assigned to the Standard Default Headset Configuration Template. To associate a User Profile
                                                      to a different template, create the new template and assign the User Profile to the new template.

Assigned User Profiles

Lists the User Profiles that will use this headset configuration template. For users assigned to this profile, the settings
                                          in this headset configuration template are applied to their Cisco headsets during registration.

Click the arrows to add new User Profiles from the Available User Profiles list.

The following table describes the parameters in each headset template.

Parameter

Range

Default

Notes

Speaker Volume

0 – 15

7

Controls the level of sound in the headset. 0 is very low while 15 is loud.

Configure this setting based on the ambient noise in the office environment.

Microphone Gain

Softer – Louder

Default

Gain controls how loud the user sounds to other people on the call. Softer means users sound quiet while Louder means users sound much louder.

Configure this setting based on the ambient noise in the office environment.

Sidetone

Off – High

Low

Controls how much of a user's own voice they can hear through their headset. Off turns off the sidetone while High means that users receive much more feedback from their headset microphones.

Equalizer

Warmest – Brightest

Default

Controls the Equalizer settings. Warmer settings mean users hear more bass in their headsets, while a brighter setting means
                                          users hear more treble.

Audio Bandwidth

Wide Band, Narrow Band

Wide Band

Controls the Digital Enhanced cordless Telecommunications (DECT) codec in the Cisco Headset 560 Series .

In a dense DECT environment, set the field to Narrow Band to limit the Cisco Headset 560 Series to the G.727 codec.

Bluetooth

On, Off

On

Controls the use of Bluetooth on the Cisco Headset 560 Series with Multibase . When this parameter is set to Off , the base deletes all devices paired with it.

Conference

On, Off

On

Controls the use of the conferencing feature on the Cisco Headset 560 Series . Conferencing allows up to three guest headsets to pair with the same base at once.

See Cisco Headset 500 Series User Guide for more information on conferencing.

Firmware Source

Allow from UCM or Cisco Cloud (firmware will upgrade only), Restrict to UCM only (firmware may upgrade or downgrade)

Allow from UCM or Cisco Cloud

Controls the headset's firmware upgrade source.

By default, users can upgrade their headset through a devices and software connected to Unified CM or through a cloud-connected
                                          device or software. You can restrict your headsets to only accept firmware changes through a Unified CM source.

DECT Radio Range

Autorange, Medium Range, Short Range

Medium Range

Controls the maximum distance between the Cisco Headset 560 Series and its base.

By default, the bases have a DECT range of over 330 feet (100 meters) in ideal conditions. If you configure the DECT radio
                                          range to Medium Range or Short Range , the headset base consumes less power but users can't move as far from the base while on a call. Configure DECT radio range
                                          to Short Range for high density headset deployment.

For more detailed information on DECT deployment, refer to the white paper on Cisco Headset deployment, How to Deploy DECT at Work for the Cisco Headset 560 Series .

Headset dock behavior

On, Off

On

Controls how the Cisco Headset 560 Series behaves if you lift the headset off the base when you have an incoming call.

### Configure a Headset Template

The Standard Default Headset Configuration Template is a system-defined template. You can assign new User Profiles to the
                                             Standard Default Headset Template but you can't edit the template. By default, all user profiles are assigned to this template.
                                             To disassociate a user profile from this template, you must assign the profile to a new template.

Step 1

From Cisco Unified CM Administration, choose Device > Headset > Headset Template .

Step 2

Do either of the following:

- To edit an existing template, select the template.

- To create a new template, select any existing template and click Copy . The existing settings are applied to your new template.

Step 3

Add a Name and Description for the template.

Step 4

Under Model and Firmware Settings , assign any customized headset settings that you want to apply to this template. To add a new setting, click the Add button and configure the settings.

Step 5

Use the up and down arrows to move the User Profiles that you want to assign to this template to the Assigned Users Profiles list box. All users whom are assigned to those profiles will also be assigned to this headset template.

Step 6

Click Save .

Step 7

Use the Set to Default button to return to the default template settings.

Step 8

Click Apply Config .

For a Standard Default Headset Configuration Template, the Apply Config button takes effect for the following:

Devices owned by users you added to the Assigned User Profile list

Anonymous devices

For a Customized Headset Configuration Template, the Apply Config button takes effect only for devices owned by users you added to the Assigned User Profiles list.

## Firmware Management

Most phones and devices connected to the Unified Communications Manager support the Cisco Headset 500 Series and Cisco Headset
                           700 Series. Install the latest phone firmware release and device package before connecting your headset to a phone. When the
                           headset first connects, it downloads the required firmware and begins the upgrade process.

For a given headset model, the following two firmware options are supported:

Remain on current version —Choose this option if you want the headset to remain on the existing firmware version (that is, the headset firmware version
                                 is not upgraded to the latest system firmware version).

Latest —Choose this option to upgrade or downgrade the headset. The system installs and runs the chosen software, even if that firmware
                                 is an older release from what the headset currently has.

For example, if you choose 1-5-1-10 as the latest, that firmware will be installed on the headset regardless of whether the headset currently has 1-5-1-9 or 1-5-1-11 .

### Firmware Considerations

Users assigned to the standard headset template will always receive the latest headset firmware and settings.

Settings shown in the Headset Template Configuration (both Standard and Custom) are always set to the Latest firmware for all headset model series.

## Headset Inventory Management

Cisco IP Phones send headset inventory data to Unified Communications Manager whenever the headset is in a connected or disconnected
                              state. Unified Communications Manager stores the inventory data so you can generate an Inventory Summary Report or Custom
                              Inventory Report for all headsets deployed in this server.

Report information includes: headset serial and model number, docking station details, firmware, configuration templates used,
                              vendor details, and headset connection status to devices.

### Headset Inventory Settings

From Cisco Unified CM Administration, use the Device > Headset > Headset Inventory window to view a full list of all headsets deployed on your server. You can use this information to generate reports for
                                 all deployed headsets. If you click the Serial Number of the device, you can view details of individual headsets in a pop-up
                                 window.

Field

Description

Serial Number

Serial Number of the headset. This number is unique for every individual headset.

The Cisco Headset 520 and 530 Series report the serial number found on the USB controller. The Cisco Headset 560 and 700 Series
                                             report the headset serial number found on inside of the left armband.

Model

Model number of the headset.

Vendor

Displays vendor details.

Type

Indicates the type of headset connection: Wired, DECT Wireless, or Unknown.

Firmware

Displays the most current firmware load of the headset.

User

Displays information of the end user using the phone or device.

Template

Display the name of the headset configuration template.

Status (since)

Displays the status of the headset activities. It can be: Connected or Disconnected.

Dock Model

Displays the type of docking model station.

Device Name

Name of the device to which the headset is connected to.

Device Model

Displays the Cisco IP Phone or Cisco Jabber model number. For example, CP-8865 is a Cisco IP Phone model. CSF is a device
                                             type for either Cisco Jabber for Mac or Cisco Jabber for Windows.

Software Version

Displays the latest version of the software used. It can be a phone firmware or a Jabber software version.

Headset Age (days)

Displays the age of the headset. If the record is deleted, the headset age is reset.

### View Headset Inventory

Step 1

From Cisco Unified CM Administration, choose Device > Headset > Headset Inventory .

Step 2

Do either of the following:

- Select Find to see a full list of headsets deployed on your server.

- Enter a one or more search criteria into the search box and select Find .

### Headset Inventory Summary

#### Headset Inventory by Model

From Cisco Unified CM Administration, you can use the Device > Headset > Headset Inventory Summary window to view an aggregate summary of your deployed headsets in the Headset Inventory Summary window.

Field

Description

Headset Model

The headset model number.

Quantity

Lists the number of headsets for each model type in your deployment.

Click the link in the Quantity column to navigate to the detailed Headset Inventory page, filtered by model type.

#### Headset Inventory by Status

Click the hyperlinks in the Headset Model , Active , Inactive , or Unassigned columns to navigate to the detailed Headset Inventory page for each status.

Field

Description

Headset Model

The headset model number.

Active

The headset has connected within the last 30 days.

Inactive

The headset hasn't connected in the last 30 days.

Unassigned

The user ID doesn't exist in the system or the inventory record doesn't have a user ID mapping.

### Get an Aggregate Summary of Your Deployed Headsets

In Cisco Unified CM Administration, select Device > Headset > Headset Inventory Summary .

You can view a breakdown of headset inventory by model or by headset status.

## Headset Troubleshooting and Diagnostics

You can configure Unified Communications Manager or Cisco Unified Real-Time Monitoring Tool (RTMT) to collect Problem Report
                           Tool (PRT) logs for headsets connected to Cisco IP Phones. The PRT includes data on call quality, codecs used, audio settings,
                           wireless settings, and alert logs.

Unified Communications Manager stores the call diagnostics details for Headsets. Cisco IP Phones send headset diagnostics
                           data in Headset-Stat header either in a BYE message or a 200 OK response to BYE message to update the CMRs in Unified Communications
                           Manager.

Cisco IP Phones share the headset diagnostics data with Unified Communications Manager and this information is stored in the
                           following fields in the CMR record:

SN—Serial number of the headset.

Metrics—Headset metrics such as RSSI frame errors, connection drop reason, beacon moves, audio settings, and DECT bandwidth.

For detailed information on how to export and view CMR records, see the Call Reporting and Billing Administration Guide for Cisco Unified Communications Manager .

### Generate PRT for Endpoints on Unified CM

Use this procedure to trigger the Problem Reporting Tool (PRT) on the endpoints.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select one or more phones that the headset connects to.

Step 3

Click Generate PRT for Selected to collect PRT logs for the headsets used by the selected phones.

Step 4

Click Save .

Cisco Unified Communications Manager sends SIP Notify messages to remotely trigger the log collection on the phone and upload
                                             it to the log server configured in the “Customer support upload URL” parameter.

### Generate PRT for Endpoints on RTMT

Step 1

Open the Trace and Log Central options.

Step 2

In the Trace & Log Central tree hierarchy, choose Generate PRT .

Step 3

Enter the Device name as configured in the Find and List Phones page in the Cisco Unified CM Administration user interface.

Step 4

Click Generate PRT .

The generated report is uploaded at the Customer support upload URL . The download option is available only if the Customer support upload URL parameter is configured at the Enterprise, Profile, or Device level in the Cisco Unified CM Administration user interface.

Check the Customer support upload URL parameter in the Enterprise, Profile, or Device level configuration page settings. Else, PRT generation fails.

| Note | The Cisco Headset Management feature is not supported in 12.0(x) or 12.5(1). For earlier versions, you may have a limited
                                       support for sending headset configuration templates for IP phones manually via the defaultheadsetconfig.json configuration file and TFTP. Refer to your headset Administration Guide for details. |
|---|---|

| New Serviceability Feature | Unified CM 12.5(1) or earlier + Phone Firmware 12.1(1) or earlier | Unified CM 12.5(1)SU1 and above** + Phone Firmware 12.1(1) or earlier | Unified CM 12.5(1) or earlier + Phone Firmware 12.5(1) | Unified CM 12.5(1)SU1 and above** + Phone Firmware 12.5(1) | Unified CM 12.5(1) or earlier + Phone Firmware 12.5(1)SR3 | Unified CM 12.5(1)SU1 and above** + Phone Firmware 12.5(1)SR3 |
|---|---|---|---|---|---|---|
| COP file installation required | X | X | X | X | X | — |
| Manual remote configuration | — | — | X | N/A | X | — |
| Headset firmware management on Unified CM | — | — | — | — | — | X |
| Remote headset configuration through Unified CM | — | — | — | — | — | X |
| Headset inventory on Unified CM | — | — | — | — | — | X* |
| Configuration Reset on the phone UI | — | — | — | — | X | X |
| Headset Call Management Records (CMR) | — | — | — | — | — | X* |

| New Serviceability Feature | Unified CM 12.5(1) or earlier + Jabber version 12.5(1) or earlier | Unified CM 12.5(1)SU1 and above** + Jabber version 12.5(1) or earlier | Unified CM 12.5(1) or earlier + Jabber version 12.6(1) | Unified CM 12.5(1)SU1 and above** + Jabber version 12.6(1) | Unified CM 12.5(1) or earlier + Jabber version 12.6(1)MR | Unified CM 12.5(1)SU1 and above** + Jabber version 12.6(1)MR |
|---|---|---|---|---|---|---|
| COP file installation required | X | X | X | X | X | X |
| Headset firmware management through Unified CM | — | — | — | — | — | X |
| Remote headset configuration through Unified CM | — | — | — | X | — | X |
| Headset inventory on Unified CM | — | — | — | X* | — | X* |
| Local configuration reset | — | — | — | — | X | X |
| Local UI configuration | — | — | X | X | X | X |
| Local headset version display | — | — | — | — | X | X |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate Cisco Headset Service | Turn on Cisco Headset Service in Cisco Unified Serviceability. |
| Step 2 | Prepare Your Headset COP Files | Make sure you install and upgrade the latest headset firmware using a COP file. |
| Step 3 | Configure User Profiles for Headset Users | If you haven't yet configured User Profiles, use this procedure to set up profiles for your users. If all User Profiles are
                                          configured, you can skip this task. |
| Step 4 | Apply User Profiles to End Users | Assign User Profiles to your end users. If you've already assigned User Profiles, you can skip this task. |
| Step 5 | Configure a Headset Template | Configure default settings and firmware for a Cisco headset template. Associate User Profiles to the template such that users
                                          whom use that User Profile are assigned to this headset template. |
| Step 6 | View Headset Inventory | Check that you can see your deployed headset inventory through the Cisco Unified CM interface. |

| Note | Cisco Headset service should be activated on all the Unified Communications Manager nodes wherever Cisco CallManager service
                                             is already running. Ensure that you activate the Cisco Headset service on the Unified Communications Manager nodes where you
                                             want to administer headsets  using the Cisco Unified CM Administration interface. The Cisco CallManager service will be automatically
                                             activated when you enable the Cisco Headset service. Deactivate the Cisco CallManager service if you do not need it. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, navigate to Cisco Unified Serviceability and click Go . |
|---|---|
| Step 2 | Select Tools > Service Activation . |
| Step 3 | Check the Cisco Headset Service check box from the CM Services section and select Save . |

| Note | Ensure that the Cisco Headset service is up and running before the COP file is installed. Ensure that the headset COP file is installed on all nodes of Unified Communications Manager. |
|---|---|

| Note | Configure multiple User Profiles for different groups of users as per your deployment needs. By default, all User Profiles
                                          get assigned to the System default headset template. You can assign them to customized templates when you configure your headset
                                          template. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > User Profile . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter a Name and Description for the user profile. |
| Step 4 | Assign a Universal Device Template to apply to users' Desk Phones , Mobile and Desktop Devices , and Remote Destination/Device Profiles . |
| Step 5 | Assign a Universal Line Template to apply to the phone lines for users in this user profile. |
| Step 6 | If you want the users in this user profile to be able to use the self-provisioning feature to provision their own phones,
                                          do the following: Check the Allow End User to Provision their own phones check box. In the Limit Provisioning once End User has this many phones field, enter a maximum number of phones the user is allowed to provision. The maximum is 20. |
| Step 7 | If you want Cisco Jabber users associated with this user profile to be able to use the Mobile and Remote Access  feature,
                                          check the Enable Mobile and Remote Access check box. Note By default, this check box is selected. When you uncheck this check box, the Jabber Policies section is disabled and No Service client policy option is selected by default. Note This setting is mandatory only for Cisco Jabber users. Non-Jabber users do not need this setting to be able to use Mobile
                                                      and Remote Access. The Mobile and Remote Access feature is applicable only for Jabber Mobile and Remote Access users and not
                                                      to any other endpoints or clients. | Note | By default, this check box is selected. When you uncheck this check box, the Jabber Policies section is disabled and No Service client policy option is selected by default. | Note | This setting is mandatory only for Cisco Jabber users. Non-Jabber users do not need this setting to be able to use Mobile
                                                      and Remote Access. The Mobile and Remote Access feature is applicable only for Jabber Mobile and Remote Access users and not
                                                      to any other endpoints or clients. |
| Note | By default, this check box is selected. When you uncheck this check box, the Jabber Policies section is disabled and No Service client policy option is selected by default. |
| Note | This setting is mandatory only for Cisco Jabber users. Non-Jabber users do not need this setting to be able to use Mobile
                                                      and Remote Access. The Mobile and Remote Access feature is applicable only for Jabber Mobile and Remote Access users and not
                                                      to any other endpoints or clients. |
| Step 8 | Assign the Jabber policies for this user profile. From the Jabber Desktop Client Policy , and Jabber Mobile Client Policy drop-down list, choose one of the following options: No Service—This policy disables access to all Cisco Jabber services. IM & Presence only—This policy enables only instant messaging and presence capabilities. IM & Presence, Voice and Video calls—This policy enables instant messaging, presence, voicemail, and conferencing capabilities
                                             for all users with audio or video devices. This is the default option. Note Jabber desktop client includes Cisco Jabber for Windows users and Cisco Jabber for Mac users. Jabber mobile client includes
                                                      Cisco Jabber for iPad and iPhone users and Cisco Jabber for Android users. | Note | Jabber desktop client includes Cisco Jabber for Windows users and Cisco Jabber for Mac users. Jabber mobile client includes
                                                      Cisco Jabber for iPad and iPhone users and Cisco Jabber for Android users. |
| Note | Jabber desktop client includes Cisco Jabber for Windows users and Cisco Jabber for Mac users. Jabber mobile client includes
                                                      Cisco Jabber for iPad and iPhone users and Cisco Jabber for Android users. |
| Step 9 | If you want the users in this user profile to set the maximum login time for Extension Mobility or Extension Mobility Cross
                                          Cluster through the Cisco Unified Communications Self Care Portal, check the Allow End User to set their Extension Mobility maximum login time check box. Note By default Allow End User to set their Extension Mobility maximum login time check box is unchecked. | Note | By default Allow End User to set their Extension Mobility maximum login time check box is unchecked. |
| Note | By default Allow End User to set their Extension Mobility maximum login time check box is unchecked. |
| Step 10 | Click Save . |

| Note | By default, this check box is selected. When you uncheck this check box, the Jabber Policies section is disabled and No Service client policy option is selected by default. |
|---|---|

| Note | This setting is mandatory only for Cisco Jabber users. Non-Jabber users do not need this setting to be able to use Mobile
                                                      and Remote Access. The Mobile and Remote Access feature is applicable only for Jabber Mobile and Remote Access users and not
                                                      to any other endpoints or clients. |
|---|---|

| Note | Jabber desktop client includes Cisco Jabber for Windows users and Cisco Jabber for Mac users. Jabber mobile client includes
                                                      Cisco Jabber for iPad and iPhone users and Cisco Jabber for Android users. |
|---|---|

| Note | By default Allow End User to set their Extension Mobility maximum login time check box is unchecked. |
|---|---|

| Note | If you've already assigned all users to the appropriate User Profiles, you can skip this task. |
|---|---|

| Step 1 | To add a new end user to the Unified Communications Manager database manually, perform the following: In Cisco Unified CM Administration, choose User Management > End User . Click Add New . Enter the User ID and Last name . Choose the User Rank from the drop-down list. Complete the fields in the End User Configuration window. For field descriptions, see the online help. Click Save . |
|---|---|
| Step 2 | To associate the end user with the device, perform the following: In Cisco Unified CM Administration, choose Device > Phone . Select the Cisco IP Phone or device. Under Device Information, select User as the Owner and select the Owner User ID . Click Save and Apply Config for the configuration changes to take effect. |

| Note | The Standard Default Headset Configuration template is created only when the Cisco Headset Service is activated in the Cisco Unified Serviceability user interface. |
|---|---|

| Field | Description |
|---|---|
| Headset Template Configuration |
| Name | Enter a unique name to identify the headset template. |
| Description | Enter a description that identifies use of the template. |
| Model and Firmware Settings |
| Choose Model Series | Choose any supported headset model that offers reliable, high-quality sound for your device. |
| Add | For a standard template, you can view the default pre-defined firmware versions and settings of the headset models. You cannot
                                          edit the default values. For customized templates, click Add to add a new headset model and corresponding settings. You cannot add another existing headset model in the same template.
                                          You can add different headset models in a customized template; however, you can only use one firmware per headset model. For
                                          more information on headset parameters, see the "Headset Configuration Parameters" table below. For Standard Default Headset Template Configuration, you can only edit settings by installing a headset COP file. |
| Firmware | Select the required firmware version. Remain on current version—Choose this option if you want the headset to remain on the existing firmware version (that is,
                                                the headset firmware version is not upgraded to the latest firmware version on the system). Latest—Choose this option if you want to upgrade the headset firmware version to the latest firmware version on the system. |
| Delete | For customized templates, click Delete to remove the headset model from the headset template. |
| Profile Configuration |
| Available User Profiles | Lists the configured User Profiles that are available to use with this headset template. To associate a User Profile to this template, select the profile and click the down arrow to move the template to Assigned
                                          User Profiles. Note By default, all User Profiles get assigned to the Standard Default Headset Configuration Template. To associate a User Profile
                                                      to a different template, create the new template and assign the User Profile to the new template. | Note | By default, all User Profiles get assigned to the Standard Default Headset Configuration Template. To associate a User Profile
                                                      to a different template, create the new template and assign the User Profile to the new template. |
| Note | By default, all User Profiles get assigned to the Standard Default Headset Configuration Template. To associate a User Profile
                                                      to a different template, create the new template and assign the User Profile to the new template. |
| Assigned User Profiles | Lists the User Profiles that will use this headset configuration template. For users assigned to this profile, the settings
                                          in this headset configuration template are applied to their Cisco headsets during registration. Click the arrows to add new User Profiles from the Available User Profiles list. |

| Note | By default, all User Profiles get assigned to the Standard Default Headset Configuration Template. To associate a User Profile
                                                      to a different template, create the new template and assign the User Profile to the new template. |
|---|---|

| Note | On-premises and multiplatform headset serviceability features are unavailable through an RJ-9 connection. |
|---|---|

| Parameter | Range | Default | Notes |
|---|---|---|---|
| Speaker Volume | 0 – 15 | 7 | Controls the level of sound in the headset. 0 is very low while 15 is loud. Configure this setting based on the ambient noise in the office environment. |
| Microphone Gain | Softer – Louder | Default | Gain controls how loud the user sounds to other people on the call. Softer means users sound quiet while Louder means users sound much louder. Configure this setting based on the ambient noise in the office environment. |
| Sidetone | Off – High | Low | Controls how much of a user's own voice they can hear through their headset. Off turns off the sidetone while High means that users receive much more feedback from their headset microphones. |
| Equalizer | Warmest – Brightest | Default | Controls the Equalizer settings. Warmer settings mean users hear more bass in their headsets, while a brighter setting means
                                          users hear more treble. |
| Audio Bandwidth | Wide Band, Narrow Band | Wide Band | Controls the Digital Enhanced cordless Telecommunications (DECT) codec in the Cisco Headset 560 Series . In a dense DECT environment, set the field to Narrow Band to limit the Cisco Headset 560 Series to the G.727 codec. |
| Bluetooth | On, Off | On | Controls the use of Bluetooth on the Cisco Headset 560 Series with Multibase . When this parameter is set to Off , the base deletes all devices paired with it. |
| Conference | On, Off | On | Controls the use of the conferencing feature on the Cisco Headset 560 Series . Conferencing allows up to three guest headsets to pair with the same base at once. See Cisco Headset 500 Series User Guide for more information on conferencing. |
| Firmware Source | Allow from UCM or Cisco Cloud (firmware will upgrade only), Restrict to UCM only (firmware may upgrade or downgrade) | Allow from UCM or Cisco Cloud | Controls the headset's firmware upgrade source. By default, users can upgrade their headset through a devices and software connected to Unified CM or through a cloud-connected
                                          device or software. You can restrict your headsets to only accept firmware changes through a Unified CM source. |
| DECT Radio Range | Autorange, Medium Range, Short Range | Medium Range | Controls the maximum distance between the Cisco Headset 560 Series and its base. By default, the bases have a DECT range of over 330 feet (100 meters) in ideal conditions. If you configure the DECT radio
                                          range to Medium Range or Short Range , the headset base consumes less power but users can't move as far from the base while on a call. Configure DECT radio range
                                          to Short Range for high density headset deployment. For more detailed information on DECT deployment, refer to the white paper on Cisco Headset deployment, How to Deploy DECT at Work for the Cisco Headset 560 Series . |
| Headset dock behavior | On, Off | On | Controls how the Cisco Headset 560 Series behaves if you lift the headset off the base when you have an incoming call. |

| Note | The Standard Default Headset Configuration Template is a system-defined template. You can assign new User Profiles to the
                                             Standard Default Headset Template but you can't edit the template. By default, all user profiles are assigned to this template.
                                             To disassociate a user profile from this template, you must assign the profile to a new template. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Headset > Headset Template . |
|---|---|
| Step 2 | Do either of the following: To edit an existing template, select the template. To create a new template, select any existing template and click Copy . The existing settings are applied to your new template. |
| Step 3 | Add a Name and Description for the template. |
| Step 4 | Under Model and Firmware Settings , assign any customized headset settings that you want to apply to this template. To add a new setting, click the Add button and configure the settings. |
| Step 5 | Use the up and down arrows to move the User Profiles that you want to assign to this template to the Assigned Users Profiles list box. All users whom are assigned to those profiles will also be assigned to this headset template. |
| Step 6 | Click Save . |
| Step 7 | Use the Set to Default button to return to the default template settings. |
| Step 8 | Click Apply Config . For a Standard Default Headset Configuration Template, the Apply Config button takes effect for the following: Devices owned by users you added to the Assigned User Profile list Anonymous devices For a Customized Headset Configuration Template, the Apply Config button takes effect only for devices owned by users you added to the Assigned User Profiles list. |

| Field | Description |
|---|---|
| Serial Number | Serial Number of the headset. This number is unique for every individual headset. The Cisco Headset 520 and 530 Series report the serial number found on the USB controller. The Cisco Headset 560 and 700 Series
                                             report the headset serial number found on inside of the left armband. Note For non-Cisco headsets, the Device Name is used as the Serial Number. Using the same non-Cisco headset with multiple phones
                                                      creates duplicate headset records. | Note | For non-Cisco headsets, the Device Name is used as the Serial Number. Using the same non-Cisco headset with multiple phones
                                                      creates duplicate headset records. |
| Note | For non-Cisco headsets, the Device Name is used as the Serial Number. Using the same non-Cisco headset with multiple phones
                                                      creates duplicate headset records. |
| Model | Model number of the headset. |
| Vendor | Displays vendor details. |
| Type | Indicates the type of headset connection: Wired, DECT Wireless, or Unknown. |
| Firmware | Displays the most current firmware load of the headset. |
| User | Displays information of the end user using the phone or device. |
| Template | Display the name of the headset configuration template. |
| Status (since) | Displays the status of the headset activities. It can be: Connected or Disconnected. |
| Dock Model | Displays the type of docking model station. |
| Device Name | Name of the device to which the headset is connected to. |
| Device Model | Displays the Cisco IP Phone or Cisco Jabber model number. For example, CP-8865 is a Cisco IP Phone model. CSF is a device
                                             type for either Cisco Jabber for Mac or Cisco Jabber for Windows. |
| Software Version | Displays the latest version of the software used. It can be a phone firmware or a Jabber software version. |
| Headset Age (days) | Displays the age of the headset. If the record is deleted, the headset age is reset. |

| Note | For non-Cisco headsets, the Device Name is used as the Serial Number. Using the same non-Cisco headset with multiple phones
                                                      creates duplicate headset records. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Headset > Headset Inventory . |
|---|---|
| Step 2 | Do either of the following: Select Find to see a full list of headsets deployed on your server. Enter a one or more search criteria into the search box and select Find . |

| Field | Description |
|---|---|
| Headset Model | The headset model number. |
| Quantity | Lists the number of headsets for each model type in your deployment. Note Click the link in the Quantity column to navigate to the detailed Headset Inventory page, filtered by model type. | Note | Click the link in the Quantity column to navigate to the detailed Headset Inventory page, filtered by model type. |
| Note | Click the link in the Quantity column to navigate to the detailed Headset Inventory page, filtered by model type. |

| Note | Click the link in the Quantity column to navigate to the detailed Headset Inventory page, filtered by model type. |
|---|---|

| Field | Description |
|---|---|
| Headset Model | The headset model number. |
| Active | The headset has connected within the last 30 days. |
| Inactive | The headset hasn't connected in the last 30 days. |
| Unassigned | The user ID doesn't exist in the system or the inventory record doesn't have a user ID mapping. |

| In Cisco Unified CM Administration, select Device > Headset > Headset Inventory Summary . You can view a breakdown of headset inventory by model or by headset status. |
|---|

| Note | Headset CMR records apply to Cisco Headset 500 series, but not to 700 series. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select one or more phones that the headset connects to. |
| Step 3 | Click Generate PRT for Selected to collect PRT logs for the headsets used by the selected phones. |
| Step 4 | Click Save . Cisco Unified Communications Manager sends SIP Notify messages to remotely trigger the log collection on the phone and upload
                                             it to the log server configured in the “Customer support upload URL” parameter. |

| Step 1 | Open the Trace and Log Central options. |
|---|---|
| Step 2 | In the Trace & Log Central tree hierarchy, choose Generate PRT . The Generate PRT wizard appears. |
| Step 3 | Enter the Device name as configured in the Find and List Phones page in the Cisco Unified CM Administration user interface. |
| Step 4 | Click Generate PRT . The generated report is uploaded at the Customer support upload URL . The download option is available only if the Customer support upload URL parameter is configured at the Enterprise, Profile, or Device level in the Cisco Unified CM Administration user interface. Note Check the Customer support upload URL parameter in the Enterprise, Profile, or Device level configuration page settings. Else, PRT generation fails. | Note | Check the Customer support upload URL parameter in the Enterprise, Profile, or Device level configuration page settings. Else, PRT generation fails. |
| Note | Check the Customer support upload URL parameter in the Enterprise, Profile, or Device level configuration page settings. Else, PRT generation fails. |

| Note | Check the Customer support upload URL parameter in the Enterprise, Profile, or Device level configuration page settings. Else, PRT generation fails. |
|---|---|