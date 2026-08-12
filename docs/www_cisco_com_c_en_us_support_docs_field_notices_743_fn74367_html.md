  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74367.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74367.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74367.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74367.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74367.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Unified Communications Manager (CallManager)](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-field-notices-list.html)


# Field Notice: FN74367 - Cisco Unified Communications Manager IM and Presence Rich Presence Based on Microsoft 365 Calendar Integration Will Not Get Updated - Software Upgrade Recommended
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74367.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74367.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/743/fn74367.html)


Updated:February 6, 2026
Document ID:FN74367
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
High
**Impact Rating:**
High
**First Published:**
2026-Feb-06
**Last Published:**
2026-Feb-06
**Revision:**
1.0
**Cisco Bug IDs:**
  * [CSCwp67350](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwp67350)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| Unified Communications Manager IM and Presence Service  | -  |   |   |  
| Unified Communications Manager Updates  | 14  | 14  |   |  
| Unified Communications Manager Updates  | 14SU1  | 14SU1  |   |  
| Unified Communications Manager Updates  | 14SU2  | 14SU2  |   |  
| Unified Communications Manager Updates  | 14SU3  | 14SU3  |   |  
| Unified Communications Manager Updates  | 14SU4  | 14SU4  |   |  
| Unified Communications Manager Updates  | 14SU4a  | 14SU4a  |   |  
| Unified Communications Manager Updates  | 14SU5  | 14SU5  |   |  
| Unified Communications Manager Updates  | 15  | 15  |   |  
| Unified Communications Manager Updates  | 15SU1  | 15SU1  |   |  
| Unified Communications Manager Updates  | 15SU1a  | 15SU1a  |   |  
| Unified Communications Manager Updates  | 15SU2  | 15SU2  |   |  
| Unified Communications Manager Updates  | 15SU3  | 15SU3  |   |  
| Unified Communications Manager Updates  | 15SU3a  | 15SU3a  |   |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwp67350](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwp67350)  | Implement migration from EWS to Microsoft Graph API in IM&P  |  
  

### Problem Description
  

Cisco Unified Communications Manager IM and Presence (Unified CM IM&P) will not get calendar status from users of Microsoft 365 Exchange beginning October 1, 2026, because Microsoft is retiring Exchange Web Services (EWS) APIs. 
Microsoft 365 calendar integration with Cisco Unified CM IM&P allows users to incorporate their calendar and meeting status in Microsoft Outlook into their availability status on the Cisco Unified CM IM&P Service. This integration can be accomplished by connecting the Cisco Unified CM IM&P Service to Microsoft 365 through EWS. 
  

### Background
  

Microsoft is deprecating EWS for third-party applications to integrate with Microsoft 365 and replacing it with Graph API. Starting October 1, 2026, Microsoft will block EWS requests from non-Microsoft apps to Microsoft 365.
**Microsoft announcement:** [Retirement of Exchange Web Services in Exchange Online](https://techcommunity.microsoft.com/blog/exchange/retirement-of-exchange-web-services-in-exchange-online/3924440)
**Note:** This applies only to Microsoft 365 and Exchange Online (all environments). There are no changes to EWS in Exchange Server. EWS will continue to be fully supported for Exchange on-premises mailboxes.
  

### Problem Symptom
  

Beginning October 1, 2026, Cisco Unified CM IM&P will not get calendar status from users of Microsoft 365 Exchange.
Calendar status is a specific presence status that represents the free/busy status of users based on their calendar.
[![A screenshot of a computer](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74367_72b4b196c31efa502f7fdbbf0501314e.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/743/fn74367_72b4b196c31efa502f7fdbbf0501314e.png "A screenshot of a computer")
With EWS retirement in Microsoft 365, Cisco Unified CM IM&P will not be able to incorporate **In meeting** and **Out of Office** calendar statuses as the overall user status. 
  

### Workaround/Solution
  

**Solution**
Cisco Unified CM IM&P Service will migrate to Graph API in releases 15SU4 and later. Upgrade to Release 15SU4 before October 1, 2026, as shown in the following table. Upgrading is the only option to sustain calendar integration.  
| Cisco Unified CM IM&P Release  | First Fixed Release  |  
| --- | --- |  
| 14, 14 SU1, 14 SU2, 14 SU3, 14 SU3a, 14 SU4, 14 SU5  | Migrate to a fixed release  |  
| 15, 15 SU1, 15 SU2, 15 SU3  | 15 SU4  |  
  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.0  | Initial Release  | —  | 2026-FEB-06  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74367.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Customers Also Viewed
  * [Field Notice: FN74345 - Cisco On-Premises Calling Products: Impact on Secure Communication Due to Upcoming Changes to TLS certificates Issued by Public Certificate Authorities with Client Authentication EKU, Starting May 2026 - Workaround Provided](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74345.html)
  * [Regenerate Certificates In Unified Communications Manager](https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/214231-certificate-regeneration-process-for-cis.html)
  * [Troubleshoot CUCM Database Replication Issues](https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200396-Steps-to-Troubleshoot-Database-Replicati.html)
  * [Install CUCM Cluster Using Data Export and Import Feature](https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/222244-install-cucm-cluster-using-data-export-a.html)
  * [Collect Trace Data from a CUCM Cluster](https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/200787-How-to-Collect-Traces-for-CUCM-9-x-10-x.html)
  * [Reset or Change CUCM OS Admin and Security Password](https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213527-changing-cucm-os-admin-and-security-pass.html)
  * + Show 3 More


### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74367.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Communications Manager IM and Presence Service Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-im-presence-service-version-14/model.html)
  * [Unified Communications Manager Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-14/model.html)
  * [Unified Communications Manager Version 15](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-15/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74367.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74367.html)
By continuing to use our website, you acknowledge the use of cookies. 
[Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html) Change Settings
![Company Logo](https://cdn.cookielaw.org/logos/03fc55fe-0057-4b2f-817d-763e7ecdb316/a7f4c642-c43c-4666-acea-858c0449029c/cisco-logo-transparent.png)
## Consent Manager
Your opt out preference signal is honored.
## Consent Manager
  * ### Your Privacy
  * ### Strictly Necessary Cookies
  * ### Performance Cookies
  * ### Targeting Cookies
  * ### Functional Cookies


#### Your Privacy
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. From the list on left, please choose whether this site may use Performance and/or Targeting Cookies. By selecting Strictly Necessary Cookies only, you are requesting Cisco not to sell or share your personal data. Note, blocking some types of cookies may impact your experience on the site and the services we are able to offer.
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies provide metrics related to the performance and usability of our site. They are primarily focused on gathering information about how you interact with our site, including: page load times, response times, error messages, and allowing a replay of a visitor’s interactions with our site, which enables us to review and analyze visitor behavior, helping to improve site usability and functionality. These cookies also allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. If you do not allow these cookies we will not know when you have visited our site and will not be able to monitor its performance.
Cookies Details
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Cookies Details
Back Button
### Cookie List
Filter Button
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Clear
  * checkbox label label


Apply Cancel
Save Settings
Allow All
[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/solutions/consent-and-preferences/)
