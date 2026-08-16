---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-lync-integration-14-cup0-b-rcc-lync-server-integration-14-c-a50edf7b24
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/lync_integration/14/cup0_b_rcc-lync-server-integration-14/cup0_b_rcc-lync-server-integration-1251_chapter_0101.html
retrieved_at: 2026-08-16T16:34:36.442623+00:00
---

Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 14 and SUs

# Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 14 and SUs

Updated: November 27, 2025

Chapter: Normalization Rules Setup

## Chapter: Normalization Rules Setup

# Normalization Rules Setup

## Set Up Normalization Rules on Microsoft Active Directory

A reverse look-up of a directory number to username does not work under these conditions:

- the user is not provisioned for E.164 in Active Directory and

- Active Directory phone number normalization rules are not set up

Under these conditions, the application identifies the call as coming from an extension number, and the username will not
                              display in Microsoft Lync .

Therefore you must set up the correct normalization rules for the Active Directory address book on the Microsoft Lync server to enable the Microsoft Lync user to see the name of the calling party in the popup window that displays when the call is made.

You must provide a normalization rule file for extension dialing. See the sample normalization rules topic for an example.

### Before you begin

The CA-signed certificate for Microsoft Lync must be on the Microsoft Lync PC to achieve correct certificate distribution for address book synchronization. If a common CA is used to sign certificates,
                              for example Verisign or RSA, the CA certificate may already come installed on the PC.

Step 1

Ensure that normalization is enabled in Lync Server. To do this, open the Lync Server Management Shell and enter the following
                                       command:

If the UseNormalizationRules value is set to True, normalization is enabled. If the UseNormalizationRules value is set to
                                          False, enter the following command to enable normalization:

Step 2

Locate the ABFiles subdirectory in the Lync Server's shared directory that was configured during initial server deployment.
                                       Select Topology Builder > File Stores to identify the file server FQDN and share name. The path is as follows: \\<Server FQDN>\<Share Folder>\1-WebServices-1\ABFiles

Step 3

Navigate to the following sample file: C:\Program Files\Microsoft Lync Server 2010\WebComponents\Address Book Files\Files\Sample_Company_Phone_Number_Normalization_Rules.txt

Step 4

Make a copy of the Sample_Company_Phone_Number_Normalization_Rules.txt file and save it as Company_Phone_Number_Normalization_Rules.txt
                                       in the ABFiles directory.

You must save the Company_Phone_Number_Normalization_Rules.txt file in the ABFiles directory, and not where the actual address
                                                      book files are saved.

Step 5

Open the Company_Phone_Number_Normalization_Rules.txt file in Notepad and remove regex code like [\s()\-\./]* . Microsoft Lync Server ignores non-telephony related digits and only analyzes the continuous 0-9 numerical digit patterns.
                                       However it does recognize the + prefix.

Step 6

In Lync Server Management Shell, enter the following command to import the new settings in the Company_Phone_Number_Normalization_Rules.txt
                                       file and apply them to numbers stored in the address book files:

Step 7

Wait for five before you force an address book update on the Lync client, see Update Microsoft Lync Address Book .

### What to do next

Update Microsoft Lync Address Book

### Sample Normalization Rules

```
## +1 (ddd) ddd-dddd EXTddddd
#
\+1(\d{10})EXT(\d{5})
+1$1;ext=$2
#
# +1 (ddd) ddd-dddd Xddddd
#
\+1(\d{10})[Xx]{1}(\d{5})
+1$1;ext=$2
#
# 1 (ddd) ddd-dddd
#
1(\d{10})
+1$1
#
# +1 (ddd) 70ddddd
#
\+1(\d{3})70(\d{5})
+1$170$2;ext=$2
#
# 70d-dddd Xddddd
#
70(\d{5})[Xx]{1}(\d{5})
+142570$1;ext=$2
#
# ddd-dddd Xddddd
#
(\d{7})[Xx]{1}(\d{5})
+1425$1;ext=$2
```

## Update Microsoft Lync Address Book

With the default server/client settings, the Address Book is not immediately updated. To ensure that the Address Book is updated
                              with the latest users added to the Active Directory, you must force the update on the server side and then force Microsoft Lync to pull down the latest files to update its local GalContacts.db file.

Step 1

On Lync Server, enter the following command in the Lync Server Management Shell:

This command triggers the Lync Server to synchronize current Active Directory information in the SQL database into the downloadable
                                          client and device address book files.

Wait five minutes for the synchronization process to complete.

