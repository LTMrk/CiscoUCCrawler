---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-systemconfig-cucm-b-system-configuration-guide-1251su4--6325c8edc6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/systemConfig/cucm_b_system-configuration-guide-1251su4/cucm_m_device-onboarding-via-activation-codes.html
retrieved_at: 2026-08-16T17:40:19.837736+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4 to 12.5(1)SU7

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4 to 12.5(1)SU7

Updated: July 31, 2025

Chapter: Device Onboarding via Activation Codes

## Chapter: Device Onboarding via Activation Codes

# Device Onboarding via Activation Codes

## Activation Codes Overview

Activation codes make onboarding newly provisioned phones easy. An activation code is a single-use, 16-digit value that a
                              user must enter on a phone while registering the phone. Activation codes provide a simple method for provisioning and onboarding
                              phones without requiring an administrator to collect and input the MAC Address for each phone manually. This method is a simple
                              alternative to autoregistration that you can use this method to provision a large number of phones, a single phone, or even
                              to re-register existing phones.

You can also use Mobile and Remote Access-compliant devices to easily and securely register over Mobile and Remote Access
                              using an activation code.

Activation Code Device Onboarding works in the following modes:

On premise

Mobile Remote Access (MRA)

Activation codes provide the following benefits:

Onboarding using activation codes ensures that all newly provisioned phones or untrusted phones have their Manufacturing Installed
                                    Certificate (MIC) assessed and verified by Unified Communications Manager .

Cisco Manufacturing Root certificates must be present in the CallManager-trust store to perform onboarding activity.

No need to manually enter actual MAC addresses. Administrators can use dummy MAC addresses and the phone updates the configuration
                                    automatically with the real MAC address during registration.

No need to deploy an IVR, such as TAPS, to convert phone names from BAT to SEP.

Phone users can obtain their activation codes via the Self-Care Portal, provided the Show Phones Ready to Activate enterprise parameter is set to True . Otherwise, administrators must provide the codes to phone users.

When you provision with BAT MAC addresses, activation codes are tied to the phone model. BAT MAC is a reference to the device name that starts with 'BAT' and is followed by a random 12 hexidecimal digits that look
                                             like a MAC address. When saving a device configuration page with a blank MAC Address field, a random name with this format
                                             is created for you. You must enter an activation code that matches the phone model in order to activate the phone.

For added security, you can provision the phone with the actual MAC address of the phone. This option involves more configuration
                                          because the administrator must gather and input each phone's MAC address during provisioning, but provides greater security
                                          because users must enter the activation code that matches the actual MAC address on their phone.

### Onboarding Process Flow in On-Premise Mode

Following is the process flow for onboarding new phones via activation codes :

Administrator sets the configuration to require the user to enter an activation code for onboarding.

Administrator provisions and configures the phone. If BAT MAC addresses are being used, the administrator does not enter the actual MAC address.

Phone gets an IP address for TFTP via a DHCP opt 150, or from an alternate TFTP as configured in Phone settings. The phone
                                       downloads the XMLDefault file, and detects that an activation code is in use.

The user enters the activation code on the phone.

The Phone authenticates to Cisco Unified Communications Manager via the activation code and manufacturer-installed certificate.

The Phone requires the TVS service when the activation code is used for onboarding phones. The ITL file provides this TVS
                                       function which contains the certificate of the TVS service that runs on the Unified CM server TCP port 2445.

Cisco Unified Communications Manager updates the device configuration with the actual MAC address. The TFTP server sense the
                                       device configuration to the phone, allowing the phone to register. Note that device registration can be up to five minutes.

It's recommended to add an additional subscriber to the default communication manager group for on-premise activation code
                                                   onboarding. Else, when the node in the default communication manager group goes down, you may face onboarding issues.

### Onboarding Process Flow in Mobile and Remote Access Mode

Following is the process flow for onboarding new phones via activation codes when you use the Mobile and Remote Access mode:

Administrator configures Cloud/Hybrid communication to Enable Activation Code Onboarding with Cisco Cloud and specifies the
                                       Mobile and Remote Access Activation Domain.

Administrator configures additional Mobile and Remote Access Service Domains, if required.

Administrator creates a full-device configuration without specifying MAC address (BAT, AXL, GUI). The device name will be
                                       a random BAT MAC address.

Administrator requests activation code for this device. Device Activation Service requests the code from the cloud-based device
                                       activation service.

The user can get the code from the self-care portal or the administrator can send it to the user.

The user powers up the phone and enters the activation code.

Phone learns from the cloud the location of Expressway and authenticates to Mobile and Remote Access/Cisco Unified Communications
                                       Manager.

Device activation service updates device configuration in the database with the phone's MAC address.

The phone can now register and get its phone-specific configuration file from TFTP like normal Mobile and Remote Access, and
                                       register with Cisco Unified Communications Manager.

