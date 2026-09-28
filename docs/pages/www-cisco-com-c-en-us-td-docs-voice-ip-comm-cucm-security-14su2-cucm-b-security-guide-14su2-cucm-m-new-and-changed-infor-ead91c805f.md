---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-security-14su2-cucm-b-security-guide-14su2-cucm-m-new-and-changed-infor-ead91c805f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/14SU2/cucm_b_security-guide-14su2/cucm_m_new-and-changed-information.html
retrieved_at: 2026-08-17T00:27:16.301447+00:00
---

Security Guide for Cisco Unified Communications Manager Release 14 and SUs

# Security Guide for Cisco Unified Communications Manager Release 14 and SUs

Updated: April 8, 2026

Chapter: New and Changed Information

## Chapter: New and Changed Information

- New and Changed Information

- New and Changed Information

# New and Changed Information

## New and Changed Information

The following table provides an overview of the significant changes to the features in this guide up to this current release.
                              The table does not provide an exhaustive list of all changes made to the guide or of the new features up to this release.

Feature or Change

Description

See

Date

FIPS Requirements

In Release 14SU5, the CiscoSSL version is updated.

FIPS Setup

October 09, 2025

Support to renew refresh token automatically

Unified Communications Manager supports the automatic renewal of refresh token for Webex clients in Release 14SU4.

OAuth Framework

May 30, 2024

Oauth—Eliminate Refresh token dependency on CUCM publisher

In Release 14SU4, this feature introduces a new enterprise parameter ‘ Auto Renew Refresh Token ’ that is enabled by default.

Refer to the 'Common Enterprise Parameters and Services' section of the System Configuration Guide for Cisco Unified Communications Manager

May 30, 2024

ECDHE cipher support on CAPF and TVS

Updated cipher list to include ECDHE cipher support on CAPF and TVS

Cipher Limitations

May 30, 2024

Certificate Revocation List Support

In Release 14SU3, this feature introduces certificate revocation list, where the CA will have a list of digital certificates
                                          that have been revoked before their actual or assigned expiration date.

Certificate Revocation Configuration

May 18, 2023

Cisco SSL7 upgrade

In Release 14SU2, CiscoSSL and Ciscofom is upgraded from version 6 to 7 in Unified Communication Manager.

FIPS Setup

FIPS Mode Restrictions

Web Requests From CCMAdmin or CCMUser to Cisco Unified Communications Manager

June 16, 2022

CiscoSSL6x to CiscoSSL7x upgrade (VOS modules, being done by Adaptation team)

In Release 14SU2, CiscoSSL and Ciscofom is upgraded from version 6 to 7 in Unified Communication Manager.

FIPS Setup

FIPS Mode Restrictions

June 16, 2022

Enrollment over Secure Transport Support

In Release 14SU2, this feature supports the automatic enrollment of certificates with CAs having inbuilt EST server mode.

Configure Online Certificate Authority Settings

June 16, 2022

EPNM multi line enhancement (TFTP work)

Unified Communications Manager supports masking of External Phone Number for all configured line numbers for the latest phone
                                          models in Release 14SU2.

External Phone Number Mask

June 16, 2022

Making OU not mandatory as part of CSR generation

In Release 14SU2, this feature introduces an option to include the Organization Unit field in the Certificate Signing Request.

June 16, 2022

Spectralink/Saturn and Mars (Support download of large files from CUCM TFTP)

Unified Communications Manager supports HTTP range requests (RFC7233) support on TFTP and Proxy TFTP (if the download file
                                          is at least 100MB) in Release 14SU1.

Potential Issues with Firmware Installs

October 27, 2021

SSO Redirect URI for Webex Apps

This feature enhances the security of Cisco Jabber/Webex Client that uses the external browser to perform SSO to be cross
                                          launched by the browser using SSO Redirect URI.

SSO Redirect URI for Webex Apps

October 27, 2021

TFTP proxy support for Oauth

Unified Communications Manager supports TFTP Proxy in SIP OAuth deployments.

Configure TFTP Server Dynamically

Configure TFTP Server Manually

Enable SIP OAuth Mode

Certificate Signing Request Fields

October 27, 2021

CSCvu05478 : Unable to upload multiple certificates from same certificate authority

