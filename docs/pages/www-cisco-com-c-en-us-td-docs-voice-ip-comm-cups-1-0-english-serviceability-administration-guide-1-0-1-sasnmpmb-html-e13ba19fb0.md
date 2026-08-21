---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-english-serviceability-administration-guide-1-0-1-sasnmpmb-html-e13ba19fb0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0/english/serviceability/administration/guide/1_0_1/sasnmpmb.html
retrieved_at: 2026-08-21T16:10:29.826755+00:00
---

Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(1)

# Cisco Unified Presence Server Serviceability Administration Guide, Release 1.0(1)

Updated: July 17, 2006

Chapter: MIB2 System Group Configuration

## Chapter: MIB2 System Group Configuration

- Related Topics

## MIB2 System Group Configuration

Cisco Unified Presence Server Serviceability provides the MIB2 System Group Configuration window where you can configure the system contact and system location objects for the MIB-II system group. For example, you could enter Administrator, 555-121-6633, for the system contact and San Jose, Bldg 23, 2nd floor, for the system location.

Perform the following procedure to configure a system contact and system location for the MIB-II system group.

Tip This procedure supports SNMP v1, v2c, and v3 configuration.

Step 1 Choose Snmp > SystemGroup Configuration > MIB2 System Group Configuration .

Step 2 From the Server drop-down list box, choose the server for which you want to configure contacts.

Step 3 In the Contact field, enter a person to notify when problems occur.

Step 4 In the System Location field, enter the location of the person that is identified as the system contact.

Step 5 To apply the system configuration to all of the nodes in the cluster, check the Apply To All Nodes check box.

Step 6 Click Save .

A message indicates that changes will not take effect until you restart the SNMP master agent.

Step 7 To continue the configuration without restarting the SNMP master agent service, click Cancel . To restart the SNMP master agent service, click OK .

Note To clear the Contact and System Location fields, click the Clear button. To delete the system configuration, click the Clear button and the Save button.

Additional Information

See the Related Topics .

## Related Topics

• Simple Network Management Protocol, Cisco Unified CallManager Serviceability System Guide

• SNMP V1/V2c Configuration, page 16-1

• SNMP V3 Configuration, page 17-1