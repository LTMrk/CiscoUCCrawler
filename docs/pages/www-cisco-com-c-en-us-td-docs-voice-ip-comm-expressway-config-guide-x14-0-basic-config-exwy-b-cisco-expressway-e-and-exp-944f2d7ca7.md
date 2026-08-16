---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-basic-config-exwy-b-cisco-expressway-e-and-exp-944f2d7ca7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/basic_config/exwy_b_cisco-expressway-e-and-expressway-c-basic-configuration-deployment-guide-x14-0/exwy_m_system-checks.html
retrieved_at: 2026-08-16T15:27:48.962697+00:00
---

Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

# Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

Updated: April 14, 2021

Chapter: System Checks

## Chapter: System Checks

# System Checks

## Zone Status

Go to Status > Zones on both Expressway-C and Expressway-E to check that the traversal zone is Active . You can also check the zone status in Configuration > Zones > Zones .

If the traversal zone is not active, do the following:

Review the traversal zone configuration.

Check that the relevant ports are enabled for outbound routing on the NAT and firewall devices located between the Expressway-C
                                 and Expressway-E. See Appendix 3: Firewall and NAT Settings .

Check that the username and password credentials are configured correctly (and match) on Expressway-C and Expressway-E traversal
                                 zones and in the authentication database on the Expressway-E.

## Registration Status

Check that all endpoints which are expected to be registered are actually registered to the relevant Expressway. And that
                           they are registering the expected aliases. All successfully registered endpoints are listed on Status > Registrations > By device .

If the expected endpoints are not registered, review the following items:

The endpoint’s registration configuration. Is it configured to register with the Expressway-E if located on the external network
                                 / internet, and to register with the Expressway-C if located on the internal network?

The SIP domains ( Task 7: Configuring SIP Domains ).

Any registration restriction configuration applied to the Expressway (optional, Task 18: Configuring Registration Restriction Policy (Optional) ).

In some cases, home endpoints may fail to register when using SRV records. This can happen if the endpoint uses the home router
                           for its DNS server, and the router's DNS server software doesn't support SRV records lookup. (Also applies to the DNS server
                           being used by a PC when Jabber Video is running on it.) If registration failure occurs, do either of the following:

Change the DNS server on the endpoint to use a publicly available DNS server which can resolve SRV record lookups. For example, Google – 8.8.8.8

Change the SIP server address on the endpoint to use the FQDN of a node in the Expressway cluster and not the cluster SRV
                                 record. So that the device performs an AAAA or A record lookup.

## Call Signaling

If calls do not complete, despite the endpoints being successfully registered to a Expressway:

Review the  Expressway-C search rule configuration.

Review the Expressway-E search rule configuration.

Check the search history page for search attempts and failures ( Status > Search history ).

Check the Event Log for call connection failure reasons ( Status > Logs > Event Log ).

## Connectivity Test Tool

The SRV connectivity tester is a network utility that tests whether the Expressway can connect to particular services on a
                           given domain. You can use this tool to proactively test your connectivity while configuring Expressway-based solutions such
                           as Cisco Webex Hybrid Call Service or business-to-business video calling.You specify the DNS Service Record Domain and the
                           Service Record Protocols you want to query for that domain. The Expresswaydoes a DNS SRV query for each specified protocol,
                           and then attempts TCP connections to the hosts returned by the DNS. If you specify TLS, the Expressway only attempts a TLS
                           connection after the TCP succeeds. The Expressway connectivity test page shows the DNS response and the connection attempts.
                           For any connection failures, the reason is provided along with advice to help with resolving specific issues. To troubleshoot
                           connectivity, you can download the TCP data from your test in .pcap format. You can selectively download a dump of the DNS
                           query, or a specific connection attempt, or you can get a single .pcap file showing the whole test.

What To Do Next

When you've completed the system checks and are satisfied that the system is working as expected, Create a System Backup and then go on to " Optional Configuration Tasks " .