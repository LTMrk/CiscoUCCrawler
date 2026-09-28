---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8832-english-ag-cs88-b-8832-mpp-ag-new-cs88-b-8832-mpp-adminguide-05df2c94a9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8832/english/AG/cs88_b_8832-mpp-ag_new/cs88_b_8832-mpp-adminguide_chapter_0110.html
retrieved_at: 2026-08-21T13:50:00.740069+00:00
---

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide for Release 11.3(1) and Later

# Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide for Release 11.3(1) and Later

Updated: November 21, 2019

Chapter: Access Control Configuration

## Chapter: Access Control Configuration

# Access Control Configuration

## Access Control

If the <Phone-UI-User-Mode> parameter is enabled, the phone GUI honors the user access attribute of the relevant parameters
                           when the GUI presents a menu item.

For menu entries that are associated with a single configuration parameter:

Provisioning the parameter with “ua=na” (“ua” stands for “user access”) attribute makes the entry disappear.

Provisioning the parameter with “ua=ro” attribute makes the entry read-only and non-editable.

For menu entries that are associated with multiple configuration parameters:

Provisioning all concerned parameters with “ua=na” attribute makes the entries disappear.

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

## User Access Attribute

The user access ( ua ) attribute controls may be used to change access by the User account. If the ua attribute is not specified, the existing user access setting is retained. This attribute does not affect access by the Admin
                           account.

The ua attribute, if present, must have one of the following values:

na—No access

ro—Read-only

rw—Read and write

y—Preserve value

The y value must be used together with na , ro , or rw .

The following example illustrates the ua attribute. Notice in the last line that the ua attribute is updated to rw , and the station name field ( Travel Agent 1 ) is preserved. If y is not included, Travel Agent 1 is overwritten:

```
<flat-profile>
			<SIP_TOS_DiffServ_Value_1_ ua=”na”/>
 		<Dial_Plan_1_ ua=”ro”/>	
			<Dial_Plan_2_ ua=”rw”/>
<Station_Name ua=“rw” preserve-value="y">Travel Agent 1</Station_Name></flat-profile>
```

Double quotes must enclose the value of the ua option.

## Access the Phone Web Interface

The phone firmware provides mechanisms for restricting end-user access to some parameters. The firmware provides specific
                              privileges for sign-in to an Admin account or a User account. Each can be independently password-protected.

Admin account–Allows the full access to all administration web server parameters

User account–Allows the access to a subset of the administration web server parameters

If your service provider has disabled access to the configuration utility, contact the service provider before proceeding.

Ensure that the computer can communicate with the phone. No VPN in use.

Start a web browser.

Enter the IP address of the phone in your web browser address bar.

- User Access: http://<ip address>

- Admin Access: http://<ip address>/admin/advanced

- Admin Access: http://<ip address> , click Admin Login and click advanced

For example, http://10.64.84.147/admin

Enter the password when prompted.

## Control Access to the Phone Settings

You can configure the phone to allow or block access to the configuration parameters on the phone web page or the phone screen.
                              The parameters for access control allow you to:

Indicate which configuration parameters are available to the user account when creating the configuration.

Enable or disable the access to the administration web server.

Enable or disable user access to the phone screen menus.

Bypass the Set password screen for the user.

Restrict the Internet domains that the phone accesses for resync, upgrades, or SIP registration for Line 1.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code. To configure each parameter,
                              see the syntax of the string in Access Control Parameters .

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Click Voice > System .

In the System Configuration section, configure the parameters as defined in the Access Control Parameters table.

Click Submit All Changes to apply the changes.

### Access Control Parameters

The following table defines the function and usage of the access control parameters in the System Configuration section under the Voice > System tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file (cfg.xml)
                                 with XML code to configure a parameter.

Parameter Name

Description and Default Value

Enable Web Server

Enables or disables access to the phone web interface. Set this parameter to Yes to allow users or administrators to access the phone web interface. Otherwise, set it to No . When set to No , the phone web interface isn't accessible.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, set to Yes to allow the access.

Allowed values: Yes|No

Default: Yes.

Enable Web Admin Access

Allows or blocks the access to the phone administration pages:

http://<phone_IP>/admin

When set to No , the web page for administrator is inaccessible. Only the web page for user is accessible.

