---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-release-guide-uccx-b-uccx-solut-b723f9f35b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/release/guide/uccx_b_uccx-solution-release-notes-125/uccx_b_uccx-solution-release-notes-125_chapter_0111.html
retrieved_at: 2026-08-16T21:01:57.664871+00:00
---

Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1)

# Release Notes for Cisco Unified Contact Center Express Solution, Release 12.5(1)

Updated: January 31, 2020

Chapter: Cisco Finesse

## Chapter: Cisco Finesse

# Cisco Finesse

## New Features

### Improvements to Finesse Failover

This release optimizes the Desktop failover and Unified CCX Engine failover performances.

Desktop Failover—The maximum time taken for the desktop failover with the default desktop layout, varies from 35 seconds to
                                       75 seconds over LAN for 400 agents, once an active Finesse server is found.

Unified CCX Engine Failover—If Unified CCX Engine failover is involved, then the time taken is longer as it includes the time
                                       taken for the Cisco Finesse Server failover.

The failover time varies depending on the WAN bandwidth, the number of signed-in users, network latency, and the number of
                                 gadgets configured on the Finesse desktop.

For more information on deployment practices and guidelines to ensure optimal failover performance, see Guidelines for Optimal Desktop Failover and Failover Planning sections in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

For more information on ensuring how the custom gadgets improve failover performance, see Best Practices for Gadget Development section in Cisco Finesse Web Services Developer Guide at https://developer.cisco.com/docs/finesse/#!rest-api-dev-guide .

#### Desktop Performance Improvements

This release optimizes the Finesse desktop performance in the following areas:

Uses HTTP/2 by default for loading resources. This provides significant improvement when starting up the desktop compared
                                       to the older HTTP 1.1.

Consumes significantly lesser desktop bandwidth when reloading the Finesse desktop (without gadgets) from the cache.

Uses fewer requests for loading resources.

Serves static resources much faster using client-side resource caching.

Provides cached REST responses at a team-level for configuration data to improve the desktop loading.

Improves gadget loading by caching the gadget definitions.

#### Finesse Server Performance Improvements

This release optimizes the Finesse server performance in the following areas.

Significantly reduces the average CPU consumption while the server is under load.

Optimizes the server performance by avoiding dynamic server pages, using SSL termination, faster CTI message parsing, and
                                       cached static resources.

Provides access to more memory and reduces GC latencies as the Cisco Finesse server uses 64-bit Java 8.

Optimizes CTI request processing to reduce the latencies in sending requests to the server.

Reduces overall latencies for CTI communication.

### Keyboard Shortcuts

This release provides keyboard shortcuts for easy access to the Finesse desktop features. The keyboard shortcuts define an
                              alternate way to perform a specific action on the Finesse agent and supervisor desktop. The administrator can set the utils finesse set_property desktop enableShortCutKeys to true to enable this feature.

For more information, see Access Keyboard Shortcuts section in Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html .

### Edit Call Variables

This release allows agents and supervisors to edit the call variable values from the Finesse desktop. The administrator can
                              configure any of the callVariable values, including ECC variables as editable. The agent and the supervisor can edit the call
                              variable values during an active call or in the wrap-up state.

Call variables edit operation updates the values of the variables within the particular call. All entities listening to dialog
                                          events receive the updated call variables through the Cisco Finesse notifications. If any CTI clients are connected to the
                                          same CTI server , they also receive notifications of the changed call data though CTI call events. However, application scripts or databases
                                          that are used to populate the call variables are not directly affected by this edit.

For more information, see Edit Call Variables section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html and Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html .

### Drag-and-Drop and Resize Gadget or Component

This release allows agents and supervisors to drag-and-drop or resize the gadgets or components in the Finesse desktop. The
                                 administrator can customize the desktop property value of these features through the desktop layout:

Default layout ( Desktop Layout )

Team-specific layouts ( Manage Team Resources > Desktop Layout )

Alternatively, the administrator can also set the utils finesse set_property desktop enableDragDropAndResizeGadget to true to enable these features.

For more information, see Drag-and-Drop and Resize Gadget or Component section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### Gadget Expand and Collapse

This release supports to expand and collapse of gadgets dynamically in the Finesse desktop to optimize available screen space.

For more information, see Container Services section in JavaScript Library at https://developer.cisco.com/docs/finesse/#!javascript-library .

### Desktop Layout Editors

This release provides two types of editors in the Desktop Layout and Team Resources of the Cisco Finesse administration console.

Text Editor —A plain text editor. It is the default editor. Use the Expand All option to see all the code details and Search box to refine results.

XML Editor —An XML editor. The administrator cannot add or edit comments (<!-- -->) in this editor.

