---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-216549-how-to-renew-expired-database-cluster-ce-html-536538c0d9
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/216549-how-to-renew-expired-database-cluster-ce.html
retrieved_at: 2026-08-21T13:13:05.670674+00:00
---

How to renew expired database cluster certificates in Cisco Meeting Server (CMS)

# How to renew expired database cluster certificates in Cisco Meeting Server (CMS)

### Download Options

Updated: December 24, 2020

Document ID: 216549

Contents

## Contents

## Introduction

This document describes how to renew expired (client and server) certificates on database cluster on Cisco Meeting Server (CMS).

## Prerequisites

### Components Used

Cisco Meeting Server

## Background Information

Certificate (client and server) used to create a database cluster on Cisco Meeting Server comes with an expiry date.

Once the certificate expires, database nodes in cluster stops talking to each other. Certificates cannot be renewed on CMS database cluster nodes unless cluster is removed using CLI command "database cluster remove". Certificates are tied to DB servcies which does not let us make any changes, unless a cluster is torndown and certificates are disengaged.

## Configure

### Network Diagram

### Procedure Overview

Step 1. Take a backup of CMS Nodes in the cluster

Step 2. Fetch the backup file from cms via FTP and store on local pc.

Step 3.  Remove database cluster node from cluster.

Step 4. Update the certificates.

Note : Try to give same certificate file name as used earlier (which got expired). You may need to remove old expired certificates from Cisco Meeting Server for new one to take affect.

Step 5. Create cluster again database cluster initialize.

Step 6. Follow process to create cluster.

Note : Above procedure to follow on all slaves and then at last update on master nodes

### Configuration Procedure

Step 1. In the output of "database cluster status" Certificate shows expired for CMS database cluster.

Step 2. Verify certificate expiry by running " pki inspect <cert name>" command

Caution : We cannot update the certificate when database cluster is active. We need to remove the node from cluster. If an attempt is made to update certificate while cluster is active. Following error is noticed

Step 3. Create a backup file on the node by runinng  backup snapshot <filename>

Step 4. Login to FTP client and pull the file on local PC.

Step 5. Pull the .bak file from cms to local PC

Step 6. Run command to remove the  node from database cluster. " database cluster remove"

Note :Press "Y" in caps. lower case "y" wont proceed.

Step 7. Node is detaching from cluster

Step 8. Node has been removed from database cluster.

Step 9. Update new certificates files for databse cluster. Database cluster would need client and server certificate.

```
database cluster certs <server_key> <server_crt> <client_key> <client_crt> <ca_crt>
```

Step 10. Add node to the database cluster again.

Step 11. New certificate files have been updated.

Step 12. Add the node to the database cluster master.

Step 13. Database cluster is good again with updated certificates

### Contributed by Cisco Engineers

Vikram Dutta

Cisco TAC Engineer

### This Document Applies to These Products

- Meeting Server