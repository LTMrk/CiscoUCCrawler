---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-srnd-design-guide-cmesrnd-clproc-html-9673023189
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/srnd/design/guide/cmesrnd/clproc.html
retrieved_at: 2026-08-21T22:57:59.383828+00:00
---

Cisco Unified CallManager Express Solution Reference Network Design Guide

# Cisco Unified CallManager Express Solution Reference Network Design Guide

Updated: November 2, 2007

Chapter: Cisco Unified CallManager Express Call Transfer and Forward

## Chapter: Cisco Unified CallManager Express Call Transfer and Forward

## Cisco Unified CallManager Express Call Transfer and Forward

Configuring call transfer and forwarding for H.323 VoIP calls is a fairly complex task in most real-world H.323 VoIP networks. This is especially true if you have a mixture of H.323 VoIP systems from different vendors. Even if you have an all-Cisco H.323 VoIP network, there are still interactions to consider, unless all your VoIP systems are running relatively up-to-date Cisco IOS software. This means having at least Cisco IOS Release 12.3 software in all your voice-enabled routers. Ideally, you should have Cisco IOS Release 12.3(4)T or later software (this is the Cisco Unified CallManager Express (Cisco Unified CME) 3.0 base code version). There are also some special considerations if you are using a Cisco Unified CallManager in addition to your Cisco IOS-based Cisco Unified CME systems addressed in "Connecting Multiple Cisco Unified CallManager Express Systems with VoIP." The good news is that with the right software and configuration, there are workable solutions for most of your VoIP call transfer and forwarding needs.

In a VoIP network, getting an optimized system working for call transfer and forwarding requires the active cooperation of all endpoints involved in a call transfer or call forward. This means your ability to perform a call transfer or forward depends on the capabilities of the calling party's VoIP system as well as your Cisco Unified CME system configuration. A call transfer also depends on the capabilities of the final VoIP system that you are transferring the call to.

In traditional TDM-based PBX telephony, call transfer and forwarding usually operate within the limited scope of a single PBX system and, therefore, are simpler operations. For example, you are often limited to call transfers between extensions on the same PBX only.

In a VoIP-based system, you can potentially transfer or forward calls between any VoIP endpoints, regardless of their physical location. Of course, being able to do this in practice requires making sure that you have support for transfer and forwarding built into all your VoIP endpoints.

With Cisco Unified CME, you have three basic choices for the protocol used to support call transfer and forwarding for H.323 VoIP calls:

• Standards-based H.450 —Recommended because it provides for optimal call paths and unlimited sequential transfers and forwards.

• Cisco H.323 extension —Mostly obsolete, but useful if you are using software older than Cisco IOS Release 12.2(15)T.

• Hairpin call routing —Allows for maximum compatibility, but uses more WAN bandwidth and results in higher delay and jitter.

The default H.323 call transfer protocol used by Cisco Unified CME is the Cisco mechanism. This mechanism supports only blind call transfer (that is, no transfer consultation). It is selected as the default simply for purposes of backward compatibility with earlier Cisco IOS releases.

The default call forwarding mechanism provides for automatic local forwarding only (that is, within the same Cisco Unified CME system). It does not provide forwarding display update notification of the call forwarding to the calling party's IP phone. For incoming VoIP calls from another Cisco Unified CME system that are nonlocally forwarded to a third Cisco Unified CME system, the Cisco-proprietary H.323 protocol extensions are used.

Even if you do not require H.323 VoIP call transfers (because you do not need to make calls across an IP connection to another site), you should still select the H.450 configuration method for call transfers. This enables call transfer with consultation for local calls within your system and for PSTN calls that use PSTN voice ports that are physically on your Cisco Unified CME router. (PSTN voice ports on a router other than the Cisco Unified CME system appear as H.323 VoIP calls to the Cisco Unified CME system.) It also prepares your system to use the standards-based H.450 protocol in case you want to add support for H.323 or SIP VoIP transfer and forwarding to another site at some point in the future.

Sections that follow address the following topics:

• Call Transfer Methods for VoIP

• Cisco Unified CME VoIP Call Transfer Options

• Call Forward Methods for VoIP

• Cisco Unified CME VoIP Call Forwarding Options

