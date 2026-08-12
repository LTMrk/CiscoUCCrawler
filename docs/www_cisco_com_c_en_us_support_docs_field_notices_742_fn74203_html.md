  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74203.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74203.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74203.html)


  * [Cisco.com Worldwide](https://www.cisco.com/site/us/en/index.html)
  * [Products and Services](https://www.cisco.com/site/us/en/products/index.html)
  * [Solutions](https://www.cisco.com/site/us/en/solutions/index.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Learn](https://www.cisco.com/site/us/en/learn/index.html)
  * [Explore Cisco](https://www.cisco.com/site/us/en/about/sitemap.html)
  * [How to Buy](https://www.cisco.com/site/us/en/buy/index.html)
  * [Partners Home](https://www.cisco.com/site/us/en/partners/index.html)
  * [Partner Program](https://www.cisco.com/site/us/en/partners/360-partner-program/partner-program/index.html)
  * [Support](https://www.cisco.com/site/us/en/partners/support-help/index.html)
  * [Tools](https://www.cisco.com/site/us/en/partners/360-partner-program/tools-training/index.html)
  * [Find a Cisco Partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
  * [Meet our Partners](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html)
  * [Become a Cisco Partner](https://www.cisco.com/site/us/en/partners/index.html)


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74203.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74203.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Unity Connection](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-field-notices-list.html)


# Field Notice: FN74203 - Cisco Unity Connection Unified Messaging with Microsoft 365, Voicemail Stored in Cisco Unity Connection Will Not Sync with Exchange Online (Outlook) Email Inbox - Software Upgrade Recommended
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/742/fn74203.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74203.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/742/fn74203.html)


Updated:November 15, 2024
Document ID:FN74203
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
High
**Impact Rating:**
High
**First Published:**
2024-Nov-15
**Last Published:**
2024-Nov-15
**Revision:**
1.0
**Cisco Bug IDs:**
  * [CSCwm41395](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwm41395)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  

  
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| Unity Connection Updates  | 12  | 12.5(1), 12.5(1)SU1, 12.5(1)SU2, 12.5(1)SU3, 12.5(1)SU4, 12.5(1)SU5, 12.5(1)SU6, 12.5(1)SU7  |   |  
| Unity Connection Updates  | 14  | 14  |   |  
| Unity Connection Updates  | 14SU1  | 14SU1  |   |  
| Unity Connection Updates  | 14SU2  | 14SU2  |   |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwm41395](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwm41395)  | Retirement of RBAC Application Impersonation in Exchange Online  |  
  

### Problem Description
  

After February 2025, voicemails that are stored in Cisco Unity Connection will not sync with Microsoft 365 Exchange Online (Outlook) Email Inbox. Microsoft has announced that they will retire the Application Impersonation role and its feature set in February 2025. Once this occurs, it will break the synchronization between Cisco Unity Connection and the Microsoft 365 Single Inbox feature as Cisco Unity Connection uses the Application Impersonation role to connect to Microsoft 365. 
  

### Background
  

Cisco Unity Connection uses the Microsoft Application Impersonation role and its feature set to connect with Microsoft 365 Exchange Online (Outlook) as part of the Single Inbox feature in the Unified Messaging service. Cisco Unity Connection uses this service account to authenticate to Exchange Online and to perform Exchange Web Services API calls to Exchange Online. The service account user is assigned to the Application Impersonation role for authentication and to sync voice messages with Exchange Online.
Microsoft has announced the retirement of the Application Impersonation role and its feature set in February 2025.
After February 2025, Unified Messaging service accounts will not be able to use the Application Impersonation role to connect to Microsoft 365 because this role and its feature set will be removed. This will impact the Single Inbox feature and will break the synchronization between Cisco Unity Connection and Microsoft 365.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/742/fn74203_a3a8fc598789da104dc14047cebb35c9.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/742/fn74203_a3a8fc598789da104dc14047cebb35c9.png "Related image, diagram or screenshot.")
  

### Problem Symptom
  

After February 2025, voicemails that are stored in Cisco Unity Connection will not sync with an Exchange Online email inbox when the Single Inbox feature is being used in the Cisco Unity Connection Unified Messaging service.
  

### Workaround/Solution
  

**Solution**
Cisco recommends upgrading Cisco Unity Connection and configuring the Unified Messaging service with Microsoft 365 using Oauth2.0 with client credentials.
Customers are advised to upgrade to an appropriate [fixed software release](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes) as indicated in the following table:  
| Cisco Unity Connection Release  | Fixed Release  |  
| --- | --- |  
| 12.5(1)  
12.5(1) SU1  
12.5(1) SU2  
12.5(1) SU3  
12.5(1) SU4  
12.5(1) SU5  
12.5(1) SU6  
12.5(1) SU7  
12.5(1) SU8  |  12.5(1) SU81 **Note:** Although this issue is addressed in 12.5(1) SU8, Cisco recommends that customers upgrade to Cisco Unity Connection Release 15.  |  
| 14  
14 SU1  
14 SU2  |  14 SU31 **Note:** Although this issue is addressed in 14 SU3, Cisco recommends that customers upgrade to Cisco Unity Connection Release 15.  |  
1. If a customer has subscribed to SpeechView, they should upgrade to either Cisco Unity Connection Release 14 SU4 or Release 15 SU2.
**Notes:**
  * Only Cisco Unity Connection releases 12.5(1) SU8 and later or releases 14 SU3 and later will support the Single Inbox feature in the Unified Messaging service after February 2025. Customers that are using Single Inbox are encouraged to upgrade to these releases.
  * If a customer has subscribed to SpeechView, a transcription service offered through Cisco Unity Connection, they should upgrade to Cisco Unity Connection Release 14 SU4 or Release 15 SU2. For more information, see [Cisco Unity Connection SpeechView Transcription Service Will Stop Working after December 30, 2024](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74144.html).


Cisco has migrated to Oauth2.0 with client credentials flow. To configure the Unified Messaging service with Microsoft 365 using Oauth2.0 with client credentials flow, see the Task List for Configuring Unified Messaging with Office 365 section in the following documents:
  * [Unified Messaging Guide for Cisco Unity Connection Release 12.5(1)](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/unified_messaging/b_12xcucumgx/b_12xcucumgx_chapter_01.html#ID-2370-000005f5)
  * [Unified Messaging Guide for Cisco Unity Connection Release 14](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/unified_messaging/guide/b_14cucumgx/b_14cucumgx_chapter_01.html#ID-2370-000005f5)

  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.0  | Initial Release  | —  | 2024-NOV-15  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74203.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74203.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unity Connection](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/series.html)
  * [Unity Connection Version 12.x](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-12-x/model.html)
  * [Unity Connection Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-14/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/742/fn74203.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74203.html)
