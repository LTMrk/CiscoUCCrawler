  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/640/fn64071.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/640/fn64071.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/640/fn64071.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/640/fn64071.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/640/fn64071.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Collaboration Endpoints](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Cisco IP Phone 8800 Series](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-field-notices-list.html)


# Field Notice: FN - 64071 - CP-8831 DCU (Keypad) Problems - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/640/fn64071.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/640/fn64071.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/640/fn64071.html)


Updated:January 14, 2019
Document ID:FN64071
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 26-Jan-16  | Initial Release  |  
| 10.0  | 25-Oct-17  | Migration to new field notice system  |  
| 10.1  | 14-Jan-19  | Fixed Broken Image Links  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| CP-8831-BR-K9=  |   |  
| CP-8831-DCU-S=  |   |  
| CP-8831-EU-K9=  |   |  
| CP-8831-J-K9=  |   |  
| CP-8831-K9=  |   |  
| CP-8831-LA-K9=  |   |  
| CP-8831-TW-K9=  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvf34445](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvf34445)  | There were no defects filed with this field notice at the time of publication.  |  
### Problem Description
CP-8831 with a V02 keyboard boots up to a blank LCD at installation or shows the Cisco logo. The 8831 appears as if the keyboard unit (display control unit - DCU) is bad, however this is not the case. This occurs when the 8831 has been downgraded to firmware version 9.3.3. In order to fix the issue the phone must be upgraded back to 10.3.1SR2, which requires a stepped upgrade. Details are in the Workaround/Solution section.
All units with serial numbers between FOC1926xxxx and FOC1952xxxx are affected.
### Background
In manufacturing there was a component change to the DCU that requires new firmware in order to operate. The original firmware 9.3.3 does not contain the driver necessary to operate the DCU. That driver is only available in firmware versions 10.3.1-SR1 and later.
The 10.3.1-SR1 firmware does not have the blocker that prevents the 8831 from downgrading to an earlier firmware version.
Customers who have standardized on the 9.3.3 firmware, for example, will see their new 8831 downgrade to 9.3.3 automatically which disables the operation of the DCU.
Even if the customer completes a Return Material Authorization (RMA) for the 8831 and installs a new replacement 8831, the same problem occurs because of the way the firmware is managed.
### Problem Symptom
CP-8831 boots up to either a blank LCD or an LCD that shows the Cisco logo at installation. The unit shows registered in CUCM and might receive calls, but no calls can be placed.
### Workaround/Solution
All units with serial numbers between FOC1926xxxx and FOC1952xxxx are affected.
For CP-8831 devices with a V01 designation, no action is required. These devices do not have the new DCU hardware and therefore have no driver dependency within the firmware.
For CP-8831 devices with a V02 designation, in order to prevent this issue from occurring, see the Solution section. If this issue has already occurred and is need of recovery, see the Workaround section.
It is possible, at the time of this release, that 10.3.1(SR2) will not yet be published. In that case use 10.3.1(SR1).
**Solution**
In order to prevent the 8831 V02 from downgrading firmware prior to connection to the network when the CUCM default load is 9.3.3, complete these steps:
  1. Download 10.3.1-SR2 from Cisco.com.
  2. Load the 10.3.1-SR2 firmware onto the TFTP server.
  3. Restart the TFTP service on the CUCM.
  4. Point the new 8831 to the 10.3.1-SR2 load from the administration page for each new device.
  5. Connect a new 8831 to the network and it will upgrade to 10.3.1-SR2.


**Workaround**
In order to recover CP-8831 V02 units that have already downgraded to 9.3.3, complete these steps:
  1. Download cmterm-8831-sip.9-3-3-TO-10-3-1-v2.zip from Cisco.com.
  2. Load the cmterm-8831-sip.9-3-3-TO-10-3-1-v2.zip firmware onto the TFTP server from the TFTP File Management Page.
  3. Restart the TFTP service on the CUCM.
  4. Point the new 8831 to the cmterm-8831-sip.9-3-3-TO-10-3-1-v2.zip load from the administration page for each new device.
  5. Connect a new 8831 to the network.
  6. After the 8831 has upgraded to 9-3-3-TO-10-3-1-v2, point the 8831 to the 10.3.1-SR2 load from the administration page for each new device.
  7. Initiate reset to load 10.3.1-SR2.


Firmware releases 10.3.1 SR2 and later contain the downgrade blocker.
### How To Identify Affected Products
See these images for examples on where to locate the version number for your product.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/640/fn64071_nzd6iw1547157419244.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/640/fn64071_nzd6iw1547157419244.png "Related image, diagram or screenshot.")
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/640/fn64071_nzd6en1547157436423.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/640/fn64071_nzd6en1547157436423.png "Related image, diagram or screenshot.")
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/640/fn64071.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/640/fn64071.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/640/fn64071.html)
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
