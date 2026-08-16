---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-lync-integration-14-cup0-b-rcc-lync-server-integration-14-c-57a276d1a4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/lync_integration/14/cup0_b_rcc-lync-server-integration-14/cup0_b_rcc-lync-server-integration-1251_chapter_0100.html
retrieved_at: 2026-08-16T16:34:32.474216+00:00
---

Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 14 and SUs

# Remote Call Control with Microsoft Lync Server for IM and Presence Service, Release 14 and SUs

Updated: November 27, 2025

Chapter: Microsoft Component Integration Setup for IM and Presence Service

## Chapter: Microsoft Component Integration Setup for IM and Presence Service

# Microsoft Component Integration Setup for IM and Presence Service

## Line URI Setup on
                        	 Microsoft Active Directory

Before you
                              		  configure the Line URI parameter on Microsoft Active Directory, note the
                              		  following:

For the Line
                                    				URI, we recommend that you use the format: tel:xxxx;phone-context=dialstring where:

xxxx specifies
                                          					 the directory number that the CTI Manager reports to IM and Presence Service as the calling or
                                          					 called number when a call is placed.

phone-context=dialstring enables the Microsoft Lync client to control one of the devices that are associated with the directory
                                          					 number.

If you are using
                                          			 E.164 numbers, do not include phone-context=dialstring because it will result in
                                          			 an error at the Microsoft Lync client. See Lync Error When Using E.164 Numbers .

If you configure
                                    				the device ID, the Microsoft Lync client controls that particular device on initial sign in; for example: tel:xxxx;phone-context=dialstring;device=SEP0002FD3BB5C5

If you configure
                                    				the partition, the Microsoft Lync client specifies the partition for the directory number; for example: tel:xxxx;phone-context=dialstring;device=SEP0002FD3BB5C5;partition=myPartition

The Line URI
                                    				only takes effect when the Microsoft Lync user
                                    				signs in.

After initial
                                    				sign in, the Microsoft Lync user
                                    				can change the line appearance that they wish to control using the Cisco
                                    				Unified Communications Manager IM and Presence Service Lync Remote Call
                                    				Control Plugin.

If you do not
                                    				configure the device ID in the Line URI, the CTI Gateway determines the devices
                                    				that are associated with the line Directory Number (DN). If only one device is
                                    				associated with the line DN, the CTI Gateway uses that device.

You can also use
                                          			 the E.164 format for the Line URI. However, you must ensure that the DNs are
                                          			 also configured with E.164 on Cisco Unified Communications
                                             				Manager .

## IM and Presence
                        	 Service User Authentication

When
                              		  configuring the SIP URI on Microsoft Active Directory, consider how IM and Presence Service performs the user
                              		  authentication checks. The user authentication logic is as follows:

IM and Presence Service checks if the Microsoft Lync (sign in) user ID matches the Cisco Unified Communications
                                       				  Manager user ID. If IM and Presence Service cannot find a match:

IM and Presence Service checks if the Microsoft Lync user
                                    				email (the From header) matches the Cisco Unified Communications
                                       				  Manager user email. If IM and Presence Service cannot find a match:

IM and Presence Service checks if the Microsoft Lync user
                                    				email matches the ocsPrimaryAddress value of a Cisco Unified Communications
                                       				  Manager user.

For
                              		  example, a user Joe has the Microsoft Lync user
                              		  ID joe@someCompany.com. The From header in the SIP INVITE is
                              		  sip:joe@someCompany.com.

In this
                              		  case, IM and Presence Service checks the
                              		  following:

If there is a
                                    				user in the Cisco Unified Communications
                                       				  Manager database whose user ID is 'joe'. If this user ID does not
                                    				exist:

If there is a
                                    				user in the Cisco Unified Communications
                                       				  Manager database whose mail is 'joe@someCompany.com'. If this mail
                                    				does not exist:

If there is a
                                    				user in the Cisco Unified Communications
                                       				  Manager database whose ocsPrimaryAddress is
                                    				'sip:joe@someCompany.com'.

## Set Up Microsoft
                        	 Active Directory

### Before you begin

- Read the topic describing
                                 			 Line URI configuration on Microsoft Active
                                    				Directory .

- Read the topic describing the
                                 			 user authentication checks on IM and Presence Service .

Step 1

From the Microsoft
                                          				Active Directory application window, add a user name and the
                                       			 telephone number that are associated with each particular user.

Step 2

For each of the
                                       			 users that you added, open the Properties window on Microsoft Active Directory and
                                       			 configure the following parameters:

Enable the
                                             				  user for the Microsoft Lync Server.

Enter the
                                             				  SIP URI.

Enter the Microsoft Lync server name or pool.

Caution

Ensure the Microsoft Lync server name or pool name does not contain the underscore character.

Under
                                             				  Telephony Settings, select Configure .

Check Enable Remote call control .

Enter the
                                             				  Remote Call Control SIP URI; for example, sip:8000@my-cups.my-domain.com , where my-cups.my-domain.com specifies the FQDN of the IM and Presence Service node
                                             				  that you configured for this integration.

Enter the
                                             				  Line URI value.

Important

The SIP URI
                                                      				  that you enter on Microsoft Active Directory must match the static route URI
                                                      				  that you define when you are configuring static routes on Microsoft Lync .

### What to do next

Enable Users in Lync Server Control Panel

## Enable Users in Lync
                        	 Server Control Panel

