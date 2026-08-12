  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74221.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74221.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74221.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74221.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74221.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Switches](https://www.cisco.com/c/en/us/support/switches/category.html)
  * [Cisco Catalyst 9200 Series Switches](https://www.cisco.com/c/en/us/support/switches/catalyst-9200-r-series-switches/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/switches/catalyst-9200-r-series-switches/products-field-notices-list.html)


# Field Notice: FN74221 - Expired Device Certificate Causes Umbrella DNS Connections to Fail in Cisco Catalyst 9200 and 9300 Switches - Configuration Change Recommended
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/742/fn74221.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74221.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/742/fn74221.html)


Updated:January 17, 2025
Document ID:FN74221
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
High
**Impact Rating:**
High
**First Published:**
2025-Jan-17
**Last Published:**
2025-Jan-17
**Revision:**
1.0
**Cisco Bug IDs:**
  * [CSCwm33388](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwm33388)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  

  
  
  
| Affected Software Product  | Affected Release  | Affected Release Number  | Comments  |  
| --- | --- | --- | --- |  
| IOS XE Software  | 17  | 17.10.1, 17.11.1, 17.12.1, 17.12.2, 17.12.3, 17.12.4, 17.13.1, 17.14.1, 17.15.1, 17.15.2, 17.7.1, 17.8.1, 17.9.1, 17.9.2, 17.9.3, 17.9.4, 17.9.4a, 17.9.5, 17.9.6, 17.9.6a  | 17.7.1: All the releases post 17.7.1 are impacted.  |  
  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwm33388](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwm33388)  | Issue Detected as Resolved - Certificate with Common Name: "ISRG Root X1" will expire soon  |  
  

### Problem Description
  

The digital certificate that is used by Cisco Catalyst 9200 and 9300 Switches to register with Cisco Umbrella DNS expired on September 30, 2024. Cisco Catalyst 9200 and 9300 Switches with the expired certificate will fail to register with the Cisco Umbrella DNS service.
  

### Background
  

The Cisco Umbrella DNS security solution uses digital certificates during the SSL handshake to establish secure HTTPS connections for device registration. The current SSL certificate on affected Cisco Catalyst 9200 and 9300 Switches expired on September 30, 2024.
This problem affects Cisco Catalyst 9200 and 9300 Switches when they are configured to use Cisco Umbrella API keys for registration.
**Note:** This issue does not affect customers who are using token-based authentication for Cisco Umbrella DNS registration. 
  

### Problem Symptom
  

Affected Cisco Catalyst 9200 and 9300 Switches with expired Cisco Umbrella root certificate authority (CA) certificates cannot establish secure connections with Cisco Umbrella DNS for device registration. Because affected devices are not registered with the Cisco Umbrella DNS service, user DNS requests are not redirected to the Cisco Umbrella domain server by the affected switches for DNS security policy enforcement. DNS requests from the users of affected switches will not be dropped and will be serviced by the DNS domain server that is configured on the devices.
**Note:** Cisco Catalyst 9200 and 9300 Switches that are configured for Cisco Umbrella DNS security and that are already in operation will not be impacted until reboot. The expired certificate is used only during device registration with the Cisco Umbrella DNS service, not for individual DNS requests. Device registration occurs when the CiscoUmbrella DNS service is initially configured or when the configured device is rebooted.
  

### Workaround/Solution
  

