  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72593.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72593.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72593.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72593.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72593.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Collaboration Endpoints](https://www.cisco.com/c/en/us/support/collaboration-endpoints/category.html)
  * [Cisco IP Phone 6800 Series with Multiplatform Firmware](https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/products-field-notices-list.html)


# Field Notice: FN - 72593 - Expiring Manufacturer Installed Certificate in Multiplatform Phones - Configuration Change Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/725/fn72593.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72593.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/725/fn72593.html)


Updated:August 31, 2023
Document ID:FN72593
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 24-Aug-23  | Initial Release  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| CP-6821-3PCC-K9=  |   |  
| CP-6841-3PCC-K9=  |   |  
| CP-6851-3PCC-K9=  |   |  
| CP-6861-3PW-K9  |   |  
| CP-6871-3PCC-K9=  |   |  
| CP-7811-3PCC-K9=  |   |  
| CP-7821-3PCC-K9=  |   |  
| CP-7832-3PCC-K9=  |   |  
| CP-7841-3PCC-K9=  |   |  
| CP-7861-3PCC-K9=  |   |  
| CP-8811-3PCC-K9=  |   |  
| CP-8831-3PCC-K9=  |   |  
| CP-8832-3PCC-K9=  |   |  
| CP-8841-3PCC-K9=  |   |  
| CP-8845-3PCC-K9=  |   |  
| CP-8851-3PCC-K9=  |   |  
| CP-8861-3PCC-K9=  |   |  
| CP-8865-3PCC-K9=  |   |  
| ATA191-3PW-K9  |   |  
| ATA192-3PW-K9  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCwf82386](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwf82386)  | Expiring SUDI/MIC in phones  |  
### Problem Description
Multiplatform phones (MPPs) will fail to provision or operate properly due to an expiring Manufacturer Installed Certificate (MIC).
### Background
The MIC issued by the Cisco Manufacturing Certificate Authority (CMCA) is used to provide a Secure Unique Device Identifier (SUDI) certificate in phones. A MIC is valid up to 10 years from the date of manufacture or on May 14, 2029, whichever comes first.
The products listed in the Products Affected section are base Product ID's (PIDs). PIDs related to the listed base PIDs are still affected.
### Problem Symptom
Once the MIC expires:
  * Secure provisioning might not work if the server challenges the phone to present the client certificate.
  * Any HTTPS communication will not work if it requires Mutual Transport Layer Security (TLS).
  * Phone media might not work.
  * Phone software upgrades might fail if the server validates the phone MIC before providing the firmware files.
  * 802.1x authentication will fail if the phone is authenticated via a MIC.


### Workaround/Solution
For MPP desk and conference phones, upgrade to the latest firmware and then turn on SUDI refresh. In firmware versions later than Version 12.0.3, the refresh is completed automatically.
For devices running firmware versions between Version 11.3.5 and Version 12.0.2, you have these options:
  * Option 1: In the phone configuration file (cfg.xml) with XML, enter a string in this format: 
`<MIC_Cert_Refresh_Enable ua="na">Yes</MIC_Cert_Refresh_Enable>`
  * Option 2: On the phone web page, navigate to `**Voice > Provisioning > MIC Cert Settings**`and choose`**Yes**`in order to enable the MIC certificate renewal.


Be sure to update your server trust store to include new Cisco manufacturing root certificates listed in field notice [FN72302](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72302.html).
**Notes:**
  * There is no workaround for 8831-3PCC. In order to have secure communications, plan on procuring a Cisco 8832 MPP.
  * The ATA-191 MPP and ATA-192 MPP do not have a SUDI refresh feature available yet. The earliest expiry of these devices’ certificates starts in 2027.


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72593.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Customers Also Viewed
  * [Set up Voicemail on a Cisco 6800, 7800, or 8800 Series IP Phone with Multiplatform Firmware](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5695-set-up-voicemail-on-a-cisco-ip-phone-8800-series-multiplatfo.html)
  * [Transfer Calls on a Cisco IP Phone 6800, 7800, or 8800 Series with Multiplatform Firmware](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-8800-series/smb5713-transfer-calls-on-a-cisco-ip-phone-8800-series-multiplatform.html)
  * [Access Voicemail on the Cisco 6800, 7800, or 8800 Series Multiplatform IP Phone](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-7800-series/smb5721-access-voicemail-on-the-cisco-ip-phone-7800-or-8800-series-m.html)
  * [How to Access the Web Configuration Page of a Cisco IP Phone 6800 Series with Multiplatform Firmware](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-6800-series/access-the-web-page-of-a-6800-series-ip-phone.html)
  * [Configure Speed Dial on a Cisco IP Phone with Multiplatform Firmware](https://www.cisco.com/c/en/us/support/docs/smb/collaboration-endpoints/cisco-ip-phone-6800-series/configure-speed-dial-on-a-cisco-ip-phone-6800-series-with-multiplatform-firmware.html)
  * + Show 2 More


### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72593.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/725/fn72593.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72593.html)
