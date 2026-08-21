---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-security-12-5-1su6-cucm-b-security-guide-1251su6-cucm-m-v150-minimum-es-f7da48aeaa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/12_5_1SU6/cucm_b_security-guide-1251su6/cucm_m_v150-minimum-essential-requirements.html
retrieved_at: 2026-08-21T08:45:05.296383+00:00
---

Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: March 22, 2024

Chapter: V.150 Minimum Essential Requirements

## Chapter: V.150 Minimum Essential Requirements

# V.150 Minimum Essential Requirements

## V.150
                        	 Overview

The V.150 Minimum Essential Requirements feature allows you to make secure calls in a modem over an IP network. The feature
                           uses a dial-up modem for large installed bases of modems and telephony devices operating on a traditional public switched
                           telephone network (PSTN). The V.150.1 recommendation specifically defines how to relay data from modems and telephony devices
                           on a PSTN into and out of an IP network through a modem. The V.150.1 is an ITU-T recommendation for using a modem over IP
                           networks that support dial-up modem calls.

The Cisco V.150.1
                           		Minimum Essential Requirements feature complies with the requirements of the
                           		National Security Agency (NSA) SCIP-216 Minimum Essential Requirements (MER)
                           		for V.150.1 recommendation. The SCIP-216 recommendation has simplified the
                           		existing V.150.1 requirements.

Cisco V.150.1 MER feature supports the following interfaces:

Media Gateway Control Protocol(MGCP) T1(PRI and CAS) and E1(PRI) trunks

Session Initiation Protocol (SIP) trunks

Skinny Client Control Protocol (SCCP) for analog gateway endpoints

Secure Communication Interoperability Protocol-End Instruments (SCIP-EI)

## Configure V.150
                        	 Task Flow

Complete these tasks to add V.150 support in Unified Communications Manager .

Step 1

To Configure Media Resource Group Task Flow , perform the following subtasks:

Add Media Resource Group and Media Resource Group List for V.150 and non V.150 devices.

Step 2

Configure the Gateway for Cisco V.150 (MER)

Add V.150
                                          				functionality to a gateway.

Step 3

Configure V.150 MGCP Gateway Port Interface

If you want to
                                          				use V.150 support across an MGCP gateway, add V.150 support to the port
                                          				interface.

Step 4

Configure V.150 SCCP Gateway Port Interface

If you want to
                                          				use V.150 support across an SCCP gateway, add V.150 support to the port
                                          				interface.

Step 5

Configure V.150 Support for Phone

Add V.150
                                          				support to the phones that will be placing V.150 calls.

Step 6

To Configure SIP Trunk Task Flow , perform one or any of the following subtasks:

Add V.150 support to the SIP trunk that will be used for V.150 calls.

Step 7

To use the V.150 MER feature, you also need to configure IOS on your gateway to support the feature.

For more information on IOS gateway configuration settings, see http://www.cisco.com/c/en/us/td/docs/ios/12_4t/12_4t4/mer_cg_15_1_4M.html .

### Configure Media
                           	 Resource Group Task Flow

Your system should already be set up with basic call control functionality. For instructions on how to set up the call control
                                 system, see System Configuration Guide for Cisco Unified Communications Manager .

For Unified Communications Manager , you must have one of the following releases installed:

The minimum version is Release 10.5(2) SU3

For 11.0, the minimum version will be 11.0(1) SU2

All releases from 11.5(1) on support this feature

You must have Cisco IOS Release 15.6(2)T or later.

V.150 is not supported with Media Termination Point (MTP). We recommend that you remove MTP from devices, trunks, and gateways
                                 that are handling V.150 calls.

Complete these tasks to configure two sets of media resource groups: a media resource group with MTP resources for non-V.150
                                 calls, and a media resource group without MTP resources for V.150 calls.

Step 1

Configure Media Resource Group for Non-V.150 Endpoints

You can configure the Media Resource Group with MTP for non-V.150 endpoints.

Step 2

Configure a Media Resource Group List for Non-V.150 Endpoints

Configure a Media Resource Group list that includes your MTP Media Resources for non-V.150 endpoints.

Step 3

Configure Media Resource Group for V.150 Endpoints

Configure Media Resource Group without MTP resources for secure V.150 calls.

Step 4

Configure a Media Resource Group List for V.150 Endpoints

Configure a Media Resource Group list without MTP after adding the required resources in the Media Resource Group for secure
                                             V.150 endpoints.

