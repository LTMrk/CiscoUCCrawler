  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70288.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70288.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70288.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70288.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70288.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Routers](https://www.cisco.com/c/en/us/support/routers/category.html)
  * [Cisco 4000 Series Integrated Services Routers](https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/products-field-notices-list.html)


# Field Notice: FN - 70288 - ISR-WAAS Does Not Deploy Successfully on an ISR-4321 Router Installed with Cisco IOS XE Software Release 16.9.x - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/702/fn70288.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70288.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/702/fn70288.html)


Updated:November 5, 2018
Document ID:FN70288
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 03-Sep-18  | Initial Release  |  
| 2.0  | 04-Nov-18  | Updated the Problem Description, Background, Problem Symptom, and Workaround/Solution sections  |  
### Products Affected  
| Affected OS Type  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| NON-IOS  | 6.2  | 6.2.1, 6.2.1a, 6.2.3, 6.2.3a, 6.2.3b, 6.2.3c, 6.2.3d, 6.2.3e  | This issue is specific to ISR-WAAS that runs on ISR 4321 when used with Cisco IOS XE Software Release 16.9.x only.  |  
| NON-IOS  | 6.4  | 6.4.1, 6.4.1a  | This issue is specific to ISR-WAAS that runs on ISR 4321 when used with Cisco IOS XE Software Release 16.9.x only.  |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvj74332](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvj74332)  | Not able to deploy ISR-WAAS in ISR-4321 router installed with IOS-XE-16.9.x version  |  
### Problem Description
The CPU share for the container services has been reduced in Cisco IOS® XE Software Release 16.9.x, which leads to Integrated Services Router-Wide Area Application Services (ISR-WAAS) installation failure. This issue is specific to the ISR-WAAS 200 model that runs on ISR 4321 when used with Cisco IOS XE Software Release 16.9.1.
### Background
Due to the resource allocation changes for container services in ISR 4321, these versions are impacted for ISR-WAAS 200:
  * **In an ISR 4321 router with Cisco IOS XE Software Release 16.9.x or later:** The ISR-WAAS 200 model with WAAS Version 6.x (all versions earlier than 6.4.1b) cannot be deployed.
  * **In an ISR 4321 router that runs WAAS Version 6.x (all versions earlier than 6.4.1b):** If Cisco IOS XE is upgraded from an earlier release to 16.9.x or later, ISR-WAAS 200 will not come up.


### Problem Symptom
WAAS Version 6.x (all versions earlier than 6.4.1b) will fail to deploy on an ISR 4321 router with Cisco IOS XE Software Release 16.9.x or later; and WAAS version 6.x (all versions earlier than 6.4.1b) will not come up if Cisco IOS XE is upgraded from an earlier release to 16.9.x or later.
### Workaround/Solution
Customers who run Cisco IOS XE Software Release 16.9.x or later with an affected WAAS release should upgrade their WAAS software to 6.4.1b (or later) as shown in this table:  
| Router  | Cisco IOS Version  | WAAS Version  | Impacted  |  
| --- | --- | --- | --- |  
| ISR 4321  | 16.8.x or earlier  | All supported versions  | No  |  
| 16.9.x or later  | 6.x (All versions earlier than 6.4.1b)  | Yes  |  
| 5.x, 6.4.1b or later  | No  |  
**Note:** Once WAAS is deployed with version 6.4.1b (or later), you can downgrade the WAAS version to any of the supported versions (including impacted versions) via the WAAS User Interface.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70288.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70288.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [4000 Series Integrated Services Routers](https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/702/fn70288.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70288.html)
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
