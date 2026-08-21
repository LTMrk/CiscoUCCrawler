---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-managed-services-12-5-1-cucm-b-managed-services-guide-1251-cucm-b-manag-a583ea798b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/managed_services/12_5_1/cucm_b_managed-services-guide-1251/cucm_b_managed-services-guide-1251_chapter_01000.html
retrieved_at: 2026-08-21T09:00:27.303820+00:00
---

Managed Services Guide for Cisco Unified Communications Manager and IM and Presence Service

# Managed Services Guide for Cisco Unified Communications Manager and IM and Presence Service

Updated: January 22, 2019

Chapter: Vendor-Specific Management Information Base

## Chapter: Vendor-Specific Management Information Base

# Vendor-Specific Management Information Base

This chapter describes the vendor-specific Management Information Base (MIB) text documents that Unified Communications Manager supports and that are used with Simple Network Management Protocol (SNMP).

## Vendor-Specific Management Information Base

The MIBs described in this chapter exist on various Cisco Media Convergence Servers (MCS), depending on vendor and model number.
                              To query these MIBS, you can use the standard MIB browsers provided by the vendor. Go to the following URLs:

For HP, go to http://h18013.www1.hp.com/products/servers/management/hpsim/index.html to download HP SIM .

For IBM, go to http://www-03.ibm.com/systems/management/director/index.html to download IBM Systems Director .

## Supported Servers - Cisco Unified CM Releases

This section lists the supported server models and unsupported server models by MIB and by Cisco Unified CM Release.

### Cisco Unified Communications Manager Release 10.0(1) Supported Servers

In Release 10.0(1) and later, Cisco only supports virtualized deployments of Unified Communications Manager on Cisco Unified Computing System servers, or on a Cisco-approved third-party server configuration. In Release 10.0(1) and
                                 later, Cisco does not support deployments of Unified Communications Manager on Cisco Media Convergence Server servers.

For more information about the deployment of Unified Communications Manager in a virtualized environment, see:

http://docwiki.cisco.com/wiki/Unified_Communications_in_a_Virtualized_Environment .

### Cisco Unified CM Release 9.5(1) Supported Servers

Cisco Unified CM Release 9.5(1)

IBM Server Models

HP Server Models

- MCS-7816-I4-IPC1/CCX1

- MCS-7835-H2-IPC1

- MCS-7816-I5-IPC1/CCX1

- MCS-7835-H2-IPC2

- MCS-7825-I4-IPC1

- MCS-7845-H2-IPC1

- MCS-7825-I5-IPC1

- MCS-7845-H2-IPC2

- MCS-7825-I6-IPC1

- MCS-7828-I4-SS1

- MCS-7828-I5-SS1

- MCS-7835-I3-IPC1

- MCS-7845-I3-IPC1

- MCS-7845-I4-IPC1

#### Cisco Unified CM Release 9.5(1) Inapplicable MIBs

IBM-SYSTEM-POWER MIB does not apply to the following IBM server models:

MCS-7816-I4-IPC1/CCX1

MCS-7816-I5-IPC1/CCX1

MCS-7825-I4-IPC1

MCS-7825-I5-IPC1

MCS-7825-I6-IPC1

MCS-7828-I4-SS1

MCS-7828-I5-SS1

IBM-SYSTEM-RAID MIB does not apply to the following IBM server models:

MCS-7816-I4-IPC1/CCX1

MCS-7816-I5-IPC1/CCX1

MCS-7825-I4-IPC1

MCS-7825-I5-IPC1

MCS-7825-I6-IPC1

MCS-7828-I4-SS1

MCS-7828-I5-SS1

MCS-7835-I3-IPC1

MCS-7845-I3-IPC1

MCS-7845-I4-IPC1

IBM-SYSTEM-STORAGE MIB does not apply to the following IBM server models:

MCS-7816-I4-IPC1/CCX1

MCS-7816-I5-IPC1/CCX1

HP-CPQSCSI MIB does not apply to the following HP server model:

MCS-7835-H2-IPC1

MCS-7835-H2-IPC2

MCS-7845-H2-IPC1

MCS-7845-H2-IPC2

### Cisco Unified CM Release 8.5(1) Supported Servers

Cisco Unified CM Release 8.5(1)

IBM Server Models

HP Server Models

Cisco Unified Computing System

- MCS-7816-I3-IPC1

- MCS-7816-H3-IPC1

- UCS B200 M1

- MCS-7816-I4-IPC1/CCX1

- MCS-7825-H2-IPC1

- UCS C210 M1

- MCS-7816-I5-IPC1/CCX1

- MCS-7825-H3-IPC1

—

- MCS-7825-I3-IPC1

- MCS-7825-H4-IPC1

—

- MCS-7825-I4-IPC1

- MCS-7828-H3-IPC1

—

- MCS-7825-I5-IPC1

- MCS-7835-H2-IPC1

—

- MCS-7828-I3-SS1

- MCS-7835-H2-IPC2

—

- MCS-7828-I4-SS1

- DL380G6 (Single E5504 CPU)

—

- MCS-7828-I5-SS1

- MCS-7845-H2-IPC1

—

- MCS-7835-I2-IPC1

- MCS-7845-H2-IPC2

—

- MCS-7835-I2-IPC2

- DL380G6 (Single E5540 CPU)

—

- MCS-7835-I3-IPC1

—

—

- MCS-7845-I2-IPC1

—

—

- MCS-7845-I2-IPC2

—

—

- MCS-7845-I3-IPC1

—

—

#### Cisco Unified CM Release 8.5(1) Inapplicable MIBs

IBM-SYSTEM-POWER MIB does not apply to the following IBM server models:

MCS-7815-I2-IPC1

MCS-7816-I3-IPC1

MCS-7816-I4-IPC1/CCX1

MCS-7816-I5-IPC1/CCX1

MCS-7825-I2-IPC1

MCS-7825-I3-IPC1

MCS-7825-I4-IPC1

MCS-7825-I5-IPC1

MCS-7828-I3-SS1

MCS-7828-I4-SS1

MCS-7828-I5-SS1

IBM-SYSTEM-RAID MIB does not apply to the following IBM server models:

MCS-7815-I2-IPC1

MCS-7816-I3-IPC1

MCS-7816-I4-IPC1/CCX1

MCS-7816-I5-IPC1/CCX1

MCS-7825-I4-IPC1

MCS-7825-I5-IPC1

MCS-7828-I4-SS1

MCS-7828-I5-SS1

MCS-7835-I3-IPC1

MCS-7845-I3-IPC1

IBM-SYSTEM-STORAGE-MIB does not apply to the following IBM server models:

MCS-7815-I2-IPC1

MCS-7816-I3-IPC1

MCS-7816-I4-IPC1/CCX1

MCS-7816-I5-IPC1/CCX1

MCS-7825-I2-IPC1

MCS-7825-I3-IPC1

MCS-7828-I3-SS1

MCS-7835-I2-IPC1

MCS-7835-I2-IPC2

MCS-7845-I2-IPC1

MCS-7845-I2-IPC2

HP CPQSCSI MIB does not apply to the following HP server model:

MCS-7816-H3-IPC1

MCS-7825-H2-IPC1

MCS-7825-H3-IPC1

MCS-7825-H4-IPC1

MCS-7828-H3-IPC1

MCS-7835-H2-IPC1

MCS-7835-H2-IPC2

DL380G6 (Single E5504 CPU)

MCS-7845-H2-IPC1

MCS-7845-H2-IPC2

DL380G6 (Single E5540 CPU)

### Cisco Unified CM Release 8.0(2) Supported Servers

Cisco Unified CM Release 8.0(2)

IBM Server Models

HP Server Models

Cisco Unified Computing System

- MCS-7815-I2-IPC1

- MCS-7816-H3-IPC1

- UCS B200 M1

- MCS-7816-I3-IPC1

- MCS-7825-H2-IPC1

—

- MCS-7816-I4-IPC1/CCX1

- MCS-7825-H3-IPC1

—

- MCS-7825-I2-IPC1

- MCS-7825-H4-IPC1

—

- MCS-7825-I3-IPC1

- MCS-7828-H3-IPC1

—

- MCS-7825-I4-IPC1

- MCS-7835-H2-IPC1

—

- MCS-7828-I3-SS1

- MCS-7835-H2-IPC2

—

- MCS-7828-I4-SS1

- DL380G6 (Single E5504 CPU)

—

- MCS-7835-I2-IPC1

- MCS-7845-H2-IPC1

—

- MCS-7835-I2-IPC2

- MCS-7845-H2-IPC2

—

- MCS-7835-I3-IPC1

- DL380G6 (Single E5540 CPU)

—

- MCS-7845-I2-IPC1

—

—

- MCS-7845-I2-IPC2

—

—

- MCS-7845-I3-IPC1

—

—

#### Cisco Unified CM Release 8.0(2) Inapplicable MIBs

IBM-SYSTEM-POWER MIB does not apply to the following IBM server models:

MCS-7815-I2-IPC1

MCS-7816-I3-IPC1

MCS-7816-I4-IPC1/CCX1

MCS-7825-I2-IPC1

MCS-7825-I3-IPC1

