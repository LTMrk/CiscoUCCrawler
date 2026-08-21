---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-srnd-design-guide-cmesrnd-external-html-e2ddab720e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/srnd/design/guide/cmesrnd/external.html
retrieved_at: 2026-08-21T22:58:12.876722+00:00
---

Cisco Unified CallManager Express Solution Reference Network Design Guide

# Cisco Unified CallManager Express Solution Reference Network Design Guide

Updated: November 2, 2007

Chapter: Integrating External Applications with Cisco Unified CallManager Express

## Chapter: Integrating External Applications with Cisco Unified CallManager Express

## Integrating External Applications with Cisco Unified CallManager Express

Cisco Unified CallManager Express (Cisco Unified CME) can be extended to interface with external applications offered by Cisco and other vendors. This chapter briefly reviews the external applications that you can integrate with Cisco Unified CME, such as applications that use the Telephony Application Programming Interface (TAPI) and Extensible Markup Language (XML) interfaces.

Although Cisco Unity Express is the integrated voice mail system we recommend for use with Cisco Unified CME you also have the option to deploy one of several external voice mail systems with Cisco Unified CME.

See the following documents for more information about Cisco Unity Express and i ntegration with Cisco Unified CME:

• Cisco Unity Express Design Guide http://www.cisco.com/en/US/docs/voice_ip_comm/unity_exp/design/design21/cuedg21.html

• Excerpts from Cisco IP Communications Express: CallManager Express with Cisco Unity Express http://www.cisco.com/en/US/docs/voice_ip_comm/unity_exp/design/CP_CIPExpress/excerpts.html

Other external applications integrate with Cisco Unified CME by using Skinny Client Control Protocol (SCCP) connections. This chapter does not discuss these application because they appear to Cisco Unified CME as IP phones (SCCP endpoints) and not as an application using an application interface, such as TAPI or XML. SCCP applications register with Cisco Unified CME as IP phones do and communicate with the Cisco Unified CME call processing features via SCCP messages as any IP phone would. Applications in this category include softphone PC applications such as the Cisco IP Communicator and IP Blue Software Solutions softphone.

More information about IP Blue can be found at the following URL: http://www.ipblue.com/ .

This chapter addresses integrating Cisco Unified CME to external application in the following sections:

• Cisco Unified CME External Voice Mail Options

• TAPI and XML Application Architecture

• TAPI Applications

• Extensible Markup Language Applications

Note For additional information, see the "Related Documents and References" section on page xii .

## Cisco Unified CME External Voice Mail Options

Cisco Unity Express is the integrated voice mail system we recommend for use with Cisco Unified CME. However, you also have the option to deploy one of several external voice mail systems with Cisco Unified CME. You might want to consider one of these voice mail options for your office in the following situations:

• If you are using a Cisco Unified CME platform, such as the Cisco 1760-V, that does not support Cisco Unity Express (although you could use a separate router to house Cisco Unity Express as of 2.0)

• If your Cisco Unified CME router platform does not have any available slots to add the Cisco Unity Express hardware

• If you require features such as unified messaging that are not yet available with Cisco Unity Express

• If you want to deploy a centralized voice mail system to support multiple Cisco Unified CME sites instead of a distributed voice mail option at each site

• If you have an existing legacy voice mail system that you want to continue to use

This chapter briefly reviews the external voice mail options available for use with Cisco Unified CME. These options include the Cisco Unity voice mail system and several nonCisco systems that integrate with Cisco Unified CME via either H.323 Voice over IP (VoIP) or an analog phone interface.

### Cisco Unity Voice Mail

Cisco Unity is a Microsoft Windows 2000 server-based IP unified messaging system. Cisco Unity scales up to several thousand users and typically is deployed in a central site of an enterprise network with a Cisco CallManager providing the call control.

Note Note that Cisco Unity and Cisco Unity Express are two different voice mail systems. Cisco Unity Express is a hardware module installed inside the Cisco Unified CME router scaling up to 100 voice mailboxes, whereas Cisco Unity is a separate Windows server platform scaling up to thousands of users.

Cisco Unity unified messaging capabilities allow you to integrate voice mail, e-mail, and faxes into the same end-user mailbox. The mailbox operation is highly customizable via call handlers. Cisco Unity provides options for integrating with the Microsoft Outlook or Lotus Notes mail architectures. Cisco Unity leverages Active Directory to access your network's user and location directory.

Although Cisco Unity unified messaging features provide many productivity-enhancing applications such as Cisco Personal Assistant and text-to-speech support, you can also choose to deploy it as a voice mail-only system. Cisco Personal Assistant is a telephony application suite that streamlines communications by helping users manage how and where they can be reached.

Different levels of licensing are available with Cisco Unity for a voice mail-only deployment or a full unified messaging system. Cisco Unity is a sophisticated messaging system with robust failover and networking options.

Cisco Unity uses IP as the transport and SCCP for call control, appearing to Cisco Unified CME as an IP phone (SCCP) endpoint. Cisco Unity can support a single Cisco Unified CME in a standalone deployment or can be deployed at a central site in your network with multiple Cisco Unified CMEs at remote sites in a centralized voice mail scenario. These architectures are discussed further in the following sections.

Note Cisco Unified CME is Cisco IOS software-based, whereas Cisco Unity is a Microsoft Windows 2000-based application; therefore, users considering this combination of applications should have a good working knowledge of both operating systems. Cisco Unity uses Microsoft Exchange (5.5, 2000, and 2003) or Lotus Domino mail stores, so familiarity with these technologies is also beneficial.

