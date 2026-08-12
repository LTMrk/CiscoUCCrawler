  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/638/fn63899.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/638/fn63899.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/638/fn63899.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/638/fn63899.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/638/fn63899.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Collaboration Endpoints](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Cisco IP Phone 8800 Series](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-field-notices-list.html)


# Field Notice: FN - 63899 - CP-8831 Radio Frequency Issue - Workaround Provided
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/638/fn63899.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/638/fn63899.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/638/fn63899.html)


Updated:May 17, 2018
Document ID:FN63899
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 17-Dec-15  | Initial Release  |  
| 10.0  | 09-Oct-17  | Migration to new field notice system  |  
| 10.1  | 17-May-18  | Updated the Defect Information Table  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| CP-8831-3PCC-K9=  |   |  
| CP-8831-BASE-S=  |   |  
| CP-8831-DC-K9=  |   |  
| CP-8831-K9=  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvf34445](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvf34445)  | There were no defects filed with this field notice at the time of publication.  |  
### Problem Description
The CP-8831 as shipped, if not configured correctly by the Unified Communications Manager (UCM) administrator, can operate with Digital Enhanced Cordless Telecommunications (DECT) frequencies inappropriate for the country that the 8831 operates within.
In addition, all 8831s deployed in Australia, Europe, Taiwan, Japan and Brazil, or any region that does not use the North American spectrum for DECT signaling, and runs firmware earlier than 10.3.1(SR2) will not be compliant with the DECT frequencies in those countries.
### Background
Today, there are options for the partner or customer to change the DECT frequency of a CP-8831 to a locally compliant band. The DECT microphone ships disabled and only becomes enabled when a user attempts to pair a microphone. The expectation was that customers and partners would follow our instructions to change the frequency band if needed. When the UCM administrator configures the wireless microphone region to the region appropriate for that country, the frequency band is made correct for that country. However, there have been a few isolated incidents whereby the wireless microphone region had not been set and the 8831 defaulted to the locale for the product or North America if the locale was not set. This causes the product to operate with DECT frequencies that are out of compliance for that country.
### Problem Symptom
If product is not specifically configured to the DECT wireless microphone region for the country it operates within, it could operate outside the established DECT frequency range for that country.
### Workaround/Solution
As there is no product defect, there is no requirement from Cisco for customers to return product already deployed at their sites.
**Ensure the Product is Configured Correctly on UCM Administrator**
If the customer experiences a problem with the DECT band on the 8831 not meeting their region's compliance specifications, the customer should follow these instructions from the [Maintain and Operate guide](http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/9_3_3/english/adminguide/CS38_BK_A8C4AC51_00_adminguide-8831/CS38_BK_A8C4AC51_00_adminguide-8831_chapter_011.pdf "Maintain and Operate Guide"), page 10 under Wireless Microphone Region Setting.
The default value for the Wireless Microphone Region setting is United States. If you use the device in a locale outside the United States and you configure a wireless microphone to pair with the device, you must change the Wireless Microphone Region setting to your region. This change is required to ensure that the wireless microphone is operated within the licensed bandwidth for the region and therefore can be operated in accordance with radiocommunications license conditions and without causing interference with other radiocommunications services.
Use Cisco Unified Communications Manager Administration to change the Wireless Microphone Region setting.
**Procedure for Interim Work-Around**
  1. In Cisco Unified Communications Manager Administration, go to **Device > Phone**.
  2. Use the Find capability to find the Cisco Unified IP Conference Phone 8831.
  3. In the Product Specific Configuration Layout area of the Phone Configuration window, change the Wireless Microphone Region setting to the region where the device is located. The drop-down box lists the available regions.


**Procedure for Solution: Apply Software Load**
Cisco is making region-specific software available to customers in the form of an engineering special. In certain countries, each 8831 is required to be locked down to the relevant DECT region for the respective country and the Engineering Special (ES) load will be pushed out to 8831 customers. In other cases, if customers request that an 8831 be locked down to a DECT region for their respective country, a Technical Assistance Center (TAC) case can be opened to get access to the ES load. Note that once this firmware is applied, the 8831 will be locked to the DECT region and will cease to default to the configuration received from the UCM administrator.
**Solution for New Orders of 8831**
Moving forward, Cisco is creating region-specific PIDs that will be locked down at manufacturing time to the wireless microphone DECT region based on the PID ordered. The PIDs are identified in these charts.
  
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/638/fn63899_njdg77.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/638/fn63899_njdg77.png "Related image, diagram or screenshot.")  
  
  
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/638/fn63899_njdg8r.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/638/fn63899_njdg8r.png "Related image, diagram or screenshot.")
There might be a small number of customers who cannot or will not change the DECT frequency on their 8831's. For those customers, contact 8831-radiofrequency@cisco.com for replacement options.
**For those devices deployed in Australia, Europe, Taiwan, Japan and Brazil, or any region that does not use the North American spectrum for DECT signaling, a firmware upgrade is mandatory.** Complete the steps below in order to upgrade the software. Failure to do so might violate local regulations. (Devices deployed in countries not listed here can also use 10.3.1(SR2) without concern.)
In order to prevent the 8831 V02 from downgrading firmware before it connects to the network when the CUCM default load is 9.3.3, complete these steps:
  1. Download 10.3.1-SR2 from Cisco.com .
  2. Load the 10.3.1-SR2 firmware onto the TFTP server .
  3. Restart the TFTP service on the CUCM.
  4. Point the new 8831s to the 10.3.1-SR2 load from the administration page for each new device.
  5. Connect a new 8831 to the network, and it will upgrade to 10.3.1-SR2.


**Workaround**
In order to recover CP-8831 V02 units that have already downgraded, complete these steps:
  1. Download [cmterm-8831-sip.9-3-3-TO-10-3-1-v2.zip from Cisco.com](https://software.cisco.com/download/release.html?mdfid=284738433&amp;softwareid=282074288&amp;os=&amp;release=10.3\(1\)SR2&amp;relind=AVAILABLE&amp;rellifecycle=&amp;reltype=latest&amp;i=!pp).
  2. From the TFTP File Management Page, load the cmterm-8831-sip.9-3-3-TO-10-3-1-v2.zip firmware onto the TFTP server.
  3. Restart the TFTP service on the CUCM.
  4. Point the new 8831s to the cmterm-8831-sip.9-3-3-TO-10-3-1-v2.zip load from the administration page for each new device.
  5. Point the new 8831s to the 10.3.1-SR2 load from the administration page for each new device.
  6. Connect a new 8831 to the network.
  7. Initiate reset to load 10.3.1-SR2.


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/638/fn63899.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/638/fn63899.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/638/fn63899.html)
