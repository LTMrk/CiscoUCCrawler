  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72570.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72570.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72570.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72570.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72570.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Routers](https://www.cisco.com/c/en/us/support/routers/category.html)
  * [Cisco Catalyst 8200 Series Edge Platforms](https://www.cisco.com/c/en/us/support/routers/catalyst-8200-series-edge-platforms/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/routers/catalyst-8200-series-edge-platforms/products-field-notices-list.html)


# Field Notice: FN - 72570 - Weak Cryptographic Algorithms Are Not Allowed by Default for OSPF IPsec Configuration in Cisco IOS XE Release 17.11.1 and Later - Configuration Change Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/725/fn72570.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72570.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/725/fn72570.html)


Updated:June 29, 2023
Document ID:FN72570
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 22-Jun-23  | Initial Release  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | IOSXE  | 17  | 17.11.1, 17.11.1a  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCwd28106](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwd28106)  | Deprecate weak cryptographic encryption algorithms used in an OSPFv3 IPsec configuration  |  
### Problem Description
In software releases earlier than Cisco IOS® XE Release 17.11.1, weak cryptographic algorithms DES, 3DES, and MD5 can be configured for Open Shortest Path First (OSPF) using the IPsec protocol.
In Cisco IOS XE Release 17.11.1 and later, weak cryptographic algorithms are no longer allowed by default due to their weak cryptographic properties. Cisco strongly recommends the use of stronger cryptographic algorithms in their place. In order to continue to use such weak cryptographic encryption algorithms, explicit configuration is required. Otherwise, OSPF neighborship will fail to establish and cause service disruption as a result.
This table lists the OSPF IPsec configurations and algorithms affected by this change.  
| Command  | Keyword Deprecated  |  
| --- | --- |  
|  `interface <interface-name>  
 			  
 			   ospfv3 encryption ipsec spi 0x100 esp <encryption type> <authentication type>`  |  `{des | 3des | md5}`  |  
|  `router ospfv3 <process>  
 			  
 			   area <area-id> encryption ipsec spi <spi value> esp <encryption type> <authentication type>`  |  `{des | 3des | md5}`  |  
|  `router ospfv3 <process>  
 			  
 			   address-family ipv6 unicast  
 			  
 			   area <area-id> virtual-link <x.x.x.x> encryption ipsec spi <spi value> esp <encryption types> <authentication type>`  |  `{des | 3des | md5}`  |  
### Background
In Cisco IOS XE Release 17.11.1 and later, such weak cryptographic encryption algorithms will not be allowed by default and require explicit configuration to be allowed.

```
Device(config-router)#**area 1 encryption ipsec spi 0x100 esp ?**

  aes-cbc  Use AES-CBC encryption

  null     ESP with no encryption

Device(config-router-af)#**area 1 virtual-link 1.1.1.1 encryption ipsec spi 0x100 esp ?**

  aes-cbc  Use AES-CBC encryption

  null     ESP with no encryption
```

### Problem Symptom
If the OSPFv3 IPsec configuration is not updated to use strong cryptographic algorithms prior to the Cisco IOS XE Release 17.11.1 software upgrade, OSPF neighborship will fail to establish and cause service disruption as a result.
### Workaround/Solution
**Recommended Solution**
Before you upgrade the software to Cisco IOS XE Release 17.11.1 or later, update the OSPFv3 IPsec configuration to use strong cryptographic algorithms, specifically AES-CBC for encryption and SHA1 for authentication.
**Workaround**
This is a workaround only and not the recommended solution.
Enter this configuration command for OSPFv3 IPsec in order to continue to function with the weak algorithms upon an upgrade to Cisco IOS XE Release 17.11.1.

```
Device(config)#**crypto engine compliance shield disable**
```

**Note:** This command is only available in Cisco IOS XE Release 17.7.1 and later, and will only take effect after a reboot. Cisco does NOT recommend this option as these weak cryptographic algorithms are insecure and do not provide adequate protection from modern threats. This command should only be used as a last resort.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72570.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72570.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Catalyst 8000V Edge Software](https://www.cisco.com/c/en/us/support/routers/catalyst-8000v-edge-software/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/725/fn72570.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72570.html)
