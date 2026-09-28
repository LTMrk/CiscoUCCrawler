---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-wbxt-hybridservices-hybridcalldevices-wbxhs-m-deployment--8ef4de6a39
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/wbxt/hybridservices/hybridcalldevices/wbxhs_m_deployment-guide-for-webex-devices-hybrid-call/wbxhs_m_deployment-guide-for-webex-devices-hybrid-call_chapter_00.html
retrieved_at: 2026-08-20T23:57:22.570488+00:00
---

Deployment guide for Hybrid Calling for Webex Devices (Device Connector)

# Deployment guide for Hybrid Calling for Webex Devices (Device Connector)

Updated: October 12, 2023

Chapter: Overview of Hybrid Calling for Webex
                            Devices

## Chapter: Overview of Hybrid Calling for Webex
                            Devices

# Overview of Hybrid Calling for Webex
                        Devices

## Hybrid Calling for Webex
                           Devices

Hybrid Calling for Devices (device connector) is not supported within the Dedicated Instance (DI) for Webex Calling.

There is no requirement for an Expressway-based solution (device connector) because you can use the pre-configured inter-op
                                       SIP trunk between Webex Calling Multi-Tenant and Dedicated Instance. Devices registered to Unified CM in your DI use the trunk
                                       to connect with Webex-registered devices.

You can use Webex Edge for Devices for devices registered in your dedicated instance, or you can register your devices to Webex Calling.

### Hybrid Calling for devices in Workspaces

You can use Hybrid Calling for Webex
                                 Devices to provide hybrid call functionality for Room, Desk, and Cisco Webex Board devices that are added to Workspaces in Control Hub. Webex devices are registered to the cloud, and when they are enabled with Hybrid Calling , they also connect to the enterprise. Webex devices in the Workspace become a part of your existing on-premises dial plan,
                              allowing these devices to call user extensions or the PSTN, and receive incoming
                              calls.

Call directly from the device —Although the devices in a Workspace are
                              registered to the cloud, you can provide them with a line and PSTN service that is
                              served through your Unified CM deployment. People can call these devices to join a
                              meeting; people can also use these devices to dial other extensions or numbers.

Call from Webex App while connected to the device —From Webex App , users can also call phone numbers while connected to a cloud-registered Webex
                              device that is enabled for Hybrid Calling . They can call someone's mobile phone number or the local pizza place directly
                              from Webex App and have the call take place on the Webex device.

Webex Device Connector is a lightweight piece of software that connects your Unified CM configuration
                              with cloud configuration and Webex devices registered to the cloud. You can use the
                              software automate synchronizing Unified CM configuration to device in your Control
                              Hub-managed organization. You get the software from Control Hub and install it on a
                              Windows or Mac device or virtual machine in your network that can access your
                              premises environment and the devices themselves.

### Hybrid Calling for devices associated with users (Personal Mode)

You can also add Hybrid Calling to Room, Desk, and Board devices that are associated with a user in personal
                              mode. These devices don't need to be added to Workspaces. Webex devices in Personal
                              Mode become a part of your existing on-premises dial plan, allowing these devices to
                              call user extensions or the PSTN, and receive incoming calls.

They appear in Control Hub under devices and are associated with users in your
                              organization. They register to the cloud and share the same directory number that is
                              tied to a user's Webex App account if they're already enabled for Unified CM calling ( https://www.cisco.com/go/webex-teams-ucm-calling ).

On a personal mode device enabled for Hybrid Calling, if a user dials a number on
                                          the device, the call goes through the enterprise like a typical PSTN call.
                                          However, a SIP call always goes through the Webex cloud rather than the
                                          enterprise.

## Calling functionality for users

Calling for Webex App users is outside of the scope of this document. The Webex Device Connector-based
                              architecture for Hybrid Calling only supports Webex devices registered to the cloud.
                              If you want to provide calling features to users in your organization, see this deployment guide to set up Webex App users with Unified CM calling; this deployment model uses a Webex App client-based integration into your Unified CM environment.

Hybrid Calling with the Call Connector architecture is end of life (EOL)
                                             and no longer supported.

## Hybrid Calling for Webex Devices architecture

This diagram shows the on-premises and cloud components that comprise the Hybrid Calling for Webex
                                       Devices architecture. This architecture provides call connectivity to Webex cloud-registered devices in a Workspace (created in Control Hub), so that
                                    these devices can use the Unified CM dial plan. You manually synchronize
                                    configuration between premises and cloud by running a sync in the Webex Device Connector software.

## Global Hybrid Calling architecture

If you have a global deployment and use a single SIP destination for Hybrid Calling , traffic from Webex to enterprise goes through a single DNS SRV and can’t be routed to an Expressway cluster based on the location of the caller
                           or called users. This causes media to hairpin through this node even if the caller and called users are on the other side
                           of the world, causing potential latency.

With Multiple SIP Destinations for Hybrid Calling , when a call is made from Webex to the enterprise, Webex directs the call to an Expressway (SIP Destination) that is associated with the the
                           Webex device in a Workspace in Control Hub configuration.

This deployment options provides the benefit of selecting the most appropriate downstream route for each call.

For more information, see Recommendations for global Hybrid Calling deployments .

| Note | Hybrid Calling for Devices (device connector) is not supported within the Dedicated Instance (DI) for Webex Calling. There is no requirement for an Expressway-based solution (device connector) because you can use the pre-configured inter-op
                                       SIP trunk between Webex Calling Multi-Tenant and Dedicated Instance. Devices registered to Unified CM in your DI use the trunk
                                       to connect with Webex-registered devices. You can use Webex Edge for Devices for devices registered in your dedicated instance, or you can register your devices to Webex Calling. |
|---|---|

| Note | On a personal mode device enabled for Hybrid Calling, if a user dials a number on
                                          the device, the call goes through the enterprise like a typical PSTN call.
                                          However, a SIP call always goes through the Webex cloud rather than the
                                          enterprise. |
|---|---|

| Note | Hybrid Calling with the Call Connector architecture is end of life (EOL)
                                             and no longer supported. |
|---|---|