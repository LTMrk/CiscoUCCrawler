  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn28275.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn28275.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn28275.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn28275.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn28275.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Contact Center](https://www.cisco.com/c/en/us/support/contact-center/category.html)
  * [Cisco Unified Contact Center Express](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-field-notices-list.html)


# Field Notice: *Expired* FN - 28275 - New Install of Cisco IP Contact Center (IPCC) Express or IP/IVR 3.1(2) Fails to Display The AppAdmin Screen on The New MCS Servers
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/200/fn28275.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn28275.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/200/fn28275.html)


Updated:January 14, 2004
Document ID:FN28275
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
  
[](http://www.cisco.com/warp/customer/tech_tips/index/fn.html)
### Revised April 28, 2008  
January 14, 2004
### NOTICE:
### THIS FIELD NOTICE HAS BEEN EXPIRED AND IS NO LONGER MAINTAINED OR UPDATED BY CISCO.
### THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE, WARRANTY OR SUPPORT. USE OF THE INFORMATION ON THIS FIELD NOTICE OR MATERIALS LINKED FROM THIS FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.
* * *
### Products Affected  
|  Product  |  Comments  |  
| --- | --- |  
|  IPCC Express and IP/IVR  |  New installations on the MCS-7835H-3000 or MCS-7825H-3000  |  
### Problem Description
New Install of Cisco IP Contact Center (IPCC) Express or IP/IVR on the new MCS servers, MCS-7835H-3000 or MCS-7825H-3000, fails to bring up the AppAdmin screen for the final steps in the installation.
### Background
Two new servers have been qualified for use with IPCC Express and IP/IVR. These servers are the MCS-7835H-3000 and the MCS-7825H-3000. When installing version 3.1(2) on these new servers, the AppAdmin screen does not get displayed for the final steps of the installation.
### Problem Symptoms
During the final stage of the installation, the AppAdmin screen should be displayed allowing the installer to complete the installation process. This does not occur. At the end of the installation, the installer will ask to reboot the server. After reboot, the AppAdmin page should display, but it does not. Users will see a plain screen without any icons and it will be in that state until rebooted.
### Workaround/Solution
The workaround documented in the DDTS is to either log off and back on or to reboot the server. This will launch the AppAdmin screen, allowing the installation to proceed.
### DDTS
To follow the bug ID link below and see detailed bug information, you must be a [registered](http://tools.cisco.com/RPF/register/register.do) user and you must be logged in.  
|  DDTS  |  Description  |  
| --- | --- |  
|  [CSCed25174](http://www.cisco.com/cgi-bin/Support/Bugtool/onebug.pl?bugid=CSCed25174) ([registered](http://tools.cisco.com/RPF/register/register.do) customers only)  |  Cannot bring up appadmin page after installation  |  
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/warp/customer/687/Directory/DirTAC.shtml) by one of the following methods:
  * [Open a service request on Cisco.com](http://tools.cisco.com/ServiceRequestTool/create/)
  * [By email](http://www.cisco.com/warp/customer/687/Directory/DirTAC.shtml#email)
  * [By telephone](http://www.cisco.com/warp/customer/687/Directory/DirTAC.shtml#telephone)


### Receive Email Notification For New Field Notices
[Product Alert Tool](http://www.cisco.com/cgi-bin/Support/FieldNoticeTool/field-notice) - Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
* * *
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn28275.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn28275.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Unified Contact Center Express](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/200/fn28275.html)
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
