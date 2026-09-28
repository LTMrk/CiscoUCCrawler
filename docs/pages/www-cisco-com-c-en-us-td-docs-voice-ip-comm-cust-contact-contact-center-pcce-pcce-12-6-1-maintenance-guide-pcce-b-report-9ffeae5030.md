---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-maintenance-guide-pcce-b-report-9ffeae5030
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/maintenance/guide/pcce_b_Reporting-User-Guide-12_6_1/pcce_b_cisco-packaged-contact-center-enterprise_chapter_010000.html
retrieved_at: 2026-08-21T16:56:36.686329+00:00
---

Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.6(1)

Updated: May 10, 2021

Chapter: Missing Data

## Chapter: Missing Data

- Missing Data

- Temporarily                              	 Missing Data

- Permanently                              	 Missing Data

# Missing Data

## Temporarily
                        	 Missing Data

If your
                           		configuration includes an external HDS, you may notice that you are missing
                           		records from reports during the Logger recovery process.

If the Logger
                           		connected to the external HDS goes offline, the external HDS does not connect
                           		to a different Logger. For example, if the external HDS is connected to Logger
                           		A and Logger A fails, the HDS does not connect to Logger B. When Logger A comes
                           		back up, it recovers data from Logger B and begins to receive current
                           		historical information. After Logger A has recovered all of the data from
                           		Logger B, it replicates this data to the external HDS.

If reports are run
                           		from the external HDS for recent intervals while Logger A is offline or while
                           		the Logger is in the process of recovering or replicating data, you might not
                           		see data for those intervals in reports. These records are missing only
                           		temporarily; you will see the data after the replication process for the tables
                           		used by the reports is complete.

If your deployment
                                       		  does not include an external HDS and Logger A goes offline, you will not see
                                       		  report data from the interval during which Logger A was offline until Logger A
                                       		  has recovered that data from Logger B.

## Permanently
                        	 Missing Data

The Packaged CCE
                           		Logger retention settings and database size are configured to ensure sufficient
                           		database space for the data. In the unlikely event that the Logger's Central
                           		Database becomes full or reaches a configured threshold size, Packaged CCE
                           		frees up database space by running an emergency purge on historical database
                           		tables.

The emergency purge
                           		goes through each historical table in a predefined order one at a time and
                           		purges one hour's worth of data from the table, looping through the tables if
                           		necessary. As data is purged from each historical table, a check is made to
                           		verify if the free space is more than the minimum threshold value. Once
                           		adequate space has been recovered, the emergency purge procedure stops.

| Note | If your deployment
                                       		  does not include an external HDS and Logger A goes offline, you will not see
                                       		  report data from the interval during which Logger A was offline until Logger A
                                       		  has recovered that data from Logger B. |
|---|---|