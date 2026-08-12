  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74118.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74118.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74118.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74118.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74118.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Routers](https://www.cisco.com/c/en/us/support/routers/category.html)
  * [Cisco 4000 Series Integrated Services Routers](https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/products-field-notices-list.html)


# Field Notice: FN74118 - Some PWR-CC1-500WAC Power Supplies May Show Incorrect Power Readings in Cisco IOS XE Software, Resulting in Incorrect Fan Speed Control - Hardware Upgrade Available
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/741/fn74118.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74118.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/741/fn74118.html)


Updated:May 1, 2024
Document ID:FN74118
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Product Name  | Description  | Comments  |  
| --- | --- | --- |  
| PWR-CC1-500WAC  | Cisco C8300 1RU AC Power supply with PoE  |   |  
  
  

  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwi62291](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwi62291)  | PWR-CC1-500WAC has incorrect power reading and may overheat  |  
  

### Problem Description
  

On affected Cisco C8300-1N1S-6T and Cisco C8300-1N1S-4T2X Routers, incorrect power readings are reported in Cisco IOS XE Software, resulting in incorrect fan speed control of the power supply. For affected routers that are running in nonredundant power supply mode, the power supply may eventually overheat and cause the router to shut down.
  

### Background
  

Affected routers contain power supplies that were manufactured with incorrect calibration of the current sensing circuitry. This problem only affects the 500-watt power supply with product identifier (PID) PWR-CC1-500WAC. Affected power supplies report incorrect power readings to the operating system software and can cause the software to set the cooling fan speed incorrectly.
  

### Problem Symptom
  

Affected Cisco C8300-1N1S-6T and Cisco C8300-1N1S-4T2X Routers with incorrectly calibrated power supplies will report incorrect power values in Cisco IOS XE Software. Power values can be observed by entering the **show environment | incl Watts** CLI command.
In the example below, the output power is listed as 3W and 6W, respectively; this is incorrect and abnormal.
> 
```
Router#show environment | incl Watts  
> 
P0          P: In pwr       Normal          30    Watts     na  
> 
**P0          P: Out pwr      Normal          3     Watts     na**  
> 
P1          P: In pwr       Normal          42    Watts     na  
> 
**P1          P: Out pwr      Normal          6     Watts     na**  
> 
P2          P: pwr          Normal          2     Watts     na  
> 
R0          P: pwr          Normal          43    Watts     na
```

In certain router configurations, it has been observed that due to the incorrect power reading in the power supply unit (PSU), the cooling of the PSU can be compromised so that when it is running in nonredundant power supply mode (one PSU is unpowered), the PSU may overheat, resulting in the system shutting down.
  

### Workaround/Solution
  

If a power supply is confirmed to be affected using the Serial Number Validation Tool, request a replacement.
  

### How to Identify Affected Products
  

In order to verify if your product is affected by this issue, use the [Cisco Support Assistant (CSA)](https://cs.co/FNSNV) to validate the serial number for your device(s). The serial number for the affected device(s) should be included in the form in this field notice.
Serial numbers of the affected power supplies will have the first nine characters _DCI2441T0_ or _DCI2507T0_. If the first 9 characters do not match one of these, then the PSU is not affected. If the first 9 characters do match one of these, then use the Serial Number Validation Tool to confirm whether the PSU is affected.
**Add show inventory command:**
> 
```
sh inventory  
> 
  
> 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
> 
INFO: Please use "show license UDI" to get serial number for licensing.  
> 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  
> 
  
> 
NAME: "Chassis", DESCR: "Cisco C8300-1N1S-6T Chassis"  
> 
PID: C8300-1N1S-6T     , VID: V01  , SN: FDO2530M03Z  
> 
  
> 
**NAME: "Power Supply Module 0", DESCR: "500W AC with POE for Cisco C8300 1RU"  
> 
PID: PWR-CC1-500WAC    , VID: V01  , SN: DCI2507T0P5**  
> 
  
> 
**NAME: "Power Supply Module 1", DESCR: "500W AC with POE for Cisco C8300 1RU"  
> 
PID: PWR-CC1-500WAC    , VID: V01  , SN: DCI2507T0P9**  
> 
  
> 
NAME: "Fan Tray", DESCR: "Cisco C8300 1RU Fan Assembly"  
> 
PID: C8300-FAN-1R      , VID:      , SN:          
```

  

### Serial Number Validation
  

The Cisco Support Assistant (CSA) can help verify whether a device is impacted by the issue that is described in this Field Notice. To check the device, either enter the serial number in the CSA on the right side of this page or click the following URL: <https://cs.co/FNSNV>.
### Upgrade Program Information
  

Support Case Manager (SCM) must be used for ordering replacement parts for this Field Notice. To open SCM in a new tab, click the following link:   
[ https://mycase.cloudapps.cisco.com/fieldnotice?fn=FN74118](https://mycase.cloudapps.cisco.com/fieldnotice?fn=FN74118)
SCM will validate eligibility and ensure that a request for a particular serial number has not already been submitted. If there is already a request, SCM will indicate **RMA already submitted and NOT eligible for replacement.**
Provide the following information: 
  1. Affected serial numbers. Note that a serial number entitlement check may be performed. 
  2. One ship-to address per request.
  3. Service Request number (SR#). This is not required, but if one exists, enter it for better tracking purposes.


Order entry supports up to 50 serial numbers per request. For more than 50, submit additional requests. 
### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.0  | Initial Release  | —  | 2024-MAY-01  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74118.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Customers Also Viewed
  * [Hardware Installation Guide for Cisco 4000 Series Integrated Services Routers --- Overview of the Cisco 4000 Series ISRs](https://www.cisco.com/c/en/us/td/docs/routers/access/4400/hardware/installation/guide4400-4300/C4400_isr/Overview.html)
  * [Hardware Installation Guide for Cisco 4000 Series Integrated Services Routers --- Install and Upgrade Internal Modules and FRUs](https://www.cisco.com/c/en/us/td/docs/routers/access/4400/hardware/installation/guide4400-4300/C4400_isr/FRUs_Modules.html)
  * [Implement Performance License for Integrated Service Router 4000](https://www.cisco.com/c/en/us/support/docs/routers/4000-series-integrated-services-routers/217135-performance-license-on-cisco-isr4000.html)
  * [Cisco 4000 Series ISRs Software Configuration Guide, Cisco IOS XE Gibraltar 16.12.x --- Installing the Software](https://www.cisco.com/c/en/us/td/docs/routers/access/4400/software/configuration/xe-16-12/isr4400swcfg-xe-16-12-book/installing_the_software.html)
  * + Show 1 More


### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74118.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [4431 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4441-x-integrated-services-router-isr/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/741/fn74118.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74118.html)
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
