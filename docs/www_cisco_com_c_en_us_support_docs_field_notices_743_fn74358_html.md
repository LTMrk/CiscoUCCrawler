  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74358.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74358.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74358.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74358.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74358.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Expressway Series](https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-field-notices-list.html)


# Field Notice: FN74358 - Cisco Expressway: SMTP May Fail to Connect After March 1, 2026 - Workaround Provided
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74358.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74358.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/743/fn74358.html)


Updated:December 19, 2025
Document ID:FN74358
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
High
**Impact Rating:**
High
**First Published:**
2025-Dec-19
**Last Published:**
2025-Dec-19
**Revision:**
1.0
**Cisco Bug IDs:**
  * [CSCws03948](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws03948)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| Expressway Core and Edge  | X14  | X14.0.0, X14.0.1, X14.0.10, X14.0.11, X14.0.2, X14.0.3, X14.0.4, X14.0.5, X14.0.6, X14.0.7, X14.0.8, X14.0.9, X14.2.0, X14.2.1, X14.2.2, X14.2.5, X14.2.6, X14.2.7, X14.3.0, X14.3.1, X14.3.2, X14.3.3, X14.3.4, X14.3.5, X14.3.6, X14.3.7  | All releases are affected  |  
| Expressway Core and Edge  | X15  | X15.0.0, X15.0.1, X15.0.2, X15.0.3, X15.2.0, X15.2.1, X15.2.2, X15.2.3, X15.2.4, X15.2.4., X15.3.0, X15.3.1  | All releases are affected  |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCws03948](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws03948)  | Expressway may fail to connect to Microsoft 365 SMTP server after March 1, 2026  |  
  

### Problem Description
  

Cisco Expressway may fail to connect to the Microsoft 365 SMTP server after March 1, 2026.
  

### Background
  

After March 1, 2026, Microsoft will no longer support Basic authentication with Client Submission (SMTP AUTH) endpoints. The notification about the retirement of Basic authentication on Microsoft 365 is available at the following link: <https://techcommunity.microsoft.com/blog/exchange/exchange-online-to-retire-basic-auth-for-client-submission-smtp-auth/4114750>
  

### Problem Symptom
  

After March 1, 2026, Cisco Expressway SMTP interfaces that are configured as clients using Basic authentication to connect with Microsoft 365 may encounter the following issues:
  * Failure to send emails from Cisco Expressway using SMTP Basic authentication with Microsoft 365
  * Authentication errors or connection refusals from Microsoft 365 SMTP servers
  * Disruption of email notifications, alerts, and workflows that are dependent on SMTP Basic authentication

  

### Workaround/Solution
  

Customers are encouraged to use an intermediate SMTP relay to communicate with the Microsoft 365 SMTP server.
  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.0  | Initial Release  | —  | 2025-DEC-19  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74358.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74358.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74358.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74358.html)