To provide secure solution for work from home remote users, Expressway's Mobile and Remote Access is the recommended solution
                                             and not TRP.

## Activation Code Prerequisites

As of Release 12.5(1), the following Cisco IP Phone models support onboarding via activation codes: 7811, 7821, 7832, 7841,
                              7861, 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR.

Additionally, Release 12.5(1)SU1 supports the following Cisco IP Phone models: 8832 and 8832NR

### Self Care Portal

If you plan to have your users use the Self Care Portal to onboard their phones, you need to set the portal up beforehand
                              so that your users will have access. For details, go to "Self Care Portal" chapter of the Feature Configuration Guide for Cisco Unified Communications Manager .

## Device Onboarding with Activation Codes Task Flow in On-Premise Mode

Step 1

Activate the Device Activation Service

The Cisco Device Activation Service must be running in Cisco Unified Serviceability.

Step 2

Set Registration Method to use Activation Codes

Under Device Defaults, set the default registration method to use Activation Codes for supported phone models.

Step 3

Provision phones with activation code requirement. Following are two provisioning example options:

- Add Phone with Activation Code Requirement

- Add Phones with Activation Codes via Bulk Administration

Cisco Unified Communications Manager has a variety of provisioning methods, including the options on the left. Whichever method
                                          you choose, make sure the Requires Activation Code for Onboarding check box is checked within that phone's Phone Configuration .

Step 4

Activate Phones

Distribute activation codes to users. Users must enter the code on the phone in order to use the phone.

### Activate the Device Activation Service

Step 1

From Cisco Unified Serviceability, choose Tools > Service Activation .

Step 2

From the Server drop-down, choose the Unified Communications Manager publisher node and click Go .

Step 3

Under CM Services , confirm that the Status of the Cisco Device Activation Service says Activated .

Step 4

If the service is not running, check the adjacent check box and click Save .

#### What to do next

### Set Registration Method to use Activation Codes

Use this procedure to configure the system defaults so that phones of a specific model type will use activation codes to register
                                 with Unified Communications Manager .

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Device Defaults .

Step 2

In the Device Defaults Configuration window, select the device type that will use activation codes for registration in the Dual Bank Information section, and change On-Premise Onboarding Method from Auto Registration to Activation Code .

Step 3

Click Save .

When device default is set to Activation Code, and if Auto Registration is earlier used for phone types, subsequent addition
                                                         of new phones should follow Activation Code Onboarding or Manual Configuration of Phone (Using MAC address) and Registration.

For more information, see Add Phone with Activation Code Requirement and Add Phones with Activation Codes via Bulk Administration section to provision new phones.

### Add Phone with Activation Code Requirement

#### Before you begin

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Add New From Template to add settings from a universal line or device template.

Step 3

From the Phone Type drop-down menu, select the phone model.

Step 4

In the MAC Address field, enter a MAC address. With activation codes, you can use a dummy MAC address or the phone's actual MAC address.

You can modify the MAC address of a phone in the following scenarios:

BAT{mac}->SEP{mac} : You should know the exact device name for prefix to change from ?BAT? to ?SEP? upon Save .

SEP{mac}->BAT{mac}: You can blank out the MAC address for prefix to change from ?SEP? to ?BAT? and a new device name with a prefix of ?BAT? .

Step 5

From the Device Template drop-down, select a template such as an existing Universal Device Template with the settings ou want to apply.

Step 6

From the Directory Number field, select an existing directory number, or click New and do the following:

In the Add New Extension popup, enter a new directory number and a Line Template that contains the settings you want to apply.

Click Save and then click Close .

Step 7

Optional. From the User field, select the User ID that you want to apply to this phone.

Step 8

Click Add .

Step 9

Check the Requires Activation Code for Onboarding check box. In case of Mobile and Remote Access mode, check the Allow Activation Code via Mobile and Remote Access check box.

Step 10

Configure any other settings that you want to apply. Refer to the online help for help with the fields and their settings.

Step 11

Click Save , and then click OK .

#### What to do next

### Add Phones with Activation Codes via Bulk Administration

Step 1

Configure BAT Provisioning Template

Configure a BAT Template that contains the settings that you want to apply to provisioned phones.

Step 2

Create CSV File with New Phones

Create a CSV file that contains the new phones that you want to add.

Step 3

Insert Phones

Use Bulk Administrations's Insert Phones function to add the new phones to the database.

#### Configure BAT Provisioning Template

##### Before you begin

Step 1

From Cisco Unified CM Administration, choose Bulk Administration > Phones > Phone Template .

Step 2

Click Add New .

Step 3

From the Phone Type drop-down, select the phone model for which you want to create a template.

Step 4

Enter a Template Name .

Step 5

Check the Require Activation Code for Onboarding check box. In case of Mobile and Remote Access mode, check the Allow Activation Code via Mobile and Remote Access check box.

