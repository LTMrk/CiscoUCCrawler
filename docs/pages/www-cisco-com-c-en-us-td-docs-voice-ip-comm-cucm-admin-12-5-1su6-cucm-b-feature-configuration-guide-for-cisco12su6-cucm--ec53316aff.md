---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su6-cucm-b-feature-configuration-guide-for-cisco12su6-cucm--ec53316aff
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU6/cucm_b_feature-configuration-guide-for-cisco12su6/cucm_m_emergency-call-handling-with-redsky.html
retrieved_at: 2026-08-16T16:38:41.151414+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU6

Updated: October 8, 2025

Chapter: Emergency Call Handling with RedSky

## Chapter: Emergency Call Handling with RedSky

# Emergency Call Handling with RedSky

## Emergency Call Handling with RedSky Overview

Important

This feature is applicable from Releases 12.5(1)SU6 and 14SU2 onwards.

The RedSky solutions integrated with Unified Communications Manager allow the clients to have an active location for 9-1-1
                           emergency calling coverage for their entire workforce, whether on campus or remote and send the calls to emergency responders.

The endpoints store the location URI received from the RedSky server as a response to HTTP Enabled Location Delivery (HELD)
                           request. When an emergency number 9-1-1 is dialed from Webex, the Unified Communications Manager obtains the previously saved
                           location URI as Geolocation header in INVITE message and routes the calls to the RedSky server with outgoing INVITE containing
                           the location URI as Geolocation header corresponding to the location of the called device. RedSky server replaces with the
                           right ELIN and sends the call to any Public Safety Answering Points (PSAP) for an emergency transmit. E911 Anywhere simultaneously
                           sends call notifications including SMS text, Email, and Security desk screen alerts.

The Cisco Emergency Responder automatically finds and tracks the dispatchable locations of all your devices as they move throughout
                           the enterprise so you can comply with E911 regulations. Emergency Responder tracks Cisco IP Phones through Switch Port or
                           Access Point or IP Subnet or Manually configured. Emergency Responder maintains the status of the phones (On-premises, Off-premises,
                           unlocated), and passes on any Automatic Location Information (ALI) or ELIN information to RedSky. Phone users rely on Unified
                           CM to route their emergency calls to RedSky and the designated emergency provider.

For Off-premises phones, if the user's phone's current location has not been previously defined, the user is directed to the
                           Emergency Responder Off-Premises User web page to create a new location. After the new location has been defined and the address
                           has been confirmed, emergency calls placed from off-premises phones will then be completed through the RedSky.

We recommend that when an employee is working on-premises at an organization site, the user’s location should be defined by
                                       the calling system administrator.

## Emergency Call Handling Configuration Task Flow

The administrator can use the following task to have a dynamic location for 9-1-1 emergency calling and transfer the call
                              to emergency responders.

Step 1

Configure RedSky Server

Create a SIP Trunk for routing the call to the RedSky server.

Step 2

Configure Service Profile

Add the Service Profile details of an end-user for emergency calls.

Step 3

Assign the Service Profile

Assign the created service profile to the Webex client end-user.

Step 4

Setting Up the SIP Route Pattern for Routing Calls

Create SIP Route Pattern with the domain name and associate the same with the previously created SIP trunk.

### Configure RedSky Server

Use this procedure to create a SIP Trunk for routing the call to the RedSky server.

Steps 7, 8 and 9 are only needed during on-premises integration.

Step 1

From Cisco Unified CM Administration, choose Device > Trunk .

Step 2

Click Add New .

Step 3

From the Trunk Type drop-down list, choose SIP Trunk .

Step 4

From the Protocol Type drop-down list, choose the type of SIP trunk that matches your deployment and click Next .

Step 5

In the SIP Information area, enter an IPv4 address of the RedSky server, fully qualified domain name, or DNS SRV record for the server or endpoint
                                          that you want to connect to the SIP trunk in the Destination Address text box.

Step 6

From the SIP Trunk Security Profile drop-down, assign a security profile. If you don't select this option, a SIP Trunk Security Profile nonsecure profile will
                                          be assigned.

Step 7

(Optional) From the SIP Profile drop-down list, assign a Ping option enabled RedSky SIP profile.

Step 8

(Optional) In the Normalization Script area, from the Normalization Script drop-down, choose redsky-alternate-id-interop .

