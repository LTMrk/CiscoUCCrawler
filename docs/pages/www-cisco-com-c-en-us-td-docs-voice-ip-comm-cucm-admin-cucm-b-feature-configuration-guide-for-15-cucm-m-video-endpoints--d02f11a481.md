---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-cucm-b-feature-configuration-guide-for-15-cucm-m-video-endpoints--d02f11a481
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/cucm_b_feature-configuration-guide-for-15/cucm_m_video-endpoints-management.html
retrieved_at: 2026-08-16T16:06:20.099941+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: March 26, 2026

Chapter: Video Endpoints Management

## Chapter: Video Endpoints Management

# Video Endpoints Management

## Video Endpoints Management Overview

This feature simplifies the administrator's job of provisioning and managing Cisco TelePresence video endpoints. An administrator
                              can provision settings for Cisco TelePresence endpoints in Unified Communications Manager and then push those Product-Specific
                              Configuration settings to endpoints.

Prior to Release 12.5(1)SU1, only a limited set of Product-Specific Configurations were pushed from Unified Communications
                              Manager to the endpoint resulting in a partial configuration of the endpoint. Administrator had to rely on Cisco TelePresence Management Suite or TelePresence Endpoint's web interface to configure all
                                 the settings. The Phone Configuration window in Unified Communications Manager contains a complete Product-Specific Configuration layout
                              for Cisco TelePresence endpoints that matches what users see on their endpoint. This update lets administrators apply settings
                              on behalf of users and then push those settings to users.

The Bulk Administration Tool (BAT) Phone Template Configuration page also displays the new model-specific configurations in a tabbed layout, supporting the complete list of endpoint parameters.
                                          You can import the entire set of parameters or modify a specific parameter in the endpoint in bulk.

Video endpoints managements feature provides the following benefits:

TelePresence endpoints can be fully provisioned from Unified Communications Manager—Endpoints parameters listed in the Unified
                                    Communications Manager user interface are in the same order as listed in the Advanced Configuration settings of your Cisco TelePresence model. For more information on the various advanced parameters, see the respective model
                                    in the Collaboration Endpoints Administrator Guides.

New Product-Specific Configuration Layout—New layout details the model-specific configurations in a tabbed layout. This is an upgrade from the earlier flat
                                    format that provided access only to a limited set of parameters. The new layout ensures that you have a complete list of Cisco
                                    TelePresence settings on the Cisco Unified CM Administration interface.

Automatic migration of the configuration data from the video endpoints—This simplifies the deployment of endpoints by automatically
                                    synching data from endpoints to Unified Communications Manager and vice versa. Endpoint configurations can be fully restored
                                    in case of reset to factory settings or Product Returns & Replacements (RMA) swaps.

Any endpoint that supports Collaboration Endpoint (CE) Software 9.8 or higher can use this new provisioning layout for the
                                          Product-Specific Configuration fields on the Phone Configuration page. If you are using a CE software version prior to 9.8,
                                          you will be able to view all the new set of advanced parameters; but, the new set of parameters functions only if you upgrade
                                          your CE Software version to 9.8 or higher. The subset of parameters supported is marked with a “#” to the right of each parameter
                                          value in the user interface. You must load a device pack onto Unified Communications Manager if a device type is capable of
                                          supporting the new provisioning framework, but does not show the additional parameters.

## Video Endpoints Management Feature Compatibility

Following table details the video endpoints management feature compatibility with Unified Communications Manager and Collaboration
                              Endpoint (CE) versions:

Unified Communications Manager Version

CE Endpoint Version

Expected Behavior

12.5(1) SU1

9.8 and above

Devices added prior to 12.5(1) SU1:

Advanced Configuration UI (Tabbed Layout) for successfully backed up devices

Limited Configuration UI (Flat Layout) for devices yet to be backed up

New device added through UI/BAT/AXL:

Advanced Configuration UI

12.5(1) SU1

9.7 and below

Devices added prior to 12.5(1) SU1:

Limited Configuration UI

New device added through UI/BAT/AXL:

Advanced Configuration UI with only a limited set of parameters taking into effect

12.5(1) and below

9.8 and above

Limited Configuration UI

## Migration Considerations for Video Endpoints Provisioning

### Auto Backup After Unified Communications Manager Upgrade

When upgrading to Unified Communications Manager 12.5(1)SU1, the existing configuration data for the supported endpoint types
                              is automatically migrated from endpoints to Unified Communications Manager.

