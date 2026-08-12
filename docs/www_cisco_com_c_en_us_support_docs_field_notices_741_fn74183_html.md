  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74183.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74183.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74183.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74183.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74183.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Unity Connection](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-field-notices-list.html)


# Field Notice: FN74183 - Cisco Jabber and Cisco Webex App Show Voicemail Service Disconnected From Cisco Unity Connection - Configuration Change Recommended
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/741/fn74183.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74183.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/741/fn74183.html)


Updated:September 25, 2024
Document ID:FN74183
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Medium
**Impact Rating:**
Medium
**First Published:**
2024-Sep-19
**Last Published:**
2024-Sep-19
**Revision:**
1.0
**Cisco Bug IDs:**
  * [CSCwk33540](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwk33540), 
  * [CSCwm00548](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwm00548)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| Jabber Software  | 14  | 14.3(1)  | 14.3(1): All releases 14.3(1)1 and later  |  
| Unity Connection Updates  | 12  | 12.5(1), 12.5(1)SU1, 12.5(1)SU2, 12.5(1)SU3, 12.5(1)SU4, 12.5(1)SU5, 12.5(1)SU6, 12.5(1)SU7, 12.5(1)SU8, 12.5(1)SU8a, 12.5(1)SU9  |   |  
| Unity Connection Updates  | 14  | 14  |   |  
| Unity Connection Updates  | 15  | 15  |   |  
| Webex App, formerly Webex Teams  | 44  | 44.5  | 44.5: All releases 44.5 and later  |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwk33540](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwk33540)  | WebEx 44.5+ shows voicemail services disconnected with Unity (Jabber/ Webex App)  |  
| [CSCwm00548](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwm00548)  | WebEx 44.5+ shows voicemail services disconnected (CUC)  |  
  

### Problem Description
  

Cisco Jabber releases 14.3(1) and later and Cisco Webex App releases 44.5 and later do not support SHA-1. Consequently, Cisco Unity Connection certificates that are signed with SHA-1 will show voicemail services as disconnected.
  

### Background
  

Cisco Jabber releases 14.3(1) and later and Cisco Webex App releases 44.5 and later will not support SHA-1 in trusted TLS negotiations. TLS server certificates and public CA-signed certificates must use SHA-2.
Cisco has made this change to align with the latest industry standards, to provide enhanced security considerations to customers, and to support industry-wide deprecation of SHA-1. Other software providers have made similar changes:
  * For iOS 13 and later and macOS Catalina 10.15 and later, TLS server certificates and issuing CAs must use a hash algorithm from the SHA-2 family in the signature algorithm because SHA-1 signed certificates are no longer trusted for TLS negotiations. See [Requirements for trusted certificates in iOS 13 and macOS 10.15](https://support.apple.com/en-in/103769).
  * Customers who operate on Windows OS versions must have SHA-2 code signing support installed on their devices to install the latest updates released on or after July 2019. Devices without SHA-2 support will not be able to install any Windows updates on or after July 2019. See [SHA-1 Windows content to be retired August 3, 2020](https://techcommunity.microsoft.com/t5/windows-it-pro-blog/sha-1-windows-content-to-be-retired-august-3-2020/ba-p/1544373).
  * For Android 10 and later releases, certificates that use the SHA-1 hash algorithm are not trusted in TLS connections. See [Behavior changes: all apps](https://developer.android.com/about/versions/10/behavior-changes-all).

  

### Problem Symptom
  

Cisco Unity Connection voicemail services will show as disconnected if security certificates are signed with SHA-1. TLS negotiations with Jabber releases 14.3(1) and later and Webex App releases 44.5 and later will fail with SHA-1 signed security certificates.
  

### Workaround/Solution
  

Cisco recommends working with your certificate provider to sign Unity Connection certificates with SHA-2 algorithms.
  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.0  | Initial Release  | —  | 2024-SEP-19  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74183.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74183.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Jabber](https://www.cisco.com/c/en/us/support/unified-communications/jabber/series.html)
  * [Unity Connection Version 12.x](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-12-x/model.html)
  * [Unity Connection Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-14/model.html)
  * [Unity Connection Version 15](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-15/model.html)
  * [Webex App](https://www.cisco.com/c/en/us/support/unified-communications/spark/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74183.html)
