  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-tfo-bypass-MmzZrtes.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-tfo-bypass-MmzZrtes.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-tfo-bypass-MmzZrtes.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-tfo-bypass-MmzZrtes.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Multiple Cisco Products Snort TCP Fast Open File Policy Bypass Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-snort-tfo-bypass-MmzZrtes.html) to Save Content 
Print
### Available Languages
Updated:May 20, 2021
Document ID:1610556831591522
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Multiple Cisco Products Snort TCP Fast Open File Policy Bypass Vulnerability
Medium
Advisory ID: 
cisco-sa-snort-tfo-bypass-MmzZrtes
First Published:
2021 January 13 16:00 GMT
Last Updated: 
2021 May 20 13:27 GMT
Version 1.2: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
[Yes](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-tfo-bypass-MmzZrtes.html#workarounds)
Cisco Bug IDs:
[CSCvt43136](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvt43136)
[CSCvu88532](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvu88532)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-tfo-bypass-MmzZrtes.html)
CVE-2021-1224
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-tfo-bypass-MmzZrtes.html)
CWE-693
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-tfo-bypass-MmzZrtes.html)
CVSS Score:
[ Base 5.8](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:L/A:N)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:L/A:N/E:X/RL:X/RC:X
CVE-2021-1224
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-tfo-bypass-MmzZrtes.html)
CWE-693
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-tfo-bypass-MmzZrtes.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort-tfo-bypass-MmzZrtes/csaf/cisco-sa-snort-tfo-bypass-MmzZrtes.json)
Email 
## 
Summary 
  * Multiple Cisco products are affected by a vulnerability with TCP Fast Open (TFO) when used in conjunction with the Snort detection engine that could allow an unauthenticated, remote attacker to bypass a configured file policy for HTTP.
The vulnerability is due to incorrect detection of the HTTP payload if it is contained at least partially within the TFO connection handshake. An attacker could exploit this vulnerability by sending crafted TFO packets with an HTTP payload through an affected device. A successful exploit could allow the attacker to bypass configured file policy for HTTP packets and deliver a malicious payload.
Cisco has released software updates that address this vulnerability. There are workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort-tfo-bypass-MmzZrtes>


## 
Affected Products 
  * ##  Vulnerable Products 
At the time of publication, this vulnerability affected the following Cisco products if they were running releases earlier than the first fixed release of Cisco software:
    * 3000 Series Industrial Security Appliances (ISAs)
    * Firepower Threat Defense (FTD) Software
    * Meraki MX64
    * Meraki MX64W
    * Meraki MX67
    * Meraki MX67C
    * Meraki MX67W
    * Meraki MX68
    * Meraki MX68CW
    * Meraki MX68W
    * Meraki MX84
    * Meraki MX100
    * Meraki MX250
    * Meraki MX450
At the time of publication, this vulnerability affected the following Cisco products if they were running releases earlier than the first fixed release of Cisco UTD Snort IPS Engine Software for IOS XE or Cisco UTD Engine for IOS XE SD-WAN Software: 
    * 1000 Series Integrated Services Routers (ISRs)
    * 4000 Series ISRs
    * Catalyst 8000V Edge Software
    * Catalyst 8200 Series Edge Platforms
    * Catalyst 8300 Series Edge Platforms
    * Catalyst 8500L Edge Platforms
    * Cloud Services Router 1000V (CSR 1000V)
    * Integrated Services Virtual Router (ISRv)