Upgrade Unified Communications Manager to version 12.5(1)SU1 or later.

Endpoints register to Unified Communications Manager.

Unified Communications Manager then sends a SIP Notify message to endpoints requesting for the full set of Product-Specific
                                    Configuration parameters.

Endpoints that are upgraded to CE 9.8 and above send full set of configuration data to Unified Communications Manager (in
                                    xConfiguration format) using a SIP REFER message.

Unified Communications Manager processes this configuration data and populates the complete list of Cisco TelePresence settings
                                    (Advanced Configuration UI) on the Cisco Unified CM Administration interface.

Unified Communications Manager server displays the complete endpoint configuration settings in the new layout only if Unified
                                                CM is able to successfully back up data from the endpoint.

### Configuration Control Modes

Navigate to the Product-Specific Configuration Layout section on the Phone Configuration page and choose the Configuration Control Mode under "General Settings" in the Miscellaneous tab to control the various modes. Following are the various Configuration Control Modes:

Unified CM and Endpoint (Default) —Use this mode if you want Unified Communications Manager and endpoint to operate as the multi-prime source for provisioning
                                    endpoint data. If Unified CM and Endpoint is the configured mode, any update made via an endpoint locally is synched with
                                    the Unified CM server.

Unified CM —Use this mode if you want Unified Communications Manager to operate as the centralized primary source for provisioning endpoint
                                    data and does not want to accept any configurations done from the endpoints locally.

Endpoint —Use this mode if you want endpoints to operate as the centralized primary source of configuration data. In this mode, endpoint
                                    ignores any configuration data from Unified Communications Manager and doesn’t sync back the changes done locally. This mode
                                    is typically used when an Audiovisual (AV) integrator is installing the endpoints and wants to control configuration from
                                    the endpoint.

In the Endpoint mode, CE devices continue to accept that limited set of parameters supported prior to release 12.5(1)SU1. Unified Communications
                                          Manager indicates these parameters with a "#" symbol. CE devices will ignore the extended set of parameters supported from
                                          the 12.5(1)SU1 release onwards.

### On-demand Configuration Pull Functionality

Administrators can use the Get Config from Phone option to pull configuration changes from the CE 9.8 endpoint devices on-demand at that given point.

Navigate to the Product-Specific Configuration Layout section on the Phone Configuration page and click the Get Config from Phone button on the top corner of the page to pull any data configuration from the CE 9.8 endpoints on-demand. This option is enabled
                              only if the endpoint is in the registered state.

## Video Endpoints Migration Report

Video Endpoint with Extended Configuration Backup is the new filter is introduced on the Find and List Phones window for release 12.5(1)SU1. Administrators can search for
                           details on how many CE endpoints got migrated automatically and how many CE endpoints did not. Based on this information,
                           they can take corrective measures.

In the Find and List Phones window, the Video Endpoint with Extended Configuration Backup filter is applicable only for video endpoints running Collaboration Endpoint (CE) Software 9.8 or higher.

## Provisioning and Migration Scenarios

The following table describe various provisioning and migration scenarios. All of these scenarios assume that your TelePresence
                              video endpoints are upgraded to a CE release that supports Product-Specific Configuration provisioning from Unified CM. In
                              Unified CM, these settings appear in the Product-Specific Configuration section, but on the endpoint, they appear under Advanced Configuration .

Task

Existing Configuration Summary

What to do

Provisioning New Video Endpoints

Brand new device

Device is not provisioned on Unified CM

No existing settings on the device or on Unified CM

With Unified CM at a minimum release 12.5(1)SU1 and the CE endpoint at 9.8, you can provision new endpoints and manage the
                                          product-specific configurations from Unified CM.

Migrating Existing Video Endpoints from VCS

Existing device

Device is not provisioned on Unified CM

Device is configured, but Unified CM does not have any of the configurations

If you are migrating existing video endpoints from a Cisco TelePresence Video Communications Server to Cisco Unified Communications
                                          Manager:

Adding Phones via Phone Configuration window in Unified CM:

Add the phone to Unified CM, but DO NOT CLICK Save .

Register the phone. After registration, the existing Advanced Configuration settings from the phone are uploaded to Unified CM and display in Product-Specific Configurations in the Phone Configuration window.

In the Phone Configuration window, configure the new settings and click Save . The provisioned settings download to the phone.

