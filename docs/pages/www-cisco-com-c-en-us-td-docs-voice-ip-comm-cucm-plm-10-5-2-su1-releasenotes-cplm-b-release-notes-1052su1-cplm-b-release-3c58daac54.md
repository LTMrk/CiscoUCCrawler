---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-10-5-2-su1-releasenotes-cplm-b-release-notes-1052su1-cplm-b-release-3c58daac54
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/10_5_2_SU1/releasenotes/cplm_b_release-notes-1052su1/cplm_b_release-notes-cplm-1052su1_chapter_01.html
retrieved_at: 2026-09-08T04:52:02.497271+00:00
---

Release Notes for Cisco Prime License Manager, Release 10.5(2)SU1a

# Release Notes for Cisco Prime License Manager, Release 10.5(2)SU1a

## Results

Updated: September 27, 2017

Chapter: Important Notes

## Chapter: Important Notes

# Important Notes

## Pre-Upgrade COP File

You can upgrade to Cisco Prime License Manager Release 10.5(x) from Cisco Prime License Manager Release 10.0(1) or Enterprise
                              License Manager Release 9.x. 
                              		While upgrading from Cisco Prime License Manager Release 10.0(1) to Cisco Prime License Manager Release 10.5(x) is a direct
                              upgrade, upgrading from pre-10.0(1) requires one or more  COP files. Depending on the upgrade path, you may need to download
                              and install one or both of the following COP files from Cisco.com:

- elm_Elm_v9_1_1_PlmUpgrade.cop.sgn

- ciscocm.version3-keys.cop.sgn

For information about which COP file you need to apply prior to performing an upgrade, see topics relating to license management
                                          in the Compatibility Information for Cisco Unified Communications Manager : http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-device-support-tables-list.html .

The elm_Elm_v9_1_1_PlmUpgrade.cop.sgn COP file provides the means
                              for a 9.1(1) standalone Enterprise License Manager server installation to upgrade to 10.x
                              or greater standalone Cisco Prime License Manager software.

The ciscocm.version3-keys.cop.sgn COP file has the RSA keys that are required to
                              		  validate the upgrade. Missing RSA-3 keys will, for example, result in status
                              		  errors in the Software Installation/Upgrade window.

Validation will
                                          		  fail even if the md5sum value of the ISO is correct.

To find COP files
                              		  on Cisco.com, navigate to Support > Downloads > Unified
                                    				Communications > Unified Communications Management > Cisco Prime License Manager > Cisco Prime License Manager 10.5 > Prime License Manager Software Patches .

You can verify that you
                              		  have the correct COP file installed by entering  the following commands:

admin:show version active

Active Master Version:
                                 			 <8.5.1.10000-26>

Active Version Installed
                                 			 Software Options:

<ciscocm.version3-keys.cop>

admin:

## Deployment

In Release 10.0(1)
                              		  and later, virtualized deployments of Cisco Prime License Manager are only
                              		  supported on VMware ESXi hypervisor hosts.

## Set Manual
                        	 MAC

On a virtual machine, the MAC can be dynamic or static (manual). We recommend a static MAC because the licenses are linked
                              to MAC. Configure virtual machines with static (manual) MAC by following  the steps below.

Using vCenter or vSphere
                                       			 Client, select Edit
                                          				virtual machine settings .

Select Network
                                          				adapter 1 .

Take note of
                                       			 the MAC address.

Select the
                                       			 manual option for the MAC address.

Set the MAC
                                       			 address as noted earlier, or set another unique MAC address.

Select OK to save
                                       			 the settings.

## Browser
                        	 Support

The following
                              		  browser versions are officially supported by Cisco Prime License Manager:

Edge

20.10240

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

## Manual License
                        	 Fulfillment

The license fulfilled with the first license request must be
                              		  installed before subsequent license requests are generated.

| Note | For information about which COP file you need to apply prior to performing an upgrade, see topics relating to license management
                                          in the Compatibility Information for Cisco Unified Communications Manager : http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-device-support-tables-list.html . |
|---|---|

| Note | Validation will
                                          		  fail even if the md5sum value of the ISO is correct. |
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
| Firefox | 17 -
                                       					 33 , 45.0b10 |
| Internet Explorer | 9, 10
                                       					 , 11 |
| Chrome | 23 -
                                       					 38 , 49.0.2623.75 |
| Safari | 6.0 ,
                                       					 9.0.3 |
| Edge | 20.10240 |