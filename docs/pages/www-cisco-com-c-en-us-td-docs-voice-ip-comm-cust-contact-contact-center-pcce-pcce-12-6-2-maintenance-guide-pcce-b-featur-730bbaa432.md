---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-2-maintenance-guide-pcce-b-featur-730bbaa432
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_2/maintenance/guide/pcce_b_features-guide-1262/pcce_b_features-guide-1261_chapter_0101.html
retrieved_at: 2026-08-21T12:28:29.273047+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(2)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 12.6(2)

Updated: November 15, 2024

Chapter: Business Hours

## Chapter: Business Hours

# Business Hours

## Business Hours Overview

Business hours are the working hours during which you conduct business. You can create and modify business hours and set weekly
                              and daily schedules for each business hour. You can create different business hour schedules for regular working days and
                              holidays. You can also open or close the business hours if there is an emergency.

You can define the status reasons for business hours and assign codes for each status reason. Status reason is required when
                              you force open or force close a business hour, and when you add special hours and holidays.

### Contact Center Enterprise Reference Design Support for Business Hours

Packaged CCE supports Business Hours for these reference designs:

2000 Agents

4000 Agents

12000 Agents

## Business Hours Use Cases

Use the Business Hours feature to manage the incoming customer calls or digital channel communications , by routing these contacts based on the Business Hours you configure.

Use the Business Hour status in an IF node in scripts to control the call and digital channel contacts, such as email and
                              chat, and notify the customers accordingly.

You can have Business Hours scripts for the following treatments:

When the business is open, route calls and digital contacts to the applicable skill groups and precision queues.

When the business is closed, play the message for the closed status with the appropriate Status Reason and terminate the call.
                                    Route the digital contacts to the appropriate queues.

When the business is not open 24x7, route the calls to skill groups and precision queues for after-hours support or play the
                                    after-hours message.

When the business is open 24x7, at a predefined time before the end of each shift, route the calls and digital contacts to
                                    the appropriate queues for the next shift.

When the business is closed for an emergency on a working day, notify the customers contacting your contact center appropriately
                                    about the emergency closing.

Based on reason code and status, the customers will hear appropriate prompts on the call.

## Set the Principal AW for Business Hours

You must specify and set the Principal AW before configuring the Business Hours.

The Principal AW (Admin Workstation) is responsible for managing background tasks that are run periodically to sync configuration
                                 with other solution components, such as SSO management, Smart Licensing, etc.

Step 1

In Unified CCE Administration, go to Infrastructure > Inventory .

Step 2

Click the AW that you want to set as Principal AW .

Step 3

Select the Principal AW check box.

Step 4

Enter the Unified CCE Diagnostic Framework Service domain, username, and password.

The credential must be of a domain user who is a member of the local administrator group if ADSecurityGroupUpdate registry key in AW is zero. If ADSecurityGroupUpdate registry key is set to 1, then the user must be available in the Config security group under the instance OU. These credentials
                                          must be valid on all CCE components in your deployment (routers, PGs, AWs, and so on).

Every time the Active Directory credentials are updated, the credentials configured here must be updated as well.

Step 5

Click Save .

Step 6

Restart Tomcat service on Principal AW machine.

## Business Hours Set Up Workflow

This section provides information necessary to set up the Business Hours feature.

Tasks

Documentation

Scripting for Business Hours

Business Hours Variables and Dynamic Formula for Business Hours in the Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html

Business Hours Configuration

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

### Scripting for Business Hours

To enable scripting for Business Hours, use the following variables:

Business Hour Status—The real time status based on the configured Business Hours.

Reason Code— The reason code associated with the current status.

These variables must be  used in the CCE script IF node to route the customer contacts.

### Business Hours Configuration

Business hours can be configured by defining the following:

Default Open/Close (as per Business Calendar) : The status of the regular hours.

Force Open : Force the status of Business Hours to Open with a reason code.

Force Closed : Force the status of Business Hours to Closed with a reason code.