The
                              		  following procedure describes how to enable new users in the Lync Server
                              		  Control Panel.

Step 1

Go to the
                                       			 Windows server that has Microsoft Lync Server installed.

Step 2

Select Start All
                                             				  Programs > Microsoft Lync Server > Lync Server Control
                                             				  Panel .

Step 3

Choose Enable
                                          				users for Lync Server from the Top
                                          				Actions menu.

Step 4

Select Add .

Step 5

Select the LDAP
                                          				search option and select Find .

Step 6

Click on the
                                       			 user to enable and select OK .

Step 7

Choose the
                                       			 application pool from the Assign
                                          				users to a pool drop-down list.

Step 8

Select the Specify a
                                          				SIP URI option and enter the SIP URI, for example, sip:UserA@lyncdomain.com , where UserA is the user you added and lyncdomain.com specifies the domain name of the Lync
                                       			 server.

Step 9

Choose Remote
                                          				call control from the Telephony drop-down list.

Step 10

Enter the Line
                                       			 URI in the format tel:<telephone_number>, where <telephone_number>
                                       			 is the telephone number you entered when adding the user.

Step 11

Enter the Line
                                       			 Server URI, for example, sip:UserA@my-cups.my-domain .com, where UserA is the user you added and my-cups.my-domain.com specifies the domain name of
                                       			 the IM and Presence Service node.

Please note the
                                          				following:

The Line
                                             				  Server URI domain is the value that is matched by the static route MatchUri
                                             				  parameter. See Set Up Static Route for Microsoft Lync Server .

The Line
                                             				  Server URI domain and the value in the MatchUri parameter must match to enable the Lync
                                             				  server to correctly route SIP messages to the IM and Presence Service node.

The IM and Presence Service node
                                             				  must also have this domain set as its proxy domain.

Step 12

Select Enable at the top of the window to enable the new
                                       			 user. The user should have a check mark in the Enabled column.

### What to do next

Microsoft Lync Server Setup Overview

## Microsoft Lync Server Setup Overview

This topic provides a brief description of the configuration required on Microsoft Lync Server for this integration. A comprehensive description of Microsoft Lync configuration is out of the scope of this document. For more information, see the Microsoft Lync documentation at the following URL: http://technet.microsoft.com/en-us/library/gg558664.aspx.

Make sure that the Microsoft Lync server is properly installed and activated. Make sure that the following items are configured on Microsoft Lync :

- Certificate configuration

- Static Routes

- Authorized Host

- Domain Name Server

- Pool Properties

- Server Properties

- Pool Users

- User Configuration

- Microsoft Lync Client Configuration

If the CTI Gateway is configured to use TCP, you must define the IP address of the Gateway in Lync Server Topology Builder.
                                          See the following URL for more information: http://technet.microsoft.com/en-us/library/gg602125.aspx.

You configure the Microsoft Lync Server  using the Lync Server Management Shell utility. The Management Shell utility is installed
                              by default with the Lync server installation. Set up the following items during Microsoft Lync server  configuration:

static routes

application pools

Remote Call Control (RCC) application

Lync server SIP listen port

After you set up the Microsoft Lync Server, commit the topology and restart the front-end service.

### Set Up Static Route
                           	 for Microsoft Lync Server

The Lync
                                 		  server uses the static route to match the URI of the incoming client's SIP
                                 		  message INVITE. The Lync server references the URI value as the Line Server
                                 		  URI.

Step 1

Select Start > All
                                                				  Programs > Microsoft Lync Server > Lync Server Management
                                                				  Shell .

Step 2

Enter the
                                          			 following command to verify the current system configuration:

Step 3

Enter the
                                          			 following command to create a static route:

Step 4

At the prompt,
                                          			 enter the following command to load the static route into the Lync server.

Step 5

Verify the new
                                          			 system configuration by entering the Get command from Step 2 again.

If you need to
                                                         				  modify or delete a static route, enter the following command:

Remove-CsStaticRoutingConfiguration –Identity Global

The following
                                             				table describes the parameters that you use to insert a new static route for
                                             				Lync server.

Parameter

Description

$tcpRoute

The name
                                                         						  of the variable. It can be named anything but it must begin with a $ and mach the reference in the Set command.

New-CsStaticRoute

The
                                                         						  internal command that populates the static route to a variable.

-TCPRoute

This
                                                         						  parameter configures the route as TCP.

-Destination

The IP
                                                         						  address of the IM and Presence Service node.

-Port

The port
                                                         						  to which the IM and Presence Service node listens. For
                                                         						  TCP, the port is 5060.

-MatchUri

This
                                                         						  value is compared to the Line Server URI value that is specified for each user
                                                         						  in the Lync Control Panel. See Enable Users in Lync Server Control Panel .

This
                                                         						  MatchURI value and the Line Server URI value must both match the IM and Presence Service node FQDN.

The
                                                         						  value of this parameter must be written in double quotes, for example,

-MatchUri
                                                            							 "my-cups.my-domain.com"

-ReplaceHostInRequestUri

This
                                                         						  parameter replaces the URI in the initial INVITE to the value that is
                                                         						  referenced in the Destination parameter.

-CsStaticRoutingConfiguration

The
                                                         						  internal command to move parameter values to the routing database.

-Route

This
                                                         						  parameter takes the parameters in the variable and adds the static route.

#### What to do next

Set Up Application Pool for Microsoft Lync Server

### Set Up Application
                           	 Pool for Microsoft Lync Server

