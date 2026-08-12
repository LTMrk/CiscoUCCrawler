  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70219.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70219.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70219.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70219.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligent-contact-management-enterprise/products-field-notices-list.html)


# Field Notice: FN - 70219 - CUIC LiveData Gadgets Broken with Google Chrome Browser Version 67 - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/702/fn70219.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70219.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/702/fn70219.html)


Updated:June 29, 2018
Document ID:FN70219
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 11-Jun-18  | Initial Release  |  
| 1.1  | 22-Jun-18  | Added a CUIC Metadata Tag  |  
| 1.2  | 29-Jun-18  | Updated the Workaround/Solution Section with UCCE/UCCX Links  |  
### Products Affected  
| Affected OS Type  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| NON-IOS  | ICM Ver 11  | 11.5(1), 11.6(1)  |   |  
| NON-IOS  | Unified CCX 11  | 11.5(1)SU1  |   |  
| NON-IOS  | 11  | 11.6(1)  |   |  
| NON-IOS  | 11  | 11.6, 11.0, 11.5  |   |  
| NON-IOS  | CUIC VERSION 11.6  | 11.6(1)  |   |  
| NON-IOS  | CUIC VERSION 11.5  | 11.5(1)  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvj74116](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvj74116)  | Reports in CUIC and corresponding Gadgets in Finesse does not work with Chrome v67  |  
| [CSCvj79877](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvj79877)  | [UCCX] Reports in CUIC and corresponding Gadgets in Finesse does not work with Chrome v67  |  
### Problem Description
For both Unified Contact Center Express (UCCX) and Unified Contact Center Enterprise (UCCE) solutions, LiveData reports within the Cisco Finesse Desktop and the Cisco Unified Intelligence Center (CUIC) reports in the CUIC report viewer fail to load in the Google Chrome browser Version 67. The reports in CUIC and the LiveData gadgets hang when they are loaded. This issue is only seen with the Google Chrome browser Version 67.
### Background
Google released an update to their Chrome browser that includes a change to an internal parameter used to display reporting data in the report viewer and in the LiveData gadget. In the Version 67 update, the reports fail to load.
### Problem Symptom
After the Google Chrome browser is updated to Version 67:
  * The LiveData gadgets come up blank on the agent and the Finesse Supervisor Desktop.
  * CUIC reports do not load in the CUIC report viewer. This is only applicable to this specific browser version.


### Workaround/Solution
Workarounds to this issue are:
  * Use another supported browser. This issue is not seen with any other supported browser.
  * Use an earlier version of Google Chrome. This issue is only seen with Google Chrome Version 67
  * If customers wish to use Google Chrome Version 67 and later, these files need to be installed: 
    * UCCE - [Version 11.6: 11.6(1)ES07 and Version 11.5: 11.5(1)ES11](https://software.cisco.com/download/home/282163829/type/282377062/release/11.6%25281%2529)
    * UCCX - [Version 11.5 and 11.6](https://software.cisco.com/download/home/286314216/type/286315794/release/MultipleRelease_Cops)


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70219.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70219.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)
  * [Unified Intelligence Center](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/702/fn70219.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/702/fn70219.html)
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
