  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72318.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72318.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72318.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72318.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72318.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Unified Communications Manager (CallManager)](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-field-notices-list.html)


# Field Notice: FN - 72318 - Cisco Unified Communications Manager / Session Management Edition: QuoVadis Root CA 2 Decommission Might Affect Smart Licensing and Smart Call Home Functionality - Workaround Provided
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/723/fn72318.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72318.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/723/fn72318.html)


Updated:August 12, 2022
Document ID:FN72318
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 3.0  | 12-Aug-22  | Updated the Workaround/Solution section  |  
| 2.0  | 24-Feb-22  | Updated the Problem Description, Background, Problem Symptom, and Workaround/Solution Sections  |  
| 1.0  | 07-Jan-22  | Initial Release  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | Unified Communications Manager Updates  | 14  | 14  |   |  
| NON-IOS  | Unified Communications Manager Updates  | UCM  | 12.0(1)SU1, 12.0(1)SU2, 12.0(1)SU3, 12.0(1)SU4, 12.0(1)SU5, 12.5(1), 12.5(1)SU1, 12.5(1)SU2, 12.5(1)SU3, 12.5(1)SU4  |   |  
| NON-IOS  | Unified Communications Manager / Cisco Unity Connection Updates  | UCM  | 11.5(1), 11.5(1)SU1, 11.5(1)SU10, 11.5(1)SU2, 11.5(1)SU3, 11.5(1)SU3a, 11.5(1)SU3b, 11.5(1)SU4, 11.5(1)SU5, 11.5(1)SU6, 11.5(1)SU7, 11.5(1)SU8, 11.5(1)SU9, 11.5(2), 12.0(1), 12.0(2), 12.5(1)  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvx00530](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvx00530)  | QuoVadis root CA decommission on Unified Communications Manager  |  
### Problem Description
For affected versions of the Cisco Unified Communications Manager (CUCM) and Session Management Edition (SME) software, some Secure Sockets Layer (SSL) certificates issued from the QuoVadis root certificate authority (CA) trust chain before March 31, 2021, cannot be renewed from this CA. Once those certificates expire on devices or are removed from the Cisco cloud servers, functions such as Smart Licensing and Smart Call Home will fail to establish secure connections to Cisco and might not operate properly.
### Background
The QuoVadis Root CA 2 Public Key Infrastructure (PKI) used by CUCM and SME software to issue SSL certificates is subject to an industry-wide issue that affects revocation abilities. Due to this issue, no new QuoVadis Root CA 2 certificates will be issued or renewed by Cisco after March 31, 2021. This affects certificate renewals on devices, Cisco cloud servers, and third-party services.
Certificates issued before the QuoVadis Root CA 2 was decommissioned will continue to be valid. However, the certificates will not renew when they expire on either the device or the Cisco cloud server. This will cause functions such as Smart Licensing and Smart Call Home to fail to establish secure connections to Cisco cloud servers.
This table shows a summary of the QuoVadis Root CA 2 certificate expiration dates for affected Cisco services.  
| Cisco Cloud Server  | QuoVadis Certificate Expiration Date  | Affected Services  |  
| --- | --- | --- |  
| tools.cisco.com  | February 5, 2022  | 
  * Smart Licensing
  * Smart Call Home

 |  
### Problem Symptom
Expiration of the QuoVadis Root CA 2 certificates affects these services with the associated symptoms.  
| Affected Services  | Symptoms for Affected Services  |  
| --- | --- |  
| Smart Licensing  | Failure to connect to the server (Details are provided in this section)  |  
| Smart Call Home  | Failure to connect to the server and the Call-Home HTTP request fails  |  
For CUCM and SME, affected versions will be unable to connect to the Smart Licensing and Smart Call Home services hosted by Cisco. Smart licenses might fail entitlement and reflect an Out of Compliance status.
For CUCM, choose **System > Licensing > License Management** in the administrator web interface to view the licensing status.
The features that use Smart Licensing will continue to function for 90 days after the last successful secure connection. Some Smart Licensing symptoms are:
  * The CUCM server will indicate the last attempt to renew license authorization has failed to communicate with the Smart Licensing server. 
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72318img1.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72318img1.jpg "Related image, diagram or screenshot.")
  * The CUCM server will show the "Authorization Expired" state if there is no communication with the Smart Licensing server within 90 days. 
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72318img2.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72318img2.jpg "Related image, diagram or screenshot.")
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72318img3.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72318img3.jpg "Related image, diagram or screenshot.")
  * The CUCM server will then show the "Out of Compliance" state if there is no communication with the Smart Licensing server and administrators will be unable to provision users or devices until the certification is renewed with IdenTrust. 
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72318img4.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72318img4.jpg "Related image, diagram or screenshot.")
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72318img5.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/723/fn72318img5.jpg "Related image, diagram or screenshot.")