MCS-7825-I4-IPC1

MCS-7828-I3-SS1

MCS-7828-I4-SS1

IBM-SYSTEM-RAID MIB does not apply to the following IBM server models:

MCS-7815-I2-IPC1

MCS-7816-I3-IPC1

MCS-7816-I4-IPC1/CCX1

MCS-7825-I4-IPC1

MCS-7828-I4-SS1

MCS-7835-I3-IPC1

MCS-7845-I3-IPC1

IBM-SYSTEM-STORAGE-MIB does not apply to the following IBM server models:

MCS-7815-I2-IPC1

MCS-7816-I3-IPC1

MCS-7816-I4-IPC1/CCX1

MCS-7825-I2-IPC1

MCS-7825-I3-IPC1

MCS-7828-I3-SS1

MCS-7835-I2-IPC1

MCS-7835-I2-IPC2

MCS-7845-I2-IPC1

MCS-7845-I2-IPC2

HP CPQSCSI MIB does not apply to the following HP server model:

MCS-7816-H3-IPC1

MCS-7825-H2-IPC1

MCS-7825-H3-IPC1

MCS-7825-H4-IPC1

MCS-7828-H3-IPC1

MCS-7835-H2-IPC1

MCS-7835-H2-IPC2

DL380G6 (Single E5504 CPU)

MCS-7845-H2-IPC1

MCS-7845-H2-IPC2

DL380G6 (Single E5540 CPU)

### Cisco Unified CM Release 8.0(1) Supported Servers

Unified Communications Manager Release 8.0(1)

IBM Server Models

HP Server Models

- MCS-7815-I2-IPC1 1

- MCS-7816-H3-IPC1 2

- MCS-7816-I3-IPC1 3

- MCS-7825-H2-IPC1 4

- MCS-7816-I4-IPC1 5

- MCS-7825-H2-IPC2 6

- MCS-7825-I2-IPC1 7

- MCS-7825-H3-IPC1 8

- MCS-7825-I2-IPC2 9

- MCS-7825-H4-IPC1 10

- MCS-7825-I3-IPC1 11

- MCS-7828-H3

- MCS-7825-I4-IPC1 12

- MCS-7835-H2-IPC1 13

- MCS-7828-I3

- MCS-7835-H2-IPC2 14

- MCS-7828-I4

- MCS-7845-H2-IPC1 15

- MCS-7835-I2-IPC1 16

- MCS-7845-H2-IPC2 17

- MCS-7835-I2-IPC2 18

—

- MCS-7835-I3-IPC1 19

—

- MCS-7845-I2-IPC1 20

—

- MCS-7845-I2-IPC2 21

—

- MCS-7845-I3-IPC1 22

—

For information about the product end-of-life notices, go to http://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_eol_notices_list.html

#### Cisco Unified CM Release 8.0(1) Inapplicable MIBs

IBM-SYSTEM-POWER MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7815-I3-IPC1

MCS-7816-I3-IPC1

MCS-7816-I4-IPC1

MCS-7825I-3.0-IPC1

MCS-7825-I1-IPC1

MCS-7825-I2-IPC1

MCS-7825-I3-IPC1

MCS-7825-I4-IPC1

MCS-7828-I3-IPC1

IBM-SYSTEM-RAID MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7815-I3-IPC1

MCS-7816-I3-IPC1

MCS-7816-I4-IPC1

MCS-7825-I4-IPC1

MCS-7828-I4-IPC1

IBM-SYSTEM-STORAGE-MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7815-I3-IPC1

MCS-7816-I3-IPC1

MCS-7816-I4-IPC1

MCS-7825I-3.0-IPC1

MCS-7825-I1-IPC1

MCS-7825-I2-IPC1

MCS-7825-I3-IPC1

MCS-7828-I3-IPC1

MCS-7835I-3.0-IPC1

MCS-7835-I1-IPC1

MCS-7835-I2-IPC1

MCS-7835-I2-IPC2

MCS-7845I-3.0-IPC1

MCS-7845-I1-IPC1

MCS-7845-I2-IPC1

MCS-7845-I2-IPC2

HP CPQSCSI MIB does not apply to the following HP server model:

MCS-7816-H4-IPC1

MCS-7825H-3.0-IPC1

MCS-7825-H1-IPC1

MCS-7825-H2-IPC1

MCS-7825-H3-IPC1

MCS-7825-H4-IPC1

MCS-7828-H3-IPC1

MCS-7835H-3.0-IPC1

MCS-7835-H1-IPC1

MCS-7835-H2-IPC1

MCS-7835-H2-IPC2

MCS-7845H-3.0-IPC1

MCS-7845-H1-IPC1

MCS-7845-H2-IPC1

MCS-7845-H2-IPC2

HP CPQSM2 MIB does not apply to the following HP server model:

MCS-7825H-3.0-IPC1

### Cisco Unified CM Release 7.1(2) Supported Servers

Cisco Unified CM Release 7.1(2)

IBM Server Models

HP Server Models

- MCS-7815-I1-IPC1

- MCS-7816-H3-IPC1

- MCS-7815-I2-IPC1

- MCS-7816-H4-IPC1/CCX1

- MCS-7815-I3-IPC1

- MCS-7825H-3.0-IPC1

- MCS-7816-I3-IPC1

- MCS-7825-H1-IPC1

- MCS-7816-I4-IPC1/CCX1

- MCS-7825-H2-IPC1

- MCS-7825I-3.0-IPC1

- MCS-7825-H3-IPC1

- MCS-7825-I1-IPC1

- MCS-7825-H4-IPC1/CCE1/CCX1/ECS1/RC1

- MCS-7825-I2-IPC1

- MCS-7828-H3-IPC1

- MCS-7825-I3-IPC1

- MCS-7835H-3.0-IPC1

- MCS-7825-I4-IPC1/CCE1/CCX1/ECS1/RC1

- MCS-7835-H1-IPC1

- MCS-7828-I3-IPC1

- MCS-7835-H2-IPC1

- MCS-7835I-3.0-IPC1

- MCS-7835-H2-IPC2/CCE2/CCX2/RC2/ECS2

- MCS-7835-I1-IPC1

- MCS-7845H-3.0-IPC1

- MCS-7835-I2-IPC1

- MCS-7845-H1-IPC1

- MCS-7835-I2-IPC2/CCE2/CCX2/RC2/ECS2

- MCS-7845-H2-IPC1

- MCS-7845I-3.0-IPC1

- MCS-7845-H2-IPC2/CCE2/CCX2/RC2/ECS

- MCS-7845-I1-IPC1

—

- MCS-7845-I2-IPC1

—

- MCS-7845-I2-IPC2/CCE2/CCX2/RC2/ECS2

—

#### Cisco Unified CM Release 7.1(2) Inapplicable MIBs

IBM-SYSTEM-POWER MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7815-I3-IPC1

MCS-7816-I3-IPC1

MCS-7816-I4-IPC1/CCX1

MCS-7825I-3.0-IPC1

MCS-7825-I1-IPC1

MCS-7825-I2-IPC1

MCS-7825-I3-IPC1

MCS-7825-I4-IPC1/CCE1/CCX1/ECS1/RC1

MCS-7828-I3-IPC1

IBM-SYSTEM-RAID MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7815-I3-IPC1

MCS-7816-I3-IPC1

MCS-7816-I4-IPC1/CCX1

HP CPQSM2 MIB does not apply to the following HP server model:

MCS-7825H-3.0-IPC1

### Cisco Unified CM Release 7.1(1) Supported Servers

Cisco Unified CM Release 7.1(1)

IBM Server Models

HP Server Models

- MCS-7815-I1-IPC1

- MCS-7816-H3-IPC1

- MCS-7815-I2-IPC1

- MCS-7816-H4-IPC1/CCX1

- MCS-7815-I3-IPC1

- MCS-7825H-3.0-IPC1

- MCS-7816-I3-IPC1

- MCS-7825-H1-IPC1

- MCS-7816-I4-IPC1/CCX1

- MCS-7825-H2-IPC1

- MCS-7825I-3.0-IPC1

- MCS-7825-H3-IPC1

- MCS-7825-I1-IPC1

- MCS-7825-H4-IPC1/CCE1/CCX1/ECS1/RC1

- MCS-7825-I2-IPC1

- MCS-7828-H3-IPC1

- MCS-7825-I3-IPC1

- MCS-7835H-3.0-IPC1

- MCS-7825-I4-IPC1/CCE1/CCX1/ECS1/RC1

- MCS-7835-H1-IPC1

- MCS-7828-I3-IPC1

- MCS-7835-H2-IPC1

- MCS-7835I-3.0-IPC1

- MCS-7835-H2-IPC2/CCE2/CCX2/RC2/ECS2

- MCS-7835-I1-IPC1

- MCS-7845H-3.0-IPC1

- MCS-7835-I2-IPC1

- MCS-7845-H1-IPC1

- MCS-7835-I2-IPC2/CCE2/CCX2/RC2/ECS2

- MCS-7845-H2-IPC1

- MCS-7845I-3.0-IPC1

- MCS-7845-H2-IPC2/CCE2/CCX2/RC2/ECS2

