---
doc_id: www-cisco-com-c-en-us-support-docs-conferencing-meeting-server-215910-configuring-ldap-users-on-cisco-meeting-html-56f2cb989c
source_url: https://www.cisco.com/c/en/us/support/docs/conferencing/meeting-server/215910-configuring-ldap-users-on-cisco-meeting.html
retrieved_at: 2026-08-21T13:12:48.828544+00:00
---

Configuring LDAP Users on Cisco Meeting Server via API

# Configuring LDAP Users on Cisco Meeting Server via API

### Download Options

Updated: January 4, 2021

Document ID: 215910

Contents

## Contents

## Introduction

This document describes configuration of LDAP (Lightweight Directory Access Protocol) on Cisco Meeting Server via API (Application Programming Interface).

## Prerequisites

PostMan App

Cisco Meeting Server (CMS)

Microsoft Active Directory

### Requirements

There are no specific requirements for this document.

### Components Used

Cisco Meeting Server

Microsoft Active Directory

## Background Information

High level configuration flow to sync LDAP via API.

Step 1. Configure /ldapServers parameter thru API as described below

- LDAP server's address/port information

- Username and password for accessing the server

- Secure of non secure ldap.

Step 2 : Configure /ldapMappings parameter through API as described below

- LDAP user properties objects to cms corresponding user objects

- Example cms user jid will map to $sAMAccountName$@domain.com on cms and etc.

Step 3: Configure /ldapSources parameters thru API as described below which to tie ldapServers and ldapMappings object.

## Configure

Step 1. Configure /ldapServers

- Send a POST for /ldapServers , which would create a ldapServer ID. Use unique /ldapServers ID for further configuration.

- Response to POST would return in similar format <ldapServer id="7ca32cc4-389f-46f5-a1b0-0a468af291a4">

- Capture below information to update LDAP Server ID per the CMS API Reference Guide

- Sample POST Method with Parameters

- Perform a GET to verify configured parameters

Step 2, Configure /ldapMappings

- Send a POST for /ldapMappings  to create a /ldapMappings ID. Use /ldapMappings ID and configure below parameters.

- Capture below information to update LDAP Mapping ID per the CMS API Reference Guide

- Configure below parameters for ldapMappings

- Perform a GET to verify configured parameters.

Step 3. Configure /ldapsources

- Send a POST for /ldapsources to create a /ldapsources ID. Use /ldapsources ID and configure below parameters.

- Capture below information to update LDAP Mapping ID per the CMS API Reference Guide

- Configure below parameters for ldapSources

- Perform a GET to verify configured parameters.

Configuration is complete. We can perform a full sync now.

## Verify

Step 1. Send POST for /ldapSyncs from API and check event logs

Step 2. Check in event logs if sync is completed.

Step 3. Verify Users are synced from ldap source.

## Troubleshoot

Verify API parameters and LDAP Attributes are accurate.

Taking packet captures from call Bridge helps in isolating connectivity issues with LDAP.

### Contributed by Cisco Engineers

Vikram Dutta

Cisco TAC Engineer

### This Document Applies to These Products

- Meeting Server