If you want to allow the access to the administration web page again after the access is blocked, you need to perform a factory
                                                         reset from the phone.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, set this parameter to Yes to allow the access. Otherwise, set it to No .

Allowed values: Yes|No

Default: Yes

Admin Password

Allows you to set or change the password for accessing the phone administration web pages.

The Admin Password parameter is only available on the phone administration web page.

A valid password must contain 4 to 127 characters from three out of the four types: capital letter, small letter, number,
                                             and special character.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format: <Admin_Password ua="na">P0ssw0rd_tes89</Admin_Password>

In the phone web interface, enter the password for administrator access.

Default: Empty

User Password

Allows you or the phone user to set or change the password for accessing the phone web interfaces and the menus on the phone
                                             screen.

You can also set or change the user password from the phone screen menu Applications > Device administration > Set password .

A valid password must contain 4 to 127 characters from three out of the four types: capital letter, small letter, number,
                                             and special character.

In the configuration file (cfg.xml), you can use the User_Password parameter to bypass the Set password screen that prompts on the first boot or after a factory reset. For more information, see Bypass the Set Password Screen .

Default: Empty

Phone-UI-User-Mode

This parameter works only with the user access the ( ua ) attribute attached to an element tag in the configuration file (cfg.xml). You can restrict the parameters that the phone
                                             users see on the phone screen.

When set to Yes , you can use the ua attribute to control user access to specific parameters on the phone screen menu. When set to No , the ua attribute isn’t working.

The options for the ua attribute are “na”, “ro”, and “rw”. Parameters designated as “na” don't appear on the phone screen. Parameters designated
                                             as “ro” aren't editable by the user. Parameters designated as “rw” are editable by the user.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, set to Yes and then set the ua attribute of the desired parameter in the phone configuration file.

Example:

```
<Phone-UI-User-Mode ua="na">Yes</Phone-UI-User-Mode>
<Enable_VLAN ua="ro">Yes</Enable_VLAN>
<Preferred_Audio_Device ua="rw">Headset</Preferred_Audio_Device>
<Block_ANC_Setting ua="na">Yes</Block_ANC_Setting>
```

With the settings in the example, the user:

Can see but can't change the setting of VLAN ( Enable_VLAN ) on the phone screen menu

Can change the setting of Preferred audio device ( Preferred_Audio_Device )

Can't see the menu item Block anonymous call ( Block_ANC_Setting ) on the phone screen.

Allowed values: Yes|No

Default: No

User Password Prompt

Controls whether the user password setup screen prompts.

Perform one of the following:

In the phone configuration file with XML(cfg.xml), enter a string in this format:

In the phone web interface, set to Yes to make the prompt available to the user.

Allowed values: Yes|No

Default: Yes

## Bypass the Set Password Screen

This feature isn’t available from firmware release 11.2.3 and later.

You can bypass the phone Set password screen on the first boot or after a factory reset, based on these provisioning actions:

DHCP configuration

EDOS configuration

User password configuration using in the phone XML configuration file

After the User Password is configured, the set password screen doesn't appear.

Edit the phone cfg.xml file in a text or XML editor.

Insert the <User_Password> tag using one of these options.

- No password (start and end tag) – <User_Password></User_Password>

- Password value (4-127 characters) – <User_Password >Abc123</User_Password>

- No password (start tag only) – <User_Password />

Save the changes to the cfg.xml file.

| Step 1 | Ensure that the computer can communicate with the phone. No VPN in use. |
|---|---|
| Step 2 | Start a web browser. |
| Step 3 | Enter the IP address of the phone in your web browser address bar. User Access: http://<ip address> Admin Access: http://<ip address>/admin/advanced Admin Access: http://<ip address> , click Admin Login and click advanced For example, http://10.64.84.147/admin |
| Step 4 | Enter the password when prompted. |

| Step 1 | Click Voice > System . |
|---|---|
| Step 2 | In the System Configuration section, configure the parameters as defined in the Access Control Parameters table. |
| Step 3 | Click Submit All Changes to apply the changes. |

