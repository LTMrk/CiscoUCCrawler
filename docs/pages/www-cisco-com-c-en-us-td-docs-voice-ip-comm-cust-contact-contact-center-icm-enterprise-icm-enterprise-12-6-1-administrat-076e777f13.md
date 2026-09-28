---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-administrat-076e777f13
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/administration/guide/ucce_b_administration-guide-for-cisco-unified_1261/ucce-m-change-limits-for-calls-per-second.html
retrieved_at: 2026-08-16T20:47:11.649652+00:00
---

Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.6(1)

# Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.6(1)

Updated: May 14, 2021

Chapter: Appendix

## Chapter: Appendix

- Appendix

- Change Limits for Calls Per Second to Support 36000 Agents

# Appendix

## Change Limits for Calls Per Second to Support 36000 Agents

Each Unified CCE instance database contains Configuration Limit scalability records. Supporting up to 36000 active agents
                              requires the modification of the following records:

Call Per Second rate

Deployment Max CPS

You can change the values for these records using the Configuration Limit tool, which modifies the Configuration_Limit Database
                              table.

The Configuration Limit tool is a command-line utility tool from the bin directory of all Unified ICM and Unified CCE Administration
                              & Data Servers. You must have privileges for the Setup or Config Groups in the Active Directory for the chosen Unified CCE
                              instance.

Using the Configuration Limit tool, you can only change the ConfigLimitCurrentValue. You cannot change the ConfigLimitDefaultValue.

Step 1

In the Windows Run dialog, type configlimit , and then click Enter .

Run the Configuration Limit tool on the same machine as the Distributor for the instance that you want to configure. If there
                                                      are several instances of the Administration & Data Server on the Distributor machine, use the Select Administration Server
                                                      tool to select the instance to configure.

Step 2

To view currently configured parameter limits, run the following command: cl /show

Step 3

To change the calls per second limit, run a command in the following format: cl /id [ConfigLimitID] /value [ConfigLimitCurrentValue][/update]

Where

ConfigLimitID valid values are:

12—CPS_CAPACITY

14—DEPLOYMENT_MAX_CAPACITY

ConfigLimitCurrentValue is the parameter limit.

To set the maximum supported Calls per Second capacity support for congestion control: cl /id 12 /value 310 /update

To set the maximum supported Calls per Second for this Deployment Type: cl /id 14 /value 310 /update

| Note | Using the Configuration Limit tool, you can only change the ConfigLimitCurrentValue. You cannot change the ConfigLimitDefaultValue. |
|---|---|

| Step 1 | In the Windows Run dialog, type configlimit , and then click Enter . Note Run the Configuration Limit tool on the same machine as the Distributor for the instance that you want to configure. If there
                                                      are several instances of the Administration & Data Server on the Distributor machine, use the Select Administration Server
                                                      tool to select the instance to configure. | Note | Run the Configuration Limit tool on the same machine as the Distributor for the instance that you want to configure. If there
                                                      are several instances of the Administration & Data Server on the Distributor machine, use the Select Administration Server
                                                      tool to select the instance to configure. |
|---|---|---|---|
| Note | Run the Configuration Limit tool on the same machine as the Distributor for the instance that you want to configure. If there
                                                      are several instances of the Administration & Data Server on the Distributor machine, use the Select Administration Server
                                                      tool to select the instance to configure. |
| Step 2 | To view currently configured parameter limits, run the following command: cl /show |
| Step 3 | To change the calls per second limit, run a command in the following format: cl /id [ConfigLimitID] /value [ConfigLimitCurrentValue][/update] Where ConfigLimitID valid values are: 12—CPS_CAPACITY 14—DEPLOYMENT_MAX_CAPACITY ConfigLimitCurrentValue is the parameter limit. To set the maximum supported Calls per Second capacity support for congestion control: cl /id 12 /value 310 /update To set the maximum supported Calls per Second for this Deployment Type: cl /id 14 /value 310 /update |

| Note | Run the Configuration Limit tool on the same machine as the Distributor for the instance that you want to configure. If there
                                                      are several instances of the Administration & Data Server on the Distributor machine, use the Select Administration Server
                                                      tool to select the instance to configure. |
|---|---|