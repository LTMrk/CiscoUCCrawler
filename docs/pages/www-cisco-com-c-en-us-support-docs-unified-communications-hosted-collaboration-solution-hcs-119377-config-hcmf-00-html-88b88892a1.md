---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-hosted-collaboration-solution-hcs-119377-config-hcmf-00-html-88b88892a1
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/hosted-collaboration-solution-hcs/119377-config-hcmf-00.html
retrieved_at: 2026-09-01T14:58:26.366436+00:00
---

Configure HCM-F 10.X License and HLM Workflow

# Configure HCM-F 10.X License and HLM Workflow

Updated: February 11, 2016

Document ID: 119377

Contents

## Contents

## Introduction

This document describes the HCS License Manager (HLM), which runs as a stand-alone Java application on the Cisco HCM-Fulfillment (HCM-F) platform. It utilizes the HCM-F service infrastructure and message framework which is responsible to interact/provision with Unified Communications (UC) applications and the Prime License Manager (PLM) in order to fetch and change their deployment modes. It utilizes the Simple Object Access Protocol (SOAP) API in order to interact with the UC applications and Representational State Transfer (REST) for the PLM interaction.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Hosted Collaboration Solution (HCS) deployments.

### Components Used

The information in this document is based on these software and hardware versions:

- HCM-F Version 10.6.1

- PLM Version 10.X

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

In HCS deployments, only the stand-alone PLM instances are supported. Co-resident PLMs with Cisco Unified Communications Manager (CUCM) or CUCxn are not supported for the management of HCS licenses. Each standalone PLM supports licenses up to 1000 UC application clusters regardless of the number of users in each cluster. The former Enterprise License Manager (ELM) supported up to 200 clusters. The service provider can have multiple PLMs on HCM-F.

## Configure

Note : Use the Command Lookup Tool ( registered customers only) in order to obtain more information on the commands used in this section.

Note : The deployment mode must be set on HCM-F accordingly with the license type installed earlier in PLM.

- Name - PLN name

- Hostname - PLM IP address or Fully Qualified Domain Name (FQDN)

- User ID - PLM OS administrator user

- Password - PLM OS administrator password

Note : As soon the PLM is added, the PLM password cannot be changed anymore in the HCM-F GUI. This feature will be introduced in a future HCM-F release and any password changes on the PLM side will break the integration with HCM-F.

This workflow will be started as soon as the PLM is added:

- HLM validates the connection with PLM. The connection is established in HTTPS, port 8443 with the OS administrator user id and password with service provider IP.

- HLM checks the PLM version in order to invoke the correct API and set the version accordingly.

- HLM sets the PLM deployment mode.

- PLM replies with a 200 OK if the mode is changed accordingly.

In order to verify if the PLM deployment mode is on HCS mode, enter this URL in a browser: https://plmServerHostname/elm-resources

PLM replies with the current deployment mode, as shown in this image.

The eligible clusters appear in the pop-up window. Check the checkbox for the cluster and click Assign .

Note : After the cluster is assigned to the ELM in HCM-F, the application is rebooted.

The detailed HLM workflow, while it assigns the cluster into PLM via HCM-F is:

- HLM checks to see if the cluster is eligible to be assigned to ELM.

- PLM checks to see if the cluster is allowed to be added in PLM (only a CUCM cluster with a pub server and CUC cluster can be added into PLM).

- HLM sends a set deployment mode to the UC application web deployment service.

- HLM sends a get deployment in order to verify the mode was set correctly.

- HLM sends a restart request.

- HLM goes into a five minute polling mode, asking the UC application 'is Restart complete'.

- The UC application can take up to 40 minutes, before an HLM timeout.

- Once the UC application has responded with 'restart Complete', HLM sends one more 'get deployment mode' in order to verify the mode.

- HLM now sends a request to force add the cluster into the PLM.

- Every four hours, the HLM audit process checks to see if the UC application is out-of-sync between PLM and HCM-F.

Notes : The UC application reboots as per step 5. HLM contacts the UC application via Service Provide IP and reboot the cluster via the UC application OS admin user/password.

## Verify

Use this section to confirm that your configuration works properly.

In order to verify the UC application is in deployment mode, enter the utils create report platform command in the UC application CLI. CUCM generates the report. Review the report in order to easily verify the deployment mode as per this snippet:

```
<ProductDeploymentMode> <ParamNameText>Deployment Mode for this instance</ParamNameText> <ParamValue>HCS</ParamValue>
```

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

20-Nov-2015

Initial Release

### Contributed by Cisco Engineers

Andrea Cingolani

Cisco TAC Engineer

### This Document Applies to These Products

- Hosted Collaboration Solution (HCS)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 20-Nov-2015 | Initial Release |