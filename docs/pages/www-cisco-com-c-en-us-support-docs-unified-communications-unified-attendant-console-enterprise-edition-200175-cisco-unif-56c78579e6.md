---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-attendant-console-enterprise-edition-200175-cisco-unif-56c78579e6
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-attendant-console-enterprise-edition/200175-Cisco-Unified-Attendant-Console-Licensin.html
retrieved_at: 2026-09-07T15:48:54.563537+00:00
---

CUAC Licensing and Troubleshoot Commonly Faced Issues

# CUAC Licensing and Troubleshoot Commonly Faced Issues

### Download Options

Updated: February 9, 2017

Document ID: 200175

Contents

## Contents

## Introduction

This document describes the licensing structure of Cisco Unified Attendant Console (CUAC) server/server-less that starts from version 8.x upto version 11.x and also troubleshoots some commonly faced scenarios.

## Prerequisites

### Requirements

Cisco recommends that you have basic knowledge of CUAC.

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Unified Enterprise Attendant Console (CUEAC) - 8.x and 9.x

- Cisco Unified Business Attendant Console (CUBAC) - 8.x and 9.x

- Cisco Unified Department Attendant Console (CUDAC) - 8.x and 9.x

- Cisco Unified Premium Attendant Console (CUPAC) - 9.x

- Cisco Unified Attendant Console Advanced (CUACA) - 10.x and 11.x

- Cisco Unified Attendant Console Standard - serverless (CUACS) - 10.x and 11.x

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

### Important Terms

#### License Activation Code

- The License Activation Code is a 27 character code which you will receive once you order licenses.

- It is in the format : xxxxx-xxxxx-xxxxx-xxxxx-xxxxx-xx.

- It is sent to the company in a .pdf format if e-delivery method is used; sent on a piece of paper if physical configuration is used.

#### Registration Code

- It is a 8-character code mapped which depends on number of factors that include the server MAC address.

- Located in the CUAC WebAdmin page under Help > Licensing (for server based deployment) and under Help > About CUAC Standard (for server-less deployment).

Note : For server-less deployment (CUAC Standard), Registration Code is renamed as Machine Code.

### Licensing Ordering Information (SKU)

- Version 8 (end of sale Oct 21, 2013)

CUE-ATT-CON         Enterprise Edition

CUB-ATT-CON         Business Edition

CUD-ATT-CON         Department Edition

- Version 9 (end of sale Dec 18, 2015)

eDelivery:

L-CUACD9X-ATT-CON            Department Edition

L-CUACB9X-ATT-CON            Business Edition

L-CUACE9X-ATT-CON            Enterprise Edition

L-CUACP9X-ATT-CON            Premium Edition

Physical Delivery:

CUACD9X-ATT-CON            Department Edition

CUACB9X-ATT-CON            Business Edition

CUACE9X-ATT-CON            Enterprise Edition

CUACP9X-ATT-CON            Premium Edition

- Version 10

eDelivery:

L-CUAC10X-ADV               Advanced

L-CUAC10X-ADV-HA          Advanced High Availability

L-CUAC10X-STND             Standard

Physical Delivery:

CUAC10X-ADV                 Advanced

CUAC10X-ADV-HA            Advanced High Availability

CUAC10X-STND               Standard

- Version 11

eDelivery:

L-CUAC11X-ADV             Advanced

L-CUAC11X-ADV-HA        Advanced High Availability

L-CUAC11X-STND           Standard

Physical Delivery:

CUAC11X-ADV              Advanced

CUAC11X-ADV-HA         Advanced High Availability

CUAC11X-STND            Standard

### Order Information to Upgrade CUAC

There are two ways to purchase the upgrade License Activation Code (LAC), which is used to retrieve the upgrade license. If you have a valid Unified Communications Software Subscription ( UCSS) or Software Support Service (SWSS) contract then you can purchase Quantity 1 of the upgrade LAC via PUT (Product Upgrade Tool) website for free. If you do not have a valid contract, you will have to purchase it with the use of A-la-carte with Quantity equal to the number of operators required to login simultaneously (same as the number of LAC used in the old version). Each upgrade LAC is mapped to the LAC of the old version.