As part of this CDET we will be able to upload multiple certificates from a single certificate authority using the certificate
                                          name convention Common Name_SerialNumber.

Certificate Signing Request Fields

October 27, 2021

CSCvz05710 - CiscoJ upgrade to 5.3.6 version backport to 12.5 SU6

As part of this feature we will upgrade to CiscoJ 5.3.7 version in 12.5 SU6 and 14 SU1.

FIPS Setup

October 27, 2021

| Feature or Change | Description | See | Date |
|---|---|---|---|
| FIPS Requirements | In Release 14SU5, the CiscoSSL version is updated. | FIPS Setup | October 09, 2025 |
| Support to renew refresh token automatically | Unified Communications Manager supports the automatic renewal of refresh token for Webex clients in Release 14SU4. | OAuth Framework | May 30, 2024 |
| Oauth—Eliminate Refresh token dependency on CUCM publisher | In Release 14SU4, this feature introduces a new enterprise parameter ‘ Auto Renew Refresh Token ’ that is enabled by default. | Refer to the 'Common Enterprise Parameters and Services' section of the System Configuration Guide for Cisco Unified Communications Manager | May 30, 2024 |
| ECDHE cipher support on CAPF and TVS | Updated cipher list to include ECDHE cipher support on CAPF and TVS | Cipher Limitations | May 30, 2024 |
| Certificate Revocation List Support | In Release 14SU3, this feature introduces certificate revocation list, where the CA will have a list of digital certificates
                                          that have been revoked before their actual or assigned expiration date. | Certificate Revocation Configuration | May 18, 2023 |
| Cisco SSL7 upgrade | In Release 14SU2, CiscoSSL and Ciscofom is upgraded from version 6 to 7 in Unified Communication Manager. | FIPS Setup FIPS Mode Restrictions Web Requests From CCMAdmin or CCMUser to Cisco Unified Communications Manager | June 16, 2022 |
| CiscoSSL6x to CiscoSSL7x upgrade (VOS modules, being done by Adaptation team) | In Release 14SU2, CiscoSSL and Ciscofom is upgraded from version 6 to 7 in Unified Communication Manager. | FIPS Setup FIPS Mode Restrictions | June 16, 2022 |
| Enrollment over Secure Transport Support | In Release 14SU2, this feature supports the automatic enrollment of certificates with CAs having inbuilt EST server mode. | Configure Online Certificate Authority Settings | June 16, 2022 |
| EPNM multi line enhancement (TFTP work) | Unified Communications Manager supports masking of External Phone Number for all configured line numbers for the latest phone
                                          models in Release 14SU2. | External Phone Number Mask | June 16, 2022 |
| Making OU not mandatory as part of CSR generation | In Release 14SU2, this feature introduces an option to include the Organization Unit field in the Certificate Signing Request. | Certificate Signing Request Fields | June 16, 2022 |
| Spectralink/Saturn and Mars (Support download of large files from CUCM TFTP) | Unified Communications Manager supports HTTP range requests (RFC7233) support on TFTP and Proxy TFTP (if the download file
                                          is at least 100MB) in Release 14SU1. | Potential Issues with Firmware Installs | October 27, 2021 |
| SSO Redirect URI for Webex Apps | This feature enhances the security of Cisco Jabber/Webex Client that uses the external browser to perform SSO to be cross
                                          launched by the browser using SSO Redirect URI. | SSO Redirect URI for Webex Apps | October 27, 2021 |
| TFTP proxy support for Oauth | Unified Communications Manager supports TFTP Proxy in SIP OAuth deployments. | Configure TFTP Server Dynamically Configure TFTP Server Manually Enable SIP OAuth Mode Certificate Signing Request Fields | October 27, 2021 |
| CSCvu05478 : Unable to upload multiple certificates from same certificate authority | As part of this CDET we will be able to upload multiple certificates from a single certificate authority using the certificate
                                          name convention Common Name_SerialNumber. | Certificate Signing Request Fields | October 27, 2021 |
| CSCvz05710 - CiscoJ upgrade to 5.3.6 version backport to 12.5 SU6 | As part of this feature we will upgrade to CiscoJ 5.3.7 version in 12.5 SU6 and 14 SU1. | FIPS Setup | October 27, 2021 |