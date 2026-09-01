---
doc_id: help-webex-com-en-us-article-nsjpi6h-saml-auto-account-creation-and-update-for-control-hub-0d93e98385
source_url: https://help.webex.com/en-us/article/nsjpi6h/SAML-Auto-Account-Creation-and-Update-for-Control-Hub
retrieved_at: 2026-09-01T20:26:12.220566+00:00
---

## Modify Single sign-on authentication in Control Hub

### Before you begin

Ensure that the following preconditions are met:

SSO is already configured. For information on using the SSO configuration wizard, see Single Sign-On Integration in Control Hub .

The domains have already been verified.

The domains are claimed and turned on. This feature ensures users from your domain are
            created and updated once each time they authenticate with your IdP.

If DirSync or Entra ID are enabled then SAML JIT create or update will not work.

Block user profile update is enabled. SAML Update Mapping is allowed because this configuration controls the user’s ability to edit the attributes. Admin-controlled methods of creation and update are still supported.

Self-registration must be enabled, as SAML JIT account creation won’t work if this
            setting is disabled. For more information, see Prevent users
              from self-registering with your domain .

Newly created users won't automatically get assigned licenses unless the organization has an automatic license template set up.

User provisioning for SAML JIT provisioning of groups is limited to a single group only.

## Configure Just-in-Time (JIT) and SAML mapping

Sign in to Control
          Hub .

Go to Management > Security > Authentication .

Go to the Identity provider tab.

Go to the IdP and click .

Select Edit SAML mapping .

Configure Just-in-Time (JIT) settings .

- Create or activate user: if no active user is found, then Webex Identity creates the user and update the attributes after the user has
                authenticated with the IdP.

- Update user with SAML attributes: if a user with email address is found, then Webex Identity updates the user with the attributes mapped in the SAML Assertion.

Configure SAML mapping required attributes .

Webex Identity attribute name

SAML attribute name

Attribute description

Username / Primary email address

Example: uid

Map the UID attribute to the provisioned user's email, upn, or
                      edupersonprincipalname.

Configure the Linking attributes .

Webex Identity attribute name

SAML attribute name

Attribute description

externalId

Example: user.objectid

To identify this user from other individual profiles. This is necessary when
                      mapping between directories or changing other profile attributes.

Extension Attribute 1

Example: user.extensionattribute1

Map these custom attributes to extended attributes in Entra ID or your directory, for tracking codes.

Extension Attribute 2

Example: user.extensionattribute2

Extension Attribute 3

Example: user.extensionattribute3

Extension Attribute 4

Example: user.extensionlattribute4

Extension Attribute 5

Example: user.extensionattribute5

Configure Profile attributes .

Webex Identity attribute name

SAML attribute name

Attribute description

externalId

Example: user.objectid

To identify this user from other individual profiles. This is necessary when
                      mapping between directories or changing other profile attributes.

preferredLanguage

Example: user.preferredlanguage

The user's preferred language.

locale

Example: user.locale

The user's primary work location.

timezone

Example: user.timezone

The user's primary time zone.

displayName

Example: user.displayname

The user's display name in Webex.

name.givenName

Example: user.givenname

The user's first name.

name.familyName

Example: user.surname

The user's last name.

addresses.streetAddress

Example: user.streetaddress

The street address of their primary work location.

addresses.locality

addresses.region

Example: user.region

The region of their primary work location.

addresses.postalCode

Example: user.postalcode

The zip code of their primary work location.

addresses.country

Example: user.country

The country of their primary work location.

phoneNumbers.work

Example: work phonenumber

The work phone number of their primary work location. Use the international
                      E.164 format only (15 digits maximum).

phoneNumbers.extension

Example: extension phonenumber

The work extension of their primary work phone number. Use the international
                      E.164 format only (15 digits maximum).

phoneNumbers.mobile

title

Example: user.jobtitle

The user's job title.

department

Example: user.department

The user's job department or team.

Configure Group attributes .

- Create a group in Control Hub and note the Webex group ID.

- Go to your user directory or IdP and set up an attribute for users who will be
              assigned to the Webex group ID.

- Update your IdP's configuration to include a claim that carries this attribute name
              along with the Webex Group ID (e.g. c65f7d85-b691-42b8-a20b-12345xxxx). You can also use the External ID
              for managing changes to group names or for future integration scenarios. For example,
              syncing with Entra ID or implementing SCIM group synchronization.

- Specify the exact name of the attribute that will be sent in the SAML Assertion
              with the group ID. This is used to add the user to a group.

- Specify the exact name of the external ID of the group object if you are using a
              group from your directory to send members in the SAML Assertion.

