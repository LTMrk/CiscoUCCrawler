---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-212109-how-to-use-ldp-exe-to-search-ldap-server-html-f4cf2d5e7e
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/212109-How-to-Use-LDP-EXE-to-Search-LDAP-Server.html
retrieved_at: 2026-08-20T22:13:58.909855+00:00
---

How to Use ldp.exe to Search LDAP Servers

# How to Use ldp.exe to Search LDAP Servers

Updated: July 9, 2018

Document ID: 212109

Contents

## Contents

## Introduction

This document describes how to troubleshoot Lightweight Directory Access Protocol (LDAP) issues related to Jabber with a tool that allows you to search the LDAP directory the same way as Jabber.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- LDAP

- Jabber

### Components Used

This document is not restricted to specific software and hardware versions

## Install ldp.exe and Connect/Bind to Your Server

Step 1. Open the  in order to download the .zip file that contains the tool. Once you download the file, unzip it.

Step 2. Open the ldp.exe tool.

Step 3. You must connect to your Server and then bind to it. Choose Connection > Connect and enter your server's IP address or Fully Qualified Domain Name (FQDN). Click OK .

Step 4.Choose Connection > Bind . Enter your credentials and your domain. Click OK .

Step 5. Verify that you are Authenticated as dn:'username' . You are now ready to proceed to search the LDAP directory.

## Search Your LDAP Directory with ldp.exe

You need a search base filter to proceed. An example is:

When you have a search base filter, choose Browse > Search .

Depending on the Search Base you used, you can modify your scope. In this example, One Level is used. At this point you can enter your search filter and click Run .

For example, to see all users enter (&(objectCategory=person)(objectClass=user)) .

## Sample Searches That Can Prove Helpful

&(givenName=Fareed)(objectClass=user))

Specific Users based on First Name

### Full LDAP Attributes List

First Name

givenName

Middle Name / Initials

initials

Last Name

sn

Logon Name

userPrincipalName

Logon Name (Pre Windows 2000)

sAMAccountName

Display Name

displayName

Full Name

name/cn

Description

description

Office

physicalDeliveryOfficeName

Telephone Number

telephoneNumber

Email

mail

Web Page

wWWHomePage

Password

password

Street

streetAddress

PO Box

postOfficeBox

City

l

State/Province

st

Zip/Postal Code

postalCode

Country

co

Country 2 Digit Code - eg. US

c

Country code -eg. for US country code is 840

countryCode

Group

memberOf

Account Expires (use same date format as server)

accountExpires

User Account Control

userAccountControl

Profile Path

profilePath

Log in Script

scriptPath

Home Folder

homeDirectory

Home Drive

homeDrive

Log on to

userWorkstations

Home

homePhone

Pager

pager

Mobile

mobile

Fax

facsimileTelephoneNumber

IP Phone

ipPhone

Notes

info

Title

title

Department

department

Company

company

Manager

manager

Mail Alias

mailNickName

Simple Display Name

displayNamePrintable

Hide from Exchange address lists

msExchHideFromAddressLists

Sending Message Size (KB)

submissionContLength

Receiving Message Size (KB)

delivContLength

Accept messages from Authenticated Users only

msExchRequireAuthToSendTo

Reject Messages From

unauthOrig

Accept Messages From

authOrig

Send on Behalf

publicDelegates

Forward To

altRecipient

Deliver and Redirect

deliverAndRedirect

Reciepient Limits

msExchRecipLimit

Use mailbox store defaults

mDBuseDefaults

Issue Warning at (KB)

mDBStorageQuota

Prohibit Send at (KB)

mDBOverQuotaLimit

Prohibit Send and receive at (KB)

mDBOverHardQuotaLimit

Do not permanently delete messages until the store has been backed up

deletedItemFlags

keep deleted items for (days)

garbageCollPeriod

Outlook Mobile Access

msExchOmaAdminWirelessEnable

Outlook Web Access

protocolSettings

Allow Terminal Server Logon

tsAllowLogon

Terminal Services Profile Path

tsProfilePath

Terminal Services Home Directory

tsHomeDir

Terminal Services Home Drive

tsHomeDirDrive

Start the following program at logon

tsInheritInitialProgram

Starting Program file name

tsIntialProgram

Start in

tsWorkingDir

Connect client drive at logon

tsDeviceClientDrives

Connect client printer at logon

tsDeviceClientPrinters

Default to main client printer

tsDeviceClientDefaultPrinter

End disconnected session

