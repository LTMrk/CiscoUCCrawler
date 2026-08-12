  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20150128-ghost.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20150128-ghost.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20150128-ghost.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20150128-ghost.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)


# GNU glibc gethostbyname Function Buffer Overflow Vulnerability
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/csa/cisco-sa-20150128-ghost.html) to Save Content 
Print
### Available Languages
Updated:January 28, 2015
Document ID:1454783225821711
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
#  [![](https://tools.cisco.com/security/center/images/cisco-alert.svg)](https://tools.cisco.com/security/center/images/cisco-alert.svg "Related image, diagram or screenshot.")Cisco Security Advisory
# GNU glibc gethostbyname Function Buffer Overflow Vulnerability
Critical
Advisory ID: 
cisco-sa-20150128-ghost
First Published:
2015 January 28 22:30 GMT
Last Updated: 
2015 July 24 17:47 GMT
Version 1.33: 
[Final](https://tools.cisco.com/security/center/resources/security_vulnerability_policy.html#final)
Workarounds: 
[See below](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20150128-ghost.html#workarounds)
Cisco Bug IDs:
[CSCus66766](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus66766)
[CSCus68529](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68529)
[CSCus68533](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68533)
[ More... ](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20150128-ghost.html)
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20150128-ghost.html) ,[CSCus66766](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus66766),[CSCus68529](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68529),[CSCus68533](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68533),[CSCus68534](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68534),[CSCus68537](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68537),[CSCus68770](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68770),[CSCus68905](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68905),[CSCus68928](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68928),[CSCus69387](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69387),[CSCus69388](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69388),[CSCus69422](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69422),[CSCus69424](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69424),[CSCus69430](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69430),[CSCus69431](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69431),[CSCus69460](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69460),[CSCus69463](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69463),[CSCus69472](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69472),[CSCus69475](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69475),[CSCus69491](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69491),[CSCus69493](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69493),[CSCus69494](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69494),[CSCus69495](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69495),[CSCus69513](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69513),[CSCus69517](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69517),[CSCus69523](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69523),[CSCus69524](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69524),[CSCus69525](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69525),[CSCus69529](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69529),[CSCus69535](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69535),[CSCus69539](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69539),[CSCus69543](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69543),[CSCus69547](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69547),[CSCus69550](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69550),[CSCus69558](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69558),[CSCus69559](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69559),[CSCus69563](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69563),[CSCus69570](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69570),[CSCus69585](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69585),[CSCus69592](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69592),[CSCus69606](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69606),[CSCus69607](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69607),[CSCus69609](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69609),[CSCus69610](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69610),[CSCus69612](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69612),[CSCus69615](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69615),[CSCus69617](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69617),[CSCus69620](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69620),[CSCus69622](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69622),[CSCus69646](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69646),[CSCus69665](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69665),[CSCus69682](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69682),[CSCus69696](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69696),[CSCus69731](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69731),[CSCus69732](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69732),[CSCus69738](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69738),[CSCus69763](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69763),[CSCus69766](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69766),[CSCus69768](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69768),[CSCus69769](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69769),[CSCus69787](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69787),[CSCus69788](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69788),[CSCus69789](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69789),[CSCus69791](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69791),[CSCus69792](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69792),[CSCus69809](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69809),[CSCus70263](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus70263),[CSCus71708](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus71708),[CSCus71883](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus71883),[CSCus74488](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus74488),[CSCus85675](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus85675),[CSCus85759](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus85759),[CSCus95601](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus95601)
CVE-2015-0235
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20150128-ghost.html)
CWE-119
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20150128-ghost.html)
CVE-2015-0235
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20150128-ghost.html)
CWE-119
[](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20150128-ghost.html)
[ Download CVRF ](https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20150128-ghost/cvrf/cisco-sa-20150128-ghost_cvrf.xml)
Download PDF 
Email 
## 
Summary 
  * On January 27, 2015, a buffer overflow vulnerability in the GNU C library (glibc) was publicly announced. This vulnerability is related to the various gethostbyname functions included in glibc and affects applications that call these functions. This vulnerability may allow an attacker to obtain sensitive information from an exploited system or, in some instances, perform remote code execution with the privileges of the application being exploited.  
  
The glibc library is a commonly used third-party software component that is released by the GNU software project and a number of Cisco products are likely affected.  
  
This advisory will be updated as additional information becomes available. Cisco will release free software updates that address this vulnerability. Workarounds that mitigate this vulnerability are not available.   
  
This advisory is available at the following link:  
<http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20150128-ghost>


## 
Affected Products 
  * Cisco has completed the evaluation of its product line and the results can be found in the following sections.
