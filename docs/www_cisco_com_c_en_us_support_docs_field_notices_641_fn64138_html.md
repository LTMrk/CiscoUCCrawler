  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64138.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64138.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64138.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64138.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64138.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Collaboration Endpoints](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Cisco IP Phone 8800 Series](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-field-notices-list.html)


# Field Notice: FN - 64138 - IP Phones Freeze, Reboot, and Disconnect from the VPN After Software Upgrade - Firmware Upgrade Required
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/641/fn64138.html) to Save Content 
Print
### Available Languages
Updated:July 1, 2016
Document ID:FN64138
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### NOTICE: 
### THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME. 
### Revision History  
| Revision  | Date  | Comment  |  
| --- | --- | --- |  
| 1.0  | 01-JUL-2016  | Initial Public Release  |  
### Products Affected  
| Products Affected  |  
| --- |  
| IPPHONE  |  
### Problem Description
The IP phone freezes, reboots, and disconnects from the VPN after an upgrade from Cisco IOS® Software Release 15.3(3)M3 to Cisco IOS Software Release 15.3(3)M4.
### Background
The problem is caused by the Cisco IOS code change, which expects a Datagram Transport Layer Security (DTLS) header from the phone. Specifically, the X-DTLS-Header-Pad-Length attribute in the CONNECT message.
The phones hit two additional bugs (see the CDETS section) and are unable to complete the process. As a result, the phones fall back to TLS which causes the indicated behavior.
The VPN client that runs in the phone firmware is not based on the AnyConnect client, but instead uses the AnyConnect protocol. 
All firmware versions that support DTLS, Cisco IOS Software Releases 15.3(3)M4 and 15.4(3)M5 and later, are affected.
### Problem Symptoms
The IP phone freezes, reboots, and disconnects from the VPN after an upgrade from Cisco IOS Software Release 15.3(3)M3 to Cisco IOS Software Release 15.3(3)M4.
### Workaround/Solution
#### Workaround
[Cisco IOS version 15.4(3)M4](https://software.cisco.com/download/navigator.html?mdfid=286179099&divid=0&catid=268438303&i=!pp) can be used as a workaround because it does not contain the code change to expect a DTLS header from the phone.
#### Solution
Cisco recommends to use Cisco IOS Software Release 15.4(3) M4 per the workaround. 
### CDETS
To follow the bug ID link below and see detailed bug information, you must be a [registered](http://tools.cisco.com/RPF/register/register.do) customer and you must be logged in.   
| CDETS  | Description  |  
| --- | --- |  
|  [CSCup56792](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCup56792) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only)  | Supporting 4 byte DTLS header: This bug is raised to track the migration of DTLS header from 1 byte to 4 bytes to improve performance.  |  
|  [CSCte01414](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCte01414) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only)  | [DTLS] CDTP Header length shall be negotiable: This is an enhancement to AnyConnect. This is not a bug.  |  
|  [CSCuy90621](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCuy90621) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only)  | 78xx/88xx do not support X-DTLS-Header-Pad-Length:  |  
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods: 
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64138.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64138.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [IP Phone 8800 Series](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/series.html)
  * [Unified IP Phone 7900 Series](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-7900-series/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64138.html)
