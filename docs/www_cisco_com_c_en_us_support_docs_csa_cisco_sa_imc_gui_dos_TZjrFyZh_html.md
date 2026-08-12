  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-imc-gui-dos-TZjrFyZh.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-imc-gui-dos-TZjrFyZh.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-imc-gui-dos-TZjrFyZh.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-imc-gui-dos-TZjrFyZh.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Integrated Management Controller GUI Denial of Service Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-imc-gui-dos-TZjrFyZh.html) to Save Content 
Print
### Available Languages
Updated:October 20, 2021
Document ID:1634748505271208
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Integrated Management Controller GUI Denial of Service Vulnerability
Medium
Advisory ID: 
cisco-sa-imc-gui-dos-TZjrFyZh
First Published:
2021 October 20 16:00 GMT
Version 1.0: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCvy91321](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvy91321)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-imc-gui-dos-TZjrFyZh.html)
CVE-2021-34736
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-imc-gui-dos-TZjrFyZh.html)
CWE-20
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-imc-gui-dos-TZjrFyZh.html)
CVSS Score:
[ Base 5.3](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L/E:X/RL:X/RC:X
CVE-2021-34736
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-imc-gui-dos-TZjrFyZh.html)
CWE-20
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-imc-gui-dos-TZjrFyZh.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-imc-gui-dos-TZjrFyZh/csaf/cisco-sa-imc-gui-dos-TZjrFyZh.json)
Email 
## 
Summary 
  * A vulnerability in the web-based management interface of Cisco Integrated Management Controller (IMC) Software could allow an unauthenticated, remote attacker to cause the web-based management interface to unexpectedly restart.
The vulnerability is due to insufficient input validation on the web-based management interface. An attacker could exploit this vulnerability by sending a crafted HTTP request to an affected device. A successful exploit could allow the attacker to cause the interface to restart, resulting in a denial of service (DoS) condition.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability.
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-imc-gui-dos-TZjrFyZh>


## 
Affected Products 
  * ##  Vulnerable Products 
At the time of publication, this vulnerability affected the following Cisco products:   

    * UCS C-Series Rack Servers in standalone mode  

    * UCS S-Series Storage Servers in standalone mode  

For information about which Cisco software releases were vulnerable at the time of publication, see the [Fixed Software](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-imc-gui-dos-TZjrFyZh.html#fs) section of this advisory. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-imc-gui-dos-TZjrFyZh.html#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect the following Cisco products:
    * 5000 Series Enterprise Network Compute System (ENCS)
    * UCS B-Series Blade Servers
    * UCS E-Series Servers
    * UCS Manager Software


## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
### Fixed Releases
At the time of publication, the release information in the following table(s) was accurate. See the Details section in the bug ID(s) at the top of this advisory for the most complete and current information.
The left column lists Cisco software releases, and the right column indicates whether a release was affected by the vulnerability described in this advisory and which release included the fix for this vulnerability.  
| UCS C-Series Rack Servers  | First Fixed Release  |  
| --- | --- |  
| 4.1 and earlier  | 4.1(2g)  |  
| 4.2  | 4.2(1b)  |  
| UCS S-Series Storage Servers  | First Fixed Release  |  
| --- | --- |  
| 4.1 and earlier  | 4.1(3e)1  |  
1. At the time of publication, Cisco expected to fix this vulnerability in Cisco UCS S-Series Storage Servers Release 4.1(3e), scheduled for a few weeks after the publication of this advisory.
The Cisco Product Security Incident Response Team (PSIRT) validates only the affected and fixed release information that is documented in this advisory.


## 
Exploitation and Public Announcements 
  * The Cisco PSIRT is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory.


## 
Source 
  * This vulnerability was found during internal security testing.


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
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-imc-gui-dos-TZjrFyZh>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2021-OCT-20  |  
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
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Related to This Advisory 
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-imc-gui-dos-TZjrFyZh.html "Back to Top")
