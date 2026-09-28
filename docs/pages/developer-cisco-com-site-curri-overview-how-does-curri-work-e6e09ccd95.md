---
doc_id: developer-cisco-com-site-curri-overview-how-does-curri-work-e6e09ccd95
source_url: https://developer.cisco.com/site/curri/overview/how-does-curri-work/
retrieved_at: 2026-09-01T17:35:16.392063+00:00
---

# How does CURRI work?

Cisco Unified Routing Rules Interface (CURRI) Architecture

How does CURRI work ?

The administrator assigns an External Call Control Profile (ECCP) to one or more Unified CM trigger points.

When dialed digits match an ECCP enabled pattern or number, Unified CM issues a Route Request over the Cisco Unified Routing Rules Interface (CURRI).

The adjunct Route Server evaluates the information and returns call handling instructions as a Decision with Obligation:

Decision - specifies if the call is Allowed or Denied

Obligation - contains specific call routing instructions and treatment

- Route the call normally and optionally modify calling/called party number(s)

- Divert the call to a different destination or to voice mail and optionally modify calling/called party number(s)

- Reject the call and optionally play an announcement

Unified CM then routes the call based on the policy decision and obligation.

To learn more about routing a call with CURRI API, check out the the CURRI "Hello World" page.

Get Started

Subscribe to receive the latest news and updates

Subscribe