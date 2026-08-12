  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74135.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74135.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74135.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74135.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74135.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Switches](https://www.cisco.com/c/en/us/support/switches/category.html)
  * [Cisco Catalyst 9400 Series Switches](https://www.cisco.com/c/en/us/support/switches/catalyst-9400-series-switches/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/switches/catalyst-9400-series-switches/products-field-notices-list.html)


# Field Notice: FN74135 - Cisco SUDI Certificate Expires When Registered to a PKI and Used to Configure Certain Functionalities on Catalyst 9000 Platforms - Workaround Provided
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/741/fn74135.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74135.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/741/fn74135.html)


Updated:May 14, 2024
Document ID:FN74135
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Product Name  | Description  | Comments  |  
| --- | --- | --- |  
| C9200-24P  | Catalyst 9200 24-port PoE+, Base Switch  | Catalyst 9200 - All Products are impacted. Some sample products are listed in this table   |  
| C9200-24PB  | Catalyst 9200 24-port PoE+, enhanced VRF, BASE PID  |   |  
| C9200-24PXG  | Catalyst 9200 24-port 8xmGig PoE+, Base Switch  |   |  
| C9200-24T  | Catalyst 9200 24-port data only, Base Switch  |   |  
| C9200-48P  | Catalyst 9200 48-port PoE+, Base Switch  |   |  
| C9200-48PB  | Catalyst 9200 48-port PoE+, Enhanced VRF. BASE PID  |   |  
| C9200-48PL  | Catalyst 9200 48-port Partial PoE+, Base Switch  |   |  
| C9200-48PXG  | Catalyst 9200 48-port 8xmGig PoE+, Base Switch  |   |  
| C9200-48T  | Catalyst 9200 48-port data only, Base Switch  |   |  
| C9200CX-12P-2X2G  | Catalyst 9000 Compact Switch 12-Port PoE+, 240W, Essentials  |   |  
| C9200CX-12P-2XGH  | Catalyst 9000 Compact Switch 12-Port PoE+, 240W,HVDC,Ess  |   |  
| C9200CX-12T-2X2G  | Catalyst 9000 Compact Switch 12-port Data Only, Essentials  |   |  
| C9200CX-8P-2X2G  | Catalyst 9000 Compact Switch 8 port PoE+, 240W, Essentials  |   |  
| C9200CX-8P-2XGH  | Catalyst 9000 Compact Switch 8 port PoE+, 240W,HVDC,Ess  |   |  
| C9200CX-8UXG-2X  | Catalyst 9000 Compact Switch 8-Port UPoE with 4xmGig,240W,E  |   |  
| C9200CX-8UXG-2XH  | Catalyst 9000 Compact Switch 8-Port UPoE with 4xmGig,HVDC,E  |   |  
| C9200L-24P-4G  | Catalyst 9200L 24-port PoE+, Base Switch  |   |  
| C9200L-24P-4X  | Catalyst 9200L 24-port PoE+, SFP+, Base Switch  |   |  
| C9200L-24PXG-2Y  | C9200L 24-port 8xmGig, 16x1G, 2x25G, PoE+,Base Switch  |   |  
| C9200L-24PXG-4X  | C9200L 24-port 8xmGig, 16x1G, 4x10G, PoE+,Base Switch  |   |  
| C9200L-24T-4G  | Catalyst 9200L 24-port data only, Base Switch  |   |  
| C9200L-24T-4X  | Catalyst 9200L 24-port data only, SFP+ ,Base Switch  |   |  
| C9200L-48P-4G  | Catalyst 9200L 48-port PoE+, Base Switch  |   |  
| C9200L-48P-4X  | Catalyst 9200L 48-port PoE+, SFP+, Base Switch  |   |  
| C9200L-48PL-4G  | Catalyst 9200L 48-port Partial PoE+, Base Switch  |   |  
| C9200L-48PL-4X  | Catalyst 9200L 48-port Partial PoE+, SFP+, Base Switch  |   |  
| C9200L-48PXG-2Y  | C9200L 48-port 8xmGig, 40x1G, 2x25G PoE+,Base Switch  |   |  
| C9200L-48PXG-4X  | C9200L 48-port 12xmGig, 36x1G, 4x10G PoE+,Base Switch  |   |  
| C9200L-48T-4G  | Catalyst 9200L 48-port data only, Base Switch  |   |  
| C9200L-48T-4X  | Catalyst 9200L 48-port data only, SFP+ ,Base Switch  |   |  
| C9300-24H  | Catalyst 9300 24-port UPOE+, Base PID-Non-Shippable  | Catalyst 9300 - All Products are impacted. Some sample products are listed in this table   |  
| C9300-24P  | Catalyst 9300 24-port PoE+,Base switch  |   |  
| C9300-24S  | Catalyst 9300 24-port Fiber Base switch  |   |  
| C9300-24T  | Catalyst 9300 24-port data only,Base switch  |   |  
| C9300-24U  | Catalyst 9300 24-port UPOE,Base switch  |   |  
| C9300-24UB  | Catalyst Deep Buffer 9300 24-port UPOE, Base PID  |   |  
| C9300-24UX  | Catalyst 9300 24-port mGig and UPOE, base switch  |   |  
| C9300-24UXB  | Catalyst 9300 Deep Buffer 24p mGig, UPOE, Base PID  |   |  
| C9300-48H  | Catalyst 9300 48-port UPoE+, Base PID  |   |  
| C9300-48P  | Catalyst 9300 48-port PoE+,Base switch  |   |  
| C9300-48S  | Catalyst 9300 48-port Fiber , Base Switch  |   |  
| C9300-48T  | Catalyst 9300 48-port data only,Base switch  |   |  
| C9300-48U  | Catalyst 9300 48-port UPOE,Base switch  |   |  
| C9300-48UB  | Catalyst 9300 48-port UPOE Deep Buffer, Base PID  |   |  
| C9300-48UN  | Catalyst 9300 48-port of 5GbpsBase switch  |   |  
| C9300-48UXM  | Catalyst 9300 48-port(12 mGig&36 2.5Gbps), base switch  |   |  
| C9300L-24P-4G  | Catalyst 9300L 24p PoE ,4x1G Uplink, Base Switch  |   |  
| C9300L-24P-4X  | Catalyst 9300L 24p PoE ,4x10G Uplink, Base Switch  |   |  
| C9300L-24T-4G  | Catalyst 9300L 24p data ,4x1G Uplink, Base Switch  |   |  
| C9300L-24T-4X  | Catalyst 9300L 24p data ,4x10G Uplink, Base Switch  |   |  
| C9300L-24UXG-2Q  | Catalyst 9300L 24p, 8mGig ,2x40G Uplink, Base Switch  |   |  
| C9300L-24UXG-4X  | Catalyst 9300L 24p, 8mGig ,4x10G Uplink, Base Switch  |   |  
| C9300L-48P-4G  | Catalyst 9300L 48p PoE ,4x1G Uplink, Base Switch  |   |  
| C9300L-48P-4X  | Catalyst 9300L 48p PoE ,4x10G Uplink, Base Switch  |   |  
| C9300L-48PF-4G  | Catalyst 9300L 48p Full PoE+ ,4x1G Uplink, Base Switch  |   |  
| C9300L-48PF-4X  | Catalyst 9300L 48p Full PoE+ ,4x10G Uplink, Base Switch  |   |  
| C9300L-48T-4G  | Catalyst 9300L 48p data ,4x1G Uplink, Base Switch  |   |  
| C9300L-48T-4X  | Catalyst 9300L 48p data ,4x10G Uplink, Base Switch  |   |  
| C9300L-48UXG-2Q  | Catalyst 9300L 48p, 12mGig ,2x40G Uplink, Base Switch  |   |  
| C9300L-48UXG-4X  | Catalyst 9300L 48p, 12mGig ,4x10G Uplink, Base Switch  |   |  
| C9300LM-24U-4Y  | Catalyst 9300L Mini 24p UPoE, Base Switch  |   |  
| C9300LM-48T-4Y  | Catalyst 9300L Mini 48p Data, Base Switch  |   |  
| C9300LM-48U-4Y  | Catalyst 9300L Mini 48p UPoE, Base Switch  |   |  
| C9300LM-48UX-4Y  | Catalyst 9300L Mini 48p 8mGig, Base Switch  |   |  
| C9300X-12Y  | Catalyst 9300X 12x25G Fiber Ports, Base Switch  |   |  
| C9300X-24HX  | Catalyst 9300 24-port mGig UPoE+, Base PID  |   |  
| C9300X-24Y  | Catalyst 9300X 24x25G Fiber Ports, Base Switch  |   |  
| C9300X-48HX  | Catalyst 9300 48-port mGig UPoE+, Base PID  |   |  
| C9300X-48HXN  | Catalyst 9300 48-port, 8xmGig+40x5G 90W UPOE+, Base PID  |   |  
| C9300X-48TX  | Catalyst 9300 48-port mGig data only, Base PID  |   |  
| C9400-SUP-1  | Cisco Catalyst 9400 Series Supervisor 1 Module  | Catalyst 9400 - Only Supervisor Cards listed here are impacted.  |  
| C9400-SUP-1XL  | Cisco Catalyst 9400 Series Supervisor 1XL Module  |   |  
| C9400-SUP-1XL-Y  | Cisco Catalyst 9400 Series Supervisor 1XL with 25G Module  |   |  
| C9500-12Q  | Catalyst 9500 12-port 40G switch, Baseboard  | Catalyst 9500 - All Products are impacted. Some sample products are listed in this table   |  
| C9500-16X  | Catalyst 9500 16-port 10Gig switch, Baseboard  |   |  
| C9500-24Q  | Catalyst 9500 24-port 40G switch, Baseboard  |   |  
| C9500-24Y4C  | Catalyst 9500 Base PID  |   |  
| C9500-32C  | Catalyst 9500 Base PID  |   |  
| C9500-32QC  | Catalyst 9500 Base PID  |   |  
| C9500-40X  | Catalyst 9500 40-port 10Gig switch, Baseboard  |   |  
| C9500-48Y4C  | Catalyst 9500 Base PID  |   |  
| C9600-SUP-1  | Cisco Catalyst 9600 Series Supervisor 1 Module  | Catalyst 9600 - Only Supervisor Cards listed here are impacted.  |  
| C9600X-SUP-2  | Cisco Catalyst 9600 Series Supervisor 2 Module  |   |  
  
  

  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwd82114](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwd82114)  | Support for both HW SUDI type and SW SUDI type trustpoints initialized with IOS PKI.  |  
