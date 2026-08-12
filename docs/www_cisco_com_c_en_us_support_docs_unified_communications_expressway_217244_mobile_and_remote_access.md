  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Expressway Series](https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/series.html)
  * [Troubleshooting TechNotes](https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-tech-notes-list.html)


# How Phone Services Failover works for Jabber Version 14 over MRA
![](https://www.cisco.com/etc/designs/cdc/fw/i/TAC_lg-icon.png)
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)
Download
Print
### Available Languages
  * [Arabic - عربي](https://www.cisco.com/c/ar_ae/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)
  * [Brazil - Português](https://www.cisco.com/c/pt_br/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)
  * [Canada - Français](https://www.cisco.com/c/fr_ca/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)
  * [China - 简体中文](https://www.cisco.com/c/zh_cn/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)
  * [China - 繁體中文 (臺灣)](https://www.cisco.com/c/zh_tw/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)
  * [Germany - Deutsch](https://www.cisco.com/c/de_de/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)
  * [Italy - Italiano](https://www.cisco.com/c/it_it/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)
  * [Korea - 한국어](https://www.cisco.com/c/ko_kr/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)
  * [Latin America - Español](https://www.cisco.com/c/es_mx/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)
  * [Netherlands - Nederlands](https://www.cisco.com/c/nl_nl/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)


### Download Options
  * [PDF](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.pdf) (23.6 KB)   
View with Adobe Reader on a variety of devices
  * [ePub](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.epub) (96.4 KB)   
View in various apps on iPhone, iPad, Android, Sony Reader, or Windows Phone
  * [Mobi (Kindle)](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.mobi) (85.1 KB)   
View on Kindle device or Kindle app on multiple devices


Updated:July 8, 2021
Document ID:217244
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
## Contents
[Introduction](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html#anc0)
[Prerequisites](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html#anc1)
[Requirements](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html#anc2)
[Components Used](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html#anc3)
[](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html#anc4)
[Background Information](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html#anc5)
[Configuration](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html#anc6)
[](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html#anc7)
[Troubleshooting](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html#anc8)
[Collect diagnostic logs](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html#anc9)
[Registration](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html#anc10)
## Introduction
This document describes how failover works for phone services on Jabber when registered via Mobile and Remote Access (MRA) with the addition of Session Traversal Utilities for NAT (STUN) keep alives on version 14 and later.
## Prerequisites
### Requirements
Cisco recommends that you have knowledge of these topics:
  * Cisco Unified Communications Manager (CUCM).
  * Cisco Expressway Core.
  * Cisco Expressway Edge.
  * Cisco Jabber for Windows.
  * Cisco Jabber for MAC.
  * Cisco Jabber for Android.
  * Cisco Jabber for iOS.


### Components Used
The information in this document is based on these software and hardware versions:
  * Expressway Version X14.0.
  * CUCM 14.0.
  * Cisco Jabber Version 14.0.


The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.
## Background Information
For versions previous to x14.0, the MRA solution does not support automatic failover for phone services on soft clients like Jabber. With the introduction of STUN keep alives, this is now supported as long as the involved components meet the required criteria, this allows jabber to register to a secondary server if the main route or server itself become compromised or unreachable.
## Configuration
The only configuration required is to enable STUN Keep Alives on the expressway servers. This feature is enabled by default and only requires to be configured if it has been previously disabled.
Step 1. Open the Expressway-C web interface.
Step 2. Navigate to **Configuration > Unified Communications > Configuration > Advanced**.
[![](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services-00.jpeg)](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services-00.jpeg "Related image, diagram or screenshot.")
Step 3. Open the Expressway-C Command Line Interface (CLI).
Step 4. Run the next command: **xconfiguration SIP Advanced StunKeepAliveForRegisteredPathEnabled: on**.
**[![](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services-01.jpeg)](https://www.cisco.com/c/dam/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services-01.jpeg "Related image, diagram or screenshot.")**
**Note** : The setting must match between core and edge servers in order to avoid decode issues.
## Troubleshooting
To ensure the feature is effective, the registration signaling needs to be analyzed.
### Collect diagnostic logs
Step 1. On the expressway servers web interface, navigate to **Maintenance > Diagnostics > Diagnostic Logging.**
Step 2. Check the **Take tcpdump while logging** checkbox.
Step 3. Select **Start new log** on both Core and Edge servers.**  
**
Step 4. Log in to your account on the jabber client with your standard username and password and wait for the phone services to register.
Step 5. Select **Stop logging** on both Core and Edge servers
Step 6. On all expressway servers, select **Collect Log** and **Download log** after it loads.
**Note** : In case of a cluster, Step 6 must be repeated on secondary peers.
### Registration
A jabber client on version 14 and later includes the tag **x-cisco-mra-ha=AR_SK** on the register message as seen below on the **Contact header** or **Supported header** , this indicates that STUN keep alives are supported.

```
 SIPMSG:
 |REGISTER sip:cmpub01.rvalverd.local SIP/2.0
 Via: SIP/2.0/TLS 172.16.84.136:58980;branch=z9hG4bK00003665
 Call-ID: 00505696-779a0005-00001bba-00007938@172.16.84.136
 CSeq: 104 REGISTER
 Contact: <sip:7514c56a-1034-a684-3299-9b956979ee5c@172.16.84.136:58980;transport=tls>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-00505696779a>";+u.sip!devicename.ccm.cisco.com="CSFMRA01";+u.sip!model.ccm.cisco.com="503";video;x-cisco-mra-ha=AR_SK;x-cisco-reg-id=1
 From: <sip:10001@cmpub01.rvalverd.local>;tag=00505696779a000700006827-00006484
```

The **200 OK** message must contain this as well on the **Supported header** to indicate the server supports it.

```
 SIPMSG:
 |SIP/2.0 200 OK
 Via: SIP/2.0/TLS 172.16.84.136:58980;branch=z9hG4bK00007e98;received=10.88.246.8;rport=58980;ingress-zone=CollaborationEdgeZone
 Call-ID: 00505696-779a0005-00001bba-00007938@172.16.84.136
 CSeq: 105 REGISTER
 Contact: <sip:7514c56a-1034-a684-3299-9b956979ee5c@10.15.20.10:5060;transport=tcp;orig-hostport=172.16.84.136:58980>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-00505696779a>";+u.sip!devicename.ccm.cisco.com="CSFMRA01";+u.sip!model.ccm.cisco.com="503";video;x-cisco-mra-ha=AR_SK;x-cisco-reg-id=1;+u.sip!userid.ccm.cisco.com="mra01";x-cisco-newreg
 From: <sip:10001@cmpub01.rvalverd.local>;tag=00505696779a000700006827-00006484
 To: <sip:10001@cmpub01.rvalverd.local>;tag=385623253
 Server: Cisco-CUCM12.5
 Expires: 120
 Date: Thu, 24 Jun 2021 19:09:09 GMT
 Supported: X-cisco-srtp-fallback,X-cisco-sis-9.2.0,X-cisco-supports-AR_SK
 Session-ID: 9b8c276600255000a0000e5dc13f0000;remote=c31f584200255000a00000ddda3c0000
```

After this, jabber then sends a STUN keep alive packet every 30 seconds to the expressway servers in order to check the path availability. The timeout for the STUN keep alive is 3 seconds and if no response is received, the jabber considers the edge node to be down and performs a registration failover via a different edge server.
**Note** : The MRA client does not attempt a registration failover while it is on an active call. Instead, the failover is queued until the call finishes. If this happens, the failover occurs even if the downed server recovers.
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  |  08-Jul-2021   | Initial Release  |  
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html "Back to Top")
![TAC Authored](https://www.cisco.com/etc/designs/cdc/fw/i/TAC_lg-icon.png)
### Contributed by Cisco Engineers
  * Randy Valverde


### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/217244-mobile-and-remote-access-phone-services.html)![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


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
