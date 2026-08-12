  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64185.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64185.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64185.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64185.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64185.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Collaboration Endpoints](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Cisco IP Phone 8800 Series](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-field-notices-list.html)


# Field Notice: FN - 64185 - Cisco Phone 8831 - DECT Compliance Issue in Select Markets Outside North America - New Configuration, Firmware Update, or Replacement Required 
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/641/fn64185.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64185.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/641/fn64185.html)


Updated:October 24, 2016
Document ID:FN64185
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### NOTICE: 
### THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME. 
### Revision History  
| Revision  | Date  | Comment  |  
| --- | --- | --- |  
| 1.1  | 24-OCT-2016  | Updated the Products Affected, Background, and Workaround/Solution Sections   |  
| 1.0  | 02-SEP-2016  | Initial Public Release  |  
### Products Affected  
| Products Affected  |  
| --- |  
| CP-8831-BR-K9=  |  
| CP-8831-EU-K9=  |  
| CP-8831-K9=  |  
| CP-8831-LA-K9=  |  
### Problem Description
Some Cisco Phone 8831 base units were shipped to regions outside North America with the Digital Enhanced Cordless Telecommunications (DECT) radio setting configured to a frequency for North America. In markets where DECT radios are not permitted, this could mean that the devices are not compliant. Dependent upon their location, affected users might need to permanently disable the DECT radio on the CP-8831 base, configure their device to the appropriate frequency, or replace the device with a No Radio (NR) version.
### Background
Regional variants were developed for Europe (EU) and other regions. Dependent upon the local regulations, users in these markets with DECT "Radio On" units shipped before the availability of the NR model might need to:
  * Download CP-8831-NR firmware in order to disable DECT permanently, or
  * Configure their device to the appropriate frequency


In regions of the world where DECT is not compliant at any frequency, such as China, Brazil, and India, an NR version of the Cisco CP-8831 is now orderable and available worldwide. With the CP-8831 NR version, the DECT radio hardware is physically present on the printed circuit board (PCB), but disabled by the firmware. No firmware can be loaded onto the NR version of the 8831 that will enable the DECT radio. The end-user or system integrator will be unable to power the radio in order to ensure it is compliant. 
For additional details and regional product IDs, see [Field Notice Number 63899](http://www.cisco.com/c/en/us/support/docs/field-notices/638/fn63899.html), titled CP-8831 Radio Frequency Issue - Upgrade Needed.
### Problem Symptoms
The issue will not affect operation, but affected customers' need to comply with regulatory requirements in the country or region where their CP-8831 units are located.
### Workaround/Solution
These products are available in which the DECT radio has been disabled:
  * CP-8831-NR-K9= (Base plus DCU)
  * CP-8831-BASE-S-NR= (Base only)
  * CP-8831-DC-NR-K9= (Daisy Chain Kit)


End-customers located in regions where DECT is prohibited and already own a CP-8831 with DECT can contact the Technical Assistance Center (TAC) and request the CP-8831-NR firmware version.
**Important Note** : Once the CP-8831-NR firmware version has been downloaded, the CP-8831 cannot be returned to DECT capabilities.
Customers who have the NR version of the 8831 can use the wired extension microphones and the Daisy Chain unit in order to extend the audio reach of their Cisco 8831.
For those customers who are unable to reach the TAC, contact 8831-radiofrequency@cisco.com for additional instructions.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods: 
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/start)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64185.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64185.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/641/fn64185.html)
