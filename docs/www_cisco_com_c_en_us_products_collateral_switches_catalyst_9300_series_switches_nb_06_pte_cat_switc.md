  * [Skip to content](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9300-series-switches/nb-06-pte-cat-switches-faq-cte-en.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9300-series-switches/nb-06-pte-cat-switches-faq-cte-en.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9300-series-switches/nb-06-pte-cat-switches-faq-cte-en.html)


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


  * [](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9300-series-switches/nb-06-pte-cat-switches-faq-cte-en.html)
  * [...](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9300-series-switches/nb-06-pte-cat-switches-faq-cte-en.html)Show All Breadcrumbs
  * [Products & Services](https://www.cisco.com/c/en/us/products/index.html)
  * [Switches](https://www.cisco.com/c/en/us/products/switches/index.html)
  * [Campus LAN Switches - Access](https://www.cisco.com/c/en/us/products/switches/campus-lan-switches-access/index.html)
  * [Cisco Catalyst 9300 Series Switches](https://www.cisco.com/c/en/us/products/switches/catalyst-9300-series-switches/index.html)
  * [Q&A](https://www.cisco.com/c/en/us/products/switches/catalyst-9300-series-switches/q-and-a-listing.html)


# Support for Precision Time Protocol on Cisco Catalyst Switches FAQ
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/products/collateral/switches/catalyst-9300-series-switches/nb-06-pte-cat-switches-faq-cte-en.html) to Save Content 
Download
Print
### Available Languages
### Download Options
  * [PDF](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9300-series-switches/nb-06-pte-cat-switches-faq-cte-en.pdf) (104.0 KB)   
View with Adobe Reader on a variety of devices


Updated:April 6, 2023
Document ID:1649451346008948
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Q.What is Precision Time Protocol (PTP)?
A.PTP is a high-precision distributed time synchronization protocol that is used to synchronize clocks across an Ethernet network. 
Q.What are the benefits of enabling PTP? 
A.PTP uses hardware stamping capability to provide accurate clock synchronization on the order of microseconds, sub-microseconds, and even nanoseconds. 
Q.What platforms in the Cisco ® Catalyst ® 9000 portfolio support PTP? 
A.PTP is supported on the following platforms in the Catalyst 9000 switching portfolio: 
●Catalyst 9300 Series platforms
●Catalyst 9400 Series platforms
●Catalyst 9500 Series platforms 
●Catalyst 9600 Series platforms 
Q.Are there any limitations on the uplink or downlink ports? 
A.The limitation on the downlink ports is for Catalyst 9300-48UXM and 9300-48UN models. PTP is supported on ports 1 to 16 for 9300-48UXM model and ports 1 to 36 for the 9300-48UN model. On Catalyst 9400, PTP is not supported on Supervisor ports. 
Q.What is the first software version that supports PTP on the Cisco Catalyst 9000 switch platforms? 
A.Table 1 lists the software versions that provided initial support for PTP. 
**Table 1.** Support for PTP in Cisco IOS XE releases  
|   |  Platform  |  Release  |  
| --- | --- | --- |  
|  **Catalyst 9300 Series**  |  All Models  |  Cisco IOS® XE 16.8.1a   |  
|  **Catalyst 9400 Series**  |  SUP-1/1XL/1XL-Y  |  17.6.1  |  
|  **Catalyst 9500 Series**  |  C9500-24Q/  
C9500-12Q/  
C9500-40X/  
C9500-16X  |  Cisco IOS XE 16.8.1a   |  
|   |  C9500-24Y4C/  
C9500-48Y4C  
C9500-32QC/  
C9500-32C  |  Cisco IOS XE 16.12.1   |  
|  **Catalyst 9600 Series**  |  With SUP-1  |  17.6.1  |  
Q.What is the license level needed to enable PTP on the Catalyst 9000 switch platforms? 
A.Network Advantage is needed to enable PTP on the Catalyst 9000 switch platforms. 
Q.What PTP profiles are supported on the Catalyst 9000 switch platforms? 
A.The PTP default profile (IEEE 1588v2), IEEE 802.1AS (gPTP) profile, 8275.1 profile and AES67 profiles are supported. 
Q.Do the Catalyst 9000 switch platforms support one-step or two-step message exchange? 
A.The switches support two-step message exchange only. One-step message exchange is not supported on the Catalyst 9000 switch platforms. 
Q.Do the Catalyst 9000 switch platforms support PTP multicast or unicast messaging? 
A.The switches support multicast messaging. 
Q.How many PTP domains are supported? 
A.The Catalyst 9000 switch platforms support one PTP domain. The domain ID is configurable. 
Q.Do the Catalyst 9000 switch platforms support PTP versions 1 and 2? 
A.The switches support PTP version 2 as per the requirements in IEEE 1588v2. They do not support PTP version 1. 
Q.Can the Catalyst 9000 switch platforms transparently transit PTP version 1 packets? 
A.Yes, the switches can transit PTP version 1 packets transparently. 
Q.Do the Catalyst 9000 switch platforms support Layer 2 and Layer 3 PTP? 
A.Yes, the switches support both Layer 2 and Layer 3 PTP. 
Q.Is PTP supported when 9300 Series switches are stacked (Cisco StackWise ® 1T/480/320)? 
A.Yes, PTP is supported when 9300 Series switches are deployed in StackWise 1T/480/320 starting 17.6.1. 
Q.Is PTP supported in StackWise Virtual environments? 
A.Yes, PTP is supported in StackWise Virtual environments starting 17.10.1. 
Q.Is PTP supported on EtherChannels? 
A.Yes, PTP is supported on EtherChannels beginning with Cisco IOS XE Release 17.2.1. 
Q.What clock modes are supported on the Catalyst 9000 switch platforms? 
A.The switches can support transparent and boundary clock modes. 
Q.Do the Catalyst 9000 switch platforms support clock synchronization across VLANs in PTP transparent mode? 
A.No, the switches do not support clock synchronization across VLANs in PTP transparent mode. Boundary clock mode can be used for inter-VLAN clock synchronization. 
Q.Do the Catalyst 9000 switch platforms forward PTP packets by default without enabling PTP on the switch? 
A.Yes, the switches forward PTP packets transparently by default. 
Q.Can we have non-PTP-enabled switches in the PTP network? 
A.Yes, it is possible to have non-PTP-enabled switches in the PTP network. This is not recommended, however, as it will decrease the accuracy of the clock synchronization. 
Q.Can we switch from one PTP mode to another? 
A.Yes, you can switch from one PTP mode to another PTP mode. It is recommended that you first clear the current PTP mode using “no PTP mode” and then configure the desired PTP mode. 
Q.Can PTP be enabled on native Layer 3 interfaces? 
A.Yes, you can enable PTP on a Layer 3 native port as well as a Layer 3 EtherChannel. 
Q.Can we enable multiple profiles (Eg: Default and 802.1AS) at the same time? 
A.No, you cannot enable two profiles at the same time. They are mutually exclusive, and only one can be enabled at a time. 
Q.Do the Catalyst 9000 switch platforms support management and signaling messages? 
A.Signaling messages are dropped. The boundary hop count is decremented for management messages, and they are forwarded without any processing, as per the requirements in IEEE 1588v2. 
Q.What peer delay mechanisms do the Catalyst 9000 switch platforms support? 
A.The switches support end-to-end and peer-to-peer delay mechanisms. 
Q.Can Catalyst 9000 switch platforms transport Dante traffic? 
A.Yes, the switches can transport Dante traffic transparently. 
Q.What is the expected accuracy of PTP on the Catalyst 9000 switch platforms? 
A.Accuracy of less than 100 nanoseconds can be expected. 
Q.Is PTP over Cisco Software-Defined Access (SD-Access) fabric supported? 
A.Yes, PTP over SD-Access fabric is supported. 
Q.Do the Catalyst 9000 switch platforms support PTP over IPv6? 
A.No, currently the switches do not support PTP over IPv6. 
Q.Is PTP aware of Virtual Routing and Forwarding (VRF) instances on the Catalyst 9000 switch platforms? 
A.No, PTP is not VRF-aware on the switches. 
Q.Is PTP over Multiprotocol Label Switching (MPLS) supported on the Catalyst 9000 switch platforms? 
A. No, PTP over MPLS is not supported on the switches. 
### Contact Cisco
  * [Get a call from Sales](https://www.cisco.com/site/us/en/about/contact-cisco/index.html?linkclickid=luh-contactus)
  * ##### Call Sales:
  * [ 1-800-553-6387 ](tel:18005536387)
  * US/CAN | 5am-5pm PT
  * [Product / Technical Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Training & Certification](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)


### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
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
