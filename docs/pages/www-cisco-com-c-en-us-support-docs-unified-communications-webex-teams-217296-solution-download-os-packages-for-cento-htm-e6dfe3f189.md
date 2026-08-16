---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-teams-217296-solution-download-os-packages-for-cento-htm-e6dfe3f189
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-teams/217296-solution-download-os-packages-for-cento.html
retrieved_at: 2026-08-16T22:06:13.265445+00:00
---

Solution: Download OS Packages for CentOS with a One-Step Query

# Solution: Download OS Packages for CentOS with a One-Step Query

### Download Options

Updated: May 26, 2021

Document ID: 217296

Contents

## Contents

## Introduction

This document describes the use of Yum-CentOS-Bot that allows the user to run queries, in order to retrieve Operating System-leveled packages as well as python third-party libraries. They are all downloaded from official repositories and the same is constricted to CentOS flavor only, for (n-2) versions. This also includes CentOS 6 which reached its End Of Life (EOL) on Nov 30th, 2020

## Problem

Sometimes the Open Virtualization Archive (OVA ) provided by the engineering for a specific application doesn't have the desired packages or a customer might demand specific packages to automate a specific module. This might also involve installing third-party python libraries. All of this can be achieved using Yum-CentOS-Bot

## Solution

You would need an account on Microsoft Teams or WebEx messaging App( formally known as WebEx Teams). Once you log in to this application, you need to search for the bot through its username i.e.

```
yum-bot@webex.bot
```

Once you have found the bot, you can greet the bot and it assists you with the commands for leveraging its available functionalities.

This bot allows you to run queries on CentOS 6, 7 and 8 versions based on requirement.

Syntax to get a package that is not available in a minimal OS by default: <CentOS version>/package <package_name>

Let's take an instance here for CentOS 6 and we are looking for openssl:

Query: 6/package openssl

Please note: CentOS 7 is selected by default and it doesn't require any redirection, so in order to get the same package from 7:

Query: /package openssl

Using this bot, you will get not only the queried package but also its dependencies.

For detailed instructions, please refer to attached video that demonstrates its usage for all its functionalities.

Video Player is loading.

0:00

0:00

LIVE

0:00

For any support or to report a bug/enhancement, you may send an email to: yumbot-helpdesk@cisco.com

### Revision History

1.0

26-May-2021

Initial Release

### Contributed by Cisco Engineers

Rahul Dang

Cisco TAC Engineer

### This Document Applies to These Products

- Webex App

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 26-May-2021 | Initial Release |