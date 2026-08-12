  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72323.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72323.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72323.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72323.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72323.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Switches](https://www.cisco.com/c/en/us/support/switches/category.html)
  * [Cisco Catalyst 9400 Series Switches](https://www.cisco.com/c/en/us/support/switches/catalyst-9400-series-switches/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/switches/catalyst-9400-series-switches/products-field-notices-list.html)


# Field Notice: FN72323 - Cisco IOS XE Software: QuoVadis Root CA 2 Decommission Might Affect Smart Licensing, Smart Call Home, and Other Functionality - Software Upgrade Recommended
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/723/fn72323.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72323.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/723/fn72323.html)


Updated:October 5, 2023
Document ID:FN72323
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| IOS XE Software  | 16  | 16.1.1, 16.1.2, 16.1.3, 16.10.1, 16.10.1a, 16.10.1b, 16.10.2, 16.10.3, 16.11.1, 16.11.1a, 16.12.1, 16.12.1a, 16.12.2, 16.12.2s, 16.12.3, 16.12.3a, 16.12.4, 16.12.5, 16.12.5b, 16.2.1, 16.2.2, 16.3.1, 16.3.10, 16.3.1a, 16.3.2, 16.3.3, 16.3.3a, 16.3.4, 16.3.5, 16.3.5b, 16.3.6, 16.3.7, 16.3.8, 16.3.9, 16.4.1, 16.4.2, 16.4.3, 16.5.1, 16.5.1a, 16.5.1b, 16.5.2, 16.5.3, 16.6.1, 16.6.10, 16.6.1a, 16.6.2, 16.6.3, 16.6.4, 16.6.5, 16.6.6, 16.6.7, 16.6.8, 16.6.9, 16.7.1, 16.7.2, 16.7.3, 16.8.1, 16.8.2, 16.8.3, 16.9.1, 16.9.2, 16.9.3, 16.9.3a, 16.9.4, 16.9.5, 16.9.6, 16.9.7, 16.9.8  | 16.1.1: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.1.2: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.1.3: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.10.1: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.10.1a: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.10.1b: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.10.2: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.10.3: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.11.1: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.11.1a: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.12.1: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.12.1a: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.12.2: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.12.2s: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.12.3: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.12.3a: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.12.4: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.12.5: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.12.5b: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.2.1: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.2.2: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.3.1: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.3.10: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.3.1a: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.3.2: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.3.3: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.3.3a: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.3.4: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.3.5: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.3.5b: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.3.6: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.3.7: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.3.8: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.3.9: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.4.1: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.4.2: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.4.3: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.5.1: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.5.1a: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.5.1b: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.5.2: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.5.3: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.6.1: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.6.10: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.6.1a: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.6.2: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.6.3: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.6.4: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.6.5: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.6.6: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.6.7: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.6.8: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.6.9: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.7.1: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.7.2: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.7.3: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.8.1: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.8.2: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.8.3: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.9.1: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.9.2: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.9.3: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.9.3a: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.9.4: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.9.5: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.9.6: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.9.7: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  
16.9.8: Cisco IOS XE Software Release 16.12.6 or later has the fix. All previous releases need to use the suggested workaround to address the issue.  |  
| IOS XE Software  | 17  | 17.1.1, 17.1.2, 17.1.3, 17.2.1, 17.2.1r, 17.2.2, 17.2.3, 17.3.1, 17.3.1a, 17.3.2, 17.3.2a, 17.3.3, 17.4.1, 17.4.1a, 17.4.1b  | 17.1.1: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  
17.1.2: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  
17.1.3: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  
17.2.1: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  
17.2.1r: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  
17.2.2: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  
17.2.3: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  
17.3.1: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  
17.3.1a: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  
17.3.2: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  
17.3.2a: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  
17.3.3: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  
17.4.1: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  
17.4.1a: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  
17.4.1b: Cisco IOS XE Software Releases 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later have the fix. All previous releases need to use the suggested workaround to address the issue.  |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCvx00521](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvx00521)  | QuoVadis root CA decommission impacting Smart Licensing and Smart Call Home Functionality  |  
  