The
                                 		  following procedure sets up an application pool that is referenced by the Lync
                                 		  server (registrar). It also links the site information to this pool.

Step 1

In the Lync
                                          			 Server Management Shell enter the following command to verify the current
                                          			 system configuration:

Step 2

Enter the
                                          			 following command to create the application pool:

Step 3

Select Y at the prompt.

Step 4

Verify the new
                                          			 system configuration by entering the Get command from Step 1 again.

Tip

If you need to
                                                         				  modify or delete the application pool, enter the following command:

Remove-CsTrustedApplicationPool -Identity
                                                            					 TrustedApplicationPool:<IP_address_CUPserver>

The following
                                             				table describes the parameters that you use to configure the application pool.

Parameter

Description

New-CsTrustedApplicationPool

The
                                                         						  internal command that adds the application pool.

-Identity

The
                                                         						  reference name of the pool which is also the IP address of the IM and Presence Service node.

The
                                                         						  value of this parameter must be written in double quotes, for example, -Identity "10.0.0.1"

This
                                                         						  value must match the value in the TrustedApplicationPoolFqdn parameter of the
                                                         						  TrustedApplication command in Set Up RCC Application for Microsoft Lync Server .

-Registrar

The FQDN
                                                         						  of the Lync server.

-Site

The
                                                         						  numeric value of the site.

Tip

You
                                                                     							 can find the site ID with the Get-CsSite Management Shell command.

-TreatAsAuthenticated

Always
                                                         						  set this value to $True

-ThrottleAsServer

Always
                                                         						  set this value to $True

-RequiresReplication

Because
                                                         						  authentication is not required for TCP, you must set this value to $False

#### What to do next

Set Up RCC Application for Microsoft Lync Server

### Set Up RCC
                           	 Application for Microsoft Lync Server

The
                                 		  following procedure adds the Microsoft Remote Call Control (RCC) application to the pool.

Step 1

In the Lync
                                          			 Server Management Shell enter the following command to verify the current
                                          			 system configuration:

Step 2

Enter the
                                          			 following command to add the RCC application to the pool:

Step 3

Select Y at the prompt.

Step 4

Verify the new
                                          			 system configuration by entering the Get command from Step 1 again.

Tip

If you need to
                                                         				  modify or delete the application pool, enter the following command:

Remove-CsTrustedApplicationPool -Identity
                                                            					 TrustedApplicationPool:<IP_address_CUPserver>

The following
                                             				table describes the parameters that you use to configure the application pool.

Parameter

Description

New-CsTrustedApplication

The
                                                         						  internal command that adds the RCC application.

-ApplicationID

The name
                                                         						  of the application, for example, RCC.

-TrustedApplicationPoolFQDN

The IP
                                                         						  address of the IM and Presence
                                                            							 Service node.

The
                                                         						  value of this parameter must be written in double quotes, for example, -Identity "10.0.0.1"

This
                                                         						  value must match the value in the Identity parameter of the
                                                         						  TrustedApplicationpool command in Set Up Application Pool for Microsoft Lync Server .

-Port

The SIP
                                                         						  TCP listening port of the IM and Presence
                                                            							 Service node. For TCP, the port is 5060.

-EnableTCP

This
                                                         						  parameter sets the transport to TCP. If this parameter is not included, the
                                                         						  transport will default to TLS.

See Security between IM and Presence Service and Microsoft Lync Setup for more information about
                                                                     							 Communication with Microsoft Lync server over TLS.

#### What to do next

Set Up Lync Server SIP Listen Port

### Set Up Lync Server
                           	 SIP Listen Port

The
                                 		  following procedure sets the SIP listen port on the Lync server. This is
                                 		  required for incoming SIP traffic from the IM and Presence Service node.

Step 1

In the Lync
                                          			 Server Management Shell enter the following command to verify the current
                                          			 system configuration:

Step 2

Enter the
                                          			 following command to set the Lync server listening port:

Step 3

Verify the new
                                          			 system configuration by entering the Get command from Step 1 again.

Tip

If you need to
                                                         				  modify or delete the application pool, enter the following command:

Remove-CsRegistrarConfiguration

The following
                                             				table describes the parameters that you use to configure the Lync server listen
                                             				port.

Parameter

Description

Set-CsRegistrar

Internal
                                                         						  command that sets the Lync server port.

registrar:

FQDN of
                                                         						  the Lync server.

-SipServerTcpPort

SIP
                                                         						  listening port of the Lync server. The default value is typically 5060.

#### What to do next

Commit Lync Server Setup

### Commit Lync Server
                           	 Setup

This
                                 		  procedure describes how to commit the topology and restart the front-end
                                 		  service.

Step 1

In the Lync
                                          			 Server Management Shell enter the following command to enable the topology:

Step 2

Enter the
                                          			 following command to output the topology to an XML file called rcc.xml and save
                                          			 it to the C drive:

You can select
                                                         				  any name and location to output the topology information.

Step 3

Open the rcc.xml
                                          			 file.

Step 4

In the Cluster
                                             				Fqdn section, change the IPAddress parameter from "<0.0.0.0>" to the IP Address of the IM and Presence Service node.

Step 5

Save the rcc.xml
                                          			 file.

Step 6

Enter the
                                          			 following command in the Lync Server Management Shell:

Step 7

Enter the
                                          			 following command to restart the front-end service:

#### What to do next

Normalization Rules Setup