| [CSCwf94778](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwf94778)  | C9200 uses H/W SUDI cert expiry date as 2029 instead of 2099  |  
  

### Problem Description
  

A Cisco Secure Unique Device Identifier (SUDI) certificate that is registered to a public key infrastructure (PKI) and that is also used to configure certain functionalities will expire on a limited number of Cisco Catalyst 9000 Switching Family products (for more information on affected products, see the Products Affected section of this Field Notice). Any service that relies on a SUDI certificate to establish a secure connection might not work after the certificate expires.
  

### Background
  

SUDI is an X.509v3 certificate that maintains the product identifier and serial number. The identity is implemented at manufacturing and is linked to a publicly identifiable root certificate authority (CA). The SUDI can be used as an immutable identity for configuration, security, auditing, and management. 
The Cisco SUDI certificate, when registered to a PKI and used to configure certain functionalities on Cisco IOS XE Software, will expire on a limited number of Catalyst 9000 Switching products. Refer to the How to Identify Affected Products and Serial Number Validation sections of this Field Notice to identify affected devices. 
To determine if a SUDI trust point is used, enter the following command:
> 
```
Switch# show run |  CISCO_IDEVID_SUDI 
```

If there is no output, no impact is expected and **no further action is required.**
Customers can check the expiration date of the SUDI certificate on their device using the **show crypto pki certificates** command.
The SUDI expiration date is bolded in the sample output below:
> 
```
Switch#show crypto pki certificates  
> Certificate  
> 
  Status: Available  
> 
  Certificate Serial Number (hex): 0380EC27  
> 
  Certificate Usage: General Purpose  
> 
  Issuer:  
> 
    cn=ACT2 SUDI CA  
> 
    o=Cisco  
> 
  Subject:  
> 
    Name: C9200-24T  
> 
    Serial Number: PID:C9200-24T SN:XXXXXXXXXXX  
> 
    cn=C9200-24T  
> 
    ou=ACT-2 Lite SUDI  
> 
    o=Cisco  
> 
    serialNumber=PID:C9200-24T SN:XXXXXXXXXXX  
> 
  Validity Date:  
> 
    start date: 08:37:26 UTC Feb 12 2019  
> 
    **end   date: 20:25:41 UTC May 14 2029**   
> 
  Associated Trustpoints: CISCO_IDEVID_SUDI 
```