- MCS-7845-I1-IPC1

—

- MCS-7845-I2-IPC1

—

- MCS-7845-I2-IPC2/CCE2/CCX2/RC2/ECS2

—

#### Cisco Unified CM Release 7.1(1) Inapplicable MIBs

IBM-SYSTEM-POWER MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7815-I3-IPC1

MCS-7816-I3-IPC1

MCS-7816-I4-IPC1/CCX1

MCS-7825I-3.0-IPC1

MCS-7825-I1-IPC1

MCS-7825-I2-IPC1

MCS-7825-I3-IPC1

MCS-7825-I4-IPC1/CCE1/CCX1/ECS1/RC1

MCS-7828-I3-IPC1

IBM-SYSTEM-RAID MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7815-I3-IPC1

MCS-7816-I3-IPC1

MCS-7816-I4-IPC1/CCX1

HP CPQSM2 MIB does not apply to the following HP server model:

MCS-7825H-3.0-IPC1

### Cisco Unified CM Release 7.0(1) Supported Servers

Cisco Unified CM Release 7.0(1)

IBM Server Models

HP Server Models

- MCS-7815-I1-IPC1

- MCS-7816-H3-IPC1

- MCS-7815-I2-IPC1

- MCS-7825H-3.0-IPC1

- MCS-7815-I3-IPC1

- MCS-7825-H1-IPC1

- MCS-7816-I3-IPC1

- MCS-7825-H2-IPC1

- MCS-7825I-3.0-IPC1

- MCS-7825-H3-IPC1

- MCS-7825-I1-IPC1

- MCS-7828-H3-IPC1

- MCS-7825-I2-IPC1

- MCS-7835H-3.0-IPC1

- MCS-7825-I3-IPC1

- MCS-7835-H1-IPC1

- MCS-7828-I3-IPC1

- MCS-7835-H2-IPC1

- MCS-7835I-3.0-IPC1

- MCS-7845H-3.0-IPC1

- MCS-7835-I1-IPC1

- MCS-7845-H1-IPC1

- MCS-7835-I2-IPC1/IPC2

- MCS-7845-H2-IPC1

- MCS-7845I-3.0-IPC1

—

- MCS-7845-I1-IPC1

—

- MCS-7845-I2-IPC1/IPC2

—

- MCS-7815-I1-IPC1

—

IBM Model MCS-7835I-2.4-EVV1 is discontinued in this release.

HP MCS-7825H-2.2-EVV1, MCS-7835H-2.4-EVV1, and MCS-7845H-2.4-EVV1 are discontinued in this release.

#### Cisco Unified CM Release 7.0(1) MIB Unsupported Servers

IBM-SYSTEM-POWER MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7815-I3-IPC1

MCS-7816-I3-IPC1

MCS-7825I-3.0-IPC1

MCS-7825-I1-IPC1

MCS-7825-I2-IPC1

MCS-7825-I3-IPC1

MCS-7828-I3-IPC1

IBM-SYSTEM-RAID MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7815-I3-IPC1

MCS-7816-I3-IPC1

HP CPQSM2 MIB does not apply to the following HP server model:

MCS-7825H-3.0-IPC1

### Cisco Unified CM Release 6.1(3) Supported Servers

Cisco Unified CM Release 6.1(3)

IBM Server Models

HP Server Models

- MCS-7815-I1-IPC1

- MCS-7816-H3-IPC1

- MCS-7815-I2-IPC1

- MCS-7825H-2.2-EVV1

- MCS-7815-I3-IPC1

- MCS-7825H-3.0-IPC1

- MCS-7816-I3-IPC1

- MCS-7825-H1-IPC1

- MCS-7825I-3.0-IPC1

- MCS-7825-H2-IPC1

- MCS-7825-I1-IPC1

- MCS-7825-H3-IPC1

- MCS-7825-I2-IPC1

- MCS-7828-H3-IPC1

- MCS-7825-I3-IPC1

- MCS-7828-H4-BE

- MCS-7828-I3-IPC1

- MCS-7835H-2.4-EVV1

- MCS-7828-I4-BE

- MCS-7835H-3.0-IPC1

- MCS-7835I-2.4-EVV1

- MCS-7835-H1-IPC1

- MCS-7835I-3.0-IPC1

- MCS-7835-H2-IPC1

- MCS-7835-I1-IPC1

- MCS-7845H-2.4-EVV1

- MCS-7835-I2-IPC1/IPC2

- MCS-7845H-3.0-IPC1

- MCS-7845I-3.0-IPC1

- MCS-7845-H1-IPC1

- MCS-7845-I1-IPC1

- MCS-7845-H2-IPC1

- MCS-7845-I2-IPC1/IPC2

—

#### Cisco Unified CM Release 6.1(3) MIB Unsupported Servers

IBM-SYSTEM-POWER MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7815-I3-IPC1

MCS-7816-I3-IPC1

MCS-7825I-3.0-IPC1

MCS-7825-I1-IPC1

MCS-7825-I2-IPC1

MCS-7825-I3-IPC1

MCS-7828-I3-IPC1

MCS-7828-I4-BE

IBM-SYSTEM-RAID MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7815-I3-IPC1

MCS-7816-I3-IPC1

HP CPQSCSI MIB does not apply to the following HP server models:

MCS-7816-H3-IPC1

MCS-7825H-2.2-EVV1

MCS-7825H-3.0-IPC1

MCS-7825-H1-IPC1

MCS-7825-H2-IPC1

MCS-7825-H3-IPC1

MCS-7828-H3-IPC1

MCS-7828-H4-BE

MCS-7835H-2.4-EVV1

MCS-7835H-3.0-IPC1

MCS-7835-H1-IPC1

MCS-7835-H2-IPC1

MCS-7845H-2.4-EVV1

MCS-7845H-3.0-IPC1

MCS-7845-H1-IPC1

MCS-7845-H2-IPC1

HP CPQSM2 MIB does not apply to the following HP server models:

MCS-7825H-2.2-EVV1

MCS-7825H-3.0-IPC1

### Cisco Unified CM Release 6.1 Supported Servers

Cisco Unified CM Release 6.1

IBM Server Models

HP Server Models

- MCS-7815-I1-IPC1

- MCS-7816-H3-IPC1

- MCS-7815-I2-IPC1

- MCS-7825H-2.2-EVV1

- MCS-7815-I3-IPC1

- MCS-7825H-3.0-IPC1

- MCS-7816-I3-IPC1

- MCS-7825-H1-IPC1

- MCS-7825I-3.0-IPC1

- MCS-7825-H2-IPC1

- MCS-7825-I1-IPC1

- MCS-7825-H3-IPC1

- MCS-7825-I2-IPC1

- MCS-7828-H3-IPC1

- MCS-7825-I3-IPC1

- MCS-7835H-2.4-EVV1

- MCS-7828-I3-IPC1

- MCS-7835H-3.0-IPC1

- MCS-7835I-2.4-EVV1

- MCS-7835-H1-IPC1

- MCS-7835I-3.0-IPC1

- MCS-7835-H2-IPC1

- MCS-7835-I1-IPC1

- MCS-7845H-2.4-EVV1

- MCS-7835-I2-IPC1/IPC2

- MCS-7845H-3.0-IPC1

- MCS-7845I-3.0-IPC1

- MCS-7845-H1-IPC1

- MCS-7845-I1-IPC1

- MCS-7845-H2-IPC1

- MCS-7845-I2-IPC1/IPC2

—

#### Cisco Unified CM Release 6.1 MIB Unsupported Servers

IBM-SYSTEM-POWER MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7815-I3-IPC1

MCS-7816-I3-IPC1

MCS-7825I-3.0-IPC1

MCS-7825-I1-IPC1

MCS-7825-I2-IPC1

MCS-7825-I3-IPC1

MCS-7828-I3-IPC1

IBM-SYSTEM-RAID MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7815-I3-IPC1

MCS-7816-I3-IPC1

HP CPQSCSI MIB does not apply to the following HP server models:

MCS-7816-H3-IPC1

MCS-7825H-2.2-EVV1

MCS-7825H-3.0-IPC1

MCS-7825-H1-IPC1

MCS-7825-H2-IPC1

MCS-7825-H3-IPC1

MCS-7828-H3-IPC1

MCS-7828-H4-BE

MCS-7835H-2.4-EVV1

MCS-7835H-3.0-IPC1

MCS-7835-H1-IPC1

MCS-7835-H2-IPC1

MCS-7845H-2.4-EVV1

MCS-7845H-3.0-IPC1

MCS-7845-H1-IPC1

MCS-7845-H2-IPC1

HP CPQSM2 MIB does not apply to the following HP server models:

MCS-7825H-2.2-EVV1

MCS-7825H-3.0-IPC1

### Cisco Unified CM Release 6.0 Supported Servers

Cisco Unified CM Release 6.0

IBM Server Models

HP Server Models

Dell Server Models

- MCS-7815-I1-IPC1

- MCS-7816-H3-IPC1

- PE2950

- MCS-7815-I2-IPC1

- MCS-7825H-2.2-EVV1

- MCS-7816-I3-IPC1

- MCS-7825H-3.0-IPC1