### Standalone Cisco Unified CME System with Cisco Unity

You can connect a standalone Cisco Unified CME with a dedicated Cisco Unity system to provide unified or voice mail services to a single site. Although technically feasible, this is often not a cost-effective way to deploy Cisco Unity. Cisco Unity is an application designed to support large numbers of users, whereas Cisco Unified CME can support only up to 240 users. Figure 8-1 shows how Cisco Unified CME is connected to the Cisco Unity system.

Although Cisco Unified CME functions as the call control system for taking care of IP phone and PSTN calls, Cisco Unity provides the voice mail services. Cisco Unity communicates with Cisco Unified CME using SCCP emulating IP phone endpoints.

Figure 8-1 Standalone Cisco Unified CME with Cisco Unity Messaging

### Multiple Cisco Unified CME Systems with a Centralized Cisco Unity System

A much more typical and cost-effective model of using Cisco Unity with Cisco Unified CME is as a centralized messaging system to several remote Cisco Unified CME sites. Figure 8-2 shows multiple Cisco Unified CME systems distributed across several smaller sites connected to a shared, centralized Cisco Unity system. A Cisco Unified CME system at the central site collocated with the Cisco Unity server is required. This Cisco Unified CME relays both voice and message waiting indicator (MWI) to the remote sites.

A centralized Cisco Unity system offers several advantages:

• It eases the management and provisioning of voice mail.

• It provides a single integrated user directory that eases sending voice mail and setting up distribution lists across users physically located at different sites.

• It facilitates forwarding and replying to voice messages without requiring networking of the distributed voice mail systems between the individual sites.

• It conserves valuable bandwidth by not forwarding and replying to voice mails between users resident at different sites.

### Configuring Cisco Unified CME for Cisco Unity

Cisco Unity integrates with Cisco Unified CME as SCCP-controlled IP phone endpoints. Each voice mail port on Cisco Unity is configured as an ephone on Cisco Unified CME, and the voice mail pilot number is configured as an ephone-dn that appears on each of the phones (ports).

Figure 8-2 Multiple Cisco Unified CME Systems with Cisco Unity Messaging

The Cisco Unity ports register with the Cisco Unified CME router using a voice mail device ID (vm-device-id) such as Cisco UM-VI2. The following example shows the Cisco Unified CME configuration for connecting to a four-port Cisco Unity voice mail system.

```
telephony-service
```

```
voicemail 6800
```

```
!
```

```
ephone-dn 32
```

```
number 6800
```

```
name "VM Port 1"
```

```
preference 0
```

```
no huntstop
```

```
!
```

```
ephone-dn 33
```

```
number 6800
```

```
name "VM port 2"
```

```
preference 1
```

```
no huntstop
```

```
!
```

```
ephone-dn 34
```

```
number 6800
```

```
name "VM port 3"
```

```
preference 2
```

```
no huntstop
```

```
!
```

```
ephone-dn 35
```

```
number 6800
```

```
preference 3
```

```
name "VM Port 4"
```

```
ephone 5
```

```
vm-device-id CiscoUM-VI1
```

```
button 1:32
```

```
!
```

```
ephone 6
```

```
vm-device-id CiscoUM-VI2
```

```
button 1:33
```

```
!
```

```
ephone 7
```

```
vm-device-id CiscoUM-VI3
```

```
button 1:34
```

```
!
```

```
ephone 8
```

```
vm-device-id CiscoUM-VI4
```

```
button 1:35
```

The voicemail 6800 command defines the voice mail pilot number as extension 6800. You can define an ephone-dn for each of the four ports; these definitions control call routing to Cisco Unity. All the ephone-dns have 6800 as the extension and are tagged with preference 0 to preference 3 . You need four individual ephone-dns, one per port, to route and deliver four calls to the Cisco Unity system simultaneously. From the Cisco Unified CME system point of view, four IP phones have an appearance of extension 6800; therefore, four individual calls to 6800 can be busy at the same time.

The preference and no huntstop designations ensure that the Cisco Unified CME system hunts across the available phones if some of them are busy.

Each of the physical ports is defined as an ephone. To Cisco Unified CME, Cisco Unity ports look like an IP phone, and they register as such. The vm-device-id (for example, Cisco UM-VI2) defined for each ephone must match the device ID configured in the Cisco Unity configuration.

You configure call forwarding to voice mail on your employee's IP phones exactly as you would for Cisco Unity Express, as shown in the following example.

```
ephone-dn 1
```

```
number 6001
```

```
call-forward busy 6800
```

```
call-forward noan 6800 timeout 10
```

With the configurations given in the previous examples, users on your system can press the messages button on their IP phones to retrieve their voice mail. They can also call the voice mail pilot number 6800 directly—for example, from the PSTN—to access their voice mail.

### MWI

MWI with Cisco Unity is accomplished via outdial directory numbers (DNs), similar to the architecture with Cisco Unity Express (but not configured in exactly the same way). Cisco Unified CME defines two MWI DNs, one for turning on MWI and another for turning it off. Cisco Unity outdials to one of these numbers to control the phone's MWI state. This configuration is shown in the following example.

```
ephone-dn 30
```

```
number 8000
```

```
mwi on
```

```
!
```

```
ephone-dn 31
```

```
number 8001
```

```
mwi off
```