Note : All a-la-carte upgrade LACs must be used together to retrieve the license, not separately.

Note : If you face any contract related issues when you order LAC via PUT, contact your accounts team or open a case with the PUT team. Link to open a case with PUT Support . TAC will not be able to assist on contract related issues.

- Version 9

Upgrade license obtained through PUT (with a UCSS contract):

CUACD9X-AC-UPG            Department Edition

CUACB9X-AC-UPG            Business Edition

CUACE9X-AC-UPG            Enterprise Edition

A la carte upgrade license (without a UCSS contract):

1. eDelivery:

L-CUACD9X-U-AC=            Department Edition

L-CUACB9X-U-AC=            Business Edition

L-CUACE9X-U-AC=            Enterprise Edition

2. Physical Delivery:

CUACD9X-U-AC=              Department Edition

CUACB9X-U-AC=              Business Edition

CUACE9X-U-AC=              Enterprise Edition

- Version 10

Upgrade license obtained through PUT (with a SWSS contract)

CUACADV10X-AC-UPG    Advanced

CUACST10X-AC-UPG       Standard

Note :  Only Department Edition deployment with a UCSS contract will be able to order this SKU through PUT.

A la carte upgrade license (without a UCSS/SWSS contract):

1. eDelivery:

L-CUAC10ADV-U-AC=      Advanced

2. Physical Delivery:

CUAC10ADV-U-AC=         Advanced

Note :  There is no a la carte upgrade option for Department Edition deployment to obtain CUAC Standard licenses.

- Version 11

Upgrade license obtained through PUT (with a SWSS contract):

CUACADV11X-AC-UPG Advanced

CUACST11X-AC-UPG    Standard

A la carte upgrade license (without a UCSS/SWSS contract)

1. eDelivery:

L-CUAC11ADV-U-AC=   Advanced

L-CUAC11ST-U-AC=      Standard

2. Physical Delivery:

CUAC11ADV-U-AC=     Advanced

CUAC11ST-U-AC=        Standard

Note : From version 10.x onwards, there are no separate Enterprise/Business/Department/Premium editions. All current Enterprise/Business/Premium edition deployment can upgrade to Advanced version and the Department edition deployment upgrade to Standard edition. You cannot upgrade to the Advanced version from any version of Department Edition.

### Comparison Between Various Versions

### Licensing Structure

#### Demo License

- 5-day demo licenses come by default during any new install or upgrade of your CUAC server.

- This 5-day demo license can be extended up to a maximum of 60-day evaluation license (one-time only) by downloading the .rgf file from the Licensing website (Activate Evaluation Software section).

- Please note that it is not technically possible to extend this Evaluation period by more than 60 days by Cisco.

- CUAC server services will be stopped if the server is not licensed with purchased licenses within this period.

#### Stand-alone Server

- Every CUAC server will have one server license.

- Number of seat licenses is purchased depending on the number of operators logged into the console simultaneously.

- All operator seat licenses can be combined under 1 consolidated LAC or can be different LACs.

- Every operator seat license has a server license tied to it so separate server licenses are not purchased.

#### Resilient Server Installation

- Untill CUAC version 9.x, separate licenses are installed on both primary and secondary servers. You will receive two different LACs for both the servers.

- From 10.x onwards, all licensing information is held on the Publisher server and information is replicated to the Subscriber server.

- There will be no resilience license by default on installation.To install/configure resilience a separate license will be required.

- Resilience is enabled by default under evaluation licenses (5 days or 60 days)

- Resilience becomes an add-on license once product is purchased.

- Current Enterprise and Business Edition deployment can add resilience to their solution at any time after migrating to CUAC Advanced.

### Steps to License CUAC server

#### Activate Purchased Software

Here is the guide which explains the step-by-step procedure (with screenshots) to retrieve the license file (.rgf format) for your server.

It also explains the steps required to retrieve the upgrade license after you purchase the Upgrade LAC from Cisco Systems.

Steps to License CUAC server

Note : Since this guide is the official document from Cisco, it was created before CUAC Advanced or CUAC Standard were released, but the steps remain the exact same for all Editions.

