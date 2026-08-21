---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmefax-html-ae62890f9b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmefax.html
retrieved_at: 2026-08-21T07:23:27.207464+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Fax Relay

## Chapter: Fax Relay

# Fax Relay

This chapter describes how to enable Skinny Client Control Protocol
                        		(SCCP) Fax Relay for analog foreign exchange service (FXS) ports under the
                        		control of Cisco Unified CME.

## Prerequisites for
                        	 Fax Relay

Cisco Unified CME 4.0(3) or a later version.

If your voice
                                    			 gateway is a separate router than the Cisco Unified CME router, an IP voice
                                    			 image of Cisco IOS Release 12.4(11)T or later is required.

SCCP Telephony
                                    			 Control (STC) application is enabled.

For
                                             				Cisco Unified CME versions before Cisco Unified CME 4.0(3), there are two
                                             				manually-controlled options for setting up facsimiles:

Fax
                                                   					 Gateway Protocol

Configure
                                                   					 the Cisco VG224, FXS port, or analog telephone adaptor (ATA) to use H.323 or
                                                   					 Session Initiation Protocol (SIP) with a specific fax relay protocol. See Fax, Modem, and Text Support
                                                      						over IP Configuration Guide .

G.711 Fax
                                                   					 Pass-Through with SCCP

This is
                                                   					 the default setup for facsimile on the Cisco VG224 and FXS ports before
                                                   					 Cisco Unified CME 4.0(3). See Fax, Modem, and Text Support
                                                      						over IP Configuration Guide .

## Restrictions for
                        	 Fax Relay

RFC2833 dual
                                    			 tone multifrequency (DTMF) digit relay under Cisco Unified CME for SCCP FXS
                                    			 ports is not supported.

SCCP FXS ports
                                    			 under Cisco Unified CME control do not natively support RFC2833 DTMF-relay.
                                    			 However, Cisco Unified CME can support conversion of DTMF digits to and from
                                    			 RFC2833 DTMF-relay on its H323 and SIP interfaces when used with
                                    			 SCCP-controlled FXS ports.

Cisco Fax Relay
                                    			 is only supported on those Cisco IOS gateways and network modules listed in Table 1 .

## Information About Fax Relay

### Fax Relay and Equipment

The fax relay feature supports the use of existing customer premises
                                       			 equipment (CPE) in voice networks by allowing legacy analog phones attached to
                                       			 a Cisco IOS gateway to be controlled by Cisco Unified CME, and by providing
                                       			 feature interoperability between analog and IP endpoints.

The voice gateway can be the same router that is being used for
                                       			 Cisco Unified CME or it may be a separate router (for example, the
                                       			 Cisco VG224).

The fax relay feature facilitates replacement of the PSTN
                                       			 time-division multiplexing (TDM) infrastructure with VoIP.

### Feature Design of
                           	 Cisco Fax Relay

Cisco Fax Relay is a
                              		proprietary fax relay implementation that uses Real-time Transport Protocol
                              		(RTP) to transport fax data. It is the default fax relay type on Cisco voice
                              		gateways and the only supported fax option for Cisco Unified CME 4.0(3) and
                              		later versions. The fax relay feature provides enhanced supplementary feature
                              		capability on analog ports connected to a Cisco integrated services router
                              		(ISR) or Cisco VG224 analog gateway. Calls through the analog FXS ports are
                              		controlled by the Cisco Unified CME system.

Before the
                              		introduction of SCCP-enhanced features, SCCP gateways supported fax
                              		pass-through only. SCCP-enhanced features add support for Cisco Fax Relay and
                              		Super Group 3 (SG3) to G3 fax relay. This feature allows the fax stream between
                              		two SG3 fax machines to negotiate down to G3 speeds (less than 14.4 kbps)
                              		allowing SG3 fax machines to interoperate over fax relay with G3 fax machines.

The SCCP telephony
                              		control (STC) application on the Cisco voice gateway presents the locally
                              		attached analog telephones as individual endpoints to the call-control system,
                              		which allows the analog phones to be controlled in the same way as IP phones.
                              		With this capability, gateway-attached endpoints share the same telephony
                              		features that are available on IP phones directly connected to
                              		Cisco Unified CME. SCCP-enhanced features provide analog endpoint to analog
                              		endpoint interoperability within the IP telephony network.

