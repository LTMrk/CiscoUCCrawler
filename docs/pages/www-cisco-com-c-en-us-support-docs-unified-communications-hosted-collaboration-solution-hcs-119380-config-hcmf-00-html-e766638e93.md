---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-hosted-collaboration-solution-hcs-119380-config-hcmf-00-html-e766638e93
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/hosted-collaboration-solution-hcs/119380-config-hcmf-00.html
retrieved_at: 2026-09-01T14:58:30.942768+00:00
---

Configure HCM-F Service Inventory Report

# Configure HCM-F Service Inventory Report

### Download Options

Updated: February 10, 2016

Document ID: 1455123994667236

Contents

## Contents

## Introduction

This document describes how the Service Inventory (SI) reports are created in a Hosted Collaboration Solution (HCS) 9.2.1 deployment and the interactions between Cisco Hosted Collaboration Mediation Fulfillment (HCM-F) Service inventory and Cisco Unified Communications Domain Manager (CUCDM) 8.1.X during this process.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on these software and hardware versions:

- CUCDM 8.1.X

- HCM-F 9.2.1

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

Cisco HCS SI is an application that provides reports for service providers for billing purposes. These reports contain data on customers, subscribers, devices, and other details that are currently provisioned on CUCDM. In addition, SI can generate reports directly from Cisco Unified Communications Manager and Cisco Unity Connection application servers for customers that are provisioned in Cisco HCM-F that do not have a CUCDM configured. SI automatically transfers the report files at regular configurable intervals to remote SFTP servers. The service providers use these reports in order to generate billing records for their customers.

### Workflow

- SI reports are scheduled and configured via Service Inventory Configuration by the administrator.

- Based on a set schedule, the SI web service submits a Simple Object Access Protocol (SOAP) request to CUCDM.

- CUCDM receives this SOAP request and triggers a transaction in order to create service inventory related data and CUCDM sends this data to HCM-F SI via SFTP.

- SI sees the new file(s), decompresses the file(s), and processes the file(s).

- SI eventually outputs a .si file(s).

- SI creates backup copies of all files, which includes .si, for later retrieval and field support if necessary.

- SI transfers the .si file(s) to the SFTP host(s) as configured in the GUI.

#### Prerequisites

HCM-F and CUCDM must be installed and configured. These services must be activated and started on HCM-F:

- Cisco CDM Database

- Cisco Tomcat

- Cisco HCS SI UI

Use Cisco HCS North Bound Interface Web Service, if you plan to configure SI through the SI administrative interface. Use Cisco HCS Fulfillment Service, if you plan to configure SI through the Cisco HCM-F NBI. Ensure that Cisco HCS CUCDMSync Service is running if you plan to run Cisco HCS CUCDMSync Service. Use Cisco HCS Provisioning Adapter Service so that automatic synchronization can propagate CUCDM data to the Shared Data Repository. SI obtains the connection data for CUCDM from the Shared Data Repository. The Cisco HCS Provisioning Adapter Service provisions credentials and SNMP information, as well as provisions remote Syslog data on Cisco Unified Communications Manager devices.

Services required differ between a CUCDM report and a supported UC Application report.

For CUCDM reports, you need these services:

- Cisco HCS Provisioning Adapter Service

- Cisco Tomcat

- Cisco HCS Service Inventory

- Cisco HCS SI UI

- Cisco CDM Database

- Cisco HCS Fulfillment Service

- Cisco HCS CUCDMSync Service

- Cisco HCS UCSMSync Service

- Cisco HCS VCenterSync Service

For supported UC Applications reports, you need these services:

- Cisco HCS Provisioning Adapter Service

- Cisco Tomcat

- Cisco HCS Service Inventory

- Cisco HCS SI UI

- Cisco CDM Database

Webservices must be activated and started on CUCDM 8.1.X.

```
=>[webservices] #
```

```
show
```

```
|OPTION |VALUE |DESCRIPTION | |------ |----- |----------- | |Enabled |True |Enable Webservice | |8.1.0 |True |Enable version 8.1.0 webservices interface | |8.0.0 |False |Enable version 8.0.0 compatible webservices interface |
```

## Configure

Note : Use the Command Lookup Tool ( registered customers only) in order to obtain more information on the commands used in this section.

Ensure that you have added CUCDM as a management application instance in HCM-F. This is because HCM-F Service Inventory relies on data from CUCDM in order to generate SI reports, hence it needs to be added.

