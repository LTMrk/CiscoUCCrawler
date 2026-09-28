---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-interdomain-federation-14-cup0-b-interdomain-federation-gui-f02d9a523f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/interdomain_federation/14/cup0_b_interdomain-federation-guide-14/cup0_b_interdomain-federation-1251su3_chapter_01000.html
retrieved_at: 2026-08-16T16:27:50.645591+00:00
---

Interdomain Federation Guide for the IM and Presence Service, Release 14 and SUs

# Interdomain Federation Guide for the IM and Presence Service, Release 14 and SUs

Updated: January 22, 2023

Chapter: Interdomain Federation with Skype for Business

## Chapter: Interdomain Federation with Skype for Business

# Interdomain Federation with Skype for Business

This section explains the Interdomain Federation with Skype for Business.

## Skype for Business Interdomain Federation

The IM and Presence Service supports interdomain federation with Skype for Business server via Expressway. The following integrations
                              are supported:

Business to Business—Federation with a remote Skype for Business server in another company's network

Single Enterprise Network—Federation with an on-premise Skype for Business server that is located within the same enterprise
                                    network, but in a different domain.

You can also configure federation with a Skype for Business server that is hosted by an Office365 deployment. For details,
                                          including configuration information, refer to Interdomain Federation with Office 365 .

### Skype for Business Federation Example

With Business to Business federation, communication occurs between the IM and Presence Service on the left of the diagram,
                                       and a remote Skype for Business server that is located in another company's network on the right side of the diagram. This
                                       integation requires communications to cross the company firewall. So in addition to an Expressway-C that is deployed within
                                       the enterprise network, you must deploy Expressway-E within the DMZ of the firewall.

With Single Enterprise Network, an on-premise Skype for Business server is located in the company network, but in a separate
                                       domain. In the diagram, the Skype for Business server is within the internal firewall. This integration requires Expressway-C,
                                       but does not require Expressway-E as communication does not need to cross the firewall.

## Skype for Business Federation Task Flow

A business to business integration with another business that is deploying an on-premise Skype for Business server.

Within a single enterprise, you can configure interdomain federation between the IM and Presence Service and an on-premise
                                       Skype for Business server.

For federation with an Office 365-hosted Skype for Business deployment, go to Interdomain Federation with Office 365 .

### Before You Begin

By default, the Federation routing parameter is set to the database publisher node FQDN upon installation. If you want to
                              reset this value, go to Configure Federation Routing Parameters .

IM and Presence Service Configuration

Expressway Configuration

Skype for Business Configuration

Description

Step 1

Turn on Federation Services

Make sure that Federation services are running.

Step 2

Assign DNS SRV for IM and Presence

Configure a DNS SRV record so that Skype for Business can route traffic to the IM and Presence Service.

Step 3

Add Federated Domain to IM and Presence

Add domain entries for all Skype for Business domains.

Step 4

Configure Static Route on IM and Presence

Configure a static route that points to  Expressway-C.

Step 5

Add Expressway as a TLS Peer

Configure Expressway-C as a TLS peer.

Step 6

Add Expressway to Access Control List

Add all Expressway-C servers to an access control list.

Step 7

Restart Cisco XCP Router

After completing your configurations, restart the Cisco XCP Router service.

Step 8

Configure Expressway for Federation with Skype for Business

Configure Expressway for interdomain federation.

Step 9

Configure User Trust Settings

Configure trust settings for IM and Presence users.

Step 10

Configure Global Federation Access Settings

Configure global access edge settings for federation.

Step 11

Add IM and Presence as Allowed Domain

Optional. Complete this task only if your global access edge settings do not allow the IM and Presence domain.

Step 12

Add Expressway as SIP Federated Provider for IM and Presence

Optional. Complete this task only if you are not using a DNS SRV to route traffic to the IM and Presence Service.

Step 13

Exchange Certificates

Exchange certificates between the servers in your setup.

### Turn on Federation Services

