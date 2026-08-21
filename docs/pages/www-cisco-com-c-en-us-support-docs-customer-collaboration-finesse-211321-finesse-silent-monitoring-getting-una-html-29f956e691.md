---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-finesse-211321-finesse-silent-monitoring-getting-una-html-29f956e691
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/finesse/211321-Finesse-Silent-Monitoring-Getting-Una.html
retrieved_at: 2026-08-21T06:42:58.426219+00:00
---

Error "Unable to Silent Monitor at this time (CTIError=Generic Error)" Occurs in Finesse Silent Monitoring

# Error "Unable to Silent Monitor at this time (CTIError=Generic Error)" Occurs in Finesse Silent Monitoring

Updated: June 5, 2017

Document ID: 211321

Contents

## Contents

## Introduction

This document describes a solution for the Cisco Finesse problem when a supervisor is not able to silent monitor an agent.

## Problem

When you try to use the Silent Monitoring feature, Finesse Supervisor gets an error; "Unable to Silent Monitor at this time (CTIError=Generic Error)".

The most common cause of this issue is that Monitoring Calling Search Space (CSS) on the supervisor line does not have the priviledge to monitor the agent line.

## Solution

These SQL queries allow you to check if the supervisor has the privilege to monitor the agent line.

In this example, the agent has directory number (DN) 1011 in partition global_pt and the supervisor has DN 1012 in partition supervisor_pt with monitoring CSS supervisor_css .

1. Get the agent line and partition details.

```
admin: run sql SELECT d.pkid devid,d.name mac,n.dnorpattern number,rp.name pt,d.allowcticontrolflag ction, ts.name bib FROM devicenumplanmap dnm INNER JOIN device d ON d.pkid=dnm.fkdevice INNER JOIN numplan n ON n.pkid=dnm.fknumplan INNER JOIN typestatus ts ON ts.enum==d.tkstatus_builtinbridge LEFT JOIN routepartition rp ON rp.pkid=n.fkroutepartition WHERE n.dnorpattern='1011' devid                                mac             number pt       ction bib ==================================== =============== ====== ======== ===== === 7d416919-fab9-4807-bcc0-61c4bbc28c49 SEPC80084AA8721 1011 agent_pt t     On
```

2. Get the supervisor line and monitoring CSS details.

```
admin: run sql SELECT d.pkid devid,d.name mac,n.dnorpattern number,rp.name svisor_line_pt,css.name svisor_monitoring_css FROM devicenumplanmap dnm INNER JOIN device d ON d.pkid=dnm.fkdevice INNER JOIN numplan n ON n.pkid=dnm.fknumplan LEFT JOIN routepartition rp ON rp.pkid=n.fkroutepartition LEFT JOIN callingsearchspace css ON css.pkid==dnm.fkcallingsearchspace_monitoring WHERE n.dnorpattern='1012' devid                                mac             number svisor_line_pt svisor_monitoring_css ==================================== =============== ====== ============== ===================== 2633e474-b883-4cbe-8f07-3a7dddd4f7bc SEP005056996F7E 1012 supervisor_pt supervisor_css
```

3. Verify if the agent's partition is present in the supervisors monitoring CSS.

```
admin: run sql SELECT pkid,name,clause FROM callingsearchspace WHERE name='supervisor_css' pkid                                 name           clause ==================================== ============== ===================== 29b204f6-cc9e-4b39-58eb-cc093c91f6d3 supervisor_css agent_pt :p1:global_pt
```

The column clause has ordered a list of partitions that belong to a specific CSS. In the example supervisor_css , it has three partitions in the this order: agent_pt , p1 , global_pt .

In the non-working scenario, agent's line partition will be missing the clause line, so you need to add it in order to make the silent monitoring feature to work.

### Revision History

1.0

05-Jun-2017

Initial Release

### Contributed by Cisco Engineers

Alexander Levichev

Cisco TAC Engineer

### This Document Applies to These Products

- Finesse

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 05-Jun-2017 | Initial Release |