In order to do so, choose Infastructure Manager > Management Network > Management Application > Add New .

When you integrate with a CUCDM version earlier than 8.1.2, the API version must be set to 8.0. The API version can be set to either 8.0 or 8.1 when you integrate with CUCDM 8.1.2 or later. Also, note that if the 8.0 API version is configured, SIP trunks will not be synced and only the location name will be synced for Customer Location.

- Port - The port defaults to 8181. This is the SOAP port that is used by SI in order to send the first SOAP message to CUCDM.

- Credentials - Choose the credential Type ADMIN and provide a User ID (in this case hcmf). This user is used to access CUCDM.

Note : This user also needs to exist in CUCDM with the same password. In order to check this, from the CUCDM GUI choose General Administration > Administration Users .

When you add/configure this user, ensure the Webservice access has been checked. (This user is used by HCM-F SI in order to send  a WebService Request to CUCDM, hence it needs to be enabled.)

Report Generation sourced from CUCDM has now been covered. SI, however, can also generate reports directly from a supported UC Application, Cisco Unified Communications Manager, and Cisco Unity Connection application servers for customers that are provisioned in Cisco HCM-F that do not have a CUCDM configured.

If you do not have a CUCDM configured, you need to add Cisco Unified Communications Manager (CUCM) and Cisco Unity Connection (CUC) application servers manually in order to run a Service Inventory report.

### Add Credentials

In order to add credentials,

- Click the Credentials tab.

- Click Add New .

Note : BOTH PLATFORM and ADMIN are required in order to run the UC Application Report Collection.

- Complete the User ID , Password, and Re-enter Password fields.

- Click Save .

- Repeat to add the next Credential Type .

### Add the Network Adress

- Click the Network Address tab.

- Click Add New .

- Select the Network Space : Service Provider Space .

This is required for both Cisco Unified Communications Manager and Cisco Unity Connection.

### Cluster Applications

Repeat all for the next Cluster Application.

Next, configure the Service Inventory piece on the Service Inventory Configuration Page on HCM-F, as shown in this image.

### Overview Page

Here you can set the schedule that defines when you would like the report to begin.

Note : The Report Format Version is key here.

The Cisco HCS 9.1(1) report format version is only compatible with CUCDM Version 8.1 and later. The Cisco HCS 9.0(1) report format version is compatible with CUCDM Version 8.0 and later. If you run an earlier version of the CUCDM software, choose the 8.6(2) report format version.

#### SI CUCDM Report

- In order to ensure that Version 9.1(1) and 9.0(1) HCS report formats are generated properly, navigate to Infrastructure Manager > Management Application . On this page, be sure to choose the CUCDM Software Version 8.0 or 8.1 and not Version 7.4.

The Username field is greyed out (hardcoded).

CUCDM uses the username, adminsftp, in order to transfer data to the SI application. You cannot update this field.

Note : CUCDM learns this password from SI when SI sends the original SOAP request.

- In the Service Provider SFTP Settings section, configure the hostname and port (22) along with the username/password  for the SFTP server to which you will send the .si report files.

## Troubleshoot

This section provides information you can use in order to troubleshoot your configuration.

Important logs are:

- activelog tomcat/logs/catalina.out - includes request and response messages to and from CUCDM.

- activelog tomcat/logs/si/log4j - contains all SI-specific operations.

Note : If you use SI without CUCDM, also review these logs: - /var/log/active/hcs/chpa - Provisioning Adapter Service Log files - /var/log/active/hcs/ucpa – ucpa Service Log files

Complete these steps in order to set the log levels to Detailed (debug) level:

```
admin:
```

```
set trace tracelevel
```

- Enter the tracelevel (use the CLI command show tracelevels in order to find allowed tracelevels) - Detailed

The record(s) are updated successfully.

Once that is done, wait for the next report generation as per your schedule. The first thing to check is whether you can see the transaction in VOSS. Search for a transaction called CreateServiceInventory. This transaction should succeed.

Note that you can see the User ID in the transaction output is the hcmf user that was configured earlier both in HCM-F as well as on CUCDM.

Once that is done, check whether the files have made it into SI correctly. It is important to understand how the report data structure functions in SI. The format of a SI file is an ASCII-based file with the ".si" file extension. (The file extension for the UC Application Service Inventory Common Format is .ucsi)

