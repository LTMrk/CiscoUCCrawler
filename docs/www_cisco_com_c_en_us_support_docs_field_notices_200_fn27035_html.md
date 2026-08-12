  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn27035.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn27035.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn27035.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn27035.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn27035.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Unified Contact Center Express](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-field-notices-list.html)


# Field Notice: *Expired* FN - 27035 - Integrated Contact Distribution (ICD) Agents Stuck in RESERVED State With IP Contact Center (IPCC) Express
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/200/fn27035.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn27035.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/200/fn27035.html)


Updated:November 5, 2003
Document ID:FN27035
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
  
[](http://www.cisco.com/warp/customer/tech_tips/index/fn.html)
### Revised April 28, 2008  
November 5, 2003
### NOTICE:
### THIS FIELD NOTICE HAS BEEN EXPIRED AND IS NO LONGER MAINTAINED OR UPDATED BY CISCO.
### THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE, WARRANTY OR SUPPORT. USE OF THE INFORMATION ON THIS FIELD NOTICE OR MATERIALS LINKED FROM THIS FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.
* * *
### Products Affected
Cisco IP Contact Center (IPCC) Express version 3.0(2) and later.
### Problem Description
Integrated Contact Distribution (ICD) Agents are stuck in RESERVED state, leaving calls in the Queue and forcing the agent to log out and back in.
### Background
ICD Agents are forced to log out and back in after being left in RESERVED state due to various issues. See for more information..
### Problem Symptoms
Agents can be left in a RESERVED state for a variety of reasons. Below are examples of some of the reasons:
  1. Misconfiguration. The following configurations are not supported for agent phones:
     * Two lines on an agents phone that have the same extension but exist in different partitions
     * An ICD extension assigned to multiple devices.
     * Call forwarding on an ICD line is not supported prior to CRS 3.1.
     * Call waiting enabled on an ICD line.
**Note:** Configuring an ICD extension in a device profile is supported.
  2. [CSCeb36950](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCeb36950) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only) - The Select Resource step is set to `Connect = No` and the Failed Branch of the Connect Step has a Goto step that jumps back into the Select Resource Step.
  3. [CSCdx46617](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCdx46617) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only) - An ICD Route point is the destination of a redirect from another CRS script. The script should have a Delay step before the Accept step that gives the transferring party time to complete their transfer before the CRS script answers the call
  4. [CSCeb49310](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCeb49310) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only) - Caller is redirected to an ICD CTI route point from another script. After the call is redirected and the call is queued, call will no longer be queued after 8-10sec. The caller remains in an ICD script loop but does not go to an Agent when one becomes available. Agents are left in RESERVED state if call is queued then routed to Agent before it disappears from queue.
  5. [CSCec02808](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCec02808) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only) - Call is blind transferred to CRS from Unity and Agent is stuck in RESERVED.


### Workaround/Solution
  1. [CSCeb36950](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCeb36950) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only) . Modify the script so that the Goto step jumps to a label that is before the Select Resource Step. For more information on this issue refer to the [Cisco IPCC Express Technical Tip](http://www.cisco.com/warp/customer/78/IPCC-CallStuck-In-Q.html).
  2. [CSCdx46617](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCdx46617) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only) . Always add a SetContactInfo step to the Successful branch of a Redirect step.
  3. [CSCeb49310](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCeb49310) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only) . Use the Subflow step to send callers to the ICD script instead of Redirect step. Or add a delay of more than 15 seconds in the ICD script before the call gets to the Select Resource Step in the ICD workflow. This can be done by putting in a Delay Step or by playing prompts that are at least 15 seconds.
**Solution:** This problem only occurs when connecting to CallManager 3.2 or 3.3. Bug ID [CSCeb44077](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCeb44077) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only) is corrected in CCM 3.3(2) ES43, 3.2(3) ES15, and 3.3(3) ES01.1.
  4. [CSCec02808](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCec02808) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only) . Resolved in CRS 3.1(2) or 3.1(1) - SR2 ES1


### DDTS
To follow the bug ID link below and see detailed bug information, you must be a [registered](http://tools.cisco.com/RPF/register/register.do) user and you must be logged in.  
|  DDTS  |  Description  |  
| --- | --- |  
|  [CSCeb36950](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCeb36950) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only)  |  Documentation on Select Resourece Step  |  
|  [CSCdx46617](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCdx46617) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only)  |  Redirect to ICD rp could remain in Q or mess up agent state and RTR  |  
|  [CSCeb49310](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCeb49310) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only)  |  Calls unanswerable & agent state changed to reserved  |  
|  [CSCec02808](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCec02808) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only)  |  Agent stuck in RESERVED for call blind-xferred from Unity to IPCC Express  |  
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/warp/customer/687/Directory/DirTAC.shtml) by one of the following methods:
  * [Open a service request on Cisco.com](http://tools.cisco.com/ServiceRequestTool/create/)
  * [By email](http://www.cisco.com/warp/customer/687/Directory/DirTAC.shtml#email)
  * [By telephone](http://www.cisco.com/warp/customer/687/Directory/DirTAC.shtml#telephone)


### Receive Email Notification For New Field Notices
[Product Alert Tool](http://www.cisco.com/cgi-bin/Support/FieldNoticeTool/field-notice) - Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
* * *
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn27035.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn27035.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Contact Center Express](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/200/fn27035.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn27035.html)
