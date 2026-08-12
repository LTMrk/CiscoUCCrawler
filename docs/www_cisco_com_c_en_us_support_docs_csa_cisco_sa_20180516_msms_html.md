  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180516-msms.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180516-msms.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180516-msms.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180516-msms.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# Cisco Meeting Server Media Services Denial of Service Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-20180516-msms.html) to Save Content 
Print
### Available Languages
Updated:May 16, 2018
Document ID:1526489004879476
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg)](https://sec.cloudapps.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory 
# Cisco Meeting Server Media Services Denial of Service Vulnerability
High
Advisory ID: 
cisco-sa-20180516-msms
First Published:
2018 May 16 16:00 GMT
Version 1.0: 
[Final](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
No workarounds available
Cisco Bug IDs:
[CSCve79693](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCve79693)
[CSCvf91393](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvf91393)
[CSCvg64656](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvg64656)
[ More... ](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180516-msms.html)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180516-msms.html) ,[CSCve79693](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCve79693),[CSCvf91393](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvf91393),[CSCvg64656](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvg64656),[CSCvh30725](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvh30725),[CSCvi86363](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvi86363)
CVE-2018-0280
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180516-msms.html)
CVSS Score:
[ Base 7.5](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.0&vector=CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H)[![](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png)](https://sec.cloudapps.cisco.com/security/center/images/blue-square.png "Related image, diagram or screenshot.")**Click Icon to Copy Verbose Score**   
CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H/E:X/RL:X/RC:X
CVE-2018-0280
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180516-msms.html)
[ Download CSAF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180516-msms/csaf/cisco-sa-20180516-msms.json)
[ Download CVRF ](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180516-msms/cvrf/cisco-sa-20180516-msms_cvrf.xml)
Email 
## 
Summary 
  * A vulnerability in the Real-Time Transport Protocol (RTP) bitstream processing of the Cisco Meeting Server could allow an unauthenticated, remote attacker to cause a denial of service (DoS) condition.  
  
The vulnerability is due to insufficient input validation of incoming RTP bitstreams. An attacker could exploit this vulnerability by sending a crafted RTP bitstream to an affected Cisco Meeting Server. A successful exploit could allow the attacker to deny audio and video services by causing media process crashes resulting in a DoS condition on the affected product.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability. 
This advisory is available at the following link:  
<https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180516-msms>


## 
Affected Products 
  * ##  Vulnerable Products 
This vulnerability affects Cisco Meeting Server deployments that are running Cisco Meeting Server Software Releases 2.0, 2.1, 2.2, and 2.3.
Administrators can determine which Cisco Meeting Server Software release is running on a device by using the **version** command in the CLI. The following example shows the output of the command for a device that is running Cisco Meeting Server Software Release 2.2.11:
> 
```
    system> **version**
    2_2_11 
```

##  Products Confirmed Not Vulnerable 
Only products listed in the [Vulnerable Products](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180516-msms.html#vp) section of this advisory are known to be affected by this vulnerability.


## 
Details 
  * Cisco Meeting Server incorporates video, audio, and content-sharing capabilities into software that can be accessed via a conference room, desktop, or mobile device. Cisco Meeting Server works across Cisco video rooms and connects with Skype for Business and other hardware providers to allow a seamless meeting architecture. This capability exists via collaboration between Cisco and Acano, which was acquired by Cisco in 2016.  



## 
Workarounds 
  * There are no workarounds that address this vulnerability.


## 
Fixed Software 
  * Cisco has released free software updates that address the vulnerability described in this advisory. Customers may only install and expect support for software versions and feature sets for which they have purchased a license. By installing, downloading, accessing, or otherwise using such software upgrades, customers agree to follow the terms of the Cisco software license:   
<https://www.cisco.com/c/en/us/products/end-user-license-agreement.html>
Additionally, customers may only download software for which they have a valid license, procured from Cisco directly, or through a Cisco authorized reseller or partner. In most cases this will be a maintenance upgrade to software that was previously purchased. Free security software updates do not entitle customers to a new software license, additional software feature sets, or major revision upgrades.
When considering software upgrades, customers are advised to regularly consult the advisories for Cisco products, which are available from the [Cisco Security Advisories and Alerts page](https://www.cisco.com/go/psirt), to determine exposure and a complete upgrade solution.
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.
**Customers Without Service Contracts**
Customers who purchase directly from Cisco but do not hold a Cisco service contract and customers who make purchases through third-party vendors but are unsuccessful in obtaining fixed software through their point of sale should obtain upgrades by contacting the Cisco TAC:  
<https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html>
Customers should have the product serial number available and be prepared to provide the URL of this advisory as evidence of entitlement to a free upgrade.
**Fixed Releases**
The following Cisco Meeting Server Software releases address this vulnerability:  
| **Cisco Meeting Server**  | **First Fixed Release for This Vulnerability**  |  
| --- | --- |  
| 2.0  | Affected; migrate to 2.2.10  
 |  
| 2.1  
 | 2.1.12 (see note)  
 |  
| 2.2  | 2.2.10  |  
| 2.3  | 2.3.1  |  
**Note:** Cisco Meeting Server Software Release 2.1 has reached the end of support and can be used only for upgrade chain purposes. For more information, refer to the “End Of Software Maintenance” section in [Cisco Meeting Server Release 2.3.0 Release Notes](https://www.cisco.com/c/dam/en/us/td/docs/conferencing/ciscoMeetingServer/Release_Notes/Version-2-3/Cisco-Meeting-Server-Release-Notes-2-3-0.pdf).
For information about the Cisco Meeting Server Software release model, refer to [Cisco Meeting Server: End of maintenance and support policy](https://www.cisco.com/c/dam/en/us/td/docs/conferencing/ciscoMeetingServer/White_papers/Cisco-Meeting-Server-End-of-Maintenance-and-support-of-sofware.pdf).


## 
Exploitation and Public Announcements 
  * The Cisco Product Security Incident Response Team (PSIRT) is not aware of any public announcements or malicious use of the vulnerability that is described in this advisory. 


## 
Source 
  * This vulnerability was found during resolution of a Cisco TAC support case.


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
  * <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180516-msms>


## 
Revision History 
  * | Version  | Description  | Section  | Status  | Date  |  
| --- | --- | --- | --- | --- |  
| 1.0  | Initial public release.  | —  | Final  | 2018-May-16  |  
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
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20180516-msms.html "Back to Top")
