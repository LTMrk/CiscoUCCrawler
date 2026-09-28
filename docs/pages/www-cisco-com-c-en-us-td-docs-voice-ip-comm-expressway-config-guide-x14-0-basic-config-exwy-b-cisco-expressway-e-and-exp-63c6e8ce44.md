---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-basic-config-exwy-b-cisco-expressway-e-and-exp-63c6e8ce44
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/basic_config/exwy_b_cisco-expressway-e-and-expressway-c-basic-configuration-deployment-guide-x14-0/exwy_m_endpoint-registration.html
retrieved_at: 2026-08-16T15:27:44.770762+00:00
---

Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

# Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

Updated: April 14, 2021

Chapter: Endpoint Registration

## Chapter: Endpoint Registration

- Endpoint Registration

- Endpoint Registration

# Endpoint Registration

## Endpoint Registration

The example network configuration diagram shows three endpoints.

Endpoint

IP address

Network

EX90

10.0.0.15

Internal network

EX60

10.0.0.16

Internal network

EX60

192.168.0.2

Home user network

After system configuration, endpoint registration should be possible using these endpoint configuration details:

EX90 (uses SIP protocol)

SIP URI

user.one.ex90@example.com

SIP Proxy1

expc.internal-domain.net

EX60 (uses H.323 and SIP protocol)

H.323 ID

user.two.mxp@example.com

H.323 E.164

7654321

Gatekeeper IP Address

expc.internal-domain.net

SIP URI

user.two.mxp@example.com

SIP Proxy1

expc.internal-domain.net

EX60 at home (uses H.323 and SIP protocol)

H.323 ID

user.three.mxp@example.com

H.323 E.164

1234567

Gatekeeper IP Address

expe.example.com

SIP URI

user.three.mxp@example.com

SIP Proxy1

expe.example.com

What To Do Next

The Expressway routing configuration is now complete. Go to the next section, " System Checks " .

| Endpoint | IP address | Network |
|---|---|---|
| EX90 | 10.0.0.15 | Internal network |
| EX60 | 10.0.0.16 | Internal network |
| EX60 | 192.168.0.2 | Home user network |

| EX90 (uses SIP protocol) |
|---|
| SIP URI | user.one.ex90@example.com |
| SIP Proxy1 | expc.internal-domain.net |
| EX60 (uses H.323 and SIP protocol) |
| H.323 ID | user.two.mxp@example.com |
| H.323 E.164 | 7654321 |
| Gatekeeper IP Address | expc.internal-domain.net |
| SIP URI | user.two.mxp@example.com |
| SIP Proxy1 | expc.internal-domain.net |
| EX60 at home (uses H.323 and SIP protocol) |
| H.323 ID | user.three.mxp@example.com |
| H.323 E.164 | 1234567 |
| Gatekeeper IP Address | expe.example.com |
| SIP URI | user.three.mxp@example.com |
| SIP Proxy1 | expe.example.com |