---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-im-presence-service-220186-trou-ca379ba5ae
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-im-presence-service/220186-troubleshoot-missing-drf-components-in-t.html
retrieved_at: 2026-08-16T23:38:35.434872+00:00
---

Troubleshoot Missing DRF Components in the IM&P Server Nodes

# Troubleshoot Missing DRF Components in the IM&P Server Nodes

### Download Options

Updated: February 1, 2023

Document ID: 220186

Contents

## Contents

## Introduction

This document describes how to add missing components in the the Unified Communications Manager IM and Presence (IM&P).

## Background

Missing components from the Unified Communications Manager IM and Presence (IM&P) when Disaster Recovery System (DRS) has missing components, must be found and added.

## Components in IM&P Nodes

The DRS which provides the capability to perform a data backup for all the IM and Presence nodes. Occasionally, due to unexpected internal server errors the IM and Presence nodes can be missing some of the components that cause the DRF backup not to be successful. The IM and Presence nodes must have the these components in order to perform a backup task successfully.

### I M&P Publisher

--------------------------------------------- IM_AND_PRESENCE PLATFORM IM_AND_PRESENCE CLM IM_AND_PRESENCE DB IM_AND_PRESENCE PREFS IM_AND_PRESENCE XCP IM_AND_PRESENCE SYSLOGAGT IM_AND_PRESENCE CDPAGT IM_AND_PRESENCE TCT IM_AND_PRESENCE BAT IM_AND_PRESENCE CUP IM_AND_PRESENCE REPORTER

### IM&P Subscriber

--------------------------------------------- IM_AND_PRESENCE REPORTER IM_AND_PRESENCE CUP IM_AND_PRESENCE PLATFORM IM_AND_PRESENCE CLM IM_AND_PRESENCE XCP IM_AND_PRESENCE CDPAGT IM_AND_PRESENCE TCT IM_AND_PRESENCE SYSLOGAGT

The DRS backs up all of its components automatically when they are all complete, however certain times the IM and Presence nodes can be missing some components and this issue causes the backup process to fail. If that is the case, you can see this error in the DRF logs.

Log File snippet.

=====================================================

Server : IMPSub

Feature : IM_AND_PRESENCE

Component : DB

Time Completed: 2020-08-21-09-29-27

Result Code : 1-Please check the component logs for further details.

Result String : ERROR

=====================================================

prebackup

ready for backup

required space = 9672860

df -k /tmp/db_drf_backup/ | grep -v Filesystem | awk '{print }'

ready for backup

exiting pre_db_backup

Beginning do_db_backup

command to execute /bin/chmod a+w /common/drf/db_drf_backup

command to execute /bin/touch /common/drf/db_drf_backup/drf_ontape_backup.gz

command to execute /bin/chmod 660 /common/drf/db_drf_backup/drf_ontape_backup.gz

command to execute /bin/chown informix:informix /common/drf/db_drf_backup/drf_ontape_backup.gz

Creating Ontape Backup of DB...

command to execute /bin/su - informix -c "ontape -s -L 0 | /bin/gzip > /common/drf/db_drf_backup/drf_ontape_backup.gz" 2>>/common/drf/backup.log

Warning: ONCONFIG /usr/local/cm/db/informix/etc/onconfig.ccm is not owned by user informix (uid=512).

drf_ontape_backup created is of size [28347431]

Ontape Backup completed!

Starting sub backup operation on each sub.

command to execute /usr/local/cm/bin/invoke_sub_backup.py /common/drf/backup.log /common/drf/status.txt

08/21/20 09:29:11 - status file=/common/drf/status.txt

08/21/20 09:29:11 - in subBackup

08/21/20 09:29:11 - pub is impsub1.example.com

08/21/20 09:29:11 - getting Sub node list

08/21/20 09:29:11 - in versionCheckOk

08/21/20 09:29:20 - Good Subscribers are ['impsub1', 'impsub2']

08/21/20 09:29:20 - processing node impsub1

08/21/20 09:29:20 - calling remote procesdure to backup subscriber for node impsub1

08/21/20 09:29:27 - Sub data not found, node impsub1

08/21/20 09:29:27 - after do_sub_backup

08/21/20 09:29:27 – impsub1 sub backup failed

Sub Backup failed.

EXITING!

----> BEGIN Standard Output

----> END Standard Output

----> BEGIN Standard Error

----> END Standard Error

## Missing Components

In order to see if the IM&P components are complete run the the this command  in both nodes through the IM&P CLI .

- utils disaster_recovery show_registration nodename

Where nodename is the IP address of the node or its name.

## List of Commands for Missing Components

