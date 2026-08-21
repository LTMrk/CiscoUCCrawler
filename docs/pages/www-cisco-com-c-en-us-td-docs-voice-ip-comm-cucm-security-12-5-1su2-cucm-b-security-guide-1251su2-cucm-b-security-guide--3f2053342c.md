---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-security-12-5-1su2-cucm-b-security-guide-1251su2-cucm-b-security-guide--3f2053342c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/12_5_1SU2/cucm_b_security-guide-1251SU2/cucm_b_security-guide-1251SU2_chapter_01001.html
retrieved_at: 2026-08-21T08:40:07.336228+00:00
---

Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: March 22, 2024

Chapter: Phone Security

## Chapter: Phone Security

# Phone Security

This chapter provides information about phone security.

## Phone Security Overview

At installation, Unified Communications Manager boots up in nonsecure mode. When the phones boot up after the Unified Communications Manager installation, all devices register as nonsecure with Unified Communications Manager .

After you upgrade from Unified Communications Manager 4.0(1) or a later release, the phones boot up in the device security mode that you enabled prior to the upgrade; all devices
                              register by using the chosen security mode.

The Unified Communications Manager installation creates a self-signed certificate on the Unified Communications Manager and TFTP server. You may also choose to use a third-party, CA-signed certificate for Unified Communications Manager instead of the self-signed certificate. After you configure authentication, Unified Communications Manager uses the certificate to authenticate with supported Cisco Unified IP Phone s. After a certificate exists on the Unified Communications Manager and TFTP server, Unified Communications Manager does not reissue the certificates during each Unified Communications Manager upgrade. You must create a new CTL file with the new certificate entries.

Tip

For information on unsupported or nonsecure scenarios, see topics related to interactions and restrictions.

Unified Communications Manager maintains the authentication and encryption status at the device level. If all devices that are involved in the call register
                              as secure, the call status registers as secure. If one device registers as nonsecure, the call registers as nonsecure, even
                              if the phone of the caller or recipient registers as secure.

Unified Communications Manager retains the authentication and encryption status of the device when a user uses Cisco Extension Mobility . Unified Communications Manager also retains the authentication and encryption status of the device when shared lines are configured.

Tip

When you configure a shared line for an encrypted Cisco IP Phone, configure all devices that share the lines for encryption;
                                          that is, ensure that you set the device security mode for all devices to encrypted by applying a security profile that supports
                                          encryption.

## Trusted Devices

Unified Communications Manager allows Security icons to be enabled by phone model on Cisco IP Phones. The Security icon indicates whether the call is secure
                              and the connected device is trusted.

A Trusted Device represents a Cisco device or a third-party device that has passed Cisco security criteria for trusted connections.
                              This includes, but is not limited to, signaling/media encryption, platform hardening, and assurance. If a device is trusted,
                              a Security icon displays and a secure tone plays on supported devices. Also, the device may provide other features or indicators
                              that are related to secure calls.

Unified Communications Manager determines whether a device is trusted when you add it to your system. The security icon displays for information purposes
                              only, and the administrator cannot configure it directly.

Unified Communications Manager also indicates whether a gateway is trusted by displaying an icon and a message in Unified Communications Manager Administration .

This section describes the behavior of the security icon for trusted devices on both the Cisco IP Phones and in Unified Communications Manager Administration .

### Cisco Unified Communications Manager Administration

The following windows in Unified Communications Manager Administration indicate whether a device is trusted:

#### Gateway Configuration

For each gateway type, the Gateway Configuration window ( Device > Gateway ) displays either Device is trusted or Device is not trusted , along with a corresponding icon.

The system determines whether the device is trusted, based on the device type. You cannot configure whether the device is
                                 trusted.

#### Phone Configuration

For each phone device type, the Phone Configuration window ( Device > Phone ) displays either Device is trusted or Device is not trusted , along with a corresponding icon.

The system determines whether the device is trusted, based on the device type. You cannot configure whether the device is
                                 trusted.

#### Device Called Trust Determination Criteria

The type of device that a user calls affects the security icon that displays on the phone. The system considers the following
                                    three criteria to determine whether the call is secure:

Are all devices on the call trusted?

Is the signaling secure (authenticated and encrypted)?

Is the media secure?