##  Vulnerable Products 
Customers interested in tracking the progress of any of the following bugs can visit the [Cisco Bug Search Tool](https://bst.cloudapps.cisco.com/bugsearch/ "Bug Search Tool") to view the defect details and optionally select _Save Bug_ and activate the _Email Notification_ feature to receive automatic notifications when the bug is updated. Fixed software may be obtained from the [cisco.com](http://www.cisco.com/cisco/web/support/index.html#%7Eshp_download) download page. **  
  
Products and services listed in the subsections below have had their exposure to this vulnerability confirmed.  
**  
  
| Product  | Defect  | Fixed releases availability  |  
| --- | --- | --- |  
| Collaboration and Social Media  |  
| Cisco MeetingPlace  | [CSCus69792](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69792)  | 8.6(1.18) 8.5(5.45) (27-Feb-2015)  |  
| Cisco SocialMiner  | [CSCus68534](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68534)  | Affected systems have been updated.  |  
| Cisco WebEx Meetings Server versions 2.x  | [CSCus69430](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69430)  | 2.5MR2 2.0.1.707 (9-Feb-2015)  |  
| Cisco WebEx Node for MCS  | [CSCus69424](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69424)  | eureka-3.12.8 (22-Mar-2015)  |  
| Endpoint Clients and Client Software  |  
| Cisco Jabber Guest 10.0(2)  | [CSCus69789](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69789)  | 10.6.5 (23-Apr-2015)  |  
| Cisco MMP server  | [CSCus69437](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69437)  | MMP3.8.2.1 (TBD)  |  
| Network Application, Service, and Acceleration  |  
| Cisco Application and Content Networking System (ACNS)  | [CSCus69585](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69585)  |   |  
| Cisco GSS 4492R Global Site Selector  | [CSCus69592](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69592)  | 4.1.3.0.9 (1-Apr-2015)  |  
| Cisco Intercloud Fabric  | [CSCus71883](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus71883)  | Affected systems have been updated.  |  
| Cisco Prime Network Service Controller (PNSC)  | [CSCus71883](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus71883)  | Affected systems have been updated.  |  
| Cisco Visual Quality Experience Server  | [CSCus69570](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69570)  | Affected systems have been updated.  |  
| Cisco Visual Quality Experience Tools Server  | [CSCus69570](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69570)  | Affected systems have been updated.  |  
| Cisco Wide Area Application Services (WAAS)  | [CSCus69606](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69606)  | 2.18  
2.2 (9-Apr-2015)  |  
| Network and Content Security Devices  |  
| Cisco ASA CX and Cisco Prime Security Manager  | [CSCus69607](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69607)  | 100.1 (TBD)  |  
| Cisco Content Security Appliance Updater Servers  | [CSCus69422](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69422)  | 2.0.3 : Available  |  
| Cisco Intrusion Prevention System Solutions (IPS)  | [CSCus69646](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69646)  | 7.1.10 (08-May-2015)  
7.3.4 (TBD)  |  
| Cisco Physical Access Gateway  | [CSCus69612](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69612)  | Affected products have been patched.  |  
| Cisco Physical Access Manager  | [CSCus69613](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69613)  | CPAM 1.5.3 (3-Apr-2015)  |  
| Cisco Registered Envelope Service (CRES)  | [CSCus66766](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus66766)  | 4.3.0-191 (3-Feb-2015)  |  
| Cisco Secure ACS 5.x  | [CSCus68826](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68826)  | Affected systems have been updated.  |  
| Cisco Virtual Security Gateway for Microsoft Hyper-V  | [CSCus69456](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69456)  | 5.2(1)VSG2(1.3) (30-May-2015)  |  
| Identity Services Engine (ISE)  | [CSCus68798](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68798)  | 001.001(003.913) (20-Feb-2015)  |  
| Iron Port Encryption Appliance  | [CSCus66747](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus66747)  | 6.5.7 (TBD)  |  
| Network Management and Provisioning  |  
| Cisco Access Registrar Appliance  | [CSCus69480](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69480)  | Affected systems have been updated.  |  
| Cisco Application Networking Manager  | [CSCus69444](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69444)  | 005.260 (2-Mar-2015)  |  
| Cisco Multicast Manager  | [CSCus69474](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69474)  |   |  
| Cisco Network Analysis Module  | [CSCus69494](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69494)  | NAM 6.2 (June 2015)  |  
| Cisco Prime Access Registrar Appliance  | [CSCus69480](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69480)  | Affected systems have been updated.  |  
| Cisco Prime Collaboration Deployment  | [CSCus69763](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69763)  | 11.0 (Available)  
10.5.3 (27-Feb-2015)  |  
| Cisco Prime Data Center Network Manager  | [CSCus69452](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69452)  | 7.1(1.83) (17-Mar-2015)  |  
| Cisco Prime IP Express  | [CSCus69491](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69491)  | 008.003 (17-Mar-2015)   |  
| Cisco Prime Infrastructure Plug and Play Gateway Server  | [CSCus69495](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69495)  | Affected systems have been updated.  |  
| Cisco Prime Infrastructure  | [CSCus68905](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68905)  | PI2.2 (27-Feb-2015)  |  
| Cisco Prime LAN Management Solution  | [CSCus69472](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69472)  | 4.0 (31-May-2015)  |  
| Cisco Prime License Manager  | [CSCus69543](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69543)  | 10.5.2 (May 2015)  |  
| Cisco Prime Network Registrar (CPNR) virtual appliance  | [CSCus69475](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69475)  | 8.3 (19-Feb-2015)  |  
| Cisco Prime Service Catalog Virtual Appliance  | [CSCus69559](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69559)  | 11.0 (Available)  |  
| Cisco Quantum Policy Suite (QPS)  | [CSCus69663](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69663)  | Affected systems have been updated.  
 |  
| Cisco Quantum SON Suite  | [CSCus69664](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69664)  | Affected systems have been updated.  |  
| Cisco Quantum Virtualized Packet Core  | [CSCus69664](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69664)  | Affected systems have been updated.  |  
| Cisco TelePresence MPS Series  | [CSCus69539](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69539)  | No future releases planned.  |  
| Cisco UCS Central  | [CSCus69460](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69460)  | 1.3(0.293) 1.2(1e)S4 (26-Feb-2015)  |  
| CiscoWorks LMS Portal  | [CSCus74488](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus74488)  | 4.002 (30-May-2015)  |  
| Feature Analytics Service  | [CSCus69395](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69395)  | Affected systems have been updated.  |  
| Network Profiler  | [CSCus69713](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69713)  | Affected products have been patched.  |  
| Routing and Switching - Enterprise and Service Provider  |  
| Cisco ASR 5000 Series  | [CSCus69388](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69388)  | v16.1.8 (18-Mar-2015)  
v16.4.6 (20-Mar-2015)  
V17.1.2 (19-Feb-2015)  
v17.2.0 (18-Feb-2015)  |  
| Cisco IOS-XE for ASR1k, ASR903, ISR4400, CSR1000v  | [CSCus69732](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69732)  | 15.5(2)S/XE3.15.0S (31-Mar-2015)  
15.5(1)S1/XE3.14.1S (3-Mar-2015)  
15.4(3)S3/XE3.13.3S (29-May-2015)  
15.4(2)S3/XE3.12.3S (28-Mar-2015)  
15.4(1)S4/XE3.11.4S (29-May-2015)  
15.3(3)S6/XE3.10.6S (30-Jul-2015)  
15.2(4)S7/XE3.7.7S (20-Mar-2015)  
15.5(3)S/XE3.16.0S (31-Jul-2015)  |  
| Cisco IOS-XE for Catalyst 3k, 4k, AIR-CT5760, and Cisco RF Gateway 10 (RFGW-10)  | [CSCus69731](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69731)  |    
15.2(3) (April 2015)  
15.2(2) (March 2015)  
15.2(1) )(No additional releases are planned)  
15.1(2) (May 2015)  
15.1(1)SG (No additional releases are planned)  
15.0(2)SG (April 2015)   
15.2(4)E (September 2015)  |  
| Cisco MDS 9000 Series Multilayer Switches  | [CSCus78917](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus78917)  |  NX-OS 5.2 (20-Feb-2015)  
NX-OS 6.2 (30-Mar-2015)  |  
| Cisco Nexus 1000V Series Switches  | [CSCus71708](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus71708)  | 5.2(1)SV3(1.4) (9-May-2015)  |  
| Cisco Nexus 1000V Switch for VMware vSphere  | [CSCus69609](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69609)  | 2.1 (Available)  
2.2/2.3 (June 2015)   |  
| Cisco Nexus 3000 series switches  | [CSCus68770](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68770)  | 6.0(2)U6(0.128) (17-Mar-2015)  |  
| Cisco Nexus 4000 Series  | [CSCus69648](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69648)  | 4.1(2)E1(1o) (30-May-2015)  |  
| Cisco Nexus 5000 Series Switches  | [CSCus68591](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68591)  | 5.2(1).N1(9) (8-Apr-2015)  
6.0(2).N2(7) (15-Apr-2015)  
7.0(6).N1(1) (30-Mar-2015)  
7.1(1)N1(1) (10-Apr-2015)  |  
| Cisco Nexus 7000  | [CSCus68892](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68892)  | Nexus 7.0 (30-May-2015)  
Nexus 6.2 (17-Mar-2015)  |  
| Cisco Nexus 9000 Series (standalone, running NxOS)  | [CSCus68764](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68764)  | Affected systems have been updated.  |  
| Cisco OnePK All-in-One VM  | [CSCus69610](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69610)  | No further releases are planned.  |  
| Cisco Prime Data Center Network Manager  | [CSCus68928](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68928)  | 1.0(3f) (11-Feb-2015)  |  
| Cisco Service Control Application for Broadband  | [CSCus69738](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69738)  | 5.2.0 (5-Apr-2015)  |  
| Cisco Service Control Collection Manager  | [CSCus69738](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69738)  | 5.2.0 (5-Apr-2015)  |  
| Cisco Service Control Engine 1010  | [CSCus69738](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69738)  | 5.2.0 (5-Apr-2015)  |  
| Cisco Service Control Engine 2020  | [CSCus69738](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69738)  | 5.2.0 (5-Apr-2015)  |  
| Cisco Service Control Engine 8000  | [CSCus69738](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69738)  | 5.2.0 (5-Apr-2015)  |  
| Cisco Service Control Subscriber Manager  | [CSCus69738](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69738)  | 5.2.0 (5-Apr-2015)  |  
| IOS-XR for Cisco Network Convergence System (NCS) 6000  | [CSCus69517](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69517)  | Affected systems have been updated.  |  
| Nexus 2000 Series FEX  | [CSCus68591](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68591)  | 5.2(1).N1(9) (8-Apr-2015)  
6.0(2).N2(7) (15-Apr-2015)  
7.0(6).N1(1) (30-Mar-2015)  
7.1(1)N1(1) (10-Apr-2015)  |  
| Sunstone XRv-64 VRP  | [CSCus73199](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus73199)  |   |  
| Routing and Switching - Small Business  |  
| Cisco DPH150 Series MicroCell Solution  | [CSCus69653](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69653)  | 10.0 (9-Mar-2015)  |  
| Cisco Small Business ISA500 Series Integrated Security Appliances  | [CSCus69620](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69620)  | No further releases are planned.  |  
| Unified Computing  |  
| Cisco Standalone rack server CIMC  | [CSCus69461](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69461)  | 2.0(9) (20-Nov-2015)  |  
| Cisco UCS Manager  | [CSCus69458](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69458)  | 2.2(3d)AS9 (26-Feb-2015)  |  
| Cisco Unified Computing System E-Series Blade Server  | [CSCus69386](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69386)  | TBD  |  
| Cisco Virtualization Experience Media Engine  | [CSCus69809](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69809)  | No further releases are planned.  |  
| UCS IO Modules  | [CSCus69459](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69459)  | 3.1 (28-Apr-2015)  |  
| Voice and Unified Communications Devices  |  
| Cisco 190 ATA Series Analog Terminal Adaptor  | [CSCus69757](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69757)  | 1.3.7 (31-Dec-2015)  |  
| Cisco Agent Desktop for Cisco Unified Contact Center Express  | [CSCus69768](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69768)  | 10.6(1) (24-Feb-2015)   |  
| Cisco Emergency Responder  | [CSCus85675](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus85675)  | Affected systems have been updated.  |  
| Cisco Finesse  | [CSCus68529](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68529)  | 11.0.1 (18-Jun-2015)  |  
| Cisco Hosted Collaboration Mediation Fulfillment  | [CSCus69787](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69787)  | 10.6(1) (26-Mar-2015)  |  
| Cisco IP Interoperability and Collaboration System (IPICS)  | [CSCus69563](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69563)  | Affected systems have been updated.  |  
| Cisco MediaSense  | [CSCus68533](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68533)  | 11.0(1) 10.5(1)SU1 (18-Feb-2015)  |  
| Cisco Paging Server (Informacast)  | [CSCus69788](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69788)  | Contact TAC for upgrade options.  |  
| Cisco Paging Server  | [CSCus69788](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69788)  | Contact TAC for upgrade options.  |  
| Cisco SPA112 2-Port Phone Adapter  | [CSCus69622](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69622)  | 1.3.7 (31-Dec-2015)  |  
| Cisco SPA122 ATA with Router  | [CSCus69622](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69622)  | 1.3.7 (31-Dec-2015)  |  
| Cisco SPA232D Multi-Line DECT ATA  | [CSCus69622](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69622)  | 1.3.7 (31-Dec-2015)  |  
| Cisco SPA525G  | [CSCus69632](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69632)  | 7.5.8 (31-Dec-2015)  |  
| Cisco Unified 7800 series IP Phones  | [CSCus70263](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus70263)  | Affected systems have been updated.  |  
| Cisco Unified 8961 IP Phone  | [CSCus70298](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus70298)  | Affected systems have been updated.  |  
| Cisco Unified 9951 IP Phone  | [CSCus70298](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus70298)  | Affected systems have been updated.  |  
| Cisco Unified 9971 IP Phone  | [CSCus70298](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus70298)  | Affected systems have been updated.  |  
| Cisco Unified Communications Manager (UCM) 10.0  | [CSCus66650](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus66650)  | 11.0(0.98000.246) (11-Mar-2015)  |  
| Cisco Unified Communications Manager (UCM) 7.x  | [CSCus66650](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus66650)  | 11.0(0.98000.246) (11-Mar-2015)  |  
| Cisco Unified Communications Manager (UCM) 8.x  | [CSCus66650](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus66650)  | 11.0(0.98000.246) (11-Mar-2015)  |  
| Cisco Unified Communications Manager (UCM) 9.x  | [CSCus66650](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus66650)  | 11.0(0.98000.246) (11-Mar-2015)  |  
| Cisco Unified Communications Manager IM and Presence Service (CUPS)  | [CSCus69785](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69785)  | IM&P 8.6.5 SU5 (31-Jul- 2015)  
IM&P 9.1.1SU5 (30-April-2015)  
IM&P 10.5.1SU3 (03-Apr-2015)  
IM&P 10.5.2b ( 25-Mar-2015)   
IM&P 11.0.1 (19-Jun-2015)  |  
| Cisco Unified Communications Manager Session Management Edition (SME)  | [CSCus66650](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus66650)  | 11.0(0.98000.246) (11-Mar-2015)  |  
| Cisco Unified Contact Center Express  | [CSCus68524](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68524)  | UCCX 11.0(1) (30-June-2015)  |  
| Cisco Unified IP Conference Phone 8831  | [CSCus69752](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69752)  | 9.3.4(5) (31-Aug-2015)  |  
| Cisco Unified IP Phone 8941 and 8945 (SIP)  | [CSCus69795](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69795)  | 9.4(2)SR2 (Aug 2015)  |  
| Cisco Unified Intelligence Center (CUIC)  | [CSCus68537](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus68537)  | 11.0(1) (30-Jun-2015)  |  
| Cisco Unified Intelligence Center  | [CSCus69769](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69769)  | 11.0 (TBD)  |  
| Cisco Unified Sip Proxy  | [CSCus69387](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69387)  | 9.0 (30-Jun-2015)  |  
| Cisco Unified Wireless IP Phone  | [CSCus69817](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69817)  | 1.4.7 (June 2015)  |  
| Cisco Unity Connection (UC)  | [CSCus69766](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69766)  | Affected systems have been updated.  |  
| Video, Streaming, TelePresence, and Transcoding Devices  |  
| Cisco CDS Internet Streaming  | [CSCus84663](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus84663)  | 004.001(000.120) 004.000(000.163) (13-Feb-2015)  |  
| Cisco Cloud Object Store (COS)  | [CSCus69567](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69567)  | Affected systems have been updated.  
 |  