Step 9

(Optional) For Parameter Name and Parameter Value , enter the respective information.

The following inputs are supported for Parameter Name :

RedSky-CustomerID —This is a mandatory field. It is the HELD ID from RedSky admin page. This is used to identify the customer account for the
                                                   calling party.

Alternate-Callback-Number —This is an optional field. This field inserts an optional callback number for emergency calls. It should be used for callers
                                                   that do not have Direct Inward Dial (DID) numbers for callback.

Ext-Length —This is an optional field. This parameter is used for customers with non-E.164 numbering convention. The parameter will enters
                                                   the non-E.164 into the RedSky E911-User-ID header.

Agent-Ext —This is an optional field. This parameter identifies agent extensions based on the matching digits. Populating this parameter
                                                   puts the agent calling party into the RedSky E911-User-ID header.

The script does not only look for leading digits in the extension it looks at. For example, if Agent-Ext is set to “5”, 12345678
                                                   will match, although 12345678 does not have a 5 as a leading digit.

If Agent-Ext is set to 100200, then 123410020088 will match although 100200 is not a leading digit.

If Agent-Ext is set to 12, then 446658787 will not match because it does not contain 12.

Step 10

Click Save .

### Configure Service Profile

Use this procedure to add the Service Profile details of an end-user for emergency calls.

#### Before you begin

You must create a SIP Trunk with the destination as the RedSky server and a SIP Profile with Ping options enabled. A SIP route
                                       pattern must be created with the required domain name (RedSky), and it is associated with the trunk created previously.

A service profile is applied for a given device only when the owner's user ID is specified.

The Emergency Call Handling with RedSky feature can be done without using Cisco Emergency Responder emergency call routing.

Step 1

From Cisco Unified CM Administration, choose User Management > User Settings > Service Profile .

Step 2

Click Add New .

Step 3

Enter a Name and Description for the chosen Service Profile Configuration.

For each UC service that you want to be a part of this profile, assign the Primary , Secondary , and Tertiary connections for that service. The fields in the Service Profile Configuration window vary depending on which UC service you configure.

Step 4

In the Emergency Calling Profile section, perform the following:

Check Enable Emergency Calling to enable configuration parameters to endpoints and soft clients to update location and send
                                                emergency calls to the Emergency Calling Service Provider.

Enter the Company ID and Passphrase provided by the Emergency Calling Service Provider when the account is created, and service
                                                is enabled in the Organization ID and Secret field. For example, 32-character alphanumeric string provided by RedSky.

Enter the passphrase required by the Emergency Calling Service Provider Authorization Service in the Secret field. For example, 16-character alphanumeric string provided by RedSky.

Enter the URL that the device uses to request and set the location in the Location URL field.

Enter the Emergency Service Numbers . By default, 911, 933 is entered with a comma separating each number.

When Webex client dials any emergency pattern configured in Emergency Numbers, it will be routed with Geolocation headers
                                                               to the RedSky server configured in the SIP Trunk.

Step 5

Complete the remaining fields in the Service Profile Configuration window. For detailed field descriptions, see the online Help.

Step 6

Click Save .

### Assign the Service Profile

Use this procedure to assign the created service profile to the Webex client end-user. If Webex is not registered to Unified
                                 CM, the end-user will not be active and does not route the emergency calls to RedSky.

You can apply the Service Profile to an end-user to assign the UC services configuration settings in the Service Profile to
                                 that end user. You can configure different service profiles for different groups of users in the organization so that each
                                 group of users has the right services configured for their job.

Step 1

From Cisco Unified CM Administration, choose User Management > End User .

Step 2

In the Find and List Users window, perform either of the following:

Click Add New to configure a new user.

Specify the filters in the Find User Where field and then click Find to retrieve a list of users.

For more information on associating a device with a user, see the Associate Devices to End User section in Cisco Emergency Responder Administration Guide .

Step 3

In the Service Settings section, select the RedSky Service Profile from the UC Service Profile drop-down list.

Step 4

Complete the remaining fields in the End User Configuration window. For detailed field descriptions, see the online help.

Step 5

Click Save .

### Setting Up the SIP Route Pattern for Routing Calls

Use this procedure to create SIP Route Pattern with the domain name and associate the same with the previously created SIP
                                 trunk.

