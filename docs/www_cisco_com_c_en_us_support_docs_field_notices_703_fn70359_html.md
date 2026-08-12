  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70359.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70359.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70359.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70359.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70359.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Switches](https://www.cisco.com/c/en/us/support/switches/category.html)
  * [Cisco Catalyst 3650 Series Switches](https://www.cisco.com/c/en/us/support/switches/catalyst-3650-series-switches/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/switches/catalyst-3650-series-switches/products-field-notices-list.html)


# Field Notice: FN - 70359 - C3650/C3850 and C9300/C9500 Devices That Run on Certain Cisco IOS XE 16.3.x or 16.6.x Software Releases Might Observe a Memory Leak - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/703/fn70359.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70359.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/703/fn70359.html)


Updated:February 21, 2019
Document ID:FN70359
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 23-Jan-19  | Initial Release  |  
| 1.1  | 24-Jan-19  | Updated the Products Affected Section  |  
| 1.2  | 21-Feb-19  | Updated the Title, Products Affected, Problem Description, and Workaround/Solution Sections  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | IOSXE  | 16  | 16.3.1, 16.3.1a, 16.3.2, 16.3.3, 16.3.4, 16.3.5, 16.3.5b, 16.6.1, 16.6.1a, 16.6.2, 16.6.3  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvh89372](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvh89372)  | Memory leak in linux_iosd-imag and/or platform_mgr after every FRU removable  |  
### Problem Description
C3650/C3850 and C9300/C9500 devices that run on a Cisco IOS® XE Software Release as mentioned in Products Affected List might observe a memory leak in "linux_iosd-imag" and "platform_mgr" processes. The issue might also be observed on the active switch on a stack.
### Background
This memory leak is caused by incorrect internal memory handling. As a result, the memory is not freed correctly.
### Problem Symptom
If a C3650/C3850 or C9300/C9500 device is impacted by this issue, the processes "linux_iosd-imag" and/or "platform_mgr" will display increasing memory size when checked with this **show** CLI command.

```
Switch#**show platform software process memory switch 1 r0 all sorted**

   Pid     VIRT       **RSS**      PSS      Heap    Shared  Private              Name
------------------------------------------------------------------------------------
  5329  1796052    **621080**    527162        80   108284    512796   linux_iosd-imag  

 15755   917476    **119924**     34383      1752    98220     21704      platform_mgr


Switch#**show platform software process memory switch 1 r0 all sorted**

   Pid     VIRT       **RSS**       PSS      Heap   Shared   Private            Name
------------------------------------------------------------------------------------
  5329  1870404    **712544**    617188        80   110276    602268   linux_iosd-imag   

 15755   968948    **172380**     85746     52900    99380     73000      platform_mgr  


```

In the previous two displays, the memory size under the RSS column increased by 90Mb for "linux_iosd-imag" process and by 60 Mb for "platform_mgr" process.
For further information on how to determine if the device is affected by the leak, see this [Cisco bug discussion](https://supportforums.cisco.com/t5/cisco-bug-discussions/cscvh89372-memory-leak-in-linux-iosd-image/m-p/3376656/highlight/true#M7176).
### Workaround/Solution
As a temporary workaround, reload the switch in order to reclaim memory.
For a permanent fix, upgrade to Cisco IOS XE Software Release 16.3.6, 16.6.4, 16.9.1, or later. We recommend customers to review CCO download page on current recommended starred release in these release trains. All members of a stack should be software upgraded.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70359.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Customers Also Viewed
  * [Troubleshoot Catalyst 3850 Output Drops](https://www.cisco.com/c/en/us/support/docs/switches/catalyst-3850-series-switches/200594-Catalyst-3850-Troubleshooting-Output-dr.html)
  * [System Management Configuration Guide, Cisco IOS XE Release 3SE (Catalyst 3650 Switches) --- Working with Cisco IOS XE Software Bundles](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3650/software/release/3se/system_management/configuration_guide/b_sm_3se_3650_cg/b_sm_3se_3650_cg_chapter_010101.html)
  * [Catalyst 3650 Switch Hardware Installation Guide --- Overview](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3650/hardware/installation/guide/Cat3650hig_book/HIGOVERV.html)
  * [Catalyst 3650 Switch Hardware Installation Guide --- Configuring the Switch with the CLI-Based Setup Program](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3650/hardware/installation/guide/Cat3650hig_book/HGcliSET.html)
  * + Show 1 More


### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70359.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/703/fn70359.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/703/fn70359.html)
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
