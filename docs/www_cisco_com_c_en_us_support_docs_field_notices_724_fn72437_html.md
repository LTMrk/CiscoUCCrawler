  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/724/fn72437.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/724/fn72437.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/724/fn72437.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/724/fn72437.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/724/fn72437.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Servers - Unified Computing](https://www.cisco.com/c/en/us/support/servers-unified-computing/category.html)
  * [Cisco UCS C-Series Rack Servers](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/products-field-notices-list.html)


# Field Notice: FN - 72437 - AMD M6 Servers Might Fail Initial Discovery When Equipped with a Cisco VIC Card - Configuration Change Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/724/fn72437.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/724/fn72437.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/724/fn72437.html)


Updated:September 6, 2022
Document ID:FN72437
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 30-Aug-22  | Initial Release  |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
| UCSC-C245-M6SX  |   |  
| UCSC-C225-M6N  |   |  
| UCSC-C225-M6S  |   |  
| UCSC-C225-M6N=  | Part Alternate  |  
| UCSC-C225-M6S=  | Part Alternate  |  
| UCSC-C245-M6SX=  | Part Alternate  |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCwc50011](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwc50011)  | AMD M6 servers may fail initial discovery when equipped with Cisco card for Management  |  
### Problem Description
Cisco Unified Computing System (UCS) AMD-based M6 rack servers might not discover properly in UCS Manager Integrated Mode or Intersight Managed Mode (IMM) due to the incorrect Cisco Integrated Management Controller (IMC) setting from manufacturing. Standalone servers might also be unmanageable during initial installation from the factory.
### Background
All Cisco UCS AMD-based M6 rack servers that were manufactured before August 2022 were shipped with the incorrect Network Interface Controller (NIC) mode setting. The NIC mode setting is the configuration option that tells the rack server which port to use for management, which includes UCS Manager integration or IMM discovery. When the server is configured with a Cisco card (VIC/MLOM), the expectation is that it will be configured to be managed through the Cisco card by default. Instead, these servers shipped from manufacturing with the Cisco NIC mode set to `**Dedicated**`, which means that the server will attempt to use the dedicated management port on the back of the server for all management functions, which includes discovery and UCS Manager integration.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/724/fn72437img2.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/724/fn72437img2.jpg "Related image, diagram or screenshot.")
### Problem Symptom
Cisco UCS AMD-based M6 rack servers (C225 and C245) will fail initial automatic discovery under IMM/UCS Manager integration when they attempt to discover using the Cisco card. The servers will not appear as available to be claimed or discovered. Only the dedicated management port will allow for successful discovery, management, or integration until any of the workarounds are performed.
These servers will not be manageable through the Cisco card until a workaround is performed. Instead, they can be managed through the dedicated management port, which is the port marked 8 in this image:
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/724/fn72437img3.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/724/fn72437img3.jpg "Related image, diagram or screenshot.")
### Workaround/Solution
Reset Cisco IMC to factory defaults in order to restore the appropriate management mode option for the server. Alternatively, from the Cisco IMC Configuration Utility, change the NIC mode setting to the appropriate Cisco card. Setting up server management through the dedicated management port is not required in order to reset a server back to factory defaults.
**Option 1. Reset Using Local Keyboard, Video, and Mouse**
From a local keyboard, video, and mouse (KVM) session, reboot the server into the F8 Configuration Utility and reset to factory defaults. Alternatively, manually change to the desired NIC mode settings which are on the first property page. In order to reset to the defaults, press `**F1**`to show additional settings, choose`**Factory Default**`, and then press`**F10**`two times to save the configuration.
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/724/fn72437img4.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/724/fn72437img4.jpg "Related image, diagram or screenshot.")
**Option 2. Reset Using Smart Access Serial**
Use the Smart Access Serial or USB connection to connect directly to the Cisco IMC CLI and reset the Cisco IMC to factory defaults. The serial interface is Port 7 in the previous figure. This mode requires authentication to the Cisco IMC with the default password. More details can be found in the [Cisco UCS C-Series Servers Integrated Management Controller CLI Configuration Guide, Release 4.2](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/cli/config/guide/4_2/b_cisco_ucs_c-series_cli_configuration_guide_42/b_Cisco_UCS_C-Series_CLI_Configuration_Guide_41_chapter_010000.html?bookSearch=true#task_6252C3DCB779426787C8834BED4E0327).
The CLI command to reset a server to factory defaults is:

```
Server# **scope server**
Server /cimc # **factory-default**
```

**Option 3. Reset with XML API**
Users who have a method to connect to a dedicated management port through DHCP can use the XML Application Programming Interface (API) to perform a bulk Cisco IMC reset to factory defaults or NIC mode change. For information on which APIs to use, see the [Cisco UCS Rack-Mount Servers Cisco IMC XML API Programmer's Guide, Release 4.2](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/api/4_2/b-cisco-imc-xml-api-42.html).
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/724/fn72437.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/724/fn72437.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [UCS C225 M6 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c225-m6-rack-server/model.html)
  * [UCS C245 M6 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c245-m6-rack-server/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/724/fn72437.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/724/fn72437.html)
