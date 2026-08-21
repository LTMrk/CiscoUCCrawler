---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-english-serviceability-administration-guide-1-0-1-sasnmpv3-html-e51065f7b2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0/english/serviceability/administration/guide/1_0_1/sasnmpv3.html
retrieved_at: 2026-08-21T16:10:26.028357+00:00
---

Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(1)

# Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(1)

Updated: July 17, 2006

Chapter: SNMP V3 Configuration

## Chapter: SNMP V3 Configuration

- SNMP User Configuration

- SNMP Notification Destination Configuration for V3

- Related Topics

## SNMP V3 Configuration

This chapter, which describes how to configure SNMP v3, so the network management system can monitor Cisco Unified Presence Server, contains the following topics:

• SNMP User Configuration

• SNMP Notification Destination Configuration for V3

Tip If you use SNMP v1 or v2c, see the "SNMP V1/V2c Configuration" section on page 16-1 .

## SNMP User Configuration

Perform the following procedure to configure user(s) for SNMP.

Step 1 Choose Snmp > V3 Configuration > User .

Step 2 From the Server drop-down list box, choose the server where you want to provide access.

Step 3 Perform one of the following tasks:

• To add a new SNMP user, click the Add New button and go to Step 4 .

• To modify an existing SNMP user, click the name of the SNMP user that you want to edit and go to Step 5 .

• To delete an SNMP user, check the check box next to the SNMP user(s) that you want to delete and click Delete Selected . Go to Step 11 .

Step 4 In the User Name field, enter the name of the user for which you want to provide access. The name can contain up to 32 characters and can contain any combination of alphanumeric characters, hyphens (-), and underscore characters (_).

Tip Enter users that you have already configured for the network management system (NMS).

Step 5 To require authentication, check the Authentication Required check box, enter the password in the Password and Reenter Password fields, and choose the appropriate protocol. The password must contain at least 8 characters.

Step 6 If you checked the Authentication Required check box, you can specify privacy information. To require privacy, check the Privacy Required check box, enter the password in the Password and Reenter Password fields, and check the protocol check box. The password must contain at least 8 characters.

Tip After you check the Privacy Required check box, the DES (Data Encryption Standard) check box automatically appears checked. The DES protocol prevents packets from being disclosed.

Step 7 From the Host IP Addresses Information group box, indicate the host from which you want to receive SNMP packets. Choose one of the following options:

• To accept SNMP packets from any host, click the Accept SNMP Packets from any host radio button.

• To accept SNMP packets from specific hosts, click the Accept SNMP Packets only from these host s radio button. In the Host IP Address field, enter a host from which you want to accept SNMP packets and click Insert . Repeat this process for each host from which you want to accept SNMP packets. To delete a host, choose that host from the Host IP Addresses list box and click Remove .

Step 8 From the Access Privileges drop-down list box, choose the appropriate access level.

Step 9 To apply the user configuration to all of the nodes in the cluster, check the Apply To All Nodes check box.

Step 10 Click Insert to save a new user, or click Save to save changes to an existing user.

Step 11 A message indicates that changes will not take effect until you restart the SNMP master agent. To continue the configuration without restarting the SNMP master agent, click Cancel . To restart the SNMP master agent service, click OK .

Tip Cisco recommends that you wait until you finish the SNMP configuration before you restart the SNMP master agent service. For information on how to restart the service, see the "Managing Services" section .

Note To access this Cisco Unified Presence Server server with the user that you configure, make sure that you configure this user on the NMS with the appropriate authentication and privacy settings.

Additional Information

See the Related Topics .

## SNMP Notification Destination Configuration for V3

Perform the following procedure to configure the trap/Inform receiver.

Step 1 Choose Snmp > V3 Configuration > Notification Destination .

Step 2 From the Server drop-down list box, choose the server for which you want to configure notification destination.

Step 3 Perform one of the following tasks:

• To add a new SNMP notification destination, click the Add New button and go to Step 4 .

• To modify an existing SNMP notification destination, click the name of the SNMP notification destination that you want to edit and go to Step 5 .

• To delete an SNMP notification destination, check the check box next to the SNMP notification destination(s) that you want to delete and click Delete Selected . Go to Step 12 .

Step 4 From the Host IP Addresses drop-down list box, choose the Host IP address or choose Add New. If you chose Add New, enter the IP address.

Step 5 In the Port Number field, enter the notification receiving port number on the destination server.

Step 6 From the Notification Type drop-down list box, choose the appropriate notification type.

If you choose Inform, go to Step 7 . If you choose Trap, go to Step 8 .

Tip Cisco recommends that you choose the Inform option. The Inform function retransmits the message until it is acknowledged, thus, making it more reliable than traps.

Step 7 From the Remote SNMP Engine Id drop-down list box, choose the engine ID or choose Add New. If you chose Add New, enter the ID in the Remote SNMP Engine Id field.

Step 8 From the Security Level drop-down list box, choose the appropriate security level for the user.

• noAuthNoPriv—No authentication or privacy configured.

• authNoPriv—Authentication configured, but no privacy configured.

• authPriv—Authentication and privacy configured.

Step 9 From the User Information group box, perform one of the following tasks to associate or disassociate the notification destination with the user.

• To create a new user, click the Create New User button and see the "SNMP User Configuration" section .

• To modify an existing user, check the user check box and click Updated Select User ; then, see the "SNMP User Configuration" section .

• To delete a user, check the check box of the user and click Delete Selected User .

Note The users that display vary depending on the security level that you chose from the previous step.

Step 10 To apply the notification destination to all nodes in the cluster, check the Apply To All Nodes check box.

Step 11 To save a notification destination, click Insert , or click Save to save changes to an existing notification destination.

Step 12 A message indicates that changes will not take effect until you restart the SNMP master agent. To continue the configuration without restarting the SNMP master agent, click Cancel . To restart the SNMP master agent service, click OK .

Tip Cisco recommends that you wait until you finish the SNMP configuration before you restart the SNMP master agent service. For information on how to restart the service, see the "Managing Services" section .

The SNMP v.3 Notification Destination window displays the destination IP address, port number, security model version, security name, level, and notification type.

Additional Information

See the Related Topics .

## Related Topics

• SNMP V1/V2c Configuration, page 16-1

• MIB2 System Group Configuration

• SNMP User Configuration

• SNMP Notification Destination Configuration for V3

• Simple Network Management Protocol, Cisco Unified CallManager Serviceability System Guide