All emergency calls that are routed to the Emergency Provider must match a route pattern. The route pattern directs the call
                                 to a Route Group, Route List, and SIP Trunk or PRI gateway that can reach the RedSky server.

PRI - RedSky provides the customer an account-specific access number. In this case, the number is the customer ID and the
                                 CALLING PARTY is the user reference. It follows traditional RP/RG/RL/GW redundancy. The calling party number must match the
                                 RedSky user’s ID.

We recommend using SIP Trunks to connect with the RedSky server. For dedicated instances, this is the default method. For
                                 customers having an on-premises deployment of Unified Communications Manager on-premises, you must configure the SIP Trunk, Route Group and Route List before creating the route pattern that will be
                                 used to reach the RedSky server.

If using a SIP trunk, the administrator must use a predefined LUA script to ensure proper customer identification. For Unified
                                 CM deployments, you must upload the script and apply it to the SIP Trunk. The LUA script allows for only one parameter, which
                                 is the RedskyOrgID.

Step 1

From Cisco Unified CM Administration, choose Call Routing > SIP Route Pattern .

Step 2

Click Add New to add the RedSky route pattern.

Step 3

From the Pattern Usage drop-down, choose Domain Routing .

Step 4

Enter the route string in the IPv4 Pattern or IPv6 Pattern field depending on whether you are deploying the IPv4 or IPv6 address.

Step 5

Choose a RedSky SIP trunk in the SIP Trunk/Route List* drop-down.

Step 6

(Optional) Click the Edit link to view or change the Trunk Configuration details.

Step 7

Complete the remaining fields in the SIP Route Pattern Configuration window. For detailed field descriptions, see the online
                                          Help.

Step 8

Click Save .

| Important | This feature is applicable from Releases 12.5(1)SU6 and 14SU2 onwards. |
|---|---|

| Note | We recommend that when an employee is working on-premises at an organization site, the user’s location should be defined by
                                       the calling system administrator. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure RedSky Server | Create a SIP Trunk for routing the call to the RedSky server. |
| Step 2 | Configure Service Profile | Add the Service Profile details of an end-user for emergency calls. |
| Step 3 | Assign the Service Profile | Assign the created service profile to the Webex client end-user. |
| Step 4 | Setting Up the SIP Route Pattern for Routing Calls | Create SIP Route Pattern with the domain name and associate the same with the previously created SIP trunk. |

| Note | Steps 7, 8 and 9 are only needed during on-premises integration. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunk . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Trunk Type drop-down list, choose SIP Trunk . |
| Step 4 | From the Protocol Type drop-down list, choose the type of SIP trunk that matches your deployment and click Next . |
| Step 5 | In the SIP Information area, enter an IPv4 address of the RedSky server, fully qualified domain name, or DNS SRV record for the server or endpoint
                                          that you want to connect to the SIP trunk in the Destination Address text box. |
| Step 6 | From the SIP Trunk Security Profile drop-down, assign a security profile. If you don't select this option, a SIP Trunk Security Profile nonsecure profile will
                                          be assigned. |
| Step 7 | (Optional) From the SIP Profile drop-down list, assign a Ping option enabled RedSky SIP profile. |
| Step 8 | (Optional) In the Normalization Script area, from the Normalization Script drop-down, choose redsky-alternate-id-interop . |
| Step 9 | (Optional) For Parameter Name and Parameter Value , enter the respective information. The following inputs are supported for Parameter Name : RedSky-CustomerID —This is a mandatory field. It is the HELD ID from RedSky admin page. This is used to identify the customer account for the
                                                   calling party. Alternate-Callback-Number —This is an optional field. This field inserts an optional callback number for emergency calls. It should be used for callers
                                                   that do not have Direct Inward Dial (DID) numbers for callback. Ext-Length —This is an optional field. This parameter is used for customers with non-E.164 numbering convention. The parameter will enters
                                                   the non-E.164 into the RedSky E911-User-ID header. Agent-Ext —This is an optional field. This parameter identifies agent extensions based on the matching digits. Populating this parameter
                                                   puts the agent calling party into the RedSky E911-User-ID header. The script does not only look for leading digits in the extension it looks at. For example, if Agent-Ext is set to “5”, 12345678
                                                   will match, although 12345678 does not have a 5 as a leading digit. If Agent-Ext is set to 100200, then 123410020088 will match although 100200 is not a leading digit. If Agent-Ext is set to 12, then 446658787 will not match because it does not contain 12. |
