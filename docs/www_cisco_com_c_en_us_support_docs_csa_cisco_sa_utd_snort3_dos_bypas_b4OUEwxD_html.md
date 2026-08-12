  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Unified Threat Defense Snort Intrusion Prevention System Engine for Cisco IOS XE Software Security Policy Bypass and Denial of Service Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.html) to Save Content 
Print
### Available Languages
Updated:September 25, 2024
Document ID:1727290217326213
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Unified Threat Defense Snort Intrusion Prevention System Engine for Cisco IOS XE Software Security Policy Bypass and Denial of Service Vulnerability
Medium
Advisory ID: 
cisco-sa-utd-snort3-dos-bypas-b4OUEwxD
First Published:
2024 September 25 16:00 GMT
Version 1.0: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCwj21273](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwj21273)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.html)
CVE-2024-20508
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.html)
CWE-122
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.html)
CVSS Score:
[ Base 5.8](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:L/A:N)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:L/A:N/E:X/RL:X/RC:X
CVE-2024-20508
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.html)
CWE-122
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD/csaf/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.json)
Email 
## 
Summary 
  * A vulnerability in Cisco Unified Threat Defense (UTD) Snort Intrusion Prevention System (IPS) Engine for Cisco IOS XE Software could allow an unauthenticated, remote attacker to bypass configured security policies or cause a denial of service (DoS) condition on an affected device.
This vulnerability is due to insufficient validation of HTTP requests when they are processed by Cisco UTD Snort IPS Engine. An attacker could exploit this vulnerability by sending a crafted HTTP request through an affected device. A successful exploit could allow the attacker to trigger a reload of the Snort process. If the action in case of Cisco UTD Snort IPS Engine failure is set to the default, _fail-open_ , successful exploitation of this vulnerability could allow the attacker to bypass configured security policies. If the action in case of Cisco UTD Snort IPS Engine failure is set to _fail-close_ , successful exploitation of this vulnerability could cause traffic that is configured to be inspected by Cisco UTD Snort IPS Engine to be dropped.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD>


## 
Affected Products 
  * ##  Vulnerable Products 
At the time of publication, this vulnerability affected the following Cisco products if they were running a vulnerable release of Cisco UTD Snort IPS Engine for Cisco IOS XE Software and had the Web Filtering feature, the Multi-Tenancy feature, or both enabled:
    * 1000 Series Integrated Services Routers (ISRs)
    * 4000 Series ISRs
    * Catalyst 8000V Edge Software
    * Catalyst 8200 Series Edge Platforms
    * Catalyst 8300 Series Edge Platforms
    * Catalyst 8500L Series Edge Platforms
    * Catalyst IR8300 Rugged Series Routers
For information about which Cisco software releases were vulnerable at the time of publication, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.html#fs) section of this advisory. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
### Determine the Device Configuration
For information about how to determine the device configuration, see the following sections.
**Determine Whether Cisco UTD Snort IPS Engine Is Enabled**
To determine whether Cisco UTD Snort IPS Engine is enabled on a device, use the **show utd engine standard status** command on the device CLI. If there is no output, Cisco UTD Snort IPS Engine is not enabled, and the device is not affected by this vulnerability. If the output shows **_Yes_** under **Running** , Cisco UTD Snort IPS Engine is enabled and the device is affected, as shown in the following example:
> 
```
Router#**show utd engine standard status**   
>   
> Profile              : Cloud-Low  
> System memory        :  
>              Usage  : 6.00 %  
>              Status : Green  
> Number of engines    : 1  
>   
>   
> Engine        **Running**    Health     Reason      
> =======================================================  
> Engine(#1):   _Yes_        Green      None  
> =======================================================  
> .  
> .  
> .
```

**Determine Whether Multi-Tenancy Is Enabled**
To determine whether Multi-Tenancy is enabled on Cisco UTD Snort IPS Engine, use the **show utd engine standard config | include Multi-tenancy** command on the device CLI. If there is no output, Multi-Tenancy is disabled, and the device is affected by this vulnerability only if Web Filtering is enabled. If the output shows _**Enabled**_ under **Multi-tenancy** , Multi-Tenancy is enabled, and the device is affected regardless of the Web Filtering configuration, as shown in the following example:
> 
```
Router#**show utd engine standard config | include Multi-tenancy**  
> **Multi-tenancy**: _Enabled_
```

**Determine Whether Web Filtering Is Enabled**
To determine whether Web Filtering is enabled on Cisco UTD Snort IPS Engine, use the **show utd engine standard config | include Web-Filter** command on the device CLI. If the output shows **_Disabled_** or there is no output, Web Filtering is disabled, and the device is affected by this vulnerability only if Multi-Tenancy is enabled. If the output shows **_Enabled_** under **Web-Filter** , Web Filtering is enabled, and the device is affected regardless of the Multi-Tenancy configuration, as shown in the following example:
> 
```
Router#**show utd engine standard config | include Web-Filter**  
> **Web-Filter**    : _Enabled  
> _
```

**Determine the Configured Fail Policy**
To determine the configured action in case of Cisco UTD Snort IPS Engine failure, use the **show platform software utd global | include Fail Policy** command on the device CLI. The following example shows the output of the **show platform software utd global | include Fail Policy** command on a device that has the action in case of Cisco UTD Snort IPS Engine failure set to **_Fail-open_** :
> 
```
Router# **show platform software utd global | include Fail Policy**  
> **Fail Policy**          : _Fail-open  
> _
```

##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect the following products:
    * Cisco Adaptive Security Appliance (ASA) Software
    * Cisco Catalyst 8500 Series Edge Platforms
    * Cisco Cloud Services Routers 1000V
    * Cisco Firepower Threat Defense (FTD) Software
    * Cisco Integrated Services Virtual Routers (ISRv)
    * Cisco Secure Firewall Management Center (FMC) Software, formerly Firepower Management Center Software
    * Open Source Snort


## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Fixed Releases
At the time of publication, the release information in the following table was accurate. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
The left column lists Cisco software releases, and the right column indicates whether a release was affected by the vulnerability that is described in this advisory and which release included the fix for this vulnerability.  
| Cisco UTD Snort IPS Engine Release  | First Fixed Release  |  
| --- | --- |  
| Earlier than 17.12  | Not vulnerable.  |  
| 17.12  | 17.12.4  |  
| 17.13  | Migrate to a fixed release.  |  
| 17.14  | Not vulnerable.  |  
The Cisco Product Security Incident Response Team (PSIRT) validates only the affected and fixed release information that is documented in this advisory.


## 
Exploitation and Public Announcements 
  * The Cisco PSIRT is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory.


## 
Source 
  * This vulnerability was found during the resolution of a Cisco TAC support case.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Related to This Advisory 
## 
URL 
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2024-SEP-25  |  
Show Less


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
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Related to This Advisory 
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.html "Back to Top")
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