Step 6

Configure values for the following mandatory fields:

- Device Pool

- Phone Button Template

- Owner User ID

- Device Security Profile

- SIP Profile

Step 7

Complete any remaining fields in the Phone Template Configuration window. For help with the fields and their settings, refer to the online help.

Step 8

Click Save .

##### What to do next

#### Create CSV File with New Phones

Step 1

From Cisco Unified CM Administration, choose Bulk Administration > Upload/Download Files .

Step 2

Click Find .

Step 3

Select and download the bat.xlt spreadsheet.

Step 4

Open the spreadsheet and go to the Phones tab.

Step 5

Add your new phone details to the spreadsheet. If you are using dummy MAC addresses, leave the MAC Address field empty. Check the Require Activation Code for Onboarding check box. In case of Mobile and Remote Access mode, check the Allow Activation Code via Mobile and Remote Access check box.

Step 6

When you are done, click Export to BAT Format .

Step 7

From Cisco Unified CM Administration, choose Bulk Administration > Upload/Download Files .

Step 8

Upload the csv file.

Click Add New .

Click Choose File and select the csv file for uploading.

Select Phones as the target.

Select Insert Phones - Specific Details for the transaction type.

Click Save .

##### What to do next

#### Insert Phones

Step 1

Select Bulk Administration > Phones > Insert Phones .

Step 2

From the File Name drop-down, select your csv file.

Step 3

From the Phone Template Name drop-down, select the provisioning template that you created.

Step 4

Check the Create Dummy MAC Address check box.

Step 5

Check the Run Immediately check box to run the job right away. If you choose to run the job later, you must schedule the job in the Bulk Administration
                                             Tool’s Job Scheduler.

Step 6

Click Submit.

##### What to do next

### Activate Phones

After provisioning, distribute activation codes to your phone users so that they can activate their phones. Following are
                                 two options for gathering and distributing activation codes:

Self-Care Portal—Phone users can log in to the Self-Care Portal in order obtain the activation code that applies to their
                                       phone. They can either input the code on the phone manually, or use their phone's video camera to scan the barcode that displays
                                       in Self-Care. Either method will work. To use Self-Care to activate the phone, the Show Phones Ready to Activate enterprise parameter must be set to True in Cisco Unified Communications Manager (this is the default setting).

CSV File—You can also export the list of outstanding users and activation codes to a csv file, which you can then distribute
                                       to your users. For a procedure, see Export Activation Codes .

#### Registration Process

Phone users must enter the activation code on their phone in order to use their phones. After a phone user enters the correct
                                 activation code on the phone, the following occurs:

Their phone authenticates with Cisco Unified Communications Manager.

The phone configuration in Cisco Unified Communications Manager updates with the actual MAC address of the phone.

The phone downloads the configuration file and any other relevant files from the TFTP server and registers with Cisco Unified
                                       Communications Manager.

#### What to do Next

The phone is now ready to use.

#### Export Activation Codes

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

From Related Links , select Export Activation Codes and click Go .

## Device Onboarding Task Flow (Mobile and Remote Access Mode)

### Before you begin

Step 1

Enable Cisco Cloud Onboarding via Mobile and Remote Access

Under Cloud Onboarding , generate voucher, enable Activation Code Onboarding and specify the Mobile and Remote Access activation domain.

Step 2

Mobile and Remote Access Service Domain Configuration (Optional)

Onboard the cluster to the cloud to allow remote Mobile and Remote Access device onboarding to a specific Mobile and Remote
                                          Access Activation Domain.

Step 3

Upload Custom Certificate (Optional)

Optional. If you want to use your own custom certificates, remote Mobile and Remote Access endpoints will be able to download
                                          them from the cloud and use them to connect to Expressway.

Step 4

Provision phones with activation code requirement. Following are two provisioning sample options:

- Add Phone with Activation Code Requirement

- Add Phones with Activation Codes via Bulk Administration

You must provision the phone in the Unified CM database. Unified CM has a variety of provisioning methods that you can use,
                                          including these sample options.

Step 5

Activate Phones

Distribute activation codes to users. Users must enter the code on the phone in order to use the phone.

### Enable Cisco Cloud Onboarding via Mobile and Remote Access

Step 1

To authorize the cluster (CCMAct service) to connect to the cloud-based device activation service, generate the voucher by
                                          clicking the Generate Voucher button.

Step 2

Specify an Mobile and Remote Access Activation Domain. (This is copied to the Mobile and Remote Access Service Domain list
                                          automatically.)

Step 3

Enable activation code onboarding by checking the 'Enable the Activation Code Onboarding' and 'Allow Mobile and Remote Access
                                          Onboarding' checkboxes. If you configured device defaults onboarding using 'Auto Registration', then the 'Allow Mobile and
                                          Remote Access Onboarding' checkbox is disabled and automatically checked as it can only work for phones in Mobile and Remote
                                          Access mode. If you configured device defaults onboarding using 'Activate Code', then both the check boxes are available.