- MCS-7825I-3.0-IPC1

- MCS-7825-H1-IPC1

- MCS-7825-I1-IPC1

- MCS-7825-H2-IPC1

- MCS-7825-I2-IPC1

- MCS-7825-H3-IPC1

- MCS-7828-I3-IPC1

- MCS-7828-H3-IPC1

- MCS-7835I-2.4-EVV1

- MCS-7835H-2.4-EVV1

- MCS-7835I-3.0-IPC1

- MCS-7835H-3.0-IPC1

- MCS-7835-I1-IPC1

- MCS-7835-H1-IPC1

- MCS-7835-I2-IPC1

- MCS-7835-H2-IPC1

- MCS-7845I-3.0-IPC1

- MCS-7845H-2.4-EVV1

- MCS-7845-I1-IPC1

- MCS-7845H-3.0-IPC1

- MCS-7845-I2-IPC1

- MCS-7845-H1-IPC1

- MCS-7825-I3-IPC1

- MCS-7845-H2-IPC1

#### Cisco Unified CM Release 6.0 MIB Unsupported Servers

IBM-SYSTEM-POWER (UMSPOWER) MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7816-I3-IPC1

MCS-7825I-3.0-IPC1

MCS-7825-I1-IPC1

MCS-7825-I2-IPC1

MCS-7825-I3-IPC1

MCS-7828-I3-IPC1

IBM-SERVERAID MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7825I-3.0-IPC1

MCS-7825-I1-IPC1

MCS-7825-I2-IPC1

MCS-7835-I2-IPC1

MCS-7845-I2-IPC1

IBM-SYSTEM-RAID MIB does not apply to the following IBM server models:

MCS-7815-I1-IPC1

MCS-7815-I2-IPC1

MCS-7816-I3-IPC1

HP CPQSCSI MIB does not apply to the following HP server models:

MCS-7816-H3-IPC1

MCS-7825H-2.2-EVV1

MCS-7825H-3.0-IPC1

MCS-7825-H1-IPC1

MCS-7825-H2-IPC1

MCS-7825-H3-IPC1

MCS-7828-H3-IPC1

MCS-7835H-2.4-EVV1

MCS-7835H-3.0-IPC1

MCS-7835-H1-IPC1

MCS-7835-H2-IPC1

MCS-7845H-2.4-EVV1

MCS-7845H-3.0-IPC1

MCS-7845-H1-IPC1

MCS-7845-H2-IPC1

HP CPQSM2 MIB does not apply to the following HP server models:

MCS-7825H-2.2-EVV1

MCS-7825H-3.0-IPC1

## IBM MIBs

MIB

OID

Function

Supported for browsing only

IBM-SYSTEM-HEALTH-MIB

1.3.6.1.4.1.2.6.159.1.1.30

Provides temperature, voltage, and fan status

IBM-SYSTEM-ASSETID-MIB

1.3.6.1.4.1.2.6.159.1.1.60

Provides hardware component asset data

IBM-SYSTEM-LMSENSOR-MIB

1.3.6.1.4.1.2.6.159.1.1.80

Provides temperature, voltage, and fan details

IBM-SYSTEM-NETWORK-MIB

1.3.6.1.4.1.2.6.159.1.1.110

Provides Network Interface Card (NIC) status

IBM-SYSTEM-MEMORY-MIB

1.3.6.1.4.1.2.6.159.1.1.120

Provides physical memory details

IBM-SYSTEM-POWER-MIB

1.3.6.1.4.1.2.6.159.1.1.130

Provides power supply details

IBM-SYSTEM-PROCESSOR-MIB

1.3.6.1.4.1.2.6.159.1.1.140

Provides CPU asset/status data

Supported for system traps

IBM-SYSTEM-TRAP

1.3.6.1.4.1.2.6.159.1.1.0

Provides temperature, voltage, fan, disk, NIC, memory, power supply, and CPU details

IBM-SERVERAID-MIB

1.3.6.1.4.1.2.6.167.2

Provides RAID status

IBM-SYSTEM-RAID-MIB

1.3.6.1.4.1.2.6.159.1.1.200.1

Provides RAID status

IBM-SYSTEM-STORAGE-MIB

1.3.6.1.4.1.2.6.159.3.1

Provides RAID status

### IBM Hardware Status Messages

Cisco Unified CM Release 6.x

MCS-78xx Status

MIBS and Object Names

Object Responses

System Fan

IBM-SYSTEM-LMSENSOR-MIB::ibmSystem TachometerStatus (also see ibmSystemTachometerKeyIndex)

This is a string indicating the current status of the object. Various operational and non-operational statuses can be defined.

Operational statuses are OK, Degraded and Pred Fail. Pred Fail indicates that an element may be functioning properly but predicting
                                             a failure in the near future. An example is a SMART-enabled hard drive.

Non-operational statuses are Error, Starting, Stopping and Service. Service can apply during mirror-resilvering of a disk,
                                             reload of a user permissions list, or other administrative work.

Not all such work is on-line, yet the managed element is neither OK nor in one of the other states.

OK = Normal; Error = Critical

Voltage Sensor

IBM-SYSTEM-LMSENSOR-MIB::ibmSystem VoltageSensorStatus (also see ibmSystemVoltageSensorKeyIndex)

This is a string indicating the current status of the object. Various operational and non-operational statuses can be defined.

Operational statuses are OK, Degraded and Pred Fail. Pred Fail indicates that an element may be functioning properly but predicting
                                             a failure in the near future. An example is a SMART-enabled hard drive.

Non-operational statuses are Error, Starting, Stopping and Service. Service can apply during mirror-resilvering of a disk,
                                             reload of a user permissions list, or other administrative work. Not all such work is on-line, yet the managed element is
                                             neither OK nor in one of the other states.

OK = Normal; Error = Critical

Thermal

IBM-SYSTEM-LMSENSOR-MIB::ibmSystem TemperatureSensorStatus (also see ibmSystemTemperatureSensorKeyIndex)

The Status property is a string indicating the current status of the object. Various operational and non-operational statuses
                                             can be defined. Operational statuses are OK, Degraded and Pred Fail. Pred Fail indicates that an element may be functioning
                                             properly but predicting a failure in the near future. An example is a SMART-enabled hard drive. Non-operational statuses can
                                             also be specified. These are Error, Starting, Stopping and Service. The latter, Service, could apply during mirror-resilvering
                                             of a disk, reload of a user permissions list, or other administrative work. Not all such work is on-line, yet the managed
                                             element is neither OK nor in one of the other states. OK     = Normal; Error = Critical

Network Interface Card

IBM-SYSTEM-NETWORK-MIB::ibmSystem LogicalNetworkAdapterStatus (also see ibmSystemLogicalNetworkAdapterKeyIndex)

The online status of the adapter.

Logical Drive

IBM-SYSTEM-TRAP-MIB::ibmSystem RaidLogicalDriveStatus (also see ibmSystemRaidLogicalDriveKeyIndex)

The status of the logical drive

Physical Drive

IBM-SYSTEM-TRAP-MIB::ibmSystem RaidDiskDriveStatus & ibmSystemRaidControllerStatus (also see ibmSystemRaidDiskDriveKeyIndex
                                             & ibmSystemRaidControllerKeyIndex)

## Hewlett Packard MIBs

MIB

OID

Function

Supported for browsing and system traps

CPQSTDEQ-MIB

1.3.6.1.4.1.232.1

Provides hardware component configuration data

CPQSINFO-MIB

1.3.6.1.4.1.232.2

Provides hardware component asset data

CPQIDA-MIB

1.3.6.1.4.1.232.3

Provides RAID status/events

CPQHLTH-MIB

1.3.6.1.4.1.232.6

Provides hardware components status/events

CPQSTSYS-MIB

1.3.6.1.4.1.232.8

Provides storage (disk) systems status/events

CPQSM2-MIB

1.3.6.1.4.1.232.9

Provides iLO status/events

CPQTHRSH-MIB

1.3.6.1.4.1.232.10

Provides alarm threshold management

CPQHOST-MIB

1.3.6.1.4.1.232.11

Provides operating system information

CPQIDE-MIB

1.3.6.1.4.1.232.14

Provides IDE (CD-ROM) drive status/events

CPQNIC-MIB

1.3.6.1.4.1.232.18

Provides Network Interface Card (NIC) status/events

### HP Hardware Status Messages

The following table lists status messages, MIBs and OIDs, MIB object names and clearing values, and object responses.

Cisco Unified CM Release 6.x

MCS-78xx Status

MIB and OID

MIB Object Name and Clearing Value

Object Response

Logical Drive 23

CPQIDA-MIB1.3.6.1.4.1.232.3.2.3.1.1.4

cpqDaLogDrvStatus

Clearing Value = 2

The logical drive can be in one of the following states:

- Ok (2) Indicates that the logical drive is in normal operation mode.

- Failed (3) Indicates that more physical drives have failed than the fault tolerance mode of the logical drive can handle without
                                                data loss.

- Unconfigured (4) Indicates that the logical drive is not configured.

- Recovering (5) Indicates that the logical drive is using Interim Recovery Mode. In Interim Recovery Mode, at least one physical
                                                drive has failed, but the logical drive's fault tolerance mode lets the drive continue to operate with no data loss.

