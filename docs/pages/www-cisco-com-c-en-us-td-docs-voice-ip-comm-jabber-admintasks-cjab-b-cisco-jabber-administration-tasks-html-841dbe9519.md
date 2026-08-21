---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-admintasks-cjab-b-cisco-jabber-administration-tasks-html-841dbe9519
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/admintasks/cjab_b_cisco-jabber-administration-tasks.html
retrieved_at: 2026-08-21T06:59:33.250861+00:00
---

Cisco Jabber Administration Tasks

# Cisco Jabber Administration Tasks

### Download Options

Updated: April 16, 2024

First Published: April 4, 2024

Last Updated: April 16, 2024

# Cisco Jabber Administration Tasks

## Cisco Jabber Administration Tasks Overview

This document contains administrative tasks related to Cisco Jabber.

This document contains the following sections:

Calls : Information related to calling.

Chat : Information related to chat.

Customizations : Information related to customizations.

Integrations : Information related to Jabber integrations with other producrs.

Migrations : Information related to the migration of Jabber users to Webex.

### Mobile application management license agreement

Mobile application management currently isn't supported for Webex Meetings Online customers.

The Mobile Application Management (MAM) wrapper program's focus is to make IPA and APK files available to customers outside
                              of app stores for MAM integration purposes. This program is provided free of charge (normal Jabber and Webex licensing costs do apply).

Cisco doesn't test any MAM wrappers or SDK integrations with Jabber or Webex , and only supports the unwrapped (latest released) version of Jabber and Webex . Any issues that customers find with the modified versions of Jabber or Webex must be reproduced with the unwrapped versions before submitting a Cisco support case.

While others may test their integrations with Cisco applications, Cisco cannot make any support statement around those integrations.

Integrations may sandbox applications, meaning that some interaction with other apps (such as Webex cross-launch) may not perform correctly.

Cisco only supports the latest version of Cisco Jabber, Webex App , and Webex Meetings mobile apps. As a result, there’s an expectation that customers upgrade their user bases once Cisco releases new versions
                              in the App Store and Google Play Store. These versions will also be available through the MAM program.

Even if an initial MAM integration is successful, subsequent changes to the ecosystem including OS updates, new devices, new
                              Jabber or Webex versions, and new wrappers, SDKs, or other software versions could break subsequent integrations. As such, we recommend that
                              customers participate in our Early Adopter Program (EAP) also to ensure that updates to Jabber do not break use cases that
                              the customer is targeting.

The Mobile Application Management License Agreement is an agreement that's made between Cisco and another organization or
                        licensee looking to wrap the mobile application.

For more information, contact your Site Administrator or CSM .

## Calls

This section contains the following information:

Call Behavior Setup

### Call Behavior Setup

Jabber can be set up to make calls from the Webex App.

Depending upon the user’s calling license, the calling behavior options can be set up.

For Unified CM licensed users, you can set up to make calls directly from the Cisco Jabber or through the Webex App, and choose
                              the domain (organization domain or UC Manager profile) that gets applied to the users. You can configure the settings at organization
                              level, group level, and user level.

For users without paid calling services from Cisco, you can set up third-party applications to initiate calls. By default,
                              all calls through the Webex App use "Call on Webex" option. You can configure the settings at the organization level.

For Webex Calling licensed users, the Webex App is the default calling application to make calls. Hence, no specific calling
                              behavior configuration is needed.

For more information, see the Set up calling behavior article.

## Chat

This section contains the following information:

Persistent Chat Room Participants

### Persistent Chat Room Participants

If you are a moderator or an administrator, you can add people to persistent chat rooms. When you add people who have not
                        already signed up to Cisco Jabber, they'll get a notification after they sign in for the first time.

#### Add People to Persistent Chat Rooms in Windows

Step 1

Go to Rooms , choose the room where you want to add a member.

Step 2

Click Edit Room to view the room details and click Members and type the first letters of their name or email address in the search field, pick them from the list, and then click Save .

Step 3

To remove a participant, choose the name and click x .

You can remove a participant only from the restricted room.

#### Add People to Persistent Chat Rooms in Mac