Step 4

Click Save .

### Mobile and Remote Access Service Domain Configuration (Optional)

To configure Mobile and Remote Access Service Domain for your phone, use the following procedure:

Step 1

Choose Advanced Features > Mobile and Remote Access Service Domain to access the Mobile and Remote Access Service Domain window.

Step 2

Enter the Mobile and Remote Access Service Domain name.

Step 3

Enter the SRV record for the Expressway-E that is used for activation.

Step 4

Choose the default Mobile and Remote Access Service Domain by checking the Default check box next to the selected domain. This is the domain that is used when you choose '< None >' at the device pool level.

Step 5

Access the Dependency Records using the link on the row of that record that also lists the number of dependencies.

### Upload Custom Certificate (Optional)

To upload custom certificates, use the following procedure:

Step 1

Upload the certificates to the Expressway. Do not remove any other certificates.

Step 2

Upload the new certificates to Unified Communications Manager using the path CUCM OS Administration > Certificate Management . Use the “Phone-Edge-trust” type. ( Unified Communications Manager sends these to the cloud and then to the phone to access the Expressway.)

Step 3

Remove any other “Phone-Edge-trust” type certificates, as desired, so that the custom certificates are the only ones in use.

## Additional Tasks for Activation Code

The following table lists additional tasks that you may need for activation codes.

Task

Generate activation codes for registered phones

If you want to generate an activation code for an already-registered phone:

From Cisco Unified CM Administration, choose Device > Phone .

Search for and open the Phone Configuation for the phone for which you want to generate an activation code.

Check the Requires Activation Code for Onboarding check box and click Save .

Regenerate activation codes for unregistered phones

To generate a new activation code for an unregistered phone, such as may be required if the activation process for a new phone
                                          fails, do the following:

From Cisco Unified CM Administration, choose Device > Phone .

Search for and open the Phone Configuation for the phone for which you want to generate an activation code.

Click Release Activation Code

Click Generate New Activation Code and click Save .

Set Optional Activation Code Parameters

If you want to configure optional service parameters for activation codes.

From Cisco Unified CM Administration, choose System > Service Parameters .

From the Server drop-down, select the publisher node.

From the Service drop-down, select Cisco Device Activation Service .

Configure a value for the following optional service parameters. For help with the settings, refer to the context-sensitive
                                                help

Activation Time to Live (Hours) —The number of hours that an activation code remains active. The default is 168

Enable Mobile and Remote Access Activation —Set this to True (the default setting) to enable Mobile and Remote Access activation.

Mobile and Remote Access Activation Domain —The domain where Mobile and Remote Access device activation takes place.

Click Save .

## Activation Code Use Cases

The following table highlights sample use cases with device onboarding via activation codes.

Use Case

Description

Replace an existing phone

Activation codes make it easy to replace existing phones. For example, let’s say that a remote worker needs a new phone as
                                          their phone is damaged.

The administrator opens the Phone Configuration settings for the damaged phone in Unified Communications Manager.

The administrator blanks out the MAC Address , checks the Requires Activation Code for Onboarding check box, and clicks Save .

The user acquires a new phone of the same phone model, and plugs their phone into the network.

The user logs in to Self-Care to get their activation code, and inputs the code on the phone. The phone onboards successfully.

Secure shipping of new phone with activation codes

In a more secure environment where you can ensure that phone shipping process is secure by ting the activation code to a specific
                                          MAC address as follows:

The administrator provisions a new phone in Unified Communications Manager.

In the Phone Configuration settings for the new phone, the administrator enters the phone’s actual MAC Address and checks the Requires Activation Code for Onboarding check box.

The administrator packages the phone and ships the phone to the user.

The user plugs the new phone into the network.

The user logs in to Self-Care to get the activation code, enters the code on the phone. The phone onboards successfully.

Secure shipping of new phone (autoregistration)

As an alternative to activation codes, you can also use autoregistration and TAPS to securely ship phones to a remote worker:

In the Device Defaults Configuration , the administrator makes sure that the Onboarding Method for the phone model is Autoregistration .

The administrator provisions a new phone in Unified Communications Manager. In the Phone Configuration for the new phone, the administrator blanks out the phone’s actual MAC Address .

The administrator packages the phone and ships the phone to the user.

The user plugs the new phone into the network, and lets it autoregister.

The user uses TAPS to map the autoregistered record back to the old record.

This scenario requires you to configure both autoregistration and TAPS.

Re-onboarding phones via autoregistration

You can switch onboarding methods for specific phone models between Activation Codes and Autoregistration via the On-Premise Onboarding Method field in the Device Defaults Configuration window.

Onboarding On-Premise phones for Use in Mobile and Remote Access mode