| Cisco D9036 Modular Encoding Platform  | [CSCus69682](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69682)  | Affected systems have been updated.  |  
| Cisco DCM Series 9900-Digital Content Manager  | [CSCus69463](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69463)  | V16.0.0 (1-Apr-2015)  |  
| Cisco Digital Media Manager (DMM)  | [CSCus69547](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69547)  | 5.6 (5-Feb-2015)  |  
| Cisco Edge 300 Digital Media Player  | [CSCus69651](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69651)  | 1.6RB2 (20-March-2015)  |  
| Cisco Edge 340 Digital Media Player  | [CSCus69652](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69652)  | A patch file is available for vulnerable releases.  |  
| Cisco Expressway Series  | [CSCus69558](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69558)  | X8.5 X8.2 (30-Jan-2015)  |  
| Cisco Show and Share (SnS)  | [CSCus69547](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69547)  | 5.6 (5-Feb-2015)  |  
| Cisco TelePresence 1310  | [CSCus69749](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69749)  | 6.1.7-16R (Available)  
1.9.10 (16-May-2015)  |  
| Cisco TelePresence Conductor  | [CSCus69523](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69523)  | XC3.0 XC2.4 (30-Jan-2015)  |  
| Cisco TelePresence EX Series  | [CSCus69550](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69550)  | TC7.3.2 (19-Mar-2015)  |  
| Cisco TelePresence Exchange System (CTX)  | [CSCus69524](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69524)  | 1.3.0.4.3.0  
(15-Apr-2015)  |  
| Cisco TelePresence MX Series  | [CSCus69550](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69550)  | TC7.3.2 (19-Mar-2015)  |  
| Cisco TelePresence Multipoint Switch (CTMS)  | [CSCus69525](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69525)  | No further releases are planned.  |  
| Cisco TelePresence Profile Series  | [CSCus69550](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69550)  | TC7.3.2 (19-Mar-2015)  |  
| Cisco TelePresence Recording Server (CTRS)  | [CSCus69535](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69535)  | No further releases are planned.  |  
| Cisco TelePresence SX Series  | [CSCus69550](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69550)  | TC7.3.2 (19-Mar-2015)  |  
| Cisco TelePresence System 1000  | [CSCus85759](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus85759)  | 1.10.10 and 6.1.7 (25-Feb-2015)  
1.9.10 (23-March-2015)  |  
| Cisco TelePresence System 1100  | [CSCus85759](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus85759)  | 1.10.10 and 6.1.7 (25-Feb-2015)  
1.9.10 (23-March-2015)  |  
| Cisco TelePresence System 1300  | [CSCus85759](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus85759)  | 1.10.10 and 6.1.7 (25-Feb-2015)  
1.9.10 (23-March-2015)  |  
| Cisco TelePresence System 3000 Series  | [CSCus85759](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus85759)  | 1.10.10 and 6.1.7 (25-Feb-2015)  
1.9.10 (23-March-2015)  |  
| Cisco TelePresence System 500-32  | [CSCus69749](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69749)  | 6.1.7-16R (Available)  
1.9.10 (16-May-2015)  |  
| Cisco TelePresence System 500-37  | [CSCus85759](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus85759)  | 1.10.10 and 6.1.7 (25-Feb-2015)  
1.9.10 (23-March-2015)  |  
| Cisco TelePresence TE Software (for E20 - EoL)  | [CSCus69551](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69551)  | TE4.1.6 (31-Mar-2015)  
 |  
