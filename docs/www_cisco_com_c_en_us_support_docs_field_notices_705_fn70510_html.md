  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70510.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70510.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70510.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70510.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70510.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Enterprise Chat and Email](https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-field-notices-list.html)


# Field Notice: FN - 70510 - Chrome Version 80 Update for SameSite Cookie Causes ECE Gadget and Dock Chat to Malfunction - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/705/fn70510.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70510.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/705/fn70510.html)


Updated:February 10, 2020
Document ID:FN70510
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 04-Feb-20  | Initial Release  |  
| 1.1  | 10-Feb-20  | Updated the Products Affected, Problem Symptom, and Workaround/Solution Sections  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | Enterprise Chat and Email  | 11  | 11.5(1), 11.6(1)  | Release 11.5(1) and 11.6(1) customers are advised to upgrade to Release 11.6(1) ES8 in order to apply the ET  |  
| NON-IOS  | Enterprise Chat and Email  | 12  | 12.0(1)  | Update to ECE 12.0 ES3 in order to apply the ET  |  
| NON-IOS  | Enterprise Chat and Email  | 12  | 12.5(1)  | Apply ET1  |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvs83450](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvs83450)  | Explicitly assert the "SameSite" cookie attribute in ECE application  |  
### Problem Description
The Enterprise Chat and Email (ECE) gadget and dock chat malfunction after you apply the Chrome Version 80 update for SameSite cookie.
### Background
Currently the Chrome SameSite cookie default is "None", which allows third-party cookies to track users across sites. However, from February 2020, cookies will default into "SameSite=Lax", which means cookies are only set when the domain in the URL of the browser matches the domain of the cookie - a first-party cookie. Any cookie with the "SameSite=None" label must also have a secure flag, therefore it will only be created and sent through requests made over HTTPs.
### Problem Symptom
The agent will not be able to log in to the ECE gadget inside Finesse on ECE Releases 11.5(1), 11.6(1), 12.0(1), and 12.5(1).
**Behavior on the Agent Side**
When an agent tries to log in to the ECE gadget inside Finesse, the agent will be logged out immediately. When the agent tries to log in again, this message is displayed:
`You have at least one session that is already in progress. Would you like to end the existing sessions and begin new session?`
When you click **Continue** , the agent will still not be able to log in to the application as shown in these screenshots:
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70510img11580847286553.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70510img11580847286553.png "Related image, diagram or screenshot.")
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70510img21580847153131.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70510img21580847153131.png "Related image, diagram or screenshot.")
Network traces from the agent console in Chrome for this issue are shown here.  
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70510img31580847326922.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70510img31580847326922.png "Related image, diagram or screenshot.")
**Behavior on the Customer Side**
The dock chat customer is not able to refresh, navigate, or pop out a dock template for cross domain if SameSite is enabled. Sample screenshots are shown here:
Customer dock chat website with docked chat icon.  
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70510img41580847341861.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70510img41580847341861.png "Related image, diagram or screenshot.")
Customer initiates the chat.  
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70510img51580847358655.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70510img51580847358655.png "Related image, diagram or screenshot.")
On refresh, the docked chat window disappeared.  
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70510img61580847388151.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70510img61580847388151.png "Related image, diagram or screenshot.")
If the customer undocks a dock chat, the chat window does not load.  
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70510img71580847405855.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/705/fn70510img71580847405855.png "Related image, diagram or screenshot.")
The agent will not be able to log in to the ECE gadget inside Finesse on ECE Releases 11.5(1), 11.6(1), 12.0(1), and 12.5(1).
### Workaround/Solution
Do not update Chrome. Apply the given Engineering Test (ET) on the latest Engineering Special (ES) of the respective ECE releases.
  * [Release 11.6](https://software.cisco.com/download/home/268439622/type/286310764/release/11.6\(1\)_ES8) - Release 11.5(1) and 11.6(1) customers are advised to upgrade to Release 11.6(1) ES8 in order to apply the ET2
  * [Release 12.0](https://software.cisco.com/download/home/268439622/type/286310764/release/12.0\(1\)_ES3) - Update to ECE 12.0(1) ES3 in order to apply the ET1
  * [Release 12.5](https://software.cisco.com/download/home/286311237/type/286310764/release/12.5\(1\)) - Apply the ET1


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70510.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70510.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Enterprise Chat and Email](https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/series.html)
  * [Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/705/fn70510.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70510.html)
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