Step 1

Log in to the Cisco Unified IM and Presence Serviceability user interface. Choose Tools > Service Activation .

Step 2

Fom the Server drop-down, choose an IM and Presence node and click Go .

Step 3

Under IM and Presence Services , make sure that the adjacent radio button to the Cisco XCP SIP Federation Connection Manager service is checked.

Step 4

Click Save .

Step 5

The Cisco SIP Proxy service must be running for SIP federation to work. Log in to the Cisco Unified IM and Presence Serviceability user interface. Choose Tools > Feature Services and verify that the Cisco SIP Proxy service is running.

### Assign DNS SRV for IM and Presence

Configure a DNS SRV record for the IM and Presence Service. Skype for Business uses this record to route traffic to IM and
                                 Presence Service via Expressway.

With business to business federation, the record must be a public DNS SRV that points to the Expressway-E IP addresses.

For federation within a single enterprise, you can use internal DNS that points to the Expressway-C IP addresses.  Expressway-E
                                       is not required as the federation takes place within a single enterprise.

Example :

```
nslookup
set type=srv
_sipfederationtls._tcp.expwye
```

where expwye is the domain for Expressway-E.

You can still configure interdomain federation without the DNS SRV record, but in this case, you must add the route manually
                                             on the Skype for Business server. If you choose to do this, you can skip this task.

#### What to do next

Add Federated Domain to IM and Presence

### Add Federated Domain to IM and Presence

On the IM and Presence Service, add a Federated domain entry for each Skype for Business domain that you want to federate
                                 with.

Step 1

From Cisco Unified CM IM and Presence Administration, choose Presence > Inter-Domain Federation > SIP Federation .

Step 2

Click Add New .

Step 3

In the Domain Name field, enter the Skype for Business domain.

Step 4

Enter a Description of the domain. For example, Skype for Business federated domain .

Step 5

From the Integration Type drop-down, select Inter-domain to OCS/Lync/S4B .

Step 6

Click Save .

#### What to do next

Restart Cisco XCP Router

### Configure Static Route on IM and Presence

On the IM and Presence Service, configure a static route for Skype for Business users. The static  route must use TLS and
                                 point to   Expressway-C.

Step 1

From Cisco Unified CM IM and Presence Administration, choose Presence > Routing > Static Routes .

Step 2

Click Add New .

Step 3

In the Destination Pattern field, enter the Skype for Business FQDN in a reversed format. For example, if the domain is s4b.com , enter .com.s4b.* .

Step 4

In the Next Hop field, enter the Expressway-C  IP address or FQDN.

Step 5

In the Next Hop Port field enter 5061 .

Step 6

From the Route Type drop-down list, choose Domain .

Step 7

From the Protocol Type drop-down list box, select TLS .

Step 8

Click Save .

#### What to do next

Add Expressway as a TLS Peer

### Add Expressway as a  TLS Peer

Use this procedure in the IM and Presence Service to configure Expressway-C as a peer for TLS.

Step 1

Add Expressway-C as a TLS peer subject:

From Cisco Unified CM IM and Presence Administration, choose System > Security > TLS Peer Subjects .

Click Add New .

In the Peer Subject Name field, enter the Expressway-C fully qualified domain name of the Expressway-C.

Enter a Description .

Click Save .

Step 2

Create a TLS Context that includes the Expressway TLS peer subject that you configured:

From Cisco Unified CM Administration, choose System > Security > TLS Context Configuration

Click Find .

Select Default_Cisco_UP_SIP_Proxy_Peer_Auth_TLS_Context .

Under TLS Cipher Mapping , use the arrows to move the desired TLS ciphers to the Selected TLS Ciphers box. However, leaving this at the default settng should be sufficient in most cases.

Under TLS Peer Subject Mapping , use the arrows to move the TLS peer subject that you created to the Selected TLS Peer Subjects list box.

Click Save .

### Add Expressway to Access Control List

On the IM and Presence Service, add inbound access control list (ACL) entries for each Expressway-C server so that Expressway-C
                                 can access the IM and Presence Service without authentication. For multicluster deployments, complete this procedure on each
                                 cluster.

If you have an ACL that provides global access ( Allow from all ), or an ACL which provides access to the domain on which the Expressway-C server resides (for example, Allow from company.com ) then you do not need to add ACL entries for the Expressway-C server.

Step 1

Log in to the IM and Presence Service publisher node.

Step 2

From Cisco Unified CM IM Administration, choose System > Security > Incoming ACL .

Step 3

Create your ACL entries:

Click Add New .

Enter a Description for the new ACL entry. For example, Skype for Business Federation via Expressway-C .

Enter an Address Pattern that provides access to the Expressway-C IP address or FQDN. For example, Allow from 10.10.10.1 or Allow from expwyc.company.com .

Click Save .

Repeat this set of steps to create another ACL entry. To provide server  access, you need two entries: an ACL with the server
                                                IP address, and an ACL with the server FQDN.

Step 4

Restart Cisco SIP Proxy services:

Choose Presence > Routing > Settings .

Click Restart All Proxy Services .

#### What to do next

Restart Cisco XCP Router

### Restart Cisco XCP Router

After completing your configurations, restart the Cisco XCP Router .

Step 1

From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services .

Step 2

From the Server drop-down list box, choose the IM and Presence database publisher node and click Go .

Step 3

Under IM and Presence Services , select the Cisco XCP Router service.

Step 4

Click Restart .

Step 5

Repeat this procedure for all IM and Presence Service cluster nodes.

#### What to do next

Configure Static Route on IM and Presence

### Configure Expressway for Federation with Skype for Business

After interdomain federation is configured on the IM and Presence Service, set up Expressway for interdomain federation with
                                 Skype for Business.

For business to business interdomain federation, you must deploy both Expressway-C and Expressway-E.

For interdomain federation with a Skype for Business server that is located within your enterprise network, you can deploy
                                       an Expressway-C cluster only as the communication does not need to extend across the WAN.

http://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html .

Make sure that your Expressway-C zone configuration points to the port that is associated with TLS Peer Authentication on
                                             the IM and Presence Service. You can confirm the correct port on Cisco Unified CM IM and Presence Administration by going
                                             to System > Application Listeners and confirming the port associated to Default Cisco SIP Proxy TLS Listener - Peer Auth . The default is 5062 .

#### What to do next

After Expressway is configured, proceed with the  Skype for Business setup:

Configure User Trust Settings

### Configure User Trust Settings

On the Skype for Business server, configure user trust settings for Federated IM and Presence users.

Step 1

Log in to the Skype for Business server.

Step 2

In the left navigation bar, click Federation and External Access .

Step 3

In the header bar, click EXTERNAL ACCESS POLICY .

Step 4

Click New and select User Policy .

Step 5

In the Name field, enter the IM and Presence domain

Step 6

Check the following options:

- Enable communications with federated users

- Enable communications with remote users

- Enable communications with public users

Step 7

Click Commit .

#### What to do next

Configure Global Federation Access Settings

### Configure Global Federation Access Settings

On the Skype for Business server, configure global access edge settings for SIP Federation.

Step 1

In the left navigation bar, click Federation and External Access .

Step 2

In the header bar, click ACCESS EDGE CONFIGURATION .

Step 3

Select Global .

Step 4

If you want to allow access to all domains globally, select each of the following options. Otherwise, choose which options
                                          you want to allow:

- Enable federation and public IM connectivity

- Enable partner domain discovery—Select this option to use a public DNS SRV record to route traffic to the IM and Presence
                                             Service. If you do not want to use a DNS SRV record, or do not have a DNS SRV record, leave this option unchecked.

- Enable remote user access

- Enable anonymous user access to conferences

If you choose not to allow access globally, you will have to add the IM and Presence manually as an allowed domain and a SIP
                                                         Federated Provider.

Step 5

Click Commit .

#### What to do next

If you configured restricted access  (i.e., you left some global options unchecked), Add IM and Presence as Allowed Domain .

If you allowed access globally, but do not have a public DNS SRV record for routing to IM and Presence Service, Add Expressway as SIP Federated Provider for IM and Presence .

Otherwise, if you allowed access globally, and you have a public DNS SRV record to route traffic to the IM and Presence Service, Exchange Certificates .

### Add IM and Presence as Allowed Domain

Use this procedure if the Global Access Edge settings on the Skype for Business server do not allow all domains. In this case,
                                 add a specific entry for the IM and Presence Service domain.

Step 1

In the left navigation bar, click Federation and External Access .

Step 2

In the header bar, click SIP FEDERATED DOMAINS .

Step 3

Click New and select Allowed domain .

Step 4

In the Domain name field, enter the IM and Presence domain.

Step 5

In the Access Edge Service (FQDN) field, enter the Expressway-E fully qualified domain name.

Step 6

Click Commit .

#### What to do next

Confirm if you are using a public DNS SRV record to route traffic from Skype for Business to the IM and Presence Service.

If you are not using a DNS SRV record, add Expressway manually as a SIP Provider for IM and Presence. See Add Expressway as SIP Federated Provider for IM and Presence .

If you are using a  DNS SRV record, Exchange Certificates .

### Add Expressway as SIP Federated Provider for IM and Presence

Use this procedure on the Skype for Business server if you are not using a DNS SRV record to route traffic from Skype for
                                 Business. In this case, you must add Expressway manually as a SIP Federation Provider for IM and Presence Service.

Step 1

On the Skype for Business server, click Federation and External Access .

Step 2

Click SIP FEDERATED PROVIDERS .

Step 3

Click New and select Hosted provider .

Step 4

In the Provider name field, enter your IM and Presence domain.

Step 5

In the Access Edge service (FQDN) field, enter the fully qualified domain name of the Expressway-E server.

Step 6

Click Commit .

#### What to do next

Exchange Certificates

### Exchange Certificates

Follow this process to exchange certificates among the servers in your Interdomain Federation with Skype for Business deployment.

External Edge certificates from the Skype for Business edge server must have the following OID values under Enhanced Key Usage:

Server Authentication: (1.3.6.1.5.5.7.3.1)

Client Authentication: (1.3.6.1.5.5.7.3.2)

Step 1

Download certificates from each system in the deployment:

- IM and Presence Service (internal certificate can be self-signed)

- Expressway-C (internal certificate can be self-signed)

- Expressway-E (external certificate must be CA-signed). Note that the Expressway-E is required for Business to Business federation
                                             only. Expressway-E is not used for single enterprise network.

- Skype for Business edge server (External Edge certificate must be CA-signed)

Step 2

On the IM and Presence Service, upload the Expressway-C certificate to cup-trust .

Step 3

On the Expressway-C, upload the IM and Presence Service certificate and, (for Single Enterprise Network federation only) the
                                          Skype for Business certificate.

Step 4

Upload the Skype for Business certificate as follows:

- (Single Enterprise Network). On the Expressway-C, upload the Skype for Business certificate

- (Business to Businss only) On the Expressway-E, upload the Skype for Business External Edge certificate.

Step 5

On the Skype for Business edge server, upload the Expressway-E external certificate (for Business to Business) or the Expressway-C
                                          certificate (for federation within a single enterprise).

#### Certificate Notes

For IM and Presence Service, you can download and upload certificates from the Certificate Management window in Cisco Unified IM OS Administration (choose Security > Certificate Management ). For detailed procedures, see the "Security Configuration" chapter of the Configuration and Administration Guide for IM and Presence Service at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-installation-and-configuration-guides-list.html .

For Expressway certificate management, see the Cisco Expressway Administrator Guide at http://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-maintenance-guides-list.html .

