---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-interdomain-federation-12-5-1-cup0-b-interdomain-federation-91c43c385f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/interdomain_federation/12_5_1/cup0_b_interdomain-federation-1251/cup0_b_interdomain-federation-1251_chapter_010011.html
retrieved_at: 2026-08-16T17:22:53.424453+00:00
---

Interdomain Federation Guide for the IM and Presence Service, Release 12.5(1)

# Interdomain Federation Guide for the IM and Presence Service, Release 12.5(1)

Updated: January 22, 2024

Chapter: Troubleshooting an XMPP Federation Integration

## Chapter: Troubleshooting an XMPP Federation Integration

- Troubleshooting an XMPP Federation Integration

- Check System Troubleshooter

# Troubleshooting an XMPP Federation Integration

This section provides information on the ways to Troubleshoot an XMPP Federation Integration.

## Check System Troubleshooter

If you deploy multiple IM and Presence Service clusters and you configure XMPP federation, you must turn on XMPP federation on at least one node per cluster. You must configure
                              the same XMPP federation settings and policy on each cluster; the IM and Presence Service does not replicate the XMPP federation configuration across cluster. The System Troubleshooter reports if XMPP federation
                              settings across clusters are not synchronized. The System Troubleshooter performs the following checks:

Step 1

XMPP federation is enabled consistently across intercluster
                                             				  peers.

The SSL Mode is configured consistently across intercluster
                                             				  peers.

The "Required Valid client-side certificates" is configured
                                             				  consistently across intercluster peers.

The SASL settings are configured consistently across
                                             				  intercluster peers.

The dialback secret is configured consistently across
                                             				  intercluster peers.

The default Admin Policy for XMPP Federation is configured
                                             				  consistently across inter-cluster peers.

The Policy hosts are configured consistently across
                                             				  inter-cluster peers.

Step 2

Log in to the Cisco Unified CM IM and Presence
                                          				  Administration user interface. Choose Diagnostics > System
                                             				  Troubleshooter .

Step 3

Ensure there are green check marks beside the following:

Verify the XMPP Federation settings match on all
                                                					 interclustered peers.

Verify that SASL settings have been correctly configured for
                                                					 all intercluster peers.

Verify that XMPP has been uniformly disabled or enabled on at
                                                					 least one node in each all clusters.

Verify that the default Admin Policy is consistent across all
                                                					 intercluster peers.

Verify that the Host Policy is consistent across all
                                                					 intercluster peers.

The System Troubleshooter provides recommended actions if it
                                          				reports a problem with any of these checks.

If all tests in System Troubleshooter are passed and problems with exchanging IM and availability still persist, check if
                                                the Enable use of Email Address when Federating setting, on the Presence Settings page is configured consistently across intercluster peers.

If all tests in System Troubleshooter are passed and problems with exchanging IM and availability still persist, check if
                                                the Enable use of Email Address for Inter-domain Federation setting, on the Presence Settings page is configured consistently across intercluster peers.

### What to do next

Location of Log File for XMPP Federation

| Step 1 | XMPP federation is enabled consistently across intercluster
                                             				  peers. The SSL Mode is configured consistently across intercluster
                                             				  peers. The "Required Valid client-side certificates" is configured
                                             				  consistently across intercluster peers. The SASL settings are configured consistently across
                                             				  intercluster peers. The dialback secret is configured consistently across
                                             				  intercluster peers. The default Admin Policy for XMPP Federation is configured
                                             				  consistently across inter-cluster peers. The Policy hosts are configured consistently across
                                             				  inter-cluster peers. |
|---|---|
| Step 2 | Log in to the Cisco Unified CM IM and Presence
                                          				  Administration user interface. Choose Diagnostics > System
                                             				  Troubleshooter . |
| Step 3 | Ensure there are green check marks beside the following: Verify the XMPP Federation settings match on all
                                                					 interclustered peers. Verify that SASL settings have been correctly configured for
                                                					 all intercluster peers. Verify that XMPP has been uniformly disabled or enabled on at
                                                					 least one node in each all clusters. Verify that the default Admin Policy is consistent across all
                                                					 intercluster peers. Verify that the Host Policy is consistent across all
                                                					 intercluster peers. The System Troubleshooter provides recommended actions if it
                                          				reports a problem with any of these checks. |

| Note | If all tests in System Troubleshooter are passed and problems with exchanging IM and availability still persist, check if
                                                the Enable use of Email Address when Federating setting, on the Presence Settings page is configured consistently across intercluster peers. If all tests in System Troubleshooter are passed and problems with exchanging IM and availability still persist, check if
                                                the Enable use of Email Address for Inter-domain Federation setting, on the Presence Settings page is configured consistently across intercluster peers. |
|---|---|