| Note | If you are using
                                          			 E.164 numbers, do not include phone-context=dialstring because it will result in
                                          			 an error at the Microsoft Lync client. See Lync Error When Using E.164 Numbers . |
|---|---|

| Note | You can also use
                                          			 the E.164 format for the Line URI. However, you must ensure that the DNs are
                                          			 also configured with E.164 on Cisco Unified Communications
                                             				Manager . |
|---|---|

| Step 1 | From the Microsoft
                                          				Active Directory application window, add a user name and the
                                       			 telephone number that are associated with each particular user. |
|---|---|
| Step 2 | For each of the
                                       			 users that you added, open the Properties window on Microsoft Active Directory and
                                       			 configure the following parameters: Enable the
                                             				  user for the Microsoft Lync Server. Enter the
                                             				  SIP URI. Enter the Microsoft Lync server name or pool. Caution Ensure the Microsoft Lync server name or pool name does not contain the underscore character. Under
                                             				  Telephony Settings, select Configure . Check Enable Remote call control . Enter the
                                             				  Remote Call Control SIP URI; for example, sip:8000@my-cups.my-domain.com , where my-cups.my-domain.com specifies the FQDN of the IM and Presence Service node
                                             				  that you configured for this integration. Enter the
                                             				  Line URI value. Important The SIP URI
                                                      				  that you enter on Microsoft Active Directory must match the static route URI
                                                      				  that you define when you are configuring static routes on Microsoft Lync . | Caution | Ensure the Microsoft Lync server name or pool name does not contain the underscore character. | Important | The SIP URI
                                                      				  that you enter on Microsoft Active Directory must match the static route URI
                                                      				  that you define when you are configuring static routes on Microsoft Lync . |
| Caution | Ensure the Microsoft Lync server name or pool name does not contain the underscore character. |
| Important | The SIP URI
                                                      				  that you enter on Microsoft Active Directory must match the static route URI
                                                      				  that you define when you are configuring static routes on Microsoft Lync . |

| Caution | Ensure the Microsoft Lync server name or pool name does not contain the underscore character. |
|---|---|

| Important | The SIP URI
                                                      				  that you enter on Microsoft Active Directory must match the static route URI
                                                      				  that you define when you are configuring static routes on Microsoft Lync . |
|---|---|

| Step 1 | Go to the
                                       			 Windows server that has Microsoft Lync Server installed. |
|---|---|
| Step 2 | Select Start All
                                             				  Programs > Microsoft Lync Server > Lync Server Control
                                             				  Panel . |
| Step 3 | Choose Enable
                                          				users for Lync Server from the Top
                                          				Actions menu. |
| Step 4 | Select Add . |
| Step 5 | Select the LDAP
                                          				search option and select Find . |
| Step 6 | Click on the
                                       			 user to enable and select OK . |
| Step 7 | Choose the
                                       			 application pool from the Assign
                                          				users to a pool drop-down list. |
| Step 8 | Select the Specify a
                                          				SIP URI option and enter the SIP URI, for example, sip:UserA@lyncdomain.com , where UserA is the user you added and lyncdomain.com specifies the domain name of the Lync
                                       			 server. |
| Step 9 | Choose Remote
                                          				call control from the Telephony drop-down list. |
| Step 10 | Enter the Line
                                       			 URI in the format tel:<telephone_number>, where <telephone_number>
                                       			 is the telephone number you entered when adding the user. |
| Step 11 | Enter the Line
                                       			 Server URI, for example, sip:UserA@my-cups.my-domain .com, where UserA is the user you added and my-cups.my-domain.com specifies the domain name of
                                       			 the IM and Presence Service node. Please note the
                                          				following: The Line
                                             				  Server URI domain is the value that is matched by the static route MatchUri
                                             				  parameter. See Set Up Static Route for Microsoft Lync Server . The Line
                                             				  Server URI domain and the value in the MatchUri parameter must match to enable the Lync
                                             				  server to correctly route SIP messages to the IM and Presence Service node. The IM and Presence Service node
                                             				  must also have this domain set as its proxy domain. |
| Step 12 | Select Enable at the top of the window to enable the new
                                       			 user. The user should have a check mark in the Enabled column. |

| Note | This topic provides a brief description of the configuration required on Microsoft Lync Server for this integration. A comprehensive description of Microsoft Lync configuration is out of the scope of this document. For more information, see the Microsoft Lync documentation at the following URL: http://technet.microsoft.com/en-us/library/gg558664.aspx. |
|---|---|

| Note | If the CTI Gateway is configured to use TCP, you must define the IP address of the Gateway in Lync Server Topology Builder.
                                          See the following URL for more information: http://technet.microsoft.com/en-us/library/gg602125.aspx. |
|---|---|

| Step 1 | Select Start > All
                                                				  Programs > Microsoft Lync Server > Lync Server Management
                                                				  Shell . |
|---|---|
| Step 2 | Enter the
                                          			 following command to verify the current system configuration: Get-CsStaticRoutingConfiguration |
| Step 3 | Enter the
                                          			 following command to create a static route: $tcpRoute = New-CsStaticRoute
                                             				-TCPRoute -Destination <IP_address_CUPserver> -Port 5060 -MatchUri
                                             				"<Line_Server_URI_domain>" -ReplaceHostInRequestUri $true |
| Step 4 | At the prompt,
                                          			 enter the following command to load the static route into the Lync server. Set-CsStaticRoutingConfiguration -Route
                                             				@{Add=$tcpRoute} |
