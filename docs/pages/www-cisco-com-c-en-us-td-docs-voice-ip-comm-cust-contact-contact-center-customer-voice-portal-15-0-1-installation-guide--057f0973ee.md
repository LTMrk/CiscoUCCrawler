---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-installation-guide--057f0973ee
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/installation/guide/ccvp_b_1501_installation-upgrade-guide-cisco-unified-customer-voice-portal/ccvp_m_1501_unified-cvp-licensing.html
retrieved_at: 2026-08-21T03:01:06.581129+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: April 30, 2025

Chapter: Unified CVP Licensing

## Chapter: Unified CVP Licensing

# Unified CVP Licensing

## License Plan

Unified CVP now supports Smart Licensing which is a flexible software licensing model that streamlines the way you activate
                              and manage Cisco software licenses across your organization. For detailed feature overview on Smart Licensing, see Administration Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

All Unified CVP servers, including Unified CVP server and VoiceXML server, need to register with Cisco SSM . Unified CVP OAMP and CVP Reporting server do not need any licensing registration.

### Upgrading from Classic License

After purchasing, the product licenses will be visible in your Smart Account. If you have a classic license, you will need
                              to convert the PAKs to Smart Account. For more information on converting your classic license to Smart Account, see https://software.cisco.com/web/fw/softwareworkspace/smartlicensing/ssmcompiledhelps/c_conversion_settings.html .

Unified CVP Call Server/VXML Server

Self Service Ports

Unified CVP Server license

The licenses for the ports on the Unified CVP Call Server and the Unified CVP VXML Server. A Unified CVP VXML Server license
                                          is for the number of self-service ports plus queued sessions.

Unified CVP Reporting Server

No License is required for the Unified CVP Reporting Server.

Unified CVP OAMP Server

No License is required for the Unified CVP OAMP Server.

Whenever Unified CVP is installed or upgraded, the Web Service Manager certificate from Unified CVP Call Server/Unified CVP
                                          VXML Server needs to be imported into the keystore of the Unified CVP OAMP/PCCE Server.

For information on the detailed steps, see the Unified CVP Security > Secure Communication between CVP and OAMP Server section of the Cisco CVP Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

## Smart Account

You can request and set up a Smart Account, or request access to an existing Smart Account at http://software.cisco.com .

Step 1

Go to Cisco Software Central – software.cisco.com.

Step 2

Select Request a Smart Account .

Step 3

Enter your information.

For more information on Smart License products and solutions go to https://www.cisco.com/go/smartlicensing .

## Specific License Reservation

Devices (product instances of Unified CVP ) that register with Smart Licensing have to share the license information with Cisco Smart Software Manager ( Cisco SSM ) at regular intervals. Your deployments that cannot periodically share license utilization data with Cisco SSM or due to regulatory reasons can use the Specific License Reservation feature. Cisco offers license reservation as an on-request configuration for such product instances.

You can reserve licenses (including add-on licenses) for your product instance on Cisco SSM . Specific License Reservation is enabled through the option License Management in the Unified CVP NOAMP portal.

The reserved licenses require no renewal or reauthorization unless there is a license usage change on the device. License
                                       reservation provides limited functionality to certain Smart Licensing features such as transfer of licenses between products,
                                       license usage, and asset management.

The Specific License Reservation (SLR) feature does not offer the following benefits that are available as part of the Smart
                                       Licensing feature:

Dynamic movement of license consumption between products

Real-time license usage visibility and asset management

Simplified product registration

Before uninstalling Cisco Unified Customer Voice Portal 15.0(1) to base versions 12.6(1) or 12.5(1), always make sure to return
                                       the license reservation if registered with SLR.

