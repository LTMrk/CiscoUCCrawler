---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-serviceability-guide-1-0-2-sasnmpv1-html-053ad8eaa7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/serviceability/guide/1_0_2/sasnmpv1.html
retrieved_at: 2026-08-21T16:06:48.798341+00:00
---

Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: SNMP V1/V2c Configuration

## Chapter: SNMP V1/V2c Configuration

## SNMP V1/V2c Configuration

This chapter, which describes how to configure SNMP versions 1 and 2c, so the network management system can monitor Cisco Unified Presence Server, contains the following topics:

• SNMP Community String Configuration

• SNMP Notification Destination Configuration for V1/V2c

Tip If you use SNMP version 3, see the "SNMP V3 Configuration" section .

## SNMP Community String Configuration

Because the SNMP agent provides security by using community strings, you must configure the community string to access any management information base (MIB) in a Cisco Unified Presence Server system. Change the community string to limit access to the Cisco Unified Presence Server system. To add, modify, and delete community strings, access the SNMP Community String configuration window.

Step 1 Choose Snmp > V1/V2c Configuration > Community String .

Step 2 From the Server drop-down list box, choose the server for which you want to configure a community string.

Step 3 Perform one of the following tasks:

• To add a new community string, click the Add New button and go to Step 4 .

• To modify an existing community string, click the name of the community string that you want to edit and go to Step 5 .

• To delete a community string, check the check box next to the community string(s) that you want to delete and click Delete Selected . A message indicates that the system will delete notification entries that relate to this community string. To continue the deletion, click OK and then go to Step 9 .

Step 4 In the Community String Name field, enter a name for the community string. The name can contain up to 32 characters and can contain any combination of alphanumeric characters, hyphens (-), and underscore characters (_).

Tip Choose community string names that will be hard for outsiders to figure out.

Step 5 From the Host IP Addresses Information group box, indicate from which host you want to receive SNMP packets. Click one of the following options:

• To accept SNMP packets from any host, click the Accept SNMP Packets from any host radio button.

• To accept SNMP only from specified hosts, click the Accept SNMP Packets only from these host s radio button. In the Host IP Address field, enter a host from which you want to accept packets and click Insert . Repeat this process for each host from which you want to accept packets. To delete a host, choose that host from the Host IP Addresses list box and click Remove .

Step 6 From the Access Privileges drop-down list box, choose the appropriate access level from the following list:

• ReadOnly—The community string can only read the values of MIB objects.

• ReadWrite—The community string can read and write the values of MIB objects.

• ReadWriteNotify—The community string can read and write the values of MIB objects and send MIB object values for a trap and inform messages.

• NotifyOnly—The community string can only send MIB object values for a trap and inform messages.

• None—The community string cannot read, write, or send trap information.

Note To change the Cisco Unified Presence Server trap configuration parameters, you need to use a community with NotifyOnly or ReadWriteNotify privileges.

Step 7 To apply the community string to all nodes in the cluster, check the Apply To All Nodes check box.

Step 8 Click Insert to save a new community string or click Save to save changes to an existing community string.

Step 9 A message indicates that changes will not take effect until you restart the SNMP master agent. To continue the configuration without restarting the SNMP master agent, click Cancel . To restart the SNMP master agent service, click OK .

Note Cisco recommends that you wait until you finish all the SNMP configuration before you restart the SNMP master agent service. For information on how to restart the service, see the "Managing Services" section .

The system refreshes and displays the SNMP Community String Configuration window. The community string that you created displays in the window.

Additional Information

See the Related Topics .

## SNMP Notification Destination

Choose the appropriate topic:

• SNMP Notification Destination Configuration for V1/V2c

• SNMP Notification Destination Configuration for V3

## SNMP Notification Destination Configuration for V1/V2c

Perform the following procedure to configure the notification destination (trap/inform receiver) for V1/V2c.

Step 1 Choose Snmp > V1/V2c Configuration > Notification Destination .

Step 2 From the Server drop-down list box, choose the server for which you want to configure notification destination.

Step 3 Perform one of the following tasks:

• To add a new SNMP notification destination, click the Add New button and go to Step 4 .

• To modify an existing SNMP notification destination, click the name of the SNMP notification destination that you want to edit and go to Step 5 .

• To delete an SNMP notification destination, check the check box next to the SNMP notification destination(s) that you want to delete and click Delete Selected . Go to Step 11 .

Step 4 From the Host IP Addresses drop-down list box, choose the Host IP address of the trap destination or choose Add New. If you choose Add New, enter the IP address.

Step 5 In the Port Number field, enter the notification receiving port number on the destination server that receives SNMP packets.

Step 6 From the SNMP Version Information Group pane, click the appropriate SNMP version radio button, either V1 or V2C, which depends on the version of SNMP that you are using.

If you choose V1, continue with Step 8 . If you choose V2C, continue with step Step 7 .

Step 7 From the Notification Type drop-down list box, choose the appropriate notification type.

Step 8 From the Community String drop-down list box, choose the community name to be used in the notification messages that this host generates.

Tip Only community strings with minimum notify privileges (ReadWriteNotify or Notify Only) display. If you have not configured a community string with these privileges, no options appear in the drop-down list box. If necessary, click the Create New button to create a community string. For information on how to create a community string, see the "SNMP Community String Configuration" section .

Step 9 To apply the notification destination to all nodes in the cluster, check the Apply To All Nodes check box.

Step 10 Click Insert to save a notification destination or click Save to save changes to an existing notification destination.

Step 11 A message indicates that changes will not take effect until you restart the SNMP master agent. To continue the configuration without restarting the SNMP master agent, click Cancel . To restart the SNMP master agent, click OK .

Note Cisco recommends that you wait until you finish the SNMP configuration before you restart the SNMP master agent service. For information on how to restart the service, see the "Managing Services" section .

Additional Information

See the Related Topics .

## Related Topics

• SNMP Community String Configuration

• SNMP V3 Configuration

• MIB2 System Group Configuration

• Simple Network Management Protocol, Cisco Unified CallManager Serviceability System Guide

• SNMP Notification Destination Configuration for V1/V2c