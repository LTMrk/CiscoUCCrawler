---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-release-gui-4a0d6c2ce2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/release/guide/rcct_b_cce-solutions-rns-12-6-2/cfin_m_1262_finesse-release-notes.html
retrieved_at: 2026-08-16T19:37:32.971644+00:00
---

Release Notes for Cisco Contact Center Enterprise Solutions, Release 12.6(2)

# Release Notes for Cisco Contact Center Enterprise Solutions, Release 12.6(2)

Updated: February 27, 2026

Chapter: Cisco Finesse

## Chapter: Cisco Finesse

# Cisco Finesse

## New Features

### Manage Digital Channels gadget

This gadget allows agents and supervisors to interact with customers through digital channels. This gadget is available only
                                 with SSO login. This gadget is available to agents and supervisors only when an administrator configures and assigns at least
                                 one digital channel to them. The following digital channels are available:

Chat/Social Channels— Represents the Chat and SMS media.

Email— Represents the email digital channel.

For information on how to configure this gadget, see the Manage Digital Channels gadget section in the Cisco Finesse Administration Guide .

For information on how to use this gadget, see the Cisco Contact Center Enterprise Manage Digital Channels Gadget User Guide .

### Customizable gadget behavior

As an administrator, you can now modify the desktop layout entry of a gadget to customize and override the gadget properties.
                                 You can modify the gadget properties for a specific team.

For an example on customizing and overriding the gadget properties, see the Manage Digital Channels gadget properties section in the Cisco Finesse Administration Guide .

### Refresh of drag-and-drop and resize gadgets feature

The desktop drag-and-drop and resize behaviors are refreshed to provide new capabilities. The new capabilities that are now
                                 available on the desktop are as follows:

The restrictions on moving and resizing of page level gadgets are removed.

Each desktop tab can be customized to have a unique layout without affecting other tabs.

Each desktop tab can be reset to its original layout without affecting the customizations of other tabs.

If the browser size is reduced, based on the width of the browser, the gadgets in the desktop layout are automatically organized
                                       one below the other.

When the desktop drag-and-drop feature is enabled, Maximize and Collapse features are available in the Multi-Tab gadget.

Call Control gadget automatically minimizes and restores when the gadgets under Call Control gadget are maximized and restored
                                       respectively.

For instructions, see the Drag-and-Drop and Resize Gadget or Component section in the Cisco Finesse Agent and Supervisor Desktop User Guide .

### JMX Counters for Finesse APIs

You can now access the detailed application API performance-related counters through REST APIs. For more information, see
                                 the Finesse Performance API section in the Cisco FinesseWeb Services Developer and JavaScript Guide on DevNet .

### Finesse REST APIs

The following are the new Finesse REST APIs:

/finesse/api/DigitalChannels/Configuration —This API enables you to get the digital channel configuration.

/finesse/api/ScriptSelectors —This API enables you to get the script-selectors for specific channels (Voice and Non-Voice) or for both the channels.

finesse/api/performance —This API enables you to get the complete list of JMX counters exposed in Cisco Finesse Tomcat service.

https://<FQDN>/finesse/api/User/<id>/Media —A new method PUT is introduced, which enables you to update a list of Media objects for all nonvoice Media Routing Domains (MRDs) configured
                                       on Unified CCE.

https://<FQDN>/desktop/api/ResourceURLs?type=desktop —Returns in string format the list of all the valid desktop web application file paths that are available on the server.

https://<FQDN>/desktop/api/ResourceURLs?type=3rdParty —Returns in string format the list of all the valid third-party gadget web application file paths that are available on the
                                       server.

For more information on the Finesse REST APIs, see the Cisco FinesseWeb Services Developer and JavaScript Guide on DevNet .

#### JavaScript APIs

The following is the new JavaScript API that is introduced corresponding to the newly introduced Finesse API:

finesse.containerservices.NotificationPopoverService —This API enables you to create notifications for login failures and show them on the Finesse desktop. You can also capture
                                          notifications from any of the gadgets and display them on the navigation bar of the Finesse desktop.

For details about this API, see the Container Services section in the Cisco Finesse Web Services Developer and JavaScript Guide on DevNet .

### New Desktop Capabilities

Finesse introduces the following new desktop capabilities for notifications:

Notification icon on the navigation pane

Desktop popups for alerting users