• Transfer and Forward Proxy Function

• Call Transfer and Forward Interoperability with Cisco Unified CallManager

• Call Transfer and Forwarding with Routed Signaling H.323 Gatekeepers

Note For additional information, see the "Related Documents and References" section .

## Call Transfer Methods for VoIP

This section describes several methods for implementing call transfer across VoIP networks:

• H.450 and SIP

• Hairpin Routing

• H.450.12

• Empty Capabilities Set

### H.450 and SIP

The ITU-T standards-based H.450.2 transfer method and the Cisco method operate in a similar way. In both cases, when a call transfer occurs, a control message is sent back to the transferee party to request that the transferee initiates a follow-on call from the transferee to the final transfer-to destination. In the H.450.2 case, the follow-on call originated by the transferee can act to replace the transfer consultation call that is in progress between the transferor and the transfer-to destination party. The consultation call between transferor and transfer-to and the original transferee-transferor call are not torn down until the "replaces" operation is completed successfully. The term replaces is used here in the context of "Call 2 replaces call 1." If for any reason the replacement operation fails, it is usually possible for the transferor to reconnect the call to the transferee. The H.450.2 mechanism works in a manner similar to the REFER method used for SIP VoIP calls. The Cisco transfer mechanism does not support the call replacement mechanism and, therefore, allows you to perform only blind call transfers. This proprietary method is similar to the older BYE/ALSO method that was used to perform blind transfers for SIP VoIP calls. The BYE/ALSO method has been mostly superseded by the SIP REFER method.

Both of these H.323 call transfer methods result in an optimal direct call path between the transferee and the transfer-to party after the call transfer is committed.

### Hairpin Routing

The third alternative is to hairpin route the VoIP call transfer. In this case, the original transferee-to-transferor VoIP call leg is kept, and a second transferor to transfer-to VoIP call leg is created for the consultation call phase of the transfer. When the transfer is committed, the original and consultation call legs are simply bridged together at the Cisco Unified CME router. This method has the advantage that it has no end-to-end dependency on the capabilities of the transferee or transfer-to VoIP endpoint.

It also has disadvantages. One significant disadvantage is that the final transferred call is relayed through the transferor's Cisco Unified CME system. This means that the transferred call continues to consume resources on the transferor Cisco Unified CME system even after the transfer is committed. It also means that the media path for voice packets for the transferred call may hairpin route through the transferor's Cisco Unified CME system, so both the original call and the transferred call continue to consume WAN bandwidth. If the amount of WAN bandwidth is limited, this may prevent new VoIP calls from being established until the transferred call is terminated. The other significant disadvantage of hairpin routing calls is the cumulative bandwidth, delay, and jitter problems that occur if a call is transferred multiple times (chained or sequential transfers).

### H.450.12

You can compromise between the H.450.2 and hairpin routing call methods by turning on the H.450.12 protocol on your Cisco Unified CME system (this is recommended). You must be using at least Cisco Unified CME 3.1 to use H.450.12. With H.450.12 enabled, your Cisco Unified CME system can use the H.450.12 protocol to automatically discover the H.450.x capabilities of VoIP endpoints within your VoIP network. When H.450.12 is enabled, the Cisco Unified CME system can automatically detect when an H.450.2 transfer is possible. When it isn't possible, the Cisco Unified CME system can fall back to using VoIP hairpin routing. Cisco Unified CME also can automatically detect a call from a (non-H.450-capable) Cisco Unified CallManager.

### Empty Capabilities Set

For the sake of completeness, it is worth mentioning a fourth alternative for call transfers: Empty Capabilities Set (ECS). Cisco Unified CME does not support the instigation of transfer using ECS. But because a Cisco Unified CME router also has the full capabilities of the Cisco IOS Release H.323 voice infrastructure software, it can process receipt of an ECS request coming from a far-end VoIP device. In other words, a Cisco Unified CME system can be a transferee or transfer-to party in an ECS-based transfer. A Cisco Unified CME system does not originate a transfer request using ECS. The problem with ECS-based transfers is that in many ways they represent a combination of the worst aspects of the end-to-end dependencies of H.450.2 together with the cumulative problems of hairpin for multiple transfers. Many ECS-based transfer implementations do not allow you to transfer a call that has already been transferred in the general case of VoIP intersystem transfers.

