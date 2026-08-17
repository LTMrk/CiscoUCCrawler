---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-windows-9-7-cjab-bk-c606d8a9-00-cisco-jabber-dns-configuration-guide--f0e75a65ca
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/Windows/9_7/CJAB_BK_C606D8A9_00_cisco-jabber-dns-configuration-guide/CJAB_BK_C606D8A9_00_cisco-jabber-dns-configuration-guide_chapter_010.html
retrieved_at: 2026-08-17T03:32:06.608415+00:00
---

Cisco Jabber DNS Configuration Guide

# Cisco Jabber DNS Configuration Guide

Updated: September 28, 2017

Chapter: Service (SRV) Records

## Chapter: Service (SRV) Records

Contents

# Service (SRV) Records

You deploy multiple DNS SRV records in different locations on your enterprise DNS structure. Understand which records you should provision on which name servers. Review examples of SRV records to ensure a successful deployment.

- Deploy SRV Records

- SRV Records

## Deploy SRV Records

The client queries name servers for records in the services domain. The services domain is determined as described in How the Client Discovers Available Services .

You must deploy SRV records in each DNS zone for those service domains if your organization has multiple subsets of users who use different service domains.

### Deploy SRV Records in a Separate Domain Structure

In a separate name design there are two domains, an internal domain and an external domain. The client queries for SRV records in the services domain. The internal name server must serve records for the services domain. However in a separate name design, a zone for the services domain might not exist on the internal name server.

- Deploy records within an internal zone for the services domain.

- Deploy records within a pinpoint subdomain zone on the internal name server.

#### Use an Internal Zone for a Services Domain

If you do not already have a zone for the services domain on the internal name server, you can create one. This method makes the internal name server authoritative for the services domain. Because it is authoritative, the internal name server does not forward queries to any other name server.

This method changes the forwarding relationship for the entire domain and has the potential to disrupt your internal DNS structure. If you cannot create an internal zone for the services domain, you can create a pinpoint subdomain zone on the internal name server.

#### Use a Pinpoint Subdomain Zone

- Cisco Jabber for
				  Windows 9.6.x

- Cisco Jabber for iPhone
				  and iPad 9.6.0

Support of the fixed pinpoint subdomain has been replaced in later versions of Cisco Jabber by the support of the new VoiceServicesDomain configuration key.

- Internal  DNS authoritative for : example.local

- External DNS authoritative for : example.com

Set VoiceServicesDomain=cisco-uc.example.com

Create a zone on both the internal and external DNS server for cisco-uc.example.com .

- _cisco-uds ._tcp.example.com (on Internal DNS)

- _cuplogin ._tcp.example.com (on Internal DNS)

You can create a pinpoint subdomain and zone on the internal name server. The pinpoint zone provides a dedicated location to serve specific records for the pinpoint subdomain. As a result, the internal name server becomes authoritative for that subdomain. The internal name server does not become authoritative for the parent domain, so the behavior of queries for records in the parent domain does not change.

The following diagram illustrates configuration created by the procedure.

In this configuration, the following SRV records are deployed with the internal DNS name server:

- _cisco-uds ._tcp.example.com

- _cuplogin ._tcp.example.com

You must use the following name for the pinpoint subdomain zone: cisco-internal. services-domain .

The external name server contains a zone for the parent external domain, example.com .

The internal name server contains a zone for the parent internal domain, example.local .

The Cisco Jabber Services Domain is example.com .

The external name server contains a zone for the parent external domain, example.com .

- Zone for the parent internal domain, example.local .

- Zone for the pinpoint subdmain zone, cisco-internal.example.com .

The internal name server serves the _cisco-uds and _cuplogin SRV records from cisco-internal.example.com .

When the client queries the name server for SRV records, it issues additional queries if the name server does not return _cisco-uds or _cuplogin .

The additional queries check for the cisco-internal. domain-name pinpoint subdomain zone.

- _cisco-uds ._tcp.example.com

- _cuplogin ._tcp.example.com

- _collab-edge ._tls.example.com