Step 2

With Administrator  privileges on Microsoft Lync , enter the following command in the Windows Command Prompt:

This command forces Microsoft Lync to immediately download the address book.

Step 3

Check whether the GalContacts.db and GalContacts.db.idx files exist on Microsoft Lync . If they do exist, delete them from the user's profile directory.

Step 4

Exit Microsoft Lync . Do not just sign out.

Step 5

Start the Microsoft Lync client and sign in again.

Step 6

Verify that the updated GalContacts.db and GalContacts.db.idx files have been downloaded.

Step 7

Perform a search for the new users and verify that their usernames display in Microsoft Lync .

### What to do next

Security Certificate Setup for IM and Presence Service

| Note | You must provide a normalization rule file for extension dialing. See the sample normalization rules topic for an example. |
|---|---|

| Step 1 | Ensure that normalization is enabled in Lync Server. To do this, open the Lync Server Management Shell and enter the following
                                       command: Get-CsAddressBookConfiguration If the UseNormalizationRules value is set to True, normalization is enabled. If the UseNormalizationRules value is set to
                                          False, enter the following command to enable normalization: Set-CsAddressBookConfiguration -UseNormalizationRules $True |
|---|---|
| Step 2 | Locate the ABFiles subdirectory in the Lync Server's shared directory that was configured during initial server deployment.
                                       Select Topology Builder > File Stores to identify the file server FQDN and share name. The path is as follows: \\<Server FQDN>\<Share Folder>\1-WebServices-1\ABFiles |
| Step 3 | Navigate to the following sample file: C:\Program Files\Microsoft Lync Server 2010\WebComponents\Address Book Files\Files\Sample_Company_Phone_Number_Normalization_Rules.txt |
| Step 4 | Make a copy of the Sample_Company_Phone_Number_Normalization_Rules.txt file and save it as Company_Phone_Number_Normalization_Rules.txt
                                       in the ABFiles directory. Note You must save the Company_Phone_Number_Normalization_Rules.txt file in the ABFiles directory, and not where the actual address
                                                      book files are saved. | Note | You must save the Company_Phone_Number_Normalization_Rules.txt file in the ABFiles directory, and not where the actual address
                                                      book files are saved. |
| Note | You must save the Company_Phone_Number_Normalization_Rules.txt file in the ABFiles directory, and not where the actual address
                                                      book files are saved. |
| Step 5 | Open the Company_Phone_Number_Normalization_Rules.txt file in Notepad and remove regex code like [\s()\-\./]* . Microsoft Lync Server ignores non-telephony related digits and only analyzes the continuous 0-9 numerical digit patterns.
                                       However it does recognize the + prefix. |
| Step 6 | In Lync Server Management Shell, enter the following command to import the new settings in the Company_Phone_Number_Normalization_Rules.txt
                                       file and apply them to numbers stored in the address book files: Update-CsAddressBook |
| Step 7 | Wait for five before you force an address book update on the Lync client, see Update Microsoft Lync Address Book . |

| Note | You must save the Company_Phone_Number_Normalization_Rules.txt file in the ABFiles directory, and not where the actual address
                                                      book files are saved. |
|---|---|

| Step 1 | On Lync Server, enter the following command in the Lync Server Management Shell: Update-CsAddressBook This command triggers the Lync Server to synchronize current Active Directory information in the SQL database into the downloadable
                                          client and device address book files. Note Wait five minutes for the synchronization process to complete. | Note | Wait five minutes for the synchronization process to complete. |
|---|---|---|---|
| Note | Wait five minutes for the synchronization process to complete. |
| Step 2 | With Administrator  privileges on Microsoft Lync , enter the following command in the Windows Command Prompt: reg add HKLM\Software\Policies\Microsoft\Communicator /v GalDownloadInitialDelay /t REG_DWORD /d 0 /f This command forces Microsoft Lync to immediately download the address book. |
| Step 3 | Check whether the GalContacts.db and GalContacts.db.idx files exist on Microsoft Lync . If they do exist, delete them from the user's profile directory. |
| Step 4 | Exit Microsoft Lync . Do not just sign out. |
| Step 5 | Start the Microsoft Lync client and sign in again. |
| Step 6 | Verify that the updated GalContacts.db and GalContacts.db.idx files have been downloaded. |
| Step 7 | Perform a search for the new users and verify that their usernames display in Microsoft Lync . |

| Note | Wait five minutes for the synchronization process to complete. |
|---|---|