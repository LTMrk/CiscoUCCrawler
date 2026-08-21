---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-218377-configure-call-forwarding-selective-for-h-5083cbfec9
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/218377-configure-call-forwarding-selective-for.html
retrieved_at: 2026-08-21T07:15:45.547740+00:00
---

Configure Call Forwarding Selective for Webex Calling

# Configure Call Forwarding Selective for Webex Calling

### Download Options

Updated: April 6, 2023

Document ID: 218377

Contents

## Contents

## Introduction

This document describes the basic functionality of Call Forwarding Selective for Auto Attendant and Call Queue and provides some examples.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Basic understanding of features such as Auto Attendant, Call Queue, and Scheduling

- Have admin roles in the organization

- Have a clear understanding of what must be configured

- Active Telephone Number assigned to the desired features

### Components Used

The information in this document is based on Control Hub.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

This document describes the basic functionality of Call Forwarding Selective for Auto Attendant and Call Queue and provides some examples. Note that the solutions presented for the examples are not the only way to achieve the goal. The value of these examples is their simplicity and practical use.

Webex Calling has the option to create Auto Attendant and Call Queue. These features allow you to organize groups of agents that receive calls based on the configuration.

Note : After you check your Call Forwarding selective configuration, there are multiple criteria set in the Call Forwarding Selective for the Auto Attendant. The criteria are checked based on the order they are listed. In this case, Business Hours come prior to the Holiday. Thus, when the system checks for Business Hours first, and if it satisfies the condition, it no longer checks the next criteria. It is suggested that you update the criteria name with numbers so that the Holiday criteria are checked first. For example, 01_Holiday, 02_Business, and so on.

## Call Queue

For these examples, you must have a hunt group that works as follows:

- During Business Hours: Incoming Calls are routed to Call Queue agents.

- After Business Hours (from 5:00 PM to 09:00 AM of the next day): Incoming calls routed to the voicemail of a particular user.

The best way to accomplish this is to create a Selective forward rule for the PM schedule (5:30 PM to 11:59 PM) in order to cover the after-hours for that day, and a Selective forward rule for the non-working hours of the next day (12:00 AM to 8:59 AM). Both must forward any calls to voicemail.

### Scheduling

You must create two schedules for this example:

- Afterhours that cover the rest of the day after Business Hours: 5:30 PM to 11:59 PM. This is 'PM Forwarding'.

- Afterhours that cover the time before Business Hours: 12:00 AM to 8:59 AM. This is 'AM Forwarding'.

Step 1. In order to create the two schedules, you must navigate to the Location of the Hunt group and Scheduling .

Step 2. Choose Add Schedule .

Step 3. Create the PM forwarding schedule as shown in this image:

Step 4. Click Save .

Step 5. Create the AM forwarding schedule as shown in this image:

Step 6. If you do not work on Saturday and Sunday, you must apply the rule from 12:00 AM to 11:59 PM. This applies the forwarding for the entire day.

Step 7. Click Save .

Note : If the Schedule for Call Forwarding Selective (for Afterhours), ends at 8:59 AM, calls made after 08:59 AM, for example, at 08:59:01 AM, calls do not trigger the call forwarding and instead calls are routed to Business Hours.

### Call Forward Selective

Assign the schedules to the Call Queue in the section Call Forwarding Selective.

Step 1. Navigate to Call queue and Call Forwarding .

Step 2. Choose Selectively Forward Calls . You must choose the phone number to which the calls are forwarded. You must check the voicemail option if you like to send calls to voicemail.

Step 3. Choose Edit for the first schedule.

Step 4. Choose the schedule you created for the rule. In this case, AM Forwarding .

Step 5. There is no Holiday schedule chosen (otherwise, it is mandatory to create a new rule, specific to Holidays).

Step 6. The forward to is set to the default number chosen in the Call Forwarding.

Step 7. Calls from any number are applied for the rule.

Step 8. Click Save .

Step 9. You must accomplish the same for the PM schedule.

Step 10. Choose Save .

The Call Forwarding is shown in this image:

Step 11. Choose Save .

## Auto Attendant