If user A is associated with groupID 1234 and user B with groupID 4567, they are assigned to separate groups. This scenario
              indicates that a single attribute allows users to associate with multiple group IDs.
              While this is uncommon, it is possible and can be considered as an additive change.
              For example, if user A initially signs in using groupID 1234, they
              become a member of the corresponding group. If user A later signs in using groupID 4567, they are also added to this second group.

SAML JIT provisioning does not support the removal of users from groups or any deletion of users.

Webex Identity attribute name

SAML attribute name

Attribute description

groupId

Example: groupId

Map group attributes from IdP to Webex Identity group Attributes for the purpose of mapping that user to a
                      group for licensing or the setting service.

groupexternalId

Example: groupexternalId

Map group attributes from IdP to Webex Identity group Attributes for the purpose of mapping that user to a
                      group for licensing or the setting service.

For a list of SAML assertion attributes for Webex Meetings, see SAML Assertion Attributes for Webex Meetings and Jabber .

| 1 | Sign in to Control
          Hub . |
|---|---|
| 2 | Go to Management > Security > Authentication . |
| 3 | Go to the Identity provider tab. |
| 4 | Go to the IdP and click . |
| 5 | Select Edit SAML mapping . |
| 6 | Configure Just-in-Time (JIT) settings . Create or activate user: if no active user is found, then Webex Identity creates the user and update the attributes after the user has
                authenticated with the IdP. Update user with SAML attributes: if a user with email address is found, then Webex Identity updates the user with the attributes mapped in the SAML Assertion. Confirm users can sign in with a different, unidentifiable email address. |
| 7 | Configure SAML mapping required attributes . Table 1. Required attributes Webex Identity attribute name SAML attribute name Attribute description Username / Primary email address Example: uid Map the UID attribute to the provisioned user's email, upn, or
                      edupersonprincipalname. | Webex Identity attribute name | SAML attribute name | Attribute description | Username / Primary email address | Example: uid | Map the UID attribute to the provisioned user's email, upn, or
                      edupersonprincipalname. |
| Webex Identity attribute name | SAML attribute name | Attribute description |
| Username / Primary email address | Example: uid | Map the UID attribute to the provisioned user's email, upn, or
                      edupersonprincipalname. |
| 8 | Configure the Linking attributes . This should be unique to the user. It is used to lookup a user so that Webex can
          update all profile attributes, including email for a user. Table 2. Linking attributes Webex Identity attribute name SAML attribute name Attribute description externalId Example: user.objectid To identify this user from other individual profiles. This is necessary when
                      mapping between directories or changing other profile attributes. Extension Attribute 1 Example: user.extensionattribute1 Map these custom attributes to extended attributes in Entra ID or your directory, for tracking codes. Extension Attribute 2 Example: user.extensionattribute2 Extension Attribute 3 Example: user.extensionattribute3 Extension Attribute 4 Example: user.extensionlattribute4 Extension Attribute 5 Example: user.extensionattribute5 | Webex Identity attribute name | SAML attribute name | Attribute description | externalId | Example: user.objectid | To identify this user from other individual profiles. This is necessary when
                      mapping between directories or changing other profile attributes. | Extension Attribute 1 | Example: user.extensionattribute1 | Map these custom attributes to extended attributes in Entra ID or your directory, for tracking codes. | Extension Attribute 2 | Example: user.extensionattribute2 | Extension Attribute 3 | Example: user.extensionattribute3 | Extension Attribute 4 | Example: user.extensionlattribute4 | Extension Attribute 5 | Example: user.extensionattribute5 |
| Webex Identity attribute name | SAML attribute name | Attribute description |
| externalId | Example: user.objectid | To identify this user from other individual profiles. This is necessary when
                      mapping between directories or changing other profile attributes. |
| Extension Attribute 1 | Example: user.extensionattribute1 | Map these custom attributes to extended attributes in Entra ID or your directory, for tracking codes. |
| Extension Attribute 2 | Example: user.extensionattribute2 |
| Extension Attribute 3 | Example: user.extensionattribute3 |
| Extension Attribute 4 | Example: user.extensionlattribute4 |
| Extension Attribute 5 | Example: user.extensionattribute5 |
| 9 | Configure Profile attributes . Table 3. Profile attributes Webex Identity attribute name SAML attribute name Attribute description externalId Example: user.objectid To identify this user from other individual profiles. This is necessary when
                      mapping between directories or changing other profile attributes. preferredLanguage Example: user.preferredlanguage The user's preferred language. locale Example: user.locale The user's primary work location. timezone Example: user.timezone The user's primary time zone. displayName Example: user.displayname The user's display name in Webex. name.givenName Example: user.givenname The user's first name. name.familyName Example: user.surname The user's last name. addresses.streetAddress Example: user.streetaddress The street address of their primary work location. addresses.locality Example: user.locality The locality of their primary work location. addresses.region Example: user.region The region of their primary work location. addresses.postalCode Example: user.postalcode The zip code of their primary work location. addresses.country Example: user.country The country of their primary work location. phoneNumbers.work Example: work phonenumber The work phone number of their primary work location. Use the international
                      E.164 format only (15 digits maximum). phoneNumbers.extension Example: extension phonenumber The work extension of their primary work phone number. Use the international
                      E.164 format only (15 digits maximum). phoneNumbers.mobile Example: mobile phonenumber The mobile phone number of their primary work location. Use the
                    international E.164 format only (15 digits maximum). title Example: user.jobtitle The user's job title. department Example: user.department The user's job department or team. emails.work Example: work emails The user's work emails. organization Example: user.organization The user's organisation ID | Webex Identity attribute name | SAML attribute name | Attribute description | externalId | Example: user.objectid | To identify this user from other individual profiles. This is necessary when
                      mapping between directories or changing other profile attributes. | preferredLanguage | Example: user.preferredlanguage | The user's preferred language. | locale | Example: user.locale | The user's primary work location. | timezone | Example: user.timezone | The user's primary time zone. | displayName | Example: user.displayname | The user's display name in Webex. | name.givenName | Example: user.givenname | The user's first name. | name.familyName | Example: user.surname | The user's last name. | addresses.streetAddress | Example: user.streetaddress | The street address of their primary work location. | addresses.locality | Example: user.locality | The locality of their primary work location. | addresses.region | Example: user.region | The region of their primary work location. | addresses.postalCode | Example: user.postalcode | The zip code of their primary work location. | addresses.country | Example: user.country | The country of their primary work location. | phoneNumbers.work | Example: work phonenumber | The work phone number of their primary work location. Use the international
                      E.164 format only (15 digits maximum). | phoneNumbers.extension | Example: extension phonenumber | The work extension of their primary work phone number. Use the international
                      E.164 format only (15 digits maximum). | phoneNumbers.mobile | Example: mobile phonenumber | The mobile phone number of their primary work location. Use the
                    international E.164 format only (15 digits maximum). | title | Example: user.jobtitle | The user's job title. | department | Example: user.department | The user's job department or team. | emails.work | Example: work emails | The user's work emails. | organization | Example: user.organization | The user's organisation ID |
| Webex Identity attribute name | SAML attribute name | Attribute description |
| externalId | Example: user.objectid | To identify this user from other individual profiles. This is necessary when
                      mapping between directories or changing other profile attributes. |
| preferredLanguage | Example: user.preferredlanguage | The user's preferred language. |
| locale | Example: user.locale | The user's primary work location. |
| timezone | Example: user.timezone | The user's primary time zone. |
| displayName | Example: user.displayname | The user's display name in Webex. |
| name.givenName | Example: user.givenname | The user's first name. |
| name.familyName | Example: user.surname | The user's last name. |
| addresses.streetAddress | Example: user.streetaddress | The street address of their primary work location. |
| addresses.locality | Example: user.locality | The locality of their primary work location. |
| addresses.region | Example: user.region | The region of their primary work location. |
| addresses.postalCode | Example: user.postalcode | The zip code of their primary work location. |
| addresses.country | Example: user.country | The country of their primary work location. |
| phoneNumbers.work | Example: work phonenumber | The work phone number of their primary work location. Use the international
                      E.164 format only (15 digits maximum). |
| phoneNumbers.extension | Example: extension phonenumber | The work extension of their primary work phone number. Use the international
                      E.164 format only (15 digits maximum). |
| phoneNumbers.mobile | Example: mobile phonenumber | The mobile phone number of their primary work location. Use the
                    international E.164 format only (15 digits maximum). |