## Cisco Unified CME VoIP Call Transfer Options

Your Cisco Unified CME system by default is set up to allow local transfers between IP phones only. It uses the Cisco H.323 call transfer extensions to transfer calls that include an H.323 VoIP participant.

To configure your Cisco Unified CME system to use H.450.2 transfers (this is recommended), set transfer-system full-consult under the telephony-service command mode. You also have to use this configuration for SIP VoIP transfers.

To configure your Cisco Unified CME system to permit transfers to nonlocal destinations (VoIP or PSTN), set the transfer-pattern command under telephony-service . The transfer-pattern command also allows you to specify that specific transfer-to destinations should receive only blind transfers. You also have to use this configuration for SIP VoIP transfers. The transfer-pattern command allows you to restrict trunk-to-trunk transfers to prevent incoming PSTN calls from being transferred back out to the PSTN (employee toll fraud). Trunk-to-trunk transfers are disabled by default, because the default is to allow only local extension-to-extension transfers.

To allow the H.450.12 service to automatically detect the H.450.2 capabilities of endpoints in your H.323 VoIP network, use the supplementary-services command in voice service voip command mode.

To enable hairpin routing of VoIP calls that cannot be transferred (or forwarded) using H.450, use the allow-connections command. The following example shows a call transfer configuration using this command.

```
voice service voip
```

```
supplementary-service h450.12
```

```
allow-connections h323 to h323
```

```
telephony-service
```

```
transfer-system full-consult
```

```
transfer-pattern .T
```

The configuration shown in the preceding example turns on the H.450.2 ( transfer-system full-consult ) and H.450.12 services, allows VoIP-to-VoIP hairpin call routing ( allow-connections ) for calls that don't support H.450, and permits transfers to all possible destinations ( transfer-pattern ). The transfer permission is set to .T to provide full wildcard matching for any number of digits. (The T stands for terminating the transfer destination digit entry with a timeout.)

The following example shows a configuration for more restrictive transfer permissions.

```
telephony-service
```

```
transfer-system full-consult
```

```
transfer-pattern 1...
```

```
transfer-pattern 2... blind
```

This example permits transfers using full consultation to nonlocal extensions in the range 1000 to 1999. It also permits blind transfers to nonlocal extensions in the range 2000 to 2999.

## Call Forward Methods for VoIP

This section describes different mechanisms for handling call forwarding in a VoIP network:

• H.450.3 Call Forwarding

• H.323 Facility Message

• VoIP Hairpin Call Forwarding

You can configure your Cisco Unified CME to handle VoIP call forwarding in several different ways. Select the method to use depending on how you want forwarding to operate.

### H.450.3 Call Forwarding

You can use the ITU-T H.450.3 standard for call forwarding (this is recommended). It has some similarities to H.450.2 (call transfer). When a call is forwarded, an H.450.3 message is sent back to the calling party requesting that the caller reoriginate a follow-on call to the forwarded-to destination. If Cisco Unified CME is configured to use H.450.3, it is used even if the forward-to destination is another local IP phone within the same Cisco Unified CME system as the forwarding phone (or forwarder). Use this method if you want the calling VoIP party to always be able to see the phone number he or she is being forwarded to. Just like the H.450.2 transfer case, use of H.450.3 requires that all the VoIP endpoints in your VoIP network support H.450 services.

### H.323 Facility Message

The second choice is to use the quasi-standard H.323 Facility Message mechanism for forwarding. This is the default call forwarding configuration for Cisco Unified CME. This method is used as the default, because it provides backward compatibility with earlier (and current) Cisco IOS releases. It's also quite widely supported by third-party and nonCisco IOS VoIP systems. When this mechanism is used, an H.323 Facility Message is sent back to the VoIP caller only for the case of forwarding to a nonlocal number. If the forward-to destination is local to the forwarding phone, the call forward operation is handled internally within the Cisco Unified CME system. In this case, the remote calling IP phone cannot update its display to show the forwarded destination.

### VoIP Hairpin Call Forwarding

