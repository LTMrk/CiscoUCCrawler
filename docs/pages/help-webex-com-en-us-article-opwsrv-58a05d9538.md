---
doc_id: help-webex-com-en-us-article-opwsrv-58a05d9538
source_url: https://help.webex.com/en-us/article/opwsrv
retrieved_at: 2026-11-02T13:12:19.894456+00:00
---

## Manage access to the phone web interface

### Administrator and user accounts

The Cisco IP Phone firmware provides specific administrator and user accounts. These accounts provide specific login privileges. The administrator account name is admin ; the user account name is user . These account names cannot be changed.

The admin account gives the service provider or Value-added Reseller (VAR) configuration access to the phone. The user account gives limited and configurable control to the device end user.

The user and admin accounts can be password protected independently. If the service provider sets an administrator account password, you are prompted for it when you click Admin Login . If the password does not yet exist, the screen refreshes and displays the administration parameters. No default passwords are assigned to either the administrator or the user account. Only the administrator account can assign or change passwords.

The administrator account can view and modify all web profile parameters, including web parameters, that are available to the user login. The phone system administrator can further restrict the parameters that a user account can view and modify through use of a provisioning profile.

Configuration parameters that are available to the user account are configurable on the phone. User access to the phone web user interface can be disabled.

### User access attribute

The user access ( ua ) attribute controls may be used to change access by the User account. If the ua attribute is not specified, the existing user access setting is retained. This attribute does not affect access by the Admin account.

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
	<Station_Name ua=“rw”>Travel Agent 1</Station_Name>
</flat-profile>
```

Double quotes must enclose the value of the ua option.

### User Preference Attribute

The user-pref attribute allows you to set some user preferred value to provide a
        seamless experience for your user. Users can make further changes from the phone or from the
        phone administration web page. Any parameter changed by user is marked as user modified with
        an attribute um . Any changes made by the user are preserved. The user-pref attribute can be updated during provisioning using XML configurations delivered with the Profile Rule parameter.

The user-pref attribute is not mandatory. However, if present, must have one of the
        following values:

y—Indicates to honor the user-made changes to be included during the configuration. It
        also specifies to set the value set by the administrator if the user has not modified
        it.

n—Indicates to honor the administrator set value provided through XML configurations. If
        the user-pref attribute is not included, it has the same effect as setting its value
        to "n".

The following example illustrates the user-pref attribute:

```
<flat-profile>
	<Display_Brightness ua="rw" user-pref="y">5</Display_Brightness>
</flat-profile>
```

The following example illustrates the um attribute.

```
<flat-profile>
	<Display_Brightness ua="rw" user-pref="y" um="y">5</Display_Brightness>
