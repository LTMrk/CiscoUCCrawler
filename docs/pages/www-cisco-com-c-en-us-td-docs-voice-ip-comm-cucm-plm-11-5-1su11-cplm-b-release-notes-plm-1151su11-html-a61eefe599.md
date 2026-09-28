---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-11-5-1su11-cplm-b-release-notes-plm-1151su11-html-a61eefe599
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/11_5_1SU11/cplm-b-release-notes-plm-1151su11.html
retrieved_at: 2026-09-07T15:49:36.364829+00:00
---

Release Notes for Cisco Prime License Manager, Release 11.5(1)SU11

# Release Notes for Cisco Prime License Manager, Release 11.5(1)SU11

### Download Options

Updated: April 7, 2022

First Published: April 7, 2022

# About Cisco Prime License Manager

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

## Important Notes

### Manual License
                  	 Fulfillment

The license fulfilled with the first license request must be
                        		  installed before subsequent license requests are generated.

### Pre-Upgrade COP
                  	 File

You can upgrade to Cisco Prime License Manager Release 11.5(1) from Cisco Prime License Manager Release 11.x or Enterprise
                        License Manager Release 9.x. While upgrading from Cisco Prime License Manager Release 10.x or 11.x to Cisco Prime License
                        Manager Release 11.5(1) is a direct upgrade, upgrading from pre-10.0(1) requires one or more COP files. Depending on the upgrade
                        path, you may need to download and install one or both of the following COP files from Cisco.com:

elm_Elm_v9_1_1_PlmUpgrade.cop.sgn

ciscocm.version3-keys.cop.sgn

For information about which COP file you need to apply prior to performing an upgrade, see topics relating to license management
                                 in the Compatibility Information for Cisco Unified Communications Manager .

The elm_Elm_v9_1_1_PlmUpgrade.cop.sgn COP file provides the means for a 9.1(1) standalone Enterprise License Manager server
                        installation to upgrade to 10.x or later standalone Cisco Prime License Manager software.

This cop file is not required for 9.1(2) systems. The version3-keys file is required.

The
                        		  ciscocm.version3-keys.cop.sgn COP file has the RSA keys that are required to
                        		  validate the upgrade. Missing RSA-3 keys will, for example, result in status
                        		  errors in the Software Installation/Upgrade window.

Without the RSA-3 key update, validation fails even if the md5sum value of the ISO is correct.

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

### Deployment

In Release 10.0(1)
                        		  and later, virtualized deployments of Cisco Prime License Manager are only
                        		  supported on VMware ESXi hypervisor hosts.

### Set Manual
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

### Browser
                  	 Support

The following web browsers are supported:

Firefox with Windows 10 (64-bit)

Chrome with Windows 10 (64-bit)

Internet Explorer 11 with Windows 10 (64-bit)

Internet Explorer 11 with Windows 7 (64-bit)

Internet Explorer 11 with Windows 8.1 (64-bit)

Microsoft Edge browser with Windows 10 (32-bit/64-bit)

Safari with MacOS (10.x)

We recommend that you use the latest version for all the web browsers supported.

### Supported Languages

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

### Upgrade Prime License Manager

Install the ciscocm.elm.switchversion.V1.k3.cop.sgn COP file, while upgrading Cisco Prime License Manager from any of the following versions to Cisco Prime License Manager version
                        11.5.1 SU2 or any higher version.

11.5.1.11900-5 - PLM 11.5.1 SU1a

11.5.1.11900-4 - PLM 11.5.1 SU1

11.5.1.12001-2 - PLM 11.5.1 ES(12001-2)

11.5.1.12001-1 - PLM 11.5.1 ES(12001-1)

## Caveats

### Bug Search
                  	 Tool

The system grades known problems (bugs) per severity level. These release notes contain descriptions of the following bug
                     levels:

All severity level 1 or 2 bugs

Significant severity level 3 bugs

All customer-found bugs

You can
                     		search for open and resolved caveats of any severity for any release using the Cisco Bug Search tool, an online tool
                     		  available for customers to query defects according to their own needs.

To access the Cisco Bug Search tool, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Follow these
                     		steps to use Cisco Bug Search tool:

Access the Cisco Bug Search tool: https://bst.cloudapps.cisco.com/bugsearch .

Log in with your
                           			 Cisco.com user ID and password.

If you are looking for information about a specific problem, enter the bug ID number in the Search for: field and click Go .

Tip

Click Help on the Bug Search page for information about
                                 		  how to search for bugs, create saved searches, and create bug groups.

### Open Caveats

There are no known issues in this release.

### Resolved Caveats

The following table lists severity 1, 2, and 3 defects that are resolved for Cisco Prime License Manager 11.5(1)SU11. For
                        more information about an individual caveat, click the Identifier.

Identifier

Headline

CSCvx00485

QuoVadis root CA decommission on Prime License Manager

CSCvy96356

CIAM: postgre-sql 9.3.9 CVE-2020-25695 and others

CSCwa82088

Copyright year has to be changed to 2022 from 2021 on 11.5SU11 PLM Page

CSCwa77221

Cisco Prime License Manager Assessment of CVE-2021-4034 Pwnkit

CSCwa56250

NSS remote code execution

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

| Tip | Click Help on the Bug Search page for information about
                                 		  how to search for bugs, create saved searches, and create bug groups. |
|---|---|

| Identifier | Headline |
|---|---|
| CSCvx00485 | QuoVadis root CA decommission on Prime License Manager |
| CSCvy96356 | CIAM: postgre-sql 9.3.9 CVE-2020-25695 and others |
| CSCwa82088 | Copyright year has to be changed to 2022 from 2021 on 11.5SU11 PLM Page |
| CSCwa77221 | Cisco Prime License Manager Assessment of CVE-2021-4034 Pwnkit |
| CSCwa56250 | NSS remote code execution |