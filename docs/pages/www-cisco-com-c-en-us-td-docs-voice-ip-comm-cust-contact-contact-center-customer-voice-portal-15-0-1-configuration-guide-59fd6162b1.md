---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-configuration-guide-59fd6162b1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/configuration/guide/ccvp_b_1501-configuration-guide-for-cisco-customer-voice-portal-release/java_runtime_environment_minor_update.html
retrieved_at: 2026-08-21T12:07:41.951396+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: December 12, 2025

Chapter: Java Runtime Environment Minor Update

## Chapter: Java Runtime Environment Minor Update

- Java Runtime Environment Minor Update

- Java Runtime Environment Minor Update

# Java Runtime Environment Minor Update

## Java Runtime Environment Minor Update

Use the JREUpdate.bat script to install a minor update of Java Runtime Environment (JRE) version on your Unified CVP Server.
                              For example, you can install a minor update of JRE version 17.0.13 to 17.0.14.

Download the JREUpdate.zip from the following location: https://software.cisco.com/download/home/270563413/type

The script does not support a major upgrade of JRE versions. For example, the script does not allow a major upgrade of JRE
                                          Version 17.0.13 to 19.

For Unified CVP 15.0(1) and higher releases, only Redhat OpenJDK JREs have to be used for further upgrades.

Step 1

Download and install the preferred Java Development Kit (JDK) version on your personal machine at https://www.openlogic.com/openjdk-downloads?field_java_parent_version_target_id=416&field_operating_system_target_id=436&field_architecture_target_id=All&field_java_package_target_id=All

Step 2

Copy the JRE folder from the installed JDK to a known location on the Unified CVP Server. For example, C:\JRE .

The jre folder is available in the JDK root folder. For example: C:\jdk17.0.13\jre .

Step 3

Right-click the JREUpdate.zip file and extract the files to a known location on your Unified CVP Server. For example, C:\Cisco\CVP\bin .

Step 4

Run this script from the command prompt: C:\Cisco\CVP\bin >JREUpdate.bat apply C:\JRE .

Step 5

Reboot the Unified CVP server.

Step 6

Ensure that the script output displays the updated JRE version.

| Note | The script does not support a major upgrade of JRE versions. For example, the script does not allow a major upgrade of JRE
                                          Version 17.0.13 to 19. |
|---|---|

| Note | For Unified CVP 15.0(1) and higher releases, only Redhat OpenJDK JREs have to be used for further upgrades. |
|---|---|

| Step 1 | Download and install the preferred Java Development Kit (JDK) version on your personal machine at https://www.openlogic.com/openjdk-downloads?field_java_parent_version_target_id=416&field_operating_system_target_id=436&field_architecture_target_id=All&field_java_package_target_id=All |
|---|---|
| Step 2 | Copy the JRE folder from the installed JDK to a known location on the Unified CVP Server. For example, C:\JRE . Note The jre folder is available in the JDK root folder. For example: C:\jdk17.0.13\jre . | Note | The jre folder is available in the JDK root folder. For example: C:\jdk17.0.13\jre . |
| Note | The jre folder is available in the JDK root folder. For example: C:\jdk17.0.13\jre . |
| Step 3 | Right-click the JREUpdate.zip file and extract the files to a known location on your Unified CVP Server. For example, C:\Cisco\CVP\bin . |
| Step 4 | Run this script from the command prompt: C:\Cisco\CVP\bin >JREUpdate.bat apply C:\JRE . The script runs and Unified CVP JRE is updated to the new version. |
| Step 5 | Reboot the Unified CVP server. |
| Step 6 | Ensure that the script output displays the updated JRE version. |

| Note | The jre folder is available in the JDK root folder. For example: C:\jdk17.0.13\jre . |
|---|---|