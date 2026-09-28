---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-management-217203-how-to-configure-blast-dial-for-cms-spac-html-773d6b5f61
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-management/217203-how-to-configure-blast-dial-for-cms-spac.html
retrieved_at: 2026-08-21T06:27:58.452028+00:00
---

How to Configure Blast Dial for CMS Spaces

# How to Configure Blast Dial for CMS Spaces

### Download Options

Updated: June 17, 2021

Document ID: 217203

Contents

## Contents

## Introduction

This document describes how to configure the blast dial feature for Cisco Meeting Management (CMM) version 3.2, to allow the feature to be applicable to Cisco Meeting Server (CMS) spaces.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CMS configuration.

- CMM configuration.

### Components Used

The information in this document is based on these software and hardware versions:

- CMS 3.2

- CMM 3.2

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

Step 1. Open the CMM web admin and Navigate to Spaces .

Step 2. Search for the desired space.

Step 3. Turn on Blast dial configuration and set the retries parameters as desired.

Step 4. Select Add contact in order to add the contacts to be called when the call is initiated.

Step 5. UAditionally you can use the Comma Separated Values (CSV) option to add multiple contacts.

- Open a new text file and add the parameters name and address , separated by a comma.

- Add the contact information to the file in CSV format, as shown in the image:

- Save the file with .csv extension.

- Navigate to CMM > Spaces > Select a space > Blast Dial Configuration > Dial-out contacts > CSV and select Upload CSV .

- Choose the previously generated file.

- Select Upload .

## Verify

In order to validate the configuration is correct, obtain the CMM log bundle, navigate to CMM > Logs > Log bundle and select Download log bundle .

Step 1. Validate that Blast Dial is configured successfully, the cmm_log.txt must show Set blast dial configuration successful: enable=True .

```
Jun 11 03:57:26 cmm01 2021-06-11 03:57:26,095 - local:admin/HTTP/IPv4:10.15.10.5:tcp:54380 - Set blast dial configuration successful: enable=True
```

Step 2. Validate that CMM added the contact information successfully, the cmm_log.txt must show the next information.

```
Jun 11 04:05:05 cmm01 2021-06-11 04:05:05,057 - local:admin/HTTP/IPv4:10.15.10.5:tcp:54380 - Set blast dial participants via JSON successful: cluster_id=1, cluster_name=<cms1_cluster>, participants=[OrderedDict([('address', 'moimar@meet.fer.local'), ('name', 'Moises Martinez')])], space_id=fd4151a3-a260-4879-b12c-e998986cc67a
```

## Troubleshooting

There is currently no specific troubleshooting information available for this configuration.

### Contributed by Cisco Engineers

Fernando Garrido

### This Document Applies to These Products

- Meeting Management