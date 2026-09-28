---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-ipad-9-3-x-jabi-bk-cceaf656-00-cisco-jabber-video-for-ipad-jabi-bk-cc-8bfe7439cc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/iPad/9_3_x/JABI_BK_CCEAF656_00_cisco-jabber-video-for-ipad/JABI_BK_CCEAF656_00_cisco-jabber-video-for-ipad_chapter_01.html
retrieved_at: 2026-08-21T19:43:34.440879+00:00
---

Cisco Jabber Video for iPad 9.3.4 Administration Guide

# Cisco Jabber Video for iPad 9.3.4 Administration Guide

Updated: November 22, 2013

Chapter: Set up Simple Sign-In using DNS SRV

## Chapter: Set up Simple Sign-In using DNS SRV

# Set up Simple Sign-In using DNS SRV

You can set up simple sign-in by using Domain Name Server Service Records (DNS SRV). DNS SRV adds an automated discovery mechanism that can eliminate the need for manual account configuration in many deployments. DNS SRV is a standards-based mechanism that enables an automated return of Unified Communications server addresses back to the Cisco Jabber Video for iPad client. The client reverts to the manual provisioning wizard if no DNS SRV records are configured.

There are two deployment models for DNS SRV when used with the client:

- Single Service In a Single Service deployment model only Instant Messaging and Presence or Unified Communications are deployed in a corporate network, not both. This may mean only Cisco WebEx Messenger or Cisco Unified Presence is deployed for Instant Messaging and Presence or Cisco Unified Communications or Cisco TelePresence Video Communication Server is deployed for video and voice calling. Administrators must configure DNS SRV according to the service and DNS SRV mapping table if only one service is deployed. Administrators need to add multiple records if they plan to deploy multiple servers for a single service. Each record must contain the proper priority and weighting information. Port numbering in DNS SRV records is not used by the client but it should still be configured to the default value. The client generates a server list based on the priority and weighting it discovers in the DNS SRV records. The client moves through this server list and attempts to connect to each one, stopping when a successful connection to a reachable server is made. The client stops regardless of whether authentication to that server is successful or not.

- Multiple Services Multiple Service deployments consist of some mix of Instant Messaging and Presence and Unified Communications services. Administrators must configure DNS SRV according to the service and DNS SRV mapping table. Administrators need to enable Unified Communications integration in Cisco WebEx Messenger or Cisco Unified Presence if they want to integrate the Unified Communications service with the Instant Messaging and Presence service. The client will not automatically sign into Unified Communication accounts after the user has signed into Instant Messaging and Presence accounts. Administrators need to add multiple records if they plan to deploy multiple servers for any single service. Each record must contain the proper priority and weighting information. Port numbering in DNS SRV records is not used by the client but it should still be configured to the default value. The client contains a service priority list that can be customized through a DNS TXT record. See Customize Discovery and Auto-Configuration for information on configuring these records. The client tries the first server in each service first. If it fails to connect to that service, it tries the next server in the same service. If it fails to authenticate with the server, it ignores the rest of the servers in this service and tries to sign-in the first server in next service. If it fails to authenticate to every server it discovered, it displays an error message to end user. The client remembers successful server connections and attempts to authenticate to them the next time the application is started. If authentication fails, the client automatically performs service discovery and sign-in with the current credentials.

Cisco requires administrators to set up a centralized TFTP server to enable DNS SRV for multi-cluster Cisco Unified Communications Manager deployments only. See Set Up Centralized TFTP Server for more information.

This section discusses this feature and how to configure it for your corporate deployment of the client.

The procedures presented in this section are specifically for this feature. Other procedures in other sections are still required for your service deployment. See How to Use this Document for information on what sections go with your specific deployment.

## Client Sign-In and Auto-Discovery

The client queries the Domain Name Server (DNS) when it is launched for the first time. After users enter their account (username@example.com), the client queries the DNS SRV records corresponding to the domain portion of the supplied accounts ( example.com in this instance). It expects responses from the DNS server that allow it to complete the configuration task and provide the user with service. The supplied account may be an email address or some other credential that uses the format of <username> @ <domain> . System administrators should make their users aware of the credentials needed to log into Cisco Jabber Video for iPad .