You can onboard the phones on-premise, and then mark the phone for onboarding again in Mobile and Remote Access mode to leverage
                                          the security provided by OAuth connection to Expressway and trusted connection from Expressway to Cisco Unified Communications
                                          Manager.

In this scenario, with 'Allow Activation Code via Mobile and Remote Access' enabled, the phone onboards on-premise, validates
                                          the OAuth access token that it received, and switches to Mobile and Remote Access mode and initiates communication with the
                                          Expressway. If your internal network does not allow communication with the Expressway from on-premise, the phone does not
                                          register, but is ready to contact the Expressway when it is powered up off-premise.

The off-premise phones that are unregistered cannot update their firmware load.This scenario is useful with out-of-the-box
                                                      phones that need to be on premise to download the latest firmware and use the Activation Code feature.

| Note | Cisco Manufacturing Root certificates must be present in the CallManager-trust store to perform onboarding activity. |
|---|---|

| Note | When you provision with BAT MAC addresses, activation codes are tied to the phone model. BAT MAC is a reference to the device name that starts with 'BAT' and is followed by a random 12 hexidecimal digits that look
                                             like a MAC address. When saving a device configuration page with a blank MAC Address field, a random name with this format
                                             is created for you. You must enter an activation code that matches the phone model in order to activate the phone. For added security, you can provision the phone with the actual MAC address of the phone. This option involves more configuration
                                          because the administrator must gather and input each phone's MAC address during provisioning, but provides greater security
                                          because users must enter the activation code that matches the actual MAC address on their phone. |
|---|---|

| Note | It's recommended to add an additional subscriber to the default communication manager group for on-premise activation code
                                                   onboarding. Else, when the node in the default communication manager group goes down, you may face onboarding issues. |
|---|---|

| Note | To provide secure solution for work from home remote users, Expressway's Mobile and Remote Access is the recommended solution
                                             and not TRP. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Activate the Device Activation Service | The Cisco Device Activation Service must be running in Cisco Unified Serviceability. |
| Step 2 | Set Registration Method to use Activation Codes | Under Device Defaults, set the default registration method to use Activation Codes for supported phone models. |
| Step 3 | Provision phones with activation code requirement. Following are two provisioning example options: Add Phone with Activation Code Requirement Add Phones with Activation Codes via Bulk Administration | Cisco Unified Communications Manager has a variety of provisioning methods, including the options on the left. Whichever method
                                          you choose, make sure the Requires Activation Code for Onboarding check box is checked within that phone's Phone Configuration . |
| Step 4 | Activate Phones | Distribute activation codes to users. Users must enter the code on the phone in order to use the phone. |

| Step 1 | From Cisco Unified Serviceability, choose Tools > Service Activation . |
|---|---|
| Step 2 | From the Server drop-down, choose the Unified Communications Manager publisher node and click Go . |
| Step 3 | Under CM Services , confirm that the Status of the Cisco Device Activation Service says Activated . |
| Step 4 | If the service is not running, check the adjacent check box and click Save . |

| Note | This procedure applies for the onboarding of on-premise endpoints only. The Onboarding Method setting under Device Defaults does not apply for onboarding of Mobile and Remote Access endpoints using activation codes. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Device Defaults . |
|---|---|
| Step 2 | In the Device Defaults Configuration window, select the device type that will use activation codes for registration in the Dual Bank Information section, and change On-Premise Onboarding Method from Auto Registration to Activation Code . |
| Step 3 | Click Save . Note When device default is set to Activation Code, and if Auto Registration is earlier used for phone types, subsequent addition
                                                         of new phones should follow Activation Code Onboarding or Manual Configuration of Phone (Using MAC address) and Registration. For more information, see Add Phone with Activation Code Requirement and Add Phones with Activation Codes via Bulk Administration section to provision new phones. | Note | When device default is set to Activation Code, and if Auto Registration is earlier used for phone types, subsequent addition
                                                         of new phones should follow Activation Code Onboarding or Manual Configuration of Phone (Using MAC address) and Registration. For more information, see Add Phone with Activation Code Requirement and Add Phones with Activation Codes via Bulk Administration section to provision new phones. |
| Note | When device default is set to Activation Code, and if Auto Registration is earlier used for phone types, subsequent addition
                                                         of new phones should follow Activation Code Onboarding or Manual Configuration of Phone (Using MAC address) and Registration. For more information, see Add Phone with Activation Code Requirement and Add Phones with Activation Codes via Bulk Administration section to provision new phones. |

| Note | When device default is set to Activation Code, and if Auto Registration is earlier used for phone types, subsequent addition
                                                         of new phones should follow Activation Code Onboarding or Manual Configuration of Phone (Using MAC address) and Registration. For more information, see Add Phone with Activation Code Requirement and Add Phones with Activation Codes via Bulk Administration section to provision new phones. |
|---|---|

| Note | If you choose not to use templates, you can add a new phone and configure settings manually, or add settings via a BAT Template.
                                          In each case, the Requires Activation Code for Onboarding check box must be checked in the Phone Configuration window. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Add New From Template to add settings from a universal line or device template. |
| Step 3 | From the Phone Type drop-down menu, select the phone model. |
| Step 4 | In the MAC Address field, enter a MAC address. With activation codes, you can use a dummy MAC address or the phone's actual MAC address. You can modify the MAC address of a phone in the following scenarios: BAT{mac}->SEP{mac} : You should know the exact device name for prefix to change from ?BAT? to ?SEP? upon Save . SEP{mac}->BAT{mac}: You can blank out the MAC address for prefix to change from ?SEP? to ?BAT? and a new device name with a prefix of ?BAT? . |
| Step 5 | From the Device Template drop-down, select a template such as an existing Universal Device Template with the settings ou want to apply. |
| Step 6 | From the Directory Number field, select an existing directory number, or click New and do the following: In the Add New Extension popup, enter a new directory number and a Line Template that contains the settings you want to apply. Click Save and then click Close . The new extension appears in the Directory Number field. |
| Step 7 | Optional. From the User field, select the User ID that you want to apply to this phone. |
| Step 8 | Click Add . |
| Step 9 | Check the Requires Activation Code for Onboarding check box. In case of Mobile and Remote Access mode, check the Allow Activation Code via Mobile and Remote Access check box. |
| Step 10 | Configure any other settings that you want to apply. Refer to the online help for help with the fields and their settings. |
| Step 11 | Click Save , and then click OK . The Phone Configuration generates the new activation code. Click View Activation Code if you want to view the code. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure BAT Provisioning Template | Configure a BAT Template that contains the settings that you want to apply to provisioned phones. |
| Step 2 | Create CSV File with New Phones | Create a CSV file that contains the new phones that you want to add. |
| Step 3 | Insert Phones | Use Bulk Administrations's Insert Phones function to add the new phones to the database. |

| Step 1 | From Cisco Unified CM Administration, choose Bulk Administration > Phones > Phone Template . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Phone Type drop-down, select the phone model for which you want to create a template. |
| Step 4 | Enter a Template Name . |
| Step 5 | Check the Require Activation Code for Onboarding check box. In case of Mobile and Remote Access mode, check the Allow Activation Code via Mobile and Remote Access check box. |
| Step 6 | Configure values for the following mandatory fields: Device Pool Phone Button Template Owner User ID Device Security Profile SIP Profile |
| Step 7 | Complete any remaining fields in the Phone Template Configuration window. For help with the fields and their settings, refer to the online help. |
| Step 8 | Click Save . |

| Note | You can also create your csv file manually. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Bulk Administration > Upload/Download Files . |
|---|---|
| Step 2 | Click Find . |
| Step 3 | Select and download the bat.xlt spreadsheet. |
| Step 4 | Open the spreadsheet and go to the Phones tab. |
| Step 5 | Add your new phone details to the spreadsheet. If you are using dummy MAC addresses, leave the MAC Address field empty. Check the Require Activation Code for Onboarding check box. In case of Mobile and Remote Access mode, check the Allow Activation Code via Mobile and Remote Access check box. |
| Step 6 | When you are done, click Export to BAT Format . |
| Step 7 | From Cisco Unified CM Administration, choose Bulk Administration > Upload/Download Files . |
| Step 8 | Upload the csv file. Click Add New . Click Choose File and select the csv file for uploading. Select Phones as the target. Select Insert Phones - Specific Details for the transaction type. Click Save . |

| Step 1 | Select Bulk Administration > Phones > Insert Phones . |
|---|---|
| Step 2 | From the File Name drop-down, select your csv file. |
| Step 3 | From the Phone Template Name drop-down, select the provisioning template that you created. |
| Step 4 | Check the Create Dummy MAC Address check box. Note For added security, you can add actual MAC addresses to the csv file such that the activation code works only for the phone
                                                         with the matching MAC address. In this instance, leave this check box unchecked. | Note | For added security, you can add actual MAC addresses to the csv file such that the activation code works only for the phone
                                                         with the matching MAC address. In this instance, leave this check box unchecked. |
| Note | For added security, you can add actual MAC addresses to the csv file such that the activation code works only for the phone
                                                         with the matching MAC address. In this instance, leave this check box unchecked. |
| Step 5 | Check the Run Immediately check box to run the job right away. If you choose to run the job later, you must schedule the job in the Bulk Administration
                                             Tool’s Job Scheduler. |
| Step 6 | Click Submit. |

| Note | For added security, you can add actual MAC addresses to the csv file such that the activation code works only for the phone
                                                         with the matching MAC address. In this instance, leave this check box unchecked. |
|---|---|