| Step 10 | Click Save . |

| Note | The Emergency Call Handling with RedSky feature can be done without using Cisco Emergency Responder emergency call routing. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Settings > Service Profile . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Enter a Name and Description for the chosen Service Profile Configuration. Note For each UC service that you want to be a part of this profile, assign the Primary , Secondary , and Tertiary connections for that service. The fields in the Service Profile Configuration window vary depending on which UC service you configure. | Note | For each UC service that you want to be a part of this profile, assign the Primary , Secondary , and Tertiary connections for that service. The fields in the Service Profile Configuration window vary depending on which UC service you configure. |
| Note | For each UC service that you want to be a part of this profile, assign the Primary , Secondary , and Tertiary connections for that service. The fields in the Service Profile Configuration window vary depending on which UC service you configure. |
| Step 4 | In the Emergency Calling Profile section, perform the following: Check Enable Emergency Calling to enable configuration parameters to endpoints and soft clients to update location and send
                                                emergency calls to the Emergency Calling Service Provider. Enter the Company ID and Passphrase provided by the Emergency Calling Service Provider when the account is created, and service
                                                is enabled in the Organization ID and Secret field. For example, 32-character alphanumeric string provided by RedSky. Enter the passphrase required by the Emergency Calling Service Provider Authorization Service in the Secret field. For example, 16-character alphanumeric string provided by RedSky. Enter the URL that the device uses to request and set the location in the Location URL field. Enter the Emergency Service Numbers . By default, 911, 933 is entered with a comma separating each number. Note When Webex client dials any emergency pattern configured in Emergency Numbers, it will be routed with Geolocation headers
                                                               to the RedSky server configured in the SIP Trunk. | Note | When Webex client dials any emergency pattern configured in Emergency Numbers, it will be routed with Geolocation headers
                                                               to the RedSky server configured in the SIP Trunk. |
| Note | When Webex client dials any emergency pattern configured in Emergency Numbers, it will be routed with Geolocation headers
                                                               to the RedSky server configured in the SIP Trunk. |
| Step 5 | Complete the remaining fields in the Service Profile Configuration window. For detailed field descriptions, see the online Help. |
| Step 6 | Click Save . |

| Note | For each UC service that you want to be a part of this profile, assign the Primary , Secondary , and Tertiary connections for that service. The fields in the Service Profile Configuration window vary depending on which UC service you configure. |
|---|---|

| Note | When Webex client dials any emergency pattern configured in Emergency Numbers, it will be routed with Geolocation headers
                                                               to the RedSky server configured in the SIP Trunk. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > End User . |
|---|---|
| Step 2 | In the Find and List Users window, perform either of the following: Click Add New to configure a new user. Specify the filters in the Find User Where field and then click Find to retrieve a list of users. Note For more information on associating a device with a user, see the Associate Devices to End User section in Cisco Emergency Responder Administration Guide . | Note | For more information on associating a device with a user, see the Associate Devices to End User section in Cisco Emergency Responder Administration Guide . |
| Note | For more information on associating a device with a user, see the Associate Devices to End User section in Cisco Emergency Responder Administration Guide . |
| Step 3 | In the Service Settings section, select the RedSky Service Profile from the UC Service Profile drop-down list. |
| Step 4 | Complete the remaining fields in the End User Configuration window. For detailed field descriptions, see the online help. |
| Step 5 | Click Save . |

| Note | For more information on associating a device with a user, see the Associate Devices to End User section in Cisco Emergency Responder Administration Guide . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > SIP Route Pattern . |
|---|---|
| Step 2 | Click Add New to add the RedSky route pattern. |
| Step 3 | From the Pattern Usage drop-down, choose Domain Routing . |
| Step 4 | Enter the route string in the IPv4 Pattern or IPv6 Pattern field depending on whether you are deploying the IPv4 or IPv6 address. |
| Step 5 | Choose a RedSky SIP trunk in the SIP Trunk/Route List* drop-down. |
| Step 6 | (Optional) Click the Edit link to view or change the Trunk Configuration details. |
| Step 7 | Complete the remaining fields in the SIP Route Pattern Configuration window. For detailed field descriptions, see the online
                                          Help. |
| Step 8 | Click Save . |