The administrator creates a new DNS SRV record for each type of service the enterprise has implemented. The client supports the following services:

- Cisco Unified Communications Manager Instant Messaging and Presence (formerly known as Cisco Unified Presence)

- Cisco WebEx Messenger (formerly known as Cisco WebEx Connect)

- Cisco Unified Communications Manager

- Cisco Telepresence Video Communication Server

- Cisco Jabber Video for Telepresence

- Cisco WebEx TelePresence

When both Instant Messaging and Presence and Unified Communications services are deployed (such as Cisco WebEx Messenger and Cisco Unified Communications Manager), the client uses the Unified Communications server as configured in the Instant Messaging and Presence service (Cisco WebEx Messenger or Cisco Unified Presence), rather than any Unified Communication server supplied using the DNS SRV record.

## DNS SRV Record

A DNS SRV record provides information on the services available in a specific domain to a client. The client then chooses a server and uses it to connect to the deployed service or server. This section provides information on the form and format of DNS SRV records. See RFC 2782 for additional technical information about DNS SRV records.

The client queries the network for all possible services corresponding to the domain portion of the user-supplied email address. It then attempts to connect based on the services it discovers through the DNS SRV record results. If there is more than one service found, the client connects to the service in this order:

- Cisco WebEx Messenger

- Cisco Unified Presence

- Cisco Unified Communications Manager

- Cisco TelePresence Video Communication Server

- Cisco Jabber Video for Telepresence

- Cisco WebEx TelePresence

The administrator can override this default order. For information on modification, see Customize Discovery and Auto-Configuration .

## Set Up DNS SRV Records

DNS records consist of a series of entries that match a server name to a single IP address in a networked environment. DNS SRV records differ in that they match a service with a server, or set of servers, in a networked environment. In doing this, DNS SRV allows a client to only have to know what type of service it is looking for instead of the actual server. This aids deployment, server management, and service failover because most networked environments have multiple, load balanced servers attending to the needs of a particular service.

When multiple servers are configured for a single service, the client tries the next server if it is unable to connect to the first entry. In the case of an authentication failure for a given service, the client stops attempting to connect to that service and display an error message.

The following table lists the DNS SRV record types for the client.

The following table gives full examples of DNS SRV records that would be used with the deployment models discussed in this document.

Cisco WebEx Messenger

Cisco WebEx Messenger and Cisco Unified Communications Manager

Cisco WebEx Messenger and Cisco TelePresence Video Communication Server

Cisco WebEx Messenger and Cisco Jabber Video for TelePresence

_xmpp-client._tcp.example.com SRV 0 5222 c2s.example.com.webexconnect.com

Cisco Unified Presence

Cisco Unified Presence and Cisco Unified Communications Manager

_cisco-phone-http._tcp.example.com SRV 0 0 80 cucm.example.com

_sip._tcp.external.example.com SRV 0 0 5060 vcse.example.com

Administrators do not need to configure DNS SRV records for Cisco Jabber Video for TelePresence or Cisco WebEx TelePresence. They are already configured and available through the Internet.

The following is an example of a single DNS SRV record that responds to discovery requests by providing the Cisco Unified Presence server address that the client uses.

_cuplogin._tcp.example.com SRV 0 1 8443 cup.example.com

The port numbers provided in the SRV records are not utilized by the client. However, the records should be configured with the provided default values.

Weighting and priority are supported within the same DNS SRV record type. Weight only takes effect for SRV records with the same priority.

In this example, the client queries the network for all possible services and gets a response for the defined Cisco Unified Presence server. This tells the client to connect to this server using the supplied credentials as Cisco Unified Presence credentials instead of credentials for any other service.

Use the following general steps to create a new DNS SRV record:

## Set Up Centralized TFTP Server

Set up a centralized TFTP server if there are multiple Cisco Unified Communications Manager clusters in the same corporate domain. You must also add a DNS SRV record so this server can be discovered. The following is an example of what such a record might look like. The items in the record appear in the following order:

