---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-220315-troubleshoot-expressway-upgrade-error-html-bd0666816f
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/220315-troubleshoot-expressway-upgrade-error.html
retrieved_at: 2026-08-16T15:43:52.974209+00:00
---

Troubleshoot Expressway Upgrade Error

# Troubleshoot Expressway Upgrade Error

### Download Options

Updated: March 29, 2023

Document ID: 220315

Contents

## Contents

## Introduction

This document describes how to fix an Expressway Upgrade Error.

## Background Information

On some occasions, while you upgrade the Expressway servers to a higher version, the upgrade fails with the error:

System error: Post install script /tandberg/etc/postinstall.current.d/52-set_pubkeyalgorithms failed

The root cause of this error is the duplicate cipher entries. The main idea in this document is to provide steps needed to remove the duplicate cipher entries in configuration.

### Components Used

Expressway on version X12.7.1.

Upgrade firmware on version X14.0.3.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## What to do Next?

In this scenario, the first step is to take an xconfig file from the Expressway. The goal is to confirm which ciphers are duplicates.

Note : Make sure to use root instead of admin account to get the xconfig file.

Log in with root account into the Expressway server by SSH , type dbxsh , then run the xconfig command. Save the output in a .txt file.

Open the xconfig file, search for the duplicated cipher entries. You are recommended to take note of which entries are duplicates. By the use of Notepad++ (Windows) or Sublime Text (Mac), it is possible to filter for the words cipher uuid , then look for duplicates, as shown in this example:

This example shows that cipher sshd_pfwd_pubkeyalgorithms has a duplicate cipher with a different Universal Unique Identifier (UUID).

Once all duplicate ciphers are identified, access the Expressway server by CLI with Putty with the root account, then delete only duplicate entries, use the UUID information, under dbxsh .

Command format: xdelete cipher uuid

Example of ciphers deleted in this xconfig file:

xdelete cipher uuid 26afb85f-80ae-4569-9d48-cf30bf741430

Repeat the same process until all duplicate entries are deleted.

Note : This procedure can take several attempts until all duplicate entries are deleted. It is recommended to take another xconfig file to double check the ciphers.

After this, proceed with the upgrade.

## Additional Information

Cisco bug ID CSCvx35891

### Revision History

1.0

29-Mar-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 29-Mar-2023 | Initial Release |