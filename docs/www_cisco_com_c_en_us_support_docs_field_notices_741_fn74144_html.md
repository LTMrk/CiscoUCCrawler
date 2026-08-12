  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74144.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74144.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74144.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74144.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74144.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Unity Connection](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-field-notices-list.html)


# Field Notice: FN74144 - Cisco Unity Connection SpeechView Transcription Service Will Stop Working after December 30, 2024 - Software Upgrade Recommended
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/741/fn74144.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74144.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/741/fn74144.html)


Updated:June 28, 2024
Document ID:FN74144
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| **Affected Software Product**  | **Affected Release**  | **Affected Release Number**  | **Affected Build Number**  |  
| --- | --- | --- | --- |  
| Cisco Unity Connection  | 12.5(1)  | 12.5(1)  | 12.5.1.10000-23  |  
| 12.5(1)  | 12.5(1)SU1  | 12.5.1.11900-57  |  
| 12.5(1)  | 12.5(1)SU2  | 12.5.1.12900-56  |  
| 12.5(1)  | 12.5(1)SU3  | 12.5.1.13900-35  |  
| 12.5(1)  | 12.5(1)SU4  | 12.5.1.14900-45  |  
| 12.5(1)  | 12.5(1)SU5  | 12.5.1.15900-38  |  
| 12.5(1)  | 12.5(1)SU6  | 12.5.1.16900-29  |  
| 12.5(1)  | 12.5(1)SU7  | 12.5.1.17900-31  |  
| 12.5(1)  | 12.5(1)SU8  | 12.5.1.18900-16  |  
| 12.5(1)  | 12.5(1)SU8a  | 12.5.1.18901-2  |  
|   | 12.5(1)  | 12.5(1)SU9  | TBD  |  
|   |   |   |   |  
| Cisco Unity Connection  | 14  | 14  | 14.0.1.10000-19  |  
| 14  | 14SU1  | 14.0.1.11900-128  |  
| 14  | 14SU2  | 14.0.1.12900-69  |  
| 14  | 14SU3  | 14.0.1.13900-70  |  
| 14  | 14SU3a  | 14.0.1.13901-2  |  
|   |   |   |   |  
| Cisco Unity Connection  | 15  | 15  | 15.0.1.10000-24  |  
| 15  | 15SU1  | 15.0.1.11900-14  |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwi70031](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwi70031)  | CUC Migrate 3rd party transcription service to Cisco Webex in-house transcription service  |  
  

### Problem Description
  

The Cisco Unity Connection SpeechView transcription service will not transcribe voicemail messages after December 30, 2024. Administrators will observe a timeout error on the SpeechView transcription services page for Cisco Unity Connection on affected releases. Users will observe a timeout error in place of a transcript on applicable clients like Webinbox and Outlook.
  

### Background
  

The third-party service supporting the Cisco Unity Connection SpeechView transcription service will reach end of life on or after December 30, 2024. As a result, Cisco will be migrating the Cisco Unity Connection SpeechView transcription service from the third-party vendor to Cisco Webex in-house transcription service. 
Cisco Webex offers in-house transcription to power closed captions and transcription in English, French, German, Spanish, and Italian (September 2024). Cisco Webex in-house transcription is a Cisco-built machine learning model that leverages automatic speech recognition to provide closed captions and transcription features. In-house transcription takes speech audio input; performs feature extraction; decodes with the use of acoustic, language, and other models; and produces the text output. The model is trained with unique Cisco data sets that are curated for diverse demographics and further fine-tuned for specific feature use with Cisco Webex Meetings, Cisco Webex Contact Center, Cisco Webex Calling, Cisco devices, and Vidcast. The migration to bring transcription services in house will help Cisco offer best-in-class technology with the latest models to transcribe voice messages across multiple languages and dialects. 
**Note:** Portuguese is not offered in Cisco Webex transcription services. For further information, customers should contact their account team.
  

### Problem Symptom
  

The Cisco Unity Connection SpeechView transcription service will not transcribe voicemail messages after December 30, 2024, which will cause voicemail transcription to stop working. Administrators will observe a timeout error on the SpeechView transcription configuration page for affected releases of Cisco Unity Connection. Users will observe a timeout error in place of a transcript on applicable clients like Webinbox and Outlook.
  

