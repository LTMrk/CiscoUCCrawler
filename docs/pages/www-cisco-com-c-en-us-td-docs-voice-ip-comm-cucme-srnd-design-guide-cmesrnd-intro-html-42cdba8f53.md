---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-srnd-design-guide-cmesrnd-intro-html-42cdba8f53
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/srnd/design/guide/cmesrnd/intro.html
retrieved_at: 2026-08-21T22:57:42.500844+00:00
---

Cisco Unified CallManager Express Solution Reference Network Design Guide

# Cisco Unified CallManager Express Solution Reference Network Design Guide

Updated: November 2, 2007

Chapter: Introducing Cisco Unified Communications

## Chapter: Introducing Cisco Unified Communications

## Introducing Cisco Unified Communications Express

Cisco Unified Communications Express is an award-winning IP communications solution that is provided with the Cisco Integrated Services Router portfolio. Cisco Unified Communications Express includes:

• Cisco Unified CallManager Express to provide rich call processing

• Cisco Unity Express to provides integrated messaging with an AIM or NM module

• Full portfolio of IP phones to meet the small medium business needs

• Full-featured voice over IP (VoIP) capability to support H.323 and Session Initiation Protocol (SIP) implementations

• Voice gateways supporting VG224 and analog telephone adaptors (ATA)

Cisco Unified Communications Express provides a complete solution based on Cisco Integrated Services Router. This solution includes:

• Integrated wired and wireless LAN

• Integrated security with VPN, firewall, and encryption

• Cisco routing and switching functionality

Cisco Unified Communications Express encompasses the following solutions:

• Basic Automatic Call Distribution (B-ACD)

Cisco Unified CallManager Express (Cisco Unified CME) B-ACD provides automatic answering and call distribution for calls through the use of interactive menus and local hunt groups.

• Customer Contact

Cisco Customer Contact solutions are a combination of strategy and architecture that promote efficient and effective customer communications across a globally capable network by enabling organizations to draw from a broader range of resources to service customers, including access to an unlimited pool of agents and multiple channels of communication as well as customer self-help tools.

• IP Telephony

IP telephony refers to technology that transmits voice communications over a network using IP standards. The Cisco Unified IP Telephony solution includes a wide array of hardware and software products such as call processing agents, IP phones, video devices, and special applications.

• Rich-Media Conferencing

Cisco Rich-Media Conferencing solutions enhance the virtual meeting environment with a integrated set of IP-based tools for voice, video, and Web conferencing.

• Third-Party Applications

We work with leading-edge companies to provide the broadest selection of innovative third-party IP telephony applications and products focused on critical business needs such messaging, customer care, and workforce optimization.

• Unified Communications

Cisco Unified Communications Express solutions deliver unified messaging (e-mail, voice, and fax messages managed from a single inbox) and intelligent voice messaging (full-featured voicemail providing advanced capabilities) to improve communications, boost productivity, and enhance customer service capabilities across an organization. Cisco Unified Communications Express solutions also enable users to streamline communication processes through the use of features such as rules-based call routing, simplified contact management, and speech recognition.

• Video Telephony

The Cisco Video Telephony solution enables real-time video communications and collaboration using the same IP network and call processing agent as the Cisco Unified IP Telephony solution. With Cisco Video Telephony, making a video call is now as easy as dialing a phone number.

Note For additional information, see the "Related Documents and References" section .

## Overview of the Cisco Unified IP Telephony Solution

The Cisco Unified IP Telephony solution is the leading converged network telephony solution for organizations that want to increase productivity and reduce the costs associated with managing and maintaining separate voice and data networks. The flexibility and sophisticated functionality of the Cisco Unified IP network infrastructure provides the framework that permits rapid deployment of emerging applications such as desktop Cisco Unified IP Telephony, unified messaging, video telephony, desktop collaboration, enterprise application integration with IP phone displays, and collaborative IP contact centers. These applications enhance productivity and increase enterprise revenues.

Figure 1-1 illustrates a typical IP Telephony solution employing the Cisco Unified IP network infrastructure, with Cisco Unified CME as the call processing agent.

The foundation architecture of the Cisco Unified IP Telephony solution includes of the following major components (see Figure 1-1 ):

• Cisco Unified IP Network Infrastructure

• Quality of Service

• Call Processing Agent

• Communication Endpoints

• Applications

• Security

• Network Management Tools