| Parameter Name | Description and Default Value |
|---|---|
| Enable Web Server | Enables or disables access to the phone web interface. Set this parameter to Yes to allow users or administrators to access the phone web interface. Otherwise, set it to No . When set to No , the phone web interface isn't accessible. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Enable_Web_Server ua="na">Yes</Enable_Web_Server> In the phone web interface, set to Yes to allow the access. Allowed values: Yes\|No Default: Yes. |
| Enable Web Admin Access | Allows or blocks the access to the phone administration pages: http://<phone_IP>/admin When set to No , the web page for administrator is inaccessible. Only the web page for user is accessible. Note If you want to allow the access to the administration web page again after the access is blocked, you need to perform a factory
                                                         reset from the phone. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Enable_Web_Admin_Access ua="na">Yes</Enable_Web_Admin_Access> In the phone web interface, set this parameter to Yes to allow the access. Otherwise, set it to No . Allowed values: Yes\|No Default: Yes | Note | If you want to allow the access to the administration web page again after the access is blocked, you need to perform a factory
                                                         reset from the phone. |
| Note | If you want to allow the access to the administration web page again after the access is blocked, you need to perform a factory
                                                         reset from the phone. |
| Admin Password | Allows you to set or change the password for accessing the phone administration web pages. The Admin Password parameter is only available on the phone administration web page. A valid password must contain 4 to 127 characters from three out of the four types: capital letter, small letter, number,
                                             and special character. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Admin_Password ua="na">P0ssw0rd_tes89</Admin_Password> In the phone web interface, enter the password for administrator access. Default: Empty |
| User Password | Allows you or the phone user to set or change the password for accessing the phone web interfaces and the menus on the phone
                                             screen. You can also set or change the user password from the phone screen menu Applications > Device administration > Set password . A valid password must contain 4 to 127 characters from three out of the four types: capital letter, small letter, number,
                                             and special character. In the configuration file (cfg.xml), you can use the User_Password parameter to bypass the Set password screen that prompts on the first boot or after a factory reset. For more information, see Bypass the Set Password Screen . Default: Empty |
| Phone-UI-User-Mode | This parameter works only with the user access the ( ua ) attribute attached to an element tag in the configuration file (cfg.xml). You can restrict the parameters that the phone
                                             users see on the phone screen. When set to Yes , you can use the ua attribute to control user access to specific parameters on the phone screen menu. When set to No , the ua attribute isn’t working. The options for the ua attribute are “na”, “ro”, and “rw”. Parameters designated as “na” don't appear on the phone screen. Parameters designated
                                             as “ro” aren't editable by the user. Parameters designated as “rw” are editable by the user. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <Phone-UI-User-Mode ua="na">No</Phone-UI-User-Mode> In the phone web interface, set to Yes and then set the ua attribute of the desired parameter in the phone configuration file. Example: <Phone-UI-User-Mode ua="na">Yes</Phone-UI-User-Mode>
<Enable_VLAN ua="ro">Yes</Enable_VLAN>
<Preferred_Audio_Device ua="rw">Headset</Preferred_Audio_Device>
<Block_ANC_Setting ua="na">Yes</Block_ANC_Setting> With the settings in the example, the user: Can see but can't change the setting of VLAN ( Enable_VLAN ) on the phone screen menu Can change the setting of Preferred audio device ( Preferred_Audio_Device ) Can't see the menu item Block anonymous call ( Block_ANC_Setting ) on the phone screen. Allowed values: Yes\|No Default: No |
| User Password Prompt | Controls whether the user password setup screen prompts. Perform one of the following: In the phone configuration file with XML(cfg.xml), enter a string in this format: <User_Password_Prompt ua="na">Yes</User_Password_Prompt> In the phone web interface, set to Yes to make the prompt available to the user. Allowed values: Yes\|No Default: Yes |

| Note | If you want to allow the access to the administration web page again after the access is blocked, you need to perform a factory
                                                         reset from the phone. |
|---|---|

| Note | This feature isn’t available from firmware release 11.2.3 and later. |
|---|---|

| Step 1 | Edit the phone cfg.xml file in a text or XML editor. |
|---|---|
| Step 2 | Insert the <User_Password> tag using one of these options. No password (start and end tag) – <User_Password></User_Password> Password value (4-127 characters) – <User_Password >Abc123</User_Password> No password (start tag only) – <User_Password /> |
| Step 3 | Save the changes to the cfg.xml file. |