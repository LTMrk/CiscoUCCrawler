  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72185.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72185.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72185.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72185.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72185.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Unified IP Interactive Voice Response (IVR)](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-ip-interactive-voice-response-ivr/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-ip-interactive-voice-response-ivr/products-field-notices-list.html)


# Field Notice: FN - 72185 - UCCE/UCCX Finesse Agents Disconnected in Chrome 88 - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/721/fn72185.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72185.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/721/fn72185.html)


Updated:August 27, 2021
Document ID:FN72185
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 24-Jul-21  | Initial Release  |  
| 1.1  | 27-Aug-21  | Updated the Products Affected and Workaround/Solution Sections  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | Finesse Software  | 12  | 12.5(1), 12.5(1)ES1, 12.5(1)ES2, 12.5(1)ES3, 12.5(1)ES4, 12.5(1)ES5, 12.5(1)ES6  | Finesse UCCE  |  
| NON-IOS  | Finesse Software  | 12  | 12.0(1), 12.0(1)ES1, 12.0(1)ES2, 12.0(1)ES3, 12.0(1)ES4, 12.0(1)ES5, 12.0(1)ES6, 12.0(1)ES7  | Finesse UCCE  |  
| NON-IOS  | Finesse Software  | 11  | 11.6(1), 11.6(1)ES1, 11.6(1)ES10, 11.6(1)ES2, 11.6(1)ES3, 11.6(1)ES4, 11.6(1)ES5, 11.6(1)ES6, 11.6(1)ES7, 11.6(1)ES8, 11.6(1)ES9  | Finesse UCCE  |  
| NON-IOS  | Unified Contact Center Express Software  | Unified CCX 12  | 12.5(1), 12.5(1)SU1  | Finesse UCCX  |  
| NON-IOS  | Unified Contact Center Express Software  | Unified CCX 11  | 11.6(2)  | Finesse UCCX  |  
| NON-IOS  | Unified Contact Center Express Latest Updates  | Unified CCX 11  | 11.6(2)ES01, 11.6(2)ES02, 11.6(2)ES03, 11.6(2)ES04, 11.6(2)ES05, 11.6(2)ES06, 11.6(2)ES07  | Finesse UCCX  |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvx68660](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvx68660)  | Agents getting disconnected in Chrome 88+  |  
| [CSCvx73795](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvx73795)  | Agents getting disconnected in Chrome 88+  |  
| [CSCvy25397](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvy25397)  | UCCE Finesse Agents getting disconnected in Chrome 88+  |  
### Problem Description
Google Chrome 88+ will heavily throttle chained JavaScript timers for minimized/background tabs in particular conditions. This change in Chrome breaks the ping mechanism between the Finesse client and the server.
The Finesse client sends a ping to the server at fixed intervals so that the presence is maintained on the server and the server knows that the client is alive. This ping mechanism is facilitated by the JavaScript timers on the Finesse client. Now, with Chrome 88, this JavaScript timer will be throttled and ping will be rescheduled to every 60 seconds when the Finesse client tab is in the background or minimized. This delay will cause the Finesse client to lose the connection with the server.
In Finesse desktops which use Bidirectional-streams Over Synchronous HTTP (BOSH) for notifications, the http-bind request with long polling is used by the client to maintain presence on the server. This is also done via recursive JavaScript timers that run on the Finesse client. Due to browser throttling of these JavaScript timers, the http-bind request is delayed and the server proceeds to disconnect the client.
### Background
For more information, see [Heavy throttling of chained JS timers beginning in Chrome 88](https://developer.chrome.com/blog/timer-throttling-in-chrome-88/).
### Problem Symptom
There will be a connection failure for these cases:
  * The Finesse for Unified Contact Center Express (Unified CCX) agent moves to Not Ready-Agent Logon while in the Talking state and Not Ready.
  * The Finesse standalone agent moves to Not Ready.


### Workaround/Solution
For a Unified Contact Center Enterprise (UCCE) Finesse standalone deployment, customers should upgrade to Finesse [Release 12.6.1](https://software.cisco.com/download/home/283613135/type/284259728/release/12.6) or later and Finesse [Release 12.5(1)ES7](https://software.cisco.com/download/home/283613135/type/284259728/release/12.5) or later.
It will also be included in the upcoming Finesse Release 12.0.1 ES08 and Finesse [Release 11.6.1 ES11](https://software.cisco.com/download/home/283613135/type/284259728/release/11.6).
The fix for Unified CCX deployments is included in these releases:
  * [Unified Contact Center Express 12.5(1) SU01 ES01](https://software.cisco.com/download/home/286325233/type/286314176/release/)
  * [Unified Contact Center Express 11.6(2)ES08](https://software.cisco.com/download/home/286321245/type/286314176/release/)


For a workaround, contact the Technical Assistance Center (TAC).
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72185.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72185.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Finesse](https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/series.html)
  * [Unified Contact Center Express 12.5(1)](https://www.cisco.com/c/en/us/support/contact-center/unified-contact-center-express-12-5-1/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/721/fn72185.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/721/fn72185.html)