### Problem Description
  

For affected versions of the Cisco IOS XE® software, some Secure Sockets Layer (SSL) certificates issued from the QuoVadis root certificate authority (CA) trust chain before March 31, 2021 cannot be renewed from this CA. Once those certificates expire on devices or are removed from the Cisco cloud servers, functions such as Smart Licensing and Smart Call Home will fail to establish secure connections to Cisco and might not operate properly. 
  

### Background
  

The QuoVadis Root CA 2 Public Key Infrastructure (PKI) used by the Cisco IOS XE software to issue SSL certificates is subject to an industry-wide issue that affects revocation abilities. Due to this issue, no new QuoVadis Root CA 2 certificates were issued or renewed by Cisco after March 31, 2021. This affects certificate renewals on devices, Cisco cloud servers, and third-party services.
Certificates issued before the QuoVadis Root CA 2 was decommissioned will continue to be valid. However, the certificates will not renew when they expire on either the device or the Cisco cloud server. This will cause functions such as Smart Licensing and Smart Call Home to fail to establish secure connections to Cisco cloud servers.
This table shows a summary of the QuoVadis Root CA 2 certificate expiration dates for affected Cisco services.  
| Cisco Cloud Server  | QuoVadis Certificate Expiration Date  | Affected Services  |  
| --- | --- | --- |  
| tools.cisco.com  | February 5, 2022  | 
  * Smart Licensing
  * Smart Call Home

 |  
| smartreceiver.cisco.com  | January 26, 2023  | 
  * Smart Licensing

 |  
  

### Problem Symptom
  

Expiration of the QuoVadis Root CA 2 certificates affects these services with the associated symptoms.  
| Affected Services  | Symptoms for Affected Services  |  
| --- | --- |  
| Smart Licensing  | Failure to connect to the server (Details are provided in this section)  |  
| Smart Call Home  | Failure to connect to the server and the Call-Home HTTP request fails  |  
For affected versions of Cisco IOS XE sofware, devices will be unable to connect to the Smart Licensing and Smart Call Home services hosted by Cisco. Smart licenses might fail entitlement and reflect an Out of Compliance status.
The features that use Smart Licensing will continue to function for one year after the last successful secure connection. Some Smart Licensing symptoms are:
  * The device might indicate a failure to communicate with the Smart Licensing server within 30 days from the last successful connection.
  * The device will show the "Authorization Expired" state if there is no communication with the Smart Licensing server within 90 days.
  * The device will show the "Unregistered" state if there is no communication with the Smart Licensing server after one year and the licensed features usage become suspended.