For Skype for Business certificates, you can use the Skype for Business Deployment Wizard to install or download certificates.
                                       Run the wizard and select the Request, Install or Assign Certificates option. For details, see your Microsoft Skype for Business documentation.

| Note | You can also configure federation with a Skype for Business server that is hosted by an Office365 deployment. For details,
                                          including configuration information, refer to Interdomain Federation with Office 365 . |
|---|---|

| Note | For federation with an Office 365-hosted Skype for Business deployment, go to Interdomain Federation with Office 365 . |
|---|---|

|  | IM and Presence Service Configuration | Expressway Configuration | Skype for Business Configuration | Description |
|---|---|---|---|---|
| Step 1 | Turn on Federation Services |  |  | Make sure that Federation services are running. |
| Step 2 | Assign DNS SRV for IM and Presence |  |  | Configure a DNS SRV record so that Skype for Business can route traffic to the IM and Presence Service. |
| Step 3 | Add Federated Domain to IM and Presence |  |  | Add domain entries for all Skype for Business domains. |
| Step 4 | Configure Static Route on IM and Presence |  |  | Configure a static route that points to  Expressway-C. |
| Step 5 | Add Expressway as a TLS Peer |  |  | Configure Expressway-C as a TLS peer. |
| Step 6 | Add Expressway to Access Control List |  |  | Add all Expressway-C servers to an access control list. |
| Step 7 | Restart Cisco XCP Router |  |  | After completing your configurations, restart the Cisco XCP Router service. |
| Step 8 |  | Configure Expressway for Federation with Skype for Business |  | Configure Expressway for interdomain federation. |
| Step 9 |  |  | Configure User Trust Settings | Configure trust settings for IM and Presence users. |
| Step 10 |  |  | Configure Global Federation Access Settings | Configure global access edge settings for federation. |
| Step 11 |  |  | Add IM and Presence as Allowed Domain | Optional. Complete this task only if your global access edge settings do not allow the IM and Presence domain. |
| Step 12 |  |  | Add Expressway as SIP Federated Provider for IM and Presence | Optional. Complete this task only if you are not using a DNS SRV to route traffic to the IM and Presence Service. |
| Step 13 | Exchange Certificates | Exchange certificates between the servers in your setup. |

| Step 1 | Log in to the Cisco Unified IM and Presence Serviceability user interface. Choose Tools > Service Activation . |
|---|---|
| Step 2 | Fom the Server drop-down, choose an IM and Presence node and click Go . |
| Step 3 | Under IM and Presence Services , make sure that the adjacent radio button to the Cisco XCP SIP Federation Connection Manager service is checked. |
| Step 4 | Click Save . |
| Step 5 | The Cisco SIP Proxy service must be running for SIP federation to work. Log in to the Cisco Unified IM and Presence Serviceability user interface. Choose Tools > Feature Services and verify that the Cisco SIP Proxy service is running. |

| Note | You can still configure interdomain federation without the DNS SRV record, but in this case, you must add the route manually
                                             on the Skype for Business server. If you choose to do this, you can skip this task. |
|---|---|

| Step 1 | From Cisco Unified CM IM and Presence Administration, choose Presence > Inter-Domain Federation > SIP Federation . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Domain Name field, enter the Skype for Business domain. |
| Step 4 | Enter a Description of the domain. For example, Skype for Business federated domain . |
| Step 5 | From the Integration Type drop-down, select Inter-domain to OCS/Lync/S4B . |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM IM and Presence Administration, choose Presence > Routing > Static Routes . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Destination Pattern field, enter the Skype for Business FQDN in a reversed format. For example, if the domain is s4b.com , enter .com.s4b.* . |
| Step 4 | In the Next Hop field, enter the Expressway-C  IP address or FQDN. |
| Step 5 | In the Next Hop Port field enter 5061 . |
| Step 6 | From the Route Type drop-down list, choose Domain . |
| Step 7 | From the Protocol Type drop-down list box, select TLS . |
| Step 8 | Click Save . |

| Step 1 | Add Expressway-C as a TLS peer subject: From Cisco Unified CM IM and Presence Administration, choose System > Security > TLS Peer Subjects . Click Add New . In the Peer Subject Name field, enter the Expressway-C fully qualified domain name of the Expressway-C. Enter a Description . Click Save . |
|---|---|
| Step 2 | Create a TLS Context that includes the Expressway TLS peer subject that you configured: From Cisco Unified CM Administration, choose System > Security > TLS Context Configuration Click Find . Select Default_Cisco_UP_SIP_Proxy_Peer_Auth_TLS_Context . Under TLS Cipher Mapping , use the arrows to move the desired TLS ciphers to the Selected TLS Ciphers box. However, leaving this at the default settng should be sufficient in most cases. Under TLS Peer Subject Mapping , use the arrows to move the TLS peer subject that you created to the Selected TLS Peer Subjects list box. Click Save . |

| Note | If you have an ACL that provides global access ( Allow from all ), or an ACL which provides access to the domain on which the Expressway-C server resides (for example, Allow from company.com ) then you do not need to add ACL entries for the Expressway-C server. |
|---|---|

| Step 1 | Log in to the IM and Presence Service publisher node. |
|---|---|
| Step 2 | From Cisco Unified CM IM Administration, choose System > Security > Incoming ACL . |
| Step 3 | Create your ACL entries: Click Add New . Enter a Description for the new ACL entry. For example, Skype for Business Federation via Expressway-C . Enter an Address Pattern that provides access to the Expressway-C IP address or FQDN. For example, Allow from 10.10.10.1 or Allow from expwyc.company.com . Click Save . Repeat this set of steps to create another ACL entry. To provide server  access, you need two entries: an ACL with the server
                                                IP address, and an ACL with the server FQDN. |
| Step 4 | Restart Cisco SIP Proxy services: Choose Presence > Routing > Settings . Click Restart All Proxy Services . |

| Step 1 | From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services . |
|---|---|
| Step 2 | From the Server drop-down list box, choose the IM and Presence database publisher node and click Go . |
| Step 3 | Under IM and Presence Services , select the Cisco XCP Router service. |
| Step 4 | Click Restart . |
| Step 5 | Repeat this procedure for all IM and Presence Service cluster nodes. |

| Note | Make sure that your Expressway-C zone configuration points to the port that is associated with TLS Peer Authentication on
                                             the IM and Presence Service. You can confirm the correct port on Cisco Unified CM IM and Presence Administration by going
                                             to System > Application Listeners and confirming the port associated to Default Cisco SIP Proxy TLS Listener - Peer Auth . The default is 5062 . |
|---|---|

| Step 1 | Log in to the Skype for Business server. |
|---|---|
| Step 2 | In the left navigation bar, click Federation and External Access . |
| Step 3 | In the header bar, click EXTERNAL ACCESS POLICY . |
| Step 4 | Click New and select User Policy . |
| Step 5 | In the Name field, enter the IM and Presence domain |
| Step 6 | Check the following options: Enable communications with federated users Enable communications with remote users Enable communications with public users |
| Step 7 | Click Commit . |

| Step 1 | In the left navigation bar, click Federation and External Access . |
|---|---|
| Step 2 | In the header bar, click ACCESS EDGE CONFIGURATION . |
| Step 3 | Select Global . |
| Step 4 | If you want to allow access to all domains globally, select each of the following options. Otherwise, choose which options
                                          you want to allow: Enable federation and public IM connectivity Enable partner domain discovery—Select this option to use a public DNS SRV record to route traffic to the IM and Presence
                                             Service. If you do not want to use a DNS SRV record, or do not have a DNS SRV record, leave this option unchecked. Enable remote user access Enable anonymous user access to conferences Note If you choose not to allow access globally, you will have to add the IM and Presence manually as an allowed domain and a SIP
                                                         Federated Provider. | Note | If you choose not to allow access globally, you will have to add the IM and Presence manually as an allowed domain and a SIP
                                                         Federated Provider. |