- Ready Rebuild (6) Indicates that the logical drive is ready for Automatic Data Recovery. The physical drive that failed has
                                                been replaced, but the logical drive is still operating in Interim Recovery Mode.

- Rebuilding (7) Indicates that the logical drive is currently doing Automatic Data Recovery. During Automatic Data Recovery,
                                                fault tolerance algorithms restore data to the replacement drive.

- Wrong Drive (8) Indicates that the wrong physical drive was replaced after a physical drive failure.

- Bad Connect (9) Indicates that a physical drive is not responding.

Physical Drive1

CPQIDA-MIB1.3.6.1.4.1.232.3.2.5.1.1.6

cpqDaPhyDrv Status

Clearing Value = 2

- The following values are valid for the physical drive status:

- other (1) Indicates that the instrument agent does not recognize the drive. You may need to upgrade your instrument agent
                                                and/or driver software.

- ok (2) Indicates the drive is functioning properly.

- failed (3) Indicates that the drive is no longer operating and should be replaced.

- predictiveFailure(4) Indicates that the drive has a predictive failure error and should be replaced.

System Fan

CPQHLTH-MIB1.3.6.1.4.1.232.6.2.6.4

cpqHeThermalSystemFan Status

Clearing Value = 2

This value will be one of the following:

- other(1) Fan status detection is not supported by this system or driver.

- ok(2) The fan is operating properly.

- degraded(2) A redundant fan is not operating properly.

- failed(4) A non-redundant fan is not operating properly.

CPU Fan

CPQHLTH-MIB1.3.6.1.4.1.232.6.2.6.5

cpqHeThermalCpuFan Status

Clearing Value = 2

This value will be one of the following:

- other(1) Fan status detection is not supported by this system or driver.

- ok(2) The fan is operating properly.

- degraded(2) A redundant fan is not operating properly.

- failed(4) A non-redundant fan is not operating properly.

Network Interface Card (NIC)

CPQNIC-MIB1.3.6.1.4.1.232.18.2.3.1.1.13

cpqNicIfPhysAdapterState

Clearing Value = 2 and 3

The following values are valid—

- unknown(1) The instrument agent was not able to determine the status of the adapter. The instrument agent may need to be upgraded.

- ok(2) The physical adapter is operating properly.

- generalFailure(3) The physical adapter has failed.

- linkFailure(4) The physical adapter has lost link. Check the cable connections to this adapter.

Thermal

CPQHLTH-MIB1.3.6.1.4.1.232.6.2.6.1

cpqHeThermalCondition

Clearing Value = 2

This value will be one of the following:

- other(1) Temperature could not be determined.

- ok(2) The temperature sensor is within normal operating range.

- degraded(3) The temperature sensor is outside of normal operating range.

- failed(4) The temperature sensor detects a condition that could permanently damage the system.

The system automatically shuts down if the failed (4) condition occurs, so it is unlikely that 4 will ever be returned by
                                                         the agent. If the cpqHeThermalDegradedAction is set to shut down (3), the system will shut down if the condition occurs.

Power Supply1

CPQHLTH-MIB1.3.6.1.4.1.232.6.2.9.3.1.5

cpqHeFltTolPowerSupply Status

Clearing Value = 1

This value will be one of the following:

- other(1) The status could not be determined or not present.

- ok(2) The power supply is operating normally.

- degraded(3) A temperature sensor, fan or other power supply component is outside of normal operating range.

- failed(4) A power supply component detects a condition that could permanently damage the system.

NIC Errors

CPQNIC-MIB1.3.6.1.4.1.232.18.2.3.1.1.16

cpqNicIfPhysAdapterGood Transmits

Clearing Value = <0.5% for 1 hour

Interface is experiencing excessive errors

1.3.6.1.4.1.232.18.2.3.1.1.18

cpqNicIfPhysAdapterBad  Transmits

1.3.6.1.4.1.232.18.2.3.1.1.17

cpqNicIfPhysAdapterGood Receives

1.3.6.1.4.1.232.18.2.3.1.1.19

cpqNicIfPhysAdapterBad Receives

NIC Utilization

CPQNIC-MIB1.3.6.1.4.1.232.18.2.3.1.1.16

cpqNicIfPhysAdapterGood Transmits

Clearing Value = <50% for 1 hour

Interface is experiencing High Utilization

1.3.6.1.4.1.232.18.2.3.1.1.18

cpqNicIfPhysAdapterBad Transmits

1.3.6.1.4.1.232.18.2.3.1.1.17

cpqNicIfPhysAdapterGood Receives

1.3.6.1.4.1.232.18.2.3.1.1.19

cpqNicIfPhysAdapterBad Receives

Memory Module Trap

1.3.6.1.4.1.232.6.3

cpqHe4CorrMemReplace MemModule

See CPQHOST-MIB for information on the following trap variables:

- sysName

- cpqHoTrapFlags

- cpqHeResMemBoardIndex

- cpqHeResMemModuleIndex

- cpqHeResMemModuleSpare PartNo

- cpqSiMemModuleSize

- cpqSiServerSystemId

Trap number is 6056 which replaces 6029.

A correctable memory log entry indicates a memory module needs to be replaced. The errors have been corrected, but the memory
                                             module should be replaced. The error information is reported in the variable cpqHeCorrMemErrDesc

78x5-H Insite Manager Service

HOST-RESOURCES-MIB1.3.6.1.2.1.25.4.2.1.2

cmaeventd

Compaq Insite Manager Service Failure

cmafcad

cmahealthd

cmahostd

Positive String ID forcmaidad

cmaided

cmanicd

cmapeerd

cmaperfd

cmasm2d

cmastdeqd

cmathreshd

## Intel MIBs

The following table  lists Intel MIBs, OID, and functions.

MIB

OID

Function

Supported for browsing and system traps

INTEL-SERVER-BASEBOARD6

1.3.6.1.4.1.343.2.10.3.6.200

Denotes the power group and describes voltage probes, status, and readings

1.3.6.1.4.1.343.2.10.3.6.300

Denotes the thermal group and describes cooling devices, fans, and temperature probes

1.3.6.1.4.1.343.2.10.3.6.10

Denotes the instances of cooling devices

1.3.6.1.4.1.343.2.10.3.6.20

Denotes the status, reading, and threshold for every cooling device and fan

1.3.6.1.4.1.343.2.10.3.6.30

Denotes the instances of temperature probes

1.3.6.1.4.1.343.2.10.3.6.40

Denotes the status, reading, thresholds for every temperature probe

1.3.6.1.4.1.343.2.10.3.6.1000

Denotes the events group and describes power, thermal, and system events

### Intel Hardware Status Messages

The following table lists status messages, MIBs and OIDs, MIB object names and clearing values, and object responses.

Cisco Unified CM Release 7.x

MCS-78xx Status

MIBS and Object Names

Object Responses

Power

INTEL-SERVER-BASEBOARD6::powerEvents

System

INTEL-SERVER-BASEBOARD6::systemEvents

Thermal

INTEL-SERVER-BASEBOARD6::thermalEvents

| Cisco Unified CM Release 9.5(1) |
|---|
| IBM Server Models | HP Server Models |
| MCS-7816-I4-IPC1/CCX1 | MCS-7835-H2-IPC1 |
| MCS-7816-I5-IPC1/CCX1 | MCS-7835-H2-IPC2 |
| MCS-7825-I4-IPC1 | MCS-7845-H2-IPC1 |
| MCS-7825-I5-IPC1 | MCS-7845-H2-IPC2 |
| MCS-7825-I6-IPC1 |  |
| MCS-7828-I4-SS1 |  |
| MCS-7828-I5-SS1 |  |
| MCS-7835-I3-IPC1 |  |
| MCS-7845-I3-IPC1 |  |
| MCS-7845-I4-IPC1 |  |

| Cisco Unified CM Release 8.5(1) |
|---|
| IBM Server Models | HP Server Models | Cisco Unified Computing System |
| MCS-7816-I3-IPC1 | MCS-7816-H3-IPC1 | UCS B200 M1 |
| MCS-7816-I4-IPC1/CCX1 | MCS-7825-H2-IPC1 | UCS C210 M1 |
| MCS-7816-I5-IPC1/CCX1 | MCS-7825-H3-IPC1 | — |
| MCS-7825-I3-IPC1 | MCS-7825-H4-IPC1 | — |
| MCS-7825-I4-IPC1 | MCS-7828-H3-IPC1 | — |
| MCS-7825-I5-IPC1 | MCS-7835-H2-IPC1 | — |
| MCS-7828-I3-SS1 | MCS-7835-H2-IPC2 | — |
| MCS-7828-I4-SS1 | DL380G6 (Single E5504 CPU) | — |
| MCS-7828-I5-SS1 | MCS-7845-H2-IPC1 | — |
| MCS-7835-I2-IPC1 | MCS-7845-H2-IPC2 | — |
| MCS-7835-I2-IPC2 | DL380G6 (Single E5540 CPU) | — |
| MCS-7835-I3-IPC1 | — | — |
| MCS-7845-I2-IPC1 | — | — |
| MCS-7845-I2-IPC2 | — | — |
| MCS-7845-I3-IPC1 | — | — |

