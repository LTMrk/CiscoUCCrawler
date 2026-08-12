  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Conferencing](https://www.cisco.com/c/en/us/support/conferencing/category.html)
  * [Cisco Meeting Server](https://www.cisco.com/c/en/us/support/conferencing/meeting-server/series.html)
  * [Support FAQ](https://www.cisco.com/c/en/us/support/conferencing/meeting-server/products-support-faq-list.html)


# Troubleshoot common issues regarding CMS conference bridge registration on CUCM
![](https://www.cisco.com/etc/designs/cdc/fw/i/TAC_lg-icon.png)
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)
Download
Print
### Available Languages
  * [Arabic - عربي](https://www.cisco.com/c/ar_ae/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)
  * [Brazil - Português](https://www.cisco.com/c/pt_br/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)
  * [Canada - Français](https://www.cisco.com/c/fr_ca/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)
  * [China - 简体中文](https://www.cisco.com/c/zh_cn/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)
  * [China - 繁體中文 (臺灣)](https://www.cisco.com/c/zh_tw/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)
  * [Germany - Deutsch](https://www.cisco.com/c/de_de/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)
  * [Italy - Italiano](https://www.cisco.com/c/it_it/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)
  * [Korea - 한국어](https://www.cisco.com/c/ko_kr/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)
  * [Latin America - Español](https://www.cisco.com/c/es_mx/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)
  * [Netherlands - Nederlands](https://www.cisco.com/c/nl_nl/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)


### Download Options
  * [PDF](https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.pdf) (19.3 KB)   
View with Adobe Reader on a variety of devices


Updated:February 13, 2025
Document ID:222766
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
## Contents
## Introduction
This document describes common issues faced when trying to register Cisco Meeting Server (CMS) as a conference bridge on Cisco Unified Call Manager (CUCM).
## **Prerequisits**
- Have configured a SIP Trunk from CUCM to CMS using CMS's FQDN rather than IP
- Have configured the CMS conference bridge on CUCM, having enabled the Override SIP Trunk Destination as HTTPS Address Hostname.
**1. TLS version mismatch**  
It can happen that CUCM is using TLS 1.0 whereas CMS is using TLS 1.2  
From version 2.3, the Meeting Server uses a minimum of TLS 1.2 and DTLS 1.2 for all services: SIP, LDAP, HTTPS (inbound connections: API, Web Admin and Web Bridge; outbound connections: CDRs) and XMPP.
**Solution**  
If needed for interop with older software that has not implemented TLS 1.2, a lower version of the protocol can be set as the minimum TLS version for the SIP, LDAP and HTTPS services. See tls <service> min-tls-version <minimum version string> and tls min-dtls-version <minimum version string> commands in the MMP Command reference guide for CMS.  
Note: A Call Bridge restart is required for changes to the tls configuration to be applied.
**2. CUCM not sending any TCP traffic to CMS**  
It can happen that you see no traffic arriving from CUCM on CMS.
**Solution**
The reason this can happen is because CUCM is unable to resolve the URL to connect to CMS. Make sure the URL used in the Override SIP Trunk Destination as HTTPS Address Hostname on the conference bridge has a corresponding A record on the DNS which the CUCM is using.
Alternatively, make sure that the Primary DNS of CUCM is able to resolve the FQDN of CMS. The secondary DNS node configured on CUCM will not be used unless the primary DNS node is completly not reachable.
In the CUCM SDL logs you will see this:

```
87042368.004 |15:18:18.129 |AppInfo |ConnectionFailureToPDP - A connection request from Unified CM to the policy decision point failed Policy Decision Point:https://webbridge_test.test.com:445/RPC2/[](https://webbridge.test.com:445/RPC2/) The cause of the connection failure:Invalid URI App ID:Cisco CallManager Cluster ID:StandAloneCluster Node ID:TPCUCMPUB  
87042368.005 |15:18:18.129 |AlarmErr |AlarmClass: CallManager, AlarmName: ConnectionFailureToPDP, AlarmSeverity: Error, AlarmMessage: , AlarmDescription: A connection request from Unified CM to the policy decision point failed, AlarmParameters: PolicyDecisionPoint:https://webbridge.test.com:445/RPC2/[](https://webbridge.test.com:445/RPC2/), FailedToConnectReason:Invalid URI, AppID:Cisco CallManager, ClusterID:StandAloneCluster, NodeID:TPCUCMPUB,
```

**3. CMS not regitsering becasue of certificate issue**
You see the TCP traffic being exchanged between CUCM and CMS, however CUCM is resetting the TCP cpnnection.
**Solution**
During the 3 way handshake to set up the TCP connection between CMS and CUCM, CMS is presenting its webadmin certificate to CUCM. The URL used in the ovverride prameter needs to be present in the WebAdmin certificate either as CN or in the SAN field.
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  |  13-Feb-2025   | Initial Release  |  
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html "Back to Top")
![TAC Authored](https://www.cisco.com/etc/designs/cdc/fw/i/TAC_lg-icon.png)
### Contributed by Cisco Engineers
  * Hassan Mohseni Pour Samii
TAC


### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/222766-troubleshoot-common-issues-regarding-cms.html)![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Meeting Server](https://www.cisco.com/c/en/us/support/conferencing/meeting-server/series.html)