| Cisco TelePresence TX 9000 Series  | [CSCus69749](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69749)  | 6.1.7-16R (Available)  
1.9.10 (16-May-2015)  |  
| Cisco TelePresence Video Communication Server (VCS)  | [CSCus69558](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69558)  | X8.5 X8.2 (30-Jan-2015)  |  
| Cisco Telepresence Integrator C Series  | [CSCus69550](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69550)  | TC7.3.2 (19-Mar-2015)  |  
| Cisco VDS Service Broker  | [CSCus69694](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69694)  | Affected systems have been updated.  |  
| Cisco Video Delivery System Recorder  | [CSCut65960](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCut65960)  | Affected systems have been updated.  |  
| Cisco Video Surveillance 3000 Series IP Cameras  | [CSCus69616](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69616)  | 2.7.0 (30-Jul-2015)  |  
| Cisco Video Surveillance 4000 Series High-Definition IP Cameras  | [CSCus69615](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69615)  | 2.4.6 (30-Jul-2015)  |  
| Cisco Video Surveillance 4300E/4500E High-Definition IP Cameras  | [CSCus69614](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69614)  | 3.2.7 (30-Jul-2015)  |  
| Cisco Video Surveillance 6000 Series IP Cameras  | [CSCus69616](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69616)  | 2.7.0 (30-Jul-2015)  |  
| Cisco Video Surveillance 7000 Series IP Cameras  | [CSCus69616](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69616)  | 2.7.0 (30-Jul-2015)  |  
| Cisco Video Surveillance Media Server  | [CSCus69617](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69617)  | VSM 7.7.0 (Sept 2015)  |  
| Cisco Video Surveillance PTZ IP Cameras  | [CSCus69616](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69616)  | 2.7.0 (30-Jul-2015)  |  
| Cisco Videoscape Back Office (VBO)  | [CSCus69557](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69557)  | Affected systems have been updated.  |  
| Cisco Videoscape Conductor  | [CSCus69665](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69665)  | 2.5 (Available)  
3.0 (Available)  
3.1 (Available)  |  
| Cisco Videoscape Distribution Suite Transparent Caching  | [CSCus69696](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69696)  | TBD   |  
| Digital Media Player(DMP) 4310  | [CSCus69526](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69526)  | Affected systems have been updated.  |  
| Digital Media Player(DMP) 4400  | [CSCus69526](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69526)  | Affected systems have been updated.  |  
| Enterprise Content Delivery Service  | [CSCus69529](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69529)  | 2.6.4 (15-May-2015)  |  
| VDS-Recorder  | [CSCus82347](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus82347)  | 3.9 (Sept-2015)  |  
| VDS-TV Caching GW  | [CSCus82347](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus82347)  | 3.9 (Sept-2015)  |  
| VDS-TV Streamer  | [CSCus82347](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus82347)  | 3.9 (Sept-2015)  |  
| VDS-TV Vault  | [CSCus82347](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus82347)  | 3.9 (Sept-2015)  |  
| Wireless  |  
| Cisco 3300 Series Mobility Services Engine  | [CSCus69493](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69493)  | 8.0 MR2 (31-Mar-2015)  |  
| Cisco Wireless LAN Controller (WLC)  | [CSCus69513](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69513)  | 8.0.120.0 (June 2015)  |  
| Cisco Wireless Location Appliance (WLA)  | [CSCus69493](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69493)  | 8.0 MR2 (31-Mar-2015)  |  
| Cisco Wireless Security Gateway Application (WSG)  | [CSCus69649](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69649)  | Affected systems have been updated.  |  
| Cisco Hosted Services  |  
| Cisco Cloud Web Security  | [CSCus69647](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69647)  | A patch file will be available (July 2015)  |  
| Cisco Cloud and Systems Management  | [CSCus69394](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69394)  | PCN4.9 (1-Mar-2015)  |  
| Cisco Connected Analytics For Collaboration  | [CSCus69410](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69410)  | 1.0 (9-Mar-2015)  |  
| Cisco Intelligent Automation for Cloud  | [CSCus69560](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69560)  | 4.2 4.1.1 (9-Mar-2015)  |  
| Cisco Smart Call Home  | [CSCus69582](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69582)  |   |  
| Cisco Smart Care  | [CSCus69595](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69595)  | Affected systems have been updated.  |  
| Cisco Universal Small Cell 5000 Series running V3.4.2.x software  | [CSCus69660](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69660)  | Affected systems have been updated.  |  
| Cisco Universal Small Cell 7000 Series running V3.4.2.x software  | [CSCus69660](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69660)  | Affected systems have been updated.  |  
| Cisco WebEx Meeting Center  | [CSCus95601](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus95601)  | Affected systems have been updated.  |  
| Cisco WebEx Node  | [CSCus69791](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69791)  | 8.5(5.14) (26-Feb-2015)  |  
| Connected Analytics for Network Deployment (CAND)  | [CSCus69411](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69411)  | glibc-2.12-1.149.el6_6.5.x86_64 (available)  |  
| Network Performance Analytics (NPA)  | [CSCus69715](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69715)  | 1.11 (4-Feb-2015)  |  
| Services Analytic Platform  | [CSCus69413](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69413)  | Affected systems have been updated.  |  
| Small Cell factory recovery root filesystem V2.99.4 or later  | [CSCus69654](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69654)  | Affected systems have been updated.  |  
| WebEx PCNow  | [CSCus69431](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCus69431)  | PCN4.9 (1-Mar-2015)  |  
##  Products Confirmed Not Vulnerable 
**Note:** The following list includes Cisco applications that are intended to be installed on a customer-provided host (either a physical server or a virtual machine) with customer-installed operating systems. Those products may use glibc as provided by the host operating system on which the Cisco product is installed. While those Cisco products do not directly include an affected version of glibc (and are not impacted by this vulnerability), Cisco recommends that customers review their host operating system installation and perform any upgrades necessary to address this vulnerability (according to the operating system vendor recommendations and general operating system security best practices).  
  