For information about which Cisco software releases are vulnerable, see the [Fixed Software](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort_filepolbypass-m4X5DgOP#fs) section of this advisory. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
At the time of publication, this vulnerability also affected all open source Snort project releases earlier than Release 2.9.17. For more information about open source Snort project releases, see the [Snort website](https://www.snort.org/).
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-tfo-bypass-MmzZrtes.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect the following Cisco products:
    * Adaptive Security Appliance (ASA) Software
    * Catalyst 8500 Edge Platforms
    * Firepower Management Center (FMC) Software
    * Meraki vMX100 Virtual Appliances
    * Meraki Z1 Appliances
    * Meraki Z3 Series Appliances


## 
Workarounds 
  * While this workaround has been deployed and was proven successful in a test environment, customers should determine the applicability and effectiveness in their own environment and under their own use conditions. Customers should be aware that any workaround or mitigation that is implemented may negatively impact the functionality or performance of their network based on intrinsic customer deployment scenarios and limitations. Customers should not deploy any workarounds or mitigations before first evaluating the applicability to their own environment and any impact to such environment.
### Cisco FTD Software Release 6.7.0
For Cisco FTD Software Release 6.7.0, as a workaround when the Snort 3 configuration option is enabled, an administrator may enable built-in rule **129:2** in the intrusion policy and set the action to **Drop** instead of **Alert**.
Use the following steps to verify that the Snort 3 configuration option is enabled. For more details, see the [Switching Between Snort 2 and Snort 3](https://www.cisco.com/c/en/us/td/docs/security/firepower/670/fdm/fptd-fdm-config-guide-670/fptd-fdm-intrusion.html#id_120089) section of the _Cisco Firepower Threat Defense Configuration Guide for Firepower Device Manager, Version 6.7_.
    1. Log in to the Admin Portal for the FTD deployment.
    2. Navigate to **Policies** > **Intrusion**.
    3. Look for the **Snort Version** line above the table. The current version is the first number in the complete version number. For example, 2.9.17-95 is a Snort 2 version.
Use the following steps to enable rule**129:2**. For more details, see the [Changing Intrusion Rule Actions (Snort 3)](https://www.cisco.com/c/en/us/td/docs/security/firepower/670/fdm/fptd-fdm-config-guide-670/fptd-fdm-intrusion.html#Cisco_Task_in_List_GUI.dita_54aef253-02ab-4044-88ea-cea05249686d) section of the _Cisco Firepower Threat Defense Configuration Guide for Firepower Device Manager, Version 6.7_.
    1. Log in to the Admin Portal for the FTD deployment.
    2. Navigate to **Policies** > **Intrusion**.
    3. Choose any system-provided policy, such as **Balanced Security and Connectivity**.
    4. Search for rule **129:2**.
    5. Check the check box next to the rule to enable it.
    6. Choose **Drop** from the **Action** drop-down list.
    7. Add the intrusion policy to a rule in **Access control policy**.


## 
Fixed Software 
  * When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Fixed Releases
At the time of publication, the following fixed release information was available for the products that were affected by this vulnerability. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information. For more information about open source Snort project releases, see the [Snort website](https://www.snort.org/).
    * Cisco FTD releases 6.4.0.12, 6.6.3, and 6.7.0 and later contained the fix for this vulnerability when the Snort 2 option is configured.
    * Cisco FTD releases 6.7.0 and later were not vulnerable when the Snort 3 option is configured and rule 129:2 is enabled to drop traffic.
    * Cisco UTD Snort IPS Engine Software for IOS XE 16.12.5, 17.3.3, and 17.4.11 contained the fix for this vulnerability.
    * Cisco had not released software updates that address this vulnerability for Meraki MX Series Security Appliances.
    * The open source Snort project releases 2.9.17 and later contained the fix for this vulnerability.
    * The open source Snort project releases 3.0 and later were not vulnerable when rule 129:2 is enabled to drop traffic.  
  
1. Starting in 17.2.1, Cisco IOS XE and IOS XE SD-WAN use the same image file.


## 
Exploitation and Public Announcements 
  * The Cisco Product Security Incident Response Team (PSIRT) is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory.


## 
Source 
  * Cisco would like to thank Guillermo Muñoz Mozos of BBVA for reporting this vulnerability.


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
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort-tfo-bypass-MmzZrtes>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.2  | Updated fixed release information for FTD.  | Fixed Software  | Final  | 2021-MAY-20  |  
| 1.1  | Added FTD and Snort 3 information. Added Catalyst products. Added Cisco FTD Release 6.7.0 workaround.  | Summary, Vulnerable Products, Products Confirmed Not Vulnerable, Workarounds, and Fixed Releases  | Final  | 2021-MAR-30  |  
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
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort-tfo-bypass-MmzZrtes.html "Back to Top")
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