#### Configure Media
                              	 Resource Group for Non-V.150 Endpoints

Use this
                                    		  procedure to add a new media resource group that includes MTP resources for
                                    		  non-V.150 endpoints.

Step 1

From Cisco Unified Communications Manager Administration , choose Media Resources > Media Resource Group .

Step 2

Click Add
                                                				New .

Step 3

In the Name field, enter the media resource group name as Do not use with V.150 devices .

Step 4

From the Available Media Resources field, choose only MTP devices and click the down-arrow key .

Step 5

Click Save .

#### Configure a Media
                              	 Resource Group List for Non-V.150 Endpoints

Configure Media Resource Group for Non-V.150 Endpoints

Use this
                                    		  procedure to add new media resource group list with MTP resources for non-V.150
                                    		  end points.

Step 1

From Cisco Unified Communications Manager Administration , choose Media Resources > Media Resource Group List .

Step 2

Click Add
                                                				New .

Step 3

In the Name field, enter a name for the media resource group list as Non- V.150 .

Step 4

From the Available Media Resources field, choose the V.150 MER resource group named Do not use with V.150 Devices and click the down-arrow key .

Step 5

Click Save .

#### Configure Media
                              	 Resource Group for V.150 Endpoints

Use this
                                    		  procedure to add new media resource group without MTP resources for V.150
                                    		  devices.

Step 1

From Cisco Unified Communications Manager Administration , choose Media Resources > Media Resource Group .

Step 2

Click Add
                                                				New .

Step 3

In the Name field, enter the media resource group name as For use with V.150 devices .

Step 4

From the Available Media Resources field, choose multiple devices except the MTP resources and click the down-arrow key .

Step 5

Click Save .

#### Configure a Media
                              	 Resource Group List for V.150 Endpoints

Configure Media Resource Group for V.150 Endpoints

Use this
                                    		  procedure to add a media resource group list without MTP resources for V.150
                                    		  devices.

Step 1

From Cisco Unified Communications Manager Administration , choose Media Resources > Media Resource Group List .

Step 2

Click Add
                                                				New .

Step 3

In the Name field, enter a name for the media resource group list as V.150 .

Step 4

From the Available Media Resources field, choose the V.150 MER resource group named For V.150 Devices and click the down-arrow key .

Step 5

Click Save .

### Configure the
                           	 Gateway for Cisco V.150 (MER)

Step 1

From Cisco Unified Communications Manager Administration , choose Device > Gateway .

Step 2

Click Add
                                             				New .

Step 3

Choose the
                                          			 gateway from the Gateway Type drop-down list.

Step 4

Click Next .

Step 5

From the Protocol drop-down list, choose a protocol.

Step 6

Depending on
                                          			 which Protocol you chose for the gateway, perform:

- For MGCP, in the Domain Name field, enter the domain name
                                             				that is configured on the gateway.

- For SCCP, in the MAC Address (Last 10 Characters) field,
                                             				enter the gateway MAC address.

Step 7

From the Unified Communications Manager Group drop-down list, choose Default .

Step 8

In the Configured Slots, VICs and Endpoints area, perform
                                          			 the following steps:

From each Module drop-down list, select the slot that corresponds to the Network Interface Module hardware that is installed on the gateway.

From each Subunit drop-down list, select the VIC that is installed on the gateway.

Click Save .

Step 9

Complete the
                                          			 remaining fields in the Gateway
                                             				Configuration window. See the online help for more information about
                                          			 the fields and their configuration options.

Step 10

Click Save .

### Configure V.150
                           	 MGCP Gateway Port Interface

Step 1

From Cisco Unified Communications Manager Administration , choose Device > Gateway .

Step 2

Enter the
                                          			 appropriate search criteria to modify the settings for an existing gateway and
                                          			 click Find .

Step 3

In the Configured Slots, VICs, and Endpoints area, locate the module and subunit on which you want to configure a port for V.150 MER and click the corresponding port icon .

Step 4

From the Device
                                             				Protocol drop-down list, choose Digital Access T1 or Digital Access PRI and click Next .

The Device Protocol drop-down list is displayed only if
                                                         				  T1 port is selected in the Configured Slots, VICs, and Endpoints area.

The Gateway Configuration window now displays the port
                                             				interface configuration.

Step 5

Select the Media Resource Group List named V.150 .

Step 6

Check the V150 (subset) check box.

Step 7

Configure the
                                          			 remaining fields, if applicable. See the online help for more information about
                                          			 the fields and their configuration options.

Step 8

Click Save .

Step 9

(Optional) If you want to configure additional port interfaces for the gateway, from the Related Links drop-down list, choose Back to MGCP Configuration and click Go . You can select a different port interface.

### Configure V.150
                           	 SCCP Gateway Port Interface

Step 1

From Cisco Unified Communications Manager Administration , choose Device > Gateway .

Step 2

Enter the
                                          			 appropriate search criteria to modify the settings for an existing SCCP gateway
                                          			 and click Find .

Step 3

In the Configured Slots, VICs, and Endpoints area, locate the module and subunit on which you want to configure a port for V.150 MER and click the corresponding port icon .

Step 4

Select the Media Resource Group List named " V.150 " .

Step 5

In the Product Specific Configuration Layout area, if the Latent Capability Registration Setting drop-down list appears, select Modem Relay or Modem Relay and Passthrough .

Step 6

Configure the remaining fields, if applicable. See the online help for more information about the fields and their configuration
                                          options.

Step 7

Click Save .

### Configure V.150
                           	 Support for Phone

Use this procedure to add V.150 support for a phone. The following phone types support V.150:

Cisco 7962—Third party SCCP end point registered as Cisco 7962

Cisco 7961G-GE—Third party SCCP end point registered as Cisco 7961G-GE

Third Party AS-SIP Endpoints

Step 1

Create an End User with the User ID same as the intended phone number.

Step 2

Configure the Digest Credentials field in the End User Configuration window for Third Party AS-SIP SIP endpoints.

For more information on how to configure a new End User, see the "Provision End Users Manually" chapter in the System Configuration Guide for Cisco Unified Communications Manager

Step 3

From Cisco Unified Communications Manager Administration , choose Device > Phone .

Step 4

Perform
                                          			 either of the following steps:

- To configure V.150 on an
                                             				existing phone, click Find and select the phone.

To
                                                				  configure a new phone for V.150, click Add New .

Step 5

From the Phone Type drop-down list, select one of the phone
                                          			 types that supports V.150, and click Next .

Step 6

For third party SCCP endpoints registered as Cisco 7962, select SCCP from the Device Protocol drop-down list, and click Next .

Step 7

From the Media Resource Group List drop-down menu, select V.150 .

Step 8

For third party AS-SIP SIP endpoints only, Configure the following fields:

- From the Digest User drop-down select the end user for this phone. The end user will be used for digest authentication.

Leave the Media Termination Point Required check box unchecked.

- Check the Early Offer support for voice and video calls check box.

Step 9

Click Save .

Step 10

Click Apply Config .

Step 11

Click OK .

### Configure SIP
                           	 Trunk Task Flow

Step 1

Configure SIP Profile for V.150

Configure a SIP Profile with SIP Best Effort Early Offer support for the SIP trunk.

Step 2

Set the Clusterwide V.150 Filter

Optional. Configure a clusterwide default setting for SIP V.150 SDP Offer Filtering.

Step 3

Add V.150 Filter to SIP Trunk Security Profile

Configure a V.150 Filter within a SIP Trunk Security Profile that you can assign to specific SIP trunks.

Step 4

Configure SIP Trunk for V.150

Configure V.150 support for the SIP trunks that will handle V.150 calls.

#### Configure SIP
                              	 Profile for V.150

Use this procedure to configure a SIP Profile with SIP Best Effort Early Offer support for the SIP trunk.

Step 1

In Cisco Unified Communications Manager Administration , choose Device > Device Settings > SIP Profile .

Step 2

Perform either
                                             			 of the following steps:

- To create a new profile,
                                                				click Add
                                                   				  New .

- To select an existing
                                                				profile, click Find and select a SIP profile.

Step 3

In the Name field, enter the SIP name for V.150.

Step 4

In the Description field, enter the description for V.150.

Step 5

From the Early Offer Support for Voice and video class drop-down list, choose Select Best Effort (no MTP inserted) .

Step 6

Enter any
                                             			 other configuration settings that you want. See the online help for more
                                             			 information about the fields and their configuration options.

Step 7

Click Save .

#### Set the
                              	 Clusterwide V.150 Filter

Use this procedure to configure a clusterwide default setting for SIP V.150 SDP Offer filtering.

If you configure a SIP V.150 SDP Offer Filtering value within a SIP Trunk Security Profile that is different than the clusterwide service parameter setting, the security
                                                profile setting overrides the cluster-wide service parameter setting for the trunks that use that security profile.

Step 1

From Cisco Unified Communications Manager Administration , choose System > Service Parameters .

Step 2

From the Server drop-down list, choose an active server.

Step 3

From the Service drop-down list, choose Cisco CallManager .

Step 4

In the Clusterwide Parameters ( Device- SIP) section, configure a value for the SIP V.150 SDP Offer Filtering service parameter.

Step 5

Choose SIP V.150 SDP Offer Filtering from the drop-down list.

Step 6

Specify the
                                             			 desired filtering action.

Step 7

Click Save .

#### Add V.150 Filter
                              	 to SIP Trunk Security Profile

Use this procedure to assign a V.150 Filter within a SIP Trunk Security Profile.

If you configure a SIP V.150 SDP Offer Filtering value within a SIP Trunk Security Profile that is different than the clusterwide service parameter, the security profile
                                                setting overrides the cluster-wide service parameter setting for the trunks that use that security profile.

Step 1

From Cisco Unified Communications Manager Administration , choose System > Security > SIP Trunk Security Profile .

Step 2

Perform one of
                                             			 the following tasks:

- Enter search criteria and Click Find to choose an existing profile from the list to modify the settings for an existing SIP Trunk Security Profile.

- Click Add New to add a new SIP Trunk Security Profile.

Step 3

Configure a
                                             			 value for the SIP
                                                				V.150 Outbound SDP Offer Filtering drop-down list.

The default setting is to use the value of the SIP V.150 Outbound SDP Offer Filtering cluster-wide service parameter.

Step 4

Configure any remaining fields in the SIP Trunk Security Profile Configuration window. See the online help for more information about the fields and their configuration options.

Step 5

Click Save .

#### Configure SIP
                              	 Trunk for V.150

Use this procedure to configure settings for a SIP trunk.

Step 1

From Cisco Unified Communications Manager Administration , choose Device > Trunk .

Step 2

Perform either
                                             			 of the following steps:

- To create a new profile,
                                                				click Add
                                                   				  New .

- Click Find and select a SIP trunk, to select an existing trunk.

Step 3

For new
                                             			 trunks, do the following:

- From the Trunk Type drop-down list, choose SIP
                                                   				  Trunk .

- From the Protocol Type drop-down list, choose SIP .

- From the Trunk Service Type drop-down list, choose None(Default) .

- Click Next .

Step 4

Enter the SIP
                                             			 trunk name in the Name field.

Step 5

Enter the SIP
                                             			 trunk description in the Description field.

Step 6

From the Media
                                                				Resource Group List drop-down list, choose the Media resource group
                                             			 list named "V.150" .

Step 7

Configure the destination address for the SIP trunk:

In the Destination Address text box, enter an IPv4 address, fully qualified domain name, or DNS SRV record for the server or endpoint that you want
                                                   to connect to the trunk.

If the destination is a DNS SRV record, check the Destination Address is an SRV check box.

To add additional destinations, click (+) button. You can add up to 16 destinations for a SIP trunk.

Step 8

From the SIP
                                                				Trunk Security Profile drop-down list, assign the SIP trunk
                                             			 security profile that you configured for this trunk.

Step 9

From the SIP
                                                				Profile drop-down list, assign the SIP profile that you set up with
                                             			 the Best Effort Early Offer setting.

Step 10

Leave the Media Termination Point Required check box unchecked.

Step 11

Configure any
                                             			 additional fields in the Trunk
                                                				Configuration window. See the online help for more information about
                                             			 the fields and their configuration options.

Step 12

Click Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | To Configure Media Resource Group Task Flow , perform the following subtasks: | Add Media Resource Group and Media Resource Group List for V.150 and non V.150 devices. |
| Step 2 | Configure the Gateway for Cisco V.150 (MER) | Add V.150
                                          				functionality to a gateway. |
| Step 3 | Configure V.150 MGCP Gateway Port Interface | If you want to
                                          				use V.150 support across an MGCP gateway, add V.150 support to the port
                                          				interface. |
| Step 4 | Configure V.150 SCCP Gateway Port Interface | If you want to
                                          				use V.150 support across an SCCP gateway, add V.150 support to the port
                                          				interface. |
| Step 5 | Configure V.150 Support for Phone | Add V.150
                                          				support to the phones that will be placing V.150 calls. |
| Step 6 | To Configure SIP Trunk Task Flow , perform one or any of the following subtasks: | Add V.150 support to the SIP trunk that will be used for V.150 calls. |
| Step 7 | To use the V.150 MER feature, you also need to configure IOS on your gateway to support the feature. | For more information on IOS gateway configuration settings, see http://www.cisco.com/c/en/us/td/docs/ios/12_4t/12_4t4/mer_cg_15_1_4M.html . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Media Resource Group for Non-V.150 Endpoints | You can configure the Media Resource Group with MTP for non-V.150 endpoints. |
| Step 2 | Configure a Media Resource Group List for Non-V.150 Endpoints | Configure a Media Resource Group list that includes your MTP Media Resources for non-V.150 endpoints. |
| Step 3 | Configure Media Resource Group for V.150 Endpoints | Configure Media Resource Group without MTP resources for secure V.150 calls. |
| Step 4 | Configure a Media Resource Group List for V.150 Endpoints | Configure a Media Resource Group list without MTP after adding the required resources in the Media Resource Group for secure
                                             V.150 endpoints. |

| Step 1 | From Cisco Unified Communications Manager Administration , choose Media Resources > Media Resource Group . |
|---|---|
| Step 2 | Click Add
                                                				New . |
| Step 3 | In the Name field, enter the media resource group name as Do not use with V.150 devices . |
| Step 4 | From the Available Media Resources field, choose only MTP devices and click the down-arrow key . The selected devices appear in the Selected Media Resources field. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified Communications Manager Administration , choose Media Resources > Media Resource Group List . |
|---|---|
| Step 2 | Click Add
                                                				New . |
| Step 3 | In the Name field, enter a name for the media resource group list as Non- V.150 . |
| Step 4 | From the Available Media Resources field, choose the V.150 MER resource group named Do not use with V.150 Devices and click the down-arrow key . The selected devices appear in the Selected Media Resources field. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified Communications Manager Administration , choose Media Resources > Media Resource Group . |
|---|---|
| Step 2 | Click Add
                                                				New . |
| Step 3 | In the Name field, enter the media resource group name as For use with V.150 devices . |
| Step 4 | From the Available Media Resources field, choose multiple devices except the MTP resources and click the down-arrow key . The selected devices appear in the Selected Media Resources field. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified Communications Manager Administration , choose Media Resources > Media Resource Group List . |
|---|---|
| Step 2 | Click Add
                                                				New . |
| Step 3 | In the Name field, enter a name for the media resource group list as V.150 . |
| Step 4 | From the Available Media Resources field, choose the V.150 MER resource group named For V.150 Devices and click the down-arrow key . The selected media resource groups appear in the Selected Media Resources field. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified Communications Manager Administration , choose Device > Gateway . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | Choose the
                                          			 gateway from the Gateway Type drop-down list. |
| Step 4 | Click Next . |
| Step 5 | From the Protocol drop-down list, choose a protocol. |
| Step 6 | Depending on
                                          			 which Protocol you chose for the gateway, perform: For MGCP, in the Domain Name field, enter the domain name
                                             				that is configured on the gateway. For SCCP, in the MAC Address (Last 10 Characters) field,
                                             				enter the gateway MAC address. |
| Step 7 | From the Unified Communications Manager Group drop-down list, choose Default . |
| Step 8 | In the Configured Slots, VICs and Endpoints area, perform
                                          			 the following steps: From each Module drop-down list, select the slot that corresponds to the Network Interface Module hardware that is installed on the gateway. From each Subunit drop-down list, select the VIC that is installed on the gateway. Click Save . The port icons appear. Each port icon corresponds to an available port interface on the gateway. You can configure any port interface by clicking the corresponding port icon . |
| Step 9 | Complete the
                                          			 remaining fields in the Gateway
                                             				Configuration window. See the online help for more information about
                                          			 the fields and their configuration options. |
| Step 10 | Click Save . |

| Step 1 | From Cisco Unified Communications Manager Administration , choose Device > Gateway . |
|---|---|
| Step 2 | Enter the
                                          			 appropriate search criteria to modify the settings for an existing gateway and
                                          			 click Find . |
| Step 3 | In the Configured Slots, VICs, and Endpoints area, locate the module and subunit on which you want to configure a port for V.150 MER and click the corresponding port icon . |
| Step 4 | From the Device
                                             				Protocol drop-down list, choose Digital Access T1 or Digital Access PRI and click Next . Note The Device Protocol drop-down list is displayed only if
                                                         				  T1 port is selected in the Configured Slots, VICs, and Endpoints area. The Gateway Configuration window now displays the port
                                             				interface configuration. | Note | The Device Protocol drop-down list is displayed only if
                                                         				  T1 port is selected in the Configured Slots, VICs, and Endpoints area. |
| Note | The Device Protocol drop-down list is displayed only if
                                                         				  T1 port is selected in the Configured Slots, VICs, and Endpoints area. |
| Step 5 | Select the Media Resource Group List named V.150 . |
| Step 6 | Check the V150 (subset) check box. |
| Step 7 | Configure the
                                          			 remaining fields, if applicable. See the online help for more information about
                                          			 the fields and their configuration options. |
| Step 8 | Click Save . |
| Step 9 | (Optional) If you want to configure additional port interfaces for the gateway, from the Related Links drop-down list, choose Back to MGCP Configuration and click Go . You can select a different port interface. |

| Note | The Device Protocol drop-down list is displayed only if
                                                         				  T1 port is selected in the Configured Slots, VICs, and Endpoints area. |
|---|---|

| Step 1 | From Cisco Unified Communications Manager Administration , choose Device > Gateway . |
|---|---|
| Step 2 | Enter the
                                          			 appropriate search criteria to modify the settings for an existing SCCP gateway
                                          			 and click Find . |
| Step 3 | In the Configured Slots, VICs, and Endpoints area, locate the module and subunit on which you want to configure a port for V.150 MER and click the corresponding port icon . |
| Step 4 | Select the Media Resource Group List named " V.150 " . |
| Step 5 | In the Product Specific Configuration Layout area, if the Latent Capability Registration Setting drop-down list appears, select Modem Relay or Modem Relay and Passthrough . |
| Step 6 | Configure the remaining fields, if applicable. See the online help for more information about the fields and their configuration
                                          options. |
| Step 7 | Click Save . |

| Step 1 | Create an End User with the User ID same as the intended phone number. |
|---|---|
| Step 2 | Configure the Digest Credentials field in the End User Configuration window for Third Party AS-SIP SIP endpoints. For more information on how to configure a new End User, see the "Provision End Users Manually" chapter in the System Configuration Guide for Cisco Unified Communications Manager |
| Step 3 | From Cisco Unified Communications Manager Administration , choose Device > Phone . |
| Step 4 | Perform
                                          			 either of the following steps: To configure V.150 on an
                                             				existing phone, click Find and select the phone. To
                                                				  configure a new phone for V.150, click Add New . |
| Step 5 | From the Phone Type drop-down list, select one of the phone
                                          			 types that supports V.150, and click Next . |
| Step 6 | For third party SCCP endpoints registered as Cisco 7962, select SCCP from the Device Protocol drop-down list, and click Next . |
| Step 7 | From the Media Resource Group List drop-down menu, select V.150 . |
| Step 8 | For third party AS-SIP SIP endpoints only, Configure the following fields: From the Digest User drop-down select the end user for this phone. The end user will be used for digest authentication. Leave the Media Termination Point Required check box unchecked. Check the Early Offer support for voice and video calls check box. |
| Step 9 | Click Save . |
| Step 10 | Click Apply Config . |
| Step 11 | Click OK . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure SIP Profile for V.150 | Configure a SIP Profile with SIP Best Effort Early Offer support for the SIP trunk. |
| Step 2 | Set the Clusterwide V.150 Filter | Optional. Configure a clusterwide default setting for SIP V.150 SDP Offer Filtering. |
| Step 3 | Add V.150 Filter to SIP Trunk Security Profile | Configure a V.150 Filter within a SIP Trunk Security Profile that you can assign to specific SIP trunks. |
| Step 4 | Configure SIP Trunk for V.150 | Configure V.150 support for the SIP trunks that will handle V.150 calls. |

| Step 1 | In Cisco Unified Communications Manager Administration , choose Device > Device Settings > SIP Profile . |
|---|---|
| Step 2 | Perform either
                                             			 of the following steps: To create a new profile,
                                                				click Add
                                                   				  New . To select an existing
                                                				profile, click Find and select a SIP profile. |
