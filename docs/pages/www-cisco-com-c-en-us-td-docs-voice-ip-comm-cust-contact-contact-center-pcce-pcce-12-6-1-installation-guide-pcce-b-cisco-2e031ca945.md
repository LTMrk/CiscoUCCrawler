---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-installation-guide-pcce-b-cisco-2e031ca945
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/installation/guide/pcce_b_cisco_pcce_installationandupgrade_guide_12_6_1/pcce_b_cisco_pcce_installationandupgrade_guide_12_5_2_chapter_0111.html
retrieved_at: 2026-08-21T16:40:14.336544+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(1)

Updated: May 14, 2021

Chapter: Upgrade Overview

## Chapter: Upgrade Overview

# Upgrade Overview

Following are the two supported upgrade methods:

Common Ground Upgrades : The Common Ground method is an in-place upgrade performed on your existing virtual machine which involves upgrading the
                              Packaged CCE and all other associated software hosted on it. If your hardware meets the requirements for this release, you
                              can perform a Common Ground upgrade without acquiring additional hardware.

CCE components can be upgraded using common ground or technology refresh upgrade.

Common Ground Upgrade is not supported if the platform upgrade from Windows Server 2016 and SQL Server 2017 to Windows Server
                                                2019 and SQL Server 2019 is planned as part of upgrade process.

Technology Refresh Upgrades : Use the Technology Refresh upgrade method to set up all the virtual machines (VMs) or the required set of VMs on a different
                              hardware. You can also upgrade the solution components and the associated software hosted on it.

For better performance, Media Routing PG (MR PG), Dialer, and Agent PG should be on the same VM.

## Upgrade Flow

### Upgrade Flowcharts for 2000 Agent Deployments

The following diagram illustrates the solution-level upgrade flow for the Packaged CCE 2000 Agent Deployment solution upgrade.

This flowchart is not applicable for redundant upgrade workflow.

The following diagrams illustrate the stages of the component-level upgrade flows for the Packaged CCE 2000 Agent Deployment solution upgrade. Each diagram covers one of the stages. The letter at the end of each flow indicates
                              the start of the next flow that you are required to perform.

### Upgrade Flowcharts for 4000 Agents and above Deployments

The following diagram illustrates the solution-level upgrade flow for the Packaged CCE 4000 Agents and above Deployment solution
                              upgrade.

The following diagrams illustrate the stages of the component-level upgrade flows for the Packaged CCE 4000 Agents and above
                              Deployment solution upgrade. Each diagram covers one of the stages. The letter at the end of each flow indicates the start
                              of the next flow that you are required to perform.

## Silent
                        	 Upgrade

There are situations when silent upgrade can be used in running an installation wizard. You can
                              				run a silent installation while performing a fresh install or an upgrade.

For more information, see Silent Installation .

## Custom Truststore to Store Component Certificates

Starting Unified CCE 12.6(x), a new custom truststore is created under the Unified ICM Installation directory <ICM install directory>\ssl\cacerts to store all the component certificates. With this new custom truststore, you don't need to export and import the certificates
                           each time Java is updated in the system.

After upgrading from Unified CCE 12.5(x) to Unified CCE 12.6(x), you should export the certificates from the Java truststore
                           to the custom truststore under the Unified ICM Installation directory <ICM install directory>\ssl\cacerts .

Export the certificate from the Java truststore:

Run the command at the command prompt: cd %JAVA_HOME%\bin .

Important

Export the certificates of all the components imported into the truststore.

Enter the truststore password when prompted.

Import the certificate to the custom truststore:

Run the command at the command prompt: cd %CCE_JAVA_HOME%\bin .

Import the certificates for all the components that you exported from the Java truststore.

Enter the truststore password when prompted.

Enter 'yes' when prompted to trust the certificate.

| Note | CCE components can be upgraded using common ground or technology refresh upgrade. Common Ground Upgrade is not supported if the platform upgrade from Windows Server 2016 and SQL Server 2017 to Windows Server
                                                2019 and SQL Server 2019 is planned as part of upgrade process. |
|---|---|

| Note | For better performance, Media Routing PG (MR PG), Dialer, and Agent PG should be on the same VM. |
|---|---|

| Note | This flowchart is not applicable for redundant upgrade workflow. |
|---|---|

| Important | Use CCE_JAVA_HOME if upgrading from Unified CCE 12.5(1a) or Unified CCE 12.5(1) with ES55 (mandatory OpenJDK ES). |
|---|---|