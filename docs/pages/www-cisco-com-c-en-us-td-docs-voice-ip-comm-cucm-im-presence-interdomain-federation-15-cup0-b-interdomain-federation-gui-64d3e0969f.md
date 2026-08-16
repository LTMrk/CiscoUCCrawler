---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-interdomain-federation-15-cup0-b-interdomain-federation-gui-64d3e0969f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/interdomain_federation/15/cup0_b_interdomain-federation-guide-15/cup0_b_interdomain-federation-1251su3_chapter_010111.html
retrieved_at: 2026-08-16T16:13:35.275651+00:00
---

Interdomain Federation Guide for the IM and Presence Service, Release 15

# Interdomain Federation Guide for the IM and Presence Service, Release 15

Updated: February 29, 2024

Chapter: IM and Presence Service Configuration for SIP Open Federation

## Chapter: IM and Presence Service Configuration for SIP Open Federation

- IM and Presence Service Configuration for SIP Open Federation

- Configure Default Static Routes for SIP Open Federation on IM and Presence Service

# IM and Presence Service Configuration for SIP Open Federation

## IM and Presence Service Configuration for SIP Open Federation

Cisco IM and Presence service supports SIP open federation for Cisco Jabber clients.

As an administrator, you can configure SIP open federation allowing Cisco Jabber users seamlessly federate with users from
                           all available domains.

This feature establishes the co-existence of open IM federation for both SIP and XMPP clients in the IM and Presence server.
                           Unlike in Controlled SIP Federation , where you must configure each federated domain separately, you can configure open federation for all domains with a single
                           static route. The static route lets Cisco Jabber federate with any external domain. More importantly, it significantly cuts
                           down the time to configure and maintain SIP federation for individual domains.

SIP Open Federation is partially configured by default on the IM and Presence Service. All you need to do to make it work
                           is to enable and activate the default static route ( .* ). See Configure Default Static Routes for SIP Open Federation on IM and Presence Service for more information.

Although the static route that enables SIP open federation is added by default, it is disabled in the following conditions:

When you install IM and Presence for the first time, or

During upgrade to a newer version of IM and Presence from an older version which does not support SIP open federation (for
                                 example, IM and Presence Release 12.5(1)SU2 or earlier)

### How SIP Open Federation Works

When a SIP request is made from any external domain, the Cisco XCP SIP Federation Connection Manager (SIP CM) checks if the
                              domain is configured or cached in the system. If the domain doesn't exist, the SIP CM sends that packet to the Cisco XCP router
                              to check the cache. If it does not find the domain in the cache, it sends the packet to the XMPP Federation Connection Manager
                              (XMPP CM). If the XMPP CM returns an error, the XCP router sends the request to the SIP CM and it finally routes that packet
                              using the pre-defined open federation route.

A SIP domain is added to the cache after the first successful correspondence and the routing with the SIP CM continues as
                              if the domain is added by the administrator. Subsequently, there will be no routing to XMPP CM and waiting on specific error.

Once the static route is configured and unblocked, you cannot block any SIP domains (new or cached) from the IM and Presence
                              node. However, if you include Expressway in your deployment, you can block certain SIP domains on the Expressway itself.

You can always disable SIP Open Federation altogether by blocking the default static route by checking the Block Route check
                              box on the Static Route page.

Disabling SIP Open Federation prevents new domains from being added, while the traffic with existing domains continues to
                              work. Administrator can remove a domain manually from SIP Federated Domains UI page to block the traffic within that domain.

When you enable SIP Open Federation, static routes are given first preference over the predefined default route.

When the unknown domain is federated through the SIP open federation, the domain is automatically cached into the server and
                              listed in the SIP open federation domains page ( Presence > Interdomain Federation > SIP Federation ).

As a result, when a request is hit from the cached domain, it directly federates with your domain bypassing the whole route
                              new domain discovery process as described above. This continues till you remove the cached domain from the list on the IM
                              and Presence server (or block it explicitly on the Expressway server).

### Configure Default Static Routes for SIP Open Federation on IM and Presence Service

SIP Open Federation is partially configured  by default on the IM and Presence Service. All you need to make it work is to
                                 unblock the static route and configure Next Hop , Next Hop Port , and Protocol Type .

Use this procedure to set up your static routes for SIP Open Federation:

Step 1

Enable XMPP federation either on the IM and Presence node or Expressway-E (if included in the deployment) for the static pre-defined
                                          route to work.

For more information on how to enable XMPP federation, see Chat and Presence XMPP Federation and Microsoft SIP Federation using IM and Presence or Expressway at:

https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html

Step 2

In Cisco Unified CM IM and Presence Administration, choose Presence > Routing > Static Routes .

Step 3

Click Find . The pre-defined static route (*.) is displayed.

Step 4

Click on the pre-defined static route (*.).

The Static Route Configuration page appears.

For SIP open federation, fields such as Destination Pattern , Route Type , Priority , Weight , and Allow Specific Route are prepopulated with default values.

Step 5

In the Next Hop field, enter the IP Address, FQDN or hostname of the next hop server.

Step 6

In the Next Hop Port field, enter the destination port on the Next Hop server.

Step 7

From the Protocol Type dropdown, select the protocol for the static route, such as, TCP, UDP, or TLS.

Step 8

Set the Service field to On if you want to be able to take a static route out of service without having to remove it completely from the
                                          system and add it again.

Step 9

Uncheck the Block Route check box.

Step 10

Click Save .

| Note | When you enable SIP Open Federation, static routes are given first preference over the predefined default route. |
|---|---|

| Step 1 | Enable XMPP federation either on the IM and Presence node or Expressway-E (if included in the deployment) for the static pre-defined
                                          route to work. For more information on how to enable XMPP federation, see Chat and Presence XMPP Federation and Microsoft SIP Federation using IM and Presence or Expressway at: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html |
|---|---|
| Step 2 | In Cisco Unified CM IM and Presence Administration, choose Presence > Routing > Static Routes . |
| Step 3 | Click Find . The pre-defined static route (*.) is displayed. |
| Step 4 | Click on the pre-defined static route (*.). The Static Route Configuration page appears. Note For SIP open federation, fields such as Destination Pattern , Route Type , Priority , Weight , and Allow Specific Route are prepopulated with default values. | Note | For SIP open federation, fields such as Destination Pattern , Route Type , Priority , Weight , and Allow Specific Route are prepopulated with default values. |
| Note | For SIP open federation, fields such as Destination Pattern , Route Type , Priority , Weight , and Allow Specific Route are prepopulated with default values. |
| Step 5 | In the Next Hop field, enter the IP Address, FQDN or hostname of the next hop server. |
| Step 6 | In the Next Hop Port field, enter the destination port on the Next Hop server. |
| Step 7 | From the Protocol Type dropdown, select the protocol for the static route, such as, TCP, UDP, or TLS. |
| Step 8 | Set the Service field to On if you want to be able to take a static route out of service without having to remove it completely from the
                                          system and add it again. |
| Step 9 | Uncheck the Block Route check box. |
| Step 10 | Click Save . |

| Note | For SIP open federation, fields such as Destination Pattern , Route Type , Priority , Weight , and Allow Specific Route are prepopulated with default values. |
|---|---|