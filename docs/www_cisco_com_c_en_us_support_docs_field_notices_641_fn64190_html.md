  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64190.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64190.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64190.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64190.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64190.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Routers](https://www.cisco.com/c/en/us/support/routers/category.html)
  * [Cisco ASR 1000 Series Aggregation Services Routers](https://www.cisco.com/c/en/us/support/routers/asr-1000-series-aggregation-services-routers/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/routers/asr-1000-series-aggregation-services-routers/products-field-notices-list.html)


# Field Notice: FN - 64190 - Cisco IOS XE - Show commands on Cisco IOS XE based platforms might not report true platform memory usage - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/641/fn64190.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64190.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/641/fn64190.html)


Updated:October 7, 2016
Document ID:FN64190
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 06-Sep-16  | Initial Release  |  
| 10.0  | 25-Oct-17  | Migration to new field notice system  |  
### Products Affected  
| Affected OS Type  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| NON-IOS  | 3  | 3.3.2S,3.3.2SE,3.3.2SG,3.3.2XO,3.3.3SE,3.3.4SE,3.3.5SE,3.4.0S,3.4.0SG,  
3.4.0SQ,3.4.0aS,3.4.1S,3.4.1SG,3.4.1SQ,3.4.2S,3.4.2SG,3.4.3S,3.4.3SG,3.4.4S,3.4.4SG,3.4.5S,  
3.4.5SG,3.4.6S,3.4.6SG,3.4.7SG,3.4.8SG,3.5.0E,3.5.0S,3.5.0SQ,3.5.1E,3.5.1S,3.5.1SQ,3.5.2E,  
3.5.2S,3.5.2SQ,3.5.3E,3.5.3SQ,3.5.4SQ,3.5.5SQ,3.5.6SQ,3.6.0E,3.6.0S,3.6.1E,3.6.1S,3.6.2E,  
3.6.2S,3.6.2aE,3.6.3E,3.6.4E,3.6.5E,3.6.5aE,3.6.5bE,3.6.6E,3.6.7E,3.7.0E,3.7.0S,3.7.0bS,  
3.7.1E,3.7.1S,3.7.1aS,3.7.2E,3.7.2S,3.7.2tS,3.7.3E,3.7.3S,3.7.4E,3.7.4S,3.7.4aS,3.7.5E,  
3.7.5S,3.7.6S,3.7.7S,3.8.0E,3.8.0S,3.8.1E,3.8.1S,3.8.2E,3.8.2S,3.8.3E,3.8.4E,3.9.0E,3.9.0S,  
3.9.0aS,3.9.1E,3.9.1S,3.9.1aS,3.9.2E,3.9.2S  |   |  
| NON-IOS  | 16  | 16.1.0,16.1.1,16.1.2,16.1.3,16.2.1,16.2.2  |   |  
| NON-IOS  | 3  | 3.12.1S,3.12.2S,3.12.3S,3.13.0S,3.13.0aS,3.13.1S,  
3.13.2S,3.13.2aS,3.13.3S,3.13.4S,3.13.5S,3.13.5aS,3.13.6S,3.13.6aS,3.13.6bS,3.13.7S,  
3.13.7aS,3.14.0S,3.14.1S,3.14.2S,3.14.3S,3.14.4S,3.15.0S,3.15.1S,3.15.1cS,3.15.2S,  
.15.3S,3.15.4S,3.16.0S,3.16.0cS,3.16.1S,3.16.1aS,3.16.2S,3.16.2aS,3.16.2bS,3.16.3S,  
3.16.3aS,3.16.4S,3.16.4aS,3.16.4bS,3.16.5S,3.18.0S,3.18.0SP,3.18.0aS,3.18.1S,3.18.1SP,  
3.18.1aSP,3.18.1bSP,3.18.1cSP,3.18.2S,3.18.2SP,3.18.2aSP,3.18.3S,3.2.0S,3.2.0SE,3.2.0SG,  
3.2.0SQ,3.2.0XO,3.2.10SG,3.2.11SG,3.2.1SE,3.2.1SG,3.2.1SQ,3.2.2S,3.2.2SE,3.2.2SG,  
3.2.2SQ,3.2.3SE,3.2.3SG,3.2.3SQ,3.2.4SG,3.2.5SG,3.2.6SG,3.2.7SG,3.2.8SG,3.2.9SG,3.3.0S,  
3.3.0SE,3.3.0SG,3.3.0SQ,3.3.0XO,3.3.1S,3.3.1SE,3.3.1SG,3.3.1SQ,3.3.1XO  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCuc40262](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCuc40262)  | Linux kernel cache is leading to confusion over memory usage  |  
### Problem Description
The **show** command on Cisco IOS XE based products might not report true platform memory usage.
### Background
On products that run Cisco IOS XE (see the Products Affected section), the Linux kernel uses free memory space in order to expand its cache. This results in the free memory space to decrease over time and might appear as if the router experiences a memory leak. This could be a false alarm since the cache can be freed if memory is needed.
### Problem Symptom
When you use the command **show platform software status control-processor** , over time the free memory might display a smaller percentage as shown in this example highlighted in **bold**.

```
Memory (kB)
```

Slot Status Total Used (Pct) **Free (Pct)** Committed (Pct)
RP0 Healthy 3972008 3942316 (99%) **29692 ( 1%)** 2392632 (60%)
### Workaround/Solution
There is one solution and two workarounds.
The solution is to upgrade to Cisco IOS XE Denali 16.3.
**Workaround 1**
In order to obtain a good estimate of free memory, enter the command **monitor platform software process rp active** :

```
top - 17:02:19 	up 26 days, 22:52,  0 users,  load average: 0.00, 0.00, 0.00
```

Tasks: 445 total, 1 running, 444 sleeping, 0 stopped, 0 zombie
Cpu(s): 0.8% us, 1.7% sy, 0.0% ni, 97.5% id, 0.0% wa, 0.0% hi, 0.0% si, 0.0% st
Mem: 3972008k total, 3946308k used, 25700k free, 223416k buffers
Swap: 0k total, 0k used, 0k free, 1537140k cached
In order to estimate the free memory, add free + buffers + cached memory. From the previous example, the estimated free memory is 25700k + 223416k + 1537140k = 1786256k. This indicates that the estimated free memory is 45% of the total memory.
**Workaround 2**
This example lists the steps to be followed in order to get accurate used and free memory on an active Route Processor (RP).
**Note** : Use of the **sync** command might increase CPU utilization of the RP.
  1. Obtain a one day platform shell license. See [Product License Registration](http://tools.cisco.com/SWIFT/LicensingUI/Quickstart). This requires a CCO account.
  2. Install the shell license obtained in Step 1.
  3. Enter the config command **platform shell**.
  4. Enter the exec command **request platform software system shell rp active**. This results in a platform shell prompt.
  5. At the platform shell prompt, enter **y**.
  6. At the shell prompt, enter **sync;echo 3 > /proc/sys/vm/drop_caches**.
  7. Exit the platform shell.
  8. Enter the command **show platform software status control-processor**.


This displays an accurate value for used and free memory using show platform software status control-processor and querying the SNMP MIB browser in order to decipher memory usage.
Free memory - 1.3.6.1.4.1.9.9.109.1.1.1.1.13
Used memory - 1.3.6.1.4.1.9.9.109.1.1.1.1.12
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64190.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64190.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [4321 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4321-integrated-services-router/model.html)
  * [4331 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4331-integrated-services-router-isr/model.html)
  * [4351 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4351-integrated-services-router/model.html)
  * [4431 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4441-x-integrated-services-router-isr/model.html)
  * [4451-X Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4451-x-integrated-services-router-isr/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/641/fn64190.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64190.html)
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
