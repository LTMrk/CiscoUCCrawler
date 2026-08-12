  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/642/fn64285.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/642/fn64285.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/642/fn64285.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/642/fn64285.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/642/fn64285.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco VG Series Gateways](https://www.cisco.com/c/en/us/support/unified-communications/vg-series-gateways/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/vg-series-gateways/products-field-notices-list.html)


# Field Notice: FN - 64285 - Functionality Issue with Cisco IOS Releases Earlier Than 15.6(3)M - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/642/fn64285.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/642/fn64285.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/642/fn64285.html)


Updated:January 18, 2019
Document ID:FN64285
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 11-Apr-17  | Initial Release  |  
| 10.0  | 16-Nov-17  | Migration to new field notice system  |  
| 10.1  | 18-Jan-19  | Fixed Broken Image Link  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| VG310  |   |  
| VG320  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvf34445](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvf34445)  | There were no defects filed with this field notice at the time of publication.  |  
### Problem Description
VG310 and VG320 voice gateways, manufactured and shipped after September 1, 2016, might not function properly if they run Cisco IOS® Software Releases earlier than 15.6(3)M.
### Background
A new hardware component was introduced into the manufacturing process on September 1, 2016 for VG310 and VG320 devices, which requires Cisco IOS Software Release 15.6(3)M or later in order to operate properly.
### Problem Symptom
The new hardware revision of the VG310 and VG320 boots up with Cisco IOS Software Releases earlier than 15.6(3)M, but the digital signal processor (DSP) fails to download the necessary firmware which causes voice calls to fail.
Units manufactured September 1, 2016 or after and run a Cisco IOS Software Release earlier than 15.6(3)M might exhibit this behavior:
  * The VG310 and VG320 boot up, but voice calls might fail.
  * The output of the **show voice dsp group all** command indicates the status of DSP 1 as "FW_DNLD_FINISHED,".


An example is shown here:

```
Router#**show voice dsp group all**
DSP groups on slot 0:
dsp 1:
State: FW_DNLD_FINISHED, firmware:
```

### Workaround/Solution
Identify the date of manufacturing of the product as described in the "How to Identify Affected Products" section. If the product was manufactured on or after September 1, 2016, ensure the device runs Cisco IOS Software Release 15.6(3)M or later.
### How To Identify Affected Products
There are two ways to identify the affected product:
Option 1: The product manufactured on September 1, 2016 or later has a suffix "P" in the model name. Check the product label located on the back of the chassis for the Model Name: VG310P or VG320P. See this image for an example.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/642/fn64285_onj9v51547508935003.jpeg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/642/fn64285_onj9v51547508935003.jpeg "Related image, diagram or screenshot.")
Option 2: Enter the Cisco IOS command **show diag** and review the Longitudinal Calibration section. The first byte indicates the revision.
  * "01" indicates a manufactured date before September 1, 2016.
  * "02" or greater indicates a manufactured date of September 1, 2016 or later.


An example is shown here:

```
Router#**show diag**

Slot 0: 
VG310 Mother board 2GE, integrated VPN, 24 onboard analog FXS and 1W Port adapter, 26 ports 
Port adapter is analyzed 
Port adapter insertion time 1d04h ago 

MAC Address block size : 72 
Manufacturing Test Data : 00 00 00 00 00 00 00 00 
Longitudinal Calibration : 02 10 0E 6E 72 0E 0D 83
```

### Additional Information
  * The new Cisco IOS software is compatible with both the old and new hardware.
  * Platforms with old and new components are completely interoperable.
  * Customers with older VG310 and VG320 voice gateways can continue to use any supported software release available on the Cisco software download portal.
  * There is no change in features or any other functionality.


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/642/fn64285.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/642/fn64285.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/642/fn64285.html)