The extension for which MWI must be turned on or off is derived from the caller ID (the number of the call's originator) provided in the SCCP message received by Cisco Unified CME. Cisco Unity populates the appropriate caller ID in the SCCP message sent to Cisco Unified CME when it initiates the call to one of the MWI DNs. Cisco Unified CME then uses this caller ID to determine which IP phone on the system should receive MWI and sends a separate SCCP message to the phone(s) to turn its MWI on or off.

The MWI configuration for Cisco Unity differs from that of Cisco Unity Express in two important ways:

• For Cisco Unity Express, the MWI DN requires wildcard dots following the MWI extension number (as many dots as you have digits in your extensions). For four-digit extensions, the MWI DN for Cisco Unity Express would specify number 8000.... instead of the number 8000 command used for Cisco Unity.

• For Cisco Unity Express, the IP phone extension for which MWI must be turned on or off is derived from the digits that match the dots just described—that is, from the called number of the outgoing call to the MWI DN. For Cisco Unity, the IP phone extension is derived from the calling number of the outgoing call to the MWI DN.

### MWI Relay

Cisco Unity physically integrates only with the single Cisco Unified CME that is collocated with it. All the Cisco Unity ports register with this Cisco Unified CME system. To get Cisco Unity to support voice mail for users of Cisco Unified CME systems at remote sites, certain information must be relayed by the central Cisco Unified CME that is physically connected to Cisco Unity.

Calls to Cisco Unity to leave or retrieve messages can be freely routed across your network between the sites based on your dial plan. The relay mechanism comes into play only for getting MWI notifications to an IP phone at a remote site.

Cisco Unified CME contains an MWI relay mechanism that is configured at the central Cisco Unified CME (the one with the MWI DNs that Cisco Unity dials). The central Cisco Unified CME cannot send an SCCP message directly to an IP phone that is registered with a different Cisco Unified CME system. Instead, it uses a Session Initiation Protocol (SIP) subscribe/notify mechanism to notify the remote Cisco Unified CME of an MWI change. The remote Cisco Unified CME system (where the IP phone is registered) then sends an SCCP message to the phone to change its MWI state. This configuration is shown in Figure 8-3 .

Figure 8-3 MWI Relay with Cisco Unity

The MWI relay configuration at the central Cisco Unified CME (site A) is shown in the following example.

```
telephony-service
```

```
ip source-address 10.10.10.1
```

```
mwi relay
```

```
mwi expires 99999
```

```
voicemail 6800
```

The mwi relay command lets the Cisco Unified CME router relay the MWI information to a remote IP phone. The mwi expires command sets the expiry timer for the SIP subscribe/notify registration.

The MWI relay configuration at one of the remote Cisco Unified CME sites (for example, site B) is shown in the following example.

```
telephony-service
```

```
ip source-address 10.20.20.10
```

```
mwi sip-server 10.10.10.1 transport tcp
```

```
!
```

```
ephone-dn 1
```

```
number 2000
```

```
mwi sip
```

```
call-forward noan 6800 timeout 10
```

```
call-forward busy 6800
```

```
!
```

```
dial-peer voice 101 voip
```

```
destination-pattern 6800
```

```
session target ipv4:10.10.10.1
```

```
codec g711ulaw
```

```
dtmf-relay h245-alphanumeric
```

```
no vad
```

The mwi sip-server command instructs the Cisco Unified CME at site B to subscribe to the SIP server on Cisco Unified CME site A (IP address 10.10.10.1 in preceding example). Each of the ephone-dns at sites B and C must contain the mwi sip command to ensure that the controlling Cisco Unified CME system knows that this phone's MWI is controlled by a SIP notification from another site. As soon as the configuration is entered, a show mwi relay clients command executed at site A shows all the extensions subscribed to the Cisco Unified CME site A SIP server.

The dial peer shown in the preceding example ensures that users at site B can dial 6800 (the voice mail pilot number). The call is routed across VoIP to site A, where the Cisco Unity system is located.

### Stonevoice Voice Mail

Cisco Unified CME can integrate with various nonCisco voice mail systems using H.323. One of the H.323 voice systems supported by Cisco Unified CME is the Stonevoice Switch Answering Machine (SSAM), a unified messaging system designed to provide access to and control over software-based voice mail services.

SSAM is a Windows 2000-based application that runs on an external PC. All traffic between Cisco Unified CME and SSAM uses H.323. Figure 8-4 shows how the Stonevoice SSAM application integrates with Cisco Unified CME.

Figure 8-4 Cisco Unified CME with Stonevoice SSAM Voice Mail

When integrated with Cisco Unified CME, SSAM supports the following:

• Direct access to voice mail

• Call forward no answer (CFNA) or call forward busy (CFB) to a personal greeting

• MWI

For more information on the SSAM system, go to http://www.stonevoice.com/ .

The following sections provide more details on integrating a Stonevoice system with Cisco Unified CME, including

• Configuring Cisco Unified CME for Stonevoice

• MWI for Stonevoice

### Configuring Cisco Unified CME for Stonevoice

Communication between Cisco Unified CME and SSAM is by H.323, so you have to configure an H.323 dial peer to direct calls into the SSAM system. You must configure a voice mail pilot number (for example, 9999) on SSAM for message retrieval and an individual voice mail number for each extension (ephone-dn). Because the original called number (the IP phone extension) is not preserved when the call is forwarded to SSAM via H.323, you must embed this information in the called number (the call forward number) delivered to SSAM.

The following example shows a sample Cisco Unified CME configuration defining a voice mail pilot number of 9999 (used when you press the messages button on your IP phone), voice mail number 9001 for extension 1001, and 9002 for extension 1002.

```
dial-peer voice 100 voip
```

```
destination-pattern 9...
```

```
session target ipv4:172.19.153.120
```

```
dtmf-relay h245-alphanumeric
```

```
codec g711ulaw
```

```
no vad
```

```
!
```

```
telephony-service
```

```
voicemail 9999
```

```
!
```

```
ephone-dn 1
```

```
number 1001
```

```
call-forward busy 9001
```

```
call-forward noan 9001 timeout 10
```

```
!
```

```
ephone-dn 2
```

```
number 1002
```

```
call-forward busy 9002
```

```
call-forward noan 9002 timeout 10
```

The voice dial peer command destination-pattern 9... ensures that all calls to 9999, 9001, and 9002 are directed to SSAM via H.323. The IP address 172.19.153.120 in this example belongs to the SSAM system.

The voicemail 9999 command under telephony service is the voice mail pilot number used when you press the messages button on your IP phone. This number must match the "Voicemail number" parameter on the SSAM Modify IP Telephony System window.

Individual voice mail forwarding numbers are defined for each extension. These are used in the call-forward busy and call-forward noan fields of the ephone-dn Cisco Unified CME configuration. These numbers must be configured on the SSAM system for each individual user. For example, for the person on ephone-dn 1, you configure his or her extension (1001) in the "First extension number" field, and configure 9001 in the "Voicemail number" field of the SSAM Account Management window for this user.

### MWI for Stonevoice

MWI is controlled by the SSAM system outdialing with H.323 to a Cisco Unified CME MWI DN. The extension for which the MWI must be turned on or off is embedded in the dialed number. The Cisco Unified CME configuration for this is shown in the following example.

```
ephone-dn 11
```

```
number 8000*....*1 secondary 8000*....*2
```

```
mwi on-off
```

```
no huntstop
```

```
!
```

```
ephone-dn 12
```

```
number 8000*....*1 secondary 8000*....*2
```

```
mwi on-off
```

```
preference 1
```

You should configure as many of these MWI ephone-dns as you have "ports" on the SSAM system so that the maximum number of simultaneous calls can be handled correctly. Use the Cisco Unified CME preference and no huntstop command designations to make sure the Cisco Unified CME system hunts across any available MWI ephone-dns.

When the SSAM system makes an outgoing call to Cisco Unified CME, the MWI information is embedded in the called party's telephone number—for example, 8000*1001*1 or 8000*1001*2. The 8000 is the MWI DN's number, and the asterisks are used as delimiters. The extension for which MWI should be turned on or off is contained between the asterisks, and the final digit in the string specifies whether MWI is on (1) or off (2).

The notation 8000*....*1 in the ephone-dn definition accepts any extension number and represents the extension digits that Cisco Unified CME extracts to determine for which IP phone to turn MWI on or off. The MWI on (ending in digit 1) and MWI off (ending in digit 2) strings are given on the same ephone-dn as the primary and secondary extensions on that ephone-dn, as shown in the preceding example.

### Analog Voice Mail

You can integrate Cisco Unified CME with analog systems to provide voice mail services, as shown in Figure 8-5 . In general, these systems connect to the Cisco Unified CME via Foreign Exchange Station (FXS) analog phone interfaces. Each port is configured as a normal plain old telephone service (POTS) dial peer in Cisco Unified CME.

Figure 8-5 Cisco Unified CME with Analog Voice Mail

Cisco Unified CME interacts with the analog voice mail system via inband dual-tone multifrequency (DTMF) tones. All call routing and MWI information exchanged between Cisco Unified CME and the voice mail system also occurs via DTMF tones.

When integrated with Cisco Unified CME, an analog voice mail system provides the following:

• Direct access to voice mail

• CFNA or CFB to a personal greeting

• MWI

Many types of analog voice mail systems are available. The Octel system from Avaya and the Reception system from Active Voice, LLC are two of the more popular models. The following sections discuss Cisco Unified CME integration with these systems.

### Octel

Integrating the Octel voice mail system with Cisco Unified CME requires configuration on both systems. The configuration sample in the following example shows how to configure the Cisco Unified CME.

```
call application voice bator flash:app-h450-transfer.2.0.0.9.tcl
```

```
call application voice bator language 1 en
```

```
call application voice bator set-location en 0 flash:/prompts
```

```
!
```

```
voice-port 1/0/0
```

```
caller-id enable
```

```
!
```

```
voice-port 1/0/1
```

```
caller-id enable
```

```
!
```

```
dial-peer voice 5000 pots
```

```
application bator
```

```
destination-pattern 5000.....
```

```
port 1/0/0
```

```
!
```

```
telephony-service
```

```
voicemail 5000
```

```
transfer-system full-consult
```

```
!
```

```
vm-integration
```

```
pattern direct 2 CGN
```

```
pattern ext-to-ext no-answer 5 CGN * FDN
```

```
pattern ext-to-ext busy 7 CGN * FDN
```

```
pattern trunk-to-ext no-answer 5 CGN * FDN
```

```
pattern trunk-to-ext busy 7 CGN * FDN
```

```
!
```

```
ephone-dn 1
```

```
number 1000
```

```
call-forward busy 5000
```

```
call-forward noan 5000 timeout 5
```

```
application bator
```

```
no huntstop
```

```
!
```

```
ephone-dn 2
```

```
number 1001
```

```
call-forward busy 5000
```

```
call-forward noan 5000 timeout 5
```

```
application bator
```

```
!
```

```
ephone-dn 100
```

```
number 3000*....*
```

```
mwi on
```

```
!
```

```
ephone-dn 101
```

```
number 3001*....*
```

```
mwi off
```

The Tool Command Language (TcL) application (called bator in the preceding configuration) is used to support a hookflash operation on the FXS ports. FXS port 1/0/0 is used for voice mail access, so the POTS dial peer points to this port. Port 1/0/1 is used for MWI operation.

The series of vm-integration commands specifies the DTMF digit strings to be generated to the analog voice mail system to control feature operation, such as selecting which greeting (external or internal, or busy or no answer) to play to the caller. The MWI DNs have asterisk delimiters surrounding the wildcards that match the extension number for which MWI must be turned on or off.

Note the following restrictions when integrating an Octel system with Cisco Unified CME:

• One FXS port must be dedicated for MWI operation.

• The Octel system must have analog ports and must be configured for analog DTMF integration. Digital and Simplified Message Desk Interface (SMDI) integration with Unified CME is not supported.

• The Octel system does not distinguish between extension-to-extension and trunk-to-extension transfers. Thus, you must configure the DTMF patterns for these transfers with the same values on the Cisco Unified CME system.

• The MWI ephone-dn must use the . wildcard rather than the T wildcard to specify the exact extension length. Also, you must use an asterisk before and after configuring the called party ID (for example, number 3000*....* ).

### Active Voice Reception

The Reception system from Active Voice, LLC is another popular voice mail system. To allow calls to be forwarded to the Reception system, you must configure Cisco Unified CME with four different DTMF patterns for the following four possible call flows:

• Extension-to-extension no answer

• Extension-to-extension busy

• Extension-to-trunk no answer

• Extension-to-trunk busy

When the Reception system receives the DTMF pattern, it plays the corresponding voice mail prompt.

The following example shows how to configure Cisco Unified CME to work with the Reception voice mail system.

```
voice-port 1/0/0
```

```
caller-id enable
```

```
!
```

```
voice-port 1/0/1
```

```
caller-id enable
```

```
!
```

```
dial-peer voice 5000 pots
```

```
application bator
```

```
destination-pattern 6800.....
```

```
port 1/0/0
```

```
!
```

```
telephony-service
```

```
voicemail 6800
```

```
!
```

```
vm-integration
```

```
pattern direct 2 CGN *
```

```
pattern ext-to-ext no-answer 5 FDN * CGN *
```

```
pattern ext-to-ext busy 7 FDN * CGN *
```

```
pattern trunk-to-ext no-answer 4 FDN * CGN *
```

```
pattern trunk-to-ext busy 6 FDN * CGN *
```

```
!
```

```
phone-dn 2
```

```
number 3002
```

```
call-forward busy 6800
```

```
call-forward noan 6800 timeout 10
```

```
!
```

```
ephone-dn 25
```

```
number A1.....*
```

```
mwi on
```

```
!
```

```
ephone-dn 26
```

```
number A2.....*
```

```
mwi off
```

### PSTN-Based Voice Mail

Another option for voice mail with Cisco Unified CME is through your PSTN provider. The call flows to the voice mail from your PSTN provider are controlled by the central office (CO) PSTN switch. If the lines to your business are busy or don't answer, the voice mail system at the CO picks up and stores the senders' voice messages at the voice mail storage located at the CO. You do not need to configure Cisco Unified CME for this type of voice mail. You do need to configure MWI, however.

CO-based voice mail systems signal MWI by using stutter dial tone. When you go off-hook on your phone, you hear the tone and know you have a message. This works well if you use an analog phone directly connected to the CO and you, therefore, get dial tone from the CO. If you have a Cisco Unified CME system in your office with IP phones on, however, dial tone comes from the Cisco Unified CME system, not from the CO.

To hear stutter dial tone provided by a CO-based voice mail system, you can use the Cisco Unified CME 3.2 FXO Trunk Line Select feature by pressing a button on your IP phone. It directly selects a CO Foreign Exchange Office (FXO) line, which gets dial tone from the CO, and you can hear stutter dial tone.

The following example shows how to use the trunk command to create a direct connection to a CO line on an IP phone.

```
voice-port 1/0/0
```

```
connection plaropx 1082
```

```
dial-peer voice 82 pots
```

```
destination-pattern 82
```

```
port 1/0/0
```

```
forward-digits 0
```

```
ephone-dn 10
```

```
number 1010
```

```
name manager
```

```
ephone-dn 11
```

```
number 1082
```

```
name private-line
```

```
trunk 82
```

```
ephone 1
```

```
button 1:10 2:11
```

Example 11-10 shows the following sequence of events:

• You press the softkey 2 on your phone, and it automatically triggers the configuration for ephone-dn 11.

• ephone-dn 11 initiates a call to 82, which matches the dial peer that points to FXO line 1/0/0.

• When line 1/0/0 goes off-hook (as if you had picked up an analog phone set directly connected to the CO), it does not dial any digits. The impact is that you can hear the dial tone provided by the CO.

## TAPI and XML Application Architecture

TAPI applications interface directly with the Cisco Unified CME call processing software to control the call processing signaling events that apply to an IP phone. For example, a TAPI application can answer a call on behalf of a phone, make the phone go off-hook, or disconnect a call. Microsoft Windows software-based screen-pop applications typically use TAPI.

XML applications interface directly with the IP phone and leverage its HTTP capabilities. The phone has one or more URLs as part of its software load that it accesses when buttons such as the services or directory keys are pressed. The XML application renders some text or graphics on the phone's display. Cisco Unified CME call processing is not involved in this application interchange. XML applications control the phone display while the phone is idle (that is, not on a call).

Figure 8-6 shows how TAPI and XML applications interface with Cisco Unified CME and its IP phones. The left side of the figure depicts a TAPI application. An employee has an IP phone and PC on the desktop. The PC runs a productivity application, such as a contact management application, that provides a screen pop based on caller ID whenever a call starts ringing. All messaging between the application and the phone passes through Cisco Unified CME and is interpreted by the Cisco Unified CME software. On the right side of the figure is an XML application. The phone has a URL that points to a server. The server application writes to the phone display using HTTP.

Figure 8-6 TAPI and XML Application Architecture

## TAPI Applications

TAPI is a Microsoft software application interface for integrating-telephony-services into Microsoft Windows software-based PC applications. Cisco Unified CME provides telephony services by a TAPI Service Provider (TSP) interface to applications.

The TSP allows TAPI-based applications such as Microsoft Outlook and Microsoft Customer Relationship Management (CRM) to provide call control to the IP phones connected to Cisco Unified CME. Other TAPI-based applications are available in the industry, such as automatic dialers. You can use these applications to control an IP phone to make and receive calls via a computer or to trigger database lookups based on caller ID.

The following sections describe TAPI in more detail, including the following topics:

• Cisco Unified CME TAPI Light

• Cisco Unified CME TSP Functions

• Cisco CRM Communications Connector

### Cisco Unified CME TAPI Light

Cisco Unified CME offers a TAPI Light capability, which is not a full TAPI implementation but a selection of the applicable components for Cisco Unified CME. The implementation consists of two parts: one part resides on the Windows platform, and the other part resides in Cisco Unified CME Cisco IOS software.

The interface between the TSP in the Microsoft Windows application and Cisco Unified CME uses SCCP over TCP. Cisco Unified CME listens on a standard TCP port, while the TAPI client authenticates to Cisco Unified CME by providing a username and password unique for each IP phone on Cisco Unified CME. The Microsoft Windows application's TSP must have the same username, password, and port number configured to be able to connect successfully with Cisco Unified CME and exert phone and call control. The username and password authentication provides a layer of security to Cisco Unified CME to enable authorized application development.

The following example shows the configuration of the username and password associated with the IP phone on Cisco Unified CME. This information must be quoted by the TAPI application during login to be able to control the phone. The telephony-service ip source-address command specifies the port number used for communication between Cisco Unified CME and the TAPI application.

```
telephony-service
```

```
ip source-address 172.19.153.129 port 2000
```

```
!
```

```
ephone-dn 1
```

```
number 3001
```

```
description User1
```

```
name User1
```

```
call-forward busy 3105
```

```
call-forward noan 3105 timeout 10
```

```
!
```

```
ephone 1
```

```
username "User 1" password user1
```

```
mac-address 0009.B7F7.5793
```

```
speed-dial 4 3100 label "AA"
```

```
button 1:1
```

You can verify IP phone TAPI application login status with the show ephone login Cisco Unified CME command.

### Cisco Unified CME TSP Functions

The Cisco Unified CME TSP provides the following functions:

• Allows multiple addresses on a single line.

• Makes calls using address book dialing from applications.

• Answers or rejects calls.

• Holds calls using window pop-ups.

• Provides caller ID information to applications.

• Places calls on hold and switches between active calls.

• Transfers calls.

When using TAPI applications with Cisco Unified CME, consider the following restrictions:

• Media or voice termination is not supported. Media or voice traffic is sent to the phone. The TAPI application has access only to signaling events.

• TAPI clients can operate on only one phone line at a time.

• Multiple users and call handling of multiple calls on a single client are not supported.

• Java TAPI (JTAPI) is not supported.

We have partnered with independent TAPI developers to provide support for TAPI development.

Table 8-1 lists the TAPI and TSP functions supported in the Cisco Unified CME TSP.

Table 8-1 Supported Cisco Unified CME TAPI/TSP Functions

lineAnswer

TSPI_lineAnswer

Answers the specified offered call.

lineBlindTransfer

TSPI_lineBlindTransfer

Performs a blind or single-step transfer of the specified call to the specified destination address.

lineClose

TSPI_lineCloseCall

Closes the specified open line device after completing or aborting all outstanding calls and asynchronous operations on the device.

lineCompleteTransfer

TSPI_lineCompleteTransfer

Completes the transfer of the specified call to the party connected in the consultation call.

lineDial

TSPI_lineDial

Dials the specified dialable number on the specified call.

lineDrop

TSPI_lineDrop

Drops or disconnects the specified call.

lineGetAddressID

TSPI_lineGetAddressID

Returns the address identifier associated with the address in a different format on the specified line.

TSPI_lineGetCallAddressID

Retrieves the address identifier for the indicated call.

lineGetCallInfo

TSPI_lineGetCallInfo

Returns detailed information about the specified call.

TAPI Function

TSP Function

Description of function.

lineGetCallStatus

TSPI_lineGetCallStatus

Returns the current status of the specified call.

lineGetDevConfig

TSPI_lineGetDevConfig

Returns a data structure object, the contents of which are specific to the line (service provider [SP]) and device class, giving the current configuration of a device associated one-to-one with the line device.

TSPI_lineGetExtensionID

Returns the extension identifier that the SP supports for the indicated line device.

lineGetID

TSPI_lineGetID

Returns a device identifier for the specified device class associated with the selected line, address, or call.

TSPI_lineGetNumAddressIDs

Retrieves the number of address identifiers supported on the indicated line.

lineHold

TSPI_lineHold

Places the specified call on hold.

lineMakeCall

TSPI_lineMakeCall

Places a call on the specified line to the specified destination address.

lineNegotiateExtVersion

TSPI_lineNegotiateExtVersion

Returns the highest extension version number the service provider can operate under for this device, given the range of possible extension versions.

TSPI_lineNegotiateTSPIVersion

Returns the highest service provider interface (SPI) version the service provider can operate under for this device, given the range of possible SPI versions.

lineOpen

TSPI_lineOpen

Opens the line device whose device identifier is given, returning the service provider's handle for the device.

lineSetCallParams

TSPI_lineSetCallParams

Sets certain parameters for an existing call.

TSPI_lineSetDefaultMedia Detection

Tells the service provider the new set of media types to detect for the indicated line, replacing any previous set.

TAPI Function

TSP Function

Description of function

lineSetStatusMessages

TSPI_lineSetStatusMessages

Lets TAPI specify which notification messages the service provider should generate for events related to status changes for the specified line or any of its addresses.

lineSetupTransfer

TSPI_lineSetupTransfer

Initiates a transfer of a call.

lineUnhold

TSPI_lineUnhold

Retrieves the specified held call.

### Cisco CRM Communications Connector

The Cisco CRM Communications Connector (Cisco CCC) integrates Cisco Unified CME with the Microsoft Business Solution Customer Relationship Management (Microsoft CRM) application. Cisco CCC provides an easy-to-use IP phone application using Microsoft Outlook or Internet Explorer as the PC client software for managing tasks and contacts.

Cisco CCC offers the following application capabilities:

• Screen pop —Opens a contact record and creates a new phone call activity record as a call arrives. Creates screen pops from click-to-dial calls and from manually dialed outbound calls.

• Click-to-dial —Allows the user to click a field on the PC window and have the PC automatically dial a number. This feature is available from a Microsoft CRM contact record on your desktop.

• Call duration tracking —Tracks the duration of a phone call and associates it with the phone activity record.

• Call information capture —Captures incoming and outgoing call information, including calling number, called number, and call start and end times.

• Customer record creation —Creates a new CRM customer record when a new customer call arrives.

Two pieces of software must be installed to activate the CRM application: one on the Microsoft CRM Server (Cisco CCC server software), and the other on each CRM client PC (Cisco CCC client software). In addition, the Cisco Unified CME TSP driver is installed on each client. The Microsoft CRM Client can use Microsoft Outlook or an HTML interface as the client software.

For information on the CRM Express Solution Specialization, go to the following URL:

http://www.cisco.com/web/partners/program/specializations/index.html

For more information on the installation of Cisco CCC, go to Cisco.com, and search for "Cisco CRM Communications Connector for Cisco CallManager Express."

## Extensible Markup Language Applications

XML is a text markup language designed to control web-based documents. With XML, you can create web pages customized for specific application requirements.

This section briefly discusses the XML applications applicable to Cisco Unified CME IP phones. For more information on developing XML applications, go to the following URL:

http://www.cisco.com/en/US/products/svcs/ps3034/ps5408/ps5418/serv_home.html

Or visit Cisco.com and search for "Developer Support Central."

### General XML Phone Services

XML services on Cisco Unified IP phones give you another way to perform or access more business applications. Some examples of XML-based services on IP phones are user direct-dial directory, announcements, and advertisements.

The IP phones are equipped with a pixel-based display that can display full graphics instead of just text on the window. The pixel-based display capabilities allow you to use sophisticated graphical presentations for applications on Cisco IP phones and make them available at any desktop, counter, or location. In addition, you can select prepackaged applications. A sample phone display with applications is shown in Figure 8-7 .

Figure 8-7 XML Application on a Cisco Unified IP Phone Display

### Cisco Unified CME XML Phone Services

In a Cisco Unified CME application, XML between an XML server and the IP phones provides customized phone displays and services. The interaction between the IP phone and the XML server includes the following events:

• The IP phone sends an HTTP request to the application server.

• The server renders an XML document and sends it to the IP phone.

• The IP phone parses the XML document and renders the screen graphics on the IP phone display.

You can build applications particular to your business, such as a store inventory or stock quote lookup capability. These applications are especially useful to employees who do not have PCs or do not work at desks. You can also write more general applications, such as displaying a large-numbered clock on the IP phone (that displays when the phone is idle), and use this in conference rooms, lobbies, or break rooms instead of a wall clock.

You can find more information about XML-based IP phone services and productivity applications at the Cisco Applications Central web portal. To get to this site, go to Cisco.com and search for "IP Communications Applications Central." This site also has application partner information and discussion forums.

### XML Application Example

Cisco Unified CME runs standards-based XML scripts developed by any XML developer. This flexibility allows you to customize XML scripts for your specified requirements and enable applications for your particular environment.

The following example shows an XML script that provides a system-wide speed-dial feature on an IP phone. When you press the appropriate keys on the IP phone, the display shows the corresponding directory page of the desired party. You can dial the phone number by simply pressing a predefined button.

```
- <IPPhoneDirectory>
```

```
<Title>XYZ Corp User Speed Dials</Title>
```

```
<Prompt>Record 1 to 6 of 6</Prompt>
```

```
- <DirectoryEntry>
```

```
<Name>Directory Assistance</Name>
```

```
<Telephone>95551212</Telephone>
```

```
</DirectoryEntry>
```

```
- <DirectoryEntry>
```

```
<Name>XYZ Paging</Name>
```

```
<Telephone>918007654321</Telephone>
```

```
</DirectoryEntry>
```

```
- <DirectoryEntry>
```

```
<Name>Alan Anderson</Name>
```

```
<Telephone>2001</Telephone>
```

```
</DirectoryEntry>
```

```
- <DirectoryEntry>
```

```
<Name>Bill Brandy</Name>
```

```
<Telephone>2003</Telephone>
```

```
</DirectoryEntry>
```

```
- <DirectoryEntry>
```

```
<Name>Charles Cramer</Name>
```

```
<Telephone>3214</Telephone>
```

```
</DirectoryEntry>
```

```
- <DirectoryEntry>
```

```
<Name>Donna Davis</Name>
```

```
<Telephone>3721</Telephone>
```

```
</DirectoryEntry>
```

```
</IPPhoneDirectory>
```

### Cisco Unified CME Configuration for XML Applications

The XML application interacts directly with the IP phone. You can activate the application in one of three ways:

• By pressing the services button on the phone

• By pressing the directory button on the phone

• By specifying an idle URL that activates when the phone has been idle for a short time

The following shows the telephony-service url command you use to configure the URL accessed by each of the three modes of activating an XML application. This URL is resident on your XML server and can be any application or code of your choice.

```
router(config)# telephony-service
```

```
router(config-telephony)# url ?
```

```
authentication  authentication url
```

```
directories     directories url
```

```
idle            idle url
```

```
information     information url
```

```
proxy-server    proxy-server url
```

```
services        services url
```

```
router# show running-config
```

```
telephony-service
```

```
load 7960-7940 P00303020214
```

```
...
```

```
ip source-address 10.10.1.100 port 2000
```

```
system message CUE System 2691
```

```
create cnf-files version-stamp 7960 Jul 15 2003 13:48:12
```

You can have a services button, a directory button, and an idle phone application configured at the same time. Cisco Unified CME creates phone loads for the IP phones by using the create cnf-files command, shown in the preceding example. This pulls the URLs specified in the telephony-service url configuration into the phone load and allows the IP phone to access the correct URL immediately when the appropriate button is pressed on the keypad. If URL settings are changed, you must reset the phones for the changes to become effective.

| TAPI Function | TSP Function | Description |
|---|---|---|
| lineAnswer | TSPI_lineAnswer | Answers the specified offered call. |
| lineBlindTransfer | TSPI_lineBlindTransfer | Performs a blind or single-step transfer of the specified call to the specified destination address. |
| lineClose | TSPI_lineCloseCall | Closes the specified open line device after completing or aborting all outstanding calls and asynchronous operations on the device. |
| lineCompleteTransfer | TSPI_lineCompleteTransfer | Completes the transfer of the specified call to the party connected in the consultation call. |
| lineDial | TSPI_lineDial | Dials the specified dialable number on the specified call. |
| lineDrop | TSPI_lineDrop | Drops or disconnects the specified call. |
| lineGetAddressID | TSPI_lineGetAddressID | Returns the address identifier associated with the address in a different format on the specified line. |
|  | TSPI_lineGetCallAddressID | Retrieves the address identifier for the indicated call. |
| lineGetCallInfo | TSPI_lineGetCallInfo | Returns detailed information about the specified call. |
| TAPI Function | TSP Function | Description of function. |
| lineGetCallStatus | TSPI_lineGetCallStatus | Returns the current status of the specified call. |
| lineGetDevConfig | TSPI_lineGetDevConfig | Returns a data structure object, the contents of which are specific to the line (service provider [SP]) and device class, giving the current configuration of a device associated one-to-one with the line device. |
|  | TSPI_lineGetExtensionID | Returns the extension identifier that the SP supports for the indicated line device. |
| lineGetID | TSPI_lineGetID | Returns a device identifier for the specified device class associated with the selected line, address, or call. |
|  | TSPI_lineGetNumAddressIDs | Retrieves the number of address identifiers supported on the indicated line. |
| lineHold | TSPI_lineHold | Places the specified call on hold. |
| lineMakeCall | TSPI_lineMakeCall | Places a call on the specified line to the specified destination address. |
| lineNegotiateExtVersion | TSPI_lineNegotiateExtVersion | Returns the highest extension version number the service provider can operate under for this device, given the range of possible extension versions. |
|  | TSPI_lineNegotiateTSPIVersion | Returns the highest service provider interface (SPI) version the service provider can operate under for this device, given the range of possible SPI versions. |
| lineOpen | TSPI_lineOpen | Opens the line device whose device identifier is given, returning the service provider's handle for the device. |
| lineSetCallParams | TSPI_lineSetCallParams | Sets certain parameters for an existing call. |
|  | TSPI_lineSetDefaultMedia Detection | Tells the service provider the new set of media types to detect for the indicated line, replacing any previous set. |
| TAPI Function | TSP Function | Description of function |
| lineSetStatusMessages | TSPI_lineSetStatusMessages | Lets TAPI specify which notification messages the service provider should generate for events related to status changes for the specified line or any of its addresses. |
| lineSetupTransfer | TSPI_lineSetupTransfer | Initiates a transfer of a call. |
| lineUnhold | TSPI_lineUnhold | Retrieves the specified held call. |