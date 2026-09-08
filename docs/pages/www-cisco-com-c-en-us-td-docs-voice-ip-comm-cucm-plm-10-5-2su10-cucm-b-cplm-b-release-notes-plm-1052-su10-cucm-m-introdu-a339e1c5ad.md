---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-10-5-2su10-cucm-b-cplm-b-release-notes-plm-1052-su10-cucm-m-introdu-a339e1c5ad
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/10_5_2SU10/cucm_b_cplm_b_release-notes-plm-1052-su10/cucm_m_introduction.html
retrieved_at: 2026-09-08T04:51:04.102007+00:00
---

Release Notes for Cisco Prime License Manager, Release 10.5(2)SU10

# Release Notes for Cisco Prime License Manager, Release 10.5(2)SU10

## Results

Updated: June 10, 2020

Chapter: Introduction

## Chapter: Introduction

# Introduction

## Revision Histroy

Date

Revision

June 11, 2020

Initial publish.

## About Cisco Prime License Manager

Cisco Prime License Manager provides simplified, enterprise-wide management of user-based licensing, including license fulfillment.
                              Cisco Prime License Manager handles licensing fulfillment, supports allocation, and reconciliation of licenses across supported
                              products, and provides enterprise-level reporting of usage and entitlement.

For more information about Cisco Prime License Manager, see the Cisco Prime License Manager User Guide .

## About Release
                        	 Notes

These release
                              		  notes describe features, requirements, restrictions, and caveats for Cisco
                              		  Prime License Manager. These release notes are updated for every maintenance
                              		  release but not for patches or hot fixes.

## Upgrade

### Upgrading
                           	 Enterprise License Manager on MCS Server to Cisco Prime License Manager on
                           	 Virtual Machine

Cisco Prime
                                 		  License Manager Release 10.0(1) and later is supported on ESXi VMware only. The
                                 		  OVA template is available from the Software Download Center under Prime License
                                 		  Manager Virtual Machine Templates. Bootable install media for new installs is
                                 		  available from the Electronic Software Delivery (ESD) along with the Cisco
                                    			 Unified Communications Manager software.

Step 1

Replace the
                                          			 MCS server with the VM Server as described in the following URL: http://www.cisco.com/en/US/docs/voice_ip_comm/cucm/install/9_1_1/replace/CUCM_BK_R1B1A464_00_replace-server-cluster-cucm-91.html .

Step 2

Upgrade the standalone Cisco Enterprise License Manager Release 9.x to standalone Cisco Prime License Manager Release 10.x
                                          using the refresh upgrade process with Cisco Prime License Manager standalone ISO as described in the Cisco Prime License
                                          Manager User Guide: https://www.cisco.com/c/en/us/support/cloud-systems-management/prime-license-manager/products-user-guide-list.html .

Step 3

Once the new instance has been installed, licenses must be
                                          			 transferred from the old instance. Cisco Global Licensing Organisation (GLO)
                                          			 can assist with this process.

### Product Interactions for Enterprise License Manager

The product
                                 		  interactions or product versions supported by Enterprise License Manager and
                                 		  Cisco Prime License Manager are shown below. For example, while Cisco Prime License
                                 		  Manager Release 10.x supports Cisco Unified Communications Manager and Cisco Unity Connection Release 10.x, a license
                                 definition update is
                                 		  required for Enterprise License Manager. License definition updates for
                                 		  Enterprise License Manager 9.x are applied by the installation of
                                 		  elm_LicenseDef_9_1_v1.cop.sgn (or the latest version) located at the Software
                                 		  Download Center under Prime License Manager Software Patches.

Product Instance Version

Managed By Enterprise License Manager 9.1

Managed by Cisco Prime License Manager 10.x and 11.x

CUCM 9.1

Yes

Yes

CUC 9.1

Yes

Yes

CUCM 10.0(1) to 11.5

Yes

W/ License Definition Updates

Yes

CUC 10.0(1) to 11.5

Yes

W/ License Definition Updates

Yes

CER 10.0(1) to 11.5

No

Yes

| Date | Revision |
|---|---|
| June 11, 2020 | Initial publish. |

| Step 1 | Replace the
                                          			 MCS server with the VM Server as described in the following URL: http://www.cisco.com/en/US/docs/voice_ip_comm/cucm/install/9_1_1/replace/CUCM_BK_R1B1A464_00_replace-server-cluster-cucm-91.html . |
|---|---|
| Step 2 | Upgrade the standalone Cisco Enterprise License Manager Release 9.x to standalone Cisco Prime License Manager Release 10.x
                                          using the refresh upgrade process with Cisco Prime License Manager standalone ISO as described in the Cisco Prime License
                                          Manager User Guide: https://www.cisco.com/c/en/us/support/cloud-systems-management/prime-license-manager/products-user-guide-list.html . |
| Step 3 | Once the new instance has been installed, licenses must be
                                          			 transferred from the old instance. Cisco Global Licensing Organisation (GLO)
                                          			 can assist with this process. |

| Product Instance Version | Managed By Enterprise License Manager 9.1 | Managed by Cisco Prime License Manager 10.x and 11.x |
|---|---|---|
| CUCM 9.1 | Yes | Yes |
| CUC 9.1 | Yes | Yes |
| CUCM 10.0(1) to 11.5 | Yes W/ License Definition Updates | Yes |
| CUC 10.0(1) to 11.5 | Yes W/ License Definition Updates | Yes |
| CER 10.0(1) to 11.5 | No | Yes |