**Note:** Offline licensing, such as Permanent License Reservation (PLR) and Specific License Reservation (SLR), is not affected by the certificate change on the Smart Licensing server. Wireless LAN Controllers and Wireless Access Points will continue to function even when smart licensing failures occur.
For additional information, refer to the [Cisco Smart Licensing Guide](https://www.cisco.com/c/en/us/buy/licensing/licensing-guide.html), [Wireless LAN Controllers Guide](https://www.cisco.com/c/dam/en/us/td/docs/wireless/controller/9800/tech-notes/c9800_sl_slr_dg.pdf), [Catalyst Switching Guide](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/16-9/configuration_guide/sys_mgmt/b_169_sys_mgmt_9300_cg/configuring_smart_licensing.html), and [Enterprise Routing Guide](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/smart-licensing/qsg/b_Smart_Licensing_QuickStart/b_Smart_Licensing_QuickStart_chapter_01.html) for your specific version of Cisco IOS XE software.
These error logs may be observed in the affected device:
`%SMART_LIC-3-COMM_FAILED: Communications failure with the Cisco Smart Software Manager (CSSM) : Fail to send out Call Home HTTP message.`
`%SMART_LIC-3-AUTH_RENEW_FAILED: Authorization renewal with the Cisco Smart Software Manager (CSSM) : Communication message send error for udi <>`
`%SMART_LIC-3-AGENT_REG_FAILED: Smart Agent for Licensing Registration with the Cisco Smart Software Manager (CSSM) failed: Fail to send out Call Home HTTP message.`
`%CALL_HOME-5-SL_MESSAGE_FAILED: Fail to send out Smart Licensing message to: https://tools.cisco.com/its/service/oddce/services/DDCEService (ERR 205 : Request Aborted)`
`%CALL_HOME-5-SL_MESSAGE_FAILED: Fail to send out Smart Licensing message to: https://tools.cisco.com/its/service/oddce/services/DDCEService (ERR 207 : Connection time out)`
  

### Workaround/Solution
  

Cisco has migrated from the QuoVadis Root CA 2 to the IdenTrust Commercial Root CA 1 for SSL certificates. Cisco recommends these two options to add the new IdenTrust Commercial Root CA 1 certificate to the affected devices.
  * Software Upgrade
  * Manual Certificate Update


**Software Upgrade**
For Cisco IOS XE-based products, upgrade the software to any of the fixed releases - 16.12.6, 17.3.4, 17.4.2, 17.5.1, 17.6.1, 17.7.1 or later to resolve the root CA certificate issue for affected platforms.
**Manual Certificate Update**
In order to resolve the issue without a software upgrade, you can implement either of these workarounds.
**Workaround 1**
For Cisco IOS XE-based products, use the PKI Trustpool Management feature in order to resolve the issue without an upgrade to the Cisco IOS XE software.
The IdenTrust Commercial Root CA 1 certificate is included in the latest **ios_core.p7b** file available at http://www.cisco.com/security/pki/trs/ios_core.p7b.
Enter these commands in order to auto-import the IdenTrust Commercial Root CA 1 certificate.
  * Enter this CLI command to download the IdenTrust Commercial Root CA 1 certificate file from Cisco and manually import into the product's truststore. 
`Device(config)# **crypto pki trustpool import url http://www.cisco.com/security/pki/trs/ios_core.p7b**`
  * If the "ios_core.p7b" file was previously copied to the product's flash, enter this CLI command to import the certificates file into the truststore. 
`Device(config)# **crypto pki trustpool import url flash:ios_core.p7b**`


**Workaround 2**
Use this workaround to manually import the IdenTrust Commercial Root CA 1 from the text below into the product's trust store. The IdenTrust Root CA 1 shown below complies with sha1WithRSAEncryption signature algorithm requirements.
  1. Use a simple text editor, such as Notepad, and copy the certificate text (without the BEGIN CERTIFICATE and END CERTIFICATE lines).
Manual Update of Trustpool via Terminal

```
-----BEGIN CERTIFICATE-----
MIIFYDCCA0igAwIBAgIQCgFCgAAAAUUjyES1AAAAAjANBgkqhkiG9w0BAQsFADBK
MQswCQYDVQQGEwJVUzESMBAGA1UEChMJSWRlblRydXN0MScwJQYDVQQDEx5JZGVu
VHJ1c3QgQ29tbWVyY2lhbCBSb290IENBIDEwHhcNMTQwMTE2MTgxMjIzWhcNMzQw
MTE2MTgxMjIzWjBKMQswCQYDVQQGEwJVUzESMBAGA1UEChMJSWRlblRydXN0MScw
JQYDVQQDEx5JZGVuVHJ1c3QgQ29tbWVyY2lhbCBSb290IENBIDEwggIiMA0GCSqG
SIb3DQEBAQUAA4ICDwAwggIKAoICAQCnUBneP5k91DNG8W9RYYKyqU+PZ4ldhNlT
3Qwo2dfw/66VQ3KZ+bVdfIrBQuExUHTRgQ18zZshq0PirK1ehm7zCYofWjK9ouuU
+ehcCuz/mNKvcbO0U59Oh++SvL3sTzIwiEsXXlfEU8L2ApeN2WIrvyQfYo3fw7gp
S0l4PJNgiCL8mdo2yMKi1CxUAGc1bnO/AljwpN3lsKImesrgNqUZFvX9t++uP0D1
bVoE/c40yiTcdCMbXTMTEl3EASX2MN0CXZ/g1Ue9tOsbobtJSdifWwLziuQkkORi
T0/Br4sOdBeo0XKIanoBScy0RnnGF7HamB4HWfp1IYVl3ZBWzvurpWCdxJ35UrCL
vYf5jysjCiN2O/cz4ckA82n5S6LgTrx+kzmEB/dEcH7+B1rlsazRGMzyNeVJSQjK
Vsk9+w8YfYs7wRPCTY/JTw436R+hDmrfYi7LNQZReSzIJTj0+kuniVyc0uMNOYZK
dHzVWYfCP04MXFL0PfdSgvHqo6z9STQaKPNBiDoT7uje/5kdX7rL6B7yuVBgwDHT
c+XvvqDtMwt0viAgxGds8AgDelWAf0ZOlqf0Hj7h9tgJ4TNkK2PXMl6f+cB7D3hv
l7yTmvmcEpB4eoCHFddydJxVdHixuuFucAS6T6C6aMN7/zHwcz09lCqxC0EOoP5N
iGVreTO01wIDAQABo0IwQDAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUwAwEB
/zAdBgNVHQ4EFgQU7UQZwNPwBovupHu+QucmVMiONnYwDQYJKoZIhvcNAQELBQAD
ggIBAA2ukDL2pkt8RHYZYR4nKM1eVO8lvOMIkPkp165oCOGUAFjvLi5+U1KMtlwH
6oi6mYtQlNeCgN9hCQCTrQ0U5s7B8jeUeLBfnLOic7iPBZM4zY0+sLj7wM+x8uwt
LRvM7Kqas6pgghstO8OEPVeKlh6cdbjTMM1gCIOQ045U8U1mwF10A0Cj7oV+wh93
nAbowacYXVKV7cndJZ5t+qntozo00Fl72u1Q8zW/7esUTTHHYPTa8Yec4kjixsU3
+wYQ+nVZZjFHKdp2mhzpgq7vmrlR94gjmmmVYjzlVYA211QC//G5Xc7UI2/YRYRK
W2XviQzdFKcgyxilJbQN+QHwotL0AMh0jqEqSI5l2xPE4iUXfeu+h1sXIFRRk0pT
AwvsXcoz7WL9RccvW9xYoIA55vrX/hMUpu09lEpCdNTDd1lzzY9GvlU47/rokTLq
l1gEIt44w8y8bckzOmoKaT+gyOpyj4xjhiO9bTyWnpXgSUyqorkqG5w2gXjtw+hG
4iZZRHUe2XWJUc0QhJ1hYMtd+ZciTY6Y5uN/9lu7rs3KSoFrXgvzUeF0K+l+J6fZ
mUlO+KWA2yUPHGNiiskzZ2s8EIPGrd6ozRaOjfAHN3Gf8qv8QfXBi+wAN10J5U6A
7/qxXDgGpRtK4dw4LTzcqx+QGtVKnO7RcGzM7vRX+Bi6hG6H
-----END CERTIFICATE-----
```

  2. In order to enter the configuration mode, enter the `**config t**`command.
  3. Enter the `**crypto pki trustpool import terminal**`command.
  4. Paste the copied PEM-formatted CA certificate and press Enter two times. The system should respond with "% PEM files import succeeded".
  5. Enter the `**exit**`command.
  6. In order to write to memory, enter the `**wr mem**`command.
  7. Enter the `**show crypto pki trustpool**`command. The output should now contain the IdenTrust certificate.


See this example:

```
Device#**config t**
Enter configuration commands, one per line. End with CNTL/Z.
Switch(config)#**crypto pki trustpool import terminal**
% Enter PEM-formatted CA certificate.
% End with a blank line or "quit" on a line by itself.
MIIFYDCCA0igAwIBAgIQCgFCgAAAAUUjyES1AAAAAjANBgkqhkiG9w0BAQsFADBK
MQswCQYDVQQGEwJVUzESMBAGA1UEChMJSWRlblRydXN0MScwJQYDVQQDEx5JZGVu
VHJ1c3QgQ29tbWVyY2lhbCBSb290IENBIDEwHhcNMTQwMTE2MTgxMjIzWhcNMzQw
MTE2MTgxMjIzWjBKMQswCQYDVQQGEwJVUzESMBAGA1UEChMJSWRlblRydXN0MScw
JQYDVQQDEx5JZGVuVHJ1c3QgQ29tbWVyY2lhbCBSb290IENBIDEwggIiMA0GCSqG
SIb3DQEBAQUAA4ICDwAwggIKAoICAQCnUBneP5k91DNG8W9RYYKyqU+PZ4ldhNlT
3Qwo2dfw/66VQ3KZ+bVdfIrBQuExUHTRgQ18zZshq0PirK1ehm7zCYofWjK9ouuU
+ehcCuz/mNKvcbO0U59Oh++SvL3sTzIwiEsXXlfEU8L2ApeN2WIrvyQfYo3fw7gp
S0l4PJNgiCL8mdo2yMKi1CxUAGc1bnO/AljwpN3lsKImesrgNqUZFvX9t++uP0D1
bVoE/c40yiTcdCMbXTMTEl3EASX2MN0CXZ/g1Ue9tOsbobtJSdifWwLziuQkkORi
T0/Br4sOdBeo0XKIanoBScy0RnnGF7HamB4HWfp1IYVl3ZBWzvurpWCdxJ35UrCL
vYf5jysjCiN2O/cz4ckA82n5S6LgTrx+kzmEB/dEcH7+B1rlsazRGMzyNeVJSQjK
Vsk9+w8YfYs7wRPCTY/JTw436R+hDmrfYi7LNQZReSzIJTj0+kuniVyc0uMNOYZK
dHzVWYfCP04MXFL0PfdSgvHqo6z9STQaKPNBiDoT7uje/5kdX7rL6B7yuVBgwDHT
c+XvvqDtMwt0viAgxGds8AgDelWAf0ZOlqf0Hj7h9tgJ4TNkK2PXMl6f+cB7D3hv
l7yTmvmcEpB4eoCHFddydJxVdHixuuFucAS6T6C6aMN7/zHwcz09lCqxC0EOoP5N
iGVreTO01wIDAQABo0IwQDAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUwAwEB
/zAdBgNVHQ4EFgQU7UQZwNPwBovupHu+QucmVMiONnYwDQYJKoZIhvcNAQELBQAD
ggIBAA2ukDL2pkt8RHYZYR4nKM1eVO8lvOMIkPkp165oCOGUAFjvLi5+U1KMtlwH
6oi6mYtQlNeCgN9hCQCTrQ0U5s7B8jeUeLBfnLOic7iPBZM4zY0+sLj7wM+x8uwt
LRvM7Kqas6pgghstO8OEPVeKlh6cdbjTMM1gCIOQ045U8U1mwF10A0Cj7oV+wh93
nAbowacYXVKV7cndJZ5t+qntozo00Fl72u1Q8zW/7esUTTHHYPTa8Yec4kjixsU3
+wYQ+nVZZjFHKdp2mhzpgq7vmrlR94gjmmmVYjzlVYA211QC//G5Xc7UI2/YRYRK
W2XviQzdFKcgyxilJbQN+QHwotL0AMh0jqEqSI5l2xPE4iUXfeu+h1sXIFRRk0pT
AwvsXcoz7WL9RccvW9xYoIA55vrX/hMUpu09lEpCdNTDd1lzzY9GvlU47/rokTLq
l1gEIt44w8y8bckzOmoKaT+gyOpyj4xjhiO9bTyWnpXgSUyqorkqG5w2gXjtw+hG
4iZZRHUe2XWJUc0QhJ1hYMtd+ZciTY6Y5uN/9lu7rs3KSoFrXgvzUeF0K+l+J6fZ
mUlO+KWA2yUPHGNiiskzZ2s8EIPGrd6ozRaOjfAHN3Gf8qv8QfXBi+wAN10J5U6A
7/qxXDgGpRtK4dw4LTzcqx+QGtVKnO7RcGzM7vRX+Bi6hG6H
% PEM files import succeeded.
Device(config)#**exit**
Device#**wr mem**
Destination filename [startup-config]?
Building configuration...
[OK]

Device#**show crypto pki trustpool**
Load for five secs: 30%/2%; one minute: 25%; five minutes: 27%
Time source is NTP, 23:40:09.537 CST Sat Mar 6 2021
CA Certificate
  Status: Available
  Certificate Serial Number (hex): 0A0142800000014523C844B500000002
  Certificate Usage: Signature
  Issuer: 
    cn=IdenTrust Commercial Root CA 1
    o=IdenTrust
    c=US
  Subject: 
    cn=IdenTrust Commercial Root CA 1
    o=IdenTrust
    c=US
  Validity Date: 
    start date: 02:12:23 CST Jan 17 2014
    end   date: 02:12:23 CST Jan 17 2034
  Associated Trustpoints: Trustpool 
  Trustpool: Downloaded


CA Certificate
  Status: Available
  Certificate Serial Number (hex): 0509
  Certificate Usage: Signature
  Issuer: 
    cn=QuoVadis Root CA 2
    o=QuoVadis Limited
    c=BM
  Subject: 
    cn=QuoVadis Root CA 2
    o=QuoVadis Limited
    c=BM
  Validity Date: 
    start date: 02:27:00 CST Nov 25 2006
    end   date: 02:23:33 CST Nov 25 2031
  Associated Trustpoints: Trustpool
  Trustpool: Built-In
<<output snipped>>
```

**Workaround 3**
This workaround is only applicable to devices that run in SD WAN mode.
  1. Place the certificate under bootflash:. 
Go to shell under the bootflash directory and create a file named "Test123.ca". This file HAS to be named as <_Trustpoint-name_ >.ca. Add this certificate content to the file:

```
-----BEGIN CERTIFICATE-----
MIIFYDCCA0igAwIBAgIQCgFCgAAAAUUjyES1AAAAAjANBgkqhkiG9w0BAQsFADBK
MQswCQYDVQQGEwJVUzESMBAGA1UEChMJSWRlblRydXN0MScwJQYDVQQDEx5JZGVu
VHJ1c3QgQ29tbWVyY2lhbCBSb290IENBIDEwHhcNMTQwMTE2MTgxMjIzWhcNMzQw
MTE2MTgxMjIzWjBKMQswCQYDVQQGEwJVUzESMBAGA1UEChMJSWRlblRydXN0MScw
JQYDVQQDEx5JZGVuVHJ1c3QgQ29tbWVyY2lhbCBSb290IENBIDEwggIiMA0GCSqG
SIb3DQEBAQUAA4ICDwAwggIKAoICAQCnUBneP5k91DNG8W9RYYKyqU+PZ4ldhNlT
3Qwo2dfw/66VQ3KZ+bVdfIrBQuExUHTRgQ18zZshq0PirK1ehm7zCYofWjK9ouuU
+ehcCuz/mNKvcbO0U59Oh++SvL3sTzIwiEsXXlfEU8L2ApeN2WIrvyQfYo3fw7gp
S0l4PJNgiCL8mdo2yMKi1CxUAGc1bnO/AljwpN3lsKImesrgNqUZFvX9t++uP0D1
bVoE/c40yiTcdCMbXTMTEl3EASX2MN0CXZ/g1Ue9tOsbobtJSdifWwLziuQkkORi
T0/Br4sOdBeo0XKIanoBScy0RnnGF7HamB4HWfp1IYVl3ZBWzvurpWCdxJ35UrCL
vYf5jysjCiN2O/cz4ckA82n5S6LgTrx+kzmEB/dEcH7+B1rlsazRGMzyNeVJSQjK
Vsk9+w8YfYs7wRPCTY/JTw436R+hDmrfYi7LNQZReSzIJTj0+kuniVyc0uMNOYZK
dHzVWYfCP04MXFL0PfdSgvHqo6z9STQaKPNBiDoT7uje/5kdX7rL6B7yuVBgwDHT
c+XvvqDtMwt0viAgxGds8AgDelWAf0ZOlqf0Hj7h9tgJ4TNkK2PXMl6f+cB7D3hv
l7yTmvmcEpB4eoCHFddydJxVdHixuuFucAS6T6C6aMN7/zHwcz09lCqxC0EOoP5N
iGVreTO01wIDAQABo0IwQDAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUwAwEB
/zAdBgNVHQ4EFgQU7UQZwNPwBovupHu+QucmVMiONnYwDQYJKoZIhvcNAQELBQAD
ggIBAA2ukDL2pkt8RHYZYR4nKM1eVO8lvOMIkPkp165oCOGUAFjvLi5+U1KMtlwH
6oi6mYtQlNeCgN9hCQCTrQ0U5s7B8jeUeLBfnLOic7iPBZM4zY0+sLj7wM+x8uwt
LRvM7Kqas6pgghstO8OEPVeKlh6cdbjTMM1gCIOQ045U8U1mwF10A0Cj7oV+wh93
nAbowacYXVKV7cndJZ5t+qntozo00Fl72u1Q8zW/7esUTTHHYPTa8Yec4kjixsU3
+wYQ+nVZZjFHKdp2mhzpgq7vmrlR94gjmmmVYjzlVYA211QC//G5Xc7UI2/YRYRK
W2XviQzdFKcgyxilJbQN+QHwotL0AMh0jqEqSI5l2xPE4iUXfeu+h1sXIFRRk0pT
AwvsXcoz7WL9RccvW9xYoIA55vrX/hMUpu09lEpCdNTDd1lzzY9GvlU47/rokTLq
l1gEIt44w8y8bckzOmoKaT+gyOpyj4xjhiO9bTyWnpXgSUyqorkqG5w2gXjtw+hG
4iZZRHUe2XWJUc0QhJ1hYMtd+ZciTY6Y5uN/9lu7rs3KSoFrXgvzUeF0K+l+J6fZ
mUlO+KWA2yUPHGNiiskzZ2s8EIPGrd6ozRaOjfAHN3Gf8qv8QfXBi+wAN10J5U6A
7/qxXDgGpRtK4dw4LTzcqx+QGtVKnO7RcGzM7vRX+Bi6hG6H
-----END CERTIFICATE-----
```

  2. Enter the `**config**`command.
```
crypto pki trustpoint Test123
	enrollment url bootflash:
	Revocation-check none
	Fingerprint DF717EAA4AD94EC9558499602D48DE5FBCF03A25
	Commit
```

  3. From exec mode, enter `**crypto pki authenticate Test123**`.

  

### For More Information
  

These products are affected:
  * Cisco 1000 Series Integrated Services Routers
  * Cisco 1100 Integrated Services Router
  * Cisco 4000 Series Integrated Services Routers
  * Cisco 4221 Integrated Services Router
  * Cisco 4321 Integrated Services Router
  * Cisco 4331 Integrated Services Router
  * Cisco 4351 Integrated Services Router
  * Cisco 4431 Integrated Services Router
  * Cisco 4451-X Integrated Services Router
  * Cisco 4461 Integrated Services Router
  * Cisco ASR 1000 Series Aggregation Services Routers
  * Cisco ASR 1000 Series IOS XE SD-WAN
  * Cisco ASR 1000 Series Route Processor (RP2)
  * Cisco ASR 1000 Series Route Processor (RP3)
  * Cisco ASR 1001-HX Router
  * Cisco ASR 1001-X Router
  * Cisco ASR 1002-HX Router
  * Cisco ASR 1002-X Router
  * Cisco ASR 1004 Router
  * Cisco ASR 1006 Router
  * Cisco ASR 1006-X Router
  * Cisco ASR 1009-X Router
  * Cisco ASR 1013 Router
  * Cisco Catalyst 1101 Rugged Router
  * Cisco Catalyst 3650 Series Switches
  * Cisco Catalyst 3850 Series Switches
  * Cisco Catalyst 8000V Edge Software
  * Cisco Catalyst 8200 Series Edge Platforms
  * Cisco Catalyst 8300 Series Edge Platforms
  * Cisco Catalyst 8500 Series Edge Platforms
  * Cisco Catalyst 8500L Series Edge Platforms
  * Cisco Catalyst 9200 Series Switches
  * Cisco Catalyst 9200L Switch Stack
  * Cisco Catalyst 9300 Series Switches
  * Cisco Catalyst 9300L Series Switches
  * Cisco Catalyst 9400 Series Switches
  * Cisco Catalyst 9404R Switch
  * Cisco Catalyst 9407R Switch
  * Cisco Catalyst 9410R Switch
  * Cisco Catalyst 9500 Series Switches
  * Cisco Catalyst 9600 Series Switches
  * Cisco Catalyst 9606R Switch
  * Cisco Catalyst 9800 Wireless Controllers for Cloud
  * Cisco Catalyst 9800-40 Wireless Controller
  * Cisco Catalyst 9800-80 Wireless Controller
  * Cisco Catalyst 9800-CL Wireless Controller for Cloud
  * Cisco Catalyst 9800-L Wireless Controller
  * Cisco Catalyst 9800-L-C Wireless Controller
  * Cisco Catalyst 9800-L-F Wireless Controller
  * Cisco Catalyst IR1100 Rugged Series Routers
  * Cisco Cloud Services Router 1000V Series
  * Cisco CSR 1000V Series IOS XE SD-WAN
  * Cisco Embedded Wireless Controller on Catalyst 9115AX Access Points
  * Cisco Embedded Wireless Controller on Catalyst 9117AX Access Points
  * Cisco Embedded Wireless Controller on Catalyst 9120AX Access Points
  * Cisco Embedded Wireless Controller on Catalyst 9130AX Access Points
  * Cisco Embedded Wireless Controller on Catalyst Access Points
  * Cisco ESR6300 Embedded Series Router
  * Cisco ESR6300 Embedded Series Routers
  * Cisco Integrated Services Virtual Router
  * Cisco ISR 1000 Series IOS XE SD-WAN
  * Cisco ISR 4000 Series IOS XE SD-WAN
  * Cisco Route Processors and Route Switch Processors
  * Cisco XE SD-WAN Routers

  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 2.4  | Added the Additional Information Section  | —  | 2022-JUN-07  |  
| 2.3  | Updated the Workaround/Solution Section  | —  | 2022-APR-19  |  
| 2.2  | Updated the Products Affected Section  | —  | 2022-MAR-03  |  
| 2.0  | Updated the Problem Description, Background, Problem Symptom, and Workaround/Solution Sections  | —  | 2022-FEB-25  |  
| 1.0  | Initial Release  | —  | 2022-JAN-24  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications)
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72323.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Customers Also Viewed
  * [Upgrading Catalyst 9400 Switches](https://www.cisco.com/c/en/us/support/docs/switches/catalyst-9400-series-switches/222283-upgrading-catalyst-9400-switches.html)
  * [Cisco Catalyst 9400 Series Switches Hardware Installation Guide --- Specifications](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9400/hardware/install/b_c9400_hig/b_c9400_hig_chapter_0110.html)
  * [Cisco Catalyst 9400 Series Switches Hardware Installation Guide --- Product Overview](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9400/hardware/install/b_c9400_hig/b_c9400_hig_chapter_00.html)
  * [Troubleshoot Power Supplies on Catalyst 9000 Switches](https://www.cisco.com/c/en/us/support/docs/switches/nexus-9000-series-switches/220196-troubleshoot-power-supplies-on-catalyst.html)
  * + Show 1 More


### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72323.html)
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

+ Show All 15 Products
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/723/fn72323.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72323.html)
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
