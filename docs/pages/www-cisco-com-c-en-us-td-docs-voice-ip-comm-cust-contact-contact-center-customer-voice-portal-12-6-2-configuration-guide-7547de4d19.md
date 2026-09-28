---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-configuration-guide-7547de4d19
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/configuration/guide/ccvp_b_1262-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp_b_configuration-guide-12-0_chapter_010110.html
retrieved_at: 2026-08-21T11:58:42.982719+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(2)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(2)

Updated: April 28, 2023

Chapter: Java Runtime Environment Minor Update

## Chapter: Java Runtime Environment Minor Update

- Java Runtime Environment Minor Update

- Java Runtime                              	 Environment Minor Update

# Java Runtime Environment Minor Update

## Java Runtime
                        	 Environment Minor Update

Use the JREUpdate.bat script to install a minor update of Java Runtime Environment (JRE) version on your Unified CVP Server. For example, you can
                              install a minor update of JRE version 1.8.0_275 to 1.8.0_x.

The script does not support a major upgrade of JRE versions. For example, the script does not allow a major upgrade of JRE
                                          Version 1.8 to 1.9/1.10.

From 12.6(1) ES-12 and higher releases, only OpenLogic OpenJDK is supported.

Step 1

Download and unzip the Java Development Kit (JDK) folder on your CVP machine.

Step 2

Copy the JRE folder from the JDK root folder to a known location on the Unified CVP Server. For example, C:\JRE .

The jre folder is available in the JDK root folder. For example: C:\openlogic-openjdk-8u332-b09-windows-64\jre .

Step 3

Go to the bin folder within the JDK root folder. For example C:\openlogic-openjdk-8u332-b09-windows-64\bin . Copy the jconsole application file and paste it in the path mentioned in Step 2 ( C:/JRE ).

Step 4

Go to the lib folder within the JDK root folder. For example C:\openlogic-openjdk-8u332-b09-windows-64\lib . Copy the jconsole executable jar file and paste it in the same path mentioned in Step 2 ( C:/JRE ).

Step 5

Go to C:/Cisco/CVP/bin and right-click the JREUpdate.zip file and extract the files to a known location on your Unified CVP Server. For example, C:\Cisco\CVP\bin .

Step 6

Run this script from the command prompt: C:\Cisco\CVP\bin >JREUpdate.bat apply C:\JRE .

Step 7

Reboot the Unified CVP server.

Step 8

Ensure that the script output displays the updated JRE version.

| Note | The script does not support a major upgrade of JRE versions. For example, the script does not allow a major upgrade of JRE
                                          Version 1.8 to 1.9/1.10. |
|---|---|

| Note | From 12.6(1) ES-12 and higher releases, only OpenLogic OpenJDK is supported. |
|---|---|

| Step 1 | Download and unzip the Java Development Kit (JDK) folder on your CVP machine. |
|---|---|
| Step 2 | Copy the JRE folder from the JDK root folder to a known location on the Unified CVP Server. For example, C:\JRE . Note The jre folder is available in the JDK root folder. For example: C:\openlogic-openjdk-8u332-b09-windows-64\jre . | Note | The jre folder is available in the JDK root folder. For example: C:\openlogic-openjdk-8u332-b09-windows-64\jre . |
| Note | The jre folder is available in the JDK root folder. For example: C:\openlogic-openjdk-8u332-b09-windows-64\jre . |
| Step 3 | Go to the bin folder within the JDK root folder. For example C:\openlogic-openjdk-8u332-b09-windows-64\bin . Copy the jconsole application file and paste it in the path mentioned in Step 2 ( C:/JRE ). |
| Step 4 | Go to the lib folder within the JDK root folder. For example C:\openlogic-openjdk-8u332-b09-windows-64\lib . Copy the jconsole executable jar file and paste it in the same path mentioned in Step 2 ( C:/JRE ). |

| Note | The jre folder is available in the JDK root folder. For example: C:\openlogic-openjdk-8u332-b09-windows-64\jre . |
|---|---|

| Step 5 | Go to C:/Cisco/CVP/bin and right-click the JREUpdate.zip file and extract the files to a known location on your Unified CVP Server. For example, C:\Cisco\CVP\bin . |
|---|---|
| Step 6 | Run this script from the command prompt: C:\Cisco\CVP\bin >JREUpdate.bat apply C:\JRE . The script runs and Unified CVP JRE is updated to the new version. |
| Step 7 | Reboot the Unified CVP server. |
| Step 8 | Ensure that the script output displays the updated JRE version. |