Figure 1-1 Typical Enterprise Cisco Unified IP Telephony Environment

### Cisco Unified IP Network Infrastructure

The network infrastructure includes public switched telephone network (PSTN) gateways, analog phone support, and digital signal processor (DSP) farms. The infrastructure can support multiple client types such as hardware phones, software phones, and video devices. The infrastructure also includes the interfaces and features necessary to integrate legacy PBX, voicemail, and directory systems. Typical products used to build the infrastructure include Cisco voice gateways (nonrouting, routing, and integrated), Cisco IOS software and Catalyst switches, and Cisco routers.

### Quality of Service

Voice, as a class of IP network traffic, has strict requirements concerning packet loss, delay, and delay variation (also known as jitter). To meet these requirements for voice traffic, the Cisco Unified IP Telephony solution includes Quality of Service (QoS) features such as classification, queuing, traffic shaping, compressed Real-Time Transport Protocol (cRTP), and Transmission Control Protocol (TCP) header compression.

The QoS components of the Cisco Unified IP Telephony solution are provided through the rich IP traffic management, queueing, and shaping capabilities of the Cisco Unified IP network infrastructure. Key elements of this infrastructure that enable QoS for IP telephony include:

• Call admission control

• Compressed RTP (cRTP)

• Enhanced queuing services

• Link efficiency

• Link fragmentation and interleaving (LFI)

• Low-latency queuing (LLQ)

• Traffic marking

• Traffic shaping

### Call Processing Agent

In the context of a standalone small/medium business application or for distributed call processing designs, Cisco Unified CME is the core call processing software for the Cisco Unified IP Telephony solution. It builds call processing capabilities on top of the Cisco Unified IP network infrastructure. Cisco Unified CME software extends enterprise telephony features and capabilities to packet telephony network devices such as IP phones, media processing devices, Voice over IP (VoIP) gateways, and multimedia applications.

You can deploy the call processing capabilities of Cisco Unified/ CME according to one of the following models, depending on the size, geographical distribution, and functional requirements of your enterprise:

• Single-site call processing model

In the single-site model, each site has its own Cisco Unified CME. No voice traffic travels over the IP WAN; instead, external calls or calls to remote sites use the public switched telephone network (PSTN).

• Multisite WAN model with distributed call processing

In the multisite WAN model with distributed call processing, each site has its own Cisco Unified CME. Communication between sites normally takes place over the IP WAN, with the PSTN serving as a backup voice path. With this model, you can interconnect any number of sites across the IP WAN.

### Communication Endpoints

A communication endpoint is a user instrument such as a desk phone or even a software phone application that runs on a PC. In the IP environment, each phone has an Ethernet connection. IP phones have all the functions you expect from a telephone, as well as more advanced features such as the ability to access World Wide Web sites.

In addition to various models of desktop Cisco Unified IP Phones, IP Telephony endpoints include the following devices:

• Software-based IP phones

Cisco Unified IP Softphone and Cisco IP Communicator are desktop applications that turn your computer into a full-featured IP phone with the added advantages of call tracking, desktop collaboration, and one-click dialing from online directories. Cisco software-based IP phones offer users the great benefit of having a portable office IP phone to use anywhere an Internet connection is available.

• Wireless IP phones

The Cisco Unified Wireless IP Phone 7920 extends the Cisco family of IP phones from 10/100 Ethernet to 802.11 wireless LAN (WLAN). The Cisco 7920 Wireless IP Phone provides multiple line appearances with functionality similar to existing Cisco 7900 Series IP Phones. In addition, the Cisco 7920 phone provides enhanced WLAN security and Quality of Service (QoS) for operation in 802.11b networks. The Cisco 7920 phone also provides support for XML-based data access and services.

### Applications

Voice and video applications build upon the call processing infrastructure to enhance the end-to-end capabilities of the Cisco Unified IP Telephony solution by adding sophisticated telephony and converged network features, such as the following:

• Cisco Unified MeetingPlace Express

Cisco Unified MeetingPlace Express is a complete rich-media conferencing solution that integrates voice and Web conferencing capabilities to make remote meetings as natural and effective as face-to-face meetings. In a single step, meeting organizers can schedule voice, video, and Web resources through either the Cisco Unified MeetingPlace Express Web interface, an IP phone, or their Microsoft Outlook or Lotus Notes calendars. Meeting invitees automatically receive notification by email or calendar invitation and can attend rich-media conferences with a single click.

