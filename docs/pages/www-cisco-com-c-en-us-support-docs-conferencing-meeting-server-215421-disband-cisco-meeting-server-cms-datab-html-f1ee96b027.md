---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-215421-disband-cisco-meeting-server-cms-datab-html-f1ee96b027
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/215421-disband-cisco-meeting-server-cms-datab.html
retrieved_at: 2026-08-21T13:12:52.802087+00:00
---

Disband Cisco Meeting Server (CMS) Database Cluster and Recluster

# Disband Cisco Meeting Server (CMS) Database Cluster and Recluster

### Download Options

Updated: April 22, 2020

Document ID: 215421

Contents

## Contents

## Introduction

This document describes how to disband the Cisco Meeting Server (CMS) database in order to configure the certificates and recluster the database after the certificate changes.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CMS basic configuration

- Database cluster

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### Remove the Database Cluster

Step 1 . Take a backup of each server in the database cluster.

Step 2 . Open a CLI session to each CMS server in the cluster.

Step 3 . Run the command backup snapshot name_of_backup to backup the CMS configuration. Step 4 . On each CMS server open a Windows Secure Copy (WinSCP) session and save the backup created on your PC. There must be two of them with extensions .bak and .json . Step 5 . On the CLI run the command database cluster status. You must see which one is the database master.

Step 6 . Choose one of the slaves first and open a CLI connection to that server. Step 7 . Once connected to the slave, run the command database cluster remove , wait until the process is complete, as shown in the image:

Step 8 . To verify the process is completed, run the command database cluster status and ensure that the database cluster remove command shows a success as shown in the image:

Step 9 . Do the same procedure on every CMS slave of the database cluster. Step 10 . Once the only node in the database cluster is the Master, open a CLI to the master and do the same procedure as describe above. Step 11 . At this point the database cluster has been disabled.

Step 12 . Apply the certificates to the database service.

### Cluster the Database

Step 1 . On the server that you want to be the master, run the command database cluster initialize . Step 2 . In order to verify the database node initialized successfully, run the command database cluster status until it shows a success against it. Step 3 . On every slave that you want to add to the cluster run the command database cluster join Master_IP_Address .

## Verify

Step 1 . Open a CLI session to every CMS that is part of the cluster.

Step 2 . Run the command database cluster status .

Step 3 . Verify that the database master is the same for all the servers and all servers are in Sync state as shown in the image:

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Contributed by Cisco Engineers

Octavio Miralrio

Cisco TAC Engineer

### This Document Applies to These Products

- Meeting Server