- _cisco-uds ._tcp.cisco-internal.example.com

- _cuplogin ._tcp.cisco-internal.example.com

## SRV Records

Understand which SRV records you should deploy and review examples of each SRV record.

- External Records

- Internal Records

### External Records

Provides the location of the Cisco VCS Expressway or Cisco Expressway-E server.

You must use the fully qualified domain name (FQDN) as the hostname in the SRV record.

The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides.

```
_collab-edge._tls.example.com   SRV service location:
          priority       = 3
          weight         = 7
          port           = 8443
          svr hostname   = vcse1.example.com
_collab-edge._tls.example.com   SRV service location:
          priority       = 4
          weight         = 8
          port           = 8443
          svr hostname   = vcse2.example.com
_collab-edge._tls.example.com   SRV service location:
          priority       = 5
          weight         = 0
          port           = 8443
          svr hostname   = vcse3.example.com
```

### Internal Records

Provides the location of Cisco Unified
				  Communications Manager version 9 and higher.

In an environment with multiple Cisco Unified
				  Communications Manager clusters, you must configure the Intercluster Lookup Service (ILS). ILS enables the client to find the user's home cluster and discover services.

Provides the location of Cisco Unified Presence .

You should use the fully qualified domain name (FQDN) as the hostname in the SRV record.

```
_cisco-uds._tcp.example.com     SRV service location:
          priority       = 6
          weight         = 30
          port           = 8443
          svr hostname   = cucm3.example.com
_cisco-uds._tcp.example.com     SRV service location:
          priority       = 2
          weight         = 20
          port           = 8443
          svr hostname   = cucm2.example.com
_cisco-uds._tcp.example.com     SRV service location:
          priority       = 1
          weight         = 5
          port           = 8443
          svr hostname   = cucm1.example.com
```

```
_cuplogin._tcp.example.com      SRV service location:
          priority       = 8
          weight         = 50
          port           = 8443
          svr hostname   = cup3.example.com
_cuplogin._tcp.example.com      SRV service location:
          priority       = 5
          weight         = 100
          port           = 8443
          svr hostname   = cup1.example.com
_cuplogin._tcp.example.com      SRV service location:
          priority       = 7
          weight         = 4
          port           = 8443
          svr hostname   = cup2.example.com
```

# Service (SRV) Records

You deploy multiple DNS SRV records in different locations on your enterprise DNS structure. Understand which records you should provision on which name servers. Review examples of SRV records to ensure a successful deployment.

- Deploy SRV Records

- SRV Records

## Deploy SRV Records

The client queries name servers for records in the services domain. The services domain is determined as described in How the Client Discovers Available Services .

You must deploy SRV records in each DNS zone for those service domains if your organization has multiple subsets of users who use different service domains.

### Deploy SRV Records in a Separate Domain Structure

In a separate name design there are two domains, an internal domain and an external domain. The client queries for SRV records in the services domain. The internal name server must serve records for the services domain. However in a separate name design, a zone for the services domain might not exist on the internal name server.

- Deploy records within an internal zone for the services domain.

- Deploy records within a pinpoint subdomain zone on the internal name server.

#### Use an Internal Zone for a Services Domain

If you do not already have a zone for the services domain on the internal name server, you can create one. This method makes the internal name server authoritative for the services domain. Because it is authoritative, the internal name server does not forward queries to any other name server.

This method changes the forwarding relationship for the entire domain and has the potential to disrupt your internal DNS structure. If you cannot create an internal zone for the services domain, you can create a pinpoint subdomain zone on the internal name server.

#### Use a Pinpoint Subdomain Zone

- Cisco Jabber for
				  Windows 9.6.x

- Cisco Jabber for iPhone
				  and iPad 9.6.0

Support of the fixed pinpoint subdomain has been replaced in later versions of Cisco Jabber by the support of the new VoiceServicesDomain configuration key.

- Internal  DNS authoritative for : example.local

- External DNS authoritative for : example.com

Set VoiceServicesDomain=cisco-uc.example.com