| Cisco Unified CM Release 8.0(2) |
|---|
| IBM Server Models | HP Server Models | Cisco Unified Computing System |
| MCS-7815-I2-IPC1 | MCS-7816-H3-IPC1 | UCS B200 M1 |
| MCS-7816-I3-IPC1 | MCS-7825-H2-IPC1 | — |
| MCS-7816-I4-IPC1/CCX1 | MCS-7825-H3-IPC1 | — |
| MCS-7825-I2-IPC1 | MCS-7825-H4-IPC1 | — |
| MCS-7825-I3-IPC1 | MCS-7828-H3-IPC1 | — |
| MCS-7825-I4-IPC1 | MCS-7835-H2-IPC1 | — |
| MCS-7828-I3-SS1 | MCS-7835-H2-IPC2 | — |
| MCS-7828-I4-SS1 | DL380G6 (Single E5504 CPU) | — |
| MCS-7835-I2-IPC1 | MCS-7845-H2-IPC1 | — |
| MCS-7835-I2-IPC2 | MCS-7845-H2-IPC2 | — |
| MCS-7835-I3-IPC1 | DL380G6 (Single E5540 CPU) | — |
| MCS-7845-I2-IPC1 | — | — |
| MCS-7845-I2-IPC2 | — | — |
| MCS-7845-I3-IPC1 | — | — |

| Unified Communications Manager Release 8.0(1) |
|---|
| IBM Server Models | HP Server Models |
| MCS-7815-I2-IPC1 1 | MCS-7816-H3-IPC1 2 |
| MCS-7816-I3-IPC1 3 | MCS-7825-H2-IPC1 4 |
| MCS-7816-I4-IPC1 5 | MCS-7825-H2-IPC2 6 |
| MCS-7825-I2-IPC1 7 | MCS-7825-H3-IPC1 8 |
| MCS-7825-I2-IPC2 9 | MCS-7825-H4-IPC1 10 |
| MCS-7825-I3-IPC1 11 | MCS-7828-H3 |
| MCS-7825-I4-IPC1 12 | MCS-7835-H2-IPC1 13 |
| MCS-7828-I3 | MCS-7835-H2-IPC2 14 |
| MCS-7828-I4 | MCS-7845-H2-IPC1 15 |
| MCS-7835-I2-IPC1 16 | MCS-7845-H2-IPC2 17 |
| MCS-7835-I2-IPC2 18 | — |
| MCS-7835-I3-IPC1 19 | — |
| MCS-7845-I2-IPC1 20 | — |
| MCS-7845-I2-IPC2 21 | — |
| MCS-7845-I3-IPC1 22 | — |

| Note | For information about the product end-of-life notices, go to http://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_eol_notices_list.html |
|---|---|

| Cisco Unified CM Release 7.1(2) |
|---|
| IBM Server Models | HP Server Models |
| MCS-7815-I1-IPC1 | MCS-7816-H3-IPC1 |
| MCS-7815-I2-IPC1 | MCS-7816-H4-IPC1/CCX1 |
| MCS-7815-I3-IPC1 | MCS-7825H-3.0-IPC1 |
| MCS-7816-I3-IPC1 | MCS-7825-H1-IPC1 |
| MCS-7816-I4-IPC1/CCX1 | MCS-7825-H2-IPC1 |
| MCS-7825I-3.0-IPC1 | MCS-7825-H3-IPC1 |
| MCS-7825-I1-IPC1 | MCS-7825-H4-IPC1/CCE1/CCX1/ECS1/RC1 |
| MCS-7825-I2-IPC1 | MCS-7828-H3-IPC1 |
| MCS-7825-I3-IPC1 | MCS-7835H-3.0-IPC1 |
| MCS-7825-I4-IPC1/CCE1/CCX1/ECS1/RC1 | MCS-7835-H1-IPC1 |
| MCS-7828-I3-IPC1 | MCS-7835-H2-IPC1 |
| MCS-7835I-3.0-IPC1 | MCS-7835-H2-IPC2/CCE2/CCX2/RC2/ECS2 |
| MCS-7835-I1-IPC1 | MCS-7845H-3.0-IPC1 |
| MCS-7835-I2-IPC1 | MCS-7845-H1-IPC1 |
| MCS-7835-I2-IPC2/CCE2/CCX2/RC2/ECS2 | MCS-7845-H2-IPC1 |
| MCS-7845I-3.0-IPC1 | MCS-7845-H2-IPC2/CCE2/CCX2/RC2/ECS |
| MCS-7845-I1-IPC1 | — |
| MCS-7845-I2-IPC1 | — |
| MCS-7845-I2-IPC2/CCE2/CCX2/RC2/ECS2 | — |

| Cisco Unified CM Release 7.1(1) |
|---|
| IBM Server Models | HP Server Models |
| MCS-7815-I1-IPC1 | MCS-7816-H3-IPC1 |
| MCS-7815-I2-IPC1 | MCS-7816-H4-IPC1/CCX1 |
| MCS-7815-I3-IPC1 | MCS-7825H-3.0-IPC1 |
| MCS-7816-I3-IPC1 | MCS-7825-H1-IPC1 |
| MCS-7816-I4-IPC1/CCX1 | MCS-7825-H2-IPC1 |
| MCS-7825I-3.0-IPC1 | MCS-7825-H3-IPC1 |
| MCS-7825-I1-IPC1 | MCS-7825-H4-IPC1/CCE1/CCX1/ECS1/RC1 |
| MCS-7825-I2-IPC1 | MCS-7828-H3-IPC1 |
| MCS-7825-I3-IPC1 | MCS-7835H-3.0-IPC1 |
| MCS-7825-I4-IPC1/CCE1/CCX1/ECS1/RC1 | MCS-7835-H1-IPC1 |
| MCS-7828-I3-IPC1 | MCS-7835-H2-IPC1 |
| MCS-7835I-3.0-IPC1 | MCS-7835-H2-IPC2/CCE2/CCX2/RC2/ECS2 |
| MCS-7835-I1-IPC1 | MCS-7845H-3.0-IPC1 |
| MCS-7835-I2-IPC1 | MCS-7845-H1-IPC1 |
| MCS-7835-I2-IPC2/CCE2/CCX2/RC2/ECS2 | MCS-7845-H2-IPC1 |
| MCS-7845I-3.0-IPC1 | MCS-7845-H2-IPC2/CCE2/CCX2/RC2/ECS2 |
| MCS-7845-I1-IPC1 | — |
| MCS-7845-I2-IPC1 | — |
| MCS-7845-I2-IPC2/CCE2/CCX2/RC2/ECS2 | — |

| Cisco Unified CM Release 7.0(1) |
|---|
| IBM Server Models | HP Server Models |
| MCS-7815-I1-IPC1 | MCS-7816-H3-IPC1 |
| MCS-7815-I2-IPC1 | MCS-7825H-3.0-IPC1 |
| MCS-7815-I3-IPC1 | MCS-7825-H1-IPC1 |
| MCS-7816-I3-IPC1 | MCS-7825-H2-IPC1 |
| MCS-7825I-3.0-IPC1 | MCS-7825-H3-IPC1 |
| MCS-7825-I1-IPC1 | MCS-7828-H3-IPC1 |
| MCS-7825-I2-IPC1 | MCS-7835H-3.0-IPC1 |
| MCS-7825-I3-IPC1 | MCS-7835-H1-IPC1 |
| MCS-7828-I3-IPC1 | MCS-7835-H2-IPC1 |
| MCS-7835I-3.0-IPC1 | MCS-7845H-3.0-IPC1 |
| MCS-7835-I1-IPC1 | MCS-7845-H1-IPC1 |
| MCS-7835-I2-IPC1/IPC2 | MCS-7845-H2-IPC1 |
| MCS-7845I-3.0-IPC1 | — |
| MCS-7845-I1-IPC1 | — |
| MCS-7845-I2-IPC1/IPC2 | — |
| MCS-7815-I1-IPC1 | — |

| Note | IBM Model MCS-7835I-2.4-EVV1 is discontinued in this release. |
|---|---|

| Note | HP MCS-7825H-2.2-EVV1, MCS-7835H-2.4-EVV1, and MCS-7845H-2.4-EVV1 are discontinued in this release. |
|---|---|