Step 1

Go to Rooms , choose the room where you want to add a member.

Step 2

Click Edit Room to view the room details and click Invite Members and type the first letters of their name or email address in the search field, pick them from the list, and then click Save .

Step 3

To remove a participant, choose the name and click x .

You can remove a participant only from the restricted room.

#### Add People to Persistent Chat Rooms in Mobile

Step 1

Go to Rooms , choose the room where you want to add a participant, and tap Information to view the details of the room..

Step 2

Tap Plus , type the first letters of their name or email address in the Add field, pick them from the list, and then tap Save .

Step 3

To remove a participant, choose one of these options:

- iPhone and iPad: Swipe on the participant's name and tap Delete .

- Android: tap Edit , choose the participant's name, and tap Delete .

You can remove a participant only from the restricted room.

## Customizations

This section contains the following information:

Emoticons

### Emoticons

Organization Administrator only

You can add custom emoticons to Cisco Jabber for Windows by creating emoticon definitions in an XML file and saving it to
                        the file system. To achieve optimal results, your custom emoticons should conform to the following guidelines:

Dimensions: 17 x 17 pixels

Transparent background

PNG file format

RGB colors

Custom emoticon definitions are available to users only if they are defined locally in emoticonDefs.xml. If you send custom
                                    emoticons to users who do not have the same emoticon definitions, those users receive the default keys, not the icons; for
                                    example:

User A defines a custom emoticon in emoticonDefs.xml. The custom emoticon definition exists only on User A's local file system.

User A sends that custom emoticon to User B.

User B receives only the default key for the custom emoticon. User B does not receive the icon.

#### Emoticon Definitions

Cisco Jabber for Windows loads emoticon definitions from emoticonDefs.xml . The following XML snippet shows the basic structure for the emoticon definitions file:

- <emoticons>

- <emoticon defaultKey=" image=" text=" order=" hidden=">

- <alt></alt>

- </emoticon>

- </emoticons>

The following table describes the elements and attributes for defining custom emoticons:

This attribute defines the default key combination that renders the emoticon.

Specify any key combination as the value.

Specify any key combination as the value.

defaultKey is an attribute of the emoticon element.

This attribute specifies the filename of the emoticon image.

Specify the filename of the emoticon as the value.

The emoticon image must exist in the same directory as emoticonDefs.xml.

This attribute is required.

Cisco Jabber for Windows supports any icon that Internet Explorer can render, including .jpeg, .png, and .gif.

image is an attribute of the emoticon element.

This attribute specifies whether the emoticon displays in the Insert emoticon dialog box.

Specify one of the following as the value:

true : Specifies the emoticon does not display in the Insert emoticon dialog box. Users must enter the key combination to render
                                    the emoticon.

false : Specifies the emoticon displays in the Insert emoticon dialog box. Users can select the emoticon from the Insert emoticon
                                    dialog box or enter the key combination to render the emoticon. This is the default value.

#### Add Custom Emoticons with Jabber for Windows

Step 1

Create a file named emoticonDefs.xml with any text editor.

Step 2

Specify the emoticon definitions as appropriate in emoticonDefs.xml .

See Emoticon Definitions for more information on the structure and available parameters for emoticonDefs.xml.

Step 3

Save and close emoticonDefs.xml .

Step 4

Save emoticonDefs.xml in the appropriate directory on the file system.

Cisco Jabber for Windows loads emoticon definitions from the following directories on the file system:

Program Files\Cisco Systems\Cisco Jabber\Emoticons

This folder contains the default emoticons for Cisco Jabber for Windows and the default emoticonDefs.xml.

Program Files\Cisco Systems\Cisco Jabber\CustomEmoticons

This folder does not exist by default. Administrators can create this folder to contain custom emoticon definitions to include
                                                               in organizational deployments.

Emoticons that you define in the CustomEmoticons folder take precedence over emoticon definitions in the default Emoticons
                                                               folder.

%USERPROFILE%\AppData\Roaming\Cisco\Unified Communications\Jabber\CSF\CustomEmoticons

This folder contains custom emoticon definitions for individual instances of Cisco Jabber for Windows.

Emoticons that you define in this directory take precedence over emoticon definitions in the CustomEmoticons folder in the
                                                               installation directory.

Step 5

Restart Cisco Jabber for Windows.

## Integrations

### Enable Cisco Jabber for Government Integration for Microsoft Teams

As an administrator, install the Cisco Jabber for Government app for a seamless call experience in Microsoft Teams.

Before you begin

#### Before you begin

To install the Jabber for Government Integration app for Microsoft 365, turn on Allow external apps in Microsoft Teams and Allow sideloading of external apps . Contact Cisco Support to download the installation package.

Before users with a Microsoft Teams account can use the Jabber tab in Microsoft Teams, Webex site administrators must link
                        users' Jabber accounts to their Microsoft 365 accounts. The email addresses for both accounts should match.

Step 1

Sign in to Microsoft Teams with your administrator account.

Step 2

Click Apps , and then select Upload a custom app > Upload for <tenant name> .

Step 3

Locate the Jabber for Government.zip on your local computer and open it.

Step 4

Click Jabber FedRAMP , and then click Add .

Step 5

Click Give Permission , and then enter your password, if required.

Step 6

In the Jabber FedRAMP app, in the dialpad, enter *CONSENT# , and then click Enter .

Step 7

Select your administrator account.

Step 8

Click Accept to grant Jabber FedRAMP the requested permissions.

### Interoperability for Cisco Webex and Jabber

When your users are in Cisco Webex and also in Cisco Jabber, you can use the interoperability setting to allow people in both
                        apps to communicate with each other.

This article provides interoperability between your cloud-based Jabber deployment and Webex. This is different to the interoperability
                                    between on-premises Jabber deployments and Webex users (see https://www.cisco.com/go/hybrid-services-message for more on that deployment).

With the Cisco Webex / Jabber Interop setting enabled:

People can send or receive messages between Webex and Jabber apps.

Jabber users see a status of On Cisco Webex , when their contact is using Webex.

#### Deployment Requirements

Supported for Cisco Jabber cloud deployments only.

Before you enable this setting, check the following:

Your organization must be added to the Cisco Platform identity service. You can check in Cisco Webex Control Hub to see if
                              your organization has been added. If your organization hasn't been added, you can contact the Cisco Customer Support team
                              or your Cisco Customer Success Manager to request that your organization is added to the Cisco Platform identity service.
                              This process to add users to the identity service takes some time to complete.

For more information on the request process for Cisco Customer Support or Cisco Customer Success Manager, see this support article .

Cisco Jabber (Webex Messenger) and Webex domains must be identical for the Webex Messenger Org to be synched into the Cisco
                              Platform identity service.

Cisco Directory Connector must be disabled in Control Hub, as this method of managing users is not compatible with how users
                              are managed in a Jabber cloud deployment.

If you use Single Sign On (SSO) for Webex Messenger then you must set up SSO for Cisco Platform identity service. For more
                              information about configuring SSO, see the Cisco Webex Messenger Install and Upgrade documentation .

#### Known Limitations

Users can only send text between Jabber and Webex, sending any other content is not supported.

You can only send messages in a space with one person, you can't send messages in group spaces.

End-to-end AES encryption is not supported.

All users must have the Cisco Webex / Jabber Interop setting enabled.

When a Jabber user without interop enabled attempts to send a message to an interop enabled user who isn't signed in to Jabber,
                              they receive this message This user is currently offline in Jabber and the message cannot be delivered .

#### Jabber Requirements

Cisco Jabber clients 11.9 or later.

Ensure the following parameter is set to False in the jabber-config.xml file: <Persistent_Chat_Enabled>False</Persistent_Chat_Enabled>

AES encryption must be disabled in Cisco Webex Messenger Administration Tool (Org Admin). In the Policy Editor tab, disable
                        the Support End-To-End Encryption for IM setting.

#### Cisco Webex Control Hub Settings

You can enable the Cisco Webex / Jabber Interop setting in Control Hub for your entire organization and then for specific people. The setting is also available as one of
                        the services to choose in the CSV file user setup.

#### Set Up Messaging Between Cisco Webex and Jabber for Your Organization

When your users are in Webex and also in Cisco Jabber, you can use this setting to allow everyone in both apps to communicate
                           with each other.

Step 1

From the customer view in https://admin.webex.com , go to Services , and then click Message > Webex Messenger .

If you don't see this option, contact the Cisco Customer Support team or your Cisco Customer Success Manager to request that
                                       your organization is added to the Cisco Platform identity service. This process to add users to the identity service takes
                                       some time to complete.

Step 2

Scroll to Options , click Cisco Webex / Jabber Interop , and then click Save .

#### Set Up Messaging Between Cisco Webex and Jabber for a User

When your users are in Webex and also in Jabber, you can use this setting to allow a person to communicate with people in
                           both Webex and Jabber.

Before you begin

##### Before you begin

You must set up messaging between Webex and Jabber for your organization before you see this setting for users.

Step 1

From the customer view in https://admin.webex.com , go to Users .

Step 2

Click on the person and then click Message Free or Message Paid .

Step 3

Click Cisco Webex / Jabber Interop and click Save .

#### Set Up Messaging Between Cisco Webex and Jabber for Many Users

Step 1

From the customer view in https://admin.webex.com , go to Users and click Manage Users .

Step 2

Choose Export and import users with a CSV template , click Next and then Export .

Step 3

Edit the CSV file that was downloaded, update the Cisco Webex / Jabber Interop column with TRUE and save the file.

Step 4

Click Import , select your file and click Open .

Step 5

Choose either Add services only or Add and remove services , and click Submit .

### Slack Integration with Dedicated Instance for In-App Calling

You can integrate Slack messaging with Cisco Calling to make voice and video calls from within the application using the Dedicated
                        Instance service.

Slack can be used by Dedicated Instance customers to integrate Slack messaging with Cisco Calling. The Cisco Jabber calling
                        application or Cisco Webex calling application for Slack is a plug-in application within Slack that enables a Slack user to
                        make voice and video calls from within the application using the Dedicated Instance service.

The Slack user installs the Cisco Calling application within Slack in his/her personal device. Webex application or Jabber
                        application must be already installed and registered with Dedicated Instance following all Dedicated Instance requirements.
                        When both installations are done, Slack can make calls using Dedicated Instance Call Control. The Slack support provides the
                        following features within Dedicated Instance for end users:

Make calls directly from the Slack client through the Unified CM

Call using the chat window using the Slack application call icon

Call using the slash option of the Slack application

#### Set Up Slack Calling

To use direct calling features from a Slack client in Dedicated Instance, follow these procedures to set up Slack calling.
                           Refer to Cisco Webex Calling for Slack for specific configuration settings required for Slack.

Refer to Cisco Webex Calling for Slack in the Webex Help Center for information about using Slack to call from a user device.

Warning

The end user must be logged into the Cisco Webex application.

The client-side integration allows partners to support Slack for Dedicated Instance with no additional changes to infrastructure
                           or configuration.

Step 1

Install Webex application or Jabber and register with Dedicated Instance. (Partner)

Follow the instructions in Webex Application Integration with Dedicated Instance for In-App Calling to integrate calling via the Unified CM with the Dedicated Instance solution.

Step 2

Follow the steps for Administrators to enable Webex calling using Dedicated Instance. (Slack Administrator)

Step 3

Follow the steps for Users to install and use Webex calling using Dedicated Instance (Slack user)

### Configure Cisco Jabber for Microsoft Teams

As an administrator, install the Jabber app for a seamless call experience in Microsoft Teams for your organization.

Before you begin

#### Before you begin

Users should be able to sign in to Cisco Jabber, and they should be successfully registered to Unified Communications Manager
                              for making calls.

Make sure you have Administrator rights for Microsoft Teams.

Make sure users' phone numbers are updated in the Azure Active Directory.

Step 1

Go to Microsoft Teams Admin Center .

Step 2

From the menu on the left, click Teams Apps > Manage Apps .

Step 3

In the search box, search for Jabber , and in the search results, click on the app name.

Step 4

Toggle on the app status to Allowed .

Step 5

From the menu on the left, go to Teams apps > Permission policies .

Step 6

Select the policy for your organization, and make sure Third Party apps is set to Allow all apps .

Step 7

From the menu on the left, select Teams apps > Setup policies .

Step 8

Select the policy for your organization.

Step 9

Click Add > Add Apps ,  search for Jabber , and click Add .

Step 10

Click Add at the bottom of the screen to confirm.

Step 11

Click Save .

It can take up to 24 hours for changes in Microsoft Teams to take effect.

## Migrations

| Note | Mobile application management currently isn't supported for Webex Meetings Online customers. |
|---|---|

| Step 1 | Go to Rooms , choose the room where you want to add a member. |
|---|---|
| Step 2 | Click Edit Room to view the room details and click Members and type the first letters of their name or email address in the search field, pick them from the list, and then click Save . |
| Step 3 | To remove a participant, choose the name and click x . You can remove a participant only from the restricted room. |

| Step 1 | Go to Rooms , choose the room where you want to add a member. |
|---|---|
| Step 2 | Click Edit Room to view the room details and click Invite Members and type the first letters of their name or email address in the search field, pick them from the list, and then click Save . |
| Step 3 | To remove a participant, choose the name and click x . You can remove a participant only from the restricted room. |

| Step 1 | Go to Rooms , choose the room where you want to add a participant, and tap Information to view the details of the room.. |
|---|---|
| Step 2 | Tap Plus , type the first letters of their name or email address in the Add field, pick them from the list, and then tap Save . |
| Step 3 | To remove a participant, choose one of these options: iPhone and iPad: Swipe on the participant's name and tap Delete . Android: tap Edit , choose the participant's name, and tap Delete . You can remove a participant only from the restricted room. |

| Note | Custom emoticon definitions are available to users only if they are defined locally in emoticonDefs.xml. If you send custom
                                    emoticons to users who do not have the same emoticon definitions, those users receive the default keys, not the icons; for
                                    example: User A defines a custom emoticon in emoticonDefs.xml. The custom emoticon definition exists only on User A's local file system. User A sends that custom emoticon to User B. User B receives only the default key for the custom emoticon. User B does not receive the icon. |
|---|---|

| Element or attribute | Description |
|---|---|
| emoticons | This element contains all emoticon definitions. |
| emoticon | This element contains the definition of an emoticon. |
| defaultKey | This attribute defines the default key combination that renders the emoticon. Specify any key combination as the value. Specify any key combination as the value. defaultKey is an attribute of the emoticon element. |
| image | This attribute specifies the filename of the emoticon image. Specify the filename of the emoticon as the value. The emoticon image must exist in the same directory as emoticonDefs.xml. This attribute is required. Cisco Jabber for Windows supports any icon that Internet Explorer can render, including .jpeg, .png, and .gif. image is an attribute of the emoticon element. |
| text | This attribute defines the descriptive text that displays in the Insert emoticon dialog box. Specify any string of unicode
                                 characters. This attribute is optional.text is an attribute of the emoticon element. |
| order | This attribute defines the order in which emoticons display in the Insert emoticon dialog box. Specify an ordinal number beginning
                                 from 1 as the value.order is an attribute of the emoticon element. This attribute is required. However, if the value of hidden
                                 is true this parameter does not take effect. |
| hidden | This attribute specifies whether the emoticon displays in the Insert emoticon dialog box. Specify one of the following as the value: true : Specifies the emoticon does not display in the Insert emoticon dialog box. Users must enter the key combination to render
                                    the emoticon. false : Specifies the emoticon displays in the Insert emoticon dialog box. Users can select the emoticon from the Insert emoticon
                                    dialog box or enter the key combination to render the emoticon. This is the default value. |
| alt | This element enables you to map key combinations to emoticons. Specify any key combination as the value. For example, if the
                                 value of defaultKey is :), you can specify :-) as the value of alt so that both key combinations render the same emoticon.
                                 This element is optional. |