- SRV Record

- Priority

- Weight

- Port

- A Record

```
cisco-phone-tftp._tcp.example.com 0 0 69 cftp.example.com
```

The cisco-phone-tftp record type is used to point to the centralized TFTP server. This example allows the client to discover the server ctftp.example.com and directly download the device configuration.

Note the following about devices and device configuration files:

- All device names must be well formed. The first three letters of the device name should be TAB followed by the user name of the person associated with the device. If John Smith's user name is jsmith , a well formed device name example would be TABJSMITH . The total length of this device name cannot exceed 15 characters.

- Cisco highly recommends that administrators enable SIP Authentication for each tablet device in every cluster.

- Administrators must not add cisco-phone-http records in the corporate domain to ensure the centralized TFTP server is discovered.

## Customize Discovery and Auto-Configuration

The default service discovery order is:

- Cisco WebEx Messenger

- Cisco Unified Presence

- Cisco Unified Communications Manager

- Cisco TelePresence Video Communication Server

- Cisco Jabber Video for TelePresence

System administrators can customize service discovery priority using DNS TXT records. Service discovery priority customization may be necessary in networked environments that provide multiple services. DNS TXT records are defined in RFC 1035 . Examples of DNS TXT usage can be found in RFC 4408 (Sender Policy Framework) and RFC 5672 (DomainKeys Identified Mail).

Administrators deploying a DNS TXT record to customize service priority must use a custom form of the typical record called a Jabber Simple Configuration Priority (JSCP) record. A typical DNS TXT record has the following format:

name ttl class TXT text

A Jabber Simple Configuration Priority record changes that slightly:

name ttl class TXT JSCP-specific-text

The JSCP-specific-text parameter defines the custom service priority. This parameter contains quoted text in the following format:

"v=jscpv1 <dns-srv-name>; <dns-srv-name>; ..."

Each service is defined using the codes defined in DNS SRV record. Priority is assigned to a service by the location it appears in the service list. The first service in the list is of the highest priority and subsequent entries are of a lesser priority.

If your Cisco WebEx Messenger deployment uses Single Sign-On (SSO), the Cisco WebEx Messenger service must always be the first service in the list.

When customizing service priority using a DNS TXT record:

- The priorities found in the DNS TXT record always supercede the default priority list.

- The DNS SRV names in DNS TXT record are recognized by the client even if additional records are present.

- A DNS SRV name with no corresponding DNS SRV record is ignored without error.

- The default priority list is used and an error logged if the DNS TXT record uses an incorrect format or empty.

- The default priority list is used if no DNS TXT record is found.

The following is an example of DNS TXT record with DNS SRV records and using a JSCP formatted record.

; UC DNS SRV records

_xmpp-client._tcp.example.com 86400 IN SRV 0 5 5222 xmppserver.example.com

_cisco-phone-tftp._tcp.example.com 86400 IN SRV 0 5 6970 cucm8xserver.example.com

_sip._tcp.internal.example.com 86400 IN SRV 0 5 5060 sipserver.example.com

; JSCP TXT RR example - ignore WebEx Messenger service and favor VCS service with centralized tftp over CUCM service.

cisco.com 30 IN TXT "v=jscpv1 _sip._tcp.internal.example.com; _cisco-phone-tftp._tcp.example.com; "

cisco.com 30 IN TXT "v=jscpv1 _cisco-phone-tftp._tcp.example.com"

This example is constructed so that the client ignores the Cisco WebEx Messenger service in favor of the Cisco Telepresence Video Communications Server service with centralized TFTP over the Cisco Unified Communications Manager service.

Follow these general steps to create new DNS SRV and DNS TXT records.

## Troubleshooting

Use the following information when troubleshooting:

- Troubleshoot DNS configuration from a network-connected device. Use the NSLOOKUP command from the Command Prompt in a Microsoft Windows environment. Information on this command can be found at http:/​/​support.microsoft.com/​kb/​816587 .

Contact your system administrator before performing manual service discovery. Performing service discovery signs you out of your current account and may remove existing account settings.