</flat-profile>
```

Factory reset clears all the configurations marked with um and user-pref attributes.

During provisioning, for any parameter, if the attribute user-pref =“n” is added,
        after you apply the configuration, the parameter’s attribute user-pref is updated to
        “n”, and the um attribute gets cleared.

### Access the phone web interface

The phone firmware provides mechanisms for restricting end-user access to some parameters. The firmware provides specific privileges for sign-in to an Admin account or a User account. Each can be independently password-protected.

Admin account–Allows the full access to all administration web server parameters

User account–Allows the access to a subset of the administration web server parameters

If your service provider has disabled access to the configuration utility, contact the service provider before proceeding.

Ensure that the computer can communicate with the phone. No VPN in use.

Enter the IP address of the phone in your web browser address bar.

- User Access: http://<ip address>

- Admin Access: http://<ip address>/admin/advanced

- Admin Access: http://<ip address> , click Admin Login and click advanced

For example, http://10.64.84.147/admin

(Optional) If prompted to set up the admin and user passwords, do the following:

It's mandatory to set up the passwords after the phone's initial registration
              (Out-Of-Box) or you perform a factory reset.

On the Set Password page, fill in the following parameters:

- Admin New Password—Enter a new password for the admin account.

- Admin Confirm Password—Enter the new admin password again, to confirm.

- User New Password—Enter a new password for the user account.

- User Confirm Password—Enter the new user password again, to confirm.

Password rules:

- The password must contain at least 8 to 127 characters.

- A combination (three out of four types) of capital letter, small lower letter, number, and special character.

- Space is not allowed.

After making changes, click Submit to apply your settings.

Enter the password when prompted.

### Control access to the phone settings

You can configure the phone to allow or block access to the configuration parameters on the phone web page or the phone screen. The parameters for access control allow you to:

Enable or disable the access to the phone web interface.

Enable or disable the access to the phone administration web page.

Set the admin or user password.

Display or hide the "No password provided" warning on the phone screen.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code. To configure each parameter, see the syntax of the string in the following table of Access control parameters .

Access the phone administration web page.

Click Voice > System .

In the System Configuration section, configure the parameters as defined in the following table of Access control parameters .

Click Submit All Changes to apply the changes.

#### Access control parameters

The following table defines the function and usage of the access control parameters in the System Configuration section under the Voice > System tab in the phone web interface. It also defines the syntax of the string that is added in the phone configuration file (cfg.xml) to configure a parameter.

Parameter Name

Description and Default Value

Enable Web Server

Enables or disables access to the phone web interface. Set this parameter to Yes to allow users or administrators to access the phone web interface. Otherwise, set it to No . When set to No , the phone web interface isn't accessible.

Perform one of the following:

In the phone configuration file (cfg.xml), enter a string in this format:

In the phone web interface, set to Yes to allow the access.

Allowed values: Yes|No

Default: Yes.

Enable Web Admin Access

Allows or blocks the access to the phone administration pages:

http://<phone_IP>/admin

When set to No , the web page for administrator is inaccessible. Only the web page for user is accessible.

If you want to allow the access to the administration web page again after the access is blocked, you need to perform a factory reset from the phone.

Perform one of the following:

In the phone configuration file (cfg.xml), enter a string in this format:

In the phone web interface, set this parameter to Yes to allow the access. Otherwise, set it to No .

Allowed values: Yes|No

Default: Yes

Admin Password

Allows you to set or change the password for accessing the phone administration web pages.

The Admin Password parameter is only available on the phone administration web page.

Valid password rules:

- The password must contain at least 8 to 127 characters.

- Three out of four types: capital letter, small letter, number, and special character.

- Space is not allowed.

The password is set to empty after you perform a phone factory reset.

Perform one of the following:

In the phone configuration file (cfg.xml), enter a string in this format: <Admin_Password ua="na">P0ssw0rd_tes89</Admin_Password>

In the phone web interface, enter the password for administrator access.

Default: Empty

User Password

Allows you or the phone user to set or change the password for accessing the phone web interfaces and the menus on the phone screen.

Valid password rules:

- The password must contain at least 8 to 127 characters.

- Three out of four types: capital letter, small letter, number, and special character.

- Space is not allowed.

The password is set to empty after you perform a phone factory reset.

Perform one of the following:

In the phone configuration file (cfg.xml), enter a string in this format: <User_Password ua="rw">P0ssw0rd_tes99</User_Password>

In the phone web interface, enter the password for user access.

Default: Empty

Display Password Warnings

Determines whether to display the No password provided warning when the user or admin password is empty. Typically, the warning message displays on the phone Issues and diagnostics screen.

The warning message disappears when both user password and admin password are set.

If Enable Web Admin Access is set to No , the password warning doesn't display on the phone
                    screen.

Perform one of the following:

In the phone configuration file (cfg.xml), enter a string in this format:

In the phone web interface, set to Yes to display the warning, set to No to hide the warning.

Allowed values: Yes|No

Default: Yes

## Manage the Settings menu visibility

Customize the phone's Settings menu to display only the menu items you want users to
        access.

By default, all menu items are visible on the phone. When you hide certain menu items, the
        index numbers of the remaining items will adjust automatically.

The custom settings take effect only on phones that have completed registration. On
          phones not yet onboarded to a calling system, all menu items remain visible.

Access the phone administration web page.

Click Voice > Phone .

In the Menu Customization section, set the desired menu items to
          Show or Hide.

The availability of menu items may vary by phone model. If all the child items are hidden, the parent menu is also hidden.

Click Submit All Changes to apply the changes.

| 1 | Ensure that the computer can communicate with the phone. No VPN in use. |
|---|---|
| 2 | Enter the IP address of the phone in your web browser address bar. User Access: http://<ip address> Admin Access: http://<ip address>/admin/advanced Admin Access: http://<ip address> , click Admin Login and click advanced For example, http://10.64.84.147/admin |
| 3 | (Optional) If prompted to set up the admin and user passwords, do the following: It's mandatory to set up the passwords after the phone's initial registration
              (Out-Of-Box) or you perform a factory reset. On the Set Password page, fill in the following parameters: Admin New Password—Enter a new password for the admin account. Admin Confirm Password—Enter the new admin password again, to confirm. User New Password—Enter a new password for the user account. User Confirm Password—Enter the new user password again, to confirm. Password rules: The password must contain at least 8 to 127 characters. A combination (three out of four types) of capital letter, small lower letter, number, and special character. Space is not allowed. After making changes, click Submit to apply your settings. |
| 4 | Enter the password when prompted. |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Click Voice > System . |
| 3 | In the System Configuration section, configure the parameters as defined in the following table of Access control parameters . |
| 4 | Click Submit All Changes to apply the changes. |

| Parameter Name | Description and Default Value |
|---|---|
| Enable Web Server | Enables or disables access to the phone web interface. Set this parameter to Yes to allow users or administrators to access the phone web interface. Otherwise, set it to No . When set to No , the phone web interface isn't accessible. Perform one of the following: In the phone configuration file (cfg.xml), enter a string in this format: <Enable_Web_Server ua="na">Yes</Enable_Web_Server> In the phone web interface, set to Yes to allow the access. Allowed values: Yes\|No Default: Yes. |
| Enable Web Admin Access | Allows or blocks the access to the phone administration pages: http://<phone_IP>/admin When set to No , the web page for administrator is inaccessible. Only the web page for user is accessible. If you want to allow the access to the administration web page again after the access is blocked, you need to perform a factory reset from the phone. Perform one of the following: In the phone configuration file (cfg.xml), enter a string in this format: <Enable_Web_Admin_Access ua="na">Yes</Enable_Web_Admin_Access> In the phone web interface, set this parameter to Yes to allow the access. Otherwise, set it to No . Allowed values: Yes\|No Default: Yes |
| Admin Password | Allows you to set or change the password for accessing the phone administration web pages. The Admin Password parameter is only available on the phone administration web page. Valid password rules: The password must contain at least 8 to 127 characters. Three out of four types: capital letter, small letter, number, and special character. Space is not allowed. The password is set to empty after you perform a phone factory reset. Perform one of the following: In the phone configuration file (cfg.xml), enter a string in this format: <Admin_Password ua="na">P0ssw0rd_tes89</Admin_Password> In the phone web interface, enter the password for administrator access. Default: Empty |
| User Password | Allows you or the phone user to set or change the password for accessing the phone web interfaces and the menus on the phone screen. Valid password rules: The password must contain at least 8 to 127 characters. Three out of four types: capital letter, small letter, number, and special character. Space is not allowed. The password is set to empty after you perform a phone factory reset. Perform one of the following: In the phone configuration file (cfg.xml), enter a string in this format: <User_Password ua="rw">P0ssw0rd_tes99</User_Password> In the phone web interface, enter the password for user access. Default: Empty |
| Display Password Warnings | Determines whether to display the No password provided warning when the user or admin password is empty. Typically, the warning message displays on the phone Issues and diagnostics screen. The warning message disappears when both user password and admin password are set. If Enable Web Admin Access is set to No , the password warning doesn't display on the phone
                    screen. Perform one of the following: In the phone configuration file (cfg.xml), enter a string in this format: <Display_Password_Warnings ua="na">Yes</Display_Password_Warnings> In the phone web interface, set to Yes to display the warning, set to No to hide the warning. Allowed values: Yes\|No Default: Yes |

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Click Voice > Phone . |
| 3 | In the Menu Customization section, set the desired menu items to
          Show or Hide. The availability of menu items may vary by phone model. If all the child items are hidden, the parent menu is also hidden. You can also use the configuration XML file (cfg.xml) to customize the Settings menu. See the following example: |
| 4 | Click Submit All Changes to apply the changes. |