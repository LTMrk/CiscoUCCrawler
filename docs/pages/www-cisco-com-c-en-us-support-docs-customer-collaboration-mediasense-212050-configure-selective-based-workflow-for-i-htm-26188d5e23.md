---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-mediasense-212050-configure-selective-based-workflow-for-i-htm-26188d5e23
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/mediasense/212050-Configure-Selective-Based-Workflow-for-I.html
retrieved_at: 2026-08-21T06:41:55.196080+00:00
---

Configure Selective Based Workflow for Incoming Calls on Finesse

# Configure Selective Based Workflow for Incoming Calls on Finesse

Updated: September 14, 2017

Document ID: 212050

Contents

## Contents

## Introduction

This document describes how to configure a Finesse workflow to record inbound calls to MediaSense.

## Prerequisites

### Requirements

Cisco recommends you have the knowledge of these topics:

- Cisco Unified Contact Center Express (UCCX) with recording licenses

- Finesse

- MediaSense

- Cisco Unified Communications Manager (CUCM)

### Components Used

- UCCX 10.6

- CUCM 10.5

- MediaSense 11.0

- Cisco Unified CCX Editor

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### Configurations

#### CUCM Configuration

Step 1. Navigate to Device > Device Settings > SIP Profile

- Select Add New

- Provide a Name: MediaSense11

- Under SIP Options Ping : Enable OPTIONS Ping to monitor destination status for Trunks with Service Type None (Default)

Step 2.  Navigate to Select Device > Trunk in the Unified CM Administration > Add New

- Trunk Type: SIP Trunk

- Device Protocol: SIP

- Select Run On All Active Unified CM Nodes radio button

- Under SIP Information Destination Address , enter MediaSense IP address with default 5060

- SIP Trunk Security Profile : Non Secure SIP Trunk Profile

- SIP Profile : MediaSense11

Step 3. Navigate to Call Routing > Route/Hunt > Route Group

- Add New

- Give it a name: MediaSense11RouteGroup

- Add MediaSense11 to Selected Devices under Current Route Group Members

Step 4. Navigate to Call Routing > Route/Hunt > Route List in the Unified CM Administration

- Add Name RouteListMediaSense11

- Under Route List Memeber Information > Selected Groups add: MediaSense11RouteGroup

- Select Run On All Active Unified CM Nodes radio button.

Step 5. Navigate to Call Routing > Route/Hunt > Route Pattern

- Add Route Pattern: 5111

- Do not include any wildcard characters when you create route patterns for the recording profile

Step 6. Navigate to Device > Device Settings > Recording Profile

- Provide the name MediaSense11Recording Profile

- Recording Destination Address is 5111

Step 7. Navigate Device > Phone

- Select the phone

- Find the Built In Bridge configuration for this and select On

- Access the Directory Number Configuration page for the line to be recorded

- Recording Option: Selective Call Recording Enabled

- Recording Profile: MediaSense11Recording Profile

- Recording Media Source: Phone Preferred

Note: Step 7 needs to be completed on all agent that will be recorded.

Step 8. Navigate U ser Management > Application User

- Add New

- Provide a name: MediaSense11AXL

Tip:At this point if you dial 5111 a you hear it ring once, then you hear silence. This means you can move on to MediaSense Configuration

#### MediaSense Configuration

Step 1. Log in to Cisco MediaSense Administration

- https://FQDN/oraadmin/Welcome.do

- Navigate to Administrator > CM Configuration

- Add Callmanager to Selected AXL Service Providers and Selected Call Control Service Providers

- Provide the Username and Password of the application user created in CUCM

Step 2. Select Tab Cisco Finesse Administration

- Enter the Primary Cisco Finesse Server IP or Hostname

- Enter the Secondary Cisco Finesse Server IP or Hostname

Step 3. Navigate to MediaSense API User Configuration

- Enter the users that access MediaSense search and manage recordings

Step 4. Navigate to Incoming Call Configuration

- Add New

- Under rule add the IP Address of CUCM and set Action to Record Audio Only

#### UCCX Script Configuration

Step 1. Open Cisco Unified CCX Editor application

- File > New > Select the Queuing Tab > Select Simple_Queuing

Step 2. Create a variable called Calltype

- Type: String

- Name: Calltype

- Value: use quotes as in the image

Step 3 . Add Set under the Accept Step

- Set can be found under General tab

- Variable: Calltype

- Value: incoming

Step 4. Add Set Enterprise Call Info step under the Set Calltype = incoming

- The Set Enterprise Call Info can be found under the Call Contact tab

- Right click on Set Enterprise Call Info > Properties

- Values: Calltype

- Name: Call.PeripheralVariable1

- Tokens: Leave as ALL

Step 5. The overall demo script looks like this:

#### Finesse Administration Configuration

Step 1. Navigate to Finesse Administration : https://FQDN or IP address:8445/cfadmin/container/?locale=en_US

Step 2. Navigate to Call Variables Tab .

- Under Call Body Left-Hand Column Layout  set Display name to equal Calltype. Set the variable to equal callVariable1.

- Ensure callVariable1 is only assigned once and that must be to Calltype

Step 3. Navigate to the Workflows tab

- Under the Manage Workflow Actions select New

- Add the following parameters seen in the below image.

- URL must be equal

```
/finesse/api/Dialog/${dialogId}
```

- Body must have this code:

```
<Dialog>
<requestedAction>START_RECORDING</requestedAction>
<targetMediaAddress>${extension}</targetMediaAddress>
</Dialog>
```

Step 4. Navigate to the Workflows Tab

- Under Manage Workflows select New

- When to perform Actions needs to equal When a Call is answered

- How to apply Conditions needs to equal If all Conditions are met

- Here callVariable1 + Is equal to + incoming

- Select the workflow you created under Manage workflow Actions

Step 5. Navigate to Team Resources tab

- Select the team that needs to only record inbound calls and not outbound calls

- Select the Workflows tab

- Add the workflow created in step 4

## Verify

- Agent user: kev7

- Agent extension: 5007

- CTI rout point: 8460

- Non agent extensionl DN: 9000

### Scenario 1. Incoming call does record

Phone 9000 dials CTI route Point 8460 > Agent 7 with extension 5007 answers the call. Because the call came via the script and Calltype equals incoming the MSrecordings workflow initiates and MediaSense records the call.

1. The image shows the Calltype is equal to incoming

2. Active recording in MediaSense shows the call currently recorded

### Scenario 2 Outbound call does not record

Outbound call from agent kev7 is not record. This is only true if agents do not call the CTI Route point 8460.

1. Agent kev7 with extension 5007 calls DN 9000 directly

2. "Active calls" In MediaSense is blank

## Troubleshoot

1. Activate persistent Logging.

- Navigate to: https://FQDN:8445/desktop/locallog

- Select Sign In With Persistent Logging

- Reproduce the incoming or outgoing call.

- Enter https://FQDN:8445/desktop/locallog again.

- Use the persistent desktop logs to search for the workflow that is created.

If early offer SIP INVITES are used, you can see this ERROR: Zero Size Tracks on recordings in the Search and Play page. Disable Early Offer support for voice and video calls in SIP profile on CUCM to resolve this issue.

### Revision History

1.0

14-Sep-2017

Initial Release

### Contributed by Cisco Engineers

Kevin Sheppard

Cisco TAC Engineer

Juanita Roda

Cisco TAC Engineer

Pavan Dave

Cisco TAC Engineer

### This Document Applies to These Products

- Finesse

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 14-Sep-2017 | Initial Release |