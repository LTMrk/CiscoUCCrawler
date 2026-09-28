---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-14su1-cucm-b-bulk-administration-guide-14su1-cucm-b-bulk-administra-2ff54a1c8c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/14SU1/cucm_b_bulk-administration-guide-14SU1/cucm_b_bulk-administration-guide-1251su2_chapter_0110000.html
retrieved_at: 2026-08-21T09:11:12.281525+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: October 27, 2021

Chapter: Gateway Templates

## Chapter: Gateway Templates

# Gateway Templates

This chapter provides information to add and update existing
                           		  Cisco gateways and ports in the Cisco Unified Communications Manager database using Cisco Unified Communications Manager Bulk Administration (BAT).

## Cisco Gateway Additions

You can use BAT to add Cisco gateways to the Cisco Unified Communications Manager database in bulk.

### Add Cisco VG200 Gateways Using BAT

Foreign Exchange Station (FXS) ports for analog devices

Foreign Exchange Office (FXO) for loopstart or groundstart trunks

T1 Primary Rate Interface (PRI) trunks for ISDN services in North America—Currently available only for Cisco VG200 gateways

E1 Primary Rate Interface (PRI) trunks for ISDN services in Europe—Currently available only for Cisco VG200 gateways.

Digital Access T1 protocol trunks

#### Before you begin

Before adding the VG200 gateways to the Cisco Unified Communications Manager database, you must first configure the gateway by using the Cisco IOS software command line interface (CLI). For gateway
                                 configuration procedures and commands, refer to the configuration documentation that is supplied with the gateway.

Step 1

Create a Cisco VG200 gateway template to define common values for a set of gateways and ports. See the Create Cisco VG200 Gateway Template .

Step 2

Create a CSV data file to define individual values for each gateway and port that you want to add. See the CSV Data File Creation for Cisco VG200 Gateways .

Step 3

Insert gateways and ports in the Cisco Unified Communications Manager database. See the Insert Gateways and Ports to Cisco Unified Communications Manager .

### Add Cisco Catalyst 6000 (FXS) Gateways and Ports Using BAT

You can use BAT to add Cisco Catalyst 6000 (FXS) gateways to the Cisco Unified Communications Manager database. You can also
                                 add FXS ports on the Cisco Catalyst 6000 (FXS) analog interface modules for analog devices. You must configure a Gateway Directory
                                 Number template to associate with these FXS ports and a Catalyst 6000 (FXS) ports template before adding these ports to the
                                 Cisco Unified Communications Manager database.

#### Before you begin

Before using BAT to add the FXS ports for the analog interface modules, you must install the Cisco Catalyst 6000 gateway by
                                 performing these tasks:

Configure the gateway by using Cisco IOS software command line interface. See the documentation that was supplied with your
                                       gateway for configuration instructions.

Use Cisco Unified Communications Manager Administration to add the Cisco Catalyst 6000 gateway in the Cisco Unified Communications
                                       Manager database. In Cisco Unified Communications Manager Administration, choose Device > Gateway and click Add New . Choose the Cisco Catalyst 6000 24 Port FXS Gateway and device protocol and then click Next .

Step 1

Create a Cisco Catalyst 6000 (FXS) gateway template. See the Create Cisco Catalyst 6000 (FXS) Gateway Template .

Step 2

To define common values for a set of FXS ports, create a Cisco Catalyst 6000 (FXS) ports template. See the FXS/FXO Port Configuration Field Descriptions .

Step 3

To define individual values for the FXS ports that you want to add, create a CSV data file. See the Create CSV Data File for Cisco Catalyst 6000 (FXS) Ports .

Step 4

Insert gateways and ports in the Cisco Unified Communications Manager database. See the Insert Gateways and Ports to Cisco Unified Communications Manager .

### Add Cisco VG224 Gateways Using BAT

Foreign Exchange Station (FXS) ports for analog devices

#### Before you begin

Before adding the VG224 gateways to the Cisco Unified Communications Manager database, you must first configure the gateway by using the Cisco IOS software command line interface (CLI). For gateway
                                 configuration procedures and commands, refer to the configuration documentation that is supplied with the gateway.

Step 1

Create a Cisco VG224 gateway template to define common values for a set of gateways and ports. See the Create Cisco VG224 Gateway Template .

Step 2

Create a CSV data file to define individual values for each gateway and port that you want to add. See the CSV Data Files Creation for Cisco VG224 Gateways and Ports .

Step 3

Insert gateways and ports in the Cisco Unified Communications Manager database. See the Insert Gateways and Ports to Cisco Unified Communications Manager .

### Add Cisco VG202 and Cisco VG204 Gateway Using BAT

You must perform the following tasks to insert Cisco VG202 or VG204 gateway and ports to Cisco Unified Communications Manager .

#### Before you begin

Before adding the VG202 or VG204 gateways to the Cisco Unified Communications Manager database, you must first configure the gateway by using the Cisco IOS software command line interface (CLI). For gateway
                                 configuration procedures and commands, refer to the configuration documentation that is supplied with the gateway.

Step 1

Create a Cisco gateway template to define common values for a set of gateways and ports. See the Create Cisco VG202 or VG204 Gateway Template .

Step 2

Create a CSV data file to define individual values for each gateway and port that you want to add. See the CSV Data File Creation for Cisco VG202 and VG204 Gateways .

Step 3

Insert gateways and ports in the Cisco Unified Communications Manager database. See the Insert Gateways and Ports to Cisco Unified Communications Manager .

### Add Cisco VG310 Gateway Template

You must perform the following tasks to insert Cisco VG310 gateway to Unified Communications Manager.

#### Before you begin

Before adding the Cisco VG310 gateways to the Unified Communications Manager database, you must first configure the gateway
                                 by using the Cisco IOS software command line interface (CLI). For gateway configuration procedures and commands, refer to
                                 the configuration documentation that is supplied with the gateway.

Step 1

Create a Cisco VG310 gateway template to define common values for a set of gateways and ports. See Create Cisco VG310 Gateway Template .

Step 2

Create a CSV data file to define individual values for each gateway and port that you want to add. See CSV Data Files Creation for Cisco VG310 Gateways and Ports .

Step 3

Insert gateways and ports in the Unified Communications Manager database. See Insert Gateways and Ports to Cisco Unified Communications Manager .

### Add Cisco VG320 Gateway Template

You must perform the following tasks to insert Cisco VG320 gateway to Unified Communications Manager.

#### Before you begin

Before adding the Cisco VG320 gateways to the Unified Communications Manager database, you must first configure the gateway
                                 by using the Cisco IOS software command line interface (CLI). For gateway configuration procedures and commands, refer to
                                 the configuration documentation that is supplied with the gateway.

Step 1

Create a Cisco VG320 gateway template to define common values for a set of gateways and ports. See Create Cisco VG320 Gateway Template .

Step 2

Create a CSV data file to define individual values for each gateway and port that you want to add. See CSV Data Files Creation for Cisco VG320 Gateways and Ports .

Step 3

Insert gateways and ports in the Unified Communications Manager database. See Insert Gateways and Ports to Cisco Unified Communications Manager .

### Add Cisco VG350 Gateway Template

You must perform the following tasks to insert Cisco VG350 gateway to Unified Communications Manager.

#### Before you begin

Before adding the Cisco VG350 gateways to the Unified Communications Manager database, you must first configure the gateway
                                 by using the Cisco IOS software command line interface (CLI). For gateway configuration procedures and commands, refer to
                                 the configuration documentation that is supplied with the gateway.

Step 1

Create a Cisco VG350 gateway template to define common values for a set of gateways and ports. See Create Cisco VG350 Gateway Template .

Step 2

Create a CSV data file to define individual values for each gateway and port that you want to add. See CSV Data Files Creation for Cisco VG350 Gateways and Ports .

Step 3

Insert gateways and ports in the Unified Communications Manager database. See Insert Gateways and Ports to Cisco Unified Communications Manager .

### Add Cisco VG420 Gateway Using BAT

You must perform the following tasks to insert Cisco VG420 gateway to Unified Communications Manager:

#### Before you begin

Important

Before adding the Cisco VG420 gateways to the Unified Communications Manager database, you must first configure the gateway
                                 by using the Cisco IOS Software command line interface (CLI). For gateway configuration procedures and commands, see the configuration
                                 documentation that is supplied with the gateway.

Step 1

Create a Cisco VG420 gateway template to define common values for a set of gateways and ports. See Create Cisco VG420 Gateway Template .

Step 2

Create a CSV data file to define individual values for each gateway and port that you want to add. See Create CSV Data Files for Cisco VG420 Gateways Using BAT Spreadsheet .

Step 3

Insert gateways and ports in the Unified Communications Manager database. See Insert Gateways and Ports to Cisco Unified Communications Manager .

### Add Cisco VG450 Gateway Using BAT

You must perform the following tasks to insert Cisco VG450 gateway to Unified Communications Manager

#### Before you begin

Before adding the Cisco VG450 gateways to the Unified Communications Manager database, you must first configure the gateway
                                 by using the Cisco IOS software command line interface (CLI). For gateway configuration procedures and commands, refer to
                                 the configuration documentation that is supplied with the gateway.

Step 1

Create a Cisco VG450 gateway template to define common values for a set of gateways and ports. See Create Cisco VG450 Gateway Template .

Step 2

Create a CSV data file to define individual values for each gateway and port that you want to add. See CSV Data Files Creation for Cisco VG450 Gateways and Ports .

Step 3

Insert gateways and ports in the Unified Communications Manager database. See Insert Gateways and Ports to Cisco Unified Communications Manager .

### Add Cisco ISR 4461 Gateway Using BAT

You must perform the following tasks to insert Cisco ISR 4461 gateway to Cisco Unified Communications Manager.

#### Before you begin

Before adding the Cisco ISR 4461 gateways to the Cisco Unified Communications Manager database, you must first configure the gateway by using the Cisco IOS software command line interface (CLI). For gateway
                                 configuration procedures and commands, refer to the configuration documentation that is supplied with the gateway.

Step 1

Create a Cisco ISR 4461 gateway template to define common values for a set of gateways and ports. See Create Cisco ISR 4461 Gateway Template .

Step 2

Create a CSV data file to define individual values for each gateway and port that you want to add. See CSV Data File Creation for Cisco ISR 4461 Gateways .

Step 3

Insert gateways and ports in the Cisco Unified Communications Manager database. See Insert Gateways and Ports to Cisco Unified Communications Manager .

## Find Gateway Template

Because you might have several gateway templates, Cisco Unified Communications Manager lets you locate specific template on the basis
                              		  of specific criteria. Use the following procedure to locate templates.

During your work in a browser session, your find/list search
                                          			 preferences get stored in the cookies on the client machine. If you navigate to
                                          			 other menu items and return to this menu item, or if you close the browser and
                                          			 then reopen a new browser window, your Cisco Unified Communications Manager search preferences get retained until you
                                          			 modify your search.

Step 1

Choose Bulk
                                             				  Administration > Gateways > Gateway
                                             				  Template .

Step 2

From the first Find Gateways where drop-down list, choose one of the following criteria:

Name

Description

DN/Route Pattern

Calling Search Space

Device Pool

Route Group Name

Device Type

Step 3

From the second Find Gateways where drop-down list, choose one of the following criteria:

begins with

contains

is exactly

ends with

is empty

is not empty

Step 4

Specify the appropriate search text, if applicable.

Tip

To find all gateways that are registered in the database, click Find without entering any search text.

Step 5

Choose Show from the third drop-down list to show the end points that are associated with gateways, and click Find .

A list of discovered templates displays by

Device Name

Description

Device Pool

Status

IP Address

Step 6

From the list of records, click the device name that matches your
                                       			 search criteria.

## Add or Edit Gateway Template

Use BAT to add or edit VG200, VG202, VG204, VG224, VG310, VG320, VG350, VG420, VG450, CiscoCatalyst 6000 (FXS), or Cisco ISR 4461 gateway templates in the Cisco Unified Communications Manager database.

Step 1

Choose Bulk Administration > Gateways > Gateway Template .

The Find and List Gateway Template window displays.

Step 2

Complete one of the following procedures:

To create a VG200 template, see the Create Cisco VG200 Gateway Template .

To create CiscoCatalyst 6000 (FXS) Ports template, see Create Cisco Catalyst 6000 (FXS) Gateway Template .

To create a VG224 template, see the Create Cisco VG224 Gateway Template .

To create a VG202 or VG204 template, see the Create Cisco VG202 or VG204 Gateway Template .

To create a Cisco VG310 template, see the Create Cisco VG310 Gateway Template .

To create a Cisco VG320 template, see the Create Cisco VG320 Gateway Template .

To create a Cisco VG350 template, see the Create Cisco VG350 Gateway Template .

To create a Cisco VG420 template, see the Create Cisco VG420 Gateway Template .

To create a Cisco VG450 template, see the Create Cisco VG450 Gateway Template

To create a Cisco ISR 4461 template, see the Create Cisco ISR 4461 Gateway Template .

### Create Cisco VG200 Gateway Template

You must create a CiscoVG200 template and then add endpoint identifiers for the network modules. Configure the following endpoint
                                 identifiers in the BAT template:

Foreign Exchange Station (FXS) ports

Foreign Exchange Office (FXO) trunks

T1 PRI trunks

E1 PRI trunks

T1 CAS trunks

Step 1

Choose Bulk
                                                				  Administration > Gateways > Gateway
                                                				  Template .

Step 2

Click Add New .

Step 3

From the Gateway Type drop-down list, select Cisco VG200 and click Next .

Step 4

Enter values for all the fields.

Step 5

Click Save .

Step 6

In the Subunit field(s), choose the appropriate type for each subunit field:

VIC-2FXS—Foreign Exchange Station (FXS) voice interface card

VIC-2FXO—Foreign Exchange Office (FXO) voice interface card

VWIC-1MFT-T1—Voice WAN interface card with one endpoint for T1CAS or T1 PRI

VWIC-2MFT-T1—Voice WAN interface card with two endpoints for T1 CAS or T1 PRI

VWIC-1MFT-E1—Voice WAN interface card with one endpoint for E1 PRI

VWIC-2MFT-E1—Voice WAN interface card with two endpoints for E1 PRI

Step 7

Click Save.

Step 8

Click an endpoint identifier (for example, 1/0/0) to configure
                                          			 device protocol information and add ports for the installed types of VICs.

Step 9

Click Reset to reset the gateway and apply the changes.

#### What to do next

Continue configuring endpoint information and ports as needed.

### Cisco VG200 Gateway Template Port Additions

The device protocols and port types that can be configured on VG200 gateways vary by the type of installed voice interface
                              cards.

#### Add FXS Ports to VG200 Gateway Template

You can use Foreign Exchange Station (FXS) ports to connect
                                    		  to any POTS device. Use this procedure to add FXS ports on a VG200 gateway
                                    		  template.

##### Before you begin

You must add an VG200 gateway template before configuring
                                    		  ports. See the Create Cisco VG200 Gateway Template for instructions.

Step 1

Find the gateway template to which you want to add FXS ports.

Step 2

From the Gateway Template Configuration window, click
                                             			 the endpoint identifier for the FXS VIC that you want to configure.

Step 3

Enter the appropriate Gateway Information and Port Information
                                             			 settings, and click Save .

See the following for field descriptions:

FXS/FXO Port Configuration Field Descriptions

POTS Port Configuration Settings

Step 4

Click Add a new DN to add directory numbers to the
                                             			 POTS port or, if you configured another type of port, go to Step 6 .

Step 5

Choose Back to MGCP Configuration in the Related Links drop-down list to return to the main VG200 Gateway Template Configuration window for the gateway to which you just added the ports and click Go .

Step 6

Click Reset to reset the gateway and apply the changes.

Step 7

Repeat Step 1 through Step 5 to add additional FXS ports.

#### Add FXO Ports to VG200 Gateway Template

Foreign Exchange Office (FXO) ports are used for connecting
                                    		  to a central office or PBX. You can add and configure FXO ports for loop start
                                    		  or ground start on an VG200 gateway template using BAT.

##### Before you begin

You must add a VG200 gateway template before configuring
                                    		  ports. See the Create Cisco VG200 Gateway Template for instructions.

Step 1

Find the gateway template to which you want to add FXS ports.

Step 2

From the Gateway Configuration window, click the endpoint
                                             			 identifiers of the FXO port that you want to configure.

Step 3

From the Port Type drop-down list, choose either Ground Start or Loop Start .

Step 4

Enter the appropriate Gateway Configuration and Port Information
                                             			 settings, and click Save .

Step 5

Choose Back to MGCP Configuration in the Related Links drop-down list to return to the main VG200 gateway configuration window for the gateway to which you just added the ports
                                             and click Go .

Step 6

Click Reset to reset the gateway and apply the changes.

Step 7

To add more FXO ports, repeat Step 2 through Step 4 .

#### Add Digital Access T1 (T1-CAS) Ports to VG200 Gateway Template

You can use BAT to add Digital Access T1 (T1-CAS) ports to
                                    		  an VG200 gateway template.

Step 1

Find the gateway template to which you want to add FXS ports.

Step 2

From the Gateway Configuration window, click the endpoint
                                             			 identifier of the Digital Access T1 (T1-CAS) port that you want to configure.

In the Device Protocol drop-down list box that
                                                				displays, choose Digital Access T1 and click Next .

Step 3

Enter the appropriate Gateway Configuration settings, and click Save .

Step 4

To reset the gateway and apply the changes, click Reset .

Step 5

See the Port Configuration Settings for the
                                             			 appropriate settings for the port type that you choose.

#### Add T1 PRI or E1 PRI Device to VG200 Gateway Template

You can use BAT to add T1 PRI or E1 PRI device to an VG200
                                    		  gateway template.

Step 1

Find the gateway template to which you want to add FXS ports.

Step 2

From the Gateway Configuration window, click the endpoint
                                             			 identifier of the T1 PRI or E1 PRI port that you want to configure.

Step 3

Configure the T1 PRI or E1 PRI device protocol settings.

Step 4

Click Save .

Step 5

Click Reset to reset the gateway and apply the changes.

### Create Cisco Catalyst 6000 (FXS) Gateway Template

Use BAT to create a CiscoCatalyst 6000 FXS gateway
                                 		  template. You must complete all fields unless otherwise noted.

Step 1

Choose Bulk
                                                				  Administration > Gateways > Gateway
                                                				  Template .

Step 2

Click Add New .

The Add a New Gateway Template window displays.

Step 3

From the Gateway Type drop-down list, choose Cisco Catalyst 6000 24 Port FXS Gateway and click Next .

The Gateway Template Configuration window displays.

Step 4

Enter a unique name for the template in the Template Name field.

Step 5

Enter the settings for the fields, and click Save .

Step 6

Click Add a New Port .

A port configuration dialog opens in a separate window.

Step 7

From the drop-down list, choose POTS as the port type depending on the gateway model that you are configuring.

Step 8

Enter the appropriate port configuration settings, and click Save .

Step 9

To add a directory numbers to an FXS port, click Add DN .

Step 10

Click Save .

### Create Cisco VG224 Gateway Template

You must create a CiscoVG224 template and then add endpoint identifiers for the network modules. Configure the following endpoint
                                 identifiers in the BAT template:

Foreign Exchange Station (FXS) ports

Step 1

Choose Bulk
                                                				  Administration > Gateways > Gateway
                                                				  Template .

The Find and List Gateway window displays.

Step 2

Click Add New .

The Add a New Gateway Template window displays.

Step 3

From the Gateway Type drop-down list, choose VG224 and click Next .

The Add a New Gateway Template window displays.

Step 4

From the Protocol drop-down list, choose MGCP or SCCP and click Next .

The Gateway Template Configuration window displays.

Step 5

Enter values for all the fields, and click Save .

See VG224 Gateway Template Field Descriptions for field descriptions.

When the insert completes, a new field displays on the pane.

Step 6

In the Subunit 0 field, choose the appropriate type for the subunit field from the drop-down list, and click Save .

VIC-2FXS—Foreign Exchange Station (FXS) voice interface card.

Step 7

Click an endpoint identifier (for example, 1/0/0) to configure
                                          			 device protocol information and add ports for the installed types of VICs.

Step 8

Click Reset to reset the gateway and apply the changes.

#### What to do next

Continue configuring endpoint information and ports as needed.

### Add FXS Ports to VG224 Gateway Template

Use BAT to add FXS ports on a VG224 gateway template.
                                 		  Foreign Exchange Station (FXS) ports are used to connect to POTS devices.

#### Before you begin

You must add a VG224 gateway template before configuring
                                 		  ports.

Step 1

Find the gateway template to which you want to add FXS ports.

Step 2

From the Gateway Template Configuration window, click the endpoint identifier for the FXS VIC that you want to configure.

The window refreshes and displays the Gateway Template Configuration window with the endpoint icons.

Step 3

Enter the appropriate Gateway Information and Port Information settings, and click Save .

See the following for field descriptions:

FXS/FXO Port Configuration Field Descriptions

POTS Port Configuration Settings

Step 4

Click Add a new DN to add directory numbers to the
                                          			 POTS port or, if you configured another type of port, go to 6 .

Step 5

To return to the main VG224 Gateway Template Configuration window for the gateway to which you just added the ports, select Back to MGCP Configuration in the Related Links drop-down list and click Go .

Step 6

Click Reset to reset the gateway and apply the changes.

Step 7

Repeat 1 through 5 to add additional FXS ports.

### Create Cisco VG202 or VG204 Gateway Template

You must create a CiscoVG202 or VG204 template and then add endpoint identifiers for the network modules. Configure the following
                                 endpoint identifiers in the BAT template:

Foreign Exchange Station (FXS) ports

Step 1

Choose Bulk
                                                				  Administration > Gateways > Gateway
                                                				  Template .

The Find and List Gateway window displays.

Step 2

Click Add New .

The Add a New Gateway Template window displays.

Step 3

From the Gateway Type drop-down list, choose VG202 or VG204 and click Next .

The Add a New Gateway Template window displays.

Step 4

From the Protocol drop-down list, choose MGCP or SCCP and click Next .

The Gateway Template Configuration window displays.

Step 5

Enter values for all the fields, and click Save .

Step 6

In the Subunit 0 field, choose the appropriate type
                                          			 for the subunit field from the drop-down list box, and click Save .

Step 7

Click an endpoint identifier (for example, 0/0) to configure
                                          			 device protocol information and add ports for the installed types of VICs.

Step 8

Click Reset to reset the gateway and apply the changes.

#### What to do next

Continue configuring endpoint information and ports as needed.

### Add FXS Ports to VG202 or VG204 Gateway Template

Use BAT to add FXS ports on a VG202 or VG204 gateway
                                 		  template. You can use Foreign Exchange Station (FXS) ports to connect to any
                                 		  POTS device.

#### Before you begin

You must add a VG202 or VG204 gateway template before you
                                 		  configure ports. See the Create Cisco VG202 or VG204 Gateway Template for instructions.

Step 1

Find the gateway template to which you want to add FXS ports.

Step 2

From the Gateway Template Configuration window, click the
                                          			 endpoint identifier for the FXS VIC that you want to configure.

Step 3

Enter the appropriate Gateway Information and Port Information settings and click Save .

See the following for field descriptions:

FXS/FXO Port Configuration Field Descriptions

POTS Port Configuration Settings

Step 4