**Note:** Offline licensing, such as Permanent License Reservation (PLR) and Specific License Reservation (SLR), is not affected by the certificate change on the Smart Licensing server.
For additional information, refer to the [Cisco Smart Licensing Guide](https://www.cisco.com/c/en/us/buy/licensing/licensing-guide.html) and the CUCM Licensing Guide for your specific version of CUCM or SME software.
### Workaround/Solution
Cisco has migrated from the QuoVadis Root CA 2 to the IdenTrust Commercial Root CA 1 for SSL certificates. Cisco recommends these two options to add the new IdenTrust Commercial Root CA 1 certificate to the CUCM.
  * Software Upgrade
  * Manual Certificate Update


**Software Upgrade (Smart Licensing only)**
For CUCM, upgrade to one of the CUCM software versions shown in the table in order to resolve the root CA certificate issue for affected platforms.  
| Release Version  | Fixed Version  |  
| --- | --- |  
|  CUCM 11.5(1), 11.5(1)SU1, 11.5(1)SU10, 11.5(1)SU2, 11.5(1)SU3, 11.5(1)SU3a, 11.5(1)SU3b, 11.5(1)SU4, 11.5(1)SU5, 11.5(1)SU6, 11.5(1)SU7, 11.5(1)SU8, 11.5(1)SU9, 11.5(2), 12.0(1) 12.0(1)SU1, 12.0(1)SU2, 12.0(1)SU3, 12.0(1)SU4, 12.0(1)SU5 CUCM 12.5(1), 12.5(1)SU1, 12.5(1)SU2, 12.5(1)SU3, 12.5(1)SU4  |  CUCM 12.5.1 SU5 or later CUCM 14 SU1 or later  |  
|  CUCM 14.0  |  CUCM 14 SU1 or later  |  
If you run CUCM version 12.5.1 SU5 or CUCM 14 SU1 or later, no action is needed as the new certificate is provided natively.
**Manual Certificate Update (Smart Call Home)**
  1. Copy and paste this IdenTrust Commercial Root CA 1 certificate into a file on your computer.
**Note:** Ensure that the administrator copies the entire string which includes -----BEGIN CERTIFICATE----- and -----END CERTIFICATE-----, pastes it into a text file, and saves it with the extension .PEM.
The updated IdenTrust Commercial Root CA 1 certificate is shown here and complies with sha1WithRSAEncryption signature algorithm requirements.

```
-----BEGIN CERTIFICATE-----
MIIFYDCCA0igAwIBAgIQCgFCgAAAAUUjyES1AAAAAjANBgkqhkiG9w0BAQsFADBK
MQswCQYDVQQGEwJVUzESMBAGA1UEChMJSWRlblRydXN0MScwJQYDVQQDEx5JZGVu
VHJ1c3QgQ29tbWVyY2lhbCBSb290IENBIDEwHhcNMTQwMTE2MTgxMjIzWhcNMzQw
MTE2MTgxMjIzWjBKMQswCQYDVQQGEwJVUzESMBAGA1UEChMJSWRlblRydXN0MScw
JQYDVQQDEx5JZGVuVHJ1c3QgQ29tbWVyY2lhbCBSb290IENBIDEwggIiMA0GCSqG
SIb3DQEBAQUAA4ICDwAwggIKAoICAQCnUBneP5k91DNG8W9RYYKyqU+PZ4ldhNlT
3Qwo2dfw/66VQ3KZ+bVdfIrBQuExUHTRgQ18zZshq0PirK1ehm7zCYofWjK9ouuU
+ehcCuz/mNKvcbO0U59Oh++SvL3sTzIwiEsXXlfEU8L2ApeN2WIrvyQfYo3fw7gp
S0l4PJNgiCL8mdo2yMKi1CxUAGc1bnO/AljwpN3lsKImesrgNqUZFvX9t++uP0D1
bVoE/c40yiTcdCMbXTMTEl3EASX2MN0CXZ/g1Ue9tOsbobtJSdifWwLziuQkkORi
T0/Br4sOdBeo0XKIanoBScy0RnnGF7HamB4HWfp1IYVl3ZBWzvurpWCdxJ35UrCL
vYf5jysjCiN2O/cz4ckA82n5S6LgTrx+kzmEB/dEcH7+B1rlsazRGMzyNeVJSQjK
Vsk9+w8YfYs7wRPCTY/JTw436R+hDmrfYi7LNQZReSzIJTj0+kuniVyc0uMNOYZK
dHzVWYfCP04MXFL0PfdSgvHqo6z9STQaKPNBiDoT7uje/5kdX7rL6B7yuVBgwDHT
c+XvvqDtMwt0viAgxGds8AgDelWAf0ZOlqf0Hj7h9tgJ4TNkK2PXMl6f+cB7D3hv
l7yTmvmcEpB4eoCHFddydJxVdHixuuFucAS6T6C6aMN7/zHwcz09lCqxC0EOoP5N
iGVreTO01wIDAQABo0IwQDAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUwAwEB
/zAdBgNVHQ4EFgQU7UQZwNPwBovupHu+QucmVMiONnYwDQYJKoZIhvcNAQELBQAD
ggIBAA2ukDL2pkt8RHYZYR4nKM1eVO8lvOMIkPkp165oCOGUAFjvLi5+U1KMtlwH
6oi6mYtQlNeCgN9hCQCTrQ0U5s7B8jeUeLBfnLOic7iPBZM4zY0+sLj7wM+x8uwt
LRvM7Kqas6pgghstO8OEPVeKlh6cdbjTMM1gCIOQ045U8U1mwF10A0Cj7oV+wh93
nAbowacYXVKV7cndJZ5t+qntozo00Fl72u1Q8zW/7esUTTHHYPTa8Yec4kjixsU3
+wYQ+nVZZjFHKdp2mhzpgq7vmrlR94gjmmmVYjzlVYA211QC//G5Xc7UI2/YRYRK
W2XviQzdFKcgyxilJbQN+QHwotL0AMh0jqEqSI5l2xPE4iUXfeu+h1sXIFRRk0pT
AwvsXcoz7WL9RccvW9xYoIA55vrX/hMUpu09lEpCdNTDd1lzzY9GvlU47/rokTLq
l1gEIt44w8y8bckzOmoKaT+gyOpyj4xjhiO9bTyWnpXgSUyqorkqG5w2gXjtw+hG
4iZZRHUe2XWJUc0QhJ1hYMtd+ZciTY6Y5uN/9lu7rs3KSoFrXgvzUeF0K+l+J6fZ
mUlO+KWA2yUPHGNiiskzZ2s8EIPGrd6ozRaOjfAHN3Gf8qv8QfXBi+wAN10J5U6A
7/qxXDgGpRtK4dw4LTzcqx+QGtVKnO7RcGzM7vRX+Bi6hG6H
-----END CERTIFICATE-----
```

  2. Upload the certificate through the Cisco Unified Operating System Administration web GUI.
Go to **Security > Certificate Management > Upload Certificate/Certificate chain**. Choose **tomcat-trust** as the Certificate Purpose and upload the certificate from the saved destination.


**Manual Certificate Update (Smart Licensing)**
For all other CUCM 12.0, 12.5, and 14 versions**,** Cisco recommends to install the COP file on the CUCM Publisher to add the new IdenTrust Commercial Root CA 1 certificate to CUCM.
  1. Follow the directions in the [Cisco Unified Communications Manager COP File for SLM CDETS CSCvx00530](https://www.cisco.com/web/software/286319173/139477/ciscocm.slm_quovadis_rootCA_decommission_v1.1.k4.cop-Readme.pdf) document.
  2. Download the [COP file v1.1.k4](http://software.cisco.com/download/home/286322286/type/286319173/release/COP-Files).
     * The COP file version has changed from v1.0.k4 to v 1.1.k4 due to the Cisco bug ID [CSCwb50904](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb50904). If you installed ciscocm.slm_quovadis_rootCA_decommission_v1.0.k4.cop.sha512 and you are still not able to get Smart License Manager to connect, it is recommended to install the latest version of the COP file (ciscocm.slm_quovadis_rootCA_decommission_v1.1.k4.cop.sha512). See the v1.1 COP file readme for additional information.
     * If you installed ciscocm.slm_quovadis_rootCA_decommission_v1.0.k4.cop.sha512 and everything is working as expected, no further action is required.


**Note** : Existing certificates issued from the HydrantID SSL ICA G3 do not need replacement. They are normal certificates issued from the current SSL certificate service and can be used until expiration.
### Additional Information
Cisco has created a web page to provide customers and partners with additional information on this issue. Consult the [QuoVadis Root CA 2 Decommission page](https://tools.cisco.com/security/center/resources/Q-CA-Root-Change) for a full list of products affected, associated Field Notices, and frequently asked questions.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72318.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72318.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Communications Manager Version 12.5](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-12-5/model.html)
  * [Unified Communications Manager Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-14/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/723/fn72318.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72318.html)
