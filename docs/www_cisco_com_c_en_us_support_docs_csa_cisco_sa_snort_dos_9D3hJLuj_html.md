  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Multiple Cisco Products Snort Modbus Denial of Service Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html) to Save Content 
Print
### Available Languages
Updated:April 26, 2022
Document ID:1642608178868464
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Multiple Cisco Products Snort Modbus Denial of Service Vulnerability
High
Advisory ID: 
cisco-sa-snort-dos-9D3hJLuj
First Published:
2022 January 19 16:00 GMT
Last Updated: 
2022 April 26 19:41 GMT
Version 1.5: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCvz25197](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvz25197)
[CSCvz27235](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvz27235)
[CSCvz34380](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvz34380)
[ More... ](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html) ,[CSCvz25197](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvz25197),[CSCvz27235](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvz27235),[CSCvz34380](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvz34380),[CSCvz79589](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvz79589)
CVE-2022-20685
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html)
CWE-190
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html)
CVSS Score:
[ Base 7.5](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H/E:X/RL:X/RC:X
CVE-2022-20685
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html)
CWE-190
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort-dos-9D3hJLuj/csaf/cisco-sa-snort-dos-9D3hJLuj.json)
Email 
## 
Summary 
  * A vulnerability in the Modbus preprocessor of the Snort detection engine could allow an unauthenticated, remote attacker to cause a denial of service (DoS) condition on an affected device.
This vulnerability is due to an integer overflow while processing Modbus traffic. An attacker could exploit this vulnerability by sending crafted Modbus traffic through an affected device. A successful exploit could allow the attacker to cause the Snort process to hang, causing traffic inspection to stop.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort-dos-9D3hJLuj>


## 
Affected Products 
  * ##  Vulnerable Products 
