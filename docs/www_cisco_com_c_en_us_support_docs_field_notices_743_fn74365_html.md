  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74365.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74365.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74365.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74365.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74365.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Unity Connection](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-field-notices-list.html)


# Field Notice: FN74365 - Cisco Unity Connection Unified Messaging with Microsoft 365 - Voicemail Stored in Cisco Unity Connection Will Not Sync with Exchange Online (Outlook) Due to EWS Deprecation - Software Upgrade Recommended
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74365.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74365.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/743/fn74365.html)


Updated:April 15, 2026
Document ID:FN74365
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
High
**Impact Rating:**
High
**First Published:**
2026-Apr-15
**Last Published:**
2026-Apr-15
**Revision:**
1.0
**Cisco Bug IDs:**
  * [CSCwp95908](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwp95908)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| Unity Connection Updates  | 14  | 14  | All releases are affected.  |  
| Unity Connection Updates  | 14SU1  | 14SU1  |   |  
| Unity Connection Updates  | 14SU2  | 14SU2  |   |  
| Unity Connection Updates  | 14SU3  | 14SU3  |   |  
| Unity Connection Updates  | 14SU3a  | 14SU3a  |   |  
| Unity Connection Updates  | 14SU4  | 14SU4  |   |  
| Unity Connection Updates  | 14SU5  | 14SU5  |   |  
| Unity Connection Updates  | 14SU6  | 14SU6  |   |  
| Unity Connection Updates  | 15  | 15  | All releases earlier than 15 SU4 are affected.  |  
| Unity Connection Updates  | 15SU1  | 15SU1  |   |  
| Unity Connection Updates  | 15SU2  | 15SU2  |   |  
| Unity Connection Updates  | 15SU3  | 15SU3  |   |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwp95908](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwp95908)  | Implement Graph API support for office 365 in unity connection.  |  
  

### Problem Description
  

Cisco Unity Connection uses Exchange Web services (EWS) for syncing Voicemail deposited on unity with Microsoft 365 (Exchange online) and on-prem Exchange. Beginning October 1, 2026, Cisco Unity Connection will not sync voicemail with Microsoft 365 as Microsoft will start deprecating Exchange Web Service (EWS) for Exchange online alone (not for on-prem exchange).
  

### Background
  

Microsoft is deprecating EWS for third-party applications to integrate with Microsoft 365 and replacing it with Graph API. Beginning October 1, 2026, Microsoft will block EWS requests from non-Microsoft apps (including Cisco Unity Connection) to Microsoft 365.
**Microsoft announcement:** [Retirement of Exchange Web Services in Exchange Online](https://techcommunity.microsoft.com/blog/exchange/retirement-of-exchange-web-services-in-exchange-online/3924440)
**Note:** This applies only to Microsoft 365 and Exchange Online (all environments). There are no changes to EWS in Exchange Server. EWS will continue to be fully supported for Exchange on-premises mailboxes.
  

### Problem Symptom
  

Voicemail, which is stored in Cisco Unity Connection, will not sync with the Microsoft 365 - Exchange (Outlook) email inbox when using the Single Inbox (Unified Messaging Service) feature.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74365_7708f6a0878007504dc14047cebb3577.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74365_7708f6a0878007504dc14047cebb3577.jpg "Related image, diagram or screenshot.")
Cisco Unity Connection users will not be able to read voice messages using Microsoft 365 (Outlook).
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74365_2c583aa0878007504dc14047cebb3580.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74365_2c583aa0878007504dc14047cebb3580.jpg "Related image, diagram or screenshot.")
Administrators will see the error **Failed to Connect to Microsoft endpoint using https://outlook.office365.com** when choosing the **Test** function in the Cisco Unity Connection admin console. 
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74365_8ed87624878007504dc14047cebb3563.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74365_8ed87624878007504dc14047cebb3563.jpg "Related image, diagram or screenshot.")
  

### Workaround/Solution
  

**Solution**
Cisco Unity Connection will migrate to Graph API in releases 15 SU4 and later. Upgrade to Release 15 SU4 before October 1, 2026, as shown in the following table. Upgrading is the only option to sustain Unified Messaging Service.  
| Cisco Unity Connection Release  | Affected Build number  | First Fixed Release  |  
| --- | --- | --- |  
| 14  | 14.0.1.10000-19  | 15 SU4  |  
| 14 SU1  | 14.0.1.11900-128  |  
| 14 SU2  | 14.0.1.12900-69  |  
| 14 SU3  | 14.0.1.13900-70  |  
| 14 SU3a  | 14.0.1.13901-2  |  
| 14 SU4  | 14.0.1.14900-36  |  
| 14 SU5  | 14.0.1.15900-25  |  
| 14 SU6  | 14.0.1.16900-10  |  
| 15  | 15.0.1.10000-24  | 15 SU4  |  
| 15 SU1  | 15.0.1.11900-14  |  
| 15 SU2  | 15.0.1.12900-43  |  
| 15 SU3  | 15.0.1.13900-61  |  
  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.0  | Initial Release  | —  | 2026-APR-15  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74365.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74365.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unity Connection Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-14/model.html)
  * [Unity Connection Version 15](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-15/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74365.html)
