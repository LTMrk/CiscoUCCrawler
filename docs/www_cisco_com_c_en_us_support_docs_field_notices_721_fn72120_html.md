  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72120.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72120.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72120.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72120.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72120.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Unified Communications Manager (CallManager)](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-field-notices-list.html)


# Field Notice: FN72120 - CUCM, SME, and IM&P: QuoVadis Root CA 2 Decommission Might Affect Incoming Calls to Cisco Jabber/WebEx (Android and iOS) - Workaround Provided
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/721/fn72120.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72120.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/721/fn72120.html)


Updated:January 26, 2026
Document ID:FN72120
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
High
**Impact Rating:**
High
**First Published:**
2021-Oct-29
**Last Published:**
2026-Jan-26
**Revision:**
2.1
**Cisco Bug IDs:**
  * [CSCwa88279](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwa88279)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| Unified Communications Manager / Cisco Unity Connection Updates  | -  | 11.5(1), 11.5(1)SU1, 11.5(1)SU10, 11.5(1)SU2, 11.5(1)SU3, 11.5(1)SU3a, 11.5(1)SU3b, 11.5(1)SU4, 11.5(1)SU5, 11.5(1)SU6, 11.5(1)SU7, 11.5(1)SU8, 11.5(1)SU9, 11.5(2), 12.0(1), 12.0(2), 12.5(1)  |   |  
| Unified Communications Manager Updates  | -  | 12.0(1)SU1, 12.0(1)SU2, 12.0(1)SU3, 12.0(1)SU4, 12.0(1)SU5, 12.5(1), 12.5(1)SU1, 12.5(1)SU2, 12.5(1)SU3, 12.5(1)SU4, 12.5(1)SU5, 14(1) Beta  |   |  
| Unified Communications Manager Updates  | 14  | 14, 14SU1  |   |  
| Unified Presence Server (CUP) Updates  | 11.5(1)  | 11.5(1), 11.5(1)SU1, 11.5(1)SU10, 11.5(1)SU2, 11.5(1)SU3, 11.5(1)SU3a, 11.5(1)SU4, 11.5(1)SU5, 11.5(1)SU5a, 11.5(1)SU6, 11.5(1)SU7, 11.5(1)SU8, 11.5(1)SU9  |   |  
| Unified Presence Server (CUP) Updates  | 12.5(1)  | 12.5(1), 12.5(1)SU1, 12.5(1)SU2, 12.5(1)SU3, 12.5(1)SU4, 12.5(1)SU5  | 12.5(1): Includes Cisco Unified Communications IM & Presence Release 12.0  
12.5(1)SU1: Includes Cisco Unified Communications IM & Presence Release 12.0  
12.5(1)SU2: Includes Cisco Unified Communications IM & Presence Release 12.0  
12.5(1)SU3: Includes Cisco Unified Communications IM & Presence Release 12.0  
12.5(1)SU4: Includes Cisco Unified Communications IM & Presence Release 12.0  
12.5(1)SU5: Includes Cisco Unified Communications IM & Presence Release 12.0  |  
| Unified Presence Server (CUP) Updates  | 14  | 14, 14SU1  |   |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwa88279](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwa88279)  | Incoming Calls to Cisco Jabber and WebEx (Android and iOS) Will Fail while in background mode  |  
  

### Problem Description
  

For affected versions of Cisco Unified Communications Manager (CUCM), Cisco Session Management Edition (SME), and Cisco Unified Communications Manager IM & Presence (IM&P), some Secure Sockets Layer (SSL) certificates issued from the QuoVadis root certificate authority (CA) trust chain before March 31, 2021 cannot be renewed from this CA. Once those certificates expire on devices or are removed from the Cisco cloud servers, functions such as Push Notification will fail to establish secure connections to Cisco and might not operate properly. 
  

### Background
  

The QuoVadis Root CA 2 Public Key Infrastructure (PKI) used by CUCM, SME, and IM&P software to issue SSL certificates is subject to an industry-wide issue that affects revocation abilities. Due to this issue, no new QuoVadis Root CA 2 certificates will be issued or renewed by Cisco after March 31, 2021. This affects certificate renewals on devices, Cisco cloud servers, and third-party services.
Certificates issued before the QuoVadis Root CA 2 was decommissioned will continue to be valid. However, the certificates on the Cisco cloud server have been updated to IdenTrust. This might cause functions such as Push Notification to fail to establish secure connections to Cisco cloud servers.
This table shows a summary of the QuoVadis Root CA 2 certificate change dates for affected Cisco services.  
| Cisco Cloud Server  | QuoVadis Certificate Expiration Date  | Affected Services  |  
| --- | --- | --- |  
| tools.cisco.com  | November 7, 2021  |  Tomcat  |  
  

### Problem Symptom
  

Expiration of the QuoVadis Root CA 2 certificates affects Push Notifications with the associated symptoms.
  * For CUCM, SME, and IM&P versions 14, 12.5 (SU5 and earlier), or 11.5 (SU10 and earlier) and have Cisco Jabber (Android or Apple iOS) or WebEx (Android or Apple iOS); customers will not receive incoming calls or message notifications once the client moves to background mode due to unsuccessful Push Notifications.
  * For CUCM, SME, and IM&P versions 14, 12.5 (SU5 and earlier), or 11.5 (SU10 and earlier); customers will not be able to enable the Push Notification service and will receive this error message: 