**The following Cisco products have been analyzed and are not affected by this vulnerability:**  
  
_Cable Modems_  

    * Cisco 3G Femtocell Wireless
    * Cisco Prime Network Registrar (CPNR) IPAM
    * Digital Life RMS 1.8.1.1 Cisco Broadband Access Center Telco Wireless 3.8.1
  
_Collaboration and Social Media_  

    * Cisco Webex Social
  
_Endpoint Clients and Client Software_  

    * Cisco AnyConnect Secure Mobility Client for Android
    * Cisco AnyConnect Secure Mobility Client for desktop platforms
    * Cisco AnyConnect Secure Mobility Client for iOS
    * Cisco IP Communicator
    * Cisco Jabber for Windows
    * Cisco NAC Agent for Mac
    * Cisco NAC Agent for Web
    * Cisco UC Integration for Microsoft Lync
    * Cisco Unified Personal Communicator
    * Cisco WebEx Connect client (Windows)
    * Cisco WebEx Meetings for Android
    * Cisco WebEx Meetings for BlackBerry
    * Cisco WebEx Meetings for WP8
    * Cisco WebEx Productivity Tools
    * OpenFlow Agent
    * WebEx Recording Playback
  
_Network Application, Service, and Acceleration_  

    * Cisco ACE 10 & 20 Application Control Engine Module
    * Cisco ACE 30 Application Control Engine Module
    * Cisco ACE 4700 Series Application Control Engine Appliances
    * Cisco Adaptive Security Appliance (ASA) Software
    * Cisco Extensible Network Controller (XNC)
    * Cisco NAC Appliance
    * Cisco Nexus Data Broker (NDB)
    * Cisco Smart Call Home Transport Gateway
    * Content Services Switch
  
