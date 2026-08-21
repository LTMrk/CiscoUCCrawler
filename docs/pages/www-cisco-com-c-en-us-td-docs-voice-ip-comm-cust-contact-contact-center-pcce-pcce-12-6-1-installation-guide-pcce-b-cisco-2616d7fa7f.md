---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-installation-guide-pcce-b-cisco-2616d7fa7f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/installation/guide/pcce_b_cisco_pcce_installationandupgrade_guide_12_6_1/pcce_b_cisco_pcce_installationandupgrade_guide_12_5_2_appendix_01001.html
retrieved_at: 2026-08-21T16:40:35.987939+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Security Considerations

## Chapter: Security Considerations

# Security Considerations

## Java Upgrades

During installations and upgrades, Unified CCE installs the base required Java version.

You can apply Java updates to your contact center as follows:

Apply Java updates for the latest 32-bit Java 8 minor version.

For the most current Java support information, see the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

You can download and install the OpenJDK Java updates from the OpenLogic website.

Modify the Windows CCE_JAVA_HOME environment variable to point to the new OpenJDK Java Runtime Environment (JRE) location if it has changed.

AppDynamics machine agent that is packaged with Unified ICM and Unified CVP uses a separate copy of OpenJDK. Any vulnerability
                                       fix for OpenJDK requires an upgrade of the AppDynamics machine agent. This update is delivered through an engineering special
                                       (ES) for Unified ICM and Unified CVP.

## Upgrade OpenJDKUtility

The Cisco Upgrade OpenJDKUtility:

Upgrades OpenJDK JRE to latest release.

Supports upgrade for both MSI and Zip file formats.

Automatically sets the CCE_JAVA_HOME environment variable to updated version so that Unified CCE applications can employ the
                                 latest OpenJDK version as the Java runtime.

Before using the tool:

Download the OpenJDK installer from the OpenLogic OpenJDK website: https://www.openlogic.com/openjdk . (Both msi and zip formats are supported).

Copy the downloaded file into the Unified CCE component VMs. For Example C:\UpgradeOpenJDKTool .

Download the utility from  and unzip OpenJdkUpgradeTool.zip to any local folder. For example: Download and Unzip under C:\UpgradeOpenJDKTool .

Run openJDKUtility.exe from unziped folder For all the supported commands and for more details, refer to the Readme.html (which is available as part of the OpenJdkUpgradeTool.zip ).

Once the installation is successful, CCE_JAVA_HOME is updated and does not trigger the system reboot.

## Upgrade Tomcat
                        	 Utility

Use the optional
                           		Cisco Upgrade Tomcat Utility to:

Upgrade Tomcat to version 9.0 build releases. (That
                                 					is, only version 9.0 build releases work
                                 					with this tool.) You may choose to upgrade to newer builds of Tomcat release 9.0 to keep up with the
                                 					latest security fixes.

Tomcat uses the following release numbering scheme: Major.minor.build. For example, you can upgrade from 9.0.21 to 9.0.22 . You cannot use this tool for major or minor version upgrades.

Before using the
                           		tool:

Download the Tomcat installer (apache-tomcat-version.exe) from the Tomcat website: http://archive.apache.org/dist/tomcat/tomcat-9/ . Copy the installer onto the Unified CCE component VMs. For Example
                                 					C:\UpgradeTomcatTool.

Download the utility zip file, extract it, and run the batch file to upgrade Tomcat.

Download link:

- <ICM install directory>:\icm\tomcat\logs

- <ICM install directory>:\icm\debug.txt

### Install Tomcat

For detailed information on the results from each step, see the ../UpgradeTomcatResults/UpgradeTomcat.log file.

Stop Unified CCE services on the VM before using the Tomcat Utility.

Step 1

From the command line, navigate to the directory where you copied the Upgrade Tomcat Utility.

Step 2

Enter this command to run the tool: tomcatutility.bat .

Step 3

When prompted, enter the full pathname of the Tomcat installer version you want
                                          to use.

```
c:\tomcatInstaller\apache-tomcat-9.0.21.exe
```

Step 4

When prompted, enter yes to continue with the install.

Step 5

Repeat these steps for all unified CCE component VMs.

| Note | AppDynamics machine agent that is packaged with Unified ICM and Unified CVP uses a separate copy of OpenJDK. Any vulnerability
                                       fix for OpenJDK requires an upgrade of the AppDynamics machine agent. This update is delivered through an engineering special
                                       (ES) for Unified ICM and Unified CVP. |
|---|---|

| Note | Stop Unified CCE services on the VM before using the Tomcat Utility. |
|---|---|

| Step 1 | From the command line, navigate to the directory where you copied the Upgrade Tomcat Utility. |
|---|---|
| Step 2 | Enter this command to run the tool: tomcatutility.bat . |
| Step 3 | When prompted, enter the full pathname of the Tomcat installer version you want
                                          to use. For example: c:\tomcatInstaller\apache-tomcat-9.0.21.exe |
| Step 4 | When prompted, enter yes to continue with the install. |
| Step 5 | Repeat these steps for all unified CCE component VMs. Note If the latest installed Tomcat does not work properly, install the previous working version using the Tomcat utility by following
                                                      the above-mentioned steps. | Note | If the latest installed Tomcat does not work properly, install the previous working version using the Tomcat utility by following
                                                      the above-mentioned steps. |
| Note | If the latest installed Tomcat does not work properly, install the previous working version using the Tomcat utility by following
                                                      the above-mentioned steps. |

| Note | If the latest installed Tomcat does not work properly, install the previous working version using the Tomcat utility by following
                                                      the above-mentioned steps. |
|---|---|