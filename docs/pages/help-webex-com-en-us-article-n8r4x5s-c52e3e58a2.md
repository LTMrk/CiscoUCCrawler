---
doc_id: help-webex-com-en-us-article-n8r4x5s-c52e3e58a2
source_url: https://help.webex.com/en-us/article/n8r4x5s
retrieved_at: 2026-11-02T13:06:28.471397+00:00
---

Typically, LLDP-MED contains a location TLV that provides the civic location information.
        Once the LLDP-MED relevant settings are finished on the phone web page, the phone can get
        location from the network switch by the LLDP-MED protocol. When an emergency number is
        dialed, the phone sends its the location information to the emergency responders to help
        them locate the physical address.

Meanwhile, after configuring the LLDP-MED relevant settings, a user can select About this device > Location from the Settings menu on a phone to view the location
        information. Complete details of a physical address include Country, State, District, City,
        Division, Neighborhood block, Street group, Trail. street suffix, Street suffix, House
        number, House number suffix, Landmark, Add. info, Place name, Zip code, Building, Unit,
        Floor, Room, Place type, Post office box, Additional code, Seat, Road, Road section, Road
        branch, Road subsection, Road pre-modifier, and Road post-modifier.

- This feature is only available for the phone lines that are registered call
            controllers that support LLDP MED TLV Location Identification Support. For the phone
            lines registered to Webex Calling, BroadWorks, or Unified CM, the configuration doesn't
            take effect.

- Only the first 255 characters are displayed for each physical address.

Before you begin

Ensure that the network switch has been configured to create a civic location and bind it to an interface on the switch.

After the switch is configured successfully, it can send location information to the phone using the LLDP-MED protocol.

For more information about how to configure the LLDP-MED TLV locations, see Configuring LLDP, LLDP-MED, and Wired Location Service .

Access the phone administration web page.

Select Voice > Ext (n) , where (n) is the phone extension number.

In the Dial Plan section, set the Emergency Number parameter.

In the E911 Geolocation Configuration section, set the following parameters as described in Parameters for LLDP-MED TLV location for emergency calls :

- E911 Enable

- Location Source

- Location Info Schema

- Retransmission Allowed

Click Submit All Changes .

## Parameters for LLDP-MED TLV location for emergency calls

Valid Values: Maximum of 63 characters

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

<Emergency_Number_1_ ua="na">911</Emergency_Number_1_>

Options:

Yes, No

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

<E911_Enable_1_ ua="na" um="y">Yes</E911_Enable_1_>

Options:

LLDP-MED, HELD

If the phone is registered to Webex Calling or BroadWorks, select this option.

If the phone is registered to the call controllers that support LLDP MED TLV Location Identification Support, select this option. Currently, the feature isn't supported on Webex Calling and BroadWorks.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

<Location_Source_1_ ua="na" um="y">LLDP-MED</Location_Source_1_>

Options:

HYBRID,  RFC4119, RFC5139

- HYBRID: PIDF-LO combines the schema defined in RFC4119 and RFC5139 .

- RFC4119: PIDF uses the schema defined in RFC4119.

- RFC5139: PIDF uses the schema defined in RFC5139.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

<Location_Info_Schema_1_ ua="na" um="y">HYBRID</Location_Info_Schema_1_>

Options:

False, True

- False: The "retransmission-allowed" element is set to "false" in PIDF-LO. The recipient is not permitted to share the device location information.

- True: The "retransmission-allowed" element is set to "true" in PIDF-LO. The recipient is permitted to share the device location information.

You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format:

<Retransmission_Allowed_1_ ua="na" um="y">True</Retransmission_Allowed_1_>

| 1 | Access the phone administration web page. |
|---|---|
| 2 | Select Voice > Ext (n) , where (n) is the phone extension number. |
| 3 | In the Dial Plan section, set the Emergency Number parameter. |
| 4 | In the E911 Geolocation Configuration section, set the following parameters as described in Parameters for LLDP-MED TLV location for emergency calls : E911 Enable Location Source Location Info Schema Retransmission Allowed |
| 5 | Click Submit All Changes . |

| Parameter | Default and options | Description |
|---|---|---|
| Section: Dial Plan |
| Emergency Number | Default: Empty Valid Values: Maximum of 63 characters | Specifies the emergency number. For multiple emergency numbers, separate each one with a comma. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Emergency_Number_1_ ua="na">911</Emergency_Number_1_> |
| Section: E911 Geolocation Configuration |
| E911 Enable | Default: Yes Options: Yes, No | Enables or disables the E911 geolocation feature. If set to Yes, the phone will insert geolocation information into the SIP INVITE when placing an emergency call. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <E911_Enable_1_ ua="na" um="y">Yes</E911_Enable_1_> |
| Location Source | Default: HELD Options: LLDP-MED, HELD | Specifies the protocol used to obtain the phone's location information. The supported protocols are: HTTP Enabled Location Delivery (HELD): It contains the device location information in Location URI. If the phone is registered to Webex Calling or BroadWorks, select this option. Link Layer Discovery Protocol-Media Endpoint Discovery (LLDP-MED): It contains the location TLVs that provide the civic location information. The civic location formation contains details about a physical address. If the phone is registered to the call controllers that support LLDP MED TLV Location Identification Support, select this option. Currently, the feature isn't supported on Webex Calling and BroadWorks. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Location_Source_1_ ua="na" um="y">LLDP-MED</Location_Source_1_> |
| Location Info Schema | Default: HYBRID Options: HYBRID,  RFC4119, RFC5139 | Specifies the PIDF format used in the SIP messages. HYBRID: PIDF-LO combines the schema defined in RFC4119 and RFC5139 . RFC4119: PIDF uses the schema defined in RFC4119. RFC5139: PIDF uses the schema defined in RFC5139. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Location_Info_Schema_1_ ua="na" um="y">HYBRID</Location_Info_Schema_1_> |
| Retransmission Allowed | Default: False Options: False, True | Determines whether to allow retransmission of the location information in SIP messages. False: The "retransmission-allowed" element is set to "false" in PIDF-LO. The recipient is not permitted to share the device location information. True: The "retransmission-allowed" element is set to "true" in PIDF-LO. The recipient is permitted to share the device location information. You can configure this parameter in the phone configuration XML file (cfg.xml) by entering a string in this format: <Retransmission_Allowed_1_ ua="na" um="y">True</Retransmission_Allowed_1_> |