Click Add a new DN to add directory numbers to the
                                          			 POTS port or, if you configured another type of port, go to Step 6 .

Step 5

To return to the main VG202 or VG204 Gateway Template Configuration window for the gateway to which you just added the ports, choose Back to MGCP Configuration in the Related Links drop-down list and click Go (if you configuring an MGCP gateway).

Step 6

Click Reset to reset the gateway and apply the changes.

Step 7

Repeat Step 2 through Step 5 to add additional FXS ports.

### Create Cisco VG310 Gateway Template

Use BAT to create a Cisco VG310 Gateway template. You must complete all fields unless otherwise noted.

Step 1

Choose Bulk Administration > Gateways > Gateway Template .

The Find and List Gateway window displays.

Step 2

Click Add New .

The Add a New Gateway Template window displays.

Step 3

From the Gateway Type drop-down list, choose VG310 and click Next .

The Gateway Template Configuration window displays.

Step 4

From the Protocol drop-down list, choose MGCP or SCCP and click Next .

The Gateway Template Configuration window displays.

Step 5

Enter a unique name for this template in the Template Name field.

Step 6

Enter values for all the fields, and click Save .

### Create Cisco VG320 Gateway Template

Use BAT to create a Cisco VG320 Gateway template. You must complete all fields unless otherwise noted.

Step 1

Choose Bulk Administration > Gateways > Gateway Template .

The Find and List Gateway window displays.

Step 2

Click Add New .

The Add a New Gateway Template window displays.

Step 3

From the Gateway Type drop-down list, choose VG320 and click Next .

The Gateway Configuration window displays.

Step 4

From the Protocol drop-down list, choose MGCP or SCCP and click Next .

The Gateway Template Configuration window displays.

Step 5

Enter a unique name for the template in the Template Name field.

Step 6

Enter values for all the fields, and click Save .

### Create Cisco VG350 Gateway Template

Use BAT to create a VG350 Gateway template. You must complete all the fields unless noted.

Step 1

Choose Bulk Administration > Gateways > Gateway Template .

The Find and List Gateway window displays.

Step 2

Click Add New .

The Add a New Gateway Template window displays.

Step 3

From the Gateway Type drop-down, choose VG350 and click Next .

Step 4

From the Protocol drop-down list, choose MGCP or SCCP , and click Next .

The Gateway Template Configuration window displays.

Step 5

Enter a unique name for the template in the Template Name field.

Step 6

Enter values for all the fields, and click Save .

### Create Cisco VG420 Gateway Template

Use BAT to create a Cisco VG420 Gateway template. You must complete all fields unless noted.

Step 1

Choose Bulk Administration > Gateways > Gateway Template .

Step 2

Click Add New .

Step 3

From the Gateway Type drop-down list, choose VG420 and click Next .

Step 4

From the Protocol drop-down list, choose SIP , SCCP or MGCP and click Next .

Step 5

Enter a unique name for the template in the Template Name field.

Step 6

Enter values for all the fields, and click Save .

See VG420 Gateway Template Field Descriptions for field descriptions.

### Create Cisco VG450 Gateway Template

Use BAT to create a VG450 Gateway template. You must complete all fields unless noted.

Step 1

Choose Bulk Administration > Gateways > Gateway Template .

The Find and List Gateway window displays.

Step 2

Click Add New .

The Add a new Gateway Template window displays.

Step 3

From the Gateway Type drop-down list, choose VG450 and click Next .

Step 4

From the Protocol drop-down list, choose SIP , MGCP or SCCP and click Next .

The Gateway Template Configuration window displays.

Step 5

Enter a unique name for the template in the Template Name field.

Step 6

Enter values for all the fields, and click Save .

### Create Cisco ISR 4461 Gateway Template

Use BAT to create a Cisco ISR 4461 Gateway template. You must complete all fields unless noted.

Step 1

Choose Bulk Administration > Gateways > Gateway Template .

The Find and List Gateway window displays.

Step 2

Click Add New .

The Add a new Gateway Template window displays.

Step 3

From the Gateway Type drop-down list, choose Cisco ISR 4461 and click Next .

Step 4

From the Protocol drop-down list, choose SIP , SCCP or MGCP and click Next .

The Gateway Template Configuration window displays.

Step 5

Enter a unique name for the template in the Template Name field.

Step 6

Enter values for all the fields, and click Save .

## Gateway Configuration Settings

Detailed field descriptions are available for all
                           		Cisco-supported gateways and ports that you can add or update using BAT.

### VG200 Gateway Template Field Descriptions

The following table provides detailed descriptions for VG200
                                 		  gateway template configuration settings.

Field

Description

Template Name

Enter a name up to 64 characters that identifies the CiscoVG200 gateway template.

Description

Enter a description that clarifies the purpose of the device.

Cisco Unified Communications Manager Group

Choose a Unified Communications Manager redundancy group from the list.

A Unified Communications Manager redundancy group includes a prioritized list of up to three Unified Communications Managers.
                                             The first Unified Communications Manager in the list serves as the primary Unified Communications Manager. If the primary
                                             Unified Communications Manager is not available or fails, the gateway attempts to connect with the next Unified Communications
                                             Manager in the list and so on.

Configured Slots, VICs, and Endpoints

Module in Slot 1

For the available slot on the VG200 gateway, choose from the
                                             					 following type of modules:

NM-1V—Network Module-1Voice has one voice interface card (VIC) in Sub-Unit 0 for FXS or FXO.

NM-2V—Network Module-2Voice has two VICs, one in Sub-Unit 0 and one in Sub-Unit 1 for either FXS or FXO.

NM-HDV—Network Module-High Density Voice has one VIC in Sub-Unit 0 either for T1 CAS or T1 PRI, or for E1 PRI.

None—No network modules are installed.

Product-Specific Configuration

Model-specific configuration fields defined by the gateway
                                             					 manufacturer

The gateway manufacturer specifies the model-specific fields
                                             					 under product-specific configuration. Because they are dynamically configured,
                                             					 they can change without notice.

To view field descriptions and help for product-specific
                                             					 configuration items, click the "?" information icon to the right of the Product Specific
                                             					 Configuration heading to display help in a popup dialog box.

If you need more information, refer to the documentation for
                                             					 the specific gateway that you are configuring or contact the manufacturer.

### VG224 Gateway Template Field Descriptions

The following table provides detailed descriptions for VG224
                                 		  gateway template configuration settings.

Field

Description

Template Name

Enter a name of up to 64 characters that identifies the
                                             					 CiscoVG224 gateway template.

Description

Enter a description that clarifies the purpose of the device.

Cisco Unified Communications Manager Group

From the drop-down list box, choose a Cisco Unified Communications Manager redundancy group.

A Cisco Unified Communications Manager redundancy group includes a prioritized list
                                             					 of up to three Cisco Unified Communications Manager s. The first Cisco Unified Communications Manager in the list serves as the primary Cisco Unified Communications Manager . If the primary Cisco Unified Communications Manager is not available or fails, the gateway
                                             					 attempts to connect with the next Cisco Unified Communications Manager in the list and so on.

Configured Slots, VICs, and Endpoints

Module in Slot 2

For the available slot on the VG224 gateway, select Analog
                                             					 from the drop-down list box.

Subunit 0

For the available subunit 0 on the VG224 gateway, choose 24FXS
                                             					 as the subunit from the drop-down list box.

Be aware that only Module in Slot 2, and Subunit 0 are
                                                         						available for VG224 gateways.

### VG202 and VG204 Gateway Template Field Descriptions

The following table provides detailed descriptions for VG202
                                 		  and VG204 gateway template configuration settings.

Field

Description

Template Name

Enter a name of up to 64 characters that identifies the
                                             					 CiscoVG202 or VG204 gateway template.

Description

Enter a description that clarifies the purpose of the device.

Cisco Unified Communications Manager Group

From the drop-down list box, choose a Cisco Unified Communications Manager redundancy group.

A Cisco Unified Communications Manager redundancy group includes a prioritized list
                                             					 of up to three Cisco Unified Communications Manager s. The first Cisco Unified Communications Manager in the list serves as the primary Cisco Unified Communications Manager . If the primary Cisco Unified Communications Manager is not available or fails, the gateway
                                             					 attempts to connect with the next Cisco Unified Communications Manager in the list and so on.

Configured Slots, VICs, and Endpoints

Module in Slot 0

For the available slot on the VG202 or VG204 gateway, select
                                             					 Analog from the drop-down list box.

Subunit 0

For the available subunit 0 on the VG202 or VG204 gateway,
                                             					 choose 2FXS as the subunit from the drop-down list box.

Be aware that only Module in Slot 0, and Subunit 0 are
                                                         						available for VG202 and VG204 gateways.

### VG310 Gateway Template Field Description

The following table provides detailed descriptions for Cisco VG310 gateway template configuration settings.

Field

Description

Template Name

Enter a name of up to 64 characters that identifies the VG310 gateway template.

Description

Enter a description that clarifies the purpose of the device.

Cisco Unified Communications Manager Group

From the drop-down list box, choose a Cisco Unified Communications Manager redundancy group.

A Cisco Unified Communications Manager redundancy group includes a prioritized list of up to three Cisco Unified Communications Manager s. The first Cisco Unified Communications Manager in the list serves as the primary Cisco Unified Communications Manager . If the primary Cisco Unified Communications Manager is not available or fails, the gateway attempts to connect with the next Cisco Unified Communications Manager in the list and so on.

Configured Slots, VICs, and Endpoints

Module in Slot 0

For the available slot on the VG310 gateway, select VG-2VWIC-MBRD from the drop-down list box.

Product-Specific Configuration

Model-specific configuration fields defined by the gateway manufacturer

The gateway manufacturer specifies the model-specific fields under product-specific configuration. Because they are dynamically
                                             configured, they can change without notice.

To view field descriptions and help for product-specific configuration items, click the "?" information icon to the right of the Product Specific Configuration heading to display help in a popup dialog box.

If you need more information, refer to the documentation for the specific gateway that you are configuring or contact the
                                             manufacturer.

### VG320 Gateway Template Field Description

The following table provides detailed descriptions for Cisco VG320 gateway template configuration settings.

Field

Description

Template Name

Enter a name of up to 64 characters that identifies the VG320 gateway template.

Description

Enter a description that clarifies the purpose of the device.

Cisco Unified Communications Manager Group

From the drop-down list box, choose a Cisco Unified Communications Manager redundancy group.

A Cisco Unified Communications Manager redundancy group includes a prioritized list of up to three Cisco Unified Communications Manager s. The first Cisco Unified Communications Manager in the list serves as the primary Cisco Unified Communications Manager . If the primary Cisco Unified Communications Manager is not available or fails, the gateway attempts to connect with the next Cisco Unified Communications Manager in the list and so on.

Configured Slots, VICs, and Endpoints

Module in Slot 0

For the available slot on the VG320 gateway, select VG-3VWIC-MBRD from the drop-down list box.

Product-Specific Configuration

Model-specific configuration fields defined by the gateway manufacturer

The gateway manufacturer specifies the model-specific fields under product-specific configuration. Because they are dynamically
                                             configured, they can change without notice.

To view field descriptions and help for product-specific configuration items, click the "?" information icon to the right of the Product Specific Configuration heading to display help in a popup dialog box.

If you need more information, refer to the documentation for the specific gateway that you are configuring or contact the
                                             manufacturer.

### VG350 Gateway Template Field Description

The following table provides detailed descriptions for Cisco VG350 gateway template configuration settings.

Field

Description

Template Name

Enter a name of up to 64 characters that identifies the VG350 gateway template.

Description

Enter a description that clarifies the purpose of the device.

Cisco Unified Communications Manager Group

From the drop-down list box, choose a Cisco Unified Communications Manager redundancy group.

A Cisco Unified Communications Manager redundancy group includes a prioritized list of up to three Cisco Unified Communications Manager s. The first Cisco Unified Communications Manager in the list serves as the primary Cisco Unified Communications Manager . If the primary Cisco Unified Communications Manager is not available or fails, the gateway attempts to connect with the next Cisco Unified Communications Manager in the list and so on.

Configured Slots, VICs, and Endpoints

Module in Slot 0

For the available slot on the VG350 gateway, select NM-4VWIC-MBRD from the drop-down list box.

Module in Slot 1/3

For the available slot on the VG350 gateway, select NONE from the drop-down list.

Module in Slot 2/4

For the available slot on the VG350 gateway, select ANALOG from the drop-down list.

Product-Specific Configuration

Model-specific configuration fields defined by the gateway manufacturer

The gateway manufacturer specifies the model-specific fields under product-specific configuration. Because they are dynamically
                                             configured, they can change without notice.

To view field descriptions and help for product-specific configuration items, click the "?" information icon to the right of the Product Specific Configuration heading to display help in a popup dialog box.

If you need more information, refer to the documentation for the specific gateway that you are configuring or contact the
                                             manufacturer.

### VG420 Gateway Template Field Descriptions

The following table provides detailed descriptions for Cisco VG420 gateway template configuration settings.

Field

Description

Template Name

Enter a name of up to 64 characters that identifies the VG420 gateway template.

Description

Enter a description that clarifies the purpose of the device.

Unified Communications Manager Group

From the drop-down list, choose a Unified Communications Manager redundancy group.

A Unified Communications Manager redundancy group includes a prioritized list of up to three Unified Communications Managers.
                                             The first Unified Communications Manager in the list serves as the primary Unified Communications Manager. If the primary
                                             Unified Communications Manager is not available or fails, the gateway attempts to connect with the next Unified Communications
                                             Manager in the list and so on.

Configured Slots, VICs, and Endpoints

Module in Slot 0

For the available slot on the VG420 gateway, select ISR-2NIM-MBRD from the drop-down list.

Module in Slot 1

For the available slot on the VG420 gateway, select ANALOG from the drop-down list.

Product-Specific Configuration

Model-specific configuration fields defined by the gateway manufacturer

The gateway manufacturer specifies the model-specific fields under product-specific configuration. Because they are dynamically
                                             configured, they can change without notice.

To view field descriptions and help for product-specific configuration items, click the "?" information icon to the right of the Product Specific Configuration heading to display help in a pop-up dialog box.

If you need more information, see the documentation for the specific gateway that you are configuring or contact the manufacturer.

### VG450 Gateway Template Field Description

The following table provides detailed descriptions for Cisco VG450 gateway template configuration settings.

Field

Description

Template Name

Enter a name of up to 64 characters that identifies the VG450 gateway template.

Description

Enter a description that clarifies the purpose of the device.

Unified Communications Manager Group

From the drop-down list box, choose a Unified Communications Manager redundancy group.

A Unified Communications Manager redundancy group includes a prioritized list of up to three Unified Communications Managers.
                                             The first Unified Communications Manager in the list serves as the primary Unified Communications Manager. If the primary
                                             Unified Communications Manager is not available or fails, the gateway attempts to connect with the next Unified Communications
                                             Manager in the list and so on.

Configured Slots, VICs, and Endpoints

Module in Slot 0

For the available slot on the VG450 gateway, select ISR-3NIM-MBRD from the drop-down list box.

Module in Slot 1/2/3

For the available slot on the VG450 gateway, select ANALOG from the drop-down list.

ANALOG—In the SM-X slot on the gateway, users can choose SM-X-16FXS/FXO, SM-X-24FXS/4FXO, SM-X-8FXS/12FXO, SM-X-56FXS, or
                                             SM-X-72FXS modules.

Product-Specific Configuration

Model-specific configuration fields defined by the gateway manufacturer

The gateway manufacturer specifies the model-specific fields under product-specific configuration. Because they are dynamically
                                             configured, they can change without notice.

To view field descriptions and help for product-specific configuration items, click the "?" information icon to the right of the Product Specific Configuration heading to display help in a popup dialog box.

If you need more information, refer to the documentation for the specific gateway that you are configuring or contact the
                                             manufacturer.

### ISR 4461 Gateway Template Field Descriptions

The following table provides detailed descriptions for Cisco ISR 4461 gateway template configuration settings.

Field

Description

Template Name

Enter a name of up to 64 characters that identifies the ISR 4461 gateway template.

Description

Enter a description that clarifies the purpose of the device.

Cisco Unified Communications Manager Group

From the drop-down list box, choose a Cisco Unified Communications Manager redundancy group.

A Cisco Unified Communications Manager redundancy group includes a prioritized list of up to three Cisco Unified Communications
                                             Managers. The first Cisco Unified Communications Manager in the list serves as the primary Cisco Unified Communications Manager.
                                             If the primary Cisco Unified Communications Manager is not available or fails, the gateway attempts to connect with the next
                                             Cisco Unified Communications Manager in the list and so on.

Configured Slots, VICs, and Endpoints

Module in Slot 0

For the available slot on the ISR 4461 gateway, select ISR-3NIM-MBRD from the drop-down list box.

Module in Slot 1/2/3

For the available slot on the ISR 4461 gateway, choose from the following type of modules:

ANALOG—In the SM-X slot on the gateway, users can choose SM-X-16FXS/FXO, SM-X-24FXS/4FXO, SM-X-8FXS/12FXO, SM-X-56FXS, or
                                                   SM-X-72FXS modules.

SM-X-NIM-ADPTR—Adapter for the NIM in a SM-X slot on the gateway.

Product-Specific Configuration

Model-specific configuration fields defined by the gateway manufacturer

The gateway manufacturer specifies the model-specific fields under product-specific configuration. Because they are dynamically
                                             configured, they can change without notice.

To view field descriptions and help for product-specific configuration items, click the "?" information icon to the right of the Product Specific Configuration heading to display help in a popup dialog box.

If you need more information, refer to the documentation for the specific gateway that you are configuring or contact the
                                             manufacturer.

### Cisco Catalyst 6000 24 Port FXS Gateway Template Field Descriptions

The following table lists configuration settings for
                                 		  CiscoCatalyst 6000 24 port FXS gateway template.

Field

Description

Description

