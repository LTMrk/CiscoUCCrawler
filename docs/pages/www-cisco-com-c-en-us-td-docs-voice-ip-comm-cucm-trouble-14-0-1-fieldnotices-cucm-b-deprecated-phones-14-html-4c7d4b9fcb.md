---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-trouble-14-0-1-fieldnotices-cucm-b-deprecated-phones-14-html-4c7d4b9fcb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/trouble/14_0_1/fieldNotices/cucm_b_deprecated-phones-14.html
retrieved_at: 2026-08-16T17:51:14.270414+00:00
---

Deprecated Phone Models in Cisco Unified Communications Manager, Release 14

# Deprecated Phone Models in Cisco Unified Communications Manager, Release 14

### Download Options

Updated: October 5, 2020

# Deprecated Phone Models in Cisco Unified Communications Manager, Release 14

## Overview

After a careful review of feedback from our customers and partners, Cisco is reversing its decision to deprecate multiple
                  models of phones in Release 14. This will allow our customers to get additional usage from working models of Cisco IP Phones
                  and not force immediate migration to alternate clients or phones during challenging business timeframes. The intent is to
                  give our customers the opportunity to move to newer phone models and clients at a pace that is reasonable.

While we are not deprecating any additional endpoints in Release 14, Cisco’s policy to end of life phones has not changed.
                  Cisco will not issue bug fixes or security enhancements for endpoints that have reached End of Software Maintenance or End
                  of Support status, regardless of whether those endpoints are deprecated or not deprecated. Cisco will not test Unified Communications
                  Manager with End of Life phones. Nor will we fix Unified Communications Manager bugs that are related to End of Life phones
                  unless the issue can be replicated on a phone that is not End of Life.

Phones that were deprecated in Releases 11.x and 12.x will remain deprecated in all future releases.

## Products Affected

Producs Affected

Version

Cisco Unified Communications Manager

14

Cisco Business Edition 6000

14

Cisco Business Edition 7000

14

## Existing Phone Deprecations

The following phone models were first deprecated in Release 12.0(x). That deprecation status carries over to Release 14:

Cisco Unified Wireless IP Phone 7921

Cisco Unified IP Phone 7970

Cisco Unified IP Phone 7971

The following phone models were first deprecated in Release 11.5(x). That deprecation status carries over to Release 14:

Cisco IP Phone 12 S

Cisco IP Phone 12 SP

Cisco IP Phone 12 SP+

Cisco IP Phone 30 SP+

Cisco IP Phone 30 VIP

Cisco Unified IP Phone 7902G

Cisco Unified IP Phone 7905G

Cisco Unified IP Phone 7910

Cisco Unified IP Phone 7910G

Cisco Unified IP Phone 7910+SW

Cisco Unified IP Phone 7910G+SW

Cisco Unified IP Phone 7912G

Cisco Unified Wireless IP Phone 7920

Cisco Unified IP Conference Station 7935

## Background

These phone models were deprecated for the following reasons:

Security—Since legacy phone models are not updated with critical software fixes, we have limited ability to protect customers
                        when security issues arise.

New feature implementation—Some phone models were introduced many years ago (for example, the 7900 series was introduced ten
                        years ago). The old hardware on these phone models impacts the implementation of new features and new security features.

Sustaining—No development support or regression testing is currently being done for these older phones.

End of Life – The phone models listed above have their End Of Sale and End of Life announced. These phone models will reach
                        Last Date of Support before the FCS date for Cisco Unified Communications Manager, Release 14.

For End of Life and End of Sale Announcement notices, please refer to:

## Problem / Symptom

If you are running any of these phone models that have been deprecated, after you upgrade and switch over to the new release,
                  registration will be blocked on the phone. If the phone remains powered on, the phone will make repeated registration attempts,
                  which will create unnecessary network traffic as well as a load on the Cisco CallManager service.

If you register an End of Life phone to Cisco Unified Communications Manager, you will get limited support:

No bug and security fixes will be provided for that phone.

We will not provide fixes for Cisco Unified Communications Manager in regard to these phones unless the same problem can be
                        replicated with supported phone models.

The older phone models may be a security risk in your network. Cisco will not evaluate whether an end of life phone model
                        will be affected by a security vulnerability.

## Take Action Now

To guarantee that you have full support, before you upgrade, do the following:

Identify any deprecated phones and remove or replace them before you move forward with your upgrade to Release 14.

Identify phones that are end of life and establish your strategy for these phones. Leverage competitive trade-in programs
                        to upgrade your phones. Or, work with your Cisco account team to refresh phones in a cost effective manner.

Consider a soft client strategy with Jabber and Cisco Headsets.

Talk to your partner about migrating to supported Cisco 7800 and 8800 series IP Phones:

Cisco IP Phone 7800 Series:

https://www.cisco.com/c/en/us/products/collaboration-endpoints/unified-ip-phone-7800-series/index.html .

Cisco IP Phone 8800 Series:

https://www.cisco.com/c/en/us/products/collaboration-endpoints/unified-ip-phone-8800-series/index.html .

## Licensing

You do not need to purchase a new device license to replace a deprecated phone with a supported phone. The device license
                  becomes available for a new phone when you remove the deprecated phone from the system. When the new phone is added to the
                  system, the newly added phone uses an available license.

| Producs Affected | Version |
|---|---|
| Cisco Unified Communications Manager | 14 |
| Cisco Business Edition 6000 | 14 |
| Cisco Business Edition 7000 | 14 |