For a detailed procedure, see Add Migrating Video Endpoint to Unified CM

Adding Phones via Bulk Administration

Make sure that the csv file or BAT Template that you use for provisioning does not include the Product-Specific Configuration
                                          fields.

Adding Phones via AXL

Make sure that the AXL request does not include any Product-Specific Configuration fields.

Upgrading from an Earlier Release of Unified CM with Registered Video Endpoints

Existing device

Device is provisioned on a pre-12.5 release of Unified CM

Unified CM has a limited set of Product-Specific Configuration settings for the device

So long as the CE endpoint is at a supported version, when you upgrade Unified CM, the Advanced Configuration settings from the endpoint get pulled into Unified CM automatically following device registration and display under the Product-Specific Configuration section of the Phone Configuration window.

After registration, you can set the Configuration Control Mode in addition to whatever settings you want.

### Add Migrating Video Endpoint to Unified CM

If you are migrating existing Cisco TelePresence Video Endpoints from a Cisco TelePresence Video Communications Server to
                                 Unified Communications Manager, use this procedure to add the CE endpoint into Unified CM via the Phone Configuration window so that the existing Advanced Configurations from the endpoint can be managed from the Phone Configuration window in Unified CM.

#### Before you begin

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Add New from Template and enter the following phone details:

- Select the model from the Phone Type drop-down list.

- Enter the MAC Address of the endpoint

- From the Device Template , select a Universal Device Template.

- Select the Directory Number that you want to add to the phone. If none exists, click New and configure a directory number.

- From the User drop-down list, select the user whom will own the device.

Step 3

Click Add . The Phone Configuration displays with the universal device template settings filling out the phone configuration. The Product-Specific Configuration section also appears, but with default settings, rather than the existing settings from the phone.

Step 4

DO NOT CLICK Save . If you save settings, Unified CM does not load existing settings from the phone. If you saved by mistake, go straight to
                                          the troubleshooting Note at the bottom of this procedure for recovery steps.

Step 5

Register the phone.

Step 6

In the Phone Configuration window, configure how you want endpoint settings to be managed by configuring the Configuration Control Mode field:

- Unified CM and Endpoint (Default) —Use this mode if you want Unified Communications Manager and endpoint to operate as the multi-prime source for provisioning
                                             endpoint data. If Unified CM and Endpoint is the configured mode, any update made via an endpoint locally is synched with
                                             the Unified CM , and any change made on Unified CM syncs to the endpoint.

- Unified CM —Use this mode if you want Unified Communications Manager to operate as the centralized primary source for provisioning endpoint
                                             data and does not want to accept any configurations done from the endpoints locally.

- Endpoint —Use this mode if you want endpoints to operate as the centralized primary source of configuration data. In this mode, the
                                             endpoint maintains existing settings, ignores any configuration data from Unified Communications Manager, and doesn’t sync
                                             back the changes done locally. This mode is typically used when an Audiovisual (AV) integrator is installing the endpoints
                                             and wants to control configuration from the endpoint.

Step 7

Configure any phone settings that you want. For more information on the fields and their configuration options, see Online Help.

Step 8

Click Save .

If you clicked Save mistakenly in the Phone Configuration window prior to device registration, the existing Advanced Configuration settings from the endpoint will not load to Unified CM when the device registers. To recover, do the following prior to device
                                             registration:

In Unified CM, set the Configuration Control Mode to Endpoint and click Save .

Let the phone register to Unified CM.

After registration, return to the device configuration in the Phone Configuration window and click the Get Config from Device button.  The setting results in the existing Advanced Configurations on the phone getting pulled into Unified CM. Note that this button does not appear until after device registration.

Return to Step 6 of the procedure in order to complete the configuration.

| Note | The Bulk Administration Tool (BAT) Phone Template Configuration page also displays the new model-specific configurations in a tabbed layout, supporting the complete list of endpoint parameters.
                                          You can import the entire set of parameters or modify a specific parameter in the endpoint in bulk. |
|---|---|

| Note | Any endpoint that supports Collaboration Endpoint (CE) Software 9.8 or higher can use this new provisioning layout for the
                                          Product-Specific Configuration fields on the Phone Configuration page. If you are using a CE software version prior to 9.8,
                                          you will be able to view all the new set of advanced parameters; but, the new set of parameters functions only if you upgrade
                                          your CE Software version to 9.8 or higher. The subset of parameters supported is marked with a “#” to the right of each parameter
                                          value in the user interface. You must load a device pack onto Unified Communications Manager if a device type is capable of
                                          supporting the new provisioning framework, but does not show the additional parameters. |
