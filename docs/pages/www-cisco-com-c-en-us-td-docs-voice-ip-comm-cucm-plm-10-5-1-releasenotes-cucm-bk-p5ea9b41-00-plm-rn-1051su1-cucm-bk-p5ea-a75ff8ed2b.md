---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-10-5-1-releasenotes-cucm-bk-p5ea9b41-00-plm-rn-1051su1-cucm-bk-p5ea-a75ff8ed2b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/10_5_1/releasenotes/CUCM_BK_P5EA9B41_00_plm-rn-1051su1/CUCM_BK_P5EA9B41_00_plm-rn-1051su1_chapter_00.html
retrieved_at: 2026-09-08T04:52:36.655133+00:00
---

Release Notes for Cisco Prime License Manager Release 10.5(1)SU1

# Release Notes for Cisco Prime License Manager Release 10.5(1)SU1

Updated: October 23, 2014

Chapter: Introduction

## Chapter: Introduction

# Introduction

## About Release
	 Notes

For more information about Cisco Prime License Manager, see http:/​/​www.cisco.com/​en/​US/​partner/​products/​ps13081/​products_​user_​guide_​list.html .

## Upgrades

For a standalone Enterprise
		  License Manager deployment, use the Prime License Manager ISO:

- To upgrade to Cisco Prime License Manager Release 10.5(1), use the following ISO file: CiscoPrimeLM_64bitLnx_10.5.1.11901-1.sgn.iso.

You can upgrade a standalone Enterprise License Manager Release 9.1(2) deployment to a standalone Cisco Prime License Manager Release 10.x deployment.

For co-resident deployments, Enterprise License Manager Release 9.1 is upgraded to Cisco Prime License Manager Release 10.x with Release 10.x of a Unified Communications application (Cisco Unity Connection or Cisco Unified Communications Manager) upgrade.

- Upgrading
		  Enterprise License Manager on MCS Server to Cisco Prime License Manager on
		  Virtual Machine

- Product
		  Interactions for Enterprise License Manager

### Upgrading
		  Enterprise License Manager on MCS Server to Cisco Prime License Manager on
		  Virtual Machine

Cisco Prime License Manager Release 10.0(1) and later is supported on ESXi VMware only. The OVA is available from the Software Download Center under Prime License Manager Virtual Machine Templates.

### Product
		  Interactions for Enterprise License Manager

The product
		  interactions or product versions supported by Enterprise License Manager and
		  Cisco Prime License Manager are shown below. For example, while Cisco Prime License
		  Manager Release 10.x supports Cisco Unified Communications Manager and Cisco Unity Connection Release 10.x, a license definition update is
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

| Step 1 | Replace the MCS server
			 with the VM Server as described in the following URL: http:/​/​www.cisco.com/​en/​US/​docs/​voice_ip_comm/​cucm/​install/​9_1_1/​replace/​CUCM_​BK_​R1B1A464_​00_​replace-server-cluster-cucm-91.html . |
|---|---|
| Step 2 | Upgrade the standalone Cisco
			 Enterprise License Manager Release 9.x to standalone Cisco Prime License
			 Manager Release 10.x using the refresh upgrade process with Cisco Prime License Manager
			 standalone ISO as described in the Cisco Prime License Manager User Guide : http:/​/​www.cisco.com/​c/​en/​us/​support/​cloud-systems-management/​prime-license-manager/​products-user-guide-list.html . |

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