| Note | For additional requirements on how to configure user access for the Self-Care portal, see the "Self-Care Portal" chapter of
                                                the Feature Configuration Guide for Cisco Unified Communications Manager . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | From Related Links , select Export Activation Codes and click Go . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable Cisco Cloud Onboarding via Mobile and Remote Access | Under Cloud Onboarding , generate voucher, enable Activation Code Onboarding and specify the Mobile and Remote Access activation domain. |
| Step 2 | Mobile and Remote Access Service Domain Configuration (Optional) | Onboard the cluster to the cloud to allow remote Mobile and Remote Access device onboarding to a specific Mobile and Remote
                                          Access Activation Domain. |
| Step 3 | Upload Custom Certificate (Optional) | Optional. If you want to use your own custom certificates, remote Mobile and Remote Access endpoints will be able to download
                                          them from the cloud and use them to connect to Expressway. |
| Step 4 | Provision phones with activation code requirement. Following are two provisioning sample options: Add Phone with Activation Code Requirement Add Phones with Activation Codes via Bulk Administration | You must provision the phone in the Unified CM database. Unified CM has a variety of provisioning methods that you can use,
                                          including these sample options. |
| Step 5 | Activate Phones | Distribute activation codes to users. Users must enter the code on the phone in order to use the phone. |

| Step 1 | To authorize the cluster (CCMAct service) to connect to the cloud-based device activation service, generate the voucher by
                                          clicking the Generate Voucher button. |
|---|---|
| Step 2 | Specify an Mobile and Remote Access Activation Domain. (This is copied to the Mobile and Remote Access Service Domain list
                                          automatically.) |
| Step 3 | Enable activation code onboarding by checking the 'Enable the Activation Code Onboarding' and 'Allow Mobile and Remote Access
                                          Onboarding' checkboxes. If you configured device defaults onboarding using 'Auto Registration', then the 'Allow Mobile and
                                          Remote Access Onboarding' checkbox is disabled and automatically checked as it can only work for phones in Mobile and Remote
                                          Access mode. If you configured device defaults onboarding using 'Activate Code', then both the check boxes are available. |
| Step 4 | Click Save . |

| Step 1 | Choose Advanced Features > Mobile and Remote Access Service Domain to access the Mobile and Remote Access Service Domain window. |
|---|---|
| Step 2 | Enter the Mobile and Remote Access Service Domain name. |
| Step 3 | Enter the SRV record for the Expressway-E that is used for activation. |
| Step 4 | Choose the default Mobile and Remote Access Service Domain by checking the Default check box next to the selected domain. This is the domain that is used when you choose '< None >' at the device pool level. |
| Step 5 | Access the Dependency Records using the link on the row of that record that also lists the number of dependencies. |

| Step 1 | Upload the certificates to the Expressway. Do not remove any other certificates. |
|---|---|
| Step 2 | Upload the new certificates to Unified Communications Manager using the path CUCM OS Administration > Certificate Management . Use the “Phone-Edge-trust” type. ( Unified Communications Manager sends these to the cloud and then to the phone to access the Expressway.) |
| Step 3 | Remove any other “Phone-Edge-trust” type certificates, as desired, so that the custom certificates are the only ones in use. |

| Task | Procedure |
|---|---|
| Generate activation codes for registered phones | If you want to generate an activation code for an already-registered phone: From Cisco Unified CM Administration, choose Device > Phone . Search for and open the Phone Configuation for the phone for which you want to generate an activation code. Check the Requires Activation Code for Onboarding check box and click Save . |
| Regenerate activation codes for unregistered phones | To generate a new activation code for an unregistered phone, such as may be required if the activation process for a new phone
                                          fails, do the following: From Cisco Unified CM Administration, choose Device > Phone . Search for and open the Phone Configuation for the phone for which you want to generate an activation code. Click Release Activation Code Click Generate New Activation Code and click Save . |
| Set Optional Activation Code Parameters | If you want to configure optional service parameters for activation codes. From Cisco Unified CM Administration, choose System > Service Parameters . From the Server drop-down, select the publisher node. From the Service drop-down, select Cisco Device Activation Service . Configure a value for the following optional service parameters. For help with the settings, refer to the context-sensitive
                                                help Activation Time to Live (Hours) —The number of hours that an activation code remains active. The default is 168 Enable Mobile and Remote Access Activation —Set this to True (the default setting) to enable Mobile and Remote Access activation. Mobile and Remote Access Activation Domain —The domain where Mobile and Remote Access device activation takes place. Click Save . |