Create a zone on both the internal and external DNS server for cisco-uc.example.com .

- _cisco-uds ._tcp.example.com (on Internal DNS)

- _cuplogin ._tcp.example.com (on Internal DNS)

You can create a pinpoint subdomain and zone on the internal name server. The pinpoint zone provides a dedicated location to serve specific records for the pinpoint subdomain. As a result, the internal name server becomes authoritative for that subdomain. The internal name server does not become authoritative for the parent domain, so the behavior of queries for records in the parent domain does not change.

The following diagram illustrates configuration created by the procedure.

In this configuration, the following SRV records are deployed with the internal DNS name server:

- _cisco-uds ._tcp.example.com

- _cuplogin ._tcp.example.com

You must use the following name for the pinpoint subdomain zone: cisco-internal. services-domain .

The external name server contains a zone for the parent external domain, example.com .

The internal name server contains a zone for the parent internal domain, example.local .

The Cisco Jabber Services Domain is example.com .

The external name server contains a zone for the parent external domain, example.com .

- Zone for the parent internal domain, example.local .

- Zone for the pinpoint subdmain zone, cisco-internal.example.com .

The internal name server serves the _cisco-uds and _cuplogin SRV records from cisco-internal.example.com .

When the client queries the name server for SRV records, it issues additional queries if the name server does not return _cisco-uds or _cuplogin .

The additional queries check for the cisco-internal. domain-name pinpoint subdomain zone.

- _cisco-uds ._tcp.example.com

- _cuplogin ._tcp.example.com

- _collab-edge ._tls.example.com

- _cisco-uds ._tcp.cisco-internal.example.com

- _cuplogin ._tcp.cisco-internal.example.com

## SRV Records

Understand which SRV records you should deploy and review examples of each SRV record.

- External Records

- Internal Records

### External Records

Provides the location of the Cisco VCS Expressway or Cisco Expressway-E server.

You must use the fully qualified domain name (FQDN) as the hostname in the SRV record.

The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides.

```
_collab-edge._tls.example.com   SRV service location:
          priority       = 3
          weight         = 7
          port           = 8443
          svr hostname   = vcse1.example.com
_collab-edge._tls.example.com   SRV service location:
          priority       = 4
          weight         = 8
          port           = 8443
          svr hostname   = vcse2.example.com
_collab-edge._tls.example.com   SRV service location:
          priority       = 5
          weight         = 0
          port           = 8443
          svr hostname   = vcse3.example.com
```

### Internal Records

Provides the location of Cisco Unified
				  Communications Manager version 9 and higher.

In an environment with multiple Cisco Unified
				  Communications Manager clusters, you must configure the Intercluster Lookup Service (ILS). ILS enables the client to find the user's home cluster and discover services.

Provides the location of Cisco Unified Presence .

You should use the fully qualified domain name (FQDN) as the hostname in the SRV record.

```
_cisco-uds._tcp.example.com     SRV service location:
          priority       = 6
          weight         = 30
          port           = 8443
          svr hostname   = cucm3.example.com
_cisco-uds._tcp.example.com     SRV service location:
          priority       = 2
          weight         = 20
          port           = 8443
          svr hostname   = cucm2.example.com
_cisco-uds._tcp.example.com     SRV service location:
          priority       = 1
          weight         = 5
          port           = 8443
          svr hostname   = cucm1.example.com
```

```
_cuplogin._tcp.example.com      SRV service location:
          priority       = 8
          weight         = 50
          port           = 8443
          svr hostname   = cup3.example.com
_cuplogin._tcp.example.com      SRV service location:
          priority       = 5
          weight         = 100
          port           = 8443
          svr hostname   = cup1.example.com
_cuplogin._tcp.example.com      SRV service location:
          priority       = 7
          weight         = 4
          port           = 8443
          svr hostname   = cup2.example.com
```

