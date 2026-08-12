  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70037.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70037.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70037.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70037.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70037.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-field-notices-list.html)


# Field Notice: FN - 70037 - Enterprise Chat & Email (ECE) 11.5(1) Installer Intermittently Fails with Error Message - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/700/fn70037.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70037.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/700/fn70037.html)


Updated:December 20, 2017
Document ID:FN70037
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 19-Dec-17  | Initial Release  |  
### Products Affected  
| Affected OS Type  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| NON-IOS  | 11  | 11.5(1)  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCve61410](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCve61410)  | ECE 11.5 install fails at Blueboard  |  
### Problem Description
Customers who upgrade from E-Mail Interaction Manager (EIM) / Web Interaction Manager (WIM) to Enterprise Chat & Email (ECE) or install ECE Release 11.5(1) might encounter Cisco bug ID [CSCve61410](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCve61410) in the upgrade process.
### Background
Java 8 uses Transport Layer Security (TLS) v1.2 (the highest level protocol available on the host machine) in order to negotiate with the database server. Since the Java Database Connectivity (JDBC) driver used in the 11.5(1) installer contains an older sqljdbc4 file, there is a 5-10% chance that customers might encounter this symptom. This file is ONLY used in the installation process and does not affect or impact operations of production systems.
### Problem Symptom
In the installation process, the installer might intermittently fail to establish a connection to the Structured Query Language (SQL) server. The 11.5(1) installer (and installer ONLY, this is not applicable for post-install production) uses a slightly older JDBC driver in order to establish a secure connection to a SQL server that uses Secure Sockets Layer (SSL) encryption. ECE Release 11.5(1) installs Java 8 which uses TLSv1.2 in order to negotiate the connection to the database server and because the JDBC driver contains a slightly older sqljdbc4 file, there is a 5% - 10% chance that customers might encounter this symptom.
**Detection**
If you are impacted by this defect, one of these issues might occur:
  * In most cases, the installer freezes at a particular panel/splash screen.
  * The installer prompts a generic error message.


If you encounter either of those issues, investigate the upgrade_installer logs located in one of these locations and look for the trace message.
**Locations of Installer Logs**
If the file server is already installed:  
Cisco_Home\eService\installation\logs\eg_log_Server_Name_eGainInstaller.log
If it is a new installation:  
C:\Users\Your_Username\AppData\Local\Temp\egain_installer_Server_Name.log
**Trace Message**
The driver could not establish a secure connection to SQL Server by using SSL encryption. Error: "SQL Server returned an incomplete response. The connection has been closed.". <@>  
com.microsoft.sqlserver.jdbc.SQLServerException: The driver could not establish a secure connection to SQL Server by using Secure Sockets Layer (SSL) encryption. Error: "SQL Server returned an incomplete response. The connection has been closed.".  
at com.microsoft.sqlserver.jdbc.SQLServerConnection.terminate(SQLServerConnection.java:1352)  
at com.microsoft.sqlserver.jdbc.TDSChannel.enableSSL(IOBuffer.java:1533)  
at com.microsoft.sqlserver.jdbc.SQLServerConnection.connectHelper(SQLServerConnection.java:1042)
Once you confirm the issue, follow the workaround steps in the next section in order to resolve the issue.
### Workaround/Solution
In order to add a Java Virtual Machine (JVM) parameter (Djdk.tls.client.protocols=TLSv1) to manually force Java 8 to use TLSv1 in the install/upgrade process, complete these steps:
  1. Do not proceed with the install, but simply keep the installer up and running until you proceed to step 7.
  2. Open a Microsoft Windows temp folder. (Click **Start**. In the Search field, enter **Run**. In the Open field, enter **%temp%**.)  
When you run the installer again as instructed in step 1, a new folder is created in the Windows temp folder which is the extract of the installer. (The folder in the Windows temp folder is created dynamically with a name that starts with capital letter I. For example, I1483955861.)
  3. Copy the temp folder (for example, I1483955861) from the Windows temp folder location to the Desktop and stop the installer.
  4. From the folder copied to the Desktop, open the setup.lax file via any text editor such as Notepad or TextPad (for example, \Desktop\I1483955861\Windows\setup.lax).
  5. In order to modify the property named lax.nl.java.option.additional, append the parameter -Djdk.tls.client.protocols=TLSv1 to it. For example, if the property is:  
  
lax.nl.java.option.additional=-XX:MaxPermSize=256M -Xss192K  
  
change it to  
  
lax.nl.java.option.additional=-XX:MaxPermSize=256M -Xss192K -Djdk.tls.client.protocols=TLSv1
  6. Save the updated setup.lax file.
  7. Cancel the installation.
  8. Copy the updated folder from the Desktop location to the temp folder in the Windows location (replace the existing folder).
  9. From the Windows temp folder, open the updated folder (per the example, I1483955861)\Windows. Right-click the setup.exe file and click **Run** as the administrator.


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70037.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70037.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/700/fn70037.html)
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
