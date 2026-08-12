  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72072.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72072.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72072.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72072.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72072.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Servers - Unified Computing](https://www.cisco.com/c/en/us/support/servers-unified-computing/category.html)
  * [Cisco UCS C-Series Rack Servers](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/products-field-notices-list.html)


# Field Notice: FN72072 - UCS S3260 M5 Server Power-On Failure - Replace on Failure
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/720/fn72072.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72072.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/720/fn72072.html)


Updated:July 9, 2024
Document ID:FN72072
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Product Name  | Description  | Comments  |  
| --- | --- | --- |  
| UCS-S3260-M5SRB  | UCS S3260 M5 Server Node for Intel Scalable CPUs  |   |  
| UCS-S3260-M5SRB=  | UCS S3260 M5 Server Node for Intel Scalable CPUs  |   |  
| UCSX-TPM2-001=  | Trusted Platform Module 1.2 for UCS (SPI-based)  | Only if installed on impacted S3260  |  
| UCSX-TPM2-002=  | Trusted Platform Module 2.0 for UCS servers  | Only if installed on impacted S3260  |  
| UCSX-TPM2-002B=  | Trusted Platform Module2.0 UCS server (FIPS 140-2 Compliant)  | Only if installed on impacted S3260  |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCvt08343](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvt08343)  | UCS-S3260-M5SRB System fails to power on after an overcurrent event  |  
  

### Problem Description
  

A limited number of Unified Computing System (UCS) S3260 M5 server nodes (UCS-S3260-M5SRB) might fail to power on due to a damaged capacitor.
  

### Background
  

A subset of S3260 M5 server nodes shipped before February 2020 with a specific Voltage Regulator Module (VRM) might fail over time due to mechanical stress. This can result in a failure to power on.
This issue is isolated to a specific VRM component which is no longer in use.
Systems with susceptible components can be identified by the server serial number. See the Serial Number Validation section for the validation link.
  

### Problem Symptom
  

The Standalone Cisco Integrated Management Controller (IMC) System Event Log (SEL) will report:
  * Platform alert POWER_ON_FAIL #0x34 | Predictive Failure asserted | Asserted
  * Critical FRU_MB POWER_ON_FAIL: Platform sensor for FRU_MB, Predictive Failure asserted


UCS Manager integrated systems will report these faults:
  * Motherboard of server [X/Y] (service profile: ) power: failed
  * Unable to change server power state-MC Error(-20)


The Cisco IMC CLI output of the **`power status`**command will report VDD-Power-Good “inactive” and Power-On-Fail “active”, as shown in this example:

```
   Power Status:
   OP: [ status ]
   Power-State:                 [ on ]
   Master-State:                [ Master ]
   VDD-Power-Good:              [ inactive ]
   Power-On-Fail:               [ active ]  
   Power-Ctrl-Lock:             [ unlocked ]
   Power-System-Status:         [ Good ]
   Front-Panel Power Button:    [ Disabled ]
   Front-Panel Reset Button:    [ Disabled ]
   Source of Last Power Change: [ No Transition ]
```

Technical support logs can be checked in order to verify that the reason for the Power-On-Fail matches this specific issue. If the serial number is affected and you have experienced these symptoms, follow the normal Return Materials Authorization (RMA) process to request a replacement.
  

### Workaround/Solution
  

This is a hardware issue with no software workaround. Failed nodes should be replaced. The server serial numbers should be checked for exposure with the Serial Number Validation tool. See the Serial Number Validation section for the link.
If nodes are identified as requiring replacement, also validate if a Trusted Platform Module (TPM) is currently installed. See the How to Identify Affected Products section for more information.
  

### How to Identify Affected Products
  

Impacted servers can be identified by the serial number. Verification methods vary slightly based on management mode - UCS Manager or Standalone Cisco IMC software.
**CLI - UCS Manager**
Use SSH to connect to your UCS Manager CLI and enter this command in order to list all server inventory.

```
6454-FI-B# **show server inventory**
    2/1     UCS-S3260-M5SRB      V01          FCH22207VKZ          Equipped                   786432
```

**GUI - UCS Manager**
In UCS Manager, click the **Equipment** tab and navigate to the S3260 chassis. For each server within the chassis, click the **General** tab. Check the Properties section for the serial number details.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72072img1.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72072img1.jpg "Related image, diagram or screenshot.")
**CLI - Standalone Cisco IMC**
Use SSH to connect to your Cisco IMC CLI and enter this command:

```
    S3260# **show server**
    Server ID Serial Number PID
    --------- ------------- ----------------
    1         FCH221872CC   UCS-S3260-M5SRB

```

**GUI – Standalone Cisco IMC**
Open the menu from the top-left corner and navigate to the **Compute** section. Choose a server and click the **General** tab. In the Server Properties section, confirm the serial number.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72072img2.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72072img2.jpg "Related image, diagram or screenshot.")
**TPM Validation**
If nodes are identified as requiring replacement, also validate if a TPM is currently installed. If so, a new TPM of the matching PID must also be requested in your RMA.
**CLI - UCS Manager**
Use SSH to connect to your UCS Manager CLI and enter these commands in order to confirm the TPM status and PID for each impacted server. Confirm if a TPM is populated, Model (PID), and Serial Number.

```
**scope server X/Y** (X = chassis number, Y= blade number for each server in question)
**scope tpm 1**
**show detail**
```

Example:

```
`**scope server 3/1**`
`**scope tpm 1;show detail**`
Trusted Platform Module:
    Enabled Status: Enabled
    Active Status: Activated
    Ownership: Owned
    Tpm Revision: 2
    Model: UCSX-TPM2-002
```

**GUI - UCS Manager**
In UCS Manager, click the **Equipment** tab and navigate to the S3260 chassis. For each server within the chassis, click the **Inventory** tab, then the **Motherboard** tab. Scroll down and expand the TPM section, which will show if a TPM is installed. Confirm if a TPM is populated, Model (PID), and Serial Number.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72072img3.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72072img3.jpg "Related image, diagram or screenshot.")
  
**CLI - Standalone Cisco IMC**
Use SSH to connect to your Cisco IMC CLI and run these commands:

```
**scope chassis
scope server X (1 and/or 2)
show tpm-inventory**
```

Confirm if a TPM is populated, Model (PID), and Serial Number.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72072img4.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72072img4.jpg "Related image, diagram or screenshot.")
  
**GUI – Standalone Cisco IMC**
Open the menu from the top-left corner and navigate to the **Compute** section. Choose a server and click the **Inventory** tab, then the **TPM** tab. Confirm if a TPM is populated, Model (PID), and Serial Number.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72072img5.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/720/fn72072img5.jpg "Related image, diagram or screenshot.")
  

### Serial Number Validation
  

The Cisco Support Assistant (CSA) can help verify whether a device is impacted by the issue that is described in this Field Notice. To check the device, either enter the serial number in the CSA on the right side of this page or click the following URL: <https://cs.co/FNSNV>.
### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.3  | Added information about RMA process.  | Problem Symptom and How to Identify Affected Products  | 2024-JUL-09  |  
| 1.2  | Updated the Workaround/Solution and Problem Description sections  | Workaround/Solution; Problem Description  | 2023-JUL-24  |  
| 1.1  | Updated the Products Affected, Workaround/Solution, and How to Identify Affected Products sections.  | —  | 2021-JUL-26  |  
| 1.0  | Initial Release  | —  | 2021-MAR-26  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72072.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72072.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [UCS C3260 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c3260-rack-server/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/720/fn72072.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/720/fn72072.html)