| Use Case | Description |
|---|---|
| Replace an existing phone | Activation codes make it easy to replace existing phones. For example, let’s say that a remote worker needs a new phone as
                                          their phone is damaged. The administrator opens the Phone Configuration settings for the damaged phone in Unified Communications Manager. The administrator blanks out the MAC Address , checks the Requires Activation Code for Onboarding check box, and clicks Save . The user acquires a new phone of the same phone model, and plugs their phone into the network. The user logs in to Self-Care to get their activation code, and inputs the code on the phone. The phone onboards successfully. Note In this scenario, the user can onboard any new phone so long as it is the same phone model as the damaged phone. In a more
                                                   secure environment, the administrator may need to provision a replacement phone to replace the old phone (see below). | Note | In this scenario, the user can onboard any new phone so long as it is the same phone model as the damaged phone. In a more
                                                   secure environment, the administrator may need to provision a replacement phone to replace the old phone (see below). |
| Note | In this scenario, the user can onboard any new phone so long as it is the same phone model as the damaged phone. In a more
                                                   secure environment, the administrator may need to provision a replacement phone to replace the old phone (see below). |
| Secure shipping of new phone with activation codes | In a more secure environment where you can ensure that phone shipping process is secure by ting the activation code to a specific
                                          MAC address as follows: The administrator provisions a new phone in Unified Communications Manager. In the Phone Configuration settings for the new phone, the administrator enters the phone’s actual MAC Address and checks the Requires Activation Code for Onboarding check box. The administrator packages the phone and ships the phone to the user. The user plugs the new phone into the network. The user logs in to Self-Care to get the activation code, enters the code on the phone. The phone onboards successfully. Note In this scenario, the user can onboard only that specific phone. | Note | In this scenario, the user can onboard only that specific phone. |
| Note | In this scenario, the user can onboard only that specific phone. |
| Secure shipping of new phone (autoregistration) | As an alternative to activation codes, you can also use autoregistration and TAPS to securely ship phones to a remote worker: In the Device Defaults Configuration , the administrator makes sure that the Onboarding Method for the phone model is Autoregistration . The administrator provisions a new phone in Unified Communications Manager. In the Phone Configuration for the new phone, the administrator blanks out the phone’s actual MAC Address . The administrator packages the phone and ships the phone to the user. The user plugs the new phone into the network, and lets it autoregister. The user uses TAPS to map the autoregistered record back to the old record. Note This scenario requires you to configure both autoregistration and TAPS. | Note | This scenario requires you to configure both autoregistration and TAPS. |
| Note | This scenario requires you to configure both autoregistration and TAPS. |
| Re-onboarding phones via autoregistration | You can switch onboarding methods for specific phone models between Activation Codes and Autoregistration via the On-Premise Onboarding Method field in the Device Defaults Configuration window. Note If you want to re-onboard an existing phone via autoregistration, you must delete the existing record from the database for
                                                   autoregistration to work. | Note | If you want to re-onboard an existing phone via autoregistration, you must delete the existing record from the database for
                                                   autoregistration to work. |
| Note | If you want to re-onboard an existing phone via autoregistration, you must delete the existing record from the database for
                                                   autoregistration to work. |
| Onboarding On-Premise phones for Use in Mobile and Remote Access mode | You can onboard the phones on-premise, and then mark the phone for onboarding again in Mobile and Remote Access mode to leverage
                                          the security provided by OAuth connection to Expressway and trusted connection from Expressway to Cisco Unified Communications
                                          Manager. In this scenario, with 'Allow Activation Code via Mobile and Remote Access' enabled, the phone onboards on-premise, validates
                                          the OAuth access token that it received, and switches to Mobile and Remote Access mode and initiates communication with the
                                          Expressway. If your internal network does not allow communication with the Expressway from on-premise, the phone does not
                                          register, but is ready to contact the Expressway when it is powered up off-premise. Note The off-premise phones that are unregistered cannot update their firmware load.This scenario is useful with out-of-the-box
                                                      phones that need to be on premise to download the latest firmware and use the Activation Code feature. | Note | The off-premise phones that are unregistered cannot update their firmware load.This scenario is useful with out-of-the-box
                                                      phones that need to be on premise to download the latest firmware and use the Activation Code feature. |
| Note | The off-premise phones that are unregistered cannot update their firmware load.This scenario is useful with out-of-the-box
                                                      phones that need to be on premise to download the latest firmware and use the Activation Code feature. |

| Note | In this scenario, the user can onboard any new phone so long as it is the same phone model as the damaged phone. In a more
                                                   secure environment, the administrator may need to provision a replacement phone to replace the old phone (see below). |
|---|---|

| Note | In this scenario, the user can onboard only that specific phone. |
|---|---|

| Note | This scenario requires you to configure both autoregistration and TAPS. |
|---|---|

| Note | If you want to re-onboard an existing phone via autoregistration, you must delete the existing record from the database for
                                                   autoregistration to work. |
|---|---|

| Note | The off-premise phones that are unregistered cannot update their firmware load.This scenario is useful with out-of-the-box
                                                      phones that need to be on premise to download the latest firmware and use the Activation Code feature. |
|---|---|