• Cisco Unity Express Auto Attendant and Voice Mail

Cisco Unity Express provides a distributed AA and voice-mail application to an IP Telephony solution where the large offices may have a high-end voice mail solution (such as Cisco Unity) and one or more of the smaller remote offices may use a local or distributed Cisco Unity Express for voice mail. Cisco Unity Express is deployed with one of two call-processing models that are based on either Cisco Unified CME or Cisco Unified CallManager.

The call processing engine (Cisco Unified CME or Cisco Unified CallManager) manages the IP phones and features such as call-forward-busy (CFB) and call-forward-no-answer (CFNA) to the voice mail pilot number, while Cisco Unity Express provides the AA menus, scripts and voice mail telephony user interface (TUI) sessions for callers retrieving or leaving voice messages. Cisco Unity Express stores the AA scripts and prompts, voice mail subscriber spoken names, greetings and voice mail messages.

Cisco Unity Express interfaces with Cisco Unified CME call control via a Session Initiation Protocol (SIP) interface and to Cisco Unified CallManager via a Java Telephony Applications Programming Interface (JTAPI) interface.

• Unified messaging

Cisco Unity delivers powerful unified messaging (email, voice, and fax messages sent to one inbox) and intelligent voice messaging (full-featured voicemail providing advanced functionality) to improve communications, boost productivity, and enhance customer service capabilities across your organization. With Cisco Unity Unified Messaging, you can listen to your e-mail over the phone, check voice messages from the Internet, and (when integrated with a supported third-party fax server) send faxes anywhere.

• Web services for Cisco Unified IP Phones

You can use Cisco Unified IP Phones to deploy customized client services with which users can interact via the keypad and display. You can create applications for Cisco Unified IP Phone services by using the eXtensible Markup Language (XML) Application Programming Interface (API) and deploy them using HTTP from standard web servers, such as Microsoft IIS. Some typical services that can be provided through a Cisco Unified IP Phone include a full conferencing interface, the ability to manage data records even if no PC is available, and the ability to display employee alerts, clocks, stock market information, customer contact information, daily schedules, and so forth.

• Cisco Unified CME B-ACD

Cisco Unified CME B-ACD provides automatic answering and call distribution for calls through the use of interactive menus and local hunt groups. Each Cisco Unified CME B-ACD application consists of one or more auto-attendant (AA) services and one call-queue service.

### Security

The Cisco Unified IP Telephony solution addresses security in the following main areas, among others:

• Physical security for restricting physical access to important application servers and network components

• Network access security to prevent hostile logins or attacks

• Security measures for your Cisco router running Cisco Unified CME

• Mechanisms for defining calling privileges for various classes of users

• Careful network design and management to enhance security

### Network Management Tools

The Cisco Unified IP network infrastructure offers a number of network management, QoS, and security management tools that support the IP Telephony solution. Cisco Unified CME offers enhanced software and configuration management tools that leverage the strength and flexibility of IP networks. The Cisco Unified CME user interface simplifies the most common subscriber and telephony configuration tasks by building upon legacy telephony administration systems and adding software and web-based applications.

In addition, CiscoWorks 2000 includes a number of network management tools to manage the operations, administration, and maintenance of IP Telephony networks.

CiscoWorks IP Communications Operations Manager (CiscoWorks IPCOM) provides a suite of applications and tools that facilitate effective management of IP Telephony installations. CiscoWorks IPCOM provides the following major features:

• Problem-focused fault analysis — Provides timely information about the health of IP Telephony environments.

• Confidence testing and monitoring — Permits the use synthetic testing to emulate normal day-to-day operations and to validate operational readiness of the IP infrastructure and the Cisco Unified IP Telephony deployment.

• Intelligent integration with existing management infrastructures — Generates intelligent traps that can be forwarded to other event-management systems installed in the network, sent to email or pager gateways, or displayed on the Alerts and Activities Display (AAD).

• Evaluation and correlation capabilities — Allows for the evaluation of the general health of the IP Telephony environment in the monitored network environment.

• Alerts and activities display (AAD) — Provides a proactive, web-based operations screen for real-time status and alerting of actual and suspected problems in the underlying IP network as well as in the Cisco Unified IP Telephony implementation.

• Cisco Unified IPCOM Multiview — Enables large enterprise customers and managed service providers to partition specific user communities and manage each from a single Cisco Unified IPCOM implementation.