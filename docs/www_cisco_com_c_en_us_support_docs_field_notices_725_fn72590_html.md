  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72590.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72590.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72590.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72590.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72590.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Packaged Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-field-notices-list.html)


# Field Notice: FN - 72590 - Cloud Connect Is Unable to Check for and Download New Software Due to DevHub Authentication Token Expiration - Workaround Provided
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/725/fn72590.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72590.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/725/fn72590.html)


Updated:August 23, 2023
Document ID:FN72590
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 16-Aug-23  | Initial Release  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | Cloud Connect  | 12  | 12.6(1), 12.6(1)ES1, 12.6(1)ES2, 12.6(1)ES3, 12.6(1)ES4, 12.6(1)SecurityPatch, 12.6(2)  | This Field Notice applies to Cisco Unified Contact Center Enterprise (UCCE) and Packaged Contact Center Enterprise (PCCE) deployments that utilize Cloud Connect for Orchestration to check for and download new software. It is not specific to Engineering Specials and does not apply to customers using Webex Contact Center Enterprise (WxCCE).  |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCwf60543](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwf60543)  | CCBU software download failure due to Devhub token expiry  |  
### Problem Description
Unified Contact Center Enterprise (UCCE) and Packaged Contact Center Enterprise (PCCE) customers utilizing Cloud Connect for Orchestration to check for and download new software will encounter an authentication failure. This failure is due to the Authentication token associated with the API key becoming invalidated as part of Cisco’s Single Sign-On (SSO) backend technology migration.
### Background
Beginning August 31, 2023, Cisco will migrate the backend technology for SSO. As a result of this migration, the Authentication token linked to the API key created from the DevHub console will be invalidated.
### Problem Symptom
Following the migration of Cisco's SSO backend technology, Cloud Connect will begin sending emails to administrators to inform them of software download failures. The emails will contain specific messages based on the affected feature on Cloud Connect. Refer to the information in this table for further details.  
| Affected Feature on Cloud Connect  | Symptoms for Affected Features  | Where Symptoms Will Be Noticed  | Log Text Indicating Symptoms  |  
| --- | --- | --- | --- |  
|  Orchestration software download from DevHub to Cloud Connect.  | 
  * The scheduled software download will fail.
  * Enforcing a manual software download will fail.

 |  Software Download Ansible Log  
(software_download_ansible.log)  |  Ansible Log: Response message is:  
"Download request has been canceled: ExpiredRefreshToken”  |  
|  Configuring Cisco hosted cloud-based software artifactory using the `**utils image-repository set**`command via the CLI.  |  The `**utils image-repository set**`command via the CLI will fail.  | 
  * CLI Console
  * CLI Log

 | 
  * Console Message:  
“Authentication token expired for CCO ID used to generate API key. Log in to aritifactory URL with CCO ID to refresh the token.”
  * CLI Log:  
Cisco Artifactory configuration failed. Response code: 400.  
Response message:  
“Download request has been canceled: ExpiredRefreshToken”

 |  
**Note:** For instructions to download the orchestration logs, refer to the following section:
  * For Cisco Unified Contact Center Enterprise, refer to [Cisco Unified Contact Center Enterprise Install and Upgrade Guides](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html) > Installation and Upgrade Guide for your release > CCE Orchestration > Orchestration in CCE Deployment > Maintenance Tasks > Serviceability.
  * For Cisco Packaged Contact Center Enterprise, refer to [Cisco Packaged Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html)[ Install and Upgrade Guides](https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html) > Installation and Upgrade Guide for your release > Orchestration > CCE Orchestration > Orchestration in CCE Deployment > Maintenance Tasks > Serviceability.


### Workaround/Solution
After the migration cutover date, administrators using the UCCE Orchestration software download or configuring Cisco hosted cloud-based software artifactory via the CLI with the **`utils image-repository set`**command need to log in to the[Cisco DevHub console](https://devhub-download.cisco.com/console/) with the same Cisco.com User ID (CCO ID) that was originally used to generate the API key configured for Cloud Connect Orchestration.
This will associate a new authentication token with the API key. It is important to note that you do not need to regenerate the API key. Once you have logged in to the DevHub console, the UCCE Orchestration software download and the `**utils image-repository set**`command via the CLI will work as expected.
**Note:** The CCO ID used to generate the API key currently configured in Cloud Connect for Orchestration should have access to download the software. If the CCO ID originally used to generate the API key is no longer available or if access to contract registered software is revoked for the presently used CCO ID, generate the API key with any valid CCO ID with access to software download and configure it in Cloud Connect for Orchestration.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72590.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72590.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Packaged Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/series.html)
  * [Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/725/fn72590.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72590.html)
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