| Step 5 | Verify the new
                                          			 system configuration by entering the Get command from Step 2 again. Note If you need to
                                                         				  modify or delete a static route, enter the following command: Remove-CsStaticRoutingConfiguration –Identity Global The following
                                             				table describes the parameters that you use to insert a new static route for
                                             				Lync server. Table 1. Static route
                                                   				parameters Parameter Description $tcpRoute The name
                                                         						  of the variable. It can be named anything but it must begin with a $ and mach the reference in the Set command. New-CsStaticRoute The
                                                         						  internal command that populates the static route to a variable. -TCPRoute This
                                                         						  parameter configures the route as TCP. -Destination The IP
                                                         						  address of the IM and Presence Service node. -Port The port
                                                         						  to which the IM and Presence Service node listens. For
                                                         						  TCP, the port is 5060. -MatchUri This
                                                         						  value is compared to the Line Server URI value that is specified for each user
                                                         						  in the Lync Control Panel. See Enable Users in Lync Server Control Panel . This
                                                         						  MatchURI value and the Line Server URI value must both match the IM and Presence Service node FQDN. The
                                                         						  value of this parameter must be written in double quotes, for example, -MatchUri
                                                            							 "my-cups.my-domain.com" -ReplaceHostInRequestUri This
                                                         						  parameter replaces the URI in the initial INVITE to the value that is
                                                         						  referenced in the Destination parameter. -CsStaticRoutingConfiguration The
                                                         						  internal command to move parameter values to the routing database. -Route This
                                                         						  parameter takes the parameters in the variable and adds the static route. | Note | If you need to
                                                         				  modify or delete a static route, enter the following command: Remove-CsStaticRoutingConfiguration –Identity Global | Parameter | Description | $tcpRoute | The name
                                                         						  of the variable. It can be named anything but it must begin with a $ and mach the reference in the Set command. | New-CsStaticRoute | The
                                                         						  internal command that populates the static route to a variable. | -TCPRoute | This
                                                         						  parameter configures the route as TCP. | -Destination | The IP
                                                         						  address of the IM and Presence Service node. | -Port | The port
                                                         						  to which the IM and Presence Service node listens. For
                                                         						  TCP, the port is 5060. | -MatchUri | This
                                                         						  value is compared to the Line Server URI value that is specified for each user
                                                         						  in the Lync Control Panel. See Enable Users in Lync Server Control Panel . This
                                                         						  MatchURI value and the Line Server URI value must both match the IM and Presence Service node FQDN. The
                                                         						  value of this parameter must be written in double quotes, for example, -MatchUri
                                                            							 "my-cups.my-domain.com" | -ReplaceHostInRequestUri | This
                                                         						  parameter replaces the URI in the initial INVITE to the value that is
                                                         						  referenced in the Destination parameter. | -CsStaticRoutingConfiguration | The
                                                         						  internal command to move parameter values to the routing database. | -Route | This
                                                         						  parameter takes the parameters in the variable and adds the static route. |
| Note | If you need to
                                                         				  modify or delete a static route, enter the following command: Remove-CsStaticRoutingConfiguration –Identity Global |
| Parameter | Description |
| $tcpRoute | The name
                                                         						  of the variable. It can be named anything but it must begin with a $ and mach the reference in the Set command. |
| New-CsStaticRoute | The
                                                         						  internal command that populates the static route to a variable. |
| -TCPRoute | This
                                                         						  parameter configures the route as TCP. |
| -Destination | The IP
                                                         						  address of the IM and Presence Service node. |
| -Port | The port
                                                         						  to which the IM and Presence Service node listens. For
                                                         						  TCP, the port is 5060. |
| -MatchUri | This
                                                         						  value is compared to the Line Server URI value that is specified for each user
                                                         						  in the Lync Control Panel. See Enable Users in Lync Server Control Panel . This
                                                         						  MatchURI value and the Line Server URI value must both match the IM and Presence Service node FQDN. The
                                                         						  value of this parameter must be written in double quotes, for example, -MatchUri
                                                            							 "my-cups.my-domain.com" |
| -ReplaceHostInRequestUri | This
                                                         						  parameter replaces the URI in the initial INVITE to the value that is
                                                         						  referenced in the Destination parameter. |
| -CsStaticRoutingConfiguration | The
                                                         						  internal command to move parameter values to the routing database. |
| -Route | This
                                                         						  parameter takes the parameters in the variable and adds the static route. |

| Note | If you need to
                                                         				  modify or delete a static route, enter the following command: Remove-CsStaticRoutingConfiguration –Identity Global |
|---|---|

| Parameter | Description |
|---|---|
| $tcpRoute | The name
                                                         						  of the variable. It can be named anything but it must begin with a $ and mach the reference in the Set command. |
| New-CsStaticRoute | The
                                                         						  internal command that populates the static route to a variable. |
| -TCPRoute | This
                                                         						  parameter configures the route as TCP. |
| -Destination | The IP
                                                         						  address of the IM and Presence Service node. |
| -Port | The port
                                                         						  to which the IM and Presence Service node listens. For
                                                         						  TCP, the port is 5060. |
| -MatchUri | This
                                                         						  value is compared to the Line Server URI value that is specified for each user
                                                         						  in the Lync Control Panel. See Enable Users in Lync Server Control Panel . This
                                                         						  MatchURI value and the Line Server URI value must both match the IM and Presence Service node FQDN. The
                                                         						  value of this parameter must be written in double quotes, for example, -MatchUri
                                                            							 "my-cups.my-domain.com" |
