  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-app-bypass-cSBYCATq.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-app-bypass-cSBYCATq.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-app-bypass-cSBYCATq.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-app-bypass-cSBYCATq.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Multiple Cisco Products Snort Application Detection Engine Policy Bypass Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-snort-app-bypass-cSBYCATq.html) to Save Content 
Print
### Available Languages
Updated:May 16, 2022
Document ID:1610556829350519
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Multiple Cisco Products Snort Application Detection Engine Policy Bypass Vulnerability
Medium
Advisory ID: 
cisco-sa-snort-app-bypass-cSBYCATq
First Published:
2021 January 13 16:00 GMT
Last Updated: 
2022 May 16 18:45 GMT
Version 1.2: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCvs85467](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvs85467)
[CSCvu21318](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvu21318)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-app-bypass-cSBYCATq.html)
CVE-2021-1236
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-app-bypass-cSBYCATq.html)
CWE-670
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-app-bypass-cSBYCATq.html)
CVSS Score:
[ Base 4.0](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.0&vector=CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:C/C:N/I:L/A:N)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.0/AV:N/AC:H/PR:N/UI:N/S:C/C:N/I:L/A:N/E:X/RL:X/RC:X
CVE-2021-1236
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-app-bypass-cSBYCATq.html)
CWE-670
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-app-bypass-cSBYCATq.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort-app-bypass-cSBYCATq/csaf/cisco-sa-snort-app-bypass-cSBYCATq.json)
Email 
## 
Summary 
  * Multiple Cisco products are affected by a vulnerability in the Snort application detection engine that could allow an unauthenticated, remote attacker to bypass the configured policies on an affected system.
The vulnerability is due to a flaw in the detection algorithm. An attacker could exploit this vulnerability by sending crafted packets that would flow through an affected system. A successful exploit could allow the attacker to bypass the configured policies and deliver a malicious payload to the protected network.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort-app-bypass-cSBYCATq>


## 
Affected Products 
  * ##  Vulnerable Products 
At the time of publication, this vulnerability affected all open source Snort project releases earlier than Release 2.9.14. For more information, see the [Snort website](https://www.snort.org/).
At the time of publication, this vulnerability affected the following Cisco products if they were running a vulnerable release of Cisco software:
    * 3000 Series Industrial Security Appliances (ISAs)
    * Firepower Threat Defense (FTD) Software
At the time of publication, this vulnerability affected the following Cisco products if they were running a release earlier than the first fixed release of Cisco Unified Threat Defense (UTD) Snort Intrusion Prevention System (IPS) Engine for Cisco IOS XE Software or Cisco UTD Engine for Cisco IOS XE SD-WAN Software. **Note:** UTD is not installed on these devices by default. If the UTD file is not installed, the device is not vulnerable.
    * 1000 Series Integrated Services Routers (ISRs)
    * 4000 Series Integrated Services Routers (ISRs)
    * Cloud Services Router 1000V
    * Integrated Services Virtual Router (ISRv)
For information about which Cisco software releases are vulnerable, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-app-bypass-cSBYCATq.html#fs) section of this advisory. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
### Determine Whether UTD is Enabled
To determine whether UTD is enabled on a device, issue the **show utd engine standard status** command and check for a **Yes** under **Running**. If there is no output, the device is not affected. The following output example shows a device that has UTD enabled:
> 
```
Router# **show utd engine standard status **  
> Engine version       : 1.0.19_SV2.9.16.1_XE17.3  
> Profile              : Cloud-Low  
> System memory        :  
>              Usage  : 6.00 %  
>              Status : Green  
> Number of engines    : 1
```
  
>  
```
Engine        **Running**    Health     Reason      
> ===========================================  
> Engine(#1):   **Yes**        Green      None  
> =======================================================
  
> .  
> .  
> .
```

##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-app-bypass-cSBYCATq.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect the following Cisco products:
    * Adaptive Security Appliance (ASA) Software
    * Firepower Management Center (FMC) Software
    * Meraki Security Appliances


## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Fixed Releases
At the time of publication, Cisco Firepower Threat Defense (FTD) releases 6.5.0.5 and later contained the fix for this vulnerability.
At the time of publication, Cisco UTD Snort IPS Engine Software for IOS XE 17.4.11 contained the fix for this vulnerability.
At the time of publication, the open source Snort project release 2.9.14.10 and later contained the fix for this vulnerability. For more information, see the [Snort website](https://www.snort.org/).
See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
1. Starting in 17.2.1, IOS XE and IOS XE SD-WAN use the same image file.


## 
Exploitation and Public Announcements 
  * The Cisco Product Security Incident Response Team (PSIRT) is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory.


## 
Source 
  * This vulnerability was found during the resolution of a Cisco TAC support case.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Related to This Advisory 
## 
URL 
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort-app-bypass-cSBYCATq>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.2  | Added instructions to determine whether UTD is enabled and running.  | Vulnerable Products  | Final  | 2022-MAY-16  |  
| 1.1  | Updated vulnerability information for Cisco UTD Engine requirements.  | Vulnerable Products  | Final  | 2021-NOV-12  |  
| 1.0  | Initial public release.  | —  | Final  | 2021-JAN-13  |  
Show Complete History...


* * *
## 
Legal Disclaimer 
  * THIS DOCUMENT IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE. YOUR USE OF THE INFORMATION ON THE DOCUMENT OR MATERIALS LINKED FROM THE DOCUMENT IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS DOCUMENT AT ANY TIME.
A standalone copy or paraphrase of the text of this document that omits the distribution URL is an uncontrolled copy and may lack important information or contain factual errors. The information in this document is intended for end users of Cisco products.


## 
Feedback 
  * [Leave additional feedback](javascript:openNewWindow\(\);)


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Related to This Advisory 
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-app-bypass-cSBYCATq.html "Back to Top")