|---|---|

| Unified Communications Manager Version | CE Endpoint Version | Expected Behavior |
|---|---|---|
| 12.5(1) SU1 | 9.8 and above | Devices added prior to 12.5(1) SU1: Advanced Configuration UI (Tabbed Layout) for successfully backed up devices Limited Configuration UI (Flat Layout) for devices yet to be backed up New device added through UI/BAT/AXL: Advanced Configuration UI Note It's highly recommended that you run CE 9.8 or higher. | Note | It's highly recommended that you run CE 9.8 or higher. |
| Note | It's highly recommended that you run CE 9.8 or higher. |
| 12.5(1) SU1 | 9.7 and below | Devices added prior to 12.5(1) SU1: Limited Configuration UI New device added through UI/BAT/AXL: Advanced Configuration UI with only a limited set of parameters taking into effect Note For migrations with CE 9.7 or earlier, you cannot maintain the existing endpoint configuration during migration. When the
                                                   migrated device registers, Unified CM overwrites the existing configuration with default settings. | Note | For migrations with CE 9.7 or earlier, you cannot maintain the existing endpoint configuration during migration. When the
                                                   migrated device registers, Unified CM overwrites the existing configuration with default settings. |
| Note | For migrations with CE 9.7 or earlier, you cannot maintain the existing endpoint configuration during migration. When the
                                                   migrated device registers, Unified CM overwrites the existing configuration with default settings. |
| 12.5(1) and below | 9.8 and above | Limited Configuration UI |

| Note | It's highly recommended that you run CE 9.8 or higher. |
|---|---|

| Note | For migrations with CE 9.7 or earlier, you cannot maintain the existing endpoint configuration during migration. When the
                                                   migrated device registers, Unified CM overwrites the existing configuration with default settings. |
|---|---|

| Note | Unified Communications Manager server displays the complete endpoint configuration settings in the new layout only if Unified
                                                CM is able to successfully back up data from the endpoint. |
|---|---|

| Note | In the Endpoint mode, CE devices continue to accept that limited set of parameters supported prior to release 12.5(1)SU1. Unified Communications
                                          Manager indicates these parameters with a "#" symbol. CE devices will ignore the extended set of parameters supported from
                                          the 12.5(1)SU1 release onwards. |
|---|---|

| Note | In the Find and List Phones window, the Video Endpoint with Extended Configuration Backup filter is applicable only for video endpoints running Collaboration Endpoint (CE) Software 9.8 or higher. |
|---|---|

| Task | Existing Configuration Summary | What to do |
|---|---|---|
| Provisioning New Video Endpoints | Brand new device Device is not provisioned on Unified CM No existing settings on the device or on Unified CM | With Unified CM at a minimum release 12.5(1)SU1 and the CE endpoint at 9.8, you can provision new endpoints and manage the
                                          product-specific configurations from Unified CM. |
| Migrating Existing Video Endpoints from VCS | Existing device Device is not provisioned on Unified CM Device is configured, but Unified CM does not have any of the configurations | If you are migrating existing video endpoints from a Cisco TelePresence Video Communications Server to Cisco Unified Communications
                                          Manager: Adding Phones via Phone Configuration window in Unified CM: Add the phone to Unified CM, but DO NOT CLICK Save . Register the phone. After registration, the existing Advanced Configuration settings from the phone are uploaded to Unified CM and display in Product-Specific Configurations in the Phone Configuration window. In the Phone Configuration window, configure the new settings and click Save . The provisioned settings download to the phone. For a detailed procedure, see Add Migrating Video Endpoint to Unified CM Adding Phones via Bulk Administration Make sure that the csv file or BAT Template that you use for provisioning does not include the Product-Specific Configuration
                                          fields. Adding Phones via AXL Make sure that the AXL request does not include any Product-Specific Configuration fields. |
| Upgrading from an Earlier Release of Unified CM with Registered Video Endpoints | Existing device Device is provisioned on a pre-12.5 release of Unified CM Unified CM has a limited set of Product-Specific Configuration settings for the device | So long as the CE endpoint is at a supported version, when you upgrade Unified CM, the Advanced Configuration settings from the endpoint get pulled into Unified CM automatically following device registration and display under the Product-Specific Configuration section of the Phone Configuration window. After registration, you can set the Configuration Control Mode in addition to whatever settings you want. |