| title | Example: user.jobtitle | The user's job title. |
| department | Example: user.department | The user's job department or team. |
| emails.work | Example: work emails | The user's work emails. |
| organization | Example: user.organization | The user's organisation ID |
| 10 | Configure Group attributes . Create a group in Control Hub and note the Webex group ID. Go to your user directory or IdP and set up an attribute for users who will be
              assigned to the Webex group ID. Update your IdP's configuration to include a claim that carries this attribute name
              along with the Webex Group ID (e.g. c65f7d85-b691-42b8-a20b-12345xxxx). You can also use the External ID
              for managing changes to group names or for future integration scenarios. For example,
              syncing with Entra ID or implementing SCIM group synchronization. Specify the exact name of the attribute that will be sent in the SAML Assertion
              with the group ID. This is used to add the user to a group. Specify the exact name of the external ID of the group object if you are using a
              group from your directory to send members in the SAML Assertion. If user A is associated with groupID 1234 and user B with groupID 4567, they are assigned to separate groups. This scenario
              indicates that a single attribute allows users to associate with multiple group IDs.
              While this is uncommon, it is possible and can be considered as an additive change.
              For example, if user A initially signs in using groupID 1234, they
              become a member of the corresponding group. If user A later signs in using groupID 4567, they are also added to this second group. SAML JIT provisioning does not support the removal of users from groups or any deletion of users. Table 4. Group attributes Webex Identity attribute name SAML attribute name Attribute description groupId Example: groupId Map group attributes from IdP to Webex Identity group Attributes for the purpose of mapping that user to a
                      group for licensing or the setting service. groupexternalId Example: groupexternalId Map group attributes from IdP to Webex Identity group Attributes for the purpose of mapping that user to a
                      group for licensing or the setting service. For a list of SAML assertion attributes for Webex Meetings, see SAML Assertion Attributes for Webex Meetings and Jabber . | Webex Identity attribute name | SAML attribute name | Attribute description | groupId | Example: groupId | Map group attributes from IdP to Webex Identity group Attributes for the purpose of mapping that user to a
                      group for licensing or the setting service. | groupexternalId | Example: groupexternalId | Map group attributes from IdP to Webex Identity group Attributes for the purpose of mapping that user to a
                      group for licensing or the setting service. |
| Webex Identity attribute name | SAML attribute name | Attribute description |
| groupId | Example: groupId | Map group attributes from IdP to Webex Identity group Attributes for the purpose of mapping that user to a
                      group for licensing or the setting service. |
| groupexternalId | Example: groupexternalId | Map group attributes from IdP to Webex Identity group Attributes for the purpose of mapping that user to a
                      group for licensing or the setting service. |

| Webex Identity attribute name | SAML attribute name | Attribute description |
|---|---|---|
| Username / Primary email address | Example: uid | Map the UID attribute to the provisioned user's email, upn, or
                      edupersonprincipalname. |

| Webex Identity attribute name | SAML attribute name | Attribute description |
|---|---|---|
| externalId | Example: user.objectid | To identify this user from other individual profiles. This is necessary when
                      mapping between directories or changing other profile attributes. |
| Extension Attribute 1 | Example: user.extensionattribute1 | Map these custom attributes to extended attributes in Entra ID or your directory, for tracking codes. |
| Extension Attribute 2 | Example: user.extensionattribute2 |
| Extension Attribute 3 | Example: user.extensionattribute3 |
| Extension Attribute 4 | Example: user.extensionlattribute4 |
| Extension Attribute 5 | Example: user.extensionattribute5 |

| Webex Identity attribute name | SAML attribute name | Attribute description |
|---|---|---|
| externalId | Example: user.objectid | To identify this user from other individual profiles. This is necessary when
                      mapping between directories or changing other profile attributes. |
| preferredLanguage | Example: user.preferredlanguage | The user's preferred language. |
| locale | Example: user.locale | The user's primary work location. |
| timezone | Example: user.timezone | The user's primary time zone. |
| displayName | Example: user.displayname | The user's display name in Webex. |
| name.givenName | Example: user.givenname | The user's first name. |
| name.familyName | Example: user.surname | The user's last name. |
| addresses.streetAddress | Example: user.streetaddress | The street address of their primary work location. |
| addresses.locality | Example: user.locality | The locality of their primary work location. |
| addresses.region | Example: user.region | The region of their primary work location. |
| addresses.postalCode | Example: user.postalcode | The zip code of their primary work location. |
| addresses.country | Example: user.country | The country of their primary work location. |
| phoneNumbers.work | Example: work phonenumber | The work phone number of their primary work location. Use the international
                      E.164 format only (15 digits maximum). |
| phoneNumbers.extension | Example: extension phonenumber | The work extension of their primary work phone number. Use the international
                      E.164 format only (15 digits maximum). |
| phoneNumbers.mobile | Example: mobile phonenumber | The mobile phone number of their primary work location. Use the
                    international E.164 format only (15 digits maximum). |
| title | Example: user.jobtitle | The user's job title. |
| department | Example: user.department | The user's job department or team. |
| emails.work | Example: work emails | The user's work emails. |
| organization | Example: user.organization | The user's organisation ID |

| Webex Identity attribute name | SAML attribute name | Attribute description |
|---|---|---|
| groupId | Example: groupId | Map group attributes from IdP to Webex Identity group Attributes for the purpose of mapping that user to a
                      group for licensing or the setting service. |
| groupexternalId | Example: groupexternalId | Map group attributes from IdP to Webex Identity group Attributes for the purpose of mapping that user to a
                      group for licensing or the setting service. |