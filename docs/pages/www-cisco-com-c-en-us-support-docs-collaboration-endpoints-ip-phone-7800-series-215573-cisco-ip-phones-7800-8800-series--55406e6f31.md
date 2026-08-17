---
doc_id: www-cisco-com-c-en-us-support-docs-collaboration-endpoints-ip-phone-7800-series-215573-cisco-ip-phones-7800-8800-series--55406e6f31
source_url: https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/ip-phone-7800-series/215573-cisco-ip-phones-7800-8800-series-fails-t.html
retrieved_at: 2026-08-17T01:09:13.081980+00:00
---

Cisco IP Phones 7800/8800 Series fails to register over MRA if phone has expired Sectigo/Addtrust root certificate

# Cisco IP Phones 7800/8800 Series fails to register over MRA if phone has expired Sectigo/Addtrust root certificate

### Download Options

Updated: June 3, 2020

Document ID: 215573

Contents

## Contents

## Introduction

This document describes the solution for Cisco IP Phones 7800/8800 Series registration failure over MRA (Mobile Remote Access) if phone has expired Sectigo/Addtrust root certificate which expried on 30th May 2020.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Problem

Cisco IP Phones 7800/8800 Series fails to register over MRA if phone has expired Sectigo/Addtrust root certificate which expried on 30th May 2020 and Expressway has signed it certfictate from Sectigo/Addtrust CA.

Per 12.7 firmware Certificate Authority Trust List, Trust list has expired Sectigo/Addtrust certificate on IP phone trust store.

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cuipph/all_models/ca-list/CA-Trust-List.pdf

To verify the certificate validity copy the fingerprint mentioned in document for certificate trust store and browse to https://crt.sh/ paste the fingerprint in the white box and click search

Once search is completed you can verify the validity of the certificate

## Solution

Firmware to 12.8 has a fix wherein expired certificates have been cleaned, This issue is documented by Cisco bug ID CSCvt26128.

You can download the latest firmware thru links documented below for 7800 and 8800 Series Phones

https://www.cisco.com/web/software/282074288/151637/cmterm-78xx.12-8-1-0001-455-readme.html cmterm-78xx.12-8-1-0001-455.k3.cop.sgn

https://www.cisco.com/web/software/282074288/151637/cmterm-8845_8865.12-8-1-0001-455-readme.html cmterm-8845_65-sip.12-8-1-0001-455.k3.cop.sgn https://www.cisco.com/web/software/282074288/151637/cmterm-88xx.12-8-1-0001-455-readme.html cmterm-88xx-sip.12-8-1-0001-455.k3.cop.sgn

## Limitation

Note : Phone firmwares upgrade over MRA isn't supported. This issue is documented by Cisco bug ID CSCvb29314.

### Contributed by Cisco Engineers

Vikram Dutta

Cisco TAC Engineer

Sharan Sampath

Cisco TAC Engineer

Mohammed Noorulla Khan

Cisco TAC Engineer

### This Document Applies to These Products

- Expressway Series

- IP Phone 7800 Series