| Step 1 | Create a new zone on the internal name server. Important: You must use the following name for the pinpoint subdomain zone: cisco-internal. services-domain . The pinpoint subdomain zone responds to queries from hosts on the internal network. However, the domain is a subdomain of the external domain. The first part of the name is a fixed value that the client expects, cisco-internal . |
|---|---|
| Step 2 | Deploy the _cisco-uds and _cuplogin SRV records in the pinpoint subdomain zone. Before creating a pinpoint subdomain zone The external name server contains a zone for the parent external domain, example.com . The internal name server contains a zone for the parent internal domain, example.local . The Cisco Jabber Services Domain is example.com . After creating a pinpoint subdomain zone The external name server contains a zone for the parent external domain, example.com . Internal name server contains the following: Zone for the parent internal domain, example.local . Zone for the pinpoint subdmain zone, cisco-internal.example.com . The internal name server serves the _cisco-uds and _cuplogin SRV records from cisco-internal.example.com . |

| Service Record | Description |
|---|---|
| _collab-edge | Provides the location of the Cisco VCS Expressway or Cisco Expressway-E server. Note You must use the fully qualified domain name (FQDN) as the hostname in the SRV record. The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides. | Note | You must use the fully qualified domain name (FQDN) as the hostname in the SRV record. The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides. |
| Note | You must use the fully qualified domain name (FQDN) as the hostname in the SRV record. The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides. |

| Note | You must use the fully qualified domain name (FQDN) as the hostname in the SRV record. The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides. |
|---|---|

| Service Record | Description |
|---|---|
| _cisco-uds | Provides the location of Cisco Unified
				  Communications Manager version 9 and higher. Remember: In an environment with multiple Cisco Unified
				  Communications Manager clusters, you must configure the Intercluster Lookup Service (ILS). ILS enables the client to find the user's home cluster and discover services. |
| _cuplogin | Provides the location of Cisco Unified Presence . |

| Note | You should use the fully qualified domain name (FQDN) as the hostname in the SRV record. |
|---|---|

| Step 1 | Create a new zone on the internal name server. Important: You must use the following name for the pinpoint subdomain zone: cisco-internal. services-domain . The pinpoint subdomain zone responds to queries from hosts on the internal network. However, the domain is a subdomain of the external domain. The first part of the name is a fixed value that the client expects, cisco-internal . |
|---|---|
| Step 2 | Deploy the _cisco-uds and _cuplogin SRV records in the pinpoint subdomain zone. Before creating a pinpoint subdomain zone The external name server contains a zone for the parent external domain, example.com . The internal name server contains a zone for the parent internal domain, example.local . The Cisco Jabber Services Domain is example.com . After creating a pinpoint subdomain zone The external name server contains a zone for the parent external domain, example.com . Internal name server contains the following: Zone for the parent internal domain, example.local . Zone for the pinpoint subdmain zone, cisco-internal.example.com . The internal name server serves the _cisco-uds and _cuplogin SRV records from cisco-internal.example.com . |

| Service Record | Description |
|---|---|
| _collab-edge | Provides the location of the Cisco VCS Expressway or Cisco Expressway-E server. Note You must use the fully qualified domain name (FQDN) as the hostname in the SRV record. The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides. | Note | You must use the fully qualified domain name (FQDN) as the hostname in the SRV record. The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides. |
| Note | You must use the fully qualified domain name (FQDN) as the hostname in the SRV record. The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides. |

| Note | You must use the fully qualified domain name (FQDN) as the hostname in the SRV record. The client requires the FQDN to use the cookie that the Cisco VCS Expressway or Cisco Expressway-E server provides. |
|---|---|

| Service Record | Description |
|---|---|
| _cisco-uds | Provides the location of Cisco Unified
				  Communications Manager version 9 and higher. Remember: In an environment with multiple Cisco Unified
				  Communications Manager clusters, you must configure the Intercluster Lookup Service (ILS). ILS enables the client to find the user's home cluster and discover services. |
| _cuplogin | Provides the location of Cisco Unified Presence . |

| Note | You should use the fully qualified domain name (FQDN) as the hostname in the SRV record. |
|---|---|