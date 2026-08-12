  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63454.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63454.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63454.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63454.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63454.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-field-notices-list.html)


# Field Notice: FN - 63454 - Agent desktops upgraded to Cisco Agent Desktop 8.5(2) are unable to launch - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/634/fn63454.html) to Save Content 
Print
### Available Languages
Updated:January 22, 2021
Document ID:FN63454
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 06-Sep-11  | Initial Release  |  
| 10.0  | 13-Oct-17  | Migration to new field notice system  |  
| 10.1  | 22-Jan-21  | Corrected Formatting Issues  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | Cisco Agent Desktop Software Releases  |   | 8.5(4),8.5(2)a  |   |  
| NON-IOS  | Unified Contact Center Enterprise Virtual Machine Templates  | 8  | 8.5  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCts33268](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCts33268)  | Agent unable to start due to phonedev.dll dependency issue  |  
| [CSCts26142](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCts26142)  | CAD 8.5(2) failed to start application not initialised properly  |  
| [CSCts26131](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCts26131)  | CAD agent.exe does not launch after upgrade to 8.5(2) MR2  |  
### Problem Description
Agent desktops upgraded to Cisco Agent Desktop 8.5(2) are unable to launch. An error message appears and the application is terminated.
### Background
During the course of installing the maintenance release to the CAD Services (typically on a Peripheral Gateway), the update creates an install package (Cisco Desktop Services 8.5(2) Maintenance Release 2.msi) for distribution to the agent, supervisor, and administrator client applications. When executed on Cisco Agent Desktop 8.5(1) client desktops, the installer replaces a subset of the application's file set. One of the replacement files, "phonedev.dll" is corrupt and prevents the Cisco Agent Desktop client from launching. To correct the problem, the Maintenance Release must be reissued with a new phonedev.dll.
### Problem Symptom
Upon launching Cisco Agent Desktop, the user sees the error message "Application failed to initialize properly (0xc0150002). Click on OK to terminate the application."
The correct build version for the phonedev.dll is 8.5.2.18
The specific version that is bad is 8.5.2.17
### Workaround/Solution
The CAD 8.5(2) Maintenance Release will be reissued as CAD 8.5(2a).
CAD 8.52(a) is available for download on Cisco.com at [http://www.cisco.com/cisco/software/release.html?mdfid=273556285&flowid=5220&softwareid=280840589&release=8.5%282%29a&relind=AVAILABLE&rellifecycle=&reltype=latest](http://www.cisco.com/cisco/software/release.html?mdfid=273556285&flowid=5220&softwareid=280840589&release=8.5%282%29a&relind=AVAILABLE&rellifecycle=&reltype=latest).
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63454.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63454.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/634/fn63454.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/634/fn63454.html)
