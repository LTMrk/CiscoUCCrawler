  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72265.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72265.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72265.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72265.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72265.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Routers](https://www.cisco.com/c/en/us/support/routers/category.html)
  * [Cisco XE SD-WAN Routers](https://www.cisco.com/c/en/us/support/routers/xe-sd-wan-routers/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/routers/xe-sd-wan-routers/products-field-notices-list.html)


# Field Notice: FN - 72265 - Expired PKI Certificate on vEdge, ISR, and ASR Routers Causes SD-WAN Umbrella DNS Connections to Fail - Software Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/722/fn72265.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72265.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/722/fn72265.html)


Updated:November 23, 2021
Document ID:FN72265
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 08-Nov-21  | Initial Release  |  
| 1.1  | 22-Nov-21  | Updated the Workaround/Solution Section  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | IOSXE  | 17  | 17.3.1, 17.3.1a, 17.3.1w, 17.3.1x, 17.3.2, 17.3.2a, 17.3.3, 17.3.3a, 17.3.4, 17.3.4a, 17.4.1, 17.4.1a, 17.4.1b, 17.4.2, 17.5.1, 17.5.1a, 17.6.1, 17.6.1a  | Cisco SD-WAN "controller mode" only  |  
| NON-IOS  | vEdge Software  | 20  | 20.3.1, 20.3.2, 20.3.3, 20.3.4, 20.4.1.1, 20.4.1.2, 20.4.2, 20.5.1, 20.6.1  |   |  
| NON-IOS  | IOSXE  | 16  | 16.10.1, 16.10.1a, 16.10.1b, 16.10.1c, 16.10.1d, 16.10.1e, 16.10.1f, 16.10.1g, 16.10.1i, 16.10.1s, 16.10.2, 16.10.3, 16.11.1, 16.11.1a, 16.11.1b, 16.11.1c, 16.11.1s, 16.11.2, 16.12.1, 16.12.1a, 16.12.1c, 16.12.1s, 16.12.1t, 16.12.1w, 16.12.1x, 16.12.1y, 16.12.1z, 16.12.1z1, 16.12.1z2, 16.12.2, 16.12.2a, 16.12.2s, 16.12.2t, 16.12.3, 16.12.3a, 16.12.3s, 16.12.4, 16.12.4a, 16.12.5, 16.12.5a, 16.12.5b, 16.12.6  | Cisco SD-WAN images only  |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCvz86967](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvz86967)  | DST Root CA X3 Expiration causing umbrella integration to fail  |  
| [CSCvz86972](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvz86972)  | cEdge DST Root CA X3 Expiration causing umbrella integration to fail  |  
### Problem Description
The public key infrastructure (PKI) certificate used by Cisco SD-WAN routers to register with Cisco Umbrella Domain Name System (DNS) expired on 2021-09-30. Cisco SD-WAN routers with the expired PKI certificate fail to register with the Umbrella DNS service. The result of this failure is that all subsequent client DNS requests are dropped.
### Background
This problem affects Cisco vEdge router products as well as Cisco IOS® XE routers that run in SD-WAN Controller mode. Affected router series include Cisco Integrated Services Router (ISR), Cisco Aggregation Services Router (ASR), the Cisco CSR 1000v Cloud Services Router, the Cisco Integrated Services Virtual Router (ISRV), and Cisco Catalyst 8000v Edge Software. Affected products include a PKI certificate based on the DST Root CA X3 trust anchor. This certificate is used to establish a secure connection between a Cisco SD-WAN router and Cisco Umbrella DNS on routers that are configured to use Cisco Umbrella as their DNS service. The DST Root CA X3 certificate expired on 2021-09-30 and does not auto-renew. Once the certificate expires, all subsequent secure DNS registration requests between the SD-WAN router and Cisco Umbrella fail.
For additional background information, see [DST Root CA X3 Expiration (September 2021)](https://letsencrypt.org/docs/dst-root-ca-x3-expiration-september-2021/).
### Problem Symptom
Affected devices fail to establish secure connections with the Umbrella DNS service and DNS registration fails. Once registration fails, no DNS capability is available on Cisco IOS XE SD-WAN routers and all DNS requests from clients fail. On Cisco vEdge routers, DNS requests will be forwarded instead of redirected to the secure Umbrella DNS service. Without an available DNS service, client devices will experience a variety of network reachability failures such as web sites unavailable, cloud services unavailable, and so on.
Affected devices that are already in operation and part of an overlay will not immediately experience DNS related failures. The expired certificate is only used during device registration with the Cisco Umbrella DNS service, not for individual DNS requests. Device registration occurs when the Cisco Umbrella DNS service is initially configured or when the device is rebooted with an existing Cisco Umbrella DNS configuration present.
This problem only affects Cisco SD-WAN routers configured for Umbrella DNS. Cisco routers that run in Cisco IOS XE Autonomous mode are not affected. Cisco IOS XE devices that run in Autonomous mode use a different PKI certificate for Umbrella DNS. That certificate is not affected. Also, this problem does not affect devices configured for Cisco Umbrella Secure Internet Gateway (SIG) tunnel.
### Workaround/Solution
There is no workaround. Affected devices must have the expired DST Root CA X3 certificate replaced with a new unexpired certificate rooted in ISRG Root X1. Customers who do not currently use Cisco Umbrella DNS, but expect to deploy it in the future, can replace the expired certificate by upgrading the SD-WAN router software to a version that contains the new certificate. The new certificate is installed automatically during the upgrade. Software releases that contain the new certificate are expected to become available in December 2021.
Customers with affected routers already configured for Cisco Umbrella DNS can replace the expired certificates by copying a new ISRG Root X1 rooted certificate to each affected router. Follow these instructions in order to replace the certificate.
**Cisco IOS XE Routers That Run in Controller Mode**
  1. Download the new unexpired certificate from this web site and place it on a device that has access to the affected routers in the SD-WAN overlay. 
```
https://letsencrypt.org/certs/isrg-root-x1-cross-signed.pem
```

  2. Enter the Linux `**scp**`command or similar mechanism in order to perform a secure file copy from the download device onto each affected router. For example:
```
**scp ./isrg-root-x1-cross-signed.pem admin@<_EdgeIP_>:bootflash:trustidrootx3_ca.ca**
```

Substitute <_EdgeIP_ > with the IP address of the affected router.
  3. Once the file copy completes, reload the router in order to complete the installation process.


Alternately, the new ISRG Root X1 rooted certificate can be downloaded to Cisco vMange and copied to each affected router. It is not possible to copy the new certificate directly into the router's bootflash with this method. Instead, the new certificate must be copied into a temporary directory first and then copied into the final bootflash location while logged into the router.
  1. Log into vManage and access vshell. 
```
vManage# **vshell**
vManage:~$ pwd
/home/admin
```

  2. Download the new unexpired certificate from the letsencrypt.org web site. 
```
**wget https://letsencrypt.org/certs/isrg-root-x1-cross-signed.pem --no-check-certificate**
```

  3. Enter the Linux `**scp**`command in order to perform a secure file copy from vManage into a temporary location on each affected router. For example:
```
**scp -P 830 isrg-root-x1-cross-signed.pem admin@<_EdgeIP_>:/bootflash/sdwan/trustidrootx3_ca.ca**
```

Substitute <_EdgeIP_ > with the IP address of the affected router.
  4. Log into the affected router.
  5. Enter the `**copy**`CLI command in order to copy the new certificate from the temporary location into bootflash.

```
router# **copy bootflash:/sdwan/trustidrootx3_ca.ca bootflash:**
Destination filename [trustidrootx3_ca.ca]?
```

  6. Enter the `**delete**`CLI command in order to remove the certificate file from the temporary location.

```
router# **delete bootflash:/sdwan/trustidrootx3_ca.ca**
```

  7. Reload the router in order to complete the certificate installation process.


**Cisco vEdge Routers**
Cisco vEdge routers require authorized root access in order to replace the certificate. The access procedure requires Cisco Technical Assistance Center (TAC) intervention. Customers with affected Cisco vEdge routers should contact the Cisco TAC for assistance with the expired certificate.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72265.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72265.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [4221 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4221-integrated-services-router-isr/model.html)
  * [4321 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4321-integrated-services-router/model.html)
  * [4331 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4331-integrated-services-router-isr/model.html)
  * [4351 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4351-integrated-services-router/model.html)
  * [4431 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4441-x-integrated-services-router-isr/model.html)
  * [4451-X Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4451-x-integrated-services-router-isr/model.html)
  * [4461 Integrated Services Router](https://www.cisco.com/c/en/us/support/routers/4461-integrated-services-router/model.html)
  * [ASR 1000 Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/asr-1000-series-ios-xe-sd-wan/model.html)
  * [ISR 1000 Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/isr-1000-series-ios-xe-sd-wan/model.html)
  * [ISR 4000 Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/isr-4000-series-ios-xe-sd-wan/model.html)

+ Show All 10 Products
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/722/fn72265.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/722/fn72265.html)
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
