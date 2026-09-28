---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-191-english-admin-guide-at91-b-ata191-admin-guide-at91-b-ata191-admin-g-bee476d7b2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/191/english/admin-guide/at91_b_ata191-admin-guide/at91_b_ata191-admin-guide_chapter_0100.html
retrieved_at: 2026-08-21T20:39:33.852341+00:00
---

Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

# Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

Updated: August 15, 2025

Chapter: Configure Fax Services

## Chapter: Configure Fax Services

# Configure Fax Services

## Fax Services

The ATA 191 provides two modes of fax services that provide internetworking with Cisco IOS gateways over IP networks. These
                           modes are called fax pass-through mode and T.38 fax relay mode.

With fax pass-through mode, the ATA 191 encodes fax traffic within the G.711 voice codec.  The fax traffic is then passed
                           through the Voice Over IP (VoIP) network as though the fax were a voice call.

With T.38 fax relay mode, the ATA 191 supports the transmission of faxes, in real time, between two standard fax terminals
                           communicating over SIP networks. T.38 fax relay mode provides a more reliable and error-free method of sending faxes over
                           an IP network.

## Fax Mode

You can choose the preferred fax mode on the phone configuration page of the Unified CM administration page. From the fax
                           mode pull-down window, choose one of the following modes:

Fax passthrough

T.38 fax relay

NSE Fax passthrough—G711ulaw

NSE Fax passthrough—G711alaw

You can set the Fax Error correction mode override values. From the fax mode pull-down window, choose one of the following
                           modes:

On

Off

Default

### Fax Modem Standards

The ATA 191 supports the following fax modem standards:

ITU-T V.34

ITU-T V.34 Annex 12

K56flex

V.21

V.22

V.23

V.32

V.32bis

V.44

V.90

V.92

V.34 is not supported for T.38 relay fax.

### Fax Modem Speeds

The ATA 191 supports the following fax modem speeds:

33.6 kb/s

31.2 kb/s

28.8 kb/s

26.4 kb/s

24 kb/s

21.6 kb/s

19.2 kb/s

16.8 kb/s

14.4 kb/s

12 kb/s

9.6 kb/s

7.2 kb/s

4.8 kb/s

2.4 kb/s

The speeds that are only used in V.34 do not apply for fax using T.38 relay.

| Note | V.34 is not supported for T.38 relay fax. |
|---|---|

| Note | The speeds that are only used in V.34 do not apply for fax using T.38 relay. |
|---|---|