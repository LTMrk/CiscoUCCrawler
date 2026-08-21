---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-hosted-collaboration-solution-hcs-200122-how-to-set-calling-li-9459f4e9b0
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/hosted-collaboration-solution-hcs/200122-How-to-set-Calling-Line-ID-Presentation.html
retrieved_at: 2026-08-21T13:54:39.693721+00:00
---

How to set Calling Line ID Presentation Name and Calling Line ID Presentation Number to Restricted using CUCDM

# How to set Calling Line ID Presentation Name and Calling Line ID Presentation Number to Restricted using CUCDM

### Download Options

Updated: September 8, 2015

Document ID: 200122

Contents

## Contents

## Introduction

This document describes the modus operandi to configure Calling Line ID Presentation Name feature and Calling Line ID Presentation Number feature to Restricted using Cisco Unified Domain Manager (CUCDM).

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUCDM

- Cisco Unified Communications Managers (CUCM)

### Components Used

The information in this document is based on these software and hardware versions:

- CUCDM  8.1 and above

- CUCM version 8 and above

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

Using the default models, CUCDM ignores the settings you define for Calling Line ID Presentation Name feature and Calling Line ID Presentation Number feature under the Add Number Translation section (General Administration/Number Translation).

## Configure

- In CUCDM, navigate to General Administration/Number Translation/Add Number Translation sect ion .

Set the Calling Line ID Presentation Name and Calling Line ID Presentation Number to Restricted.This pushes the translation pattern on CUCM.

- When the translation pattern is created on CUCM, it sets the CLI preferences to Default as opposed to Restricted.

- In CUCM, you can see the Pattern OK albeit with an incorrect Calling Line ID Presentation Name feature and Calling Line ID Presentation Number feature . The traces show that CUCDM is sending Default preference instead of Restricted preference for the respective parameter.

### Configuration Example

```
<pattern>811XXXXX</pattern>
 <routePartitionName>InterSiteRoutingPT</routePartitionName>
 <routeFilterName></routeFilterName> 

 addTransPattern : 
 <transPattern> 
 <pattern>811XXXXX</pattern>
 <description></description>
 <usage>Translation</usage> 
 <routePartitionName>InterSiteRoutingPT</routePartitionName>
 <blockEnable>false</blockEnable> 
 <calledPartyTransformationMask></calledPartyTransformationMask>
 <callingPartyTransformationMask></callingPartyTransformationMask> 
 <useCallingPartyPhoneMask>Off</useCallingPartyPhoneMask>
 <callingPartyPrefixDigits></callingPartyPrefixDigits>
 <dialPlanName></dialPlanName>
 <dialPlanWizardGenId></dialPlanWizardGenId>
 <messageWaiting>Wink</messageWaiting> 
 <networkLocation>OnNet</networkLocation>
 <patternUrgency>false</patternUrgency> 
 <prefixDigitsOut></prefixDigitsOut>
 <routeFilterName></routeFilterName>
 <callingLinePresentationBit>Default</callingLinePresentationBit> 
 <callingNamePresentationBit>Default</callingNamePresentationBit>
 <provideOutsideDialtone>false</provideOutsideDialtone>
 <callingSearchSpaceName>IncomingToSite-CSS60</callingSearchSpaceName>
 <routeNextHopByCgpn>false</routeNextHopByCgpn>
 <releaseClause>Call Rejected</releaseClause> 
 </transPattern>
```

This is the offending parameter:

```
<callingLinePresentationBit>Default</callingLinePresentationBit>
<callingNamePresentationBit>Default</callingNamePresentationBit>
```

This is by design. The values selected in the CLI drop down, when adding a number. Translation has no direct impact on the Route Patterns or Translate Patterns. Instead, it is used to populate two substitution variables:

- #CLIRORCLIPNUMBER#

- #CLIRORCLIPNAME#

Only if these variables are used in the Feature Configuration Template elements, the dropdown settings will have any influence on the actual CUCM provisioning.

In order to overcome this, add the following parameters in the model:

- Calling Line Presentation - #CLIRORCLIPNUMBER#

- Calling Name Presentation -  #CLIRORCLIPNAME#

After this, you can use the CLID settings on the Add Number Translation field.

## Verify

Rerun the transaction from CUCDM and verify whether the appropriate values have been pushed into the CUCM for Calling Line Presentation and Calling Name Presentation features.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Revision History

1.0

21-Apr-2016

Initial Release

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- Hosted Collaboration Solution (HCS)

- Unified Communications Manager (CallManager)

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 21-Apr-2016 | Initial Release |