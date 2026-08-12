  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62560.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62560.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62560.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62560.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62560.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Collaboration Systems Release](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/products-field-notices-list.html)


# Field Notice: FN - 62560 - Potential Loss of CallManager Services While Upgrading From Any Release of 5.x To Any Other Release of 5.x.
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/620/fn62560.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62560.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/620/fn62560.html)


Updated:October 27, 2006
Document ID:FN62560
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
  
[](http://www.cisco.com/warp/customer/tech_tips/index/fn.html)
### October 27, 2006
### NOTICE:
### THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.
* * *
### Products Affected  
|  Products Affected  |  
| --- |  
|  CallManager - CallManager 5.0  |  
### Problem Description
During a Callmanager, Linux to Linux upgrade, the Callmanager may become starved for CPU resources during the initial FTP download of the patch file and restart. This causes any registered phone to unregister and call processing to stop.
### Background
During a Linux to Linux upgrade of a cluster, the Cisco CallManager (CCM) Service may experience outages due to the lack of CPU resources. The CPU resources during the upgrade process will consume a very high amount of disk I/O. This will cause the CCM Service and others, to exit CCM and restart Service Manager.
### Problem Symptoms
The Cisco CallManager(CCM) Service will stop and any active phone calls will be dropped.
### Workaround/Solution
The upgrade from any CallManager release of 5.x to any other release of 5.x.should be applied during a Maintenance Window to ensure the least amount of outages to the users.
### DDTS
To follow the bug ID link below and see detailed bug information, you must be a [registered](http://tools.cisco.com/RPF/register/register.do) user and you must be logged in.  
|  DDTS  |  Description  |  
| --- | --- |  
|  [CSCsd84481](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCsd84481) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only)  |  High Disk I/O Wait Cause CCM Service Outage During L2 Upgrades  |  
### Revision History  
|  Revision  |  Date  |  Comment  |  
| --- | --- | --- |  
|  1.0  |  27-Oct-2006  |  Initial Public Release  |  
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/warp/customer/687/Directory/DirTAC.shtml) by one of the following methods:
  * [Open a service request on Cisco.com](http://tools.cisco.com/ServiceRequestTool/create/)
  * [By email](http://www.cisco.com/warp/customer/687/Directory/DirTAC.shtml#email)
  * [By telephone](http://www.cisco.com/warp/customer/687/Directory/DirTAC.shtml#telephone)


### Receive Email Notification For New Field Notices
[Product Alert Tool](http://www.cisco.com/cgi-bin/Support/FieldNoticeTool/field-notice) - Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
* * *
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62560.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62560.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Collaboration Systems Release](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/620/fn62560.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62560.html)
