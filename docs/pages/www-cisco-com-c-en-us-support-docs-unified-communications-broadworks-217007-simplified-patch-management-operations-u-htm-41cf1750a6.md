---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-217007-simplified-patch-management-operations-u-htm-41cf1750a6
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks/217007-simplified-patch-management-operations-u.html
retrieved_at: 2026-09-07T13:03:36.213240+00:00
---

Simplified patch management operations using NFM (Network Function Manager)

# Simplified patch management operations using NFM (Network Function Manager)

### Download Options

Updated: March 13, 2021

Document ID: 217007

Contents

## Contents

The present article shows how the NFM (Network Function Manager) portal simplifies the operations of maintaining the Cisco BroadWorks servers by automatically downloading software and performing most patching management operations including creating custom patch bundle (PB) .

The NFM portal is the preferred solution for Cisco BroadWorks operators to manage patches and software. Considering that the Xchange portal will be eventually decommissioned, it is strongly advised to leverage and understand these functionalities in order to fully optimize maintenance operations.

The Network Function Manager also supports these operations:

- Listing patches

- Applying and removing patches

- Running healthmon

- Automatically/manually updating SWManager

- Creating patching report

## High Level Architecture

### Main Key Components

#### NFM Portal

The operators typically performs most of the operations through the admin portal available from the NFM FrontEnd.  It is typically deployed on /nfmPortal/ and therefore available via http(s)://<NFM_IP_or_FQDN>/nfmPortal/.

### Software Distribution Center

#### Cisco Repository

This is the source repository where all patches and other components are downloaded from.  The repository is using Web-based Distributed Authoring and Versioning (WebDAV) and resides on Cisco.  The transfers are fully automated as configured with the NFM scheduling.

```
NFM_CLI/Applications/SoftwareManagement/SoftwareDistributionCenter> get site = https://api.cisco.com username = <CiscoAccountLogin> password = ******** downloadBinaryFiles = true deletionDelayInDays = 1 connectionTimeoutInSeconds = 30 useCiscoDownload = true
```

```
NFM_CLI/Applications/SoftwareManagement/SoftwareDistributionCenter> validate Validating Software Distribution Center configuration... successful. NFM_CLI/Applications/SoftwareManagement/SoftwareDistributionCenter>
```

#### Local Repository

This is where the downloaded patches and other software components are stored locally, that is customer's environment.

Example:

```
bwadmin@r23nfm01.calo.cisco.com$ ls -1 /var/broadworks/fileTransfer/software/22.0.1123/ as/ bss/ dbs/ ips/ nds/ ns/ platform/ ps/ ums/ xs/ xsp/ bwadmin@r23nfm01.calo.cisco.com$
```

### Architecture Diagram

## Creating a Custom PB (Patch Bundle)

### Steps

- Login in the NFM portal

- Access the Software section from the left navigation panel

- Create a template by highlighting a specific software release, for example 24.0_1.944

- After expanding the selected release, click on 'Add' under the 'Templates' tab

- From the list of patches being displayed, select individual patches by manual selecting them or by using a filtering criteria, for example System Critical Patches (Sys Crit)

- Enter a "Patch Template Name" and "Save"

- After that step, the name of the Patch Bundle (BD) filename will eventually show up

- To transfer and/or apply this newly created PB, select a node from the list of the bottom panel

- Select the "Apply Patches" from the upper right pull down menu

- From the "Apply Patches" window, select the template name / patch bundle

- In order to only transfer the patch bundle (PB) file (and not to apply it), select "Upload patches only" checkbox

- Click on "Apply Patches" button

- The patch bundle (PB) will be transferred to the selected node under /var/broadworks/patches directory

### Example

```
bwadmin@ol8as.cisco.com$ ls -lhtr /var/broadworks/patches | tail -n1 -rw-rw---- 1 bwadmin bwadmin 189M Mar 12 17:29 PB.as.24.0.944.pb20210312172527 .Linux-x86_64.zip bwadmin@ol8as.cisco.com$
```

```
AS_CLI/Maintenance/Patching> detail PB.as.24.0.944.pb20210312172527 Patch Name State ================================================================================ AP.as.24.0.944.ap375266 installed AP.as.24.0.944.ap370326 installed AP.as.24.0.944.ap376023 installed AP.as.24.0.944.ap376410 installed AP.as.24.0.944.ap376889 installed AP.as.24.0.944.ap375902 installed AP.as.24.0.944.ap375646 installed AP.as.24.0.944.ap375273 installed AP.as.24.0.944.ap378164 installed AP.as.24.0.944.ap378122 installed AP.as.24.0.944.ap378150 installed AP.as.24.0.944.ap375996 installed AP.as.24.0.944.ap375655 installed AP.as.24.0.944.ap375369 installed AP.as.24.0.944.ap375489 installed AP.as.24.0.944.ap375860 installed AP.as.24.0.944.ap376147 installed AP.as.24.0.944.ap374803 installed AP.as.24.0.944.ap378506 installed AP.as.24.0.944.ap374832 installed AP.as.24.0.944.ap376024 installed AP.as.24.0.944.ap377651 installed AP.as.24.0.944.ap378178 installed AP.as.24.0.944.ap376205 installed 24 entries found. * -> Patch(es) applied from this bundle. AS_CLI/Maintenance/Patching>
```

## Getting Started and References

- Cisco BroadWorks Feature Guides: Network Function Manager

- Network Function Manager: Patch Management

### Revision History

1.0

26-Mar-2021

Initial Release

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- BroadWorks

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 26-Mar-2021 | Initial Release |