24x7 setting: Set the schedules for 24x7 working. Status is Always Open.

Special Hours & Holiday : Configure a holiday or
                                    special day. On a holiday, you can close the Business Hours for the whole
                                    day or open it for specific hours. On a special day, you can configure extra
                                    working hours (in cases where 24x7 working is not set), the evaluation stops
                                    when the Special Hours & Holiday step is evaluated and the status is
                                    derived from this step. Further Business Hours setting for that day will not
                                    be evaluated.

Custom : Configure the regular working hours for a weekday and, if necessary, specify the working hours for each day in a week.

The following variables control this feature:

Time Zone : The line of Business or team’s operational time zone.

Reason Code : Reason code for special days and Force Open/Close status.

Apply the appropriate reason codes when you configure a Business Hour with Force Open , Force Close , and Special Hours & Holidays . When these Business Hour schedules are in effect, the associated reason code is available in the scripting environment and
                                    the real time reports. Reason Code configuration is not available for regular weekdays. In such cases, the system reports the default open and default close
                                    reason codes.

Department : Associate the business hours to a department so that the change to business hours is restricted to only the user of that
                                    department.

### Configure Yearly Schedules

You can configure and maintain a Business hours calendar for the whole year.

Configure the regular working hours for weekdays.

Configure Special Hours & Holidays schedules for whole year by doing the following:

Add the Special Hours & Holidays details for all the special hours and holidays for the whole year into the CSV template file.

On the Import Special Hours & Holidays page, click Choose File and browse to the special hours and holidays file.

Click Import to upload the file.

After you import the configuration file, the configurations are loaded on the Business Hours page. Validate the configurations.

Click Save .

When you update the configured Business Hours, remove any elapsed schedules and then update the new schedules for any new
                                          special hours or holidays in a Business Hour configuration.

### Daylight Saving Time

The Business Hours feature uses Time Zone to determine the status based on the Business Hours configured. Time Zone is set based on the local time. When the daylight saving time (DST) settings are applicable to any Time Zone , the status is automatically adjusted for DST.

In case, any new Timezone definition is added or updated at the Windows Operating System (OS) through patch, apply that OS
                                          patch at both Side A and Side B at the same time.

### Business Hours Status Evaluation

The status is evaluated using the following order of the configured Business Hour settings:

Force Open or Close

Special Hours and Holiday schedule

Open/Close as per Business Calendar

The evaluation terminates at the step at which the status is determined.

For example, if Special Hours & Holidays is configured, the evaluation stops when the Special Hours & Holiday step is evaluated and the status is derived from this step.

If any configuration is changed, the status is re-evaluated and updated to reflect the change.

| Step 1 | In Unified CCE Administration, go to Infrastructure > Inventory . |
|---|---|
| Step 2 | Click the AW that you want to set as Principal AW . The Edit CCE AW window opens. |
| Step 3 | Select the Principal AW check box. |
| Step 4 | Enter the Unified CCE Diagnostic Framework Service domain, username, and password. The credential must be of a domain user who is a member of the local administrator group if ADSecurityGroupUpdate registry key in AW is zero. If ADSecurityGroupUpdate registry key is set to 1, then the user must be available in the Config security group under the instance OU. These credentials
                                          must be valid on all CCE components in your deployment (routers, PGs, AWs, and so on). Note Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. | Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
| Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
| Step 5 | Click Save . |
| Step 6 | Restart Tomcat service on Principal AW machine. |

| Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
|---|---|

| Tasks | Documentation |
|---|---|
| Scripting for Business Hours | Business Hours Variables and Dynamic Formula for Business Hours in the Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html |
| Business Hours Configuration | Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html |

| Note | When you update the configured Business Hours, remove any elapsed schedules and then update the new schedules for any new
                                          special hours or holidays in a Business Hour configuration. |
|---|---|

| Note | In case, any new Timezone definition is added or updated at the Windows Operating System (OS) through patch, apply that OS
                                          patch at both Side A and Side B at the same time. |
|---|---|