| Note | The procedures presented in this section are specifically for this feature. Other procedures in other sections are still required for your service deployment. See How to Use this Document for information on what sections go with your specific deployment. |
|---|---|

| Service | DNS SRV Record |
|---|---|
| Cisco WebEx Messenger | _xmpp-client._tcp |
| Cisco Unified Presence | _cuplogin._tcp |
| Cisco Unified Communications Manager TFTP | _cisco-phone-tftp._tcp |
| Cisco Unified Communications Manager CCMCIP | _cisco-phone-http._tcp |
| Cisco TelePresence Video Communication Server (Internal) | _sip._tcp.internal |
| Cisco TelePresence Video Communication Server (External) | _sip._tcp.external |
| Cisco Jabber Video for TelePresence | _ciscowtp._tcp |
| Cisco WebEx TelePresence | _ciscowtp._tcp |

| Deployment Model | Full DNS SRV Record Example |
|---|---|
| Cisco WebEx Messenger Cisco WebEx Messenger and Cisco Unified Communications Manager Cisco WebEx Messenger and Cisco TelePresence Video Communication Server Cisco WebEx Messenger and Cisco Jabber Video for TelePresence | _xmpp-client._tcp.example.com SRV 0 5222 c2s.example.com.webexconnect.com |
| Cisco Unified Presence Cisco Unified Presence and Cisco Unified Communications Manager | _cuplogin._tcp.example.com SRV 0 1 8443 cup.example.com |
| Cisco Unified Communications Manager | _cisco-phone-tftp._tcp.example.com SRV 0 0 69 cucm.example.com _cisco-phone-http._tcp.example.com SRV 0 0 80 cucm.example.com |
| Cisco TelePresence Video Communication Server | _sip._tcp.internal.example.com SRV 0 0 5060 vcsc.example.com _sip._tcp.external.example.com SRV 0 0 5060 vcse.example.com |
| Cisco Jabber Video for TelePresence | _ciscowtp._tcp.jabber.com SRV 0 0 443 boot.ciscojabbervideo.com |
| Cisco WebEx TelePresence | _ciscowtp._tcp.webex.com SRV 0 0 443 boot.telepresence.webex.com |

| Note | Administrators do not need to configure DNS SRV records for Cisco Jabber Video for TelePresence or Cisco WebEx TelePresence. They are already configured and available through the Internet. |
|---|---|

| Note | The port numbers provided in the SRV records are not utilized by the client. However, the records should be configured with the provided default values. |
|---|---|

| Note | Weighting and priority are supported within the same DNS SRV record type. Weight only takes effect for SRV records with the same priority. |
|---|---|

| Step 1 | Compile information on the network services offered. |
|---|---|
| Step 2 | Determine the weighting and priority to assign to each server in the case of multiple servers. |
| Step 3 | Create the new DNS SRV records. |
| Step 4 | Deploy the new records to the network DNS configuration. |

| Note | Note the following about devices and device configuration files: All device names must be well formed. The first three letters of the device name should be TAB followed by the user name of the person associated with the device. If John Smith's user name is jsmith , a well formed device name example would be TABJSMITH . The total length of this device name cannot exceed 15 characters. Cisco highly recommends that administrators enable SIP Authentication for each tablet device in every cluster. Administrators must not add cisco-phone-http records in the corporate domain to ensure the centralized TFTP server is discovered. |
|---|---|

| Note | If your Cisco WebEx Messenger deployment uses Single Sign-On (SSO), the Cisco WebEx Messenger service must always be the first service in the list. |
|---|---|

| Step 1 | Compile information on the network services offered. |
|---|---|
| Step 2 | Determine the weighting and priority to assign to each server in the case of multiple servers. |
| Step 3 | Determine the order of service discovery. |
| Step 4 | Create the new DNS SRV records. |
| Step 5 | Create the DNS TXT record based on step 3. |
| Step 6 | Deploy the new DNS SRV records and DNS TXT record to the network DNS server. |

| Note | Contact your system administrator before performing manual service discovery. Performing service discovery signs you out of your current account and may remove existing account settings. |
|---|---|