---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-windows-9-7-cjab-bk-c606d8a9-00-cisco-jabber-dns-configuration-guide--57ddd42c89
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/Windows/9_7/CJAB_BK_C606D8A9_00_cisco-jabber-dns-configuration-guide/CJAB_BK_C606D8A9_00_cisco-jabber-dns-configuration-guide_chapter_01.html
retrieved_at: 2026-08-21T05:27:12.620694+00:00
---

Cisco Jabber DNS Configuration Guide

# Cisco Jabber DNS Configuration Guide

Updated: September 28, 2017

Chapter: Domain Name System  Designs

## Chapter: Domain Name System  Designs

Contents

# Domain Name System  Designs

- Separate domain names outside and inside the corporate network.

- Same domain name outside and inside the corporate network.

- Separate Domain Design

- Same Domain Design

## Separate Domain Design

An example of a separate domain design is one where your organization registers the following external domain with an Internet name authority: example.com .

- A subdomain of the external domain, for example, example.local .

- A different domain to the external domain, for example, example.com .

- The internal name server has zones that contain resource records for internal domains. The internal name server is authoritative for the internal domains.

- The internal name server forwards requests to the external name server when a DNS client queries for external domains.

- The external name server has a zone that contains resource records for your organization’s external domain. The external name server is authoritative for that domain.

- The external name server can forward requests to other external name servers. However, the external name server cannot forward requests to the internal name server.

## Same Domain Design

An example of a same domain design is one where your organization registers example.com as an external domain with an Internet name authority. Your organization also uses example.com as the name of the internal domain.

- Same Domain, Split-Brain

- Same Domain, Not Split-Brain

### Same Domain, Split-Brain

Two DNS zones represent the single domain; one DNS zone in the internal name server and one DNS zone in the external name server.

- Hosts inside the corporate network access only the internal name server.

- Hosts on the public Internet access only the external name server.

- Hosts that move between the corporate network and the public Internet access different name servers at different times.

### Same Domain, Not Split-Brain

In the same domain, not split-brain design, internal and external hosts are served by one set of name servers and can access the same DNS information.

This design is not common because it exposes more information about the internal network to potential attackers.

# Domain Name System  Designs

- Separate domain names outside and inside the corporate network.

- Same domain name outside and inside the corporate network.

- Separate Domain Design

- Same Domain Design

## Separate Domain Design

An example of a separate domain design is one where your organization registers the following external domain with an Internet name authority: example.com .

- A subdomain of the external domain, for example, example.local .

- A different domain to the external domain, for example, example.com .

- The internal name server has zones that contain resource records for internal domains. The internal name server is authoritative for the internal domains.

- The internal name server forwards requests to the external name server when a DNS client queries for external domains.

- The external name server has a zone that contains resource records for your organization’s external domain. The external name server is authoritative for that domain.

- The external name server can forward requests to other external name servers. However, the external name server cannot forward requests to the internal name server.

## Same Domain Design

An example of a same domain design is one where your organization registers example.com as an external domain with an Internet name authority. Your organization also uses example.com as the name of the internal domain.

- Same Domain, Split-Brain

- Same Domain, Not Split-Brain

### Same Domain, Split-Brain

Two DNS zones represent the single domain; one DNS zone in the internal name server and one DNS zone in the external name server.

- Hosts inside the corporate network access only the internal name server.

- Hosts on the public Internet access only the external name server.

- Hosts that move between the corporate network and the public Internet access different name servers at different times.

### Same Domain, Not Split-Brain

In the same domain, not split-brain design, internal and external hosts are served by one set of name servers and can access the same DNS information.

This design is not common because it exposes more information about the internal network to potential attackers.