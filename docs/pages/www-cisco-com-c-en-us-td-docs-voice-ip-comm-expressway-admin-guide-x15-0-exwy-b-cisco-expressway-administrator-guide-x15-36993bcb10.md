---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-admin-guide-x15-0-exwy-b-cisco-expressway-administrator-guide-x15-36993bcb10
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X15-0/exwy_b_cisco-expressway-administrator-guide-x15/exwy_m_expressway-interfaces.html
retrieved_at: 2026-08-16T22:31:41.186312+00:00
---

Cisco Expressway Administrator Guide (X15.0)

# Cisco Expressway Administrator Guide (X15.0)

Updated: December 19, 2023

Chapter: Expressway Interfaces

## Chapter: Expressway Interfaces

# Expressway Interfaces

## About the Web Interface

This section summarizes the Expressway web user interface, and the CLI and API.

System configuration is normally carried out through the web interface. To use the web interface:

Open a browser window and in the address bar type the IP address or the FQDN of the system.

Enter a valid administrator Username and Password and click Login (see the user accounts section for details on setting up administrator accounts). The Overview page is displayed.

If you receive a warning message regarding Expressway's security certificate, you can ignore this until you are ready to secure
                           the system.

Field Markers

A red star indicates a mandatory field

An orange symbol indicates a field that must be configured on each peer in the cluster

Supported Browsers

The Expressway web interface is designed for and tested with Microsoft Edge, Firefox, and Chrome. We do not officially support
                           using other browsers for accessing the User Interface.

JavaScript and cookies must be enabled to use the Expressway web interface.

HTTP Methods

The Expressway web server allows the following HTTP methods:

Method

Used by Web UI?

Used by API?

Used to...

GET

Yes

Yes

Retrieve data from a specified resource. For example, to return a specific page in the Expressway web interface.

POST

Yes

Yes

Apply data to a web resource. For example, when an administrator saves changes to a setting using the Expressway web interface.

OPTIONS

No

Yes

For a specified URL, returns the HTTP methods supported by the server. For example, the Expressway can use OPTIONS to test
                                       a proxy server for HTTP/1.1 compliance.

PUT

No

Yes

Send a resource to be stored at a specified URI. Our REST API commands use this method to change the Expressway configuration.

DELETE

No

Yes

Delete a specified resource. For example, the REST API uses DELETE for record deletion.

How to disable user access to the API

Administrators have API access by default. This can be disabled in two ways:

If the Expressway is running in advanced account security mode, then API access is automatically disabled for all users.

API access for individual administrators can be disabled through their user configuration options.

## Web Page Features and Layout

This section describes the available features on Expressway web interface pages.

The elements included in the example web pages shown here are described in the table below.

Page element

Description

Page name and location

Every page shows the page name and the menu path to that page. Each part of the menu path is a link; clicking on any of the
                                          higher level menu items takes you to that page.

System alarm

This icon appears on the top right corner of every page when there is a system alarm in place. Click on this icon to go to
                                          the Alarms page which gives information about the alarm and its suggested resolution.

Help

This icon appears on the top right corner of every page. Clicking on this icon opens a new browser window with help specific
                                          to the page you are viewing. It gives an overview of the purpose of the page, and introduces any concepts configured from
                                          the page.

Log out

This icon appears on the top right corner of every page. Clicking on this icon ends your administrator session.

Field level information

An information box appears on the configuration pages whenever you either click on the Information icon or click inside a
                                          field. This box gives you information about the particular field, including where applicable the valid ranges and default
                                          value. To close the information box, click on the X at its top right corner.

Information bar

The Expressway provides you with feedback in certain situations, for example when settings have been saved or when you need
                                          to take further action. This feedback is given in a yellow information bar at the top of the page.

Sorting columns

Click on column headings to sort the information in ascending and descending order.

Select All and Unselect All

Use these buttons to select and unselect all items in the list.

Mandatory field

Indicates an input field that must be completed.

Peer-specific configuration item

When an Expressway is part of a cluster, most items of configuration are applied to all peers in a cluster. However, items
                                          indicated with a must be specified separately on each cluster peer.

System Information

The name of the user currently logged in and their access privileges, the system name (or LAN 1 IPv4 address if no system
                                          name is configured), local system time, currently selected language, serial number and Expressway software version are shown
                                          at the bottom of the page.

You cannot change configuration settings if your administrator account has read-only privileges.

### Missing Application Menu in Web User Interface

When Expressway is installed, the menus that appear in the web user interface are tailored to match the service selections
                                 chosen in the Service Setup Wizard. In some cases, depending on the combination of services selected, the Applications menu may be missing from the interface. If this happens and you want to restore the menu, do the following:

