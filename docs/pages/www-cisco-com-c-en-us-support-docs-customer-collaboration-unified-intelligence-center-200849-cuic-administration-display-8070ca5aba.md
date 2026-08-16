---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-intelligence-center-200849-cuic-administration-display-8070ca5aba
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-intelligence-center/200849-CUIC-Administration-Display-Unknown-St.html
retrieved_at: 2026-08-16T19:25:09.152767+00:00
---

CUIC Administration Display "Unknown" Status for All Nodes in the Control Center Page

# CUIC Administration Display "Unknown" Status for All Nodes in the Control Center Page

Updated: November 10, 2016

Document ID: 200849

Contents

## Contents

## Introduction

In Cisco Unified Intelligence Center (CUIC) the cluster nodes are displayed with a misleading “Unknown” status.

## Problem

In the CUIC Administrator under Control Center -> Device Center tab check nodes status.

Download catalina.out logs using the following command.

```
admin: file get activelog tomcat/logs/catalina*
```

Find the following error messages in the catalina.log file.

com.cisco.ccbu.oamp.omgr.wsm.WSMConnectionException: Fatal transport error: sun.security.validator.ValidatorException: No trusted certificate found at com.cisco.ccbu.oamp.omgr.wsm.WSMRequest.sendRequest(WSMRequest.java:167) at com.cisco.ccbu.oamp.omgr.wsm.status.HttpStatusRequestManager$HttpStatusRequestWorker.run(HttpStatusRequestManager.java:95)

com.cisco.ccbu.oamp.omgr.wsm.WSMConnectionException: Fatal transport error: sun.security.validator.ValidatorException: No trusted certificate found at com.cisco.ccbu.oamp.omgr.wsm.WSMRequest.sendRequest(WSMRequest.java:167) at com.cisco.ccbu.oamp.omgr.wsm.status.HttpServmStatusRequestManager$HttpServmStatusRequestWorker.run(HttpServmStatusRequestManager.java:90)

## Solution

In case of self-signed certificates - regenerate Tomcat certificate and restart "Cisco Tomcat" service.

```
admin: set cert regen tomcat admin: utils service restart Cisco Tomcat
```

As for CA signed certificates - they need to be regenarated according to the procedure.

UCCE: Obtain and Upload CA Signed Certificate

Ensure that all the certificates from the chain are uploaded in the correct order starting from the root.

## Related Defects

CSCua46681 OAMP device control shows CUIC status as UNKNOWN 9.0(1) CSCua47572 OAMP welcome page shows application & system version as unknown 9.0(1) CSCun82152 Dataset status is unknown caused by open ended scheduled reports 8.x, 9.x, 10.0 CSCur39984 CUIC reports failing with "Dataset Status is Unknown" error message 10.5(1),9.1(1) CSCuy08053 Database Status Is Unknown 10.6(1) CSCuu10923 Control center buttons are disabled (e.g. Start, Shutdown, Restart) 10.5.1, 11.0

### Revision History

1.0

10-Nov-2016

Initial Release

### Contributed by Cisco Engineers

Hariharan Swaminathan

Cisco Engineering

Alexander Levichev

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Intelligence Center

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 10-Nov-2016 | Initial Release |