  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72368.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72368.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72368.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72368.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72368.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Conferencing](https://www.cisco.com/c/en/us/support/conferencing/category.html)
  * [Cisco Meeting Server](https://www.cisco.com/c/en/us/support/conferencing/meeting-server/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/conferencing/meeting-server/products-field-notices-list.html)


# Field Notice: FN - 72368 - Some DIMMs Might Fail Prematurely Due to a Manufacturing Deviation - Hardware Upgrade Available
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/723/fn72368.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72368.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/723/fn72368.html)


Updated:December 21, 2022
Document ID:FN72368
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 2.1  | 16-Nov-22  | Updated the Upgrade Program to Use Support Case Manager (SCM)  |  
| 2.0  | 28-Oct-22  | Updated the Products Affected and Background Sections  |  
| 1.1  | 10-May-22  | Updated to correct 64G memory PID  |  
| 1.0  | 05-May-22  | Initial Release  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| CNBR-MR-X32G2RT-H  |   |  
| UCS-ML-X64G4RS-H  |   |  
| CSP-MR-X32G2RS-H  |   |  
| CIT3-MR-X16G1RS-H  |   |  
| ULTM-MR-X32G2RS-H  |   |  
| UCS-MR-X32G2RT-H=  |   |  
| BE7K-RAM  |   |  
| CSP-MR-X16G1RS-H  |   |  
| UCS-MR-X32G2RS-H=  |   |  
| BE6K-RAM-M5-NEW  |   |  
| CSP-MR-X16G1RT-H  |   |  
| CSP-MR-X32G2RT-H  |   |  
| BE7K-RAM-M5-NEW  |   |  
| UCS-ML-X64G4RT-H=  |   |  
| BE6K-RAM  |   |  
| UCS-MR-X16G1RS-H=  |   |  
| UCS-MR-X16G1RT-H=  |   |  
| HX-ML-X64G4RS-H=  |   |  
| HX-MR-X32G2RS-H=  |   |  
| HX-MR-X32G2RT-H=  |   |  
| HX-MR-X16G1RT-H=  |   |  
| HX-ML-X64G4RT-H=  |   |  
| HX-MR-X16G1RS-H=  |   |  
| HX-MR-X16G1RT-H=  |   |  
| UCS-MR-X64G2RT-H=  |   |  
| UCS-ML-128G4RT-H=  |   |  
| UCS-ML-128G4RT-H  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCwb13808](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb13808)  | DIMMs from specific MFG failing at higher than expected rate  |  
### Problem Description
A limited number of DIMMs shipped from Cisco are impacted by a known deviation in the memory supplier's manufacturing process. This deviation might result in a higher rate of failure.
### Background
DIMM manufacturers compose their DIMMs of multiple memory modules to reach the desired capacity. A 16GB DIMM might be composed of the same modules that a 32GB DIMM is composed of. In this case, a manufacturing deviation in specific modules impacts 16GB, 32GB, 64GB, and 128GB DIMMs. This deviation was contained to a specific date range, and the DIMMs which use these chips were manufactured during the middle to end of 2020. Since the discovery of this deviation, additional limits have been imposed on the manufacturing process to ensure that future DIMMs are not exposed to this process variation.
### Problem Symptom
Most DIMMs with this manufacturing deviation will exhibit persistent correctable memory errors. If left untreated, the DIMMs might eventually encounter an uncorrectable memory event. If encountered during runtime, uncorrectable errors will cause a sudden unexpected server reset. If encountered during Power-On Self-Test (POST), the DIMM will be mapped out and the total available memory reduced. In some cases a boot error might be seen.
Various DIMM Reliability, Availability, and Serviceability (RAS) features or even operating system features might mask the extent of these correctable errors. It is recommended to check your DIMMs for exposure using the Serial Number Validation Tool described in the Serial Number Validation section of this field notice. Only specific DIMMs are impacted by this issue, so do not rely solely on the DIMM error count to judge exposure.
### Workaround/Solution
This is a hardware failure. A replacement is strongly recommended in order to avoid potential for unexpected server failure.
A replacement DIMM placed in the same slot as a previously failed DIMM might not immediately show as healthy. If a DIMM does not come up healthy on the first boot after the replacement process, verify the physical DIMM seating. Seating is the most common cause for immediate DIMM errors after replacement.
Cisco recommends to run memory diagnostics prior to placing servers into production in order to mitigate early runtime errors. For more details, see the Testing memory section of [Cisco UCS HX M5 Memory Technical Overview - Memory RAS Features](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/technical-overview-c17-743902.html).
### How To Identify Affected Products
Impacted DIMMs can be identified based on their serial number. Once you have identified your DIMM serial numbers, you will need to use the Serial Number Validation Tool described in the Serial Number Validation section of this field notice. These methods can be used against any Cisco Unified Computing System (UCS) or Hyperflex server, with access to a management utility (Cisco Integrated Management Controller (IMC) or UCS Manager).
**Note:** The manufacturer's serial numbers are 18 alphanumeric characters long. Cisco UCS Manager output will truncate this to the last eight characters. This truncated serial number is unique and sufficient to identify an impacted DIMM. If you have trouble retrieving your serial number, there are other methods available to Cisco. Reach out to your account team or the Technical Assistance Center (TAC) for further instructions.
**UCS Manager CLI (Simplest Method)**
Use SSH to connect to your UCS Manager CLI and enter the `**show server inventory memory detail | egrep "^Server|Serial"**`command. The Vendor Serial (SN) field is the serial number of your DIMM(s) and can be entered into the Serial Number Validation Tool. Note that unpopulated memory slots will show as blank.