Affected devices must have the affected certificate replaced with a new Cisco Umbrella root certificate that is valid until the year 2035. Customers who do not currently use Cisco Umbrella DNS but who expect to deploy it in the future can replace the affected certificate by following the below mentioned steps.
For affected devices, the following X1 certificate must be downloaded and installed. 
> `-----BEGIN CERTIFICATE-----`
> `MIIFazCCA1OgAwIBAgIRAIIQz7DSQONZRGPgu2OCiwAwDQYJKoZIhvcNAQELBQAw`
> `TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh`
> `cmNoIEdyb3VwMRUwEwYDVQQDEwxJU1JHIFJvb3QgWDEwHhcNMTUwNjA0MTEwNDM4`
> `WhcNMzUwNjA0MTEwNDM4WjBPMQswCQYDVQQGEwJVUzEpMCcGA1UEChMgSW50ZXJu`
> `ZXQgU2VjdXJpdHkgUmVzZWFyY2ggR3JvdXAxFTATBgNVBAMTDElTUkcgUm9vdCBY`
> `MTCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAK3oJHP0FDfzm54rVygc`
> `h77ct984kIxuPOZXoHj3dcKi/vVqbvYATyjb3miGbESTtrFj/RQSa78f0uoxmyF+`
> `0TM8ukj13Xnfs7j/EvEhmkvBioZxaUpmZmyPfjxwv60pIgbz5MDmgK7iS4+3mX6U`
> `A5/TR5d8mUgjU+g4rk8Kb4Mu0UlXjIB0ttov0DiNewNwIRt18jA8+o+u3dpjq+sW`
> `T8KOEUt+zwvo/7V3LvSye0rgTBIlDHCNAymg4VMk7BPZ7hm/ELNKjD+Jo2FR3qyH`
> `B5T0Y3HsLuJvW5iB4YlcNHlsdu87kGJ55tukmi8mxdAQ4Q7e2RCOFvu396j3x+UC`
> `B5iPNgiV5+I3lg02dZ77DnKxHZu8A/lJBdiB3QW0KtZB6awBdpUKD9jf1b0SHzUv`
> `KBds0pjBqAlkd25HN7rOrFleaJ1/ctaJxQZBKT5ZPt0m9STJEadao0xAH0ahmbWn`
> `OlFuhjuefXKnEgV4We0+UXgVCwOPjdAvBbI+e0ocS3MFEvzG6uBQE3xDk3SzynTn`
> `jh8BCNAw1FtxNrQHusEwMFxIt4I7mKZ9YIqioymCzLq9gwQbooMDQaHWBfEbwrbw`
> `qHyGO0aoSCqI3Haadr8faqU9GY/rOPNk3sgrDQoo``//fb4hVC1CLQJ13hef4Y53CI`
> `rU7m2Ys6xt0nUW7/vGT1M0NPAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNV`
> `HRMBAf8EBTADAQH/MB0GA1UdDgQWBBR5tFnme7bl5AFzgAiIyBpY9umbbjANBgkq`
> `hkiG9w0BAQsFAAOCAgEAVR9YqbyyqFDQDLHYGmkgJykIrGF1XIpu+ILlaS/V9lZL`
> `ubhzEFnTIZd+50xx+7LSYK05qAvqFyFWhfFQDlnrzuBZ6brJFe+GnY+EgPbk6ZGQ`
> `3BebYhtF8GaV0nxvwuo77x/Py9auJ/GpsMiu/X1+mvoiBOv/2X/qkSsisRcOj/KK`
> `NFtY2PwByVS5uCbMiogziUwthDyC3+6WVwW6LLv3xLfHTjuCvjHIInNzktHCgKQ5`
> `ORAzI4JMPJ+GslWYHb4phowim57iaztXOoJwTdwJx4nLCgdNbOhdjsnvzqvHu7Ur`
> `TkXWStAmzOVyyghqpZXjFaH3pO3JLF+l+/+sKAIuvtd7u+Nxe5AW0wdeRlN8NwdC`
> `jNPElpzVmbUq4JUagEiuTDkHzsxHpFKVK7q4+63SM1N95R1NbdWhscdCb+ZAJzVc`
> `oyi3B43njTOQ5yOf+1CceWxG1bQVs5ZufpsMljq4Ui0/1lvh+wjChP4kqKOJ2qxq`
> `4RgqsahDYVvTH9w7jXbyLeiNdd8XM2w9U/t7y0Ff/9yi0GE44Za4rF2LN9d11TPA`
> `mRGunUHBcnWEvgJBQl9nJEiU0Zsnvgc/ubhPgXRR4Xq37Z0j4r7g1SgEEzwxA57d`
> `emyPxgcYxn/eR44/KJ4EBs+lVDR3veyJm+kXQ99b21/+jh5Xos1AnX5iItreGCc=`
> `-----END CERTIFICATE-----`
This certificate can also be downloaded from <https://letsencrypt.org/certs/isrgrootx1.pem>.
For affected Cisco devices, complete the following installation instructions:
  1. Download the new, unexpired certificate from <https://letsencrypt.org/certs/isrgrootx1.pem>.
  2. Log in to the affected device.
  3. Remove existing enrolled trustpoint using the following CLI input:  