Before a supported Cisco Unified IP Phone displays the Lock Security icon, be aware that all three of these criteria must be met. For calls that involve a device that
                                    is not trusted, regardless of signaling and media security, the overall status of the call will stay unsecure, and the phone
                                    will not display the Lock icon. For example, if you include an untrusted device in a conference, the system considers its
                                    call leg, as well as the conference itself, to be unsecure.

## Phone Model Support

There are two categories of phone models which support security in Unified Communications Manager: Secure Cisco phones and
                              Secure Preferred Vendor phones. Secure Cisco phones are pre-installed with a Manufacture-Installed Certificate (MIC) and support
                              automatic generation and exchange of Locally-Significant Certificates (LSC) using the Certificate Authority Proxy Function
                              (CAPF). Secure Cisco phones are capable of registering with Cisco Unified CM using the MIC without additional certificate
                              management. For additional security, you can create and install an LSC on the phone using CAPF. See topics related to phone
                              security setup and settings for more information.

Secure Preferred Vendor phones do not come pre-installed with a MIC, and do not support CAPF for generating LSCs. In order
                              for Secure Preferred Vendor phones to connect to Cisco Unified CM, a certificate must be provided with the device, or generated
                              by the device. The phone supplier must provide the details on how to acquire or generate a certificate for the phone. Once
                              you obtain the certificate, you must upload the certificate to the Cisco Unified CM using the OS Administration Certificate
                              Management interface.  See topics related to preferred vendor SIP phone security set up for more information.

For a list of security features that are supported on your phone, refer to the phone administration and user documentation
                              that supports this Unified Communications Manager release or the firmware documentation that supports your firmware load.

You can also use Cisco Unified Reporting to list the phones that support a particular feature. For more information about using Cisco Unified Reporting , see the Cisco Unified Reporting Administration Guide .

## Preferred Vendor SIP Phone Security Set Up

Secure Preferred Vendor phones are phone types that are manufactured by third-party vendors but are installed in the Cisco
                              Unified database via a COP file. Unified Communications Manager provides security for a preferred vendor SIP phone. In order
                              to support security, you must enable Security Encryption or Security Authentication for the preferred vendor SIP phone in
                              the COP file. These phone types appear in the drop-down list in the Add a New Phone window. While all preferred vendor phones
                              support Digest Authorization, not all preferred vendor phones support TLS security. Security capabilities is based on the
                              phone model. If the Phone Security Profile includes a "Device Security Mode" field, then it supports TLS security.

If the preferred vendor phone supports TLS security, there are two modes that are possible: per-device certificate and shared
                              certificate. The phone supplier must specify which mode is applicable for the phone as well as instructions on generating
                              or acquiring a certificate for the phone.

### Set Up Preferred Vendor SIP Phone Security Profile Per-Device Certificates

To configure the preferred vendor SIP phone security profile with per-device certificates, perform the following procedure:

Step 1

Upload the certificate for each phone using the OS Administration Certificate Management interface.

Step 2

In the Cisco Unified Administration, choose System > Security > Phone Security Profile .

Step 3

Configure a new Phone Security Profile for the device type of this phone and in the Device Security Mode drop-down list, choose Encrypted or Authenticated .

Step 4

To configure the new SIP phone in the CCMAdmin interface, choose Device > Phone > Add New .

Step 5

Select Phone type.

Step 6

Fill in the required fields.

Step 7

In the Device Security Profile drop-down list, select the profile you just created.

### Set Up Preferred Vendor SIP Phone Security Profile Shared Certificates

To configure the preferred vendor SIP phone security profile with shared certificates, perform the following procedure:

Step 1

Using instructions from the phone vendor, generate a certificate with a Subject Alternate Name (SAN) string. The SAN must
                                          be of type DNS. Make a note of the SAN specified in this step. For example, X509v3 extensions:

X509v3 Subject Alternative Name

DNS:AscomGroup01.acme.com

The SAN must be of type DNS or security will not be enabled.

Step 2

Upload the shared certificate using the OS Administration Certificate Management interface.

Step 3

In the Cisco Unified Administration, choose System > Security > Phone Security Profile .

Step 4

In the Name field, enter the name of the Subject Alt Name (SAN), which is the name on the certificate provided by the preferred vendor,
                                          or if there is no SAN enter the Certificate Name.

The name of the security profile must match the SAN in the certificate exactly or security will not be enabled.

Step 5

In the Device Security Mode drop-down list, choose Encrypted or Authenticated .

Step 6

In the Transport type drop-down list, choose TLS .

Step 7

