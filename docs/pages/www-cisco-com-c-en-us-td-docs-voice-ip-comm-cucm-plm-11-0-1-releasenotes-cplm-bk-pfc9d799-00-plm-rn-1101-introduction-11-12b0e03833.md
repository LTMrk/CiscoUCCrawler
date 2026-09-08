---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-11-0-1-releasenotes-cplm-bk-pfc9d799-00-plm-rn-1101-introduction-11-12b0e03833
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/11_0_1/releasenotes/CPLM_BK_PFC9D799_00_plm-rn-1101/introduction_1101.html
retrieved_at: 2026-09-08T04:50:47.438201+00:00
---

Release Notes for Cisco Prime License Manager, Release 11.0(1)

# Release Notes for Cisco Prime License Manager, Release 11.0(1)

## Results

Updated: June 12, 2015

Chapter: Introduction

## Chapter: Introduction

# Introduction

## About Cisco Prime License Manager

Cisco Prime License Manager provides simplified, enterprise-wide
		management of user-based licensing, including license fulfillment. Cisco Prime
		License Manager handles licensing fulfillment, supports allocation and
		reconciliation of licenses across supported products, and provides
		enterprise-level reporting of usage and entitlement.

For more
		  information about Cisco Prime License Manager, see the Cisco Prime License Manager User Guide at http:/​/​www.cisco.com/​en/​US/​partner/​products/​ps13081/​products_​user_​guide_​list.html .

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

Cisco Prime License Manager Release 10.0(1) and later is supported on ESXi VMware only. The OVA is available from the Software Download Center under Prime License Manager Virtual Machine Templates.

### Product Interactions for Enterprise License Manager

The product
		  interactions or product versions supported by Enterprise License Manager and
		  Cisco Prime License Manager are shown below. For example, while Cisco Prime License
		  Manager Release 10.x supports Cisco Unified Communications Manager and Cisco Unity Connection Release 10.x, a license definition update is
		  required for Enterprise License Manager. License definition updates for
		  Enterprise License Manager 9.x are applied by the installation of
		  elm_LicenseDef_9_1_v1.cop.sgn (or the latest version) located at the Software
		  Download Center under Prime License Manager Software Patches.

Managed by Cisco Prime License Manager 10.x and 11.x

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

CER 10.0(1) and later

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
					 By Enterprise License Manager 9.1 | Managed by Cisco Prime License Manager 10.x and 11.x |
|---|---|---|
| CUCM 9.1 | Yes | Yes |
| CUC 9.1 | Yes | Yes |
| CUCM 10.0(1) and later | Yes W/
					 License Definition Updates | Yes |
| CUC 10.0(1) and later | Yes W/
					 License Definition Updates | Yes |
| CER 10.0(1) and later | No | Yes |