tsTimeOutSettingsDisConnections

Active Session limit

tsTimeOutSettingsConnections

Idle session limit

tsTimeOutSettingsIdle

When session limit reached or connection broken

tsBrokenTimeOutSettings

Allow reconnection

tsReConnectSettings

Remote Control

tsShadowSettings

Protect accidental deletion

preventDeletion

Manager can update members

managerCanUpdateMembers

You can also check out the Micrsoft Search Filter Syntax Page for more insight on the syntax.

### Contributed by Cisco Engineers

Fareed Warrad

Cisco TAC Engineer

Edited by Deepak Kumar

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber

| CN=users,DC=farewarr,DC=com |
|---|

| (&(objectCategory=person)(objectClass=user)) | All Users |
|---|---|
| (&(sAMAccountName=fwarrad)(objectClass=user)) | Specific User based on ID |
| (&(sn=Warrad)(objectClass=user)) | Specific users based on lastname |
| &(givenName=Fareed)(objectClass=user)) | Specific Users based on First Name |

| Name in AD | LDAP Attribute Name |
|---|---|
| First Name | givenName |
| Middle Name / Initials | initials |
| Last Name | sn |
| Logon Name | userPrincipalName |
| Logon Name (Pre Windows 2000) | sAMAccountName |
| Display Name | displayName |
| Full Name | name/cn |
| Description | description |
| Office | physicalDeliveryOfficeName |
| Telephone Number | telephoneNumber |
| Email | mail |
| Web Page | wWWHomePage |
| Password | password |
| Street | streetAddress |
| PO Box | postOfficeBox |
| City | l |
| State/Province | st |
| Zip/Postal Code | postalCode |
| Country | co |
| Country 2 Digit Code - eg. US | c |
| Country code -eg. for US country code is 840 | countryCode |
| Group | memberOf |
| Account Expires (use same date format as server) | accountExpires |
| User Account Control | userAccountControl |
| Profile Path | profilePath |
| Log in Script | scriptPath |
| Home Folder | homeDirectory |
| Home Drive | homeDrive |
| Log on to | userWorkstations |
| Home | homePhone |
| Pager | pager |
| Mobile | mobile |
| Fax | facsimileTelephoneNumber |
| IP Phone | ipPhone |
| Notes | info |
| Title | title |
| Department | department |
| Company | company |
| Manager | manager |
| Mail Alias | mailNickName |
| Simple Display Name | displayNamePrintable |
| Hide from Exchange address lists | msExchHideFromAddressLists |
| Sending Message Size (KB) | submissionContLength |
| Receiving Message Size (KB) | delivContLength |
| Accept messages from Authenticated Users only | msExchRequireAuthToSendTo |
| Reject Messages From | unauthOrig |
| Accept Messages From | authOrig |
| Send on Behalf | publicDelegates |
| Forward To | altRecipient |
| Deliver and Redirect | deliverAndRedirect |
| Reciepient Limits | msExchRecipLimit |
| Use mailbox store defaults | mDBuseDefaults |
| Issue Warning at (KB) | mDBStorageQuota |
| Prohibit Send at (KB) | mDBOverQuotaLimit |
| Prohibit Send and receive at (KB) | mDBOverHardQuotaLimit |
| Do not permanently delete messages until the store has been backed up | deletedItemFlags |
| keep deleted items for (days) | garbageCollPeriod |
| Outlook Mobile Access | msExchOmaAdminWirelessEnable |
| Outlook Web Access | protocolSettings |
| Allow Terminal Server Logon | tsAllowLogon |
| Terminal Services Profile Path | tsProfilePath |
| Terminal Services Home Directory | tsHomeDir |
| Terminal Services Home Drive | tsHomeDirDrive |
| Start the following program at logon | tsInheritInitialProgram |
| Starting Program file name | tsIntialProgram |
| Start in | tsWorkingDir |
| Connect client drive at logon | tsDeviceClientDrives |
| Connect client printer at logon | tsDeviceClientPrinters |
| Default to main client printer | tsDeviceClientDefaultPrinter |
| End disconnected session | tsTimeOutSettingsDisConnections |
| Active Session limit | tsTimeOutSettingsConnections |
| Idle session limit | tsTimeOutSettingsIdle |
| When session limit reached or connection broken | tsBrokenTimeOutSettings |
| Allow reconnection | tsReConnectSettings |
| Remote Control | tsShadowSettings |
| Protect accidental deletion | preventDeletion |
| Manager can update members | managerCanUpdateMembers |