To configure the new SIP phone in the CCMAdmin interface, choose Device > Phone > Add New .

Step 8

Select Phone type.

Step 9

Fill in the required fields

Step 10

In the Device Security Profile drop-down list, select the profile you just created.

## View Phone Security Settings

You can configure and view certain security-related settings on phones that support security; for example, you can view whether
                              a phone has a locally significant certificate or manufacture-installed certificate installed. For additional information on
                              the security menu and icons, refer to the Cisco IP Phone Administration Guide and Cisco IP Phone User Guide that supports your phone model.

When Unified Communications Manager classifies a call as authenticated or encrypted, an icon is displayed on the phone and indicates the call state. It also
                              determines when Unified Communications Manager classifies the call as authenticated or encrypted.

## Set Up Phone
                        	 Security

The
                              		  following procedure describes the tasks to configure security for supported
                              		  phones.

Step 1

If you have not already done so, configure the Cisco CTL Client and ensure that the Unified Communications Manager security mode equals Mixed Mode.

Step 2

If the phone
                                       			 does not contain a locally significant certificate (LSC) or
                                       			 manufacture-installed certificate (MIC), install a LSC by using the Certificate
                                       			 Authority Proxy Function (CAPF).

Step 3

Configure phone
                                       			 security profiles.

Step 4

Apply a phone
                                       			 security profile to the phone.

Step 5

After you
                                       			 configure digest credentials, choose the Digest User from the Phone
                                       			 Configuration window.

Step 6

On Cisco Unified IP Phone 7962 or 7942 (SIP only), enter the digest authentication username and password (digest credentials) that you configured in
                                       the End User Configuration window.

This document does not provide procedures on how to enter the digest authentication credentials on the phone. For information
                                                      on how to perform this task, see Administration Guide for Cisco Unified Communications Manager that supports your phone model and this version of Unified Communications Manager .

Step 7

Encrypt the
                                       			 phone configuration file, if the phone supports this functionality.

Step 8

To harden the
                                       			 phone, disable phone settings.

## Phone Security Interactions and Restrictions

This section provides the interaction and restriction on Phone Security.

Feature

Interaction and Restriction

Certificate Encryption

Beginning from Unified Communications Manager Release 11.5(1) SU1, all the LSC certificates issued by CAPF service are signed with SHA-256 algorithm. Therefore, Cisco Unified IP Phone 7900 Series, 8900 Series, and 9900 Series supports SHA-256 signed LSC certificates and external SHA2 identity certificates
                                       (Tomcat, CallManager, CAPF, TVS, and so on). For any other cryptographic operation that require validation of signature, only
                                       SHA-1 is supported.

If you use phone models which are in End of Software Maintenance or End of Life, we strongly recommend using the Unified Communications Manager before 11.5(1)SU1 release.

## Where to Find More
                        	 Information About Phone Security

### Related Cisco
                              		  Documentation

Administration Guide for Cisco Unified Communications Manager

Troubleshooting Guide for Cisco Unified Communications
                                          					 Manager

| Tip | For information on unsupported or nonsecure scenarios, see topics related to interactions and restrictions. |
|---|---|

| Tip | When you configure a shared line for an encrypted Cisco IP Phone, configure all devices that share the lines for encryption;
                                          that is, ensure that you set the device security mode for all devices to encrypted by applying a security profile that supports
                                          encryption. |
|---|---|

| Step 1 | Upload the certificate for each phone using the OS Administration Certificate Management interface. |
|---|---|
| Step 2 | In the Cisco Unified Administration, choose System > Security > Phone Security Profile . |
| Step 3 | Configure a new Phone Security Profile for the device type of this phone and in the Device Security Mode drop-down list, choose Encrypted or Authenticated . |
| Step 4 | To configure the new SIP phone in the CCMAdmin interface, choose Device > Phone > Add New . |
| Step 5 | Select Phone type. |
| Step 6 | Fill in the required fields. |
| Step 7 | In the Device Security Profile drop-down list, select the profile you just created. |

| Step 1 | Using instructions from the phone vendor, generate a certificate with a Subject Alternate Name (SAN) string. The SAN must
                                          be of type DNS. Make a note of the SAN specified in this step. For example, X509v3 extensions: X509v3 Subject Alternative Name DNS:AscomGroup01.acme.com Note The SAN must be of type DNS or security will not be enabled. | Note | The SAN must be of type DNS or security will not be enabled. |
