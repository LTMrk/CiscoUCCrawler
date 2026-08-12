  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72511.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72511.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72511.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72511.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72511.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Switches](https://www.cisco.com/c/en/us/support/switches/category.html)
  * [Cisco Catalyst 9300 Series Switches](https://www.cisco.com/c/en/us/support/switches/catalyst-9300-series-switches/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/switches/catalyst-9300-series-switches/products-field-notices-list.html)


# Field Notice: FN - 72511 - RSA Keys Less Than 2048 Bits Are Not Supported for SSH in Cisco IOS XE Release 17.11.1 and Later - Workaround Provided
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/725/fn72511.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72511.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/725/fn72511.html)


Updated:May 16, 2023
Document ID:FN72511
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  | 09-May-23  | Initial Release  |  
### Products Affected  
| Affected OS Type  | Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- | --- |  
| NON-IOS  | IOSXE  | 17  | 17.11.1, 17.11.1a  |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCwc72599](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwc72599)  | Device should not allow RSA keys less than 2048 bits in strength for SSH  |  
### Problem Description
In releases earlier than Cisco IOS XE Release 17.11.1, RSA keys less than 2048 bits can be used for the SSH server on the device.
In Cisco IOS XE Release 17.11.1 and later, RSA keys less than 2048 bits are denied for use with SSH by default due to its weak cryptographic properties. Cisco recommends to use stronger RSA keys that are at least 2048 bits. In order to continue to use RSA keys less than 2048 bits for SSH, explicit configuration is required. Without such a configuration change, SSH service on the device is disabled and SSH sessions to the device will fail. This results in loss of remote access to the device through SSH.
### Background
In Cisco IOS XE Release Bengaluru 17.6.1 and later, configuration of RSA keys less than 2048 bits for SSH generates a warning about a RSA key size compliance violation, but it does not impact SSH operations to the device. This warning message is displayed when a weak RSA key pair is used for SSH.
`%SSH-5-SSH_COMPLIANCE_VIOLATION_RSA_KEY_SIZE: SSH RSA Key Size compliance violation detected. Kindly note that the usage of keys smaller than 2048 bits will be deprecated in the upcoming releases. Please revise your key configuration accordingly to avoid service impact.`
In Cisco IOS XE Release 17.11.1 and later, RSA keys less than 2048 bits are denied by default and require explicit configuration to be allowed.
### Problem Symptom
If the RSA key pair is not updated to be at least 2048 bits for SSH, or if the configuration is not explicitly enabled to allow weak cryptographic algorithms prior to the Cisco IOS XE Release 17.11.1 upgrade, then the SSH server will be disabled upon an upgrade to Cisco IOS XE Release 17.11.1. This results in failure of the remote SSH sessions to the device. 
### Workaround/Solution
The solution is to update the RSA key pair used with SSH to at least 2048 bits.
Prior to an upgrade to Cisco IOS XE Release 17.11.1 or later, enter this command in order to identify the RSA key modulus size.

```
Device#**show ip ssh | include Modulus**

Modulus Size : 1024 bit
```

In order to update the RSA key pair, complete these steps:
  1. Enter this command in order to generate a new RSA key pair that is at least 2048 bits in strength. 
```
Device#**config terminal**

Enter configuration commands, one per line.  End with CNTL/Z.

csr1(config)#**crypto key generate rsa modulus 2048 label strong-ssh-key**

The name for the keys will be: strong-ssh-key


% The key modulus size is 2048 bits

% Generating 2048 bit RSA keys, keys will be non-exportable...

[OK] (elapsed time was 0 seconds)
```

  2. Enter this command in order to associate the newly generated RSA key pair with SSH. 
```
Device(config)#**ip ssh rsa keypair-name strong-ssh-key**
```



If it is not possible to update the RSA key pair, then this configuration command is required for SSH to continue to use the weak RSA key pair upon an upgrade to Cisco IOS XE Release 17.11.1.

```
Device(config)#**crypto engine compliance shield disable**
```

**Note:** This command is only available in Cisco IOS XE Release 17.7.1 and later, and will only take effect after a reboot.
Cisco does NOT recommend this option as these weak cryptographic algorithms are insecure and do not provide adequate protection from modern threats and should only be used as a last resort.
### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification For New Field Notices
[My Notifications](https://cway.cisco.com/mynotifications)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72511.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Customers Also Viewed
  * [Recommended Releases for Catalyst 9200/9300/9400/9500/9600 Platforms](https://www.cisco.com/c/en/us/support/docs/switches/catalyst-9300-series-switches/214814-recommended-releases-for-catalyst-9200-9.html)
  * [Cisco Catalyst 9300 Series Switches Hardware Installation Guide --- Product Overview](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/hardware/install/b_c9300_hig/Product-overview.html)
  * [Cisco Catalyst 9300 Series Switches Hardware Installation Guide --- Installing a Switch](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/hardware/install/b_c9300_hig/Installing-a-switch.html)
  * [Release Notes for Cisco Catalyst 9300 Series Switches, Cisco IOS XE Cupertino 17.9.x --- Upgrading the Switch Software](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/17-9/release_notes/ol-17-9-9300/upgrading_the_switch_software.html)
  * [Upgrade Catalyst 9300 Switches](https://www.cisco.com/c/en/us/support/docs/switches/catalyst-9300-series-switches/222280-upgrading-catalyst-9300-switches.html)
  * + Show 2 More


### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72511.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Catalyst 8000V Edge Software](https://www.cisco.com/c/en/us/support/routers/catalyst-8000v-edge-software/series.html)
  * [ISR 1000 Series IOS XE SD-WAN](https://www.cisco.com/c/en/us/support/routers/isr-1000-series-ios-xe-sd-wan/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/725/fn72511.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72511.html)
