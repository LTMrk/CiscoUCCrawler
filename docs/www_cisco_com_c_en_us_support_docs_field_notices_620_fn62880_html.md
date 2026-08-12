  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62880.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62880.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62880.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62880.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62880.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Unified Contact Center Express](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-field-notices-list.html)


# Field Notice: FN - 62880 - New Zealand Daylight Savings Time Policy Changes Effective September 2007 - For Cisco Unified Contact Center Express (Unified CCX)
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/620/fn62880.html) to Save Content 
Print
### Available Languages
Updated:September 20, 2007
Document ID:FN62880
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
  
[](https://www.cisco.com/warp/customer/tech_tips/index/fn.html)
### Revised September 20, 2007
### September 4, 2007
### NOTICE:
### THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.
* * *
### Products Affected  
|  Products Affected  |  
| --- |  
|  UCCX - 2.2(X), 3.0(X), 3.1(X), 3.5(X), 4.0(X), 4.1(X), 4.5(X), 5.0(X)  |  
### Problem Description
The operating systems of most Cisco products that support Daylight Savings Time (DST) have built in mechanisms to automatically change the times, based on current user-selected rules. Once the new DST is implemented, the time on devices that maintain time zone information will continue to change according to the old method, unless changes are made.
New Zealand Standard Time is currently defined in the Time Act 1974 as being the 12 hours ahead of the coordinated Universal Time. The Department of Internal Affairs of New Zealand administers the Act.
The switchover dates to and from Daylight Savings Time (DST) will shift in the New Zealand in calendar year 2007. DST will commence one week earlier (the last Sunday in September) and will end three week later (the first Sunday in April'2008), each occurring at 2:00 A.M.
Because assumptions around the timing of the ongoing DST transition were designed into both the Microsoft Windows operating system and the Cisco Unified Contact Center software, adequate preparation for this event is necessary in order to avoid negative impact to system data reporting context. Further, as the JDK/JRE (Java) runtime facilities are themselves subject to the same update requirements, certain components of the product that utilize the JDK/JRE are required to have the Java Platform JDK NZ DST Timezone Updater patch tool applied. The tool is available directly from Sun Microsystems' Sun Developer Network.
This notice is intended to both alert you to the specific impact of the DST change and to detail the necessary remedial steps to ensure consistent and seamless product operation. Several Enterprise and Hosted product and product options are affected, and each requires specific consideration. Cisco Unified Contact Center (UCCX) is discussed in the following section. Customers deploying these product and configuration options should follow the steps outlined in the notice to ensure they avoid encountering problems with the forthcoming September 2007 DST transition.
The Contact Center product/product options affected are:
Cisco Unified Contact Center Express (Unified CCX), - (formerly IPCC Express, CRS), Cisco IP Interactive Voice Response (IP IVR) and Cisco IP Queue Manager (IP QM)
### Background
On April 30, 2007, the Minister of Internal Affairs issued a statement regarding a change in Daylight Saving Time policy for New Zealand. The change in policy has modified the start and end dates for Daylight Saving Time (DST). Beginning in 2007 and beyond, Daylight Saving Time in New Zealand will start on the last Sunday of September at 2:00 A.M. local time and end on the first Sunday of April at 3:00 A.M. local time.
Specifically for 2007-2008, Daylight Saving Time will begin at 2:00 A.M. local time on September 30, 2007, and end at 3:00 A.M. local time on April 6, 2008.
For more information, see the statement issued by the Minister of Internal Affairs: [Daylight saving to be extended](http://www.dia.govt.nz/diawebsite.nsf/wpg_URL/Services-Daylight-Saving-Index?OpenDocument).
The old Daylight Saving Time policy dictated that DST started on the first Sunday in October and ended on the third Sunday in March.
### Problem Symptoms
Problem Symptoms for Unified CCX
Failure to update the Unified CCX servers may result in the following:
  1. Historical Reports: Reports are off by one hour (pre-DST time) for the periods September 30, 2007 - October 6, 2007 and March 16, 2008 - April 6, 2008, as HR time is obtained from Unified CCX server.
  2. Trace timestamps: Time stamp in some logs will be off by one hour (pre-DST time).
  3. Real Time reports: Reports are off by one hour (pre-DST time) for the periods September 30, 2007 - October 6, 2007 and March 16, 2008 - April 6, 2008, as RTR time is obtained from Unified CCX server.
  4. Data written to the Unified CCX database: Data Time stamp will be off by one hour (pre-DST time) for the periods September 30, 2007 - October 6, 2007 and March 16, 2008 - April 6, 2008, as time is obtained from Unified CCX server.
  5. Scripts using the "Time of Day" step: Calls will be routed based on pre-DST time for the periods September 30, 2007 - October 6, 2007 and March 16, 2008 - April 6, 2008, as time is obtained from Unified CCX server.


### Workaround/Solution
Unified CCX (formerly IPCC Express, Customer Response Solution (CRS))
Includes: Cisco Unified Contact Center Express (Unified CCX), Cisco IP Interactive Voice Response (IP IVR) and Cisco IP Queue Manager (IP QM).
Patching Unified CCX servers is a multi step process as outlined below:
  1. Apply the appropriate OS patch on all Unified CCX servers.
  2. Depending on the Unified CCX version, apply appropriate SUN patch to update Java time zone rules on all Unified CCX servers.
  3. Apply Microsoft OS patches on all Cisco Agent Desktop (CAD)/Cisco Supervisor Desktop(CSD) machines.


Unified CCX uses the same OS build as current CCM Windows OS versions. Therefore, the OS fix for Unified CCX is the same as the OS fix for Cisco CallManager and it is necessary to apply OS patch on all Unified CCX servers.
To obtain the 2007 New Zealand DST changes required for the operating system, apply either:
2000-4-4a-sr10 (win-OS-Upgrade-K9-2000-4-4a-sr10.exe)
or
2000-4-5a-sr2 (win-OS-Upgrade-K9-2000-4-5a-sr2.exe)
or
2003-1-1-sr7 (win-OS-K9-2003-1-1-sr7.exe)
or
2003-1-2a-sr2 (win-OS-upgrade-K9.2003-1-2a-sr2.exe)
(or higher OS release) from [CallManager & Voice Apps Crypto Software](https://www.cisco.com/cgi-bin/tablebuild.pl/cmva-3des?psrtdcat20e2) ([registered](https://tools.cisco.com/RPF/register/register.do) customers only) link.
**Note:** Please do not apply Tzedit.exe patch provided by Microsoft or other patches provided by any third party vendors on Unified CCX servers.
Unified CCX 2.2(x), 3.0(x), 3.1(x) and 3.5(x)
**Note:** We strongly encourage you to upgrade to Unified CCX 4.0(5a) as soon as possible to avoid problems with future Daylight Saving changes. **Do not apply any OS patch on Unified CCX servers if you follow the manual workaround below.**
Unified CCX Manual Workaround:
  1. On the new New Zealand Daylight Saving Time date, Logon with administrator privileges to all Unified CCX Servers, starting with the engine node.
  2. Click Start, Settings, Control Panel, Date and Time.
  3. Click on Time Zone tab.
  4. Uncheck the **Automatically adjust clock for daylight savings changes.**
  5. Click on Date and Time tab.
  6. Adjust (if needed) the time to the actual time.
  7. Click Apply or Ok.
  8. Repeat steps for all other servers.


Important Steps To Perform:
  1. On or before the last Sunday of September, uncheck **Automatically adjust clock for Daylight Saving changes.**
  2. On the last Sunday of September, on or after 2:01 A.M., move the clock ahead one hour.
  3. On the first Sunday of April, on or after 3:01 A.M., move the clock behind one hour.


Please note, however, that manually adjusting the clock on the Unified CCX servers could result in a conflict in time which may produce time synchronization issues. For instance, adjusting the clock during any active call would result in incorrect historical records for that call. Therefore, adjusting the clock is best to be done when fewest active calls are present or the Unified CCX engine is stopped.
Alternatively, customers could upgrade to Unified CCX 4.0(5a) and follow the procedure listed below for Unified CCX 4.0(x) to accommodate the DST change.
Unified CCX 4.0(x), 4.1(x), 4.5(x) and 5.0(x)
The Unified CCX installation copies the private Java Runtime Engine (JRE) to path **C:\Program Files\wfavvid\java\current\bin\java** directory. Sun Microsystems has made available a tool to update the time zone database of current installations. To update the database used by Unified CCX's JRE, follow the steps listed below exactly. Because the JRE installed is considered "private" - it is not listed in the registry at **HKLM\Software\JavaSoft** or placed in the System Path - failure to specify the path to the java.exe used by Unified CCX can result in the update being applied to the incorrect JRE should other JREs be present on the machine.
Information regarding the tool that performs the JRE updates is available at the [Sun Java SE TZupdater Tool](http://java.sun.com/javase/tzupdater_README.html) page and in a README.html file with the tool itself.
Steps to Update the JRE
  1. Stop the Node Manager service on the Unified CCX server. During this time Unified CCX will not function.
  2. Visit [Java SE Downloads](http://java.sun.com/javase/downloads/index.jsp) with your browser of choice.
  3. Select the Download button to the right of the choice "JDK US DST Timezone Update Tool - 1.2.2"
**Note:** You will need to log-into a Sun Online Account before downloading the patch. If you do not have a Sun Online Account, you can register for one free-of-charge. A valid email address is required for registration.
  4. Download the patch to a folder of your choice on the Unified CCX system. The patch comes in the form a Zip file.
  5. Unzip the contents of the patch to the same folder. There should now be a file present named "tzupdater.jar"
  6. Open a command-line window and browse to the path where tzupdater.jar is located.
  7. Issue the following from the command-line - **PLEASE INCLUDE THE QUOTES:**
`"C:\Program Files\wfavvid\java\current\bin\java" -jar tzupdater.jar -u -v`
where "u" and "v" are both lower-case letters.
Again, this entire command is issued from a command-line window after browsing to the same folder as where "tzupdater.jar" is located.
  8. The output from the above command should be similar to:

```
java.home: C:\Program Files\wfavvid\java\current 
java.vendor: Sun Microsystems Inc. 
java.version: 1.4.2_15 
JRE time zone data version: tzdata200xx 
Embedded time zone data version: tzdata2007f 
Extracting files... done. 
Renaming directories... done. 
Validating the new time zone data... done. 
Time zone data update is complete.

```

  9. To verify the update was successful, issue this command:
`"C:\Program Files\wfavvid\java\current\bin\java" -jar tzupdater.jar -u`
and verify the returned text is
`You have the same version as the embedded one.`
Note the lack of a "-v" in the above command.
  10. Restart Unified CCX server.


If this update needs to be reversed for whatever reason, steps are provided in the README.html file mentioned earlier.
References:
Sun DST FAQ - <http://java.sun.com/developer/technicalArticles/Intl/USDST_Faq.html>
Sun TZupdater ReadMe - <http://java.sun.com/javase/tzupdater_README.html>
Sun download archive - <http://java.sun.com/products/archive/>
Sun TZupdater 1.3.1 ReadMe - <http://java.sun.com/j2se/1.3/tzupdater131/tzupdater131_README.html>  
|  Product  |  Version  |  Tested (Y/I*)  |  Components Tested (All Specific)  |  
| --- | --- | --- | --- |  
|  UCCX 3.5(4) with SR2  |  3.5(4)  |  Y  |  All  |  
|  UCCX 4.0(5/5a) with SR1  |  4.0(5/5a)  |  Y  |  All  |  
|  UCCX 4.1(1) with SR1  |  4.1(1)  |  Y  |  All  |  
|  UCCX 4.5(2)  |  4.5(2)  |  Y  |  All  |  
|  UCCX 5.0(1) with SR1  |  5.0(1)  |  Y  |  All  |  
* Testing Disposition
I - In Progress (indicating that testing is in progress and will be updated when complete)
Y - Yes (tested)
NA - Not Applicable (none of the security updates are being tested because of a "Not Applicable" or "Deferred" assessment.)
### DDTS
To follow the bug ID link below and see detailed bug information, you must be a [registered](https://tools.cisco.com/RPF/register/register.do) user and you must be logged in.  
|  DDTS  |  Description  |  
| --- | --- |  
|  [CSCsj75782](https://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj75782) ([registered](https://tools.cisco.com/RPF/register/register.do) customers only)  |  Update needed for CRS for New Zealand DST changes 2007  |  
|  [CSCsk15778](https://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk15778) ([registered](https://tools.cisco.com/RPF/register/register.do) customers only)  |  Current CRS time in RTR is not changing for NZ DST.  |  
|  [CSCsk08442](https://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk08442) ([registered](https://tools.cisco.com/RPF/register/register.do) customers only)  |  WFM Considerations for 2007 New Zealand Daylight Savings Time Change.  |  
|  [CSCsk08455](https://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk08455) ([registered](https://tools.cisco.com/RPF/register/register.do) customers only)  |  QM Considerations for 2007 New Zealand Daylight Savings Time Change  |  
|  [CSCsk08476](https://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk08476) ([registered](https://tools.cisco.com/RPF/register/register.do) customers only)  |  CAD/CSD Considerations for 2007 New Zealand Daylight Savings Time Change.  |  
|  [CSCsk08555](https://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsk08555) ([registered](https://tools.cisco.com/RPF/register/register.do) customers only)  |  EIM/WIM Considerations for 2007 New Zealand Daylight Savings Time Change  |  
|  [CSCsj56236](https://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj56236) ([registered](https://tools.cisco.com/RPF/register/register.do) customers only)  |  CallManager Update needed for New Zealand DST changes in 2007  |  
|  [CSCsj75858](https://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj75858) ([registered](https://tools.cisco.com/RPF/register/register.do) customers only)  |  Outbound does not handle new Daylight Savings Time dates for 2007 [New Zealand]  |  
|  [CSCsj56317](https://tools.cisco.com/Support/BugToolKit/search/getBugDetails.do?method=fetchBugDetails&bugId=CSCsj56317) ([registered](https://tools.cisco.com/RPF/register/register.do) customers only)  |  MCS-OS Update needed for New Zealand DST changes in 2007  |  
### Revision History  
|  Revision  |  Date  |  Comment  |  
| --- | --- | --- |  
|  1.1  |  20-SEP-2007  |  Under the Workaround/Solution section: Added OS version 2000-4-5a-sr2 (win-OS-Upgrade-K9-2000-4-5a-sr2.exe) Changed "JDK US DST Timezone Update Tool - 1.2.1" version to 1.2.2.  |  
|  1.0  |  04-SEP-2007  |  Initial Public Release  |  
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/warp/customer/687/Directory/DirTAC.shtml) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/create/)
  * [By email](https://www.cisco.com/warp/customer/687/Directory/DirTAC.shtml#email)
  * [By telephone](https://www.cisco.com/warp/customer/687/Directory/DirTAC.shtml#telephone)


### Receive Email Notification For New Field Notices
[Product Alert Tool](https://www.cisco.com/cgi-bin/Support/FieldNoticeTool/field-notice) - Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
* * *
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62880.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62880.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Contact Center Express](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/620/fn62880.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/620/fn62880.html)