| Cisco Unified CM Release 6.1(3) |
|---|
| IBM Server Models | HP Server Models |
| MCS-7815-I1-IPC1 | MCS-7816-H3-IPC1 |
| MCS-7815-I2-IPC1 | MCS-7825H-2.2-EVV1 |
| MCS-7815-I3-IPC1 | MCS-7825H-3.0-IPC1 |
| MCS-7816-I3-IPC1 | MCS-7825-H1-IPC1 |
| MCS-7825I-3.0-IPC1 | MCS-7825-H2-IPC1 |
| MCS-7825-I1-IPC1 | MCS-7825-H3-IPC1 |
| MCS-7825-I2-IPC1 | MCS-7828-H3-IPC1 |
| MCS-7825-I3-IPC1 | MCS-7828-H4-BE |
| MCS-7828-I3-IPC1 | MCS-7835H-2.4-EVV1 |
| MCS-7828-I4-BE | MCS-7835H-3.0-IPC1 |
| MCS-7835I-2.4-EVV1 | MCS-7835-H1-IPC1 |
| MCS-7835I-3.0-IPC1 | MCS-7835-H2-IPC1 |
| MCS-7835-I1-IPC1 | MCS-7845H-2.4-EVV1 |
| MCS-7835-I2-IPC1/IPC2 | MCS-7845H-3.0-IPC1 |
| MCS-7845I-3.0-IPC1 | MCS-7845-H1-IPC1 |
| MCS-7845-I1-IPC1 | MCS-7845-H2-IPC1 |
| MCS-7845-I2-IPC1/IPC2 | — |

| Cisco Unified CM Release 6.1 |
|---|
| IBM Server Models | HP Server Models |
| MCS-7815-I1-IPC1 | MCS-7816-H3-IPC1 |
| MCS-7815-I2-IPC1 | MCS-7825H-2.2-EVV1 |
| MCS-7815-I3-IPC1 | MCS-7825H-3.0-IPC1 |
| MCS-7816-I3-IPC1 | MCS-7825-H1-IPC1 |
| MCS-7825I-3.0-IPC1 | MCS-7825-H2-IPC1 |
| MCS-7825-I1-IPC1 | MCS-7825-H3-IPC1 |
| MCS-7825-I2-IPC1 | MCS-7828-H3-IPC1 |
| MCS-7825-I3-IPC1 | MCS-7835H-2.4-EVV1 |
| MCS-7828-I3-IPC1 | MCS-7835H-3.0-IPC1 |
| MCS-7835I-2.4-EVV1 | MCS-7835-H1-IPC1 |
| MCS-7835I-3.0-IPC1 | MCS-7835-H2-IPC1 |
| MCS-7835-I1-IPC1 | MCS-7845H-2.4-EVV1 |
| MCS-7835-I2-IPC1/IPC2 | MCS-7845H-3.0-IPC1 |
| MCS-7845I-3.0-IPC1 | MCS-7845-H1-IPC1 |
| MCS-7845-I1-IPC1 | MCS-7845-H2-IPC1 |
| MCS-7845-I2-IPC1/IPC2 | — |

| Cisco Unified CM Release 6.0 |
|---|
| IBM Server Models | HP Server Models | Dell Server Models |
| MCS-7815-I1-IPC1 | MCS-7816-H3-IPC1 | PE2950 |
| MCS-7815-I2-IPC1 | MCS-7825H-2.2-EVV1 |
| MCS-7816-I3-IPC1 | MCS-7825H-3.0-IPC1 |
| MCS-7825I-3.0-IPC1 | MCS-7825-H1-IPC1 |
| MCS-7825-I1-IPC1 | MCS-7825-H2-IPC1 |
| MCS-7825-I2-IPC1 | MCS-7825-H3-IPC1 |
| MCS-7828-I3-IPC1 | MCS-7828-H3-IPC1 |
| MCS-7835I-2.4-EVV1 | MCS-7835H-2.4-EVV1 |
| MCS-7835I-3.0-IPC1 | MCS-7835H-3.0-IPC1 |
| MCS-7835-I1-IPC1 | MCS-7835-H1-IPC1 |
| MCS-7835-I2-IPC1 | MCS-7835-H2-IPC1 |
| MCS-7845I-3.0-IPC1 | MCS-7845H-2.4-EVV1 |
| MCS-7845-I1-IPC1 | MCS-7845H-3.0-IPC1 |
| MCS-7845-I2-IPC1 | MCS-7845-H1-IPC1 |
| MCS-7825-I3-IPC1 | MCS-7845-H2-IPC1 |

| MIB | OID | Function |
|---|---|---|
| Supported for browsing only |
| IBM-SYSTEM-HEALTH-MIB | 1.3.6.1.4.1.2.6.159.1.1.30 | Provides temperature, voltage, and fan status |
| IBM-SYSTEM-ASSETID-MIB | 1.3.6.1.4.1.2.6.159.1.1.60 | Provides hardware component asset data |
| IBM-SYSTEM-LMSENSOR-MIB | 1.3.6.1.4.1.2.6.159.1.1.80 | Provides temperature, voltage, and fan details |
| IBM-SYSTEM-NETWORK-MIB | 1.3.6.1.4.1.2.6.159.1.1.110 | Provides Network Interface Card (NIC) status |
| IBM-SYSTEM-MEMORY-MIB | 1.3.6.1.4.1.2.6.159.1.1.120 | Provides physical memory details |
| IBM-SYSTEM-POWER-MIB | 1.3.6.1.4.1.2.6.159.1.1.130 | Provides power supply details |
| IBM-SYSTEM-PROCESSOR-MIB | 1.3.6.1.4.1.2.6.159.1.1.140 | Provides CPU asset/status data |
| Supported for system traps |
| IBM-SYSTEM-TRAP | 1.3.6.1.4.1.2.6.159.1.1.0 | Provides temperature, voltage, fan, disk, NIC, memory, power supply, and CPU details |
| IBM-SERVERAID-MIB | 1.3.6.1.4.1.2.6.167.2 | Provides RAID status |
| IBM-SYSTEM-RAID-MIB | 1.3.6.1.4.1.2.6.159.1.1.200.1 | Provides RAID status |
| IBM-SYSTEM-STORAGE-MIB | 1.3.6.1.4.1.2.6.159.3.1 | Provides RAID status |

| Cisco Unified CM Release 6.x |
|---|
| MCS-78xx Status | MIBS and Object Names | Object Responses |
| System Fan | IBM-SYSTEM-LMSENSOR-MIB::ibmSystem TachometerStatus (also see ibmSystemTachometerKeyIndex) | This is a string indicating the current status of the object. Various operational and non-operational statuses can be defined. Operational statuses are OK, Degraded and Pred Fail. Pred Fail indicates that an element may be functioning properly but predicting
                                             a failure in the near future. An example is a SMART-enabled hard drive. Non-operational statuses are Error, Starting, Stopping and Service. Service can apply during mirror-resilvering of a disk,
                                             reload of a user permissions list, or other administrative work. Not all such work is on-line, yet the managed element is neither OK nor in one of the other states. OK = Normal; Error = Critical |
| Voltage Sensor | IBM-SYSTEM-LMSENSOR-MIB::ibmSystem VoltageSensorStatus (also see ibmSystemVoltageSensorKeyIndex) | This is a string indicating the current status of the object. Various operational and non-operational statuses can be defined. Operational statuses are OK, Degraded and Pred Fail. Pred Fail indicates that an element may be functioning properly but predicting
                                             a failure in the near future. An example is a SMART-enabled hard drive. Non-operational statuses are Error, Starting, Stopping and Service. Service can apply during mirror-resilvering of a disk,
                                             reload of a user permissions list, or other administrative work. Not all such work is on-line, yet the managed element is
                                             neither OK nor in one of the other states. OK = Normal; Error = Critical |
| Thermal | IBM-SYSTEM-LMSENSOR-MIB::ibmSystem TemperatureSensorStatus (also see ibmSystemTemperatureSensorKeyIndex) | The Status property is a string indicating the current status of the object. Various operational and non-operational statuses
                                             can be defined. Operational statuses are OK, Degraded and Pred Fail. Pred Fail indicates that an element may be functioning
                                             properly but predicting a failure in the near future. An example is a SMART-enabled hard drive. Non-operational statuses can
                                             also be specified. These are Error, Starting, Stopping and Service. The latter, Service, could apply during mirror-resilvering
                                             of a disk, reload of a user permissions list, or other administrative work. Not all such work is on-line, yet the managed
                                             element is neither OK nor in one of the other states. OK     = Normal; Error = Critical |
| Network Interface Card | IBM-SYSTEM-NETWORK-MIB::ibmSystem LogicalNetworkAdapterStatus (also see ibmSystemLogicalNetworkAdapterKeyIndex) | The online status of the adapter. |
| Logical Drive | IBM-SYSTEM-TRAP-MIB::ibmSystem RaidLogicalDriveStatus (also see ibmSystemRaidLogicalDriveKeyIndex) | The status of the logical drive |
| Physical Drive | IBM-SYSTEM-TRAP-MIB::ibmSystem RaidDiskDriveStatus & ibmSystemRaidControllerStatus (also see ibmSystemRaidDiskDriveKeyIndex
                                             & ibmSystemRaidControllerKeyIndex) |  |

| MIB | OID | Function |
|---|---|---|
| Supported for browsing and system traps |
| CPQSTDEQ-MIB | 1.3.6.1.4.1.232.1 | Provides hardware component configuration data |
| CPQSINFO-MIB | 1.3.6.1.4.1.232.2 | Provides hardware component asset data |
| CPQIDA-MIB | 1.3.6.1.4.1.232.3 | Provides RAID status/events |
| CPQHLTH-MIB | 1.3.6.1.4.1.232.6 | Provides hardware components status/events |
| CPQSTSYS-MIB | 1.3.6.1.4.1.232.8 | Provides storage (disk) systems status/events |
| CPQSM2-MIB | 1.3.6.1.4.1.232.9 | Provides iLO status/events |
| CPQTHRSH-MIB | 1.3.6.1.4.1.232.10 | Provides alarm threshold management |
| CPQHOST-MIB | 1.3.6.1.4.1.232.11 | Provides operating system information |
| CPQIDE-MIB | 1.3.6.1.4.1.232.14 | Provides IDE (CD-ROM) drive status/events |
| CPQNIC-MIB | 1.3.6.1.4.1.232.18 | Provides Network Interface Card (NIC) status/events |