| Step 1 | Create a file named emoticonDefs.xml with any text editor. |
|---|---|
| Step 2 | Specify the emoticon definitions as appropriate in emoticonDefs.xml . Note See Emoticon Definitions for more information on the structure and available parameters for emoticonDefs.xml. | Note | See Emoticon Definitions for more information on the structure and available parameters for emoticonDefs.xml. |
| Note | See Emoticon Definitions for more information on the structure and available parameters for emoticonDefs.xml. |
| Step 3 | Save and close emoticonDefs.xml . |
| Step 4 | Save emoticonDefs.xml in the appropriate directory on the file system. Note Cisco Jabber for Windows loads emoticon definitions from the following directories on the file system: Program Files\Cisco Systems\Cisco Jabber\Emoticons This folder contains the default emoticons for Cisco Jabber for Windows and the default emoticonDefs.xml. Program Files\Cisco Systems\Cisco Jabber\CustomEmoticons This folder does not exist by default. Administrators can create this folder to contain custom emoticon definitions to include
                                                               in organizational deployments. Emoticons that you define in the CustomEmoticons folder take precedence over emoticon definitions in the default Emoticons
                                                               folder. %USERPROFILE%\AppData\Roaming\Cisco\Unified Communications\Jabber\CSF\CustomEmoticons This folder contains custom emoticon definitions for individual instances of Cisco Jabber for Windows. Emoticons that you define in this directory take precedence over emoticon definitions in the CustomEmoticons folder in the
                                                               installation directory. | Note | Cisco Jabber for Windows loads emoticon definitions from the following directories on the file system: Program Files\Cisco Systems\Cisco Jabber\Emoticons This folder contains the default emoticons for Cisco Jabber for Windows and the default emoticonDefs.xml. Program Files\Cisco Systems\Cisco Jabber\CustomEmoticons This folder does not exist by default. Administrators can create this folder to contain custom emoticon definitions to include
                                                               in organizational deployments. Emoticons that you define in the CustomEmoticons folder take precedence over emoticon definitions in the default Emoticons
                                                               folder. %USERPROFILE%\AppData\Roaming\Cisco\Unified Communications\Jabber\CSF\CustomEmoticons This folder contains custom emoticon definitions for individual instances of Cisco Jabber for Windows. Emoticons that you define in this directory take precedence over emoticon definitions in the CustomEmoticons folder in the
                                                               installation directory. |
| Note | Cisco Jabber for Windows loads emoticon definitions from the following directories on the file system: Program Files\Cisco Systems\Cisco Jabber\Emoticons This folder contains the default emoticons for Cisco Jabber for Windows and the default emoticonDefs.xml. Program Files\Cisco Systems\Cisco Jabber\CustomEmoticons This folder does not exist by default. Administrators can create this folder to contain custom emoticon definitions to include
                                                               in organizational deployments. Emoticons that you define in the CustomEmoticons folder take precedence over emoticon definitions in the default Emoticons
                                                               folder. %USERPROFILE%\AppData\Roaming\Cisco\Unified Communications\Jabber\CSF\CustomEmoticons This folder contains custom emoticon definitions for individual instances of Cisco Jabber for Windows. Emoticons that you define in this directory take precedence over emoticon definitions in the CustomEmoticons folder in the
                                                               installation directory. |
| Step 5 | Restart Cisco Jabber for Windows. |

| Note | See Emoticon Definitions for more information on the structure and available parameters for emoticonDefs.xml. |
|---|---|

| Note | Cisco Jabber for Windows loads emoticon definitions from the following directories on the file system: Program Files\Cisco Systems\Cisco Jabber\Emoticons This folder contains the default emoticons for Cisco Jabber for Windows and the default emoticonDefs.xml. Program Files\Cisco Systems\Cisco Jabber\CustomEmoticons This folder does not exist by default. Administrators can create this folder to contain custom emoticon definitions to include
                                                               in organizational deployments. Emoticons that you define in the CustomEmoticons folder take precedence over emoticon definitions in the default Emoticons
                                                               folder. %USERPROFILE%\AppData\Roaming\Cisco\Unified Communications\Jabber\CSF\CustomEmoticons This folder contains custom emoticon definitions for individual instances of Cisco Jabber for Windows. Emoticons that you define in this directory take precedence over emoticon definitions in the CustomEmoticons folder in the
                                                               installation directory. |