Various features that might be linked to the SUDI certificate are shown in the following sample configurations:
**HTTPS**
> 
```
ip http secure-trustpoint CISCO_IDEVID_SUDI  
> 
ip http client secure-trustpoint CISCO_IDEVID_SUDI
```

**SSH authentication that uses certificates**
> 
```
ip ssh server certificate  
> 
   profile server  
> 
      trustpoint sign CISCO_IDEVID_SUDI
```

**Zero Touch Deployment (ZTD) that uses a certificate enrollment profile for enrollment or reenrollment**
> 
```
crypto pki profile enrollment profile-name  
> 
   credential CISCO_IDEVID_SUDI
```

  

### Problem Symptom
  

Any services that rely on a trustpoint that is configured with an expired Cisco SUDI certificate will be affected. Some examples are as follows:
  * HTTP server over TLS (HTTPS) - HTTPS will produce an error in the browser that indicates that the certificate is expired.
  * SSH server - Applications that use SUDI certificates to authenticate the SSH session might fail to authenticate.


**Note:** This use of SUDI certificates is rare. Username and password authentication and non-SUDI public or private key authentication are not affected.
  

### Workaround/Solution
  

Customers should refer to the information below to apply the recommended action for their device.
For suggestions related to software upgrade , please evaluate your network deployment before upgrading the devices.
### Catalyst 9200
All units have a SUDI expiration in 2099; however, due to defect CSCwf94778, the device may show an earlier SUDI expiration date.
**Recommended Action:** Upgrade to fixed [versions 17.12.2/17.9.5/17.13.1](https://software.cisco.com/download/home/286320865/type/282046477/release/Cupertino-17.9.5) and later or apply the workarounds described below.
**Note:** The Serial Number Validation Tool/Link is not applicable for this product family.
### Catalyst 9300
All units that show as Affected in the Serial Number Validation Tool have a SUDI expiration of Date of Manufacturing + 10 years or 2029, whichever is earlier.
**Recommended Action:** Refer to the workarounds described below.
All units that show as Not Affected in the Serial Number Validation Tool have a SUDI expiry of 2099; however, due to defect CSCwd82114, units may show an earlier SUDI expiration date.
**Recommended Action:** Upgrade to fixed [versions 17.12.1/17.9.5/17.13.1](https://software.cisco.com/download/home/286315874/type/282046477/release/Cupertino-17.9.5) and later or apply the workarounds described below.
### Catalyst 9400
All units that show as Affected in the Serial Number Validation Tool have a SUDI expiration of Date of Manufacturing + 10 years or 2029, whichever is earlier.
**Recommended Action:** Refer to the workarounds described below.
All units that show as Not Affected in the Serial Number Validation Tool have a SUDI expiration of 2099; however, due to defect CSCwd82114, units may show an earlier SUDI expiration date.
**Recommended Action:** Upgrade to fixed [versions 17.12.1/17.9.5/17.13.1](https://software.cisco.com/download/home/286320244/type/282046477/release/Cupertino-17.9.5) and later or apply the workarounds described below.
### Catalyst 9500 - C9500-16X, C9500-40X, C9500-12Q, C9500-24Q
All units that show as Affected in the Serial Number Validation Tool have a SUDI expiration of Date of Manufacturing + 10 years or 2029 or 2037, whichever is earlier.
**Recommended Action:** Refer to the workarounds described below.
All units that show as Not Affected in the Serial Number Validation Tool have a SUDI expiration of 2099; however, due to defect CSCwd82114, units may show an earlier SUDI expiration date.
**Recommended Action:** Upgrade to fixed [versions 17.12.1/17.9.5/17.13.1](https://software.cisco.com/download/home/286315863/type/282046477/release/Cupertino-17.9.5) and later or apply the workarounds described below.
### Catalyst 9500 - C9500-32C, C9500-32QC, C9500-48Y4C, C9500-24Y4C
All units have a SUDI expiration of 2099; however, due to defect CSCwd82114, devices may show an earlier SUDI expiration date.
**Recommended Action:** Upgrade to fixed [versions 17.12.1/17.9.5/17.13.1](https://software.cisco.com/download/home/286315863/type/282046477/release/Cupertino-17.9.5) and later or apply the workarounds described below.
**Note:** The Serial Number Validation Tool/Link is not applicable for this product family.
### Catalyst 9600/9600X
All units have a SUDI expiration of 2099; however, due to defect CSCwd82114, devices may show an earlier SUDI expiration date.
**Recommended Action:** Upgrade to fixed [versions 17.12.1/17.9.5/17.13.1](https://software.cisco.com/download/home/286322137/type/282046477/release/Cupertino-17.9.5) and later or apply the workarounds described below.
**Note:** The Serial Number Validation Tool/Link is not applicable for this product family.
### Workarounds
Customers should use one of the following three workaround methods to install an alternate certificate:
  * Install a certificate from a CA.
  * Use the local Cisco IOS CA server to generate and sign a new certificate.
  * Use the Simple Certificate Enrollment Protocol (SCEP) to acquire a certificate from the customer's PKI.


**Notes:**
  * Introduction of a new certificate on a device might require import of the issuer's certificate on any peer devices where the new certificate is used to protect communication.
  * After a new non-SUDI certificate is obtained, the configuration of any feature that is identified in the Background section of this Field Notice must be updated. The trust point configuration commands must be reconfigured to be able to use the new certificate.


For more information on each workaround option, see below.
**Install a Certificate from a CA**
In this workaround, a certificate request is generated and displayed by Cisco IOS XE Software. The administrator then copies the request and submits it to a third-party CA and retrieves the result.
**Note:** Use of a CA to sign certificates is a security best practice. This procedure is provided as a workaround in this field notice. However, Cisco recommends continuing to use the third-party CA-signed certificate after you apply this workaround rather than using a self-signed certificate.
To install a certificate from a third-party CA, complete the following steps:
  1. Create a certificate signing request (CSR) using the following CLI input: 
> 
```
Switch#conf t  
> Enter configuration commands, one per line. End with CNTL/Z.  
> Switch(config)# crypto pki trustpoint TEST  
> Switch(ca-trustpoint)# enrollment term pem  
> Switch(ca-trustpoint)# subject-name CN=TEST  
> Switch(ca-trustpoint)# revocation-check none  
> Switch(ca-trustpoint)# rsakeypair TEST  
> Switch(ca-trustpoint)# exit  
> Switch(config)# crypto pki enroll TEST  
> % Start certificate enrollment ..  
> % The subject name in the certificate will include: CN=TEST  
> % The subject name in the certificate will include: Switch.cisco.com  
> % The serial number in the certificate will be: <serial no>  
> % Include an IP address in the subject name? [no]: no  
> >Display Certificate Request to terminal? [yes/no]: yes  
> Certificate Request follows:  
>   -----BEGIN CERTIFICATE REQUEST-----  
> A Base64 Certificate is displayed here. Copy it, along with the ---BEGIN and ---END lines.  
> -----END CERTIFICATE REQUEST-----  
> ---End - This line not part of the certificate request---
```

  2. Submit the CSR to the third-party CA.  
**Note:** The procedure to submit the CSR to a third-party CA and retrieve the resulting certificate varies based on the CA that is used. Consult the documentation of your CA for instructions on how to perform this step.
  3. Download the new identity certificate for the switch along with the CA certificate.
  4. Install the CA certificate on the device using the following CLI input: 
> 
```
Switch# conf t  
> Enter configuration commands, one per line.  End with CNTL/Z.  
> Switch(config)# crypto pki auth TEST  
> Enter the base 64 encoded CA certificate.  
> End with a blank line or the word "quit" on a line by itself  
> -----BEGIN CERTIFICATE-----  
> REMOVED  
> -----END CERTIFICATE-----  
> Certificate has the following attributes:  
>    Fingerprint MD5: 79D15A9F C7EB4882 83AC50AC 7B0FC625  
>    Fingerprint SHA1: 0A80CC2C 9C779D20 9071E790 B82421DE B47E9006  
> % Do you accept this certificate? [yes/no]: yes  
> Trustpoint CA certificate accepted.  
> % Certificate successfully imported  
> Install the identity certificate on the device.  
> Switch(config)# crypto pki import TEST certificate  
>     Enter the base 64 encoded certificate.  
> End with a blank line or the word "quit" on a line by itself  
>   -----BEGIN CERTIFICATE-----  
> REMOVED  
> -----END CERTIFICATE-----  
> % Switch Certificate successfully imported
```



**Use the Local Cisco IOS CA server to Generate and Sign a New Certificate**
To use the local Cisco IOS CA server to generate and sign a new certificate, use the following CLI input.
**Note:** The local CA server feature is not available on all products. 
> 
```
Switch# conf t  
> Enter configuration commands, one per line.  End with CNTL/Z.  
> Switch(config)# ip http server  
> Switch(config)# crypto pki server IOS-CA  
> Switch(cs-server)# grant auto  
> Switch(cs-server)# database level complete  
> Switch(cs-server)# no shut  
> %Some server settings cannot be changed after CA certificate generation.  
> % Please enter a passphrase to protect the private key  
> % or type Return to exit  
> Password: <password>  
> Re-enter password: <password>  
> % Generating 1024 bit RSA keys, keys will be non-exportable...  
> [OK] (elapsed time was 1 seconds)  
> % Certificate Server enabled.  
> Switch# show crypto pki server IOS-CA Certificates  
> Serial Issued date Expire date Subject Name  
> 1 21:31:40 EST Jan 1 2020 21:31:40 EST Dec 31 2022 cn=IOS-CA  
> Switch# conf t  
> Enter configuration commands, one per line.  End with CNTL/Z.  
> Switch(config)# crypto pki trustpoint TEST  
> Switch(ca-trustpoint)# enrollment url http://<local interface ip>:80  
>    # Replace <local interface ip> with the IP address of an interface on the switch  
> Switch(ca-trustpoint)# subject-name CN=TEST  
> Switch(ca-trustpoint)# revocation-check none  
> Switch(ca-trustpoint)# rsakeypair TEST  
> Switch(ca-trustpoint)# exit  
> Switch# conf t  
> Enter configuration commands, one per line.  End with CNTL/Z.  
> Switch(config)# crypto pki auth TEST  
> Certificate has the following attributes:  
> Fingerprint MD5: C281D9A0 337659CB D1B03AA6 11BD6E40  
> Fingerprint SHA1: 1779C425 3DCEE86D 2B11C880 D92361D6 8E2B71FF  
> % Do you accept this certificate? [yes/no]: yes  
> Trustpoint CA certificate accepted.  
> Switch(config)# crypto pki enroll TEST  
> %  
> % Start certificate enrollment ..  
> % Create a challenge password. You will need to verbally provide this  
> password to the CA Administrator in order to revoke your certificate.  
> For security reasons your password will not be saved in the configuration.  
> Please make a note of it.  
> Password: <password>  
> Re-enter password: <password>  
> % The subject name in the certificate will include: CN=TEST  
> % The subject name in the certificate will include: Switch.cisco.com  
> % Include the switch serial number in the subject name? [yes/no]: yes  
> % The serial number in the certificate will be: <serial no>  
> % Include an IP address in the subject name? [no]: no  
> Request certificate from CA? [yes/no]: yes  
> % Certificate request sent to Certificate Authority  
> % The 'show crypto pki certificate verbose TEST' command will show the fingerprint.
```

**Use SCEP to Acquire a Certificate from the Customer's PKI**
This use case is typical for utility customers. To set up the device to acquire a certificate from the customer's PKI, use the following steps:
  1. Create a new trustpoint Locally Significant Device Identifier (LDevID) using the following CLI input: 
> 
```
crypto pki trustpoint LDevID  
>  enrollment retry count 10  
>  enrollment retry period 2  
>  enrollment profile LDevID  
>  serial-number none  
>  fqdn none  
>  ip-address none  
>  password  
>  fingerprint 3F520C4C0F3236C9CA3D5C209C9948EC  
>  subject-name serialNumber=PID:<product id> SN:<serial no>,CN=<serial no>  
>  revocation-check none  
>  rsakeypair LDevID 2048
```

  2. Create an enrollment profile for the new trustpoint LDevID using the following CLI input: 
> 
```
crypto pki profile enrollment LDevID  
> enrollment url  http://192.168.0.254:80  < This is the RA or CA IP address and the port number.
```

  3. Authenticate the trustpoint using the followig CLI input: 
> 
```
conf t  
> crypto pki authenticate LDevID
```

  4. Enroll the trustpoint using the following CLI input: 
> 
```
conf t  
> crypto pki enroll LDevID
```

  5. Use the new LDevID certificate instead of SUDI for configurations and applications.

  

### How to Identify Affected Products
  

In order to verify if your product is affected by this issue, use the [Cisco Support Assistant (CSA)](https://cs.co/FNSNV) to validate the serial number for your device(s). The serial number for the affected device(s) should be included in the form in this field notice.
To determine if a product may be affected, refer to the Serial Number Validation section of this Field Notice.
If the product is listed as Affected or Not Affected, refer to the Workaround/Solution section of this Field Notice for more details on the recommended action for the product.
**Note** : Serial Number Validation is not applicable for Catalyst 9200/Catalyst 9500 (Selected Products) and Catalyst 9600. Refer to the Workaround/Solution section for more details.
  

### Serial Number Validation
  

The Cisco Support Assistant (CSA) can help verify whether a device is impacted by the issue that is described in this Field Notice. To check the device, either enter the serial number in the CSA on the right side of this page or click the following URL: <https://cs.co/FNSNV>.
### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 1.0  | Initial Release  | —  | 2024-MAY-14  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74135.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Customers Also Viewed
  * [Upgrading Catalyst 9400 Switches](https://www.cisco.com/c/en/us/support/docs/switches/catalyst-9400-series-switches/222283-upgrading-catalyst-9400-switches.html)
  * [Cisco Catalyst 9400 Series Switches Hardware Installation Guide --- Specifications](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9400/hardware/install/b_c9400_hig/b_c9400_hig_chapter_0110.html)
  * [Cisco Catalyst 9400 Series Switches Hardware Installation Guide --- Product Overview](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9400/hardware/install/b_c9400_hig/b_c9400_hig_chapter_00.html)
  * [Troubleshoot Power Supplies on Catalyst 9000 Switches](https://www.cisco.com/c/en/us/support/docs/switches/nexus-9000-series-switches/220196-troubleshoot-power-supplies-on-catalyst.html)
  * + Show 1 More


### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74135.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [Catalyst 9200 Series Switches](https://www.cisco.com/c/en/us/support/switches/catalyst-9200-r-series-switches/series.html)
  * [Catalyst 9300 Series Switches](https://www.cisco.com/c/en/us/support/switches/catalyst-9300-series-switches/series.html)
  * [Catalyst 9400 Series Switches](https://www.cisco.com/c/en/us/support/switches/catalyst-9400-series-switches/series.html)
  * [Catalyst 9500 Series Switches](https://www.cisco.com/c/en/us/support/switches/catalyst-9500-series-switches/series.html)
  * [Catalyst 9600 Series Switches](https://www.cisco.com/c/en/us/support/switches/catalyst-9600-series-switches/series.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/741/fn74135.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74135.html)