| -ReplaceHostInRequestUri | This
                                                         						  parameter replaces the URI in the initial INVITE to the value that is
                                                         						  referenced in the Destination parameter. |
| -CsStaticRoutingConfiguration | The
                                                         						  internal command to move parameter values to the routing database. |
| -Route | This
                                                         						  parameter takes the parameters in the variable and adds the static route. |

| Step 1 | In the Lync
                                          			 Server Management Shell enter the following command to verify the current
                                          			 system configuration: Get-CSTrustedApplicationPool |
|---|---|
| Step 2 | Enter the
                                          			 following command to create the application pool: New-CsTrustedApplicationpool
                                             				-Identity "<IP_address_CUPserver>" -Registrar <Lync_server_FQDN>
                                             				–Site 1 –TreatAsAuthenticated $True –ThrottleAsServer $True
                                             				–RequiresReplication $False |
| Step 3 | Select Y at the prompt. |
| Step 4 | Verify the new
                                          			 system configuration by entering the Get command from Step 1 again. Tip If you need to
                                                         				  modify or delete the application pool, enter the following command: Remove-CsTrustedApplicationPool -Identity
                                                            					 TrustedApplicationPool:<IP_address_CUPserver> The following
                                             				table describes the parameters that you use to configure the application pool. Table 2. Application
                                                   				pool parameters Parameter Description New-CsTrustedApplicationPool The
                                                         						  internal command that adds the application pool. -Identity The
                                                         						  reference name of the pool which is also the IP address of the IM and Presence Service node. The
                                                         						  value of this parameter must be written in double quotes, for example, -Identity "10.0.0.1" This
                                                         						  value must match the value in the TrustedApplicationPoolFqdn parameter of the
                                                         						  TrustedApplication command in Set Up RCC Application for Microsoft Lync Server . -Registrar The FQDN
                                                         						  of the Lync server. -Site The
                                                         						  numeric value of the site. Tip You
                                                                     							 can find the site ID with the Get-CsSite Management Shell command. -TreatAsAuthenticated Always
                                                         						  set this value to $True -ThrottleAsServer Always
                                                         						  set this value to $True -RequiresReplication Because
                                                         						  authentication is not required for TCP, you must set this value to $False | Tip | If you need to
                                                         				  modify or delete the application pool, enter the following command: Remove-CsTrustedApplicationPool -Identity
                                                            					 TrustedApplicationPool:<IP_address_CUPserver> | Parameter | Description | New-CsTrustedApplicationPool | The
                                                         						  internal command that adds the application pool. | -Identity | The
                                                         						  reference name of the pool which is also the IP address of the IM and Presence Service node. The
                                                         						  value of this parameter must be written in double quotes, for example, -Identity "10.0.0.1" This
                                                         						  value must match the value in the TrustedApplicationPoolFqdn parameter of the
                                                         						  TrustedApplication command in Set Up RCC Application for Microsoft Lync Server . | -Registrar | The FQDN
                                                         						  of the Lync server. | -Site | The
                                                         						  numeric value of the site. Tip You
                                                                     							 can find the site ID with the Get-CsSite Management Shell command. | Tip | You
                                                                     							 can find the site ID with the Get-CsSite Management Shell command. | -TreatAsAuthenticated | Always
                                                         						  set this value to $True | -ThrottleAsServer | Always
                                                         						  set this value to $True | -RequiresReplication | Because
                                                         						  authentication is not required for TCP, you must set this value to $False |
| Tip | If you need to
                                                         				  modify or delete the application pool, enter the following command: Remove-CsTrustedApplicationPool -Identity
                                                            					 TrustedApplicationPool:<IP_address_CUPserver> |
| Parameter | Description |
| New-CsTrustedApplicationPool | The
                                                         						  internal command that adds the application pool. |
| -Identity | The
                                                         						  reference name of the pool which is also the IP address of the IM and Presence Service node. The
                                                         						  value of this parameter must be written in double quotes, for example, -Identity "10.0.0.1" This
                                                         						  value must match the value in the TrustedApplicationPoolFqdn parameter of the
                                                         						  TrustedApplication command in Set Up RCC Application for Microsoft Lync Server . |
| -Registrar | The FQDN
                                                         						  of the Lync server. |
| -Site | The
                                                         						  numeric value of the site. Tip You
                                                                     							 can find the site ID with the Get-CsSite Management Shell command. | Tip | You
                                                                     							 can find the site ID with the Get-CsSite Management Shell command. |
| Tip | You
                                                                     							 can find the site ID with the Get-CsSite Management Shell command. |
| -TreatAsAuthenticated | Always
                                                         						  set this value to $True |
| -ThrottleAsServer | Always
                                                         						  set this value to $True |
| -RequiresReplication | Because
                                                         						  authentication is not required for TCP, you must set this value to $False |

| Tip | If you need to
                                                         				  modify or delete the application pool, enter the following command: Remove-CsTrustedApplicationPool -Identity
                                                            					 TrustedApplicationPool:<IP_address_CUPserver> |
|---|---|

| Parameter | Description |
|---|---|
| New-CsTrustedApplicationPool | The
                                                         						  internal command that adds the application pool. |
