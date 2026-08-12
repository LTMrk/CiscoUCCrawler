  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63938.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63938.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63938.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63938.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63938.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Routers](https://www.cisco.com/c/en/us/support/routers/category.html)
  * [Cisco 4000 Series Integrated Services Routers](https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/products-field-notices-list.html)


# Field Notice: FN - 63938 - ISR4451X/K9 & ISR4431/K9 - Silent "PowerON" Reload - CPLD Update Required - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/639/fn63938.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63938.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/639/fn63938.html)


Updated:October 26, 2017
Document ID:FN63938
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 08-Jan-16  | Initial Release  |  
| 10.0  | 26-Oct-17  | Migration to new field notice system  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| ISR4451-X/K9  |   |  
| ISR4331/K9  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCuq20417](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCuq20417)  | ISR 4451-X Silent Reload  |  
### Problem Description
Cisco Integrated Service Router (ISR) 4451-X/K9 or ISR4431/K9 might silently reload without any core files, with the reload reason PowerON. This problem can be due to Cisco bug ID [CSCuq20417](https://tools.cisco.com/bugsearch/bug/CSCuq20417) and/or Cisco bug ID [CSCup18799](https://tools.cisco.com/bugsearch/bug/CSCup18799). Both problems are now resolved.
**Note** : This issue is not related to hardware, and a firmware update corrects the problem. Cisco recommends that customers upgrade the firmware according to the instructions in this field notice. This issue is fixed in CPLD version 15010638 and later.
### Background
Cisco bug ID [CSCuq20417](https://tools.cisco.com/bugsearch/bug/CSCuq20417) and Cisco bug ID [CSCup18799](https://tools.cisco.com/bugsearch/bug/CSCup18799) Service Requests (SRs) were opened due to a **PowerON** issue in the field.
### Problem Symptom
ISR4451-X/K9 or ISR4431/K9 routers might silently reload without any core files, with reload reason **PowerON**.
### Workaround/Solution
In order to resolve the issue, a Complex Programmable Logic Device (CPLD) upgrade is needed.
**Note** : This upgrade can be performed in the field.
Before upgrading the CPLD image, identify the Cisco IOS® XE version that runs on the router.
**Verify the Cisco IOS XE Release on the Router**
If the Cisco IOS image on the router run these or newer versions, an automatic power cycle of the router occurs after the CPLD upgrade:
- isr4400-universalk9.03.13.01.S.154-3.S1-ext.SPA.bin
- isr4400-universalk9_npe.03.13.01.S.154-3.S1-ext.SPA.bin or newer
If the Cisco IOS image used is an older release version, after the CPLD upgrade, a soft reload of the router must be performed. When it is gracefully shutdown, **Turn off** and **Turn on** the router.
The new CPLD image is located at:
[ISR4451-X/K9](https://software.cisco.com/download/release.html?i=!y&mdfid=284389362&softwareid=283425232&release=15.4\(3\)S2&os=)
[ISR4431/K9](https://software.cisco.com/download/release.html?i=!y&mdfid=284358776&softwareid=283425232&release=15.4\(3\)S2&os=)
Download the appropriate image and copy the image to the router's bootflash:
Here are the [upgrade instructions](http://www.cisco.com/c/en/us/td/docs/routers/access/4400/cpld/isr4400_hwfp.html#pgfId-1068031).
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63938.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Customers Also Viewed
  * [Hardware Installation Guide for Cisco 4000 Series Integrated Services Routers --- Overview of the Cisco 4000 Series ISRs](https://www.cisco.com/c/en/us/td/docs/routers/access/4400/hardware/installation/guide4400-4300/C4400_isr/Overview.html)
  * [Hardware Installation Guide for Cisco 4000 Series Integrated Services Routers --- Install and Upgrade Internal Modules and FRUs](https://www.cisco.com/c/en/us/td/docs/routers/access/4400/hardware/installation/guide4400-4300/C4400_isr/FRUs_Modules.html)
  * [Implement Performance License for Integrated Service Router 4000](https://www.cisco.com/c/en/us/support/docs/routers/4000-series-integrated-services-routers/217135-performance-license-on-cisco-isr4000.html)
  * [Cisco 4000 Series ISRs Software Configuration Guide, Cisco IOS XE Gibraltar 16.12.x --- Installing the Software](https://www.cisco.com/c/en/us/td/docs/routers/access/4400/software/configuration/xe-16-12/isr4400swcfg-xe-16-12-book/installing_the_software.html)
  * + Show 1 More


### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63938.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [4331 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4331-integrated-services-router-isr/model.html)
  * [4351 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4351-integrated-services-router/model.html)
  * [4451-X Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4451-x-integrated-services-router-isr/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/639/fn63938.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63938.html)
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