If there are missing components in a node it is required to create a root account via CLI to add manually the missing components through the use of the certain commands, each for every missing component. The list shows the commands with their specific path for every component it is required to run the corresponding command for each one of the missing components in the right node:

- REPORTER.

python /usr/local/platform/bin/drfRegisterComponent.py -f IM_AND_PRESENCE -c REPORTER -e /common/drf/scripts/reporter/reporter_error_map.txt -s /common/drf/scripts/reporter/reporter_script.xml -d /common/drf/scripts/reporter/reporter_dependency.xml

- CUP.

python /usr/local/platform/bin/drfRegisterComponent.py -f IM_AND_PRESENCE -c CUP -e /usr/local/sip/drf/epas/bin/epas_error_map.txt -s /usr/local/sip/drf/epas/bin/epas_script.xml -d /usr/local/sip/drf/epas/bin/epas_dependency.xml

- BAT.

python /usr/local/platform/bin/drfRegisterComponent.py -f IM_AND_PRESENCE -c BAT -e /common/drf/scripts/bat/bat_error_map.txt -s /common/drf/scripts/bat/bat_script.xml -d /common/drf/scripts/bat/bat_dependency.xml

- PLATFORM.

python /usr/local/platform/bin/drfRegisterComponent.py  -f IM_AND_PRESENCE -c PLATFORM -e /usr/local/platform/script/platform/platform_error_map.txt -s /usr/local/platform/script/platform/platform_script.xml -d /usr/local/platform/script/platform/platform_dependency.xml

- CLM.

python /usr/local/platform/bin/drfRegisterComponent.py  -f IM_AND_PRESENCE -c CLM -e /usr/local/platform/bin/clm/clm_drf_error_map.txt -s /usr/local/platform/bin/clm/clm_drf_script.xml -d /usr/local/platform/bin/clm/clm_drf_dependency.xml

- XCP.

python /usr/local/platform/bin/drfRegisterComponent.py -f IM_AND_PRESENCE -c XCP -e /usr/local/xcp/drf/cup_xcp_error_map.txt -s /usr/local/xcp/drf/cup_xcp_script.xml -d /usr/local/xcp/drf/cup_xcp_dependency.xml

- TCT.

python /usr/local/platform/bin/drfRegisterComponent.py -f IM_AND_PRESENCE -c TCT -e /usr/local/platform/script/tct/tct_error_map.txt -s /usr/local/platform/script/tct/tct_script.xml -d /usr/local/platform/script/tct/tct_dependency.xml

- PREFS.

python /usr/local/platform/bin/drfRegisterComponent.py -f IM_AND_PRESENCE -c PREFS -e /usr/local/cm/bin/prefsdrf/prefs_error_map.txt -s /usr/local/cm/bin/prefsdrf/prefs_script.xml -d /usr/local/xcp/drf/prefs_dependency.xml

- SYSLOGAGT.

python /usr/local/platform/bin/drfRegisterComponent.py -f IM_AND_PRESENCE -c SYSLOGAGT -e /usr/local/cm/syslogagt/conf/syslogagt_error_map.txt -s /usr/local/cm/syslogagt/conf/syslogagt_script.xml -d /usr/local/cm/syslogagt/conf/syslogagt_dependency.xml

- CDPAGT.

python /usr/local/platform/bin/drfRegisterComponent.py -f IM_AND_PRESENCE -c CDPAGT -e /usr/local/cm/cdpagt/conf/cdpagt_error_map.txt -s /usr/local/cm/cdpagt/conf/cdpagt_script.xml -d /usr/local/cm/cdpagt/conf/cdpagt_dependency.xml

- DB.

python /usr/local/platform/bin/drfRegisterComponent.py -f IM_AND_PRESENCE -c DB -e /usr/local/cm/bin/database_error_map.txt -s /usr/local/cm/bin/database_script.xml -d /usr/local/cm/bin/database_dependency.xml

After the ones that were missing are added, they must be displated after the command runs again.

- utils disaster_recovery show_registration nodename

After the task is complete the IM&P node backup task must start.

## Cisco bug ID CSCuv53092

On the other hand, if there are more components added than expected the DRF backup task fails as well. That is caused by the  Cisco bug ID CSCuv53092 in that case the workaround referred in the defect fixes the issue.

Refer to Cisco bug ID CSCuv53092.

Note : Only registered Cisco users can access internal Cisco tools and bug information.

## Related Information

- Cisco Technical Support & Downloads

### Revision History

1.0

01-Feb-2023

Initial Release

### Contributed by Cisco Engineers

Mario Aguilar Olea

Cisco Technical Consulting Enigneer

### This Document Applies to These Products

- Unified Communications Manager IM & Presence Service

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 01-Feb-2023 | Initial Release |