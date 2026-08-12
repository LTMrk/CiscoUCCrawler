  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64302.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64302.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64302.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64302.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64302.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Servers - Unified Computing](https://www.cisco.com/c/en/us/support/servers-unified-computing/category.html)
  * [Cisco UCS C-Series Rack Servers](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/products-field-notices-list.html)


# Field Notice: FN - 64302 - Select 7.2K RPM SAS LFF HDDs Might be Susceptible to Data Loss on Loss of Power - Workaround Provided
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/643/fn64302.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64302.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/643/fn64302.html)


Updated:May 21, 2018
Document ID:FN64302
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 10-Jul-17  | Initial Release  |  
| 10.0  | 11-Dec-17  | Migration to new field notice system  |  
| 10.1  | 21-May-18  | Fixed Broken Image Links  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
|  UCS-C3K-HD4TB=   |  Part Alternate   |  
|  UCS-C3K-HD4TB   |   |  
|  UCS-C3K-HD4TBRR=   |  Part Alternate   |  
|  UCS-C3K-HD4TBRR   |   |  
|  UCS-HD4T7KL12G=   |  Part Alternate   |  
|  UCS-HD2T7KL12G=   |  Part Alternate   |  
|  UCS-HD2T7KL12G   |   |  
|  UCS-HD4T7KL12G   |   |  
|  UCS-HD1T7KL12G   |   |  
|  UCS-HD1T7KL12G=   |  Part Alternate   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCve54383](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCve54383)  | Seagate MakaraBP1/2/4TB SAS Write Cache Mode Enable when delivering to Cisco  |  
### Problem Description
Select Serial Attached SCSI (SAS) 7.2K RPM Large Form Factor (LFF) drives had drive write cache enabled during manufacturing. If drive write cache is enabled during a power loss it can result in loss of data. This issue is limited to drives used on these platforms: - C220-M3/M4L - C240-M3/M4L - UCSC-C3X60
### Background
Cisco ships all of their hard drives from manufacturing with drive write cache disabled. During a quality audit, select units were found to have the drive write cache enabled. The issue has been remediated in the manufacturing process. Users of potentially affected devices are recommended to change the drive cache configuration.
### Problem Symptom
If a drive on one of the affected platforms has drive write cache enabled, and the cache is not flushed prior to power loss, data that still resides in the drive cache will be lost.
### Workaround/Solution
The solution is to disable write cache. Users will generally have two types of setups with their hard drives; just a bunch of disks (JBOD) and redundant array of independent disks (RAID). The procedure to change the drive write cache settings differs depending on the OS and which setup the drive is in. In order to use the correct tool, you will have to know which OS you have and which storage volume setup is configured. Refer to this table in order to see which tool you need to use.  
|   | JBOD  | RAID  |  
| --- | --- | --- |  
| ESX  | Bootable Linux ISO  | StorCLI  |  
| Linux  | SDPARM  | StorCLI  |  
| Windows  | Windows Disk Drive Policy  | StorCLI  |  
For users who have JBOD drives, see "Users Whose Drives are Configured as Hardware JBOD". For users who use a RAID set, see "Users Who Run Their Hard Drives in RAID.
### Users Whose Drives are Configured as Hardware JBOD
#### Users Who Run ESXi with JBOD Mode
Users who run ESXi in JBOD need to create a bootable Linux ISO image file with the SDPARM utility installed so that drive write cache can be disabled.
#### How to Change the Drive Write Cache Setting in Windows with JBOD Mode
Users can use the Windows Disk Drive Policy in order to change the drive write cache. Users who wish to use the Windows Disk Drive Policy should refer to [HOW TO: Manually Turn Disk Write Caching On or Off](https://support.microsoft.com/en-us/help/324805/how-to-manually-turn-disk-write-caching-on-or-off).
#### How to Change the Drive Write Cache Setting in Linux with JBOD Mode
  1. Run **sdparm /dev/sdx** in order to display information on a particular drive, where:  

     * sdx can be sda, sdb, sdc, and so on. In this example it is sdb.
     * This displays all SCSI mode pages and their settings.
     * In the previous example, the mode page you want to change is "Caching".
  2. Run **sdparm --get=WCE /dev/sdb** in order to get the write cache setting on /dev/sdb.  

The returned data is _WCE 1 [cha: y, def: 1, sav: 1],_ where:
     * WCE 1 means the "current" setting is write cache enabled.
     * cha: y means the write cache setting is changeable.
     * def: 1 means the "Default" setting is write cache enabled. This value cannot be modified.
     * sav: 1 means the "Saved" setting is write cache enabled.
  3. Run **sdparm -s WCE=0 --save /dev/sdb** in order to set the "Current" and "Saved" settings to Off (that is, write cache disabled).  

  4. Run **sdparm --get=WCE /dev/sdb** in order to get the write cache setting on device /dev/sdb.  

The returned data is _WCE 0 [cha: y, def: 1, sav: 0],_ where:
     * WCE 0 means the "Current" setting is write cache disabled.
     * cha: y means the write cache setting is changeable.
     * def: 1 means the "Default" setting is write cache enabled.
     * sav: 0 means the "Saved" setting is write cache disabled. At the next power up, the Saved setting will be loaded into the Current so write cache will still be disabled.


[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/643/fn64302_oq7v44.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/643/fn64302_oq7v44.jpg "Related image, diagram or screenshot.")
### Users Who Run Their Hard Drives in RAID
Users who run their hard drives in RAID need to [download StorCL](https://www.broadcom.com/support/download-search/?pg=&pf=&pn=&po=&pa=&dk=storcli). From the download page, choose **Management Software and Tools** , and look for "Latest MegaRAID Storcli". StorCLI can be used for all OSs in order to change the drive write cache for drives that are in a RAID set. This example shows the StorCLI command being used in Linux. Although the OSs are different, the StorCLI command should be the same or similar. From a command line, enter **storcli64 /cx/vx set pdcache=Off** where cx is "c" followed by the controller number and vx is "v" followed by the virtual drive number.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/643/fn64302_ori1hu.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/643/fn64302_ori1hu.jpg "Related image, diagram or screenshot.")
### How To Identify Affected Products
### How to Verify the Current Drive Write Cache Setting in Windows for Users Whose Hard Drives are Configured as Hardware JBOD
Users can check the drive cache settings by checking the settings at [ HOW TO: Manually Turn Disk Write Caching On or Off](https://support.microsoft.com/en-us/help/324805/how-to-manually-turn-disk-write-caching-on-or-off).
### How to Verify the Current Drive Write Cache Setting in Linux for Users Whose Hard Drives are Configured as Hardware JBOD
From a command prompt, enter **sdparm --get=WCE /dev/sdx** in order to get the write cache setting on device /dev/sdx where sdx is "sd" followed by the drive letter.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/643/fn64302_oqtty7.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/643/fn64302_oqtty7.jpg "Related image, diagram or screenshot.")
If the value returned is 1, the write cache is enabled. Refer to the Workaround/Solution section for steps to take in order to correct the situation.
### How to Verify the Current Drive Write Cache Setting in RAID
From a command prompt, enter **storcli64 /C0 show all | grep -C 5 PDC** in order to get the write cache settings on your virtual drives.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/643/fn64302_ori1bd.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/643/fn64302_ori1bd.jpg "Related image, diagram or screenshot.")
There are three possible settings for the drive cache. Look under the "PDC" column:
  * "enbl" which means the drive write cache is enabled.
  * "dflt" which means the drive write cache is enabled.
  * "dsbl" which means the drive write chache is disabled.


If the PDC value is not "dsbl", then write cache is enabled. Refer to the Workaround/Solution section for steps to take in order to correct the situation.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64302.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64302.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [UCS C220 M4 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c220-m4-rack-server/model.html)
  * [UCS C240 M4 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c240-m4-rack-server/model.html)
  * [UCS C3260 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c3260-rack-server/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/643/fn64302.html)
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
