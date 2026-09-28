---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b04ucset-html-d5e3600f1e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b04ucset.html
retrieved_at: 2026-08-21T16:12:14.553463+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Unified Personal Communicator Settings

## Chapter: Unified Personal Communicator Settings

- Configuring Cisco Unified Personal Communicator Settings

## Unified Personal Communicator Settings

Use Unified Personal Communicator settings to configure the settings that apply to all Cisco Unified Personal Communicator users.

## Configuring Cisco Unified Personal Communicator Settings

Follow this procedure to configure the Unified Personal Communicator settings.

Step 1 Choose Application > Unified Personal Communicator > Settings .

The Unified Personal Communicator Settings window displays.

Step 2 Enter the appropriate configuration settings as described in Table 23-1 .

Step 3 Enter the appropriate LDAP attribute name for your environment that maps to the given Cisco Unified Personal Communicator attribute name. For a list of Cisco Unified Personal Communicator attribute names and the corresponding default LDAP name, see Table 23-2

Step 4 To save the data, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Table 23-1 Cisco Unified Personal Communicator Configuration Settings

Primary TFTP Server

This parameter specifies the primary TFTP server address, either as a fully qualified domain name or as an IP address.

Maximum characters: 128

Backup TFTP Server

This parameter specifies the backup TFTP server address, either as a fully qualified domain name or as an IP address.

Maximum characters: 128

Table 23-2 LDAP Attribute Mapping

UID

employeenumber

LastName

sn

Nickname

nickname

Photo

jpegPhoto

DisplayName

displayName

NameSuffix

BusinessEMail

mail

BusinessPhoneNumber

telephoneNumber

BusinessMobilePhone

mobile

BusinessFax

facsimileTelephoneNumber

HomeEMail

HomeFax

FirstName

givenName

MiddleName

initials

UserID

uid

Title

title

NamePrefix

Gender

IM

uid

BusinessVoiceMail

voicemail

BusinessPager

pager

BusinessOtherPhone

HomeMobilePhone

URL

labeledURL

| Field | Description |
|---|---|
| Primary TFTP Server | This parameter specifies the primary TFTP server address, either as a fully qualified domain name or as an IP address. Maximum characters: 128 |
| Backup TFTP Server | This parameter specifies the backup TFTP server address, either as a fully qualified domain name or as an IP address. Maximum characters: 128 |

| Unified Personal Communicator Attribute Name | Default LDAP Attribute Name |
|---|---|
| UID | employeenumber |
| LastName | sn |
| Nickname | nickname |
| Photo | jpegPhoto |
| DisplayName | displayName |
| NameSuffix |  |
| BusinessEMail | mail |
| BusinessPhoneNumber | telephoneNumber |
| BusinessMobilePhone | mobile |
| BusinessFax | facsimileTelephoneNumber |
| HomeEMail |  |
| HomeFax |  |
| FirstName | givenName |
| MiddleName | initials |
| UserID | uid |
| Title | title |
| NamePrefix |  |
| Gender |  |
| IM | uid |
| BusinessVoiceMail | voicemail |
| BusinessPager | pager |
| BusinessOtherPhone |  |
| HomeMobilePhone |  |
| URL | labeledURL |