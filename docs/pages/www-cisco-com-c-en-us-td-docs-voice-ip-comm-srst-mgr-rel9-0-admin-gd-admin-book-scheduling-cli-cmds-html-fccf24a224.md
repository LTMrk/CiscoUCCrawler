---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-scheduling-cli-cmds-html-fccf24a224
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/scheduling_cli_cmds.html
retrieved_at: 2026-08-21T23:40:16.488279+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 11, 2014

Chapter: Scheduling CLI Commands

## Chapter: Scheduling CLI Commands

- Examples

## Scheduling CLI Commands

Cisco Unified SRST Manager enables you to schedule the execution of a block of CLI commands. Blocks of commands are entered interactively, using a symbol delimiter character to start and stop the execution. The execution of the block of commands begins in EXEC mode, but mode-changing commands are allowed in the command block.

The following limitations apply in Cisco Unified SRST Manager Release 11.0:

- The maximum size of the block of commands is 1024 characters, including new lines.

- Commands in the block cannot use the comma “,” character or the delimiter character. For example, if the delimiter character is configured to be “#”, that character cannot be used in the command blocks.

- Only system administrators can schedule the execution of blocks of commands.

- CLI commands are executed under system super-user privileges.

- Notification for the execution of these command blocks is not available. Error messages and results are available in log files only.

### SUMMARY STEPS

1. kron schedule [ name ]

2. description

3. repeat every { number days at time |number weeks on day | number months on day date | number years on month month } at time

Note Instead of the repeat every command, you can optionally use one of the following commands:

- repeat once at time

- repeat daily at time

- repeat monthly on day date at time

- repeat weekly on day at time

- repeat yearly on month month at time

4. start-date date

5. stop-date date

6. commands delimiter

7. exit

8. show kron schedules

9. show kron schedule detail job

### DETAILED STEPS

Step 1

kron schedule [ name ]

Enters kron schedule configuration mode.

Step 2

description description

srstmgr-1(kron-schedule)# description backup

(Optional) Enters a description for the scheduled kron job.

Step 3

repeat every { number days | number weeks on day | number months on day date | number years on month month } at time time

srstmgr-1(kron-schedule)# repeat every 2 days at time 10:00

Specifies how often a recurring scheduled kron job occurs. To configure a one-time kron job, use the repeat once command. You can also optionally use one of the other repeat commands listed in the previous note.

Step 4

start-date date

srstmgr-1(kron-schedule)# start-date 08/30/2012

Specifies the start date for the recurring scheduled kron job to occur.

Step 5

stop-date date

srstmgr-1(kron-schedule)# stop-date 11/20/2012

Specifies the stop date for the recurring scheduled kron job to occur.

Step 6

Enters an interactive mode where commands in the the command block can be entered for the scheduled kron job. Use the delimiter character to delimit the command block.

Note Any symbol can be a delimiter. The “%” symbol is shown for example purposes only.

Step 7

exit

Exits kron schedule configuration mode.

Step 8

show kron schedules

srstmgr-1# show kron schedule

Displays a list of scheduled kron jobs.

Step 9

show kron schedule detail job name

srstmgr-1# show kron schedule detail job kron1011

Displays information about a specific scheduled kron job.

### Examples

The following is sample output from the show kron schedules command:

The following is sample output from the show kron schedule detail job command:

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | kron schedule [ name ] srstmgr-1# kron schedule kron1011 | Enters kron schedule configuration mode. |
| Step 2 | description description srstmgr-1(kron-schedule)# description backup | (Optional) Enters a description for the scheduled kron job. |
| Step 3 | repeat every { number days \| number weeks on day \| number months on day date \| number years on month month } at time time srstmgr-1(kron-schedule)# repeat every 2 days at time 10:00 | Specifies how often a recurring scheduled kron job occurs. To configure a one-time kron job, use the repeat once command. You can also optionally use one of the other repeat commands listed in the previous note. |
| Step 4 | start-date date srstmgr-1(kron-schedule)# start-date 08/30/2012 | Specifies the start date for the recurring scheduled kron job to occur. |
| Step 5 | stop-date date srstmgr-1(kron-schedule)# stop-date 11/20/2012 | Specifies the stop date for the recurring scheduled kron job to occur. |
| Step 6 | commands delimiter srstmgr-1(kron-schedule)# commands % Enter CLI commands to be executed. End with the character ‘%’. Maximum size is 1024 characters, it may not contain symbol %. %show version show running-config config t hostname aaa % srstmgr-1(kron-schedule)# | Enters an interactive mode where commands in the the command block can be entered for the scheduled kron job. Use the delimiter character to delimit the command block. Note Any symbol can be a delimiter. The “%” symbol is shown for example purposes only. |
| Step 7 | exit | Exits kron schedule configuration mode. |
| Step 8 | show kron schedules srstmgr-1# show kron schedule | Displays a list of scheduled kron jobs. |
| Step 9 | show kron schedule detail job name srstmgr-1# show kron schedule detail job kron1011 | Displays information about a specific scheduled kron job. |