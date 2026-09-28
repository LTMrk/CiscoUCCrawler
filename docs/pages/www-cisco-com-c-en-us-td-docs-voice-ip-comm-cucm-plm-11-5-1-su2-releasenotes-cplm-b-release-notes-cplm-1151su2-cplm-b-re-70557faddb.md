---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-11-5-1-su2-releasenotes-cplm-b-release-notes-cplm-1151su2-cplm-b-re-70557faddb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/11_5_1_SU2/releasenotes/cplm_b_release-notes-cplm-1151su2/cplm_b_release-notes-cplm-1151su2_chapter_010.html
retrieved_at: 2026-08-21T07:08:58.720979+00:00
---

Release Notes for Cisco Prime License Manager, Release 11.5(1)SU2

# Release Notes for Cisco Prime License Manager, Release 11.5(1)SU2

## Results

Updated: March 22, 2018

Chapter: Important Notes

## Chapter: Important Notes

# Important Notes

## Manual License
                        	 Fulfillment

The license fulfilled with the first license request must be
                              		  installed before subsequent license requests are generated.

## Pre-Upgrade COP
                        	 File

You can upgrade to Cisco Prime License Manager Release 11.5(1) from Cisco Prime License Manager Release 11.x or Enterprise
                              License Manager Release 9.x. While upgrading from Cisco Prime License Manager Release 10.x or 11.x to Cisco Prime License
                              Manager Release 11.5(1) is a direct upgrade, upgrading from pre-10.0(1) requires one or more COP files. Depending on the upgrade
                              path, you may need to download and install one or both of the following COP files from Cisco.com:

elm_Elm_v9_1_1_PlmUpgrade.cop.sgn

ciscocm.version3-keys.cop.sgn

The elm_Elm_v9_1_1_PlmUpgrade.cop.sgn COP file provides the means for a 9.1(1) standalone Enterprise License Manager server
                              installation to upgrade to 10.x or later standalone Cisco Prime License Manager software.

The
                              		  ciscocm.version3-keys.cop.sgn COP file has the RSA keys that are required to
                              		  validate the upgrade. Missing RSA-3 keys will, for example, result in status
                              		  errors in the Software Installation/Upgrade window.

To find COP files on Cisco.com, navigate to the software patches specific to your release: Support > Downloads > Unified Communications > Unified Communications Management > Cisco Prime License Manager .

You can verify
                              		  that you have the correct COP file installed by entering the following
                              		  commands:

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

Step 1

Using vCenter or vSphere
                                       			 Client, select Edit
                                          				virtual machine settings .

Step 2

Select Network
                                          				adapter 1 .

Step 3

Take note of
                                       			 the MAC address.

Step 4

Select the
                                       			 manual option for the MAC address.

Step 5

Set the MAC
                                       			 address as noted earlier, or set another unique MAC address.

Step 6

Select OK to save
                                       			 the settings.

## Browser
                        	 Support

The following web browsers are supported:

Firefox with Windows 10 (64-bit)

Chrome with Windows 10 (64-bit)

Internet Explorer 11 with Windows 10 (64-bit)

Internet Explorer 11 with Windows 7 (64-bit)

Internet Explorer 11 with Windows 8.1 (64-bit)

Microsoft Edge browser with Windows 10 (32-bit/64-bit)

Safari with MacOS (10.x)

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

## Upgrade Prime License Manager

Install the ciscocm.elm.switchversion.V1.k3.cop.sgn COP file, while upgrading Cisco Prime License Manager from any of the following versions to Cisco Prime License Manager version
                              11.5.1 SU2 or any higher version.

11.5.1.11900-5 - PLM 11.5.1 SU1a

11.5.1.11900-4 - PLM 11.5.1 SU1

11.5.1.12001-2 - PLM 11.5.1 ES(12001-2)

11.5.1.12001-1 - PLM 11.5.1 ES(12001-1)

## Synchronization Failure with Application Error

If you see an application error during synchronization with Unified Communications Manager of 11.5.1 SU3 or of a higher version,
                              the error is actually a version mismatch error.

| Note | For information about which COP file you need to apply prior to performing an upgrade, see topics relating to license management
                                       in the Compatibility Information for Cisco Unified Communications Manager . |
|---|---|

| Note | This cop file is not required for 9.1(2) systems. The version3-keys file is required. |
|---|---|

| Note | Without the RSA-3 key update, validation fails even if the md5sum value of the ISO is correct. |
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

| Note | We recommend that you use the latest version for all the web browsers supported. |
|---|---|