| -Identity | The
                                                         						  reference name of the pool which is also the IP address of the IM and Presence Service node. The
                                                         						  value of this parameter must be written in double quotes, for example, -Identity "10.0.0.1" This
                                                         						  value must match the value in the TrustedApplicationPoolFqdn parameter of the
                                                         						  TrustedApplication command in Set Up RCC Application for Microsoft Lync Server . |
| -Registrar | The FQDN
                                                         						  of the Lync server. |
| -Site | The
                                                         						  numeric value of the site. Tip You
                                                                     							 can find the site ID with the Get-CsSite Management Shell command. | Tip | You
                                                                     							 can find the site ID with the Get-CsSite Management Shell command. |
| Tip | You
                                                                     							 can find the site ID with the Get-CsSite Management Shell command. |
| -TreatAsAuthenticated | Always
                                                         						  set this value to $True |
| -ThrottleAsServer | Always
                                                         						  set this value to $True |
| -RequiresReplication | Because
                                                         						  authentication is not required for TCP, you must set this value to $False |

| Tip | You
                                                                     							 can find the site ID with the Get-CsSite Management Shell command. |
|---|---|

| Step 1 | In the Lync
                                          			 Server Management Shell enter the following command to verify the current
                                          			 system configuration: Get-CSTrustedApplication |
|---|---|
| Step 2 | Enter the
                                          			 following command to add the RCC application to the pool: New-CsTrustedApplication
                                             				-ApplicationID RCC -TrustedApplicationPoolFqdn "<IP_address_CUPserver>"
                                             				-Port 5060 -EnableTcp |
| Step 3 | Select Y at the prompt. |
| Step 4 | Verify the new
                                          			 system configuration by entering the Get command from Step 1 again. Tip If you need to
                                                         				  modify or delete the application pool, enter the following command: Remove-CsTrustedApplicationPool -Identity
                                                            					 TrustedApplicationPool:<IP_address_CUPserver> The following
                                             				table describes the parameters that you use to configure the application pool. Table 3. Application
                                                   				configuration parameters Parameter Description New-CsTrustedApplication The
                                                         						  internal command that adds the RCC application. -ApplicationID The name
                                                         						  of the application, for example, RCC. -TrustedApplicationPoolFQDN The IP
                                                         						  address of the IM and Presence
                                                            							 Service node. The
                                                         						  value of this parameter must be written in double quotes, for example, -Identity "10.0.0.1" This
                                                         						  value must match the value in the Identity parameter of the
                                                         						  TrustedApplicationpool command in Set Up Application Pool for Microsoft Lync Server . -Port The SIP
                                                         						  TCP listening port of the IM and Presence
                                                            							 Service node. For TCP, the port is 5060. -EnableTCP This
                                                         						  parameter sets the transport to TCP. If this parameter is not included, the
                                                         						  transport will default to TLS. Note See Security between IM and Presence Service and Microsoft Lync Setup for more information about
                                                                     							 Communication with Microsoft Lync server over TLS. | Tip | If you need to
                                                         				  modify or delete the application pool, enter the following command: Remove-CsTrustedApplicationPool -Identity
                                                            					 TrustedApplicationPool:<IP_address_CUPserver> | Parameter | Description | New-CsTrustedApplication | The
                                                         						  internal command that adds the RCC application. | -ApplicationID | The name
                                                         						  of the application, for example, RCC. | -TrustedApplicationPoolFQDN | The IP
                                                         						  address of the IM and Presence
                                                            							 Service node. The
                                                         						  value of this parameter must be written in double quotes, for example, -Identity "10.0.0.1" This
                                                         						  value must match the value in the Identity parameter of the
                                                         						  TrustedApplicationpool command in Set Up Application Pool for Microsoft Lync Server . | -Port | The SIP
                                                         						  TCP listening port of the IM and Presence
                                                            							 Service node. For TCP, the port is 5060. | -EnableTCP | This
                                                         						  parameter sets the transport to TCP. If this parameter is not included, the
                                                         						  transport will default to TLS. Note See Security between IM and Presence Service and Microsoft Lync Setup for more information about
                                                                     							 Communication with Microsoft Lync server over TLS. | Note | See Security between IM and Presence Service and Microsoft Lync Setup for more information about
                                                                     							 Communication with Microsoft Lync server over TLS. |
| Tip | If you need to
                                                         				  modify or delete the application pool, enter the following command: Remove-CsTrustedApplicationPool -Identity
                                                            					 TrustedApplicationPool:<IP_address_CUPserver> |
| Parameter | Description |
| New-CsTrustedApplication | The
                                                         						  internal command that adds the RCC application. |
| -ApplicationID | The name
                                                         						  of the application, for example, RCC. |
| -TrustedApplicationPoolFQDN | The IP
                                                         						  address of the IM and Presence
                                                            							 Service node. The
                                                         						  value of this parameter must be written in double quotes, for example, -Identity "10.0.0.1" This
                                                         						  value must match the value in the Identity parameter of the
                                                         						  TrustedApplicationpool command in Set Up Application Pool for Microsoft Lync Server . |
| -Port | The SIP
                                                         						  TCP listening port of the IM and Presence
                                                            							 Service node. For TCP, the port is 5060. |
| -EnableTCP | This
                                                         						  parameter sets the transport to TCP. If this parameter is not included, the
                                                         						  transport will default to TLS. Note See Security between IM and Presence Service and Microsoft Lync Setup for more information about
                                                                     							 Communication with Microsoft Lync server over TLS. | Note | See Security between IM and Presence Service and Microsoft Lync Setup for more information about
                                                                     							 Communication with Microsoft Lync server over TLS. |