Enter the purpose of the device. The description can include
                                             					 up to 50 characters in any language, but it cannot include double-quotes ( " ),
                                             					 percentage sign ( % ), ampersand (&), back-slash ( \ ), or angle brackets
                                             					 (<>).

Device Pool

From the drop-down list box, select the appropriate device
                                             					 pool.

The device pool specifies a collection of properties for this
                                             					 device that includes Communications Manager Group, Date / Time Group, Region, and
                                             					 Calling Search Space for auto-registration of devices.

Common Device Configuration

Choose the common device configuration to which you want this
                                             					 gateway assigned. The common device configuration includes the attributes
                                             					 (services or features) that are associated with a particular user. You
                                             					 configure the common device configurations in the Common Device Configuration window.

To see the common device configuration settings, click the
                                             					 View Details link.

Media Resource Group List

This list provides a prioritized grouping of media resource
                                             					 groups. An application chooses the required media resource, such as a Music On
                                             					 Hold server, from among the available media resources according to the priority
                                             					 order that a Media Resource Group List defines.

Network Hold MOH Audio Source

Choose the network hold audio source for this group of IP
                                             					 gateways.

The network hold audio source identifies the audio source from
                                             					 which music is played when the system places a call on hold, such as when the
                                             					 user transfers or parks a call.

Calling Search Space

From the drop-down list box, select the appropriate calling
                                             					 search space. The calling search space specifies a collection of partitions
                                             					 that are searched to determine how a collected (originating) number should be
                                             					 routed.

You can configure the number of calling search spaces that
                                             					 display in this drop-down list box by using the Max List Box Items enterprise
                                             					 parameter. If more calling search spaces exist than the Max List Box Items
                                             					 enterprise parameter specifies, the ellipsis button (...) displays next to the
                                             					 drop-down list box. Click the... button to display the Select Calling Search
                                             					 Space window. Enter a partial calling search space name in the List items where
                                             					 Name contains field. Click the desired calling search space name in the list of
                                             					 calling search spaces that displays in the Select item to use box and click OK .

To set the maximum list box items, choose System > Enterprise
                                                               							 Parameters and choose UnifiedCMAdmin Parameters.

AAR Calling Search Space

Choose the appropriate calling search space for the device to
                                             					 use when it performs automated alternate routing (AAR). The AAR calling search
                                             					 space specifies the collection of route partitions that are searched to
                                             					 determine how to route a collected (originating) number that is otherwise
                                             					 blocked due to insufficient bandwidth.

Location

Select the appropriate location for this device. The location
                                             					 specifies the total bandwidth that is available for calls to and from this
                                             					 location. A location setting of None means that the locations feature does not
                                             					 keep track of the bandwidth that this device consumes.

AAR Group

Choose the automated alternate routing (AAR) group for this
                                             					 device. The AAR group provides the prefix digits that are used to route calls
                                             					 that are otherwise blocked due to insufficient bandwidth. An AAR group setting
                                             					 of None specifies that no rerouting of blocked calls will be attempted.

Network Locale

From the drop-down list box, choose the locale that is
                                             					 associated with the gateway. The network locale identifies a set of detailed
                                             					 information to support the hardware in a specific location. The network locale
                                             					 contains a definition of the tones and cadences that the device uses in a
                                             					 specific geographic area.

Choose only a network locale that is already installed and
                                                         						supported by the associated devices. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up.

Use Trusted Relay Point

From the drop-down list box, enable or disable whether Cisco Unified Communications Manager inserts a trusted relay point (TRP) device
                                             					 with this media endpoint. Choose one of the following values:

- Default—If you
                                                						choose this value, the device uses the Use Trusted Relay Point setting from the
                                                						common device configuration with which this device associates.

- Off—Choose this
                                                						value to disable the use of a TRP with this device. This setting overrides the
                                                						Use Trusted Relay Point setting in the common device configuration with which
                                                						this device associates.

- On—Choose this
                                                						value to enable the use of a TRP with this device. This setting overrides the
                                                						Use Trusted Relay Point setting in the common device configuration with which
                                                						this device associates.

A Trusted Relay Point (TRP) device designates an MTP or
                                             					 transcoder device that is labeled as Trusted Relay Point.

Cisco Unified Communications Manager places the TRP closest to the
                                             					 associated endpoint device if more than one resource is needed for the endpoint
                                             					 (for example, a transcoder or RSVP Agent).

If both TRP and MTP are required for the endpoint, TRP gets
                                             					 used as the required MTP.

Port Selection Order

Choose the order in which ports are chosen. If you are not
                                             					 sure which port order to use, choose TOP_DOWN:

- TOP_DOWN—Selects
                                                						ports in descending order, from port 1 to port 8.

- BOTTOM_UP—Selects
                                                						ports in ascending order, from port 8 to port 1.

Load Information

Enter the appropriate firmware load information for the
                                             					 gateway.

The values that you enter here override the default values for
                                             					 this gateway.

Transmit UTF-8 for Calling Party Name

This device uses the user locale setting of the device's
                                             					 device pool to determine whether to send unicode and whether to translate
                                             					 received unicode information.

For the sending device, if you check this check box and the
                                             					 user locale setting in the device's device pool matches the terminating phone's
                                             					 user locale, the device sends unicode. If the user locale settings do not
                                             					 match, the device sends ASCII.

The receiving device translates incoming unicode characters
                                             					 based on the user locale setting of the sending device's device pool. If the
                                             					 user locale setting matches the terminating phone's user locale, the phone
                                             					 displays the characters.

The phone may display junk characters if the two ends of the
                                                         						trunk configure user locales that do not belong to the same language group.

Calling Party Transformation CSS

This setting allows you to localize the calling party number
                                             					 on the device. Make sure that the Calling Party Transformation CSS that you
                                             					 choose contains the calling party transformation pattern that you want to
                                             					 assign to this device.

The device takes on the attributes of the Calling Party
                                             					 Transformation Pattern when you assign the pattern to a partition where the
                                             					 Calling Party Transformation CSS exists.

Use Device Pool Calling Party Transformation CSS

To use the Calling Party Transformation CSS that is configured
                                             					 in the device pool that is assigned to this device, check this check box. If
                                             					 you do not check this check box, the device uses the Calling Party
                                             					 Transformation CSS that you configured in the device configuration window.

Multilevel Precedence and Preemption (MLPP)
                                                						Information

MLPP Domain

From the drop-down list box, choose an MLPP domain to
                                             					 associate with this device. If you leave the value <None>, this device
                                             					 inherits its MLPP domain from the value that was set for the device's device
                                             					 pool. If the device pool does not have an MLPP Domain setting, this device
                                             					 inherits its MLPP Domain from the value that was set for the MLPP Domain
                                             					 Identifier enterprise parameter.

MLPP Indication

This device type does not have this setting.

MLPP Preemption

This setting does not have this device type.

Geo Location Configuration

Geo Location

From the drop-down list box, select a geo location.

You can select the Unspecified geo location, which designates
                                             					 that this device does not associate with a geo location.

You can also select a geo location that has been configured
                                             					 with the System > Geolocation
                                                   						  Configuration menu option.

Geo Location Filter

From the drop-down list box, select a geo location filter.

If you leave the <None> setting, no geo location filter
                                             					 gets applied for this device.

You can also select a geo location filter that has been
                                             					 configured with the System > Geolocation
                                                   						  Filter menu option.

### FXS/FXO Port Configuration Field Descriptions

The following table provides detailed descriptions for
                                 		  FXS/FXO port configuration settings.

For the VG200 gateway, not all switch emulation types
                                 		  support the network side. How you configure the gateway switch type determines
                                 		  whether you may or may not be able to set network side.

Field

Description

Device Information

End-Point Name

For VG200 gateways, this display-only field contains a string
                                             					 that Cisco Unified Communications Manager generates that uniquely identifies the VG200
                                             					 analog interface.

Description

Cisco Unified Communications Manager generates a string that uniquely
                                             					 identifies the analog MGCP description.

For example:

AALN/S0/SU1/1@domain.com

You can edit this field. The description can include up to 50
                                             					 characters in any language, but it cannot include double-quotes
                                             					 ( " ), percentage sign ( % ), ampersand
                                             					 ( & ), back-slash ( \ ), or angle brackets
                                             					 (<>).

Device Pool

From the drop-down list box, choose the appropriate device
                                             					 pool.

The device pool specifies a collection of properties for this
                                             					 device including Communications Manager Group, Date/Time Group, Region, and
                                             					 Calling Search Space for auto registration of devices.

Media Resource Group List

This list provides a prioritized grouping of media resource
                                             					 groups. An application chooses the required media resource, such as a Music On
                                             					 Hold server, from among the available media resources according to the priority
                                             					 order that is defined in a Media Resource Group List.

Packet Capture Mode (for Cisco IOS MGCP gateways only)

Configure this field only when you need to troubleshoot
                                             					 encrypted signaling information for the Cisco IOS MGCP gateway. Configuring
                                             					 packet capturing may cause call-processing interruptions. For more information
                                             					 about this field, see the Cisco Unified Communications Manager Security Guide .

Packet Capture Duration (for Cisco IOS MGCP gateways only)

Configure this field only when you need to troubleshoot
                                             					 encrypted signaling information for the Cisco IOS MGCP gateway. Configuring
                                             					 packet capturing may cause call-processing interruptions. For more information
                                             					 about this field, see the Cisco Unified Communications Manager Security Guide .

Calling Search Space

From the drop-down list box, choose the appropriate calling
                                             					 search space. A calling search space comprises a collection of route partitions
                                             					 that are searched to determine how a collected (originating) number should be
                                             					 routed.

AAR Calling Search Space

Choose the appropriate calling search space for the device to
                                             					 use when it performs automated alternate routing (AAR). The AAR calling search
                                             					 space specifies the collection of route partitions that are searched to
                                             					 determine how to route a collected (originating) number that is otherwise
                                             					 blocked due to insufficient bandwidth.

Location

Use locations to implement call admission control (CAC) in a
                                             					 centralized call-processing system. CAC enables you to regulate audio quality
                                             					 and video availability by limiting the amount of bandwidth that is available
                                             					 for audio and video calls over links between locations. The location specifies
                                             					 the total bandwidth that is available for calls to and from this location.

From the drop-down list box, choose the appropriate location
                                             					 for this device.

A location setting of Hub_None means that the locations
                                             					 feature does not keep track of the bandwidth that this device consumes. A
                                             					 location setting of Phantom specifies a location that enables successful CAC
                                             					 across intercluster trunks that use H.323 or SIP protocol.

To configure a new location, use the System > Location menu option.

AAR Group

Choose the automated alternate routing (AAR) group for this
                                             					 device. The AAR group provides the prefix digits that are used to route calls
                                             					 that are otherwise blocked due to insufficient bandwidth. An AAR group setting
                                             					 of None specifies that no rerouting of blocked calls will be attempted.

Network Locale

From the drop-down list box, choose the locale that is
                                             					 associated with the gateway. The network locale identifies a set of detailed
                                             					 information to support the hardware in a specific location. The network locale
                                             					 contains a definition of the tones and cadences that the device uses in a
                                             					 specific geographic area.

Choose only a network locale that is already installed and
                                                         						that the associated devices support. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up.

Use Trusted Relay Point

From the drop-down list box, enable or disable whether Cisco Unified Communications Manager inserts a trusted relay point (TRP) device
                                             					 with this media endpoint. Choose one of the following values:

- Default—If you
                                                						choose this value, the device uses the Use Trusted Relay Point setting from the
                                                						common device configuration with which this device associates.

- Off—Choose this
                                                						value to disable the use of a TRP with this device. This setting overrides the
                                                						Use Trusted Relay Point setting in the common device configuration with which
                                                						this device associates.

- On—Choose this
                                                						value to enable the use of a TRP with this device. This setting overrides the
                                                						Use Trusted Relay Point setting in the common device configuration with which
                                                						this device associates.

A Trusted Relay Point (TRP) device designates an MTP or
                                             					 transcoder device that is labeled as Trusted Relay Point.

Cisco Unified Communications Manager places the TRP closest to the
                                             					 associated endpoint device if more than one resource is needed for the endpoint
                                             					 (for example, a transcoder or RSVP Agent).

If both TRP and RSVP Agent are needed for the endpoint, Cisco Unified Communications Manager first tries to find an RSVP Agent that can
                                             					 also be used as a TRP.

If both TRP and transcoder are needed for the endpoint, Cisco Unified Communications Manager first tries to find a transcoder that is also
                                             					 designated as a TRP.

Transmit UTF-8 for Calling Party Name

This device uses the user locale setting of the device pool
                                             					 for the device to determine whether to send unicode and whether to translate
                                             					 received unicode information.

For the sending device, if you check this check box and the
                                             					 user locale setting in the device pool for the device matches the terminating
                                             					 phone user locale, the device sends unicode. If the user locale settings do not
                                             					 match, the device sends ASCII.

The receiving device translates incoming unicode characters
                                             					 based on the user locale setting of the sending device pool for the device. If
                                             					 the user locale setting matches the terminating phone user locale, the phone
                                             					 displays the characters.

The phone may display junk characters if the two ends of the
                                                         						trunk configure user locales that do not belong to the same language group.

Calling Party Transformation CSS

This setting, which displays for FXS ports (not FXO ports),
                                             					 allows you to localize the calling party number on the device. Make sure that
                                             					 the Calling Party Transformation CSS that you choose contains the calling party
                                             					 transformation pattern that you want to assign to this device.

Tip

Use Device Pool Calling Party Transformation CSS

To use the Calling Party Transformation CSS that is configured
                                             					 in the device pool that is assigned to this device, check this check box. If
                                             					 you do not check this check box, the device uses the Calling Party
                                             					 Transformation CSS that you configured in the Gateway Configuration window.

This settings displays for FXS ports, not FXO ports.

Hotline Device

Check this check box to make this device a Hotline device.
                                             					 Hotline devices can only connect to other Hotline devices. This feature is an
                                             					 extension of PLAR, which configures a phone to automatically dial one directory
                                             					 number when it goes off-hook. Hotline provides additional restrictions that you
                                             					 can apply to devices that use PLAR.

To implement Hotline, you must also create a softkey template
                                             					 without supplementary service softkeys, and apply it to the Hotline device.

Multilevel Precedence and Preemption (MLPP)
                                                						Information

MLPP Domain

From the drop-down list box, select an MLPP domain to
                                             					 associate with this device. If you leave the value <None>, this device
                                             					 inherits its MLPP domain from the value set for the device pool for the device.
                                             					 If the device pool does not have an MLPP Domain setting, this device inherits
                                             					 its MLPP Domain from the value set for the MLPP Domain Identifier enterprise
                                             					 parameter.

MLPP Indication

Be aware that this setting is not available for all devices.
                                             					 If available, this setting specifies whether a device that can play precedence
                                             					 tones will use the capability when it places an MLPP precedence call.

From the drop-down list box, choose a setting to assign to
                                             					 this device from the following options:

- Default—This
                                                						device inherits its MLPP indication setting from its device pool.

- Off—This device
                                                						does not handle nor process indication of an MLPP precedence call.

- On—This device
                                                						does handle and process indication of an MLPP precedence call.

Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off or Default (when default is Off) while
                                                         						MLPP Preemption is set to Forceful.

MLPP Preemption

Be aware that this setting is not available for all devices.
                                             					 If available, this setting specifies whether a device that can preempt calls in
                                             					 progress will use the capability when it places an MLPP precedence call.

From the drop-down list box, choose a setting to assign to
                                             					 this device from the following options:

- Default—This
                                                						device inherits its MLPP preemption setting from its device pool.

- Disabled—This
                                                						device does not allow preemption of lower precedence calls to take place when
                                                						necessary for completion of higher precedence calls.

- Forceful—This
                                                						device allows preemption of lower precedence calls to take place when necessary
                                                						for completion of higher precedence calls.

Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off or Default (when default is Off) while
                                                         						MLPP Preemption is set to Forceful.

Port Information (POTS)

Port Direction

Choose the direction of calls that are passing through this
                                             					 port:

- Inbound—Use for
                                                						incoming calls only.

- Outbound—Use for
                                                						outgoing calls.

- Bothways—Use for
                                                						inbound and outbound calls (default).

Prefix DN(for FXS ports)

Enter the prefix digits that are appended to the digits that
                                             					 this trunk receives on incoming calls.

Cisco Unified Communications Manager adds prefix digits after first
                                             					 truncating the number in accordance with the Num Digits setting.

You can enter the international escape character + .

Num Digits(for FXS ports)

Enter the number of significant digits to collect, from 0 to
                                             					 32.

Cisco Unified Communications Manager counts significant digits from the
                                             					 right (last digit) of the number called.

Use this field for the processing of incoming calls and to
                                             					 indicate the number of digits starting from the last digit of the called number
                                             					 that is used to route calls coming into the PRI span. See Prefix DN.

Expected Digits(for FXS ports)

Enter the number of digits that are expected on the inbound
                                             					 side of the trunk. For this rarely used field, leave zero as the default value
                                             					 if you are unsure.

SMDI Port Number (0-4096)

Use this field for analog access ports that connect to a
                                             					 voice-messaging system.

Set the SMDI Port Number equal to the actual port number on
                                             					 the voice-messaging system to which the analog access port connects.

Voice-mail logical ports typically must match physical ports
                                                         						for the voice-messaging system to operate correctly.

Unattended Port

Check this check box to indicate an unattended port on this
                                             					 device.

Geo Location Configuration

Geo Location

From the drop-down list box, choose a geo location.

You can choose the Unspecified geo location, which designates
                                             					 that this device does not associate with a geo location.

You can also choose a geolocation that has been configured
                                             					 with the System > Geolocation
                                                   						  Configuration menu option.

Geo Location Filter

From the drop-down list box, choose a geo location filter.

If you leave the <None> setting, no geo location filter
                                             					 gets applied for this device.

You can also choose a geo location filter that has been
                                             					 configured with the System Geolocation
                                                						Filter menu option.

This field is not supported for FXS gateways.

Product-Specific Configuration

Model-specific configuration fields defined by the gateway
                                             					 manufacturer

The gateway manufacturer specifies the model-specific fields
                                             					 under product-specific configuration. Because they are dynamically configured,
                                             					 they can change without notice.

To view field descriptions and help for product-specific
                                             					 configuration items, click the "?" information icon to the right of the Product Specific
                                             					 Configuration heading to display help in a popup dialog box.

If you need more information, refer to the documentation for
                                             					 the specific gateway that you are configuring or contact the manufacturer.

### Digital Access T1 Trunks on Cisco VG200 Gateway Template Field Descriptions

The following table provides detailed field descriptions for
                                 		  adding or updating values for the T1 CAS trunks on a CiscoVG200 gateway.

Some fields display the values that were configured in Cisco Unified Communications Manager Administration.

In the BAT user interface, field names that have an asterisk
                                 		  require an entry. Consider an entry in fields without an asterisk as optional.

Field

Description

End-Point Name

For VG200 gateways, this display-only field contains a string
                                             					 that Cisco Unified Communications Manager generates that uniquely identifies the VG200
                                             					 digital interface.

For example:

S1/DS1-0@VG200-2

S1 indicates slot 1, DS1-0 designates the digital interface,
                                             					 and @ VG200-2 designates the VG200 template name.

Description

Enter a description that clarifies the purpose of the device.
                                             					 The description can include up to 50 characters in any language, but it cannot
                                             					 include double-quotes ("), percentage sign
                                             					 ( % ), ampersand (&), back-slash
                                             					 ( \ ), or angle brackets (<>).

Device Pool

From the drop-down list box, choose the appropriate device
                                             					 pool.

The device pool specifies a collection of properties for this
                                             					 device including Communications Manager Group, Date / Time
                                             					 Group, Region, and Calling Search Space for auto-registration of devices.

Call Classification

This parameter determines whether an incoming call that is
                                             					 using this gateway is considered off the network (OffNet) or on the network
                                             					 (OnNet).

When the Call Classification field is configured as Use System
                                             					 Default, the setting of the Cisco Unified Communications Manager clusterwide service parameter, Call
                                             					 Classification, determines whether the gateway is OnNet or OffNet.

This field provides an OnNet or OffNet alerting tone when the
                                             					 call is OnNet or OffNet, respectively.

Media Resource Group List

This list provides a prioritized grouping of media resource
                                             					 groups. An application chooses the required media resource, such as a Music On
                                             					 Hold server, from among the available media resources according to the priority
                                             					 order that is defined in a Media Resource List.

Calling Search Space

From the drop-down list box, choose the appropriate calling
                                             					 search space. A calling search space designates a collection of route
                                             					 partitions that are searched to determine how a collected (originating) number
                                             					 should be routed.

You can configure the number of calling search spaces that
                                             					 display in this drop-down list box by using the Max List Box Items enterprise
                                             					 parameter. If more calling search spaces exist than the Max List Box Items
                                             					 enterprise parameter specifies, the ellipsis button (...) displays next to the
                                             					 drop-down list box. Click the... button to display the Select Calling Search Space window. Enter
                                             					 a partial calling search space name in the List items where Name contains
                                             					 field. Click the desired calling search space name in the list of calling
                                             					 search spaces that displays in the Select item to use box and click OK .

To set the maximum list box items, choose System > Enterprise
                                                               							 Parameters and choose UnifiedCMAdmin Parameters.

AAR Calling Search Space

Choose the appropriate calling search space for the device to
                                             					 use when automated alternate routing (AAR) is performed. The AAR calling search
                                             					 space specifies the collection of route partitions that are searched to
                                             					 determine how to route a collected (originating) number that is otherwise
                                             					 blocked due to insufficient bandwidth.

Location

Choose the appropriate location for this device. The location
                                             					 specifies the total bandwidth that is available for calls to and from this
                                             					 location. A location setting of None means that the locations feature does not
                                             					 keep track of the bandwidth that this device consumes.

AAR Group

Choose the automated alternate routing (AAR) group for this
                                             					 device. The AAR group provides the prefix digits that are used to route calls
                                             					 that are otherwise blocked due to insufficient bandwidth. An AAR group setting
                                             					 of None specifies that no rerouting of blocked calls will be attempted.

MLPP Domain

From the drop-down list box, choose an MLPP domain to
                                             					 associate with this device. If you leave the value <None>, this device
                                             					 inherits its MLPP domain from the value that was set for the device's device
                                             					 pool. If the device pool does not have an MLPP Domain setting, this device
                                             					 inherits its MLPP Domain from the value that was set for the MLPP Domain
                                             					 Identifier enterprise parameter.

Handle DTMF Precedence Signals

Check this box to enable this gateway to interpret special
                                             					 DTMF signals as MLPP precedence levels.

Load Information

Enter the appropriate firmware load information for the
                                             					 gateway.

The values that you enter here override the default values for
                                             					 this gateway.

Port Selection Order

Choose the order in which channels or ports are allocated for
                                             					 outbound calls from first (lowest number port) to last (highest number port) or
                                             					 from last to first.

Valid entries include TOP_DOWN (first to last) or BOTTOM_UP
                                             					 (last to first). If you are not sure which port order to use, choose TOP_DOWN.

Digit Sending

Choose one of the following digit sending types for
                                             					 out-dialing:

- DTMF—Dual-tone
                                                						multifrequency. Normal touchtone dialing

- MF—Multifrequency

- PULSE—Pulse
                                                						(rotary) dialing

Network Locale

From the drop-down list box, choose the locale that is
                                             					 associated with the gateway. The network locale identifies a set of detailed
                                             					 information to support the hardware in a specific location. The network locale
                                             					 contains a definition of the tones and cadences that the device uses in a
                                             					 specific geographic area.

Choose only a network locale that is already installed and
                                                         						supported by the associated devices. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up.

SMDI Base Port

Enter the first SMDI port number of the T1 span.

If you set this parameter to a nonzero value and this gateway
                                             					 belongs to an unknown type of route list, route group, or route list, hunting
                                             					 does not continue past this span.

Geo Location Configuration

Geo Location

From the drop-down list box, choose a geo location.

You can choose the Unspecified geo location, which designates
                                             					 that this device does not associate with a geo location.

You can also choose a geolocation that has been configured
                                             					 with the System > Geolocation
                                                   						  Configuration menu option.

Geo Location Filter

From the drop-down list box, choose a geo location filter.

If you leave the <None> setting, no geo location filter
                                             					 gets applied for this device.

You can also choose a geo location filter that has been
                                             					 configured with the System > Geolocation
                                                   						  Filter menu option.

Product-Specific Configuration

Model-specific configuration fields that the gateway
                                             					 manufacturer defines

The gateway manufacturer specifies the model-specific fields
                                             					 under product-specific configuration. Because they are dynamically configured,
                                             					 they can change without notice.

To view field descriptions and help for product-specific
                                             					 configuration items, click the "?" information icon to the right of the Product Specific
                                             					 Configuration heading to display help in a popup dialog box.

If you need more information, refer to the documentation for
                                             					 the specific gateway that you are configuring or contact the manufacturer.

### T1 PRI or E1 PRI Trunks on Cisco VG200 Gateway Template Field Descriptions

The following table provides field descriptions for adding
                                 		  or updating values for T1 PRI or E1 PRI trunks on a Cisco VG200 gateway.

Some fields display the values that were configured in Cisco Unified Communications Manager Administration.

In the BAT user interface, field names that have an asterisk
                                 		  require an entry. Consider an entry in fields without an asterisk as optional.

Field

Description

Device Information

Endpoint Name

For VG200 gateways, this display-only field contains a string
                                             					 that is generated by Cisco Unified Communications Manager that uniquely identifies the VG200 endpoint.

For example:

S1/DS1-0 @ VG200-2

S1 indicates slot 1, DS1-0 designates the digital interface,
                                             					 and @ VG200-2 designates the VG200 domain name.

Description

Enter a description for the end-point that you are
                                             					 configuring. The description can include up to 50 characters in any language,
                                             					 but it cannot include double-quotes ("), percentage sign
                                             					 ( % ), ampersand (&), back-slash
                                             					 ( \ ), or angle brackets (<>).

Device Pool

Choose the device pool for this group of
                                             					 gateways / ports.

A device pool defines sets of common characteristics for
                                             					 devices, such as region, date/time group, Cisco Unified Communications Manager group, and calling search space for
                                             					 auto-registration.

Call Classification

From the drop-down list box, choose an option to configure the
                                             					 device as on net, off net, or system default.

If you chose 'Use System Default' at the device level, the
                                             					 system uses the value of the service parameter to determine whether the device
                                             					 is internal (on net) or external (off net).

Network Locale

Choose the network locale that you want to associate with this
                                             					 gateway.

The Network Locale comprises a set of tones and cadences that
                                             					 Cisco gateways and phones use when communicating with the PSTN and other
                                             					 networks in a specific geographical area.

Media Resource Group List

Choose the media resource group list (MRGL) for this group of
                                             					 gateways/ports.

An MRGL specifies a list of prioritized media resource groups.
                                             					 An application can choose required media resources from among the available
                                             					 ones according to the priority order that is defined in the MRGL.

Location

Choose the location for this group of gateways/ports.

A location indicates the remote location that is accessed by
                                             					 using restricted bandwidth connections.

AAR Group

Choose the automated alternate routing (AAR) group for this
                                             					 device. The AAR group provides the prefix digits that are used to route calls
                                             					 that are otherwise blocked due to insufficient bandwidth. An AAR group setting
                                             					 of None specifies that no rerouting of blocked calls will be attempted.

Load Information

Enter the appropriate load information for the custom software
                                             					 for gateway. The values that you enter here override the default values for
                                             					 this gateway.

To use the default load, leave this field blank.

Transmit UTF-8 for Calling Party Name

This device uses the user locale setting of the device's
                                             					 device pool to determine whether to send Unicode and whether to translate
                                             					 received Unicode information.

For the sending device, if you check this check box and the
                                             					 user locale setting in the device's device pool matches the terminating phone's
                                             					 user locale, the device sends Unicode. If the user locale settings do not
                                             					 match, the device sends ASCII.

The receiving device translates incoming Unicode characters
                                             					 based on the user locale setting of the sending device's device pool. If the
                                             					 user locale setting matches the terminating phone's user locale, the phone
                                             					 displays the characters.

The phone may display junk characters if the two ends of the
                                             					 trunk configure user locales that do not belong to the same language group.

Multilevel Precedence and Preemption (MLPP)
                                                						Information

MLPP Domain (e.g., "0000FF" )

Enter a hexadecimal value for the MLPP domain that is
                                             					 associated with this device. Ensure that the value is blank or a value between
                                             					 0 and FFFFFF.

Interface Information

PRI Protocol Type

Choose the communications protocol for the span:

For E1 PRI spans, you have these options:

- PRI
                                                						AUSTRALIAN—Australian ISDN

- PRI EURO—European
                                                						ISDN

- PRI ISO QSIG
                                                						E1—European inter-PBX signaling protocol

For T1 PRI spans you have several options, depending on the
                                             					 carrier or switch:

- PRI 4ESS —AT&T
                                                						interexchange carrier, Lucent Definity switch

- PRI 5E8
                                                						Custom—CiscoUnifiedIPPhone, Nortel Meridian switch, Lucent Definity switches

- PRI 5E8
                                                						Teleos—Madge Teleos box

- PRI 5E8
                                                						Intecom—Intecom PBX

- PRI5E9—AT&T
                                                						family local exchange switch or carrier

- PRI NI2—Sprint
                                                						local exchange switch or carrier

- PRI DMS-100—Sprint
                                                						local exchange switch or carrier

- PRI DMS-250—MCI
                                                						and Sprint local exchange switch or carrier

- PRI ETSI
                                                						SC—European local exchange carrier on T1; also, Japanese local exchange.

- PRI ISO QSIG
                                                						T1—Inter-PBX signaling protocol

Protocol Side

Choose the appropriate protocol side. This setting specifies
                                             					 whether the gateway connects to a Central Office/Network device or to a User
                                             					 device.

Make sure that the two ends of the PRI connection use opposite
                                             					 settings. For example, if you connect to a PBX and the PBX uses User as its
                                             					 protocol side, choose Network for this device. Typically, use User for Central
                                             					 Office (CO) connections.

Channel Selection Order

Choose the order in which channels or ports are enabled from
                                             					 first (lowest number port) to last (highest number port) or from last to first.

Valid entries include TOP_DOWN (last to first) or BOTTOM_UP
                                             					 (first to last). If you are not sure which port order to use, choose TOP_DOWN.
                                             					 The default specifies BOTTOM_UP.

Channel IE Type

Choose one of the following values to specify whether channel
                                             					 selection is presented as a channel map or a slot map:

- Number—B-channel
                                                						usage always presents a channel map format.

- Slotmap—B-channel
                                                						usage always presents a slotmap format.

- Use Number When
                                                						1B—Channel usage presents a channel map for one B-channel but presents a
                                                						slotmap if more than one B-channel exists. This represents the default value.

PUnifiedCMType

Specify the digital encoding format. Choose one of the
                                             					 following formats:

- a-law: Use for
                                                						Europe and the rest of the world.

- mu-law: Use for
                                                						North America, HongKong, Taiwan, and Japan.

Delay for First Restart

For this optional field, enter the rate, in 1/8-second
                                             					 increments, at which the spans are brought in service. The delay occurs when
                                             					 many PRI spans are enabled on a system and the Inhibit Restarts at PRI
                                             					 Initialization check box is unchecked. The default value specifies 32.

For example, set the first five cards to 0 and set the next
                                             					 five cards to 16. (Wait 2 seconds before bringing them in service.)

Delay Between Restarts

Enter the time, in 1/8-second increments, between restarts.
                                             					 The delay occurs when a PRI RESTART is sent if the Inhibit Restarts check box
                                             					 is unchecked. The default value specifies 4.

Inhibit Restarts at PRI Initialization

A restart message confirms the status of the ports on a PRI
                                             					 span. If RESTARTS are not sent, Cisco Unified Communications Manager assumes that the ports are in service. By
                                             					 default, the box gets checked.

When the D-channel successfully connects with another PRI
                                             					 trunk D-channel, it sends restarts when this box is unchecked.

Enable Status Poll

Check the check box to enable the Cisco Unified Communications Manager advanced service parameter, Change B-Channel
                                             					 Maintenance Status. This service parameter allows you to take individual
                                             					 B-channels out of service while the B-channels are active.

Uncheck this check box to disable the service parameter Change
                                             					 B-Channel Maintenance Status.

Default leaves this field unchecked.

Unattended Ports

Check this check box to indicate an unattended port on this
                                             					 device.

Call Routing Information - Inbound Calls

Significant Digits

This field represents the number of final digits that a PRI
                                             					 span should retain on inbound calls. A trunk with significant digits enabled
                                             					 truncates all but the final few digits of the address that is provided on an
                                             					 inbound call.

Enable or disable this check box depending on whether you want
                                             					 to collect significant digits:

- If you do not
                                                						check the check box, Cisco Unified Communications Manager does not truncate the inbound number.

- If you check the
                                                						check box, you also need to choose the number of significant digits to collect.
                                                						By default, the box remains checked.

Calling Search Space

Choose the calling search space for this group of
                                             					 phones/ports.

A calling search space specifies the collection of Route
                                             					 Partitions that are searched to determine how a dialed number should be routed.

AAR Calling Search Space

Choose the appropriate calling search space for the device to
                                             					 use when it performs automated alternate routing (AAR). The AAR calling search
                                             					 space specifies the collection of route partitions that are searched to
                                             					 determine how to route a collected (originating) number that is otherwise
                                             					 blocked due to insufficient bandwidth.

Prefix DN

For this optional field, enter the prefix digits that are
                                             					 appended to the digits that this trunk receives on incoming calls.

Cisco Unified Communications Manager adds prefix digits after first
                                             					 truncating the number in accordance with the Num Digits setting.

Call Routing Information - Outbound
                                                						Calls

Calling Line ID Presentation

Choose whether you want the Cisco Unified Communications Manager to transmit or block the caller’s phone
                                             					 number.

Choose Default if you do not want to change calling line ID
                                             					 presentation. Choose Allowed if you want Cisco Unified Communications Manager to send "Calling Line ID Allowed." Choose Restricted if you want Cisco Unified Communications Manager to send "Calling Line ID Restricted."

Calling Party Selection

Any outbound call on a gateway can send directory number
                                             					 information. Choose which directory number is sent:

- Originator—Send
                                                						the directory number of the calling device. This number serves as the default
                                                						value.

- First Redirect
                                                						Number—Send the directory number of the redirecting device.

- Last Redirect
                                                						Number—Send the directory number of the last device that redirected the call.

Calling Party IE Number Type Unknown

Choose the format for the type of number in calling party
                                             					 directory numbers.

Cisco Unified Communications Manager sets the calling directory number (DN)
                                             					 type. Cisco recommends that you do not change the default value unless you have
                                             					 advanced experience with dialing plans, such as NANP or the European dialing
                                             					 plan. You may need to change the default in Europe because Cisco Unified Communications Manager does not recognize European national dialing
                                             					 patterns. You can also change this setting when you are connecting to PBXs that
                                             					 are using routing as a non-national type number.

Choose one of the following options:

- Communications
                                                						Manager—The Cisco Unified Communications Manager sets the directory number type. This
                                                						option represents the default value.

- International—Use
                                                						when you are dialing outside the dialing plan for your country.

- National—Use when
                                                						you are dialing within the dialing plan for your country.

- Unknown—This
                                                						option specifies that the dialing plan is unknown.

Called Party IE Number Type Unknown

Choose the format for the type of number in called party
                                             					 directory numbers. Cisco Unified Communications Manager sets the called directory number (DN) type.
                                             					 Cisco recommends that you do not change the default value unless you have
                                             					 extensive experience with dialing plans, such as NANP or the European dialing
                                             					 plan. You may need to change the default in Europe because Cisco Unified Communications Manager does not recognize European national dialing
                                             					 patterns. You can also change this setting when you are connecting to PBXs that
                                             					 use routing as a non-national type number.

Choose one of the following options:

- Communications
                                                						Manager—For the default setting, the Cisco Unified Communications Manager sets the directory number type.

- International—Use
                                                						when you are dialing outside the dialing plan for your country.

- National—Use when
                                                						you are dialing within the dialing plan for your country.

- Unknown—This
                                                						option specifies that the dialing plan is unknown.

Called Numbering Plan

Choose the format for the numbering plan in called party
                                             					 directory numbers.

Cisco Unified Communications Manager sets the called DN numbering plan.
                                             					 Cisco recommends that you do not change the default value unless you have
                                             					 extensive experience with dialing plans, such as NANP or the European dialing
                                             					 plan. You may need to change the default in Europe because Cisco Unified Communications Manager does not recognize European national dialing
                                             					 patterns. You can also change this setting when you are connecting to PBXs that
                                             					 are using routing as a non-national type number.

Choose one of the following options:

- Communications
                                                						Manager—For the default setting, the Cisco Unified Communications Manager sets the Numbering Plan in the
                                                						directory number.

- ISDN—Use when you
                                                						are dialing outside the dialing plan for your country.

- National
                                                						Standard—Use when you are dialing within the dialing plan for your country.

- Private—Use when
                                                						you are dialing within a private network.

- Unknown—This
                                                						option specifies that the dialing plan is unknown.

Calling Numbering Plan

Choose the format for the numbering plan in calling party
                                             					 directory numbers.

Cisco Unified Communications Manager sets the calling DN numbering plan.
                                             					 Cisco recommends that you do not change the default value unless you have
                                             					 extensive experience with dialing plans, such as NANP or the European dialing
                                             					 plan. You may need to change the default in Europe because Cisco Unified Communications Manager does not recognize European national dialing
                                             					 patterns. You can also change this setting when you are connecting to PBXs that
                                             					 are using routing as a non-national type number.

Choose one of the following options:

- Communications
                                                						Manager—For the default setting, the Cisco Unified Communications Manager sets the Numbering Plan in the
                                                						directory number.

- ISDN—Use when you
                                                						are dialing outside the dialing plan for your country.

- National
                                                						Standard—Use when you are dialing within the dialing plan for your country.

- Private—Use when
                                                						you are dialing within a private network.

- Unknown—This
                                                						option specifies that the dialing plan is unknown.

Number of Digits to Strip

Choose the number of digits, from 0 to 32, to strip on
                                             					 outbound calls. The default value specifies 0.

For example, 8889725551234 is dialed; the number of digits to
                                             					 strip is 3. In this example, Cisco Unified Communications Manager strips 888 from the outbound number.

Caller ID DN

Enter the pattern, from 0 to 24 digits, that you want to use
                                             					 for caller ID.

For example, in North America

- 555XXXX = Variable
                                                						caller ID, where X equals an extension number. The CO appends the number with
                                                						the area code if you do not specify it.

- 5555000 = Fixed
                                                						caller ID, for when you want the Corporate number to be sent instead of the
                                                						exact extension from which the call is placed. The CO appends the number with
                                                						the area code if you do not specify it.

SMDI Base Port

Enter the first SMDI port number of the T1 span.

PRI Protocol Type Specific Information

Display IE Delivery

For this optional field, check the check box to enable
                                             					 delivery of the display information element (IE) in SETUP and CONNECT messages
                                             					 for the calling and called party name delivery service. By default, the box
                                             					 remains unchecked.

Redirecting Number IE Delivery—Outbound

For this optional field, check the check box to include the
                                             					 Redirecting Number IE in the SETUP message to indicate the first redirecting
                                             					 number and the redirecting reason of the call when a call is forwarded. By
                                             					 default, the box remains unchecked.

This setting applies to the SETUP message only on all
                                             					 protocols for digital access gateways.

Redirecting Number IE Delivery—Inbound

For this optional field, check the check box to include the
                                             					 Redirecting Number IE in the SETUP message to indicate the first redirecting
                                             					 number and the redirecting reason of the call when a call is forwarded. By
                                             					 default, the box remains unchecked.

This setting applies to the SETUP message only on all
                                             					 protocols for digital access gateways.

Send Extra Leading Character in Display IE

Check this check box to include a special leading character
                                             					 byte (non ASCII, nondisplayable) in the DisplayIE field.

Uncheck this check box to exclude this character byte from the
                                             					 DisplayIE field.

This check box only applies to the DMS-100 protocol and the
                                             					 DMS-250 protocol.

Default leaves this setting disabled (unchecked).

Setup of Non-ISDN Progress Indicator IE Enable

For this optional field, you may need to specify a value in
                                             					 this field to force ringback on some PBXs.

The default specifies unchecked. Check this check box only if
                                             					 users are not receiving ringback tones on outbound calls.

When this setting is enabled, Cisco Unified Communications Manager sends Q.931 setup messages out digital (that
                                             					 is, non-H.323) gateways with the Progress Indicator field set to non-ISDN.

This message notifies the destination device that the Cisco Unified Communications Manager gateway is non-ISDN and that the destination
                                             					 device should play inband ringback.

This problem usually associates with Cisco Unified Communications Manager s that connect to PBXs through digital
                                             					 gateways.

MCDN Channel Number Extension Bit Set to Zero

This field applies to DMS-100 protocol only. Check the check
                                             					 box to indicate that an Interface Identifier is present. By default, the box
                                             					 remains unchecked.

Send Calling Name in Facility IE

This field applies to DMS-100 protocol only. Enter the value
                                             					 that you obtained from the PBX provider. Valid values range from 0 to 255.

Interface Identifier Present

This field applies to DMS-100 protocol only. Check the check
                                             					 box to indicate that an Interface Identifier is present. By default, the box
                                             					 remains unchecked.

Interface Identifier Value

This field applies to DMS-100 protocol only. Enter the value
                                             					 that you obtained from the PBX provider. Valid values range from 0 to 255.

Connected Line ID Presentation

Choose whether you want the Cisco Unified Communications Manager to allow or block the connected party’s phone
                                             					 number.

Choose Default if you do not want to change the connected line
                                             					 ID presentation. Choose Allowed if you want Cisco Unified Communications Manager to send "Connected Line ID Allowed." Choose Restricted if you want Cisco Unified Communications Manager to send "Connected Line ID Restricted."

UUIE Configuration

Passing Precedence Level Through UUIE

Check this check box to enable passing MLPP information
                                             					 through the PRI 4ESS UUIE field. This box is used for working along with DRSN
                                             					 switch.

The system makes this check box available only if the PRI
                                             					 Protocol Type value of PRI4ESS is specified for this gateway.

The default value specifies unchecked.

Security Access Level

Enter the value for the security access level. Valid values
                                             					 include 00 through 99. The system makes this field available only if the
                                             					 Passing Precedence Level Through UUIE check box is checked. The default value
                                             					 specifies 2.

Geo Location Configuration

Geo Location

From the drop-down list box, choose a geo location.

You can choose the Unspecified geo location, which designates
                                             					 that this device does not associate with a geo location.

You can also choose a geolocation that has been configured
                                             					 with the System > Geolocation
                                                   						  Configuration menu option.

Geo Location Filter

From the drop-down list box, choose a geo location filter.

If you leave the <None> setting, no geo location filter
                                             					 gets applied for this device.

You can also choose a geo location filter that has been
                                             					 configured with the System > Geolocation
                                                   						  Configuration Filter menu option.

Product-Specific Configuration

The gateway manufacturer specifies the model-specific fields
                                             					 under product-specific configuration. To view field descriptions and help for
                                             					 product-specific configuration items, click the "?" information icon to the right of the Product Specific
                                             					 Configuration heading to display help in a popup window. If you need more
                                             					 information, refer to the documentation for the specific gateway that you are
                                             					 configuring.

## Port Configuration Settings

Detailed field descriptions are available for all port types
                           		and Cisco-supported gateway configuration settings.

### POTS Port Configuration Settings

The following table describes the POTS port configuration
                                 		  settings.

Field

Description

Port Type

From the Port Type drop-down list box, choose
                                             					 POTS.

Beginning Port Number

Ending Port Number

Choose whether you want to add and configure all available
                                             					 ports, a single port, or a range of ports by setting values for the Beginning
                                             					 Port Number and Ending Port Number fields:

- To specify a range
                                                						of ports, choose appropriate values for Beginning Port Number and Ending Port
                                                						Number.

- To create a single
                                                						port, choose the same number in the Beginning Port Number and Ending Port
                                                						Number fields.

- To add all
                                                						available ports, choose All Ports for both the Beginning Port Number and Ending
                                                						Port Number fields.

Port Direction

Choose the direction of calls that pass through this port:

- Inbound—Use for
                                                						incoming calls only.

- Outbound—Use for
                                                						outgoing calls.

- Bothways—Use for
                                                						inbound and outbound calls (default).

Audio Signal Adjustment into IP Network

This field specifies the gain or loss that is applied to the
                                             					 received audio signal relative to the port application type.

Improper gain setting may cause audio echo. Use caution when
                                                         						you are adjusting this setting.

Audio Signal Adjustment from IP Network

This field specifies the gain or loss that is applied to the
                                             					 transmitted audio signal relative to the port application type.

Improper gain setting may cause audio echo. Use caution when
                                                         						you are adjusting this setting.

Prefix DN

Enter the prefix digits that are appended to the digits that
                                             					 this trunk receives on incoming calls.

The Cisco Unified Communications Manager adds prefix digits after it truncates the
                                             					 number in accordance with the Num Digits setting.

Num Digits

Enter the number of significant digits to collect, from 0 to
                                             					 32.

Cisco Unified Communications Manager counts significant digits from the
                                             					 right (last digit) of the number that is called.

Use this field for the processing of incoming calls and to
                                             					 indicate the number of digits starting from the last digit of the called number
                                             					 that are used to route calls that are coming into the PRI span. See Prefix DN.

Expected Digits

Enter the number of digits that are expected on the inbound
                                             					 side of the trunk. For this rarely used field, leave zero as the default value
                                             					 if you are unsure.

Call Restart Timer (1000-5000 ms)

Call Restart Timer (1000-5000 ms); ms indicates time in
                                             					 milliseconds.

Offhook Validation Timer (100-1000 ms)

Offhook Validation Timer (100-1000 ms); ms indicates time in
                                             					 milliseconds.

Onhook Validation Timer (100-1000 ms)

Onhook Validation Timer (100-1000 ms); ms indicates time in
                                             					 milliseconds.

Hookflash Timer (100-1500 ms)

Hookflash Timer (100-1500 ms); ms indicates time in
                                             					 milliseconds.

SMDI Port Number (0-4096)

Use this field for analog access ports that connect to a
                                             					 voice-messaging system.

Set the SMDI Port Number equal to the actual port number on
                                             					 the voice-messaging system to which the analog access port connects.

Voice-mail logical ports typically must match physical ports
                                                         						for the voice-messaging system to operate correctly.

Product-Specific Configuration

Model-specific configuration fields that the gateway
                                             					 manufacturer defines

The gateway manufacturer specifies the model-specific fields
                                             					 under product-specific configuration. Because they are dynamically configured,
                                             					 they can change without notice.

To view field descriptions and help for product-specific
                                             					 configuration items, click the "?" information icon to the right of the Product Specific
                                             					 Configuration heading to display help in a popup dialog box.

If you need more information, refer to the documentation for
                                             					 the specific gateway that you are configuring or contact the manufacturer.

### E and M Ports for Digital Access T1 Field Descriptions

Use the following field descriptions when you are adding or
                                 		  updating values for E&M ports for the T1 CAS trunks on a Cisco VG200
                                 		  gateway.

Some fields display the values that were configured in Cisco Unified Communications Manager Administration.

In the BAT user interface, field names that have an
                                 		  asterisk require an entry. Consider an entry in fields without an asterisk as
                                 		  optional.

The following table describes the E & M port
                                 		  configuration settings.

Field

Description

Port Type

From the Port Type drop-down list box, choose EANDM.

Beginning Port Number

Ending Port Number

Choose whether you want to add and configure all available
                                             					 ports, a single port, or a range of ports by setting values for the Beginning
                                             					 Port Number and Ending Port Number fields:

- To specify a range
                                                						of ports, choose appropriate values for Beginning Port Number and Ending Port
                                                						Number.

- To create a single
                                                						port, choose the same number in the Beginning Port Number and Ending Port
                                                						Number fields.

- To add all
                                                						available ports, choose All Ports for both the Beginning Port Number and Ending
                                                						Port Number fields.

Port Details

Port Direction

Choose the direction of calls that pass through this port:

- Inbound—Use for
                                                						incoming calls only.

- Outbound—Use for
                                                						outgoing calls.

- Both Ways—Use for
                                                						inbound and outbound calls.

Calling Party Selection

Any outbound call on a gateway can send directory number
                                             					 information. Choose which directory number is sent:

- Originator—Send
                                                						the directory number of the calling device.

- First Redirect
                                                						Number—Send the directory number of the redirecting device.

- Last Redirect
                                                						Number—Send the directory number of the last device to redirect the call.

- First Redirect
                                                						Number (External)—Send the directory number of the first redirecting device
                                                						with the external phone mask applied.

- Last Redirect
                                                						Number (External)—Send the directory number of the last redirecting device with
                                                						the external phone mask applied.

Caller ID Type

Choose the caller ID type:

- ANI—Choose this
                                                						type to use the Asynchronous Network Interface (ANI) caller ID type.

- DNIS—Choose this
                                                						type to use the Dialed Number Identification Service (DNIS) caller ID type.

Caller ID DN

Enter the pattern that you want to use for calling line ID,
                                             					 from 0 to 24 digits.

For example, in North America:

- 555XXXX = Variable
                                                						calling line ID, where X equals an extension number. The CO appends the number
                                                						with the area code if you do not specify it.

- 5555000 = Fixed
                                                						calling line ID, where you want the Corporate number to be sent instead of the
                                                						exact extension from which the call is placed. The CO appends the number with
                                                						the area code if you do not specify it.

Prefix DN

Enter the prefix digits that are appended to the called party
                                             					 number on incoming calls.

The Cisco Unified Communications Manager adds prefix digits after first truncating the
                                             					 number in accordance with the Num Digits setting.

Num Digits

Choose the number of significant digits to collect, from 0 to
                                             					 32. Cisco Unified Communications Manager counts significant digits from the right (last
                                             					 digit) of the number that is called.

Use this field if you check the Sig Digits check box. Use this
                                             					 field for the processing of incoming calls and to indicate the number of digits
                                             					 starting from the last digit of the called number that are used to route calls
                                             					 that are coming into the PRI span. See Prefix DN and Sig Digits.

Expected Digits

Enter the number of digits that are expected on the inbound
                                             					 side of the trunk. If you are unsure, leave zero as the default value for this
                                             					 rarely used field.

Unattended Port

Check this check box to indicate an unattended port on this
                                             					 device.

Product-Specific Configuration

Model-specific configuration fields that the gateway
                                             					 manufacturer defines

The gateway manufacturer specifies the model-specific fields
                                             					 under product-specific configuration. Because they are dynamically configured,
                                             					 they can change without notice.

To view field descriptions and help for product-specific
                                             					 configuration items, click the "?" information icon to the right of the Product Specific
                                             					 Configuration heading to display help in a popup dialog box.

If you need more information, refer to the documentation for
                                             					 the specific gateway that you are configuring or contact the manufacturer.

## Topics Related to Gateway Configuration Settings

| Step 1 | Create a Cisco VG200 gateway template to define common values for a set of gateways and ports. See the Create Cisco VG200 Gateway Template . |
|---|---|
| Step 2 | Create a CSV data file to define individual values for each gateway and port that you want to add. See the CSV Data File Creation for Cisco VG200 Gateways . |
| Step 3 | Insert gateways and ports in the Cisco Unified Communications Manager database. See the Insert Gateways and Ports to Cisco Unified Communications Manager . |

| Step 1 | Create a Cisco Catalyst 6000 (FXS) gateway template. See the Create Cisco Catalyst 6000 (FXS) Gateway Template . |
|---|---|
| Step 2 | To define common values for a set of FXS ports, create a Cisco Catalyst 6000 (FXS) ports template. See the FXS/FXO Port Configuration Field Descriptions . |
| Step 3 | To define individual values for the FXS ports that you want to add, create a CSV data file. See the Create CSV Data File for Cisco Catalyst 6000 (FXS) Ports . |
| Step 4 | Insert gateways and ports in the Cisco Unified Communications Manager database. See the Insert Gateways and Ports to Cisco Unified Communications Manager . |

| Step 1 | Create a Cisco VG224 gateway template to define common values for a set of gateways and ports. See the Create Cisco VG224 Gateway Template . |
|---|---|
| Step 2 | Create a CSV data file to define individual values for each gateway and port that you want to add. See the CSV Data Files Creation for Cisco VG224 Gateways and Ports . |
| Step 3 | Insert gateways and ports in the Cisco Unified Communications Manager database. See the Insert Gateways and Ports to Cisco Unified Communications Manager . |

| Step 1 | Create a Cisco gateway template to define common values for a set of gateways and ports. See the Create Cisco VG202 or VG204 Gateway Template . |
|---|---|
| Step 2 | Create a CSV data file to define individual values for each gateway and port that you want to add. See the CSV Data File Creation for Cisco VG202 and VG204 Gateways . |
| Step 3 | Insert gateways and ports in the Cisco Unified Communications Manager database. See the Insert Gateways and Ports to Cisco Unified Communications Manager . |

| Step 1 | Create a Cisco VG310 gateway template to define common values for a set of gateways and ports. See Create Cisco VG310 Gateway Template . |
|---|---|
| Step 2 | Create a CSV data file to define individual values for each gateway and port that you want to add. See CSV Data Files Creation for Cisco VG310 Gateways and Ports . |
| Step 3 | Insert gateways and ports in the Unified Communications Manager database. See Insert Gateways and Ports to Cisco Unified Communications Manager . |

| Step 1 | Create a Cisco VG320 gateway template to define common values for a set of gateways and ports. See Create Cisco VG320 Gateway Template . |
|---|---|
| Step 2 | Create a CSV data file to define individual values for each gateway and port that you want to add. See CSV Data Files Creation for Cisco VG320 Gateways and Ports . |
| Step 3 | Insert gateways and ports in the Unified Communications Manager database. See Insert Gateways and Ports to Cisco Unified Communications Manager . |

| Step 1 | Create a Cisco VG350 gateway template to define common values for a set of gateways and ports. See Create Cisco VG350 Gateway Template . |
|---|---|
| Step 2 | Create a CSV data file to define individual values for each gateway and port that you want to add. See CSV Data Files Creation for Cisco VG350 Gateways and Ports . |
| Step 3 | Insert gateways and ports in the Unified Communications Manager database. See Insert Gateways and Ports to Cisco Unified Communications Manager . |

| Important | Supported from Release 12.5(1)SU4 and 14SU1 onwards. |
|---|---|

| Step 1 | Create a Cisco VG420 gateway template to define common values for a set of gateways and ports. See Create Cisco VG420 Gateway Template . |
|---|---|
| Step 2 | Create a CSV data file to define individual values for each gateway and port that you want to add. See Create CSV Data Files for Cisco VG420 Gateways Using BAT Spreadsheet . |
| Step 3 | Insert gateways and ports in the Unified Communications Manager database. See Insert Gateways and Ports to Cisco Unified Communications Manager . |

| Step 1 | Create a Cisco VG450 gateway template to define common values for a set of gateways and ports. See Create Cisco VG450 Gateway Template . |
|---|---|
| Step 2 | Create a CSV data file to define individual values for each gateway and port that you want to add. See CSV Data Files Creation for Cisco VG450 Gateways and Ports . |
| Step 3 | Insert gateways and ports in the Unified Communications Manager database. See Insert Gateways and Ports to Cisco Unified Communications Manager . |

| Step 1 | Create a Cisco ISR 4461 gateway template to define common values for a set of gateways and ports. See Create Cisco ISR 4461 Gateway Template . |
|---|---|
| Step 2 | Create a CSV data file to define individual values for each gateway and port that you want to add. See CSV Data File Creation for Cisco ISR 4461 Gateways . |
| Step 3 | Insert gateways and ports in the Cisco Unified Communications Manager database. See Insert Gateways and Ports to Cisco Unified Communications Manager . |

| Note | During your work in a browser session, your find/list search
                                          			 preferences get stored in the cookies on the client machine. If you navigate to
                                          			 other menu items and return to this menu item, or if you close the browser and
                                          			 then reopen a new browser window, your Cisco Unified Communications Manager search preferences get retained until you
                                          			 modify your search. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Gateways > Gateway
                                             				  Template . The Find and List Gateway Template window displays. |
|---|---|
| Step 2 | From the first Find Gateways where drop-down list, choose one of the following criteria: Name Description DN/Route Pattern Calling Search Space Device Pool Route Group Name Device Type |
| Step 3 | From the second Find Gateways where drop-down list, choose one of the following criteria: begins with contains is exactly ends with is empty is not empty |
| Step 4 | Specify the appropriate search text, if applicable. Tip To find all gateways that are registered in the database, click Find without entering any search text. | Tip | To find all gateways that are registered in the database, click Find without entering any search text. |
| Tip | To find all gateways that are registered in the database, click Find without entering any search text. |
| Step 5 | Choose Show from the third drop-down list to show the end points that are associated with gateways, and click Find . A list of discovered templates displays by Device Name Description Device Pool Status IP Address |
| Step 6 | From the list of records, click the device name that matches your
                                       			 search criteria. The Gateway Configuration window displays. |

| Tip | To find all gateways that are registered in the database, click Find without entering any search text. |
|---|---|

| Step 1 | Choose Bulk Administration > Gateways > Gateway Template . The Find and List Gateway Template window displays. |
|---|---|
| Step 2 | Complete one of the following procedures: To create a VG200 template, see the Create Cisco VG200 Gateway Template . To create CiscoCatalyst 6000 (FXS) Ports template, see Create Cisco Catalyst 6000 (FXS) Gateway Template . To create a VG224 template, see the Create Cisco VG224 Gateway Template . To create a VG202 or VG204 template, see the Create Cisco VG202 or VG204 Gateway Template . To create a Cisco VG310 template, see the Create Cisco VG310 Gateway Template . To create a Cisco VG320 template, see the Create Cisco VG320 Gateway Template . To create a Cisco VG350 template, see the Create Cisco VG350 Gateway Template . To create a Cisco VG420 template, see the Create Cisco VG420 Gateway Template . To create a Cisco VG450 template, see the Create Cisco VG450 Gateway Template To create a Cisco ISR 4461 template, see the Create Cisco ISR 4461 Gateway Template . |

| Step 1 | Choose Bulk
                                                				  Administration > Gateways > Gateway
                                                				  Template . The Find and List Gateway window displays. |
|---|---|
| Step 2 | Click Add New . The Add a New Gateway Template window displays. |
| Step 3 | From the Gateway Type drop-down list, select Cisco VG200 and click Next . The Gateway Template Configuration window displays. |
| Step 4 | Enter values for all the fields. See VG200 Gateway Template Field Descriptions . |
| Step 5 | Click Save . When the insert completes, a new field displays on the
                                          			 pane. |
| Step 6 | In the Subunit field(s), choose the appropriate type for each subunit field: VIC-2FXS—Foreign Exchange Station (FXS) voice interface card VIC-2FXO—Foreign Exchange Office (FXO) voice interface card VWIC-1MFT-T1—Voice WAN interface card with one endpoint for T1CAS or T1 PRI VWIC-2MFT-T1—Voice WAN interface card with two endpoints for T1 CAS or T1 PRI VWIC-1MFT-E1—Voice WAN interface card with one endpoint for E1 PRI VWIC-2MFT-E1—Voice WAN interface card with two endpoints for E1 PRI |
| Step 7 | Click Save. When the Status indicates that the update completed, the endpoint identifiers display as links to the right of the subunit
                                          drop-down list. |
| Step 8 | Click an endpoint identifier (for example, 1/0/0) to configure
                                          			 device protocol information and add ports for the installed types of VICs. |
| Step 9 | Click Reset to reset the gateway and apply the changes. |

| Step 1 | Find the gateway template to which you want to add FXS ports. |
|---|---|
| Step 2 | From the Gateway Template Configuration window, click
                                             			 the endpoint identifier for the FXS VIC that you want to configure. The window refreshes and displays the Gateway Template Configuration window with the
                                             			 end-point icons. |
| Step 3 | Enter the appropriate Gateway Information and Port Information
                                             			 settings, and click Save . See the following for field descriptions: FXS/FXO Port Configuration Field Descriptions POTS Port Configuration Settings Note After you insert a POTS port, the window refreshes and displays the POTS port information at the bottom of the window. An Add a new DN link displays in the Directory Number Information area in the left panel. | Note | After you insert a POTS port, the window refreshes and displays the POTS port information at the bottom of the window. An Add a new DN link displays in the Directory Number Information area in the left panel. |
| Note | After you insert a POTS port, the window refreshes and displays the POTS port information at the bottom of the window. An Add a new DN link displays in the Directory Number Information area in the left panel. |
| Step 4 | Click Add a new DN to add directory numbers to the
                                             			 POTS port or, if you configured another type of port, go to Step 6 . |
| Step 5 | Choose Back to MGCP Configuration in the Related Links drop-down list to return to the main VG200 Gateway Template Configuration window for the gateway to which you just added the ports and click Go . |
| Step 6 | Click Reset to reset the gateway and apply the changes. |
| Step 7 | Repeat Step 1 through Step 5 to add additional FXS ports. |

| Note | After you insert a POTS port, the window refreshes and displays the POTS port information at the bottom of the window. An Add a new DN link displays in the Directory Number Information area in the left panel. |
|---|---|

| Note | Cisco Unified Communications Manager assumes all loop-start trunks lack positive disconnect supervision. Configure trunks
                                             with positive disconnect supervision as ground start, so active calls can be maintained during a Cisco Unified Communications
                                             Manager server failover. |
|---|---|

| Step 1 | Find the gateway template to which you want to add FXS ports. |
|---|---|
| Step 2 | From the Gateway Configuration window, click the endpoint
                                             			 identifiers of the FXO port that you want to configure. |
| Step 3 | From the Port Type drop-down list, choose either Ground Start or Loop Start . Note You must choose the same port type for both endpoint identifiers of the VIC-2FXO port. If you choose different port types,
                                                         a message displays. | Note | You must choose the same port type for both endpoint identifiers of the VIC-2FXO port. If you choose different port types,
                                                         a message displays. |
| Note | You must choose the same port type for both endpoint identifiers of the VIC-2FXO port. If you choose different port types,
                                                         a message displays. |
| Step 4 | Enter the appropriate Gateway Configuration and Port Information
                                             			 settings, and click Save . See FXS/FXO Port Configuration Field Descriptions for field descriptions. |
| Step 5 | Choose Back to MGCP Configuration in the Related Links drop-down list to return to the main VG200 gateway configuration window for the gateway to which you just added the ports
                                             and click Go . |
| Step 6 | Click Reset to reset the gateway and apply the changes. |
| Step 7 | To add more FXO ports, repeat Step 2 through Step 4 . |

| Note | You must choose the same port type for both endpoint identifiers of the VIC-2FXO port. If you choose different port types,
                                                         a message displays. |
|---|---|

| Step 1 | Find the gateway template to which you want to add FXS ports. |
|---|---|
| Step 2 | From the Gateway Configuration window, click the endpoint
                                             			 identifier of the Digital Access T1 (T1-CAS) port that you want to configure. In the Device Protocol drop-down list box that
                                                				displays, choose Digital Access T1 and click Next . |
| Step 3 | Enter the appropriate Gateway Configuration settings, and click Save . See the Digital Access T1 Trunks on Cisco VG200 Gateway Template Field Descriptions for details. |
| Step 4 | To reset the gateway and apply the changes, click Reset . |
| Step 5 | See the Port Configuration Settings for the
                                             			 appropriate settings for the port type that you choose. |

| Step 1 | Find the gateway template to which you want to add FXS ports. |
|---|---|
| Step 2 | From the Gateway Configuration window, click the endpoint
                                             			 identifier of the T1 PRI or E1 PRI port that you want to configure. |
| Step 3 | Configure the T1 PRI or E1 PRI device protocol settings. See T1 PRI or E1 PRI Trunks on Cisco VG200 Gateway Template Field Descriptions for field descriptions. |
| Step 4 | Click Save . |
| Step 5 | Click Reset to reset the gateway and apply the changes. |

| Step 1 | Choose Bulk
                                                				  Administration > Gateways > Gateway
                                                				  Template . The Find and List Gateway window displays. |
|---|---|
| Step 2 | Click Add New . The Add a New Gateway Template window displays. |
| Step 3 | From the Gateway Type drop-down list, choose Cisco Catalyst 6000 24 Port FXS Gateway and click Next . The Gateway Template Configuration window displays. |
| Step 4 | Enter a unique name for the template in the Template Name field. |
| Step 5 | Enter the settings for the fields, and click Save . See Cisco Catalyst 6000 24 Port FXS Gateway Template Field Descriptions for field descriptions. |
| Step 6 | Click Add a New Port . A port configuration dialog opens in a separate window. |
| Step 7 | From the drop-down list, choose POTS as the port type depending on the gateway model that you are configuring. See T1 PRI or E1 PRI Trunks on Cisco VG200 Gateway Template Field Descriptions for field descriptions. |
| Step 8 | Enter the appropriate port configuration settings, and click Save . See POTS Port Configuration Settings for
                                          			 field descriptions. If you have inserted POTS ports, the window refreshes and
                                          			 displays the POTS port in the list on the left side of the window. An Add DN
                                          			 link displays to the right of the new port. |
| Step 9 | To add a directory numbers to an FXS port, click Add DN . |
| Step 10 | Click Save . When the Status indicates that the update completed, the template displays on the Find and List Gateways window. To go back to the Find and List window, choose Back to Find and List from the Related Links drop-down list in the top, right corner of the window. |

| Step 1 | Choose Bulk
                                                				  Administration > Gateways > Gateway
                                                				  Template . The Find and List Gateway window displays. |
|---|---|
| Step 2 | Click Add New . The Add a New Gateway Template window displays. |
| Step 3 | From the Gateway Type drop-down list, choose VG224 and click Next . The Add a New Gateway Template window displays. |
| Step 4 | From the Protocol drop-down list, choose MGCP or SCCP and click Next . The Gateway Template Configuration window displays. |
| Step 5 | Enter values for all the fields, and click Save . See VG224 Gateway Template Field Descriptions for field descriptions. When the insert completes, a new field displays on the pane. |
| Step 6 | In the Subunit 0 field, choose the appropriate type for the subunit field from the drop-down list, and click Save . VIC-2FXS—Foreign Exchange Station (FXS) voice interface card. When the Status indicates that the update completed, the endpoint identifiers display as links to the right of the subunit
                                          drop-down list. |
| Step 7 | Click an endpoint identifier (for example, 1/0/0) to configure
                                          			 device protocol information and add ports for the installed types of VICs. |
| Step 8 | Click Reset to reset the gateway and apply the changes. |

| Step 1 | Find the gateway template to which you want to add FXS ports. |
|---|---|
| Step 2 | From the Gateway Template Configuration window, click the endpoint identifier for the FXS VIC that you want to configure. The window refreshes and displays the Gateway Template Configuration window with the endpoint icons. |
| Step 3 | Enter the appropriate Gateway Information and Port Information settings, and click Save . See the following for field descriptions: FXS/FXO Port Configuration Field Descriptions POTS Port Configuration Settings Note After you insert a POTS port, the window refreshes and displays the POTS port information at the bottom of the window. An Add a new DN link displays in the Directory Number Information area in the left panel. | Note | After you insert a POTS port, the window refreshes and displays the POTS port information at the bottom of the window. An Add a new DN link displays in the Directory Number Information area in the left panel. |
| Note | After you insert a POTS port, the window refreshes and displays the POTS port information at the bottom of the window. An Add a new DN link displays in the Directory Number Information area in the left panel. |
| Step 4 | Click Add a new DN to add directory numbers to the
                                          			 POTS port or, if you configured another type of port, go to 6 . |
| Step 5 | To return to the main VG224 Gateway Template Configuration window for the gateway to which you just added the ports, select Back to MGCP Configuration in the Related Links drop-down list and click Go . |
| Step 6 | Click Reset to reset the gateway and apply the changes. |
| Step 7 | Repeat 1 through 5 to add additional FXS ports. |

| Note | After you insert a POTS port, the window refreshes and displays the POTS port information at the bottom of the window. An Add a new DN link displays in the Directory Number Information area in the left panel. |
|---|---|

| Step 1 | Choose Bulk
                                                				  Administration > Gateways > Gateway
                                                				  Template . The Find and List Gateway window displays. |
|---|---|
| Step 2 | Click Add New . The Add a New Gateway Template window displays. |
| Step 3 | From the Gateway Type drop-down list, choose VG202 or VG204 and click Next . The Add a New Gateway Template window displays. |
| Step 4 | From the Protocol drop-down list, choose MGCP or SCCP and click Next . The Gateway Template Configuration window displays. |
| Step 5 | Enter values for all the fields, and click Save . See VG202 and VG204 Gateway Template Field Descriptions for field descriptions. When the insert completes, a new Subunit 0 field displays on the pane. |
| Step 6 | In the Subunit 0 field, choose the appropriate type
                                          			 for the subunit field from the drop-down list box, and click Save . When the Status indicates that the update completed, the
                                          			 endpoint identifiers display as links to the right of the subunit drop-down
                                          			 list boxes. |
| Step 7 | Click an endpoint identifier (for example, 0/0) to configure
                                          			 device protocol information and add ports for the installed types of VICs. |
| Step 8 | Click Reset to reset the gateway and apply the changes. |

| Step 1 | Find the gateway template to which you want to add FXS ports. |
|---|---|
| Step 2 | From the Gateway Template Configuration window, click the
                                          			 endpoint identifier for the FXS VIC that you want to configure. The window refreshes and displays the Gateway Template Configuration window with the
                                          			 endpoint icons. |
| Step 3 | Enter the appropriate Gateway Information and Port Information settings and click Save . See the following for field descriptions: FXS/FXO Port Configuration Field Descriptions POTS Port Configuration Settings Note After you insert a POTS port, the window refreshes and displays the POTS port information at the bottom of the window. An Add a new DN link displays in the Directory Number Information area in the left panel. | Note | After you insert a POTS port, the window refreshes and displays the POTS port information at the bottom of the window. An Add a new DN link displays in the Directory Number Information area in the left panel. |
| Note | After you insert a POTS port, the window refreshes and displays the POTS port information at the bottom of the window. An Add a new DN link displays in the Directory Number Information area in the left panel. |
| Step 4 | Click Add a new DN to add directory numbers to the
                                          			 POTS port or, if you configured another type of port, go to Step 6 . |
| Step 5 | To return to the main VG202 or VG204 Gateway Template Configuration window for the gateway to which you just added the ports, choose Back to MGCP Configuration in the Related Links drop-down list and click Go (if you configuring an MGCP gateway). |
| Step 6 | Click Reset to reset the gateway and apply the changes. |
| Step 7 | Repeat Step 2 through Step 5 to add additional FXS ports. |

| Note | After you insert a POTS port, the window refreshes and displays the POTS port information at the bottom of the window. An Add a new DN link displays in the Directory Number Information area in the left panel. |
|---|---|

| Step 1 | Choose Bulk Administration > Gateways > Gateway Template . The Find and List Gateway window displays. |
|---|---|
| Step 2 | Click Add New . The Add a New Gateway Template window displays. |
| Step 3 | From the Gateway Type drop-down list, choose VG310 and click Next . The Gateway Template Configuration window displays. |
| Step 4 | From the Protocol drop-down list, choose MGCP or SCCP and click Next . The Gateway Template Configuration window displays. |
| Step 5 | Enter a unique name for this template in the Template Name field. |
| Step 6 | Enter values for all the fields, and click Save . See VG310 Gateway Template Field Description for field descriptions. |

| Step 1 | Choose Bulk Administration > Gateways > Gateway Template . The Find and List Gateway window displays. |
|---|---|
| Step 2 | Click Add New . The Add a New Gateway Template window displays. |
| Step 3 | From the Gateway Type drop-down list, choose VG320 and click Next . The Gateway Configuration window displays. |
| Step 4 | From the Protocol drop-down list, choose MGCP or SCCP and click Next . The Gateway Template Configuration window displays. |
| Step 5 | Enter a unique name for the template in the Template Name field. |
| Step 6 | Enter values for all the fields, and click Save . See VG320 Gateway Template Field Description for field descriptions. |

| Step 1 | Choose Bulk Administration > Gateways > Gateway Template . The Find and List Gateway window displays. |
|---|---|
| Step 2 | Click Add New . The Add a New Gateway Template window displays. |
| Step 3 | From the Gateway Type drop-down, choose VG350 and click Next . |
| Step 4 | From the Protocol drop-down list, choose MGCP or SCCP , and click Next . The Gateway Template Configuration window displays. |
| Step 5 | Enter a unique name for the template in the Template Name field. |
| Step 6 | Enter values for all the fields, and click Save . See VG350 Gateway Template Field Description for field descriptions. |

| Step 1 | Choose Bulk Administration > Gateways > Gateway Template . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Gateway Type drop-down list, choose VG420 and click Next . |
| Step 4 | From the Protocol drop-down list, choose SIP , SCCP or MGCP and click Next . |
| Step 5 | Enter a unique name for the template in the Template Name field. |
| Step 6 | Enter values for all the fields, and click Save . See VG420 Gateway Template Field Descriptions for field descriptions. |

| Step 1 | Choose Bulk Administration > Gateways > Gateway Template . The Find and List Gateway window displays. |
|---|---|
| Step 2 | Click Add New . The Add a new Gateway Template window displays. |
| Step 3 | From the Gateway Type drop-down list, choose VG450 and click Next . |
| Step 4 | From the Protocol drop-down list, choose SIP , MGCP or SCCP and click Next . The Gateway Template Configuration window displays. |
| Step 5 | Enter a unique name for the template in the Template Name field. |
| Step 6 | Enter values for all the fields, and click Save . See VG450 Gateway Template Field Description for field descriptions. |

| Step 1 | Choose Bulk Administration > Gateways > Gateway Template . The Find and List Gateway window displays. |
|---|---|
| Step 2 | Click Add New . The Add a new Gateway Template window displays. |
| Step 3 | From the Gateway Type drop-down list, choose Cisco ISR 4461 and click Next . |
| Step 4 | From the Protocol drop-down list, choose SIP , SCCP or MGCP and click Next . The Gateway Template Configuration window displays. |
| Step 5 | Enter a unique name for the template in the Template Name field. |
| Step 6 | Enter values for all the fields, and click Save . See ISR 4461 Gateway Template Field Descriptions for field descriptions. |

| Field | Description |
|---|---|
| Template Name | Enter a name up to 64 characters that identifies the CiscoVG200 gateway template. |
| Description | Enter a description that clarifies the purpose of the device. |
| Cisco Unified Communications Manager Group | Choose a Unified Communications Manager redundancy group from the list. A Unified Communications Manager redundancy group includes a prioritized list of up to three Unified Communications Managers.
                                             The first Unified Communications Manager in the list serves as the primary Unified Communications Manager. If the primary
                                             Unified Communications Manager is not available or fails, the gateway attempts to connect with the next Unified Communications
                                             Manager in the list and so on. |
| Configured Slots, VICs, and Endpoints Note You must specify the beginning port number for some VICs. For example, if the VIC in Subunit 0 begins at 0 and has two ports
                                                      (0 and 1), the VIC in Subunit 1 must begin at a port number greater than 1 and have two ports (2 and 3 or 4 and 5). Note VG200 gateway has only one slot. | Note | You must specify the beginning port number for some VICs. For example, if the VIC in Subunit 0 begins at 0 and has two ports
                                                      (0 and 1), the VIC in Subunit 1 must begin at a port number greater than 1 and have two ports (2 and 3 or 4 and 5). | Note | VG200 gateway has only one slot. |
| Note | You must specify the beginning port number for some VICs. For example, if the VIC in Subunit 0 begins at 0 and has two ports
                                                      (0 and 1), the VIC in Subunit 1 must begin at a port number greater than 1 and have two ports (2 and 3 or 4 and 5). |
| Note | VG200 gateway has only one slot. |
| Module in Slot 1 | For the available slot on the VG200 gateway, choose from the
                                             					 following type of modules: NM-1V—Network Module-1Voice has one voice interface card (VIC) in Sub-Unit 0 for FXS or FXO. NM-2V—Network Module-2Voice has two VICs, one in Sub-Unit 0 and one in Sub-Unit 1 for either FXS or FXO. NM-HDV—Network Module-High Density Voice has one VIC in Sub-Unit 0 either for T1 CAS or T1 PRI, or for E1 PRI. None—No network modules are installed. |
| Product-Specific Configuration |
| Model-specific configuration fields defined by the gateway
                                             					 manufacturer | The gateway manufacturer specifies the model-specific fields
                                             					 under product-specific configuration. Because they are dynamically configured,
                                             					 they can change without notice. To view field descriptions and help for product-specific
                                             					 configuration items, click the "?" information icon to the right of the Product Specific
                                             					 Configuration heading to display help in a popup dialog box. If you need more information, refer to the documentation for
                                             					 the specific gateway that you are configuring or contact the manufacturer. |

| Note | You must specify the beginning port number for some VICs. For example, if the VIC in Subunit 0 begins at 0 and has two ports
                                                      (0 and 1), the VIC in Subunit 1 must begin at a port number greater than 1 and have two ports (2 and 3 or 4 and 5). |
|---|---|

| Note | VG200 gateway has only one slot. |
|---|---|

| Field | Description |
|---|---|
| Template Name | Enter a name of up to 64 characters that identifies the
                                             					 CiscoVG224 gateway template. |
| Description | Enter a description that clarifies the purpose of the device. |
| Cisco Unified Communications Manager Group | From the drop-down list box, choose a Cisco Unified Communications Manager redundancy group. A Cisco Unified Communications Manager redundancy group includes a prioritized list
                                             					 of up to three Cisco Unified Communications Manager s. The first Cisco Unified Communications Manager in the list serves as the primary Cisco Unified Communications Manager . If the primary Cisco Unified Communications Manager is not available or fails, the gateway
                                             					 attempts to connect with the next Cisco Unified Communications Manager in the list and so on. |
| Configured Slots, VICs, and Endpoints |
| Module in Slot 2 | For the available slot on the VG224 gateway, select Analog
                                             					 from the drop-down list box. |
| Subunit 0 | For the available subunit 0 on the VG224 gateway, choose 24FXS
                                             					 as the subunit from the drop-down list box. Note Be aware that only Module in Slot 2, and Subunit 0 are
                                                         						available for VG224 gateways. | Note | Be aware that only Module in Slot 2, and Subunit 0 are
                                                         						available for VG224 gateways. |
| Note | Be aware that only Module in Slot 2, and Subunit 0 are
                                                         						available for VG224 gateways. |

| Note | Be aware that only Module in Slot 2, and Subunit 0 are
                                                         						available for VG224 gateways. |
|---|---|

| Field | Description |
|---|---|
| Template Name | Enter a name of up to 64 characters that identifies the
                                             					 CiscoVG202 or VG204 gateway template. |
| Description | Enter a description that clarifies the purpose of the device. |
| Cisco Unified Communications Manager Group | From the drop-down list box, choose a Cisco Unified Communications Manager redundancy group. A Cisco Unified Communications Manager redundancy group includes a prioritized list
                                             					 of up to three Cisco Unified Communications Manager s. The first Cisco Unified Communications Manager in the list serves as the primary Cisco Unified Communications Manager . If the primary Cisco Unified Communications Manager is not available or fails, the gateway
                                             					 attempts to connect with the next Cisco Unified Communications Manager in the list and so on. |
| Configured Slots, VICs, and Endpoints |
| Module in Slot 0 | For the available slot on the VG202 or VG204 gateway, select
                                             					 Analog from the drop-down list box. |
| Subunit 0 | For the available subunit 0 on the VG202 or VG204 gateway,
                                             					 choose 2FXS as the subunit from the drop-down list box. Note Be aware that only Module in Slot 0, and Subunit 0 are
                                                         						available for VG202 and VG204 gateways. | Note | Be aware that only Module in Slot 0, and Subunit 0 are
                                                         						available for VG202 and VG204 gateways. |
| Note | Be aware that only Module in Slot 0, and Subunit 0 are
                                                         						available for VG202 and VG204 gateways. |

| Note | Be aware that only Module in Slot 0, and Subunit 0 are
                                                         						available for VG202 and VG204 gateways. |
|---|---|

| Field | Description |
|---|---|
| Template Name | Enter a name of up to 64 characters that identifies the VG310 gateway template. |
| Description | Enter a description that clarifies the purpose of the device. |
| Cisco Unified Communications Manager Group | From the drop-down list box, choose a Cisco Unified Communications Manager redundancy group. A Cisco Unified Communications Manager redundancy group includes a prioritized list of up to three Cisco Unified Communications Manager s. The first Cisco Unified Communications Manager in the list serves as the primary Cisco Unified Communications Manager . If the primary Cisco Unified Communications Manager is not available or fails, the gateway attempts to connect with the next Cisco Unified Communications Manager in the list and so on. |
| Configured Slots, VICs, and Endpoints |
| Module in Slot 0 | For the available slot on the VG310 gateway, select VG-2VWIC-MBRD from the drop-down list box. |
| Product-Specific Configuration |
| Model-specific configuration fields defined by the gateway manufacturer | The gateway manufacturer specifies the model-specific fields under product-specific configuration. Because they are dynamically
                                             configured, they can change without notice. To view field descriptions and help for product-specific configuration items, click the "?" information icon to the right of the Product Specific Configuration heading to display help in a popup dialog box. If you need more information, refer to the documentation for the specific gateway that you are configuring or contact the
                                             manufacturer. |

| Field | Description |
|---|---|
| Template Name | Enter a name of up to 64 characters that identifies the VG320 gateway template. |
| Description | Enter a description that clarifies the purpose of the device. |
| Cisco Unified Communications Manager Group | From the drop-down list box, choose a Cisco Unified Communications Manager redundancy group. A Cisco Unified Communications Manager redundancy group includes a prioritized list of up to three Cisco Unified Communications Manager s. The first Cisco Unified Communications Manager in the list serves as the primary Cisco Unified Communications Manager . If the primary Cisco Unified Communications Manager is not available or fails, the gateway attempts to connect with the next Cisco Unified Communications Manager in the list and so on. |
| Configured Slots, VICs, and Endpoints |
| Module in Slot 0 | For the available slot on the VG320 gateway, select VG-3VWIC-MBRD from the drop-down list box. |
| Product-Specific Configuration |
| Model-specific configuration fields defined by the gateway manufacturer | The gateway manufacturer specifies the model-specific fields under product-specific configuration. Because they are dynamically
                                             configured, they can change without notice. To view field descriptions and help for product-specific configuration items, click the "?" information icon to the right of the Product Specific Configuration heading to display help in a popup dialog box. If you need more information, refer to the documentation for the specific gateway that you are configuring or contact the
                                             manufacturer. |

| Field | Description |
|---|---|
| Template Name | Enter a name of up to 64 characters that identifies the VG350 gateway template. |
| Description | Enter a description that clarifies the purpose of the device. |
| Cisco Unified Communications Manager Group | From the drop-down list box, choose a Cisco Unified Communications Manager redundancy group. A Cisco Unified Communications Manager redundancy group includes a prioritized list of up to three Cisco Unified Communications Manager s. The first Cisco Unified Communications Manager in the list serves as the primary Cisco Unified Communications Manager . If the primary Cisco Unified Communications Manager is not available or fails, the gateway attempts to connect with the next Cisco Unified Communications Manager in the list and so on. |
| Configured Slots, VICs, and Endpoints |
| Module in Slot 0 | For the available slot on the VG350 gateway, select NM-4VWIC-MBRD from the drop-down list box. |
| Module in Slot 1/3 | For the available slot on the VG350 gateway, select NONE from the drop-down list. |
| Module in Slot 2/4 | For the available slot on the VG350 gateway, select ANALOG from the drop-down list. |
| Product-Specific Configuration |
| Model-specific configuration fields defined by the gateway manufacturer | The gateway manufacturer specifies the model-specific fields under product-specific configuration. Because they are dynamically
                                             configured, they can change without notice. To view field descriptions and help for product-specific configuration items, click the "?" information icon to the right of the Product Specific Configuration heading to display help in a popup dialog box. If you need more information, refer to the documentation for the specific gateway that you are configuring or contact the
                                             manufacturer. |

| Field | Description |
|---|---|
| Template Name | Enter a name of up to 64 characters that identifies the VG420 gateway template. |
| Description | Enter a description that clarifies the purpose of the device. |
| Unified Communications Manager Group | From the drop-down list, choose a Unified Communications Manager redundancy group. A Unified Communications Manager redundancy group includes a prioritized list of up to three Unified Communications Managers.
                                             The first Unified Communications Manager in the list serves as the primary Unified Communications Manager. If the primary
                                             Unified Communications Manager is not available or fails, the gateway attempts to connect with the next Unified Communications
                                             Manager in the list and so on. |
| Configured Slots, VICs, and Endpoints |
| Module in Slot 0 | For the available slot on the VG420 gateway, select ISR-2NIM-MBRD from the drop-down list. |
| Module in Slot 1 | For the available slot on the VG420 gateway, select ANALOG from the drop-down list. |
| Product-Specific Configuration |
| Model-specific configuration fields defined by the gateway manufacturer | The gateway manufacturer specifies the model-specific fields under product-specific configuration. Because they are dynamically
                                             configured, they can change without notice. To view field descriptions and help for product-specific configuration items, click the "?" information icon to the right of the Product Specific Configuration heading to display help in a pop-up dialog box. If you need more information, see the documentation for the specific gateway that you are configuring or contact the manufacturer. |

| Field | Description |
|---|---|
| Template Name | Enter a name of up to 64 characters that identifies the VG450 gateway template. |
| Description | Enter a description that clarifies the purpose of the device. |
| Unified Communications Manager Group | From the drop-down list box, choose a Unified Communications Manager redundancy group. A Unified Communications Manager redundancy group includes a prioritized list of up to three Unified Communications Managers.
                                             The first Unified Communications Manager in the list serves as the primary Unified Communications Manager. If the primary
                                             Unified Communications Manager is not available or fails, the gateway attempts to connect with the next Unified Communications
                                             Manager in the list and so on. |
| Configured Slots, VICs, and Endpoints |
| Module in Slot 0 | For the available slot on the VG450 gateway, select ISR-3NIM-MBRD from the drop-down list box. |
| Module in Slot 1/2/3 | For the available slot on the VG450 gateway, select ANALOG from the drop-down list. ANALOG—In the SM-X slot on the gateway, users can choose SM-X-16FXS/FXO, SM-X-24FXS/4FXO, SM-X-8FXS/12FXO, SM-X-56FXS, or
                                             SM-X-72FXS modules. |
| Product-Specific Configuration |
| Model-specific configuration fields defined by the gateway manufacturer | The gateway manufacturer specifies the model-specific fields under product-specific configuration. Because they are dynamically
                                             configured, they can change without notice. To view field descriptions and help for product-specific configuration items, click the "?" information icon to the right of the Product Specific Configuration heading to display help in a popup dialog box. If you need more information, refer to the documentation for the specific gateway that you are configuring or contact the
                                             manufacturer. |

| Field | Description |
|---|---|
| Template Name | Enter a name of up to 64 characters that identifies the ISR 4461 gateway template. |
| Description | Enter a description that clarifies the purpose of the device. |
| Cisco Unified Communications Manager Group | From the drop-down list box, choose a Cisco Unified Communications Manager redundancy group. A Cisco Unified Communications Manager redundancy group includes a prioritized list of up to three Cisco Unified Communications
                                             Managers. The first Cisco Unified Communications Manager in the list serves as the primary Cisco Unified Communications Manager.
                                             If the primary Cisco Unified Communications Manager is not available or fails, the gateway attempts to connect with the next
                                             Cisco Unified Communications Manager in the list and so on. |
| Configured Slots, VICs, and Endpoints |
| Module in Slot 0 | For the available slot on the ISR 4461 gateway, select ISR-3NIM-MBRD from the drop-down list box. |
| Module in Slot 1/2/3 | For the available slot on the ISR 4461 gateway, choose from the following type of modules: ANALOG—In the SM-X slot on the gateway, users can choose SM-X-16FXS/FXO, SM-X-24FXS/4FXO, SM-X-8FXS/12FXO, SM-X-56FXS, or
                                                   SM-X-72FXS modules. SM-X-NIM-ADPTR—Adapter for the NIM in a SM-X slot on the gateway. |
| Product-Specific Configuration |
| Model-specific configuration fields defined by the gateway manufacturer | The gateway manufacturer specifies the model-specific fields under product-specific configuration. Because they are dynamically
                                             configured, they can change without notice. To view field descriptions and help for product-specific configuration items, click the "?" information icon to the right of the Product Specific Configuration heading to display help in a popup dialog box. If you need more information, refer to the documentation for the specific gateway that you are configuring or contact the
                                             manufacturer. |

| Field | Description |
|---|---|
| Description | Enter the purpose of the device. The description can include
                                             					 up to 50 characters in any language, but it cannot include double-quotes ( " ),
                                             					 percentage sign ( % ), ampersand (&), back-slash ( \ ), or angle brackets
                                             					 (<>). |
| Device Pool | From the drop-down list box, select the appropriate device
                                             					 pool. The device pool specifies a collection of properties for this
                                             					 device that includes Communications Manager Group, Date / Time Group, Region, and
                                             					 Calling Search Space for auto-registration of devices. |
| Common Device Configuration | Choose the common device configuration to which you want this
                                             					 gateway assigned. The common device configuration includes the attributes
                                             					 (services or features) that are associated with a particular user. You
                                             					 configure the common device configurations in the Common Device Configuration window. To see the common device configuration settings, click the
                                             					 View Details link. |
| Media Resource Group List | This list provides a prioritized grouping of media resource
                                             					 groups. An application chooses the required media resource, such as a Music On
                                             					 Hold server, from among the available media resources according to the priority
                                             					 order that a Media Resource Group List defines. |
| Network Hold MOH Audio Source | Choose the network hold audio source for this group of IP
                                             					 gateways. The network hold audio source identifies the audio source from
                                             					 which music is played when the system places a call on hold, such as when the
                                             					 user transfers or parks a call. |
| Calling Search Space | From the drop-down list box, select the appropriate calling
                                             					 search space. The calling search space specifies a collection of partitions
                                             					 that are searched to determine how a collected (originating) number should be
                                             					 routed. You can configure the number of calling search spaces that
                                             					 display in this drop-down list box by using the Max List Box Items enterprise
                                             					 parameter. If more calling search spaces exist than the Max List Box Items
                                             					 enterprise parameter specifies, the ellipsis button (...) displays next to the
                                             					 drop-down list box. Click the... button to display the Select Calling Search
                                             					 Space window. Enter a partial calling search space name in the List items where
                                             					 Name contains field. Click the desired calling search space name in the list of
                                             					 calling search spaces that displays in the Select item to use box and click OK . Note To set the maximum list box items, choose System > Enterprise
                                                               							 Parameters and choose UnifiedCMAdmin Parameters. | Note | To set the maximum list box items, choose System > Enterprise
                                                               							 Parameters and choose UnifiedCMAdmin Parameters. |
| Note | To set the maximum list box items, choose System > Enterprise
                                                               							 Parameters and choose UnifiedCMAdmin Parameters. |
| AAR Calling Search Space | Choose the appropriate calling search space for the device to
                                             					 use when it performs automated alternate routing (AAR). The AAR calling search
                                             					 space specifies the collection of route partitions that are searched to
                                             					 determine how to route a collected (originating) number that is otherwise
                                             					 blocked due to insufficient bandwidth. |
| Location | Select the appropriate location for this device. The location
                                             					 specifies the total bandwidth that is available for calls to and from this
                                             					 location. A location setting of None means that the locations feature does not
                                             					 keep track of the bandwidth that this device consumes. |
| AAR Group | Choose the automated alternate routing (AAR) group for this
                                             					 device. The AAR group provides the prefix digits that are used to route calls
                                             					 that are otherwise blocked due to insufficient bandwidth. An AAR group setting
                                             					 of None specifies that no rerouting of blocked calls will be attempted. |
| Network Locale | From the drop-down list box, choose the locale that is
                                             					 associated with the gateway. The network locale identifies a set of detailed
                                             					 information to support the hardware in a specific location. The network locale
                                             					 contains a definition of the tones and cadences that the device uses in a
                                             					 specific geographic area. Note Choose only a network locale that is already installed and
                                                         						supported by the associated devices. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up. | Note | Choose only a network locale that is already installed and
                                                         						supported by the associated devices. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up. |
| Note | Choose only a network locale that is already installed and
                                                         						supported by the associated devices. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up. |
| Use Trusted Relay Point | From the drop-down list box, enable or disable whether Cisco Unified Communications Manager inserts a trusted relay point (TRP) device
                                             					 with this media endpoint. Choose one of the following values: Default—If you
                                                						choose this value, the device uses the Use Trusted Relay Point setting from the
                                                						common device configuration with which this device associates. Off—Choose this
                                                						value to disable the use of a TRP with this device. This setting overrides the
                                                						Use Trusted Relay Point setting in the common device configuration with which
                                                						this device associates. On—Choose this
                                                						value to enable the use of a TRP with this device. This setting overrides the
                                                						Use Trusted Relay Point setting in the common device configuration with which
                                                						this device associates. A Trusted Relay Point (TRP) device designates an MTP or
                                             					 transcoder device that is labeled as Trusted Relay Point. Cisco Unified Communications Manager places the TRP closest to the
                                             					 associated endpoint device if more than one resource is needed for the endpoint
                                             					 (for example, a transcoder or RSVP Agent). If both TRP and MTP are required for the endpoint, TRP gets
                                             					 used as the required MTP. |
| Port Selection Order | Choose the order in which ports are chosen. If you are not
                                             					 sure which port order to use, choose TOP_DOWN: TOP_DOWN—Selects
                                                						ports in descending order, from port 1 to port 8. BOTTOM_UP—Selects
                                                						ports in ascending order, from port 8 to port 1. |
| Load Information | Enter the appropriate firmware load information for the
                                             					 gateway. The values that you enter here override the default values for
                                             					 this gateway. |
| Transmit UTF-8 for Calling Party Name | This device uses the user locale setting of the device's
                                             					 device pool to determine whether to send unicode and whether to translate
                                             					 received unicode information. For the sending device, if you check this check box and the
                                             					 user locale setting in the device's device pool matches the terminating phone's
                                             					 user locale, the device sends unicode. If the user locale settings do not
                                             					 match, the device sends ASCII. The receiving device translates incoming unicode characters
                                             					 based on the user locale setting of the sending device's device pool. If the
                                             					 user locale setting matches the terminating phone's user locale, the phone
                                             					 displays the characters. Note The phone may display junk characters if the two ends of the
                                                         						trunk configure user locales that do not belong to the same language group. | Note | The phone may display junk characters if the two ends of the
                                                         						trunk configure user locales that do not belong to the same language group. |
| Note | The phone may display junk characters if the two ends of the
                                                         						trunk configure user locales that do not belong to the same language group. |
| Calling Party Transformation CSS | This setting allows you to localize the calling party number
                                             					 on the device. Make sure that the Calling Party Transformation CSS that you
                                             					 choose contains the calling party transformation pattern that you want to
                                             					 assign to this device. The device takes on the attributes of the Calling Party
                                             					 Transformation Pattern when you assign the pattern to a partition where the
                                             					 Calling Party Transformation CSS exists. |
| Use Device Pool Calling Party Transformation CSS | To use the Calling Party Transformation CSS that is configured
                                             					 in the device pool that is assigned to this device, check this check box. If
                                             					 you do not check this check box, the device uses the Calling Party
                                             					 Transformation CSS that you configured in the device configuration window. |
| Multilevel Precedence and Preemption (MLPP)
                                                						Information |
| MLPP Domain | From the drop-down list box, choose an MLPP domain to
                                             					 associate with this device. If you leave the value <None>, this device
                                             					 inherits its MLPP domain from the value that was set for the device's device
                                             					 pool. If the device pool does not have an MLPP Domain setting, this device
                                             					 inherits its MLPP Domain from the value that was set for the MLPP Domain
                                             					 Identifier enterprise parameter. |
| MLPP Indication | This device type does not have this setting. |
| MLPP Preemption | This setting does not have this device type. |
| Geo Location Configuration |
| Geo Location | From the drop-down list box, select a geo location. You can select the Unspecified geo location, which designates
                                             					 that this device does not associate with a geo location. You can also select a geo location that has been configured
                                             					 with the System > Geolocation
                                                   						  Configuration menu option. |
| Geo Location Filter | From the drop-down list box, select a geo location filter. If you leave the <None> setting, no geo location filter
                                             					 gets applied for this device. You can also select a geo location filter that has been
                                             					 configured with the System > Geolocation
                                                   						  Filter menu option. |

| Note | To set the maximum list box items, choose System > Enterprise
                                                               							 Parameters and choose UnifiedCMAdmin Parameters. |
|---|---|

| Note | Choose only a network locale that is already installed and
                                                         						supported by the associated devices. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up. |
|---|---|

| Note | The phone may display junk characters if the two ends of the
                                                         						trunk configure user locales that do not belong to the same language group. |
|---|---|

| Field | Description |
|---|---|
| Device Information |
| End-Point Name | For VG200 gateways, this display-only field contains a string
                                             					 that Cisco Unified Communications Manager generates that uniquely identifies the VG200
                                             					 analog interface. |
| Description | Cisco Unified Communications Manager generates a string that uniquely
                                             					 identifies the analog MGCP description. For example: AALN/S0/SU1/1@domain.com You can edit this field. The description can include up to 50
                                             					 characters in any language, but it cannot include double-quotes
                                             					 ( " ), percentage sign ( % ), ampersand
                                             					 ( & ), back-slash ( \ ), or angle brackets
                                             					 (<>). |
| Device Pool | From the drop-down list box, choose the appropriate device
                                             					 pool. The device pool specifies a collection of properties for this
                                             					 device including Communications Manager Group, Date/Time Group, Region, and
                                             					 Calling Search Space for auto registration of devices. |
| Media Resource Group List | This list provides a prioritized grouping of media resource
                                             					 groups. An application chooses the required media resource, such as a Music On
                                             					 Hold server, from among the available media resources according to the priority
                                             					 order that is defined in a Media Resource Group List. |
| Packet Capture Mode (for Cisco IOS MGCP gateways only) | Configure this field only when you need to troubleshoot
                                             					 encrypted signaling information for the Cisco IOS MGCP gateway. Configuring
                                             					 packet capturing may cause call-processing interruptions. For more information
                                             					 about this field, see the Cisco Unified Communications Manager Security Guide . |
| Packet Capture Duration (for Cisco IOS MGCP gateways only) | Configure this field only when you need to troubleshoot
                                             					 encrypted signaling information for the Cisco IOS MGCP gateway. Configuring
                                             					 packet capturing may cause call-processing interruptions. For more information
                                             					 about this field, see the Cisco Unified Communications Manager Security Guide . |
| Calling Search Space | From the drop-down list box, choose the appropriate calling
                                             					 search space. A calling search space comprises a collection of route partitions
                                             					 that are searched to determine how a collected (originating) number should be
                                             					 routed. |
| AAR Calling Search Space | Choose the appropriate calling search space for the device to
                                             					 use when it performs automated alternate routing (AAR). The AAR calling search
                                             					 space specifies the collection of route partitions that are searched to
                                             					 determine how to route a collected (originating) number that is otherwise
                                             					 blocked due to insufficient bandwidth. |
| Location | Use locations to implement call admission control (CAC) in a
                                             					 centralized call-processing system. CAC enables you to regulate audio quality
                                             					 and video availability by limiting the amount of bandwidth that is available
                                             					 for audio and video calls over links between locations. The location specifies
                                             					 the total bandwidth that is available for calls to and from this location. From the drop-down list box, choose the appropriate location
                                             					 for this device. A location setting of Hub_None means that the locations
                                             					 feature does not keep track of the bandwidth that this device consumes. A
                                             					 location setting of Phantom specifies a location that enables successful CAC
                                             					 across intercluster trunks that use H.323 or SIP protocol. To configure a new location, use the System > Location menu option. |
| AAR Group | Choose the automated alternate routing (AAR) group for this
                                             					 device. The AAR group provides the prefix digits that are used to route calls
                                             					 that are otherwise blocked due to insufficient bandwidth. An AAR group setting
                                             					 of None specifies that no rerouting of blocked calls will be attempted. |
| Network Locale | From the drop-down list box, choose the locale that is
                                             					 associated with the gateway. The network locale identifies a set of detailed
                                             					 information to support the hardware in a specific location. The network locale
                                             					 contains a definition of the tones and cadences that the device uses in a
                                             					 specific geographic area. Note Choose only a network locale that is already installed and
                                                         						that the associated devices support. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up. | Note | Choose only a network locale that is already installed and
                                                         						that the associated devices support. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up. |
| Note | Choose only a network locale that is already installed and
                                                         						that the associated devices support. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up. |
| Use Trusted Relay Point | From the drop-down list box, enable or disable whether Cisco Unified Communications Manager inserts a trusted relay point (TRP) device
                                             					 with this media endpoint. Choose one of the following values: Default—If you
                                                						choose this value, the device uses the Use Trusted Relay Point setting from the
                                                						common device configuration with which this device associates. Off—Choose this
                                                						value to disable the use of a TRP with this device. This setting overrides the
                                                						Use Trusted Relay Point setting in the common device configuration with which
                                                						this device associates. On—Choose this
                                                						value to enable the use of a TRP with this device. This setting overrides the
                                                						Use Trusted Relay Point setting in the common device configuration with which
                                                						this device associates. A Trusted Relay Point (TRP) device designates an MTP or
                                             					 transcoder device that is labeled as Trusted Relay Point. Cisco Unified Communications Manager places the TRP closest to the
                                             					 associated endpoint device if more than one resource is needed for the endpoint
                                             					 (for example, a transcoder or RSVP Agent). If both TRP and RSVP Agent are needed for the endpoint, Cisco Unified Communications Manager first tries to find an RSVP Agent that can
                                             					 also be used as a TRP. If both TRP and transcoder are needed for the endpoint, Cisco Unified Communications Manager first tries to find a transcoder that is also
                                             					 designated as a TRP. |
| Transmit UTF-8 for Calling Party Name | This device uses the user locale setting of the device pool
                                             					 for the device to determine whether to send unicode and whether to translate
                                             					 received unicode information. For the sending device, if you check this check box and the
                                             					 user locale setting in the device pool for the device matches the terminating
                                             					 phone user locale, the device sends unicode. If the user locale settings do not
                                             					 match, the device sends ASCII. The receiving device translates incoming unicode characters
                                             					 based on the user locale setting of the sending device pool for the device. If
                                             					 the user locale setting matches the terminating phone user locale, the phone
                                             					 displays the characters. Note The phone may display junk characters if the two ends of the
                                                         						trunk configure user locales that do not belong to the same language group. | Note | The phone may display junk characters if the two ends of the
                                                         						trunk configure user locales that do not belong to the same language group. |
| Note | The phone may display junk characters if the two ends of the
                                                         						trunk configure user locales that do not belong to the same language group. |
| Calling Party Transformation CSS | This setting, which displays for FXS ports (not FXO ports),
                                             					 allows you to localize the calling party number on the device. Make sure that
                                             					 the Calling Party Transformation CSS that you choose contains the calling party
                                             					 transformation pattern that you want to assign to this device. Tip Before the call occurs, the device must apply
                                                      					 the transformation by using digit analysis. If you configure the Calling Party
                                                      					 Transformation CSS as None, the transformation does not match and does not get
                                                      					 applied. Ensure that you configure the Calling Party Transformation Pattern in
                                                      					 a non-null partition that is not used for routing. | Tip | Before the call occurs, the device must apply
                                                      					 the transformation by using digit analysis. If you configure the Calling Party
                                                      					 Transformation CSS as None, the transformation does not match and does not get
                                                      					 applied. Ensure that you configure the Calling Party Transformation Pattern in
                                                      					 a non-null partition that is not used for routing. |
| Tip | Before the call occurs, the device must apply
                                                      					 the transformation by using digit analysis. If you configure the Calling Party
                                                      					 Transformation CSS as None, the transformation does not match and does not get
                                                      					 applied. Ensure that you configure the Calling Party Transformation Pattern in
                                                      					 a non-null partition that is not used for routing. |
| Use Device Pool Calling Party Transformation CSS | To use the Calling Party Transformation CSS that is configured
                                             					 in the device pool that is assigned to this device, check this check box. If
                                             					 you do not check this check box, the device uses the Calling Party
                                             					 Transformation CSS that you configured in the Gateway Configuration window. This settings displays for FXS ports, not FXO ports. |
| Hotline Device | Check this check box to make this device a Hotline device.
                                             					 Hotline devices can only connect to other Hotline devices. This feature is an
                                             					 extension of PLAR, which configures a phone to automatically dial one directory
                                             					 number when it goes off-hook. Hotline provides additional restrictions that you
                                             					 can apply to devices that use PLAR. To implement Hotline, you must also create a softkey template
                                             					 without supplementary service softkeys, and apply it to the Hotline device. |
| Multilevel Precedence and Preemption (MLPP)
                                                						Information |
| MLPP Domain | From the drop-down list box, select an MLPP domain to
                                             					 associate with this device. If you leave the value <None>, this device
                                             					 inherits its MLPP domain from the value set for the device pool for the device.
                                             					 If the device pool does not have an MLPP Domain setting, this device inherits
                                             					 its MLPP Domain from the value set for the MLPP Domain Identifier enterprise
                                             					 parameter. |
| MLPP Indication | Be aware that this setting is not available for all devices.
                                             					 If available, this setting specifies whether a device that can play precedence
                                             					 tones will use the capability when it places an MLPP precedence call. From the drop-down list box, choose a setting to assign to
                                             					 this device from the following options: Default—This
                                                						device inherits its MLPP indication setting from its device pool. Off—This device
                                                						does not handle nor process indication of an MLPP precedence call. On—This device
                                                						does handle and process indication of an MLPP precedence call. Note Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off or Default (when default is Off) while
                                                         						MLPP Preemption is set to Forceful. | Note | Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off or Default (when default is Off) while
                                                         						MLPP Preemption is set to Forceful. |
| Note | Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off or Default (when default is Off) while
                                                         						MLPP Preemption is set to Forceful. |
| MLPP Preemption | Be aware that this setting is not available for all devices.
                                             					 If available, this setting specifies whether a device that can preempt calls in
                                             					 progress will use the capability when it places an MLPP precedence call. From the drop-down list box, choose a setting to assign to
                                             					 this device from the following options: Default—This
                                                						device inherits its MLPP preemption setting from its device pool. Disabled—This
                                                						device does not allow preemption of lower precedence calls to take place when
                                                						necessary for completion of higher precedence calls. Forceful—This
                                                						device allows preemption of lower precedence calls to take place when necessary
                                                						for completion of higher precedence calls. Note Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off or Default (when default is Off) while
                                                         						MLPP Preemption is set to Forceful. | Note | Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off or Default (when default is Off) while
                                                         						MLPP Preemption is set to Forceful. |
| Note | Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off or Default (when default is Off) while
                                                         						MLPP Preemption is set to Forceful. |
| Port Information (POTS) |
| Port Direction | Choose the direction of calls that are passing through this
                                             					 port: Inbound—Use for
                                                						incoming calls only. Outbound—Use for
                                                						outgoing calls. Bothways—Use for
                                                						inbound and outbound calls (default). |
| Prefix DN(for FXS ports) | Enter the prefix digits that are appended to the digits that
                                             					 this trunk receives on incoming calls. Cisco Unified Communications Manager adds prefix digits after first
                                             					 truncating the number in accordance with the Num Digits setting. You can enter the international escape character + . |
| Num Digits(for FXS ports) | Enter the number of significant digits to collect, from 0 to
                                             					 32. Cisco Unified Communications Manager counts significant digits from the
                                             					 right (last digit) of the number called. Use this field for the processing of incoming calls and to
                                             					 indicate the number of digits starting from the last digit of the called number
                                             					 that is used to route calls coming into the PRI span. See Prefix DN. |
| Expected Digits(for FXS ports) | Enter the number of digits that are expected on the inbound
                                             					 side of the trunk. For this rarely used field, leave zero as the default value
                                             					 if you are unsure. |
| SMDI Port Number (0-4096) | Use this field for analog access ports that connect to a
                                             					 voice-messaging system. Set the SMDI Port Number equal to the actual port number on
                                             					 the voice-messaging system to which the analog access port connects. Note Voice-mail logical ports typically must match physical ports
                                                         						for the voice-messaging system to operate correctly. | Note | Voice-mail logical ports typically must match physical ports
                                                         						for the voice-messaging system to operate correctly. |
| Note | Voice-mail logical ports typically must match physical ports
                                                         						for the voice-messaging system to operate correctly. |
| Unattended Port | Check this check box to indicate an unattended port on this
                                             					 device. |
| Geo Location Configuration |
| Geo Location | From the drop-down list box, choose a geo location. You can choose the Unspecified geo location, which designates
                                             					 that this device does not associate with a geo location. You can also choose a geolocation that has been configured
                                             					 with the System > Geolocation
                                                   						  Configuration menu option. |
| Geo Location Filter | From the drop-down list box, choose a geo location filter. If you leave the <None> setting, no geo location filter
                                             					 gets applied for this device. You can also choose a geo location filter that has been
                                             					 configured with the System Geolocation
                                                						Filter menu option. Note This field is not supported for FXS gateways. | Note | This field is not supported for FXS gateways. |
| Note | This field is not supported for FXS gateways. |
| Product-Specific Configuration |
| Model-specific configuration fields defined by the gateway
                                             					 manufacturer | The gateway manufacturer specifies the model-specific fields
                                             					 under product-specific configuration. Because they are dynamically configured,
                                             					 they can change without notice. To view field descriptions and help for product-specific
                                             					 configuration items, click the "?" information icon to the right of the Product Specific
                                             					 Configuration heading to display help in a popup dialog box. If you need more information, refer to the documentation for
                                             					 the specific gateway that you are configuring or contact the manufacturer. |

| Note | Choose only a network locale that is already installed and
                                                         						that the associated devices support. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up. |
|---|---|

| Note | The phone may display junk characters if the two ends of the
                                                         						trunk configure user locales that do not belong to the same language group. |
|---|---|

| Tip | Before the call occurs, the device must apply
                                                      					 the transformation by using digit analysis. If you configure the Calling Party
                                                      					 Transformation CSS as None, the transformation does not match and does not get
                                                      					 applied. Ensure that you configure the Calling Party Transformation Pattern in
                                                      					 a non-null partition that is not used for routing. |
|---|---|

| Note | Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off or Default (when default is Off) while
                                                         						MLPP Preemption is set to Forceful. |
|---|---|

| Note | Do not configure a device with the following combination of
                                                         						settings: MLPP Indication is set to Off or Default (when default is Off) while
                                                         						MLPP Preemption is set to Forceful. |
|---|---|

| Note | Voice-mail logical ports typically must match physical ports
                                                         						for the voice-messaging system to operate correctly. |
|---|---|

| Note | This field is not supported for FXS gateways. |
|---|---|

| Field | Description |
|---|---|
| End-Point Name | For VG200 gateways, this display-only field contains a string
                                             					 that Cisco Unified Communications Manager generates that uniquely identifies the VG200
                                             					 digital interface. For example: S1/DS1-0@VG200-2 S1 indicates slot 1, DS1-0 designates the digital interface,
                                             					 and @ VG200-2 designates the VG200 template name. |
| Description | Enter a description that clarifies the purpose of the device.
                                             					 The description can include up to 50 characters in any language, but it cannot
                                             					 include double-quotes ("), percentage sign
                                             					 ( % ), ampersand (&), back-slash
                                             					 ( \ ), or angle brackets (<>). |
| Device Pool | From the drop-down list box, choose the appropriate device
                                             					 pool. The device pool specifies a collection of properties for this
                                             					 device including Communications Manager Group, Date / Time
                                             					 Group, Region, and Calling Search Space for auto-registration of devices. |
| Call Classification | This parameter determines whether an incoming call that is
                                             					 using this gateway is considered off the network (OffNet) or on the network
                                             					 (OnNet). When the Call Classification field is configured as Use System
                                             					 Default, the setting of the Cisco Unified Communications Manager clusterwide service parameter, Call
                                             					 Classification, determines whether the gateway is OnNet or OffNet. This field provides an OnNet or OffNet alerting tone when the
                                             					 call is OnNet or OffNet, respectively. |
| Media Resource Group List | This list provides a prioritized grouping of media resource
                                             					 groups. An application chooses the required media resource, such as a Music On
                                             					 Hold server, from among the available media resources according to the priority
                                             					 order that is defined in a Media Resource List. |
| Calling Search Space | From the drop-down list box, choose the appropriate calling
                                             					 search space. A calling search space designates a collection of route
                                             					 partitions that are searched to determine how a collected (originating) number
                                             					 should be routed. You can configure the number of calling search spaces that
                                             					 display in this drop-down list box by using the Max List Box Items enterprise
                                             					 parameter. If more calling search spaces exist than the Max List Box Items
                                             					 enterprise parameter specifies, the ellipsis button (...) displays next to the
                                             					 drop-down list box. Click the... button to display the Select Calling Search Space window. Enter
                                             					 a partial calling search space name in the List items where Name contains
                                             					 field. Click the desired calling search space name in the list of calling
                                             					 search spaces that displays in the Select item to use box and click OK . Note To set the maximum list box items, choose System > Enterprise
                                                               							 Parameters and choose UnifiedCMAdmin Parameters. | Note | To set the maximum list box items, choose System > Enterprise
                                                               							 Parameters and choose UnifiedCMAdmin Parameters. |
| Note | To set the maximum list box items, choose System > Enterprise
                                                               							 Parameters and choose UnifiedCMAdmin Parameters. |
| AAR Calling Search Space | Choose the appropriate calling search space for the device to
                                             					 use when automated alternate routing (AAR) is performed. The AAR calling search
                                             					 space specifies the collection of route partitions that are searched to
                                             					 determine how to route a collected (originating) number that is otherwise
                                             					 blocked due to insufficient bandwidth. |
| Location | Choose the appropriate location for this device. The location
                                             					 specifies the total bandwidth that is available for calls to and from this
                                             					 location. A location setting of None means that the locations feature does not
                                             					 keep track of the bandwidth that this device consumes. |
| AAR Group | Choose the automated alternate routing (AAR) group for this
                                             					 device. The AAR group provides the prefix digits that are used to route calls
                                             					 that are otherwise blocked due to insufficient bandwidth. An AAR group setting
                                             					 of None specifies that no rerouting of blocked calls will be attempted. |
| MLPP Domain | From the drop-down list box, choose an MLPP domain to
                                             					 associate with this device. If you leave the value <None>, this device
                                             					 inherits its MLPP domain from the value that was set for the device's device
                                             					 pool. If the device pool does not have an MLPP Domain setting, this device
                                             					 inherits its MLPP Domain from the value that was set for the MLPP Domain
                                             					 Identifier enterprise parameter. |
| Handle DTMF Precedence Signals | Check this box to enable this gateway to interpret special
                                             					 DTMF signals as MLPP precedence levels. |
| Load Information | Enter the appropriate firmware load information for the
                                             					 gateway. The values that you enter here override the default values for
                                             					 this gateway. |
| Port Selection Order | Choose the order in which channels or ports are allocated for
                                             					 outbound calls from first (lowest number port) to last (highest number port) or
                                             					 from last to first. Valid entries include TOP_DOWN (first to last) or BOTTOM_UP
                                             					 (last to first). If you are not sure which port order to use, choose TOP_DOWN. |
| Digit Sending | Choose one of the following digit sending types for
                                             					 out-dialing: DTMF—Dual-tone
                                                						multifrequency. Normal touchtone dialing MF—Multifrequency PULSE—Pulse
                                                						(rotary) dialing |
| Network Locale | From the drop-down list box, choose the locale that is
                                             					 associated with the gateway. The network locale identifies a set of detailed
                                             					 information to support the hardware in a specific location. The network locale
                                             					 contains a definition of the tones and cadences that the device uses in a
                                             					 specific geographic area. Note Choose only a network locale that is already installed and
                                                         						supported by the associated devices. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up. | Note | Choose only a network locale that is already installed and
                                                         						supported by the associated devices. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up. |
| Note | Choose only a network locale that is already installed and
                                                         						supported by the associated devices. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up. |
| SMDI Base Port | Enter the first SMDI port number of the T1 span. If you set this parameter to a nonzero value and this gateway
                                             					 belongs to an unknown type of route list, route group, or route list, hunting
                                             					 does not continue past this span. |
| Geo Location Configuration |
| Geo Location | From the drop-down list box, choose a geo location. You can choose the Unspecified geo location, which designates
                                             					 that this device does not associate with a geo location. You can also choose a geolocation that has been configured
                                             					 with the System > Geolocation
                                                   						  Configuration menu option. |
| Geo Location Filter | From the drop-down list box, choose a geo location filter. If you leave the <None> setting, no geo location filter
                                             					 gets applied for this device. You can also choose a geo location filter that has been
                                             					 configured with the System > Geolocation
                                                   						  Filter menu option. |
| Product-Specific Configuration |
| Model-specific configuration fields that the gateway
                                             					 manufacturer defines | The gateway manufacturer specifies the model-specific fields
                                             					 under product-specific configuration. Because they are dynamically configured,
                                             					 they can change without notice. To view field descriptions and help for product-specific
                                             					 configuration items, click the "?" information icon to the right of the Product Specific
                                             					 Configuration heading to display help in a popup dialog box. If you need more information, refer to the documentation for
                                             					 the specific gateway that you are configuring or contact the manufacturer. |

| Note | To set the maximum list box items, choose System > Enterprise
                                                               							 Parameters and choose UnifiedCMAdmin Parameters. |
|---|---|

| Note | Choose only a network locale that is already installed and
                                                         						supported by the associated devices. The list contains all available network
                                                         						locales for this setting, but not all are necessarily installed. If the device
                                                         						is associated with a network locale that it does not support in the firmware,
                                                         						the device will fail to come up. |
|---|---|

| Field | Description |
|---|---|
| Device Information |
| Endpoint Name | For VG200 gateways, this display-only field contains a string
                                             					 that is generated by Cisco Unified Communications Manager that uniquely identifies the VG200 endpoint. For example: S1/DS1-0 @ VG200-2 S1 indicates slot 1, DS1-0 designates the digital interface,
                                             					 and @ VG200-2 designates the VG200 domain name. |
| Description | Enter a description for the end-point that you are
                                             					 configuring. The description can include up to 50 characters in any language,
                                             					 but it cannot include double-quotes ("), percentage sign
                                             					 ( % ), ampersand (&), back-slash
                                             					 ( \ ), or angle brackets (<>). |
| Device Pool | Choose the device pool for this group of
                                             					 gateways / ports. A device pool defines sets of common characteristics for
                                             					 devices, such as region, date/time group, Cisco Unified Communications Manager group, and calling search space for
                                             					 auto-registration. |
| Call Classification | From the drop-down list box, choose an option to configure the
                                             					 device as on net, off net, or system default. If you chose 'Use System Default' at the device level, the
                                             					 system uses the value of the service parameter to determine whether the device
                                             					 is internal (on net) or external (off net). |
| Network Locale | Choose the network locale that you want to associate with this
                                             					 gateway. The Network Locale comprises a set of tones and cadences that
                                             					 Cisco gateways and phones use when communicating with the PSTN and other
                                             					 networks in a specific geographical area. |
| Media Resource Group List | Choose the media resource group list (MRGL) for this group of
                                             					 gateways/ports. An MRGL specifies a list of prioritized media resource groups.
                                             					 An application can choose required media resources from among the available
                                             					 ones according to the priority order that is defined in the MRGL. |
| Location | Choose the location for this group of gateways/ports. A location indicates the remote location that is accessed by
                                             					 using restricted bandwidth connections. |
| AAR Group | Choose the automated alternate routing (AAR) group for this
                                             					 device. The AAR group provides the prefix digits that are used to route calls
                                             					 that are otherwise blocked due to insufficient bandwidth. An AAR group setting
                                             					 of None specifies that no rerouting of blocked calls will be attempted. |
| Load Information | Enter the appropriate load information for the custom software
                                             					 for gateway. The values that you enter here override the default values for
                                             					 this gateway. To use the default load, leave this field blank. |
| Transmit UTF-8 for Calling Party Name | This device uses the user locale setting of the device's
                                             					 device pool to determine whether to send Unicode and whether to translate
                                             					 received Unicode information. For the sending device, if you check this check box and the
                                             					 user locale setting in the device's device pool matches the terminating phone's
                                             					 user locale, the device sends Unicode. If the user locale settings do not
                                             					 match, the device sends ASCII. The receiving device translates incoming Unicode characters
                                             					 based on the user locale setting of the sending device's device pool. If the
                                             					 user locale setting matches the terminating phone's user locale, the phone
                                             					 displays the characters. The phone may display junk characters if the two ends of the
                                             					 trunk configure user locales that do not belong to the same language group. |
| Multilevel Precedence and Preemption (MLPP)
                                                						Information |
| MLPP Domain (e.g., "0000FF" ) | Enter a hexadecimal value for the MLPP domain that is
                                             					 associated with this device. Ensure that the value is blank or a value between
                                             					 0 and FFFFFF. |
| Interface Information |
| PRI Protocol Type | Choose the communications protocol for the span: For E1 PRI spans, you have these options: PRI
                                                						AUSTRALIAN—Australian ISDN PRI EURO—European
                                                						ISDN PRI ISO QSIG
                                                						E1—European inter-PBX signaling protocol For T1 PRI spans you have several options, depending on the
                                             					 carrier or switch: PRI 4ESS —AT&T
                                                						interexchange carrier, Lucent Definity switch PRI 5E8
                                                						Custom—CiscoUnifiedIPPhone, Nortel Meridian switch, Lucent Definity switches PRI 5E8
                                                						Teleos—Madge Teleos box PRI 5E8
                                                						Intecom—Intecom PBX PRI5E9—AT&T
                                                						family local exchange switch or carrier PRI NI2—Sprint
                                                						local exchange switch or carrier PRI DMS-100—Sprint
                                                						local exchange switch or carrier PRI DMS-250—MCI
                                                						and Sprint local exchange switch or carrier PRI ETSI
                                                						SC—European local exchange carrier on T1; also, Japanese local exchange. PRI ISO QSIG
                                                						T1—Inter-PBX signaling protocol |
| Protocol Side | Choose the appropriate protocol side. This setting specifies
                                             					 whether the gateway connects to a Central Office/Network device or to a User
                                             					 device. Make sure that the two ends of the PRI connection use opposite
                                             					 settings. For example, if you connect to a PBX and the PBX uses User as its
                                             					 protocol side, choose Network for this device. Typically, use User for Central
                                             					 Office (CO) connections. |
| Channel Selection Order | Choose the order in which channels or ports are enabled from
                                             					 first (lowest number port) to last (highest number port) or from last to first. Valid entries include TOP_DOWN (last to first) or BOTTOM_UP
                                             					 (first to last). If you are not sure which port order to use, choose TOP_DOWN.
                                             					 The default specifies BOTTOM_UP. |
| Channel IE Type | Choose one of the following values to specify whether channel
                                             					 selection is presented as a channel map or a slot map: Number—B-channel
                                                						usage always presents a channel map format. Slotmap—B-channel
                                                						usage always presents a slotmap format. Use Number When
                                                						1B—Channel usage presents a channel map for one B-channel but presents a
                                                						slotmap if more than one B-channel exists. This represents the default value. |
| PUnifiedCMType | Specify the digital encoding format. Choose one of the
                                             					 following formats: a-law: Use for
                                                						Europe and the rest of the world. mu-law: Use for
                                                						North America, HongKong, Taiwan, and Japan. |
| Delay for First Restart | For this optional field, enter the rate, in 1/8-second
                                             					 increments, at which the spans are brought in service. The delay occurs when
                                             					 many PRI spans are enabled on a system and the Inhibit Restarts at PRI
                                             					 Initialization check box is unchecked. The default value specifies 32. For example, set the first five cards to 0 and set the next
                                             					 five cards to 16. (Wait 2 seconds before bringing them in service.) |
| Delay Between Restarts | Enter the time, in 1/8-second increments, between restarts.
                                             					 The delay occurs when a PRI RESTART is sent if the Inhibit Restarts check box
                                             					 is unchecked. The default value specifies 4. |
| Inhibit Restarts at PRI Initialization | A restart message confirms the status of the ports on a PRI
                                             					 span. If RESTARTS are not sent, Cisco Unified Communications Manager assumes that the ports are in service. By
                                             					 default, the box gets checked. When the D-channel successfully connects with another PRI
                                             					 trunk D-channel, it sends restarts when this box is unchecked. |
| Enable Status Poll | Check the check box to enable the Cisco Unified Communications Manager advanced service parameter, Change B-Channel
                                             					 Maintenance Status. This service parameter allows you to take individual
                                             					 B-channels out of service while the B-channels are active. Uncheck this check box to disable the service parameter Change
                                             					 B-Channel Maintenance Status. Default leaves this field unchecked. |
| Unattended Ports | Check this check box to indicate an unattended port on this
                                             					 device. |
| Call Routing Information - Inbound Calls |
| Significant Digits | This field represents the number of final digits that a PRI
                                             					 span should retain on inbound calls. A trunk with significant digits enabled
                                             					 truncates all but the final few digits of the address that is provided on an
                                             					 inbound call. Enable or disable this check box depending on whether you want
                                             					 to collect significant digits: If you do not
                                                						check the check box, Cisco Unified Communications Manager does not truncate the inbound number. If you check the
                                                						check box, you also need to choose the number of significant digits to collect.
                                                						By default, the box remains checked. |
| Calling Search Space | Choose the calling search space for this group of
                                             					 phones/ports. A calling search space specifies the collection of Route
                                             					 Partitions that are searched to determine how a dialed number should be routed. |
| AAR Calling Search Space | Choose the appropriate calling search space for the device to
                                             					 use when it performs automated alternate routing (AAR). The AAR calling search
                                             					 space specifies the collection of route partitions that are searched to
                                             					 determine how to route a collected (originating) number that is otherwise
                                             					 blocked due to insufficient bandwidth. |
| Prefix DN | For this optional field, enter the prefix digits that are
                                             					 appended to the digits that this trunk receives on incoming calls. Cisco Unified Communications Manager adds prefix digits after first
                                             					 truncating the number in accordance with the Num Digits setting. |
| Call Routing Information - Outbound
                                                						Calls |
| Calling Line ID Presentation | Choose whether you want the Cisco Unified Communications Manager to transmit or block the caller’s phone
                                             					 number. Choose Default if you do not want to change calling line ID
                                             					 presentation. Choose Allowed if you want Cisco Unified Communications Manager to send "Calling Line ID Allowed." Choose Restricted if you want Cisco Unified Communications Manager to send "Calling Line ID Restricted." |
| Calling Party Selection | Any outbound call on a gateway can send directory number
                                             					 information. Choose which directory number is sent: Originator—Send
                                                						the directory number of the calling device. This number serves as the default
                                                						value. First Redirect
                                                						Number—Send the directory number of the redirecting device. Last Redirect
                                                						Number—Send the directory number of the last device that redirected the call. |
| Calling Party IE Number Type Unknown | Choose the format for the type of number in calling party
                                             					 directory numbers. Cisco Unified Communications Manager sets the calling directory number (DN)
                                             					 type. Cisco recommends that you do not change the default value unless you have
                                             					 advanced experience with dialing plans, such as NANP or the European dialing
                                             					 plan. You may need to change the default in Europe because Cisco Unified Communications Manager does not recognize European national dialing
                                             					 patterns. You can also change this setting when you are connecting to PBXs that
                                             					 are using routing as a non-national type number. Choose one of the following options: Communications
                                                						Manager—The Cisco Unified Communications Manager sets the directory number type. This
                                                						option represents the default value. International—Use
                                                						when you are dialing outside the dialing plan for your country. National—Use when
                                                						you are dialing within the dialing plan for your country. Unknown—This
                                                						option specifies that the dialing plan is unknown. |
| Called Party IE Number Type Unknown | Choose the format for the type of number in called party
                                             					 directory numbers. Cisco Unified Communications Manager sets the called directory number (DN) type.
                                             					 Cisco recommends that you do not change the default value unless you have
                                             					 extensive experience with dialing plans, such as NANP or the European dialing
                                             					 plan. You may need to change the default in Europe because Cisco Unified Communications Manager does not recognize European national dialing
                                             					 patterns. You can also change this setting when you are connecting to PBXs that
                                             					 use routing as a non-national type number. Choose one of the following options: Communications
                                                						Manager—For the default setting, the Cisco Unified Communications Manager sets the directory number type. International—Use
                                                						when you are dialing outside the dialing plan for your country. National—Use when
                                                						you are dialing within the dialing plan for your country. Unknown—This
                                                						option specifies that the dialing plan is unknown. |
| Called Numbering Plan | Choose the format for the numbering plan in called party
                                             					 directory numbers. Cisco Unified Communications Manager sets the called DN numbering plan.
                                             					 Cisco recommends that you do not change the default value unless you have
                                             					 extensive experience with dialing plans, such as NANP or the European dialing
                                             					 plan. You may need to change the default in Europe because Cisco Unified Communications Manager does not recognize European national dialing
                                             					 patterns. You can also change this setting when you are connecting to PBXs that
                                             					 are using routing as a non-national type number. Choose one of the following options: Communications
                                                						Manager—For the default setting, the Cisco Unified Communications Manager sets the Numbering Plan in the
                                                						directory number. ISDN—Use when you
                                                						are dialing outside the dialing plan for your country. National
                                                						Standard—Use when you are dialing within the dialing plan for your country. Private—Use when
                                                						you are dialing within a private network. Unknown—This
                                                						option specifies that the dialing plan is unknown. |
| Calling Numbering Plan | Choose the format for the numbering plan in calling party
                                             					 directory numbers. Cisco Unified Communications Manager sets the calling DN numbering plan.
                                             					 Cisco recommends that you do not change the default value unless you have
                                             					 extensive experience with dialing plans, such as NANP or the European dialing
                                             					 plan. You may need to change the default in Europe because Cisco Unified Communications Manager does not recognize European national dialing
                                             					 patterns. You can also change this setting when you are connecting to PBXs that
                                             					 are using routing as a non-national type number. Choose one of the following options: Communications
                                                						Manager—For the default setting, the Cisco Unified Communications Manager sets the Numbering Plan in the
                                                						directory number. ISDN—Use when you
                                                						are dialing outside the dialing plan for your country. National
                                                						Standard—Use when you are dialing within the dialing plan for your country. Private—Use when
                                                						you are dialing within a private network. Unknown—This
                                                						option specifies that the dialing plan is unknown. |
| Number of Digits to Strip | Choose the number of digits, from 0 to 32, to strip on
                                             					 outbound calls. The default value specifies 0. For example, 8889725551234 is dialed; the number of digits to
                                             					 strip is 3. In this example, Cisco Unified Communications Manager strips 888 from the outbound number. |
| Caller ID DN | Enter the pattern, from 0 to 24 digits, that you want to use
                                             					 for caller ID. For example, in North America 555XXXX = Variable
                                                						caller ID, where X equals an extension number. The CO appends the number with
                                                						the area code if you do not specify it. 5555000 = Fixed
                                                						caller ID, for when you want the Corporate number to be sent instead of the
                                                						exact extension from which the call is placed. The CO appends the number with
                                                						the area code if you do not specify it. |
| SMDI Base Port | Enter the first SMDI port number of the T1 span. |
| PRI Protocol Type Specific Information |
| Display IE Delivery | For this optional field, check the check box to enable
                                             					 delivery of the display information element (IE) in SETUP and CONNECT messages
                                             					 for the calling and called party name delivery service. By default, the box
                                             					 remains unchecked. |
| Redirecting Number IE Delivery—Outbound | For this optional field, check the check box to include the
                                             					 Redirecting Number IE in the SETUP message to indicate the first redirecting
                                             					 number and the redirecting reason of the call when a call is forwarded. By
                                             					 default, the box remains unchecked. This setting applies to the SETUP message only on all
                                             					 protocols for digital access gateways. |
| Redirecting Number IE Delivery—Inbound | For this optional field, check the check box to include the
                                             					 Redirecting Number IE in the SETUP message to indicate the first redirecting
                                             					 number and the redirecting reason of the call when a call is forwarded. By
                                             					 default, the box remains unchecked. This setting applies to the SETUP message only on all
                                             					 protocols for digital access gateways. |
| Send Extra Leading Character in Display IE | Check this check box to include a special leading character
                                             					 byte (non ASCII, nondisplayable) in the DisplayIE field. Uncheck this check box to exclude this character byte from the
                                             					 DisplayIE field. This check box only applies to the DMS-100 protocol and the
                                             					 DMS-250 protocol. Default leaves this setting disabled (unchecked). |
| Setup of Non-ISDN Progress Indicator IE Enable | For this optional field, you may need to specify a value in
                                             					 this field to force ringback on some PBXs. The default specifies unchecked. Check this check box only if
                                             					 users are not receiving ringback tones on outbound calls. When this setting is enabled, Cisco Unified Communications Manager sends Q.931 setup messages out digital (that
                                             					 is, non-H.323) gateways with the Progress Indicator field set to non-ISDN. This message notifies the destination device that the Cisco Unified Communications Manager gateway is non-ISDN and that the destination
                                             					 device should play inband ringback. This problem usually associates with Cisco Unified Communications Manager s that connect to PBXs through digital
                                             					 gateways. |
| MCDN Channel Number Extension Bit Set to Zero | This field applies to DMS-100 protocol only. Check the check
                                             					 box to indicate that an Interface Identifier is present. By default, the box
                                             					 remains unchecked. |
| Send Calling Name in Facility IE | This field applies to DMS-100 protocol only. Enter the value
                                             					 that you obtained from the PBX provider. Valid values range from 0 to 255. |
| Interface Identifier Present | This field applies to DMS-100 protocol only. Check the check
                                             					 box to indicate that an Interface Identifier is present. By default, the box
                                             					 remains unchecked. |
| Interface Identifier Value | This field applies to DMS-100 protocol only. Enter the value
                                             					 that you obtained from the PBX provider. Valid values range from 0 to 255. |
| Connected Line ID Presentation | Choose whether you want the Cisco Unified Communications Manager to allow or block the connected party’s phone
                                             					 number. Choose Default if you do not want to change the connected line
                                             					 ID presentation. Choose Allowed if you want Cisco Unified Communications Manager to send "Connected Line ID Allowed." Choose Restricted if you want Cisco Unified Communications Manager to send "Connected Line ID Restricted." |
| UUIE Configuration |
| Passing Precedence Level Through UUIE | Check this check box to enable passing MLPP information
                                             					 through the PRI 4ESS UUIE field. This box is used for working along with DRSN
                                             					 switch. The system makes this check box available only if the PRI
                                             					 Protocol Type value of PRI4ESS is specified for this gateway. The default value specifies unchecked. |
| Security Access Level | Enter the value for the security access level. Valid values
                                             					 include 00 through 99. The system makes this field available only if the
                                             					 Passing Precedence Level Through UUIE check box is checked. The default value
                                             					 specifies 2. |
| Geo Location Configuration |
| Geo Location | From the drop-down list box, choose a geo location. You can choose the Unspecified geo location, which designates
                                             					 that this device does not associate with a geo location. You can also choose a geolocation that has been configured
                                             					 with the System > Geolocation
                                                   						  Configuration menu option. |
| Geo Location Filter | From the drop-down list box, choose a geo location filter. If you leave the <None> setting, no geo location filter
                                             					 gets applied for this device. You can also choose a geo location filter that has been
                                             					 configured with the System > Geolocation
                                                   						  Configuration Filter menu option. |
| Product-Specific Configuration The gateway manufacturer specifies the model-specific fields
                                             					 under product-specific configuration. To view field descriptions and help for
                                             					 product-specific configuration items, click the "?" information icon to the right of the Product Specific
                                             					 Configuration heading to display help in a popup window. If you need more
                                             					 information, refer to the documentation for the specific gateway that you are
                                             					 configuring. |

| Field | Description |
|---|---|
| Port Type | From the Port Type drop-down list box, choose
                                             					 POTS. |
| Beginning Port Number Ending Port Number | Choose whether you want to add and configure all available
                                             					 ports, a single port, or a range of ports by setting values for the Beginning
                                             					 Port Number and Ending Port Number fields: To specify a range
                                                						of ports, choose appropriate values for Beginning Port Number and Ending Port
                                                						Number. To create a single
                                                						port, choose the same number in the Beginning Port Number and Ending Port
                                                						Number fields. To add all
                                                						available ports, choose All Ports for both the Beginning Port Number and Ending
                                                						Port Number fields. |
| Port Direction | Choose the direction of calls that pass through this port: Inbound—Use for
                                                						incoming calls only. Outbound—Use for
                                                						outgoing calls. Bothways—Use for
                                                						inbound and outbound calls (default). |
| Audio Signal Adjustment into IP Network | This field specifies the gain or loss that is applied to the
                                             					 received audio signal relative to the port application type. Note Improper gain setting may cause audio echo. Use caution when
                                                         						you are adjusting this setting. | Note | Improper gain setting may cause audio echo. Use caution when
                                                         						you are adjusting this setting. |
| Note | Improper gain setting may cause audio echo. Use caution when
                                                         						you are adjusting this setting. |
| Audio Signal Adjustment from IP Network | This field specifies the gain or loss that is applied to the
                                             					 transmitted audio signal relative to the port application type. Note Improper gain setting may cause audio echo. Use caution when
                                                         						you are adjusting this setting. | Note | Improper gain setting may cause audio echo. Use caution when
                                                         						you are adjusting this setting. |
| Note | Improper gain setting may cause audio echo. Use caution when
                                                         						you are adjusting this setting. |
| Prefix DN | Enter the prefix digits that are appended to the digits that
                                             					 this trunk receives on incoming calls. The Cisco Unified Communications Manager adds prefix digits after it truncates the
                                             					 number in accordance with the Num Digits setting. |
| Num Digits | Enter the number of significant digits to collect, from 0 to
                                             					 32. Cisco Unified Communications Manager counts significant digits from the
                                             					 right (last digit) of the number that is called. Use this field for the processing of incoming calls and to
                                             					 indicate the number of digits starting from the last digit of the called number
                                             					 that are used to route calls that are coming into the PRI span. See Prefix DN. |
| Expected Digits | Enter the number of digits that are expected on the inbound
                                             					 side of the trunk. For this rarely used field, leave zero as the default value
                                             					 if you are unsure. |
| Call Restart Timer (1000-5000 ms) | Call Restart Timer (1000-5000 ms); ms indicates time in
                                             					 milliseconds. |
| Offhook Validation Timer (100-1000 ms) | Offhook Validation Timer (100-1000 ms); ms indicates time in
                                             					 milliseconds. |
| Onhook Validation Timer (100-1000 ms) | Onhook Validation Timer (100-1000 ms); ms indicates time in
                                             					 milliseconds. |
| Hookflash Timer (100-1500 ms) | Hookflash Timer (100-1500 ms); ms indicates time in
                                             					 milliseconds. |
| SMDI Port Number (0-4096) | Use this field for analog access ports that connect to a
                                             					 voice-messaging system. Set the SMDI Port Number equal to the actual port number on
                                             					 the voice-messaging system to which the analog access port connects. Note Voice-mail logical ports typically must match physical ports
                                                         						for the voice-messaging system to operate correctly. | Note | Voice-mail logical ports typically must match physical ports
                                                         						for the voice-messaging system to operate correctly. |
| Note | Voice-mail logical ports typically must match physical ports
                                                         						for the voice-messaging system to operate correctly. |
| Product-Specific Configuration |
| Model-specific configuration fields that the gateway
                                             					 manufacturer defines | The gateway manufacturer specifies the model-specific fields
                                             					 under product-specific configuration. Because they are dynamically configured,
                                             					 they can change without notice. To view field descriptions and help for product-specific
                                             					 configuration items, click the "?" information icon to the right of the Product Specific
                                             					 Configuration heading to display help in a popup dialog box. If you need more information, refer to the documentation for
                                             					 the specific gateway that you are configuring or contact the manufacturer. |

| Note | Improper gain setting may cause audio echo. Use caution when
                                                         						you are adjusting this setting. |
|---|---|

| Note | Improper gain setting may cause audio echo. Use caution when
                                                         						you are adjusting this setting. |
|---|---|

| Note | Voice-mail logical ports typically must match physical ports
                                                         						for the voice-messaging system to operate correctly. |
|---|---|

| Field | Description |
|---|---|
| Port Type | From the Port Type drop-down list box, choose EANDM. |
| Beginning Port Number Ending Port Number | Choose whether you want to add and configure all available
                                             					 ports, a single port, or a range of ports by setting values for the Beginning
                                             					 Port Number and Ending Port Number fields: To specify a range
                                                						of ports, choose appropriate values for Beginning Port Number and Ending Port
                                                						Number. To create a single
                                                						port, choose the same number in the Beginning Port Number and Ending Port
                                                						Number fields. To add all
                                                						available ports, choose All Ports for both the Beginning Port Number and Ending
                                                						Port Number fields. |
| Port Details |
| Port Direction | Choose the direction of calls that pass through this port: Inbound—Use for
                                                						incoming calls only. Outbound—Use for
                                                						outgoing calls. Both Ways—Use for
                                                						inbound and outbound calls. |
| Calling Party Selection | Any outbound call on a gateway can send directory number
                                             					 information. Choose which directory number is sent: Originator—Send
                                                						the directory number of the calling device. First Redirect
                                                						Number—Send the directory number of the redirecting device. Last Redirect
                                                						Number—Send the directory number of the last device to redirect the call. First Redirect
                                                						Number (External)—Send the directory number of the first redirecting device
                                                						with the external phone mask applied. Last Redirect
                                                						Number (External)—Send the directory number of the last redirecting device with
                                                						the external phone mask applied. |
| Caller ID Type | Choose the caller ID type: ANI—Choose this
                                                						type to use the Asynchronous Network Interface (ANI) caller ID type. DNIS—Choose this
                                                						type to use the Dialed Number Identification Service (DNIS) caller ID type. |
| Caller ID DN | Enter the pattern that you want to use for calling line ID,
                                             					 from 0 to 24 digits. For example, in North America: 555XXXX = Variable
                                                						calling line ID, where X equals an extension number. The CO appends the number
                                                						with the area code if you do not specify it. 5555000 = Fixed
                                                						calling line ID, where you want the Corporate number to be sent instead of the
                                                						exact extension from which the call is placed. The CO appends the number with
                                                						the area code if you do not specify it. |
| Prefix DN | Enter the prefix digits that are appended to the called party
                                             					 number on incoming calls. The Cisco Unified Communications Manager adds prefix digits after first truncating the
                                             					 number in accordance with the Num Digits setting. |
| Num Digits | Choose the number of significant digits to collect, from 0 to
                                             					 32. Cisco Unified Communications Manager counts significant digits from the right (last
                                             					 digit) of the number that is called. Use this field if you check the Sig Digits check box. Use this
                                             					 field for the processing of incoming calls and to indicate the number of digits
                                             					 starting from the last digit of the called number that are used to route calls
                                             					 that are coming into the PRI span. See Prefix DN and Sig Digits. |
| Expected Digits | Enter the number of digits that are expected on the inbound
                                             					 side of the trunk. If you are unsure, leave zero as the default value for this
                                             					 rarely used field. |
| Unattended Port | Check this check box to indicate an unattended port on this
                                             					 device. |
| Product-Specific Configuration |
| Model-specific configuration fields that the gateway
                                             					 manufacturer defines | The gateway manufacturer specifies the model-specific fields
                                             					 under product-specific configuration. Because they are dynamically configured,
                                             					 they can change without notice. To view field descriptions and help for product-specific
                                             					 configuration items, click the "?" information icon to the right of the Product Specific
                                             					 Configuration heading to display help in a popup dialog box. If you need more information, refer to the documentation for
                                             					 the specific gateway that you are configuring or contact the manufacturer. |