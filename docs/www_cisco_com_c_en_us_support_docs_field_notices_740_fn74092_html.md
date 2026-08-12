  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/740/fn74092.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/740/fn74092.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/740/fn74092.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/740/fn74092.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/740/fn74092.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Jabber for Android](https://www.cisco.com/c/en/us/support/unified-communications/jabber-android/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/jabber-android/products-field-notices-list.html)


# Field Notice: FN74092 - Cisco Unified Communications Manager and Unified Communications Manager IM & Presence Service Push Notifications May Not Work On or After March 29, 2024 - Configuration Change Recommended
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/740/fn74092.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/740/fn74092.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/740/fn74092.html)


Updated:December 19, 2023
Document ID:FN74092
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| Unified Communications Manager  | 11  | 11.5(1)  | All versions  |  
| Unified Communications Manager IM & Presence Service  | 11  | 11.5(1)  | All versions  |  
| Unified Communications Manager  | 12  | 12.5(1)  | All versions  |  
| Unified Communications Manager IM & Presence Service  | 12  | 12.5(1)  | All versions  |  
| Unified Communications Manager  | 14  | 14  | All versions  |  
| Unified Communications Manager IM & Presence Service  | 14  | 14  | All versions  |  
| Unified Communications Manager  | 15  | 15  | All versions  |  
| Unified Communications Manager IM & Presence Service  | 15  | 15  | All versions  |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwi16238](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwi16238)  | Push notifications will not work due to an IP address change with the Cisco Push REST service  |  
  

### Problem Description
  

Cisco customers who use Cisco Unified Communications Manager (Unified CM) or Cisco Unified Communication IM & Presence Service (IM&P) to manage push notifications may experience a failure of push notifications on or after March 29, 2024, for the following clients:
  * Cisco Jabber
  * Cisco Webex applications
  * Apple Push Notifications Service (APNS)
  * Google Firebase Cloud Messaging (FCM) 


This issue is due to the migration of the data center that hosts the Cisco-hosted Push REST service.
  

### Background
  

When a cluster is enabled for push notifications, Cisco Unified CM and Cisco Unified Communication IM&P use the Cisco Push REST service in the Cisco cloud to send push notifications to either the Apple Push Notification Service (APNS) or the Google Firebase Cloud Messaging (FCM) Push Notification service, which send push notifications to compatible Cisco Jabber (for messaging and calling) or Cisco Webex App clients (for calling) that run on Apple iOS or Android devices. Push notifications allow the system to communicate with the client even after the client has entered into background mode (also known as suspended mode). On March 29, 2024, Cisco will migrate the Cisco Push REST service from one data center to another.
  

### Problem Symptom
  

Push notifications that are sent from Cisco Unified CM and Cisco Unified Communication IM&P may fail to reach Cisco Jabber as well as Cisco Webex Application for Apple iOS and Android mobile clients on or after March 29, 2024.
  

### Workaround/Solution
  

**Solution**
The recommended method of configuration is, as stated in [Push Notifications Prerequisites](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/push_notifications/cucm_b_push-notifications-deployment-guide/cucm_b_push-notifications-deployment-guide_chapter_01.html#reference_CE836F3E3283BCF699F2AFC21426B783), to add fos-a.wbx2.com, push.webexconnect.com, and idbroker.webex.com to the SSL Decryption Exclusion list in the firewall. For customers who use this recommended method of configuration, no action is necessary.
For customers who have configured IP address in their Firewall ACL, it is recommended to use the Fully Qualified Domain Name (FQDN), as stated above. 
For customers who have stringent firewall policies that are based on IP address requirements, contact Cisco Technical Assistance Center (TAC) before March 29, 2024, which is the production cutover date.
For more information, see the [Push Notifications (On-Premises Deployments)](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/push_notifications/cucm_b_push-notifications-deployment-guide/cucm_b_push-notifications-deployment-guide_chapter_01.html) chapter of the _Push Notifications Deployment Guide_.
  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.0  | Initial Release  | —  | 2023-DEC-19  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications)
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/740/fn74092.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/740/fn74092.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Jabber](https://www.cisco.com/c/en/us/support/unified-communications/jabber/series.html)
  * [Jabber for Android](https://www.cisco.com/c/en/us/support/unified-communications/jabber-android/series.html)
  * [Jabber for Windows](https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/series.html)
  * [Unified Communications Manager (CallManager)](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/series.html)
  * [Unified Communications Manager IM & Presence Service](https://www.cisco.com/c/en/us/support/unified-communications/unified-presence/series.html)
  * [Unified Communications Manager IM and Presence Service Version 12.5](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-im-presence-service-version-12-5/model.html)
  * [Unified Communications Manager IM and Presence Service Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-im-presence-service-version-14/model.html)
  * [Unified Communications Manager Version 12.5](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-12-5/model.html)
  * [Unified Communications Manager Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-14/model.html)

+ Show All 9 Products
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/740/fn74092.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/740/fn74092.html)
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
