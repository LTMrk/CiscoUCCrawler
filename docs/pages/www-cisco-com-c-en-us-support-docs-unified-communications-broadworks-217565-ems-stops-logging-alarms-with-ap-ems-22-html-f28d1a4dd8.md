---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-217565-ems-stops-logging-alarms-with-ap-ems-22-html-f28d1a4dd8
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks/217565-ems-stops-logging-alarms-with-ap-ems-22.html
retrieved_at: 2026-09-07T13:03:23.269386+00:00
---

EMS stops logging alarms with AP.ems.22.0.1123.ap362164 workaround

# EMS stops logging alarms with AP.ems.22.0.1123.ap362164 workaround

### Download Options

Updated: November 17, 2021

Document ID: 217565

Contents

## Contents

AP.ems.22.0.1123.ap362164, removes:

Third-party software is refreshed and cleaned up. It causes the following functional changes:

- CMS is no longer supported. CMS migration step is therefore removed from the User Migration tool.

- PDF report is no longer available for Centralized License Reporting.

- Health Status functionality is removed.

However...

when health statistic get polled for an existing node and the Event Filter is invoked to update/save the statistic in the DB. Since ap362164 removes Health Status functionality thus its code, the method that updates the health stat in the DB does not exists anymore causing the following exception that is logged in

/var/broadworks/logs/emsBackEnd/stderr.txt file:

```
[14 Mar 2019 06:19:46:837] SYS_ERR: Exception running task: java.lang.NoSuchMethodError: com.broadsoft.ems.health.BWPolledDataHealthUtil.updatePolledDataHealth(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;IJI)Z [14 Mar 2019 06:19:46:847] SYS_ERR: java.lang.NoSuchMethodError: com.broadsoft.ems.health.BWPolledDataHealthUtil.updatePolledDataHealth(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;IJI)Z [14 Mar 2019 06:19:46:847] SYS_ERR:     at com.broadsoft.ems.fault.BWEventFilterForHealth.filter(BWEventFilterForHealth.java:118) [14 Mar 2019 06:19:46:847] SYS_ERR:     at com.adventnet.nms.eventdb.UserFilter.runAction(UserFilter.java:73) [14 Mar 2019 06:19:46:847] SYS_ERR:     at com.adventnet.nms.eventdb.EventFilter.doFilter(EventFilter.java:197) [14 Mar 2019 06:19:46:847] SYS_ERR:     at com.adventnet.nms.eventdb.EventMgr.moveToOutQ(EventMgr.java:977) [14 Mar 2019 06:19:46:847] SYS_ERR:     at com.adventnet.nms.eventdb.EventMgr.run(EventMgr.java:859) [14 Mar 2019 06:19:46:847] SYS_ERR:     at com.adventnet.management.scheduler.WorkerThread.run(WorkerThread.java:70)
```

After this uncaught exception, Alarm Report task doesn't work anymore.

Note that for nodes that are added after ap362164 is applied, there's no such problem since no Health polled data are created for the nodes

From the EMS, go to Admin tab->Event Filters, click on delete button of "BWEventFilterForHealth". Then do "restartbw" or just "restartbw EMSBackEnd" should be enough too.

By removing BWEventFilterForHealth from the event filter list, it won't be invoked by Event Filtering which is ok since Health Status is not supported anymore with ap362164.

Note that if for some reason the customer wants to remove ap362164 and go back to previous behavior, they need to manually add back the BWEventFilterForHealth (Admin tab->Event Filters->Add Filter). And then use Admin tab->Event Filters->Save Filters to put the event filters at the same order as before it was deleted (the listed order is the invoked order of the filters). Again "restartbw EMSBackEnd" is required after that.

Workaround tested by dev (Hang Tran) and also by TAC (Tania Hernandez)

### Revision History

2.0

17-Nov-2021

Initial Release

1.0

17-Nov-2021

Initial Release

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- BroadWorks

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 17-Nov-2021 | Initial Release |
| 1.0 | 17-Nov-2021 | Initial Release |