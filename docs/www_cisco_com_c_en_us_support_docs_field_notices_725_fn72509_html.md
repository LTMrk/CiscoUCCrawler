  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72509.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72509.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72509.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72509.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72509.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Routers](https://www.cisco.com/c/en/us/support/routers/category.html)
  * [Cisco Catalyst 8200 Series Edge Platforms](https://www.cisco.com/c/en/us/support/routers/catalyst-8200-series-edge-platforms/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/routers/catalyst-8200-series-edge-platforms/products-field-notices-list.html)


# Field Notice: FN - 72509 - Weak cryptographic algorithms are not allowed for SNMP user configuration after IOS XE 17.11.1a release - Configuration Change Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/725/fn72509.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72509.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/725/fn72509.html)


Updated:August 15, 2023
Document ID:FN72509
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 08-Aug-23  | Initial Release  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | IOSXE  | 17  | 17.11.1a  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCwc72594](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwc72594)  | SNMP should not allow weak authentication and privacy algorithms for v3 user  |  
### Problem Description
In IOS XE release 17.11.1a and later, weak cryptographic algorithms, specifically MD5 for authentication; DES and 3DES for encryption, are no longer allowed by default due to their vulnerabilities. If you are upgrading an affected system to Release 17.11.1a or later, you must make a configuration change; otherwise, SNMP will be disabled. 
### Background
Cisco IOS XE software allows the use of weak crypto algorithms with SNMP for users who need that capability to provide backwards compatibility. Prior to Cisco IOS XE Release 17.11.1a, these weak crypto algorithms are available by default. In Release 17.11.1a and later, these algorithms are disabled by default due to the risk they present. You must explicitly enable them in the configuration to continue to use them. 
### Problem Symptom
If the weak crypto algorithms are not updated to use stronger algorithms, or if the configuration is not explicitly enabled to allow weak crypto algorithms prior to the 17.11.1a upgrade, then SNMP v3 users with such configuration will be disabled. This will result in service interruptions for SNMP after the upgrade and remote SNMP operation to the device will fail. 
Device(config)#snmp-server user <username> <grpname> v3 auth md5 <password>
weaker algorithm MD5, DES and 3DES is not allowed for snmp user 
Device(config)#snmp-server user <username> <grpname> v3 auth md5 <password> priv des <password>
weaker algorithm MD5, DES and 3DES is not allowed for snmp user 
The following SNMP functions will be impacted: 
  * SNMP set, get, get-bulk, and snmpwalk operations from the management station. 


  * SNMP trap and inform will not be sent from the device. 


### Workaround/Solution
**Recommended Solution**
The solution is to update to stronger cryptographic algorithms, specifically SHA or SHA-2 as the authentication protocol; and AES as the privacy protocol for the SNMP v3 user. 
Prior to upgrading to IOS XE release 17.11.1a or later, identify if any of the affected algorithms (MD5, DES, 3DES) are in use by running the following command: 
Device#show snmp user 
User name: test-user 
Engine ID: 80000009030000505684BD11 
storage-type: nonvolatile active 
_**Authentication Protocol: MD5**_
_**Privacy Protocol: DES**_
Group-name: test-group 
To update these algorithms, use the following configuration command: 
snmp-server user <username> <groupname> v3 auth <sha|sha-2(256, 384, 512)> <password> priv aes <128|192|256> <password>
**Workaround (Not Recommended)**
If it is not possible to update the SNMP v3 user with stronger crypto algorithms, then the following configuration command is required to continue to use the weak algorithms: 
Device(config)#_**crypto engine compliance shield disable**_
**Note:** This command is only available in Cisco IOS XE Release 17.7.1a and later and will only take effect after a reboot. Cisco does NOT recommend this option as these weak cryptographic algorithms are insecure and do not provide adequate protection from modern threats. This command should only be used as a last resort. 
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72509.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72509.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Catalyst 8000V Edge Software](https://www.cisco.com/c/en/us/support/routers/catalyst-8000v-edge-software/series.html)
  * [ISR 1000 Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/isr-1000-series-ios-xe-sd-wan/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72509.html)
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
