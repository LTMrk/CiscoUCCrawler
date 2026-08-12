  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/support/unified-communications/category.html)
  * [Cisco Collaboration Systems Release](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/series.html)
  * [Troubleshooting TechNotes](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/products-tech-notes-list.html)


# Troubleshoot Unified Communications (UC), Non-UC, and Third-Party Virtual Machines (VMs) Co-residency
![](https://www.cisco.com/etc/designs/cdc/fw/i/TAC_lg-icon.png)
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)
Print
### Available Languages
  * [Arabic - عربي](https://www.cisco.com/c/ar_ae/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)
  * [Brazil - Português](https://www.cisco.com/c/pt_br/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)
  * [Canada - Français](https://www.cisco.com/c/fr_ca/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)
  * [China - 简体中文](https://www.cisco.com/c/zh_cn/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)
  * [China - 繁體中文 (臺灣)](https://www.cisco.com/c/zh_tw/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)
  * [Germany - Deutsch](https://www.cisco.com/c/de_de/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)
  * [Italy - Italiano](https://www.cisco.com/c/it_it/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)
  * [Korea - 한국어](https://www.cisco.com/c/ko_kr/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)
  * [Latin America - Español](https://www.cisco.com/c/es_mx/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)
  * [Netherlands - Nederlands](https://www.cisco.com/c/nl_nl/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)


Updated:May 19, 2017
Document ID:113520
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
## Contents
[Introduction](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html#anc0)
[Prerequisites](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html#anc1)
[Requirements](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html#anc2)
[Components Used](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html#anc3)
[Co-residency and “Quality of Service”](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html#anc4)
[Related Information](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html#anc5)
##  Introduction
This document clarifies some aspects of the support policy for application co-residency defined in the [Application Co-residency Support Policy](https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-sizing.html#cores) as part of the support policy for virtualized Cisco Unified Communications (UC)/Collaboration applications defined at [Cisco Collaboration Virtualization](https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html). This tech note is applicable to all UC on Unified Computing System (UCS) and other virtualization hardware options that include UCS Tested Reference Configuration, UCS Specs-based, and 3rd-party-server Specs-based. 
##  Prerequisites
###  Requirements
Cisco recommends that you have knowledge of these topics:
  * UC on UCS solution
  * UCS Tested Reference Configuration hardware
  * Specs-based hardware (UCS, HP or IBM)
  * Virtualization of Cisco Collaboration applications
  * VMware vSphere software
  * Cisco Unified Computing System hardware


**Note** : See the "Related Information" section of this document for web page links.
###  Components Used
The information in this document is based on these software and hardware versions:
  * Cisco Collaboration applications that support virtualization (see At a Glance at [Cisco Collaboration Virtualization](https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html)).
  * Support policy for Virtualization of Cisco UC/Collaboration applications (see Supporting Documentation at [Cisco Collaboration Virtualization](https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html)).


The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.
##  Co-residency and “Quality of Service”
A key principal of both network convergence and virtualization is the sharing of hardware resources.
  * A converged IP network shares network hardware among multiple traffic streams (voice, video, storage access, and other data).
  * A virtualized server (or virtualization host) shares compute, storage, and network hardware among multiple application virtual machines (VMs).


In both cases, quality of service is required to protect UC from non-UC applications when hardware resources are finite, as such:
  * Quality of Service (QoS) in routing and switching network hardware in order to ensure voice/video network traffic gets the needed bandwidth and protection from delay and jitter.
  * Adherence to UC virtualization rules (for example, physical/virtual hardware sizing, co-residency policy, and so on) in order to ensure UC VMs get the needed CPU, memory, storage capacity, and storage/network performance.


It is impossible for Cisco to test every combination of hardware and application for VM co-residency, particularly for 3rd-party application VMs whose behavior might be unpredictable or not clearly defined. Therefore, real-time performance of Cisco UC applications is only committed when installed on a UCS [Tested Reference Configuration](https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-hardware.html#trc) and then only when all conditions in the co-residency policy are followed (see [Collaboration Virtualization Sizing](https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/collaboration-virtualization-sizing.html), and for applications that support CPU Reservations like UCM and IMP, there might be [other considerations](https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cucm-vmware-support.html)).
For other environments, uncertainty can be reduced by pre-deployment testing, baselining, following general principles of virtualization, and following the rules of Cisco UC virtualization (at [Cisco Collaboration Virtualization](https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html)). However, Cisco cannot guarantee that VMs will never be starved for resources and never have performance problems.
**Key Support Considerations for Non-UC and 3rd-party Virtual Machines**
**In order to enable Cisco TAC to effectively provide support when you run Cisco UC VMs co-resident with non-UC/3rd-party app VMs, customers must ensure either of these:**
  * Non-UC/3rd-party VMs are non-critical and are able to be temporarily powered-down if required to facilitate troubleshooting.
  * If no VMs are non-critical, then spare capacity must be provisioned on virtualization hosts or physical servers for relocation (temporary or permanent) of VMs as solutions to application performance problems. Spare capacity is already a recommended design best practice for redundancy or to provide temporary staging of VMs when maintenance is required on hardware or software. Examples of “spare capacity” are extra “empty” physical servers (to provide “hot-standby” or temporary staging), or existing blade/rack-mount servers not fully utilized.


**In order to enable Cisco TAC to effectively provide support when you run Cisco UC VMs co-resident with non-UC/3rd-party app VMs, Cisco might require these activities from the customer for problem diagnosis or resolution:**
  * Changes to either the software workload or the physical hardware, in order to troubleshoot or resolve application performance problems. Examples of when these changes might be required are UC VM receiving insufficient CPU, memory, network, disk capacity or storage input/output operations per second (IOPS) from the hardware.
  * Examples of what these changes look like in an actual deployment are listed here.
    * Software: temporary power-down of non-critical VMs in order to facilitate performance troubleshooting
    * Software: move critical VMs and/or non-critical VMs in order to alternate virtualization host/physical server as temporary or permanent solution.
      * Temporarily reduce the number of virtual machines that run on a host if Cisco deems necessary for troubleshooting purposes.
      * Permanently reduce the number of virtual machines that run on a host if Cisco determines the host is overloaded.
      * Splitting a dense UC app VM into multiple less-dense VMs, then moving those less-dense VMs to alternate host. For example, splitting a CUCM 10K user OVA into multiple CUCM 7.5K user OVAs, then relocating some of those CUCM 7.5K user OVAs.
    * These approaches allow reduction of the software workload on an overloaded virtualization host/physical server, so that the workload is no longer starved for hardware resources.
  * Hardware: additions/upgrades to "fix" an overloaded host as an alternative to powering-down VMs or moving VMs.
    * For example, addition of more physical disks to increase storage capacity and/or provide IOPS.
    * For example, addition of more physical memory or more physical CPU cores.
    * For example, addition of physical NIC interfaces to address LAN congestion.
    * These approaches allow "upgrading" the overloaded hardware to accommodate the resource-starved software workload.


Cisco's provision of support is contingent upon the customer maintaining a current and fully paid support contract with Cisco.
##  Related Information
  * **[Cisco Unified Communications on Cisco Unified Computing System](https://www.cisco.com/go/uconucs?referring_site=bodynav) **
  * **[Unified Communications in a Virtualized Environment](https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-virtualization.html) **
  * **[VMware](http://www.vmware.com?referring_site=bodynav) **
  * **[DC Partner - VMware](https://www.cisco.com/go/vmware?referring_site=bodynav) **
  * **[ Unified Communications VMware Requirements](https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-software-requirements.html) **
  * **[Unified Computing](https://www.cisco.com/go/ucs?referring_site=bodynav) **
  * **[Technical Support & Documentation - Cisco Systems](https://www.cisco.com/cisco/web/support/index.html?referring_site=bodynav) **


### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  |  30-Apr-2012   | Initial Release  |  
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html "Back to Top")
![TAC Authored](https://www.cisco.com/etc/designs/cdc/fw/i/TAC_lg-icon.png)
### Contributed by Cisco Engineers
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/voice-unified-communications/unified-communications-system/113520-edcs1153298.html)![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Collaboration Systems Release](https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/series.html)
  * [Emergency Responder](https://www.cisco.com/c/en/us/support/unified-communications/emergency-responder/series.html)
  * [TelePresence Management Suite (TMS)](https://www.cisco.com/c/en/us/support/conferencing/telepresence-management-suite-tms/series.html)
  * [TelePresence Video Communication Server (VCS)](https://www.cisco.com/c/en/us/support/unified-communications/telepresence-video-communication-server-vcs/series.html)
  * [Unified Communications Manager IM & Presence Service](https://www.cisco.com/c/en/us/support/unified-communications/unified-presence/series.html)
  * [Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/series.html)
  * [Unified Contact Center Express](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/series.html)
  * [Unified Contact Center Management Portal](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-management-portal/series.html)
  * [Unified Customer Voice Portal](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/series.html)
  * [Unified Intelligence Center](https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/series.html)

+ Show All 10 Products
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