| Note | If you choose not to allow access globally, you will have to add the IM and Presence manually as an allowed domain and a SIP
                                                         Federated Provider. |
| Step 5 | Click Commit . |

| Note | If you choose not to allow access globally, you will have to add the IM and Presence manually as an allowed domain and a SIP
                                                         Federated Provider. |
|---|---|

| Step 1 | In the left navigation bar, click Federation and External Access . |
|---|---|
| Step 2 | In the header bar, click SIP FEDERATED DOMAINS . |
| Step 3 | Click New and select Allowed domain . |
| Step 4 | In the Domain name field, enter the IM and Presence domain. |
| Step 5 | In the Access Edge Service (FQDN) field, enter the Expressway-E fully qualified domain name. |
| Step 6 | Click Commit . |

| Note | If you have a DNS SRV record for the IM and Presence Service, you can skip this task. |
|---|---|

| Step 1 | On the Skype for Business server, click Federation and External Access . |
|---|---|
| Step 2 | Click SIP FEDERATED PROVIDERS . |
| Step 3 | Click New and select Hosted provider . |
| Step 4 | In the Provider name field, enter your IM and Presence domain. |
| Step 5 | In the Access Edge service (FQDN) field, enter the fully qualified domain name of the Expressway-E server. |
| Step 6 | Click Commit . |

| Note | External Edge certificates from the Skype for Business edge server must have the following OID values under Enhanced Key Usage: Server Authentication: (1.3.6.1.5.5.7.3.1) Client Authentication: (1.3.6.1.5.5.7.3.2) |
|---|---|

| Step 1 | Download certificates from each system in the deployment: IM and Presence Service (internal certificate can be self-signed) Expressway-C (internal certificate can be self-signed) Expressway-E (external certificate must be CA-signed). Note that the Expressway-E is required for Business to Business federation
                                             only. Expressway-E is not used for single enterprise network. Skype for Business edge server (External Edge certificate must be CA-signed) Note In this context, if any of the certificates, such as Expressway-E and Skype for Business, are signed by a Certificate Authority,
                                                      it is the Root CA certificate that is actually added in the relevant far end trust store. Only in the scenario of self-signed
                                                      certificates should themselves be added to the far end trust stores. | Note | In this context, if any of the certificates, such as Expressway-E and Skype for Business, are signed by a Certificate Authority,
                                                      it is the Root CA certificate that is actually added in the relevant far end trust store. Only in the scenario of self-signed
                                                      certificates should themselves be added to the far end trust stores. |
|---|---|---|---|
| Note | In this context, if any of the certificates, such as Expressway-E and Skype for Business, are signed by a Certificate Authority,
                                                      it is the Root CA certificate that is actually added in the relevant far end trust store. Only in the scenario of self-signed
                                                      certificates should themselves be added to the far end trust stores. |
| Step 2 | On the IM and Presence Service, upload the Expressway-C certificate to cup-trust . |
| Step 3 | On the Expressway-C, upload the IM and Presence Service certificate and, (for Single Enterprise Network federation only) the
                                          Skype for Business certificate. |
| Step 4 | Upload the Skype for Business certificate as follows: (Single Enterprise Network). On the Expressway-C, upload the Skype for Business certificate (Business to Businss only) On the Expressway-E, upload the Skype for Business External Edge certificate. |
| Step 5 | On the Skype for Business edge server, upload the Expressway-E external certificate (for Business to Business) or the Expressway-C
                                          certificate (for federation within a single enterprise). |

| Note | In this context, if any of the certificates, such as Expressway-E and Skype for Business, are signed by a Certificate Authority,
                                                      it is the Root CA certificate that is actually added in the relevant far end trust store. Only in the scenario of self-signed
                                                      certificates should themselves be added to the far end trust stores. |
|---|---|