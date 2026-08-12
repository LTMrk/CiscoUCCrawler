  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72074.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72074.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72074.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72074.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72074.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Hyperconverged Infrastructure](https://www.cisco.com/c/en/us/support/servers-unified-computing/category.html)
  * [Cisco HyperFlex HX-Series](https://www.cisco.com/c/en/us/support/hyperconverged-systems/hyperflex-hx-series/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/hyperconverged-systems/hyperflex-hx-series/products-field-notices-list.html)


# Field Notice: FN72074 - 64GB 2666MHz RDIMM Wear Out Failures - Replace on Failure
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/720/fn72074.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72074.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/720/fn72074.html)


Updated:May 1, 2023
Document ID:FN72074
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Product Name  | Description  | Comments  |  
| --- | --- | --- |  
| AMPPC-MEM-64GB  | Cisco Secure Endpoint 64GB DDR4 RAM (2400Mhz/PC4-19200/1.2v)  |   |  
| HX-MR-X64G4RS-H  | 64GB DDR4-2666-MHz TSV-RDIMM/PC4-21300/quad rank/x4/1.2v  |   |  
| HX-MR-X64G4RS-H=  | 64GB DDR4-2666-MHz TSV-RDIMM/PC4-21300/quad rank/x4/1.2v  |   |  
| TA-MR-X64G4RS-H  | 64GB DDR4-2666-MHz TSV-RDIMM/PC4-21300/quad rank/x4/1.2v  |   |  
| TA-MR-X64G4RS-H-OP  | 64GB DDR4-2666-MHz TSV-RDIMM/PC4-21300/quad rank/x4/1.2v  |   |  
| UCS-MR-X64G4RS-H  | 64GB DDR4-2666-MHz TSV-RDIMM/PC4-21300/quad rank/x4/1.2v  |   |  
| UCS-MR-X64G4RS-H=  | 64GB DDR4-2666-MHz TSV-RDIMM/PC4-21300/quad rank/x4/1.2v  | Part Alternate  |  
  
  

  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCvx07803](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvx07803)  | 64GB 2666MHz RDIMM Wear Out Failures  |  
  

### Problem Description
  

A limited number of 64GB DIMMs shipped from Cisco are impacted by a known deviation in the manufacturing process. This deviation might result in a higher rate of failure. A replacement is recommended.
  

### Background
  

Cisco has identified an issue with a limited number of 64GB DIMMs manufactured within a single lot. This issue is confined to a specific set of DIMMs which can be identified by the serial number. Most of the affected DIMMs shipped in early 2019. Manufacturing process improvements have been established in order to prevent similar escapes.
  

### Problem Symptom
  

DIMMs might exhibit correctable or uncorrectable errors. If encountered during runtime, uncorrectable errors might cause a sudden catastrophic server reset. If encountered during Power-On Self-Test (POST), the DIMM will be mapped out and the total available memory reduced.
  

### Workaround/Solution
  

This is a hardware error. A hardware replacement is recommended. 
If a DIMM does not come up healthy on the first boot after the replacement process, verify the physical DIMM seating before you swap the DIMM. Seating is the most common cause for immediate DIMM errors when swapping larger quantities of DIMMs.
Cisco recommends to run memory diagnostics prior to placing servers into production in order to mitigate early runtime errors. For more details, visit the "Testing memory" section of [Cisco UCS HX M5 Memory Technical Overview - Memory RAS Features](https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/technical-overview-c17-743902.html).
To request a replacement, open a case with the Technical Assistance Center (TAC) for a replacement for the failed DIMMs.
  

### How to Identify Affected Products
  

Impacted DIMMs can be identified based on their serial number. There are two methods to retrieve a DIMM serial number.
**Note:** The manufacturer's serial numbers are 18 alphanumeric characters long. Cisco Unified Computing System (UCS) Manager output will truncate this to the last eight characters. This truncated serial number is sufficient to identify an impacted DIMM. If you have trouble retrieving your serial number, there are other methods available to Cisco. Reach out to your account team or the Technical Assistance Center (TAC) for further instructions.
**CLI (Preferred)**
Use SSH to connect to your UCS Manager CLI and enter this command. The “Vendor Serial (SN)” field is the serial number of your DIMM(s) and can be entered into the Serial Number Validation Tool.

```
FI-B# **show server inventory memory detail | grep Serial**
    Equipped Serial (SN): FCH22207VKZ
    Acknowledged Serial (SN): FCH22207VKZ
        Serial (SN): FCH22207VKZ
            Serial (SN):
                Vendor Serial (SN): 390BB7C1
                Vendor Serial (SN):
                Vendor Serial (SN): 390BB7BF
                Vendor Serial (SN): 390BB4F6
                Vendor Serial (SN): 390BB37C
```

**GUI**
_UCS Manager_
Navigate to the **Server** tab in the Navigation pane of your UCS Manager. Choose a server.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72074img1.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72074img1.jpg "Related image, diagram or screenshot.")
In the Action Pane, click the **Inventory > Memory** tabs.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72074img2.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72074img2.jpg "Related image, diagram or screenshot.")
Click a DIMM and verify the serial number.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72074img3.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72074img3.jpg "Related image, diagram or screenshot.")
_Cisco Integrated Management Controller_
Log into the Cisco Integrated Management Controller (IMC) and choose**Chassis > Inventory** in the left navigation pane.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72074img4.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72074img4.jpg "Related image, diagram or screenshot.")
Click the **Memory** tab in the center Action pane in order to view the DIMM serial numbers.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72074img5.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72074img5.jpg "Related image, diagram or screenshot.")
  

### Serial Number Validation
  

The Cisco Support Assistant (CSA) can help verify whether a device is impacted by the issue that is described in this Field Notice. To check the device, either enter the serial number in the CSA on the right side of this page or click the following URL: <https://cs.co/FNSNV>.
### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.2  | Updated fix on fail instructions.  | Workaround/Solution  | 2023-MAY-01  |  
| 1.1  | Updated the Upgrade Program to use Support Case Manager (SCM).  | Upgrade Program Information  | 2023-APR-06  |  
| 1.0  | 64GB 2666MHz RDIMM Wear Out Failures  | —  | 2021-APR-12  |  
  

### For More Information
###   

If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  

  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)

  

### Receive Email Notification For New Field Notices
  

[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify. 
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72074.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72074.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [UCS C3260 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c3260-rack-server/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/720/fn72074.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72074.html)