| Note | See Security between IM and Presence Service and Microsoft Lync Setup for more information about
                                                                     							 Communication with Microsoft Lync server over TLS. |

| Tip | If you need to
                                                         				  modify or delete the application pool, enter the following command: Remove-CsTrustedApplicationPool -Identity
                                                            					 TrustedApplicationPool:<IP_address_CUPserver> |
|---|---|

| Parameter | Description |
|---|---|
| New-CsTrustedApplication | The
                                                         						  internal command that adds the RCC application. |
| -ApplicationID | The name
                                                         						  of the application, for example, RCC. |
| -TrustedApplicationPoolFQDN | The IP
                                                         						  address of the IM and Presence
                                                            							 Service node. The
                                                         						  value of this parameter must be written in double quotes, for example, -Identity "10.0.0.1" This
                                                         						  value must match the value in the Identity parameter of the
                                                         						  TrustedApplicationpool command in Set Up Application Pool for Microsoft Lync Server . |
| -Port | The SIP
                                                         						  TCP listening port of the IM and Presence
                                                            							 Service node. For TCP, the port is 5060. |
| -EnableTCP | This
                                                         						  parameter sets the transport to TCP. If this parameter is not included, the
                                                         						  transport will default to TLS. Note See Security between IM and Presence Service and Microsoft Lync Setup for more information about
                                                                     							 Communication with Microsoft Lync server over TLS. | Note | See Security between IM and Presence Service and Microsoft Lync Setup for more information about
                                                                     							 Communication with Microsoft Lync server over TLS. |
| Note | See Security between IM and Presence Service and Microsoft Lync Setup for more information about
                                                                     							 Communication with Microsoft Lync server over TLS. |

| Note | See Security between IM and Presence Service and Microsoft Lync Setup for more information about
                                                                     							 Communication with Microsoft Lync server over TLS. |
|---|---|

| Step 1 | In the Lync
                                          			 Server Management Shell enter the following command to verify the current
                                          			 system configuration: Get-CSRegistrarConfiguration |
|---|---|
| Step 2 | Enter the
                                          			 following command to set the Lync server listening port: Set-CsRegistrar
                                             				registrar:<Lync_server_FQDN> -SipServerTcpPort 5060 |
| Step 3 | Verify the new
                                          			 system configuration by entering the Get command from Step 1 again. Tip If you need to
                                                         				  modify or delete the application pool, enter the following command: Remove-CsRegistrarConfiguration The following
                                             				table describes the parameters that you use to configure the Lync server listen
                                             				port. Table 4. Lync server
                                                   				listen port parameters Parameter Description Set-CsRegistrar Internal
                                                         						  command that sets the Lync server port. registrar: FQDN of
                                                         						  the Lync server. -SipServerTcpPort SIP
                                                         						  listening port of the Lync server. The default value is typically 5060. | Tip | If you need to
                                                         				  modify or delete the application pool, enter the following command: Remove-CsRegistrarConfiguration | Parameter | Description | Set-CsRegistrar | Internal
                                                         						  command that sets the Lync server port. | registrar: | FQDN of
                                                         						  the Lync server. | -SipServerTcpPort | SIP
                                                         						  listening port of the Lync server. The default value is typically 5060. |
| Tip | If you need to
                                                         				  modify or delete the application pool, enter the following command: Remove-CsRegistrarConfiguration |
| Parameter | Description |
| Set-CsRegistrar | Internal
                                                         						  command that sets the Lync server port. |
| registrar: | FQDN of
                                                         						  the Lync server. |
| -SipServerTcpPort | SIP
                                                         						  listening port of the Lync server. The default value is typically 5060. |

| Tip | If you need to
                                                         				  modify or delete the application pool, enter the following command: Remove-CsRegistrarConfiguration |
|---|---|

| Parameter | Description |
|---|---|
| Set-CsRegistrar | Internal
                                                         						  command that sets the Lync server port. |
| registrar: | FQDN of
                                                         						  the Lync server. |
| -SipServerTcpPort | SIP
                                                         						  listening port of the Lync server. The default value is typically 5060. |

| Step 1 | In the Lync
                                          			 Server Management Shell enter the following command to enable the topology: Enable-CsTopology |
|---|---|
| Step 2 | Enter the
                                          			 following command to output the topology to an XML file called rcc.xml and save
                                          			 it to the C drive: Get-CsTopology -AsXml \|
                                             				Out-File C:\rcc.xml Note You can select
                                                         				  any name and location to output the topology information. | Note | You can select
                                                         				  any name and location to output the topology information. |
| Note | You can select
                                                         				  any name and location to output the topology information. |
| Step 3 | Open the rcc.xml
                                          			 file. |
| Step 4 | In the Cluster
                                             				Fqdn section, change the IPAddress parameter from "<0.0.0.0>" to the IP Address of the IM and Presence Service node. |
| Step 5 | Save the rcc.xml
                                          			 file. |
| Step 6 | Enter the
                                          			 following command in the Lync Server Management Shell: Publish-CsTopology -FileName
                                             				C:\rcc.xml |
| Step 7 | Enter the
                                          			 following command to restart the front-end service: Restart-Service
                                             				RtcSrv |

| Note | You can select
                                                         				  any name and location to output the topology information. |
|---|---|