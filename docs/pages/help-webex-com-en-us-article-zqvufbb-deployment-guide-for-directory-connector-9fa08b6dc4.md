---
doc_id: help-webex-com-en-us-article-zqvufbb-deployment-guide-for-directory-connector-9fa08b6dc4
source_url: https://help.webex.com/en-us/article/zqvufbb/Deployment-Guide-for-Directory-Connector
retrieved_at: 2026-09-01T14:55:59.961258+00:00
---

### Cisco directory connector Deployment Task Flow

Before you begin

Prepare Your Environment for Directory Connector

Install Directory Connector

Control Hub initially shows directory synchronization as disabled. To turn on
                        directory synchronization for your organization, you must install and
                        configure Directory Connector, and then successfully perform a full synchronization. For a new
                        installation of Directory Connector, always go to Control Hub ( https://admin.webex.com ) to get the latest version of the software so that you're using the
                        latest features and bug fixes. After you install the software, upgrades are
                        reported through the software and automatically install when available.

Sign In To Directory Connector

Sign in with your Webex administrator credentials and perform the initial setup.

Set Automatic Upgrades

It's always important to keep your Directory Connector software up to date to the latest version. We recommend that you use this
                        procedure to allow automatic upgrades to the software to be installed
                        silently when they're available.

Choose Active Directory Objects to Synchronize

By default, Directory Connector synchronizes all users that are not computers and all groups that are not
                        critical system objects for a domain. For more control over what objects get
                        synchronized, you can select specific users to synchronize and specify LDAP
                        filters by using the Object Selection page in the Directory Connector.

Map User Attributes

You can map attributes from your local Active Directory to corresponding attributes in the cloud. The only required field is the *uid.

Synchronize directory avatars by using one of the following procedures:

- Synchronize Directory Avatars From an Active Directory Attribute to the Cloud

- Synchronize Directory Avatars From a Resource Server to the Cloud

You can synchronize your users' avatars to the cloud so that each user's avatar appears when they sign in to the application. You can sychronize avatars from an Active Directory attribute or a resource server.

Synchronize On-Premises Room Information to the Webex Cloud

Use this procedure to synchronize on-premises room information from Active Directory into the Webex cloud. After you synchronize the room information, the on-premises room devices with a configured, mapped SIP address show up as searchable entries on cloud-registered room devices, such as a Webex Room Device or Cisco Webex Board

To Provision Users From Active Directory Into Control Hub , perform these steps:

- Do a Dry Run Synchronization on Your Active Directory Users

- Do a Full Synchronization of Active Directory Users Into the Cloud

- Assign Webex Services to Directory Synchronized Users in Control Hub

Follow this sequence to provision Active Directory users for Webex App accounts.You can provision users from a multiple forest or multiple
                        domain Active Directory deployment for Directory Connector 3.0 and later. During the process to onboard users from different
                        domains, you must decide whether to retain or delete the user objects which
                        might already exist in the Webex cloud—for example, test accounts from a trial. The goal is to have an
                        exact match between your Active Directories and the Webex cloud.

### Install Directory Connector

Control Hub initially shows directory synchronization as disabled. To turn on directory
                synchronization for your organization, you must install and configure Directory Connector, and then successfully perform a full synchronization.

You must install one connector for each Active Directory domain that you want to
                synchronize. A single Directory Connector instance can only serve a single domain. See the following diagram to understand
                the flow for multiple domain synchronization:

Before you begin

If you authenticate through a proxy server, ensure that you have your proxy credentials:

For proxy basic-authentication, you'll enter the username and password after
            you install an instance of the connector. Internet Explorer proxy configuration is also
            required for basic-authentication; see Use a Web Proxy Through The Browser

For proxy NTLM, you may see an error when you open the connector for the first time. See Use a Web Proxy Through The Browser .

In Control
            Hub , go to Users > Manage Users > Enable Directory Synchronization , and choose Next .

Click the Download and Install link to save the latest version of the connector installation .zip file to your VMware or Windows server.

You can obtain the .zip file directly from this link , but you must have full administrative access to a Control Hub organization for this software to work.

For a new installation, get the latest version of the software so that you're using the latest features and bug fixes. After you install the software, upgrades are reported through the software and automatically install when available.

On the VMware or Windows server, unzip and run the .msi file in the setup folder to launch the setup wizard.

Click Next , check the box to accept the license agreement, and then click Next until you see the account type screen.

Choose the type of service account that you want to use and perform the installation with an admin account:

- Local System —The default option. You can use this option if you have a proxy configured through Internet Explorer.

For a proxy that integrates with AD (NTLMv2 or Kerberos), you must use the domain account option. The account used to run Directory Connector Service must have enough privilege to pass proxy and access AD.

To avoid errors, make sure the following privileges are in place:

The server is part of the domain

The domain account can access the on-premises AD data and avatars data. The account must also have the local Administrator Role, because it must access access files under C:\Program Files .

For a Virtual Machine login, the admin account privilege must at least be able to read domain information.

Click Install . After the network test runs and if prompted, enter your proxy basic credentials, click OK , and then click Finish .

What to do next

We recommend that you reboot the server after installation. The dry run report cannot show the correct result when the data was not released. While rebooting the machine, all data is refreshed to show an exact result in the report.

### Sign In To Directory Connector

Before you begin

Ensure that you have your proxy credentials.

For proxy basic-auth, you'll enter the username and password after you open the connector for the first time.

For proxy NTLM, open Internet Explorer, click the gear icon, go to Internet options > Connections > LAN settings , ensure the proxy server information is added, and then click OK . See Use a Web Proxy Through The Browser .

Open the connector, and then add https://idbroker.webex.com to your list of trusted sites if
                    you see a prompt.

If prompted, sign in in with your proxy authentication credentials, and then sign in to Webex using your admin account and click Next .

Confirm your organization and domain.

If you don't check LDAP over SSL , DirSync will continue to
                use the LDAP connection protocol.

LDAP (Lightweight Directory Application Protocol) and Secure LDAP (LDAPS) are the connection protocols used between an application and the Domain Controller within the infrastructure. LDAPS communication is encrypted and secure.

In the CloudConnectorCommon.dll config file, make sure you add
                the ADAuthLevel setting to the appSetting node. The values can be 1,
                2, or 3. See this article from Microsoft to learn more about
                  AuthenticationTypes . Here's an example of the setting with a value of
                1:

```
<appSettings>
<add key=”ConnectorServiceURI” value="https://cloudconnector.webex.com/SynchronizationService-v1_0/?orgId=GLOBAL" />
<add key="ADAuthLevel" value="1" />
</appSettings>
```

After the Confirm Organization screen appears, click Confirm .

If you already bound AD DS/AD LDS, the Confirm Organization screen appears.

Click Confirm .

Choose one, depending on the number of Active Directory domains you want to bind to Directory Connector:

- If you have a single domain that is AD LDS , bind to the existing AD LDS source, and then click Confirm .

Because the existing source type is AD DS, you cannot select AD LDS for the new binding.

Because you have more than one domain, the existing source type must be AD DS . If you choose Bind to a new domain and click Next , you cannot select AD LDS for the new binding.

What to do next

After you sign in, you're prompted to perform a dry run synchronization.

#### Directory Connector Dashboard

When you first sign in to Directory Connector, the Dashboard appears. Here you can view a summary of all synchronization activities, view cloud statistics, perform a dry run synchronization, start a full or incremental synchronization and launch the event view to see error information.

If your session times out, sign back in.

You can easily run these tasks from the Actions Toolbar or Actions Menu.

Component

Description

Current Synchronization

Displays the status information about the synchronization that is currently
                underway. When no synchronization is being run, the status display is idle.

Next Synchronization

Displays the next scheduled full and incremental synchronizations. If no schedule
                is set, Not Scheduled is displayed.

Last Synchronization

Displays the status of the last two synchronizations performed.

Current Synchronization Status

Displays the overall status of the synchronization.

Connectors

Displays the current on-premises connectors that are available to the Cloud.

Cloud Statistics

Displays the overall status of the synchronization.

Synchronization Schedule

Displays the synchronization schedule for incremental and full synchronization.

Configuration Summary

All objects will be synchronized

All users will be synchronized

Deleted threshold has been disabled.

Manually start an incremental synchronization

This action is disabled when you pause or disable synchronization, if a full
                  synchronization was not completed, or if a synchronization is in progress.

Sync Dry Run

Perform a dry run synchronization.

Launch Event Viewer

Launch the Microsoft Event Viewer.

Refresh

Refresh the Cisco directory connector dashboard

Action

Description

Start a full synchronization instantly.

Synchronization Mode

Select either incremental or full synchronization mode.

Reset Connector Secret

Establish a conversation between Cisco directory connector and the connector service. Selecting this action will reset the secret in the
                cloud and then saves the secret locally.

Dry Run

Perform a test of the synchronization process. You must do a dry run before you do
                a full synchronization.

Troubleshooting

Turn on/off troubleshooting.

Refresh

Refresh the Cisco directory connector main screen.

Exit

Exit Cisco directory connector.

Key Combination

Action

Alt +A

Show the Actions menu

Alt +A + S

Synchronization now

Alt +A + R

Reset Connector Secret

Alt +A + D

Dry run

Alt +A + S + I

Incremental synchronization

Alt +A + S + F

Full synchronization

Alt + H

Show Help menu

Alt + H + H

Help

Alt + H + A

About

Alt + H + F

FAQ

### Set Automatic Upgrades

From Directory Connector, go to Configuration > General , and then check Automatically upgrade to the new Cisco
                        Directory Connector version .

Click Apply to save your changes.

New versions of the connector are automatically installed when they're available.

You can manually manage upgrades, if you prefer. See Upgrade to the Latest Software Release for more information.

### Choose Active Directory Objects to Synchronize

By default, Directory Connector synchronizes all users that are not computers and all groups that are not
                critical system objects for a domain. For more control over what objects get
                synchronized, you can select specific users to synchronize and specify LDAP filters
                by using the Object Selection page in the Directory Connector.

Groups for Automatic License Assignment

Control Hub allows you to manage license assignments on a per-group basis. You can
                create license templates and map them to Active Directory groups that you
                synchronize to the cloud. At the point of user creation, Webex checks user
                membership and auto license template mapping for that new user.

We recommend that you use an LDAP filter to only sync relevant groups to the cloud.
                For example, you can set the filter to:

(&(cn=Example)(objectclass=Group))*

This filter synchronizes all groups within the base DN where the name starts with
                Example. Users that aren't assigned to groups are assigned licenses from the default
                automatic license template that you configured in Control Hub.

Groups for Hybrid Data Security Deployments

In Directory Connector, you must check Groups if you're using Hybrid Data Security to configure a trial group for pilot users. See the Deployment
                    Guide for Hybrid Data Security for guidance. This Directory Connector setting does not affect other user synchronization in to the cloud.

Before you begin

Active Directory Group Recommendations for Automatic License Assignment

From Directory Connector, go to Configuration , and then click Object Selection .

In the Object Type section, check Users , and consider limiting the number of searchable containers for users.

If you want to synchronize just users in a certain group, for example, you must enter an LDAP filter in the Users LDAP filters field. If you want to sync users that are in the Example-manager group, use a filter like this one:

(&(sAMAccountName=*)(memberOf=cn=Example-manager,ou=Example,ou=Security
                            Group,dc=COMPANY))

Check Identify Room to separate room data from user data. Click Customize if you want to set up additional attributes to identify user data as room data.

Use this setting if you want to synchronize on-premises room information from Active Directory into the Webex cloud. After you synchronize the room information, the on-premises room devices with a configured, mapped SIP address show up as searchable entries on cloud-registered room devices. For more information, see Synchronize On-Premises Room Information to the Webex Cloud .

Check Groups if  you want to synchronize your Active Directory user groups to the cloud.

Do not add a user sync LDAP filter to the Groups field. You should only use the Groups field to sync the group  data itself to the cloud.

By default, groups aren't synchronized for new customers. You must enable group synchronization. You must also synchronize security groups.

Check Contacts if you want to synchronize contact information of users to the cloud.

Directory Connector only synchronizes user contacts when they are objects
                            with the contact object class. User objects can't be
                            added as contacts to Control Hub through this process.

Directory Connector only manages Contacts synchronized by the connector.
                            If there are already contacts in Control Hub, the synchronization
                            doesn't delete the contacts. If contacts are removed from the
                            synchronization scope, the contact information of users would also be removed in Control Hub.

Configure the LDAP filters. You can add extended filters by providing a valid LDAP filter. See this article for more information about configuring LDAP filters.

Specify the On Premises Base DNs to Synchronize by clicking Select to see the tree structure of your Active Directory. From here, you can select or deselect which containers to search on.

Check that the objects you want to add for this configuration, and click Select .

You can select individual or parent containers to use for synchronization. Select a parent container to enable all child containers. If you select a child container, the parent container shows a gray check mark that indicates a child has been checked. You can then click Select to accept the Active Directory containers that you checked.

If your organization places all users and groups in the Users container, you do not have to search other containers. If your organization is divided into organization units, make sure that you select OUs .

Click Apply .

Choose an option:

Apply Config Changes

Dry Run

Cancel

For information on dry runs, see Do a Dry Run Synchronization on Your Active Directory Users .

For group synchronization, you must do a full sync: Do a Full Synchronization of Active Directory Users Into the Cloud .

### Map User Attributes

You can map attributes from your local Active Directory to corresponding attributes in the cloud. The only required field is the *uid, a unique identifier for each user account in the cloud identity service.

You can choose what Active Directory attribute to map to the cloud—for example, you
        can map firstName lastName in Active Directory or a custom attribute
        expression to displayName in the cloud.

Accounts in Active Directory must have an email address; the uid maps by default to the ad field of mail (not sAMAccountName ).

If you choose to have the preferred language come from your Active Directory, then Active Directory is the single source of truth: users won't be able to change their language setting in Webex Settings and administrators won't be able to change the setting in Control Hub.

From Directory Connector, click Configuration , and then choose User Attribute Mapping .

This page shows the attribute names for Active Directory (on the left) and
                        the Webex cloud (on the right). All required attributes are marked with a red
                        asterisk.

Scroll down to the bottom of the Active Directory Attribute Names , and then choose one of these Active Directory attributes to map to the cloud attribute uid :

- mail —Used by most deployments for email format.

- userPrincipalName —An alternative choice if your mail attribute is used for other purposes in Active Directory. This attribute must be in email format.

You can map any of the other Active Directory attributes to uid, but we recommend that you use mail or userPrincipalName, as covered in the guidelines above. In some cases, the userPrincipalName is used for signing in, but a user’s email address is used to manage their calendar. You must ensure the email address for calendar management maps to the primary email address field in Webex. Add the userPrincipalName as an alternative email address. To see what attributes in Active Directory correspond to in the cloud, see Mapping Active Directory Attributes in Directory Connector .

For the synchronization to work, you must make sure the Active Directory attribute that you choose is in email format. Directory Connector shows a pop-up to remind you if you don't choose one of the recommended attributes.

If the predefined Active Directory attributes do not work for your deployment, click the attribute drop-down, scroll to the bottom, and then choose Customize Attribute to open a window that lets you define an attribute expression.

Click Help to get more information about the expressions and see examples of how expressions work. You can also see Expressions for Customized Attributes for more information.

In this example, let's map the Active Directory attributes givenName and Sn to the cloud attribute displayName :

Define the attribute expression as givenName + "" + Sn (the quotes
              being an extra space), and then provide an existing user email to verify.

Click Verify , and see if the result matches what you were expecting.

A successful result looks like this:

If the results are what you expected, click OK to save the new customized attribute.

Later, if you want to change the displayName , you
                can enter a new attribute expression

Directory Connector verifies the attribute value of uid in the identity service and
                            retrieves 3 available users under the current user filter options. If
                            all of these 3 users have a valid email format, Cisco Directory
                            Connector shows the following message:

If the attribute can't be verified, you'll see the following warning and can return to Active Directory to check and fix the user data:

(Optional) Choose mappings for mobile and telephoneNumber if you want mobile and work numbers
                    to appear, for example, in the user's contact card in Webex App.

The phone number data appears in the Webex App when a user hovers over another user's profile picture.

For more information on calling from a user's contact card, see Calling in Webex (Unified CM) Deployment Guide (admins).

Choose additional mappings for more data to appear in the contact card:

- departmentNumber

- displayName

- manager

- title

After the attributes are mapped, the information appears when a user hovers over another user's profile picture:

For more information about the contact card, see Verify Who
                            You're Contacting .

After these attributes are synchronized to each user account, you can also
                        turn on People Insights in Control Hub. This feature allows Webex App users to share more information in their profiles, and learn more about
                        each other. For more information about the feature and how to enable it, see People Insights Profiles for Webex, Jabber, Webex
                            Meetings, and Webex Events (New) in Control Hub

After you make your choices, click Apply .

Any user data that is contained in Active Directory overwrites the data in the cloud that corresponds to that user. For example, if you created a user manually in Control Hub, the user’s email address must be identical to the email in Active Directory. Any user without a corresponding email address in Active Directory is deleted.

Deleted users are kept in the cloud identity service for 7 days before they are permanently deleted.

#### Active Directory and cloud attributes

You can map attributes from your local Active Directory to corresponding attributes in the cloud by using the User Attribute Mapping tab.

This table compares the mapping between the Active Directory Attribute Names and the Cisco Cloud
            Attribute Names. These values and mappings are the default setting in Directory Connector. You can choose different attributes in the Active Directory drop-downs and determine
            which on-premises attribute synchronizes to which cloud attribute.

Think of the drop-down attributes as presets. As an alternative to the values in the Active Directory row, you can also specify a customized attribute, your own preset, in Active Directory (an expression with multiple attributes) to map to a single cloud attribute in the corresponding row. This way, you have the flexibility to determine the display names of your users—for example, you can add an expression that creates a customized attribute based on the employee title, given name, and surname in Active Directory.

You can also specify any of the Active Directory attributes to map to uid in the cloud. However, you must make sure that the on-premises attribute follows a valid email format.

You can also use alternative email addresses, if for example you want to use the userPrincipalName for signing in, but a user’s email address is used to manage their calendar. In this case, map another email address to the emails;type-work attribute. This is the email that is used for authentication; it is not used to manage your calendar. The email address you map from AD must be from a verified domain within your organization, and it must be unique and not assigned to another user.

Active Directory attribute names

Webex cloud attribute names

Notes

—

buildingName

—

c

c

This attribute specifies the user's country abbreviation.

departmentNumber

departmentNumber

This attribute is used for the user's department number that appears
                                in the contact card and people insights .

displayName

displayName

This attribute is used for the user account display name that appears
                                in Control Hub, the contact
                                    card , and people insights .

userAccountControl

ds-pwp-account-disabled

employeeNumber

employeeNumber

—

facsimileTelephoneNumber

facsimileTelephoneNumber

—

—

jabberID

This cloud attribute relates to IM addresses (XMPP type) that are
                                used by Jabber. This value is not the same as sipAddresses.

l

l

This attribute specifies the city of the user.

—

locale

—

manager

manager

This attribute is used for the user's manager name that appears in the contact card and people insights .

mobile

mobile

This attribute is used as the mobile number that appears for calling the user from the contact card .

o

o

This attribute specifies the name of the company or organization and appears in the contact card .

ou

ou

This attribute specifies the name of the organizational unit.

physicalDeliveryOfficeName

physicalDeliveryOfficeName

This attribute specifies the user's office location.

postalCode

postalCode

This attribute specifies the user's postal or zip code for physical
                                mail delivery.

preferredLanguage

preferredLanguage

This attribute sets the user's preferred language and the following
                                formats are supported: xx_YY or xx-YY. Here are a few examples:
                                en_US, en_GB, fr-CA.

If you use an unsupported language or invalid format, users'
                                preferred language will change to the language set for the
                                organization.

MSRTCSIP-PrimaryUserAddress

ipPhone

SipAddresses;type=enterprise

This attribute is used for synchronizing on-premises room information
                                from Active Directory into the Cisco Webex cloud.

sn

sn

This attribute is used for the user account last name that appears in Control Hub, the contact card , and people insights .

st

st

This attribute specifies the state or province of the user.

streetAddress

street

This attribute specifies the street address of the user for physical
                                mail delivery.

telephoneNumber

telephoneNumber

This attribute specifies the user's primary (work) phone number that is used for calling the user from the contact card .

—

timezone

This cloud attribute specifies the user's time zone.

title

title

This attribute specifies the user's title that appears in the contact card and people insights .

type

enterprise

—

*mail

*userPrincipalName

uid

A mandatory attribute mapping. For each user account, the Active
                                Directory value maps to a unique uid in the cloud.

In some cases, the userPrincipalName is used for signing in, but a
                                user’s email address is used to manage their calendar. You must
                                ensure the email address for calendar management maps to the primary
                                email address field in Webex. Add the userPrincipalName as an
                                alternative email address. The user can then use either of these
                                email addresses to sign in, as long as the correct SAML attribute mapping is in place.

See the sample attribute
                                    mapping below for how you might map an alternative email
                                address.

*userPrincipalName

*mail

<custom attribute>

emails;type-work

<New attribute for Azure user objectId>

externalId

Create a new Active Directory attribute to hold the Azure user
                                objectId, so that it does not clash with an existing one.

This attribute then maps to the externalId attribute, ensuring that
                                when Webex users create groups in Microsoft 365
                                    they automatically create teams in Webex .

##### Alternative email address mapping

#### Expressions for Customized Attributes

Operator

Description and Example

%

Removes all characters from the beginning of
                                                  the string to the position of the character or
                                                  string argument, if matched.

-

Strips the back of the input string from the
                                                  end of the specified string.

+

Concatenates input strings or expressions.

|

Evaluates the separated expressions against the
                                                  empty string, and selects the first non-empty
                                                  result.

### Synchronize Directory Avatars From an Active Directory Attribute to the Cloud

You can synchronize your users' directory avatars to the cloud so that each avatar
                appears when they sign in to the Webex App. Use this procedure to synchronize raw avatar data from an Active Directory
                attribute.

From Directory Connector, go to Configuration , click Avatar , and then check Enable .

For Get avatar from , choose AD attribute , and then choose the Avatar attribute that contains the raw avatar data that you want to synchronize to the cloud.

To verify that the avatar is accessed correctly, enter a user's email address and then click Get user's avatar .

The avatar appears to the right.

After you verify that the avatar appeared correctly, click Apply to save your changes.

The images that are synchronized become the default avatar for users in the
                            Webex App. Users are not allowed to set their own avatar after this feature is
                        enabled from Directory Connector.

The user avatars synchronize over to both Webex App and any matching accounts on the Webex site.

What to do next

Do a dry run synchronization; if there are no issues, then do a full synchronization to get your Active Directory user accounts and avatars to synchronize into the cloud and appear in Control Hub.

### Synchronize Directory Avatars From a Resource Server to the Cloud

You can synchronize your users' directory avatars to the cloud so that each avatar
                appears when they sign in to the Webex App. Use this procedure to synchronize avatars from a resource server.

Before you begin

The URI pattern and variable value in this procedure are examples. You must use actual URLs where your directory avatars are located.

The avatar URI pattern and the server where the avatars reside must be
                        reachable from the Directory Connector application. The connector needs http or https access to the images, but
                        the images don't need to be publicly accessible on the internet.

The avatar data synchronization is separated from the Active Directory user profiles. If you run a proxy, you must ensure that avatar data can be accessed by NTLM authentication or basic-auth.

From Directory Connector, go to Configuration , click Avatar , and then check Enable .

For Get avatar from , choose Resource server and then enter the Avatar URI Pattern —For example, http://www.example.com/dir/photo/zoom/{mail: .*?(?=@.*)}.jpg

Let's look at each part of the avatar URI pattern and what they mean:

- http://www.example.com/dir/photo/zoom/ —The path to where all of the photos that will
                        be synced is located. It has to be a URL which the Directory Connector service on your server must be able to reach.

- mail: —Tells Directory Connector to get the value of the mail attribute from Active Directory

.* —Any character, repeating zero or more times.

? —Tells the preceding variable to match as few characters as possible.

(?= ... ) —Matches a group after the main
                                    expression without including it in the result. Directory Connector looks for a match and doesn't include it in the output.

@.* —The at-symbol, followed by any character, repeating zero or more times.

- .jpg —The file extension for your users' avatars. See supported file types in this document and change the extension accordingly.

(Optional) If your resource server requires credentials, check Set user credential for
                        avatar , then either choose Use current service logon
                        user or Use this user and enter the
                    password.

Enter the Variable Value —For example: abcd@example.com .

Click Test to make sure the avatar URI pattern works correctly.

In this example, if the mail value for one AD entry is abcd@example.com and jpg images were being synchronized, the Final Avatar URI is http://www.example.com/dir/photo/zoom/abcd.jpg

After the URI information is verified and looks correct, click Apply .

For detailed information about using regular expressions, see the Microsoft Regular Expression Language Quick Reference .

The images that are synchronized become the default avatar for users in the
                            Webex App. Users are not allowed to set their own avatar after this feature is
                        enabled from Directory Connector.

The user avatars synchronize over to both Webex App and any matching accounts on the Webex site.

What to do next

Do a dry run synchronization; if there are no issues, then do a full synchronization to get your Active Directory user accounts and avatars to synchronize into the cloud and appear in Control Hub.

### Synchronize On-Premises Room Information to the Webex Cloud

Use this procedure to synchronize on-premises room information from Active Directory into the Webex cloud. After you synchronize the room information, the on-premises room devices with a configured, mapped SIP address show up as searchable entries on cloud-registered Webex devices (Room, Desk, and Board).

From Directory Connector, go to Synchronize , click more next to a synchronized domain, click Config , and then choose Object Selection .

Check Sync room information to the cloud to separate the room
          data from the user data during synchronization.

When this setting is disabled, room data is treated the same way as user synchronized
            data.

Go to Attribute Mapping , and then change the attribute mapping
          for the cloud attribute sipAddresses;type=enterprise .

To use value validation, the value of SIP address should be Pattern.compile("^([^@])(.*)@(.*)$")

- Choose MSRTCSIP-PrimaryUserAddress if available.

- If you don't have the above attribute in your Active Directory schema, use another
            field such as ipPhone .

Create a Room Resource mailbox in Exchange. This adds the msExchResourceMetaData;ResourceType:Room attribute which the connector then uses to identify rooms.

From Active Directory users and computers, navigate to and edit properties of the Room. Add the Fully Qualified SIP URI with a prefix of sip:

Do a dry run sync and then a full run sync in the connector.

The new room objects are listed Objects Added and matched room objects appear in Objects Matched in the dry run report. Any room objects flagged for deletion are under Rooms Deleted .

The dry run results show any room resources that were matched.

This setting separates the Active Directory room data (including the room's attribute) from user data. After the synchronization finishes, the cloud statistics on the connector dashboard show room data that was synchronized to the cloud.

What to do next

Now that you've done these steps, when you do a search on a Webex cloud-registered device, you'll see the synchronized room entries that are configured with SIP addresses. When you place a call from the Webex device on that entry, a call is placed to the SIP address that was been configured for the room.

From Control Hub, you can automatically import rooms from your Directory and create workspaces.

The endpoint cannot loop a call back to Webex App. For test dialing devices, these devices must be registered as a SIP URI on-premises or somewhere other than Webex App. If the Active Directory room system that you are searching for is registered to Webex and the same email address is on the Webex Room Device, Desk device, or Webex Board for Calendar Service, then the search results won't show the duplicate entry. The Room, Desk, or Board device is dialed directly in Webex App, and a SIP call is not made.

### Send Email Reports on Directory Synchronization Results

By default, the organization contacts or administrators always receive email notifications. With this setting, you can customize who should receive email notifications that summarize directory synchronization reports.

From Directory Connector, click Settings , and next to Email
            Receiver , toggle on Enable synchronization of
          report .

Click Add Email and then enter an email address.

If you enter an email address with an invalid format, a message pops up telling you to
            correct the issue before you can save and apply the changes.

If you need to edit any email addresses that you entered, double-click the email entry in the left column and then make any changes you need to.

After you added all the valid email addresses, click Save .

What to do next

If you decided that you want to remove email addresses, you can click Remove next to specific email address entries.

### Configure Directory Connector notifications in Control Hub

You can use Notifications in Control Hub to deliver reports from Directory Connector about errors in the
        synchronization process. Control Hub can deliver notifications to various delivery channels
        including email and Webex spaces.

Keep in mind that the notification configuration in Directory Connector doesn't
        automatically migrate to Notifications. Use the following instructions to add the correct email addresses in Notifications to receive notifications from Directory Connector.

Notifications always sends an alert for full synchronizations. Incremental synchronizations will only
          trigger an alert if there is a warning or error in the report.

Sign in to Control Hub and go to Alert Center > Manage .

Click on one of the following:

- General-Cisco Directory Connector Sync Report —This report
            documents errors in the synchronization process.

- General-Cisco Directory Connector State —This report
            documents issues in the Directory Connector status.

Scroll down to the Delivery channel section and select the
          preferred delivery method.

You can receive notification updates over email, in a designated Webex App space, or
            through Webhooks when you have them enabled at the organizational level.

You can add up to 30 email addresses to receive email alerts. Keep in mind that
                  email notifications from Directory Connector won’t change when this feature is
                  enabled from Notifications. Disable notifications in Directory Connector to avoid duplicate alerts for the
                  same event.

You need to have a Messaging license to receive bot updates in a designated Webex
                  space.

Click Save .

### Provision Users From Active Directory Into Control Hub

Follow these steps to provision Active Directory users and create corresponding user
        accounts in Control Hub. You can provision users from a multiple domain Active Directory
        deployment (with either a single forest or multiple forests) after you install a Directory Connector per domain. During the process to onboard users from different domains, you must decide
        whether to retain or delete the user objects which might already exist in the Webex cloud—for example, test accounts from a trial. The goal is to have an exact match between
        your Active Directories and the Webex cloud.

Do a Dry Run Synchronization on Your Active Directory Users

Perform a dry run to compare objects in the on-premises Active Directory and objects in the Webex cloud. A dry run allows you to see what objects will be added, modified, or deleted before you run a full or incremental synchronization and commit the changes to the cloud.

Do a Full Synchronization of Active Directory Users Into the Cloud

When you run a full synchronization, the connector service sends all filtered objects from your Active Directory (AD) to the cloud. The connector service then updates the identity store with your AD entries. If you created an auto-assign license template, you can assign that to the newly synchronized users.

Assign Webex Services to Directory Synchronized Users in Control Hub

After you complete a full user synchronization from Directory Connector in to Control Hub, you can assign Webex service licenses using a variety of methods. We recommend that you set up an auto-assign license template before
                        you use it on new Webex App users that you synchronized from Active Directory. You can also make
                        individual changes after this initial step.

#### Do a Dry Run Synchronization on Your Active Directory
            Users

Perform a dry run to compare objects in the on-premises Active Directory and objects
                in the Webex cloud. A dry run allows you to see what objects will be added, modified, or
                deleted before you run a full or incremental synchronization and commit the changes
                to the cloud.

During the process to onboard users from different domains, you must decide whether
                to retain or delete the user objects which might already exist in the Webex cloud—for example, test accounts from a trial. With Directory Connector, the goal is to have an exact match between your Active Directories and the Webex cloud.

If you have multiple domains in a single forest or multiple forests, you must do this
                step on each of the Cisco directory connector instances you've installed for each Active Directory domain.

Before you begin

You may already have some Webex App users in Control Hub before you used Directory Connector. Among the users in the cloud, some might match on-premises Active Directory
                object and be assigned licenses for services. But some may be test users that you
                want to delete while doing a synchronization. You must create an exact match between
                your Active Directory and Control Hub.

Choose one:

- After first-time sign in, click Yes on the prompt to perform a
                        dry run.

- If you miss a reminder to perform a dry run, at any time from Directory Connector, click Dashboard , choose Sync Dry Run , and then click OK to start a dry run synchronization.

When the dry run completes, you'll see one of the following results:

The Summary contains information about object matching:

Objects Matched - A user who is in Webex Common Identity and
                                also exists in the Active Directory domain i.e., if
                                someuser@cisco.com was synchronized to Webex and displayed in
                                Control Hub and the same user (someuser@cisco.com) exists in Active
                                Directory. This means the user has been matched.

Mismatched Objects - A user who is in Webex, no matter how the
                                user has been added in Common Identity, but the user doesn't exist
                                in Active Directory. It is called a Mismatched Object. For example,
                                if someuser@cisco.com was synchronized in Webex and displayed in
                                Control Hub but the same user (someuser@cisco.com) is not managed by
                                Active Directory, then the report shows the user is mismatched.

The dry run identifies the users by comparing them with domain users. The
                        application can identify the users if they belong to the current domain. In
                        the next step, you must decide whether to delete the objects or retain them.
                        The mismatched objects are identified as already existing in the Webex cloud but not existing in the on-premises Active Directory.

Review the dry run results and then choose an option depending on whether you
                    use a single domain or multiple domains:

- Single domain —Decide whether you want to keep the mismatched users.
                        If you want to keep them, choose No, retain objects ;
                        if you don't, choose Yes, delete objects . After you
                        do these steps and manually run a full sync so that there's an exact match
                        between the premises and cloud, Directory Connector automatically enables scheduled auto sync tasks.

If you keep the users, run a full sync
                            for Domain A first, and then do a dry run for Domain B. If there are
                            still mismatched users, add those users in Active Directory and then do
                            a full sync for Domain B. When there's an exact match between the
                            premises and cloud, Directory Connector automatically enables scheduled auto sync tasks.

In the Confirm Dry Run prompt, click Yes to redo the dry run synchronization and view the
                    dashboard to see the results.

Any accounts that were successfully synchronized in the dry run appear under Objects Matched .

If a user in the cloud doesn't have a corresponding user with the same email
                        in Active Directory, the entry is listed under Users Deleted . To
                        avoid this delete flag, you can add a user in Active Directory with the same
                        email address.

To view the details of the items that were synchronized, click the
                        corresponding tab for specific items or Objects Matched . To save the
                        summary information, click Save Results to File .

If the results are expected, go to Actions > Synchronization mode > Enable Synchronization , and then click Enable Now to do a manual
                    synchronization and put in manual mode at this point.

After doing a synchronization on the last Active Directory domain in your
                            multiple domain deployment, you must enable automatic mode for Directory Connector. You can enable automatic mode only when the objects are completely
                            matched between the Webex cloud and all on-premises Active Directories.

What to do next

For any mismatched user objects that you retained, you must add them to
                        Active Directory so there's an exact match between on-premises and the
                        cloud.

Choose a synchronization type:

Do a Full Synchronization of Active Directory Users Into the Cloud for when you first synchronize new
                                users to the cloud. You do so from Actions > Sync Now > Full , and then users from the current domain are
                                synchronized.

Set the Connector Schedule and Run an Incremental Synchronization after you run a full synchronization
                                and if you want to pick up changes after the initial
                                synchronization. This type of synchronization is recommended to pick
                                up on small changes made to the Active Directory user source.

By default, an incremental synchronization is set to occur every 30
                                minutes (on versions 3.4 and earlier) or every 4 hours (on versions
                                3.5 and later), but you can change this value. The incremental
                                synchronization does not occur until you initially perform a full
                                synchronization.

If you have multiple domains, repeat these steps on any other Directory Connector that you've installed.

Things to Keep in Mind

Perform a dry run before you enable full synchronization, or when you change
                        the synchronization parameters. If the dry run was initiated by a
                        configuration change, you can save the settings after the dry run is
                        complete. If you have already added users manually, performing an Active
                        Directory synchronization may cause previously added users to be removed.
                        You can check the Directory Connector Dry Run Reports to verify that all expected users are present before you
                        fully synchronize to the cloud.

If matched users are marked to be deleted and you're not sure how to proceed,
                        see troubleshooting information and how to contact support in Troubleshooting and Fixes for Directory Connector .

Deleted users are kept in the cloud identity service for 7 days before
                            they are permanently deleted.

#### Do a Full Synchronization of Active Directory Users Into the Cloud

When you run a full synchronization, the connector service sends all filtered objects from your Active Directory (AD) to the cloud. The connector service then updates the identity store with your AD entries. If you created an auto-assign license template, you can assign that to the newly synchronized users.

If you have
                multiple domains, you must do this step on each of the Directory Connector instances you've installed for each Active Directory domain.

Directory Connector synchronizes the user account state—In Active Directory, any users that are
                marked as disabled also appear as inactive in the cloud.

Before you begin

If you want the Webex App user accounts to be in Active status after the full synchronization and before users sign in for the first time, you must do these steps to bypass the email validation:

Integrate Single Sign-On with your Webex organization. See Single Sign-On with Cisco Webex Services
                                        and your Organization's Identity Provider for
                                more information.

Use Control Hub to verify and optionally claim domains contained in the email
                                addresses. See Add,
                                        Verify, and Claim Domains .

Turn activation emails on or off in Control
                                    Hub , so that new users won't receive the automatic email
                                invitation to Webex App. (You can do your own email campaign.)

Activated users who haven't signed in appear with a Verified status in Control Hub. After they sign in, they appear as Active . For more information about user statuses, see User Statuses and Actions in Cisco Webex Control Hub .

When you enable synchronization, Directory Connector asks you to perform a dry run first. We recommend that you do a dry run
                        before a full synchronization to catch any potential errors.

You must set up an auto-assign license template before you use it on new Webex App users that you synchronized from Active Directory.

If you don't use auto-assign license templates, newly synched users automatically get free licenses. They'll be able to use the same free features as those with free accounts.

Choose one:

- After first-time sign in, if the dry run is complete and looks correct for all domains, click Enable Now to allow automatic synchronization to occur.

- From Directory Connector, go to the Dashboard , click Actions , choose Synchronization Mode > Enable Synchronization , and then click Sync Now > Full to start the synchronization.

From Directory Connector, go to Synchronize , click more next to a synchronized domain, click Config , and then choose Full Sync .

Confirm the start of the synchronization.

For any changes that you make to users in Active Directory (for example,
                        display name), Control Hub reflects the change immediately when you refresh the user view, but the
                            Webex App reflects the changes up to 72 hours after you perform the
                        synchronization.

You can try to clear the local cache for the Webex App by following these directions: Windows or Mac .

During the synchronization, the dashboard shows the synchronization progress; this may include the type of synchronization, the time it started, and what phase in which the synchronization is currently running.

After synchronization, the Last Synchronization and Cloud Statistics sections are updated with the new information. User data is synchronized to the cloud.

If errors occur during the synchronization, the status indicator ball turns red.

Click Refresh if you want to update the status of the synchronization. (Synchronized items appear under Cloud Statistics .)

For information about errors, select the Launch Event Viewer from the Actions toolbar to view the error logs.

To set a synchronization schedule for ongoing incremental syncs to the cloud, see Set the Connector Schedule and Run an Incremental Synchronization .

After full synchronization is completed, the status for directory synchronization updates from Disabled to Operational on the Settings page in Control Hub.

When all data is matched between on-premises and cloud, Directory Connector changes from manual mode to automatic synchronization mode.

Unless you integrate single sign-on , verify domains, and optionally claim domains for the email accounts that you synchronized , and suppress automated emails , the Webex App user accounts remain in a Not Verified state until users sign in to Webex App for the first time to confirm their accounts. See the Before You Begin section for guidance on how to synchronize the accounts as Active users.

If you have multiple domains, do this step on any other Directory Connector that you've installed. After synchronization, the users on all domains
                        you added are listed in Control Hub.

If you integrated Single Sign-On with Webex and suppressed email notifications , the email invitations are not sent out to the newly synchronized users.

You cannot manually add users in Control Hub after the Directory Connector is enabled. Once enabled, user management is performed from Cisco directory connector and Active Directory is the single source of truth.

Any groups that you synchronized appear in Control Hub and you can assign a
                        license template so that users in that group are assigned licenses.

What to do next

When you remove a user from Active Directory, the user is soft-deleted after the next synchronization. The user becomes Inactive but the cloud identity profile is kept for seven days (to allow for recovery from accidental deletion).

When you check Account is disabled in Active Directory, the user becomes Inactive after the next synchronization. The cloud identity profile is not deleted after seven days, in case you want to enable the user again.

Note these exceptions to an incremental synchronization (follow the full synchronization steps above instead):

In the case of an updated avatar but no other attribute change, incremental sync won't update the user's avatar to the cloud.

Configuration changes on attribute mapping, base DN, filter, and avatar setting require a full synchronization.

#### Assign Webex Services to Directory Synchronized Users in Control Hub

After you complete a full user synchronization from Cisco directory connector in to Control Hub, you can use Control Hub to assign the same Webex service licenses to all of your users at once or add additional licenses to new users if you already configured an auto-assigned license template. You can make individual user account changes after this initial step.

After you complete a full user synchronization from Directory Connector in to Control Hub, you can use methods in Control Hub to globally assign Webex service licenses to all of your users, individual users, through the bulk CSV template, or automatically to new users if you already configured an auto-assign license template. You can make individual user account changes after this initial step.

When you assign a license to a Webex App user, that user receives an email confirming the assignment, by default. The email is sent by a notification service in Control Hub. If you integrated Single Sign-On (SSO) with your Webex organization, you can also suppress these automatic email notifications if you prefer to contact your users directly.

Before you begin

You must set up an auto-assign license template before you use it on new Webex App users that you synchronized from Active Directory.

Do a dry run synchronization on your Active Directory users.

After confirming the results of the dry run, do a full synchronization on your Active Directory users.

At the time of full synchronization, the user is created in the cloud, no service assignments are added, and no activation email is sent. If emails aren't suppressed, the new users receive an activation email when you assign services to users by a standard user management method in Control Hub, such as CSV import, manual user update, or through successful auto-assignment completion.

From the customer view in https://admin.webex.com , go to Management > Users , click Manage
                                                  Users , choose Modify all
                                                  synchronized users , and then click Next .

Choose an option:

- Edit Service
                                                  Licenses in Control Hub for Individual
                                                  Users —Modify users manually.

Modify Users in
                                                  Control Hub with the CSV Template —Modify
                                                  users in bulk.

What to do next

If emails aren't suppressed, an email is sent to each user with an invite to join and download Webex.

If you selected the same Webex services for all of your users, afterwards you can change license assigned individually or in bulk.

Ways to Add and Manage Users in Your Organization

### Known Issues with Directory Connector

Windows Server versions prior to 2012 R2 have a cookie
                                                issue that affects Directory Connector. This issue is fixed in versions 2012 R2 and 2016 .

For any changes that you make to users in Active
                                                Directory (for example, display name), Control Hub reflects the change immediately when you refresh
                                                the user view, but the Webex App reflects the changes 72 hours from when you
                                                perform the synchronization.

You can try to clear the local cache for the Webex App by following these directions: Windows or Mac .

When a user uses Webex App on desktop or mobile to search and call a Room
                                                that only has a synchronized SIP URI, then the call
                                                rings indefinitely at this time.

| 1 | Install Directory Connector Control Hub initially shows directory synchronization as disabled. To turn on
                        directory synchronization for your organization, you must install and
                        configure Directory Connector, and then successfully perform a full synchronization. For a new
                        installation of Directory Connector, always go to Control Hub ( https://admin.webex.com ) to get the latest version of the software so that you're using the
                        latest features and bug fixes. After you install the software, upgrades are
                        reported through the software and automatically install when available. |
|---|---|
| 2 | Sign In To Directory Connector Sign in with your Webex administrator credentials and perform the initial setup. |
| 3 | Set Automatic Upgrades It's always important to keep your Directory Connector software up to date to the latest version. We recommend that you use this
                        procedure to allow automatic upgrades to the software to be installed
                        silently when they're available. |
| 4 | Choose Active Directory Objects to Synchronize By default, Directory Connector synchronizes all users that are not computers and all groups that are not
                        critical system objects for a domain. For more control over what objects get
                        synchronized, you can select specific users to synchronize and specify LDAP
                        filters by using the Object Selection page in the Directory Connector. |
| 5 | Map User Attributes You can map attributes from your local Active Directory to corresponding attributes in the cloud. The only required field is the *uid. |
| 6 | Synchronize directory avatars by using one of the following procedures: Synchronize Directory Avatars From an Active Directory Attribute to the Cloud Synchronize Directory Avatars From a Resource Server to the Cloud You can synchronize your users' avatars to the cloud so that each user's avatar appears when they sign in to the application. You can sychronize avatars from an Active Directory attribute or a resource server. |
| 7 | Synchronize On-Premises Room Information to the Webex Cloud Use this procedure to synchronize on-premises room information from Active Directory into the Webex cloud. After you synchronize the room information, the on-premises room devices with a configured, mapped SIP address show up as searchable entries on cloud-registered room devices, such as a Webex Room Device or Cisco Webex Board |
| 8 | To Provision Users From Active Directory Into Control Hub , perform these steps: Do a Dry Run Synchronization on Your Active Directory Users Do a Full Synchronization of Active Directory Users Into the Cloud Assign Webex Services to Directory Synchronized Users in Control Hub Follow this sequence to provision Active Directory users for Webex App accounts.You can provision users from a multiple forest or multiple
                        domain Active Directory deployment for Directory Connector 3.0 and later. During the process to onboard users from different
                        domains, you must decide whether to retain or delete the user objects which
                        might already exist in the Webex cloud—for example, test accounts from a trial. The goal is to have an
                        exact match between your Active Directories and the Webex cloud. |

| 1 | In Control
            Hub , go to Users > Manage Users > Enable Directory Synchronization , and choose Next . |
|---|---|
| 2 | Click the Download and Install link to save the latest version of the connector installation .zip file to your VMware or Windows server. You can obtain the .zip file directly from this link , but you must have full administrative access to a Control Hub organization for this software to work. For a new installation, get the latest version of the software so that you're using the latest features and bug fixes. After you install the software, upgrades are reported through the software and automatically install when available. |
| 3 | On the VMware or Windows server, unzip and run the .msi file in the setup folder to launch the setup wizard. |
| 4 | Click Next , check the box to accept the license agreement, and then click Next until you see the account type screen. |
| 5 | Choose the type of service account that you want to use and perform the installation with an admin account: Local System —The default option. You can use this option if you have a proxy configured through Internet Explorer. Domain Account —Use this option if the computer is part of the domain. Directory Connector must interact with network services to access domain resources. You can enter the account information and click OK . When entering the Username , use the format {domain}\{user_name} For a proxy that integrates with AD (NTLMv2 or Kerberos), you must use the domain account option. The account used to run Directory Connector Service must have enough privilege to pass proxy and access AD. To avoid errors, make sure the following privileges are in place: The server is part of the domain The domain account can access the on-premises AD data and avatars data. The account must also have the local Administrator Role, because it must access access files under C:\Program Files . For a Virtual Machine login, the admin account privilege must at least be able to read domain information. |
| 6 | Click Install . After the network test runs and if prompted, enter your proxy basic credentials, click OK , and then click Finish . |

| 1 | Open the connector, and then add https://idbroker.webex.com to your list of trusted sites if
                    you see a prompt. |
|---|---|
| 2 | If prompted, sign in in with your proxy authentication credentials, and then sign in to Webex using your admin account and click Next . |
| 3 | Confirm your organization and domain. If you choose AD DS , check LDAP over SSL to use the secure LDAP (LDAPS) as the connection protocol, choose the domain that you want to synchronize from, and then click Confirm . If you don't check LDAP over SSL , DirSync will continue to
                use the LDAP connection protocol. LDAP (Lightweight Directory Application Protocol) and Secure LDAP (LDAPS) are the connection protocols used between an application and the Domain Controller within the infrastructure. LDAPS communication is encrypted and secure. If you choose AD LDS , enter the host, domain, and port and then click Refresh to load all application partitions. Then select the partition from the drop-down list and click Confirm . See the AD LDS section for more information. In the CloudConnectorCommon.dll config file, make sure you add
                the ADAuthLevel setting to the appSetting node. The values can be 1,
                2, or 3. See this article from Microsoft to learn more about
                  AuthenticationTypes . Here's an example of the setting with a value of
                1: <appSettings>
<add key=”ConnectorServiceURI” value="https://cloudconnector.webex.com/SynchronizationService-v1_0/?orgId=GLOBAL" />
<add key="ADAuthLevel" value="1" />
</appSettings> |
| 4 | After the Confirm Organization screen appears, click Confirm . If you already bound AD DS/AD LDS, the Confirm Organization screen appears. |
| 5 | Click Confirm . |
| 6 | Choose one, depending on the number of Active Directory domains you want to bind to Directory Connector: If you have a single domain that is AD LDS , bind to the existing AD LDS source, and then click Confirm . If you have a single domain that is AD DS , either bind to the existing domain or to a new domain. If you choose Bind to a new domain , click Next . Because the existing source type is AD DS, you cannot select AD LDS for the new binding. If you have more than one domain, choose an existing domain from the list or Bind to a new domain and then click Next . Because you have more than one domain, the existing source type must be AD DS . If you choose Bind to a new domain and click Next , you cannot select AD LDS for the new binding. |

| Component | Description |
|---|---|
| Current Synchronization | Displays the status information about the synchronization that is currently
                underway. When no synchronization is being run, the status display is idle. |
| Next Synchronization | Displays the next scheduled full and incremental synchronizations. If no schedule
                is set, Not Scheduled is displayed. |
| Last Synchronization | Displays the status of the last two synchronizations performed. |
| Current Synchronization Status | Displays the overall status of the synchronization. |
| Connectors | Displays the current on-premises connectors that are available to the Cloud. |
| Cloud Statistics | Displays the overall status of the synchronization. |
| Synchronization Schedule | Displays the synchronization schedule for incremental and full synchronization. |
| Configuration Summary | Lists the settings that you changed in the configuration. For example, the
              summary might include the following: All objects will be synchronized All users will be synchronized Deleted threshold has been disabled. |

| Action | Description |
|---|---|
| Start incremental sync | Manually start an incremental synchronization This action is disabled when you pause or disable synchronization, if a full
                  synchronization was not completed, or if a synchronization is in progress. |
| Sync Dry Run | Perform a dry run synchronization. |
| Launch Event Viewer | Launch the Microsoft Event Viewer. |
| Refresh | Refresh the Cisco directory connector dashboard |

| Action | Description |
|---|---|
| Sync Now | Start a full synchronization instantly. |
| Synchronization Mode | Select either incremental or full synchronization mode. |
| Reset Connector Secret | Establish a conversation between Cisco directory connector and the connector service. Selecting this action will reset the secret in the
                cloud and then saves the secret locally. |
| Dry Run | Perform a test of the synchronization process. You must do a dry run before you do
                a full synchronization. |
| Troubleshooting | Turn on/off troubleshooting. |
| Refresh | Refresh the Cisco directory connector main screen. |
| Exit | Exit Cisco directory connector. |

| Key Combination | Action |
|---|---|
| Alt +A | Show the Actions menu |
| Alt +A + S | Synchronization now |
| Alt +A + R | Reset Connector Secret |
| Alt +A + D | Dry run |
| Alt +A + S + I | Incremental synchronization |
| Alt +A + S + F | Full synchronization |
| Alt + H | Show Help menu |
| Alt + H + H | Help |
| Alt + H + A | About |
| Alt + H + F | FAQ |

| 1 | From Directory Connector, go to Configuration > General , and then check Automatically upgrade to the new Cisco
                        Directory Connector version . |
|---|---|
| 2 | Click Apply to save your changes. |

| 1 | From Directory Connector, go to Configuration , and then click Object Selection . |
|---|---|
| 2 | In the Object Type section, check Users , and consider limiting the number of searchable containers for users. If you want to synchronize just users in a certain group, for example, you must enter an LDAP filter in the Users LDAP filters field. If you want to sync users that are in the Example-manager group, use a filter like this one: (&(sAMAccountName=*)(memberOf=cn=Example-manager,ou=Example,ou=Security
                            Group,dc=COMPANY)) |
| 3 | Check Identify Room to separate room data from user data. Click Customize if you want to set up additional attributes to identify user data as room data. Use this setting if you want to synchronize on-premises room information from Active Directory into the Webex cloud. After you synchronize the room information, the on-premises room devices with a configured, mapped SIP address show up as searchable entries on cloud-registered room devices. For more information, see Synchronize On-Premises Room Information to the Webex Cloud . |
| 4 | Check Groups if  you want to synchronize your Active Directory user groups to the cloud. Do not add a user sync LDAP filter to the Groups field. You should only use the Groups field to sync the group  data itself to the cloud. By default, groups aren't synchronized for new customers. You must enable group synchronization. You must also synchronize security groups. |
| 5 | Check Contacts if you want to synchronize contact information of users to the cloud. Directory Connector only synchronizes user contacts when they are objects
                            with the contact object class. User objects can't be
                            added as contacts to Control Hub through this process. Directory Connector only manages Contacts synchronized by the connector.
                            If there are already contacts in Control Hub, the synchronization
                            doesn't delete the contacts. If contacts are removed from the
                            synchronization scope, the contact information of users would also be removed in Control Hub. |
| 6 | Configure the LDAP filters. You can add extended filters by providing a valid LDAP filter. See this article for more information about configuring LDAP filters. |
| 7 | Specify the On Premises Base DNs to Synchronize by clicking Select to see the tree structure of your Active Directory. From here, you can select or deselect which containers to search on. |
| 8 | Check that the objects you want to add for this configuration, and click Select . You can select individual or parent containers to use for synchronization. Select a parent container to enable all child containers. If you select a child container, the parent container shows a gray check mark that indicates a child has been checked. You can then click Select to accept the Active Directory containers that you checked. If your organization places all users and groups in the Users container, you do not have to search other containers. If your organization is divided into organization units, make sure that you select OUs . |
| 9 | Click Apply . Choose an option: Apply Config Changes Dry Run Cancel For information on dry runs, see Do a Dry Run Synchronization on Your Active Directory Users . For group synchronization, you must do a full sync: Do a Full Synchronization of Active Directory Users Into the Cloud . |

| 1 | From Directory Connector, click Configuration , and then choose User Attribute Mapping . This page shows the attribute names for Active Directory (on the left) and
                        the Webex cloud (on the right). All required attributes are marked with a red
                        asterisk. |
|---|---|
| 2 | Scroll down to the bottom of the Active Directory Attribute Names , and then choose one of these Active Directory attributes to map to the cloud attribute uid : mail —Used by most deployments for email format. userPrincipalName —An alternative choice if your mail attribute is used for other purposes in Active Directory. This attribute must be in email format. You can map any of the other Active Directory attributes to uid, but we recommend that you use mail or userPrincipalName, as covered in the guidelines above. In some cases, the userPrincipalName is used for signing in, but a user’s email address is used to manage their calendar. You must ensure the email address for calendar management maps to the primary email address field in Webex. Add the userPrincipalName as an alternative email address. To see what attributes in Active Directory correspond to in the cloud, see Mapping Active Directory Attributes in Directory Connector . For the synchronization to work, you must make sure the Active Directory attribute that you choose is in email format. Directory Connector shows a pop-up to remind you if you don't choose one of the recommended attributes. |
| 3 | If the predefined Active Directory attributes do not work for your deployment, click the attribute drop-down, scroll to the bottom, and then choose Customize Attribute to open a window that lets you define an attribute expression. Click Help to get more information about the expressions and see examples of how expressions work. You can also see Expressions for Customized Attributes for more information. In this example, let's map the Active Directory attributes givenName and Sn to the cloud attribute displayName : Define the attribute expression as givenName + "" + Sn (the quotes
              being an extra space), and then provide an existing user email to verify. Click Verify , and see if the result matches what you were expecting. A successful result looks like this: If the results are what you expected, click OK to save the new customized attribute. Later, if you want to change the displayName , you
                can enter a new attribute expression Directory Connector verifies the attribute value of uid in the identity service and
                            retrieves 3 available users under the current user filter options. If
                            all of these 3 users have a valid email format, Cisco Directory
                            Connector shows the following message: If the attribute can't be verified, you'll see the following warning and can return to Active Directory to check and fix the user data: |
| 4 | (Optional) Choose mappings for mobile and telephoneNumber if you want mobile and work numbers
                    to appear, for example, in the user's contact card in Webex App. The phone number data appears in the Webex App when a user hovers over another user's profile picture. For more information on calling from a user's contact card, see Calling in Webex (Unified CM) Deployment Guide (admins). |
| 5 | Choose additional mappings for more data to appear in the contact card: departmentNumber displayName manager title After the attributes are mapped, the information appears when a user hovers over another user's profile picture: For more information about the contact card, see Verify Who
                            You're Contacting . After these attributes are synchronized to each user account, you can also
                        turn on People Insights in Control Hub. This feature allows Webex App users to share more information in their profiles, and learn more about
                        each other. For more information about the feature and how to enable it, see People Insights Profiles for Webex, Jabber, Webex
                            Meetings, and Webex Events (New) in Control Hub |
| 6 | After you make your choices, click Apply . |

| Active Directory attribute names | Webex cloud attribute names | Notes |
|---|---|---|
| — | buildingName | — |
| c | c | This attribute specifies the user's country abbreviation. |
| departmentNumber | departmentNumber | This attribute is used for the user's department number that appears
                                in the contact card and people insights . |
| displayName | displayName | This attribute is used for the user account display name that appears
                                in Control Hub, the contact
                                    card , and people insights . |
| userAccountControl | ds-pwp-account-disabled | This attribute is used for user synchronization. Make sure the userAccountControl attribute is mapped to ds-pwp-account-disabled or users won’t be synced
                            properly. |
| employeeNumber | employeeNumber | — |
| facsimileTelephoneNumber | facsimileTelephoneNumber | — |
| — | jabberID | This cloud attribute relates to IM addresses (XMPP type) that are
                                used by Jabber. This value is not the same as sipAddresses. |
| l | l | This attribute specifies the city of the user. |
| — | locale | — |
| manager | manager | This attribute is used for the user's manager name that appears in the contact card and people insights . |
| mobile | mobile | This attribute is used as the mobile number that appears for calling the user from the contact card . |
| o | o | This attribute specifies the name of the company or organization and appears in the contact card . |
| ou | ou | This attribute specifies the name of the organizational unit. |
| physicalDeliveryOfficeName | physicalDeliveryOfficeName | This attribute specifies the user's office location. |
| postalCode | postalCode | This attribute specifies the user's postal or zip code for physical
                                mail delivery. |
| preferredLanguage | preferredLanguage | This attribute sets the user's preferred language and the following
                                formats are supported: xx_YY or xx-YY. Here are a few examples:
                                en_US, en_GB, fr-CA. If you use an unsupported language or invalid format, users'
                                preferred language will change to the language set for the
                                organization. |
| MSRTCSIP-PrimaryUserAddress ipPhone | SipAddresses;type=enterprise | This attribute is used for synchronizing on-premises room information
                                from Active Directory into the Cisco Webex cloud. |
| sn | sn | This attribute is used for the user account last name that appears in Control Hub, the contact card , and people insights . |
| st | st | This attribute specifies the state or province of the user. |
| streetAddress | street | This attribute specifies the street address of the user for physical
                                mail delivery. |
| telephoneNumber | telephoneNumber | This attribute specifies the user's primary (work) phone number that is used for calling the user from the contact card . |
| — | timezone | This cloud attribute specifies the user's time zone. |
| title | title | This attribute specifies the user's title that appears in the contact card and people insights . |
| type | enterprise | — |
| *mail *userPrincipalName | uid | A mandatory attribute mapping. For each user account, the Active
                                Directory value maps to a unique uid in the cloud. In some cases, the userPrincipalName is used for signing in, but a
                                user’s email address is used to manage their calendar. You must
                                ensure the email address for calendar management maps to the primary
                                email address field in Webex. Add the userPrincipalName as an
                                alternative email address. The user can then use either of these
                                email addresses to sign in, as long as the correct SAML attribute mapping is in place. See the sample attribute
                                    mapping below for how you might map an alternative email
                                address. |
| *userPrincipalName *mail <custom attribute> | emails;type-work | This mapping is optional, use it if you want to use alternative email
                            addresses. This is the email that is used for authentication; it is not
                            used to manage your calendar. The email address you map from AD must be
                            from a verified domain within your organization, and it must be unique
                            and not assigned to another user. |
| <New attribute for Azure user objectId> | externalId | Create a new Active Directory attribute to hold the Azure user
                                objectId, so that it does not clash with an existing one. This attribute then maps to the externalId attribute, ensuring that
                                when Webex users create groups in Microsoft 365
                                    they automatically create teams in Webex . |

| Operator | Description and Example |
|---|---|
| % | Removes all characters from the beginning of
                                                  the string to the position of the character or
                                                  string argument, if matched. Example Expression "abc@example.com" % "@" Result example.com |
| - | Strips the back of the input string from the
                                                  end of the specified string. Example Expression "abc@example.com" - "@" Result abc |
| + | Concatenates input strings or expressions. Example Expression "abc" + "" + "def" Result abc def |
| \| | Evaluates the separated expressions against the
                                                  empty string, and selects the first non-empty
                                                  result. Example Expression "" \| "abc" Result abc |

| 1 | From Directory Connector, go to Configuration , click Avatar , and then check Enable . |
|---|---|
| 2 | For Get avatar from , choose AD attribute , and then choose the Avatar attribute that contains the raw avatar data that you want to synchronize to the cloud. |
| 3 | To verify that the avatar is accessed correctly, enter a user's email address and then click Get user's avatar . The avatar appears to the right. |
| 4 | After you verify that the avatar appeared correctly, click Apply to save your changes. |

| 1 | From Directory Connector, go to Configuration , click Avatar , and then check Enable . |
|---|---|
| 2 | For Get avatar from , choose Resource server and then enter the Avatar URI Pattern —For example, http://www.example.com/dir/photo/zoom/{mail: .*?(?=@.*)}.jpg Let's look at each part of the avatar URI pattern and what they mean: http://www.example.com/dir/photo/zoom/ —The path to where all of the photos that will
                        be synced is located. It has to be a URL which the Directory Connector service on your server must be able to reach. mail: —Tells Directory Connector to get the value of the mail attribute from Active Directory .*?(?=@.*) —A regex syntax that performs these functions: .* —Any character, repeating zero or more times. ? —Tells the preceding variable to match as few characters as possible. (?= ... ) —Matches a group after the main
                                    expression without including it in the result. Directory Connector looks for a match and doesn't include it in the output. @.* —The at-symbol, followed by any character, repeating zero or more times. .jpg —The file extension for your users' avatars. See supported file types in this document and change the extension accordingly. |
| 3 | (Optional) If your resource server requires credentials, check Set user credential for
                        avatar , then either choose Use current service logon
                        user or Use this user and enter the
                    password. |
| 4 | Enter the Variable Value —For example: abcd@example.com . |
| 5 | Click Test to make sure the avatar URI pattern works correctly. In this example, if the mail value for one AD entry is abcd@example.com and jpg images were being synchronized, the Final Avatar URI is http://www.example.com/dir/photo/zoom/abcd.jpg |
| 6 | After the URI information is verified and looks correct, click Apply . For detailed information about using regular expressions, see the Microsoft Regular Expression Language Quick Reference . |

| 1 | From Directory Connector, go to Synchronize , click more next to a synchronized domain, click Config , and then choose Object Selection . |
|---|---|
| 2 | Check Sync room information to the cloud to separate the room
          data from the user data during synchronization. When this setting is disabled, room data is treated the same way as user synchronized
            data. |
| 3 | Go to Attribute Mapping , and then change the attribute mapping
          for the cloud attribute sipAddresses;type=enterprise . To use value validation, the value of SIP address should be Pattern.compile("^([^@])(.*)@(.*)$") Choose MSRTCSIP-PrimaryUserAddress if available. If you don't have the above attribute in your Active Directory schema, use another
            field such as ipPhone . |
| 4 | Create a Room Resource mailbox in Exchange. This adds the msExchResourceMetaData;ResourceType:Room attribute which the connector then uses to identify rooms. |
| 5 | From Active Directory users and computers, navigate to and edit properties of the Room. Add the Fully Qualified SIP URI with a prefix of sip: |
| 6 | Do a dry run sync and then a full run sync in the connector. The new room objects are listed Objects Added and matched room objects appear in Objects Matched in the dry run report. Any room objects flagged for deletion are under Rooms Deleted . The dry run results show any room resources that were matched. This setting separates the Active Directory room data (including the room's attribute) from user data. After the synchronization finishes, the cloud statistics on the connector dashboard show room data that was synchronized to the cloud. |

| 1 | From Directory Connector, click Settings , and next to Email
            Receiver , toggle on Enable synchronization of
          report . |
|---|---|
| 2 | Click Add Email and then enter an email address. If you enter an email address with an invalid format, a message pops up telling you to
            correct the issue before you can save and apply the changes. |
| 3 | If you need to edit any email addresses that you entered, double-click the email entry in the left column and then make any changes you need to. |
| 4 | After you added all the valid email addresses, click Save . |

| 1 | Sign in to Control Hub and go to Alert Center > Manage . |
|---|---|
| 2 | Click on one of the following: General-Cisco Directory Connector Sync Report —This report
            documents errors in the synchronization process. General-Cisco Directory Connector State —This report
            documents issues in the Directory Connector status. |
| 3 | Scroll down to the Delivery channel section and select the
          preferred delivery method. You can receive notification updates over email, in a designated Webex App space, or
            through Webhooks when you have them enabled at the organizational level. You can add up to 30 email addresses to receive email alerts. Keep in mind that
                  email notifications from Directory Connector won’t change when this feature is
                  enabled from Notifications. Disable notifications in Directory Connector to avoid duplicate alerts for the
                  same event. You need to have a Messaging license to receive bot updates in a designated Webex
                  space. |
| 4 | Click Save . |

| 1 | Do a Dry Run Synchronization on Your Active Directory Users Perform a dry run to compare objects in the on-premises Active Directory and objects in the Webex cloud. A dry run allows you to see what objects will be added, modified, or deleted before you run a full or incremental synchronization and commit the changes to the cloud. |
|---|---|
| 2 | Do a Full Synchronization of Active Directory Users Into the Cloud When you run a full synchronization, the connector service sends all filtered objects from your Active Directory (AD) to the cloud. The connector service then updates the identity store with your AD entries. If you created an auto-assign license template, you can assign that to the newly synchronized users. |
| 3 | Assign Webex Services to Directory Synchronized Users in Control Hub After you complete a full user synchronization from Directory Connector in to Control Hub, you can assign Webex service licenses using a variety of methods. We recommend that you set up an auto-assign license template before
                        you use it on new Webex App users that you synchronized from Active Directory. You can also make
                        individual changes after this initial step. |

| 1 | Choose one: After first-time sign in, click Yes on the prompt to perform a
                        dry run. If you miss a reminder to perform a dry run, at any time from Directory Connector, click Dashboard , choose Sync Dry Run , and then click OK to start a dry run synchronization. When the dry run completes, you'll see one of the following results: Detected Mismatched Objects in Directory Connector Summary of Dry Run Report Results and Mismatched Objects in
                                        Directory Connector The Summary contains information about object matching: Objects Matched - A user who is in Webex Common Identity and
                                also exists in the Active Directory domain i.e., if
                                someuser@cisco.com was synchronized to Webex and displayed in
                                Control Hub and the same user (someuser@cisco.com) exists in Active
                                Directory. This means the user has been matched. Mismatched Objects - A user who is in Webex, no matter how the
                                user has been added in Common Identity, but the user doesn't exist
                                in Active Directory. It is called a Mismatched Object. For example,
                                if someuser@cisco.com was synchronized in Webex and displayed in
                                Control Hub but the same user (someuser@cisco.com) is not managed by
                                Active Directory, then the report shows the user is mismatched. The dry run identifies the users by comparing them with domain users. The
                        application can identify the users if they belong to the current domain. In
                        the next step, you must decide whether to delete the objects or retain them.
                        The mismatched objects are identified as already existing in the Webex cloud but not existing in the on-premises Active Directory. |
|---|---|
| 2 | Review the dry run results and then choose an option depending on whether you
                    use a single domain or multiple domains: Single domain —Decide whether you want to keep the mismatched users.
                        If you want to keep them, choose No, retain objects ;
                        if you don't, choose Yes, delete objects . After you
                        do these steps and manually run a full sync so that there's an exact match
                        between the premises and cloud, Directory Connector automatically enables scheduled auto sync tasks. Multiple domains —For an organization with Domain A and Domain B,
                        first do a dry run for Domain A. If you want to keep mismatched users,
                        choose No, retain objects . (These mismatched users
                        might be members of Domain B.) If you want to delete, choose Yes,
                            delete objects . If you keep the users, run a full sync
                            for Domain A first, and then do a dry run for Domain B. If there are
                            still mismatched users, add those users in Active Directory and then do
                            a full sync for Domain B. When there's an exact match between the
                            premises and cloud, Directory Connector automatically enables scheduled auto sync tasks. |
| 3 | In the Confirm Dry Run prompt, click Yes to redo the dry run synchronization and view the
                    dashboard to see the results. Any accounts that were successfully synchronized in the dry run appear under Objects Matched . If a user in the cloud doesn't have a corresponding user with the same email
                        in Active Directory, the entry is listed under Users Deleted . To
                        avoid this delete flag, you can add a user in Active Directory with the same
                        email address. To view the details of the items that were synchronized, click the
                        corresponding tab for specific items or Objects Matched . To save the
                        summary information, click Save Results to File . |
| 4 | If the results are expected, go to Actions > Synchronization mode > Enable Synchronization , and then click Enable Now to do a manual
                    synchronization and put in manual mode at this point. After doing a synchronization on the last Active Directory domain in your
                            multiple domain deployment, you must enable automatic mode for Directory Connector. You can enable automatic mode only when the objects are completely
                            matched between the Webex cloud and all on-premises Active Directories. |

| 1 | Choose one: After first-time sign in, if the dry run is complete and looks correct for all domains, click Enable Now to allow automatic synchronization to occur. From Directory Connector, go to the Dashboard , click Actions , choose Synchronization Mode > Enable Synchronization , and then click Sync Now > Full to start the synchronization. |
|---|---|
| 2 | From Directory Connector, go to Synchronize , click more next to a synchronized domain, click Config , and then choose Full Sync . |
| 3 | Confirm the start of the synchronization. For any changes that you make to users in Active Directory (for example,
                        display name), Control Hub reflects the change immediately when you refresh the user view, but the
                            Webex App reflects the changes up to 72 hours after you perform the
                        synchronization. You can try to clear the local cache for the Webex App by following these directions: Windows or Mac . During the synchronization, the dashboard shows the synchronization progress; this may include the type of synchronization, the time it started, and what phase in which the synchronization is currently running. After synchronization, the Last Synchronization and Cloud Statistics sections are updated with the new information. User data is synchronized to the cloud. If errors occur during the synchronization, the status indicator ball turns red. |
| 4 | Click Refresh if you want to update the status of the synchronization. (Synchronized items appear under Cloud Statistics .) |
| 5 | For information about errors, select the Launch Event Viewer from the Actions toolbar to view the error logs. |
| 6 | To set a synchronization schedule for ongoing incremental syncs to the cloud, see Set the Connector Schedule and Run an Incremental Synchronization . |

| 1 | From the customer view in https://admin.webex.com , go to Management > Users , click Manage
                                                  Users , choose Modify all
                                                  synchronized users , and then click Next . |
|---|---|
| 2 | Choose an option: Edit Service
                                                  Licenses in Control Hub for Individual
                                                  Users —Modify users manually. Modify Users in
                                                  Control Hub with the CSV Template —Modify
                                                  users in bulk. |