|---|---|---|---|
| Note | The SAN must be of type DNS or security will not be enabled. |
| Step 2 | Upload the shared certificate using the OS Administration Certificate Management interface. |
| Step 3 | In the Cisco Unified Administration, choose System > Security > Phone Security Profile . |
| Step 4 | In the Name field, enter the name of the Subject Alt Name (SAN), which is the name on the certificate provided by the preferred vendor,
                                          or if there is no SAN enter the Certificate Name. Note The name of the security profile must match the SAN in the certificate exactly or security will not be enabled. | Note | The name of the security profile must match the SAN in the certificate exactly or security will not be enabled. |
| Note | The name of the security profile must match the SAN in the certificate exactly or security will not be enabled. |
| Step 5 | In the Device Security Mode drop-down list, choose Encrypted or Authenticated . |
| Step 6 | In the Transport type drop-down list, choose TLS . |
| Step 7 | To configure the new SIP phone in the CCMAdmin interface, choose Device > Phone > Add New . |
| Step 8 | Select Phone type. |
| Step 9 | Fill in the required fields |
| Step 10 | In the Device Security Profile drop-down list, select the profile you just created. |

| Note | The SAN must be of type DNS or security will not be enabled. |
|---|---|

| Note | The name of the security profile must match the SAN in the certificate exactly or security will not be enabled. |
|---|---|

| Step 1 | If you have not already done so, configure the Cisco CTL Client and ensure that the Unified Communications Manager security mode equals Mixed Mode. |
|---|---|
| Step 2 | If the phone
                                       			 does not contain a locally significant certificate (LSC) or
                                       			 manufacture-installed certificate (MIC), install a LSC by using the Certificate
                                       			 Authority Proxy Function (CAPF). |
| Step 3 | Configure phone
                                       			 security profiles. |
| Step 4 | Apply a phone
                                       			 security profile to the phone. |
| Step 5 | After you
                                       			 configure digest credentials, choose the Digest User from the Phone
                                       			 Configuration window. |
| Step 6 | On Cisco Unified IP Phone 7962 or 7942 (SIP only), enter the digest authentication username and password (digest credentials) that you configured in
                                       the End User Configuration window. Note This document does not provide procedures on how to enter the digest authentication credentials on the phone. For information
                                                      on how to perform this task, see Administration Guide for Cisco Unified Communications Manager that supports your phone model and this version of Unified Communications Manager . | Note | This document does not provide procedures on how to enter the digest authentication credentials on the phone. For information
                                                      on how to perform this task, see Administration Guide for Cisco Unified Communications Manager that supports your phone model and this version of Unified Communications Manager . |
| Note | This document does not provide procedures on how to enter the digest authentication credentials on the phone. For information
                                                      on how to perform this task, see Administration Guide for Cisco Unified Communications Manager that supports your phone model and this version of Unified Communications Manager . |
| Step 7 | Encrypt the
                                       			 phone configuration file, if the phone supports this functionality. |
| Step 8 | To harden the
                                       			 phone, disable phone settings. |

| Note | This document does not provide procedures on how to enter the digest authentication credentials on the phone. For information
                                                      on how to perform this task, see Administration Guide for Cisco Unified Communications Manager that supports your phone model and this version of Unified Communications Manager . |
|---|---|

| Feature | Interaction and Restriction |
|---|---|
| Certificate Encryption | Beginning from Unified Communications Manager Release 11.5(1) SU1, all the LSC certificates issued by CAPF service are signed with SHA-256 algorithm. Therefore, Cisco Unified IP Phone 7900 Series, 8900 Series, and 9900 Series supports SHA-256 signed LSC certificates and external SHA2 identity certificates
                                       (Tomcat, CallManager, CAPF, TVS, and so on). For any other cryptographic operation that require validation of signature, only
                                       SHA-1 is supported. Note If you use phone models which are in End of Software Maintenance or End of Life, we strongly recommend using the Unified Communications Manager before 11.5(1)SU1 release. | Note | If you use phone models which are in End of Software Maintenance or End of Life, we strongly recommend using the Unified Communications Manager before 11.5(1)SU1 release. |
| Note | If you use phone models which are in End of Software Maintenance or End of Life, we strongly recommend using the Unified Communications Manager before 11.5(1)SU1 release. |

| Note | If you use phone models which are in End of Software Maintenance or End of Life, we strongly recommend using the Unified Communications Manager before 11.5(1)SU1 release. |
|---|---|