| Cisco Unified CM Release 6.x |
|---|
| MCS-78xx Status | MIB and OID | MIB Object Name and Clearing Value | Object Response |
| Logical Drive 23 | CPQIDA-MIB1.3.6.1.4.1.232.3.2.3.1.1.4 | cpqDaLogDrvStatus Clearing Value = 2 | The logical drive can be in one of the following states: Ok (2) Indicates that the logical drive is in normal operation mode. Failed (3) Indicates that more physical drives have failed than the fault tolerance mode of the logical drive can handle without
                                                data loss. Unconfigured (4) Indicates that the logical drive is not configured. Recovering (5) Indicates that the logical drive is using Interim Recovery Mode. In Interim Recovery Mode, at least one physical
                                                drive has failed, but the logical drive's fault tolerance mode lets the drive continue to operate with no data loss. Ready Rebuild (6) Indicates that the logical drive is ready for Automatic Data Recovery. The physical drive that failed has
                                                been replaced, but the logical drive is still operating in Interim Recovery Mode. Rebuilding (7) Indicates that the logical drive is currently doing Automatic Data Recovery. During Automatic Data Recovery,
                                                fault tolerance algorithms restore data to the replacement drive. Wrong Drive (8) Indicates that the wrong physical drive was replaced after a physical drive failure. Bad Connect (9) Indicates that a physical drive is not responding. |
| Physical Drive1 | CPQIDA-MIB1.3.6.1.4.1.232.3.2.5.1.1.6 | cpqDaPhyDrv Status Clearing Value = 2 | The following values are valid for the physical drive status: other (1) Indicates that the instrument agent does not recognize the drive. You may need to upgrade your instrument agent
                                                and/or driver software. ok (2) Indicates the drive is functioning properly. failed (3) Indicates that the drive is no longer operating and should be replaced. predictiveFailure(4) Indicates that the drive has a predictive failure error and should be replaced. |
| System Fan | CPQHLTH-MIB1.3.6.1.4.1.232.6.2.6.4 | cpqHeThermalSystemFan Status Clearing Value = 2 | This value will be one of the following: other(1) Fan status detection is not supported by this system or driver. ok(2) The fan is operating properly. degraded(2) A redundant fan is not operating properly. failed(4) A non-redundant fan is not operating properly. |
| CPU Fan | CPQHLTH-MIB1.3.6.1.4.1.232.6.2.6.5 | cpqHeThermalCpuFan Status Clearing Value = 2 | This value will be one of the following: other(1) Fan status detection is not supported by this system or driver. ok(2) The fan is operating properly. degraded(2) A redundant fan is not operating properly. failed(4) A non-redundant fan is not operating properly. |
| Network Interface Card (NIC) | CPQNIC-MIB1.3.6.1.4.1.232.18.2.3.1.1.13 | cpqNicIfPhysAdapterState Clearing Value = 2 and 3 | The following values are valid— unknown(1) The instrument agent was not able to determine the status of the adapter. The instrument agent may need to be upgraded. ok(2) The physical adapter is operating properly. generalFailure(3) The physical adapter has failed. linkFailure(4) The physical adapter has lost link. Check the cable connections to this adapter. |
| Thermal | CPQHLTH-MIB1.3.6.1.4.1.232.6.2.6.1 | cpqHeThermalCondition Clearing Value = 2 | This value will be one of the following: other(1) Temperature could not be determined. ok(2) The temperature sensor is within normal operating range. degraded(3) The temperature sensor is outside of normal operating range. failed(4) The temperature sensor detects a condition that could permanently damage the system. Note The system automatically shuts down if the failed (4) condition occurs, so it is unlikely that 4 will ever be returned by
                                                         the agent. If the cpqHeThermalDegradedAction is set to shut down (3), the system will shut down if the condition occurs. | Note | The system automatically shuts down if the failed (4) condition occurs, so it is unlikely that 4 will ever be returned by
                                                         the agent. If the cpqHeThermalDegradedAction is set to shut down (3), the system will shut down if the condition occurs. |
| Note | The system automatically shuts down if the failed (4) condition occurs, so it is unlikely that 4 will ever be returned by
                                                         the agent. If the cpqHeThermalDegradedAction is set to shut down (3), the system will shut down if the condition occurs. |
| Power Supply1 | CPQHLTH-MIB1.3.6.1.4.1.232.6.2.9.3.1.5 | cpqHeFltTolPowerSupply Status Clearing Value = 1 | This value will be one of the following: other(1) The status could not be determined or not present. ok(2) The power supply is operating normally. degraded(3) A temperature sensor, fan or other power supply component is outside of normal operating range. failed(4) A power supply component detects a condition that could permanently damage the system. |
| NIC Errors | CPQNIC-MIB1.3.6.1.4.1.232.18.2.3.1.1.16 | cpqNicIfPhysAdapterGood Transmits Clearing Value = <0.5% for 1 hour | Interface is experiencing excessive errors |
| 1.3.6.1.4.1.232.18.2.3.1.1.18 | cpqNicIfPhysAdapterBad  Transmits |
| 1.3.6.1.4.1.232.18.2.3.1.1.17 | cpqNicIfPhysAdapterGood Receives |
| 1.3.6.1.4.1.232.18.2.3.1.1.19 | cpqNicIfPhysAdapterBad Receives |
| NIC Utilization | CPQNIC-MIB1.3.6.1.4.1.232.18.2.3.1.1.16 | cpqNicIfPhysAdapterGood Transmits Clearing Value = <50% for 1 hour | Interface is experiencing High Utilization |
| 1.3.6.1.4.1.232.18.2.3.1.1.18 | cpqNicIfPhysAdapterBad Transmits |
| 1.3.6.1.4.1.232.18.2.3.1.1.17 | cpqNicIfPhysAdapterGood Receives |
| 1.3.6.1.4.1.232.18.2.3.1.1.19 | cpqNicIfPhysAdapterBad Receives |
| Memory Module Trap | 1.3.6.1.4.1.232.6.3 | cpqHe4CorrMemReplace MemModule See CPQHOST-MIB for information on the following trap variables: sysName cpqHoTrapFlags cpqHeResMemBoardIndex cpqHeResMemModuleIndex cpqHeResMemModuleSpare PartNo cpqSiMemModuleSize cpqSiServerSystemId Trap number is 6056 which replaces 6029. | A correctable memory log entry indicates a memory module needs to be replaced. The errors have been corrected, but the memory
                                             module should be replaced. The error information is reported in the variable cpqHeCorrMemErrDesc |
| 78x5-H Insite Manager Service | HOST-RESOURCES-MIB1.3.6.1.2.1.25.4.2.1.2 | cmaeventd | Compaq Insite Manager Service Failure |
|  | cmafcad |
|  | cmahealthd |
|  | cmahostd |
|  | Positive String ID forcmaidad |
|  | cmaided |
|  | cmanicd |
|  | cmapeerd |
|  | cmaperfd |
|  | cmasm2d |
|  | cmastdeqd |
|  | cmathreshd |

| Note | The system automatically shuts down if the failed (4) condition occurs, so it is unlikely that 4 will ever be returned by
                                                         the agent. If the cpqHeThermalDegradedAction is set to shut down (3), the system will shut down if the condition occurs. |
|---|---|

| MIB | OID | Function |
|---|---|---|
| Supported for browsing and system traps |
| INTEL-SERVER-BASEBOARD6 | 1.3.6.1.4.1.343.2.10.3.6.200 | Denotes the power group and describes voltage probes, status, and readings |
| 1.3.6.1.4.1.343.2.10.3.6.300 | Denotes the thermal group and describes cooling devices, fans, and temperature probes |
| 1.3.6.1.4.1.343.2.10.3.6.10 | Denotes the instances of cooling devices |
| 1.3.6.1.4.1.343.2.10.3.6.20 | Denotes the status, reading, and threshold for every cooling device and fan |
| 1.3.6.1.4.1.343.2.10.3.6.30 | Denotes the instances of temperature probes |
| 1.3.6.1.4.1.343.2.10.3.6.40 | Denotes the status, reading, thresholds for every temperature probe |
| 1.3.6.1.4.1.343.2.10.3.6.1000 | Denotes the events group and describes power, thermal, and system events |

| Cisco Unified CM Release 7.x |
|---|
| MCS-78xx Status | MIBS and Object Names | Object Responses |
| Power | INTEL-SERVER-BASEBOARD6::powerEvents |  |
| System | INTEL-SERVER-BASEBOARD6::systemEvents |  |
| Thermal | INTEL-SERVER-BASEBOARD6::thermalEvents |  |