This vulnerability affects all open source Snort project releases earlier than Release 2.9.19 and Release 3.1.11.0. For more information, see the Snort [website](https://www.snort.org/).
This vulnerability affects the following Cisco products if they are running a vulnerable release of Cisco software:
    * Cyber Vision Software
    * FirePOWER Services Software - All platforms
    * Firepower Threat Defense (FTD) Software - All platforms
    * Meraki MX Series Software
**Note** : For FTD Software, Modbus inspection is enabled by default for the Security Over Connectivity and Max Detect Network Analysis Policies (NAP). For Cyber Vision Software and Meraki MX Series Software, Modbus inspection is enabled by default.
This vulnerability affects the following Cisco products if they are running a release earlier than the first fixed release of Cisco Unified Threat Defense (UTD) Snort Intrusion Prevention System (IPS) Engine for Cisco IOS XE Software or Cisco UTD Engine for Cisco IOS XE SD-WAN Software:
    * 1000 Series Integrated Services Routers (ISRs)
    * 4000 Series Integrated Services Routers (ISRs)
    * Catalyst 8000V Edge Software
    * Catalyst 8200 Series Edge Platforms
    * Catalyst 8300 Series Edge Platforms
    * Catalyst 8500 Series Edge Platforms
    * Catalyst 8500L Series Edge Platforms
    * Cloud Services Routers 1000V
    * Integrated Services Virtual Routers (ISRv)
**Note** : UTD is not installed on these devices by default.
For information about which Cisco software releases are vulnerable, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html#fs) section of this advisory.
### Determine Whether UTD is Enabled
To determine whether UTD is enabled on a device, issue the **show utd engine standard status** command and check for a **Yes** under **Running**. The following output shows a device with UTD enabled:
> 
```
Router# **show utd engine standard status **  
> Engine version       : 1.0.19_SV2.9.16.1_XE17.3  
> Profile              : Cloud-Low  
> System memory        :  
>              Usage  : 6.00 %  
>              Status : Green  
> Number of engines    : 1
```
  
>  
```
Engine        **Running**    Health     Reason      
> ===========================================  
> Engine(#1):   **Yes**        Green      None  
> =======================================================
  
> .  
> .  
> .
```

If there is no output after issuing the command, the device is not affected.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect the following Cisco products:
    * Adaptive Security Appliance (ASA) Software
    * Firepower Management Center (FMC) Software


## 
Details 
  * For the Meraki MX series devices, exploitation of this vulnerability results in the bypass of inspection services. This could result in malicious traffic not generating alerts and in turn reaching devices that are located behind the MX series device. For this reason, the Security Impact Rating (SIR) for Meraki MX devices is Medium.
For Cyber Vision, exploitation of this vulnerability results in the bypass of Snort intrusion detection (IDS) services. This could result in malicious traffic not generating alerts. Deep packet inspection (DPI) and anomaly detection services are not impacted. For this reason, the SIR for Cyber Vision software is Medium.


## 
Workarounds 
  * While there are no workarounds that address this vulnerability, for FTD Software that is managed by Firepower Management Center (FMC) the Modbus preprocessor can be disabled to mitigate the attack vector for this vulnerability.
To disable a preprocessor in an FTD NAP for a device running Snort 2, see [Preprocessor Configuration in a Network Analysis Policy Notes](https://www.cisco.com/c/en/us/td/docs/security/firepower/70/configuration/guide/fpmc-config-guide-v70/getting_started_with_network_analysis_policies.html#ID-2245-000001d4).
To disable an inspector in an FTD NAP for a device running Snort 3, see [Custom Network Analysis Policy Creation for Snort 3](https://www.cisco.com/c/en/us/td/docs/security/firepower/70/configuration/guide/fpmc-config-guide-v70/getting_started_with_network_analysis_policies.html#Cisco_Concept.dita_a05cb5f4-3dc2-47f2-8aa1-b928ed67a410_snort3).
For an FTD device managed by Firepower Device Manager (FDM), the device must be running Snort 3. For more information, see [Configuring the Network Analysis Policy (Snort 3)](https://www.cisco.com/c/en/us/td/docs/security/firepower/710/fdm/fptd-fdm-config-guide-710/fptd-fdm-intrusion.html#Cisco_Task_in_List_GUI.dita_49189b70-682c-4336-9620-fe104df820f6).
If you need assistance implementing this mitigation, contact the [Cisco Technical Assistance Center (TAC)](https://www.cisco.com/go/tac/).
While this mitigation has been deployed and was proven successful in a test environment, customers should determine the applicability and effectiveness in their own environment and under their own use conditions. Customers should be aware that any workaround or mitigation that is implemented may negatively impact the functionality or performance of their network based on intrinsic customer deployment scenarios and limitations. Customers should not deploy any workarounds or mitigations before first evaluating the applicability to their own environment and any impact to such environment.


## 
Fixed Software 
  * Cisco has released free software updates that address the vulnerability described in this advisory. Customers may only install and expect support for software versions and feature sets for which they have purchased a license. By installing, downloading, accessing, or otherwise using such software upgrades, customers agree to follow the terms of the Cisco software license:  
<https://www.cisco.com/c/en/us/products/end-user-license-agreement.html>
Additionally, customers may only download software for which they have a valid license, procured from Cisco directly, or through a Cisco authorized reseller or partner. In most cases this will be a maintenance upgrade to software that was previously purchased. Free security software updates do not entitle customers to a new software license, additional software feature sets, or major revision upgrades.
When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Customers Without Service Contracts
Customers who purchase directly from Cisco but do not hold a Cisco service contract and customers who make purchases through third-party vendors but are unsuccessful in obtaining fixed software through their point of sale should obtain upgrades by contacting the Cisco TAC: <https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html>
Customers should have the product serial number available and be prepared to provide the URL of this advisory as evidence of entitlement to a free upgrade.
### Fixed Releases
**FTD and FirePOWER Services Software**  
| Cisco FTD and FirePOWER Services Software Release  | First Fixed Release  |  
| --- | --- |  
| 6.2.2 and earlier1  | Migrate to a fixed release.  |  
| 6.2.3  | Migrate to a fixed release.  |  
| 6.3.01  | Migrate to a fixed release.  |  
| 6.4.0  | 6.4.0.13  |  
| 6.5.01  | Migrate to a fixed release.  |  
| 6.6.0  | 6.6.5.1  |  
| 6.7.0  | Migrate to a fixed release.  |  
| 7.0.0  | 7.0.1  |  
1. Cisco FMC and FTD Software releases 6.2.2 and earlier, as well as releases 6.3.0 and 6.5.0, have reached [end of software maintenance](https://www.cisco.com/c/en/us/products/eos-eol-listing.html). Customers are advised to migrate to a supported release that includes the fix for this vulnerability.
For instructions on upgrading your FTD device, see [Cisco Firepower Management Center Upgrade Guide](https://www.cisco.com/c/en/us/td/docs/security/firepower/upgrade/fpmc-upgrade-guide/getting_started.html).
**Cyber Vision Software**  
| Cisco Cyber Vision Software Release  | First Fixed Release for This Vulnerability  |  
| --- | --- |  
| 3.2 and earlier  | Migrate to a fixed release.  |  
| 4.0  | 4.0.2  |  
**Meraki MX Software**  
| Cisco Meraki MX Software Release  | First Fixed Release  |  
| --- | --- |  
| MX14  | Migrate to a fixed release.  |  
| MX15  | Migrate to a fixed release.  |  
| MX16  |  16.16  |  
**UTD Software**  
| Cisco UTD Software Release  | First Fixed Release  |  
| --- | --- |  
| 16.12  | 16.12.7  |  
| 17.3  | 17.3.5  |  
| 17.6  | 17.6.2  |  
| 17.7  | Not vulnerable.  |  
**Snort Software**  
| Cisco Snort Software Release  | First Fixed Release  |  
| --- | --- |  
| 2.x  | 2.9.19  |  
| 3.x  | 3.1.11.0  |  
The Cisco Product Security Incident Response Team (PSIRT) validates only the affected and fixed release information that is documented in this advisory.


## 
Exploitation and Public Announcements 
  * The Cisco Product Security Incident Response Team (PSIRT) is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory.


## 
Source 
  * Cisco would like to thank Uri Katz of Claroty Research for reporting this vulnerability.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Action Links for This Advisory 
  * [Snort Rule 58906-58907](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html)


## 
Related to This Advisory 
## 
URL 
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort-dos-9D3hJLuj>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.5  | Updated Meraki fixed release.  | Fixed Releases  | Final  | 2022-APR-26  |  
| 1.4  | Added FirePOWER Services Software.  | Vulnerable Products, Fixed Software  | Final  | 2022-FEB-04  |  
| 1.3  | Clarified FTD policies that have Modbus enabled by default. Provided guidance on disabling Modbus preprocessor.  | Vulnerable Products, Workarounds  | Final  | 2022-JAN-26  |  
| 1.2  | Updated the platforms that will receive a hotfix.  | Fixed Software  | Final  | 2022-JAN-26  |  
| 1.1  | Updated affected releases and fixed releases for Snort software. Updated Cyber Vision product naming.  | Affected Releases, Details, and Fixed Software  | Final  | 2022-JAN-21  |  
| 1.0  | Initial public release.  | —  | Final  | 2022-JAN-19  |  
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
Action Links for This Advisory 
  * [Snort Rule 58906-58907](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html)


## 
Related to This Advisory 
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-dos-9D3hJLuj.html "Back to Top")
By continuing to use our website, you acknowledge the use of cookies. 
[Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html) Change Settings
![Company Logo](https://cdn.cookielaw.org/logos/03fc55fe-0057-4b2f-817d-763e7ecdb316/a7f4c642-c43c-4666-acea-858c0449029c/cisco-logo-transparent.png)
## Consent Manager
Your opt out preference signal is honored.
## Consent Manager
  * ### Your Privacy
  * ### Strictly Necessary Cookies
  * ### Performance Cookies
  * ### Targeting Cookies
  * ### Functional Cookies


#### Your Privacy
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. From the list on left, please choose whether this site may use Performance and/or Targeting Cookies. By selecting Strictly Necessary Cookies only, you are requesting Cisco not to sell or share your personal data. Note, blocking some types of cookies may impact your experience on the site and the services we are able to offer.
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies provide metrics related to the performance and usability of our site. They are primarily focused on gathering information about how you interact with our site, including: page load times, response times, error messages, and allowing a replay of a visitor’s interactions with our site, which enables us to review and analyze visitor behavior, helping to improve site usability and functionality. These cookies also allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. If you do not allow these cookies we will not know when you have visited our site and will not be able to monitor its performance.
Cookies Details
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Cookies Details
Back Button
### Cookie List
Filter Button
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Clear
  * checkbox label label


Apply Cancel
Save Settings
Allow All
[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/solutions/consent-and-preferences/)
