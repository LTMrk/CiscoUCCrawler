---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-configurati-60db271d27
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/configuration/guide/ucce_b_serviceability-guide-for-cisco-unified-icm-contact-center-enterprise-release-15-0/mib_results_example.html
retrieved_at: 2026-08-16T14:37:43.564314+00:00
---

Serviceability Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Serviceability Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: April 30, 2025

Chapter: MIB Results Example Appendix

## Chapter: MIB Results Example Appendix

- MIB Results Example Appendix

- Cisco Contact                              	 Center Applications MIB Results Example

# MIB Results Example Appendix

## Cisco Contact
                        	 Center Applications MIB Results Example

The following example displays the data provided by the Cisco Contact Center Applications MIB SNMP agent on the target Unified
                           CCE installation icm70 in response to a series of SNMP GETNEXT requests beginning at node ciscoCcaMIB, OID 1.3.6.1.4.1.9.9.473.

For the purpose of example, assume that a single instance cccaInstanceName.2 = ucce is installed with instance number "0" and that the following components are installed:

```
Router:
    cccaComponentName.instanceNumber(0).componentIndex(1) = RouterA
Logger:
    cccaComponentName.instanceNumber(0).componentIndex(2) = LoggerA
Campaign Manager:
    cccaComponentName.instanceNumber(0).componentIndex(3) = CampaignManager

cccaName.0 = uccergr100a.stooges.icm
cccaDescription.0 = Cisco Intelligent Contact Management / Contact Center Enterprise
cccaVersion.0 = 15.0
cccaTimeZoneName.0 = Coordinated Universal Time
cccaTimeZoneOffsetHours.0 = 0
cccaTimeZoneOffsetMinutes.0 = 0
cccaSupportToolsURL.0 = 
cccaWebSetupURL.0 = https://uccergr100a/setup
cccaNotificationsEnabled.0 = true (1)
cccaInstanceName.0 = ucce
cccaComponentType.0.1 = router (1)
cccaComponentType.0.2 = logger (2)
cccaComponentType.0.3 = campaign (7)
cccaComponentName.0.1 = RouterA
cccaComponentName.0.2 = LoggerA
cccaComponentName.0.3 = CampaignManager
cccaComponentStatus.0.1 = started (4)
cccaComponentStatus.0.2 = started (4)
cccaComponentStatus.0.3 = active (5)
cccaComponentElmtName.0.1.1 = appgw
cccaComponentElmtName.0.1.2 = ccagent
cccaComponentElmtName.0.1.3 = dbagent
cccaComponentElmtName.0.1.4 = dbworker
cccaComponentElmtName.0.1.5 = mdsproc
cccaComponentElmtName.0.1.6 = router
cccaComponentElmtName.0.1.7 = rtsvr
cccaComponentElmtName.0.1.8 = testsync
cccaComponentElmtName.0.2.9 = configlogger
cccaComponentElmtName.0.2.10 = csfs
cccaComponentElmtName.0.2.11 = cw2kfeed
cccaComponentElmtName.0.2.12 = histlogger
cccaComponentElmtName.0.2.13 = recovery
cccaComponentElmtName.0.2.14 = replication
cccaComponentElmtName.0.3.15 = baimport
cccaComponentElmtName.0.3.16 = campaignmanager
cccaComponentElmtRunID.0.1.1 = 9928
cccaComponentElmtRunID.0.1.2 = 2600
cccaComponentElmtRunID.0.1.3 = 6352
cccaComponentElmtRunID.0.1.4 = 5992
cccaComponentElmtRunID.0.1.5 = 1448
cccaComponentElmtRunID.0.1.6 = 1264
cccaComponentElmtRunID.0.1.7 = 6268
cccaComponentElmtRunID.0.1.8 = 8072
cccaComponentElmtRunID.0.2.9 = 9056
cccaComponentElmtRunID.0.2.10 = 5988
cccaComponentElmtRunID.0.2.11 = 9356
cccaComponentElmtRunID.0.2.12 = 4456
cccaComponentElmtRunID.0.2.13 = 2568
cccaComponentElmtRunID.0.2.14 = 4568
cccaComponentElmtRunID.0.3.15 = 7712
cccaComponentElmtRunID.0.3.16 = 5848
cccaComponentElmtStatus.0.1.1 = active (5)
cccaComponentElmtStatus.0.1.2 = active (5)
cccaComponentElmtStatus.0.1.3 = active (5)
cccaComponentElmtStatus.0.1.4 = active (5)
cccaComponentElmtStatus.0.1.5 = active (5)
cccaComponentElmtStatus.0.1.6 = active (5)
cccaComponentElmtStatus.0.1.7 = active (5)
cccaComponentElmtStatus.0.1.8 = active (5)
cccaComponentElmtStatus.0.2.9 = active (5)
cccaComponentElmtStatus.0.2.10 = active (5)
cccaComponentElmtStatus.0.2.11 = active (5)
cccaComponentElmtStatus.0.2.12 = active (5)
cccaComponentElmtStatus.0.2.13 = active (5)
cccaComponentElmtStatus.0.2.14 = active (5)
cccaComponentElmtStatus.0.3.15 = active (5)
cccaComponentElmtStatus.0.3.16 = active (5)
cccaRouterSide.0.1 = sideA (1)
cccaRouterCallsPerSec.0.1 = 0
cccaRouterAgentsLoggedOn.0.1 = 0
cccaRouterCallsInProgress.0.1 = 0
cccaRouterDuplexPairName.0.1 = uccergr100b
cccaRouterNicCount.0.1 = 0
cccaRouterPGsEnabledCount.0.1 = 4
cccaRouterCallsInQueue.0.1 = 0
cccaRouterAppGwEnabled.0.1 = true (1)
cccaRouterDBWorkerEnabled.0.1 = true (1)
cccaRouterPublicHighAddr.0.1 = uccergr100a
cccaRouterPublicNonHighAddr.0.1 = uccergr100a
cccaRouterPrivateHighAddr.0.1 = uccergr100ap
cccaRouterPrivateNonHighAddr.0.1 = uccergr100ap
cccaLoggerSide.0.2 = sideA (1)
cccaLoggerType.0.2 = standard (1)
cccaLoggerRouterSideAName.0.2 = uccergr100ap
cccaLoggerRouterSideBName.0.2 = uccergr100bp
cccaLoggerDuplexPairName.0.2 = uccergr100bp
cccaLoggerHDSReplication.0.2 = true (1)
cccaLoggerAvgDBWriteTime.0.2 = 0
cccaCampaignMgrDbUtilization.0.3 = 1
cccaCampaignMgrQueueDepth.0.3 = 0
cccaCampaignMgrAvgQueueTime.0.3 = 0
cccaCampaignMgrActiveDialers.0.3 = 1
```

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )