---
doc_id: www-cisco-com-c-en-us-td-docs-solutions-cvd-collaboration-hybrid-14-hybcvd-hcallsvc-html-9b48c13dcd
source_url: https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/hybrid/14/hybcvd/hcallsvc.html
retrieved_at: 2026-08-16T18:23:59.274121+00:00
---

Preferred Architecture for Cisco Webex Hybrid Services, CVD

# Preferred Architecture for Cisco Webex Hybrid Services, CVD

Updated: April 27, 2020

Chapter: Cisco Webex Hybrid Call Service

## Chapter: Cisco Webex Hybrid Call Service

## Webex Hybrid Call Service

Revised: October 22, 2021

Webex Hybrid Call Service provides seamlessly connection between Webex and Cisco Unified Communications Manager (Unified CM) as the on-premises enterprise call control.

This solution contains Webex App with native Unified CM registration, and Webex devices linked to Webex via Webex Edge for Devices Webex. Webex Edge for Devices architecture is discussed in this article:

https://help.webex.com/en-US/article/cy212z/Webex-Edge-for-Devices

In the context of this document hybrid calling consists of the following solutions:

- Webex App registered to both on-premises Unified CM and Webex

- Webex devices registered to Unified CM and linked to Webex for meetings and advanced functions

This chapter introduces important updates to the hybrid calling architecture for users and Webex devices:

- Webex App can now natively register to Unified CM and to the Webex cloud simultaneously

- When registered to Unified CM, Webex App uses the same device types that Jabber uses. The architecture, design considerations and deployment for Webex App with Unified CM calling are the same for as they are for Jabber, with a few exceptions which are outlined in this chapter.

- If Unified CM users have already been enabled for Jabber, no additional steps are required to enable Webex App with Unified CM calling. Both applications can be installed in the same laptop, but only one can be registered to Unified CM at a time.

- Webex devices (known as “Workspaces” in Webex Control Hub) no longer require the Cisco Call Connector.

- The Cisco Call Connector is replaced by the “Webex Device Connector”, a plug-in which runs on Mac or Windows PC and is used only for provisioning.

## Overview

Webex Hybrid Calling enables Webex App users and Webex devices to make and receive calls using the same dialing procedures used by endpoints registered with Cisco Unified CM.

Webex Hybrid Calling consists of two main calling features:

- Hybrid Calling for Webex App (Unified CM): enables Webex users to make and receive calls on their client through native registration of Webex App to Unified CM.

- Hybrid Calling for Webex devices: enables Webex devices for dual registration to Unified CM and Webex at the same time to keep the experience consistent with Unified CM and allows for enhanced Webex features. When a Webex device is enabled for such a functionality, it is said to be “linked” to Webex via Webex Edge for Devices, one of the deployment options of the Webex Device Connector.

### Recommended Deployment

Calling in Webex App (Unified CM) is based on native registration of the Webex App to Unified CM. As such Webex App registers to Unified CM inheriting all the benefits of Unified CM features, including Unified CM directory, corporate dial plan, user dialing habits and phone services. Registration of Webex App to Unified CM happens directly when the application is located on-premises, or via Mobile and Remote Access (MRA) when the application is located on the Internet.

As a result of this direct registration to Unified CM a variety of native calling features become available to the Webex App such as:

- Shared line: By assigning the same directory line to both the Webex App and the Unified CM device, Webex App has access to shared line functionality.

- Direct media path: Two on-premises Webex App registered to Unified CM have a direct media path. Media is not sent to the Webex Cloud.

Webex devices are Webex linked through the Webex Device Connector: Webex Device Connector supports three different options:

- Webex device cloud onboarding: This option allows to register Webex devices to the cloud via bulk onboarding

- Webex Edge for Devices: With Webex Edge devices get access to Webex cloud capabilities, while still keeping your calling and media on-premises

In this document the second option, Webex Edge for Devices is recommended, because it allows for a better integration with on-premises infrastructure and services, at the same time adding advanced cloud capabilities such as cloud-managed software upgrades and Webex optimized experiences including features like face recognition.

