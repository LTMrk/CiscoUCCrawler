---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b02svprm-html-8a1777196f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b02svprm.html
retrieved_at: 2026-08-21T16:10:51.111621+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Service Parameters Configuration

## Chapter: Service Parameters Configuration

- Configuring Service Parameters for a Service on a Server

- Displaying Parameters for a Service

- Related Topics

## Service Parameters Configuration

Service parameters for Cisco Unified Presence Server allow you to configure different services on selected servers. You can view a list of parameters and their descriptions by clicking the question mark button in the Service Parameters Configuration window. You can view the list with a particular parameter at the top by clicking that parameter.

If you deactivate a service by using Cisco Unified Presence Server Serviceability, Cisco Unified Presence Server retains any updated service parameter values. If you start the service again, Cisco Unified Presence Server sets the service parameters to the changed values.

Before You Begin

Ensure the following prerequisites are met before proceeding with the steps:

• Make sure that servers are configured. Refer to the "Server Configuration" section for more information.

• Make sure that the service is available on the servers. The Service Parameter Configuration window displays all the available services (active or not active).

Use the following topics to configure or display service parameters:

• Configuring Service Parameters for a Service on a Server

• Displaying Parameters for a Service

## Configuring Service Parameters for a Service on a Server

Use the following procedure to configure the service parameters for a particular service on a particular server.

Step 1 Choose System > Service Parameters .

Step 2 From the Server drop-down list box, choose a server.

Step 3 From the Service drop-down list box, choose the service that contains the parameter that you want to update.

Note The Service Parameter Configuration window displays all services (active or not active).

The Service Parameters Configuration window displays.

Step 4 Update the appropriate parameter value. To set all service parameters for this instance of the service to the default values, click the Set to Default button.

To view a list of parameters and their descriptions, click the question mark button as shown in Figure 3-1 . To view the list with a particular parameter at the top, click that parameter in the Service Parameters Configuration window.

Figure 3-1 Service Parameter Configuration Window

Note Some services contain service parameters that should rarely be changed. Cisco Unified Presence Server Administration does not automatically display these parameters when you access the Service Parameters Configuration window. To view all parameters, click Advanced . After all parameters display, you can redisplay the basic parameters by clicking Condensed . If the Advanced button is disabled, all parameters for that service display by default.

Step 5 Click Save .

The window refreshes, and Cisco Unified Presence Server updates the service parameter with your changes.

Additional Information

See the "Related Topics" section .

## Displaying Parameters for a Service

You may need to compare all service parameters that belong to a particular service on all servers in a cluster. You may also need to display only out-of-sync parameters (that is, service parameters for which values differ from one server to another) or parameters that have been modified from the suggested value.

Use the following procedure to display the service parameters for a particular service on all servers in a cluster.

Step 1 Choose System > Service Parameters .

Step 2 From the Server drop-down list box, choose a server.

Step 3 From the Service drop-down list box, choose the service for which you want to display the service parameters on all servers in a cluster.

Note The Service Parameter Configuration window displays all services (active or not active).

Step 4 In the Service Parameters Configuration window that displays, choose Parameters for All Servers in the Related Links drop-down list box ; then, click Go .

The Parameters for All Servers window displays. For the current service, the list shows all parameters in alphabetical order. For each parameter, the suggested value displays next to the parameter name. Under each parameter name, a list of servers that contain this parameter displays. Next to each server name, the current value for this parameter on this server displays.

For a given parameter, click on the server name or on the current parameter value to link to the corresponding service parameter window to change the value. Click Previous and Next to navigate between Parameters for All Servers windows.

Step 5 If you need to display out-of-sync service parameters, choose Out of Sync Parameters for All Servers in the Related Links drop-down list box ; then, click Go .

The Out of Sync Parameters for All Servers window displays. For the current service, service parameters that have different values on different servers display in alphabetical order. For each parameter, the suggested value displays next to the parameter name. Under each parameter name, a list of servers that contain this parameter displays. Next to each server name, the current value for this parameter on this server displays.

For a given parameter, click on the server name or on the current parameter value to link to the corresponding service parameter window to change the value. Click Previous and Next to navigate between Out of Sync Parameters for All Servers windows.

Step 6 If you need to display service parameters that have been modified from the suggested value, choose Modified Parameters for All Servers in the Related Links drop-down list box ; then, click Go .

The Modified Parameters for All Servers window displays. For the current service, service parameters that have values different from the suggested values display in alphabetical order. For each parameter, the suggested value displays next to the parameter name. Under each parameter name, a list of servers that have different values from the suggested values displays. Next to each server name, the current value for this parameter on this server displays.

For a given parameter, click on the server name or on the current parameter value to link to the corresponding service parameter window to change the value. Click Previous and Next to navigate between Modified Parameters for All Servers windows.

Additional Information

See the "Related Topics" section .

## Related Topics

• Displaying Parameters for a Service

• Configuring Service Parameters for a Service on a Server