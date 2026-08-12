  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74342.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74342.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74342.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74342.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74342.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Unified Communications Manager (CallManager)](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-field-notices-list.html)


# Field Notice: FN74342 - Cisco Unified Communications Manager: SMTP May Fail to Connect After March 1, 2026 - Workaround Provided
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74342.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74342.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/743/fn74342.html)


Updated:February 18, 2026
Document ID:FN74342
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
High
**Impact Rating:**
High
**First Published:**
2025-Dec-12
**Last Published:**
2026-Feb-18
**Revision:**
1.3
**Cisco Bug IDs:**
  * [CSCwr98478](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwr98478), 
  * [CSCws04982](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws04982), 
  * [CSCws07112](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws07112), 
  * [CSCwt12200](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt12200)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| Unity Connection  | -  |   | All releases are affected.  |  
| Prime Collaboration Deployment  | -  |   | All releases are affected.  |  
| Unified Communications Manager  | -  |   | All releases are affected.  |  
| Unified Communications Manager IM and Presence Service  | -  |   | All releases are affected.  |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwr98478](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwr98478)  | CUCM may fail to connect to Microsoft 365 SMTP server after March 1, 2026  |  
| [CSCws04982](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws04982)  | PCD may fail to connect to Microsoft 365 SMTP server after March 1, 2026  |  
| [CSCws07112](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws07112)  | CUC may fail to connect to Microsoft 365 SMTP server after March 1, 2026  |  
| [CSCwt12200](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwt12200)  | IM&P may fail to connect to Microsoft 365 SMTP server after March 1, 2026  |  
  

### Problem Description
  

Cisco Unified Communications Manager (Unified CM), Cisco Prime Collaboration Deployment, and Cisco Unity Connection may fail to connect to the Microsoft 365 SMTP server after March 1, 2026.
  

### Background
  

After March 1, 2026, Microsoft will remove support for Basic Authentication with the Client Submission (SMTP AUTH) endpoints. The Microsoft 365 retiral notification of basic authentication on Microsoft 365 is available at the following link:
[Exchange Online to retire Basic auth for Client Submission (SMTP AUTH)](https://techcommunity.microsoft.com/blog/exchange/exchange-online-to-retire-basic-auth-for-client-submission-smtp-auth/4114750)
  

### Problem Symptom
  

When SMTP interfaces are configured as a client using Basic Authentication to connect with Microsoft 365, the following may be encountered after March 1, 2026:
  * Failure to send emails from Cisco Collaboration products using SMTP Basic Authentication with Microsoft 365.
  * Authentication errors or connection refusals from Microsoft 365 SMTP servers.
  * Disruption of email notifications, alerts, and workflows dependent on SMTP Basic Authentication.

  

### Workaround/Solution
  

**Workaround**
Customers are encouraged to use an intermediate SMTP Relay to communicate with the Microsoft 365 SMTP server.
  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.3  | Added Unified Communications Manager IM&P.  | Products Affected, Defect Information  | 2026-FEB-18  |  
| 1.2  | Updated product tagging for proper classification.  | —  | 2026-JAN-28  |  
| 1.1  | Updated the lInk to the Microsoft site and aligned dates to the Microsoft announcement.  | Problem Description, Background, Problem Symptom, Title  | 2025-DEC-15  |  
| 1.0  | Initial Release  | —  | 2025-DEC-12  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74342.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74342.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Communications Manager IM and Presence Service 15](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-im-presence-service-15/model.html)
  * [Unified Communications Manager IM and Presence Service Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-im-presence-service-version-14/model.html)
  * [Unified Communications Manager Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-14/model.html)
  * [Unified Communications Manager Version 15](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-15/model.html)
  * [Unity Connection Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-14/model.html)
  * [Unity Connection Version 15](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-15/model.html)

+ Show All 6 Products
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74342.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74342.html)
