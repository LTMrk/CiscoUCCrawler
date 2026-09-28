---
doc_id: help-webex-com-en-us-article-2ktojz-a44274751d
source_url: https://help.webex.com/en-us/article/2ktojz
retrieved_at: 2026-09-07T10:36:49.863406+00:00
---

- Test Tool

- Checklists

This section covers the Hybrid Connectivity Test Tool. You can access this troubleshooting tool
            from Control Hub.

You can also access the known issues from the related articles.

## Hybrid connectivity test tool (Control Hub)

You can access the Hybrid connectivity test tool from Control Hub: from the customer view in https://admin.webex.com , go to Services > Hybrid , click Edit settings in the Hybrid Call card,
                scroll to Default SIP Destination , and then click Test next to the SIP destination that you entered.

This table lists common errors that may appear after you test a SIP destination address for Hybrid Calling. The table also provides some next steps for troubleshooting, including links to relevant details in the Troubleshooting Guide for Hybrid Call Service .

Error

Keyword

More Information and Troubleshooting Steps

No DNS addresses found

DNS SRV

DNS Lookup failed. Check that a DNS or SRV record exists for your SIP Destination and that it resolves to one or more valid IP addresses.

See Unable to resolve the Expressway-E DNS SRV/hostname in the troubleshooting guide for more information.

Connection timed out

Socket failure

Network and/or Mutual TLS connection timed out. Check network connectivity, connection speed, firewall configuration, and Mutual TLS configuration.

See these sections of the troubleshooting guide for more information:

Socket Failure: Port 5062 is Blocked Inbound to Expressway

Socket Failure: Expressway-E is not Listening on Port 5062

TLS failure

Mutual TLS handshake failures

Mutual TLS Error: Check Mutual TLS configuration in both Expressway and https://admin.webex.com , and that Mutual TLS certificates are present and valid in both locations.

See Mutual TLS Handshake Failures in the troubleshooting guide for more information.

Connect failure

Socket failure

TCP Connection failure: Check network connectivity, connection speed, and/or firewall configuration.

See these sections of the troubleshooting guide for more information:

Socket Failure: Port 5062 is Blocked Inbound to Expressway

Socket Failure: Expressway-E is not Listening on Port 5062

TCP read/write failure

Socket failure

TCP read/write failure: Please try again. If the error persists, check network connectivity, firewall configuration, and Mutual TLS configuration.

See these sections of the troubleshooting guide for more information:

Socket Failure: Port 5062 is Blocked Inbound to Expressway

Socket Failure: Expressway-E is not Listening on Port 5062

TCP Failure

Socket failure

TCP failure: TCP read/write failure: Please try again. If the error persists, check network connectivity, firewall configuration, and Mutual TLS configuration.

See these sections of the troubleshooting guide for more information:

Socket Failure: Port 5062 is Blocked Inbound to Expressway

Socket Failure: Expressway-E is not Listening on Port 5062

This section covers troubleshooting checklists and tasks that you can walk through before you contact support.

Webex status page

If calls from Webex to your enterprise are not ringing on the enterprise side, walk through the points in this checklist to double-check your configuration.

Before you walk through these troubleshooting suggestions, see https://status.webex.com for the latest information on any cloud outages. From that status page, you can also subscribe to notifications.

Mutual TLS and SIP destination

Check these troubleshooting points related to the mutual TLS connection and certificates:

Install the Webex cloud root certificate bundle on the Expressway-E.

Configure a dedicated mutual TLS port on the Expressway-E.

Configure a DNS zone for the cloud on the Expressway-E.

Open the mutual TLS port number in your firewall—5062, which may not be open by default.

Determine which root certificate option you are using in the Webex cloud—The option is used to verify your Expressway-E's SIP TLS certificate.

Default store—Is your Expressway-E certificate signed by one of the public authorities? If you are unsure, use the custom store option.

Custom store—Is your Expressway-E certificate or its signer installed in the cloud? Does the certificate contain verified Expressway-E hostnames?

From the customer view in https://admin.webex.com , go to Services > Hybrid > Hybrid Call > Settings . Check these points that are related to your SIP destination that you
                set during the deployment process:

The value points at your Expressway-E dedicated mutual TLS port.

Try to connect to the IP address:port . (Multiple addresses if you configured an SRV.)

If you configured an IP address or hostname, specify the mutual TLS port.

If you used an SRV, ensure it is in the format _sips._tcp.< domain you put in as SIP Destination > .

If you do not want to set up an SRV, you can enter IP address:port or hostname:port as your organization's SIP destination.

Expressway pair configuration

If calls from Expressway-E to the cloud are failing and you're using the manual certificate
                        management method, make sure you follow the steps in Webex Root CA Certificate Update and upload the IdenTrust certificate to your Expressway devices as soon as
                        possible.

For calls that route from Webex toward the enterprise, check the search history and network logs on the Expressway-E. This step helps you isolate the problem to either the cloud or the enterprise.

If you reuse an existing B2B zone and search rules, consider creating dedicated zones and search rules instead. This setup avoids interference with existing zone settings for B2B/MRA, avoids routing loops, and makes troubleshooting easier.

Check the search history and network logs on the Expressway-E. Verify that the SIP INVITE from the cloud arrives at the Expressway-E and matches the DNS zone that you configured for the cloud.

If the SIP INVITE does not arrive or match the configured DNS zone, then follow the route of the call toward the Unified Communications Manager. This step helps you find where the call is failing or lost.

