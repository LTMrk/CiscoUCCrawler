---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-10-5-1-releasenotes-cucm-bk-p64d2d8c-00-plm-rn-1051-cucm-bk-p64d2d8-83d2bec098
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/10_5_1/releasenotes/CUCM_BK_P64D2D8C_00_plm-rn-1051/CUCM_BK_P64D2D8C_00_plm-rn-1051_chapter_00.html
retrieved_at: 2026-09-08T04:53:06.364720+00:00
---

Release Notes for Cisco Prime License Manager Release 10.5(1)

# Release Notes for Cisco Prime License Manager Release 10.5(1)

## Results

Updated: July 15, 2014

Chapter: Introduction

## Chapter: Introduction

# Introduction

## About Release
	 Notes

For more information about Cisco Prime License Manager, see http:/​/​www.cisco.com/​en/​US/​partner/​products/​ps13081/​products_​user_​guide_​list.html .

## Upgrades

For a standalone Enterprise
		  License Manager deployment, use the Prime License Manager ISO:

- To upgrade to Cisco Prime License Manager Release 10.5(1), use the following ISO file: CiscoPrimeLM_64bitLnx_10.5.1.XXXXX-XX.sgn.iso.

Where: X represents the specific branch and build number.

For a co-resident Enterprise
		  License Manager deployment, Enterprise License Manager is
		  upgraded to Cisco Prime License Manager along with your Unified Communications product upgrade.

You can upgrade a standalone Enterprise License Manager Release 9.1(2) deployment to a standalone Cisco Prime License Manager Release 10.x deployment.

For co-resident deployments, you can upgrade Enterprise License Manager Release 9.1 to Cisco Prime License Manager Release 10.x with Release 10.x of a Unified Communications application (Cisco Unity Connection or Cisco Unified Communications Manager) upgrade.

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
			 standalone ISO as described in the Cisco Prime License Manager User Guide . |

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