```
FI-B# **show server inventory memory detail | egrep "^Server|Serial"**
Server 1/1:
    Equipped Serial (SN): FCH185071HQ
    Acknowledged Serial (SN): FCH185071HQ
        Serial (SN): FCH185071HQ
            Serial (SN):
                Vendor Serial (SN): 18ED63ED
                Vendor Serial (SN): 18ED63EC
                Vendor Serial (SN):
                Vendor Serial (SN): 18ED6F62
                Vendor Serial (SN): 18ED63EE
                Vendor Serial (SN):
                Vendor Serial (SN): 18F0457C
                Vendor Serial (SN): 18ED6E94
```

**Cisco IMC CLI**
Log into the Cisco IMC via SSH and enter these commands.

```
C220-FCHXXXXXXXX# **scope chassis**
C220-FCHXXXXXXXX /chassis # **show dimm detail | grep Serial**
    Serial Number: 80BA3892
    Serial Number: NA
    Serial Number: NA
    Serial Number: 80BA3863
```

**Intersight - Managed Object Browser or API Browser (Preferred Method)**
You can use the Managed Object Browser (MOB), which is a developer tool, to retrieve and then export the DIMM serial numbers and their location. Open a web browser and log into your Intersight account. Then, open a new tab in the same browser and open the [Intersight Developer Center](https://www.intersight.com/mobrowser/list/memory/Unit/).
**Note:** For users who have an Intersight appliance, use:  
https://[FQDN of appliance]/mobrowser/list/memory/Unit.
Add a search attribute of "Serial" with the value "ne "" (this filters for "Not Equal to NULL") to filter out empty slots. You can then export the results for use with the Serial Number Validation Tool.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72368img1.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72368img1.jpg "Related image, diagram or screenshot.")
Alternatively, you can use the Intersight API REST Client to generate and send a query which will return your DIMM SNs and location. After you log into Intersight, open a new tab and open the [Intersight Developer Center API Reference](https://intersight.com/apidocs/apirefs/api/v1/memory/Units/get/).
**Note:** For users who have an Intersight appliance, use:  
https://[fqdn of appliance]/apidocs/apirefs/api/v1/memory/Units/get/.
Add a new Query Parameter with the Key/Value pair "$select" and "Serial,Dn,Location,RegisteredDevice", another key/value of "$filter" and "Serial ne ''", "$expand" and "RegisteredDevice($select=DeviceHostname)", and a final pair of "$top" "1000". The resulting request will return a list of DIMMs, their serial number, and location for use with the Serial Number Validation Tool while filtering out null values.
**Note:** This will only return a maximum of 1000 DIMMs (the limit of API calls). If your install base contains greater than 1000 DIMMs, create a new Key/Value pair of "$skip" "1000" (or 2000, 3000, and so on) and query again. If you are unsure that you have more than 1000 DIMMs installed, you can add the "$inlinecount" "allpages" key/value pair to return the "count" of populated DIMMs. If you have difficulty querying your DIMM serial numbers, reach out to your account team or the Technical Assistance Center (TAC) for assistance.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72368img2.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72368img2.jpg "Related image, diagram or screenshot.")
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72368img3.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72368img3.jpg "Related image, diagram or screenshot.")
**Intersight (HTTP UI)**
You can view the individual DIMM serial numbers in the Intersight UI. Navigate to the **Server > Inventory** page and expand the Memory list.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72368img4.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72368img4.jpg "Related image, diagram or screenshot.")
**Intersight Advantage and Premier Customers**
Intersight Advantage and Premier customers will be automatically alerted for impacted DIMMs. Review the Advisories tab of your Intersight account for FN72368.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72368img5.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72368img5.jpg "Related image, diagram or screenshot.")
### Serial Number Validation
The Cisco Support Assistant (CSA) can help verify whether a device is impacted by the issue that is described in this Field Notice. To check the device, either enter the serial number in the CSA on the right side of this page or click the following URL: <https://cs.co/FNSNV>.
### Upgrade Program Information
Support Case Manager _must_ be used for ordering replacement parts for this Field Notice.
Click on the following link to open Support Case Manager in a new tab:   
[ https://mycase.cloudapps.cisco.com/fieldnotice?fn=FN72368](https://mycase.cloudapps.cisco.com/fieldnotice?fn=FN72368)
  1. Serial Numbers (SNs) must be provided and be affected. 
     * SN Entitlement Check will be performed. 
     * Order entry supports up to 50 SNs per request. If you have more than 50, you will need to submit more than 1 request. 
  2. One ship to address per request. 
  3. Service Request number (SR#) is not required, but if you have an Existing SR# please enter it for better tracking purposes. 


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72368.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Customers Also Viewed
  * [Generate CSR and Apply Certificates to CMS](https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/214618-generate-csr-and-apply-certificates-to-c.html)
  * [Configure Recorder on CMS Server](https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server-1000/225405-configure-recorder-on-cms-server.html)
  * [Configure CMS WebRTC or Web App Proxy over Expressway](https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/210800-configure-cms-webrtc-proxy-over-expressw.html)
  * [Configure Meeting Server (CMS) Call Bridge Database Cluster](https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/210530-configure-cisco-meeting-server-call-brid.html)
  * [Configure CMS Scheduler and Schedule a Meeting on Web App](https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server-1000/217367-configuring-cisco-meeting-server-schedul.html)
  * + Show 2 More


### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72368.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Business Edition 6000 Version 12.5](https://www.cisco.com/c/en/us/support/unified-communications/business-edition-6000-version-12-5/model.html)
  * [Business Edition 6000 Version 14](https://www.cisco.com/c/en/us/support/unified-communications/business-edition-6000-version-14/model.html)
  * [Business Edition 7000 Version 12.5](https://www.cisco.com/c/en/us/support/unified-communications/business-edition-7000-version-12-5/model.html)
  * [Business Edition 7000 Version 14](https://www.cisco.com/c/en/us/support/unified-communications/business-edition-7000-version-14/model.html)
  * [UCS C220 M5 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c220-m5-rack-server/model.html)
  * [UCS C240 M5 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c240-m5-rack-server/model.html)
  * [UCS C480 M5 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c480-m5-rack-server/model.html)

+ Show All 7 Products
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/723/fn72368.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72368.html)
