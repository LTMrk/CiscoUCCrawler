---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-configuration-gui-899c105f2e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/configuration/guide/ccvp_b_configuration-guide-12-5-1/ccvp_b_configuration-guide-12-0_chapter_010110.html
retrieved_at: 2026-08-21T17:08:34.263383+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.5(1)

Updated: January 31, 2020

Chapter: Java Runtime Environment Minor Update

## Chapter: Java Runtime Environment Minor Update

- Java Runtime Environment Minor Update

- Java Runtime                              	 Environment Minor Update

# Java Runtime Environment Minor Update

## Java Runtime
                        	 Environment Minor Update

Use the JREUpdate.bat script to install a minor update of Java Runtime Environment (JRE) version on your Unified CVP Server.
                              For example, you can install a minor update of JRE version 1.8.0_275 to 1.8.0_x.

Download the JREUpdate.zip from the following location:

https://software.cisco.com/download/release.html?mdfid=270563413&softwareid=280840592&release=10.5%281%29&relind=AVAILABLE&rellifecycle=&reltype=latest

The script does not support a major upgrade of JRE versions. For example, the script does not allow a major upgrade of JRE
                                          Version 1.8 to 1.9/1.10.

For 12.5(1a) installation, only Redhat OpenJDK JREs have to be used for further upgrades.

If FIPS is enabled in the system, disable FIPS before doing any JRE updates.

After installing the JRE Migration ES on top of 12.5(1) release, only Redhat OpenJDK JREs have to be used for further upgrades.

ES 26 onwards, the JRE in the CVP is updated with OpenLogic JRE. Specific changes, if any, in configuration files of the JRE
                                          folder should be backed up and reconfigured after the JRE update.

After installing ES 26, only Openlogic OpenJDK minor version upgrades are allowed.

Step 1

Download and install the preferred Java Development Kit (JDK)
                                       			 version on your personal machine.

Step 2

Copy the JRE folder from the installed JDK to a known location on
                                       			 the Unified CVP Server. For example, C:\JRE .

The jre folder is available in the JDK root folder. For example: C:\jdk1.8.0_275\jre .

Step 3

Right-click the JREUpdate.zip file and extract the files to a
                                       			 known location on your Unified CVP Server. For example, C:\Cisco\CVP\bin .

Step 4

Run this script from the command prompt: C:\Cisco\CVP\bin >JREUpdate.bat apply C:\JRE .

Step 5

Ensure that the script output displays the updated JRE version.

| Note | The script does not support a major upgrade of JRE versions. For example, the script does not allow a major upgrade of JRE
                                          Version 1.8 to 1.9/1.10. |
|---|---|

| Note | For 12.5(1a) installation, only Redhat OpenJDK JREs have to be used for further upgrades. If FIPS is enabled in the system, disable FIPS before doing any JRE updates. |
|---|---|

| Note | After installing the JRE Migration ES on top of 12.5(1) release, only Redhat OpenJDK JREs have to be used for further upgrades. |
|---|---|

| Note | ES 26 onwards, the JRE in the CVP is updated with OpenLogic JRE. Specific changes, if any, in configuration files of the JRE
                                          folder should be backed up and reconfigured after the JRE update. After installing ES 26, only Openlogic OpenJDK minor version upgrades are allowed. |
|---|---|

| Step 1 | Download and install the preferred Java Development Kit (JDK)
                                       			 version on your personal machine. |
|---|---|
| Step 2 | Copy the JRE folder from the installed JDK to a known location on
                                       			 the Unified CVP Server. For example, C:\JRE . Note The jre folder is available in the JDK root folder. For example: C:\jdk1.8.0_275\jre . | Note | The jre folder is available in the JDK root folder. For example: C:\jdk1.8.0_275\jre . |
| Note | The jre folder is available in the JDK root folder. For example: C:\jdk1.8.0_275\jre . |
| Step 3 | Right-click the JREUpdate.zip file and extract the files to a
                                       			 known location on your Unified CVP Server. For example, C:\Cisco\CVP\bin . |
| Step 4 | Run this script from the command prompt: C:\Cisco\CVP\bin >JREUpdate.bat apply C:\JRE . The script runs and Unified CVP JRE is updated to the new
                                       			 version. |
| Step 5 | Ensure that the script output displays the updated JRE version. |

| Note | The jre folder is available in the JDK root folder. For example: C:\jdk1.8.0_275\jre . |
|---|---|