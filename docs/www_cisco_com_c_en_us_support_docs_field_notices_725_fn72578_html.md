  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72578.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72578.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72578.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72578.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72578.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Switches](https://www.cisco.com/c/en/us/support/switches/category.html)
  * [Cisco Embedded Services 3300 Series Switches](https://www.cisco.com/c/en/us/support/switches/embedded-service-3000-series-switches/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/switches/embedded-service-3000-series-switches/products-field-notices-list.html)


# Field Notice: FN72578 - Cisco IOS XE - Smart Licensing Using Policy Might Cause High CPU/Memory Usage - Software Upgrade Recommended
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/725/fn72578.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72578.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/725/fn72578.html)


Updated:September 29, 2023
Document ID:FN72578
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| IOS XE Software  | 17  | 17.3.2a, 17.3.3, 17.3.4, 17.3.5, 17.3.6, 17.4.1, 17.5.1, 17.6.1, 17.6.2, 17.6.3, 17.6.4, 17.7.1  |   |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCvv72609](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvv72609)  | SmartLicense: High CPU usage triggered by RUM reports  |  
| [CSCwa85525](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwa85525)  | Memory leak in *MallocLite* due to growing Smart Agent Memory Utilization  |  
| [CSCwa85199](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwa85199)  | Unacknowledged Reports can cause High CPU Utilization due to Smart Agent  |  
  

### Problem Description
  

For affected versions of the Cisco IOS® XE software, devices might report high CPU or memory usage. In some scenarios, devices might report both high CPU and memory usage. 
This issue is seen only when the 'Smart Licensing Using Policy' feature is implemented on the device.
  

### Background
  

This issue is seen when the "Smart Licensing Using Policy" feature is implemented, and Resource Utilization Measurement (RUM) reports are accumulated in large quantities on the device.
The underlying reason for the accumulation could be a communication issue between the device and Cisco Smart Software Manager (CSSM). When RUM reports do not get the required acknowledgement, they accumulate on the device and can cause high CPU/memory usage.
  

### Problem Symptom
  

The underlying reason for the RUM report accumulation could be a communication issue between the device and Cisco Smart Software Manager (CSSM).
This error log might be observed in the affected device:
`%SMART_LIC-3-COMM_FAILED: Communications failure with the Cisco Smart Software Manager (CSSM) : Communications failure`
This issue can occur when there is an increasing trend of accumulated RUM reports in the device. The increasing trend of accumulated RUM reports can be viewed with multiple iterations of these commands:
Sample output is shown here:

```
system#**license smart save usage all file flash:report.txt**

system#**more flash:report.txt | count RUMReport**

Number of lines which match regexp = 214 <<<< This counter may increase over multiple iterations
```

Cisco has observed that at 1000 RUM reports, high CPU/memory usage might be seen. This value, however, is not fixed and will vary depending on network conditions and topology. It is highly recommended that the mitigation steps (see the Workaround/Solution section) are taken as soon as RUM reports start to accumulate.
For high CPU, the processes `“SAGetRUMIds”` and `“SAUtilRepSave”` will be seen.
Sample output is shown here:

```
system#**show processes cpu sorted**

CPU utilization for five seconds: 99%/99%; one minute: 99%; five minutes: 99% 

 PID  Runtime(ms)    Invoked      uSecs   5Sec   1Min   5Min TTY Process

 725  4042749037   313719798      12886 75.29% 77.09% 76.24%   0 SAGetRUMIds 

 154   164791260   261212986        630 21.62% 21.81% 22.97%   0 SAUtilRepSave
```

For high memory usage, there will be an increasing trend in memory held by the `“MallocLite”` process.
Sample output is shown here:

```
system#**show processes memory sorted**

Processor Pool Total: 1348707052 Used:  317607088 Free: 1031099964

reserve P Pool Total:     102404 Used:         88 Free:     102316

 lsmpi_io Pool Total:    6295128 Used:    6294296 Free:        832

 PID TTY  Allocated      Freed      Holding    Getbufs    Retbufs Process

  0   0          0          0    1205727320          0          0 *MallocLite*

  0   0  335560736   76485816     238693656          0          0 *Init*
```
  

### Workaround/Solution
  

**Workaround**
The underlying reason for the RUM report accumulation could be a communication issue between the device and CSSM. Ensure that the underlying connectivity operates as expected for your network as per the smart licensing implementation.
Either of these workarounds can be implemented in order to temporarily resolve the issue:
  * Clean Up RUM Report Accumulation 
Enter the `**license smart factory reset**`command followed by a device reload with the`**reload**`command.

```
system#**license smart factory reset**

%Warning: reload required after "license smart factory reset" command

system#**reload**
```

  * Manual Sync of RUM Reports 
