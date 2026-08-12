  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70548.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70548.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70548.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70548.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70548.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Enterprise Chat and Email](https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-field-notices-list.html)


# Field Notice: FN - 70548 - Unified Contact Center Enterprise (UCCE) / Enterprise Chat and Email (ECE) - Microsoft Secure LDAP Mandatory for Active Directory Connections - Workaround Provided
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/705/fn70548.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70548.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/705/fn70548.html)


Updated:April 16, 2020
Document ID:FN70548
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 16-Apr-20  | Initial Release  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | Enterprise Chat and Email  | 12  | 12.0(1), 12.0(1)_ES1, 12.0(1)_ES2, 12.0(1)_ES3, 12.5(1), 12.5(1)_ET1  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvt32156](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvt32156)  | ECE gadget is not loading in PCCE SPOG after enabling LDAP signing on Domain controller  |  
### Problem Description
**What is Changing**
Microsoft is currently updating security requirements for Lightweight Directory Access Protocol (LDAP) connections to Active Directory. After this update completes, Secure LDAP (LDAPS) will become mandatory for all LDAP connections to Active Directory from the specified Cisco Collaboration applications. After the update, LDAP connections to Active Directory from these applications will not work unless LDAPS is configured.
This security update is not expected to become mandatory until the second half of the calendar year 2020. However, it is recommended that you update the specified Cisco Collaboration applications to use LDAPS as soon as possible. This will both secure your LDAP connection and will also ensure that services remain up and running when the security update becomes mandatory.
**Why this Change is Needed**
The current default settings have a vulnerability that might expose Active Directory domain controllers to an elevation of privileges, and man-in-the-middle attacks. The LDAPS updates harden the connection to Active Directory's existing LDAP channel binding and LDAP signing mechanisms, which makes the system more secure. For more detailed information, see [Microsoft Security Advisory ADV190023](https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/ADV190023).
For additional configurations around LDAP signing, see [How to enable LDAP signing in Windows Server](https://support.microsoft.com/en-us/help/935834).
  * Non-impacted UCCE LDAP dependent components 
    * Domain Manager
    * Installation and setup
    * Configuration Manager
    * Finesse database (DB) connection
    * Websetup
    * Cisco Unified Intelligence Center (CUIC)
  * Impacted Unified Contact Center Enterprise (Unified CCE) LDAP dependent components 
    * Enterprise Chat and Email (ECE) DB connection


### Background
**CVE-2017-8563 | Windows Elevation of Privilege Vulnerability**
An elevation of privilege vulnerability exists in Microsoft Windows when a man-in-the-middle attacker is able to successfully forward an authentication request to a Windows LDAP server such as a system running Active Directory Domain Services (AD DS).
The LDAP authentication mechanism is used in Unified CCE solution components, hence might have impact due to this change. This wiki captures the impact to the Unified CCE components, recommendations, and validation information.
Reference links from Microsoft:
  * [CVE-2017-8563 | Windows Elevation of Privilege Vulnerability](https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2017-8563)
  * [ADV190023 | Microsoft Guidance for Enabling LDAP Channel Binding and LDAP Signing](https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/ADV190023)
  * [2020 LDAP channel binding and LDAP signing requirements for Windows](https://support.microsoft.com/en-us/help/4520412/2020-ldap-channel-binding-and-ldap-signing-requirement-for-windows)
  * [CVE-2017-8563 | Windows Elevation of Privilege Vulnerability](https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2017-8563)


### Problem Symptom
For ECE, see Cisco bug ID CSCvt32156.
### Workaround/Solution
For core Unified Contact Center Enterprise, there are no changes required.  
For ECE, you must enable SSL. Please refer to the Enterprise Chat and Email (ECE) Installation and Configuration guide under the chapter, "SSL Configuration" for instructions on enabling SSL. 
Please also refer to the Workaround in defect CSCvt32156 on how to specify the keystore file path for installing SSL certificates for ECE.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70548.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70548.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Enterprise Chat and Email](https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/series.html)
  * [Unified Communications Manager (CallManager)](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/series.html)
  * [Unified Communications Manager Version 12.5](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-12-5/model.html)
  * [Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/705/fn70548.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70548.html)