- The upgrade LAC does not hold any information of the licenses on your old server.

- Only when you visit the Licensing website to redeem the new licenses, you will be able to transfer the license information from your old version to the new one.

- You will need to keep either the Registration code of the old server (if not changed after upgrade) or all the old LACs used on the old server for you to successfully transfer the licenses to the new version.

- If that information is not available, collect the following information used to activate the license on the old server: Sales Oorder number or LAC or email address, username, and company/partner location used to order the licenses and open a TAC case.

#### Activate Evaluation Software

Here are the steps used to retrieve the 60 days evaluation license:

- Go to the Licensing Website www.cisco.com/go/ac .

- Sign in with your credentials. If you have not already registered, make an account (steps mentioned in the link above). (This is NOT your Cisco.com ID).

- Select the necessary company details.

- Select the version and edition for which you need the license.

- Enter the Registration code/Machine code of the server.

- Click Submit . You will receive a .rgf file mailed to your email ID.

- You can now upload this file in your serve.

- Your server will be licensed for the next 60 days.

Note : There are no separate licenses for the CUAC console client

## Troubleshoot Common Scenarios

### Problem 1: New install and no LAC received

- A new installation of CUAC server was done and  LACs were purchased from Cisco but never received the same.

- Check the order status using Cisco Order Status Query Tool . If the status of the order does not show Complete , wait while it is processed.

- If it shows Completed and you still have not received the LACs, keep the Sales Order Number that you used to purchase these LACs ready.

- Open a case with Cisco TAC for them to retrieve the LACs.

### Problem 2: Change the CUAC windows server

- Your CUAC server crashed and the installation is now done on a different server.

- The Registration Code for the new server will be different.

- Since licenses are tied to the Registration Code, your licenses will become invalid.

- Keep the old and the new Registration Code ready and open up a case with Cisco TAC for them to reset the LAC(s) for you.

- You will be able to map  the LAC(s) with the new Registration Code to generate the license file for your server after this.

### Problem 3: Re-hosting the license

- There might be a case wherein CUAC server was migrated from one Windows machine to the other or changes were made on the Windows machine.

- In these scenarios, it is possible that certain parameters to which a Registration code is tied changes, and ultimately the Registration Code as well.

- As seen previously, licenses are mapped to a particular Registration Code and when that changes, the licenses are rendered invalid.

- Contact Cisco TAC  to have them reset your LAC(s).

- You will be able to map  the LAC(s) with the new Registration Code to generate the license file for your server after this.

### Problem 4: Try to get upgrade license and it fails

Scenario:

CUAC license (Assume, 8.x) was purchased, but the install of that server was never done and you upgraded the CUAC server to (Assume, 9.x) and order the upgrade LAC(s) and When trying to redeem the upgrade LAC on www.cisco.com/go/ac , it fails.

- This is because the CUAC 8.x license was never used and hence there is no Registration Code tied to that LAC in the CUAC licensing database. Upgrade LAC does not hold any information about the old server.

- To resolve: you need to use your 8.x LAC with the 9.x server Registration Code, set that 8.x license aside and go back to www.cisco.com/go/ac , then redeem the 9.x upgrade LAC. This will successfully produce the 9.x permanent license file.

### Problem 5: You ordered incorrect SKU

- Contact your Cisco accounts team to perform an RMA on the incorrect order and then get an order for the correct part number.

- TAC will not be able to assist you on this.

### Problem 6: Licenses have expired

- In case your 5 days demo licenses have expired, you can visit the Licensing Website and retrieve the 60 days evaluation license (one-time only). Refer Steps to License CUAC server .

- In case you have already used the 60 days evaluation license and that has expired as well, the only option would be to purchase licenses from Cisco and permanently license your CUAC server. There would be no workaround to increase this 60 days evaluation period.

## Related Information

- Licensing Website: www.cisco.com/go/ac

- Install and admin guides for each CUAC edition: Install and Admin guides

- Technical Support & Documentation - Cisco Systems

### Contributed by Cisco Engineers

Antara Sargam

Cisco TAC Engineer

### Customers Also Viewed

- Activation and Installation of a CUAC Advanced License