_Network and Content Security Devices_  

    * Cisco Adaptive Security Device Manager
    * Cisco Content Security Management Appliance (SMA)
    * Cisco FireSIGHT
    * Cisco IronPort Email Security Appliance
    * Cisco NAC Guest Server
    * Cisco Web Security Appliance (WSA)
  
_Network Management and Provisioning_  

    * Cisco Connected Grid Device Manager
    * Cisco Connected Grid Network Management System
    * Cisco Discovery Service
    * Cisco Insight Reporter
    * Cisco Linear Stream Manager
    * Cisco MATE Collector
    * Cisco MATE Design
    * Cisco MATE Live
    * Cisco MGC Node Manager (CMNM)
    * Cisco MXE Series
    * Cisco Media Experience Engines (MXE)
    * Cisco Mobile Wireless Transport Manager
    * Cisco Netflow Collection Agent
    * Cisco Network Collector
    * Cisco Prime Analytics
    * Cisco Prime Cable Provisioning
    * Cisco Prime Central for SPs
    * Cisco Prime Collaboration Assurance
    * Cisco Prime Home
    * Cisco Prime Network
    * Cisco Prime Optical for SPs
    * Cisco Prime Performance Manager for SPs
    * Cisco Security Manager
    * Cisco Unified Provisioning Manager (CUPM)
    * Cisco Videoscape Distribution Suite Service Manager
    * CiscoWorks Network Compliance Manager
    * DCAF UCS Collector
    * Data Center Analytics Framework (DCAF)
    * Local Collector Appliance (LCA)
    * Prime Collaboration Provisioning
    * Security Module for Cisco Network Registrar
    * Unified Communication Audit Tool (UCAT)
    * Unified Communications Deployment Tools
    * Virtual Systems Operations Center for vPE project
  
_Routing and Switching - Enterprise and Service Provider_  

    * CRS-CGSE-PLIM
    * CRS-CGSE-PLUS
    * Cisco ASR 9000 Series Integrated Service Module
    * Cisco Broadband Access Center Telco Wireless
    * Cisco Connected Grid Routers (CGR)
    * Cisco IOS-XR for Cisco ASR 9000 Series Aggregation Services Routers
    * Cisco IOS-XR for Cisco CRS Routers
    * Cisco IOS-XR for Cisco XR 12000 Series Routers
    * Cisco IOS
    * Cisco Metro Ethernet 1200 Series Access Devices
    * Cisco ONS 15454 Series Multiservice Provisioning Platforms
    * Cisco Prime Provisioning for SPs
    * Cisco VPN Acceleration Engine
  
_Routing and Switching - Small Business_  

    * Cisco RV180W Wireless-N Multifunction VPN Router
    * Cisco Small Business AP500 Series Wireless Access Points
    * Cisco Small Business RV 120W Wireless-N VPN Firewall
    * Cisco Small Business RV Series Routers 0xxv3
    * Cisco Small Business RV Series Routers RV110W
    * Cisco Small Business RV Series Routers RV130x
    * Cisco Small Business RV Series Routers RV215W
    * Cisco Small Business RV Series Routers RV220W
    * Cisco Small Business RV Series Routers RV315W
    * Cisco Small Business RV Series Routers RV320
    * Cisco Sx220 switches
    * Cisco Sx300 switches
    * Cisco Sx500 switches
    * Cisco WAP4410N Wireless-N Access Point
  
_Unified Computing_  

    * Cisco Billing and Measurement Server 3.30
    * Cisco Common Crypto Module
    * Cisco Common Services Platform Collector
    * Cisco UCS ADA
    * Cisco UCS Director
    * Cisco USC Invicta Series
    * Cisco Unified Computing System B-Series (Blade) Servers
  