The RUM reports can be manually synced with CSSM. For instructions on how to manually sync the RUM Reports, see [Uploading Data or Requests to CSSM and Downloading a File](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9600/software/release/17-11/configuration_guide/sys_mgmt/b_1711_sys_mgmt_9600_cg/sl_using_policy.html#Cisco_Task_in_List_GUI.dita_3e53f569-57a0-4aa7-a53f-f105c4d466e7).


**Solution**
In order to resolve this issue, upgrade to one of these fixed Cisco IOS XE software releases:
  * Cisco IOS XE Release 17.3.7 or later
  * Cisco IOS XE Release 17.6.5 or later
  * Cisco IOS XE Release 17.9.1 or later


The software can be downloaded from the [Cisco Software Download](https://software.cisco.com/download/home) website.
Cisco strongly recommends that customers review the software download page for the current recommended starred releases and upgrade to those releases.
  

### For More Information
  

These products are affected:
  * Cisco 1000 Series Integrated Services Routers
  * Cisco 1100 Integrated Services Router
  * Cisco 4000 Series Integrated Services Routers
  * Cisco 4221 Integrated Services Router
  * Cisco 4321 Integrated Services Router
  * Cisco 4331 Integrated Services Router
  * Cisco 4351 Integrated Services Router
  * Cisco 4431 Integrated Services Router
  * Cisco 4451-X Integrated Services Router
  * Cisco 4461 Integrated Services Router
  * Cisco ASR 1000 Series Aggregation Services Routers
  * Cisco ASR 1000 Series IOS XE SD-WAN
  * Cisco ASR 1001-HX Router
  * Cisco ASR 1001-X Router
  * Cisco ASR 1002-HX Router
  * Cisco ASR 1002-X Router
  * Cisco ASR 1004 Router
  * Cisco ASR 1006 Router
  * Cisco ASR 1006-X Router
  * Cisco ASR 1009-X Router
  * Cisco ASR 1013 Router
  * Cisco Catalyst 8000V Edge Software
  * Cisco Catalyst 8200 Series Edge Platforms
  * Cisco Catalyst 8300 Series Edge Platforms
  * Cisco Catalyst 8500 Series Edge Platforms
  * Cisco Catalyst 8500L Series Edge Platforms
  * Cisco Catalyst 9200 Series Switches
  * Cisco Catalyst 9200L Switch Stack
  * Cisco Catalyst 9300 Series Switches
  * Cisco Catalyst 9300L Series Switches
  * Cisco Catalyst 9400 Series Switches
  * Cisco Catalyst 9500 Series Switches
  * Cisco Catalyst 9600 Series Switches
  * Cisco Catalyst 9800-40 Wireless Controller
  * Cisco Catalyst 9800-80 Wireless Controller
  * Cisco Catalyst 9800-CL Wireless Controller for Cloud
  * Cisco Catalyst 9800-L-C Wireless Controller
  * Cisco Catalyst 9800-L-F Wireless Controller
  * Cisco Cloud Services Router 1000V Series
  * Cisco CSR 1000V Series IOS XE SD-WAN
  * Cisco Embedded Wireless Controller on Catalyst 9115AX Access Points
  * Cisco Embedded Wireless Controller on Catalyst 9117AX Access Points
  * Cisco Embedded Wireless Controller on Catalyst 9120AX Access Points
  * Cisco Embedded Wireless Controller on Catalyst 9130AX Access Points
  * Cisco Embedded Wireless Controller on Catalyst Access Points
  * Cisco Integrated Services Virtual Router
  * Cisco ISR 1000 Series IOS XE SD-WAN
  * Cisco ISR 4000 Series IOS XE SD-WAN
  * Cisco XE SD-WAN Routers

  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.0  | Initial Release  | —  | 2023-MAY-24  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications)
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72578.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Customers Also Viewed
  * [Cisco Embedded Services 3300 Series Configuration --- Installation and Boot](https://www.cisco.com/c/en/us/td/docs/switches/lan/embedded/ess3300/software_config/b-cisco-embedded-services-3300-series-configuration/m-install-and-boot.html)
  * [Cisco Embedded Services 3300 Series Configuration --- Configuring the Switch Using the Web User Interface](https://www.cisco.com/c/en/us/td/docs/switches/lan/embedded/ess3300/software_config/b-cisco-embedded-services-3300-series-configuration/m-webui_config.html)
  * [Cisco Embedded Services 3300 Series Switches Hardware Technical Guide --- Implementation Options](https://www.cisco.com/c/en/us/td/docs/switches/lan/embedded/ess3300/hardware/b-cisco-embedded-services-3300-series-switches-hardware-technical-guide/m-implementation-options.html)
  * [Cisco Embedded Services 3300 Series Switches Hardware Technical Guide --- Device Zeroization and Recovery](https://www.cisco.com/c/en/us/td/docs/switches/lan/embedded/ess3300/hardware/b-cisco-embedded-services-3300-series-switches-hardware-technical-guide/m-device-zeroization-and-recovery.html)
  * [Cisco Embedded Services 3300 Series Configuration --- Implementation Options](https://www.cisco.com/c/en/us/td/docs/switches/lan/embedded/ess3300/software_config/b-cisco-embedded-services-3300-series-configuration/m-3300-implementation.html)
  * + Show 2 More


### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72578.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [4221 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4221-integrated-services-router-isr/model.html)
  * [4321 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4321-integrated-services-router/model.html)
  * [4331 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4331-integrated-services-router-isr/model.html)
  * [4351 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4351-integrated-services-router/model.html)
  * [4431 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4441-x-integrated-services-router-isr/model.html)
  * [4451-X Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4451-x-integrated-services-router-isr/model.html)
  * [4461 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4461-integrated-services-router/model.html)
  * [ASR 1000 Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/asr-1000-series-ios-xe-sd-wan/model.html)
  * [CSR 1000V Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/csr-1000v-series-ios-xe-sd-wan/model.html)
  * [Catalyst 8000V Edge Software](https://www.cisco.com/c/en/us/support/routers/catalyst-8000v-edge-software/series.html)
  * [Catalyst 9606R Switch](https://www.cisco.com/c/en/us/support/switches/catalyst-9606-switch/model.html)
  * [ESR6300 Embedded Series Router](https://www.cisco.com/c/en/us/support/routers/6300-embedded-service-router/model.html)
  * [ISR 1000 Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/isr-1000-series-ios-xe-sd-wan/model.html)
  * [ISR 4000 Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/isr-4000-series-ios-xe-sd-wan/model.html)

+ Show All 14 Products
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/725/fn72578.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72578.html)
