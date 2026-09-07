---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-217564-cap-needs-to-be-disabled-post-22-0-upgra-htm-0f3c55564e
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks/217564-cap-needs-to-be-disabled-post-22-0-upgra.html
retrieved_at: 2026-09-07T13:02:24.669439+00:00
---

CAP Needs to be Disabled Post 22.0 Upgrade on all Servers to Prevent OCS Errors

# CAP Needs to be Disabled Post 22.0 Upgrade on all Servers to Prevent OCS Errors

### Download Options

Updated: May 10, 2019

Document ID: 217564

Contents

## Contents

### Introduction

The Client Application Protocol (CAP) interface has been removed from Release 22.0. CAP is no longer supported in 22.0 and up and thus this must be disabled post upgrade to 22.0 to prevent connection attempt and OCS errors, illustrated by alarms such as “A CAP connection has been terminated between the Open Client Server and Application Server 1.2.3.4” or bwOpenClientServerASConnFailed".

After upgrading the Application Server and Xtended Services Platform to 22.0 there may be CAP alarms displayed on both the AS and XSP.

```
XSP_CLI/Monitoring/Alarm/AlarmsTable> list Identifier Timestamp Alarm Name Severity Correlation Parameter ======================================================================================================= 66414 2017-11-12 8:58:55 GMT bwOpenClientServerASConnFailed Critical 10;37;CAP;10.123.123.80; 66415 2017-11-12 8:58:55 GMT bwOpenClientServerASConnFailed Critical 10;37;CAP;10.123.123.10;
```

### Resolution

Disable the CAPProxy on all deployed servers as this is no longer supported in 22.0. It is recommended to do this in the same maintenance window as the upgrade.

```
XSP_CLI/Applications/OpenClientServer/CAPProxy> get enabled = true serverPort = 2206 numConnections = 1 XSP_CLI/Applications/OpenClientServer/CAPProxy> set enabled false *** Warning: BroadWorks needs to be restarted for the changes to take effect ***
```

After the change has been applied the server will require OpenClientServer to be restarted. If CAPProxy is disabled prior to the upgrade OpenClientServer does not need to be restarted as it will be restarted during the upgrade.

```
$ restartbw OpenClientServer
```

### Documentation

Alert #20181031

End Of Maintenance notice in section 2.24 of the 22.0 release notes

### Revision History

2.0

10-May-2019

Initial Release

1.0

16-Nov-2021

Initial Release

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- BroadWorks

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 10-May-2019 | Initial Release |
| 1.0 | 16-Nov-2021 | Initial Release |