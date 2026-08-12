  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/706/fn70613.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/706/fn70613.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/706/fn70613.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/706/fn70613.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/706/fn70613.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Unified Communications Manager (CallManager)](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-field-notices-list.html)


# Field Notice: FN - 70613 - Cisco Unified Communications Manager Secure Endpoints Might Fail to Register After a Refresh Upgrade to Version 12.5 - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/706/fn70613.html) to Save Content 
Print
### Available Languages
Updated:October 1, 2020
Document ID:FN70613
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 01-Oct-20  | Initial Release  |  
| 2.0  | 01-Oct-20  | Updated workaround section to include table  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | Unified Communications Manager Updates  | UCM  | 12.0(1)SU1, 12.0(1)SU2, 12.0(1)SU3, 12.5(1), 12.5(1)SU1, 12.5(1)SU2  |   |  
| NON-IOS  | Unified Communications Manager / Cisco Unity Connection Updates  | UCM  | 11.5(1), 11.5(1)SU1, 11.5(1)SU2, 11.5(1)SU3, 11.5(1)SU3a, 11.5(1)SU3b, 11.5(1)SU4, 11.5(1)SU5, 11.5(1)SU6, 11.5(1)SU7, 11.5(1)SU8, 12.0(1), 12.0(2)  |   |  
| NON-IOS  | Unified Communications Manager / Cisco Unity Connection Updates  | UCM v11  | 11.0, 11.0(1), 11.0(1a), 11.0(1a)SU1, 11.0(1a)SU2, 11.0(1a)SU3, 11.0(1a)SU3a, 11.0(1a)SU4  |   |  
| NON-IOS  | Unified Communications Manager / Cisco Unity Connection Updates  | UCM v10  | 10.0(1), 10.0(1)SU1, 10.0(1)SU2, 10.5(1), 10.5(1)SU1, 10.5(1)SU1a, 10.5(2), 10.5(2)SU1, 10.5(2)SU10, 10.5(2)SU2, 10.5(2)SU2a, 10.5(2)SU3, 10.5(2)SU3a, 10.5(2)SU4, 10.5(2)SU4a, 10.5(2)SU5, 10.5(2)SU6, 10.5(2)SU6a, 10.5(2)SU7, 10.5(2)SU8, 10.5(2)SU9  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvv13565](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvv13565)  | Secure endpoints may fail to register after a refresh upgrade to CUCM 12.5  |  
### Problem Description
Endpoints in secure mode might fail to register after a refresh upgrade to Cisco Unified Communications Manager (Unified CM) Version 12.5(1) (running in mixed mode) due to a mismatch in the signer of the Identity Trust List (ITL) and Certificate Trust List (CTL) files on the Unified CM server and on the endpoints. This applies to all customers who have already performed a refresh upgrade from or who plan to upgrade to Unified CM Version 12.5(1).
**Note:** Clusters that run in non-secure mode or use USB eTokens are not affected by this issue and no further action is needed. Though endpoints other than IP phones are not affected, it is strongly recommended to apply the workaround before an upgrade to Version 12.5(1)SU3.
### Background
The CTL file has two root anchors for trust verification: the ITLRecovery certificate and the CallManager certificate. Additionally, an update to the CTL file when certificates are regenerated can only be completed manually by an administrator. Since the ITLRecovery certificate is incorrectly regenerated during the refresh upgrade, when the server is switched to the new Unified CM version the CTL file will only have the CallManager certificate as a valid root anchor until it is updated with the new ITLRecovery certificate.
**Note:** If the CallManager certificate is also regenerated before the CTL file is updated with the new ITLRecovery certificate, the CTL file will no longer have any valid root anchors for trust verification. It will need to be manually deleted from the endpoint before a new CTL file will be accepted.
### Problem Symptom
Endpoints in secure mode might not be able to register to Unified CM Version 12.5(1) that runs in mixed mode after a refresh upgrade.
Another symptom is that endpoints display authentication errors when trying to connect to secure URLs, such as Corporate Directory or Phone Services. These errors are a sign that there is a problem with the ITL file on the endpoint.
### Workaround/Solution
**Workaround:**
Customers who have upgraded from CUCM 11.X or 12.0.X to any CUCM 12.5 version prior to 12.5(1)SU3 should take the steps below to ensure that the CTLFile has the correct ITLRecovery certificate:
**CAUTION** : If you have upgraded from an earlier CUCM version to any CUCM 12.5(1) version prior to 12.5(1)SU3, do not regenerate the CallManager certificate until you have performed the workaround steps listed below.
**NOTE** : If a mixed-mode cluster has previously been upgraded from a pre-12.5 CUCM release to any 12.5(1) version lower than 12.5(1)SU3, upgrading to 12.5(1)SU3 will not correct this issue. The workaround must still be performed to ensure that the CTLFile has the correct ITLRecovery certificate
1. Update the ITLRecovery certificate in the CTLFile by running the following command from the admin cli on the Publisher (NOTE: After running this command, the CTLFile will be signed by the CallManager certificate instead of the ITLRecovery certificate):
  
utils ctl reset localkey[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/706/fn70613img1.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/706/fn70613img1.jpg "Related image, diagram or screenshot.")
2. After the command completes, restart the Cisco CallManager and Cisco CTIManager services on all nodes. Once the services are back up, restart the endpoints to ensure that they get the new CTLFile.
3. Verify on an endpoint that the new CTLFile has been installed, by comparing the serial number on the endpoint (under Admin Settings – Security Setup – CTL) with the serial number returned from the “show ctl” CLI command on the TFTP server.
4. Update the CTLFile so that it will be signed by the new ITLRecovery certificate instead of the CallManager certificate (this is recommended as the ITLRecovery certificate has a 20 year expiration) by running the following command on the Publisher:
utils ctl update CTLFile
5. After the command completes, restart the Cisco CallManager and Cisco CTIManager services on all nodes. Once the services are back up, restart the endpoints to ensure that they get the new CTLFile.
6. Verify on an endpoint that the new CTLFile has been installed, by comparing the serial number on the endpoint (under Admin Settings – Security Setup – CTL) with the serial number returned from the “show ctl” CLI command on the TFTP server.
For more information about CTL files, see “[Security Guide for Cisco Unified Communications Manager, Release 12.5(1)](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/12_5_1/cucm_b_security-guide-1251/cucm_b_security-guide-1251_chapter_0100.html)”
**Solution** :
CSCvv13565 is resolved in CUCM 12.5(1)SU3 (12.5.1.13900-152). The fix ensures that the ITLRecovery certificate is not regenerated during the refresh upgrade from versions prior to CUCM 12.5(x). Customers using CUCM clusters in mixed-mode and who wish to upgrade to CUCM 12.5 from CUCM 12.0 or earlier should upgrade directly to CUCM 12.5(1)SU3 or higher to avoid hitting this issue.
**Table 1: Recommended Migration Path**
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/706/FN70613-table-image1601578295980.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/706/FN70613-table-image1601578295980.png "Related image, diagram or screenshot.")
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/706/fn70613.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/706/fn70613.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Communications Manager Version 12.5](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-12-5/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/706/fn70613.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/706/fn70613.html)
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