The Webex Device Connector is an application, downloadable from Control Hub, that runs on PC or Mac and connects on one side to Unified CM via Administrative XML (AXL) providing the Device Connector with access to Unified CM provisioning. On the other side of the Device Connector HTTPS is used to communicate with Webex (See Figure 4-1 ). This connection traverses the customer’s Internet proxy or Internet edge and does not use the firewall traversal features of the Expressway-C and Expressway-E for setup.

Figure 4-1 Webex Device Connector Provides Communication Between Unified CM and Webex for Device Provisioning

When the Webex Device Connector is used with the second option (Webex Edge for Devices), it connects to the Unified CM cluster and retrieves the list of Unified CM video devices compatible with Webex. The tool then provides the option to “link” these devices to Webex. This can be done one-by-one, or in bulk by clicking the “Link all” option. As a response, Webex creates activation codes for those devices, and those activation codes are passed on to Unified CM via Webex Device Connector. Then Unified CM uses those activation codes to link the selected devices to Webex. This flow works with Unified CM version 11.5(1) SU3 or 12.5(1) and later.

### Key Benefits

Webex Hybrid Call Service provides the following key benefits:

- Native Unified CM registration for Webex App and Webex devices

- Increased security with firewall traversal architecture for signaling and media

- Mobile and remote access architecture for Webex App and Webex devices when located on the public Internet

- Optimized call flow for Webex devices

## Architecture

The Webex Hybrid Calling architecture includes both Webex App and Webex devices registered directly to Unified CM and Webex simultaneously. These two solutions differ in the following ways.

Both the Webex App and Webex Devices have a SIP interface which communicates to Unified CM as well as a Webex interface which communicates directly with Webex. Webex App can use the Webex interface or the SIP interface for point-to-point and multi-point calls based on a set of conditions and configuration discussed later in this document.

Webex devices use the Webex interface to send calls to Webex only when a meeting is dialed. In all other call flows, the SIP interface is used instead communicating directly with Unified CM. An exception to this rule happens when a Webex linked device is configured in Control Hub for Personal Mode. When this happens, B2B calls are routed through Webex and bypass Unified CM and Expressways. In all other cases any point-to-point call and any multi-point call that does not have a Webex meeting destination is routed through Unified CM and Expressway. For example, a B2B call placed from a Webex-linked device not enabled for Personal Mode is routed through Unified CM and Expressway.

### Webex Hybrid Calling for Webex Users

The Webex App is now able to register to both Webex and Unified CM at the same time. While messaging, whiteboarding, file sharing, and meetings are still managed by Webex, calling is managed with two different behaviors:

- Webex App calling. Calls are entirely managed by the Webex cloud for both signaling and media. Media is always handled by the Webex.

- Webex App calling through Unified CM. SIP signaling is handled by Unified CM, and the Webex App sends the media to the destination without involving the Webex.

When a Webex user is enabled for Unified CM Calling, both calling behaviors are available, and the Webex App automatically selects one of the two or presents both options to the user, depending on admin configuration and dialed destinations.

When a Webex user is not enabled for Unified CM calling, only the first behavior is available, and all calls will always be sent through the Webex.

Registration to Unified CM is direct when the Webex App is on-premises, and through mobile and remote access when the application is connected over the Internet. An important consequence of this is that when the Webex App is registered to Cisco Unified CM, it provides for peer-to-peer media path whenever possible (that is, when a call does not involve mobile and remote access or when ICE is not involved). This is different than when a call is made via Webex, where the media is always hair-pinned in Webex. On the contrary, Webex App integrated with Unified CM enables media to be sent directly between two Webex App instances or between a Webex App and a Unified CM device.

The following illustration shows some of the media paths available with Webex App with Unified CM registration.

Figure 4-2 Media paths for Webex App with Unified CM registration