|---|---|

| Step 1 | Sign in to Microsoft Teams with your administrator account. |
|---|---|
| Step 2 | Click Apps , and then select Upload a custom app > Upload for <tenant name> . |
| Step 3 | Locate the Jabber for Government.zip on your local computer and open it. |
| Step 4 | Click Jabber FedRAMP , and then click Add . |
| Step 5 | Click Give Permission , and then enter your password, if required. |
| Step 6 | In the Jabber FedRAMP app, in the dialpad, enter *CONSENT# , and then click Enter . |
| Step 7 | Select your administrator account. |
| Step 8 | Click Accept to grant Jabber FedRAMP the requested permissions. |

| Note | This article provides interoperability between your cloud-based Jabber deployment and Webex. This is different to the interoperability
                                    between on-premises Jabber deployments and Webex users (see https://www.cisco.com/go/hybrid-services-message for more on that deployment). |
|---|---|

| Step 1 | From the customer view in https://admin.webex.com , go to Services , and then click Message > Webex Messenger . If you don't see this option, contact the Cisco Customer Support team or your Cisco Customer Success Manager to request that
                                       your organization is added to the Cisco Platform identity service. This process to add users to the identity service takes
                                       some time to complete. |
|---|---|
| Step 2 | Scroll to Options , click Cisco Webex / Jabber Interop , and then click Save . |

| Step 1 | From the customer view in https://admin.webex.com , go to Users . |
|---|---|
| Step 2 | Click on the person and then click Message Free or Message Paid . |
| Step 3 | Click Cisco Webex / Jabber Interop and click Save . |

| Step 1 | From the customer view in https://admin.webex.com , go to Users and click Manage Users . |
|---|---|
| Step 2 | Choose Export and import users with a CSV template , click Next and then Export . |
| Step 3 | Edit the CSV file that was downloaded, update the Cisco Webex / Jabber Interop column with TRUE and save the file. |
| Step 4 | Click Import , select your file and click Open . |
| Step 5 | Choose either Add services only or Add and remove services , and click Submit . |

| Warning | The end user must be logged into the Cisco Webex application. |
|---|---|

| Step 1 | Install Webex application or Jabber and register with Dedicated Instance. (Partner) Note Follow the instructions in Webex Application Integration with Dedicated Instance for In-App Calling to integrate calling via the Unified CM with the Dedicated Instance solution. | Note | Follow the instructions in Webex Application Integration with Dedicated Instance for In-App Calling to integrate calling via the Unified CM with the Dedicated Instance solution. |
|---|---|---|---|
| Note | Follow the instructions in Webex Application Integration with Dedicated Instance for In-App Calling to integrate calling via the Unified CM with the Dedicated Instance solution. |
| Step 2 | Follow the steps for Administrators to enable Webex calling using Dedicated Instance. (Slack Administrator) |
| Step 3 | Follow the steps for Users to install and use Webex calling using Dedicated Instance (Slack user) |

| Note | Follow the instructions in Webex Application Integration with Dedicated Instance for In-App Calling to integrate calling via the Unified CM with the Dedicated Instance solution. |
|---|---|

| Step 1 | Go to Microsoft Teams Admin Center . |
|---|---|
| Step 2 | From the menu on the left, click Teams Apps > Manage Apps . |
| Step 3 | In the search box, search for Jabber , and in the search results, click on the app name. |
| Step 4 | Toggle on the app status to Allowed . |
| Step 5 | From the menu on the left, go to Teams apps > Permission policies . |
| Step 6 | Select the policy for your organization, and make sure Third Party apps is set to Allow all apps . |
| Step 7 | From the menu on the left, select Teams apps > Setup policies . |
| Step 8 | Select the policy for your organization. |
| Step 9 | Click Add > Add Apps ,  search for Jabber , and click Add . |
| Step 10 | Click Add at the bottom of the screen to confirm. |
| Step 11 | Click Save . It can take up to 24 hours for changes in Microsoft Teams to take effect. |