The notifications are used to inform the agents about the login failures and incoming messages from various media channels.
                                 You can add specific icons, that are supported by Finesse, to the notifications. If you don’t add an icon, a default icon
                                 is displayed.

A new JavaScript API NotificationPopoverService is introduced to publish the notifications. For more information, see the Cisco Finesse Web Services Developer and JavaScript Guide on DevNet .

### Structured Logs

Finesse and Openfire logs are now in JSON format so that the logs can be used more easily with the analytical tools.

## Updated Features

### VPN-Less Finesse reverse-proxy support

The VPN-less Finesse deployments are made much easier with the support of a new installer that has the following features:

Installer autodeploys Nginx and separates the configurations from the rules.

Support for reverse-proxy access through load balancer.

Support for reverse-proxy access through clients behind a proxy.

Support for deployments that are larger than 2000 agents.

For more information, see the Reverse Proxy Automated Installer chapter in the Cisco Unified Contact Center Enterprise Features Guide .

### Finesse REST APIs

The following are the updated Finesse REST APIs:

showMyGadgetNotification—This container services API is updated to accept a new parameter messageDetails .

finesse/api/User/<id>/Media—GET method is updated to return only the non-voice MRDs associated with the user. Previously,
                                       it was incorrectly returning all of the non-voice MRDs configured in the system.

You can retrieve the complete list of MRDs configured in the system using the existing API – finesse/api/MediaDomain .

For more information, see the Container Services section in the Cisco Finesse Web Services Developer and JavaScript Guide on DevNet .

#### JavaScript APIs

The channelState object in the Digital Channel is modified to show login warnings on the respective digital channels. For more information,
                                    see the Digital Channel section in the Cisco Finesse Web Services Developer and JavaScript Guide on DevNet .

### Support for IdS Asymmetric key-based tokens

Cisco IdS 12.6(2) uses asymmetric keys for token encryption, which can be authenticated independently by clients without requesting
                                 the token validity to Cisco IdS. Cisco Finesse 12.6(2) adds support for asymmetric key tokens and switches the authentication
                                 mechanisms appropriately, based on the configured IdS. For more information, see the Single Sign-On chapter in the following documents:

Cisco Unified Contact Center Enterprise Features Guide

Cisco Packaged Contact Center Enterprise Features Guide

Cisco Finesse Web Services Developer and JavaScript Guide on DevNet

### Command Line Interface

The following are the new parameters for the utils finesse set_property webservices command-line interface (CLI):

mrdScriptSelectorPollingInterval —Time interval in seconds to poll the updates for script-selectors from Unified CCE.

drapiStatusPollingInterval —Time interval in seconds to check the DR-API status.

drapiRequestRetryInterval —Time interval in seconds to retry the DR-API request.

drapiMaxTimeToWaitBeforeRequestDiscard —Time in seconds to discard the DR-API request if there’s a failure.

drapiRequestRetryIntervalForChat —Time interval in seconds to retry the DR-API request for Chat conversations.

drapiMaxTimeToWaitBeforeRequestDiscardForChat —Time in seconds to discard the DR-API request if there’s a failure for Chat conversations.

For more information about these CLI parameters, see the Cisco Finesse CLI chapter in the Cisco Finesse Administration Guide .

## Important Notes

After the fresh install, by default the utils system reverse-proxy client-auth is enabled. If this is enabled and there are multiple certificates in the client system, when agents login to Finesse through
                                    LAN, it forces the agents to select one of the certificates to communicate with the Finesse server. If the deployments aren’t
                                    configured for VPN-less access to Finesse, disable it by running the utils system reverse-proxy client-auth disable command on both the Finesse nodes.

SSO connectivity requires Cisco IDS to be on version 12.6(2).

SSO Deployments upgrading to 12.6(2) should ensure that Reverse Proxy Installer (for VPN-Less deployments) 12.6(2) ES02 or
                                    later, followed by IdS 12.6(2) ES02 or later, is installed before upgrading any of the components like Cisco Finesse/CUIC
                                    to 12.6.(2)

For 2K Co-Res Deployment model, CUIC, LD and CCE (Router, logger and AW) should be upgraded to in the same maintenance window.

## Deprecated Features

None.

## Removed and Unsupported Features

None.

## Third Party Software Impacts

For the list of third-party softwares, see Open Source Documents . Filter by Product/Release Name and Version to download the required Open Source document.

| Note | You can retrieve the complete list of MRDs configured in the system using the existing API – finesse/api/MediaDomain . |
|---|---|