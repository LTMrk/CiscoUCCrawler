---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-installation-guide-pcce-b-cisco-89a6dc4b48
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/installation/guide/pcce_b_cisco-pcce-installationandupgrade-guide-12_5/pcce_b_cisco-pcce-installationandupgrade-guide-12_5_appendix_01100.html
retrieved_at: 2026-08-21T16:39:34.572541+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

Updated: April 3, 2021

Chapter: Security Considerations

## Chapter: Security Considerations

# Security Considerations

## Java Upgrades

In 12.5(1), after the initial release, CCE transitioned from Oracle to OpenJDK for the Java runtime environment. Newer installs
                           and upgrades with 12.5(1a) base installer run with OpenJDK JRE while the older installs and upgrades with 12.5(1) base run
                           with Oracle JRE. Existing 12.5(1) deployments will transition to OpenJDK with 12.5(1) ES55, which in turn is a mandatory prerequisite
                           for receiving further maintenance patches on CCE.

During installations and upgrades, Unified CCE installs the base required Java version.

Before updating the Java Runtime Environment (JRE):

Run the command at the command prompt: cd %CCE_JAVA_HOME%\bin .

Important

Export the certificates of all the components imported into the truststore.

Enter the truststore password when prompted.

You can apply Java updates to your contact center as follows:

You can apply Java updates for the latest 32-bit Java 8 minor version.

For the most current Java support information, see the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

You can download and install the Oracle Java updates from the Oracle website and the OpenJDK Java updates from the OpenLogic
                                 website.

Modify the Windows CCE_JAVA_HOME 1 environment variable to point to the new OpenJDK Java Runtime Environment (JRE) location if it has changed.

After updating the OpenJDK Java Runtime Environment (JRE):

Run the command at the command prompt: cd %CCE_JAVA_HOME%\bin .

Important

Import the certificates for all the components that you previously exported from the truststore before you updated the JRE.

Enter the truststore password when prompted.

Enter 'yes' when prompted to trust the certificate.

## Upgrade OpenJDKUtility

The Cisco Upgrade OpenJDKUtility:

Upgrades OpenJDK JRE to latest release.

Supports upgrade for both MSI and Zip file formats.

Automatically sets the CCE_JAVA_HOME environment variable to updated version so that Unified CCE applications can employ the
                                 latest OpenJDK version as the Java runtime.

Before using the tool:

Download the OpenJDK installer from the OpenLogic OpenJDK website: https://www.openlogic.com/openjdk . (Both msi and zip formats are supported).

Copy the downloaded file into the Unified CCE component VMs. For Example C:\UpgradeOpenJDKTool .

Download the utility from https://software.cisco.com/download/home/284360381/type/284416107/release/12.5(1) and unzip OpenJdkUpgradeTool.zip to any local folder. For example: Download and Unzip under C:\UpgradeOpenJDKTool .

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

Download link: https://software.cisco.com/download/home/284360381/type/284416107/release/12.5(1) If you are in CCE Release 12.5(2), download tomcat utility 12.5(2). Follow steps mentioned in Tomcat Utility 12.5(2) for upgrade or revert options in 12.5(2)

- <ICM install directory>:\icm\tomcat\logs

- <ICM install directory>:\icm\debug.txt

### Upgrade Tomcat

For detailed information on the results from each step, see the ../UpgradeTomcatResults/UpgradeTomcat.log file.

Stop Unified CCE services on the VM before using the Tomcat Utility.

Step 1

From the
                                          			 command line, navigate to the directory where you copied the Upgrade Tomcat
                                          			 Utility.

Step 2

Enter this command to run the tool: tomcatutility.bat -upgrade .

Step 3

When prompted,
                                          			 enter the full pathname of the new Tomcat installer.

```
c:\tomcatInstaller\apache-tomcat-9.0.21.exe
```

Step 4

When prompted,
                                          			 enter yes to continue with the upgrade.

Step 5

Repeat these
                                          			 steps for all unified CCE component VMs.

### Revert
                           	 Tomcat

For detailed
                                 		  information on the results from each step, see the
                                 		  ../UpgradeTomcatResults/UpgradeTomcat.log file.

Stop Unified CCE services on the VM before using the Tomcat Utility.

Step 1

From the
                                          			 command line, navigate to the directory where you copied the Upgrade Tomcat
                                          			 Utility.

Step 2

Enter this command to run the tool: tomcatutility.bat -revert .

Step 3

When prompted,
                                          			 enter yes to continue with the reversion.

Step 4

Repeat these
                                          			 steps for all unified CCE component VMs.

### Tomcat Utility 12.5.2

If you are on 12.5(2), perform the following steps to upgrade or to revert tomcat version. For detailed information on the
                                 results from each step, see the ../UpgradeTomcatResults/UpgradeTomcat.log file.

Stop Unified CCE services on the VM before using the Tomcat Utility.

Step 1

From the command line, navigate to the directory where you copied the Upgrade Tomcat Utility.

Step 2

Enter the command tomcatutility.bat -upgrade -noconfirm <full path to tomcat installer> to run the tool: .

To revert to older version of tomcat, execute same command with path to older tomcat installer.

Step 3

Repeat the steps for all CCE solutions.

| Important | Use JAVA_HOME if you are employing Oracle JRE. |
|---|---|

| Important | Use JAVA_HOME if you are employing Oracle JRE. |
|---|---|

| Note | Stop Unified CCE services on the VM before using the Tomcat Utility. |
|---|---|

| Step 1 | From the
                                          			 command line, navigate to the directory where you copied the Upgrade Tomcat
                                          			 Utility. |
|---|---|
| Step 2 | Enter this command to run the tool: tomcatutility.bat -upgrade . |
| Step 3 | When prompted,
                                          			 enter the full pathname of the new Tomcat installer. For example: c:\tomcatInstaller\apache-tomcat-9.0.21.exe |
| Step 4 | When prompted,
                                          			 enter yes to continue with the upgrade. |
| Step 5 | Repeat these
                                          			 steps for all unified CCE component VMs. |

| Note | Stop Unified CCE services on the VM before using the Tomcat Utility. |
|---|---|

| Step 1 | From the
                                          			 command line, navigate to the directory where you copied the Upgrade Tomcat
                                          			 Utility. |
|---|---|
| Step 2 | Enter this command to run the tool: tomcatutility.bat -revert . |
| Step 3 | When prompted,
                                          			 enter yes to continue with the reversion. |
| Step 4 | Repeat these
                                          			 steps for all unified CCE component VMs. |

| Note | Stop Unified CCE services on the VM before using the Tomcat Utility. |
|---|---|

| Step 1 | From the command line, navigate to the directory where you copied the Upgrade Tomcat Utility. |
|---|---|
| Step 2 | Enter the command tomcatutility.bat -upgrade -noconfirm <full path to tomcat installer> to run the tool: . Note To revert to older version of tomcat, execute same command with path to older tomcat installer. | Note | To revert to older version of tomcat, execute same command with path to older tomcat installer. |
| Note | To revert to older version of tomcat, execute same command with path to older tomcat installer. |
| Step 3 | Repeat the steps for all CCE solutions. |

| Note | To revert to older version of tomcat, execute same command with path to older tomcat installer. |
|---|---|