So, under normal circumstances, CUCDM sends the raw SI files (compressed) to HCM-F. HCM-F (SI) then massages the data. (SI sees the new file(s), decompresses the file(s), and processes the file(s).) Within the file structure there are a number of directories and each of these have their own meaning dependent upon the state of the data. These folders can be accessed only by the Technical Assistance Center (TAC) during a troubleshooting session via the root account.

Specifically, all the files are stored here in SI: /opt/hcs/si/backup/

- dmuncompressed/  - this is where you unzip and place the files received from CUCDM.

- cntranslated/ - then the files are translated as an intermediate step and these go into this directory.

- cisco-normalized/ - then a single file is produced (copy of the final output) and it goes in here.

- sp-normalized/  - based on the maximum file size configured on the GUI, the previously mentioned file is split into chunks based on the maximum configured fill size (then they are renumbered for sequencing).

```
/opt/hcs/si/backup/dmuncompressed [root@hcmf921 dmuncompressed]# 20150522210000GMT+1+CUCDM+1+1.dsi  20150622121500GMT+1+CUCDM+1+1.dsi 20150523210000GMT+1+CUCDM+1+1.dsi  20150623121500GMT+1+CUCDM+1+1.dsi 20150524210000GMT+1+CUCDM+1+1.dsi  20150624121500GMT+1+CUCDM+1+1.dsi 20150525210000GMT+1+CUCDM+1+1.dsi  20150625121500GMT+1+CUCDM+1+1.dsi 20150526210000GMT+1+CUCDM+1+1.dsi  20150626121500GMT+1+CUCDM+1+1.dsi [root@hcmf921 dmuncompressed]#
```

```
/opt/hcs/si/backup/cntranslated [root@hcmf921 cntranslated]# 20150602210000GMT+1+CUCDM+1+1.tsi  20150703121500GMT+1+CUCDM+1+1.tsi 20150603210000GMT+1+CUCDM+1+1.tsi  20150704121500GMT+1+CUCDM+1+1.tsi 20150604210000GMT+1+CUCDM+1+1.tsi  20150705121500GMT+1+CUCDM+1+1.tsi 20150605210000GMT+1+CUCDM+1+1.tsi  20150706121500GMT+1+CUCDM+1+1.tsi [root@hcmf921 cntranslated]#
```

```
/opt/hcs/si/backup/cisco-normalized [root@hcmf921 cisco-normalized]# 10000GMT+1+CUCDM+1+1.csi  20150703121500GMT+1+CUCDM+1+1.csi 20150603210000GMT+1+CUCDM+1+1.csi  20150704121500GMT+1+CUCDM+1+1.csi 20150604210000GMT+1+CUCDM+1+1.csi  20150705121500GMT+1+CUCDM+1+1.csi 20150605210000GMT+1+CUCDM+1+1.csi  20150706121500GMT+1+CUCDM+1+1.csi 20150606210000GMT+1+CUCDM+1+1.csi  20150707121500GMT+1+CUCDM+1+1.csi 20150607210000GMT+1+CUCDM+1+1.csi  20150708121500GMT+1+CUCDM+1+1.csi 20150608210000GMT+1+CUCDM+1+1.csi  20150709090000GMT+1+CUCDM+1+1.csi
```

```
/opt/hcs/si/backup/sp-normalized [root@hcmf921 sp-normalized]# 20150528210000GMT+1+CUCDM+1+1.si  20150628121500GMT+1+CUCDM+1+1.si 20150529210000GMT+1+CUCDM+1+1.si  20150629121500GMT+1+CUCDM+1+1.si 20150530210000GMT+1+CUCDM+1+1.si  20150630121500GMT+1+CUCDM+1+1.si 20150531210000GMT+1+CUCDM+1+1.si  20150701121500GMT+1+CUCDM+1+1.si 20150601210000GMT+1+CUCDM+1+1.si  20150702121500GMT+1+CUCDM+1+1.si
```

In order to pull the log files from SI, enter these commands

```
file get activelog  tomcat/logs/catalina.out file get activelog tomcat/logs/si/log4j/XXXXXX (where XXXX are the filenames you want to gather)
```

## Verify

There is currently no verification procedure available for this configuration.

### Contributed by Cisco Engineers

Andrea Cingolani

Cisco TAC Engineer

Kurt Van De Vel

Cisco TAC Engineer

### This Document Applies to These Products

- Hosted Collaboration Solution (HCS)