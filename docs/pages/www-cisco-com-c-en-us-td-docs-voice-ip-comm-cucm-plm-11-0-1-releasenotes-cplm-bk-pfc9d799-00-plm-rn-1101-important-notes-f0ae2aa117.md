---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-11-0-1-releasenotes-cplm-bk-pfc9d799-00-plm-rn-1101-important-notes-f0ae2aa117
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/11_0_1/releasenotes/CPLM_BK_PFC9D799_00_plm-rn-1101/important_notes_1101.html
retrieved_at: 2026-09-08T04:50:51.689167+00:00
---

Release Notes for Cisco Prime License Manager, Release 11.0(1)

# Release Notes for Cisco Prime License Manager, Release 11.0(1)

## Results

Updated: June 12, 2015

Chapter: Important Notes

## Chapter: Important Notes

# Important Notes

## Manual License
	 Fulfillment

The initial license file fulfillment must be installed and a new
		  license request obtained before requesting subsequent license fulfillment.

## Pre-Upgrade COP File

elm_Elm_v9_1_1_PlmUpgrade.cop.sgn

ciscocm.version3-keys.cop.sgn

For information about which COP file you need to apply prior to performing an upgrade, see topics relating to license management in the Compatibility Information for Cisco Unified Communications Manager at http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​products-device-support-tables-list.html

The elm_Elm_v9_1_1_PlmUpgrade.cop.sgn COP file provides the means for a 9.1(1) standalone Enterprise License Manager server installation to upgrade to 10.x or later standalone Cisco Prime License Manager software.

The ciscocm.version3-keys.cop.sgn COP file has the RSA keys that are required to validate the upgrade. Missing RSA-3 keys will, for example, result in status errors in the Software Installation/Upgrade window.

Validation will fail even if the md5sum value of the ISO is correct.

To find COP files on Cisco.com, navigate to the software patches specific to your release: Support > Downloads > Unified Communications > Unified Communications Management > Cisco Prime License Manager .

You can verify that you have the correct COP file installed by entering the following commands:

admin:show version active

Active Master Version:
			 <8.5.1.10000-26>

Active Version Installed
			 Software Options:

<ciscocm.version3-keys.cop>

admin:

## Deployment

In Release 10.0(1) and later, virtualized
		  deployments of Cisco Prime License Manager, formally known as Enterprise
		  License Manager, are only supported on VMware ESXi hypervisor hosts.

## Set Manual
	 MAC

On a virtual machine, the MAC can be dynamic or static (manual). We recommend a static MAC because the licenses are linked to MAC. Configure virtual machines with static (manual) MAC by following  the steps below.

## Browser
	 Support

The following
		  browser versions are officially supported by Cisco Prime License Manager:

## Supported Languages

Cisco Prime
		  License Manager supports 13 languages:

English
				(default)

Japanese 
			 (Japan)

Chinese
				(simplified)

Chinese (traditional)

Korean (Korea)

German(Germany)

French
				(France)

Italian (Italy)

Spanish
				(Spain)

Spanish
				(Colombia)

Portuguese
				(Brazil)

Dutch
				(Netherlands)

Russian 
			 (Russia)

| Note | For information about which COP file you need to apply prior to performing an upgrade, see topics relating to license management in the Compatibility Information for Cisco Unified Communications Manager at http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​products-device-support-tables-list.html |
|---|---|

| Note | Validation will fail even if the md5sum value of the ISO is correct. |
|---|---|

| Step 1 | Using vCenter or vSphere
			 Client, select Edit
				virtual machine settings . |
|---|---|
| Step 2 | Select Network
				adapter 1 . |
| Step 3 | Take note of
			 the MAC address. |
| Step 4 | Select the
			 manual option for the MAC address. |
| Step 5 | Set the MAC
			 address as noted earlier, or set another unique MAC address. |
| Step 6 | Select OK to save
			 the settings. |

| Browser | Supported Version |
|---|---|
| Firefox | 17 - 33 |
| Internet Explorer | 9, 10 |
| Chrome | 23 - 38 |
| Safari | 6.0 |