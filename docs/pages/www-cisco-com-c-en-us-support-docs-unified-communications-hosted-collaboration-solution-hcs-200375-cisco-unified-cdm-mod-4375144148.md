---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-hosted-collaboration-solution-hcs-200375-cisco-unified-cdm-mod-4375144148
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/hosted-collaboration-solution-hcs/200375-Cisco-Unified-CDM-Model-that-Supports-Ma.html
retrieved_at: 2026-09-01T14:58:51.695058+00:00
---

Cisco Unified CDM Model that Supports Macros

# Cisco Unified CDM Model that Supports Macros

### Download Options

Updated: May 25, 2016

Document ID: 200375

Contents

## Contents

## Introduction

This document describes how macros are used to return the data from a system in various formats. They not only test the conditions and map the data from GUI or bulk loader input to various elements in the system (in conjunction with configuration templates) but are also used to access the data in workflow and wizard steps.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on these software and hardware versions:

- Cisco Unified Communications Domain Manager (Unified CDM) 10.6.X

- Cisco Unified Communications Managers (CUCM) 10.5.2 or later

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Which model supports macros?

In general all the Cisco Unified CDM  models use macros within their workflows. Any Configuration Template (CFT), Feature Display Policy (FDP), etc that are already available in the Cisco Hosted Collaboration Solution (HCS) admin or provider admin account can be changed in the production system, this includes the usage of macros in these FDP/CFT. The CFTs can be cloned from sys to sys.hcs.Provider and modified in order to meet the customer requirements.Any changes done without the clone creation at lower hierarchy, are lost during an upgrade.

Not every model accepts the macros'  input through API/ bulk load sheets unless the CFT’s value are specified as fn.evaluate, as then CFT evaluates the macro and uses the value. Moreover, a customer can implement a macro with or without the evaluation in order to meet the customer requirements

## Configuration Example: CFT field without field Macro Evaluation

- Log in as hcsadmin user

- Bread crumb to your provider hierarchy

- As shown in the image, navigate to Role Manager > Configuration Template and then search for a CFT template that needs to be customized

- As shown in the image, select the CFT and clone it to show it up at a provider level

- Open the new CFT

- Now as shown in the image, add your Macro without evaluation. In the example, a macro in the Ldap Directory Name is applied

In this scenario, the field is simply evaluated on the basis of macro contents. For example, the Ldap Directory Name in the Cisco Unified Communications Manager (CUCM) User Template CFT: {{ macro.HcsDpCustomerName }}-LDAP, it takes the CustomerName field from the appropriate BaseCustomerDAT tuple (HcsDpCustomerName) and tack –LDAP on it regardless of what is passed in the input context (from API/bulk load) for that field.

## Configuration Example: CFT field with field Macro Evaluation

Macro evaluation is input through API's/ bulk load sheets, it is supported by certain fields within the most CFT. Moreover, this evaluation is further supported only if the CFT attribute includes embedded fn.evaluate in the input context.

For example, the Description field of HcsCucPartitionCFT from the compiled xls list supports the evaluation as fn.evaluate command is passed in the input test.

In this case, an API invoker populates this field with an embedded macro such as: Description for {{ input.PartitionItem.description }}; resulting in a value of Description for ThisExamplePartitionItem assuming PartitionItem.description == "ThisExamplePartitionName".

Without the embedded fn.evaluate (the crucial piece in supporting the embedded macros), the value field simply resolves as originally seen -- Description for {{ input.PartitionItem.description }}.

In the previous example, if one wants to enable the evaluation in the Name field it will be necessary to modify the macro in  {{ fn.evaluate input.PartitionName.Data }}.

This image shows the CFT(s) list and attributes with the evaluation already enabled macro.

## How to check the Macro function correctly?

- Log in as sysadmin

- Launch the macro evaluator

The macro evaluator can be used to evaluate macros while executing the macro to the correct hierarchy. For example, the phone macro at site level shows the phones provisioned in the site, as shown in the image.

### Revision History

1.0

25-May-2016

Initial Release

### Contributed by Cisco Engineers

Andrea Cingolani

Cisco TAC Engineer

### This Document Applies to These Products

- Hosted Collaboration Solution (HCS)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 25-May-2016 | Initial Release |