### Workaround/Solution
  

### Solution
Cisco will migrate the SpeechView transcription service to the Cisco Webex Cloud-Connected UC services. Customers are recommended to upgrade to Cisco Unity Connection Release 14 SU4 or later or Release 15 SU2 or later prior to December 30, 2024. 
Upgrade to one of the Cisco Unity Connection releases in the following table to use the Cisco Webex in-house transcription service:  
| Cisco Unity Connection Release  | First Fixed Release  |  
| --- | --- |  
| 12.5(1)  
12.5(1)SU1  
12.5(1)SU2  
12.5(1)SU3  
12.5(1)SU4  
12.5(1)SU5  
12.5(1)SU6  
12.5(1)SU7  
12.5(1)SU8  |  [14SU4](https://software.cisco.com/download/home/286328409/type/286319533/release/) (Jul 31, 2024)  
[15SU2](https://software.cisco.com/download/home/286331949/type/286319533/release/) (Sep 19, 2024)  |  
| 14  
14SU1  
14SU2  
14SU3  
14SU3a  |  [14SU4](https://software.cisco.com/download/home/286328409/type/286319533/release/) (Jul 31, 2024)  
[15SU2](https://software.cisco.com/download/home/286331949/type/286319533/release/) (Sep 19, 2024)  |  
| 15  
15SU1   |  [15SU2](https://software.cisco.com/download/home/286331949/type/286319533/release/) (Sep 19, 2024)  |  
Once Cisco Unity Connection has been upgraded to one of the fixed releases in the preceding table, the SpeechView voicemail transcription service will be available on the Service Management page on Cisco Webex Cloud-Connected UC. Use the toggle button and follow the on-screen instructions to enable the service. For more information on enabling or disabling Cisco Webex Cloud-Connected UC services in Control Hub, see [this Webex Help Center article](https://help.webex.com/en-us/article/oh49ck/Enable-or-Disable-Webex-Cloud-Connected-UC-Services-in-Control-Hub).
  

### How to Identify Affected Products
  

If the following conditions are true after December 30, 2024, the SpeechView transcription service is not functioning:
    * On the **Transcription Service for SpeechView** page, under **Status of Last Transcription Operation** , the Action Status is **Fail** , as shown in the following screenshot:  
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/741/fn74144_9a7b742483b6c250fceb70326daad3c1.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/741/fn74144_9a7b742483b6c250fceb70326daad3c1.png "Related image, diagram or screenshot.")


  
  

  * After setting the **Navigation** field to **Cisco Unity Connection Serviceability** and then choosing **Tools > Reports > SpeechView Activity Summary Report**, administrators observe **Fail** in the **Status** column and **Timeout** in the **Reason** column, as shown in the following screenshot:  
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/741/fn74144_ddcbf0e483b6c250fceb70326daad3fc.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/741/fn74144_ddcbf0e483b6c250fceb70326daad3fc.png "Related image, diagram or screenshot.")

  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.0  | Initial Release  | —  | 2024-JUN-28  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74144.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Customers Also Viewed
  * [Reset Your Voicemail PIN on Cisco Unity Connection](https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/224871-reset-your-voicemail-pin-on-cisco-unity.html)
  * [Configure Unity Connection for Office 365](https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/118828-config-cuc-00.html)
  * [Configuration Example for Secure SIP Integration Between CUCM and CUC based on Next Generation Encryption (NGE)](https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/211622-Configuration-Example-for-Secure-SIP-Int.html)
  * [SpeechView Cisco Webex in-house transcription service for Unity Connection](https://www.cisco.com/c/en/us/support/docs/unified-communications/unity-connection/Technote-SpeechView-Cisco-Webex-in-house-transcription-service-for-Unity-Connection.html)
  * + Show 1 More


### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74144.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unity Connection Version 12.x](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-12-x/model.html)
  * [Unity Connection Version 14](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-14/model.html)
  * [Unity Connection Version 15](https://www.cisco.com/c/en/us/support/unified-communications/unity-connection-version-15/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/741/fn74144.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74144.html)
