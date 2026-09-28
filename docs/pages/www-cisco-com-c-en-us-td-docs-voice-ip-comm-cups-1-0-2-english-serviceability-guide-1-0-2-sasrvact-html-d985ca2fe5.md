---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-serviceability-guide-1-0-2-sasrvact-html-d985ca2fe5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/serviceability/guide/1_0_2/sasrvact.html
retrieved_at: 2026-08-21T16:05:53.530395+00:00
---

Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Managing Services

## Chapter: Managing Services

## Managing Services

This chapter contains information on the following topics:

• Activating and Deactivating Feature Services

• Starting, Stopping, Restarting, and Refreshing Status of Services in Control Center

• Using a Command Line Interface to Start and Stop Services

## Activating and Deactivating Feature Services

You activate and deactivate services in the Service Activation window in Cisco Unified Presence Server Serviceability. Services that display in Service Activation window do not start until you activate them.

Cisco Unified Presence Server allows you to activate and deactivate feature services. You may activate or deactivate as many services as you want at the same time. Some feature services depend on other services, and the dependent services get activated before the feature service activates.

Perform the following procedure to activate or deactivate Cisco Unified Presence Server services in Cisco Unified Presence Server Serviceability.

Step 1 Choose Tools > Service Activation .

The Service Activation window displays.

Step 2 From the Server drop-down list box, choose the server.

The window displays the service names for the server that you chose and the activation status of the services.

Step 3 Click the Set Default button or activate the services that you want to use by checking the check box next to the service that you want to activate.

Step 4 After you finish making the appropriate changes, click Save .

Tip To deactivate services that you activated, uncheck the check boxes next to the services that you want to deactivate; click Update .

Additional Information

See the Related Topics .

## Starting, Stopping, Restarting, and Refreshing Status of Services in Control Center

Control Center in Cisco Unified Presence Server Serviceability allows you to view status, refresh the status, and to start, stop, and restart Cisco Unified Presence Server services for a particular server in a cluster. Starting, stopping, or restarting a Cisco Presence Server service causes all gateways that are currently registered to that Cisco Presence Server service to fail over to their secondary Cisco Presence Server service. Devices and phones need to restart only if they cannot register with another Cisco Presence Server service. Starting, stopping, or restarting a Cisco Presence Server service causes other installed applications (such as Conference Bridge or Cisco Messaging Interface) that are homed to that Cisco Unified Presence Server to start and stop as well.

Note If you are upgrading Cisco Unified Presence Server, those services that were already started on your system will start after the upgrade.

Perform the following procedure to start, stop, restart, or view the status of services for a particular server in a cluster. You can start, stop, or refresh only one service at a time.

Step 1 Depending on the service type that you want to start/stop/restart/refresh, perform one of the following tasks:

• Choose Tools > Control Center—Feature Services .

Tip You can only start/stop/restart feature services that are activated. To activate a service, see the "Activating and Deactivating Feature Services" section .

• Choose Tools > Control Center—Network Services .

Step 2 From the Server drop-down list box, choose the server.

The window displays the service names for the server that you chose, the service type, and service status. The window also displays the status of the services (Started, Running or Stopped)

Step 3 Perform one of the following tasks:

• Click the radio button next to the service that you want to start and click the Start button.

The Status changes to reflect the updated status.

• Click the radio button next to the service that you want to restart and click the Restart button.

A message indicates that restarting may take a while. Click OK .

• Click the radio button next to the service that you want to stop and click the Stop button.

The Status changes to reflect the updated status.

• To get the latest status of the services, click the Refresh button.

• To go to the Service Activation window or to the other Control Center window, choose an option from the Related Links drop-down list box and click Go .

Additional Information

See the Related Topics .

## Using a Command Line Interface to Start and Stop Services

You can start and stop the following services by issuing a command in the command line interface (CLI):

• System NTP

• System SSH

• Service Manager

• A Cisco DB

• Cisco Tomcat

• Cisco Database Layer Monitor

To start a service, enter utils service start <service name> , where service name equals the entire name of the service.

To stop a service, enter utils service stop <service name> , where service name equals the entire name of the service.

Tip You must start and stop all other services from Control Center in Cisco Unified Presence Server Serviceability.

Additional Information

See the Related Topics .

## Related Topics

• Starting, Stopping, Restarting, and Refreshing Status of Services in Control Center

• Activating and Deactivating Feature Services