_Voice and Unified Communications Devices_  

    * Cisco 7937 IP Phone
    * Cisco ATA 187 Analog Telephone Adaptor
    * Cisco Agent Desktop
    * Cisco Broadband Access Center for Cable Tools Suite 4.1
    * Cisco Broadband Access Center for Cable Tools Suite 4.2
    * Cisco Business Edition 3000 (BE3k)
    * Cisco Computer Telephony Integration Object Server (CTIOS)
    * Cisco Desktop Collaboration Experience DX650
    * Cisco Desktop Collaboration Experience DX70 and DX80
    * Cisco MS200X Ethernet Access Switch
    * Cisco PSTN Gateway (PGW 2200)
    * Cisco Packaged Contact Center Enterprise
    * Cisco Prime Cable Provisioning Tools Suite 5.0
    * Cisco Prime Cable Provisioning Tools Suite 5.1
    * Cisco Remote Silent Monitoring
    * Cisco SPA30X Series IP Phones
    * Cisco SPA50X Series IP Phones
    * Cisco SPA51X Series IP Phones
    * Cisco SPA8000 8-port IP Telephony Gateway
    * Cisco SPA8800 IP Telephony Gateway with 4 FXS and 4 FXO Ports
    * Cisco TAPI Service Provider (TSP)
    * Cisco Unified 3900 series IP Phones
    * Cisco Unified 6911 IP Phones
    * Cisco Unified 6945 IP Phones
    * Cisco Unified Attendant Console Advanced
    * Cisco Unified Attendant Console Business Edition
    * Cisco Unified Attendant Console Department Edition
    * Cisco Unified Attendant Console Enterprise Edition
    * Cisco Unified Attendant Console Premium Edition
    * Cisco Unified Attendant Console Standard
    * Cisco Unified Client Services Framework
    * Cisco Unified Communications Domain Manager
    * Cisco Unified Communications Sizing Tool
    * Cisco Unified Contact Center Enterprise
    * Cisco Unified E-Mail Interaction Manager
    * Cisco Unified IP Phone 6921
    * Cisco Unified IP Phone 7900 Series
    * Cisco Unified Integration for IBM Sametime
    * Cisco Unified Intelligent Contact Management Enterprise
    * Cisco Unified Operations Manager (CUOM)
    * Cisco Unified SIP Phone 3905
    * Cisco Unified Service Monitor
    * Cisco Unified Service Statistics Manager
    * Cisco Unified Web Interaction Manager
    * Cisco Unified Workforce Optimization
    * Cisco Unity Express
  
_Video, Streaming, TelePresence, and Transcoding Devices_  

    * Cisco AnyRes Live (CAL)
    * Cisco AnyRes VOD (CAV)
    * Cisco AutoBackup Server
    * Cisco Command 2000 Server (cmd2k) (RH Based)
    * Cisco Common Download Server (CDLS)
    * Cisco D9034-S Encoder
    * Cisco D9054 HDTV Encoder
    * Cisco D9804 Multiple Transport Receiver
    * Cisco D9824 Advanced Multi Decryption Receiver
    * Cisco D9854/D9854-I Advanced Program Receiver
    * Cisco D9858 Advanced Receiver Transcoder
    * Cisco D9859 Advanced Receiver Transcoder
    * Cisco D9865 Satellite Receiver
    * Cisco DNCS Application Server (AppServer)
    * Cisco Digital Network Control System (DNCS)
    * Cisco Digital Transport Adapter Control System (DTACS)
    * Cisco Download Server (DLS) (RH Based)
    * Cisco IPTV Service Delivery System (ISDS)
    * Cisco IPTV
    * Cisco International Digital Network Control System (iDNCS)
    * Cisco Jabber Video for TelePresence (Movi)
    * Cisco Jabber for TelePresence (Movi)
    * Cisco Model D9485 DAVIC QPSK
    * Cisco PowerVu Network Center
    * Cisco Powerkey CAS Gateway (PCG)
    * Cisco Powerkey Encryption Server (PKES)
    * Cisco Remote Conditional Access System (RCAS)
    * Cisco Remote Network Control System (RNCS)
    * Cisco TelePresence Advanced Media Gateway Series
    * Cisco TelePresence Content Server (TCS)
    * Cisco TelePresence IP Gateway Series
    * Cisco TelePresence IP VCR Series
    * Cisco TelePresence ISDN GW 3241
    * Cisco TelePresence ISDN GW MSE 8321
    * Cisco TelePresence ISDN Link
    * Cisco TelePresence MCU (8510, 8420, 4200, 4500 and 5300)
    * Cisco TelePresence MXP Software
    * Cisco TelePresence Management Suite (TMS)
    * Cisco TelePresence Management Suite Analytics Extension (TMSAE)
    * Cisco TelePresence Management Suite Extension (TMSXE)
    * Cisco TelePresence Management Suite Extension for IBM
    * Cisco TelePresence Management Suite Provisioning Extension
    * Cisco TelePresence Manager (CTSMan)
    * Cisco TelePresence Serial Gateway Series
    * Cisco TelePresence Server 8710, 7010
    * Cisco TelePresence Server on Multiparty Media 310, 320
    * Cisco TelePresence Server on Virtual Machine
    * Cisco TelePresence Supervisor MSE 8050
    * Cisco Transaction Encryption Device (TED)
    * Cisco Virtual PGW 2200 Softswitch
    * Media Services Interface
    * Tandberg Codian ISDN GW 3210/3220/3240
    * Tandberg Codian MSE 8320 model
  
_Wireless_  

    * Cisco Aironet 600 Series OfficeExtend Access Point
    * Cisco RF Gateway 1 (RFGW-1)
    * Cisco Small Business 121 Series Wireless Access Points
    * Cisco Small Business 321 Series Wireless Access Points
    * Cisco Small Business 500 Series Wireless Access Points
    * Cisco WAP371 wireless access point
    * Cisco Wireless Control System (WCS)
  
_Cisco Hosted Services_  

    * Business Video Services Automation Software (BV)
    * Cisco Cloud Services
    * Cisco Install Base Management
    * Cisco Network Configuration and Change Management Service
    * Cisco Partner Supporting Service
    * Cisco Proactive Network Operations Center
    * Cisco SLIM
    * Cisco SMB Market Place
    * Cisco Services Platform Collector (CSPC)
    * Cisco Services Provisioning Platform (SPP)
    * Cisco SmartConnection
    * Cisco SmartReports
    * Cisco USC Invicta Series Autosupport Portal
    * Cisco Unified Services Delivery Platform (CUSDP)
    * Cisco Universal Small Cell CloudBase
    * Cisco WebEx Messenger Service
    * Cisco WebEx WebOffice & Workspace
    * Core Services -Subcomponent of SNTC
    * Femto Provisioning Gateway
    * IC Capture
    * Install Base Management (IBM)
    * MACD Process Controller (MPC)
    * NetAuthenticate
    * Network Health Framework (NHF)
    * On Going Support Automation (OGSA)
    * One View
    * Partner Supporting Service (PSS) 1.x
    * Partner Supporting Service (PSS) 2.x
    * SI component of Partner Supporting Service
    * Sentinel
    * Serial Number Assessment Service (SNAS)
    * Smart Net Total Care (SNTC)
    * Smart Net Total Care
    * Support Central
    * Web Element Manager


