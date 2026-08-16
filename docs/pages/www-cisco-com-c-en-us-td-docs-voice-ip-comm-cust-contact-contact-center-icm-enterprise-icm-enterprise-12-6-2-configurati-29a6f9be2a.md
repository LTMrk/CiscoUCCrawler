---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-configurati-29a6f9be2a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/configuration/guide/ucce_b_serviceability-guide-for-cisco-unified_12_62/ucce_b_serviceability-guide-for-cisco-unified_12_6_appendix_01101.html
retrieved_at: 2026-08-16T14:41:55.327513+00:00
---

Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(2)

# Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(2)

Updated: April 28, 2023

Chapter: MIB Results Example Appendix

## Chapter: MIB Results Example Appendix

- MIB Results Example Appendix

- Cisco Contact                              	 Center Applications MIB Results Example

# MIB Results Example Appendix

## Cisco Contact
                        	 Center Applications MIB Results Example

The following
                           		example displays the data provided by the Cisco Contact Center Applications MIB
                           		SNMP agent on the target Unified ICM/Unified CCE installation icm70 in response
                           		to a series of SNMP GETNEXT requests beginning at node ciscoCcaMIB, OID
                           		1.3.6.1.4.1.9.9.473.

For the purpose of
                           		example, assume that a single instance cccaInstanceName.2 = acme is installed with instance
                           		number "0" and that the
                           		following components are installed:

```
Router:
    cccaComponentName.instanceNumber(0).componentIndex(1) = RouterA
Logger:
    cccaComponentName.instanceNumber(0).componentIndex(2) = LoggerA
Peripheral Gateway:
    cccaComponentName.instanceNumber(0).componentIndex(3) = PG1A
Distributor Admin Workstation:
    cccaComponentName.instanceNumber(0).componentIndex(4) = Distributor
A single CRSP NIC has been installed as part RouterA:
    cccaNicType.instanceNumber(0).componentIndex(1).nicIndex(1) = crsp
A single Express PIM (acmiCRS) has been installed as part of PG1A:
    cccaPimPeripheralName.instanceNumber(0).componentIndex(3).cccaPimNumber(1) = ACD 1

cccaName.0 = cc-rgr1a
cccaDescription.0 = Cisco Intelligent Contact Management / IP 
cccaVersion.0 = 7.1(1)
cccaTimeZoneName.0 = Eastern Standard Time
cccaTimeZoneOffsetHours.0 = 5
cccaTimeZoneOffsetMinutes.0 = 0
cccaSupportToolsURL.0 = 
cccaInstanceName.0 = acme
cccaComponentType.0.1 = router(1)
cccaComponentType.0.2 = logger(2)
cccaComponentType.0.3 = pg(4)
cccaComponentType.0.4 = distAW(3)
cccaComponentName.0.1 = RouterA
cccaComponentName.0.2 = LoggerA
cccaComponentName.0.3 = PG1A
cccaComponentName.0.4 = Distributor
cccaComponentStatus.0.1 = started(4)
cccaComponentStatus.0.2 = started(4)
cccaComponentStatus.0.3 = started(4)
cccaComponentStatus.0.4 = started(4)
cccaComponentElmtName.0.1.1 = ccagent
cccaComponentElmtName.0.1.2 = crspnic
cccaComponentElmtName.0.1.3 = dbagent
cccaComponentElmtName.0.1.4 = mdsproc
cccaComponentElmtName.0.1.5 = router
cccaComponentElmtName.0.1.6 = rtsvr
cccaComponentElmtName.0.1.7 = testsync
cccaComponentElmtName.0.2.8 = configlogger
cccaComponentElmtName.0.2.9 = csfs
cccaComponentElmtName.0.2.10 = histlogger
cccaComponentElmtName.0.2.11 = recovery
cccaComponentElmtName.0.3.12 = mdsproc
cccaComponentElmtName.0.3.13 = opc
cccaComponentElmtName.0.3.14 = pgagent
cccaComponentElmtName.0.3.15 = acmipim
cccaComponentElmtName.0.3.16 = testsync
cccaComponentElmtName.0.4.17 = configlogger
cccaComponentElmtName.0.4.18 = rtclient
cccaComponentElmtName.0.4.19 = rtdist
cccaComponentElmtName.0.4.20 = updateaw
cccaComponentElmtRunID.0.1.1 = 3336
cccaComponentElmtRunID.0.1.2 = 2992
cccaComponentElmtRunID.0.1.3 = 3600
cccaComponentElmtRunID.0.1.4 = 3920
cccaComponentElmtRunID.0.1.5 = 4040
cccaComponentElmtRunID.0.1.6 = 3532
cccaComponentElmtRunID.0.1.7 = 4100
cccaComponentElmtRunID.0.2.8 = 948
cccaComponentElmtRunID.0.2.9 = 3248
cccaComponentElmtRunID.0.2.10 = 1248
cccaComponentElmtRunID.0.2.11 = 3272
cccaComponentElmtRunID.0.3.12 = 4724
cccaComponentElmtRunID.0.3.13 = 4864
cccaComponentElmtRunID.0.3.14 = 4964
cccaComponentElmtRunID.0.3.15 = 5236
cccaComponentElmtRunID.0.3.16 = 5228
cccaComponentElmtRunID.0.4.17 = 5460
cccaComponentElmtRunID.0.4.18 = 5488
cccaComponentElmtRunID.0.4.19 = 5504
cccaComponentElmtRunID.0.4.20 = 5536
cccaComponentElmtStatus.0.1.1 = active(5)
cccaComponentElmtStatus.0.1.2 = started(4)
cccaComponentElmtStatus.0.1.3 = active(5)
cccaComponentElmtStatus.0.1.4 = active(5)
cccaComponentElmtStatus.0.1.5 = active(5)
cccaComponentElmtStatus.0.1.6 = active(5)
cccaComponentElmtStatus.0.1.7 = active(5)
cccaComponentElmtStatus.0.2.8 = active(5)
cccaComponentElmtStatus.0.2.9 = active(5)
cccaComponentElmtStatus.0.2.10 = active(5)
cccaComponentElmtStatus.0.2.11 = active(5)
cccaComponentElmtStatus.0.3.12 = active(5)
cccaComponentElmtStatus.0.3.13 = active(5)
cccaComponentElmtStatus.0.3.14 = active(5)
cccaComponentElmtStatus.0.3.15 = standby(6)
cccaComponentElmtStatus.0.3.16 = active(5)
cccaComponentElmtStatus.0.4.17 = active(5)
cccaComponentElmtStatus.0.4.18 = active(5)
cccaComponentElmtStatus.0.4.19 = active(5)
cccaComponentElmtStatus.0.4.20 = active(5)
cccaRouterSide.0.1 = sideA(1)
cccaRouterCallsPerSec.0.1 = 0
cccaRouterAgentsLoggedOn.0.1 = 0
cccaRouterCallsInProgress.0.1 = 0
cccaRouterDuplexPairName.0.1 = cc-rgr1a
cccaRouterNicCount.0.1 = 1
cccaNicType.0.1.1 = crsp(5)
cccaNicStatus.0.1.1 = started(4)
cccaLoggerSide.0.2 = sideA(1)
cccaLoggerType.0.2 = standard(1)
cccaLoggerRouterSideAName.0.2 = cc-rgr1a
cccaLoggerRouterSideBName.0.2 = cc-rgr1a
cccaLoggerDuplexPairName.0.2 = cc-rgr1a
cccaLoggerHDSReplication.0.2 = 0
cccaDistAwSide.0.4 = sideA(1)
cccaDistAwType.0.4 = standard(0)
cccaDistAwAdminSiteName.0.4 = cc-rgr1a
cccaDistAwRouterSideAName.0.4 = cc-rgr1a
cccaDistAwRouterSideBName.0.4 = cc-rgr1a
cccaDistAwLoggerSideAName.0.4 = cc-rgr1a
cccaDistAwLoggerSideBName.0.4 = cc-rgr1a
cccaDistAwDuplexPairName.0.4 = cc-rgr1a
cccaDistAwHDSEnabled.0.4 = 0
cccaDistAwWebViewEnabled.0.4 = false(2)
cccaDistAwWebViewServerName.0.4 = 
cccaPgNumber.0.3 = 1
cccaPgSide.0.3 = sideA(1)
cccaPgRouterSideAName.0.3 = cc-rgr1a
cccaPgRouterSideBName.0.3 = cc-rgr1a
cccaPgDuplexPairName.0.3 = cc-rgr1a
cccaPgPimCount.0.3 = 1
cccaPimPeripheralName.0.3.1 = ACD 1
cccaPimPeripheralType.0.3.1 = acmiCRS(19)
cccaPimStatus.0.3.1 = started(4)
cccaPimPeripheralHostName.0.3.1 = LabHost
```

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )