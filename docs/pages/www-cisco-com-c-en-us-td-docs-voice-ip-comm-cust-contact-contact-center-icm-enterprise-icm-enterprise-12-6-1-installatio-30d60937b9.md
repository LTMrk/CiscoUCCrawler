---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-installatio-30d60937b9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/installation/guide/ucce_b_cti-os-system-manager-guide12-6-1/ucce_b_cti-os-system-manager-guide12-5_chapter_0101.html
retrieved_at: 2026-08-16T20:04:16.262816+00:00
---

CTI OS System Manager Guide for Cisco Unified ICM, Release 12.6(1)

# CTI OS System Manager Guide for Cisco Unified ICM, Release 12.6(1)

Updated: May 12, 2021

Chapter: CTI OS Component Installation

## Chapter: CTI OS Component Installation

# CTI OS Component Installation

## Silent Installation
                        	 of CTI OS Components

CTI OS
                              		  supports installation of some CTI OS components in unattended silent install
                              		  mode. Silent install is supported for the following components:

CTI OS Agent and
                                    				Supervisor Desktops.

CTI OS Server.

You must be aware of the following for CTI OS silent installation of
                                          			 the CTI OS agent and supervisor desktops:

You must install .NET 4.7.1 prior to silent installation.

You can install only CTI OS agent and supervisor desktops of CTI
                                                				  OS Client; you cannot silently install other CTI OS Client installation
                                                				  options.

Only fresh silent installation is supported. You must uninstall
                                                				  all previous versions or patches of CTI OS Client prior to silently installing
                                                				  the CTI OS Client.

Security is not installed when you install Client phones
                                                				  silently. If you need security, run SecuritysetupPackage.exe from the installation
                                                				  CD after you complete the installation.

Silent install is not supported for CTI OS Security Server and Client.

The silent
                              		  installation process involves two tasks:

Creating a
                                    				response file.

Using the
                                    				response file to run CTI OS silent install on other machines.

Warning

Use of silent installations is discouraged, as errors encountered during the install process may go unnoticed and leave the
                                          system in an invalid state. If you choose to run installations silently, be absolutely certain that you manually perform the
                                          required pre- and post-installation instructions on the target systems.

### Create a Response File

The process of creating a response file for use with the CTI OS
                                 		  silent install installs all CTI OS components (CTI OS
                                 		  Agent Desktop, CTI OS Supervisor Desktop, CTI OS Server) that exist on the
                                 		  machine where the response file is recorded. To create a response file for use
                                 		  with the CTI OS silent install, perform the following steps.

Step 1

From a command prompt, go to the directory where the CTI OS installation setup.exe file is  located.

Step 2

Run setup with the following option: setup.exe /r .

Step 3

After the installation is complete, examine the setup log file to
                                          			 verify that installation ran to completion with no errors.

Caution

It is critical that you verify that the installation process ran
                                                         				  successfully and created a valid response file. Running the CTI OS silent install
                                                         				  with an invalid response file can leave your system in an invalid state.

Step 4

Reboot your system.

### Run CTI OS Silent Install on Other Machines

After you create a response file on one machine, you can use
                                 		  that response file to run the CTI OS silent install on other machines. To do this,
                                 		  perform the following steps.

Step 1

On the machine or machines on which you want to run
                                          			 CTI OS silent install, copy the response file ( setup.iss ) to the same directory where setup.exe is located.

Step 2

Run the setup with the following syntax: setup.exe /s .

Step 3

When the installation is complete, examine the setup log file to
                                          			 verify that installation ran to completion with no errors.

Caution

It is critical that you verify that the installation process ran
                                                         				  successfully and created a valid response file. Running CTI OS silent install
                                                         				  with an invalid response file can leave your system in an invalid state.

Step 4

Reboot your system.

## Uninstall
                        	 Components

To
                              		  uninstall the CTI OS components, rerun the Setup program for the previous
                              		  release and delete the Unified ICM Customer Instance that you specified during
                              		  CTI OS component setup.

## Recover from Failed
                        	 Installation of CTI OS