Go to Status > Overview and click Run service setup , to go back to the service setup options.

Check the option Proceed without selecting services and click Continue .

## About the Command Line Interface

The Command Line Interface (CLI) is available by default over SSH, and through the serial port on appliance-based systems.
                           These settings are controlled on the System administration page.

### To Use the CLI

Start an SSH session.

Enter the IP address or FQDN of the Expressway.

Log in as Admin (Enter username and password as Admin ).

See Enabling SSH Access to Expressway if you prefer to use your private key to authenticate.

You can now start using the CLI by typing the appropriate commands.

Use the admin and root accounts for SSH access. Other local or remote accounts are restricted from CLI access through SSH.

### Command Types

Commands are categorized into the following groups:

xStatus return information about the current status of the system. Information such as current calls and registrations is available
                                       through this command group. See Command Reference — xStatus for a full list of xStatus commands.

xConfiguration allow you to add and edit single items of data such as IP address and zones. See Command Reference — xConfiguration for a full list of xConfiguration commands.

xCommand these commands allow you to add and configure items and obtain information. See Command Reference — xCommand for a full list of xCommand commands.

xHistory provide historical information about calls and registrations.

xFeedback provide information about events as they happen, such as calls and registrations.

#### Useful Controls

Typing an xConfiguration path into the CLI returns a list of values currently configured for that element (and sub-elements where applicable).

Typing an xConfiguration path into the CLI followed by a ? returns information about the usage for that element and sub-elements.

Typing an xCommand command into the CLI with or without a ? returns information about the usage of that command.

## About the API

Administrators have access to the Expressway REST API by default, unless the Expressway is in advanced account security mode
                           or if individual access is disabled through the administrator's user configuration options.

The API is self documented using RESTful API Modeling Language (RAML). We provide a REST API Summary Guide on the "Expressway Configuration Guides" page, which summarizes how to access the base URL and the RAML definitions, and gives some example requests and responses.

Cross Site Request Forgery Protection Header

Cross-Site Request Forgery (CSRF) is an attack that forces authenticated users to submit a request to a Web application against
                           which they are currently authenticated. CSRF attacks exploit the trust a Web application has in an authenticated user.

A new header has been included to prevent such attacks and must now be sent with XML Put, SOAP, and CDB Rest API requests
                           whenever CSRF Protection is enabled . For the commands to enable or disable CSRF Header: X-CSRF-Header, see the chapter " Reference Material - xConfiguration Commands ."

All scripts/code calling CDB Rest, SOAP, or XMLPut APIs must send 'X-CSRF-Header' as part of their request headers once CSRF
                                       is enabled.

From the X14.2 release, if you are using any of these RAML APIs, you must add a custom header called X-CSRF-Header when making
                           the POST Request. The Header value is not important.

/api/provisioning/restart

/api/provisioning/common/defaultlinks

/api/provisioning/controller/b2bua/microsoftinterop/restartservice

/api/provisioning/domaincerts/domain/<domain>

/api/provisioning/certs/acme/pendingcert

/api/provisioning/certs/acme/pendingcert/deploy

/api/provisioning/domaincerts/domain/<domain>/acme/pendingcert/deploy

From the X15.0 release, the CSRF Protection Header is introduces for CDB, XMLPut, and SOAP APIs.

Disabling or Enabling the Cross-Site Request Forgery Protection : CSRF Protection is Disabled by default. You can execute the following commands to enable or disable the custom header.

xConfiguration Security CSRFProtection Status: "Disabled"

For more information, see link .

xConfiguration Security CSRFProtection Status: "Enabled"

For more information, see link .

You need not add any changes to the scripts while using any RAML API other than the above.

## Software Versions Supported by Hardware Platforms

Platform name

Serial Numbers

Scope of software version support

Small VM (OVA)

(Auto-generated)

X8.1 onwards

Medium VM (OVA)

(Auto-generated)

X8.1 onwards

Large VM (OVA)

(Auto-generated)

X8.1 onwards

CE1300 Hardware

52E5####

X14.3.1 onwards

CE1200 Hardware Revision 2 (preinstalled on UCS C220 M5L)

52E1####

X12.5.5 onwards

CE1200 Hardware Revision 1 (preinstalled on UCS C220 M5L)

52E0####

X8.11.1 onwards

CE1100 (Expressway pre-installed on UCS C220 M4L)

52D#####

Not supported (after X12.5.x) except limited support with X12.6.x versions for maintenance and bug fixing purposes only

CE1000 (Expressway pre-installed on UCS C220 M3L)

52B#####

Not supported (after X8.10.x). Refer Notes.

CE500 (Expressway pre-installed on UCS C220 M3L)

52C#####

Not supported (after X8.10.x). Refer Notes.

