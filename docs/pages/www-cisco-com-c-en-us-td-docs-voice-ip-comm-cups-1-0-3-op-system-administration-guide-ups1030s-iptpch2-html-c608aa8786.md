---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-3-op-system-administration-guide-ups1030s-iptpch2-html-c608aa8786
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_3/op_system/administration/guide/ups1030s/iptpch2.html
retrieved_at: 2026-08-21T02:48:11.340215+00:00
---

Cisco Unified Communications Operating System Administration Guide For Cisco Unified Presence Server Release 1.0(3)

# Cisco Unified Communications Operating System Administration Guide For Cisco Unified Presence Server Release 1.0(3)

Updated: February 21, 2007

Chapter: Log Into Cisco Unified Communications Operating System Administration

## Chapter: Log Into Cisco Unified Communications Operating System Administration

- Logging Into Cisco Unified Communications Operating System Administration

- Recovering the Administrator Password

## Log Into Cisco Unified Communications Operating System Administration

This chapter describes the procedure for accessing the Cisco Unified Communications Operating System Administration and also provides procedures for recovering a lost password.

## Logging Into Cisco Unified Communications Operating System Administration

To access Cisco Unified Communications Operating System Administration and log in, follow this procedure:

Step 1 Log in to Cisco Unified Presence Server Administration.

Step 2 From the Navigation menu in the upper, right corner of the Cisco Unified Presence Server Administration window, choose Cisco Unified OS Administration and click Go .

The Cisco Unified Communications Operating System Administration Logon window displays.

Note You can also access Cisco Unified Communications Operating System Administration directly by entering the following URL: http:// server-name /iptplatform.

Step 3 Enter your Administrator username and password.

Note The Administrator username and password get established during installation or created using the command line interface.

Step 4 Click Submit.

The Cisco Unified Communications Operating System Administration window displays.

## Recovering the Administrator Password

If you lose the Administrator password and cannot access the system, use the following procedure to reset the Administrator password.

Note During this procedure, you will be required to remove and then insert a valid CD or DVD in the disk drive to prove that you have physical access to the system.

Step 1 Log in to the system with the following username and password:

• Username: pwrecovery

• Password: pwreset

The Welcome to admin password reset window displays.

Step 2 Press any key to continue.

Step 3 If you have a CD or DVD in the disk drive, remove it now.

Step 4 Press any key to continue.

The system tests to ensure that you have removed the CD or DVD from the disk drive.

Step 5 Insert a valid CD or DVD into the disk drive.

The system tests to ensure that you have inserted the disk.

Step 6 After the system verifies that you have inserted the disk, you get prompted to enter a new Administrator password.

Note The system resets the Administrator username to admin . If you want to set up a different Administrator username and password, use the CLI command set password . For more information, see Appendix A, "Command Line Interface."

Step 7 Reenter the new password.

The system checks the new password for strength. If the password does not contain enough different characters, you get prompted to enter a new password.

Step 8 After the system verifies the strength of the new password, the password gets reset, and you get prompted to press any key to exit the password reset utility.