Your third choice is to use VoIP call hairpin routing. This is similar to the call transfer hairpin option. A second independent VoIP call leg is created for the forwarded call leg. This leg is bridged to the original incoming VoIP call leg. As for the transfer hairpin case, the disadvantage of this approach occurs if you have to support sequential or chained forwarding. Sequential hairpin forwarding of VoIP calls results in accumulated bandwidth and jitter/delay issues.

Just like the call transfer discussion, if you have to deal with only local LAN and PSTN connections and do not have to route VoIP H.323 calls across a WAN connection, you can just configure your system for H.450.3 operation to get your system ready to interoperate with other H.450-capable endpoints if you need this in the future.

You can also compromise between the H.450.3 and hairpin configuration by using the H.450.12 service to automatically detect H.450.3-capable VoIP endpoints, and fall back to hairpin routing for calls that do not support H.450.3.

## Cisco Unified CME VoIP Call Forwarding Options

Your Cisco Unified CME system by default is configured to support internal local forwarding. It sends only H.323 Facility Messages back to the VoIP caller for nonlocal VoIP forwarding destinations. If you have direct PSTN access on your Cisco Unified CME system, PSTN destinations accessed via local ports are considered local for the purposes of this discussion.

To turn on H.450.3 services for VoIP calls, you use the call-forward pattern command under telephony-service . This command lets you conditionally select H.450.3 service based on matching the calling party's telephone number. This lets you invoke H.450.3 for calls only from VoIP phone numbers that you know support H.450.3. You can configure the matching pattern to use .T to match all possible calling party numbers. This is similar to the match-all configuration used with the transfer-pattern command.

To permit VoIP-to-VoIP hairpin call routing for forwarded calls, set the allow-connections command under voice services voip . If you've already done this to allow hairpin transfers, you don't need to do it again for call forwarding.

As with the H.450.2 transfer case, you can turn on the H.450.12 service to compromise and allow H.450.3 where possible, and fall back to hairpin forwarding otherwise. Note that H.450.12 support was introduced in Cisco Unified CME 3.1.

The following example shows a basic configuration.

```
voice service voip
```

```
supplementary-service h450.12
```

```
allow-connections h323 to h323
```

```
telephony-service
```

```
call-forward pattern .T
```

## Transfer and Forward Proxy Function

The transfer and forward discussion so far in this chapter has related to the configuration of a single Cisco Unified CME system to cope with various possible VoIP network scenarios, including networks that have endpoints with mixed capabilities. If you have a network of Cisco Unified CME systems, you should consider partitioning it to provide a section that contains only H.450-capable endpoints. This allows you to gain the full set of H.450 service benefits within the group of VoIP network devices that support them. You can then link this segment of your VoIP network to the non-H.450 network using a Cisco IOS router configured to act as an H.450 IP-to-IP gateway.

An H.450 IP-to-IP gateway can act as a proxy for H.450.2 and H.450.3 services on behalf of VoIP devices that don't support H.450. Calls between the H.450 and non-H.450 devices can be routed to pass through the H.450 IP-to-IP gateway. H.450 messages originated by Cisco Unified CME systems can be terminated on the H.450 IP-to-IP gateway, which can invoke hairpin call routing for transfers and call forwarding as needed.

An H.450 IP-to-IP gateway makes the most sense if your network topology is arranged in a hub-and-spoke fashion. Consider a network design that has a number of Cisco Unified CME systems located at the end of WAN link spokes connected to a central hub network. In this type of network, it often makes sense to locate an H.450 IP-to-IP gateway at the central hub and to use it as a linkage point to act as a bridge into the non-H.450 segment of the VoIP network. With an H.450 IP-to-IP gateway, calls that enter the H.450 network segment through the IP-to-IP gateway can be transferred and forwarded using H.450 services within the H.450 segment of the network. Calls transferred or forwarded to destinations outside the H.450 segment are hairpin routed as needed by the H.450 IP-to-IP gateway. If the H.450 IP-to-IP gateway is located at a central hub location, hairpin routing the call at the hub is a better option than hairpin routing the call from a Cisco Unified CME system located at the far end of one of the network spokes over a WAN link. Figure 5-1 in the next section shows a IP-to-IP gateway.)

## Call Transfer and Forward Interoperability with Cisco Unified CallManager