If an
                              		  attempted CTI OS installation fails for reasons such as power failure, disk
                              		  error, or other similar circumstances, perform the following procedures to
                              		  recover from the failed installation.

Step 1

Uninstall the
                                       			 release, as documented in Uninstall
                                          				components. .

Step 2

Reinstall the
                                       			 release by performing the procedures documented in the following sections:

Install CTI OS Server .

Run Silent Monitor Service Installer .

Additional Configuration Steps .

| Note | You must be aware of the following for CTI OS silent installation of
                                          			 the CTI OS agent and supervisor desktops: You must install .NET 4.7.1 prior to silent installation. You can install only CTI OS agent and supervisor desktops of CTI
                                                				  OS Client; you cannot silently install other CTI OS Client installation
                                                				  options. Only fresh silent installation is supported. You must uninstall
                                                				  all previous versions or patches of CTI OS Client prior to silently installing
                                                				  the CTI OS Client. Security is not installed when you install Client phones
                                                				  silently. If you need security, run SecuritysetupPackage.exe from the installation
                                                				  CD after you complete the installation. |
|---|---|

| Note | Silent install is not supported for CTI OS Security Server and Client. |
|---|---|

| Warning | Use of silent installations is discouraged, as errors encountered during the install process may go unnoticed and leave the
                                          system in an invalid state. If you choose to run installations silently, be absolutely certain that you manually perform the
                                          required pre- and post-installation instructions on the target systems. |
|---|---|

| Step 1 | From a command prompt, go to the directory where the CTI OS installation setup.exe file is  located. |
|---|---|
| Step 2 | Run setup with the following option: setup.exe /r . This outputs a file called setup.iss to the < drive >:\Windows directory. |
| Step 3 | After the installation is complete, examine the setup log file to
                                          			 verify that installation ran to completion with no errors. Caution It is critical that you verify that the installation process ran
                                                         				  successfully and created a valid response file. Running the CTI OS silent install
                                                         				  with an invalid response file can leave your system in an invalid state. | Caution | It is critical that you verify that the installation process ran
                                                         				  successfully and created a valid response file. Running the CTI OS silent install
                                                         				  with an invalid response file can leave your system in an invalid state. |
| Caution | It is critical that you verify that the installation process ran
                                                         				  successfully and created a valid response file. Running the CTI OS silent install
                                                         				  with an invalid response file can leave your system in an invalid state. |
| Step 4 | Reboot your system. |

| Caution | It is critical that you verify that the installation process ran
                                                         				  successfully and created a valid response file. Running the CTI OS silent install
                                                         				  with an invalid response file can leave your system in an invalid state. |
|---|---|

| Step 1 | On the machine or machines on which you want to run
                                          			 CTI OS silent install, copy the response file ( setup.iss ) to the same directory where setup.exe is located. |
|---|---|
| Step 2 | Run the setup with the following syntax: setup.exe /s . |
| Step 3 | When the installation is complete, examine the setup log file to
                                          			 verify that installation ran to completion with no errors. Caution It is critical that you verify that the installation process ran
                                                         				  successfully and created a valid response file. Running CTI OS silent install
                                                         				  with an invalid response file can leave your system in an invalid state. | Caution | It is critical that you verify that the installation process ran
                                                         				  successfully and created a valid response file. Running CTI OS silent install
                                                         				  with an invalid response file can leave your system in an invalid state. |
| Caution | It is critical that you verify that the installation process ran
                                                         				  successfully and created a valid response file. Running CTI OS silent install
                                                         				  with an invalid response file can leave your system in an invalid state. |
| Step 4 | Reboot your system. |

| Caution | It is critical that you verify that the installation process ran
                                                         				  successfully and created a valid response file. Running CTI OS silent install
                                                         				  with an invalid response file can leave your system in an invalid state. |
|---|---|

| Step 1 | Uninstall the
                                       			 release, as documented in Uninstall
                                          				components. . |
|---|---|
| Step 2 | Reinstall the
                                       			 release by performing the procedures documented in the following sections: Install CTI OS Server . Run Silent Monitor Service Installer . Additional Configuration Steps . |