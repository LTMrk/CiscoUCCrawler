---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-bd78d07ab2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_0110111.html
retrieved_at: 2026-08-16T17:33:23.986626+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Cisco TelePresence

## Chapter: Configure Cisco TelePresence

# Configure Cisco TelePresence

## Cisco TelePresence

### Cisco TelePresence Conductor

The Cisco TelePresence Conductor simplifies multiparty video communications. The conductor lies within a video communications
                              network, working in conjunction with one or more conference bridges and one or more call control devices (either Cisco TelePresence
                              Video Communication Servers (VCSs) or Unified Communications Managers). It allows the video network to be configured so you
                              can spontaneous or rendezvous conferences can be easily provisioned, initiated, accessed, and managed.

For ad hoc conferences, a SIP trunk is used from Unified Communications Manager to TelePresence Conductor. Set up the relevant
                              TelePresence Conductor Location’s ad hoc IP address as the destination of a SIP trunk on Unified Communications Manager. Ad
                              hoc calls for that location can then be routed down that SIP trunk.

For rendezvous conferences a separate SIP trunk is used from Unified Communications Manager to TelePresence Conductor. Set
                              up the relevant TelePresence Conductor Location’s rendezvous IP address as the destination of a SIP trunk on Unified Communications
                              Manager. Rendezvous calls for that location can then be routed down that SIP trunk.

For detailed tasks about how to configure your system with Cisco TelePresence Conductor, see the deployment guides at http://www.cisco.com/c/en/us/support/conferencing/telepresence-conductor/products-installation-and-configuration-guides-list.html .

### Cisco TelePresence Conference Bridges

The Cisco TelePresence Server is a scalable videoconferencing bridge that works with Cisco Unified Communications Manager
                              to bring multiparty video to your unified communications deployments. It offers flexible video, audio, and content-sharing
                              capabilities for multiparty videoconferencing. You can easily create, launch, and join meetings using standards-based video
                              endpoints, mobile devices, Cisco Webex clients, and third-party video endpoints.

The Cisco TelePresence Multipoint Control Unit (MCU) is a high definition multipoint video conferencing bridge. It delivers
                              up to 1080p at 30 frames per second, full continuous presence for all conferences, full transcoding, and is ideal if you want
                              to configure mixed high definition endpoint environments. The Cisco TelePresence MCU supports SIP as the signaling call control
                              protocol. It has a built in Web Server that allows for complete configuration, control, and monitoring of the system and conferences.

The Cisco TelePresence Server is primarily controlled by Cisco TelePresence Conductor. For detailed tasks about how to configure
                              these conference bridges within your system, see the deployment guides at http://www.cisco.com/c/en/us/support/conferencing/telepresence-conductor/products-installation-and-configuration-guides-list.html .

### Cisco TelePresence Video Communication Server

The Cisco TelePresence Video Communication Server (VCS)
                              simplifies session management and control of telepresence
                              conferences. The VCS delivers provides secure communications, simplified large-scale provisioning, and
                              network administration in conjunction with Cisco TelePresence
                              Management Suite (Cisco TMS). The VCS interworks with
                              Cisco Unified Communications Manager (Unified Communications Manager), bringing rich
                              telepresence services to your system.

For detailed tasks about how to configure Cisco TelePresence VCS to integrate with your system, see the deployment guides
                              at http://www.cisco.com/c/en/us/support/unified-communications/telepresence-video-communication-server-vcs/products-installation-and-configuration-guides-list.html .