Cisco Unified CallManager 4.0 and earlier does not support H.450 services. Cisco Unified CME 3.1 can automatically detect H.323 calls that go to or come from Cisco Unified CallManager. It does this using H.323 information elements included in H.323 call setup, progress, alerting, and connect messages. You can optionally turn on H.450.12 services for calls to Cisco Unified CallManager, and use the lack of H.450.12 indications to invoke hairpin VoIP call routing by your Cisco Unified CME systems, but this is not required.

You may have a VoIP network in which turning on H.450.12 produces ambiguous results as far as the detection of H.450.2 and H.450.3 capabilities. One example of this occurs when you have older Cisco Unified CME 3.0 (or even Cisco ITS [the earlier Cisco Unified CME name] 2.1) systems in your network. Although Cisco Unified CME 3.0 systems do support H.450.2 and H.450.3, they don't support H.450.12 capabilities indications. If you turn on H.450.12 on your Cisco Unified CME 3.1 systems and you also have some older Cisco Unified CME 3.0 routers, the Cisco Unified CME 3.1 systems assume that the Cisco Unified CME 3.0 routers cannot perform H.450.2/3 services, because no H.450.12 indication is forthcoming from the Cisco Unified CME 3.0 systems. So in a network with a mixture of Cisco Unified CME 3.0, Cisco Unified CME 3.1, and Cisco Unified CallManagers, it makes sense to turn off the H.450.12 service and assume that all endpoints can perform H.450.2/3 except for the endpoints that are detected as explicitly being Cisco Unified CallManager systems.

Also, if you have a Cisco Unified CallManager system, it is probably located at a central corporate site with Cisco Unified CME systems at branch offices. This arrangement lends itself naturally to a hub-and-spoke network design with the Cisco Unified CallManager at the hub and the Cisco Unified CME systems at the ends of the network spokes. This type of network design is a good candidate for an H.450 IP-to-IP gateway using the H.450 IP-to-IP gateway to front-end the Cisco Unified CallManager and act as a proxy for H.450 services between the Cisco Unified CallManager and the network of Cisco Unified CME systems. The H.450 IP-to-IP gateway can also be configured to act as the PSTN Voice gateway for the Cisco Unified CallManager system (using either H.323 or MGCP), so you don't need to dedicate a separate router for the H.450 IP-to-IP gateway. It can also provide centralized PSTN access for the Cisco Unified CME systems. Performance wise, calls that pass through the H.450 IP-to-IP gateway consume a similar amount of CPU and memory resources as a call terminated by the router as a PSTN gateway call. See Figure 5-1 .

Figure 5-1 H.450 IP-to-IP Gateway

Cisco Unified CallManager 4.0 or earlier should be configured to interface with Cisco Unified CME systems or an H.450 IP-to-IP gateway using H.323 Inter-Cluster Trunk (ICT) mode and a Media Termination Point (MTP). In addition, Cisco Unified CallManager 3.3(3) should be configured to disable H.323 fast-start.

## Call Transfer and Forwarding with Routed Signaling H.323 Gatekeepers

An H.323 gatekeeper that uses routed signaling acts as a call proxy for basic A-to-B calls. All calls that reference the gatekeeper have H.323 signaling that passes through the gatekeeper. The presence of this type of gatekeeper in your network has a significant impact on your network from the H.450 service point of view. Your routed signaling gatekeeper may or may not support H.450 services. It may be able to pass through H.450 messages transparently, or it may block some or all of them. It may even be able to act as an H.450 IP-to-IP gateway.

A worst-case design approach for dealing with a routed signaling gatekeeper would be to assume that H.450.2/3 services do not work through the gatekeeper. In this case you can configure your Cisco Unified CME systems to force hairpin routing of all VoIP calls that have to transfer or forward back into the VoIP network. You can do this by turning off H.450 services under the voice service voip command, as shown in the following example.

```
voice service voip
```

```
no supplementary-service h450.2
```

```
no supplementary-service h450.3
```

```
allow-connections h323 to h323
```

```
telephony-service
```

```
call-forward pattern .T
```

```
transfer-system full-consult
```

```
transfer-pattern .T
```

Note Note that by default, the H.450.12 service is disabled, so there is no need to specifically include commands to turn it off.