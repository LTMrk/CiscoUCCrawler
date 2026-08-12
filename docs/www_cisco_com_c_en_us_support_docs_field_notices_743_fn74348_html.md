  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74348.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74348.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74348.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74348.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74348.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Packaged Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-field-notices-list.html)


# Field Notice: FN74348 - Cisco Unified Contact Center Enterprise and Cisco Cloud Connect Orchestration Feature May Fail to Connect after May 4, 2026 - Software Upgrade Recommended
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74348.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74348.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/743/fn74348.html)


Updated:March 18, 2026
Document ID:FN74348
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Critical
**Impact Rating:**
Critical
**First Published:**
2026-Mar-18
**Last Published:**
2026-Mar-18
**Revision:**
1.0
**Cisco Bug IDs:**
  * [CSCws24436](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws24436)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| Cloud Connect  | 12  | 12.6(2)  |   |  
| Cloud Connect  | 15  | 15.0(1)  |   |  
| Packaged Contact Center Enterprise  | -  |   | Releases 12.6(2) and 15.0(1) are affected.  |  
| Unified Contact Center Enterprise  | -  |   | Releases 12.6(2) and 15.0(1) are affected.  |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCws24436](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCws24436)  | Devhub upgrade is required to compliance with Cisco security standards for UCCE/PCCE CloudConnect Orchestration  |  
  

### Problem Description
  

Effective May 4, 2026, Cisco will discontinue support for API Key authentication within the Cloud Connect orchestration feature of Cisco Unified Contact Center Enterprise (UCCE) and Cisco Packaged Contact Center Enterprise (PCCE). To ensure continued access to Cisco DevHub software downloads and uninterrupted orchestration operations, customers are required to transition to Identity Token authentication.
For detailed migration instructions and the required actions, see the **Workaround/Solution** section of this Field Notice.
  

### Background
  

On May 4, 2026, Cisco will implement a security enhancement for the Cisco DevHub software artifactory. This update requires a change to the authentication method used to access and download software for Cisco UCCE and Cisco PCCE within the Cloud Connect orchestration feature. Customers who are currently using API Key authentication must migrate to Identity Token to ensure continued orchestration functionality.
  

### Problem Symptom
  

Failure to complete the required action by May 4, 2026, will result in the following service impacts:
  * **Inability to download software:** Orchestration users will be unable to access or download software packages from the Cisco DevHub.
  * **Orchestration service disruption:** Orchestration-driven patching and upgrade operations for Cisco UCCE and Cisco PCCE on Cloud Connect will fail.

  

### Workaround/Solution
  

**Solution**
**Required Actions for Devhub Authentication Migration**
To maintain uninterrupted access to Cisco DevHub for Cisco UCCE and Cisco PCCE Cloud Connect orchestration, complete the following steps:
#### Part 1: Devhub Authentication Migration Pre-Rollout Patching (Complete Before May 4, 2026)
Install the required Engineering Special (ES) on Cloud Connect for the specific release to ensure compatibility with the new authentication method:
  * [**12.6(2):** Install **ES04**](https://software.cisco.com/download/home/268439622/type/286325642/release/12.6\(2\)ES4)
  * [**15.0(1):** Install **ES202511**](https://software.cisco.com/download/home/268439622/type/286325642/release/15.0\(1\)ES202511)


**Note** : While 15.0(1) supports Identity Token configuration without an ES, **ES202511** is mandatory only for customers who use the Identity Token Auto-Rotation feature.
#### Part 2: Devhub Authentication Migration Post-Rollout Configuration Update (effective May 4, 2026)
After the DevHub security enhancement is live, complete the following steps in Cloud Connect publisher:
  1. **Generate Identity Token:** Follow the instructions in the **Generate the Artifactory Identity Token** section of the proper [CCE Install and Upgrade Guide](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html).
  2. **Update Authentication Method:** Change the authentication method to **Identity Token** using the CLI. For more information, see the **CLI to Configure Authentication Method for Artifactory** section of the proper [CCE Install and Upgrade Guide](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html).
  3. **Configure Credentials:** Update authentication credentials with the newly generated Identity token. For more information, see the **CLI to Configure Artifactory URL and Artifactory Authentication Credentials** section of the proper [CCE Install and Upgrade Guide](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html).
  4. **[Optional] Enable Auto-Rotation:** To automate token updates and eliminate manual intervention every six months, configure Identity Token Auto-Rotation. For more information, see the **Configure Identity Token Auto Rotation** section of the proper [CCE Install and Upgrade Guide](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html).

  

### Additional Information
  

**Note for 12.6(1) Environments:** Customers who are currently running Cisco Cloud Connect Release 12.6(1) must upgrade to Release 12.6(2) and install ES04. This Engineering Special is exclusively available for Release 12.6(2) in accordance with standard product release guidelines.
  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.0  | Initial Release  | —  | 2026-MAR-18  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74348.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Customers Also Viewed
  * [Field Notice: FN74382 - Cisco Unified Contact Center Products: Impact on Secure Communication Due to Upcoming Changes to TLS certificates Issued by Public Certificate Authorities with Client Authentication EKU, Starting March 2027 - Workaround Provided](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74382.html)
  * [Implement CA-Signed Certificates in a CCE 12.6 Solution](https://www.cisco.com/c/en/us/support/docs/contact-center/packaged-contact-center-enterprise/220730-implement-ca-signed-certificates-in-a-cc.html)
  * [Configure and Troubleshoot CVP Smart License on PCCE 12.5](https://www.cisco.com/c/en/us/support/docs/contact-center/packaged-contact-center-enterprise/215400-configure-pcce-12-5-and-cvp-12-5-smart.html)
  * [Exchange Self-Signed Certificates in a PCCE Solution](https://www.cisco.com/c/en/us/support/docs/contact-center/packaged-contact-center-enterprise/215354-exchange-self-signed-certificates-in-a-p.html)
  * [Enhance Database Performance for Contact Center UCCE/PCCE](https://www.cisco.com/c/en/us/support/docs/contact-center/packaged-contact-center-enterprise/220155-enchance-database-performance-for-contac.html)
  * + Show 2 More


### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74348.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Packaged Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/series.html)
  * [Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/743/fn74348.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74348.html)