You must have an Auto Attendant that works as follows:

- During Business Hours: the Auto Attendant menu is played.

- After Business Hours (from 5:00 PM to 09:00 AM of the next day): Incoming calls routed to the voicemail of a particular user.

The best way to accomplish this is to create a Selective forwarding selective, similar to the earlier Call Queue example.

Note : Auto Attendant already has a Schedule configured. You must ensure the Selective call forwarding schedule does not overlap.

Step 1. In your Auto Attendant, choose Schedule .

In this example, the Schedule is set to Monday to Friday from 9:00 AM to 5:00 PM.

### Scheduling

You must create two schedules for this example:

- Afterhours that cover the rest of the day after Business Hours: 5:01 PM to 11:59 PM. This is 'PM Forwarding'.

- Afterhours that cover the time before Business Hours: 12:00 AM to 8:59 AM. This is 'AM Forwarding'.

Step 1. You must navigate to the Location of the Auto Attendant and choose Scheduling .

Step 2. Choose Add Schedule and create the PM forwarding schedule.

Note : It is important not to overlap. You must start at 05:01 PM as the AA schedule ends at 5:00 PM.

Step 3. Choose Save .

Step 4. Create AM Schedule, for the time 12:00 AM to 8:59 AM.

Step 5. Choose Save .

Note : If the Schedule for call forwarding selective (for Afterhours), ends at 8:59 AM, the calls made after 08:59 AM, for example, at 08:59:01 AM, calls do not trigger the call forwarding and instead calls are routed to Business Hours.

### Call Forward Selective

Assign the Schedules to the Auto Attendant Call forwarding Selective.

Step 1. Navigate to Auto Attendant and choose Call Forwarding .

Step 2. Enable it and choose Selectively Forward Calls .

Step 3. Choose the user you need the calls to be forwarded to and check the Send to voicemail option, so the calls go straight to voicemail.

Step 4. Add the schedule AM Forwarding and choose the schedule you created earlier.

Step 5. There is no Holiday schedule chosen (otherwise, it is mandatory to create a new rule specific to Holidays).

Step 6. Add the PM schedule.

Step 7. There is no Holiday schedule chosen (otherwise, it is mandatory to create a new rule specific to Holidays).

Step 8. The Auto Attendant scheduled settings are shown in this image:

## Holiday

The best way to have a forwarding selective for specific Holidays is to create a separate rule.

Here is the same example as used for Auto Attendant.

You want the Auto Attendant calls forwarded to another number during Holidays with this schedule:

- During Christmas Eve

- During the last two weeks of November

The easiest way to achieve this is to create a Selective forwarding selective with a Holiday schedule.

### Scheduling

Step 1. Navigate to the Location of the Auto Attendant and create a schedule for the Holiday. Choose Scheduling .

Step 2. Click Add Schedule .

Step 3. Name the Holiday Schedule and choose the type as Holiday .

Step 4. Create the Holiday for Christmas and choose All Day and By Date .

Note: In this example, you chose yearly Recurrence . However, if you use either Recurrence or None in this field, the feature works just well.

Step 5. Click Save .

Step 6. Create the Holiday for the last two weeks of November under the same Schedule.

Step 7. Choose the dates you want to use. In this example, November 21 to November 30 covers the 'last 2 weeks of November'.

Step 8. Click Save .

Step 9. The image shows this result:

### Call Forward Selective

Assign the Schedules to the Auto Attendant Call forwarding Selective.

Step 1. Navigate to Auto Attendant and choose Call Forwarding .

Step 2. Since you created the rules for PM and AM, you can click Add When to Forward to create your new rule for Holiday.

Step 3. Choose Every Day All Day along with the Holiday Schedule you created for the location.

Step 4. You must verify that the Holiday schedule is correct:

Step 5. Click Save .

Now the Auto Attendant not only has a forwarding selective for the Afterhours but also for specific Holidays.

## Related Information

### Revision History

2.0

06-Apr-2023

Initial Release

1.0

01-Nov-2022

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 06-Apr-2023 | Initial Release |
| 1.0 | 01-Nov-2022 | Initial Release |