## 
Details 
  * A buffer overflow was found in the GNU C library's (glibc) ___nss_hostname_digits_dots()_ function, which, in turn, is used by the _gethostbyname()_ , _gethostbyname2()_ , and other glibc function calls. The vulnerable code in the affected functions is designed to prevent DNS lookups for addresses that do not need to be resolved (i.e. they are already IPv4 or IPv6 addresses). These vulnerable functions are commonly used by networking applications.  
  
Systems that contain glibc versions 2.2 to 2.17 are affected by this vulnerability. Applications that statically link to an affected version are also affected by this vulnerability.  
  
The impact of this vulnerability varies based on hardware and software configurations. A remote, unauthenticated attacker that is able to provide a hostname to an application that is using an affected function may be able to exploit this vulnerability to obtain sensitive information from memory or perform remote code execution with the same privileges as the process or application being exploited.  
  
This vulnerability has been assigned the Common Vulnerabilities and Exposures (CVE) ID CVE-2015-0235.  
  
More information provided for each bug ID listed in the "Vulnerable Products" section of this advisory can be found in the [Cisco Bug Search Tool](https://bst.cloudapps.cisco.com/bugsearch/ "Bug Search Tool").


## 
Workarounds 
  * There are currently no network-based mitigations for this vulnerability or any mitigations that can be performed directly on affected systems.  
  
Cisco has published an Event Response for this vulnerability: <http://www.cisco.com/web/about/security/intelligence/ERP_GHOST_29-Jan-2015.html>


## 
Fixed Software 
  * When considering software upgrades, customers are advised to consult the Cisco Security Advisories, Responses, and Notices archive at <http://www.cisco.com/go/psirt> and review subsequent advisories to determine exposure and a complete upgrade solution.  
  
In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the Cisco Technical Assistance Center (TAC) or their contracted maintenance providers.


## 
Exploitation and Public Announcements 
  * This vulnerability was reported by Qualys and Alexander Peslyak of the Openwall Project. It was released on January 27, 2015.


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Action Links for This Advisory 
  * [Snort Rule 33225](https://www.snort.org/rule_docs/33225)
[Snort Rule 33226](https://www.snort.org/rule_docs/33226)
[Snort Rule 33275](https://www.snort.org/rule_docs/33275)
[Snort Rule 39925](https://www.snort.org)


## 
Related to This Advisory 
  * [Cisco Event Response: GNU glibc gethostbyname Function Buffer Overflow Vulnerability](http://www.cisco.com/web/about/security/intelligence/ERP_GHOST_29-Jan-2015.html)
[CVE-2015-0235: A GHOST in the Machine](http://blogs.cisco.com/talos/ghost-glibc)


## 
URL 
  * <http://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20150128-ghost>


## 
Revision History 
  * | Revision 1.33  | 2015-July-24  | Updated Fixed Releases availability data for some products.  |  
| --- | --- | --- |  
| Revision 1.32  | 2015-May-22  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.31  | 2015-April-28  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.30  | 2015-April-14  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.29  | 2015-April-10  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.28  | 2015-March-31  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.27  | 2015-March-27  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.26  | 2015-March-24  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.25  | 2015-March-20  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.24  | 2015-March-17  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.23  | 2015-March-13  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.22  | 2015-March-10  |  Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.21  | 2015-March-06  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.20  | 2015-March-03  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.19  | 2015-February-27  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.18  | 2015-February-24  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.17  | 2015-February-20  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.16  | 2015-February-19  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.15  | 2015-February-18  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.14  | 2015-February-17  |  Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.13  | 2015-February-16  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.12  | 2015-February-13  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.11  | 2015-February-12  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.10  | 2015-February-11  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.9  | 2015-February-10  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.8  | 2015-February-09  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.7  | 2015-February-06  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.6  | 2015-February-06  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.5  | 2015-February-04  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.4  | 2015-February-03  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.3  | 2015-February-03  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.2  | 2015-January-30  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections.  |  
| Revision 1.1  | 2015-January-29  | Updated the Affected Products, Vulnerable Products, and Products Confirmed Not Vulnerable sections. Added Cisco ERP to Workarounds section.  |  
| Revision 1.0  | 2015-January-28  | Initial public release.  |  
Show Complete History...


* * *
## 
Legal Disclaimer 
  * THIS DOCUMENT IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE. YOUR USE OF THE INFORMATION ON THE DOCUMENT OR MATERIALS LINKED FROM THE DOCUMENT IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS DOCUMENT AT ANY TIME.
A stand-alone copy or paraphrase of the text of this document that omits the distribution URL is an uncontrolled copy, and may lack important information or contain factual errors. The information in this document is intended for end-users of Cisco products.


## 
Feedback 
  * [Leave additional feedback](javascript:openNewWindow\(\);)


## 
Cisco Security Vulnerability Policy 
  * To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.


## 
Subscribe to Cisco Security Notifications
  * [Subscribe](https://www.cisco.com/c/en/us/support/web/tools/cns/notifications.html)


## 
Action Links for This Advisory 
  * [Snort Rule 33225](https://www.snort.org/rule_docs/33225)
[Snort Rule 33226](https://www.snort.org/rule_docs/33226)
[Snort Rule 33275](https://www.snort.org/rule_docs/33275)
[Snort Rule 39925](https://www.snort.org)


## 
Related to This Advisory 
  * [Cisco Event Response: GNU glibc gethostbyname Function Buffer Overflow Vulnerability](http://www.cisco.com/web/about/security/intelligence/ERP_GHOST_29-Jan-2015.html)
[CVE-2015-0235: A GHOST in the Machine](http://blogs.cisco.com/talos/ghost-glibc)


[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20150128-ghost.html "Back to Top")