This is applicable for appliances that have reached the end-of-life and end-of-support. For Hardware that is past the Last Day of Support : There is no support for Hardware issues or Software issues (which includes the Hardware embedded Software like BIOS, firmware,
                                          and drivers).

| Method | Used by Web UI? | Used by API? | Used to... |
|---|---|---|---|
| GET | Yes | Yes | Retrieve data from a specified resource. For example, to return a specific page in the Expressway web interface. |
| POST | Yes | Yes | Apply data to a web resource. For example, when an administrator saves changes to a setting using the Expressway web interface. |
| OPTIONS | No | Yes | For a specified URL, returns the HTTP methods supported by the server. For example, the Expressway can use OPTIONS to test
                                       a proxy server for HTTP/1.1 compliance. |
| PUT | No | Yes | Send a resource to be stored at a specified URI. Our REST API commands use this method to change the Expressway configuration. |
| DELETE | No | Yes | Delete a specified resource. For example, the REST API uses DELETE for record deletion. |

| Page element |  | Description |
|---|---|---|
| Page name and location |  | Every page shows the page name and the menu path to that page. Each part of the menu path is a link; clicking on any of the
                                          higher level menu items takes you to that page. |
| System alarm |  | This icon appears on the top right corner of every page when there is a system alarm in place. Click on this icon to go to
                                          the Alarms page which gives information about the alarm and its suggested resolution. |
| Help |  | This icon appears on the top right corner of every page. Clicking on this icon opens a new browser window with help specific
                                          to the page you are viewing. It gives an overview of the purpose of the page, and introduces any concepts configured from
                                          the page. |
| Log out |  | This icon appears on the top right corner of every page. Clicking on this icon ends your administrator session. |
| Field level information |  | An information box appears on the configuration pages whenever you either click on the Information icon or click inside a
                                          field. This box gives you information about the particular field, including where applicable the valid ranges and default
                                          value. To close the information box, click on the X at its top right corner. |
| Information bar |  | The Expressway provides you with feedback in certain situations, for example when settings have been saved or when you need
                                          to take further action. This feedback is given in a yellow information bar at the top of the page. |
| Sorting columns |  | Click on column headings to sort the information in ascending and descending order. |
| Select All and Unselect All |  | Use these buttons to select and unselect all items in the list. |
| Mandatory field |  | Indicates an input field that must be completed. |
| Peer-specific configuration item |  | When an Expressway is part of a cluster, most items of configuration are applied to all peers in a cluster. However, items
                                          indicated with a must be specified separately on each cluster peer. |
| System Information |  | The name of the user currently logged in and their access privileges, the system name (or LAN 1 IPv4 address if no system
                                          name is configured), local system time, currently selected language, serial number and Expressway software version are shown
                                          at the bottom of the page. |

| Note | You cannot change configuration settings if your administrator account has read-only privileges. |
|---|---|

| Note | Use the admin and root accounts for SSH access. Other local or remote accounts are restricted from CLI access through SSH. |
|---|---|

| Note | All scripts/code calling CDB Rest, SOAP, or XMLPut APIs must send 'X-CSRF-Header' as part of their request headers once CSRF
                                       is enabled. |
|---|---|

| Note | You need not add any changes to the scripts while using any RAML API other than the above. |
|---|---|

| Platform name | Serial Numbers | Scope of software version support |
|---|---|---|
| Small VM (OVA) | (Auto-generated) | X8.1 onwards |
| Medium VM (OVA) | (Auto-generated) | X8.1 onwards |
| Large VM (OVA) | (Auto-generated) | X8.1 onwards |
| CE1300 Hardware (Expressway pre-installed on UCS C220 M6S) | 52E5#### | X14.3.1 onwards |
| CE1200 Hardware Revision 2 (preinstalled on UCS C220 M5L) | 52E1#### | X12.5.5 onwards |
| CE1200 Hardware Revision 1 (preinstalled on UCS C220 M5L) | 52E0#### | X8.11.1 onwards |
| CE1100 (Expressway pre-installed on UCS C220 M4L) | 52D##### | Not supported (after X12.5.x) except limited support with X12.6.x versions for maintenance and bug fixing purposes only |
| CE1000 (Expressway pre-installed on UCS C220 M3L) | 52B##### | Not supported (after X8.10.x). Refer Notes. |
| CE500 (Expressway pre-installed on UCS C220 M3L) | 52C##### | Not supported (after X8.10.x). Refer Notes. |

| Note | This is applicable for appliances that have reached the end-of-life and end-of-support. For Hardware that is past the Last Day of Support : There is no support for Hardware issues or Software issues (which includes the Hardware embedded Software like BIOS, firmware,
                                          and drivers). |
|---|---|