> 
```
Switch(config)#no crypto pki trustpoint ISRGRootX1                                                                                                                                                                                                                                                                                                                                          
> % Removing an enrolled trustpoint will destroy all certificates                                                                                                                                                                                                                                                                                                                                
>  received from the related Certificate Authority.                                                                                                                                                                                                                                                                                                                                              
>                                                                                                                                                                                                                                                                                                                                                                                                
> Are you sure you want to do this? [yes/no]: yes                                                                                                                                                                                                                                                                                                                                                
> % Be sure to ask the CA administrator to revoke your certificates.
```

  4. Configure a trustpoint. If one is not already present, create a trustpoint that will be used to store the certificate using the following CLI input: 
> 
```
Switch# configure terminal  
> Switch(config)# crypto pki trustpoint **<MY_TRUSTPOINT_NAME>**  
> Switch(config-trustpoint)# enrollment terminal  
> Switch(config-trustpoint)# revocation-check none  
> Switch(config-trustpoint)# exit  
> Switch(config)#
```

Replace **< MY_TRUSTPOINT_NAME>** with the name you want to assign to your trustpoint.
  5. Use the **crypto pki authenticate** CLI config command to import the certificate by pasting in the text from the certificate file that was downloaded in Step 1. 
> 
```
Switch(config)# crypto pki authenticate <MY_TRUSTPOINT_NAME>  
>    
> Enter the base 64 encoded CA certificate.  
> End with a blank line or the word "quit" on a line by itself  
> [paste certificate text here]  
> Certificate has the following attributes:  
>        Fingerprint MD5: 0CD2F9E0 DA1773E9 ED864DA5 E370E74E   
>       Fingerprint SHA1: CABD2A79 A1076A31 F21D2536 35CB039D 4329A5E8   
> % Do you accept this certificate? [yes/no]: yes  
> Trustpoint CA certificate accepted.  
> % Certificate successfully imported   
> Switch(config)#exit  
> Switch#
```


  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.0  | Initial Release  | —  | 2025-JAN-17  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74221.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Customers Also Viewed
  * [Perform Password Recovery on Catalyst 9000 Series Switches](https://www.cisco.com/c/en/us/support/docs/switches/catalyst-9200-series-switches/223262-perform-password-recovery-on-catalyst.html)
  * [Cisco Catalyst 9200CX Compact Series Switches Hardware Installation Guide --- Product Overview](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9200/hardware/install/b-c9200cx-hig/b-c9200cx-product-overview.html)
  * [Upgrade Catalyst 9200 switches](https://www.cisco.com/c/en/us/support/docs/switches/catalyst-9200-series-switches/222282-upgrading-catalyst-9200-switches.html)
  * [Cisco Catalyst 9200 Series Switches Hardware Installation Guide --- Product Overview](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9200/hardware/install/b-c9200-hig/product_overview.html)
  * [Cisco Catalyst 9200CX Compact Series Switches Hardware Installation Guide --- Installing a Compact Switch](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9200/hardware/install/b-c9200cx-hig/Installing-a-compact-switch.html)
  * + Show 2 More


### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74221.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Catalyst 9200 Series Switches](https://www.cisco.com/c/en/us/support/switches/catalyst-9200-r-series-switches/series.html)
  * [Catalyst 9300 Series Switches](https://www.cisco.com/c/en/us/support/switches/catalyst-9300-series-switches/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/742/fn74221.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74221.html)