| Note | Make sure to follow this procedure closely. The settings from the endpoint do not automatically upload to Unified CM until
                                          after device registration. |
|---|---|

| Note | This procedure uses the Add New from Template setting in the Unified CM Phone Configuration window. You can also use tools like Bulk Administration or AXL to add the endpoint. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Add New from Template and enter the following phone details: Select the model from the Phone Type drop-down list. Enter the MAC Address of the endpoint From the Device Template , select a Universal Device Template. Select the Directory Number that you want to add to the phone. If none exists, click New and configure a directory number. From the User drop-down list, select the user whom will own the device. |
| Step 3 | Click Add . The Phone Configuration displays with the universal device template settings filling out the phone configuration. The Product-Specific Configuration section also appears, but with default settings, rather than the existing settings from the phone. Note You can also add the device using the Phone Configuration window's Add New , but this method requires that you enter settings manually. | Note | You can also add the device using the Phone Configuration window's Add New , but this method requires that you enter settings manually. |
| Note | You can also add the device using the Phone Configuration window's Add New , but this method requires that you enter settings manually. |
| Step 4 | DO NOT CLICK Save . If you save settings, Unified CM does not load existing settings from the phone. If you saved by mistake, go straight to
                                          the troubleshooting Note at the bottom of this procedure for recovery steps. |
| Step 5 | Register the phone. During registration, the existing Advanced Configuration settings from the phone get pulled into Unified CM and display in the Phone Configuration window's Product-Specific Configuration section. |
| Step 6 | In the Phone Configuration window, configure how you want endpoint settings to be managed by configuring the Configuration Control Mode field: Unified CM and Endpoint (Default) —Use this mode if you want Unified Communications Manager and endpoint to operate as the multi-prime source for provisioning
                                             endpoint data. If Unified CM and Endpoint is the configured mode, any update made via an endpoint locally is synched with
                                             the Unified CM , and any change made on Unified CM syncs to the endpoint. Unified CM —Use this mode if you want Unified Communications Manager to operate as the centralized primary source for provisioning endpoint
                                             data and does not want to accept any configurations done from the endpoints locally. Endpoint —Use this mode if you want endpoints to operate as the centralized primary source of configuration data. In this mode, the
                                             endpoint maintains existing settings, ignores any configuration data from Unified Communications Manager, and doesn’t sync
                                             back the changes done locally. This mode is typically used when an Audiovisual (AV) integrator is installing the endpoints
                                             and wants to control configuration from the endpoint. Note If you want to maintain existing settings on the endpoint, it's recommended to choose Endpoint mode, at least until after the endpoint has completed the registration process in full. You can switch the configuration
                                                      to one of the other modes after you complete this procedure. | Note | If you want to maintain existing settings on the endpoint, it's recommended to choose Endpoint mode, at least until after the endpoint has completed the registration process in full. You can switch the configuration
                                                      to one of the other modes after you complete this procedure. |
| Note | If you want to maintain existing settings on the endpoint, it's recommended to choose Endpoint mode, at least until after the endpoint has completed the registration process in full. You can switch the configuration
                                                      to one of the other modes after you complete this procedure. |
| Step 7 | Configure any phone settings that you want. For more information on the fields and their configuration options, see Online Help. |
| Step 8 | Click Save . The provisioned settings in Unified Communications Manager download to the endpoint. |

| Note | You can also add the device using the Phone Configuration window's Add New , but this method requires that you enter settings manually. |
|---|---|

| Note | If you want to maintain existing settings on the endpoint, it's recommended to choose Endpoint mode, at least until after the endpoint has completed the registration process in full. You can switch the configuration
                                                      to one of the other modes after you complete this procedure. |
|---|---|

| Note | If you clicked Save mistakenly in the Phone Configuration window prior to device registration, the existing Advanced Configuration settings from the endpoint will not load to Unified CM when the device registers. To recover, do the following prior to device
                                             registration: In Unified CM, set the Configuration Control Mode to Endpoint and click Save . Let the phone register to Unified CM. After registration, return to the device configuration in the Phone Configuration window and click the Get Config from Device button.  The setting results in the existing Advanced Configurations on the phone getting pulled into Unified CM. Note that this button does not appear until after device registration. Return to Step 6 of the procedure in order to complete the configuration. |
|---|---|