For more information, see Default Layout XML section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### Customize Desktop Properties

This release allows the administrator to customize the desktop properties for individual Teams through the desktop layout
                                 using the following layouts:

Default layout ( Desktop Layout )

Team-specific layouts ( Manage Team Resources > Desktop Layout )

For more information, see Customize Desktop Properties and Customize Desktop Properties at Team Level sections in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### Configuration for Cloud Connect

This release allows the administrator to configure the Cloud Connect server settings in the Finesse administration console
                                 to contact the Cisco Cloud Services, such as Cisco Webex Experience Management .

For more information, see Cloud Connect Server Settings section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### Security Banner Message

This release provides custom banner messages in the administrator and desktop Sign In pages. The administrator can use the
                              following CLIs to define the custom security banner message.

utils finesse set_property desktop desktopSecurityBannerMessage < value >

utils finesse set_property admin adminSecurityBannerMessage < value >

For more information, see Desktop Properties and Service Properties sections in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### Automatic Desktop Login Retries

This release supports automatic desktop login retries when the desktop login fails due to device-related errors. The administrator
                                 can use the following CLIs to enable, define the number of attempts and intervals in seconds for the retry login mechanism.
                                 By default, the value of this property is set to true.

utils finesse set_property desktop enableRetryLoginFeature { true|false }

utils finesse set_property desktop loginFailureRetryAttempts < value >

utils finesse set_property desktop loginFailureRetryInterval < value >

For more information, see Desktop Properties section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### Finesse IP Phone Agent Certificate Management

This release requires HTTPS for Finesse IP Phone Agent (IPPA) to address the security vulnerabilities across the solutions.
                              The administrator must ensure to import the following certificates and configuration changes to use the FIPPA functionality.

Import the Cisco Unified Communications Manager (CUCM) certificate to the trust store as tomcat-trust .

Import the Unified CCX host certificate to the CUCM trust store as Phone-trust .

For more information, see Finesse IP Phone Agent Certificate Management section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### Supported Content Security Policy Directives

This release allows the administrator to use the following CLI commands to view, add, or delete the frame-access sources in
                                 the response header of Cisco Finesse. This ensures that only the configured sources can embed the Cisco Finesse in an iFrame
                                 within their HTML pages.

utils finesse frame_access_whitelist add [source1,source2]

utils finesse frame_access_whitelist delete

utils finesse frame_access_whitelist list

For more information, see Supported Content Security Policy Directives in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

This feature is available from Unified CCX Release 12.5(1) ES02.

### Enhanced Log Collection

#### 3rdpartygadget Log Directory

This release provides the 3rdpartygadget log directory, which contains information, error, startup, and shutdown-related logs
                                 for the Finesse 3rdpartygadget server.

#### WebProxy Service Logs

The administrator can use the file get activelog webproxy recurs compress CLI to obtain logs for the WebProxy Service.

For more information, see Log Collection section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

#### Automatic Log Collection for Desktop Users

The administrator can use the following CLI to create, list, and delete automatic desktop log collection schedules for agents
                                 and supervisors.

utils finesse desktop_auto_log_collection { create | list | delete }

For more information, see Log Collection Schedule section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### Set Commands

The following CLIs have been introduced in this release:

#### Call Variables Logging

The administrator can use the following CLIs to enable or disable the call variables logging.

utils finesse set_property webservices logCallVariables { true|false }

utils finesse set_property fippa logCallVariables { true|false }

#### Enforcement of X.509 Certificate Trust Validation

The administrator can set the utils finesse set_property webservices trustAllCertificates to false to enable the validation of the X.509 CA or the self-signed certificate.

#### Preloading of the Secondary Resources

The administrator can set the utils finesse set_property desktop preLoadSecondaryResources to true to enable the preloading of static resources from the secondary server to ensure faster failover.

#### XMPP Socket and BOSH/WebSocket (HTTP)

The administrator can set the utils finesse set_property webservices enableInsecureOpenfirePort to true to enable the Cisco Finesse Notification Service unsecure XMPP port (5222) and HTTP-BOSH/WebSocket port (7071).

#### WebProxy Service

The administrator can use the following CLIs to clear, set access log-level and log-severity for the logs that are generated
                                 by the WebProxy Service.

utils webproxy cache clear

set webproxy access-log-level

set webproxy log-severity

show webproxy access-log-level

show webproxy log-severity

For more information, see Cisco Finesse CLI section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### REST APIs

The following APIs have been introduced in this release:

CompressedClientLog—Post Compressed Log to Finesse

TeamResource—Get Reason Codes

TeamResource—Get Wrap-Up Reasons

TeamResource—Get Media Properties Layouts