For more information, refer to the Smart Licensing section in the Administration Guide for Cisco Unified Customer Voice Portal 15.0(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

## Unified CVP Redundant Port

The Redundant Port supports a redundancy model in which one or more failover servers are available to take calls when the
                           primary servers are unavailable.

For example, if a customer has purchased 1500 Self-Service ports, these ports can be used across devices or locations or
                           servers. The customer is entitled to run only 1500 ports simultaneously. The total number of calls that receive queuing or
                           self-service treatment cannot exceed 1500.

For all Microapp-based applications (except GS Microapp), when the VXML/IVR ports usage exceeds the system capacity, the call
                                       gets disconnected gracefully. The GS Microapp puts the call on hold until license is available.

## Evaluation License

After installation, Unified CVP runs under the 90-day evaluation period. The 90-day evaluation period is the usage period.
                           At the end of the evaluation period, if the system is not registered with Cisco SSM , it will enter a state of Enforcement where system operations are restricted. For more information, see Out-Of-Compliance and Enforcement Rules section in Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

Register the system with Cisco SSM or Cisco SSM On-Prem within 90-days to avoid getting in the Enforcement state or to exit the Enforcement state.

The Call Server and VXML Server evaluation licenses support 3000 ports on all Call Control ports and Self Service ports. These
                           licenses are useful for testing or evaluation purpose.

For any other licenses such as Non Production System (NPS) or Not for Resale (NFR), refer to the Solutions Ordering Guide .

## Generate a License

### Before you begin

Access the product authorization key (PAK) that you received with the Unified CVP software.

This procedure only applies when you are performing a fresh install of Packaged CCE. If you are upgrading from Unified CVP
                                          Release 11.x to 12.0, use the Unified CVP 11.0 license.

Step 1

Sign in to the Product License Registration Portal at https://tools.cisco.com/SWIFT/LicensingUI/Home .

Step 2

Click Continue to Product License Registration .

Step 3

In the Get New Licenses field, enter your PAK.

You can enter up to 10 PAKs, separated by commas.

Step 4

Click Fulfill .

Step 5

Select your features and enter the quantity.

Step 6

In the Serial Number field, enter the following:

- For a Unified CVP Server or Unified CVP Reporting Server, enter the IP address.

Step 7

Click Next .

Step 8

Accept the terms of the License Agreement, enter your Recipient Information, and click Submit .

Your request is processed.

Step 9

Click Download to download your license.

### What to do next

Ensure that the license file is named as cvp.license .

Copy the license file to C:\Cisco\CVP\conf\license . Shut down gracefully and then restart each of the Call Server components for the new license to take effect.

## Apply and Upgrade
                        	 Call Server/VXML Server/Reporting Server License

Step 1

From the Device
                                          				Management menu, select a Unified CVP component.

The Find,
                                             				  Add, Delete, Edit window lists the Unified CVP components that are
                                          				added to the network map.

Step 2

Click the Unified CVP component link, and then click Edit .

Step 3

From the
                                       			 toolbar, click File
                                             				  Transfer > Licenses .

The File Transfer page appears listing the host name and IP address for the selected Unified CVP component.

Step 4

From Select
                                          				From Available License Files , select the license file, and then
                                       			 click Select .

If the license file is not listed in the Select From Available License Files text box, click Select a License File from Your Local PC and enter the filename in the text box. Alternatively, click Browse to search the license file on the local file system.

Step 5

To transfer
                                       			 the license file to the selected Unified CVP component, click Transfer .

Step 6

Select and restart the Unified CVP component through the Operations Console.

For more information, see Operations Console Online Help for Cisco Unified Customer Voice Portal.

### What to do next

Verify that
                                    				VXML Server is operational and that the license is applied by running the status.bat or status administrative script. Run this script at %CVP_HOME%\VXMLServer\admin and review the output.

On the Operations Console, verify that Reporting Server is operational. For more details, see Operations Console Online Help for Cisco Unified Customer Voice Portal .

For upgrade information, see Solutions Ordering Guide .

For more information about Unified CVP licensing, see Configuration Guide for
                                             				  Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

### Microapps
                           	 Licensing

Beginning with Release 11.5(1), the IVR service that was part of the Call Server is now part of the VXML Server. The Voice
                              Browser sends a request to the VXML Server to service its requests. Whenever the VXML Server receives a request from Voice
                              Browser, it consumes one license.  Microapps, during the execution on VXML Server, consumes an IVR port.

In all Microapps, when the existing VXML license ports are exhausted, the call gets disconnected. However, in GS Microapp,
                                          the on-hold functionality provided by the actual VXML application is executed.

| Unified CVP Component | Required License |
|---|---|
| Unified CVP Call Server/VXML Server | Self Service Ports Unified CVP Server license The licenses for the ports on the Unified CVP Call Server and the Unified CVP VXML Server. A Unified CVP VXML Server license
                                          is for the number of self-service ports plus queued sessions. |
| Unified CVP Reporting Server | No License is required for the Unified CVP Reporting Server. |
| Unified CVP OAMP Server | No License is required for the Unified CVP OAMP Server. |

| Note | Whenever Unified CVP is installed or upgraded, the Web Service Manager certificate from Unified CVP Call Server/Unified CVP
                                          VXML Server needs to be imported into the keystore of the Unified CVP OAMP/PCCE Server. For information on the detailed steps, see the Unified CVP Security > Secure Communication between CVP and OAMP Server section of the Cisco CVP Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
|---|---|

| Step 1 | Go to Cisco Software Central – software.cisco.com. |
|---|---|
| Step 2 | Select Request a Smart Account . |
| Step 3 | Enter your information. For more information on Smart License products and solutions go to https://www.cisco.com/go/smartlicensing . |

| Note | The reserved licenses require no renewal or reauthorization unless there is a license usage change on the device. License
                                       reservation provides limited functionality to certain Smart Licensing features such as transfer of licenses between products,
                                       license usage, and asset management. The Specific License Reservation (SLR) feature does not offer the following benefits that are available as part of the Smart
                                       Licensing feature: Dynamic movement of license consumption between products Real-time license usage visibility and asset management Simplified product registration Before uninstalling Cisco Unified Customer Voice Portal 15.0(1) to base versions 12.6(1) or 12.5(1), always make sure to return
                                       the license reservation if registered with SLR. |
|---|---|

| Note | For all Microapp-based applications (except GS Microapp), when the VXML/IVR ports usage exceeds the system capacity, the call
                                       gets disconnected gracefully. The GS Microapp puts the call on hold until license is available. |
|---|---|

| Note | This procedure only applies when you are performing a fresh install of Packaged CCE. If you are upgrading from Unified CVP
                                          Release 11.x to 12.0, use the Unified CVP 11.0 license. |
|---|---|

| Step 1 | Sign in to the Product License Registration Portal at https://tools.cisco.com/SWIFT/LicensingUI/Home . |
|---|---|
| Step 2 | Click Continue to Product License Registration . |
| Step 3 | In the Get New Licenses field, enter your PAK. You can enter up to 10 PAKs, separated by commas. |
| Step 4 | Click Fulfill . |
| Step 5 | Select your features and enter the quantity. |
| Step 6 | In the Serial Number field, enter the following: For a Unified CVP Server or Unified CVP Reporting Server, enter the IP address. |
| Step 7 | Click Next . |
| Step 8 | Accept the terms of the License Agreement, enter your Recipient Information, and click Submit . Your request is processed. |
| Step 9 | Click Download to download your license. Your license is also sent to you by email. |

| Step 1 | From the Device
                                          				Management menu, select a Unified CVP component. The Find,
                                             				  Add, Delete, Edit window lists the Unified CVP components that are
                                          				added to the network map. |
|---|---|
| Step 2 | Click the Unified CVP component link, and then click Edit . |
| Step 3 | From the
                                       			 toolbar, click File
                                             				  Transfer > Licenses . The File Transfer page appears listing the host name and IP address for the selected Unified CVP component. |
| Step 4 | From Select
                                          				From Available License Files , select the license file, and then
                                       			 click Select . Note If the license file is not listed in the Select From Available License Files text box, click Select a License File from Your Local PC and enter the filename in the text box. Alternatively, click Browse to search the license file on the local file system. | Note | If the license file is not listed in the Select From Available License Files text box, click Select a License File from Your Local PC and enter the filename in the text box. Alternatively, click Browse to search the license file on the local file system. |
| Note | If the license file is not listed in the Select From Available License Files text box, click Select a License File from Your Local PC and enter the filename in the text box. Alternatively, click Browse to search the license file on the local file system. |
| Step 5 | To transfer
                                       			 the license file to the selected Unified CVP component, click Transfer . |
| Step 6 | Select and restart the Unified CVP component through the Operations Console. For more information, see Operations Console Online Help for Cisco Unified Customer Voice Portal. |

| Note | If the license file is not listed in the Select From Available License Files text box, click Select a License File from Your Local PC and enter the filename in the text box. Alternatively, click Browse to search the license file on the local file system. |
|---|---|

| Note | In all Microapps, when the existing VXML license ports are exhausted, the call gets disconnected. However, in GS Microapp,
                                          the on-hold functionality provided by the actual VXML application is executed. |
|---|---|