See the mutual TLS troubleshooting checklist.

Check the route header. Verify that it contains the cluster fully qualified domain name (FQDN) value that is configured under Unified Communications Manager enterprise settings and in the Expressway search rules. See this example route header and highlighted cluster FQDN:

Route: <sip:[Obfuscated];transport=tls;lr>,<sip:myucmcluster.example.com;lr>

In this example, the home cluster FQDN is myucmcluster.example.com .

Unified CM configuration

Emails in Unified Communications Manager must exactly match the email (synchronized from Active Directory or from any other source) in the Webex cloud.

Directory URIs must match any domains that you verified in your organization.

Check your codec configuration .

Webex services support the following codecs:

Audio—G.711, G.722, AAC-LD

Video—H.264

We support G.729 for joining a Webex meeting, Personal Room meeting, or Webex App meeting from a SIP device. We do not support G.729 for dialing 1:1 from Webex App to a SIP device or bridge.

On the home Unified Communications Manager cluster of the affected users, choose System > Enterprise Parameters ; under Clusterwide Domain Configuration , check the cluster fully qualified domain name (FQDN) setting. The FQDN value that you used must follow these guidelines:

FQDN Guideline

Description and Example

Multiple clusters

The entry must be unique for each cluster with Hybrid Calling—For example, cluster1.example.com , cluster2.example.com , and so on.

No wildcards

Do not use entries with wildcards, such as *.example.com or example*.com.

First FQDN entry for Hybrid Calling

In a list of multiple entries, the Webex cloud uses the first entry on the left for Hybrid Calling, and that first entry must not contain a wildcard.

See this example of three FQDN entries from left to right (the first one being for Hybrid Calling): cluster1.example.com *.example.com example*.com

Different from Expressway-E

Must be different from the Expressway-E system, DNS, and domain name. Otherwise, Expressway-E strips the route header.

New entry for Hybrid Calling

If your current FQDN entry in Unified CM doesn't meet the requirements listed above, you can add a new element to the beginning of the cluster FQDN setting for Hybrid Calling.

For example, if your existing FQDN setting in Cisco Unified Communications Manager is *.example.com *.example.org , add a unique, non-wildcard entry at the beginning of the field: " cluster1.example.com *.example.com *.example.org"

| Error | Keyword | More Information and Troubleshooting Steps |
|---|---|---|
| No DNS addresses found | DNS SRV | DNS Lookup failed. Check that a DNS or SRV record exists for your SIP Destination and that it resolves to one or more valid IP addresses. See Unable to resolve the Expressway-E DNS SRV/hostname in the troubleshooting guide for more information. |
| Connection timed out | Socket failure | Network and/or Mutual TLS connection timed out. Check network connectivity, connection speed, firewall configuration, and Mutual TLS configuration. See these sections of the troubleshooting guide for more information: Socket Failure: Port 5062 is Blocked Inbound to Expressway Socket Failure: Expressway-E is not Listening on Port 5062 |
| TLS failure | Mutual TLS handshake failures | Mutual TLS Error: Check Mutual TLS configuration in both Expressway and https://admin.webex.com , and that Mutual TLS certificates are present and valid in both locations. See Mutual TLS Handshake Failures in the troubleshooting guide for more information. |
| Connect failure | Socket failure | TCP Connection failure: Check network connectivity, connection speed, and/or firewall configuration. See these sections of the troubleshooting guide for more information: Socket Failure: Port 5062 is Blocked Inbound to Expressway Socket Failure: Expressway-E is not Listening on Port 5062 |
| TCP read/write failure | Socket failure | TCP read/write failure: Please try again. If the error persists, check network connectivity, firewall configuration, and Mutual TLS configuration. See these sections of the troubleshooting guide for more information: Socket Failure: Port 5062 is Blocked Inbound to Expressway Socket Failure: Expressway-E is not Listening on Port 5062 |
| TCP Failure | Socket failure | TCP failure: TCP read/write failure: Please try again. If the error persists, check network connectivity, firewall configuration, and Mutual TLS configuration. See these sections of the troubleshooting guide for more information: Socket Failure: Port 5062 is Blocked Inbound to Expressway Socket Failure: Expressway-E is not Listening on Port 5062 |

| FQDN Guideline | Description and Example |
|---|---|
| Multiple clusters | The entry must be unique for each cluster with Hybrid Calling—For example, cluster1.example.com , cluster2.example.com , and so on. |
| No wildcards | Do not use entries with wildcards, such as *.example.com or example*.com. |
| First FQDN entry for Hybrid Calling | In a list of multiple entries, the Webex cloud uses the first entry on the left for Hybrid Calling, and that first entry must not contain a wildcard. See this example of three FQDN entries from left to right (the first one being for Hybrid Calling): cluster1.example.com *.example.com example*.com |
| Different from Expressway-E | Must be different from the Expressway-E system, DNS, and domain name. Otherwise, Expressway-E strips the route header. |
| New entry for Hybrid Calling | If your current FQDN entry in Unified CM doesn't meet the requirements listed above, you can add a new element to the beginning of the cluster FQDN setting for Hybrid Calling. For example, if your existing FQDN setting in Cisco Unified Communications Manager is *.example.com *.example.org , add a unique, non-wildcard entry at the beginning of the field: " cluster1.example.com *.example.com *.example.org" |