If a Webex App is on-premises and registered to Cisco Unified CM, the media path to another on-premises Webex App or Unified CM device is peer-to-peer (media paths #1 and #2 in Figure 4-2 ).

If a Webex user is on the Internet, and another Webex user is on-premises, the communication is peer-to-peer through Mobile and remote access (media path #3). If a Webex user calls a Webex user who has not been enabled for Unified CM registration, the media path traverses Webex (media path #4) whether one or both clients are on-premises or not. If both Webex users are enabled for UCM registration and ICE enablement is configured across the infrastructure (Unified CM, Expressway and Webex App), then there is direct media path (media path #5). Under these conditions, if ICE negotiation is successful, the media path will not involve Unified CM or Expressway anymore. Instead, only signaling will flow through Unified CM and Expressway. For more information about ICE media path optimization, you can refer to the Media Optimization with ICE Enablement in Cisco Enterprise Collaboration Preferred Architecture 12.5.

The Webex App registered with Unified CM supports CTI. This allows a Webex App user to:

- Select one of the desk phones associated with that user on Cisco Unified CM

- Start and answer a call on the associated desk phone by using the Webex App

Note CTI is not supported through mobile and remote access. Desk phone control over MRA requires the controlled device to be registered through MRA and the controlling Webex App connected via VPN.

A Webex user must be enabled in Control Hub for Cisco Unified CM calling. This can be done globally or for selected users. If users have already been enabled for Call Service Connect, disable Call Service Connect and Call Service Aware first before enabling Unified CM calling.

The Webex App locates Unified CM by using the following DNS SRV records:

- _cisco-uds._tcp.<domain> in the internal DNS Server

- _collab-edge._tls.<domain> in a public DNS Server

Those records point to Unified CM if the user is on-premises, or to the Expressway-E if the user is on the Internet.

### User Experience

After a Webex user has been enabled for Unified CM calling, and once the user has logged into the Webex App, a secondary pop-up window appears. This window requires the user to enter the username and password for Unified CM. Unless single-sign-on is enabled, a different set of credentials might be used for the Webex App initial login and the Unified CM login.

When a Webex user enabled for Unified CM calling wants to click-to-dial to another user, he might have several options, as it is discussed in the Webex App Call Options Priority sub-section. Webex native calling option is available for everyone, but destinations that involve Unified CM routing (such as the called user’s directory number or mobile phone) are only available for those users who have been enabled for Unified CM calling.

Any call that has numeric destination, including mobile numbers, PSTN destination and Unified CM directory numbers, will be routed through Unified CM.

For example, if a Webex user dials any number instead of clicking a contact, that number is routed to Unified CM, directly or through mobile and remote access. As a result, any public +E.164 number, as well as enterprise significant numbers, are directed towards Unified CM, which will route those numbers internally or towards the PSTN.

It is worth noting that numbers from Unified CM are populated by Directory Connector, and they appear for all users. However, only if the calling user has been enabled for Unified CM calling, will they be able to click on the number, regardless of whether the called user is enabled for Unified CM registration or not. If the called user is not enabled for Unified CM registration then the numeric call will be sent to the called user’s Unified CM registereddevice.

Unlike numeric routing, SIP URIs routing behavior is configurable. A number followed by a domain is a SIP URI, and as such it follows the SIP URI configuration set by the administrator. This is discussed in the next section Webex App SIP URI dialing.

While numeric calls are always routed through Unified CM, SIP URI call routing is administratively configurable on Control Hub for Webex users.

Two options are available for SIP URI call routing:

- All SIP URI calls are routed via Unified CM, with the exception of Webex domains which are directly routed to Webex. This is shown in Figure 4-3 .

Figure 4-3 SIP URI calls are routed through Unified CM, with the exception of Webex services

By selecting this option, all SIP URI calls will be routed through Unified CM. The major benefit is that Unified CM will be able to apply class-of-service for SIP URI calls, and a consistent caller ID. Because numbers are always routed through Unified CM, only Webex services calls (like calls to Webex meetings) are routed through Webex and do not involve Unified CM.

Figure 4-4 shows this scenario when Alice dials to Bob, who belongs to another company and uses a 3rd party device and infrastructure. As the illustration shows, this B2B call will always be hairpinned through Expressway and Unified CM.

As Figure 4-4 shows, by selecting the first option all SIP URIs will be sent to Unified CM. This way, Bob will receive a call from alice@ent-pa.com, consistent with Unified CM dial plan, instead of a call coming from the Webex SIP URI alice@ent-pa.call.webex.com

Figure 4-4 Alice making a B2B call to Bob

- Only calls that match specific domains are routed via Cisco Unified CM. All other SIP URI calls, as well as Webex domains, are routed through Webex. This is shown in Figure 4-5 .

Figure 4-5 Only internal SIP URI calls are routed through Cisco Unified CM

By selecting this option, the administrator configures specific domains which will be routed via Unified CM. If the administrator configures the enterprise domains ent-pa.com and ent2-pa.com, SIP URI internal calls will be routed through Unified CM. External domains such as B2B calls, and Webex calls will be routed through Webex. This option achieves the benefit that business-to-business calls will not consume licenses on Expressway. The downside of it is that Unified CM will not have any control on business-to-business calls, and that the caller ID will match the Webex SIP Address instead of the Directory URI configured in Unified CM. This is shown in Figure 4-6 .

Figure 4-6 Only selected domains are routed through Cisco Unified CM

In this scenario, Alice dials out to Bob, who has a 3rd party devices and infrastructure. The administrator wants only internal domains (ent-pa.com and ent2-pa.com in the example) to be routed through Unified CM. Because Bob’s domain is xyz.com, this call is not sent through Unified CM. Instead, it is routed as a B2B call by Webex. This calling ID that Bob will see is alice@ent-pa.call.webex.com instead of alice@ent-pa.com, because Webex uses the Webex SIP Address and not the directory URI.

### Webex App Call Options Priority

Available call options for the users are:

- Work Number (UCM directory number)

- Enterprise SIP URI

- Mobile Number

- Call on Webex

- Extension

Between these calling options, the administrator can specify both the priority of the option and the hidden options. For example, an administrator could configure in Control Hub Work Number as first option, Enterprise SIP URI as the second option, and to hide the other options. If the administrator chooses Work Number as the first available call option, when users make a call from Webex, the call will always be routed to a person’s work number. If that person doesn’t have a work number, the call is automatically routed to the next available option, such as their SIP URI.

### Webex Hybrid Calling for Webex Devices

Webex Edge for Devices allows Webex devices to be registered with Unified CM, directly or through mobile and remote access. This helps preserve the dialing habit and voice and video services of Unified CM. At the same time the Webex device is cloud-linked and will use Webex advanced features when in a meeting. In contrast to the Webex App, the routing of Webex device traffic when enabled through Webex Edge for Devices uses a different logic. If the destination is not a We bex meeting, the call will always be routed via Unified CM. This might involve Expressway-C and Expressway-E if the Webex device is off-premises or if it is dialing a B2B destination.

If the destination is a Webex meeting, the call will be routed directly from the device to Webex as a native call. This call flow excludes both Unified CM and Expressway. Though similar, Webex App routing logic is more configurable. The following table summarizes the differences.

Numeric routing

Through Unified CM

Through Unified CM

SIP URI routing to non-Webex destinations

Through Unified CM

Through Unified CM

Webex point-to-point destinations

room02@ent-pa.room.webex.com

Through Webex

Through Unified CM

Webex multipoint destinations

Through Webex

Through Webex

Please note that the table above works for Webex-linked devices enabled for shared mode. If the Webex-linked device is enabled for Personal Mode, any B2B call will be routed through Webex. This is the ony exception to the rule described above.

The following picture shows call flows for an on-premises Unified CM registered Webex device and linked to Webex:

Figure 4-7 Call flows for an on-premises Webex-linked device

If a Webex device, on-premises registered to Unified CM and linked to Webex via a secondary registration, dials out to another Unified CM registered device, the signaling goes through Unified CM and media is direct, as paths 1 and 2 indicate.

Path 3 shows the media path to a B2B destination, happening through Expressways.

If a Webex device dials out to a Webex meeting, both signaling and media go directly to Webex as path 4 illustrates. In this case Unified CM, Expressway-C and Expressway-E are not involved.

The following picture shows some call flows for an off-premises Webex device, registered to Unified CM via Expressway-C and Expressway-E.

Figure 4-8 Call flows for an off-premises Webex-linked device

In this scenario a Webex device is off-premises, registered to Unified CM via Expressway (Mobile and Remote Access - MRA). If this endpoint dials to a device registered to Unified CM in the internal network, the signaling goes through Expressways and Unified CM, and media through Expressway, as path 1 shows.

If the Webex device dials out to a B2B external destination, the signaling goes through Expressway and Unified CM, and the media is hair pinned on Expressway-C. This is shown in path 2.

If the Webex device dials to another Webex device off-premises and registered to Unified CM via Mobile and remote access, media path is diret if both endpoints are configured for ICE media path optimization and ICE negotiation is successful, as path 3 shows and hair pinned on Expressway-C if one or both devices are not configured for ICE or ICE negotiation fails, similarly to what happens with media path 2.

If the Webex device dials to a Webex Meeting, both signaling and path are direct to Webex and do not involve Unified CM and Expressway, as shown in path 4.

### Security

Both architecture for users and for devices support security. Signaling is secured by means of TLS, and media is encrypted using sRTP. Because the current architecture relies on Unified CM and Expressway, security methodologies are the same that are discussed in the Preferred Architecture for Cisco Collaboration 14 Enterprise On-Premises Deployment, CVD. Please refer to this document if you need more information:

https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/enterprise/14/collbcvd.html

## Deployment Overview

### Deployment Considerations for Multiple Unified CM Clusters

Webex App and Webex devices supports multiple Unified CM clusters. In this case, Expressway-C can be associated to every cluster, as shown in Figure 4-9 .

Figure 4-9 Expressway-C Supporting Multiple Unified CM Clusters

When multiple clusters are deployed, Webex App and Webex devices register to the correct cluster based on theuser’s home cluster settings. A full explanation is covered in the Preferred Architecture CVD for Cisco Collaboration here:

https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/enterprise/14/collbcvd/control.html

### Deployment Considerations for Multiple Expressway Clusters

When multiple Expressway clusters are deployed it might be desirable that Webex App and Webex devices register through the Expressway clusters closest to their Unified CM home cluster.

To achieve this, Control Hub provides for UC Manager Profiles. The administrator will configure a specific UC Manager Profile for every Expressway cluster. The UC Manager Profile includes the voice services domain that will be used for service discover. Then the UC Manager Profile is added to those Webex users that belong to the same region where that Expressway cluster is configured.

If, for example, there are 3 regions for the company ent-pa.com: US, APAC and EMEA, and for each region different SRV records are configured in public DNS:

- collab-edge._tls.us.ent-pa.com resolving into A records for Expressway-E’s located in the US

- collab-edge._tls.emea.ent-pa.com resolving into A records for Expressway-E’s located in EMEA

- collab-edge._tls.apac.ent-pa.com resolving into A records for Expressway-E’s located in APAC

In Control Hub the administrator will create three UC Manager Profiles:

- US Profile with a voice service domain of us.ent-pa.com

- EMEA Profile with a voice service domain of emea.ent-pa.com

- APAC Profile with a voice service domain of apac.ent-pa.com

Then the administrator will apply one of these 3 profiles to each of the users, based on their location, one by one or in bulk.

The result is that when a user registers to Webex, the corresponding profile is selected, and Webex will retrieve the SRV record to discover the Expressway cluster for that user. In this way the Webex App will always register through the same Expressway-E and Expressway-C cluster.

Webex devices do not support UC Manager profiles, but when they register the user will be instructed to use the discovery domain available in the user’s location. In the example above, if the user is based in the US, he or she will be told to use the service domain us.ent-pa.com when registering with username and password through the Webex device interface.

### High Availability

High Availability is achieved using clustering for both Unified CM and Expressways.

## Deployment Process

### Webex App (Unified CM) Deployment

For a detailed process for deploying calling in Webex App with Unified CM refer to the Deployment Guide for Calling in Webex (Unified CM), available at

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wbxt/ucmcalling/unified-cm-wbx-teams-deployment-guide/unified-cm-wbx-teams-deployment-guide_chapter_010.html

1. Associate a Service Profile to the user. This profile is assigned to Webex App with Unified CM calling users, in order to enable Webex users for CTI

a. Create a Service Profile

b. Create CTI UC Service

c. Associate the CTI UC Service to the Service Profile

d. Associate the Service Profile to the user so the user inherits CTI control capability.

2. Create DNS SRV records for service discovery. A detailed description is found in this document: Service Discovery chapter of the Planning Guide for Cisco Jabber, available here: https://www.cisco.com/c/en/us/support/unified-communications/jabber-windows/products-installation-guides-list.html

a. This involves creating a split DNS environment. For the domain ent-pa.com:

- collab-edge._tls.ent-pa.com in the public DNS

- cisco-uds._tcp.ent-pa.com in the internal DNS

3. In order to enable SAML Single-Sign-On, see the SAML SSO Deployment Guide for Cisco Unified Communications Applications available at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html

For cloud (Control Hub) configuration, see Single Sign-On Integration in Control Hub at: https://help.webex.com/en-us/lfu88u/Single-Sign-On-Integration-in-Control-Hub

4. In order to enable LDAP authentication and synchronization, see the Preferred Architecture for Cisco Collaboration Enterprise On-Premises CVD, Call Control section, Architecture subsection, LDAP paragraphs: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/design/guides/PAdocs.html#pgfId-92068

5. Configure users for Webex on Unified CM:

a. On Unified CM, check that the user’s details include the mail ID. This is an important step as the mail ID is the unique identifier in Webex.

b. On Unified CM, associate a directory URI to the user's directory number.

c. Check the home cluster checkbox for users who are configured on that specific Unified CM cluster

d. Ensure that the Enable User for Unified CM IM and Presence (Configure IM and Presence in the associated UC Service Profile) option is not checked. Webex App messaging is used instead.

e. Apply the previously configured UC Service Profile

f. Enable CTI for the user

g. Create a Webex App softphone device using the Cisco Unified Client Services Framework (CSF), Cisco Dual Mode for Android, Cisco Dual Mode for iPhone, or Cisco Jabber for Tablet device type, depending on the platform in use (PC/Mac, Android, iOS, tablets)

h. Add a Directory Number for the device

i. Associate the device to the user

6. On Unified CM, check that enterprise parameter Cluster Fully Qualified Domain Name is configured. Make sure that the first value in the space separated list is not a wildcard.

7. If encryption is required for on-premises call legs, enable SIP OAuth. A description is found in the Preferred Architecture CVD, Security section, available at https://www.cisco.com/go/pa. For further information on SIP OAuth, see the SIP OAuth Mode chapter in the Feature Configuration Guide for Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

8. Set Calling Behavior in Control Hub: if Hybrid Call Service is enabled for users, disable it. Select Calling in Webex (Unified CM)

9. Setup Expressway-C and Expressway-E for Mobile and remote access following the Mobile and Remote Access through Cisco Expressway Deployment Guide: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html

### Webex Devices Deployment

Pre-requisites

- Webex device registered to Unified CM

- Expressway setup for Mobile and Remote Access (as shown above)

- AXL user configured on Unified CM

- Download the Webex Device Connector from Control Hub and select “I want cloud features for my on-premises registered devices”, then click “Link devices registered with Cisco Unified Communications Manager”

- Enter the Host, Username (Standard AXL APU Access username), and Password for your Unified CM and click Connect. If you have Unified CM with public signed certificates, make sure those are valid or click Proceed without certificate validation

- The Device Connector retrieves the name and description of the Unified CM configured devices. The Contact Info Name becomes the name for the Workspace the device is connected to. If there is no Contact Info Name set, the System Unit Name or MAC address is used

- If you want to change the device name, you can do it from Unified CM

- Click Link All to link all of the listed devices. To link an individual device, click the “Link” button next to it

|  | Webex App | Webex Device |
|---|---|---|
| Numeric routing | Through Unified CM | Through Unified CM |
| SIP URI routing to non-Webex destinations | Through Unified CM | Through Unified CM |
| Webex point-to-point destinations room02@ent-pa.room.webex.com | Through Webex | Through Unified CM |
| Webex multipoint destinations | Through Webex | Through Webex |