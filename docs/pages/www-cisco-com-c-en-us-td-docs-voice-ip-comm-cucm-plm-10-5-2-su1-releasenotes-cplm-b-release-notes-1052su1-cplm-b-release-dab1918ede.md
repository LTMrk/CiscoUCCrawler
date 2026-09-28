---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-10-5-2-su1-releasenotes-cplm-b-release-notes-1052su1-cplm-b-release-dab1918ede
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/10_5_2_SU1/releasenotes/cplm_b_release-notes-1052su1/cplm_b_release-notes-cplm-1052su1_chapter_00.html
retrieved_at: 2026-09-08T04:51:54.338683+00:00
---

Release Notes for Cisco Prime License Manager, Release 10.5(2)SU1a

# Release Notes for Cisco Prime License Manager, Release 10.5(2)SU1a

## Results

Updated: September 27, 2017

Chapter: Introduction

## Chapter: Introduction

# Introduction

## About Release
                        	 Notes

These release
                              		  notes describe features, requirements, restrictions, and caveats for Cisco
                              		  Prime License Manager. These release notes are updated for every maintenance
                              		  release but not for patches or hot fixes.

## Upgrades

For co-resident deployments, Enterprise License Manager Release 9.1 is upgraded to Cisco Prime License Manager Release 10.x
                              with Release 10.x of a Unified Communications application (Cisco Unity Connection or Cisco Unified Communications Manager)
                              upgrade.

You can upgrade a standalone Enterprise License Manager Release 9.1(2) deployment to a standalone Cisco Prime License Manager
                              Release 10.x deployment.

### Upgrading
                           	 Enterprise License Manager on MCS Server to Cisco Prime License Manager on
                           	 Virtual Machine

Cisco Prime
                                 		  License Manager Release 10.0(1) and later is supported on ESXi VMware only. The
                                 		  OVA template is available from the Software Download Center under Prime License
                                 		  Manager Virtual Machine Templates. Bootable install media for new installs is
                                 		  available from the Electronic Software Delivery (ESD) along with the Cisco
                                    			 Unified Communications Manager software.

Replace the
                                          			 MCS server with the VM Server as described in the following URL: http://www.cisco.com/en/US/docs/voice_ip_comm/cucm/install/9_1_1/replace/CUCM_BK_R1B1A464_00_replace-server-cluster-cucm-91.html .

Upgrade the
                                          			 standalone Cisco Enterprise License Manager Release 9.x to standalone Cisco
                                          			 Prime License Manager Release 10.x using the refresh upgrade process with Cisco
                                          			 Prime License Manager standalone ISO as described in the Cisco Prime
                                             				License Manager User Guide : http://www.cisco.com/c/en/us/support/cloud-systems-management/prime-license-manager/products-user-guide-list.html .

Once the new instance has been installed, licenses must be
                                          			 transferred from the old instance. Cisco Global Licensing Organisation (GLO)
                                          			 can assist with this process.

### Product
                           		  Interactions for Enterprise License Manager

The product
                              		  interactions or product versions supported by Enterprise License Manager and
                              		  Cisco Prime License Manager are shown below. For example, while Cisco Prime License
                              		  Manager Release 10.x supports Cisco Unified Communications Manager and Cisco Unity Connection Release 10.x, a license
                              definition update is
                              		  required for Enterprise License Manager. License definition updates for
                              		  Enterprise License Manager 9.x are applied by the installation of
                              		  elm_LicenseDef_9_1_v1.cop.sgn (or the latest version) located at the Software
                              		  Download Center under Prime License Manager Software Patches.

Managed by Cisco Prime License Manager 10.x

CUCM 9.1

Yes

Yes

CUC 9.1

Yes

Yes

CUCM 10.0(1) and later

Yes

W/
                                          					 License Definition Updates

Yes

CUC 10.0(1) and later

Yes

W/
                                          					 License Definition Updates

Yes

CER 10.0(1)

No

Yes

| Step 1 | Replace the
                                          			 MCS server with the VM Server as described in the following URL: http://www.cisco.com/en/US/docs/voice_ip_comm/cucm/install/9_1_1/replace/CUCM_BK_R1B1A464_00_replace-server-cluster-cucm-91.html . |
|---|---|
| Step 2 | Upgrade the
                                          			 standalone Cisco Enterprise License Manager Release 9.x to standalone Cisco
                                          			 Prime License Manager Release 10.x using the refresh upgrade process with Cisco
                                          			 Prime License Manager standalone ISO as described in the Cisco Prime
                                             				License Manager User Guide : http://www.cisco.com/c/en/us/support/cloud-systems-management/prime-license-manager/products-user-guide-list.html . |
| Step 3 | Once the new instance has been installed, licenses must be
                                          			 transferred from the old instance. Cisco Global Licensing Organisation (GLO)
                                          			 can assist with this process. |

| Product
                                          					 Instance Version | Managed
                                          					 By Enterprise License Manager 9.1 | Managed by Cisco Prime License Manager 10.x |
|---|---|---|
| CUCM 9.1 | Yes | Yes |
| CUC 9.1 | Yes | Yes |
| CUCM 10.0(1) and later | Yes W/
                                          					 License Definition Updates | Yes |
| CUC 10.0(1) and later | Yes W/
                                          					 License Definition Updates | Yes |
| CER 10.0(1) | No | Yes |