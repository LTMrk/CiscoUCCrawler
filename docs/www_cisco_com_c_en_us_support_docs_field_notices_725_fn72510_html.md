  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72510.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72510.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72510.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72510.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72510.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Switches](https://www.cisco.com/c/en/us/support/switches/category.html)
  * [Cisco Catalyst 9200 Series Switches](https://www.cisco.com/c/en/us/support/switches/catalyst-9200-r-series-switches/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/switches/catalyst-9200-r-series-switches/products-field-notices-list.html)


# Field Notice: FN72510 - Cisco IOS XE Software: Weak Cryptographic Algorithms Are Not Allowed by Default for IPsec Configuration in Certain Cisco IOS XE Software Releases - Configuration Change Recommended
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/725/fn72510.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72510.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/725/fn72510.html)


Updated:January 20, 2026
Document ID:FN72510
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Medium
**Impact Rating:**
Medium
**First Published:**
2023-Mar-07
**Last Published:**
2026-Jan-20
**Revision:**
1.5
**Cisco Bug IDs:**
  * [CSCwc72588](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwc72588)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| IOS XE Software  | 17  | 17.11.1, 17.11.1a, 17.12.1, 17.13.1, 17.14.1, 17.15.1  |   |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwc72588](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwc72588)  | Router should not allow weak cryptographic algorithms to be configured for IPsec  |  
  

### Problem Description
  

In releases earlier than the Cisco IOS XE Software releases that are listed in the table in the Workaround/Solution section of this field notice, weak crypto algorithms, including integrity, encryption, and Diffie-Hellman group algorithms, can be configured for IPsec protocol negotiation as well as data plane traffic protection.
In the Cisco IOS XE Software releases that are listed in the table in the Workaround/Solution section of this field notice, weak crypto algorithms are no longer allowed by default due to their weak cryptographic properties. Cisco strongly recommends the use of stronger cryptographic algorithms in their place. To continue to use such weak algorithms, explicit configuration is required. Otherwise, **IPsec tunnel negotiation will fail and cause service disruption as a result.**
The following table lists the IPsec configuration components and algorithms that are affected by this change:  
| IPsec Configuration  | Command  | Keyword Deprecated  |  
| --- | --- | --- |  
| IKEv1 Policy  | crypto isakmp policy priority  | encryption {des | 3des}  
hash md5  
group {1 | 2 | 5}  |  
| IKEv2 Proposal  | crypto ikev2 proposal name  | encryption {des | 3des}  
integrity md5  
group {1 | 2 | 5 | 24}  |  
| IPsec Transform-set  | crypto ipsec transform-set name  | ah-md5-hmac  
esp-gmac  
esp-des  
esp-3des  
esp-null  
esp-md5-hmac  |  
| IPsec Profile  | crypto ipsec profile name  | set pfs {group1 | group2 | group5 | group24}  |  
| Crypto Map  | crypto map name  | set pfs {group1 | group2 | group5 | group24}  |  
  

### Background
  

In Cisco IOS XE Software releases Benaluru 17.6.1 and later, configuration of the IPsec protocol with a weak crypto algorithm generates a warning as shown in this example:
> 
```
Device(config)#**crypto isakmp policy 10**  
>   
> Device(config-isakmp)#**encryption des**  
>   
> %Warning: weaker encryption algorithm is deprecated
```

However, the command is accepted and the weak algorithm can still be used for protocol negotiation for IPsec.
In the Cisco IOS XE Software releases that are listed in the table in the Workaround/Solution section of this field notice, such weak crypto algorithms will be rejected by default and require explicit configuration to be allowed.
  

### Problem Symptom
  

If the IPsec configuration is not updated to use strong cryptographic algorithms before upgrading to one of the Cisco IOS XE Software releases that is listed in the table in the Workaround/Solution section of this field notice, IPsec tunnel negotiation will fail, resulting in service disruption.
  

### Workaround/Solution
  

**Solution (Recommended)**
Update the configuration to use strong cryptographic algorithms for IPsec.
**Workaround (Not Recommended)**
Enter the following configuration command for IPsec to continue to function with the weak algorithms after upgrading to one of the Cisco IOS XE Software releases that is listed in the table below:
> 
```
Device(config)#**crypto engine compliance shield disable**
```

**Note:** This command is only available in Cisco IOS XE Software releases 17.7.1 and later and will only take effect after a reboot. Cisco does **not** recommend this option as these weak cryptographic algorithms are insecure and do not provide adequate protection from modern threats. This command should only be used as a last resort.  
| Technology  | Cisco Product  | Affected Cisco IOS XE Software Release  |  
| --- | --- | --- |  
| Enterprise Routing  | ASR1000 series  
ISR4000 series  
ISR1100 series  
Catalyst 8000 series  | 17.11.1a and later  |  
| Wireless  | Catalyst 9800 Series Wireless Controller  
Catalyst CG418-E Cellular Gateway  
Catalyst CG522-E Cellular Gateway  
Catalyst 9115AX Access Points (APs)  
Catalyst 9117AX APs  
Catalyst 9120AX APs  
Catalyst 9130AX APs  | 17.13.1 and later  |  
| SP Access  | ASR920  
ASR903  
NCS520  
NCS4200  | 17.12.1 and later  |  
| Switching  | Catalyst 9200 Series  
Catalyst 9300 Series  
Catalyst 9400 Series  
Catalyst 9500 Series  | 17.15.1 and later  |  
| IoT Routing  | IR1101  
IR8140H  
IR1800 Series  
IR8340  
ESR6300  | 17.14.1 and later  |  
  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.5  | Added crypto map IPsec configuration to table.  | Problem Description  | 2026-JAN-20  |  
| 1.4  | Updated affected releases.  | Problem Description, Background, Problem Symptom, Workaround/Solution  | 2024-JAN-10  |  
| 1.3  | Updated the table in Problem Description to include group 24 under IKEv2 Proposal.  | Problem Description  | 2023-NOV-21  |  
| 1.2  | Updated the Problem Description and Problem Symptom Sections.  | —  | 2023-APR-10  |  
| 1.1  | Updated the Workaround/Solution Section.  | —  | 2023-MAR-15  |  
| 1.0  | Initial Release  | —  | 2023-MAR-07  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72510.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72510.html)
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
  * [CSR 1000V Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/csr-1000v-series-ios-xe-sd-wan/model.html)
  * [Catalyst 8000V Edge Software](https://www.cisco.com/c/en/us/support/routers/catalyst-8000v-edge-software/series.html)
  * [Catalyst 9606R Switch](https://www.cisco.com/c/en/us/support/switches/catalyst-9606-switch/model.html)
  * [ESR6300 Embedded Series Router](https://www.cisco.com/c/en/us/support/routers/6300-embedded-service-router/model.html)
  * [ISR 1000 Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/isr-1000-series-ios-xe-sd-wan/model.html)
  * [ISR 4000 Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/isr-4000-series-ios-xe-sd-wan/model.html)
  * [Integrated Services Virtual Router](https://www.cisco.com/c/en/us/support/routers/integrated-services-virtual-router/series.html)
  * [Network Convergence System 520](https://www.cisco.com/c/en/us/support/routers/network-convergence-system-520-router/model.html)

+ Show All 16 Products
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72510.html)
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
