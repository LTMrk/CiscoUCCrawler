---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-15-english-administration-guide-cer0-b-cisco-emergency-responder-adminis-1a2d417e92
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/15/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-15/cer0_m_cer-administration-web-interface.html
retrieved_at: 2026-08-21T15:02:51.086911+00:00
---

Cisco Emergency Responder Administration Guide, Release 15 and SUs

# Cisco Emergency Responder Administration Guide, Release 15 and SUs

Updated: March 17, 2026

Chapter: Cisco Emergency Responder Administration Web Interface

## Chapter: Cisco Emergency Responder Administration Web Interface

# Cisco Emergency Responder Administration Web Interface

## Server Groups in Cluster

The
                              		  Emergency Responder Server Groups in Cluster page appears when you choose System >
                                 			 Cisco Emergency
                                 			 Responder Groups in Cluster .

### Authorization
                              		  Requirements

You must
                              		  have system administrator, ERL administrator, or network administrator
                              		  authority to access this page.

### Description

Use the
                              		  Emergency Responder Server Groups in Cluster page to view the Emergency
                              		  Responder groups that form an Emergency Responder cluster. You can view which
                              		  Emergency Responder servers belong to each Emergency Responder group within the
                              		  cluster. You can click on the link for the remote server groups in an Emergency
                              		  Responder cluster (select either the primary server or the backup server) to go
                              		  directly to the Emergency Responder interface for these servers.

The
                              		  following table describes the Emergency Responder Server Groups in Cluster
                              		  page.

Field

Description

Notes

Emergency Responder Groups list

A
                                          					 list of the Emergency Responder server groups that are pointing to the same
                                          					 cluster database host.

Click a group name to view the servers in the group.

The
                                          					 Emergency Responder cluster consists of this set of Emergency Responder groups.
                                          					 You create the cluster when installing Emergency Responder servers. See Installation on a New System .

Emergency Responder Group Name

The
                                          					 name of the server group.

Click the server group name to display the servers in that group
                                          					 in the Servergroup Details section of page.

Primary Host Name

The
                                          					 DNS host name or IP address of the primary server in the group.

Click this host name (except for the local server group) to open
                                          					 the Emergency Responder administration page for that server in a new window.

Standby Host Name

The
                                          					 DNS host name or IP address of the standby, or backup server in the group.

Click this host name (except for the local Server Group) to open
                                          					 the Emergency Responder administration page for that server in a new window.

Delete button

Click Delete to remove the Emergency Responder group you are viewing from the Emergency
                                          					 Responder cluster.

Only system administrators can delete a Emergency Responder
                                          					 group from the cluster.

Delete a group from the cluster before you uninstall a Emergency
                                          					 Responder group.

## Group
                        	 Settings

The
                              		  Emergency Responder Group Settings page appears when you choose System >
                                 			 Cisco ER Group Settings .

### Authorization
                              		  Requirements

You must have a system administrator authority to access this page.

### Description

Use the Emergency Responder Group Settings page to define the operational characteristics of an Emergency Responder server
                              group.

The
                              		  following table describes the Emergency Responder Server Group Settings page.

Field

Description

Notes

Emergency Responder Group Name

The name of the server group. This name is used for your information only, so create a name you find useful.

Peer TCP Port

The TCP port used for communications between Emergency Responder servers within the server group. If you don't want to use
                                          the default port, ensure you select an unused port.

The range is 1024 to 65535.

Heartbeat Count

The number of counts an Emergency Responder server should wait before declaring an unresponsive Emergency Responder server
                                          unavailable.

The default number of counts is 3. The range is 3 to 10.

The time between counts is defined in Heartbeat Interval.

Heartbeat Interval (in sec)

The number of seconds between sending heartbeat messages to the other Emergency Responder server in the server group.

The default is 30 seconds. The range is 30 to 300 seconds.

Active Call Timeout (in min)

How long to maintain a call route mapping so the PSAP can call back the emergency caller.

The default is 180 minutes (3 hours). The range is 30 to 1440 minutes.

SMTP Mail Server

The IP address or fully qualified name of the mail server (for example, email.domain.com).

Check the Enable Secured connection check box to send mails from the SMTP Mail Server in a secure mode.

Configure an email server if you want Emergency Responder to send email or email-based pages to security officers when an
                                          emergency call is made.

Ensure to configure the SMTP Mail Server in a secure mode and the SMTP server certificate is added to the Tomcat trust store
                                          of the Cisco Emergency Responder before enabling the check box. Failing to do so may result in email alert delivery failure.

The Port number for enabling Secure SMTP connection is 587. To set up a Secure SMTP connection, perform the following:

Exchange Cisco Emergency Responder Tomcat certificate chain to SMTP server's root certificate directory.

Upload SMTP server certificate chain as tomcat-trust certificates on Cisco Emergency Responder.

Restart Cisco Tomcat service on Cisco Emergency Responder servers using the CLI command utils service restart Cisco Tomcat .

Source Mail ID

If you configure a mail server, you must enter an email account on that server that can be used for sending email.

Emails or pages sent to security come from this email account.

System Administrator Mail ID

Mail account where Emergency Responder sends critical information about the system.

Emails or pages sent to the system administrator by Emergency Responder come to this email account.

Calling Party Modification

Dynamic modification of the calling party number. Allows you to reduce the number of route patterns by configuring multiple
                                          ELIN numbers for a single route pattern. ELIN numbers must still be unique.

You must set this flag if you enabled Calling Party Modification when you created Emergency Responder as a Unified CM user.

Syslog

Select from the drop-down list that enables and disables the writing of log messages.

Syslog Server

The name of the server that has the log messages.

Enter the fully qualified DNS name of the server, for example, cw2k.domain.com.

Enter the hostname or IP address of the syslog server to accept syslog messages. This server handles the logging of all the
                                          Cisco Emergency Responder application event-related information.

514 is the default port used to communicate.

You can only enter a server name if you choose Enable Syslog .

Notes

Any notes you want to enter to help you understand the use of the server group.

Dynamic Tracking of Switch IP Address

Dynamically updates a LAN switch's IP address if it is configured with hostname in Emergency Responder.

This action is not applicable to LAN switches that are added to Emergency Responder using an IP address.

Security end user web interface language

Pulldown menu allows you to select the language that is displayed on the users web page—English (US), French (Canada), or
                                          Spanish (Spain).

After you change the language, you must complete the following before the language is displayed on the users web page:

Restart Emergency Responder Service in Emergency Responder Serviceability by choosing Tools > Control Center .

Restart Cisco Tomcat service using the CLI command utils service restart Cisco Tomcat .

Refresh the current Emergency Responder User webpage.

Limit Concurrent Sessions

Limits the number of concurrent sessions per user.

Selecting or deselecting this check box enables or disables the Max. number of concurrent sessions drop-down list.

Max. number of concurrent sessions

If Limit Concurrent Sessions is enabled, this limit is applicable for all the users.

The limit is imposed separately for each Emergency Responder website:

Emergency Responder Administration

Emergency Responder Serviceability

Emergency Responder User

Emergency Responder Admin Utility

Enable AXL & Cluster Secured connection

AXL communication with other products and cluster communication is secured.

Ensure the Cisco Unified Communications Manager tomcat-trust certificate and the Cisco Emergency Responder server group certificate is added to the Tomcat trust store of the Cisco Emergency Responder (in both publisher and subscriber). Failing to do so may result in breaking of AXL communication between Cisco Unified Communications Manager and Cisco Emergency Responder , along with the cluster communication within the Cisco Emergency Responder group.

Discovery Threshold Time (in hrs)

Set the threshold time after which the Emergency Responder sends you an email alert when the discovery of Cisco IP Phones
                                          or devices is stalled. Emergency Responder should be able track the devices anytime from 6 to 24 hours.

Check the Enable Discovery Mail Alert check box to enable the Discovery mail alert option.

The default is 0 hours if you do not enable the Enable Discovery Mail Alert check box. The threshold range is 6 to 24 hours.

IPv6 Subnet Configurations have precedence over IPv4

Check the check box if you want the E911 calls to take precendence of IPv6 subnet over the IPv4 subnet. If you uncheck this
                                          option, IPv4 subnet is given precedence, and the calls are routed via the IPv4 subnet.

For more information on the various IPv6/IPv4 precedence scenarios using both dual-stack and single stack devices, see Table 2 .

Cisco Jabber devices will not work with IPv6 subnets in Emergency Responder.

HTTPS Certificates

This parameter defines the certificates that are supported by the Cisco Tomcat service for establishing HTTPS connections.
                                          This parameter defines whether to enable RSA or both ECDSA and RSA certificates while establishing inbound connections. By
                                          default, the HTTPS interface supports only RSA Certificates.

ECDSA certificates are enabled only if the "All Supported EC and RSA Certificates" option is selected.

Default: RSA Certificates Only

Ensure that you restart the Cisco Tomcat service on all the nodes for the parameter change to take effect.

Update Settings button

Click Update Settings to save and activate your changes.

Cancel Changes button

Click Cancel Changes to change the fields on this page back to the last saved settings.

Scenario

IPv6 Subnet Added

IPv4 Subnet Added

IPv6 Precedence Disabled

IPv6 Precedence Enabled

New call from IPv6 + IPv4 Dual stack phone

Yes

Yes

Calls are routed via the ERL assigned to the IPv4 subnet

Calls are routed via the ERL assigned to the IPv6 subnet

New call from IPv6 + IPv4 Dual stack phone

Yes

No

Calls are routed via the ERL assigned to the IPv6 subnet

Calls are routed via the ERL assigned to the IPv6 subnet

New call from IPv6 + IPv4 Dual stack phone

No

Yes

Calls are routed via the ERL assigned to the IPv4 subnet

Calls are routed via the ERL assigned to the IPv4 subnet

New call from IPv6 + IPv4 Dual stack phone

No

No

Call is routed using the routing pattern configured for the caller's ERL. If none of the call routing criteria is used to
                                          determine the phone location using the Call Routing Order , the default ERL treatment is provided.

Call is routed using the routing pattern configured for the caller's ERL. If none of the call routing criteria is used to
                                          determine the phone location using the Call Routing Order , the default ERL treatment is provided.

New call from IPv6 single stack phone

Yes

Not a valid scenario since the phone has only the IPv6 subnet configured

Calls are routed via the ERL assigned to the IPv6 subnet

Calls are routed via the ERL assigned to the IPv6 subnet

New call from IPv6 single stack phone

No

Not a valid scenario since the phone has only the IPv6 subnet configured

Call is routed using the routing pattern configured for the caller's ERL. If none of the call routing criteria is used to
                                          determine the phone location using the Call Routing Order , the default ERL treatment is provided.

Call is routed using the routing pattern configured for the caller's ERL. If none of the call routing criteria is used to
                                          determine the phone location using the Call Routing Order , the default ERL treatment is provided.

New call from IPv4 single stack phone

Not a valid scenario since the phone has only the IPv4 subnet configured

Yes

Calls are routed via the ERL assigned to the IPv4 subnet

Calls are routed via the ERL assigned to the IPv4 subnet

New call from IPv4 single stack phone

Not a valid scenario since the phone has only the IPv4 subnet configured

No

Call is routed using the routing pattern configured for the caller's ERL. If none of the call routing criteria is used to
                                          determine the phone location using the Call Routing Order , the default ERL treatment is provided.

Call is routed using the routing pattern configured for the caller's ERL. If none of the call routing criteria is used to
                                          determine the phone location using the Call Routing Order , the default ERL treatment is provided.

## Telephony Settings

The
                              		  Telephony Settings page appears when you choose System >
                                 			 Telephony Settings .

### Authorization
                              		  Requirements

You must
                              		  have system administrator authority to access this page.

### Description

Use the
                              		  Telephony Settings page to define the telephone numbers and telephony ports
                              		  used by the Emergency Responder group.

The
                              		  following table describes the Telephony Settings page.

Field

Description

Notes

Route Point for Primary Emergency Responder Server

The CTI route point that the primary server should use, such as
                                          					 911.

See Create Emergency Call Route Points for more information.

Route Point for Standby Emergency Responder Server

The CTI route point that the standby server should use, such as
                                          					 912. Configure this number as the call forward number for the primary emergency
                                          					 number.

See Create Emergency Call Route Points for more information.

PSAP Callback Route Point Pattern

CTI route point that you defined to receive calls from the
                                          					 public safety answering point (PSAP). For example, 913XXXXXXXXXX (913 plus ten
                                          					 Xs).

The number can only consist of numbers and Xs.

For more information, see Create Emergency Call Route Points .

ELIN Digit Strip Pattern

Digits to strip from the beginning of the PSAP Callback Route
                                          					 Point Pattern, for example, 913. The number that results from stripping the
                                          					 pattern should be the ELIN numbers that the PSAP can use to call into your
                                          					 network.

This string must be part of the PSAP Callback Route Point
                                          					 Pattern.

Default
                                          					 ELIN Digit Translation

ELIN number obtained after stripping 913 is matched to a callers extension. If the mapping is not found, Emergency Responder
                                          will translate ELIN to Default ELIN Digit Translation number and complete the PSAP Call-back.

The number could be a dialable extension number or a route pattern. If the number is not reachable the PSAP Call-back will
                                          receive a reorder tone.

UDP Port Begin

Port numbers that are used by CTI ports during their
                                          					 registration.

The range is 1024 to 65535.

Inter-Emergency Responder Group Route Pattern

Route pattern that other Emergency Responder groups use to route
                                          					 emergency calls to this group, for example, 1000.911.

The pattern can only consist of numbers and dots.

For a more detailed explanation of this number, see "Create route patterns for Inter-Cisco Emergency Responder Group Communications".

IP
                                          					 Type of service (00-FF)

Value of the type of service (ToS) byte in the IP header. The
                                          					 default 0xB8 implies a ToS class of Priority Queue. It is recommended that this
                                          					 default value be used for Emergency Responder.

The ToS value entered here only applies to the RTP packets sent
                                          					 by Emergency Responder for the onsite audio alert feature.

Onsite Alert Prompt Repeat Count

Number of times the prompt is played on the onsite alert phone.

Use IP Address from call signaling

If
                                          					 this parameter is enabled, Emergency Responder obtains the IP address of the
                                          					 phone from JTAPI. This parameter is used to route the call. If an IP subnet is
                                          					 configured for the phone, this parameter setting takes precedence over any
                                          					 other manual configuration.

If
                                          					 this parameter is disabled, Emergency Responder uses the manual configuration
                                          					 of the phone to route the call.

This field is applicable only if Emergency Responder is configured with Cisco Unified Communications Manager 6.x and above.

Update Settings button

Click Update
                                             						Settings to save and activate your changes.

Cancel Changes button

Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings.

National E911 Service Provider Route/Translation Pattern

Enter the route patterns or translation pattern for an National E911 Service Provider emergency response location (ERL). An National E911 Service Provider ERL is an ERL that is serviced by National E911 Service Provider . National E911 Service Provider ERL only lists the route patterns that have been configured on this page. You can add new route patterns or translation patterns,
                                          or you can update or remove existing route patterns or translation patterns. National E911 Service Provider Route Pattern Settings supports a maximum of 3000 characters in total.

To add a new route or translation pattern, click on the text
                                          					 box, enter the route pattern, including numbers and wildcard (do not use
                                          					 spaces), and click Add .

To update an existing route pattern, click on the appropriate
                                          					 route pattern, modify the pattern, and click Update .

To remove an existing route pattern, click on the appropriate
                                          					 route pattern and click Remove .

To cancel your existing changes and go back to the last saved
                                          					 settings, click Cancel
                                             						Changes.

## Server Settings for Emergency ResponderServerGroup

The Server
                              		  Settings for Emergency ResponderServerGroup page appears when you choose System > Server
                                 			 Settings .

### Authorization
                              		  Requirements

You must
                              		  have system administrator authority to access this page.

### Description

Emergency
                              		  Responder servers are inserted in the Emergency Responder group when the
                              		  Emergency Responder services are started. (See Installation on a New System .)

Use the
                              		  Server Settings for Emergency ResponderServerGroup page to update server
                              		  settings, for example, to change the server name or to change the trace and
                              		  debug settings, or to delete servers.

You cannot modify
                                          			 the host name of the server.

The
                              		  following table describes the Server Settings Emergency ResponderServerGroup
                              		  page.

Field

Description

Notes

Displays the status of the Server Settings Emergency
                                          					 ResponderServerGroup page.

Server

List of servers you have already created. Click on a server name
                                          					 to see the settings for that server.

You can configure a maximum of two servers per server group.

Server Name

The name of the server.

Change this server name field to any desired value.

Host Name

The DNS name of the Emergency Responder server.

This field cannot be modified.

A
                                          					 selection of subsystems for which you must collect detailed debug information.
                                          					 Debug information includes trace messages as well as more detailed messages.
                                          					 Only select subsystems at the request of Cisco Technical Support; the debug
                                          					 information is for Cisco's use to help resolve problems that you cannot solve
                                          					 yourself.

See Trace and Debug Information for an explanation of each field.

Select All button

Selects all subsystems in the Debug Package List.

Clear All button

Clears all selected subsystems in the Debug Package List.

A
                                          					 selection of subsystems for which you must collect brief trace information.
                                          					 Only select subsystems at the request of Cisco Technical Support; the trace
                                          					 information is for Cisco's use to help resolve problems that you cannot solve
                                          					 yourself.

If
                                          					 you select a subsystem for debug, you do not have to select it for trace.

See Trace and Debug Information for an explanation of each field.

Select All button

Selects all subsystems in the Trace Package List.

Clear All button

Clears all selected subsystems in the Trace Package List.

Update Settings button

Click Update when viewing an existing server's settings to save
                                          					 changes you make to the settings.

Only available when viewing the settings of an existing server.

Cancel Changes button

Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings.

## License
                        	 Manager

The License
                              		  Manager page appears when you choose System > License
                              		  Manager .

### Authorization
                              		  Requirements

You must have the
                              		  system administrator authority to access the License
                                 			 Manager page.

### Description

The License
                                 			 Manager page provides the summary and detailed information on the
                              		  system license usage, as it is reported to the Cisco Smart Software Manager or
                              		  Cisco Smart Software Manager satellite. Licenses are assigned to the company
                              		  Smart Account and are not node locked to a device.

Field

Description

Status

Displays the steps to register with Cisco Smart Software Manager or Cisco Smart Software Manager satellite and the current
                                          license registration mode.

For information on alarms or licensing alerts and compliance, see License Manager Status Messages and License Compliance .

For Permanent License Reservation, status message displays the number of licenses that the administrator specified for this
                                                      system to operate within. License count does not affect compliance status and it is for administrator reference only.

Admin can set the license count through Command Line Interface.

Smart Software Licensing
                                             						Status

Registration Status

Displays the current registration status of the product. The different statuses are:

Registered—For the product which is registered.

Unregistered or Unidentified—For the product which is unregistered.

Unregistered-Registration Expired—For the product whose registration has expired.

Registered-Specific License Reservation /Universal License Reservation —For product which is registered in SLR /PLR mode.

Reservation In Progress—For product whose License Reservation is in progress.

License
                                          					 Authorization Status

Displays the overall authorization status of the product. The different statuses are:

Authorized—Product in authorized or in compliance state.

Authorization Expired—Authorization is expired for the product. This usually happens when the product has not communicated
                                                with Cisco for 90 continuous days.

Out of Compliance—Product is in out of compliance state because of insufficient licenses.

No Licenses in Use—Product does not consume any licenses.

Evaluation Mode—Product is in evaluation mode and not yet registered with Cisco.

Evaluation Period Expired—Evaluation period has expired.

Not Applicable—Unable to determine current registration status.

Authorized-Reserved—Product in authorized or in compliance status for the reserved licenses.

Not Authorized-Reserved—Product is not in authorized state because of insufficient licenses reserved.

Export Control Not Allowed—Product in eval mode.

Transport
                                          					 Settings

Specifies the type of licensing transport mode used in Emergency Responder.

Important

From Release 15SU2 onwards, Call Home as a transport mode for smart licensing is deprecated. Smart Transport mode, the new
                                                      transport mode is introduced for smart licensing.

Transport Settings for Emergency Responder displays one of the following modes:

Call Home —Indicates that Emergency Responder is using call home for smart licensing communication to Cisco Smart Software Manager or
                                                Cisco Smart Software Manager satellite.

Smart Transport (Applicable from Release 15SU2 onwards) —Indicates that Emergency Responder is using smart transport for smart licensing communication to Cisco Smart Software Manager
                                                or Cisco Smart Software Manager satellite.

When you log in to Emergency Responder, a warning message indicates that you are currently using the Call Home mode. In case
                                          you want to switch to the Smart Transport mode, click Test Connectivity and then click on Switch .

The different settings through which Cisco Emergency Responder can connect to Cisco Smart Software Manager or Smart Software
                                          Manager satellite are:

Direct—Emergency Responder sends usage information directly over the internet. No additional components are needed.

HTTP/HTTPS Proxy— Emergency Responder sends usage information over the internet through a proxy server.

Check the Authentication needed on HTTP or HTTPS proxy check box if want to register to Cisco Smart Software Manager using authentication based proxy server. If you enable this
                                                check box, only then the Proxy User and Proxy Password fields are enabled.

Enter the details in the following fields:

Host Name/IP Address

Port

Proxy User

Proxy Password

Smart Software Manager satellite— Emergency Responder sends usage information to an on-premise Smart Software Manager. Periodically, an exchange of information is performed to
                                                keep the databases in synchronization. For more information on installation or configuration of the Smart Software Manager
                                                satellite, go to this URL: https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager-satellite.html .

Transport Gateway—Emergency Responder sends usage information to Cisco Smart Software Manager through a Cisco Transport Gateway.

Check the Do not share my hostname or IP address with Cisco check box to allow the administrator to restrict the exchange of IP Address and hostname of the Emergency Responder during
                                                the registration and synchronization to Cisco Smart Software Manager or Cisco Smart Software Manager Satellite.

Test connectivity with Smart Transport—Allows the administrator to test the Emergency Responder connection to Smart Transport
                                                endpoint through transport setting configurations.

Switch—Allows the administrator to change the transport mode from Call Home to Smart Transport. Cisco Smart License Manager
                                                service is restarted during switch process. This option is available only for Direct or HTTP/HTTPS Proxy server or Cisco Smart
                                                Software Manager satellite in Call Home Mode.

If you choose not to configure the domain and Domain Name System (DNS) on Emergency Responder , then you can select the Cisco Smart Software Manager satellite or transport gateway or proxy server under Transport settings. In such cases, DNS that can resolve https://www.cisco.com has to be configured on the Cisco Smart Software Manager satellite , or Transport Gateway, or HTTP/HTTPS Proxy server.

Transport Gateway as a transport mode is not supported in Smart Transport. Therefore, it continues to use call home post upgrade.
                                                      To switch to Smart Transport mode, deregister the product. Also, the system must connect to Smart Transport URL using Direct
                                                      or Cisco Smart Software Manager satellite or HTTP/HTTPS Proxy server. In case of any issues with Smart Transport mode, use
                                                      the license smart call-home destination address TransportGateway command to fall back to the Call Home mode.

Smart
                                          					 Account Name

Displays information of the customer Smart Account. It is created from the Request a Smart Account option under Administration section of the https://software.cisco.com/ . It is the primary account created to represent the customer and all licenses for a company that are assigned to this Smart
                                          Account. It also manages licenses for all Cisco products.

Virtual
                                          					 Account

A
                                          					 self-defined construct to reflect the company organization. Licenses and
                                          					 Product instances can be distributed across virtual accounts. Created and
                                          					 maintained by the administrator on the Cisco Smart Software Manager or Cisco
                                          					 Smart Software Manager satellite with full visibility to company assets.

Licensing
                                          					 Mode

Displays the licensing mode of the product. The default mode is Enterprise.

Export-Controlled Functionality

Specifies if the Export-Controlled functionality was enabled
                                          					 in the token with which the product was registered.

Displays one of the following status information:

Allowed—The token registered with has Allow export-controlled functionality selected.

Not Allowed—The token registered with do not have Allow export-controlled functionality selected or Cisco Emergency Responder
                                                not registered.

Actions

The Actions drop-down list box gets activated only after a successful registration. It lists the following type of actions which can
                                          be performed:

Renew Authorization Now

Renew Registration Now

Reregister

Deregister

Register

Use the Register button to register Cisco Emergency Responder with Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

Request Entitlement Now

Synchronize Now

Click
                                          					 the Synchronize Now button to send a synchronization
                                          					 (entitlement) request to Cisco Smart License Manager.

Last
                                          					 Synchronization

This is
                                          					 a static field that displays the last authorization attempt time and its
                                          					 success or failure status. For example, Jan 19 23:31:00 2017 IST (Succeeded).

License Requirement by
                                             						Type

License
                                          					 Type

Displays
                                          					 the Cisco Emergency Responder (CER) license type. The only available license
                                          					 type is CER_USER.

Description

Displays the description for the license type which is, CER User License.

Status

Displays the current license status based on the license type (CER_USER).The different statuses are:

Authorization Expired—The authorized period has expired.

Evaluation—The agent is using the evaluation period for this entitlement.

Evaluation Period Expired—Evaluation period has expired.

Authorized—In compliance (authorized).

No Licenses in Use—There are no licenses being consumed by the product instance.

Out of Compliance—Out of compliance.

Waiting—The initial state after an entitlement request while waiting for the authorization request response.

Count

Displays the total number of users currently tracked.

Details of Cisco ER Licenses

Number
                                          					 of phones discovered

Displays
                                          					 the number of discovered phones tracked in an IP Subnet and the Switch port.

Number
                                          					 of phones manually configured

Displays
                                          					 the number of manually configured phones. For example, analog phones.

Total
                                          					 number of users being tracked currently

Displays
                                          					 the number of phones tracked by Cisco Emergency Responder, which requires a
                                          					 User License. When you click the displayed hyperlinked number, the Tracked Phones List window is displayed, which lists
                                          					 the tracked phones.

Total
                                          					 number of users configured not to be tracked

Displays
                                          					 a list of phones configured with an IP Subnet and Cisco Emergency Responder does not track it.

In a scenario where a Dual-stack phone has both the IPv4 and IPv6 addresses configured, and the phone falls under both the
                                                      IPv4 and IPv6 subnets having the same priority, and one of the subnet is trackable and the other one is non-trackable, the
                                                      phone is considered to be trackable.

Smart
                                             						Licensing Product Registration

The
                                          					 Smart Software Manager or Cisco Smart Software Manager satellite manages the
                                          					 product license. It also provides a link to the Smart Software Manager page.

### Smart Software
                           	 Licensing Product Registration

The Smart
                                 		  Software Licensing Product Registration window is displayed when you
                              		click the Register button on the License
                                 		  Manager page. See License Manager page for more information on the system license usage.

Field

Description

Status

Displays the
                                          				  product registration status.

Product
                                          				  Instance Registration Token

Displays a
                                          				  text area where you can enter the product registration token generated from the
                                          				  Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

Reregister
                                          				  this product instance if it is already registered

Check the Reregister this product instance if it is already
                                             					 registered check box to enable a force registration of the product
                                          				  with Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

Register

Click the Register button to register Cisco Emergency Responder with Cisco Smart
                                          				  Software Manager or Cisco Smart Software Manager satellite.

The Register button gets disabled after a successful
                                          		  registration with Cisco Smart Software Manager or Cisco Smart Software Manager
                                          		  satellite.

### Transport
                           	 Setting

The Transport Setting window is displayed when you click View/Edit link from the License Manager page. For more information on system license usage, see License Manager page.

In Transport
                                 		  Setting window, you can configure how the product communicates with
                              		Cisco Smart Software Manager or Cisco Smart Software Manager satellite. You can
                              		click the radio button to select one of the options. The available Transport
                              		Setting options are tabulated.

Field

Description

Status

Displays the current configuration status of the Smart Call Home or Smart Transport (Applicable from Release 15SU2 onwards) .

When you log in to Emergency Responder, a warning message indicates that you are currently using the Call Home mode. In case
                                          you want to switch to the Smart Transport mode, click Test Connectivity and then click on Switch .

Transport Gateway as a transport mode is not supported in Smart Transport. Therefore, it continues to use call home post upgrade.
                                                      To switch to Smart Transport mode, deregister the product. Also, the system must connect to Smart Transport URL using Direct
                                                      or Cisco Smart Software Manager satellite or HTTP/HTTPS Proxy server. In case of any issues with Smart Transport mode, use
                                                      the license smart call-home destination address TransportGateway command to fall back to the Call Home mode.

Transport Settings

Direct

Product
                                          				  sends usage information directly over the internet. No additional components
                                          				  are needed. This is the default communication mode.

HTTP or
                                          				  HTTPS Proxy Server

Product
                                          				  sends usage information over the internet through a proxy server (such as Cisco
                                          				  Transport Gateway or Apache).

Check the Authentication needed on HTTP or HTTPS proxy check box if want to register to Cisco Smart Software Manager using authentication based proxy server. If you enable this
                                          check box, only then the Proxy User and Proxy Password fields are enabled.

Enter the details in the following fields:

Host Name/IP Address

Port

Proxy User

Administrators should ensure that they enter the configured user name for proxy in the Proxy User field.

Proxy Password

Smart Software Manager satellite

Emergency Responder sends usage information to an on-premise Smart Software Manager. Periodically, an exchange of information is performed to
                                          keep the databases in synchronization. For more information on installation or configuration of the Smart Software Manager
                                          satellite, go to this URL: https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager-satellite.html .

If you are using HTTP for Call Home, go to the URL: http://Satellite-ip/Transportgateway .

If you are using HTTPS for Call Home, go to the URL: https://SatelliteFQDN-OR-IP-address/TransportGateway .

If you are using HTTP for Smart Transport, go to the URL: http://Satellite-ip/SmartTransport .

If you are using HTTPS for Smart Transport, go to the URL: https://SatelliteFQDN-OR-IP-address/SmartTransport .

Transport Gateway

Emergency Responder sends usage information to Cisco Smart Software Manager through a Cisco Transport Gateway.

Test connectivity with Smart Transport

Allows the administrator to test the Emergency Responder connection to Smart Transport endpoint through transport setting
                                          configurations.

Switch

Allows the administrator to change the transport mode from Call Home to Smart Transport. Cisco Smart License Manager service
                                          is restarted during switch process. This option is available only for Direct or HTTP/HTTPS Proxy server or Cisco Smart Software
                                          Manager satellite in Call Home Mode.

Do not share my hostname or IP address with Cisco

Check the check box to allow the administrator to restrict the exchange of IP Address and hostname of the Cisco Emergency
                                          Responder during the registration and synchronization to Cisco Smart Software Manager or Cisco Smart Software Manager Satellite.

When the check box is selected, Cisco Emergency Responder will not share the IP Address or hostname information from being
                                                      sent through registration and regular license compliance synchronization activities. A unique identifier is generated for
                                                      the Cisco Emergency Responder Product Instance and will need to be used for cross-referencing in Cisco Smart Software Manager.

Transport settings
                                          		  are shared with Smart
                                             			 Call Home , so any changes made in the Transport
                                             			 Setting window applies to other features using this service.

### Smart Software
                           	 Licensing Product Re-registration

The Smart
                                 		  Software Licensing Product Re-registration window is displayed when
                              		you select the Reregister option from the Actions drop-down list box on the License
                                 		  Manager page. See License Manager page for more information on the system license usage.

Field

Description

Status

Displays the
                                          				  product re-registration status.

Product
                                          				  Instance Registration Token

Displays a
                                          				  text area where you can enter the product registration token generated from the
                                          				  Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

Re-register

Click the Re-register button to re-register the product with
                                          				  Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

## Email Alert
                        	 Settings

The Email
                              		  Alert Settings page appears when you choose System > Mail
                                 			 Alert Configurations .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the
                              		  Email Alert Settings page to specify the parameters under which Emergency
                              		  Responder sends email alerts. Use the check box to the right of each parameter
                              		  to enable (check) or disable (uncheck) email alerts for that parameter. Check
                              		  the Include event viewer contents in mail check box if you want to include the
                              		  details from the event viewer in the email message.

The
                              		  following table describes the Email Alert Settings page.

Field

Discovery Engine Registration Failed

The Discovery Engine fails to register

Discovery Engine goes out of connection

The Discovery Engine loses connection

For unreachable devices during recovery

Devices such as switches and CiscoUnified
                                          					 CommunicationsManagers become unreachable

Call information

A
                                          					 911 call is placed

Call routing session ended due to problems

Call routing is stopped due to any of these reasons:

- Invalid CMC

- Invalid FAC

- FAC and CMC needed

- CMC needed

- FAC needed

- RESOURCE_BUSY

Rerouting of call

An
                                          					 emergency call is rerouted

Routing failure

Call routing fails

Route Point out of Service

The route point goes out of service

Cluster DB Failure

The server cannot communicate with the cluster database host

Intra Cluster Failure

The intra-cluster communication to a server group in the cluster
                                          					 fails

Subscriber becomes active

The Subscriber becomes active

Publisher comes back online

The Publisher comes back online

Not able to get the JTAPI Provider

When Emergency Responder cannot get the JTAPI provider

Available user licenses get exhausted during phone tracking

When the number of user licenses are exhausted during phone
                                          					 tracking

Switch Port location change reporting

When you enable switch port change reporting for phones

Suppress IP Communicator location change reporting

When you filter CiscoUnifiedIP Communicator from the location
                                          					 change reporting email alerts

DRF Alert

Enable or Disable DRF backup or restore mail alerts

Update Settings button

Updates the email alert settings

Cancel Changes button

Cancels changes made to the email alert settings

## Add
                        	 Subscriber

The Add
                              		  Subscriber page appears when you choose System > Add
                                 			 Subscriber .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the Add Subscriber page to add a subscriber server to an Emergency Responder server group. After adding the subscriber
                              information, you must enter the correct publisher server information when prompted during installation.

### Before You
                              		  Begin

You must first configure a publisher server before configuring a subscriber server.

The
                              		  following table describes the Add Subscriber page.

Field

Description

HostName

Host name of the subscriber server.

Insert button

Click Insert to add the new subscriber server.

Cancel Changes button

Removes input from the Add Subscriber page.

A
                                          					 list of all currently configured servers, showing the host name and IP address
                                          					 of each server.

## National E911 Service Provider VUI Settings

The National E911 Service Provider VUI Settings page appears when you choose System > National E911 Service Provider VUI Settings .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the National E911 Service Provider VUI Settings page to enter the account information that is required for Emergency Responder to interoperate with National E911 Service Provider Validation and Update Interface. After entering the required information, you can test the connectivity to National E911 Service Provider from this page.

The following table describes the National E911 Service Provider VUI Settings page.

Field

Description

Displays status messages.

Upload Certificate

Uploads the certificate from your local drive to the Emergency
                                          					 Responder server.

To
                                          					 upload a certificate, follow these steps:

Click Upload Certificate

An
                                                						  Upload Certificate window appears.

Click
                                                						  the Browse button to locate the certificate file on your local
                                                						  machine.

Click
                                                						  the Upload button to upload the certificate file.

National E911 Service Provider Certificate Password

The password that was generated with this certificate.

VUI URL

VUI URL is provided by National E911 Service Provider .

Enable HTTP Proxy

Check this check box if you want to use a proxy server for requests between Emergency Responder and National E911 Service
                                          Provider.

Proxy Host Name/IP Address

Enter the IP address or hostname of the proxy server, along with the port.

For example, http://<ip_address_or_hostname>:port.

Authentication needed on HTTP Proxy

Check this check box if you want to communicate with the National E911 Service Provider using authentication based proxy server.
                                          If you enable this check box, only then the Proxy User Name and Proxy Password fields are enabled.

Proxy User Name

Enter the configured user name for proxy server in the Proxy User Name field.

Proxy Password

Enter the password that is associated to the username.

Test and Validate Certificate

Use this button to test the validity of your certificate.

VUI Schema URL

The VUI Schema URL provided by National E911 Service Provider .

National E911 Service Provider Account ID

Your National E911 Service Provider Account ID provided by National E911 Service Provider .

Max VUI Connections

The maximum number of simultaneous VUI connections that
                                          					 Emergency Responder allows across the Server group.

MyE911 for Location Updates

Set this drop-down to True if Cisco Jabber and Webex App are using MyE911 or Remote Location Manager to set the users location when Off-premises. Setting
                                          this drop-down to False requires users to update their location through Cisco’s Off-Premise User Page.

By default, this option is set to True .

Test Connectivity

Use this link to verify whether Emergency Responder can successfully connect to National E911 Service Provider VUI.

Delete Account

Deletes an existing National E911 Service Provider account from the Emergency Responder database.

Update

Click Update to save the changes you made on this page.

Cancel

Click Cancel to change the fields on this page back to the last saved
                                          					 settings.

## Onsite Alert
                        	 Settings

The Onsite
                                 			 Alert Settings page appears when you choose ERL > Onsite
                                 			 Alert Settings .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the
                              		  Onsite Alert Settings page to add information about your onsite alert
                              		  personnel. When you configure ERLs, you assign these personnel to them.
                              		  Emergency Responder alerts the assigned personnel when an emergency call is
                              		  made within the zone.

The
                              		  following table describes the Onsite Alert Settings page.

Field

Description

Notes

Onsite Alert ID

The identifier for the onsite alert contact. The identifiers you
                                          					 use should be based on your site identification strategy (for example, security
                                          					 ID or badge number). This field is used throughout Emergency Responder to
                                          					 identify the contact; for example, you select from Onsite Alert IDs when
                                          					 assigning contacts to zones. The Onsite Alert ID cannot be modified after you
                                          					 have saved it.

Use a naming strategy meaningful to your organization, but which
                                          					 is also useful when configuring zones in Emergency Responder.

Onsite Alert Name

The name of the onsite alert contact.

Onsite Alert Number

The telephone number for the onsite alert contact. This number
                                          					 must be a voice telephone number; do not enter the number of a voice-mail
                                          					 system or an automated attendant.

When Emergency Responder gets an emergency call from an ERL, it
                                          					 calls the onsite alert number of the contact for the ERL and plays a
                                          					 prerecorded message that includes the phone number from which the emergency
                                          					 call was placed.

Onsite Alert Email Address

The email address for the onsite alert contact, for example,
                                          					 email@domain.com.

When Emergency Responder gets an emergency call from an ERL, it
                                          					 emails the onsite alert contact associated with the ERL. If the email ID is for
                                          					 an email paging system, the contact receives a page instead of an email. The
                                          					 email or page includes the phone number from which the emergency call was
                                          					 placed.

You can add multiple email addresses by separating each
                                                      						address with a comma (,). Avoid extra spaces between the email addresses.

Onsite Alert Pager Address

The pager email address for the onsite alert contact, for
                                          					 example, <pager_number>@domain.com.

You can limit the size of the message that is sent to the pager
                                          					 by configuring the fields on the Pager Alert Setting Page. See Pager Alert Settings .

Available
                                          					 User Group

The User
                                          					 Group which will receive the specific web alert from the associated ERL. By
                                          					 default Emergency Responder User Group is selected, which has all users.

The users
                                          					 can view all alerts in the system by selecting ALL on the Web Alert page.

Insert

Click the Insert button to add the contact to the list of
                                          					 contacts. The contact is then listed in the Available Onsite Alerts section of the page.

Cancel Changes

Click the Cancel Changes button to cancel any changes made to
                                          					 this page.

Section of the page that displays onsite alert contacts that
                                          					 have already been configured. For configured onsite alert contacts, the
                                          					 following information is displayed:

Onsite Alert ID

Onsite Alert Name

Onsite Alert Number

Onsite Alert Email Address

Onsite User Group

To change an entry, click the entry or click the Edit icon; the person's contact information is loaded in the
                                          					 edit boxes. Make your changes and click Update .

To delete an entry, click the Delete icon on the same line as the entry.

If no contacts have previously been configured, this section is
                                          					 blank.

You cannot modify a contact's Onsite Alert ID.

Before you can delete the entry, you must update the ERLs to
                                          					 which the person is assigned to remove the person from the ERL.

Add New

Click the Add New button to add another contact.

Update

Click the Update button when viewing an existing contact's
                                          					 information to save changes you make to the information.

Only available when viewing the information for an existing
                                          					 contact.

Export

Click
                                          					 the Export button to export the onsite alert settings to
                                          					 another file. For more information, see Export OnsiteAlert Data .

Import

Click
                                          					 the Import button to import the onsite alert settings to
                                          					 your Cisco Emergency Responder configuration. For more
                                          					 information, see Import OnsiteAlert Data .

### Export OnsiteAlert
                           	 Data

The Export
                                 		  OnsiteAlert Data window appears when you click Export on the Onsite
                                 		  Alert Settings page (opened when you choose ERL > Onsite Alert
                                    			 Settings ).

#### Authorization
                                 		  Requirements

You must have the
                                 		  system administrator or ERL administrator authority to access this window.

#### Description

Create a file
                                          				containing the Emergency Responder Export OnsiteAlert Data.

Use the Download option to download a file containing the
                                          				Emergency Responder Export OnsiteAlert Data. For more information, see Download File .

The following
                                 		  table describes the fields found on the Export
                                    			 OnsiteAlert Data window.

Field

Description

Select
                                             					 Export Format

Select
                                             					 the file format from the drop-down list that matches the file being imported.

Enter
                                             					 Export File Name

Enter the
                                             					 name of the file that you want to create. Do not include the file extension.

Export

Click the Export button to add data from the import file to
                                             					 your Cisco Emergency Responder configuration.

Close

Click the Close button to close the window.

This text
                                             					 box displays status information.

Select a
                                             					 File to Download

Select a
                                             					 file from the drop-down list and click the Download button to download the file to your
                                             					 machine.

### Import
                           	 OnsiteAlert Data

The Import
                                 		  OnsiteAlert Data window appears when you click Import on the Onsite
                                 		  Alert Settings page (opened when you choose ERL > Onsite Alert
                                    			 Settings ).

#### Authorization
                                 		  Requirements

You must have the
                                 		  system administrator or ERL administrator authority to access this window.

#### Description

Use the Import
                                    			 OnsiteAlert Data window to create or update several OnsiteAlert Data
                                 		  details at once from the file in which you have defined their data. You can
                                 		  create this file using a spreadsheet and save the information in the required
                                 		  formats. The View
                                    			 sample file link provides the sample information to create or
                                 		  update your import file.

You can import a
                                 		  previously exported file or you can upload a file that you created on your
                                 		  local system using the Upload option. For more information, see Upload File .

The following
                                 		  table describes the fields found on the Import
                                    			 OnsiteAlert Data window.

Field

Description

Select
                                             					 Import Format

Select
                                             					 the file format from the drop-down list that matches the file being imported.

Click View sample file link to view an example of the
                                             					 expected format and sequence of values. Use this sample information to create
                                             					 your import file in a spreadsheet.

Select
                                             					 File to Import

Select
                                             					 the file from the drop-down list from which you want to import data.

Import

Click the Import button to add data from the import file to
                                             					 your Cisco Emergency Responder configuration.

Upload

Click the Upload button to upload the file from your machine.
                                             					 For more information, see Upload File .

Close

Click the Close button to close the window.

This text box displays status information.

## Pager and Email Alert Configurations

The Pager Alert Settings and Email Alert Settings page appears when you choose ERL > Pager Alert and Email Alert Configurations .

### Authorization Requirements

You must have a system administrator or ERL administrator authority to access this page.

### Description

Use the Pager Alert and Email Alert Configurations page to limit the size of system-wide pager and email messages by selecting
                              the fields that are sent to the pager and by editing the labels for those fields.

The following table describes the Pager Alert Settings and Email Alert Settings page.

Field

Descriptions

You can limit the size of the pager message that is sent by selecting the following fields and editing the labels are associated
                                          with those fields:

Extension

ERL

Location

System Time

Server

Local Time

Check the check box to select the fields that you want to display on the pager.

Click the text box to edit the label that you want to send to the pager.

Update Pager Settings

Click Update Settings to save changes that you made.

Restore Pager Defaults

Click Restore Defaults to restore the default pager and label settings.

Send Sample Message to a pager

Enter a pager address in the text box and click Send Test Message to send a test message to your pager.

Email Alert Settings

You can customize email messages sent to the configured onsite security person by choosing the required fields. You can also
                                          add additional notes or mask digits on Caller DN to reflect the local dialing pattern.

Caller Extension

Display Name

Zone

Location

System Call Time

Local Call Time

Server Details—Enter the URL details for the Emergency Responder User page in which you can check the 911 call details. In
                                                case you are updating the hostname, ensure that you enter the new hostname in the server details.

Additional Notes—Enables you to provide any additional information as Admin Notes and the information is available in the
                                                email alerts.

Discard DN digits—You can enter the count of digits to be masked from the beginning on Caller DN to reflect the local dialing
                                                pattern.

Check the check box to select the fields that you want to display on the email message.

Click the editable label text boxes to modify the label that you want to send to the email message.

Update Email Settings

Click Update Email Settings to save the changes made.

Restore Email Defaults

Click Restore Email Defaults to restore the default email message and label settings.

Sample Email Message Preview

Select the required email alert field settings and click Update Email Settings to preview the sample email message.

## Conventional
                        	 ERL

The
                              		  Conventional ERL page appears when you choose ERL
                                 			 >Conventional ERL .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the
                              		  Conventional ERL Data page to define the emergency response locations (ERLs)
                              		  for your company. An ERL might be a whole building (if it is small), the floor
                              		  of a building, or an area on a floor. Each community can have different laws
                              		  concerning the size of an ERL, so consult your local ordinances and with your
                              		  service provider before deciding on your ERLs. The ERLs you create are used by
                              		  emergency response teams to locate the emergency, so the ERL should be small
                              		  enough that these teams can locate the caller within a reasonable time.

The
                              		  following table describes the Find and List ERLs page.

Field

Description

Notes

Find Conventional ERL where...

Select search criteria and click Find to list existing ERLs. To
                                          					 list all ERLs, click Find without entering any criteria. From the drop-down menu, you can select the
                                          					 number of records that display per page for each search.

From the search results list, you can:

- Click an entry to view and
                                             						update its characteristics.

- Click the Copy icon to create a new ERL with the same ALI data.

- Click the Delete icon to remove the ERL.

- Click view... in the Audit Trail column to view a history of
                                             						changes made to that ERL. See ERL Audit Trail for more information.

When copying an ERL, information that must be unique in an ERL
                                          					 is not copied.

See Add New ERL for more information.

Configure Default ERL

You must configure the Default ERL before configuring any other
                                          					 ERLs.

The default ERL is the system-defined ERL that is used to route
                                          					 calls if no other ERL configuration is found.

During the
                                                      						migration of data in an upgrade scenario, if any manually configured phone is
                                                      						assigned to the Default ERL, it remains there until it is modified.

See Add New ERL for more information.

Add New ERL

Click Add New
                                             						ERL to create a new ERL.

See Add New ERL for more information.

Configure Default ERL

Click Configure
                                             						Default ERL to configure a default ERL

Export

Click the Export link to create a file containing your ERL configuration.

See Export ERL Data for information about exporting ERL data.

Import

Click the Import link to create or update ERLs using information stored in a
                                          					 separate file. By importing ERL data, you can create or update many ERLs at one
                                          					 time.

See Import ERL Data for information about importing ERL data.

### Add New ERL

On the ERL Information
                                                				for ERL Name page, the ERL Name variable is replaced with the name of
                                             			 the ERL associated with the page. For example, if you click the Default ERL,
                                             			 the page that appears is titled ERL Information
                                                				for Default . If the ERL name is First Floor, the page that appears is
                                             			 titled ERL Information
                                                				for First Floor .

The Add
                                 		  New ERL and ERL Information for ERL Name pages are essentially the same, as
                                 		  follows:

The Add New ERL
                                       				page appears when you select Add New ERL on the Find ERL Data page (opened when you choose ERL >
                                          				  Conventional ERL ). The page also appears if you click Copy for
                                       				an existing ERL.

The ERL
                                       				Information for Default page opens when you click Configure
                                          				  Default ERL on the Find ERL Data page. The ERL Information for ERL Name
                                       				page also appears when you click any of the links associated with an existing
                                       				ERL in the list on the Find ERL Data page (opened when you choose ERL >
                                          				  Conventional ERL ).

You cannot use
                                                   				  default ERLs as a Test ERL. The Test ERL check box is not available on the ERL
                                                   				  Information for Default page.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the
                                 		  Add New ERL page to create a new emergency response location (ERL).
                                 		  Alternatively, you can create or update many ERLs at once by importing
                                 		  predefined ERL information from a separate file.

Emergency
                                 		  Responder allows you to select the ERL as a Test ERL.

Use the
                                 		  Find ERL Data page to view or update an existing ERL.

See ELIN Numbers Emergency Calls and PSAP Callbacks for information about configuring the ELIN numbers in Cisco Unified Communications Manager.

If you
                                 		  want to route emergency calls to onsite security instead of the PSAP, see Set Up ERLs for Non-PSAP Deployment for the Route and Translation Pattern and ELIN settings.

The
                                 		  following table describes the Add New ERL and ERL Information pages.

Field

Description

Notes

ERL Name

The name of the ERL. The naming strategy you use is critical.
                                             					 The ERL name is one of the primary pieces of information your security team
                                             					 sees when alerted to an emergency call. If the name is easy to understand and
                                             					 descriptive, it can help your team respond quickly to a call.

For example, if you are creating an ERL for each floor in a
                                             					 three story building called Building J, your ERL names might be BldgJ-Floor1,
                                             					 BldgJ-Floor2, BldgJ-Floor3.

Work with your security team to develop an ERL naming strategy.

You cannot change the name of an existing ERL. To change an ERL
                                             					 name, create a new ERL, then delete the old ERL.

Any leading and trailing spaces are trimmed.

Description

Enter a description of the new ERL (optional).

Test ERL (Used for Synthetic Testing)

Check this check box if this ERL is used for testing.

See Set Up Test ERLs .

This setting is not available on the ERL Information for
                                             					 Default; default ERLs may not be used as test ERLs.

The combination of a route pattern and a phone number that
                                             					 jointly route the emergency call to the PSAP and provide the PSAP with a
                                             					 callback number if the PSAP needs to call the emergency caller after
                                             					 disconnecting the call.

Each ERL must have unique ELINs. The number of ELINs that you
                                             					 define determines how many callbacks you can support. ELINs are used in order
                                             					 as emergency calls are made, and recycled as needed. For example, if you define
                                             					 two ELINs for an ERL, and three emergency calls are made, the PSAP cannot
                                             					 recontact the first emergency caller.

However, concurrent emergency calls are not limited by the
                                             					 number of ELINs: you could have ten active emergency calls even if you only
                                             					 have two ELINs. The number of ELINs only controls PSAP callback capability.

Emergency
                                                         						Responder restricts the association of an ELIN with an ERL if the ELIN has been
                                                         						configured as a DID Number for an Off-Premises Emergency Responder user.
                                                         						Emergency Responder does not impose this restriction if the DID Number belongs
                                                         						to a user who has never associated an off-premises location in Emergency
                                                         						Responder.

Route/Translation Pattern

The phone number, defined as a route pattern in Cisco Unified Communications Manager, that is configured to use the gateway
                                             that the call should be routed through to get to the correct PSAP. This number must include the external emergency number,
                                             such as 911 in the USA. For example, 10.911 or 10911. The pattern can only contain numbers and dots.

ELIN Number

The unique phone number which the PSAP can use to locate a
                                             					 caller an emergency caller if the call is hung up. This number must be a DID
                                             					 (direct inward dial) number provided by your service provider; that is, it must
                                             					 be routeable on the PSTN. Enter the entire number, including area code, for the
                                             					 North American Numbering Plan, such as 4085551212, or an E.164 Number including
                                             					 country code such as +14085551212. The number can only contain numbers, a plus
                                             					 sign (+), single hyphens, dots, or parentheses.

The National E911 Service Provider ERL allows maximum of 10 characters and the data type should only be numbers.

An ELIN when being sent as ANI to PSAP through outgoing
                                             					 Gateway must be a DID (direct inward dial) number provided by your service
                                             					 provider.

If an ELIN number has a numerical sign "+" , then add a "." between the "+" sign and the number in Cisco Unified Communications Manager ,PSAP Call Back translation pattern. The '+' can be
                                             					 removed using discard digit "Predot" .

For example, if E.164 number includes a country code such as
                                             					 +14085551212, then in the Cisco Unified Communications Manager ,PSAP Call Back translation pattern you should enter
                                             					 '\+.XXXXXXXXXX X ' , not '\+1.XXXXXXXXXX'. The 913 pattern should be 913
                                             					 followed by 11X instead of 10X.

Add button

To add a route point and ELIN combination, enter the information
                                             					 and click Add .

Update button

To change an existing combination, select it in the list, change
                                             					 the information in the edit boxes, and click Update .

Remove button

To remove a combination, select it in the list and click Remove .

Available
                                             					 Onsite Alert IDs

Text box that displays the IDs of all available onsite alert personnel.

The onsite alert IDs list displays in a numerical order.

You must
                                             					 first add the contact to the list of onsite alert personnel.

Add button

Select the onsite alert (security) contacts to be assigned to
                                             					 the ERL. These contacts are notified when an emergency call is made from the
                                             					 ERL. To add a contact, select an Onsite Alert ID from the Available Onsite
                                             					 Alert IDs list and click Add .
                                             					 The contact's ID then appears in the Onsite Alert IDs for the ERL text box.

Remove button

To remove a contact for the ERL, select the appropriate ID in
                                             					 the Onsite Alert IDs for the ERL text box and click Remove .

ALI Details button

Click ALI
                                                						Details to view or change the automatic location information (ALI) of an
                                             					 ERL. The ALI provides detailed information about the location of the ERL, such
                                             					 as street address and phone number.

Time Zone

Select a time zone for the ERL. The time zone provides the list of all available time zones.

When you dial 911, the selected time zone is set as the local call time in Pager and Emergency alert. If a time zone is not
                                             selected, then the local call time is same as the system call time.

Insert button

Click Insert to save your changes to the new ERL.

The Insert button is only available when creating a new ERL.

Cancel Changes button

Click Cancel
                                                						Changes to change the fields on this page back to the last saved
                                             					 settings.

Update button

Click Update to save your changes to the ERL.

The Update button is only available when changing an existing
                                             					 ERL.

Close button

Click Close to close the window. You must click Update or Insert to save your changes before you click Close .

### ALI
                           	 Information

On the ALI
                                                				Information ( for ERL Name) page, the ERL Name variable is replaced with the
                                             			 appropriate ERL name. For example, if you click on ALI Details on the ERL
                                             			 Information for Default page, the page that appears is titled ALI
                                                				Information for Default . If the ERL name is First Floor, the page that
                                             			 appears is titled ALI
                                                				Information for First Floor .

The ALI
                                 		  Information (for ERL Name) page appears when you do one of these:

Click Add/Edit ALI in the ERL Address section on the Add New ERL page.

The Add New
                                                   				  ERL page appears when you choose Add New
                                                      					 ERL on the Find ERL Data page (opened when you choose ERL >
                                                      					 Conventional ERL ).

Click Add/Edit ALI on the ERL Information for ERL Name page. The ERL Information
                                       				for ERL Name page appears when you click on an existing ERL name or on Configure
                                          				  Default ERL on the Find ERL Data page (opened when you choose ERL >
                                          				  Details ).

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the
                                 		  Enter ALI Information page to enter the automatic location information (ALI)
                                 		  for an emergency response location (ERL). Send this information to your service
                                 		  provider, who will ensure it gets into the required database so that calls from
                                 		  your ELINs are routed to the local PSAP and public safety answering points
                                 		  (PSAPs) can locate an emergency caller.

The data
                                 		  requirements for these fields might differ from service provider to service
                                 		  provider. Contact your service provider to determine their requirements. The
                                 		  descriptions of the fields in are based on the National Emergency Number
                                 		  Association (NENA) Version 2 standards (USA).

Caution

The quality of
                                             			 the information you enter here is critical. This information is displayed to
                                             			 emergency call operators and to your local response team. They use this
                                             			 information to locate emergency callers. If the data is incorrect or difficult
                                             			 to understand, emergency response can be delayed, which might result in
                                             			 casualties that could have been prevented.

Field

Description

Notes

Select a Tag

Select the tag whose associated ALI data you want to load into
                                             					 the window. You can then edit the information for this specific ALI.

You can simplify the entry of ALI data by setting up tags in a
                                             					 file called validate.txt. This page explains where to place the file, and where
                                             					 to find the samplevalidate.txt file, which explains the format of the file.

When you create a tag, you enter information that is common
                                             					 between several ALIs, such as company name, city, state, and so forth. For
                                             					 example, if you have a 25-story building, and you are creating an ERL for each
                                             					 floor, you could create a tag called "25story." Then, instead of retyping the information for the
                                             					 building 25 times, you select a tag and the ALI data is loaded with the data
                                             					 you defined for the tag.

Field

Description

Value Type

(A =
                                             					 Alphabets, N = Numeric, S = Special Characters [# @ & * ( ) - _ + , . : ; "
                                             					 ' /] )

House
                                             					 Number

The
                                             					 number from the postal street address for the building. Example: 170 in 170
                                             					 West Tasman Dr.

AN, dash
                                             					 "-", and @ sign "@"

The
                                             					 number can be up to 10 characters, but your service provider might only support
                                             					 8 character numbers.

House
                                             					 Number Suffix

The number extension (such as /2) for the house number, if any.

ANS

Street Name

The street name from the postal address for the building.

ANS

You are
                                             					 limited to 60 characters.

Prefix
                                             					 Directional

The
                                             					 type of street. Select the type from the drop-down list, and the field is
                                             					 filled with one of the abbreviations accepted by the U.S. Postal Service
                                             					 Publication 28, for example, AVE for Avenue.

N

S

E

W

NE

NW

SE

SW

Street
                                             					 Suffix

The
                                             					 type of street. Select the type from the drop-down list, and the field is
                                             					 filled with one of the abbreviations accepted by the U.S. Postal Service
                                             					 Publication 28, for example, AVE for Avenue.

A

You can
                                             					 also type in the suffix. You are limited to 4 characters.

Post
                                             					 Directional

A
                                             					 trailing directional indicator if the street name contains one, for example, N
                                             					 for North.

N

S

E

W

NE

NW

SE

SW

Community Name

The
                                             					 community name for the address, for example, a city, town, or district name.

ANS

You are
                                             					 limited to 32 characters.

State

The
                                             					 2-digit state abbreviation.

A

You are
                                             					 limited to 2 characters.

Main
                                             					 NPA

The
                                             					 3-digit area code of the main number associated with the ERL.

N

Main
                                             					 Telephone No.

The
                                             					 main phone number associated with the ERL. This might be the number of the
                                             					 security office for the ERL.

N

Class
                                             					 of Service

Select
                                             					 the class of service for the ERL.

If you
                                             					 do not know your class of service, ask your service provider.

Type of
                                             					 Service

Select
                                             					 the type of service for the ERL.

If you
                                             					 do not know your class of service, ask your service provider.

Exchange

The
                                             					 Local Exchange Carrier (LEC) exchange identifier for the serving telephone
                                             					 office for the phone.

ANS

You are
                                             					 limited to 4 characters. Ask your service provider for this identifier

Customer Name

The
                                             					 subscriber name associated with the ERL, and typically your company name.

ANS

You are
                                             					 limited to 32 characters.

Order
                                             					 Number

The
                                             					 service order number of the activity of establishing or updating this record.

ANS

You are
                                             					 limited to 10 characters. Work with your service provider to determine a valid
                                             					 order number, if one is needed.

Extract
                                             					 Date

The
                                             					 date on which the record was created.

Date
                                             					 [mmddyy]

County
                                             					 ID

The
                                             					 county identification code for the zone. In the USA, use the FIPS code assigned
                                             					 to the county by the U.S. Census Bureau.

AN

You are
                                             					 limited to 4 characters.

Zip
                                             					 Code

The
                                             					 postal zip code for the address.

AN,
                                             					 hyphen "-"

Indicates a U.S. zip code on a U.S. service order record or a Canadian postal
                                             					 code on a Canadian service order record. U.S. Format: NNNNN or NNNNN-NNNN;
                                             					 Canadian Format: ANANAN or ANA[space] NAN

Zip
                                             					 Code Extension

The
                                             					 postal zip code "plus four" number.

AN,
                                             					 hyphen "-"

You are
                                             					 limited to 4 digits.

Customer Code

Your
                                             					 customer code. Ask your service provider if you do not know your code.

ANS

You are
                                             					 limited to 3 characters.

If you
                                             					 change this field, Emergency Responder generates two records: a Delete record
                                             					 to remove the ALI with the old code, and an Insert record to add the ALI with
                                             					 the new code. This Delete and Insert sequence is only generated the next time
                                             					 you export ALI: you must ensure that you submit this export file to the service
                                             					 provider.

Comments

Optional comments. These commentsmight be displayed at the PSAP if an emergency
                                             					 call is made from this ERL.

You are
                                             					 limited to 30 characters.

Longitude

The
                                             					 longitude of the ERL.

N, dot
                                             					 ".", plus "+", minus "-"

You are
                                             					 limited to 9 digits.

Latitude

The
                                             					 latitude of the ERL.

N, dot
                                             					 ".", plus "+", minus "-"

You are
                                             					 limited to 9 digits.

Elevation

The
                                             					 elevation of the ERL.

AN dot
                                             					 ".", plus "+",minus "-"

You are
                                             					 limited to 5 digits.

TAR
                                             					 Code

The
                                             					 taxing area rate code.

ANS

You are
                                             					 limited to 6 characters.

Location

Additional location information, in free form, to help identify the exact
                                             					 location of the phone.

This
                                             					 information is displayed to your security personnel along with the ERL name
                                             					 when an emergency call is made, so use this field to help locate the caller.
                                             					 For example, you might repeat the street address that is defined in several
                                             					 separate fields elsewhere on this page.

ANS

You are
                                             					 limited to 60 characters.

Reserved

Information your service provider might require to create a valid ALI file.

AN

Ask
                                             					 your service provider if you must

enter
                                             					 anything in the reserved area.

Be
                                             					 aware that NENA and CSV requirements may be different. For example, ERL Import
                                             					 does not require that you enter anything in the Reserved field. You can give an
                                             					 empty string in each of the ERL records and Emergency Responder accepts this
                                             					 file for importing. However, you must not delete the field itself from the
                                             					 file. The field must be there in the record; it can be an empty string
                                             					 delimited with a comma.

### Export ERL
                           	 Data

The Export
                                 		  ERL Data page appears when you click the Export link on the Find ERL Data page (opened when you choose ERL >
                                    			 Conventional ERL ).

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the
                                 		  Export ERL Data page to create ERL export files for your own use only; do not
                                 		  submit ERL export files to your service provider. For example, use an ERL
                                 		  export file to back up your configuration or to move it to another Emergency
                                 		  Responder server.

To create
                                 		  a file to send to your service provider to update their ALI data, see Export PS-ALI Records .

The
                                 		  following table describes the Export ERL Data page.

Field

Description

Select Export Format

The file format to be used in the export file. For ERL data,
                                             					 either csv (comma-separated value) or XML.

Enter Export File Name

The name of the file you want to create. Do not include a file
                                             					 extension.

Export button

Click Export to create the export file.

Close button

Click Close to close the window.

### Import ERL
                           	 Data

The Import
                                 		  ERL Data page appears when you click the Import link on the Find ERL Data page (opened when you choose ERL >
                                    			 Conventional ERL ).

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the
                                 		  Import ERL Data page to create or update many ERLs at once from a file in which
                                 		  you have defined the ERL data. Create this file using a spreadsheet that can
                                 		  save the information in one of the required formats (CSV or XML). View the
                                 		  samples from this page before attempting to create an import file.

If you must update many ERLs, you can export the ERL data, update the export file, and reimport the file.

You can
                                 		  also use the Upload utility to upload a file containing ERL data from your
                                 		  local system; you can then import the ERL data. See Upload File for more information.

The
                                 		  following table describes the Import ERL Data page.

Field

Description

Select Import Format

Select the format used in the file you are importing.

After you select the format, click View
                                                						sample file to see an example of the expected format and sequence of
                                             					 values. Use this sample information to create your import file in a
                                             					 spreadsheet.

Select File to Import

Select the file from which you want to import ERL data.

Upload button

Click Upload to upload a file from your local system. See Upload File for more information.

Import button

Click Import to add ERL data from the import file to the Emergency Responder database.

The
                                                         						imported ERL data overwrites conflicting data in the Emergency Responder
                                                         						database.

Close button

Click Close to close the window.

## Off-Premises
                        	 ERL

The Find
                              		  Off-Premises ERL Data page appears when you choose ERL >
                                 			 Off-Premise ERL > Search And List .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the
                              		  Off-Premise ERL Data page to define the emergency response locations (ERLs) for
                              		  individuals with phones that are located outside of the corporate network.

The
                              		  following table describes the Find and List Off-Premise ERLs page.

Field

Description

Notes

Find Off-Premises ERL where...

Select search criteria and click Find to list existing Off-Premise ERLs.
                                          					 To list all ERLs, click Find without entering any criteria. From the drop-down list, you can select the
                                          					 number of records that display per page for each search.

From the search results list, you can:

Click an entry to view and update its characteristics.

Click the Copy icon to create a new ERL with the same ALI data.

Click the Delete icon to remove the ERL.

Click view... in the Audit Trail column to view a history of changes made to that ERL. See ERL Audit Trail for more information.

When copying an ERL, information that must be unique in an ERL
                                          					 is not copied.

Add New ERL

Click Add New
                                             						ERL to create a new ERL.

### Add New ERL

The Add New ERL (Off-Premise phones) page appears when you choose Add New ERL on the Find National E911 Service Provider ERL Data page (opened when you choose ERL > Off-Premise ERL > Search and List ).

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the
                                 		  Add New ERL page to create a new emergency response location (ERL) for
                                 		  Off-Premise phones. Alternatively, you can create or update many ERLs at once
                                 		  by importing predefined ERL information from a separate file.

Use the
                                 		  Find ERL Data page to view or update an existing ERL.

The
                                 		  following table describes the Add New ERL (Off-Premise Phones) page.

Field

Description

ERL Name

The name of the ERL. The naming strategy you use is critical.
                                             					 The ERL name is one of the primary pieces of information your security team
                                             					 sees when alerted to an emergency call. If the name is easy to understand and
                                             					 very descriptive, it can help your team respond quickly to a call.

Work with your security team to develop an ERL naming strategy.

You cannot change the name of an existing ERL. To change an ERL
                                             					 name, create a new ERL, then delete the old ERL.

Any leading and trailing spaces is trimmed.

Description

Enter a description of the new ERL (optional).

Route/Translation Pattern

The phone number, defined as a route pattern in Cisco Unified Communications Manager, that is configured to use the gateway
                                             the call should be routed through to get to the correct PSAP. This number must include the external emergency number, such
                                             as 911 in the USA. For example, 10.911 or 10911. The pattern can only contain numbers and dots.

Add button

To
                                             					 add a route point, choose a route point from the drop-down list and click Add .

Remove button

To
                                             					 remove a combination, select it in the list and click Remove .

Available Onsite Alert IDs

Text box that displays the IDs of all available onsite alert
                                             					 personnel.

You must first add the contact to the list of onsite alert
                                             					 personnel.

Add button

Select the onsite alert (security) contacts to be assigned to
                                             					 the ERL. These contacts are notified when an emergency call is made from the
                                             					 ERL. To add a contact, select an Onsite Alert ID from the Available Onsite
                                             					 Alert IDs list and click Add .
                                             					 The contact ID then appears in the Onsite Alert IDs for the ERL text box.

Remove button

To
                                             					 remove a contact for the ERL, select the appropriate ID in the Onsite Alert IDs
                                             					 for the ERL text box and click Remove .

ERL Address

ALI Details button

Click ALI Details to view or change the automatic location information (ALI) of an ERL. The ALI provides detailed information
                                             about the location of the ERL, such as street address and phone number.

Time Zone

Select a time zone for the ERL. The time zone provides the list of all available time zones.

When you dial 911, the selected time zone is set as the local call time in Pager and Emergency alert. If a time zone is not
                                             selected, then the local call time is same as the system call time.

Insert button

Click Insert to save your changes to the new ERL.

The Insert button is only available when creating a new ERL.

Cancel Changes button

Click Cancel
                                                						Changes to change the fields on this page back to the last saved
                                             					 settings.

Update button

Click Update to save your changes to the ERL.

The Update button is only available when changing an existing
                                             					 ERL.

Close button

Click Close to close the window. You must click Update or Insert to save your changes before you click Close .

## Off-Premise ERL -
                        	 Secondary Status

The
                              		  Secondary Status page appears when you choose ERL >
                                 			 Off-Premise ERL > Secondary Status .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the Secondary Status page to query the National E911 Service Provider Secondary Status database for information about off-premise telephone number record update transactions that were flagged
                              with errors. These records may include the following:

Corrected records that are now in the National E911 Service Provider database.

Error records
                                    				that are referred back to customers for correction.

Deleted error records from the National E911 Service Provider database.

You can query the National E911 Service Provider Secondary status database for off-premise telephone number records with errors.

The
                              		  following table describes the Secondary Status for Off-Premise phones.

Field

Description

Find DIDs where...

Select search criteria and click Find to list the result of a query on the National E911 Service Provider secondary status server.

## Find National E911 Service Provider ERL

The Find National E911 Service Provider ERL page appears when you choose ERL > National E911 Service Provider ERL > National E911 Service Provider ERL (Search and List) .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

When you use National E911 Service Provider V91-1-1 services, you can use the National E911 Service Provider ERL Data page to define the emergency response locations (ERLs) for your company.

The following table describes the Find and List National E911 Service Provider ERLs page.

Field

Description

Notes

Find National E911 Service Provider ERL where...

Select search criteria and click Find to list existing National E911 Service Provider ERLs. To list all ERLs, click Find without entering any criteria. From the drop-down list, you can select the number of records that display per page for each
                                          search.

From the search results list, you can:

Click an entry to view and update its characteristics.

Click the Copy icon to create a new ERL with the same ALI data.

Click the Delete icon to remove the ERL.

Click view... in the Audit Trail column to view a history of changes made to that ERL. See ERL Audit Trail for more information.

When copying an ERL, information that must be unique in an ERL
                                          					 is not copied.

See Add New ERL for more information.

Add New ERL

Click Add New
                                             						ERL to create a new ERL.

See Add New ERL for more information.

Level of service button

Click Level of service to display the level of service that National E911 Service Provider designates for the specific address that is configured in the ALI details. National E911 Service Provider supports the following level of service:

No Coverage— National E911 Service Provider does not have access to the selective router and cannot provide the callback number and address to the PSAP that services
                                                that address.

Basic—The PSAP that provides service currently can not provide emergency support for wire line services or VoIP service providers.

Enhanced—Calls can be routed to the PSAP with the existing E9-1-1 selective router network, and National E911 Service Provider can provide the callback number and address to the PSAP.

Bulk TN Update button

Select multiple ERLs and click Bulk TN
                                             						Update to update the ELIN for the selected ERL.

Export

Click the Export link to create a file containing your ERL configuration.

See Export ERL Data for information about exporting ERL
                                          					 data.

Import

Click the Import link to create or update ERLs using information stored in a
                                          					 separate file. By importing ERL data, you can create or update many ERLs at one
                                          					 time.

See Import ERL Data for information about importing
                                          					 ERL data.

## Default ALI
                        	 Values

The Default ALI Values page appears when you choose ERL > National E911 Service Provider ERL > Default ALI Values .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the Default ALI Values page to set the default values that automatically populate the respective ALI fields when a new National E911 Service Provider ERL is created.

The
                              		  following table describes the Default ALI Information page.

Field

Description

Type of Service

Defines the type of service for the calling party number, such
                                          					 as FX in 911 area or Non-Pub.

National E911 Service Provider recommends setting the default to Non-Pub.

Class of Service

Defines the class of service for the calling party number, such
                                          					 as residential, business, VoIP.

National E911 Service Provider recommends setting the default to VoIP.

Company ID

Specified by National E911 Service Provider .

Customer Name

Specified by National E911 Service Provider .

Update button

Click Update to save your changes.

Cancel Changes button

Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings.

## National E911 Service Provider ERL - Secondary Status

The Secondary Status page appears when you choose ERL > National E911 Service Provider ERL > Secondary Status .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the Secondary Status page to query the National E911 Service Provider Secondary Status database for information about telephone number record update transactions that were previously flagged
                              with errors. These records may include the following:

Corrected records that are now in the National E911 Service Provider database.

Error records that are referred to customers for correction.

Deleted error records from the National E911 Service Provider database.

You can query the National E911 Service Provider Secondary status database for telephone number records with errors that have been corrected.

Query in Secondary Status is not supported with RedSky.

The following table describes the Secondary Status for phones that are serviced by National E911 Service Provider .

Field

Description

Find ELINS where...

Select search criteria and click Find to list the result of a query on the National E911 Service Provider secondary status server.

## National E911 Service Provider Schedule

The National E911 Service Provider Schedule page appears when you choose ERL > National E911 Service Provider ERL > National E911 Service Provider Schedule .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the National E911 Service Provider Schedule page to specify the day of the week and time when ALI update requests and secondary status update requests are sent
                              to National E911 Service Provider . ALI update requests sends newly created TN records to National E911 Service Provider . Secondary Status update requests sends queries to National E911 Service Provider requesting information about records with errors that have been corrected.

The following table describes the National E911 Service Provider Schedule page.

Field

Description

Notes

Add new
                                          					 schedule

Specify the day of the week and time of the day when you want to
                                          					 schedule an update:

Select
                                                						  the days of the week when you want to run the switch port and phone update
                                                						  process.

Select
                                                						  the time of day when you want the process to run. 00 hour and 00 min is
                                                						  midnight. Time is based on the 24-hour clock.

Check
                                                						  the Enable Schedule check box if you
                                                						  want to activate this schedule.

Choose
                                                						  either ALI Update Schedule or Secondary Status Update Schedule .

We recommend that you run the National E911 Service Provider update process at least once per day. Because of the added network traffic, it is best to run the process outside normal
                                          business hours.

Add button

Click Add to
                                          					 add the schedule to the list of schedules.

Cancel Changes button

Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings.

Update button

Click Update when viewing an existing schedule to save changes you make to the schedule.

Only available when viewing an existing schedule.

## View ALI
                        	 Discrepancies

The View ALI Discrepancies page appears when you choose ERL > National E911 Service Provider ERL > View ALI Discrepancies .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the View ALI Discrepancies page to view discrepancies in the records between the ALI data that is stored in the local
                              Emergency Responder database and the ALI data for this ELIN in the National E911 Service Provider database.

View ALI Discrepancies is not supported with RedSky.

The
                              		  following table describes the Find ALI Discrepancies page.

Field

Description

Find ELIN where...

Enter search criteria to select the ELIN that you want to find.

To find all ELIN, click Find without entering any criteria.

To narrow your search, select the field that you want to search
                                          					 on from the drop-down list, select the search relationship (is contains, begins
                                          					 with, and so on), and enter the search string. Click Find .

### View ALI
                           	 Discrepancies for a Specific ELIN

Choose ERL > National E911 Service Provider ERL > View ALI Discrepancies and search for discrepancies. The View ALI Discrepancies for a specific ELIN page appears when you select a specific ELIN
                                 from the results.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the View ALI Discrepancies for a Specific ELIN page to view discrepancies in the records between the ALI data that is
                                 stored in the local Emergency Responder database and the ALI data for this ELIN in the National E911 Service Provider database.

The
                                 		  following table describes the Find ALI Discrepancies for a specific ELIN page.

Field

Description

ALI Fields

List of ALI field information from the local Emergency Responder database and from National E911 Service Provider database:

House Number

House Suffix

Street Name

Prefix Directional

Street Suffix

Post Directional

Community Name

State

Main NPA

Class of Service

Type of Service

Exchange

Customer Name

Order Number

Extract Date

County ID

Company ID

Zip Code

Zip Code Extension

Customer Code

Comments

Longitude

Latitude

Elevation

TAR Code

Location

Reserved

Save button

Click Save to save your changes in the local Emergency Responder database.

Save National E911 Service Provider ALI Info button

Click Save National E911 Service Provider ALI Info to update the National E911 Service Provider VUI database.

Cancel Changes button

Click Cancel
                                                						Changes to change the fields on this page back to the last saved
                                             					 settings.

Close button

Click Close to close the window.

## ERL Migration
                        	 Tool

The ERL
                              		  Migration Tool page appears when you choose ERL > ERL
                                 			 Migration Tool .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the ERL Migration Tool page to migrate ERLs from conventional ERL data to National E911 Service Provider ERL data and vice versa.

The
                              		  following table describes the ERL Migration Tool page.

Field

Description

Displays status messages

Find

Select search criteria and click Find to list either existing Conventional ERLs or National E911 Service Provider ERLs.

From the search results list, you can select the ERLs that you
                                          					 want to migrate

Migrate to National E911 Service Provider ERL Button

When you search for Conventional ERLs, you can select the ERLs that you want to migrate to National E911 Service Provider .

When you click the Migrate to National E911 Service Provider ERL button, you can select an National E911 Service Provider route point for all the selected ERL.

Migrate to Regular ERL

When you search for National E911 Service Provider ERLs, you can select the ERLs that you want to migrate to a conventional ERL data.

When you click the Migrate to Regular ERL button, you can
                                          					 enter a route point, and specify whether the ERL is a test ERL and test the
                                          					 ERL.

## SNMP Settings

The SNMP Settings page appears when you choose Phone Tracking > SNMPv2 Settings or Phone Tracking > SNMPv3 Settings .

### Authorization Requirements

You must have system administrator or network administrator
                              		  authority to access this page.

### Description

Use the SNMPv2 Settings page or  the SNMPv3 Settings page  to define the SNMP read
                              		  community string used by your switches.

### SNMP v2 Settings
                           	 Page

Use the
                                 		  information in the following table to configure the SNMPv2 Settings.

Field

Description

Notes

IP Address/Host Name

The IP address or hostname of a switch whose SNMP read community
                                             					 string you are defining.

If you use the same read community string for all switches, you
                                             					 only need to define one entry: *.*.*.*.

If you use different read community strings for sets of
                                             					 switches, you can define each set, using variables and ranges. For example, if
                                             					 you have 10 switches from 10.1.115.0 to 10.1.125.0, you can use 10.1.115-125.0
                                             					 as the IP address. You can also mix ranges and variables, such as
                                             					 *.*.115-125.*.

You are not defining your switches on this page, you are only
                                             					 associating IP address patterns to read community strings.

Emergency Responder only tries to use the string with the
                                             					 specific switches you identify on the LAN Switch Details page. See LAN Switch Details for more information.

If two or more patterns match an IP address, Emergency Responder
                                             					 uses the SNMP string associated with the most closely matching pattern.

Timeout

The time, in seconds, in which Emergency Responder should
                                             					 consider an attempted SNMP connection to a switch to have failed. See the
                                             					 explanation of Retries for more information.

Default is 10 seconds. The optimal value is 10 to 15 seconds.

Maximum Retry Attempts

The number of times Emergency Responder should attempt to
                                             					 contact a switch.

With each retry, the previous timeout is multiplied by 2, to
                                             					 ensure that the switch has enough time to respond. For example, if you specify
                                             					 10 for timeout, the first attempt times out in 10 seconds, the second attempt
                                             					 times out in 20 seconds, the third attempt times out in 40 seconds, and so
                                             					 forth.

Default is 2 retries. This number does not include the initial
                                             					 attempt; that is, if retries are 2, Emergency Responder attempts to contact a
                                             					 switch up to 3 times (the initial attempt plus 2 retries).

The optimal value is 2 to 3 retries.

Read Community

The SNMPv2 read community string for the switch. The name can contain up to 50 characters and can contain any combination of alphanumeric characters, hyphens (-), and underscore
                                                characters (_).

Community string does not support special characters like angle brackets (< >), backslash (\), colon (:), quotation marks
                                                         (“ “), and tilde (~).

Default is public for any IP address not covered in the SNMPv2
                                             					 settings list.

Insert

Click the Insert button to add the entry to the
                                             					 list of SNMP settings.

Cancel Changes

Click the Cancel Changes button to change the
                                             					 fields on this page back to the last saved settings.

A list of SNMPv2 settings that you have already defined.

To change an entry, click any of the links associated with the
                                             					 entry to load the details into the edit boxes at the top of the page. Then make
                                             					 your changes and click Update .

To delete an entry, click the Delete icon for the entry.

Add New

Click the Add New button to add another SNMPv2
                                             					 setting.

Update

Click the Update button to save changes you make
                                             					 to an existing SNMPv2 setting.

Only available when viewing an existing setting.

Export

Click the Export button to export the SNMPv2 data
                                             					 settings to another file. For more information, see Export SNMPv2 Data .

Import

Click the Import button to import the SNMPv2 data
                                             					 settings to your Cisco Emergency Responder configuration. For
                                             					 more information, see Import SNMPv2 Data .

#### Export SNMPv2
                              	 Data

The Export
                                    		  SNMPv2 Data window appears when you click Export on the SNMPv2
                                    		  Settings page (opened when you choose Phone
                                       			 Tracking > SNMPv2 Settings ).

##### Authorization
                                    		  Requirements

You must have the
                                    		  system administrator or ERL administrator authority to access this window.

##### Description

Create a file
                                             				containing the Emergency Responder Export SNMPv2 Data.

Use the Download option to download a file containing the
                                             				Emergency Responder Export SNMPv2 Data. For more information, see Download File .

The following
                                    		  table describes the fields found on the Export
                                       			 SNMPv2 Data window.

Field

Description

Select
                                                					 Export Format

Select
                                                					 the file format from the drop-down list that matches the file being imported.

Enter
                                                					 Export File Name

Enter the
                                                					 name of the file that you want to create. Do not include the file extension.

Export

Click the Export button to add data from the import file to
                                                					 your Cisco Emergency Responder configuration.

Close

Click the Close button to close the window.

This text box displays status information.

Select a
                                                					 File to Download

Select a
                                                					 file from the drop-down list and click the Download button to download the file to your
                                                					 machine.

#### Import SNMPv2
                              	 Data

The Import
                                    		  SNMPv2 Data window appears when you click Import on the SNMPv2
                                    		  Settings page (opened when you choose Phone
                                       			 Tracking > SNMPv2 Settings ).

##### Authorization
                                    		  Requirements

You must have the
                                    		  system administrator or ERL administrator authority to access this window.

##### Description

Use the Import
                                       			 SNMPv2 Data window to create or update several SNMPv2 settings
                                    		  details at once from the file in which you have defined their data. You can
                                    		  create this file using a spreadsheet and save the information in the required
                                    		  formats. The View
                                       			 sample file link provides the sample information to create or
                                    		  update your import file.

You can import a
                                    		  previously exported file or you can upload a file that you created on your
                                    		  local system using the Upload option. For more information, see Upload File .

The following
                                    		  table describes the fields found on the Import
                                       			 SNMPv2 Data window.

Field

Description

Select
                                                					 Import Format

Select
                                                					 the file format from the drop-down list that matches the file being imported.

Click View sample file link to view an example of the
                                                					 expected format and sequence of values. Use this sample information to create
                                                					 your import file in a spreadsheet.

Select
                                                					 File to Import

Select
                                                					 the file from the drop-down list from which you want to import data.

Import

Click the Import button to add data from the import file to
                                                					 your Cisco Emergency Responder configuration.

Upload

Click the Upload button to upload the file from your machine.
                                                					 For more information, see Upload File .

Close

Click the Close button to close the window.

This text box displays status information.

### SNMP v3 Settings
                           	 Page

Use the
                                 		  information in the following table to configure the SNMP v3 Settings.

Field

Description

Notes

User Information

IP
                                             					 Address/Host Name

Enter the
                                             					 IP address or hostname of the Cisco Unified Communications Manager or LAN
                                             					 switch.

For IPv6 address, wildcard characters are not supported.

You can
                                             					 also use a range of number for octets, such as 15 to 30.

User Name

Enter the
                                             					 username configured on Cisco Unified Communications Manager or LAN switch.

The name
                                             					 can contain up to 32 characters and can contain any combination of alphanumeric
                                             					 characters, hyphens (-), and underscore characters (_).

Authentication
                                                						Information

Password

To enable
                                             					 authentication, check the Authentication Required check box; in the Password
                                             					 and the Reenter Password fields, enter the password for the user configured on
                                             					 the Cisco Unified Communications Manager or LAN switch.

Protocol

Choose
                                             					 the appropriate protocol as configured for the user on Cisco Unified
                                             					 Communications Manager or LAN switch.

Privacy Information

Password

If you
                                             					 selected the Authentication Required check box, you can specify the privacy
                                             					 information.

To require
                                             					 privacy, select the check box, enter the password in both the Password, and the
                                             					 Reenter Password fields for the user configured on the Cisco Unified
                                             					 Communications Manager or LAN switch.

Protocol

Choose the
                                             					 appropriate protocol as configured for the user on Cisco Unified Communications
                                             					 Manager or LAN switch.

Other Information

Timeout
                                             					 (in seconds)

The length
                                             					 of time that an attempted SNMP connection remains idle before it is considered
                                             					 to have failed.

For more
                                             					 information, see the explanation for Maximum Retry Attempts.

The
                                             					 default value is 10 seconds. The optimal value is 10 to 15 seconds.

Maximum
                                             					 Retry Attempts

The number
                                             					 of times Emergency Responder attempts to contact a Cisco Unified Communications
                                             					 Manager or a switch.

With each
                                             					 retry, the previous timeout is multiplied by two to ensure that the switch has
                                             					 time to respond. For example, if you specify a Timeout value of 10 seconds, the
                                             					 first attempt times out in 10 seconds, the second attempt times out in 20
                                             					 seconds, and the third attempt times out in 40 seconds.

The
                                             					 default value is two. But the optimal value is two to three retries.

The
                                             					 Maximum Retry Attempts does not include the initial attempt. For example, if
                                             					 Maximum Retry Attempts is set to two, Emergency Responder attempts to contact a
                                             					 switch three times - the initial attempt plus two retries.

Insert

Click the Insert button to add the entry to the
                                             					 list of SNMP settings.

Cancel Changes

Click the Cancel Changes button to change the
                                             					 fields on this page back to the last saved settings.

A list of SNMPv3 settings that you have already
                                             					 defined.

To change an entry, click any of the links
                                             					 associated with the entry to load the details into the edit boxes at the top of
                                             					 the page. Then make your changes and click Update .

To delete an entry, click the Delete icon for the entry.

Add New

Click the Add New button to add another SNMPv3
                                             					 setting.

Update

Click the Update button to save changes you make
                                             					 to an existing SNMPv3 setting.

Only available when viewing an existing setting.

Import

Click the Import button to import the SNMPv3 data
                                             					 settings to your Cisco Emergency Responder configuration. For
                                             					 more information, see Import SNMPv3 Data .

#### Import SNMPv3
                              	 Data

The Import
                                    		  SNMPv3 Data window appears when you click Import on the SNMPv3
                                    		  Settings page (opened when you choose Phone
                                       			 Tracking > SNMPv3 Settings ).

##### Authorization
                                    		  Requirements

You must have the
                                    		  system administrator or ERL administrator authority to access this window.

##### Description

Use the Import
                                       			 SNMPv3 Data window to create or update several SNMPv3 settings
                                    		  details at once from the file in which you have defined their data. You can
                                    		  create this file using a spreadsheet and save the information in the required
                                    		  formats. The View
                                       			 sample file link provides the sample information to create or
                                    		  update your import file.

You can import a
                                    		  previously exported file or you can upload a file that you created on your
                                    		  local system using the Upload option. For more information, see Upload File .

The following
                                    		  table describes the fields found on the Import
                                       			 SNMPv3 Data window.

Field

Description

Select
                                                					 Import Format

Select
                                                					 the file format from the drop-down list that matches the file being imported.

Click View sample file link to view an example of the
                                                					 expected format and sequence of values. Use this sample information to create
                                                					 your import file in a spreadsheet.

Select
                                                					 File to Import

Select
                                                					 the file from the drop-down list from which you want to import data.

Import

Click the Import button to add data from the import file to
                                                					 your Cisco Emergency Responder configuration.

Upload

Click the Upload button to upload the file from your machine.
                                                					 For more information, see Upload File .

Close

Click the Close button to close the window.

This text box displays status information.

## Phone Tracking
                        	 Schedule

The Phone
                              		  Tracking Schedule page appears when you choose Phone Tracking
                                 			 > Schedule .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or network administrator authority to access this
                              		  page.

### Description

Use the
                              		  Phone Tracking Schedule page to define the CiscoEmergencyResponder (Emergency
                              		  Responder) schedule for updating phone and switch information from the network.
                              		  Emergency Responder updates network information using two processes:

Phone Tracking—A
                                    				periodic comparison of the phones registered with
                                    				CiscoUnifiedCommunicationsManager to the location information obtained from
                                    				the switches. If a phone moves, Emergency Responder updates the phone ERL.

Switch Port and
                                    				Phone Update—The phone tracking process plus a more extensive check of the
                                    				network switches, which can identify new or changed switch modules (additional
                                    				or removed ports). Ensure that your ERL administrator updates the ERL
                                    				assignment for new ports.

The
                              		  following table describes the Phone Tracking Schedule page.

Field

Description

Notes

Incremental Phone Tracking

Incremental Phone Tracking Interval

The time, in minutes, between making updates to the known phone
                                          					 locations. This periodic update ensures that phones that have moved are located
                                          					 and assigned to the correct ERL.

Click Update to save your changes to this field.

The default is 30 minutes.

The range of the interval that can be defined is 5 to 300
                                          					 minutes.

Enhanced Location Phone Tracking

The time, in minutes, between

making updates to the unknown phone locations. This periodic update ensures that devices that have moved are located and assigned
                                          to the correct ERL.

Click Update to save your changes to this field.

The default is 2 minutes.

The range of the interval that can be defined is 1 to 180 minutes.

By default, AXL Incremental Phone tracking should not be greater than Incremental Phone tracking.

Enter the schedule that you want to add:

Select
                                                						  the days of the week when you want to run the switch port and phone update
                                                						  process.

Select
                                                						  the time of day when you want the process to run. 00 hour and 00 min is
                                                						  midnight. Time is based on the 24-hour clock.

We recommend that you run the switch port and phone update
                                          					 process at least once per day. Because of the added network traffic, it is best
                                          					 to run the process outside normal business hours.

Insert button

Click Insert to add the schedule to the list of schedules.

Cancel Changes button

Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings.

Update button

Click Update when viewing an existing schedule to save changes that you make to the
                                          					 schedule.

Only available when viewing an existing schedule.

The list of schedules you have defined.

To change a schedule, click the Hour link, the Minute link, or
                                          					 the Edit icon to load it into the Modify Schedule area above the list. Then,
                                          					 make your changes and click Update .

To remove a schedule, click the Delete icon for the schedule.

If any schedules overlap, only one schedule is run.

Add New button

Click Add New to
                                          					 add another schedule.

## Cisco Unified
                        	 Communications Manager Clusters

The Cisco Unified Communications Manager Clusters page appears when you choose Phone Tracking > Cisco Unified Communications Manager .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or network administrator authority to access this
                              		  page.

### Description

Use the Cisco Unified Communications Manager Clusters page to identify the Cisco Unified Communications Manager clusters whose
                              emergency calls this Emergency Responder group handles. Only assign a Cisco Unified Communications Manager cluster to a single
                              Emergency Responder group. Emergency Responder gets the list of phones registered with these Cisco Unified Communications
                              Manager servers and tracks the movements of these phones.

The following table describes the Cisco Unified Communications Manager Clusters page.

Field

Description

Notes

Cisco Unified Communications Manager

The IP address or DNS name of a Cisco Unified Communications Manager server that is running Cisco Unified Communications Manager
                                          and SNMP services.

Only add one server per Cisco Unified Communications Manager cluster—Emergency Responder can identify the other servers in
                                          the cluster. The Cisco Unified Communications Manager server you specify represents the cluster in which it is a member.

When viewing a previously defined Cisco Unified Communications Manager server, Emergency Responder displays a CCM List link. Click CCM List to view a list of the Cisco Unified Communications Manager servers that belong to the same cluster as the selected server.

The Cisco Unified Communications Manager servers should have run the CCM service at least once.

After the IP address or DNS name has been configured, it cannot
                                          					 be modified.

CTI Manager

The IP address or DNS name of the CTI Manager used by the specified Cisco Unified Communications Manager server.

CTI Manager User Name

The name of the user created in the Cisco Unified Communications Manager server for Emergency Responder use.

This user must have specific characteristics and device
                                          					 assignments. See Create Emergency Responder Cisco Unified Communications Manager User for specific information.

CTI Manager Password

The password for the user.

Backup CTI Manager 1

The IP address or DNS name of the backup CTI Manager used by the specified Cisco Unified Communications Manager server.

Backup CTI Manager 2

The IP address or DNS name of the backup CTI Manager used by the specified Cisco Unified Communications Manager server.

Telephony Port Begin Address

The number of the first CTI port to use for calling onsite alert
                                          					 (security) personnel. When an emergency call is made, Emergency Responder calls
                                          					 the onsite alert personnel for the originating ERL using the telephony ports
                                          					 you configure here.

You must first create this port in Cisco Unified Communications Manager. See Create Required CTI Ports for more information.

Number of Telephony Ports

The number of CTI ports. Enter the number of CTI ports you created in Cisco Unified Communications Manager. The number of
                                          ports is the number of concurrent calls Emergency Responder can make to onsite alert personnel.

The ports used are in sequence from the beginning port. For
                                          					 example, if you enter 3000 for the begin port, and 4 for number of ports,
                                          					 Emergency Responder uses 3000, 3001, 3002, and 3003.

Enable Secure Connection check box

Check this check box to enable a secure connection. You can
                                          					 enter data in the other fields of this section only if you have enabled Secure
                                          					 Connection.

TFTP Server IP Address

The IP address of the TFTP server.

TFTP Server Port

The port of the TFTP server.

Backup TFTP Server IP Address

The IP address of the backup TFTP server, for the Unified CM
                                          					 node being added.

CAPF Server IP Address

The IP address of the CAPF server.

CAPF Server Port

The port of the CAPF server.

Instance ID for Publisher

The instance ID for the Publisher node.

Secure Authentication String for Publisher

The secure authentication string for the Publisher node.

Instance ID for Subscriber

The instance ID for the Subscriber node.

Secure Authentication String for Subscriber

The secure authentication string for the Subscriber node.

Enable SRTP for Audio Alerts

Check this check box if you want Emergency Responder to send Secure Real-Time Transport Protocol (SRTP) enabled Onsite Phone
                                          alert to Onsite Security Users during an Emergency Call. With this option enabled for each Unified Communication Manager cluster,
                                          the Emergency Responder Onsite personnel receive secured onsite audio alerts.

The default value for this check box leaves it unchecked.

The value of this field gets determined by the setting of the Unified Communications Manager service parameter Block Unencrypted Calls . This parameter specifies whether Unified Communications Manager allows calls from Emergency Responder without data encryption.

When the Block Unencrypted Calls parameter is set to TRUE, only calls with media encryption support are allowed and unencrypted calls are blocked. When the Block Unencrypted Calls parameter is set to FALSE, calls are allowed whether or not their media is encrypted.

AXL Username

The username for the application user on Cisco Unified
                                          					 Communications Manager with privileges to perform AXL queries.

The selected user in the Cisco Emergency Responder Location Management application server in Unified CM should match the user
                                                      in the Cisco Emergency Responder page: Phone Tracking > CUCM > AXL Username . Though, the Emergency Responder AXL username and CTI username have the required permissions, the username selected in the
                                                      application server must match the AXL username.

After updating the application server username, you must also restart the CUCM Cisco E911 network service on all the nodes
                                                      in the cluster. This service restart causes the Unified CM 911 to use the new userID and establish the connection between
                                                      the two servers.

AXL Password

The password for the application user on Cisco Unified
                                          					 Communications Manager with privileges to perform AXL queries.

AXL Port Number

The port number that is used by the application on Cisco Unified
                                          					 Communications Manger. The default value is 8443.

SNMP Settings

Use SNMPv3
                                          					 for discovery

Check this
                                          					 check box if the Cisco Unified Communications Manager has SNMPv3 enabled and
                                          					 you want Emergency Responder to use SNMPv3 for discovery.

Insert button

Click Insert to add the new CiscoUnifiedCommunicationsManager
                                          					 server to the list of servers.

Cancel Changes button

Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings.

Update button

Click Update when viewing an existing server to save changes you
                                          					 make to the server.

Only available when viewing an existing server. Replaces the Insert button when viewing an existing server.

Add New button

Click Add New to add another Cisco Unified Communications Manager server.

Cisco Unified Communications Manager list

A list of Cisco Unified Communications Manager servers defined for this Emergency Responder group. Click a server link or
                                          the Edit icon to view and modify the Emergency Responder configuration for the server. Click the Delete icon to delete the server.

Click Number of Users associated link to find
                                          					 the list of remote users associated with the Cisco Unified Communications
                                          					 Manager Server node.

## LAN Switch
                        	 Details

The LAN
                              		  Switch Details page appears when you choose Phone Tracking
                                 			 > LAN Switch Details .

Cisco Emergency Responder supports SNMP Version 1, Version 2 , Version 2C, and Version 3 of a LAN switch.

### Authorization
                              		  Requirements

You must
                              		  have system administrator or network administrator authority to access this
                              		  page.

### Description

Use the LAN Switch Details page to add, remove, or change the switches that Emergency Responder manages. Ensure that you identify
                              all switches that might have phones attached to them. You can only assign switch ports to ERLs if you enter the switches on
                              this page. Any phones attached to unidentified switches or ports are listed as unlocated phones in Emergency Responder, and
                              are assigned to the Default ERL.

Switches should not be configured with Static Engine ID.

The
                              		  following table describes the LAN Switch Details page.

Field

Description

Switch Host Name/IP Address

The IP address or DNS name of the switch.

For more information on standardized valid IPv4 or IPv6 address formats, see the following:

https://docs.oracle.com/javame/config/cdc/ref-impl/pbp1.1.2/jsr217/java/net/Inet4Address.html

https://docs.oracle.com/javame/config/cdc/ref-impl/pbp1.1.2/jsr217/java/net/Inet6Address.html

Description

Description of this switch.

Enable CAM-based Phone Tracking

Check this check box if there might be phones attached to this
                                          					 switch that do not use the Cisco Discovery Protocol (CDP) to announce
                                          					 themselves to the network. For non-CDP phones, Emergency Responder must use the
                                          					 Content Addressable Memory (CAM) information about the switch to identify
                                          					 phones.

Use port description as port location

Check this check box if you want to display the switch port
                                          					 description that is configured on the switch in the Location Field.

When the checkbox is enabled, the port description for each port will be updated in the database to reflect the location of
                                                      the port during each discovery. As a result, the time taken for the discovery process will be impacted depending on the number
                                                      of ports with descriptions on the switch.

Use SNMPv3
                                          					 for Discovery

Select
                                          					 this check box if the switch has SNMPv3 enabled and Emergency Responder should
                                          					 discover it using SNMPv3.

Insert button

Check Insert to add the switch to the list of switches.

When you click Insert, Emergency Responder asks if you want to
                                          					 run the switch port and phone update process on the switch right away. Click OK to
                                          					 run the process now, or click Cancel to add the switch to the configuration without running the process right away.

See Manually Run the Switch-Port and Phone Update Process for information about running the process if you select not to run it
                                                      						immediately.

Update button

Click Update when viewing an existing switch to save changes that you make to the switch.

Cancel Changes button

Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings.

LAN Switch list

A
                                          					 list of the switches you have already defined. Click the IP address/DNS name of
                                          					 the switch or click the Edit icon to view and modify settings for the switch. Click the Delete icon to delete the switch.

Add LAN Switch button

Click Add LAN
                                             						Switch to add another switch.

Export

Click the Export link to export the switch definitions to another file. See Export LAN Switch for more information.

Import

Click the Import link to import a list of switches into the Emergency Responder configuration.
                                          					 This list might be exported from your network management software. See Import LAN Switch for more information.

### Export LAN
                           	 Switch

The
                                 		  Export LAN Switch page appears when you click Export in the LAN Switch Details
                                 		  page (opened when you choose Phone Tracking
                                    			 > LAN Switch Details ).

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or network administrator authority to access this
                                 		  page.

#### Description

Use the
                                 		  Export LAN Switch page to create a file containing the Emergency Responder
                                 		  switch configuration.

If you
                                 		  must update several switch entries in Emergency Responder, you can export the
                                 		  switch information, make your changes in the export file using a spreadsheet,
                                 		  then reimport the file.

You can
                                 		  also download a file to your local system using the Download utility. See Download File for more information.

The
                                 		  following table describes the Export LAN Switch page.

Field

Description

Select Export Format

The format to use for the file, such as CSV (comma- separated
                                             					 values).

Enter Export File Name

The name of the file you want to create. Do not include the file
                                             					 extension.

Export button

Click Export to create the file. The Status
                                             					 box shows the status of the exportation.

Close button

Click Close to close the window.

Select a File to Download

Use the pull-down menu to select a LAN switches configuration
                                             					 file and click Download to download the file to your
                                             					 local system.

### Import LAN
                           	 Switch

The
                                 		  Import LAN Switch page appears when you click Import in the LAN Switch Details page (opened
                                 		  when you choose Phone Tracking > LAN Switch Details ).

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or network administrator authority to access this
                                 		  page.

#### Description

Use the
                                 		  Import LAN Switch page to add several switches at once to the Emergency
                                 		  Responder configuration. You can import a previously exported file or a file
                                 		  that you created on your local system and uploaded using the Upload utility.
                                 		  See Upload File for more information.

The
                                 		  following table describes the Import LAN Switch page.

Field

Description

Select Import Format

Select the format used in the file you are importing.

After you select the format, click view
                                                						sample file to see an example of the expected format and sequence of
                                             					 values. Use this sample information to create your import file in a
                                             					 spreadsheet, or to determine if your network management software can create the
                                             					 required format.

Select File to Import

Select the file from which you want to import data.

Before you can import a file, you must place it in the folder
                                             					 mentioned on this page.

Upload button

Click Upload to upload a file from your local system. See Upload File for more information.

Import button

Click Import to add data from the information in the import file to your Emergency Responder
                                             					 configuration.

Emergency Responder asks you whether you want to run phone
                                             					 tracking on the imported switch. You must run phone tracking before you can
                                             					 configure the switch ports, so normally you should choose OK . If
                                             					 you choose Cancel , Emergency Responder imports the switches but does
                                             					 not run the phone tracking process.

If you
                                                         						elect not to run the phone-tracking process, after importing the file, run the
                                                         						switch port and phone update process. See Manually Run the Switch-Port and Phone Update Process .

Close button

Click Close to close the window.

Text box that displays status information.

## Run Switch-Port and
                        	 Phone Update

When you
                           		choose Phone Tracking/Run
                              		  Switch-Port & Phone Update , a dialog box appears that prompts you to "Press Okay to run
                              		  Switch-Port and Phone update process on Emergency Responder."

Authorization Requirements

You must
                           		have system administrator or ERL administrator authority to access this page.

Description

Use the Run
                           		Switch-Port and Phone Update page to run manually the switch port and phone
                           		update process.

## Switch Port
                        	 Details

The
                              		  Switch Port Details page appears when you choose ERL
                                 			 Membership > Switch Ports .

### Authorization
                              		  Requirements

You must have a system administrator or ERL administrator authority to access this page.

### Description

Use the Switch Port Details page to assign switch ports to ERLs. This assignment allows the Emergency Responder to assign
                              the correct ERL to phones that connect to the network through the configured ports.

If the IOS software on the switch needs to be upgraded to the latest version, execute the snmp-server ifindex persist command before the upgrade. Failure in executing this command leads to a change of port indexes. In that scenario, Emergency
                                          Responder treats the existing port as a new port and turns the assigned ERL to Blank (no ERL).

To support switches such as the Cisco Catalyst 3750 switch, which has ports that can be uniquely identified by Switch ID,
                              Module ID and Port ID combination, Emergency Responder uses the following port-naming convention:

IfName—New field
                                    				display name for port as given for the switch CLI (for example, Fa1/5 or
                                    				Gi2/0/1).

Port
                                          					 Identifier—Replaces the Module ID/Port ID.

It contains {optional} <<Switch ID (for stackable switches like the Cisco Catalyst 3750)>>/ {optional} <<relative position
                                          of the module in switch>> / <<relative position of port in the module>> .

Search on Port
                                    				IfName replaces the Module ID/Port ID search.

The
                              		  following table describes the Switch Port Details page.

Field

Description

Notes

Switch Port Search
                                             						Parameters

Find ports where

Enter search criteria to select the ports that you want to view
                                          					 or configure.

To view all ports, click Find without entering any criteria.

To narrow your search:

Select All to indicate that only calls that match every criteria be selected (an AND search); select Any to indicate that calls that match any search criteria be selected (an OR search). From the pull-down menu, select the field
                                                that you want to search on (ERL Name, Phone MAC Address, and so on), select the search relationship (contains, starts with,
                                                and so on), enter the search string, and select how many results on page are displayed.

To search on a combination of fields, click the Plus icon ( + ) to add more search parameters. Click the Minus icon ( – ) to remove search parameters.)

Click Find when you have entered all the search parameters.

If you are configuring ports, generate a list of ports using the Find button.

The list of switch ports that match your search criteria, one
                                          					 line per port.

To assign ERLs to selected ports, check the check box to the
                                          					 left of the switch details, enter the ERL name in the text box, or click Search
                                             						ERL to find and select the ERL, then click Assign
                                             						ERL .

To view and update the phone location for a port, click the View link in the port's Location column.

Location name or switch port description cannot include special characters, such as the pound sign (#), comma (,), percentage
                                                      (%), ampersand (&), question mark (?), and forward slash (/).

To change the fields shown in the list and to change their
                                          					 order, click Edit
                                             						View . This action opens a separate Edit View page:

To add a field, select it in the Available Fields list and click > (right arrow).

To remove a field, select it in the Selected Fields list and click < (left arrow).

You cannot
                                                      						remove the ERL Name from the table view.

Click Apply to save your changes on the Edit Table View page. Click Close to close the window.

Emergency Responder displays a maximum number of 1,000 switch
                                          					 port records at a time. If the search results in more than 1,000 switch ports,
                                          					 an error message to refine the search is displayed.

If many ports match your search criteria, Emergency Responder uses several pages to display them. Use the First, Previous,
                                          Next, and Last links at the bottom of the page to move between pages. You can also enter a specific page number on the Page
                                          field and press Enter to move to that page.

Export

Click Export to export the ERL to switch port configuration to another file. See Export Switch Ports for more information.

Import

Click Import to import a set of ERL-to-port mappings into the Emergency Responder
                                          					 configuration. See Import Switch Ports for more information.

### Export Switch
                           	 Ports

The
                                 		  Export Switch Ports page appears when you click Export in the
                                 		  Switch Port Details page (opened when you choose ERL Membership
                                    			 > Switch Ports ).

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the
                                 		  Export Switch Ports page to create a file containing the Emergency Responder
                                 		  switch port configuration.

If you
                                 		  must make changes to a large number of port-to-ERL assignments, you can export
                                 		  a file, make your changes in the file using a spreadsheet, and then reimport
                                 		  the file.

You can
                                 		  also download a file using the Download utility, modify it on your local
                                 		  system, then upload it using the Upload utility. See Download File for more information.

The
                                 		  following table describes the Export Switch Ports page.

Field

Description

Select Export Format

The format to use for the file, such as CSV (comma-separated
                                             					 values).

Enter Export File Name

The name of the file you want to create. Do not include the file
                                             					 extension.

Export button

Click Export to create the file. The Status box shows the status of the exportation.

Close button

Click Close to close the window.

Select a File to Download

Use the pull-down menu to select a file and click Download to download the file to your local system.

### Import Switch
                           	 Ports

The
                                 		  Import Switch Ports page appears when you click Import in the
                                 		  Switch Port Details page (opened when you choose ERL Membership
                                    			 > Switch Ports ).

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the
                                 		  Import Switch Ports page to add or update several switch port configurations at
                                 		  once to the Emergency Responder configuration. Switch port configurations are
                                 		  mappings of ports to ERLs.

To create
                                 		  the switch port import file, follow these steps:

Export the
                                       				switch port details.

Modify the ERK
                                       				field of these records and save the file.

Import the file
                                       				using switch port import.

You can
                                 		  also create the import file on your local system and then upload the file using
                                 		  the Upload utility. See Upload File for more information.

The
                                 		  following table describes the Import Switch Ports page.

Field

Description

Select Import Format

Select the format used in the file you are importing.

After you select the format, click view
                                                						sample file to see an example of the expected format and sequence of
                                             					 values. You can use this sample information to create your import file in a
                                             					 spreadsheet, but it is easier to export the switch port information from
                                             					 Emergency Responder, modify the export file using a spreadsheet program, and
                                             					 then import the modified file.

See Export Switch Port Information for information about exporting
                                                         						switch port information.

Select File to Import

Select the file from which you want to import data.

Upload button

Click Upload to upload a file from your local system. See Upload File for more information.

Import button

Click Import to add data from the information in the import file to your Emergency Responder
                                             					 configuration. ERL assignments in the import file override assignments that
                                             					 already exist in the Emergency Responder configuration.

Port ERL
                                                         						configurations are only updated if Emergency Responder has discovered the port
                                                         						before you import the port configuration.

Close button

Click Close to close the window.

Text box that displays status information.

### Save Switch Port Configuration

The Save Switch Port Configuration page appears when you click Save Switch Config in the Switch Port Details page (opened when you choose ERL Membership > Switch Ports ).

#### Authorization Requirements

You must have system administrator or ERL administrator authority to access this page.

#### Description

Use the Save Switch Port Configuration page to save the configuration details in a file containing the Emergency Responder
                                 switch port configurations.

The Save Switch Configuration functionality can be used only when the IP address of the old switch and the new switch is the
                                             same. If the IP address of the old switch and the new switch is different, you must perform an export switch functionality
                                             to export the old switch port details, delete the old switch records, and then import the new switch details.

If you need to make changes to an existing switch and replace it with a newer switch, or even change large number of port-to-ERL
                                 assignments of an existing switch, you should first save and download the existing configuration details in a CSV file. You
                                 can then add or remove an existing switch and add a new switch and run Full Discovery, and then upload the saved CSV file
                                 to reuse the existing configuration changes that was saved in the CSV file. For example, you can reuse the ERL name and Location
                                 details of the previous switch that you had configured.

You can download the saved CSV files from the Save Switch Port Configuration page.

You can also download or delete saved CSV files using the File Management Utility > Switch Config Files option.

The following table describes the Save Switch Port Configuration page.

Field

Description

Select Save Config Format

The format to use for the file, such as CSV (comma-separated values).

Enter Save Config File name

The name of the file you want to create. Do not include the file extension.

Save Config

Click Save Config to create the file. The Status box shows the status of the exportation.

Close

Click Close to close the window.

Select a File to Download

Use the drop-down menu to select a file and click Download to download the file to your local system.

### Upload Switch Port Configuration

The Upload Switch Port Configuration page appears when you click Upload Switch Config in the Switch Port Details page (opened when you choose ERL Membership > Switch Ports ).

#### Authorization Requirements

You must have system administrator or ERL administrator authority to access this page.

#### Description

Use the Upload Switch Port Configuration page to add or update switch port configurations (ERL Name and Location details)
                                 at once to the Emergency Responder switch port configuration. From the Select File to Upload Config drop-down list, you can choose one of the saved CSV files and upload the selected file.

The Upload Switch Port Configuration functionality can be used only when the IP address of the old and the new switch is the
                                             same. If the IP address of the old and new switch is different, you must perform an export switch functionality to export
                                             the old switch port details, delete the old switch records, and then import the new switch details.

The following table describes the Upload Switch Port Configuration page.

Field

Description

Select Upload config File Format

Select the format used in the file you are importing. For example, CSV format.

After you select the format, click View Sample File to see an example of the expected format and sequence of values. You can use this sample information to create your saved
                                             configuration file in a spreadsheet.

See Save Switch Port Configuration for information about exporting saved switch port information.

Select File to Upload Config

From the drop-down list, choose the file which for you want to import data.

Upload

Click Upload to upload a file from your local system. The Status box shows the status of the exportation.

You can find details on the total number of port updates, and details on the total number of ports that have changed for the
                                             location, and ERL changes and updates.

Close

Click Close to close the window.

## Access Point
                        	 Details

The
                              		  Access Point Details page appears when you choose ERL
                                    				Membership > Access Points .

### Authorization
                              		  Requirements

You
                              		  must have system administrator or ERL administrator authority to access this
                              		  page.

### Description

The Access Point
                              		  Details page lists all the Access Points configured in the corresponding Cisco
                                 			 Unified Communications Manager .

You can assign
                              		  Access Points to ERLs on the Access Point Details page. This assignment allows Cisco
                                 			 Emergency Responder to assign the correct ERL to phones that connect
                              		  to the network through the configured Access Point.

The
                              		  following table describes the Access Point Details page.

Field

Description

Notes

Status

Ready—Displays when the Access Point page is loaded
                                                   						  successfully.

Update
                                                   						  successful—Displays when an ERL assignment is made successfully.

ERL
                                                   						  Not Found—Displays when trying to assign an ERL which is not available.

Access Point Search
                                             						Parameters

Find

Enter search criteria to select the Access Points that you want
                                          					 to view or configure.

To view all Access Points, click Find without entering any criteria.

To narrow your search:

Access Point Name

Bssid

ERL Name

contains

is
                                                         								not Empty

starts with

Ends with

is
                                                         								Empty

is
                                                         								Exactly

Enter
                                                						  the required search string in next empty field.

From the and show items per page drop-down list, choose the appropriate number of results to be displayed on the page.

- Click Find when you have entered all the search parameters.

Access
                                          					 Points

Last
                                                   						  discovery was done at—Displays the time and date of the last major/AXL
                                                   						  discovery if the find result is successful.

No
                                                   						  active query—This is displayed if you click the Access Point page without
                                                   						  clicking the Find button.

No
                                                   						  matching records—This is displayed when Find is unable to retrieve the matching records.

Phone Location tables are being modified. Please wait and try again—This is
                                                   						  displayed when the Cisco Emergency Recorder server is not loaded
                                                   						  completely.

Phone Location details are not populated as phone tracking is still in
                                                   						  progress. Try after some time—This is displayed when the phone tracking engine
                                                   						  is still running.

Cisco Emergency Responder server is not yet
                                                   						  initialized completely. Please wait—This is displayed when the Cisco Emergency Responder service is restarted.

Cisco Emergency Responder is not running: Failed to
                                                   						  contact Cisco Emergency Responder —This is displayed when the Cisco Emergency Responder service is restarted.

The list of Access Points that match your search criteria, one
                                          					 line per Access Point.

To assign ERLs to selected Access Point, check the check box to
                                          					 the left of the access details, enter the ERL name in the text box, or click Search ERL to find and select the ERL, then click Assign ERL .

To view the phones associated to that Access Point, click the View Phones link in the Access Point's View Phones column. The phone details include Phone, MAC Address, IP Address, Extension, and Phone
                                          Type. For more information, see Access Point Phones .

Emergency Responder displays a maximum number of 1,000 Access
                                          					 Point records at a time. If the search results in more than 1,000 access
                                          					 points, an error message to refine the search is displayed.

If a large number of points match your search criteria, Emergency Responder uses several pages to display them. Use the First , Previous , Next , and Last links at the bottom of the page to move between pages. You can also enter a specific page number on the Page field and press Enter to move to that page.

Export

Click Export to export the ERL to Access Point configuration to another file. For more information, see Access Point Phones .

### Access Point Phones

The Access Point Phones page appears when you choose ERL Membership > Access Points and click View Phones on any one of the records returned by the Access Point search.

#### Authorization Requirements

You must have a system administrator or ERL administrator authority to access this page.

#### Description

Use the Access Point Phones page to view the Access Point Name, the Bssid for each Access Point, and the list of phones tracked
                                 in that Access point.

### Export Access
                           	 Points

The
                                 		  Export Access Points page appears when you click Export on
                                 		  the Access Point Details page (opened when you choose ERL
                                       				Membership > Access Points ).

#### Authorization
                                 		  Requirements

You
                                 		  must have a system administrator or ERL administrator authority to access this
                                 		  page.

#### Description

Use the
                                 		  Export Access Points page to create a file containing the Cisco
                                    			 Emergency Responder access point configuration.

You can export a file and download the exported file using the Download utility. See Download File for more information.

The
                                 		  following table describes the Export Access Points page.

Field

Description

Select Export Format

The format to use for the file, such as CSV (comma-separated
                                             					 values).

Enter Export File Name

The name of the file you want to create. Do not include the file
                                             					 extension.

Export button

Click Export to create the file. The Status box shows the
                                             					 status of the exportation.

Close button

Click Close to close the window.

Select a File to Download

Use the drop-down menu to select a file and click Download to download the file to your local system.

## Find and List IPv4 and IPv6 Subnets (Applicable from Release 15SU1 onwards)

The Find and List IPv4 and IPv6 Subnets page appears when you choose ERL Membership > IP Subnets .

### Authorization
                              		  Requirements

You must have a system administrator or ERL administrator authority to access this page.

### Description

Use the Find and List IPv4 and IPv6 Subnets page to locate and view IP subnets that you would like to modify or delete. You can also navigate to add new IPv4 or IPv6 Subnets from this page.

The following table describes the Find and List IPv4 and IPv6 Subnets page.

Field

Description

Find IP Subnets where...

To list specific IP subnets, select the search criteria and click Find .To list all IP subnets, click Find without entering any criteria.

Add New IPv4 Subnet or Add New IPv6 Subnet

IP Subnets list

Displays results of the IPv4 and IPv6 Subnets search. For the IPv4 and IPv6 Subnets found, the system displays the Subnet
                                          ID, Subnet Mask (IPv4)/Prefix  Length (IPv6), ERL Name, and Location.

Click on one of the preceding records or click the Edit icon to modify that IPv4 or IPv6 subnet. The Configure IPv4 Subnet or Configure IPv6 Subnet page appears. Change the Location
                                          field or the ERL Name field.

When modifying an existing IPv4 subnet, you cannot change the Subnet ID or the Subnet Mask.

When modifying an existing IPv6 subnet, you cannot change the Subnet ID or the Prefix Length.

Click Update to save your changes to the IPv4 or IPv6 subnet.

Click the View Phones icon in any record to view all of the IP subnet phones. The IP Subnet Phones page displays a list of the discovered phones
                                          in the IP subnet. See Configure IPv4 Subnet or Configure IPv6 Subnet (Applicable from Release 15SU1 Onwards) .

Click the Delete icon to remove an IPv4 or IPv6 subnet. When you click Delete , Cisco Emergency Responder asks if you want to run the switch port, and the phone updates the process right away. Click OK to run the process immediately or click Cancel to delete the IPv4 or IPv6 subnet without running the process immediately.

Cancel Changes button

Click Cancel Changes to cancel any changes made on the Configure IPv4 Subnet or Configure IPv6 Subnet page.

The Cancel Changes button is viewable only on the  Configure IPv4 Subnet or Configure IPv6 Subnet page.

Add New IP Subnet (IPv4)

Click Add New IP Subnet to configure new IPv4 subnets. The Configure IPv4 Subnet page appears. See Configure IPv4 Subnet for more information.

Add New IP Subnet (IPv6)

Click Add New IP Subnet to configure new IPv6 subnets. The Configure IPv6 Subnet page appears. See Configure IPv6 Subnet (Applicable from Release 15SU1 Onwards) for more information.

Export

Click Export to create a file containing the IP subnets configuration information. The Export IP Subnet page appears. See Export IP Subnets for more information.

Import

Click Import to import IP subnet configuration information from a file. The Import IP Subnet page appears. See Import IP Subnets for more information.

### Configure IPv4 Subnet

To reach the Configure IPv4 Subnet page, choose ERL > Membership > IP Subnets and click on Add New IPv4 Subnet . The Configure IPv4 Subnet page appears.

#### Authorization Requirements

You must have a system administrator or ERL administrator authority to access this page.

#### Description

Use the Configure IPv4 Subnet page to manually define an IP subnet and its ERL. You must manually define an IP Subnet if the
                                 Emergency Responder cannot automatically track the type of phone. One example is if the phone is wireless. See Network Hardware and Software Requirements for information about phone support.

You can choose not to track the phones in an IP Subnet by checking the check box Do not track phones under this IP subnet . If you do not track the phones in an IP subnet, then you do not need the Emergency Responder User Licenses for these phones.

The following table describes the Configure IPv4 Subnet page.

Field

Description

Add New IPv4 Subnet

Subnet ID

Enter a valid IPv4 subnet address that you want to define.

For more information on standardized valid IPv4 address formats, see https://docs.oracle.com/javame/config/cdc/ref-impl/pbp1.1.2/jsr217/java/net/Inet4Address.html .

Subnet Mask

The mask of the subnet you want to define. Based on the bit mask, this value represents the number of IPv4 addresses that
                                             are included in this subnet.

Do not track phones under this IP subnet

Check this check box if you do not want this IPv4 subnet and the underlying phones tracked by Cisco Emergency Responder. If
                                             you do not track the phones in an IPv4 subnet, then you do not need the Emergency Responder User Licenses for these phones.

Location (optional)

The location of the new IP subnet.

ERL Name

The ERL to assign to the subnet. Type in a valid ERL name or click Search ERL to find and select the ERL.

Insert button

Click Insert to add the subnet.

When you click Insert , Emergency Responder asks if you want to run the switch port, and the phone updates the process on the switch immediately.
                                             Click OK to run the process now, or click Cancel to add the IPv4 subnet to the configuration without running the process immediately.

Cancel Changes button

Click Cancel Changes to change the fields on this page back to the last saved settings.

### Configure IPv6 Subnet (Applicable from Release 15SU1 Onwards)

To reach the Configure IPv6 Subnet page, choose ERL > Membership > IP Subnets and click on Add New IPv6 Subnet . The Configure IPv6 Subnet page appears.

#### Authorization Requirements

You must have a system administrator or ERL administrator authority to access this page.

#### Description

Use the Configure IPv6 Subnet page to manually define an IP subnet and its ERL. You must manually define an IP Subnet if the
                                 Emergency Responder cannot automatically track the type of phone. One example is if the phone is wireless. See Network Hardware and Software Requirements for information about phone support.

You can choose not to track the phones in an IP Subnet by checking the check box Do not track phones under this IP subnet . If you do not track the phones in an IP subnet, then you do not need the Emergency Responder User Licenses for these phones.

The following table describes the Configure IPv6 Subnet page.

Field

Description

Add New IP Subnet

Subnet ID

Enter a valid IPv6 subnet address that you want to define.

For more information on standardized valid IPv6 address formats, see https://docs.oracle.com/javame/config/cdc/ref-impl/pbp1.1.2/jsr217/java/net/Inet6Address.html .

Prefix Length

(Mandatory) Enter a prefix length for the subnet. The range is 1 to 128.

Do not track phones under this IP subnet

Check this check box if you do not want this IPv6 subnet and the underlying phones tracked by Cisco Emergency Responder. If
                                             you do not track the phones in an IPv6 subnet, then you do not need the Emergency Responder User Licenses for these phones.

Location (optional)

The location of the new IP subnet.

ERL Name

The ERL to assign to the subnet. Type in a valid ERL name or click Search ERL to find and select the ERL.

Insert button

Click Insert to add the subnet.

When you click Insert , Emergency Responder asks if you want to run the switch port, and the phone updates the process on the switch immediately.
                                             Click OK to run the process now, or click Cancel to add the IPv6 subnet to the configuration without running the process immediately.

Cancel Changes button

Click Cancel Changes to change the fields on this page back to the last saved settings.

### IP Subnet
                           	 Phones

The IP Subnet Phones page appears when you choose ERL > Membership/ IP > Subnets and click the View Phones icon in any records returned by the IP Subnet Search.

#### Authorization Requirements

You must have system administrator or ERL administrator authority to
                                 		  access this page.

#### Description

Use the IP subnet Phones page to view all the IP subnet
                                 		  phones discovered by Emergency Responder.

The IP subnet phones page displays the subnet ID, the
                                 		  subnet mask for each IP subnet and lists all the phones tracked in that IP
                                 		  subnet, and when the last phone was tracked.

### Export IP
                           	 Subnets

To reach the Export IP Subnets page, choose ERL Membership > IP > Subnets . On the Find and List IP Subnets page, click the Export link. The Export IP Subnets page appears.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the
                                 		  Export IP Subnets page to create a file containing the Emergency Responder
                                 		  Export IP Subnet configurations.

If you
                                 		  must update a large number of Export IP Subnets, you can export the phone data,
                                 		  make your changes in the file using a spreadsheet, and then reimport the file.

You can
                                 		  also download a file using the Download utility, modify it on your local
                                 		  system, then upload it using the Upload utility. See Download File for more information.

The
                                 		  following table describes the Export IP Subnets page.

Field

Description

Select Export Format

Select the format used in the file that you are importing.

After you select the format, click view
                                                						sample file to see an example of the expected format and sequence of
                                             					 values. Use this sample information to create your import file in a
                                             					 spreadsheet.

Enter Export File Name

The name of the file you want to create. Do not include the file
                                             					 extension

Export button

Click Export to add data from the import file to your Emergency Responder configuration.

Close button

Click Close to close the window.

Select a File to Download

Use the pull-down menu to select a file and click Download to download the file to your local system.

### Import IP
                           	 Subnets

To reach the Import IP Subnets page, choose ERL Membership > IP Subnets . On the Find and List IP Subnets page, click the Import link. The Import IP Subnets page appears.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the
                                 		  Import IP Subnet page to create or update many IP subnet phones at once from a
                                 		  file in which you have defined their data. Create this file using a spreadsheet
                                 		  that can save the information in one of the required formats. View the samples
                                 		  from this page before attempting to create or update an import file.

If you
                                 		  must update many IP subnet phones, you can export the phone data, update the
                                 		  export file, and reimport the file.

You can
                                 		  also upload a previously downloaded file that you have modified on your local
                                 		  system. See Upload File for more information.

The
                                 		  following table describes the Import IP Subnets page.

Field

Description

Select Import Format

Select the format used in the file you are importing.

After you select the format, click view
                                                						sample file to see an example of the expected format and sequence of
                                             					 values. Use this sample information to create or update your import file in a
                                             					 spreadsheet.

Select File to Import

Select the file from which you want to import data.

Upload button

Click Upload to upload a file from your local system. See Upload File for more information.

Import button

Click Import to add data from the import file to your Emergency Responder configuration.

Close button

Click Close to close the window.

Text box that displays status information.

## Unlocated
                        	 Phones

The
                              		  Unlocated Phones page appears when you choose ERL Membership > Unlocated Phones .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the
                              		  Unlocated Phones page to identify phones that are registered with
                              		  CiscoUnifiedCommunicationsManager, but which Emergency Responder cannot
                              		  locate. A phone can become unlocated for several reasons:

The phone is
                                    				attached to a switch that is not defined in Emergency Responder.

The phone is
                                    				connected to an unsupported device, such as a router port, a hub connected to a
                                    				router, or an unsupported switch.

The switch to
                                    				which the phone is connected is currently unreachable; for example, it does not
                                    				respond to SNMP queries.

The phone is not
                                    				found under any configured IP subnet and the phone is not configured as a
                                    				synthetic phone.

The phone that
                                    				was manually assigned.

The phone that
                                    				was previously identified as an unlocated phone and assigned an ERL.

Because
                              		  Emergency Responder cannot assign an unlocated phone to the appropriate ERL,
                              		  try to identify and resolve all problems that are preventing Emergency
                              		  Responder from locating these phones on your network. If you cannot resolve the
                              		  problems by defining switches in Emergency Responder, or by moving phones to
                              		  supported switch ports, you might have to manually assign a phone to an ERL on
                              		  this page. See Unlocated Phones for troubleshooting information.

The
                              		  following table describes the Unlocated Phones page.

Field

Description

Find phones where...

Enter search criteria to select the unlocated phones you want to
                                          					 find.

To find all unlocated phones, click Find without entering any criteria.

To narrow your search:

- Select All to indicate that only phones that match every criteria be selected (an AND
                                             						search); select Any to indicate that phones that match any search criteria be selected (an OR
                                             						search). From the pull-down menu, select the field you want to search on (Phone
                                             						Extension, Phone MAC Address, and so on), select the search relationship (is
                                             						Exactly, Starts with, and so on), and enter the search string.

- To search on a combination of
                                             						fields, click the Plus icon (+) to add additional search parameters. (Click the Minus icon to ( – ) remove search parameters.)

- Click Find when you have entered all of the search parameters.

Assign ERL

To assign the ERL, select the phones by checking the check box
                                          					 next to the phones, click Search
                                             						ERL to find and select the ERL, and click Assign
                                             						ERL .

Unassign ERL

To unassign a ERL, select the phones and click on Unassign ERL button.

List of unlocated phones

A
                                          					 list of the phones Emergency Responder could not assign to a specific ERL. The
                                          					 following information is displayed:

- Emergency Responder Group

- Phone IPv4
                                             						Address

- Phone IPv6 Address

- Phone Mac Address

- Phone Extension

- Assigned ERL

- Effective ERL

- ERL Rule

If the phone has moved to a switch served by a different
                                          					 Emergency Responder group, the Emergency Responder group name is shown for the
                                          					 phone in the list.

If there
                                                      						are a lot of unlocated phones, Emergency Responder uses more than one page to
                                                      						list them. You can only assign phones to ERLs from one page at a time. Use the
                                                      						links at the bottom of the list to move from page to page.

### Export Unlocated
                           	 Phones

To view the Export Unlocated Phones page, choose ERL Membership > Unlocated Phones and click Export .

#### Authorization Requirements

You must have system administrator or ERL administrator authority to
                                 		  access this page.

#### Description

Create a file containing the Emergency Responder Export Unlocated
                                          				Phones.

Use the Download utility to download a file containing the
                                          				Emergency Responder Export Unlocated Phones.

The following table describes the fields found on the Export Unlocated
                                 		  Phones page.

Field

Description

Select Export Format

Select the file format that matches the file being imported.

After you select the format, click View Sample File to see an example of
                                             					 the expected format and sequence of values. Use this example when creating your
                                             					 imported file.

Enter Export File Name

The name of the file that you want to create. Do not include
                                             					 the file extension.

Export button

Click Export to add data from the import file
                                             					 to your Emergency Responder configuration.

Close button

Click Close to close the window.

Download

Select a File to Download

Use the pulldown menu to select a file. Click Download to download the file.

## Find and List
                        	 Manually Configured Phone

The Find
                              		  and List Manually Configured Phones page appears when you choose ERL Membership
                                 			 > Manually Configured Phones .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the
                              		  Find and List Manually Configured Phones page to locate and view phones that
                              		  you would like to modify or delete. You can also navigate to add new phones
                              		  from this page.

The
                              		  following table describes the Find and List Manually Configured Phones page.

When you are
                                          			 performing this search as part of an E.164 dial plan, the "+" is a valid
                                          			 character.

Field

Description

Find manual phones where Line Number...

Enter search criteria to select the manually configured phones
                                          					 that you want to find.

To find all manually configured phones, click Find without entering any criteria.

To narrow your search, use the pull-down menu to select the
                                          					 search condition (contains, Starts with, and so on) and enter the line number
                                          					 in the text box. You can also select how many results are displayed per page
                                          					 from the pull-down menu. When you have specified your search criteria, click Find .

Manually Configured Phones list

Displays the search results. For each phone found, the system
                                          					 displays the Line Number, ERL Name, IPv4 Address, IPv6 Address, and Location. Click on one of these records or click the Edit icon to view and modify the information for that phone. The Modify Manual Phone
                                          					 page appears. You can change the MAC Address, IPv4 Address, IPv6 Address, Phone Type, Version, Location, and ERL Name.

When
                                                      						modifying a manual phone, you cannot change the Subnet ID or the Line Number.

Click Update to save your changes.

Add new Manual Phone

Click Add new
                                             						Manual Phone to add a manually configured phone. The Add New Manual Phone
                                          					 page appears. See Add New Manual Phone for more information.

The Add new
                                                         						  Manual Phone button is also available from the Modify Manual Phone page.

Export

To export Manually Configured Phone information to a file, click Export on the Find and List Manually Configured Phones page. See Export Manual Phones for more information.

Import

To import Manually Configured Phone information to a file, click Import on the Find and List Manually Configured Phones page. See Import Manual Phones for more information.

### Add New Manual
                           	 Phone

To reach
                                 		  the Add New Manual Phone page, choose ERL Membership
                                    			 > Manually Configured Phones . On the Find and List Manually Configured Phones page, click the Add new Manual Phone link. The Add New Manual Phone page appears.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the
                                 		  Add New Manual Phone page to manually define a phone ERL. You must manually
                                 		  define a phone if any of these conditions apply:

Emergency
                                       				Responder cannot automatically track the type of phone, for example, if the
                                       				phone is analog. See Network Hardware and Software Requirements for information about phone support.

The phone is
                                       				hosted on an unsupported port, such as a router port, a hub connected to a
                                       				router, or a port on an unsupported switch.

For
                                 		  manually defined phones, Emergency Responder cannot automatically locate and
                                 		  update ERL information. You should regularly review manual phone configurations
                                 		  to ensure that they are correct.

The
                                 		  following table describes the Add New Manual Phone page.

Field

Description

Add New Manual Phone

Line Number

The extension of the phone you want to define.

MAC Address

The MAC address of the phone, if it is an IP phone.

IPv4 Address

The IPv4 address of the phone, if it is an IP phone.

IPv6 Address

The IPv6 address of the phone, if it is an IP phone.

Phone Type

The type of phone, such as analog. This field is for your
                                             					 information only.

Version

The version of the phone software, if any. This field is for
                                             					 your information only.

Location

The location of the phone.

ERL Name

The ERL that you want to assign to the phone. To find and select
                                             					 the ERL, click Search
                                                						ERL .

Insert button

Click Insert to add the phone to the list of phones.

The Insert
                                                         						button only appears when you are adding a phone.

Cancel Changes button

Click Cancel
                                                						Changes to change the fields on this page back to the last saved
                                             					 settings.

### Export Manual
                           	 Phones

To reach
                                 		  the Export Manual Phones page, choose ERL Membership
                                    			 > Manually Configured Phones . On the Find and List Manually Configured Phones page, click the Export link. The Export Manual Phones page appears.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the
                                 		  Export Manual Phones page to create a file containing the Emergency Responder
                                 		  manual phone configurations.

If you
                                 		  must update a large number of manually configured phones, you can export the
                                 		  phone data, make your changes in the file using a spreadsheet, and then
                                 		  reimport the file.

You can
                                 		  also download a file to your local system using the Download utility, modify
                                 		  the file, and then upload it using the Upload utility. See Download File for more information.

The
                                 		  following table describes the Export Manual Phones page.

Field

Description

Select Export Format

Select the format used in the file you are importing.

After you select the format, click view
                                                						sample file to see an example of the expected format and sequence of
                                             					 values. Use this sample information to create your import file in a
                                             					 spreadsheet.

Enter Export File Name

The name of the file that you want to create. Do not include the
                                             					 file extension.

Export button

Click Export to export the file to a file.

Close button

Click Close to close the window.

Select a file to download

Use the pull-down menu to select a file and then click Download to download the file to your local system.

### Import Manual
                           	 Phones

To reach
                                 		  the Import Manual Phones page, choose ERL Membership
                                    			 > Manually Configured Phones . On the Find and List Manually Configured Phones page, click the Import link. The Import Manual Phones page appears.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the
                                 		  Import Manual Phones page to create or update many manually configured phones
                                 		  at once from a file in which you have defined their data. Create this file
                                 		  using a spreadsheet that can save the information in one of the required
                                 		  formats. View the samples from this page before attempting to create or update
                                 		  an import file.

If you
                                 		  must update a lot of manually configured phones, you can export the phone data,
                                 		  update the export file, and reimport the file.

You can
                                 		  also upload a file from a local system using the Upload utility and then import
                                 		  the data in the file. See Upload File for more details.

The
                                 		  following table describes the Import Manual Phones page.

Field

Description

Select Import Format

Select the format used in the file you are importing.

After you select the format, click view
                                                						sample file to see an example of the expected format and sequence of
                                             					 values. Use this sample information to create your import file in a
                                             					 spreadsheet.

Select File to Import

Select the file from which you want to import data.

Upload

Click Upload to upload a file from a local system. The Upload File page appears. See Upload File for more details.

Import button

Click Import to add data from the import file to your Emergency Responder configuration.

Close button

Click Close to close the window.

Displays status messages.

## Find and List
                        	 Synthetic Phones

The Find
                              		  and List Synthetic Phones page appears when you choose ERL Membership
                                 			 > Synthetic Phones .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the
                              		  Find and List Synthetic Phones page to locate and view phones that you would
                              		  like to modify or delete. You can also navigate to add new synthetic phones
                              		  from this page.

The
                              		  following table describes the Find and List Synthetic Phones page.

Field

Description

Find Synthetic phones where MAC Address

Enter search criteria to select the synthetic phones you want to
                                          					 find.

To find all synthetic phones, click Find without entering any criteria.

To narrow your search, use the pull-down menu to select the
                                          					 search condition (contains, Starts with, and so on) and enter the MAC address
                                          					 in the text box. You can also select how many results per page are displayed
                                          					 from the pull-down menu. When you have specified your search criteria, click Find .

Synthetic Phones list

Displays the search results. For each phone found, the system
                                          					 displays the Line Number, ERL Name, IP Address, and Location. Click on one of
                                          					 these records or click the Edit icon to view and modify the information for that phone. The Modify Synthetic
                                          					 Phone page appears. You can change the MAC Address, IP Address, Phone Type,
                                          					 Version, Location, and ERL Name.

When
                                                      						modifying a synthetic phone, you cannot change the Subnet ID or the Line
                                                      						Number.

Click Update to save your changes.

Add new Synthetic Phone

Click Add new
                                             						Synthetic Phone to add a synthetic phone. The Add New Synthetic Phone page
                                          					 appears. See Add New Synthetic Phone for more information.

The Add new
                                                         						  Synthetic Phone button is also available from the Modify Synthetic Phone
                                                      						page.

### Add New Synthetic
                           	 Phone

To reach
                                 		  the Add New Synthetic Phone page, choose ERL Membership
                                    			 > Synthetic Phones . On the Find and List Synthetic Phones page, click
                                 		  the Add new Synthetic
                                    			 Phone link. The Add New Synthetic Phone page appears.

You cannot configure test ERLs for off-premise ERLs and National E911 Service Provider ERLs.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the
                                 		  Add New Synthetic Phone page to manually define a synthetic phone ERL. You must
                                 		  configure synthetic phones in the subnet for testing ERL configurations.

For
                                 		  synthetic phones, Emergency Responder cannot automatically locate and update
                                 		  ERL information. You should regularly review synthetic phone configurations to
                                 		  ensure that they are correct.

The
                                 		  following table describes the Add New Synthetic Phone page.

Field

Description

Notes

MAC Address

The MAC address of the synthetic phone, or a range of MAC
                                             					 addresses.

The synthetic MAC address must be within the range 00059a3b7700
                                             					 - 0059a3b8aff

Enter the MAC address in this format: xx-xx-xx-xx-xx-xx or
                                             					 xxxxxxxxxxxx

ERL Name

The ERL to assign to the synthetic phone. Type in a valid ERL
                                             					 name or select the ERL from the drop-down list.

Insert button

Click Insert to add the synthetic phone to the list of phones.

The Insert button only appears when you are adding a phone.

New button

Click New to
                                             					 add another phone.

The New button only appears when you are viewing an existing phone.

Update button

Click Update when viewing an existing phone to save changes you make to the phone.

The Update button only appears when you are viewing an existing phone.

Cancel Changes button

Click Cancel
                                                						Changes to change the fields on this page back to the last saved
                                             					 settings.

## Find and List
                        	 Users

The Find
                              		  and List Users page appears when you choose User Management
                                 			 > User .

### Authorization
                              		  Requirements

You must
                              		  have system administrator authority to access this page.

### Description

Use the
                              		  Find and List Users page to find and list current users, to add new users, and
                              		  to modify and delete current users.

The
                              		  following table describes the Find and List Users page.

Field

Description

Find User where User Name

Enter search criteria to select the users that you want to find.

To find all users, click Find without entering any criteria.

To narrow your search:

- Select All to indicate that
                                             						only users that match the selected criteria be displayed (an AND search).

- Select Any to indicate that users that match any search criteria be selected (an OR
                                             						search).

Authentication Mode—Both, Remote or Local

User
                                                      								Name— Ends with, Starts with, contains or Exactly.

Unified CM Cluster—Ends with, Starts with, contains or Exactly.

- To search on a combination of
                                             						fields, click the Plus icon ( + ) to add additional search parameters. (Click the Minus
                                             						icon ( - ) to remove
                                             						search parameters.)

- Click Find when you have entered all of the search parameters.

Users list

This section of the page displays the search results. If there
                                          					 are no usernames are displayed after completion of the search, then no users
                                          					 have been configured yet.

Username

Displays the users name based on the selection criteria.

Authentication Mode

Displays the authentication mode of the user. The authentication
                                          					 mode can be either Remote or Local.

Unified CM Cluster

This value is displayed only when the user is authenticated
                                          					 remotely, with the Unified CM server.

Edit icon

Click the user name or the Edit icon to display the Modify User page, which
                                          					 allows you to change the user authentication mode, password and Unified CM
                                          					 cluster. The Modify User page also displays which groups and roles have been
                                          					 assigned to the user.

Delete icon

Click the Delete icon to delete the user from the system.

You cannot
                                                      						delete the Administrator.

Add New User button

Click the Add New User button to open the Add User page. See Table 1 for a description of the Add User page.

Delete Users button

Click the Delete Users button to delete users in bulk. Select
                                          					 multiple users, both remote and local, by checking the check box and then
                                          					 clicking the Delete Users button.

Change to Remote Users button

Click the Change to Remote Users button to change local users
                                          					 to remotely authenticated users in bulk.

Change to IdP Users button

Click the Change to IdP Users button to change
                                          					 local or remote users to IdP users, whose password is maintained in IdP.

### Add User

The Add
                                 		  User page appears when you choose User Management
                                    			 > User and click Add new User on the Find and List Users page. You can also access the Add User page from the
                                 		  Modify User page. See Modify User for more information.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator authority to access this page.

#### Description

Use the
                                 		  Add User page to add a new user to the system.

The
                                 		  following table describes the Add User page.

Field

Description

User Name

Enter the username for the new user.

Authentication Mode

Select the authentication mode of the new user. The user can
                                             					 either be a Remote user, Local user, or a IdP user.

Password

Enter the password for the new user.

Reset on
                                             					 Next Logon

Check the Reset on Next Logon check box to reset or change the
                                             					 password after a successful sign-in.

This
                                             					 field is enabled only for the local users.

Confirm Password

Reenter the password for the new user.

Unified CM Cluster

This field is enabled only when the user is a Remote user.
                                             					 Select a Unified CM cluster, from the drop-down list, to authenticate the
                                             					 remote user.

Insert button

Inserts the new user.

Cancel Changes button

Cancels changes made to the Add User page.

### Modify User

The
                                 		  Modify User page appears when you choose User Management
                                    			 > User , search for a user, and then click a user name or on the Edit icon associated with the user on the Find and
                                 		  List Users page.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator authority to access this page.

#### Description

Use the
                                 		  Modify User page to change a current user's password.

The
                                 		  following table describes the Modify User page.

Field

Description

User Name

Displays the name of the user whose information is being
                                             					 modified.

You cannot
                                                         						change the username on the Modify User page.

Authentication Mode

Change the authentication mode for a user. You can change a
                                             					 local user to a remote user and a remote user to local user.

Password

Enter the new password for the user.

Reset on Next Logon

Check the Reset on Next Logon check box to reset
                                             					 or change the password after a successful sign-in.

This field is enabled only for the local users.

Confirm Password

Reenter the new password for the user.

Unified CM Cluster

Select a Unified CM cluster. This is required when you change a
                                             					 local user to remote user. You can also change the Unified CM cluster of an
                                             					 existing remote user to another Unified CM Cluster.

The
                                                         						Unified CM Cluster drop down box are enabled only when the authentication mode
                                                         						is selected as remote.

Update button

Applies changes made from the Modify User page.

User
                                                         						authentication at passphrase change is valid only for the Cisco ER
                                                         						Administration page. Active sessions of the user in any of the other navigation
                                                         						pages do not get cancelled.

Cancel Changes button

Cancels changes made to the Modify User page.

Add new User

Click this button to add a new user. The Add User page appears. See Table 1 for more information.

Activate User

Click Activate User to activate the user account.

The option is enabled only when that particular user is
                                             					 inactive.

The option is always disabled for remote users.

Unlock User

Click Unlock User to unlock the account.

The option is enabled only when that particular user account
                                             					 is locked.

The option is always disabled for remote users.

Displays the groups to which the user is assigned.

Displays the roles to which the user is assigned.

### Change to Remote
                           	 User

The
                                 		  Change to Remote Users page appears when you choose User Management
                                    			 > User and click Change to Remote
                                    			 Users on the Find and List Users page.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator authority to access this page.

#### Description

Use the
                                 		  Change to Remote Users page to change the authentication mode of the local user
                                 		  to remote user.

The
                                 		  following table describes the Remote User page.

Field

Description

Unified CM Cluster

Select the Unified CM Cluster from the drop-down box to remotely
                                             					 authenticate the selected users.

Selected Users

Displays the local users that change to remote users.

Update button

Applies changes made from the Change to Remote Users page.

Close button

Closes the window.

## Find and List
                        	 Roles

The Find
                              		  and List Roles page appears when you choose User Management
                                 			 > Role .

### Authorization
                              		  Requirements

You must
                              		  have system administrator authority to access this page.

### Description

Use the
                              		  Find and List Role page to find, list, modify, and delete current roles, and to
                              		  add new roles.

The
                              		  following table describes the Find and List Roles page.

Field

Description

Find Role where Role Name is

Enter search criteria to select the role you want to find.

To find all roles, click Find without entering any criteria.

To narrow your search, use the pull-down menu to select the
                                          					 search condition (contains, Starts with, and so on) and enter the role in the
                                          					 text box. You can also select how many results per page are displayed from the
                                          					 pull-down menu. When you have specified your search criteria, click Find .

Section of the page in which the search results are displayed.
                                          					 These default roles are created during installation:

- Emergency Responder System
                                             						Admin

- Emergency Responder ERL Admin

- Emergency Responder Network
                                             						Admin

- Emergency Responder User

When you click on the Role Name link or the Description link for
                                          					 any of the default roles, the Standard Role page for that role displays, which
                                          					 displays the following information:

- Role Name

- Description

- List of resources assigned to
                                             						that role

You cannot
                                                      						modify any of the information for default roles. You can only modify
                                                      						information for roles that you create.

After you create additional roles, they are listed along with
                                          					 the default roles. When you click on the role name, description, or Edit icon
                                          					 for a role that you have created, the Modify Role page appears. See Table 1 for more information about the
                                          					 Modify Role page.

Edit icon

Click the Edit icon to display the Modify Role page. See Table 1 for information about the Modify
                                          					 Role page.

Delete icon

Click the Delete icon to delete the role from the system.

You cannot
                                                      						delete any of the default roles.

Add New Role button

Click Add New
                                             						Role to display the Add Role page. This button is also available on the
                                          					 Modify Role and Add Role pages. See Table 1 for information about the Add Role
                                          					 page.

### Add Role

The Add
                                 		  Role page appears when you choose User Management
                                    			 > Role and click Add new Role on the Find and List Roles page. You can also access the Add Role page from the
                                 		  Modify Role and Standard Role pages. See Modify Role for more information.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator authority to access this page.

#### Description

Use the
                                 		  Add Role page to add a new role to the system.

The
                                 		  following table describes the Add Role page.

Field

Description

Role Name

The name of the new role you are adding.

Description

A
                                             					 description of the new role.

This section of the page displays a list of all available
                                             					 resources. The check boxes to the left of each resource allow you to select or
                                             					 deselect the resource to be assigned to the new role.

Select All button

Click Select
                                                						All to select all the listed resources.

Clear All button

Click Clear
                                                						All to deselect all currently selected resources.

Insert button

Click Insert to add the new role.

Cancel Changes button

Click Cancel
                                                						Changes to cancel the Add Role operation.

### Modify Role

The
                                 		  Modify Role page appears when you choose User Management
                                    			 > Role , search for a role, and then click on a role name, description, or the Edit icon
                                 		  associated with the role on the Find and List Roles page.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator authority to access this page.

#### Description

Use the
                                 		  Modify Role page to modify information for an existing role.

You cannot modify
                                             			 any information for the four default roles.

The
                                 		  following table describes the Modify Role page.

Field

Description

Role Name

The name of the new role you are modifying.

The Role
                                                         						Name cannot be changed.

Description

A
                                             					 description of the role you are modifying. Modify the description by adding new
                                             					 text in the text box.

This section of the page displays a list of all available
                                             					 resources. The check boxes to the left of the resources indicate which
                                             					 resources have been assigned to this role. Modify the resource assignments by
                                             					 checking or unchecking the boxes.

Select All button

Click Select
                                                						All to select all the listed resources.

Clear All button

Click Clear All to deselect all currently selected resources.

Update button

Click Update to save the changes made to the Modify Role page.

Cancel Changes button

Click Cancel
                                                						Changes to cancel the changes made to the Modify Role page.

Add new Role button

Allows you to add a new role. See the Add Role for information about adding new
                                             					 roles.

## Find and List User
                        	 Groups

The Find
                              		  and List User Groups page appears when you choose User Management
                                 			 > User Group .

### Authorization
                              		  Requirements

You must
                              		  have system administrator authority to access this page.

### Description

Use the
                              		  Find and List User Groups page to find, list, modify, and delete current user
                              		  groups, and to add new user groups.

The
                              		  following table describes the Find and List User Groups page.

Field

Description

Find User Group where User Group Name

Enter search criteria to select the user group you want to find.

To find all user groups, click Find without entering any criteria.

To narrow your search, use the pull-down menu to select the
                                          					 search condition (contains, Starts with, and so on) and enter the user group in
                                          					 the text box. You can also select how many results per page are displayed from
                                          					 the pull-down menu. When you have specified your search criteria, click Find .

Section of the page in which the search results are displayed.
                                          					 When you click on the User Group Name link, the Description link, or the Edit
                                          					 icon, the Modify User Group page appears. See Modify User Group for information.

Edit icon

Click the Edit icon to display the Modify User Group page. See Modify User Group for information.

Delete icon

Click the Delete icon to delete the user group from the system.

You cannot
                                                      						delete default user groups that were created during installation.

Add New User Group button

Click the Add New
                                             						User Group button to display the Add User Group page. See Table 1 for information about the Add User
                                          					 Group page.

### Add User
                           	 Group

The Add
                                 		  User Group page appears when you choose User Management
                                    			 > User Group and click Add new User Group on the Find and List User Groups page. You can also access the Add
                                 		  User Group page from the Modify User Group page. See Modify User Group for more information.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator authority to access this page.

#### Description

Use the
                                 		  Add User Group page to add a new user group to the system.

The
                                 		  following table describes the Add User Group page.

Field

Description

User Group Name

The name of the new user group you are adding.

Description

A
                                             					 description of the new user group.

This section of the page has a text box that displays the names
                                             					 of the users you add to the user group.

Add Users button

Allows you to add users to the new group. When you click Add
                                                						Users , the Add Users page appears. See Add User for more information.

Remove Users button

Allows you to remove users from the group. To do so, highlight
                                             					 the username in the text box and click Remove
                                                						Users .

This section of the page has a text box that displays the roles
                                             					 you assign to the new user group.

Add Roles button

Allows you to assign roles to the new group. When you click Add
                                                						Roles , the Add Roles page appears. See Add Role for more information.

Remove Roles button

Allows you to remove roles from the group. To do so, highlight
                                             					 the role name in the text box and click Remove
                                                						Roles .

Insert button

Click Insert to add the new role.

### Modify User
                           	 Group

The
                                 		  Modify User Group page appears when you choose User Management
                                    			 > User Group , search for a user group, and then click a user group name, description, or the Edit icon associated with the user group on the
                                 		  Find and List User Groups page.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator authority to access this page.

#### Description

Use the
                                 		  Modify Role page to modify information for an existing user group.

The
                                 		  following table describes the Modify User Group page.

Field

Description

User Group Name

The name of the user group you are modifying.

The User
                                                         						Group Name cannot be changed.

Description

A
                                             					 description of the User Group you are modifying. Modify the description by
                                             					 adding or changing text in the text box.

This section of the page has a text box that displays the names
                                             					 of the users currently in the user group.

Add Users button

Allows you to add more users to the group. When you click Add
                                                						User , the Add User page appears. See Add User for more information.

Remove Users button

Allows you to remove users from the group. To do so, highlight
                                             					 the username in the text box and click Remove
                                                						Users .

This section of the page has a text box that displays the roles
                                             					 currently assigned to the user group.

Add Roles button

Allows you to assign more roles to the group. When you click Add
                                                						Roles , the Add Role page appears. See Add Role for more information.

You cannot
                                                         						add roles to the default roles that were assigned to a default user group
                                                         						during installation. If the user group that you are modifying is a default user
                                                         						group, then the Add
                                                            						  Roles button is not visible.

Remove Roles button

Allows you to remove roles from the group. To do so, highlight
                                             					 the role name in the text box and click Remove
                                                						Roles .

You cannot
                                                         						remove the default roles that were assigned to a default user group during
                                                         						installation. If the user group you are modifying is a default user group, then
                                                         						the Remove
                                                            						  Roles button is not visible.

Update button

Click Update to save the changes made to the Modify User Group page.

Add New User Group button

Allows you to add a new user group. See Add User Group for information.

## Credential Policy
                        	 Page

The Credential Policy page appears when you choose User
                                    				Management > User Settings > Credential Policy or EnhancedSecurityMode Credential Policy .

The
                                                				  Credential Policy option is enabled when the system is in the normal mode.

The
                                                				  EnhancedSecurityMode Credential Policy option is enabled when the system is in
                                                				  Enhanced Security Mode.

Local administrator accounts will never expire as they are always configured as standard users. Hence, if you update any credential
                                                policy or EnhancedSecurityMode credential policy for a local administrator the changes won't take effect.

### Authorization
                              		  Requirements

You must have
                              		  system administrator authority to access this page.

### Description

Use the Credential Policy page to update policy values in the
                              		  EnhancedSecurityMode or in the normal mode depending on the security level
                              		  required.

The following table describes the Credential Policy field settings.

Field

Description

Display Name

Credential Policy or EnhancedSecurityMode Credential Policy name is displayed based on the option selected by you.

Failed Logon

Specify the number of failed sign-in attempts allowed.

You can enter a number between 1 to100.

To allow unlimited failed sign-ins, check the No Failed Logon check box.

The default setting specified for Cisco Emergency Responder (Emergency Responder) in a normal mode is set to 0 (if Emergency Responder is upgraded from pre 11.5 version) or 5 (if Emergency
                                                      Responder 11.5 is a fresh installation) or 3 (if Emergency Responder is in Enhanced Security Mode).

Reset Failed Logon Attempts Every (minutes)

Specify the number of minutes after which the counter is reset for failed sign-in attempts. You can log in again after the
                                          counter is reset.

Enter a number between 1 to120.

The default setting specified for Emergency Responder in normal mode is 1 (if Emergency Responder is upgraded from pre 11.5
                                          version) or 30 (if Emergency Responder 11.5 is a fresh installation) or 30 (if Emergency Responder is in Enhanced Security
                                          Mode).

Credential Expires After (days)

Specify the number of days after which the credential or password expires.

Enter a number between 0 to 365.

To allow credentials to never expire, enter 0 or check the Never Expires check box.

The default setting is 0. Never Expires check box is checked if Emergency Responder is in normal mode (for both upgrade and fresh installation) and 180 if Emergency
                                          Responder is in Enhanced Security Mode.

Minimum Credential Length

Specify the minimum length for user credentials (password).

Do not enter 0 as blank passwords are not allowed. Enter a number between1 to 64.

Validation of, one uppercase, one lowercase, one numeric, and one special character on password happens only when the value
                                          is greater than or equal to four.

The default setting is 1 if Emergency Responder is in normal mode (for both upgrade and fresh installation) and 14 if the
                                          Emergency Responder is in Enhanced Security Mode.

Minimum number of character changes between successive credentials

Specify the minimum characters that should be changed while updating a new password.

Enter a number between of 0 to 64. The value should never be greater than the Minimum Credential Length field value.

The default setting specified is 1 if Emergency Responder is in normal mode (for both upgrade and fresh installation) and
                                          4 if Emergency Responder is in Enhanced Security Mode.

Stored Number of Previous Credentials

Specify the number of previous user credentials to store. This setting prevents a user from configuring a recently used credential
                                          that is saved in the user list.

Enter a number between 0 to 25. If you do not want to save any old credentials, enter 0.

The default setting specified is 0 if Emergency Responder is in normal mode (for both upgrade and fresh installation) and
                                          12 if Emergency Responder is in Enhanced Security Mode.

Inactive Days Allowed

Specify the number of days that an account can remain inactive before the account gets deactivated.

Enter a number between 0 to 5000. If you never want the account to be inactive, enter 0.

The default setting specified is 0 for Emergency Responder both in the normal mode (for both upgrade and fresh installation)
                                          and in the Enhanced Security Mode.

Expiry Warning Days

Enter a number between 0 to 90 to specify the number of days before a user password expires and to start receiving warning
                                          notifications.

The value should never be greater than the Credential Expires After (days) field.

The default setting specified is 0 for Emergency Responder both in the normal mode (for both upgrade and fresh installation)
                                          and in the Enhanced Security Mode.

Save

Click the Save button to save the changes.

Clear Changes

Click the Clear Changes button to clear any change done in the fields and to restore the last saved information.

Set to Default

Click the Set to Default button to restore the default values settings depending on the Cisco Emergency Responder mode.

## Call History

The Call
                              		  History page appears when you choose Reports > Call
                                 			 History .

### Authorization
                              		  Requirements

You must
                              		  have system administrator, ERL administrator, network administrator, or user
                              		  authority to access this page.

### Description

Use the
                              		  Call History page to view the history of emergency calls made from your
                              		  network. Emergency Responder maintains the most recent 10,000 call history
                              		  records. There is no restriction on when these calls were placed.

The
                              		  following table describes the Call History page.

Field

Description

Search criteria

Enter search criteria to select the calls you want to find.

To find all calls, click Find without entering any criteria.

To narrow your search:

- Select All to indicate that only calls that match every criteria be selected (an AND
                                             						search); select Any to indicate that calls that match any search criteria be selected (an OR
                                             						search). From the pull down menu, select the field that you want to search on
                                             						(ERL Name, Caller Extension, and so on), select the search relationship
                                             						(contains, begins with, and so on), and enter the search string.

- To search on a combination of
                                             						fields, click the Plus icon (+) to add additional search parameters. Click the Minus icon ( – ) to remove search parameters.

- When you have entered all of
                                             						the search parameters, click Find .

A
                                          					 list of emergency calls that match your search criteria is displayed with the
                                          					 following information:

- ERL Name—Click the name to
                                             						view details about the ERL and its ALI information. See Conventional ERL for descriptions of the
                                             						configuration fields.

- Caller Extension—The
                                             						extension used to place the emergency call.

- Time—The time the call was
                                             						made.

- Date—The date the call was
                                             						made.

- Route Pattern-ELIN No.—The
                                             						route pattern and ELIN combination used for the call. See Conventional ERL for more detailed information about
                                             						these fields.

- Location—The location of the
                                             						phone based on whether the phone was configured manually, or whether it was
                                             						configured based on the switch port or IP subnet.

- Call Acknowledged—The
                                             						acknowledged status of a call on the Web Alert page.

- Acknowledged By—The ID of the
                                             						user who acknowledged the call.

- Time Acknowledged—The time
                                             						that the call was acknowledged.

- Date Acknowledged—The date
                                             						that the call was acknowledged.

- Comments—Any comments entered
                                             						about the call. If you click the Edit icon, the Call Details page appears, on which you can enter or change comments
                                             						about the call in the Comments
                                                						  about the call text box.

If a large number of calls match your search criteria, the
                                          					 system uses several pages to display them. Use the First, Previous, Next, and
                                          					 Last links at the bottom of the page to move between pages. You can also enter
                                          					 a specific page number in the Page field and press Enter to move to that page.

Download

Click Download to save the call history data to a spreadsheet that
                                          					 you can view or download to your local system.

Update

Click Update to include your comments in the call history for the call.

Only
                                                      						viewable from the Call Details page.

Cancel Changes

Click Cancel
                                             						Changes to remove unsaved comments. You can then reenter comments.

Only
                                                      						viewable from the Call Details page.

Close

Click Close to close the Call Details page.

Only
                                                      						viewable from the Call Details page.

## ERL Audit
                        	 Trail

The ERL
                              		  Audit Trail page appears when you perform one of these actions:

Choose Reports >
                                       				  ERL Audit Trail .

Click view in
                                    				the Audit Trail column for an ERL displayed on the ERL Configuration page
                                    				(opened by choosing ERL >
                                       				  Conventional ERL .)

### Authorization
                              		  Requirements

You must
                              		  have system administrator, ERL administrator, or network administrator
                              		  authority to access this page.

### Description

Use the
                              		  ERL Audit Trail page to view the change history for ERLs.

The
                              		  following table describes the ERL Audit Trail page.

Field

Description

Search criteria

Enter search criteria to select the audit details that you want
                                          					 to find.

To find all audit details, click Find without entering any criteria.

To narrow your search:

Select All to indicate that only audit details that match every criteria be selected (an AND search); select Any to indicate that audit details that match any search criteria be selected (an OR search). From the pull-down menu, select
                                                the field that you want to search on (ERL Name, Modified By, and so on), select the search relationship (contains, begins
                                                with, and so on), and enter the search string. If searching by ERL Name, you can type in the ERL name or use the pull-down
                                                menu to select an ERL.

To search on a combination of fields, click the Plus icon (+) to add additional search parameters. Click the Minus icon ( – ) to remove search parameters.

When you have entered all of the search parameters, click Find .

A
                                          					 list of ERL change records that match your search criteria. Each change to an
                                          					 ERL is recorded in a separate record, so a single ERL may have many audit
                                          					 records. The list displays the following information for each record:

ERL Name—The name of the ERL that was changed.

Modified By—The login ID of the user who changed the ERL.

Modified Time—The date and time the ERL was changed.

Modification Details—A list of the fields that were changed in the ERL or its ALI. Use the scroll bars to move up and down
                                                in the Modification Details text box.

If there
                                                      						are a large number of records match your search, Emergency Responder uses more
                                                      						than one page to list them. Use the links at the bottom of the list to move
                                                      						from page to page. You can also enter a page number in the Page field and press Enter to go to a specific page.

## Export PS-ALI
                        	 Records

The
                              		  Export PS-ALI Records page appears when you choose Tools > Export
                                 			 PS-ALI Records .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the
                              		  Export PS-ALI Records page to create a file in a NENA format that you can send
                              		  to your service provider. Your service provider uses this file to update their
                              		  ALI data for your organization. Your service provider needs this information so
                              		  that emergency calls from your ERLs can be routed to the correct public safety
                              		  answering point (PSAP).

Always
                              		  submit an export file to your service provider. If you do not submit an export
                              		  file, subsequent export files might not have correct command information for
                              		  the database update, and you must manually edit the export file to make it
                              		  uploadable. Your service provider can provide you with error information if the
                              		  database upload fails.

If you change the
                                          			 customer code in your ALI record, Emergency Responder generates two records
                                          			 when exporting ALI: a Delete record to remove the ALI with the old code, and an
                                          			 Insert record to add the ALI with the new code. This Delete and Insert sequence
                                          			 is only generated the first time you export ALI after changing the code. You
                                          			 must ensure that you submit this export file to the service provider.

You can
                              		  also use export files to back up your ERL configuration. ELIN must be
                              		  associated to an ERL while exporting PS-ALI records.

The
                              		  following table describes the Export RS-ALI Records page.

Field

Description

Select NENA Format

The file format to be used in the export file, NENA formats 3.0,
                                          					 2.1, or 2.0.

File to Export

The name of the file you want to create. Do not include a file
                                          					 extension.

Company Name (NENA Header field)

The name of your company. You cannot have spaces in the name.

The data
                                                      						complies with NENA requirements.

Cycle Counter (NENA Header field)

The sequence in which this export is created. This field is
                                          					 automatically increased each time you export data. You can change it if it
                                          					 becomes unsynchronized with the sequence submitted to your service provider.
                                          					 However, changing the sequence number does not affect the data placed in the
                                          					 file; if you are redoing an export, you must manually edit the export file to
                                          					 change the record status fields.

The data
                                                      						complies with NENA requirements.

End of Line Format

Allows you to select the end-of-line format for the PS-ALI
                                          					 records that is exported for download. You can select from the following two
                                          					 formats:

- Windows style (\r\n)

- Unix/Linux style (\n)

Export button

Click Export to create the export file.

Download File

Click Download
                                             						File to download an exported PS-ALI file.

Cancel button

Click Cancel to cancel the export operation.

## PS-ALI
                        	 Converter

The
                              		  PS-ALI Converter page appears when you choose Tools > PS-ALI
                                 			 Converter .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the
                              		  PS-ALI Converter tool to generate an ERL file that can be accepted by the
                              		  Emergency Responder ERL. The PS-ALI Converter tool converts ALI files from a
                              		  NENA 2.0 format into a csv (comma-separated value) text file. You can then
                              		  modify the csv file (for example, to add or change an ERL name) and save the
                              		  modified ERL details by importing the file into Emergency Responder.

If you change the
                                          			 customer code in your ALI record, Emergency Responder generates two records
                                          			 when exporting ALI: a Delete record to remove the ALI with the old code, and an
                                          			 Insert record to add the ALI with the new code. This Delete and Insert sequence
                                          			 is only generated the first time you export ALI after changing the code. You
                                          			 must ensure you submit this export file to the service provider.

Field

Description

Select PS-ALI file (NENA 2.0 format)

The name of the PS-ALI file to be converted. The file must be in
                                          					 the default format, NENA format 2.0.

Output File (in csv format) Name

The name of the csv file that you want to create.

Convert button

Click Convert to create the csv file.

Cancel button

Click Cancel to stop the converting process. and close the window.

### PS-ALI Records
                           	 Download

Download File
                                 		  appears when you choose Export PS-ALI records->Download

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

The Exported PS-ALI
                                 		  Records can be downloaded from here using the download button.

Field

Description

Select a file to Download

Use the pull-down menu to select a file and click Download to download the file to your local system.

Close
                                             					 button

Click Close to close the window.

## ERL Debug
                        	 Tool

The ERL
                              		  Debug Tool page appears when you choose Tools > ERL
                                 			 Debug Tool .

### Authorization
                              		  Requirements

You must have a system administrator or ERL administrator authority to access this page.

### Description

The ERL
                              		  Debug Tool takes the phone extension as input and displays the ERLs currently
                              		  being used for routing emergency calls for the phones.

Use this
                              		  diagnostic tool to verify the Emergency Responder configuration during the ERL
                              		  creation and the ERL assignment phase and to troubleshoot calls directed to
                              		  incorrect ERLs.

In a scenario where a Dual-stack phone has both the IPv4 and IPv6 addresses configured, and the phone falls under both the
                                          IPv4 and IPv6 subnets having the same priority, and one of the subnets is trackable and the other one is non-trackable, the
                                          phone is considered to be trackable.

The
                              		  following table describes the ERL Debug Tool page.

Field

Description

Find Phones where extension

Enter search criteria to select the extensions that you want to
                                          					 find.

To find all extensions, click Find without entering any criteria.

To narrow your search, use the drop-down menu to select the search condition (contains, Starts with, and so on) and enter
                                          the extension in the text box. You can also select how many results per page are displayed from the drop-down menu. When you
                                          have specified your search criteria, click Find .

Matching records

Section of the page that displays the ERLs currently being used
                                          					 for routing emergency calls for the phones. For each extension found, the
                                          					 following information is displayed:

Phone extension

ERL

Phone IPv4 Address

Phone IPv6 Address

MAC Address

Why this ERL is Used?

If the configurations are not correct, make any required
                                          					 changes.

Export
                                          					 button

Click Export to create the export file.

### ERL Debug Tool
                           	 Export

The Export ERL Debug
                                 		  Tool page appears when you click Export in the
                                 		  ERL Debug Tool page.

#### Authorization
                                 		  Requirements

You must
                                 		  have system administrator or ERL administrator authority to access this page.

#### Description

Use the Export ERL
                                 		  Debug Tool page to create a file which shows phone extension with ERLs
                                 		  currently being used for routing emergency calls for the phones.

Field

Description

Select Export Format

The format to use for the file, such as CSV (comma-separated
                                             					 values).

Enter Export
                                             					 File Name

The name of the file you want to create. Do not include the file
                                             					 extension.

Export
                                             					 button

Click Export to create the file. The Status box shows the status of the exportation.

Close button

Click Close to close the window.

Download

Select a
                                             					 File to Download

Use the
                                             					 pull-down menu to select a file and click Download to download the file to your local system.

## ALI Formatting
                        	 Tool

The ALI
                              		  Formatting Tool page appears when you choose Tools > ALI
                                 			 Formatting Tool .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the
                              		  ALI Formatting Tool page to customize the format of PS-ALI records to
                              		  facilitate error-free PS-ALI record transactions with service providers.

The ALI
                              		  Formatting Tool (AFT) reads the NENA file generation by the Emergency Responder
                              		  and displays all ELIN records. You can then do one or more of the following:

View the details
                                    				of the ALI records

Select a record
                                    				and update the value for ALI fields, which can be edited using the AFT

Perform a bulk
                                    				update operation on multiple ALI records

Selectively
                                    				export ALI records based on area code, city code, and so on

The
                              		  following table describes the ALI Formatting Tool page.

Field

Description

Use the pull-down menu to select a service provider

Use the pull-down menu to select an input file

Submit button

Click the Submit button to display the Search for ELINs page, which is described in Table 2 .

The
                              		  following table describes the Search for ELINs page.

Field

Description

Allows you to search ELINs by Local Code, Area Code, or City
                                          					 Code.

Add (+) button

Adds more search parameters

Remove (-) button

Removes search parameters

The
                              		  following table describes the Bulk Update page.

Field

Description

Remove Changes/Generate File button

Shows all the ELINs that have been changed.

Search for ELIN

Displays the ELIN search page.

The
                              		  following table describes the Review Changes/Generate File page.

Field

Description

Add More ELIN

Displays the remaining ELINs that have not been changed.

Remove ELIN

Removes the selected ELINs from the list

Search for ELIN

Displays the ELIN search screen

Generate File button

Generates the formatted file.

The
                              		  following table describes the Download Formatted File page.

Field

Description

Download Formatted File button

Displays a Download File dialog box so that the formatted file
                                          					 can be downloaded to the local system.

## File Management
                        	 Utility

The File
                              		  Management Utility page appears when you choose Tools > File
                                 			 Management Utility .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the
                              		  File Management Utility page to search for, download, or delete exported files.

The
                              		  following table describes the File Management Utility page.

Field

Description

From the pull-down menu, select the type of file that you want
                                          					 to search for.

Search button

Click Search to perform the search.

Area of the page that displays the search results. Displays the
                                          					 File Name, Last Modified data, and File Size for each file found.

Download button

Downloads the selected file.

Before you
                                                      						click Download , click in the box next to the file name to select
                                                      						the file. To select all files listed, click in the box next to the File Name
                                                      						column heading.

Delete button

Deletes the selected file.

Before you click Delete , click in the box next to the file name to select the file. To select all files listed, click in the box next to the File
                                                      Name column heading.

## Purge Call
                        	 History

The Purge
                              		  Utility for Call History page appears when you choose Tools > Purge
                                 			 Utility .

### Authorization
                              		  Requirements

You must
                              		  have system administrator or ERL administrator authority to access this page.

### Description

Use the
                              		  Purge Call History Utility to delete call history records that are older than
                              		  an age that you specify. You can use this utility to purge records immediately
                              		  or schedule daily purging of call history records. Emergency Responder logs the
                              		  results of the purge in the Emergency Responder Administration logs.

The
                              		  following table describes the purge utility page.

Field

Description

Displays status messages

Purge Data older than

Specify the age of record that you want to delete.

Daily Purge at

Specify a time (UTC) during the day at which old records are deleted.

Purge Data older than

Specify the age of record that you want to delete.

Update

Click Update to save and activate your changes.

Cancel

Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings.

## SAML Single
                        	 Sign-On

The SAML Single
                              		  Sign-On page appears when you choose Cisco ER
                                    				Administration > System > SAML Single
                                    				Sign-On .

### Authorization
                              		  Requirements

You
                              		  must have system administrator authority to access this page.

### Description

SAML Single
                                 			 Sign-On (SSO) page is used to enable or disable Single Sign-On, on Cisco
                                 			 Emergency Responder . It also allows you to import IdP metadata and
                              		  export Cisco
                                 			 Emergency Responder metadata. You cannot access the Disaster Recovery
                                 			 System and Cisco
                                 			 OS Unified Administration pages, when Single Sign-On is enabled
                              		  on Cisco Emergency
                                 			 Responder , you need to have the normal admin credentials to access
                              		  these pages. For more information on the configuration settings, see "SAML Single
                                 			 Sign-On" chapter in Cisco
                                 			 Emergency Responder Administration Guide at http://www.cisco.com/c/en/us/support/unified-communications/emergency-responder/products-maintenance-guides-list.html

Field

Description

Status

Displays
                                             					 status messages.

Server
                                             					 Name

Specifies
                                             					 the names of all the servers in the server group.

SSO
                                             					 Status

Indicates that the SAML Single Sign-On is enabled on the server.

Indicates that SAML Single Sign-On is disabled on the server.

Re-Import
                                             					 Metadata

This
                                                            						  option is displayed as N/A (Not Applicable) for the publisher node.

Last
                                             					 Metadata Import

Specifies
                                             					 the time when the IdP metadata was last imported on the server. This field
                                             					 displays "Never" if you are running the SAML Single Sign-On setup for
                                             					 the first time.

Export
                                             					 Metadata

Export Metadata field is enabled only when Single
                                             					 Sign-On is successfully enabled on both publisher and the subscriber. Click the Export
                                                						Metadata icon to download the server metadata file. A SAML metadata file
                                             					 must be generated for the specified server, and downloaded using the browser.
                                             					 You must then import this metadata file to the IdP server.

Important

If you
                                                         						change the hostname or domain of a node, ensure that you download the metadata
                                                         						from that node and upload the file to the IdP server again.

The Export All Metadata button is enabled by default,
                                             					 regardless of whether the SAML Single Sign-On state set to active.

Last
                                             					 Metadata Export

Specifies
                                             					 the time when the SAML metadata file of the specified server was last exported.
                                             					 This field displays "Never" if you are running the SAML Single Sign-On setup for
                                             					 the first time.

SSO Test

Displays
                                             					 the test results of the SAML configuration with the IdP. The test ensures that
                                             					 the specified server trusts the IdP, and that the IdP trusts the specified
                                             					 server. The trust relationship between the server and the IdP depends on the
                                             					 success of exporting and importing of SAML metadata files.

Indicates that a test has not been performed on this server.

Indicates that a test has been successfully run on this server, and that the
                                                      							 server and the IdP trust one another.

Indicates that a test was attempted on the specified server, but that either
                                                      							 the server does not trust the IdP, or the IdP does not trust the server, or
                                                      							 some other network or IdP issue prevented the test from passing.

Run SSO
                                             					 Test

Click Run
                                                						SSO Test to run the Single Sign-On test. You must run this test before
                                             					 enabling SAML Single Sign-On. The SAML Single Sign-On setup cannot be completed
                                             					 until this test is successful. To run this test, there must be at least one
                                             					 LDAP synchronized user with administrator rights. You must also know the
                                             					 password for that user ID.

You
                                                         						cannot run this test until the IdP metadata file is imported to the server, and
                                                         						the server metadata file is exported to the IdP server.

Enable
                                             					 SAML SSO

Click Enable
                                                						SAML SSO to start the SAML Single Sign-On configuration.

Export
                                             					 All Metadata

Click Export
                                                						All Metadata to export the SAML metadata files from each server. These
                                             					 files are converted to a compressed file (.zip) for easy download. You must
                                             					 extract the file and then import each file to the IdP.

Update
                                             					 IdP Metadata File

Click Update
                                                						IdP Metadata File to update IdP metadata on all the servers in the cluster.

Fix All
                                             					 Disabled Servers

Click Fix
                                                						All Disabled Servers to enable SAML Single Sign-On, on the servers on which
                                             					 it is disabled.

View
                                             					 IdP Trust Metadata File

Click View
                                                						IdP Trust Metadata File to download a copy of the IdP metadata file.

| Field | Description | Notes |
|---|---|---|
| Emergency Responder Groups |
| Emergency Responder Groups list | A
                                          					 list of the Emergency Responder server groups that are pointing to the same
                                          					 cluster database host. Click a group name to view the servers in the group. | The
                                          					 Emergency Responder cluster consists of this set of Emergency Responder groups.
                                          					 You create the cluster when installing Emergency Responder servers. See Installation on a New System . |
| Servergroup Details |
| Emergency Responder Group Name | The
                                          					 name of the server group. | Click the server group name to display the servers in that group
                                          					 in the Servergroup Details section of page. |
| Primary Host Name | The
                                          					 DNS host name or IP address of the primary server in the group. | Click this host name (except for the local server group) to open
                                          					 the Emergency Responder administration page for that server in a new window. |
| Standby Host Name | The
                                          					 DNS host name or IP address of the standby, or backup server in the group. | Click this host name (except for the local Server Group) to open
                                          					 the Emergency Responder administration page for that server in a new window. |
| Delete button | Click Delete to remove the Emergency Responder group you are viewing from the Emergency
                                          					 Responder cluster. | Only system administrators can delete a Emergency Responder
                                          					 group from the cluster. Delete a group from the cluster before you uninstall a Emergency
                                          					 Responder group. |

| Field | Description | Notes |
|---|---|---|
| Emergency Responder Group Name | The name of the server group. This name is used for your information only, so create a name you find useful. |  |
| Peer TCP Port | The TCP port used for communications between Emergency Responder servers within the server group. If you don't want to use
                                          the default port, ensure you select an unused port. | The range is 1024 to 65535. |
| Heartbeat Count | The number of counts an Emergency Responder server should wait before declaring an unresponsive Emergency Responder server
                                          unavailable. | The default number of counts is 3. The range is 3 to 10. The time between counts is defined in Heartbeat Interval. |
| Heartbeat Interval (in sec) | The number of seconds between sending heartbeat messages to the other Emergency Responder server in the server group. | The default is 30 seconds. The range is 30 to 300 seconds. |
| Active Call Timeout (in min) | How long to maintain a call route mapping so the PSAP can call back the emergency caller. | The default is 180 minutes (3 hours). The range is 30 to 1440 minutes. |
| SMTP Mail Server | The IP address or fully qualified name of the mail server (for example, email.domain.com). Check the Enable Secured connection check box to send mails from the SMTP Mail Server in a secure mode. | Configure an email server if you want Emergency Responder to send email or email-based pages to security officers when an
                                          emergency call is made. Ensure to configure the SMTP Mail Server in a secure mode and the SMTP server certificate is added to the Tomcat trust store
                                          of the Cisco Emergency Responder before enabling the check box. Failing to do so may result in email alert delivery failure. The Port number for enabling Secure SMTP connection is 587. To set up a Secure SMTP connection, perform the following: Exchange Cisco Emergency Responder Tomcat certificate chain to SMTP server's root certificate directory. Upload SMTP server certificate chain as tomcat-trust certificates on Cisco Emergency Responder. Restart Cisco Tomcat service on Cisco Emergency Responder servers using the CLI command utils service restart Cisco Tomcat . |
| Source Mail ID | If you configure a mail server, you must enter an email account on that server that can be used for sending email. | Emails or pages sent to security come from this email account. |
| System Administrator Mail ID | Mail account where Emergency Responder sends critical information about the system. | Emails or pages sent to the system administrator by Emergency Responder come to this email account. |
| Calling Party Modification | Dynamic modification of the calling party number. Allows you to reduce the number of route patterns by configuring multiple
                                          ELIN numbers for a single route pattern. ELIN numbers must still be unique. | You must set this flag if you enabled Calling Party Modification when you created Emergency Responder as a Unified CM user. |
| Syslog | Select from the drop-down list that enables and disables the writing of log messages. |  |
| Syslog Server | The name of the server that has the log messages. Enter the fully qualified DNS name of the server, for example, cw2k.domain.com. | Enter the hostname or IP address of the syslog server to accept syslog messages. This server handles the logging of all the
                                          Cisco Emergency Responder application event-related information. 514 is the default port used to communicate. Note You can only enter a server name if you choose Enable Syslog . | Note | You can only enter a server name if you choose Enable Syslog . |
| Note | You can only enter a server name if you choose Enable Syslog . |
| Notes | Any notes you want to enter to help you understand the use of the server group. |  |
| Dynamic Tracking of Switch IP Address | Dynamically updates a LAN switch's IP address if it is configured with hostname in Emergency Responder. | This action is not applicable to LAN switches that are added to Emergency Responder using an IP address. |
| Security end user web interface language | Pulldown menu allows you to select the language that is displayed on the users web page—English (US), French (Canada), or
                                          Spanish (Spain). | After you change the language, you must complete the following before the language is displayed on the users web page: Restart Emergency Responder Service in Emergency Responder Serviceability by choosing Tools > Control Center . Restart Cisco Tomcat service using the CLI command utils service restart Cisco Tomcat . Refresh the current Emergency Responder User webpage. |
| Limit Concurrent Sessions | Limits the number of concurrent sessions per user. | Selecting or deselecting this check box enables or disables the Max. number of concurrent sessions drop-down list. |
| Max. number of concurrent sessions | If Limit Concurrent Sessions is enabled, this limit is applicable for all the users. | The limit is imposed separately for each Emergency Responder website: Emergency Responder Administration Emergency Responder Serviceability Emergency Responder User Emergency Responder Admin Utility |
| Enable AXL & Cluster Secured connection | AXL communication with other products and cluster communication is secured. | Ensure the Cisco Unified Communications Manager tomcat-trust certificate and the Cisco Emergency Responder server group certificate is added to the Tomcat trust store of the Cisco Emergency Responder (in both publisher and subscriber). Failing to do so may result in breaking of AXL communication between Cisco Unified Communications Manager and Cisco Emergency Responder , along with the cluster communication within the Cisco Emergency Responder group. |
| Discovery Threshold Time (in hrs) | Set the threshold time after which the Emergency Responder sends you an email alert when the discovery of Cisco IP Phones
                                          or devices is stalled. Emergency Responder should be able track the devices anytime from 6 to 24 hours. Check the Enable Discovery Mail Alert check box to enable the Discovery mail alert option. | The default is 0 hours if you do not enable the Enable Discovery Mail Alert check box. The threshold range is 6 to 24 hours. |
| IPv6 Subnet Configurations have precedence over IPv4 | Check the check box if you want the E911 calls to take precendence of IPv6 subnet over the IPv4 subnet. If you uncheck this
                                          option, IPv4 subnet is given precedence, and the calls are routed via the IPv4 subnet. For more information on the various IPv6/IPv4 precedence scenarios using both dual-stack and single stack devices, see Table 2 . | Note Cisco Jabber devices will not work with IPv6 subnets in Emergency Responder. | Note | Cisco Jabber devices will not work with IPv6 subnets in Emergency Responder. |
| Note | Cisco Jabber devices will not work with IPv6 subnets in Emergency Responder. |
| HTTPS Certificates | This parameter defines the certificates that are supported by the Cisco Tomcat service for establishing HTTPS connections.
                                          This parameter defines whether to enable RSA or both ECDSA and RSA certificates while establishing inbound connections. By
                                          default, the HTTPS interface supports only RSA Certificates. ECDSA certificates are enabled only if the "All Supported EC and RSA Certificates" option is selected. Default: RSA Certificates Only | Note Ensure that you restart the Cisco Tomcat service on all the nodes for the parameter change to take effect. | Note | Ensure that you restart the Cisco Tomcat service on all the nodes for the parameter change to take effect. |
| Note | Ensure that you restart the Cisco Tomcat service on all the nodes for the parameter change to take effect. |
| Update Settings button | Click Update Settings to save and activate your changes. |  |
| Cancel Changes button | Click Cancel Changes to change the fields on this page back to the last saved settings. |  |

| Note | You can only enter a server name if you choose Enable Syslog . |
|---|---|

| Note | Cisco Jabber devices will not work with IPv6 subnets in Emergency Responder. |
|---|---|

| Note | Ensure that you restart the Cisco Tomcat service on all the nodes for the parameter change to take effect. |
|---|---|

| Scenario | IPv6 Subnet Added | IPv4 Subnet Added | IPv6 Precedence Disabled | IPv6 Precedence Enabled |
|---|---|---|---|---|
| New call from IPv6 + IPv4 Dual stack phone | Yes | Yes | Calls are routed via the ERL assigned to the IPv4 subnet | Calls are routed via the ERL assigned to the IPv6 subnet |
| New call from IPv6 + IPv4 Dual stack phone | Yes | No | Calls are routed via the ERL assigned to the IPv6 subnet | Calls are routed via the ERL assigned to the IPv6 subnet |
| New call from IPv6 + IPv4 Dual stack phone | No | Yes | Calls are routed via the ERL assigned to the IPv4 subnet | Calls are routed via the ERL assigned to the IPv4 subnet |
| New call from IPv6 + IPv4 Dual stack phone | No | No | Call is routed using the routing pattern configured for the caller's ERL. If none of the call routing criteria is used to
                                          determine the phone location using the Call Routing Order , the default ERL treatment is provided. | Call is routed using the routing pattern configured for the caller's ERL. If none of the call routing criteria is used to
                                          determine the phone location using the Call Routing Order , the default ERL treatment is provided. |
| New call from IPv6 single stack phone | Yes | Not a valid scenario since the phone has only the IPv6 subnet configured | Calls are routed via the ERL assigned to the IPv6 subnet | Calls are routed via the ERL assigned to the IPv6 subnet |
| New call from IPv6 single stack phone | No | Not a valid scenario since the phone has only the IPv6 subnet configured | Call is routed using the routing pattern configured for the caller's ERL. If none of the call routing criteria is used to
                                          determine the phone location using the Call Routing Order , the default ERL treatment is provided. | Call is routed using the routing pattern configured for the caller's ERL. If none of the call routing criteria is used to
                                          determine the phone location using the Call Routing Order , the default ERL treatment is provided. |
| New call from IPv4 single stack phone | Not a valid scenario since the phone has only the IPv4 subnet configured | Yes | Calls are routed via the ERL assigned to the IPv4 subnet | Calls are routed via the ERL assigned to the IPv4 subnet |
| New call from IPv4 single stack phone | Not a valid scenario since the phone has only the IPv4 subnet configured | No | Call is routed using the routing pattern configured for the caller's ERL. If none of the call routing criteria is used to
                                          determine the phone location using the Call Routing Order , the default ERL treatment is provided. | Call is routed using the routing pattern configured for the caller's ERL. If none of the call routing criteria is used to
                                          determine the phone location using the Call Routing Order , the default ERL treatment is provided. |

| Field | Description | Notes |
|---|---|---|
| Specify telephony attributes |
| Route Point for Primary Emergency Responder Server | The CTI route point that the primary server should use, such as
                                          					 911. | See Create Emergency Call Route Points for more information. |
| Route Point for Standby Emergency Responder Server | The CTI route point that the standby server should use, such as
                                          					 912. Configure this number as the call forward number for the primary emergency
                                          					 number. | See Create Emergency Call Route Points for more information. |
| PSAP Callback Route Point Pattern | CTI route point that you defined to receive calls from the
                                          					 public safety answering point (PSAP). For example, 913XXXXXXXXXX (913 plus ten
                                          					 Xs). The number can only consist of numbers and Xs. | For more information, see Create Emergency Call Route Points . |
| ELIN Digit Strip Pattern | Digits to strip from the beginning of the PSAP Callback Route
                                          					 Point Pattern, for example, 913. The number that results from stripping the
                                          					 pattern should be the ELIN numbers that the PSAP can use to call into your
                                          					 network. | This string must be part of the PSAP Callback Route Point
                                          					 Pattern. |
| Default
                                          					 ELIN Digit Translation | ELIN number obtained after stripping 913 is matched to a callers extension. If the mapping is not found, Emergency Responder
                                          will translate ELIN to Default ELIN Digit Translation number and complete the PSAP Call-back. | The number could be a dialable extension number or a route pattern. If the number is not reachable the PSAP Call-back will
                                          receive a reorder tone. |
| UDP Port Begin | Port numbers that are used by CTI ports during their
                                          					 registration. | The range is 1024 to 65535. |
| Inter-Emergency Responder Group Route Pattern | Route pattern that other Emergency Responder groups use to route
                                          					 emergency calls to this group, for example, 1000.911. The pattern can only consist of numbers and dots. | For a more detailed explanation of this number, see "Create route patterns for Inter-Cisco Emergency Responder Group Communications". |
| IP
                                          					 Type of service (00-FF) | Value of the type of service (ToS) byte in the IP header. The
                                          					 default 0xB8 implies a ToS class of Priority Queue. It is recommended that this
                                          					 default value be used for Emergency Responder. | The ToS value entered here only applies to the RTP packets sent
                                          					 by Emergency Responder for the onsite audio alert feature. |
| Onsite Alert Prompt Repeat Count | Number of times the prompt is played on the onsite alert phone. |  |
| Use IP Address from call signaling | If
                                          					 this parameter is enabled, Emergency Responder obtains the IP address of the
                                          					 phone from JTAPI. This parameter is used to route the call. If an IP subnet is
                                          					 configured for the phone, this parameter setting takes precedence over any
                                          					 other manual configuration. If
                                          					 this parameter is disabled, Emergency Responder uses the manual configuration
                                          					 of the phone to route the call. Note The feature is mainly for Analog Phones (which are manually defined). This option can be tracked behind IP Gateways and receive
                                                   IP Subnet treatment. | Note | The feature is mainly for Analog Phones (which are manually defined). This option can be tracked behind IP Gateways and receive
                                                   IP Subnet treatment. | This field is applicable only if Emergency Responder is configured with Cisco Unified Communications Manager 6.x and above. |
| Note | The feature is mainly for Analog Phones (which are manually defined). This option can be tracked behind IP Gateways and receive
                                                   IP Subnet treatment. |
| Update Settings button | Click Update
                                             						Settings to save and activate your changes. |  |
| Cancel Changes button | Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings. |  |
| National E911 Service Provider Route Pattern Settings |
| National E911 Service Provider Route/Translation Pattern | Enter the route patterns or translation pattern for an National E911 Service Provider emergency response location (ERL). An National E911 Service Provider ERL is an ERL that is serviced by National E911 Service Provider . National E911 Service Provider ERL only lists the route patterns that have been configured on this page. You can add new route patterns or translation patterns,
                                          or you can update or remove existing route patterns or translation patterns. National E911 Service Provider Route Pattern Settings supports a maximum of 3000 characters in total. | To add a new route or translation pattern, click on the text
                                          					 box, enter the route pattern, including numbers and wildcard (do not use
                                          					 spaces), and click Add . To update an existing route pattern, click on the appropriate
                                          					 route pattern, modify the pattern, and click Update . To remove an existing route pattern, click on the appropriate
                                          					 route pattern and click Remove . To cancel your existing changes and go back to the last saved
                                          					 settings, click Cancel
                                             						Changes. |

| Note | The feature is mainly for Analog Phones (which are manually defined). This option can be tracked behind IP Gateways and receive
                                                   IP Subnet treatment. |
|---|---|

| Note | You cannot modify
                                          			 the host name of the server. |
|---|---|

| Field | Description | Notes |
|---|---|---|
| Status | Displays the status of the Server Settings Emergency
                                          					 ResponderServerGroup page. |  |
| Select Server |
| Server | List of servers you have already created. Click on a server name
                                          					 to see the settings for that server. | You can configure a maximum of two servers per server group. |
| Modify Server Settings |
| Server Name | The name of the server. | Change this server name field to any desired value. |
| Host Name | The DNS name of the Emergency Responder server. | This field cannot be modified. |
| Debug Package List | A
                                          					 selection of subsystems for which you must collect detailed debug information.
                                          					 Debug information includes trace messages as well as more detailed messages.
                                          					 Only select subsystems at the request of Cisco Technical Support; the debug
                                          					 information is for Cisco's use to help resolve problems that you cannot solve
                                          					 yourself. | See Trace and Debug Information for an explanation of each field. |
| Select All button | Selects all subsystems in the Debug Package List. |  |
| Clear All button | Clears all selected subsystems in the Debug Package List. |  |
| Trace Package List | A
                                          					 selection of subsystems for which you must collect brief trace information.
                                          					 Only select subsystems at the request of Cisco Technical Support; the trace
                                          					 information is for Cisco's use to help resolve problems that you cannot solve
                                          					 yourself. If
                                          					 you select a subsystem for debug, you do not have to select it for trace. | See Trace and Debug Information for an explanation of each field. |
| Select All button | Selects all subsystems in the Trace Package List. |  |
| Clear All button | Clears all selected subsystems in the Trace Package List. |  |
| Update Settings button | Click Update when viewing an existing server's settings to save
                                          					 changes you make to the settings. | Only available when viewing the settings of an existing server. |
| Cancel Changes button | Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings. |  |

| Field | Description |
|---|---|
| Status | Displays the steps to register with Cisco Smart Software Manager or Cisco Smart Software Manager satellite and the current
                                          license registration mode. For information on alarms or licensing alerts and compliance, see License Manager Status Messages and License Compliance . Note For Specific License Reservation status message displays current license status. Note For Permanent License Reservation, status message displays the number of licenses that the administrator specified for this
                                                      system to operate within. License count does not affect compliance status and it is for administrator reference only. Admin can set the license count through Command Line Interface. | Note | For Specific License Reservation status message displays current license status. | Note | For Permanent License Reservation, status message displays the number of licenses that the administrator specified for this
                                                      system to operate within. License count does not affect compliance status and it is for administrator reference only. Admin can set the license count through Command Line Interface. |
| Note | For Specific License Reservation status message displays current license status. |
| Note | For Permanent License Reservation, status message displays the number of licenses that the administrator specified for this
                                                      system to operate within. License count does not affect compliance status and it is for administrator reference only. Admin can set the license count through Command Line Interface. |
| Smart Software Licensing
                                             						Status |
| Registration Status | Displays the current registration status of the product. The different statuses are: Registered—For the product which is registered. Unregistered or Unidentified—For the product which is unregistered. Unregistered-Registration Expired—For the product whose registration has expired. Registered-Specific License Reservation /Universal License Reservation —For product which is registered in SLR /PLR mode. Note Smart Agent may reflect status as Universal License Reservation but is for Permanent Licenses Reservation feature. Reservation In Progress—For product whose License Reservation is in progress. | Note | Smart Agent may reflect status as Universal License Reservation but is for Permanent Licenses Reservation feature. |
| Note | Smart Agent may reflect status as Universal License Reservation but is for Permanent Licenses Reservation feature. |
| License
                                          					 Authorization Status | Displays the overall authorization status of the product. The different statuses are: Authorized—Product in authorized or in compliance state. Authorization Expired—Authorization is expired for the product. This usually happens when the product has not communicated
                                                with Cisco for 90 continuous days. Out of Compliance—Product is in out of compliance state because of insufficient licenses. No Licenses in Use—Product does not consume any licenses. Evaluation Mode—Product is in evaluation mode and not yet registered with Cisco. Evaluation Period Expired—Evaluation period has expired. Not Applicable—Unable to determine current registration status. Authorized-Reserved—Product in authorized or in compliance status for the reserved licenses. Not Authorized-Reserved—Product is not in authorized state because of insufficient licenses reserved. Export Control Not Allowed—Product in eval mode. |
| Transport
                                          					 Settings Note This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. | Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. | Specifies the type of licensing transport mode used in Emergency Responder. Important From Release 15SU2 onwards, Call Home as a transport mode for smart licensing is deprecated. Smart Transport mode, the new
                                                      transport mode is introduced for smart licensing. Transport Settings for Emergency Responder displays one of the following modes: Call Home —Indicates that Emergency Responder is using call home for smart licensing communication to Cisco Smart Software Manager or
                                                Cisco Smart Software Manager satellite. Smart Transport (Applicable from Release 15SU2 onwards) —Indicates that Emergency Responder is using smart transport for smart licensing communication to Cisco Smart Software Manager
                                                or Cisco Smart Software Manager satellite. Note All freshly installed Emergency Responder supports only Smart Transport. When you log in to Emergency Responder, a warning message indicates that you are currently using the Call Home mode. In case
                                          you want to switch to the Smart Transport mode, click Test Connectivity and then click on Switch . The different settings through which Cisco Emergency Responder can connect to Cisco Smart Software Manager or Smart Software
                                          Manager satellite are: Direct—Emergency Responder sends usage information directly over the internet. No additional components are needed. HTTP/HTTPS Proxy— Emergency Responder sends usage information over the internet through a proxy server. Check the Authentication needed on HTTP or HTTPS proxy check box if want to register to Cisco Smart Software Manager using authentication based proxy server. If you enable this
                                                check box, only then the Proxy User and Proxy Password fields are enabled. Enter the details in the following fields: Host Name/IP Address Port Proxy User Note Administrators should ensure that they enter the configured user name for proxy in the Proxy User field. Proxy Password Smart Software Manager satellite— Emergency Responder sends usage information to an on-premise Smart Software Manager. Periodically, an exchange of information is performed to
                                                keep the databases in synchronization. For more information on installation or configuration of the Smart Software Manager
                                                satellite, go to this URL: https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager-satellite.html . Transport Gateway—Emergency Responder sends usage information to Cisco Smart Software Manager through a Cisco Transport Gateway. Check the Do not share my hostname or IP address with Cisco check box to allow the administrator to restrict the exchange of IP Address and hostname of the Emergency Responder during
                                                the registration and synchronization to Cisco Smart Software Manager or Cisco Smart Software Manager Satellite. Note When the check box is selected, Emergency Responder will not share the IP Address or hostname information from being sent
                                                         through registration and regular license compliance synchronization activities. A unique identifier is generated for the Cisco
                                                         Emergency Responder Product Instance and must be used for cross-referencing in Cisco Smart Software Manager. Test connectivity with Smart Transport—Allows the administrator to test the Emergency Responder connection to Smart Transport
                                                endpoint through transport setting configurations. Switch—Allows the administrator to change the transport mode from Call Home to Smart Transport. Cisco Smart License Manager
                                                service is restarted during switch process. This option is available only for Direct or HTTP/HTTPS Proxy server or Cisco Smart
                                                Software Manager satellite in Call Home Mode. Note Switch Button is enabled once Test connectivity with Smart Transport is successful with Smart Transport. Note Select the Do not share my hostname or IP address with Cisco check box for privacy. It does not share IP Address or Hostname information being sent through during registration and regular
                                                   license compliance sync. Note If you choose to use a direct connection, then you must configure Domain Name System (DNS) on Emergency Responder that can resolve https://tools.cisco.com/its/service/oddce/services/DDCEService for Call Home or https://smartreceiver.cisco.com for Smart Transport . Note If you choose not to configure the domain and Domain Name System (DNS) on Emergency Responder , then you can select the Cisco Smart Software Manager satellite or transport gateway or proxy server under Transport settings. In such cases, DNS that can resolve https://www.cisco.com has to be configured on the Cisco Smart Software Manager satellite , or Transport Gateway, or HTTP/HTTPS Proxy server. Note If you choose not to use the DNS server in your deployment and not connect to the internet, then you can select the Cisco
                                                   Smart Software Manager satellite with manual synchronization in disconnected mode. Note Transport Gateway as a transport mode is not supported in Smart Transport. Therefore, it continues to use call home post upgrade.
                                                      To switch to Smart Transport mode, deregister the product. Also, the system must connect to Smart Transport URL using Direct
                                                      or Cisco Smart Software Manager satellite or HTTP/HTTPS Proxy server. In case of any issues with Smart Transport mode, use
                                                      the license smart call-home destination address TransportGateway command to fall back to the Call Home mode. | Important | From Release 15SU2 onwards, Call Home as a transport mode for smart licensing is deprecated. Smart Transport mode, the new
                                                      transport mode is introduced for smart licensing. | Note | All freshly installed Emergency Responder supports only Smart Transport. | Note | Administrators should ensure that they enter the configured user name for proxy in the Proxy User field. | Note | When the check box is selected, Emergency Responder will not share the IP Address or hostname information from being sent
                                                         through registration and regular license compliance synchronization activities. A unique identifier is generated for the Cisco
                                                         Emergency Responder Product Instance and must be used for cross-referencing in Cisco Smart Software Manager. | Note | Switch Button is enabled once Test connectivity with Smart Transport is successful with Smart Transport. | Note | Select the Do not share my hostname or IP address with Cisco check box for privacy. It does not share IP Address or Hostname information being sent through during registration and regular
                                                   license compliance sync. | Note | If you choose to use a direct connection, then you must configure Domain Name System (DNS) on Emergency Responder that can resolve https://tools.cisco.com/its/service/oddce/services/DDCEService for Call Home or https://smartreceiver.cisco.com for Smart Transport . | Note | If you choose not to configure the domain and Domain Name System (DNS) on Emergency Responder , then you can select the Cisco Smart Software Manager satellite or transport gateway or proxy server under Transport settings. In such cases, DNS that can resolve https://www.cisco.com has to be configured on the Cisco Smart Software Manager satellite , or Transport Gateway, or HTTP/HTTPS Proxy server. | Note | If you choose not to use the DNS server in your deployment and not connect to the internet, then you can select the Cisco
                                                   Smart Software Manager satellite with manual synchronization in disconnected mode. | Note | Transport Gateway as a transport mode is not supported in Smart Transport. Therefore, it continues to use call home post upgrade.
                                                      To switch to Smart Transport mode, deregister the product. Also, the system must connect to Smart Transport URL using Direct
                                                      or Cisco Smart Software Manager satellite or HTTP/HTTPS Proxy server. In case of any issues with Smart Transport mode, use
                                                      the license smart call-home destination address TransportGateway command to fall back to the Call Home mode. |
| Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. |
| Important | From Release 15SU2 onwards, Call Home as a transport mode for smart licensing is deprecated. Smart Transport mode, the new
                                                      transport mode is introduced for smart licensing. |
| Note | All freshly installed Emergency Responder supports only Smart Transport. |
| Note | Administrators should ensure that they enter the configured user name for proxy in the Proxy User field. |
| Note | When the check box is selected, Emergency Responder will not share the IP Address or hostname information from being sent
                                                         through registration and regular license compliance synchronization activities. A unique identifier is generated for the Cisco
                                                         Emergency Responder Product Instance and must be used for cross-referencing in Cisco Smart Software Manager. |
| Note | Switch Button is enabled once Test connectivity with Smart Transport is successful with Smart Transport. |
| Note | Select the Do not share my hostname or IP address with Cisco check box for privacy. It does not share IP Address or Hostname information being sent through during registration and regular
                                                   license compliance sync. |
| Note | If you choose to use a direct connection, then you must configure Domain Name System (DNS) on Emergency Responder that can resolve https://tools.cisco.com/its/service/oddce/services/DDCEService for Call Home or https://smartreceiver.cisco.com for Smart Transport . |
| Note | If you choose not to configure the domain and Domain Name System (DNS) on Emergency Responder , then you can select the Cisco Smart Software Manager satellite or transport gateway or proxy server under Transport settings. In such cases, DNS that can resolve https://www.cisco.com has to be configured on the Cisco Smart Software Manager satellite , or Transport Gateway, or HTTP/HTTPS Proxy server. |
| Note | If you choose not to use the DNS server in your deployment and not connect to the internet, then you can select the Cisco
                                                   Smart Software Manager satellite with manual synchronization in disconnected mode. |
| Note | Transport Gateway as a transport mode is not supported in Smart Transport. Therefore, it continues to use call home post upgrade.
                                                      To switch to Smart Transport mode, deregister the product. Also, the system must connect to Smart Transport URL using Direct
                                                      or Cisco Smart Software Manager satellite or HTTP/HTTPS Proxy server. In case of any issues with Smart Transport mode, use
                                                      the license smart call-home destination address TransportGateway command to fall back to the Call Home mode. |
| Smart
                                          					 Account Name Note This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. | Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. | Displays information of the customer Smart Account. It is created from the Request a Smart Account option under Administration section of the https://software.cisco.com/ . It is the primary account created to represent the customer and all licenses for a company that are assigned to this Smart
                                          Account. It also manages licenses for all Cisco products. |
| Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. |
| Virtual
                                          					 Account Note This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. | Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. | A
                                          					 self-defined construct to reflect the company organization. Licenses and
                                          					 Product instances can be distributed across virtual accounts. Created and
                                          					 maintained by the administrator on the Cisco Smart Software Manager or Cisco
                                          					 Smart Software Manager satellite with full visibility to company assets. |
| Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. |
| Licensing
                                          					 Mode | Displays the licensing mode of the product. The default mode is Enterprise. |
| Export-Controlled Functionality | Specifies if the Export-Controlled functionality was enabled
                                          					 in the token with which the product was registered. Note The Allow export-controlled functionality on the products registered with this token check box is not displayed for the Smart Accounts that are not permitted to use the Export-Controlled functionality. Displays one of the following status information: Allowed—The token registered with has Allow export-controlled functionality selected. Not Allowed—The token registered with do not have Allow export-controlled functionality selected or Cisco Emergency Responder
                                                not registered. Note In Specific License Reservation or Permanent License Reservation , Export-Controlled functionality of product depends on the configuration of Smart Account to which it is registered. | Note | The Allow export-controlled functionality on the products registered with this token check box is not displayed for the Smart Accounts that are not permitted to use the Export-Controlled functionality. | Note | In Specific License Reservation or Permanent License Reservation , Export-Controlled functionality of product depends on the configuration of Smart Account to which it is registered. |
| Note | The Allow export-controlled functionality on the products registered with this token check box is not displayed for the Smart Accounts that are not permitted to use the Export-Controlled functionality. |
| Note | In Specific License Reservation or Permanent License Reservation , Export-Controlled functionality of product depends on the configuration of Smart Account to which it is registered. |
| Actions Note This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. | Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. | The Actions drop-down list box gets activated only after a successful registration. It lists the following type of actions which can
                                          be performed: Renew Authorization Now Renew Registration Now Reregister Deregister |
| Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. |
| Register Note This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. | Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. | Use the Register button to register Cisco Emergency Responder with Cisco Smart Software Manager or Cisco Smart Software Manager satellite. Note The Register button gets disabled after a successful registration with Cisco Smart Software Manager or Cisco Smart Software Manager satellite. | Note | The Register button gets disabled after a successful registration with Cisco Smart Software Manager or Cisco Smart Software Manager satellite. |
| Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. |
| Note | The Register button gets disabled after a successful registration with Cisco Smart Software Manager or Cisco Smart Software Manager satellite. |
| Request Entitlement Now |
| Synchronize Now Note This section will not be available when Specific License Reservation is enabled. | Note | This section will not be available when Specific License Reservation is enabled. | Click
                                          					 the Synchronize Now button to send a synchronization
                                          					 (entitlement) request to Cisco Smart License Manager. |
| Note | This section will not be available when Specific License Reservation is enabled. |
| Last
                                          					 Synchronization Note This section will not be available when Specific License Reservation is enabled. | Note | This section will not be available when Specific License Reservation is enabled. | This is
                                          					 a static field that displays the last authorization attempt time and its
                                          					 success or failure status. For example, Jan 19 23:31:00 2017 IST (Succeeded). Note This field gets displayed only after a successful registration with the Cisco Smart Software Manager or Cisco Smart Software
                                                   Manager satellite. | Note | This field gets displayed only after a successful registration with the Cisco Smart Software Manager or Cisco Smart Software
                                                   Manager satellite. |
| Note | This section will not be available when Specific License Reservation is enabled. |
| Note | This field gets displayed only after a successful registration with the Cisco Smart Software Manager or Cisco Smart Software
                                                   Manager satellite. |
| License Requirement by
                                             						Type |
| License
                                          					 Type | Displays
                                          					 the Cisco Emergency Responder (CER) license type. The only available license
                                          					 type is CER_USER. |
| Description | Displays the description for the license type which is, CER User License. |
| Status | Displays the current license status based on the license type (CER_USER).The different statuses are: Authorization Expired—The authorized period has expired. Evaluation—The agent is using the evaluation period for this entitlement. Evaluation Period Expired—Evaluation period has expired. Authorized—In compliance (authorized). No Licenses in Use—There are no licenses being consumed by the product instance. Out of Compliance—Out of compliance. Waiting—The initial state after an entitlement request while waiting for the authorization request response. |
| Count | Displays the total number of users currently tracked. |
| Details of Cisco ER Licenses |
| Number
                                          					 of phones discovered | Displays
                                          					 the number of discovered phones tracked in an IP Subnet and the Switch port. |
| Number
                                          					 of phones manually configured | Displays
                                          					 the number of manually configured phones. For example, analog phones. |
| Total
                                          					 number of users being tracked currently | Displays
                                          					 the number of phones tracked by Cisco Emergency Responder, which requires a
                                          					 User License. When you click the displayed hyperlinked number, the Tracked Phones List window is displayed, which lists
                                          					 the tracked phones. |
| Total
                                          					 number of users configured not to be tracked | Displays
                                          					 a list of phones configured with an IP Subnet and Cisco Emergency Responder does not track it. Note In a scenario where a Dual-stack phone has both the IPv4 and IPv6 addresses configured, and the phone falls under both the
                                                      IPv4 and IPv6 subnets having the same priority, and one of the subnet is trackable and the other one is non-trackable, the
                                                      phone is considered to be trackable. | Note | In a scenario where a Dual-stack phone has both the IPv4 and IPv6 addresses configured, and the phone falls under both the
                                                      IPv4 and IPv6 subnets having the same priority, and one of the subnet is trackable and the other one is non-trackable, the
                                                      phone is considered to be trackable. |
| Note | In a scenario where a Dual-stack phone has both the IPv4 and IPv6 addresses configured, and the phone falls under both the
                                                      IPv4 and IPv6 subnets having the same priority, and one of the subnet is trackable and the other one is non-trackable, the
                                                      phone is considered to be trackable. |
| Smart
                                             						Licensing Product Registration |
| The
                                          					 Smart Software Manager or Cisco Smart Software Manager satellite manages the
                                          					 product license. It also provides a link to the Smart Software Manager page. |

| Note | For Specific License Reservation status message displays current license status. |
|---|---|

| Note | For Permanent License Reservation, status message displays the number of licenses that the administrator specified for this
                                                      system to operate within. License count does not affect compliance status and it is for administrator reference only. Admin can set the license count through Command Line Interface. |
|---|---|

| Note | Smart Agent may reflect status as Universal License Reservation but is for Permanent Licenses Reservation feature. |
|---|---|

| Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. |
|---|---|

| Important | From Release 15SU2 onwards, Call Home as a transport mode for smart licensing is deprecated. Smart Transport mode, the new
                                                      transport mode is introduced for smart licensing. |
|---|---|

| Note | All freshly installed Emergency Responder supports only Smart Transport. |
|---|---|

| Note | Administrators should ensure that they enter the configured user name for proxy in the Proxy User field. |
|---|---|

| Note | When the check box is selected, Emergency Responder will not share the IP Address or hostname information from being sent
                                                         through registration and regular license compliance synchronization activities. A unique identifier is generated for the Cisco
                                                         Emergency Responder Product Instance and must be used for cross-referencing in Cisco Smart Software Manager. |
|---|---|

| Note | Switch Button is enabled once Test connectivity with Smart Transport is successful with Smart Transport. |
|---|---|

| Note | Select the Do not share my hostname or IP address with Cisco check box for privacy. It does not share IP Address or Hostname information being sent through during registration and regular
                                                   license compliance sync. |
|---|---|

| Note | If you choose to use a direct connection, then you must configure Domain Name System (DNS) on Emergency Responder that can resolve https://tools.cisco.com/its/service/oddce/services/DDCEService for Call Home or https://smartreceiver.cisco.com for Smart Transport . |
|---|---|

| Note | If you choose not to configure the domain and Domain Name System (DNS) on Emergency Responder , then you can select the Cisco Smart Software Manager satellite or transport gateway or proxy server under Transport settings. In such cases, DNS that can resolve https://www.cisco.com has to be configured on the Cisco Smart Software Manager satellite , or Transport Gateway, or HTTP/HTTPS Proxy server. |
|---|---|

| Note | If you choose not to use the DNS server in your deployment and not connect to the internet, then you can select the Cisco
                                                   Smart Software Manager satellite with manual synchronization in disconnected mode. |
|---|---|

| Note | Transport Gateway as a transport mode is not supported in Smart Transport. Therefore, it continues to use call home post upgrade.
                                                      To switch to Smart Transport mode, deregister the product. Also, the system must connect to Smart Transport URL using Direct
                                                      or Cisco Smart Software Manager satellite or HTTP/HTTPS Proxy server. In case of any issues with Smart Transport mode, use
                                                      the license smart call-home destination address TransportGateway command to fall back to the Call Home mode. |
|---|---|

| Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. |
|---|---|

| Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. |
|---|---|

| Note | The Allow export-controlled functionality on the products registered with this token check box is not displayed for the Smart Accounts that are not permitted to use the Export-Controlled functionality. |
|---|---|

| Note | In Specific License Reservation or Permanent License Reservation , Export-Controlled functionality of product depends on the configuration of Smart Account to which it is registered. |
|---|---|

| Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. |
|---|---|

| Note | This section will not be available when Specific License Reservation or Permanent License Reservation is enabled. |
|---|---|

| Note | The Register button gets disabled after a successful registration with Cisco Smart Software Manager or Cisco Smart Software Manager satellite. |
|---|---|

| Note | This section will not be available when Specific License Reservation is enabled. |
|---|---|

| Note | This section will not be available when Specific License Reservation is enabled. |
|---|---|

| Note | This field gets displayed only after a successful registration with the Cisco Smart Software Manager or Cisco Smart Software
                                                   Manager satellite. |
|---|---|

| Note | In a scenario where a Dual-stack phone has both the IPv4 and IPv6 addresses configured, and the phone falls under both the
                                                      IPv4 and IPv6 subnets having the same priority, and one of the subnet is trackable and the other one is non-trackable, the
                                                      phone is considered to be trackable. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays the
                                          				  product registration status. |
| Product
                                          				  Instance Registration Token | Displays a
                                          				  text area where you can enter the product registration token generated from the
                                          				  Cisco Smart Software Manager or Cisco Smart Software Manager satellite. |
| Reregister
                                          				  this product instance if it is already registered | Check the Reregister this product instance if it is already
                                             					 registered check box to enable a force registration of the product
                                          				  with Cisco Smart Software Manager or Cisco Smart Software Manager satellite. |
| Register | Click the Register button to register Cisco Emergency Responder with Cisco Smart
                                          				  Software Manager or Cisco Smart Software Manager satellite. |

| Note | The Register button gets disabled after a successful
                                          		  registration with Cisco Smart Software Manager or Cisco Smart Software Manager
                                          		  satellite. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays the current configuration status of the Smart Call Home or Smart Transport (Applicable from Release 15SU2 onwards) . When you log in to Emergency Responder, a warning message indicates that you are currently using the Call Home mode. In case
                                          you want to switch to the Smart Transport mode, click Test Connectivity and then click on Switch . Note Transport Gateway as a transport mode is not supported in Smart Transport. Therefore, it continues to use call home post upgrade.
                                                      To switch to Smart Transport mode, deregister the product. Also, the system must connect to Smart Transport URL using Direct
                                                      or Cisco Smart Software Manager satellite or HTTP/HTTPS Proxy server. In case of any issues with Smart Transport mode, use
                                                      the license smart call-home destination address TransportGateway command to fall back to the Call Home mode. | Note | Transport Gateway as a transport mode is not supported in Smart Transport. Therefore, it continues to use call home post upgrade.
                                                      To switch to Smart Transport mode, deregister the product. Also, the system must connect to Smart Transport URL using Direct
                                                      or Cisco Smart Software Manager satellite or HTTP/HTTPS Proxy server. In case of any issues with Smart Transport mode, use
                                                      the license smart call-home destination address TransportGateway command to fall back to the Call Home mode. |
| Note | Transport Gateway as a transport mode is not supported in Smart Transport. Therefore, it continues to use call home post upgrade.
                                                      To switch to Smart Transport mode, deregister the product. Also, the system must connect to Smart Transport URL using Direct
                                                      or Cisco Smart Software Manager satellite or HTTP/HTTPS Proxy server. In case of any issues with Smart Transport mode, use
                                                      the license smart call-home destination address TransportGateway command to fall back to the Call Home mode. |
| Transport Settings |
| Direct | Product
                                          				  sends usage information directly over the internet. No additional components
                                          				  are needed. This is the default communication mode. |
| HTTP or
                                          				  HTTPS Proxy Server | Product
                                          				  sends usage information over the internet through a proxy server (such as Cisco
                                          				  Transport Gateway or Apache). Check the Authentication needed on HTTP or HTTPS proxy check box if want to register to Cisco Smart Software Manager using authentication based proxy server. If you enable this
                                          check box, only then the Proxy User and Proxy Password fields are enabled. Enter the details in the following fields: Host Name/IP Address Port Proxy User Note Administrators should ensure that they enter the configured user name for proxy in the Proxy User field. Proxy Password | Note | Administrators should ensure that they enter the configured user name for proxy in the Proxy User field. |
| Note | Administrators should ensure that they enter the configured user name for proxy in the Proxy User field. |
| Smart Software Manager satellite | Emergency Responder sends usage information to an on-premise Smart Software Manager. Periodically, an exchange of information is performed to
                                          keep the databases in synchronization. For more information on installation or configuration of the Smart Software Manager
                                          satellite, go to this URL: https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager-satellite.html . If you are using HTTP for Call Home, go to the URL: http://Satellite-ip/Transportgateway . If you are using HTTPS for Call Home, go to the URL: https://SatelliteFQDN-OR-IP-address/TransportGateway . If you are using HTTP for Smart Transport, go to the URL: http://Satellite-ip/SmartTransport . If you are using HTTPS for Smart Transport, go to the URL: https://SatelliteFQDN-OR-IP-address/SmartTransport . |
| Transport Gateway | Emergency Responder sends usage information to Cisco Smart Software Manager through a Cisco Transport Gateway. |
| Test connectivity with Smart Transport | Allows the administrator to test the Emergency Responder connection to Smart Transport endpoint through transport setting
                                          configurations. |
| Switch | Allows the administrator to change the transport mode from Call Home to Smart Transport. Cisco Smart License Manager service
                                          is restarted during switch process. This option is available only for Direct or HTTP/HTTPS Proxy server or Cisco Smart Software
                                          Manager satellite in Call Home Mode. Note Switch Button is enabled once Test connectivity with Smart Transport is successful with Smart Transport. | Note | Switch Button is enabled once Test connectivity with Smart Transport is successful with Smart Transport. |
| Note | Switch Button is enabled once Test connectivity with Smart Transport is successful with Smart Transport. |
| Do not share my hostname or IP address with Cisco | Check the check box to allow the administrator to restrict the exchange of IP Address and hostname of the Cisco Emergency
                                          Responder during the registration and synchronization to Cisco Smart Software Manager or Cisco Smart Software Manager Satellite. Note When the check box is selected, Cisco Emergency Responder will not share the IP Address or hostname information from being
                                                      sent through registration and regular license compliance synchronization activities. A unique identifier is generated for
                                                      the Cisco Emergency Responder Product Instance and will need to be used for cross-referencing in Cisco Smart Software Manager. | Note | When the check box is selected, Cisco Emergency Responder will not share the IP Address or hostname information from being
                                                      sent through registration and regular license compliance synchronization activities. A unique identifier is generated for
                                                      the Cisco Emergency Responder Product Instance and will need to be used for cross-referencing in Cisco Smart Software Manager. |
| Note | When the check box is selected, Cisco Emergency Responder will not share the IP Address or hostname information from being
                                                      sent through registration and regular license compliance synchronization activities. A unique identifier is generated for
                                                      the Cisco Emergency Responder Product Instance and will need to be used for cross-referencing in Cisco Smart Software Manager. |

| Note | Transport Gateway as a transport mode is not supported in Smart Transport. Therefore, it continues to use call home post upgrade.
                                                      To switch to Smart Transport mode, deregister the product. Also, the system must connect to Smart Transport URL using Direct
                                                      or Cisco Smart Software Manager satellite or HTTP/HTTPS Proxy server. In case of any issues with Smart Transport mode, use
                                                      the license smart call-home destination address TransportGateway command to fall back to the Call Home mode. |
|---|---|

| Note | Administrators should ensure that they enter the configured user name for proxy in the Proxy User field. |
|---|---|

| Note | Switch Button is enabled once Test connectivity with Smart Transport is successful with Smart Transport. |
|---|---|

| Note | When the check box is selected, Cisco Emergency Responder will not share the IP Address or hostname information from being
                                                      sent through registration and regular license compliance synchronization activities. A unique identifier is generated for
                                                      the Cisco Emergency Responder Product Instance and will need to be used for cross-referencing in Cisco Smart Software Manager. |
|---|---|

| Note | Transport settings
                                          		  are shared with Smart
                                             			 Call Home , so any changes made in the Transport
                                             			 Setting window applies to other features using this service. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays the
                                          				  product re-registration status. |
| Product
                                          				  Instance Registration Token | Displays a
                                          				  text area where you can enter the product registration token generated from the
                                          				  Cisco Smart Software Manager or Cisco Smart Software Manager satellite. |
| Re-register | Click the Re-register button to re-register the product with
                                          				  Cisco Smart Software Manager or Cisco Smart Software Manager satellite. |

| Field | An email alert is sent
                                          					 when: |
|---|---|
| Discovery Parameters |
| Discovery Engine Registration Failed | The Discovery Engine fails to register |
| Discovery Engine goes out of connection | The Discovery Engine loses connection |
| For unreachable devices during recovery | Devices such as switches and CiscoUnified
                                          					 CommunicationsManagers become unreachable |
| Emergency Call Routing Parameters |
| Call information | A
                                          					 911 call is placed |
| Call routing session ended due to problems | Call routing is stopped due to any of these reasons: Invalid CMC Invalid FAC FAC and CMC needed CMC needed FAC needed RESOURCE_BUSY |
| Rerouting of call | An
                                          					 emergency call is rerouted |
| Routing failure | Call routing fails |
| Route Point out of Service | The route point goes out of service |
| Cluster Parameters |
| Cluster DB Failure | The server cannot communicate with the cluster database host |
| Intra Cluster Failure | The intra-cluster communication to a server group in the cluster
                                          					 fails |
| Misc Parameters |
| Subscriber becomes active | The Subscriber becomes active |
| Publisher comes back online | The Publisher comes back online |
| Not able to get the JTAPI Provider | When Emergency Responder cannot get the JTAPI provider |
| Available user licenses get exhausted during phone tracking | When the number of user licenses are exhausted during phone
                                          					 tracking |
| Switch Port location change reporting | When you enable switch port change reporting for phones |
| Suppress IP Communicator location change reporting | When you filter CiscoUnifiedIP Communicator from the location
                                          					 change reporting email alerts |
| DRF Alert | Enable or Disable DRF backup or restore mail alerts |
| Update Settings button | Updates the email alert settings |
| Cancel Changes button | Cancels changes made to the email alert settings |

| Field | Description |
|---|---|
| Add Subscriber |
| HostName | Host name of the subscriber server. |
| Insert button | Click Insert to add the new subscriber server. |
| Cancel Changes button | Removes input from the Add Subscriber page. |
| Configured Servers | A
                                          					 list of all currently configured servers, showing the host name and IP address
                                          					 of each server. |

| Field | Description |
|---|---|
| Status | Displays status messages. |
| National E911 Service Provider VUI Settings |
| Upload Certificate | Uploads the certificate from your local drive to the Emergency
                                          					 Responder server. To
                                          					 upload a certificate, follow these steps: Click Upload Certificate An
                                                						  Upload Certificate window appears. Click
                                                						  the Browse button to locate the certificate file on your local
                                                						  machine. Click
                                                						  the Upload button to upload the certificate file. |
| Validate Certificate |
| National E911 Service Provider Certificate Password | The password that was generated with this certificate. |
| VUI URL | VUI URL is provided by National E911 Service Provider . |
| Enable HTTP Proxy | Check this check box if you want to use a proxy server for requests between Emergency Responder and National E911 Service
                                          Provider. |
| Proxy Host Name/IP Address | Enter the IP address or hostname of the proxy server, along with the port. For example, http://<ip_address_or_hostname>:port. |
| Authentication needed on HTTP Proxy | Check this check box if you want to communicate with the National E911 Service Provider using authentication based proxy server.
                                          If you enable this check box, only then the Proxy User Name and Proxy Password fields are enabled. |
| Proxy User Name | Enter the configured user name for proxy server in the Proxy User Name field. |
| Proxy Password | Enter the password that is associated to the username. |
| Test and Validate Certificate | Use this button to test the validity of your certificate. |
| Configure Account Details |
| VUI Schema URL | The VUI Schema URL provided by National E911 Service Provider . |
| National E911 Service Provider Account ID | Your National E911 Service Provider Account ID provided by National E911 Service Provider . |
| Max VUI Connections | The maximum number of simultaneous VUI connections that
                                          					 Emergency Responder allows across the Server group. |
| MyE911 for Location Updates | Set this drop-down to True if Cisco Jabber and Webex App are using MyE911 or Remote Location Manager to set the users location when Off-premises. Setting
                                          this drop-down to False requires users to update their location through Cisco’s Off-Premise User Page. By default, this option is set to True . |
| Test Connectivity | Use this link to verify whether Emergency Responder can successfully connect to National E911 Service Provider VUI. |
| Delete Account | Deletes an existing National E911 Service Provider account from the Emergency Responder database. |
| Update | Click Update to save the changes you made on this page. |
| Cancel | Click Cancel to change the fields on this page back to the last saved
                                          					 settings. |

| Note | Sometimes the prompts do not get played at the onsite alert phone when the call is initiated from the CTI ports. To avoid
                                       this problem, configure only one line per CTI port in the Unified CM that is configured for Emergency Responder. |
|---|---|

| Note | In case a user configures an onsite alert for a call (not for email), the calling party displays as the Emergency Responder
                                       CTI port. |
|---|---|

| Field | Description | Notes |
|---|---|---|
| Add New Onsite Alert Contact |
| Onsite Alert ID | The identifier for the onsite alert contact. The identifiers you
                                          					 use should be based on your site identification strategy (for example, security
                                          					 ID or badge number). This field is used throughout Emergency Responder to
                                          					 identify the contact; for example, you select from Onsite Alert IDs when
                                          					 assigning contacts to zones. The Onsite Alert ID cannot be modified after you
                                          					 have saved it. | Use a naming strategy meaningful to your organization, but which
                                          					 is also useful when configuring zones in Emergency Responder. |
| Onsite Alert Name | The name of the onsite alert contact. |  |
| Onsite Alert Number | The telephone number for the onsite alert contact. This number
                                          					 must be a voice telephone number; do not enter the number of a voice-mail
                                          					 system or an automated attendant. | When Emergency Responder gets an emergency call from an ERL, it
                                          					 calls the onsite alert number of the contact for the ERL and plays a
                                          					 prerecorded message that includes the phone number from which the emergency
                                          					 call was placed. |
| Onsite Alert Email Address | The email address for the onsite alert contact, for example,
                                          					 email@domain.com. | When Emergency Responder gets an emergency call from an ERL, it
                                          					 emails the onsite alert contact associated with the ERL. If the email ID is for
                                          					 an email paging system, the contact receives a page instead of an email. The
                                          					 email or page includes the phone number from which the emergency call was
                                          					 placed. Note You can add multiple email addresses by separating each
                                                      						address with a comma (,). Avoid extra spaces between the email addresses. | Note | You can add multiple email addresses by separating each
                                                      						address with a comma (,). Avoid extra spaces between the email addresses. |
| Note | You can add multiple email addresses by separating each
                                                      						address with a comma (,). Avoid extra spaces between the email addresses. |
| Onsite Alert Pager Address | The pager email address for the onsite alert contact, for
                                          					 example, <pager_number>@domain.com. | You can limit the size of the message that is sent to the pager
                                          					 by configuring the fields on the Pager Alert Setting Page. See Pager Alert Settings . |
| Available
                                          					 User Group | The User
                                          					 Group which will receive the specific web alert from the associated ERL. By
                                          					 default Emergency Responder User Group is selected, which has all users. | The users
                                          					 can view all alerts in the system by selecting ALL on the Web Alert page. |
| Insert | Click the Insert button to add the contact to the list of
                                          					 contacts. The contact is then listed in the Available Onsite Alerts section of the page. |  |
| Cancel Changes | Click the Cancel Changes button to cancel any changes made to
                                          					 this page. |  |
| Available Onsite Alerts | Section of the page that displays onsite alert contacts that
                                          					 have already been configured. For configured onsite alert contacts, the
                                          					 following information is displayed: Onsite Alert ID Onsite Alert Name Onsite Alert Number Onsite Alert Email Address Onsite User Group To change an entry, click the entry or click the Edit icon; the person's contact information is loaded in the
                                          					 edit boxes. Make your changes and click Update . To delete an entry, click the Delete icon on the same line as the entry. | If no contacts have previously been configured, this section is
                                          					 blank. You cannot modify a contact's Onsite Alert ID. Before you can delete the entry, you must update the ERLs to
                                          					 which the person is assigned to remove the person from the ERL. |
| Add New | Click the Add New button to add another contact. |  |
| Update | Click the Update button when viewing an existing contact's
                                          					 information to save changes you make to the information. | Only available when viewing the information for an existing
                                          					 contact. |
| Export | Click
                                          					 the Export button to export the onsite alert settings to
                                          					 another file. For more information, see Export OnsiteAlert Data . |  |
| Import | Click
                                          					 the Import button to import the onsite alert settings to
                                          					 your Cisco Emergency Responder configuration. For more
                                          					 information, see Import OnsiteAlert Data . |  |

| Note | You can add multiple email addresses by separating each
                                                      						address with a comma (,). Avoid extra spaces between the email addresses. |
|---|---|

| Field | Description |
|---|---|
| Export
                                             					 OnsiteAlert Data |  |
| Select
                                             					 Export Format | Select
                                             					 the file format from the drop-down list that matches the file being imported. |
| Enter
                                             					 Export File Name | Enter the
                                             					 name of the file that you want to create. Do not include the file extension. |
| Export | Click the Export button to add data from the import file to
                                             					 your Cisco Emergency Responder configuration. |
| Close | Click the Close button to close the window. |
| Export
                                             					 Status | This text
                                             					 box displays status information. |
| Download |  |
| Select a
                                             					 File to Download | Select a
                                             					 file from the drop-down list and click the Download button to download the file to your
                                             					 machine. |

| Note | Ensure that you restart the Cisco Emergency Responder service after using the Import feature to update the Emergency Responder
                                          onsite alerts in bulk, for the changes to take effect. |
|---|---|

| Field | Description |
|---|---|
| Import
                                             					 OnsiteAlert Data |  |
| Select
                                             					 Import Format | Select
                                             					 the file format from the drop-down list that matches the file being imported. Click View sample file link to view an example of the
                                             					 expected format and sequence of values. Use this sample information to create
                                             					 your import file in a spreadsheet. |
| Select
                                             					 File to Import | Select
                                             					 the file from the drop-down list from which you want to import data. |
| Import | Click the Import button to add data from the import file to
                                             					 your Cisco Emergency Responder configuration. |
| Upload | Click the Upload button to upload the file from your machine.
                                             					 For more information, see Upload File . |
| Close | Click the Close button to close the window. |
| Import
                                             					 Status | This text box displays status information. |

| Note | If you are upgrading Emergency Responder from any source version prior to Release 12.5.1, ensure that you check the Local
                                       Call Time check box to receive the local call time via emails and pager alerts in the upgraded version. |
|---|---|

| Field | Descriptions |
|---|---|
| Pager Alert Settings |
|  | You can limit the size of the pager message that is sent by selecting the following fields and editing the labels are associated
                                          with those fields: Extension ERL Location System Time Server Local Time Check the check box to select the fields that you want to display on the pager. Click the text box to edit the label that you want to send to the pager. |
| Update Pager Settings | Click Update Settings to save changes that you made. |
| Restore Pager Defaults | Click Restore Defaults to restore the default pager and label settings. |
| Send Sample Message to a pager | Enter a pager address in the text box and click Send Test Message to send a test message to your pager. |
| Email Alert Settings |
|  | You can customize email messages sent to the configured onsite security person by choosing the required fields. You can also
                                          add additional notes or mask digits on Caller DN to reflect the local dialing pattern. Caller Extension Display Name Zone Location System Call Time Local Call Time Server Details—Enter the URL details for the Emergency Responder User page in which you can check the 911 call details. In
                                                case you are updating the hostname, ensure that you enter the new hostname in the server details. Additional Notes—Enables you to provide any additional information as Admin Notes and the information is available in the
                                                email alerts. Discard DN digits—You can enter the count of digits to be masked from the beginning on Caller DN to reflect the local dialing
                                                pattern. Check the check box to select the fields that you want to display on the email message. Click the editable label text boxes to modify the label that you want to send to the email message. |
| Update Email Settings | Click Update Email Settings to save the changes made. |
| Restore Email Defaults | Click Restore Email Defaults to restore the default email message and label settings. |
| Sample Email Message Preview | Select the required email alert field settings and click Update Email Settings to preview the sample email message. |

| Field | Description | Notes |
|---|---|---|
| ERL Search Parameters |
| Find Conventional ERL where... | Select search criteria and click Find to list existing ERLs. To
                                          					 list all ERLs, click Find without entering any criteria. From the drop-down menu, you can select the
                                          					 number of records that display per page for each search. From the search results list, you can: Click an entry to view and
                                             						update its characteristics. Click the Copy icon to create a new ERL with the same ALI data. Click the Delete icon to remove the ERL. Click view... in the Audit Trail column to view a history of
                                             						changes made to that ERL. See ERL Audit Trail for more information. | When copying an ERL, information that must be unique in an ERL
                                          					 is not copied. See Add New ERL for more information. |
| Configure Default ERL | You must configure the Default ERL before configuring any other
                                          					 ERLs. The default ERL is the system-defined ERL that is used to route
                                          					 calls if no other ERL configuration is found. Note During the
                                                      						migration of data in an upgrade scenario, if any manually configured phone is
                                                      						assigned to the Default ERL, it remains there until it is modified. | Note | During the
                                                      						migration of data in an upgrade scenario, if any manually configured phone is
                                                      						assigned to the Default ERL, it remains there until it is modified. | See Add New ERL for more information. |
| Note | During the
                                                      						migration of data in an upgrade scenario, if any manually configured phone is
                                                      						assigned to the Default ERL, it remains there until it is modified. |
| Add New ERL | Click Add New
                                             						ERL to create a new ERL. | See Add New ERL for more information. |
| Configure Default ERL | Click Configure
                                             						Default ERL to configure a default ERL |  |
| Export | Click the Export link to create a file containing your ERL configuration. | See Export ERL Data for information about exporting ERL data. |
| Import | Click the Import link to create or update ERLs using information stored in a
                                          					 separate file. By importing ERL data, you can create or update many ERLs at one
                                          					 time. | See Import ERL Data for information about importing ERL data. |

| Note | During the
                                                      						migration of data in an upgrade scenario, if any manually configured phone is
                                                      						assigned to the Default ERL, it remains there until it is modified. |
|---|---|

| Note | On the ERL Information
                                                				for ERL Name page, the ERL Name variable is replaced with the name of
                                             			 the ERL associated with the page. For example, if you click the Default ERL,
                                             			 the page that appears is titled ERL Information
                                                				for Default . If the ERL name is First Floor, the page that appears is
                                             			 titled ERL Information
                                                				for First Floor . |
|---|---|

| Note | You cannot use
                                                   				  default ERLs as a Test ERL. The Test ERL check box is not available on the ERL
                                                   				  Information for Default page. |
|---|---|

| Note | If you are upgrading Emergency Responder from any source version prior to Release 12.5.1, ensure that you check the Local
                                          Call Time check box to receive the local call time via emails and pager alerts in the upgraded version. |
|---|---|

| Field | Description | Notes |
|---|---|---|
| ERL Settings |
| ERL Name | The name of the ERL. The naming strategy you use is critical.
                                             					 The ERL name is one of the primary pieces of information your security team
                                             					 sees when alerted to an emergency call. If the name is easy to understand and
                                             					 descriptive, it can help your team respond quickly to a call. For example, if you are creating an ERL for each floor in a
                                             					 three story building called Building J, your ERL names might be BldgJ-Floor1,
                                             					 BldgJ-Floor2, BldgJ-Floor3. Work with your security team to develop an ERL naming strategy. | You cannot change the name of an existing ERL. To change an ERL
                                             					 name, create a new ERL, then delete the old ERL. Any leading and trailing spaces are trimmed. |
| Description | Enter a description of the new ERL (optional). |  |
| Test ERL (Used for Synthetic Testing) | Check this check box if this ERL is used for testing. See Set Up Test ERLs . | This setting is not available on the ERL Information for
                                             					 Default; default ERLs may not be used as test ERLs. |
| ELIN Settings | The combination of a route pattern and a phone number that
                                             					 jointly route the emergency call to the PSAP and provide the PSAP with a
                                             					 callback number if the PSAP needs to call the emergency caller after
                                             					 disconnecting the call. | Each ERL must have unique ELINs. The number of ELINs that you
                                             					 define determines how many callbacks you can support. ELINs are used in order
                                             					 as emergency calls are made, and recycled as needed. For example, if you define
                                             					 two ELINs for an ERL, and three emergency calls are made, the PSAP cannot
                                             					 recontact the first emergency caller. However, concurrent emergency calls are not limited by the
                                             					 number of ELINs: you could have ten active emergency calls even if you only
                                             					 have two ELINs. The number of ELINs only controls PSAP callback capability. Note Emergency
                                                         						Responder restricts the association of an ELIN with an ERL if the ELIN has been
                                                         						configured as a DID Number for an Off-Premises Emergency Responder user.
                                                         						Emergency Responder does not impose this restriction if the DID Number belongs
                                                         						to a user who has never associated an off-premises location in Emergency
                                                         						Responder. | Note | Emergency
                                                         						Responder restricts the association of an ELIN with an ERL if the ELIN has been
                                                         						configured as a DID Number for an Off-Premises Emergency Responder user.
                                                         						Emergency Responder does not impose this restriction if the DID Number belongs
                                                         						to a user who has never associated an off-premises location in Emergency
                                                         						Responder. |
| Note | Emergency
                                                         						Responder restricts the association of an ELIN with an ERL if the ELIN has been
                                                         						configured as a DID Number for an Off-Premises Emergency Responder user.
                                                         						Emergency Responder does not impose this restriction if the DID Number belongs
                                                         						to a user who has never associated an off-premises location in Emergency
                                                         						Responder. |
| Route/Translation Pattern | The phone number, defined as a route pattern in Cisco Unified Communications Manager, that is configured to use the gateway
                                             that the call should be routed through to get to the correct PSAP. This number must include the external emergency number,
                                             such as 911 in the USA. For example, 10.911 or 10911. The pattern can only contain numbers and dots. |  |
| ELIN Number | The unique phone number which the PSAP can use to locate a
                                             					 caller an emergency caller if the call is hung up. This number must be a DID
                                             					 (direct inward dial) number provided by your service provider; that is, it must
                                             					 be routeable on the PSTN. Enter the entire number, including area code, for the
                                             					 North American Numbering Plan, such as 4085551212, or an E.164 Number including
                                             					 country code such as +14085551212. The number can only contain numbers, a plus
                                             					 sign (+), single hyphens, dots, or parentheses. The National E911 Service Provider ERL allows maximum of 10 characters and the data type should only be numbers. | An ELIN when being sent as ANI to PSAP through outgoing
                                             					 Gateway must be a DID (direct inward dial) number provided by your service
                                             					 provider. If an ELIN number has a numerical sign "+" , then add a "." between the "+" sign and the number in Cisco Unified Communications Manager ,PSAP Call Back translation pattern. The '+' can be
                                             					 removed using discard digit "Predot" . For example, if E.164 number includes a country code such as
                                             					 +14085551212, then in the Cisco Unified Communications Manager ,PSAP Call Back translation pattern you should enter
                                             					 '\+.XXXXXXXXXX X ' , not '\+1.XXXXXXXXXX'. The 913 pattern should be 913
                                             					 followed by 11X instead of 10X. |
| Add button | To add a route point and ELIN combination, enter the information
                                             					 and click Add . |  |
| Update button | To change an existing combination, select it in the list, change
                                             					 the information in the edit boxes, and click Update . |  |
| Remove button | To remove a combination, select it in the list and click Remove . |  |
| Onsite Alert Settings |
| Available
                                             					 Onsite Alert IDs | Text box that displays the IDs of all available onsite alert personnel. Note The onsite alert IDs list displays in a numerical order. | Note | The onsite alert IDs list displays in a numerical order. | You must
                                             					 first add the contact to the list of onsite alert personnel. |
| Note | The onsite alert IDs list displays in a numerical order. |
| Add button | Select the onsite alert (security) contacts to be assigned to
                                             					 the ERL. These contacts are notified when an emergency call is made from the
                                             					 ERL. To add a contact, select an Onsite Alert ID from the Available Onsite
                                             					 Alert IDs list and click Add .
                                             					 The contact's ID then appears in the Onsite Alert IDs for the ERL text box. |  |
| Remove button | To remove a contact for the ERL, select the appropriate ID in
                                             					 the Onsite Alert IDs for the ERL text box and click Remove . |  |
| ERL Address |
| ALI Details button | Click ALI
                                                						Details to view or change the automatic location information (ALI) of an
                                             					 ERL. The ALI provides detailed information about the location of the ERL, such
                                             					 as street address and phone number. |  |
| Time Zone | Select a time zone for the ERL. The time zone provides the list of all available time zones. | When you dial 911, the selected time zone is set as the local call time in Pager and Emergency alert. If a time zone is not
                                             selected, then the local call time is same as the system call time. |
| Insert button | Click Insert to save your changes to the new ERL. | The Insert button is only available when creating a new ERL. |
| Cancel Changes button | Click Cancel
                                                						Changes to change the fields on this page back to the last saved
                                             					 settings. |  |
| Update button | Click Update to save your changes to the ERL. | The Update button is only available when changing an existing
                                             					 ERL. |
| Close button | Click Close to close the window. You must click Update or Insert to save your changes before you click Close . |  |

| Note | Emergency
                                                         						Responder restricts the association of an ELIN with an ERL if the ELIN has been
                                                         						configured as a DID Number for an Off-Premises Emergency Responder user.
                                                         						Emergency Responder does not impose this restriction if the DID Number belongs
                                                         						to a user who has never associated an off-premises location in Emergency
                                                         						Responder. |
|---|---|

| Note | The onsite alert IDs list displays in a numerical order. |
|---|---|

| Note | On the ALI
                                                				Information ( for ERL Name) page, the ERL Name variable is replaced with the
                                             			 appropriate ERL name. For example, if you click on ALI Details on the ERL
                                             			 Information for Default page, the page that appears is titled ALI
                                                				Information for Default . If the ERL name is First Floor, the page that
                                             			 appears is titled ALI
                                                				Information for First Floor . |
|---|---|

| Note | The Add New
                                                   				  ERL page appears when you choose Add New
                                                      					 ERL on the Find ERL Data page (opened when you choose ERL >
                                                      					 Conventional ERL ). |
|---|---|

| Caution | The quality of
                                             			 the information you enter here is critical. This information is displayed to
                                             			 emergency call operators and to your local response team. They use this
                                             			 information to locate emergency callers. If the data is incorrect or difficult
                                             			 to understand, emergency response can be delayed, which might result in
                                             			 casualties that could have been prevented. |
|---|---|

| Field | Description | Notes |
|---|---|---|
| Find all prevalidated fields from validation file by selecting a
                                             					 tag |
| Select a Tag | Select the tag whose associated ALI data you want to load into
                                             					 the window. You can then edit the information for this specific ALI. | You can simplify the entry of ALI data by setting up tags in a
                                             					 file called validate.txt. This page explains where to place the file, and where
                                             					 to find the samplevalidate.txt file, which explains the format of the file. When you create a tag, you enter information that is common
                                             					 between several ALIs, such as company name, city, state, and so forth. For
                                             					 example, if you have a 25-story building, and you are creating an ERL for each
                                             					 floor, you could create a tag called "25story." Then, instead of retyping the information for the
                                             					 building 25 times, you select a tag and the ALI data is loaded with the data
                                             					 you defined for the tag. |
| Field | Description | Value Type (A =
                                             					 Alphabets, N = Numeric, S = Special Characters [# @ & * ( ) - _ + , . : ; "
                                             					 ' /] ) |
| ALI Data |
| House
                                             					 Number | The
                                             					 number from the postal street address for the building. Example: 170 in 170
                                             					 West Tasman Dr. | AN, dash
                                             					 "-", and @ sign "@" The
                                             					 number can be up to 10 characters, but your service provider might only support
                                             					 8 character numbers. |
| House
                                             					 Number Suffix | The number extension (such as /2) for the house number, if any. | ANS |
| Street Name | The street name from the postal address for the building. | ANS You are
                                             					 limited to 60 characters. |
| Prefix
                                             					 Directional | The
                                             					 type of street. Select the type from the drop-down list, and the field is
                                             					 filled with one of the abbreviations accepted by the U.S. Postal Service
                                             					 Publication 28, for example, AVE for Avenue. | Can be
                                             					 one of these directions: N S E W NE NW SE SW |
| Street
                                             					 Suffix | The
                                             					 type of street. Select the type from the drop-down list, and the field is
                                             					 filled with one of the abbreviations accepted by the U.S. Postal Service
                                             					 Publication 28, for example, AVE for Avenue. | A You can
                                             					 also type in the suffix. You are limited to 4 characters. |
| Post
                                             					 Directional | A
                                             					 trailing directional indicator if the street name contains one, for example, N
                                             					 for North. | Can be
                                             					 one of these directions: N S E W NE NW SE SW |
| Community Name | The
                                             					 community name for the address, for example, a city, town, or district name. | ANS You are
                                             					 limited to 32 characters. |
| State | The
                                             					 2-digit state abbreviation. | A You are
                                             					 limited to 2 characters. |
| Main
                                             					 NPA | The
                                             					 3-digit area code of the main number associated with the ERL. | N |
| Main
                                             					 Telephone No. | The
                                             					 main phone number associated with the ERL. This might be the number of the
                                             					 security office for the ERL. | N |
| Class
                                             					 of Service | Select
                                             					 the class of service for the ERL. | If you
                                             					 do not know your class of service, ask your service provider. |
| Type of
                                             					 Service | Select
                                             					 the type of service for the ERL. | If you
                                             					 do not know your class of service, ask your service provider. |
| Exchange | The
                                             					 Local Exchange Carrier (LEC) exchange identifier for the serving telephone
                                             					 office for the phone. | ANS You are
                                             					 limited to 4 characters. Ask your service provider for this identifier |
| Customer Name | The
                                             					 subscriber name associated with the ERL, and typically your company name. | ANS You are
                                             					 limited to 32 characters. |
| Order
                                             					 Number | The
                                             					 service order number of the activity of establishing or updating this record. | ANS You are
                                             					 limited to 10 characters. Work with your service provider to determine a valid
                                             					 order number, if one is needed. |
| Extract
                                             					 Date | The
                                             					 date on which the record was created. | Date
                                             					 [mmddyy] |
| County
                                             					 ID | The
                                             					 county identification code for the zone. In the USA, use the FIPS code assigned
                                             					 to the county by the U.S. Census Bureau. | AN You are
                                             					 limited to 4 characters. |
| Zip
                                             					 Code | The
                                             					 postal zip code for the address. | AN,
                                             					 hyphen "-" Indicates a U.S. zip code on a U.S. service order record or a Canadian postal
                                             					 code on a Canadian service order record. U.S. Format: NNNNN or NNNNN-NNNN;
                                             					 Canadian Format: ANANAN or ANA[space] NAN |
| Zip
                                             					 Code Extension | The
                                             					 postal zip code "plus four" number. | AN,
                                             					 hyphen "-" You are
                                             					 limited to 4 digits. |
| Customer Code | Your
                                             					 customer code. Ask your service provider if you do not know your code. | ANS You are
                                             					 limited to 3 characters. If you
                                             					 change this field, Emergency Responder generates two records: a Delete record
                                             					 to remove the ALI with the old code, and an Insert record to add the ALI with
                                             					 the new code. This Delete and Insert sequence is only generated the next time
                                             					 you export ALI: you must ensure that you submit this export file to the service
                                             					 provider. |
| Comments | Optional comments. These commentsmight be displayed at the PSAP if an emergency
                                             					 call is made from this ERL. | You are
                                             					 limited to 30 characters. |
| Longitude | The
                                             					 longitude of the ERL. | N, dot
                                             					 ".", plus "+", minus "-" You are
                                             					 limited to 9 digits. |
| Latitude | The
                                             					 latitude of the ERL. | N, dot
                                             					 ".", plus "+", minus "-" You are
                                             					 limited to 9 digits. |
| Elevation | The
                                             					 elevation of the ERL. | AN dot
                                             					 ".", plus "+",minus "-" You are
                                             					 limited to 5 digits. |
| TAR
                                             					 Code | The
                                             					 taxing area rate code. | ANS You are
                                             					 limited to 6 characters. |
| Location | Additional location information, in free form, to help identify the exact
                                             					 location of the phone. This
                                             					 information is displayed to your security personnel along with the ERL name
                                             					 when an emergency call is made, so use this field to help locate the caller.
                                             					 For example, you might repeat the street address that is defined in several
                                             					 separate fields elsewhere on this page. | ANS You are
                                             					 limited to 60 characters. |
| Reserved | Information your service provider might require to create a valid ALI file. | AN Ask
                                             					 your service provider if you must enter
                                             					 anything in the reserved area. Be
                                             					 aware that NENA and CSV requirements may be different. For example, ERL Import
                                             					 does not require that you enter anything in the Reserved field. You can give an
                                             					 empty string in each of the ERL records and Emergency Responder accepts this
                                             					 file for importing. However, you must not delete the field itself from the
                                             					 file. The field must be there in the record; it can be an empty string
                                             					 delimited with a comma. |

| Field | Description |
|---|---|
| Select Export Format | The file format to be used in the export file. For ERL data,
                                             					 either csv (comma-separated value) or XML. |
| Enter Export File Name | The name of the file you want to create. Do not include a file
                                             					 extension. |
| Export button | Click Export to create the export file. |
| Close button | Click Close to close the window. |

| Note | Import ERL Data does not support configuring E.164 number with a leading plus sign ( +). Ensure that you remove the leading
                                          plus sign before importing onsite alert details. |
|---|---|

| Field | Description |
|---|---|
| Select Import Format | Select the format used in the file you are importing. After you select the format, click View
                                                						sample file to see an example of the expected format and sequence of
                                             					 values. Use this sample information to create your import file in a
                                             					 spreadsheet. |
| Select File to Import | Select the file from which you want to import ERL data. |
| Upload button | Click Upload to upload a file from your local system. See Upload File for more information. |
| Import button | Click Import to add ERL data from the import file to the Emergency Responder database. Note The
                                                         						imported ERL data overwrites conflicting data in the Emergency Responder
                                                         						database. | Note | The
                                                         						imported ERL data overwrites conflicting data in the Emergency Responder
                                                         						database. |
| Note | The
                                                         						imported ERL data overwrites conflicting data in the Emergency Responder
                                                         						database. |
| Close button | Click Close to close the window. |

| Note | The
                                                         						imported ERL data overwrites conflicting data in the Emergency Responder
                                                         						database. |
|---|---|

| Field | Description | Notes |
|---|---|---|
| ERL Search Parameters |
| Find Off-Premises ERL where... | Select search criteria and click Find to list existing Off-Premise ERLs.
                                          					 To list all ERLs, click Find without entering any criteria. From the drop-down list, you can select the
                                          					 number of records that display per page for each search. From the search results list, you can: Click an entry to view and update its characteristics. Click the Copy icon to create a new ERL with the same ALI data. Click the Delete icon to remove the ERL. Click view... in the Audit Trail column to view a history of changes made to that ERL. See ERL Audit Trail for more information. | When copying an ERL, information that must be unique in an ERL
                                          					 is not copied. |
| Add New ERL | Click Add New
                                             						ERL to create a new ERL. |  |

| Field | Description | Note |
|---|---|---|
| ERL Settings |
| ERL Name | The name of the ERL. The naming strategy you use is critical.
                                             					 The ERL name is one of the primary pieces of information your security team
                                             					 sees when alerted to an emergency call. If the name is easy to understand and
                                             					 very descriptive, it can help your team respond quickly to a call. Work with your security team to develop an ERL naming strategy. | You cannot change the name of an existing ERL. To change an ERL
                                             					 name, create a new ERL, then delete the old ERL. Any leading and trailing spaces is trimmed. |
| Description | Enter a description of the new ERL (optional). |  |
| Route/Translation Pattern Settings |
| Route/Translation Pattern | The phone number, defined as a route pattern in Cisco Unified Communications Manager, that is configured to use the gateway
                                             the call should be routed through to get to the correct PSAP. This number must include the external emergency number, such
                                             as 911 in the USA. For example, 10.911 or 10911. The pattern can only contain numbers and dots. |  |
| Add button | To
                                             					 add a route point, choose a route point from the drop-down list and click Add . |  |
| Remove button | To
                                             					 remove a combination, select it in the list and click Remove . |  |
| Onsite Alert Settings |  |
| Available Onsite Alert IDs | Text box that displays the IDs of all available onsite alert
                                             					 personnel. | You must first add the contact to the list of onsite alert
                                             					 personnel. |
| Add button | Select the onsite alert (security) contacts to be assigned to
                                             					 the ERL. These contacts are notified when an emergency call is made from the
                                             					 ERL. To add a contact, select an Onsite Alert ID from the Available Onsite
                                             					 Alert IDs list and click Add .
                                             					 The contact ID then appears in the Onsite Alert IDs for the ERL text box. |  |
| Remove button | To
                                             					 remove a contact for the ERL, select the appropriate ID in the Onsite Alert IDs
                                             					 for the ERL text box and click Remove . |  |
| ERL Address |
| ALI Details button | Click ALI Details to view or change the automatic location information (ALI) of an ERL. The ALI provides detailed information
                                             about the location of the ERL, such as street address and phone number. |  |
| Time Zone | Select a time zone for the ERL. The time zone provides the list of all available time zones. | When you dial 911, the selected time zone is set as the local call time in Pager and Emergency alert. If a time zone is not
                                             selected, then the local call time is same as the system call time. |
| Insert button | Click Insert to save your changes to the new ERL. | The Insert button is only available when creating a new ERL. |
| Cancel Changes button | Click Cancel
                                                						Changes to change the fields on this page back to the last saved
                                             					 settings. |  |
| Update button | Click Update to save your changes to the ERL. | The Update button is only available when changing an existing
                                             					 ERL. |
| Close button | Click Close to close the window. You must click Update or Insert to save your changes before you click Close . |  |

| Field | Description |
|---|---|
| Find DIDs where... | Select search criteria and click Find to list the result of a query on the National E911 Service Provider secondary status server. |

| Field | Description | Notes |
|---|---|---|
| ERL Search Parameters |
| Find National E911 Service Provider ERL where... | Select search criteria and click Find to list existing National E911 Service Provider ERLs. To list all ERLs, click Find without entering any criteria. From the drop-down list, you can select the number of records that display per page for each
                                          search. From the search results list, you can: Click an entry to view and update its characteristics. Click the Copy icon to create a new ERL with the same ALI data. Click the Delete icon to remove the ERL. Click view... in the Audit Trail column to view a history of changes made to that ERL. See ERL Audit Trail for more information. | When copying an ERL, information that must be unique in an ERL
                                          					 is not copied. See Add New ERL for more information. |
| Add New ERL | Click Add New
                                             						ERL to create a new ERL. | See Add New ERL for more information. |
| Level of service button | Click Level of service to display the level of service that National E911 Service Provider designates for the specific address that is configured in the ALI details. National E911 Service Provider supports the following level of service: No Coverage— National E911 Service Provider does not have access to the selective router and cannot provide the callback number and address to the PSAP that services
                                                that address. Basic—The PSAP that provides service currently can not provide emergency support for wire line services or VoIP service providers. Enhanced—Calls can be routed to the PSAP with the existing E9-1-1 selective router network, and National E911 Service Provider can provide the callback number and address to the PSAP. |  |
| Bulk TN Update button | Select multiple ERLs and click Bulk TN
                                             						Update to update the ELIN for the selected ERL. |  |
| Export | Click the Export link to create a file containing your ERL configuration. | See Export ERL Data for information about exporting ERL
                                          					 data. |
| Import | Click the Import link to create or update ERLs using information stored in a
                                          					 separate file. By importing ERL data, you can create or update many ERLs at one
                                          					 time. | See Import ERL Data for information about importing
                                          					 ERL data. |

| Field | Description |
|---|---|
| Default ALI Values for National E911 Service Provider ERLs |
| Type of Service | Defines the type of service for the calling party number, such
                                          					 as FX in 911 area or Non-Pub. Note National E911 Service Provider recommends setting the default to Non-Pub. | Note | National E911 Service Provider recommends setting the default to Non-Pub. |
| Note | National E911 Service Provider recommends setting the default to Non-Pub. |
| Class of Service | Defines the class of service for the calling party number, such
                                          					 as residential, business, VoIP. Note National E911 Service Provider recommends setting the default to VoIP. | Note | National E911 Service Provider recommends setting the default to VoIP. |
| Note | National E911 Service Provider recommends setting the default to VoIP. |
| Company ID | Specified by National E911 Service Provider . |
| Customer Name | Specified by National E911 Service Provider . |
| Update button | Click Update to save your changes. |
| Cancel Changes button | Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings. |

| Note | National E911 Service Provider recommends setting the default to Non-Pub. |
|---|---|

| Note | National E911 Service Provider recommends setting the default to VoIP. |
|---|---|

| Note | Query in Secondary Status is not supported with RedSky. |
|---|---|

| Field | Description |
|---|---|
| Find ELINS where... | Select search criteria and click Find to list the result of a query on the National E911 Service Provider secondary status server. |

| Field | Description | Notes |
|---|---|---|
| Add new
                                          					 schedule | Specify the day of the week and time of the day when you want to
                                          					 schedule an update: Select
                                                						  the days of the week when you want to run the switch port and phone update
                                                						  process. Select
                                                						  the time of day when you want the process to run. 00 hour and 00 min is
                                                						  midnight. Time is based on the 24-hour clock. Check
                                                						  the Enable Schedule check box if you
                                                						  want to activate this schedule. Choose
                                                						  either ALI Update Schedule or Secondary Status Update Schedule . | We recommend that you run the National E911 Service Provider update process at least once per day. Because of the added network traffic, it is best to run the process outside normal
                                          business hours. |
| Add button | Click Add to
                                          					 add the schedule to the list of schedules. |  |
| Cancel Changes button | Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings. |  |
| Update button | Click Update when viewing an existing schedule to save changes you make to the schedule. | Only available when viewing an existing schedule. |

| Note | View ALI Discrepancies is not supported with RedSky. |
|---|---|

| Field | Description |
|---|---|
| Find ELIN where... | Enter search criteria to select the ELIN that you want to find. To find all ELIN, click Find without entering any criteria. To narrow your search, select the field that you want to search
                                          					 on from the drop-down list, select the search relationship (is contains, begins
                                          					 with, and so on), and enter the search string. Click Find . |

| Field | Description |
|---|---|
| View National E911 Service Provider ALI Discrepancies |
| ALI Fields | List of ALI field information from the local Emergency Responder database and from National E911 Service Provider database: House Number House Suffix Street Name Prefix Directional Street Suffix Post Directional Community Name State Main NPA Class of Service Type of Service Exchange Customer Name Order Number Extract Date County ID Company ID Zip Code Zip Code Extension Customer Code Comments Longitude Latitude Elevation TAR Code Location Reserved |
| Save button | Click Save to save your changes in the local Emergency Responder database. |
| Save National E911 Service Provider ALI Info button | Click Save National E911 Service Provider ALI Info to update the National E911 Service Provider VUI database. |
| Cancel Changes button | Click Cancel
                                                						Changes to change the fields on this page back to the last saved
                                             					 settings. |
| Close button | Click Close to close the window. |

| Field | Description |
|---|---|
| Status | Displays status messages |
| ERL Search Parameter |
| Find | Select search criteria and click Find to list either existing Conventional ERLs or National E911 Service Provider ERLs. From the search results list, you can select the ERLs that you
                                          					 want to migrate |
| Migrate to National E911 Service Provider ERL Button | When you search for Conventional ERLs, you can select the ERLs that you want to migrate to National E911 Service Provider . When you click the Migrate to National E911 Service Provider ERL button, you can select an National E911 Service Provider route point for all the selected ERL. |
| Migrate to Regular ERL | When you search for National E911 Service Provider ERLs, you can select the ERLs that you want to migrate to a conventional ERL data. When you click the Migrate to Regular ERL button, you can
                                          					 enter a route point, and specify whether the ERL is a test ERL and test the
                                          					 ERL. |

| Field | Description | Notes |
|---|---|---|
| Add SNMPv2 Community Setting |
| IP Address/Host Name | The IP address or hostname of a switch whose SNMP read community
                                             					 string you are defining. If you use the same read community string for all switches, you
                                             					 only need to define one entry: *.*.*.*. If you use different read community strings for sets of
                                             					 switches, you can define each set, using variables and ranges. For example, if
                                             					 you have 10 switches from 10.1.115.0 to 10.1.125.0, you can use 10.1.115-125.0
                                             					 as the IP address. You can also mix ranges and variables, such as
                                             					 *.*.115-125.*. Note If you are using IPv6 address, then wildcard characters are not supported. Enter the details for each switch. | Note | If you are using IPv6 address, then wildcard characters are not supported. Enter the details for each switch. | You are not defining your switches on this page, you are only
                                             					 associating IP address patterns to read community strings. Emergency Responder only tries to use the string with the
                                             					 specific switches you identify on the LAN Switch Details page. See LAN Switch Details for more information. If two or more patterns match an IP address, Emergency Responder
                                             					 uses the SNMP string associated with the most closely matching pattern. |
| Note | If you are using IPv6 address, then wildcard characters are not supported. Enter the details for each switch. |
| Timeout | The time, in seconds, in which Emergency Responder should
                                             					 consider an attempted SNMP connection to a switch to have failed. See the
                                             					 explanation of Retries for more information. | Default is 10 seconds. The optimal value is 10 to 15 seconds. |
| Maximum Retry Attempts | The number of times Emergency Responder should attempt to
                                             					 contact a switch. With each retry, the previous timeout is multiplied by 2, to
                                             					 ensure that the switch has enough time to respond. For example, if you specify
                                             					 10 for timeout, the first attempt times out in 10 seconds, the second attempt
                                             					 times out in 20 seconds, the third attempt times out in 40 seconds, and so
                                             					 forth. | Default is 2 retries. This number does not include the initial
                                             					 attempt; that is, if retries are 2, Emergency Responder attempts to contact a
                                             					 switch up to 3 times (the initial attempt plus 2 retries). The optimal value is 2 to 3 retries. |
| Read Community | The SNMPv2 read community string for the switch. The name can contain up to 50 characters and can contain any combination of alphanumeric characters, hyphens (-), and underscore
                                                characters (_). Note Community string does not support special characters like angle brackets (< >), backslash (\), colon (:), quotation marks
                                                         (“ “), and tilde (~). | Note | Community string does not support special characters like angle brackets (< >), backslash (\), colon (:), quotation marks
                                                         (“ “), and tilde (~). | Default is public for any IP address not covered in the SNMPv2
                                             					 settings list. |
| Note | Community string does not support special characters like angle brackets (< >), backslash (\), colon (:), quotation marks
                                                         (“ “), and tilde (~). |
| Insert | Click the Insert button to add the entry to the
                                             					 list of SNMP settings. |  |
| Cancel Changes | Click the Cancel Changes button to change the
                                             					 fields on this page back to the last saved settings. |  |
| SNMPv2 Settings | A list of SNMPv2 settings that you have already defined. To change an entry, click any of the links associated with the
                                             					 entry to load the details into the edit boxes at the top of the page. Then make
                                             					 your changes and click Update . To delete an entry, click the Delete icon for the entry. |  |
| Add New | Click the Add New button to add another SNMPv2
                                             					 setting. |  |
| Update | Click the Update button to save changes you make
                                             					 to an existing SNMPv2 setting. | Only available when viewing an existing setting. |
| Export | Click the Export button to export the SNMPv2 data
                                             					 settings to another file. For more information, see Export SNMPv2 Data . |  |
| Import | Click the Import button to import the SNMPv2 data
                                             					 settings to your Cisco Emergency Responder configuration. For
                                             					 more information, see Import SNMPv2 Data . |  |

| Note | If you are using IPv6 address, then wildcard characters are not supported. Enter the details for each switch. |
|---|---|

| Note | Community string does not support special characters like angle brackets (< >), backslash (\), colon (:), quotation marks
                                                         (“ “), and tilde (~). |
|---|---|

| Field | Description |
|---|---|
| Export
                                                					 SNMPv2 Data |  |
| Select
                                                					 Export Format | Select
                                                					 the file format from the drop-down list that matches the file being imported. |
| Enter
                                                					 Export File Name | Enter the
                                                					 name of the file that you want to create. Do not include the file extension. |
| Export | Click the Export button to add data from the import file to
                                                					 your Cisco Emergency Responder configuration. |
| Close | Click the Close button to close the window. |
| Export
                                                					 Status | This text box displays status information. |
| Download |  |
| Select a
                                                					 File to Download | Select a
                                                					 file from the drop-down list and click the Download button to download the file to your
                                                					 machine. |

| Field | Description |
|---|---|
| Import
                                                					 SNMPv2 Data |  |
| Select
                                                					 Import Format | Select
                                                					 the file format from the drop-down list that matches the file being imported. Click View sample file link to view an example of the
                                                					 expected format and sequence of values. Use this sample information to create
                                                					 your import file in a spreadsheet. |
| Select
                                                					 File to Import | Select
                                                					 the file from the drop-down list from which you want to import data. |
| Import | Click the Import button to add data from the import file to
                                                					 your Cisco Emergency Responder configuration. |
| Upload | Click the Upload button to upload the file from your machine.
                                                					 For more information, see Upload File . |
| Close | Click the Close button to close the window. |
| Import
                                                					 Status | This text box displays status information. |

| Field | Description | Notes |
|---|---|---|
| Add SNMPv3 User Details |
| User Information |
| IP
                                             					 Address/Host Name | Enter the
                                             					 IP address or hostname of the Cisco Unified Communications Manager or LAN
                                             					 switch. | For IPv4 address, you
                                             					 can use an asterisk (*) as a wildcard character. Note For IPv6 address, wildcard characters are not supported. You can
                                             					 also use a range of number for octets, such as 15 to 30. | Note | For IPv6 address, wildcard characters are not supported. |
| Note | For IPv6 address, wildcard characters are not supported. |
| User Name | Enter the
                                             					 username configured on Cisco Unified Communications Manager or LAN switch. | The name
                                             					 can contain up to 32 characters and can contain any combination of alphanumeric
                                             					 characters, hyphens (-), and underscore characters (_). |
| Authentication
                                                						Information |
| Password | To enable
                                             					 authentication, check the Authentication Required check box; in the Password
                                             					 and the Reenter Password fields, enter the password for the user configured on
                                             					 the Cisco Unified Communications Manager or LAN switch. |  |
| Protocol | Choose
                                             					 the appropriate protocol as configured for the user on Cisco Unified
                                             					 Communications Manager or LAN switch. |  |
| Privacy Information |
| Password | If you
                                             					 selected the Authentication Required check box, you can specify the privacy
                                             					 information. To require
                                             					 privacy, select the check box, enter the password in both the Password, and the
                                             					 Reenter Password fields for the user configured on the Cisco Unified
                                             					 Communications Manager or LAN switch. |  |
| Protocol | Choose the
                                             					 appropriate protocol as configured for the user on Cisco Unified Communications
                                             					 Manager or LAN switch. |  |
| Other Information |
| Timeout
                                             					 (in seconds) | The length
                                             					 of time that an attempted SNMP connection remains idle before it is considered
                                             					 to have failed. For more
                                             					 information, see the explanation for Maximum Retry Attempts. | The
                                             					 default value is 10 seconds. The optimal value is 10 to 15 seconds. |
| Maximum
                                             					 Retry Attempts | The number
                                             					 of times Emergency Responder attempts to contact a Cisco Unified Communications
                                             					 Manager or a switch. With each
                                             					 retry, the previous timeout is multiplied by two to ensure that the switch has
                                             					 time to respond. For example, if you specify a Timeout value of 10 seconds, the
                                             					 first attempt times out in 10 seconds, the second attempt times out in 20
                                             					 seconds, and the third attempt times out in 40 seconds. | The
                                             					 default value is two. But the optimal value is two to three retries. The
                                             					 Maximum Retry Attempts does not include the initial attempt. For example, if
                                             					 Maximum Retry Attempts is set to two, Emergency Responder attempts to contact a
                                             					 switch three times - the initial attempt plus two retries. |
| Insert | Click the Insert button to add the entry to the
                                             					 list of SNMP settings. |  |
| Cancel Changes | Click the Cancel Changes button to change the
                                             					 fields on this page back to the last saved settings. |  |
| SNMPv3 Settings | A list of SNMPv3 settings that you have already
                                             					 defined. To change an entry, click any of the links
                                             					 associated with the entry to load the details into the edit boxes at the top of
                                             					 the page. Then make your changes and click Update . To delete an entry, click the Delete icon for the entry. |  |
| Add New | Click the Add New button to add another SNMPv3
                                             					 setting. |  |
| Update | Click the Update button to save changes you make
                                             					 to an existing SNMPv3 setting. | Only available when viewing an existing setting. |
| Import | Click the Import button to import the SNMPv3 data
                                             					 settings to your Cisco Emergency Responder configuration. For
                                             					 more information, see Import SNMPv3 Data . |  |

| Note | For IPv6 address, wildcard characters are not supported. |
|---|---|

| Field | Description |
|---|---|
| Import
                                                					 SNMPv3 Data |  |
| Select
                                                					 Import Format | Select
                                                					 the file format from the drop-down list that matches the file being imported. Click View sample file link to view an example of the
                                                					 expected format and sequence of values. Use this sample information to create
                                                					 your import file in a spreadsheet. |
| Select
                                                					 File to Import | Select
                                                					 the file from the drop-down list from which you want to import data. |
| Import | Click the Import button to add data from the import file to
                                                					 your Cisco Emergency Responder configuration. |
| Upload | Click the Upload button to upload the file from your machine.
                                                					 For more information, see Upload File . |
| Close | Click the Close button to close the window. |
| Import
                                                					 Status | This text box displays status information. |

| Field | Description | Notes |
|---|---|---|
| Incremental Phone Tracking |
| Incremental Phone Tracking Interval | The time, in minutes, between making updates to the known phone
                                          					 locations. This periodic update ensures that phones that have moved are located
                                          					 and assigned to the correct ERL. Click Update to save your changes to this field. | The default is 30 minutes. The range of the interval that can be defined is 5 to 300
                                          					 minutes. |
| Enhanced Location Phone Tracking | The time, in minutes, between making updates to the unknown phone locations. This periodic update ensures that devices that have moved are located and assigned
                                          to the correct ERL. Click Update to save your changes to this field. | The default is 2 minutes. The range of the interval that can be defined is 1 to 180 minutes. Note By default, AXL Incremental Phone tracking should not be greater than Incremental Phone tracking. | Note | By default, AXL Incremental Phone tracking should not be greater than Incremental Phone tracking. |
| Note | By default, AXL Incremental Phone tracking should not be greater than Incremental Phone tracking. |
| Add New Schedule | Enter the schedule that you want to add: Select
                                                						  the days of the week when you want to run the switch port and phone update
                                                						  process. Select
                                                						  the time of day when you want the process to run. 00 hour and 00 min is
                                                						  midnight. Time is based on the 24-hour clock. | We recommend that you run the switch port and phone update
                                          					 process at least once per day. Because of the added network traffic, it is best
                                          					 to run the process outside normal business hours. |
| Insert button | Click Insert to add the schedule to the list of schedules. |  |
| Cancel Changes button | Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings. |  |
| Update button | Click Update when viewing an existing schedule to save changes that you make to the
                                          					 schedule. | Only available when viewing an existing schedule. |
| Switch-Port and Phone Update
                                          					 Schedule | The list of schedules you have defined. To change a schedule, click the Hour link, the Minute link, or
                                          					 the Edit icon to load it into the Modify Schedule area above the list. Then,
                                          					 make your changes and click Update . To remove a schedule, click the Delete icon for the schedule. | If any schedules overlap, only one schedule is run. |
| Add New button | Click Add New to
                                          					 add another schedule. |  |

| Note | By default, AXL Incremental Phone tracking should not be greater than Incremental Phone tracking. |
|---|---|

| Field | Description | Notes |
|---|---|---|
| Add New Cisco Unified Communications Manager Cluster |  |
| Cisco Unified Communications Manager | The IP address or DNS name of a Cisco Unified Communications Manager server that is running Cisco Unified Communications Manager
                                          and SNMP services. Only add one server per Cisco Unified Communications Manager cluster—Emergency Responder can identify the other servers in
                                          the cluster. The Cisco Unified Communications Manager server you specify represents the cluster in which it is a member. | When viewing a previously defined Cisco Unified Communications Manager server, Emergency Responder displays a CCM List link. Click CCM List to view a list of the Cisco Unified Communications Manager servers that belong to the same cluster as the selected server. Note The Cisco Unified Communications Manager servers should have run the CCM service at least once. After the IP address or DNS name has been configured, it cannot
                                          					 be modified. | Note | The Cisco Unified Communications Manager servers should have run the CCM service at least once. |
| Note | The Cisco Unified Communications Manager servers should have run the CCM service at least once. |
| CTI Manager | The IP address or DNS name of the CTI Manager used by the specified Cisco Unified Communications Manager server. |  |
| CTI Manager User Name | The name of the user created in the Cisco Unified Communications Manager server for Emergency Responder use. | This user must have specific characteristics and device
                                          					 assignments. See Create Emergency Responder Cisco Unified Communications Manager User for specific information. |
| CTI Manager Password | The password for the user. |  |
| Backup CTI Manager 1 | The IP address or DNS name of the backup CTI Manager used by the specified Cisco Unified Communications Manager server. |  |
| Backup CTI Manager 2 | The IP address or DNS name of the backup CTI Manager used by the specified Cisco Unified Communications Manager server. |  |
| Telephony Port Begin Address | The number of the first CTI port to use for calling onsite alert
                                          					 (security) personnel. When an emergency call is made, Emergency Responder calls
                                          					 the onsite alert personnel for the originating ERL using the telephony ports
                                          					 you configure here. | You must first create this port in Cisco Unified Communications Manager. See Create Required CTI Ports for more information. |
| Number of Telephony Ports | The number of CTI ports. Enter the number of CTI ports you created in Cisco Unified Communications Manager. The number of
                                          ports is the number of concurrent calls Emergency Responder can make to onsite alert personnel. | The ports used are in sequence from the beginning port. For
                                          					 example, if you enter 3000 for the begin port, and 4 for number of ports,
                                          					 Emergency Responder uses 3000, 3001, 3002, and 3003. |
| Enable Secure Connection |
| Enable Secure Connection check box | Check this check box to enable a secure connection. You can
                                          					 enter data in the other fields of this section only if you have enabled Secure
                                          					 Connection. |  |
| TFTP Server IP Address | The IP address of the TFTP server. |  |
| TFTP Server Port | The port of the TFTP server. |  |
| Backup TFTP Server IP Address | The IP address of the backup TFTP server, for the Unified CM
                                          					 node being added. |  |
| CAPF Server IP Address | The IP address of the CAPF server. |  |
| CAPF Server Port | The port of the CAPF server. |  |
| Instance ID for Publisher | The instance ID for the Publisher node. |  |
| Secure Authentication String for Publisher | The secure authentication string for the Publisher node. |  |
| Instance ID for Subscriber | The instance ID for the Subscriber node. |  |
| Secure Authentication String for Subscriber | The secure authentication string for the Subscriber node. |  |
| Enable SRTP for Audio Alerts | Check this check box if you want Emergency Responder to send Secure Real-Time Transport Protocol (SRTP) enabled Onsite Phone
                                          alert to Onsite Security Users during an Emergency Call. With this option enabled for each Unified Communication Manager cluster,
                                          the Emergency Responder Onsite personnel receive secured onsite audio alerts. The default value for this check box leaves it unchecked. Note Ensure that the onsite phone supports encrypted audio calls and is properly configured in the Unified Communications Manager
                                                   to get the onsite audio alerts. | Note | Ensure that the onsite phone supports encrypted audio calls and is properly configured in the Unified Communications Manager
                                                   to get the onsite audio alerts. | The value of this field gets determined by the setting of the Unified Communications Manager service parameter Block Unencrypted Calls . This parameter specifies whether Unified Communications Manager allows calls from Emergency Responder without data encryption. When the Block Unencrypted Calls parameter is set to TRUE, only calls with media encryption support are allowed and unencrypted calls are blocked. When the Block Unencrypted Calls parameter is set to FALSE, calls are allowed whether or not their media is encrypted. |
| Note | Ensure that the onsite phone supports encrypted audio calls and is properly configured in the Unified Communications Manager
                                                   to get the onsite audio alerts. |
| AXL Settings |
| AXL Username | The username for the application user on Cisco Unified
                                          					 Communications Manager with privileges to perform AXL queries. | Note The selected user in the Cisco Emergency Responder Location Management application server in Unified CM should match the user
                                                      in the Cisco Emergency Responder page: Phone Tracking > CUCM > AXL Username . Though, the Emergency Responder AXL username and CTI username have the required permissions, the username selected in the
                                                      application server must match the AXL username. After updating the application server username, you must also restart the CUCM Cisco E911 network service on all the nodes
                                                      in the cluster. This service restart causes the Unified CM 911 to use the new userID and establish the connection between
                                                      the two servers. | Note | The selected user in the Cisco Emergency Responder Location Management application server in Unified CM should match the user
                                                      in the Cisco Emergency Responder page: Phone Tracking > CUCM > AXL Username . Though, the Emergency Responder AXL username and CTI username have the required permissions, the username selected in the
                                                      application server must match the AXL username. After updating the application server username, you must also restart the CUCM Cisco E911 network service on all the nodes
                                                      in the cluster. This service restart causes the Unified CM 911 to use the new userID and establish the connection between
                                                      the two servers. |
| Note | The selected user in the Cisco Emergency Responder Location Management application server in Unified CM should match the user
                                                      in the Cisco Emergency Responder page: Phone Tracking > CUCM > AXL Username . Though, the Emergency Responder AXL username and CTI username have the required permissions, the username selected in the
                                                      application server must match the AXL username. After updating the application server username, you must also restart the CUCM Cisco E911 network service on all the nodes
                                                      in the cluster. This service restart causes the Unified CM 911 to use the new userID and establish the connection between
                                                      the two servers. |
| AXL Password | The password for the application user on Cisco Unified
                                          					 Communications Manager with privileges to perform AXL queries. |  |
| AXL Port Number | The port number that is used by the application on Cisco Unified
                                          					 Communications Manger. The default value is 8443. |  |
| SNMP Settings |
| Use SNMPv3
                                          					 for discovery | Check this
                                          					 check box if the Cisco Unified Communications Manager has SNMPv3 enabled and
                                          					 you want Emergency Responder to use SNMPv3 for discovery. |  |
| Insert button | Click Insert to add the new CiscoUnifiedCommunicationsManager
                                          					 server to the list of servers. |  |
| Cancel Changes button | Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings. |  |
| Update button | Click Update when viewing an existing server to save changes you
                                          					 make to the server. | Only available when viewing an existing server. Replaces the Insert button when viewing an existing server. |
| Cisco Unified Communications Manager Clusters |
| Add New button | Click Add New to add another Cisco Unified Communications Manager server. |  |
| Cisco Unified Communications Manager list | A list of Cisco Unified Communications Manager servers defined for this Emergency Responder group. Click a server link or
                                          the Edit icon to view and modify the Emergency Responder configuration for the server. Click the Delete icon to delete the server. Click Number of Users associated link to find
                                          					 the list of remote users associated with the Cisco Unified Communications
                                          					 Manager Server node. |  |

| Note | The Cisco Unified Communications Manager servers should have run the CCM service at least once. |
|---|---|

| Note | Ensure that the onsite phone supports encrypted audio calls and is properly configured in the Unified Communications Manager
                                                   to get the onsite audio alerts. |
|---|---|

| Note | The selected user in the Cisco Emergency Responder Location Management application server in Unified CM should match the user
                                                      in the Cisco Emergency Responder page: Phone Tracking > CUCM > AXL Username . Though, the Emergency Responder AXL username and CTI username have the required permissions, the username selected in the
                                                      application server must match the AXL username. After updating the application server username, you must also restart the CUCM Cisco E911 network service on all the nodes
                                                      in the cluster. This service restart causes the Unified CM 911 to use the new userID and establish the connection between
                                                      the two servers. |
|---|---|

| Note | Cisco Emergency Responder supports SNMP Version 1, Version 2 , Version 2C, and Version 3 of a LAN switch. |
|---|---|

| Note | Switches should not be configured with Static Engine ID. |
|---|---|

| Field | Description |
|---|---|
| LAN Switch Details |
| Switch Host Name/IP Address | The IP address or DNS name of the switch. For more information on standardized valid IPv4 or IPv6 address formats, see the following: https://docs.oracle.com/javame/config/cdc/ref-impl/pbp1.1.2/jsr217/java/net/Inet4Address.html https://docs.oracle.com/javame/config/cdc/ref-impl/pbp1.1.2/jsr217/java/net/Inet6Address.html |
| Description | Description of this switch. |
| Enable CAM-based Phone Tracking | Check this check box if there might be phones attached to this
                                          					 switch that do not use the Cisco Discovery Protocol (CDP) to announce
                                          					 themselves to the network. For non-CDP phones, Emergency Responder must use the
                                          					 Content Addressable Memory (CAM) information about the switch to identify
                                          					 phones. |
| Use port description as port location | Check this check box if you want to display the switch port
                                          					 description that is configured on the switch in the Location Field. Note When the checkbox is enabled, the port description for each port will be updated in the database to reflect the location of
                                                      the port during each discovery. As a result, the time taken for the discovery process will be impacted depending on the number
                                                      of ports with descriptions on the switch. | Note | When the checkbox is enabled, the port description for each port will be updated in the database to reflect the location of
                                                      the port during each discovery. As a result, the time taken for the discovery process will be impacted depending on the number
                                                      of ports with descriptions on the switch. |
| Note | When the checkbox is enabled, the port description for each port will be updated in the database to reflect the location of
                                                      the port during each discovery. As a result, the time taken for the discovery process will be impacted depending on the number
                                                      of ports with descriptions on the switch. |
| Use SNMPv3
                                          					 for Discovery | Select
                                          					 this check box if the switch has SNMPv3 enabled and Emergency Responder should
                                          					 discover it using SNMPv3. |
| Insert button | Check Insert to add the switch to the list of switches. When you click Insert, Emergency Responder asks if you want to
                                          					 run the switch port and phone update process on the switch right away. Click OK to
                                          					 run the process now, or click Cancel to add the switch to the configuration without running the process right away. Note See Manually Run the Switch-Port and Phone Update Process for information about running the process if you select not to run it
                                                      						immediately. | Note | See Manually Run the Switch-Port and Phone Update Process for information about running the process if you select not to run it
                                                      						immediately. |
| Note | See Manually Run the Switch-Port and Phone Update Process for information about running the process if you select not to run it
                                                      						immediately. |
| Update button | Click Update when viewing an existing switch to save changes that you make to the switch. |
| Cancel Changes button | Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings. |
| LAN Switches |
| LAN Switch list | A
                                          					 list of the switches you have already defined. Click the IP address/DNS name of
                                          					 the switch or click the Edit icon to view and modify settings for the switch. Click the Delete icon to delete the switch. |
| Add LAN Switch button | Click Add LAN
                                             						Switch to add another switch. |
| Export | Click the Export link to export the switch definitions to another file. See Export LAN Switch for more information. |
| Import | Click the Import link to import a list of switches into the Emergency Responder configuration.
                                          					 This list might be exported from your network management software. See Import LAN Switch for more information. |

| Note | When the checkbox is enabled, the port description for each port will be updated in the database to reflect the location of
                                                      the port during each discovery. As a result, the time taken for the discovery process will be impacted depending on the number
                                                      of ports with descriptions on the switch. |
|---|---|

| Note | See Manually Run the Switch-Port and Phone Update Process for information about running the process if you select not to run it
                                                      						immediately. |
|---|---|

| Field | Description |
|---|---|
| Select Export Format | The format to use for the file, such as CSV (comma- separated
                                             					 values). |
| Enter Export File Name | The name of the file you want to create. Do not include the file
                                             					 extension. |
| Export button | Click Export to create the file. The Status
                                             					 box shows the status of the exportation. |
| Close button | Click Close to close the window. |
| Download |
| Select a File to Download | Use the pull-down menu to select a LAN switches configuration
                                             					 file and click Download to download the file to your
                                             					 local system. |

| Field | Description |
|---|---|
| Select Import Format | Select the format used in the file you are importing. After you select the format, click view
                                                						sample file to see an example of the expected format and sequence of
                                             					 values. Use this sample information to create your import file in a
                                             					 spreadsheet, or to determine if your network management software can create the
                                             					 required format. |
| Select File to Import | Select the file from which you want to import data. Before you can import a file, you must place it in the folder
                                             					 mentioned on this page. |
| Upload button | Click Upload to upload a file from your local system. See Upload File for more information. |
| Import button | Click Import to add data from the information in the import file to your Emergency Responder
                                             					 configuration. Emergency Responder asks you whether you want to run phone
                                             					 tracking on the imported switch. You must run phone tracking before you can
                                             					 configure the switch ports, so normally you should choose OK . If
                                             					 you choose Cancel , Emergency Responder imports the switches but does
                                             					 not run the phone tracking process. Note If you
                                                         						elect not to run the phone-tracking process, after importing the file, run the
                                                         						switch port and phone update process. See Manually Run the Switch-Port and Phone Update Process . | Note | If you
                                                         						elect not to run the phone-tracking process, after importing the file, run the
                                                         						switch port and phone update process. See Manually Run the Switch-Port and Phone Update Process . |
| Note | If you
                                                         						elect not to run the phone-tracking process, after importing the file, run the
                                                         						switch port and phone update process. See Manually Run the Switch-Port and Phone Update Process . |
| Close button | Click Close to close the window. |
| Import Status | Text box that displays status information. |

| Note | If you
                                                         						elect not to run the phone-tracking process, after importing the file, run the
                                                         						switch port and phone update process. See Manually Run the Switch-Port and Phone Update Process . |
|---|---|

| Note | If the IOS software on the switch needs to be upgraded to the latest version, execute the snmp-server ifindex persist command before the upgrade. Failure in executing this command leads to a change of port indexes. In that scenario, Emergency
                                          Responder treats the existing port as a new port and turns the assigned ERL to Blank (no ERL). |
|---|---|

| Field | Description | Notes |
|---|---|---|
| Switch Port Search
                                             						Parameters |
| Find ports where | Enter search criteria to select the ports that you want to view
                                          					 or configure. To view all ports, click Find without entering any criteria. To narrow your search: Select All to indicate that only calls that match every criteria be selected (an AND search); select Any to indicate that calls that match any search criteria be selected (an OR search). From the pull-down menu, select the field
                                                that you want to search on (ERL Name, Phone MAC Address, and so on), select the search relationship (contains, starts with,
                                                and so on), enter the search string, and select how many results on page are displayed. To search on a combination of fields, click the Plus icon ( + ) to add more search parameters. Click the Minus icon ( – ) to remove search parameters.) Click Find when you have entered all the search parameters. | If you are configuring ports, generate a list of ports using the Find button. |
|  | The list of switch ports that match your search criteria, one
                                          					 line per port. To assign ERLs to selected ports, check the check box to the
                                          					 left of the switch details, enter the ERL name in the text box, or click Search
                                             						ERL to find and select the ERL, then click Assign
                                             						ERL . To view and update the phone location for a port, click the View link in the port's Location column. Note Location name or switch port description cannot include special characters, such as the pound sign (#), comma (,), percentage
                                                      (%), ampersand (&), question mark (?), and forward slash (/). To change the fields shown in the list and to change their
                                          					 order, click Edit
                                             						View . This action opens a separate Edit View page: To add a field, select it in the Available Fields list and click > (right arrow). To remove a field, select it in the Selected Fields list and click < (left arrow). Note You cannot
                                                      						remove the ERL Name from the table view. Click Apply to save your changes on the Edit Table View page. Click Close to close the window. | Note | Location name or switch port description cannot include special characters, such as the pound sign (#), comma (,), percentage
                                                      (%), ampersand (&), question mark (?), and forward slash (/). | Note | You cannot
                                                      						remove the ERL Name from the table view. | Emergency Responder displays a maximum number of 1,000 switch
                                          					 port records at a time. If the search results in more than 1,000 switch ports,
                                          					 an error message to refine the search is displayed. If many ports match your search criteria, Emergency Responder uses several pages to display them. Use the First, Previous,
                                          Next, and Last links at the bottom of the page to move between pages. You can also enter a specific page number on the Page
                                          field and press Enter to move to that page. |
| Note | Location name or switch port description cannot include special characters, such as the pound sign (#), comma (,), percentage
                                                      (%), ampersand (&), question mark (?), and forward slash (/). |
| Note | You cannot
                                                      						remove the ERL Name from the table view. |
| Export | Click Export to export the ERL to switch port configuration to another file. See Export Switch Ports for more information. |  |
| Import | Click Import to import a set of ERL-to-port mappings into the Emergency Responder
                                          					 configuration. See Import Switch Ports for more information. |  |

| Note | Location name or switch port description cannot include special characters, such as the pound sign (#), comma (,), percentage
                                                      (%), ampersand (&), question mark (?), and forward slash (/). |
|---|---|

| Note | You cannot
                                                      						remove the ERL Name from the table view. |
|---|---|

| Field | Description |
|---|---|
| Select Export Format | The format to use for the file, such as CSV (comma-separated
                                             					 values). |
| Enter Export File Name | The name of the file you want to create. Do not include the file
                                             					 extension. |
| Export button | Click Export to create the file. The Status box shows the status of the exportation. |
| Close button | Click Close to close the window. |
| Download |
| Select a File to Download | Use the pull-down menu to select a file and click Download to download the file to your local system. |

| Field | Description |
|---|---|
| Select Import Format | Select the format used in the file you are importing. After you select the format, click view
                                                						sample file to see an example of the expected format and sequence of
                                             					 values. You can use this sample information to create your import file in a
                                             					 spreadsheet, but it is easier to export the switch port information from
                                             					 Emergency Responder, modify the export file using a spreadsheet program, and
                                             					 then import the modified file. Note See Export Switch Port Information for information about exporting
                                                         						switch port information. | Note | See Export Switch Port Information for information about exporting
                                                         						switch port information. |
| Note | See Export Switch Port Information for information about exporting
                                                         						switch port information. |
| Select File to Import | Select the file from which you want to import data. |
| Upload button | Click Upload to upload a file from your local system. See Upload File for more information. |
| Import button | Click Import to add data from the information in the import file to your Emergency Responder
                                             					 configuration. ERL assignments in the import file override assignments that
                                             					 already exist in the Emergency Responder configuration. Note Port ERL
                                                         						configurations are only updated if Emergency Responder has discovered the port
                                                         						before you import the port configuration. | Note | Port ERL
                                                         						configurations are only updated if Emergency Responder has discovered the port
                                                         						before you import the port configuration. |
| Note | Port ERL
                                                         						configurations are only updated if Emergency Responder has discovered the port
                                                         						before you import the port configuration. |
| Close button | Click Close to close the window. |
| Import Status | Text box that displays status information. |

| Note | See Export Switch Port Information for information about exporting
                                                         						switch port information. |
|---|---|

| Note | Port ERL
                                                         						configurations are only updated if Emergency Responder has discovered the port
                                                         						before you import the port configuration. |
|---|---|

| Note | The Save Switch Configuration functionality can be used only when the IP address of the old switch and the new switch is the
                                             same. If the IP address of the old switch and the new switch is different, you must perform an export switch functionality
                                             to export the old switch port details, delete the old switch records, and then import the new switch details. |
|---|---|

| Field | Description |
|---|---|
| Select Save Config Format | The format to use for the file, such as CSV (comma-separated values). |
| Enter Save Config File name | The name of the file you want to create. Do not include the file extension. |
| Save Config | Click Save Config to create the file. The Status box shows the status of the exportation. |
| Close | Click Close to close the window. |
| Download |
| Select a File to Download | Use the drop-down menu to select a file and click Download to download the file to your local system. |

| Note | The Upload Switch Port Configuration functionality can be used only when the IP address of the old and the new switch is the
                                             same. If the IP address of the old and new switch is different, you must perform an export switch functionality to export
                                             the old switch port details, delete the old switch records, and then import the new switch details. |
|---|---|

| Field | Description |
|---|---|
| Select Upload config File Format | Select the format used in the file you are importing. For example, CSV format. After you select the format, click View Sample File to see an example of the expected format and sequence of values. You can use this sample information to create your saved
                                             configuration file in a spreadsheet. See Save Switch Port Configuration for information about exporting saved switch port information. |
| Select File to Upload Config | From the drop-down list, choose the file which for you want to import data. |
| Upload | Click Upload to upload a file from your local system. The Status box shows the status of the exportation. You can find details on the total number of port updates, and details on the total number of ports that have changed for the
                                             location, and ERL changes and updates. |
| Close | Click Close to close the window. |

| Field | Description | Notes |
|---|---|---|
| Status | It
                                          					 displays various status messages based on the action performed in the Access
                                          					 point page: Ready—Displays when the Access Point page is loaded
                                                   						  successfully. Update
                                                   						  successful—Displays when an ERL assignment is made successfully. ERL
                                                   						  Not Found—Displays when trying to assign an ERL which is not available. |  |
| Access Point Search
                                             						Parameters |
| Find | Enter search criteria to select the Access Points that you want
                                          					 to view or configure. To view all Access Points, click Find without entering any criteria. To narrow your search: From
                                                						  the first Find drop-down list, choose one of the following
                                                						  criteria: Access Point Name Bssid ERL Name From
                                                						  the second where drop-down list, choose one of the following
                                                						  criteria: contains is
                                                         								not Empty starts with Ends with is
                                                         								Empty is
                                                         								Exactly Enter
                                                						  the required search string in next empty field. From the and show items per page drop-down list, choose the appropriate number of results to be displayed on the page. Click Find when you have entered all the search parameters. |  |
| Access
                                          					 Points | The
                                          					 following list displays the "Find" status information: Last
                                                   						  discovery was done at—Displays the time and date of the last major/AXL
                                                   						  discovery if the find result is successful. No
                                                   						  active query—This is displayed if you click the Access Point page without
                                                   						  clicking the Find button. No
                                                   						  matching records—This is displayed when Find is unable to retrieve the matching records. Phone Location tables are being modified. Please wait and try again—This is
                                                   						  displayed when the Cisco Emergency Recorder server is not loaded
                                                   						  completely. Phone Location details are not populated as phone tracking is still in
                                                   						  progress. Try after some time—This is displayed when the phone tracking engine
                                                   						  is still running. Cisco Emergency Responder server is not yet
                                                   						  initialized completely. Please wait—This is displayed when the Cisco Emergency Responder service is restarted. Cisco Emergency Responder is not running: Failed to
                                                   						  contact Cisco Emergency Responder —This is displayed when the Cisco Emergency Responder service is restarted. |  |
|  | The list of Access Points that match your search criteria, one
                                          					 line per Access Point. To assign ERLs to selected Access Point, check the check box to
                                          					 the left of the access details, enter the ERL name in the text box, or click Search ERL to find and select the ERL, then click Assign ERL . To view the phones associated to that Access Point, click the View Phones link in the Access Point's View Phones column. The phone details include Phone, MAC Address, IP Address, Extension, and Phone
                                          Type. For more information, see Access Point Phones . | Emergency Responder displays a maximum number of 1,000 Access
                                          					 Point records at a time. If the search results in more than 1,000 access
                                          					 points, an error message to refine the search is displayed. If a large number of points match your search criteria, Emergency Responder uses several pages to display them. Use the First , Previous , Next , and Last links at the bottom of the page to move between pages. You can also enter a specific page number on the Page field and press Enter to move to that page. |
| Export | Click Export to export the ERL to Access Point configuration to another file. For more information, see Access Point Phones . |  |

| Field | Description |
|---|---|
| Select Export Format | The format to use for the file, such as CSV (comma-separated
                                             					 values). |
| Enter Export File Name | The name of the file you want to create. Do not include the file
                                             					 extension. |
| Export button | Click Export to create the file. The Status box shows the
                                             					 status of the exportation. |
| Close button | Click Close to close the window. |
| Download |
| Select a File to Download | Use the drop-down menu to select a file and click Download to download the file to your local system. |

| Note | From Release 15SU1 onwards, Emergency Responder also supports IPv6 Subnets. Any specific reference to IP Subnets should be
                                       understood to mean either IPv4 or IPv6 Subnets. You can configure either IPv4 or IPv6 subnet when you navigate to ERL Membership > IP Subnets . |
|---|---|

| Note | Cisco Jabber devices will not work with IPv6 subnets in Emergency Responder. |
|---|---|

| Field | Description |
|---|---|
| IP Subnet Search Parameters |
| Find IP Subnets where... | To list specific IP subnets, select the search criteria and click Find .To list all IP subnets, click Find without entering any criteria. |
| IP Subnets |
| Add New IPv4 Subnet or Add New IPv6 Subnet |
| IP Subnets list | Displays results of the IPv4 and IPv6 Subnets search. For the IPv4 and IPv6 Subnets found, the system displays the Subnet
                                          ID, Subnet Mask (IPv4)/Prefix  Length (IPv6), ERL Name, and Location. Click on one of the preceding records or click the Edit icon to modify that IPv4 or IPv6 subnet. The Configure IPv4 Subnet or Configure IPv6 Subnet page appears. Change the Location
                                          field or the ERL Name field. Note When modifying an existing IPv4 subnet, you cannot change the Subnet ID or the Subnet Mask. Note When modifying an existing IPv6 subnet, you cannot change the Subnet ID or the Prefix Length. Click Update to save your changes to the IPv4 or IPv6 subnet. Click the View Phones icon in any record to view all of the IP subnet phones. The IP Subnet Phones page displays a list of the discovered phones
                                          in the IP subnet. See Configure IPv4 Subnet or Configure IPv6 Subnet (Applicable from Release 15SU1 Onwards) . Click the Delete icon to remove an IPv4 or IPv6 subnet. When you click Delete , Cisco Emergency Responder asks if you want to run the switch port, and the phone updates the process right away. Click OK to run the process immediately or click Cancel to delete the IPv4 or IPv6 subnet without running the process immediately. | Note | When modifying an existing IPv4 subnet, you cannot change the Subnet ID or the Subnet Mask. | Note | When modifying an existing IPv6 subnet, you cannot change the Subnet ID or the Prefix Length. |
| Note | When modifying an existing IPv4 subnet, you cannot change the Subnet ID or the Subnet Mask. |
| Note | When modifying an existing IPv6 subnet, you cannot change the Subnet ID or the Prefix Length. |
| Cancel Changes button | Click Cancel Changes to cancel any changes made on the Configure IPv4 Subnet or Configure IPv6 Subnet page. Note The Cancel Changes button is viewable only on the  Configure IPv4 Subnet or Configure IPv6 Subnet page. | Note | The Cancel Changes button is viewable only on the  Configure IPv4 Subnet or Configure IPv6 Subnet page. |
| Note | The Cancel Changes button is viewable only on the  Configure IPv4 Subnet or Configure IPv6 Subnet page. |
| Add New IP Subnet (IPv4) | Click Add New IP Subnet to configure new IPv4 subnets. The Configure IPv4 Subnet page appears. See Configure IPv4 Subnet for more information. |
| Add New IP Subnet (IPv6) | Click Add New IP Subnet to configure new IPv6 subnets. The Configure IPv6 Subnet page appears. See Configure IPv6 Subnet (Applicable from Release 15SU1 Onwards) for more information. |
| Export | Click Export to create a file containing the IP subnets configuration information. The Export IP Subnet page appears. See Export IP Subnets for more information. |
| Import | Click Import to import IP subnet configuration information from a file. The Import IP Subnet page appears. See Import IP Subnets for more information. |

| Note | When modifying an existing IPv4 subnet, you cannot change the Subnet ID or the Subnet Mask. |
|---|---|

| Note | When modifying an existing IPv6 subnet, you cannot change the Subnet ID or the Prefix Length. |
|---|---|

| Note | The Cancel Changes button is viewable only on the  Configure IPv4 Subnet or Configure IPv6 Subnet page. |
|---|---|

| Field | Description |
|---|---|
| Add New IPv4 Subnet |
| Subnet ID | Enter a valid IPv4 subnet address that you want to define. For more information on standardized valid IPv4 address formats, see https://docs.oracle.com/javame/config/cdc/ref-impl/pbp1.1.2/jsr217/java/net/Inet4Address.html . |
| Subnet Mask | The mask of the subnet you want to define. Based on the bit mask, this value represents the number of IPv4 addresses that
                                             are included in this subnet. |
| Do not track phones under this IP subnet | Check this check box if you do not want this IPv4 subnet and the underlying phones tracked by Cisco Emergency Responder. If
                                             you do not track the phones in an IPv4 subnet, then you do not need the Emergency Responder User Licenses for these phones. |
| Location (optional) | The location of the new IP subnet. |
| ERL Name | The ERL to assign to the subnet. Type in a valid ERL name or click Search ERL to find and select the ERL. |
| Insert button | Click Insert to add the subnet. When you click Insert , Emergency Responder asks if you want to run the switch port, and the phone updates the process on the switch immediately.
                                             Click OK to run the process now, or click Cancel to add the IPv4 subnet to the configuration without running the process immediately. |
| Cancel Changes button | Click Cancel Changes to change the fields on this page back to the last saved settings. |

| Field | Description |
|---|---|
| Add New IP Subnet |
| Subnet ID | Enter a valid IPv6 subnet address that you want to define. For more information on standardized valid IPv6 address formats, see https://docs.oracle.com/javame/config/cdc/ref-impl/pbp1.1.2/jsr217/java/net/Inet6Address.html . |
| Prefix Length | (Mandatory) Enter a prefix length for the subnet. The range is 1 to 128. |
| Do not track phones under this IP subnet | Check this check box if you do not want this IPv6 subnet and the underlying phones tracked by Cisco Emergency Responder. If
                                             you do not track the phones in an IPv6 subnet, then you do not need the Emergency Responder User Licenses for these phones. |
| Location (optional) | The location of the new IP subnet. |
| ERL Name | The ERL to assign to the subnet. Type in a valid ERL name or click Search ERL to find and select the ERL. |
| Insert button | Click Insert to add the subnet. When you click Insert , Emergency Responder asks if you want to run the switch port, and the phone updates the process on the switch immediately.
                                             Click OK to run the process now, or click Cancel to add the IPv6 subnet to the configuration without running the process immediately. |
| Cancel Changes button | Click Cancel Changes to change the fields on this page back to the last saved settings. |

| Field | Description |
|---|---|
| Select Export Format | Select the format used in the file that you are importing. After you select the format, click view
                                                						sample file to see an example of the expected format and sequence of
                                             					 values. Use this sample information to create your import file in a
                                             					 spreadsheet. |
| Enter Export File Name | The name of the file you want to create. Do not include the file
                                             					 extension |
| Export button | Click Export to add data from the import file to your Emergency Responder configuration. |
| Close button | Click Close to close the window. |
| Download |
| Select a File to Download | Use the pull-down menu to select a file and click Download to download the file to your local system. |

| Field | Description |
|---|---|
| Select Import Format | Select the format used in the file you are importing. After you select the format, click view
                                                						sample file to see an example of the expected format and sequence of
                                             					 values. Use this sample information to create or update your import file in a
                                             					 spreadsheet. |
| Select File to Import | Select the file from which you want to import data. |
| Upload button | Click Upload to upload a file from your local system. See Upload File for more information. |
| Import button | Click Import to add data from the import file to your Emergency Responder configuration. |
| Close button | Click Close to close the window. |
| Import Status | Text box that displays status information. |

| Field | Description |
|---|---|
| Unlocated Phone Search Parameters |
| Find phones where... | Enter search criteria to select the unlocated phones you want to
                                          					 find. To find all unlocated phones, click Find without entering any criteria. To narrow your search: Select All to indicate that only phones that match every criteria be selected (an AND
                                             						search); select Any to indicate that phones that match any search criteria be selected (an OR
                                             						search). From the pull-down menu, select the field you want to search on (Phone
                                             						Extension, Phone MAC Address, and so on), select the search relationship (is
                                             						Exactly, Starts with, and so on), and enter the search string. To search on a combination of
                                             						fields, click the Plus icon (+) to add additional search parameters. (Click the Minus icon to ( – ) remove search parameters.) Click Find when you have entered all of the search parameters. |
| Assign ERL | To assign the ERL, select the phones by checking the check box
                                          					 next to the phones, click Search
                                             						ERL to find and select the ERL, and click Assign
                                             						ERL . |
| Unassign ERL | To unassign a ERL, select the phones and click on Unassign ERL button. |
| List of unlocated phones | A
                                          					 list of the phones Emergency Responder could not assign to a specific ERL. The
                                          					 following information is displayed: Emergency Responder Group Phone IPv4
                                             						Address Phone IPv6 Address Phone Mac Address Phone Extension Assigned ERL Effective ERL ERL Rule If the phone has moved to a switch served by a different
                                          					 Emergency Responder group, the Emergency Responder group name is shown for the
                                          					 phone in the list. Note If there
                                                      						are a lot of unlocated phones, Emergency Responder uses more than one page to
                                                      						list them. You can only assign phones to ERLs from one page at a time. Use the
                                                      						links at the bottom of the list to move from page to page. | Note | If there
                                                      						are a lot of unlocated phones, Emergency Responder uses more than one page to
                                                      						list them. You can only assign phones to ERLs from one page at a time. Use the
                                                      						links at the bottom of the list to move from page to page. |
| Note | If there
                                                      						are a lot of unlocated phones, Emergency Responder uses more than one page to
                                                      						list them. You can only assign phones to ERLs from one page at a time. Use the
                                                      						links at the bottom of the list to move from page to page. |

| Note | If there
                                                      						are a lot of unlocated phones, Emergency Responder uses more than one page to
                                                      						list them. You can only assign phones to ERLs from one page at a time. Use the
                                                      						links at the bottom of the list to move from page to page. |
|---|---|

| Field | Description |
|---|---|
| Select Export Format | Select the file format that matches the file being imported. After you select the format, click View Sample File to see an example of
                                             					 the expected format and sequence of values. Use this example when creating your
                                             					 imported file. |
| Enter Export File Name | The name of the file that you want to create. Do not include
                                             					 the file extension. |
| Export button | Click Export to add data from the import file
                                             					 to your Emergency Responder configuration. |
| Close button | Click Close to close the window. |
| Download |
| Select a File to Download | Use the pulldown menu to select a file. Click Download to download the file. |

| Note | When you are
                                          			 performing this search as part of an E.164 dial plan, the "+" is a valid
                                          			 character. |
|---|---|

| Field | Description |
|---|---|
| Manual Phone Search Parameters |
| Find manual phones where Line Number... | Enter search criteria to select the manually configured phones
                                          					 that you want to find. To find all manually configured phones, click Find without entering any criteria. To narrow your search, use the pull-down menu to select the
                                          					 search condition (contains, Starts with, and so on) and enter the line number
                                          					 in the text box. You can also select how many results are displayed per page
                                          					 from the pull-down menu. When you have specified your search criteria, click Find . |
| Manually Configure Phones |
| Manually Configured Phones list | Displays the search results. For each phone found, the system
                                          					 displays the Line Number, ERL Name, IPv4 Address, IPv6 Address, and Location. Click on one of these records or click the Edit icon to view and modify the information for that phone. The Modify Manual Phone
                                          					 page appears. You can change the MAC Address, IPv4 Address, IPv6 Address, Phone Type, Version, Location, and ERL Name. Note When
                                                      						modifying a manual phone, you cannot change the Subnet ID or the Line Number. Click Update to save your changes. | Note | When
                                                      						modifying a manual phone, you cannot change the Subnet ID or the Line Number. |
| Note | When
                                                      						modifying a manual phone, you cannot change the Subnet ID or the Line Number. |
| Add new Manual Phone | Click Add new
                                             						Manual Phone to add a manually configured phone. The Add New Manual Phone
                                          					 page appears. See Add New Manual Phone for more information. Note The Add new
                                                         						  Manual Phone button is also available from the Modify Manual Phone page. | Note | The Add new
                                                         						  Manual Phone button is also available from the Modify Manual Phone page. |
| Note | The Add new
                                                         						  Manual Phone button is also available from the Modify Manual Phone page. |
| Export | To export Manually Configured Phone information to a file, click Export on the Find and List Manually Configured Phones page. See Export Manual Phones for more information. |
| Import | To import Manually Configured Phone information to a file, click Import on the Find and List Manually Configured Phones page. See Import Manual Phones for more information. |

| Note | When
                                                      						modifying a manual phone, you cannot change the Subnet ID or the Line Number. |
|---|---|

| Note | The Add new
                                                         						  Manual Phone button is also available from the Modify Manual Phone page. |
|---|---|

| Field | Description |
|---|---|
| Add New Manual Phone |
| Line Number | The extension of the phone you want to define. |
| MAC Address | The MAC address of the phone, if it is an IP phone. |
| IPv4 Address | The IPv4 address of the phone, if it is an IP phone. |
| IPv6 Address | The IPv6 address of the phone, if it is an IP phone. |
| Phone Type | The type of phone, such as analog. This field is for your
                                             					 information only. |
| Version | The version of the phone software, if any. This field is for
                                             					 your information only. |
| Location | The location of the phone. |
| ERL Name | The ERL that you want to assign to the phone. To find and select
                                             					 the ERL, click Search
                                                						ERL . |
| Insert button | Click Insert to add the phone to the list of phones. Note The Insert
                                                         						button only appears when you are adding a phone. | Note | The Insert
                                                         						button only appears when you are adding a phone. |
| Note | The Insert
                                                         						button only appears when you are adding a phone. |
| Cancel Changes button | Click Cancel
                                                						Changes to change the fields on this page back to the last saved
                                             					 settings. |

| Note | The Insert
                                                         						button only appears when you are adding a phone. |
|---|---|

| Field | Description |
|---|---|
| Export Manual Phones |
| Select Export Format | Select the format used in the file you are importing. After you select the format, click view
                                                						sample file to see an example of the expected format and sequence of
                                             					 values. Use this sample information to create your import file in a
                                             					 spreadsheet. |
| Enter Export File Name | The name of the file that you want to create. Do not include the
                                             					 file extension. |
| Export button | Click Export to export the file to a file. |
| Close button | Click Close to close the window. |
| Download |
| Select a file to download | Use the pull-down menu to select a file and then click Download to download the file to your local system. |

| Field | Description |
|---|---|
| Select Import Format | Select the format used in the file you are importing. After you select the format, click view
                                                						sample file to see an example of the expected format and sequence of
                                             					 values. Use this sample information to create your import file in a
                                             					 spreadsheet. |
| Select File to Import | Select the file from which you want to import data. |
| Upload | Click Upload to upload a file from a local system. The Upload File page appears. See Upload File for more details. |
| Import button | Click Import to add data from the import file to your Emergency Responder configuration. |
| Close button | Click Close to close the window. |
| Import Status | Displays status messages. |

| Field | Description |
|---|---|
| Synthetic Phone Search Parameters |
| Find Synthetic phones where MAC Address | Enter search criteria to select the synthetic phones you want to
                                          					 find. To find all synthetic phones, click Find without entering any criteria. To narrow your search, use the pull-down menu to select the
                                          					 search condition (contains, Starts with, and so on) and enter the MAC address
                                          					 in the text box. You can also select how many results per page are displayed
                                          					 from the pull-down menu. When you have specified your search criteria, click Find . |
| Synthetic Phones |
| Synthetic Phones list | Displays the search results. For each phone found, the system
                                          					 displays the Line Number, ERL Name, IP Address, and Location. Click on one of
                                          					 these records or click the Edit icon to view and modify the information for that phone. The Modify Synthetic
                                          					 Phone page appears. You can change the MAC Address, IP Address, Phone Type,
                                          					 Version, Location, and ERL Name. Note When
                                                      						modifying a synthetic phone, you cannot change the Subnet ID or the Line
                                                      						Number. Click Update to save your changes. | Note | When
                                                      						modifying a synthetic phone, you cannot change the Subnet ID or the Line
                                                      						Number. |
| Note | When
                                                      						modifying a synthetic phone, you cannot change the Subnet ID or the Line
                                                      						Number. |
| Add new Synthetic Phone | Click Add new
                                             						Synthetic Phone to add a synthetic phone. The Add New Synthetic Phone page
                                          					 appears. See Add New Synthetic Phone for more information. Note The Add new
                                                         						  Synthetic Phone button is also available from the Modify Synthetic Phone
                                                      						page. | Note | The Add new
                                                         						  Synthetic Phone button is also available from the Modify Synthetic Phone
                                                      						page. |
| Note | The Add new
                                                         						  Synthetic Phone button is also available from the Modify Synthetic Phone
                                                      						page. |

| Note | When
                                                      						modifying a synthetic phone, you cannot change the Subnet ID or the Line
                                                      						Number. |
|---|---|

| Note | The Add new
                                                         						  Synthetic Phone button is also available from the Modify Synthetic Phone
                                                      						page. |
|---|---|

| Note | You cannot configure test ERLs for off-premise ERLs and National E911 Service Provider ERLs. |
|---|---|

| Field | Description | Notes |
|---|---|---|
| MAC Address | The MAC address of the synthetic phone, or a range of MAC
                                             					 addresses. | The synthetic MAC address must be within the range 00059a3b7700
                                             					 - 0059a3b8aff Enter the MAC address in this format: xx-xx-xx-xx-xx-xx or
                                             					 xxxxxxxxxxxx |
| ERL Name | The ERL to assign to the synthetic phone. Type in a valid ERL
                                             					 name or select the ERL from the drop-down list. |  |
| Insert button | Click Insert to add the synthetic phone to the list of phones. | The Insert button only appears when you are adding a phone. |
| New button | Click New to
                                             					 add another phone. | The New button only appears when you are viewing an existing phone. |
| Update button | Click Update when viewing an existing phone to save changes you make to the phone. | The Update button only appears when you are viewing an existing phone. |
| Cancel Changes button | Click Cancel
                                                						Changes to change the fields on this page back to the last saved
                                             					 settings. |  |

| Field | Description |
|---|---|
| User Search Parameters |
| Find User where User Name | Enter search criteria to select the users that you want to find. To find all users, click Find without entering any criteria. To narrow your search: Select All to indicate that
                                             						only users that match the selected criteria be displayed (an AND search). Select Any to indicate that users that match any search criteria be selected (an OR
                                             						search). From the pull down menu,
                                             						select the field that you want to search, select its corresponding relationship
                                             						and select how many results per page are displayed. The search fields and the
                                             						corresponding relationships are: Authentication Mode—Both, Remote or Local User
                                                      								Name— Ends with, Starts with, contains or Exactly. Unified CM Cluster—Ends with, Starts with, contains or Exactly. To search on a combination of
                                             						fields, click the Plus icon ( + ) to add additional search parameters. (Click the Minus
                                             						icon ( - ) to remove
                                             						search parameters.) Click Find when you have entered all of the search parameters. |
| User |
| Users list | This section of the page displays the search results. If there
                                          					 are no usernames are displayed after completion of the search, then no users
                                          					 have been configured yet. |
| Username | Displays the users name based on the selection criteria. |
| Authentication Mode | Displays the authentication mode of the user. The authentication
                                          					 mode can be either Remote or Local. |
| Unified CM Cluster | This value is displayed only when the user is authenticated
                                          					 remotely, with the Unified CM server. |
| Edit icon | Click the user name or the Edit icon to display the Modify User page, which
                                          					 allows you to change the user authentication mode, password and Unified CM
                                          					 cluster. The Modify User page also displays which groups and roles have been
                                          					 assigned to the user. |
| Delete icon | Click the Delete icon to delete the user from the system. Note You cannot
                                                      						delete the Administrator. | Note | You cannot
                                                      						delete the Administrator. |
| Note | You cannot
                                                      						delete the Administrator. |
| Add New User button | Click the Add New User button to open the Add User page. See Table 1 for a description of the Add User page. |
| Delete Users button | Click the Delete Users button to delete users in bulk. Select
                                          					 multiple users, both remote and local, by checking the check box and then
                                          					 clicking the Delete Users button. |
| Change to Remote Users button | Click the Change to Remote Users button to change local users
                                          					 to remotely authenticated users in bulk. |
| Change to IdP Users button | Click the Change to IdP Users button to change
                                          					 local or remote users to IdP users, whose password is maintained in IdP. |

| Note | You cannot
                                                      						delete the Administrator. |
|---|---|

| Field | Description |
|---|---|
| User Name | Enter the username for the new user. |
| Authentication Mode | Select the authentication mode of the new user. The user can
                                             					 either be a Remote user, Local user, or a IdP user. |
| Password | Enter the password for the new user. |
| Reset on
                                             					 Next Logon | Check the Reset on Next Logon check box to reset or change the
                                             					 password after a successful sign-in. This
                                             					 field is enabled only for the local users. |
| Confirm Password | Reenter the password for the new user. |
| Unified CM Cluster | This field is enabled only when the user is a Remote user.
                                             					 Select a Unified CM cluster, from the drop-down list, to authenticate the
                                             					 remote user. |
| Insert button | Inserts the new user. |
| Cancel Changes button | Cancels changes made to the Add User page. |

| Field | Description |
|---|---|
| User Name | Displays the name of the user whose information is being
                                             					 modified. Note You cannot
                                                         						change the username on the Modify User page. | Note | You cannot
                                                         						change the username on the Modify User page. |
| Note | You cannot
                                                         						change the username on the Modify User page. |
| Authentication Mode | Change the authentication mode for a user. You can change a
                                             					 local user to a remote user and a remote user to local user. |
| Password | Enter the new password for the user. |
| Reset on Next Logon | Check the Reset on Next Logon check box to reset
                                             					 or change the password after a successful sign-in. This field is enabled only for the local users. |
| Confirm Password | Reenter the new password for the user. |
| Unified CM Cluster | Select a Unified CM cluster. This is required when you change a
                                             					 local user to remote user. You can also change the Unified CM cluster of an
                                             					 existing remote user to another Unified CM Cluster. Note The
                                                         						Unified CM Cluster drop down box are enabled only when the authentication mode
                                                         						is selected as remote. | Note | The
                                                         						Unified CM Cluster drop down box are enabled only when the authentication mode
                                                         						is selected as remote. |
| Note | The
                                                         						Unified CM Cluster drop down box are enabled only when the authentication mode
                                                         						is selected as remote. |
| Update button | Applies changes made from the Modify User page. Note User
                                                         						authentication at passphrase change is valid only for the Cisco ER
                                                         						Administration page. Active sessions of the user in any of the other navigation
                                                         						pages do not get cancelled. | Note | User
                                                         						authentication at passphrase change is valid only for the Cisco ER
                                                         						Administration page. Active sessions of the user in any of the other navigation
                                                         						pages do not get cancelled. |
| Note | User
                                                         						authentication at passphrase change is valid only for the Cisco ER
                                                         						Administration page. Active sessions of the user in any of the other navigation
                                                         						pages do not get cancelled. |
| Cancel Changes button | Cancels changes made to the Modify User page. |
| Add new User | Click this button to add a new user. The Add User page appears. See Table 1 for more information. |
| Activate User | Click Activate User to activate the user account. The option is enabled only when that particular user is
                                             					 inactive. The option is always disabled for remote users. |
| Unlock User | Click Unlock User to unlock the account. The option is enabled only when that particular user account
                                             					 is locked. The option is always disabled for remote users. |
| User Groups for this user | Displays the groups to which the user is assigned. |
| User Roles for this user | Displays the roles to which the user is assigned. |

| Note | You cannot
                                                         						change the username on the Modify User page. |
|---|---|

| Note | The
                                                         						Unified CM Cluster drop down box are enabled only when the authentication mode
                                                         						is selected as remote. |
|---|---|

| Note | User
                                                         						authentication at passphrase change is valid only for the Cisco ER
                                                         						Administration page. Active sessions of the user in any of the other navigation
                                                         						pages do not get cancelled. |
|---|---|

| Field | Description |
|---|---|
| Unified CM Cluster | Select the Unified CM Cluster from the drop-down box to remotely
                                             					 authenticate the selected users. |
| Selected Users | Displays the local users that change to remote users. |
| Update button | Applies changes made from the Change to Remote Users page. |
| Close button | Closes the window. |

| Field | Description |
|---|---|
| Role Search Parameters |
| Find Role where Role Name is | Enter search criteria to select the role you want to find. To find all roles, click Find without entering any criteria. To narrow your search, use the pull-down menu to select the
                                          					 search condition (contains, Starts with, and so on) and enter the role in the
                                          					 text box. You can also select how many results per page are displayed from the
                                          					 pull-down menu. When you have specified your search criteria, click Find . |
| Roles | Section of the page in which the search results are displayed.
                                          					 These default roles are created during installation: Emergency Responder System
                                             						Admin Emergency Responder ERL Admin Emergency Responder Network
                                             						Admin Emergency Responder User When you click on the Role Name link or the Description link for
                                          					 any of the default roles, the Standard Role page for that role displays, which
                                          					 displays the following information: Role Name Description List of resources assigned to
                                             						that role Note You cannot
                                                      						modify any of the information for default roles. You can only modify
                                                      						information for roles that you create. After you create additional roles, they are listed along with
                                          					 the default roles. When you click on the role name, description, or Edit icon
                                          					 for a role that you have created, the Modify Role page appears. See Table 1 for more information about the
                                          					 Modify Role page. | Note | You cannot
                                                      						modify any of the information for default roles. You can only modify
                                                      						information for roles that you create. |
| Note | You cannot
                                                      						modify any of the information for default roles. You can only modify
                                                      						information for roles that you create. |
| Edit icon | Click the Edit icon to display the Modify Role page. See Table 1 for information about the Modify
                                          					 Role page. |
| Delete icon | Click the Delete icon to delete the role from the system. Note You cannot
                                                      						delete any of the default roles. | Note | You cannot
                                                      						delete any of the default roles. |
| Note | You cannot
                                                      						delete any of the default roles. |
| Add New Role button | Click Add New
                                             						Role to display the Add Role page. This button is also available on the
                                          					 Modify Role and Add Role pages. See Table 1 for information about the Add Role
                                          					 page. |

| Note | You cannot
                                                      						modify any of the information for default roles. You can only modify
                                                      						information for roles that you create. |
|---|---|

| Note | You cannot
                                                      						delete any of the default roles. |
|---|---|

| Field | Description |
|---|---|
| Add Role |
| Role Name | The name of the new role you are adding. |
| Description | A
                                             					 description of the new role. |
| Resource Permissions | This section of the page displays a list of all available
                                             					 resources. The check boxes to the left of each resource allow you to select or
                                             					 deselect the resource to be assigned to the new role. |
| Select All button | Click Select
                                                						All to select all the listed resources. |
| Clear All button | Click Clear
                                                						All to deselect all currently selected resources. |
| Insert button | Click Insert to add the new role. |
| Cancel Changes button | Click Cancel
                                                						Changes to cancel the Add Role operation. |

| Note | You cannot modify
                                             			 any information for the four default roles. |
|---|---|

| Field | Description |
|---|---|
| Modify Role |
| Role Name | The name of the new role you are modifying. Note The Role
                                                         						Name cannot be changed. | Note | The Role
                                                         						Name cannot be changed. |
| Note | The Role
                                                         						Name cannot be changed. |
| Description | A
                                             					 description of the role you are modifying. Modify the description by adding new
                                             					 text in the text box. |
| Resource Permissions | This section of the page displays a list of all available
                                             					 resources. The check boxes to the left of the resources indicate which
                                             					 resources have been assigned to this role. Modify the resource assignments by
                                             					 checking or unchecking the boxes. |
| Select All button | Click Select
                                                						All to select all the listed resources. |
| Clear All button | Click Clear All to deselect all currently selected resources. |
| Update button | Click Update to save the changes made to the Modify Role page. |
| Cancel Changes button | Click Cancel
                                                						Changes to cancel the changes made to the Modify Role page. |
| Add new Role button | Allows you to add a new role. See the Add Role for information about adding new
                                             					 roles. |

| Note | The Role
                                                         						Name cannot be changed. |
|---|---|

| Field | Description |
|---|---|
| User Group Search Parameters |
| Find User Group where User Group Name | Enter search criteria to select the user group you want to find. To find all user groups, click Find without entering any criteria. To narrow your search, use the pull-down menu to select the
                                          					 search condition (contains, Starts with, and so on) and enter the user group in
                                          					 the text box. You can also select how many results per page are displayed from
                                          					 the pull-down menu. When you have specified your search criteria, click Find . |
| User Groups | Section of the page in which the search results are displayed.
                                          					 When you click on the User Group Name link, the Description link, or the Edit
                                          					 icon, the Modify User Group page appears. See Modify User Group for information. |
| Edit icon | Click the Edit icon to display the Modify User Group page. See Modify User Group for information. |
| Delete icon | Click the Delete icon to delete the user group from the system. Note You cannot
                                                      						delete default user groups that were created during installation. | Note | You cannot
                                                      						delete default user groups that were created during installation. |
| Note | You cannot
                                                      						delete default user groups that were created during installation. |
| Add New User Group button | Click the Add New
                                             						User Group button to display the Add User Group page. See Table 1 for information about the Add User
                                          					 Group page. |

| Note | You cannot
                                                      						delete default user groups that were created during installation. |
|---|---|

| Field | Description |
|---|---|
| Add User Group |
| User Group Name | The name of the new user group you are adding. |
| Description | A
                                             					 description of the new user group. |
| Add Users to the Group | This section of the page has a text box that displays the names
                                             					 of the users you add to the user group. |
| Add Users button | Allows you to add users to the new group. When you click Add
                                                						Users , the Add Users page appears. See Add User for more information. |
| Remove Users button | Allows you to remove users from the group. To do so, highlight
                                             					 the username in the text box and click Remove
                                                						Users . |
| Assign Roles to Group | This section of the page has a text box that displays the roles
                                             					 you assign to the new user group. |
| Add Roles button | Allows you to assign roles to the new group. When you click Add
                                                						Roles , the Add Roles page appears. See Add Role for more information. |
| Remove Roles button | Allows you to remove roles from the group. To do so, highlight
                                             					 the role name in the text box and click Remove
                                                						Roles . |
| Insert button | Click Insert to add the new role. |

| Field | Description |
|---|---|
| Modify User Group |
| User Group Name | The name of the user group you are modifying. Note The User
                                                         						Group Name cannot be changed. | Note | The User
                                                         						Group Name cannot be changed. |
| Note | The User
                                                         						Group Name cannot be changed. |
| Description | A
                                             					 description of the User Group you are modifying. Modify the description by
                                             					 adding or changing text in the text box. |
| Add Users to the Group | This section of the page has a text box that displays the names
                                             					 of the users currently in the user group. |
| Add Users button | Allows you to add more users to the group. When you click Add
                                                						User , the Add User page appears. See Add User for more information. |
| Remove Users button | Allows you to remove users from the group. To do so, highlight
                                             					 the username in the text box and click Remove
                                                						Users . |
| Assign Roles to Group | This section of the page has a text box that displays the roles
                                             					 currently assigned to the user group. |
| Add Roles button | Allows you to assign more roles to the group. When you click Add
                                                						Roles , the Add Role page appears. See Add Role for more information. Note You cannot
                                                         						add roles to the default roles that were assigned to a default user group
                                                         						during installation. If the user group that you are modifying is a default user
                                                         						group, then the Add
                                                            						  Roles button is not visible. | Note | You cannot
                                                         						add roles to the default roles that were assigned to a default user group
                                                         						during installation. If the user group that you are modifying is a default user
                                                         						group, then the Add
                                                            						  Roles button is not visible. |
| Note | You cannot
                                                         						add roles to the default roles that were assigned to a default user group
                                                         						during installation. If the user group that you are modifying is a default user
                                                         						group, then the Add
                                                            						  Roles button is not visible. |
| Remove Roles button | Allows you to remove roles from the group. To do so, highlight
                                             					 the role name in the text box and click Remove
                                                						Roles . Note You cannot
                                                         						remove the default roles that were assigned to a default user group during
                                                         						installation. If the user group you are modifying is a default user group, then
                                                         						the Remove
                                                            						  Roles button is not visible. | Note | You cannot
                                                         						remove the default roles that were assigned to a default user group during
                                                         						installation. If the user group you are modifying is a default user group, then
                                                         						the Remove
                                                            						  Roles button is not visible. |
| Note | You cannot
                                                         						remove the default roles that were assigned to a default user group during
                                                         						installation. If the user group you are modifying is a default user group, then
                                                         						the Remove
                                                            						  Roles button is not visible. |
| Update button | Click Update to save the changes made to the Modify User Group page. |
| Add New User Group button | Allows you to add a new user group. See Add User Group for information. |

| Note | The User
                                                         						Group Name cannot be changed. |
|---|---|

| Note | You cannot
                                                         						add roles to the default roles that were assigned to a default user group
                                                         						during installation. If the user group that you are modifying is a default user
                                                         						group, then the Add
                                                            						  Roles button is not visible. |
|---|---|

| Note | You cannot
                                                         						remove the default roles that were assigned to a default user group during
                                                         						installation. If the user group you are modifying is a default user group, then
                                                         						the Remove
                                                            						  Roles button is not visible. |
|---|---|

| Note | The
                                                				  Credential Policy option is enabled when the system is in the normal mode. The
                                                				  EnhancedSecurityMode Credential Policy option is enabled when the system is in
                                                				  Enhanced Security Mode. Local administrator accounts will never expire as they are always configured as standard users. Hence, if you update any credential
                                                policy or EnhancedSecurityMode credential policy for a local administrator the changes won't take effect. |
|---|---|

| Field | Description |
|---|---|
| Display Name | Credential Policy or EnhancedSecurityMode Credential Policy name is displayed based on the option selected by you. |
| Failed Logon | Specify the number of failed sign-in attempts allowed. You can enter a number between 1 to100. To allow unlimited failed sign-ins, check the No Failed Logon check box. Note The default setting specified for Cisco Emergency Responder (Emergency Responder) in a normal mode is set to 0 (if Emergency Responder is upgraded from pre 11.5 version) or 5 (if Emergency
                                                      Responder 11.5 is a fresh installation) or 3 (if Emergency Responder is in Enhanced Security Mode). | Note | The default setting specified for Cisco Emergency Responder (Emergency Responder) in a normal mode is set to 0 (if Emergency Responder is upgraded from pre 11.5 version) or 5 (if Emergency
                                                      Responder 11.5 is a fresh installation) or 3 (if Emergency Responder is in Enhanced Security Mode). |
| Note | The default setting specified for Cisco Emergency Responder (Emergency Responder) in a normal mode is set to 0 (if Emergency Responder is upgraded from pre 11.5 version) or 5 (if Emergency
                                                      Responder 11.5 is a fresh installation) or 3 (if Emergency Responder is in Enhanced Security Mode). |
| Reset Failed Logon Attempts Every (minutes) | Specify the number of minutes after which the counter is reset for failed sign-in attempts. You can log in again after the
                                          counter is reset. Enter a number between 1 to120. The default setting specified for Emergency Responder in normal mode is 1 (if Emergency Responder is upgraded from pre 11.5
                                          version) or 30 (if Emergency Responder 11.5 is a fresh installation) or 30 (if Emergency Responder is in Enhanced Security
                                          Mode). |
| Credential Expires After (days) | Specify the number of days after which the credential or password expires. Enter a number between 0 to 365. To allow credentials to never expire, enter 0 or check the Never Expires check box. The default setting is 0. Never Expires check box is checked if Emergency Responder is in normal mode (for both upgrade and fresh installation) and 180 if Emergency
                                          Responder is in Enhanced Security Mode. |
| Minimum Credential Length | Specify the minimum length for user credentials (password). Do not enter 0 as blank passwords are not allowed. Enter a number between1 to 64. Validation of, one uppercase, one lowercase, one numeric, and one special character on password happens only when the value
                                          is greater than or equal to four. The default setting is 1 if Emergency Responder is in normal mode (for both upgrade and fresh installation) and 14 if the
                                          Emergency Responder is in Enhanced Security Mode. |
| Minimum number of character changes between successive credentials | Specify the minimum characters that should be changed while updating a new password. Enter a number between of 0 to 64. The value should never be greater than the Minimum Credential Length field value. The default setting specified is 1 if Emergency Responder is in normal mode (for both upgrade and fresh installation) and
                                          4 if Emergency Responder is in Enhanced Security Mode. |
| Stored Number of Previous Credentials | Specify the number of previous user credentials to store. This setting prevents a user from configuring a recently used credential
                                          that is saved in the user list. Enter a number between 0 to 25. If you do not want to save any old credentials, enter 0. The default setting specified is 0 if Emergency Responder is in normal mode (for both upgrade and fresh installation) and
                                          12 if Emergency Responder is in Enhanced Security Mode. |
| Inactive Days Allowed | Specify the number of days that an account can remain inactive before the account gets deactivated. Enter a number between 0 to 5000. If you never want the account to be inactive, enter 0. The default setting specified is 0 for Emergency Responder both in the normal mode (for both upgrade and fresh installation)
                                          and in the Enhanced Security Mode. |
| Expiry Warning Days | Enter a number between 0 to 90 to specify the number of days before a user password expires and to start receiving warning
                                          notifications. The value should never be greater than the Credential Expires After (days) field. The default setting specified is 0 for Emergency Responder both in the normal mode (for both upgrade and fresh installation)
                                          and in the Enhanced Security Mode. |
| Save | Click the Save button to save the changes. |
| Clear Changes | Click the Clear Changes button to clear any change done in the fields and to restore the last saved information. |
| Set to Default | Click the Set to Default button to restore the default values settings depending on the Cisco Emergency Responder mode. |

| Note | The default setting specified for Cisco Emergency Responder (Emergency Responder) in a normal mode is set to 0 (if Emergency Responder is upgraded from pre 11.5 version) or 5 (if Emergency
                                                      Responder 11.5 is a fresh installation) or 3 (if Emergency Responder is in Enhanced Security Mode). |
|---|---|

| Field | Description |
|---|---|
| Call History Search Parameters |
| Search criteria | Enter search criteria to select the calls you want to find. To find all calls, click Find without entering any criteria. To narrow your search: Select All to indicate that only calls that match every criteria be selected (an AND
                                             						search); select Any to indicate that calls that match any search criteria be selected (an OR
                                             						search). From the pull down menu, select the field that you want to search on
                                             						(ERL Name, Caller Extension, and so on), select the search relationship
                                             						(contains, begins with, and so on), and enter the search string. To search on a combination of
                                             						fields, click the Plus icon (+) to add additional search parameters. Click the Minus icon ( – ) to remove search parameters. When you have entered all of
                                             						the search parameters, click Find . |
| Call History Matching
                                          					 Records | A
                                          					 list of emergency calls that match your search criteria is displayed with the
                                          					 following information: ERL Name—Click the name to
                                             						view details about the ERL and its ALI information. See Conventional ERL for descriptions of the
                                             						configuration fields. Caller Extension—The
                                             						extension used to place the emergency call. Time—The time the call was
                                             						made. Date—The date the call was
                                             						made. Route Pattern-ELIN No.—The
                                             						route pattern and ELIN combination used for the call. See Conventional ERL for more detailed information about
                                             						these fields. Location—The location of the
                                             						phone based on whether the phone was configured manually, or whether it was
                                             						configured based on the switch port or IP subnet. Call Acknowledged—The
                                             						acknowledged status of a call on the Web Alert page. Acknowledged By—The ID of the
                                             						user who acknowledged the call. Time Acknowledged—The time
                                             						that the call was acknowledged. Date Acknowledged—The date
                                             						that the call was acknowledged. Comments—Any comments entered
                                             						about the call. If you click the Edit icon, the Call Details page appears, on which you can enter or change comments
                                             						about the call in the Comments
                                                						  about the call text box. If a large number of calls match your search criteria, the
                                          					 system uses several pages to display them. Use the First, Previous, Next, and
                                          					 Last links at the bottom of the page to move between pages. You can also enter
                                          					 a specific page number in the Page field and press Enter to move to that page. |
| Download | Click Download to save the call history data to a spreadsheet that
                                          					 you can view or download to your local system. |
| Update | Click Update to include your comments in the call history for the call. Note Only
                                                      						viewable from the Call Details page. | Note | Only
                                                      						viewable from the Call Details page. |
| Note | Only
                                                      						viewable from the Call Details page. |
| Cancel Changes | Click Cancel
                                             						Changes to remove unsaved comments. You can then reenter comments. Note Only
                                                      						viewable from the Call Details page. | Note | Only
                                                      						viewable from the Call Details page. |
| Note | Only
                                                      						viewable from the Call Details page. |
| Close | Click Close to close the Call Details page. Note Only
                                                      						viewable from the Call Details page. | Note | Only
                                                      						viewable from the Call Details page. |
| Note | Only
                                                      						viewable from the Call Details page. |

| Note | Only
                                                      						viewable from the Call Details page. |
|---|---|

| Note | Only
                                                      						viewable from the Call Details page. |
|---|---|

| Note | Only
                                                      						viewable from the Call Details page. |
|---|---|

| Field | Description |
|---|---|
| ERL Audit Trail |
| Search criteria | Enter search criteria to select the audit details that you want
                                          					 to find. To find all audit details, click Find without entering any criteria. To narrow your search: Select All to indicate that only audit details that match every criteria be selected (an AND search); select Any to indicate that audit details that match any search criteria be selected (an OR search). From the pull-down menu, select
                                                the field that you want to search on (ERL Name, Modified By, and so on), select the search relationship (contains, begins
                                                with, and so on), and enter the search string. If searching by ERL Name, you can type in the ERL name or use the pull-down
                                                menu to select an ERL. To search on a combination of fields, click the Plus icon (+) to add additional search parameters. Click the Minus icon ( – ) to remove search parameters. When you have entered all of the search parameters, click Find . |
| Matching Records | A
                                          					 list of ERL change records that match your search criteria. Each change to an
                                          					 ERL is recorded in a separate record, so a single ERL may have many audit
                                          					 records. The list displays the following information for each record: ERL Name—The name of the ERL that was changed. Modified By—The login ID of the user who changed the ERL. Modified Time—The date and time the ERL was changed. Modification Details—A list of the fields that were changed in the ERL or its ALI. Use the scroll bars to move up and down
                                                in the Modification Details text box. Note If there
                                                      						are a large number of records match your search, Emergency Responder uses more
                                                      						than one page to list them. Use the links at the bottom of the list to move
                                                      						from page to page. You can also enter a page number in the Page field and press Enter to go to a specific page. | Note | If there
                                                      						are a large number of records match your search, Emergency Responder uses more
                                                      						than one page to list them. Use the links at the bottom of the list to move
                                                      						from page to page. You can also enter a page number in the Page field and press Enter to go to a specific page. |
| Note | If there
                                                      						are a large number of records match your search, Emergency Responder uses more
                                                      						than one page to list them. Use the links at the bottom of the list to move
                                                      						from page to page. You can also enter a page number in the Page field and press Enter to go to a specific page. |

| Note | If there
                                                      						are a large number of records match your search, Emergency Responder uses more
                                                      						than one page to list them. Use the links at the bottom of the list to move
                                                      						from page to page. You can also enter a page number in the Page field and press Enter to go to a specific page. |
|---|---|

| Note | If you change the
                                          			 customer code in your ALI record, Emergency Responder generates two records
                                          			 when exporting ALI: a Delete record to remove the ALI with the old code, and an
                                          			 Insert record to add the ALI with the new code. This Delete and Insert sequence
                                          			 is only generated the first time you export ALI after changing the code. You
                                          			 must ensure that you submit this export file to the service provider. |
|---|---|

| Field | Description |
|---|---|
| Export PS-ALI Records |
| Select NENA Format | The file format to be used in the export file, NENA formats 3.0,
                                          					 2.1, or 2.0. |
| File to Export | The name of the file you want to create. Do not include a file
                                          					 extension. |
| Company Name (NENA Header field) | The name of your company. You cannot have spaces in the name. Note The data
                                                      						complies with NENA requirements. | Note | The data
                                                      						complies with NENA requirements. |
| Note | The data
                                                      						complies with NENA requirements. |
| Cycle Counter (NENA Header field) | The sequence in which this export is created. This field is
                                          					 automatically increased each time you export data. You can change it if it
                                          					 becomes unsynchronized with the sequence submitted to your service provider.
                                          					 However, changing the sequence number does not affect the data placed in the
                                          					 file; if you are redoing an export, you must manually edit the export file to
                                          					 change the record status fields. Note The data
                                                      						complies with NENA requirements. | Note | The data
                                                      						complies with NENA requirements. |
| Note | The data
                                                      						complies with NENA requirements. |
| End of Line Format | Allows you to select the end-of-line format for the PS-ALI
                                          					 records that is exported for download. You can select from the following two
                                          					 formats: Windows style (\r\n) Unix/Linux style (\n) |
| Export button | Click Export to create the export file. |
| Download File | Click Download
                                             						File to download an exported PS-ALI file. |
| Cancel button | Click Cancel to cancel the export operation. |

| Note | The data
                                                      						complies with NENA requirements. |
|---|---|

| Note | The data
                                                      						complies with NENA requirements. |
|---|---|

| Note | If you change the
                                          			 customer code in your ALI record, Emergency Responder generates two records
                                          			 when exporting ALI: a Delete record to remove the ALI with the old code, and an
                                          			 Insert record to add the ALI with the new code. This Delete and Insert sequence
                                          			 is only generated the first time you export ALI after changing the code. You
                                          			 must ensure you submit this export file to the service provider. |
|---|---|

| Field | Description |
|---|---|
| Export PS-ALI Records |
| Select PS-ALI file (NENA 2.0 format) | The name of the PS-ALI file to be converted. The file must be in
                                          					 the default format, NENA format 2.0. |
| Output File (in csv format) Name | The name of the csv file that you want to create. |
| Convert button | Click Convert to create the csv file. |
| Cancel button | Click Cancel to stop the converting process. and close the window. |

| Field | Description |
|---|---|
| Select a file to Download | Use the pull-down menu to select a file and click Download to download the file to your local system. |
| Close
                                             					 button | Click Close to close the window. |

| Note | In a scenario where a Dual-stack phone has both the IPv4 and IPv6 addresses configured, and the phone falls under both the
                                          IPv4 and IPv6 subnets having the same priority, and one of the subnets is trackable and the other one is non-trackable, the
                                          phone is considered to be trackable. |
|---|---|

| Field | Description |
|---|---|
| ERL Debug Tool |
| Find Phones where extension | Enter search criteria to select the extensions that you want to
                                          					 find. To find all extensions, click Find without entering any criteria. To narrow your search, use the drop-down menu to select the search condition (contains, Starts with, and so on) and enter
                                          the extension in the text box. You can also select how many results per page are displayed from the drop-down menu. When you
                                          have specified your search criteria, click Find . |
| Matching records | Section of the page that displays the ERLs currently being used
                                          					 for routing emergency calls for the phones. For each extension found, the
                                          					 following information is displayed: Phone extension ERL Phone IPv4 Address Phone IPv6 Address MAC Address Why this ERL is Used? If the configurations are not correct, make any required
                                          					 changes. |
| Export
                                          					 button | Click Export to create the export file. |

| Field | Description |
|---|---|
| Select Export Format | The format to use for the file, such as CSV (comma-separated
                                             					 values). |
| Enter Export
                                             					 File Name | The name of the file you want to create. Do not include the file
                                             					 extension. |
| Export
                                             					 button | Click Export to create the file. The Status box shows the status of the exportation. |
| Close button | Click Close to close the window. |
| Download |
| Select a
                                             					 File to Download | Use the
                                             					 pull-down menu to select a file and click Download to download the file to your local system. |

| Field | Description |
|---|---|
| Select a Service Provider | Use the pull-down menu to select a service provider |
| Select an Input File for the
                                          					 ALI Formatting Tool from the List Below | Use the pull-down menu to select an input file |
| Submit button | Click the Submit button to display the Search for ELINs page, which is described in Table 2 . |

| Field | Description |
|---|---|
| Use Search to Filter-out
                                          					 ELINs on Area, City and Local Code(last 4-digits). | Allows you to search ELINs by Local Code, Area Code, or City
                                          					 Code. |
| Add (+) button | Adds more search parameters |
| Remove (-) button | Removes search parameters |

| Field | Description |
|---|---|
| Remove Changes/Generate File button | Shows all the ELINs that have been changed. |
| Search for ELIN | Displays the ELIN search page. |

| Field | Description |
|---|---|
| Add More ELIN | Displays the remaining ELINs that have not been changed. |
| Remove ELIN | Removes the selected ELINs from the list |
| Search for ELIN | Displays the ELIN search screen |
| Generate File button | Generates the formatted file. |

| Field | Description |
|---|---|
| Download Formatted File button | Displays a Download File dialog box so that the formatted file
                                          					 can be downloaded to the local system. |

| Field | Description |
|---|---|
| Search Parameters |
| Please Select: | From the pull-down menu, select the type of file that you want
                                          					 to search for. |
| Search button | Click Search to perform the search. |
| Exported Files | Area of the page that displays the search results. Displays the
                                          					 File Name, Last Modified data, and File Size for each file found. |
| Download button | Downloads the selected file. Note Before you
                                                      						click Download , click in the box next to the file name to select
                                                      						the file. To select all files listed, click in the box next to the File Name
                                                      						column heading. | Note | Before you
                                                      						click Download , click in the box next to the file name to select
                                                      						the file. To select all files listed, click in the box next to the File Name
                                                      						column heading. |
| Note | Before you
                                                      						click Download , click in the box next to the file name to select
                                                      						the file. To select all files listed, click in the box next to the File Name
                                                      						column heading. |
| Delete button | Deletes the selected file. Note Before you click Delete , click in the box next to the file name to select the file. To select all files listed, click in the box next to the File
                                                      Name column heading. | Note | Before you click Delete , click in the box next to the file name to select the file. To select all files listed, click in the box next to the File
                                                      Name column heading. |
| Note | Before you click Delete , click in the box next to the file name to select the file. To select all files listed, click in the box next to the File
                                                      Name column heading. |

| Note | Before you
                                                      						click Download , click in the box next to the file name to select
                                                      						the file. To select all files listed, click in the box next to the File Name
                                                      						column heading. |
|---|---|

| Note | Before you click Delete , click in the box next to the file name to select the file. To select all files listed, click in the box next to the File
                                                      Name column heading. |
|---|---|

| Field | Description |
|---|---|
| Status | Displays status messages |
| Purge Now |
| Purge Data older than | Specify the age of record that you want to delete. |
| Schedule Purge |
| Daily Purge at | Specify a time (UTC) during the day at which old records are deleted. |
| Purge Data older than | Specify the age of record that you want to delete. |
| Update | Click Update to save and activate your changes. |
| Cancel | Click Cancel
                                             						Changes to change the fields on this page back to the last saved
                                          					 settings. |

| Field | Description |
|---|---|
| Status | Displays
                                             					 status messages. |
| Server
                                             					 Name | Specifies
                                             					 the names of all the servers in the server group. |
| SSO
                                             					 Status | Displays
                                             					 one of the following statuses: Enabled Indicates that the SAML Single Sign-On is enabled on the server. Disabled Indicates that SAML Single Sign-On is disabled on the server. |
| Re-Import
                                             					 Metadata | Re-import Metadata field is enabled only when Single
                                             					 Sign-On is successfully enabled on the subscriber. Click the Re-import Metadata icon to import IdP metadata file from the
                                             					 publisher to the subscribers. Note This
                                                            						  option is displayed as N/A (Not Applicable) for the publisher node. | Note | This
                                                            						  option is displayed as N/A (Not Applicable) for the publisher node. |
| Note | This
                                                            						  option is displayed as N/A (Not Applicable) for the publisher node. |
| Last
                                             					 Metadata Import | Specifies
                                             					 the time when the IdP metadata was last imported on the server. This field
                                             					 displays "Never" if you are running the SAML Single Sign-On setup for
                                             					 the first time. |
| Export
                                             					 Metadata | Export Metadata field is enabled only when Single
                                             					 Sign-On is successfully enabled on both publisher and the subscriber. Click the Export
                                                						Metadata icon to download the server metadata file. A SAML metadata file
                                             					 must be generated for the specified server, and downloaded using the browser.
                                             					 You must then import this metadata file to the IdP server. Important If you
                                                         						change the hostname or domain of a node, ensure that you download the metadata
                                                         						from that node and upload the file to the IdP server again. The Export All Metadata button is enabled by default,
                                             					 regardless of whether the SAML Single Sign-On state set to active. | Important | If you
                                                         						change the hostname or domain of a node, ensure that you download the metadata
                                                         						from that node and upload the file to the IdP server again. |
| Important | If you
                                                         						change the hostname or domain of a node, ensure that you download the metadata
                                                         						from that node and upload the file to the IdP server again. |
| Last
                                             					 Metadata Export | Specifies
                                             					 the time when the SAML metadata file of the specified server was last exported.
                                             					 This field displays "Never" if you are running the SAML Single Sign-On setup for
                                             					 the first time. |
| SSO Test | Displays
                                             					 the test results of the SAML configuration with the IdP. The test ensures that
                                             					 the specified server trusts the IdP, and that the IdP trusts the specified
                                             					 server. The trust relationship between the server and the IdP depends on the
                                             					 success of exporting and importing of SAML metadata files. Displays
                                             					 one of the following values: Never Indicates that a test has not been performed on this server. Passed Indicates that a test has been successfully run on this server, and that the
                                                      							 server and the IdP trust one another. Failed Indicates that a test was attempted on the specified server, but that either
                                                      							 the server does not trust the IdP, or the IdP does not trust the server, or
                                                      							 some other network or IdP issue prevented the test from passing. |
| Run SSO
                                             					 Test | Click Run
                                                						SSO Test to run the Single Sign-On test. You must run this test before
                                             					 enabling SAML Single Sign-On. The SAML Single Sign-On setup cannot be completed
                                             					 until this test is successful. To run this test, there must be at least one
                                             					 LDAP synchronized user with administrator rights. You must also know the
                                             					 password for that user ID. Note You
                                                         						cannot run this test until the IdP metadata file is imported to the server, and
                                                         						the server metadata file is exported to the IdP server. | Note | You
                                                         						cannot run this test until the IdP metadata file is imported to the server, and
                                                         						the server metadata file is exported to the IdP server. |
| Note | You
                                                         						cannot run this test until the IdP metadata file is imported to the server, and
                                                         						the server metadata file is exported to the IdP server. |
| Enable
                                             					 SAML SSO | Click Enable
                                                						SAML SSO to start the SAML Single Sign-On configuration. |
| Export
                                             					 All Metadata | Click Export
                                                						All Metadata to export the SAML metadata files from each server. These
                                             					 files are converted to a compressed file (.zip) for easy download. You must
                                             					 extract the file and then import each file to the IdP. |
| Update
                                             					 IdP Metadata File | Click Update
                                                						IdP Metadata File to update IdP metadata on all the servers in the cluster. |
| Fix All
                                             					 Disabled Servers | Click Fix
                                                						All Disabled Servers to enable SAML Single Sign-On, on the servers on which
                                             					 it is disabled. |
| View
                                             					 IdP Trust Metadata File | Click View
                                                						IdP Trust Metadata File to download a copy of the IdP metadata file. |

| Note | This
                                                            						  option is displayed as N/A (Not Applicable) for the publisher node. |
|---|---|

| Important | If you
                                                         						change the hostname or domain of a node, ensure that you download the metadata
                                                         						from that node and upload the file to the IdP server again. |
|---|---|

| Note | You
                                                         						cannot run this test until the IdP metadata file is imported to the server, and
                                                         						the server metadata file is exported to the IdP server. |
|---|---|