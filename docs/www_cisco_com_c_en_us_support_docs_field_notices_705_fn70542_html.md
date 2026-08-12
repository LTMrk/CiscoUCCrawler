  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70542.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70542.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70542.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70542.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70542.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-field-notices-list.html)


# Field Notice: FN70542 - Unified Contact Center Enterprise - Tomcat Upgrade to Resolve CVE-2020-1938 Breaks Cceadmin and Websetup Page - Software Upgrade Recommended
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/705/fn70542.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70542.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/705/fn70542.html)


Updated:December 19, 2024
Document ID:FN70542
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Medium
**Impact Rating:**
Medium
**First Published:**
2020-May-07
**Last Published:**
2024-Dec-19
**Revision:**
1.2
**Cisco Bug IDs:**
  * [CSCvt31436](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvt31436)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| Unified Contact Center Enterprise Virtual Machine Templates  | 10  | 10.5  |   |  
| Unified Contact Center Enterprise Virtual Machine Templates  | 11  | 11.0, 11.6  |   |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCvt31436](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvt31436)  | CCE - Upgrading tomcat to version 7.0.100 or greater breaks cceadmin and websetup  |  
  

### Problem Description
  

An upgrade to Apache Tomcat on Unified Contact Center Enterprise (Unified CCE) components breaks the cceadmin and websetup page. This error message is given:
`HTTP Error 500.0 - Internal Server Error Calling LoadLibraryEx on ISAPI filter "C:\icm\tomcat\bin\i386\isapi_redirect.dll" failed`
This is a mandatory upgrade to address the vulnerability described in [CVE-2020-1938](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-1938). It might not be an option to revert back to an older Tomcat version.
  

### Background
  

Tomcat version 7.0.100 or greater.
This error is given:
`HTTP Error 500.0 - Internal Server Error Calling LoadLibraryEx on ISAPI filter "C:\icm\tomcat\bin\i386\isapi_redirect.dll" failed`
  

### Problem Symptom
  

The cceadmin and websetup page does not load after an upgrade to Tomcat 7.0.99 and later on Unified CCE 11.6.
  

### Workaround/Solution
  

**Workaround 1. Provide Permissions**
The permissions message states:

```
C:\icm\tomcat folder does not have enough permissions.
```

In order to provide enough permissions in the Tomcat directory and subdirectories, complete these steps:
  1. In Tomcat, inherit the security permissions: 
    1. Right-click the **Tomcat** folder.
    2. Choose **Security > Advanced**.
    3. Click **Enable Inheritance**.
    4. Click **Apply**.
  2. Stop Tomcat and modify these files: 
     * 
```
<install_drive>:\icm\tomcat\conf\server.xml
```

     * 
```
<install_drive>:\icm\ssl\cfg\server-iis.xml
```

     * 
```
<install_drive>:\icm\bin\server.xml.IIS.custom
```

In each file, replace this line:
`<Connector port="8009" protocol="AJP/1.3" redirectPort="8443" address="127.0.0.1" maxPostSize="5242880" />`
with this line:
`<Connector port="8009" protocol="AJP/1.3" redirectPort="8443" address="127.0.0.1" maxPostSize="5242880" secretRequired="false" allowedRequestAttributesPattern=".*" />`


**Workaround 2. Security Patch**
Roll back the Tomcat security patch.
**Workaround 3. Apply Patch**
Available patches:
  * [12.0(1)ES52](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/ucce_b_unified-contact-center-enterprise-engineering/ucce_b_unified-contact-center-enterprise-engineering_chapter_0101.html)
  * [12.5(1)ES20](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/ucce_b_unified-contact-center-enterprise-engineering/ucce_b_unified-contact-center-enterprise-engineering_chapter_0110.html)

  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.2  | Removed link and reference to 11.6(2)ES54 because this ES is no longer available and 11.6 is end of support.  | Workaround/Solution  | 2024-DEC-19  |  
| 1.1  | Updated the Workaround/Solution section.  | Workaround/Solution  | 2021-AUG-17  |  
| 1.0  | Initial Release  | —  | 2020-MAY-07  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70542.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70542.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/705/fn70542.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/705/fn70542.html)
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