Cisco Unified CME Fax Relay Deployment shows a multisite deployment of the fax relay feature in a Cisco Unified CME
                              		topology.

For information on
                              		configuring gateway-controlled fax relay features, see Configure Fax Relay .

#### Supported
                              	 Gateways, Modules, and Voice Interface Cards for Fax Relay

Table 1 lists supported gateways, modules, and voice interface cards (VICs).

Gateways

Extension
                                                				  Modules

Network
                                                				  Modules and Expansion Modules

VICs

Cisco
                                                      						2801

Cisco
                                                      						2811

Cisco
                                                      						2821

Cisco
                                                      						2851

Cisco
                                                      						3825

Cisco
                                                      						3845

—

NM-HD-1V

NM-HD-2V

NM-HD-2VE

VIC2-2FXS

VIC-4FXS/DID

VIC2-2BRI-NT/TE

Cisco
                                                      						2801

Cisco
                                                      						2821

Cisco
                                                      						2851

Cisco
                                                      						3825

Cisco
                                                      						3845

EVM-HD

EVM-HD-8FXS/DID

EM-3FXS/4FXO

EM-HDA-8FXS

EM-4BRI-NT/TE

—

Cisco
                                                      						2801

Cisco
                                                      						2811

Cisco
                                                      						2821

Cisco
                                                      						2851

Cisco
                                                      						3825

Cisco
                                                      						3845

—

NM-HDV2

NM-HDV2-1T1/E1

NM-HDV2-2T1/E1

VIC2-2FXS

VIC-4FXS/DID

VIC2-2BRI-NT/TE

Cisco
                                                      						VG 224

—

—

—

## Configure Fax Relay

### Configure Fax
                           	 Relay on SCCP Phones

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- fax protocol cisco

- fax-relay sg3-to-g3

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice service voip

#### Example:

```
Router(config)# voice service voip
```

Enters voice
                                             				service configuration mode and specifies VoIP encapsulation.

Step 4

fax protocol cisco

#### Example:

```
Router(config-voi-serv)# fax protocol cisco
```

Specifies the
                                             				Cisco-proprietary fax protocol as the fax protocol for SCCP analog endpoints.

This
                                                   					 command is enabled by default.

This is
                                                   					 the only supported option for Cisco Unified CME 4.0(3) and later versions.

Step 5

fax-relay sg3-to-g3

#### Example:

```
Router(config-voi-serv)# fax relay sg3-to-g3
```

(Optional)
                                             				Enables the fax stream between two SG3 fax machines to negotiate down to G3
                                             				speeds.

Step 6

exit

#### Example:

```
Router(config-voi-serv)# exit
```

Exits the
                                             				current configuration mode.

### Verify and
                           	 Troubleshoot Fax Relay Configuration

To verify the
                              		Cisco Fax Relay configuration, use the show-running
                                    			 config command. Sample output is located in the Example for Configuring Fax Relay .

Use the following
                              		commands to verify and troubleshoot SCCP gateway-controlled Fax Relay:

show voice call summary —Displays fax relay voice
                                    			 port settings.

show voice dsp —Displays fax relay digital signal
                                    			 processor (DSP) channel status.

debug voip application stcapp all — Displays SCCP
                                    			 telephony control (STC) application fax relay information.

debug voip dsm all —Displays fax relay DSP stream
                                    			 manager (DSM) messages.

debug voip dsmp all —Displays fax relay distributed
                                    			 stream media processor (DSMP) messages.

debug voip hpi all —Displays gateway DSP fax relay
                                    			 information on RTP packet events.

debug voip vtsp all —Displays gateway voice
                                    			 telephony service provider (VTSP) debugging information for fax calls.

For more
                                          		  information on these and other commands, see Cisco IOS Voice Command
                                             			 Reference , Cisco Unified Communications
                                             			 Manager Express Command Reference , and Cisco IOS Configuration
                                             			 Fundamentals Command Reference .