TeamResource—Get Phone Books

TeamResource—Get Workflows

#### REST API Response Caching

In order to improve login performance, the Finesse webproxy caches the following REST API responses:

ChatConfig

TeamResource APIs include Reason Codes, Wrap-Up Reasons, Media Properties Layouts, Phone Books, and Workflows. The responses
                                       of the TeamResource API are cached at the team-level.

For more information, see REST API Developer Guide at https://developer.cisco.com/docs/finesse/#!rest-api-dev-guide .

### JavaScript APIs

The following APIs have been introduced in this release:

finesse.shortcutkey.ShortcutKeyService

finesse.utilities.DesktopCache

For more information, see JavaScript Library at https://developer.cisco.com/docs/finesse/#!javascript-library .

## Updated Features

### Security Enhancements

This release implements the following security changes:

By default, Cisco Finesse Notification Service unsecure XMPP port 5222 and BOSH/WebSocket (HTTP) port 7071 are disabled.

For more information on enabling the ports, see Service Properties section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

For more information, see Security Enhancements section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

### Failure Message for Login

This release displays detailed error messages corresponding to login failures on the Finesse desktop. This allows the administrator
                                 to respond to client login failures without referring to the logs.

The error messages are updated for both UI and API.

The Finesse desktop UI is updated to include the 2nd Level Text error messages provided by CTI operations for sign-in scenarios.

Peripheral error codes 12004 and 12005 are replaced with desktop sign-in retries. When the sign-in retry fails, it displays
                                       the 2nd Level Text error messages provided by CTI operations.

The Cisco Finesse API payloads are updated to include the peripheral error codes and 2nd Level Text error messages provided
                                       by CTI operations. The newly added parameters are:

peripheralErrorCode

peripheralErrorMsg

peripheralErrorText

For more information, see Cisco Finesse API Errors section in REST API Developer Guide at https://developer.cisco.com/docs/finesse/#!rest-api-dev-guide .

Example

13036 PERERR_GW_E_JTAPIOBJ_PERFORMANSWERCALL_NO_TERMINAL_CONNECTION

```
1st Level Text = 'JTAPI Gateway - Error on ANSWER operation'
2nd Level Text = 'The routine performAnswerCall in class JTapiObj got a null connection from a call to 'findTerminalConnection'
```

### Team Performance Gadget

In the Team Performance gadget, supervisors can use the Search box to refine any agent details by using the search criteria such as Agent Name, State, or Extension.

### Phone Book Contact Limit

The maximum number of contacts per agent across all phone books is increased from 1500 to 6000.

### Changes in REST APIs

The following payloads are updated:

MediaPropertiesLayout APIs—The uiEditable payload indicates if the call variable values can be edited in the Finesse desktop (agent and supervisor).

#### Phone Book Contact Limit

The maximum number of contacts per agent is increased from 1500 to 6000 in the Phone Book and Contact APIs.

For more information, see REST API Developer Guide at https://developer.cisco.com/docs/finesse/#!rest-api-dev-guide .

### Changes in JavaScript APIs

The following functions are updated:

ContainerServices—The collapseMyGadget and expandMyGadget functions, that hide and display the gadget contents respectively.

DialogBase—The updateCallVariables function updates the dialog's call variables.

For more information, see JavaScript Library at https://developer.cisco.com/docs/finesse/#!javascript-library .

## Important Notes

Finesse desktop now connects to the Notification service using WebSocket or BOSH with HTTPS port 8445 instead of 7443. The
                                    advantage is that it reduces the number of certificates that needs to be accepted by the desktop during log in.

Third-party client software can connect to the Notification service using WebSocket or BOSH with either 7443 or 8445 HTTPS
                                    port.

## Deprecated Features

### Notifications over BOSH (Long Polling)

In this release, support for notifications over BOSH (long polling) is deprecated. Notifications over direct XMPP (over TCP)
                              and Websocket-based transports are the replacements.

## Removed and Unsupported Features

### Cisco Finesse Trace Logging

In this release, the following CLIs are removed:

utils finesse trace enable

utils finesse trace disable

The replacement is the utils finesse log commands that are used to add, delete, update, or view a custom log configuration in the Cisco Finesse system.

## Third Party Software Impacts

None.

| Note | Call variables edit operation updates the values of the variables within the particular call. All entities listening to dialog
                                          events receive the updated call variables through the Cisco Finesse notifications. If any CTI clients are connected to the
                                          same CTI server , they also receive notifications of the changed call data though CTI call events. However, application scripts or databases
                                          that are used to populate the call variables are not directly affected by this edit. |
|---|---|

| Note | This feature is available from Unified CCX Release 12.5(1) ES02. |
|---|---|