`"Push Notification/Activation Code Onboarding Settings cannot be configured as a valid certificate is not present in trust store. Either upload the certificates manually or check the check box to have Cisco manage the Cisco Cloud Service CA Certificates. For HTTPS proxy make sure the valid certificates are present for tomcat and tomcat trust store."`

  

### Workaround/Solution
  

Cisco has migrated from the QuoVadis Root CA 2 to the IdenTrust Commercial Root CA 1 for SSL certificates. Cisco recommends to add the new IdenTrust Commercial Root CA 1 certificate to CUCM, SME, or IM&P.
**Manual Certificate Update**
  1. Copy and paste this IdenTrust Commercial Root CA 1 Certificate into a text file on your computer. 

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

  2. Update the certificate based on the product version information in this table.  
| Push Notification Cloud Onboarding Status  | CUCM, SME, or IM&P Release  | Certificate Managed By *  | Recommended Action Must Be Performed Prior to November 7, 2021  |  
| --- | --- | --- | --- |  
| Customers who have already onboarded Push Notifications via the cloud.  | Release 14, 12.5 (SU5 and earlier), 11.5 (SU10 and earlier)  | Cisco  |  **Note:** Service restarts must be performed in the exact order as specified. The IdenTrust certificate will be automatically copied to the tomcat-trust store. Verify the IdenTrust certificate is available in the CUCM tomcat- trust. Choose **Cisco Unified OS Administration > Security > Certificate Management** and search for tomcat-trust certificates: 1. On CUCM, restart tomcat on the Publisher node.  
2. On CUCM, restart "Cisco Push Notification Service" on all nodes that have the service activated.  
3. On IM&P, restart “Cisco XCP Router” service on all the nodes.  
4. On IM&P, restart “Cisco XCP Config Manager” service on all the nodes.  |  
| Customer  |  **Note:** Service restarts must be performed in the exact order as specified. 1. Manually upload the [IdenTrust Commercial Root CA 1 certificate](https://www.identrust.com/identrust-commercial-root-ca-1 "IdenTrust Commercial Root CA 1") to the tomcat-trust store.  
2. On CUCM, restart tomcat on the Publisher node.   
3. On CUCM, restart "Cisco Push Notification Service" on all nodes that have the service activated.  
4. On IM&P, restart “Cisco XCP Router” service on all the nodes.  
5. On IM&P, restart “Cisco XCP Config Manager” service on all the nodes.  |  
| Customers who perform Push Notification onboarding via the cloud for the first time.  | Release 14,12.5 (SU5 and earlier), 11.5 (SU10 and earlier)  | Cisco  |  Manually upload the [IdenTrust Commercial Root CA 1 certificate](https://www.identrust.com/identrust-commercial-root-ca-1 "IdenTrust Commercial Root CA 1") to the tomcat-trust store. Follow the standard procedure found in the [Push Notification Deployment Guide](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/push_notifications/cucm_b_push-notifications-deployment-guide/cucm_b_push-notifications-deployment-guide_chapter_01.html).  |  
| Customer  |  
| Customers who perform Push Notification onboarding via the cloud for the first time.  | Release 14 SU1  | Cisco  |  Follow the standard procedure found in the [Push Notification Deployment Guide](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/push_notifications/cucm_b_push-notifications-deployment-guide/cucm_b_push-notifications-deployment-guide_chapter_01.html).  |  
| Customer  |  
* To verify whether you have opted for Cisco to manage the certificate or for the customer to manage the certificate, log in to **Cisco Unified CM Administration UI > Advanced Features > Cisco Cloud Onboarding**. In the Cluster Cloud Onboarding Settings section, check the **I want Cisco to manage the Cisco Cloud Service CA certifications required for this trust** check box.


**Note:** Multiple CUCM and IM&P services must be restarted for the changes to take effect. It is recommended to perform this during a maintenance window as a restart of these services will impact call services.
For more information on Push Notification Cloud Onboarding, see the [Push Notification Deployment Guide](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/push_notifications/cucm_b_push-notifications-deployment-guide/cucm_b_push-notifications-deployment-guide_chapter_01.html).
For the steps to upload a new certificate, see [Upload Certificate](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/14/adminGd/cucm_b_administration-guide-14-0-1/cucm_b_test-adminguide_chapter_01111.html#CUCM_TK_UACB16F8_00).
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/721/fn72120img4.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/721/fn72120img4.jpg "Related image, diagram or screenshot.")
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/721/fn72120img5.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/721/fn72120img5.jpg "Related image, diagram or screenshot.")
**Note:** Existing certificates issued from the HydrantID SSL ICA G3 do not need replacement. They are normal certificates issued from the current SSL certificate service and can be used until expiration.
  

### Additional Information
  

After the certificate is updated, it is recommended to ensure the IdenTrust certificates are reflected properly in the tomcat-trust store.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/721/fn72120img3.jpeg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/721/fn72120img3.jpeg "Related image, diagram or screenshot.")
  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 2.1  | Updated Step 1.  | Workaround/Solution  | 2026-JAN-26  |  
| 2.0  | Updated throughout.  | Problem Description, Background, Problem Symptom, and Workaround/Solution  | 2022-FEB-25  |  
| 1.0  | Initial Release  | —  | 2021-OCT-29  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72120.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72120.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Communications Manager IM and Presence Service Version 12.5](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-im-presence-service-version-12-5/model.html)
  * [Unified Communications Manager IM and Presence Service Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-im-presence-service-version-14/model.html)
  * [Unified Communications Manager Version 12.5](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-12-5/model.html)
  * [Unified Communications Manager Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-version-14/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/721/fn72120.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72120.html)