## Configuration Examples for Fax Relay

### Example for Configuring Fax Relay

```
voice service voip
		 fax-relay sg3-to-g3
		
		ephone-dn 44
		 number 1234
		 name fax machine
		
		ephone 33
		 mac-address 1111.2222.3333
		 button 1:44
		 type anl
```

## Feature
                        	 Information for Fax Relay

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Cisco Unified CME Version

Feature
                                             					 Information

Fax Relay

4.0(3)

Enables
                                             					 Fax Relay on analog FXS ports on Cisco IOS voice gateways under the control of
                                             					 Cisco Unified CME.

| Note | For
                                             				Cisco Unified CME versions before Cisco Unified CME 4.0(3), there are two
                                             				manually-controlled options for setting up facsimiles: Fax
                                                   					 Gateway Protocol Configure
                                                   					 the Cisco VG224, FXS port, or analog telephone adaptor (ATA) to use H.323 or
                                                   					 Session Initiation Protocol (SIP) with a specific fax relay protocol. See Fax, Modem, and Text Support
                                                      						over IP Configuration Guide . G.711 Fax
                                                   					 Pass-Through with SCCP This is
                                                   					 the default setup for facsimile on the Cisco VG224 and FXS ports before
                                                   					 Cisco Unified CME 4.0(3). See Fax, Modem, and Text Support
                                                      						over IP Configuration Guide . |
|---|---|

| Gateways | Extension
                                                				  Modules | Network
                                                				  Modules and Expansion Modules | VICs |
|---|---|---|---|
| Cisco
                                                      						2801 Cisco
                                                      						2811 Cisco
                                                      						2821 Cisco
                                                      						2851 Cisco
                                                      						3825 Cisco
                                                      						3845 | — | NM-HD-1V NM-HD-2V NM-HD-2VE | VIC2-2FXS VIC-4FXS/DID VIC2-2BRI-NT/TE |
| Cisco
                                                      						2801 Cisco
                                                      						2821 Cisco
                                                      						2851 Cisco
                                                      						3825 Cisco
                                                      						3845 | EVM-HD | EVM-HD-8FXS/DID EM-3FXS/4FXO EM-HDA-8FXS EM-4BRI-NT/TE | — |
| Cisco
                                                      						2801 Cisco
                                                      						2811 Cisco
                                                      						2821 Cisco
                                                      						2851 Cisco
                                                      						3825 Cisco
                                                      						3845 | — | NM-HDV2 NM-HDV2-1T1/E1 NM-HDV2-2T1/E1 | VIC2-2FXS VIC-4FXS/DID VIC2-2BRI-NT/TE |
| Cisco
                                                      						VG 224 | — | — | — |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice
                                             				service configuration mode and specifies VoIP encapsulation. |
| Step 4 | fax protocol cisco Example: Router(config-voi-serv)# fax protocol cisco | Specifies the
                                             				Cisco-proprietary fax protocol as the fax protocol for SCCP analog endpoints. This
                                                   					 command is enabled by default. This is
                                                   					 the only supported option for Cisco Unified CME 4.0(3) and later versions. |
| Step 5 | fax-relay sg3-to-g3 Example: Router(config-voi-serv)# fax relay sg3-to-g3 | (Optional)
                                             				Enables the fax stream between two SG3 fax machines to negotiate down to G3
                                             				speeds. |
| Step 6 | exit Example: Router(config-voi-serv)# exit | Exits the
                                             				current configuration mode. |

| Note | For more
                                          		  information on these and other commands, see Cisco IOS Voice Command
                                             			 Reference , Cisco Unified Communications
                                             			 Manager Express Command Reference , and Cisco IOS Configuration
                                             			 Fundamentals Command Reference . |
|---|---|

| Feature
                                             					 Name | Cisco Unified CME Version | Feature
                                             					 Information |
|---|---|---|
| Fax Relay | 4.0(3) | Enables
                                             					 Fax Relay on analog FXS ports on Cisco IOS voice gateways under the control of
                                             					 Cisco Unified CME. |