| Step 3 | In the Name field, enter the SIP name for V.150. |
| Step 4 | In the Description field, enter the description for V.150. |
| Step 5 | From the Early Offer Support for Voice and video class drop-down list, choose Select Best Effort (no MTP inserted) . |
| Step 6 | Enter any
                                             			 other configuration settings that you want. See the online help for more
                                             			 information about the fields and their configuration options. |
| Step 7 | Click Save . |

| Note | If you configure a SIP V.150 SDP Offer Filtering value within a SIP Trunk Security Profile that is different than the clusterwide service parameter setting, the security
                                                profile setting overrides the cluster-wide service parameter setting for the trunks that use that security profile. |
|---|---|

| Step 1 | From Cisco Unified Communications Manager Administration , choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose an active server. |
| Step 3 | From the Service drop-down list, choose Cisco CallManager . |
| Step 4 | In the Clusterwide Parameters ( Device- SIP) section, configure a value for the SIP V.150 SDP Offer Filtering service parameter. |
| Step 5 | Choose SIP V.150 SDP Offer Filtering from the drop-down list. |
| Step 6 | Specify the
                                             			 desired filtering action. |
| Step 7 | Click Save . |

| Note | If you configure a SIP V.150 SDP Offer Filtering value within a SIP Trunk Security Profile that is different than the clusterwide service parameter, the security profile
                                                setting overrides the cluster-wide service parameter setting for the trunks that use that security profile. |
|---|---|

| Step 1 | From Cisco Unified Communications Manager Administration , choose System > Security > SIP Trunk Security Profile . |
|---|---|
| Step 2 | Perform one of
                                             			 the following tasks: Enter search criteria and Click Find to choose an existing profile from the list to modify the settings for an existing SIP Trunk Security Profile. Click Add New to add a new SIP Trunk Security Profile. |
| Step 3 | Configure a
                                             			 value for the SIP
                                                				V.150 Outbound SDP Offer Filtering drop-down list. Note The default setting is to use the value of the SIP V.150 Outbound SDP Offer Filtering cluster-wide service parameter. | Note | The default setting is to use the value of the SIP V.150 Outbound SDP Offer Filtering cluster-wide service parameter. |
| Note | The default setting is to use the value of the SIP V.150 Outbound SDP Offer Filtering cluster-wide service parameter. |
| Step 4 | Configure any remaining fields in the SIP Trunk Security Profile Configuration window. See the online help for more information about the fields and their configuration options. |
| Step 5 | Click Save . |

| Note | The default setting is to use the value of the SIP V.150 Outbound SDP Offer Filtering cluster-wide service parameter. |
|---|---|

| Step 1 | From Cisco Unified Communications Manager Administration , choose Device > Trunk . |
|---|---|
| Step 2 | Perform either
                                             			 of the following steps: To create a new profile,
                                                				click Add
                                                   				  New . Click Find and select a SIP trunk, to select an existing trunk. |
| Step 3 | For new
                                             			 trunks, do the following: From the Trunk Type drop-down list, choose SIP
                                                   				  Trunk . From the Protocol Type drop-down list, choose SIP . From the Trunk Service Type drop-down list, choose None(Default) . Click Next . |
| Step 4 | Enter the SIP
                                             			 trunk name in the Name field. |
| Step 5 | Enter the SIP
                                             			 trunk description in the Description field. |
| Step 6 | From the Media
                                                				Resource Group List drop-down list, choose the Media resource group
                                             			 list named "V.150" . |
| Step 7 | Configure the destination address for the SIP trunk: In the Destination Address text box, enter an IPv4 address, fully qualified domain name, or DNS SRV record for the server or endpoint that you want
                                                   to connect to the trunk. If the destination is a DNS SRV record, check the Destination Address is an SRV check box. To add additional destinations, click (+) button. You can add up to 16 destinations for a SIP trunk. |
| Step 8 | From the SIP
                                                				Trunk Security Profile drop-down list, assign the SIP trunk
                                             			 security profile that you configured for this trunk. |
| Step 9 | From the SIP
                                                				Profile drop-down list, assign the SIP profile that you set up with
                                             			 the Best Effort Early Offer setting. |
| Step 10 | Leave the Media Termination Point Required check box unchecked. |
| Step 11 | Configure any
                                             			 additional fields in the Trunk
                                                				Configuration window. See the online help for more information about
                                             			 the fields and their configuration options. |
| Step 12 | Click Save . |