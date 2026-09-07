---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-216793-why-there-is-a-disparity-between-the-per-htm-8a9abd1db5
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks/216793-why-there-is-a-disparity-between-the-per.html
retrieved_at: 2026-09-07T13:02:45.220826+00:00
---

Why there is a disparity between the performance measurement bwNumberOfUsers and User License Count?

# Why there is a disparity between the performance measurement bwNumberOfUsers and User License Count?

### Download Options

Updated: November 12, 2020

Document ID: 216793

Contents

## Contents

The License User count is specific to the number of User Licenses consumed, while the total number of users (shown by the counter byNumberOfUsers) is greater than just consumption of User licenses. Users that do not consume User licenses are Virtual Users (Attendant Console, Call Center, Hunt Group, GroupCall, etc...) and TrunkGroup Users, hence the mismatch between the two values.

Please refer to section \"10.1.1.4 Provisioned Users\" of the System Engineering Guide for details. /php/xchange/node/422649

Example: AS_CLI/Monitoring/PM/Execution> get -f bwNumberOfUsers Label       = bwNumberOfUsers Description = \"Gives the total of users configured on the BroadWorks system\"Object ID   = .1.3.6.1.4.1.6431.1.2.16.1.2.0 Access      = ReadOnly Value = 390

AS_CLI/System/Licensing> get ... Subscriber Licenses: Name   Licensed  Used  Available ========================================= User License      50000   141      49859 Relevant statistics related to License User count are: - bwNumberOfLicensedUsers: the number of licensed users on the BroadWorks system (equal to user license numbers that the \"AS_CLI/System/Licensing> get\" command provides) - bwNumberOfNonVirtualUsers: the number of actual users - excluding virtual users - on the BroadWorks system

NOTE bwNumberOfLicensedUsers = bwNumberOfNonVirtualUsers – trunk group users. TG users are visible via AS_CLI/System/Licensing> get .... Total Number of Trunk Users = 18 ... Finally the \"Service License Reporting Tool\" represents a valid source to track the license use on the BroadWorks system. The Feature Description document of this tool is available on Xchange at: /php/xchange/node/416300

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- BroadWorks