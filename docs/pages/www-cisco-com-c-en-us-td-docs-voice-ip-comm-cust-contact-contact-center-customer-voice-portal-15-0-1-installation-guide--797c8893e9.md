---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-installation-guide--797c8893e9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/installation/guide/ccvp_b_1501_installation-upgrade-guide-cisco-unified-customer-voice-portal/ccvp_b_install_and_upgrade_12-5_chapter_010.html
retrieved_at: 2026-08-21T03:01:02.773348+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: April 30, 2025

Chapter: Unified CVP
	 Installation

## Chapter: Unified CVP
	 Installation

# Unified CVP
                     	 Installation

Cisco Unified Customer Voice Portal (CVP) ISO image contains the setup files for all the CVP components in the CVP folder.

Only a local administrator must install the Unified CVP software.

Before you install Unified CVP, refer to the licensing information in the Unified CVP Licensing chapter.

Ensure that the server chosen for Reporting Server is part of a workgroup.

Important

A new Unified CVP 15.0(1) base installer is now available for customers, which has OpenJDK JRE (v17.0.18) as the supporting Java runtime for the Unified
                                    CVP application. This is an upgrade from the previous Unified CVP 12.5(1b) installer, where OpenJDK JRE (1.8.x) was installed
                                    as the Java runtime environment on the Unified CVP components.”

Important

In the new 15.0(1) release, CVP Reporting Server has support for IBM Informix version 14.10 FC10W2.

For migrating the Reporting Server from 12.x to 15.0(1), see Migrate Unified CVP Reporting Server .

If you are testing with the self-signed TLS certificates that are generated as a part of the installation, ensure that you
                                    map the CN/SANs on the certificate to the corresponding IP through DNS or host file entries.

In the new 15.0(1) release, TLS ciphers of all the server interfaces of CVP are configured in the sip.properties file.

## Install Unified
                        	 CVP on Virtual Machines

### Before you begin

Disable large receive offload (LRO) for ESXi for virtualization
                                       				platform for Unified CVP.

Install and configure the Unified Computing System (UCS).

Install and boot VMware ESXi.

Ensure that ESXi is configured and reachable over the network.

Download the OVA template.

Step 1

Create the Unified CVP virtual machines using the OVA template.

Step 2

Select the CVP components, as required.

Step 3

Install Windows Server.

Install .Net Framework 3.5 feature from Server Manager before installing CVP components.

Step 4

Install the selected CVP components.

## Install Unified CVP Server

Fresh installation of Unified CVP includes the following voice prompt encode format types—u-law, A-law, and G729 for media
                              files. Default applications also get installed along with media files. Choose the format type as per requirement.

Step 1

Mount Unified CVP ISO, and run setup.exe.

Step 2

Review and
                                       			 accept the license agreement, and click Next .

Step 3

On the Select Package screen, choose the Unified CVP component to install on your computer, and click Next .

Internet Information Server (IIS) is the default Media Server supported by Unified CVP. For details on IIS configuration,
                                                      see the Microsoft documentation.

Step 4

At the Voice
                                          				Prompt Encode Format Type screen, select one of the following
                                       			 options:

U-Law Encoded Wave
                                                   						Format

A-Law Encoded Wave
                                                   						Format

G729 Encoded Wave Format

Step 5

On the Choose Destination Location screen, select the folder where setup will install files. By default, it is C:\Cisco\CVP .

Step 6

On the X.509
                                          				Certificate screen, enter the required information in the form, and
                                       			 click Next .

In the Common Name field, enter the hostname of the server (for example, cvp-server). The field accepts only alphanumeric characters (A-Z, a-z, 0-9), spaces,
                                                         hyphens (-), and underscores (). To re-create the certificates using FQDN in the Common Name field, after installation, refer to the Unified CVP Security chapter in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Step 7

Click Install .

You cannot
                                                      				  cancel the installation when it is in progress.

Step 8

Choose to restart the computer right after the upgrade or to restart it later, and click Finish .

After successful installation, the CVP Call Server Service Startup Type is set to Automatic by default.

### What to do next

Install Operations Console

## Install Operations
                        	 Console

Step 1

Perform Steps 1 to 6 of the Install CVP Server procedure.

Step 2

From the Ready
                                          				to Install the Program screen, review the component that you
                                       			 selected, and click Install .

Step 3

On the Ops
                                          				Console Password screen, in the Password and Password (for
                                          				verification) fields, enter a password and re-enter it for
                                       			 confirmation, and click Next .

Adhere to
                                                      				  the password formation criteria that are listed on the Operations Console
                                                      				  Password screen section.

Operations
                                                      				  Console Administrator and Web Services Administrator (wsmadmin) use the
                                                      				  Operations Console password.

Step 4

Select one of
                                       			 the options to either restart the computer right after installation or later,
                                       			 and click Finish .

### What to do next

Install Remote Operations

## Install Remote
                        	 Operations

Step 1

Perform Steps 1 to 4 of the Install Operations Console procedure.

Step 2

Choose to restart the computer right after the upgrade or to restart it later, and click Finish .

### What to do next

Install Reporting Server

## Install Second Drive on Reporting Server Virtual Machine

Step 1

Right-click My Computer > Manage .

Step 2

In Storage section, click Disk Management .

Step 3

Select the unformatted partition, which is usually Disk 1 .

Step 4

Right-click Online , and initialize the disk.

Step 5

Click Format , and follow the formatting process with NTFS.

## Install Unified CVP Reporting Server

IBM Informix database server 12.10 FC3 14.10 FC10W2 is installed as part of the Unified CVP Reporting Server.

The ImagePath for CVP Reporting Informix IDS Service in Windows registry is set to c:\db\Informix\bin\onscpah cvp . Because of this, when security scanners are run, the ImagePath changes to "c:\db\Informix\bin\onscpah cvp" . This results in the CVP Reporting Informix IDS Service not starting.

Workaround : Set ImagePath for CVP Reporting Informix IDS Service in Windows registry to "c:\db\Informix\bin\onscpah" cvp .

### Before you begin

Only the actual Local Administrator (should not be renamed) of this system can install CVP Reporting Server.

Ensure that Unified CVP Reporting Server is not part of any domain and is part of a work group.

Step 1

Mount the Unified CVP ISO image, and run setup.exe file.

Step 2

Review and accept the license agreement, and click Next .

Step 3

On the Select Package screen, select Reporting Server , and click Next .

Step 4

Select the root drive on which you want the Reporting database data and backup data to reside, and click Next .

The Database Size Selection screen appears, providing the following options:

Standard: Requires a minimum of 250GB of free disk space.

Premium: Requires a minimum of 375GB of free disk space.

Step 5

Choose the appropriate database size for the license that you purchased, and click Next .

Step 6

From the Ready to Install the Program window, review the component that you have selected, and click Install .

Step 7

On the Reporting Password window, enter a password and re-enter it for confirmation, and click Next .

Adhere to the password formation criteria that are listed on the Operations Console Password screen section.

The Reporting password requires that the Minimum Password Age parameter be set to 0 days for both the local and/or domain security policy and is subject to both the Unified CVP password
                                                            policy and the password policy enforced by the operating system of the computer on which the Reporting Server resides. For
                                                            each aspect of the password, the Reporting password must meet the requirement of the more restrictive policy. If you are installing
                                                            CVP Reporting Server please ensure that your local and/or domain security policy for MINIMUM PASSWORD AGE are set to 0 days
                                                            for the installation of the CVP Reporting Server component (In Windows, Control Panel > Administrative Tools > Local Security Policy > Account Policy > Password Policy ). If the reporting password you enter is rejected, review the list of password requirements displayed by the installer and
                                                            consider your operating system's password requirements. You can reconfigure this password repeatedly until an acceptable password
                                                            is found.

After installation, add the Unified CVP Reporting Server to the domain, if necessary.

Step 8

Choose to restart the computer right after installation or to restart it later, and click Finish .

## Install Unified
                        	 Call Studio

Important

A new Unified CVP 15.0(1) base installer is now available for customers, featuring OpenJDK JRE (v17.0.13) as the supporting
                                          Java runtime for the Unified CVP application. This is an upgrade from the previous 12.5(1) installer, where OpenJDK JRE (v1.8.x)
                                          was installed as the Java runtime environment on the Unified CVP components.

Step 1

Mount the Unified CVP software (including CVP Studio) installer ISO image (under the Installer_Windows folder), and run setup.exe .

Step 2

On the Welcome screen, click Next .

If you click Cancel here or on the dialog screens that follow before the Ready to Install the Program screen, the installation is canceled. The Exit Setup dialog box appears.

Step 3

Review Copyrights to Products used by Call Studio and click Next .

Step 4

Review and accept the license agreement, and click Next .

Step 5

On the Choose Destination Location screen, select the folder where setup will install files. By default, it is C:\Cisco\CallStudio .

Step 6

On the InstallShield Wizard Complete screen, click Install .

Step 7

Click Finish to exit the wizard.

The Call Studio software is installed on your computer.

The SolarWinds TFTP software and AnyConnect (while a VPN connection is enabled) are the known causes for the Call Studio debugger
                                          errors. To resolve the Call Studio debugger errors:

If you are using SolarWinds, stop the SolarWinds TFTP software and run the debugger.

If you are using AnyConnect, disconnect the VPN connection and run the debugger.

## Install Docker to Run Custom Code on Remote Server

Docker streamlines the deployment and administration of custom code on remote servers, enabling you to generate portable and
                           uniform container images that package your applications and their dependencies. Docker provides advantages like scalability,
                           portability, and consistency when executing custom code on remote servers.

### Install Docker on Windows Host

Follow this sequence of tasks to install the docker engine on the remote server of the windows host:

Setting up this Windows host is a one-time activity and does not need to be repeated for subsequent Docker releases.

Sequence

Task

1

Install Windows Container on Remote Server.

See, Install Windows Containers on Remote Server

2

Install Docker Engine on Remote Server (Windows).

See, Install Docker Engine on Remote Server (Windows)

3

Install Docker Compose Plugin on Remote Server (Windows).

See, Install Docker Compose Plugin on Remote Server (Windows)

4

Install Docker Image on Remote Server (Windows).

See, Install Docker Image on Remote Server (Windows)

#### Install Windows Containers on Remote Server

##### Before you begin

The recommended server version of the host is Windows Server 2022.

The recommended docker engine version of the host is 25.0.1 (and later) and the docker compose plugin version is 2.26.1 (and
                                          later). For more information, refer to the Docker documentation at https://docs.docker.com/engine/release-notes/25.0/ .

Step 1

In the remote server machine, go to Server Manager and open Manage > Add Roles and Features .

Step 2

On the Before You Begin screen, click Next .

Step 3

On the Select Installation Type screen, click Next .

Step 4

On the Select Destination Server screen, click Next .

Step 5

On the Select Server Roles screen, click Next .

Step 6

On the Select Features screen, choose the Containers to install on your computer, and click Next .

Step 7

On the Confirm Installation Selections screen, click Install .

Step 8

Click Close .

Step 9

Restart the server.

##### What to do next

Ensure that the container is installed by running the following command in PowerShell as an administrator:

```
Get-WindowsFeature -Name Containers
```

The Install State displays the status as Installed .

#### Install Docker Engine on Remote Server (Windows)

Complete the following procedure to manually install docker engine on the remote server for the windows host.

##### Before you begin

Refer to the docker documentation at https://docs.docker.com/engine/install/binaries/#install-server-and-client-binaries-on-windows for installing docker on the windows host.

Step 1

Download the latest version of the docker binary package file (.zip) from the location: https://download.docker.com/win/static/stable/x86_64 .

The recommended version for the docker zip file is 25.0.1 (and later).

Step 2

Run the following commands in the PowerShell application to install and extract the archive to your program files on the windows
                                             host:

All PowerShell commands in this procedure must be run in Administrator mode.

```
PS C:\> Expand-Archive  -Path "<Path_to_zip_file>" -DestinationPath $Env:ProgramFiles
```

For example:

```
PS C:\> Expand-Archive -Path "C:\docker\docker-25.0.1.zip" -DestinationPath $Env:ProgramFiles
```

```
PS C:\> &$Env:ProgramFiles\Docker\dockerd --register-service
```

Step 3

Run the following command in the PowerShell application to start the docker service on the windows host:

```
PS C:\> Start-Service docker
```

Verify whether the Docker Engine Service is started in Window Services.

Step 4

Verify that Docker Engine is installed and configured on the remote server for the windows host.

Run the following command in PowerShell application to verify the docker engine is installed on the remote server of the windows
                                                host:

```
&$Env:ProgramFiles\Docker\docker --version
```

For example, the above command shows the version as Docker version v25.0.1 .

#### Install Docker Compose Plugin on Remote Server (Windows)

Complete the following procedure to manually install docker compose plugin on the remote server for the windows host.

##### Before you begin

Refer to the docker documentation at https://docs.docker.com/compose/install/standalone/ for installing docker compose plugin on the windows host.

Step 1

Run the following commands in the PowerShell application on the windows host as Github now uses TLS 1.2:

All PowerShell commands in this procedure must be run in Administrator mode.

```
PS C:\> [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
```

Step 2

Run the following commands in the PowerShell application on the windows host to download the latest release of Compose:

The recommended release version for the docker compose plugin zip file is 2.26.1 (and later).

```
PS C:\> Start-BitsTransfer -Source "<Path_To_File_in_Github>" -Destination $Env:<Destination_Path>
```

For example:

```
PS C:\> Start-BitsTransfer -Source "https://github.com/docker/compose/releases/download/v2.26.1/docker-compose-windows-x86_64.exe" -Destination $Env:ProgramFiles\Docker\docker-compose.exe
```

Step 3

In case of no internet connectivity in the remote server machine, follow the below steps to install docker-compose plugin
                                             on the windows host:

Download the binary docker-compose-windows-x86_64.exe file from the following location: https://github.com/docker/compose/releases/download/v2.26.1/docker-compose-windows-x86_64.exe and copy the file to the C:\ProgramFiles\Docker folder.

Rename the file docker-compose-windows-x86_64.exe to docker-compose.exe

Run the following command in PowerShell application to install the binary file: &$Env:ProgramFiles\Docker\docker-compose.exe .

Step 4

Verify that Docker Compose plugin is installed and configured on the remote server of the windows host.

Run the following command in PowerShell application to verify the docker engine is installed on the remote server of the windows
                                                host:

```
&$Env:ProgramFiles\Docker\docker-compose --version
```

##### What to do next

After installing Docker Engine, set the system variable DOCKER_HOME to the path where Docker is installed.

For example:

Variable Name : DOCKER_HOME

Variable value : C:\Program Files\docker

After the DOCKER_HOME system variable is set, you can run the Docker commands in PowerShell application.

For example:

```
&$Env:DOCKER_HOME\docker images
```

For the changes to take effect after adding a system variable, you need to reopen the PowerShell window as an administrator.

#### Install Docker Image on Remote Server (Windows)

Complete the following procedure to install the docker image on the windows host:

##### Before you begin

Ensure that you have downloaded the customapis-windows-docker-<version>.zip installer zip file.

Step 1

Download or copy the customapis-windows-docker-<version>.zip installer zip file on the windows host.

Step 2

Create the following directory structure on the host: C:\Cisco\customapis .

Step 3

Extract the archive (.zip) to the following location: C:\Cisco\customapis , where you need the Installer to be running from.

Step 4

Open the PowerShell application on the windows host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script.

All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis .

Step 5

Use the launcher.bat file to initiate creation of external mounted folders by providing the create parameter by running the following command:

PS .\launcher.bat create

After you run the command, external mount folder gets created at location: C:\Cisco\customapis

Step 6

Use the launcher.bat file to load the windows docker image and run the container by providing the load parameter by running the following command:

PS .\launcher.bat load

Step 7

Check the status of the container at: http:// <remote_ip_address> :8080/customapis/actuator/health .

UP status means that the container is running.

Step 8

Use the launcher.bat file to view the status of the container by providing the status parameter by running the following command:

PS .\launcher.bat status

##### What to do next

Refer to the chapter "Remote Custom API Server Configuration" of the Configuration Guide fore Unified Customer Voice Portal to run the custom code using remote server on windows host.

### Install Docker on Linux Host

Follow this sequence of tasks to install the docker engine on the remote server of the linux host:

Sequence

Task

1

Install Docker Engine on Remote Server (Linux).

See, Install Docker Engine on Remote Server (Linux)

2

Install Docker Compose Plugin on Remote Server (Linux).

See, Install Docker Compose Plugin on Remote Server (Linux)

3

Install Docker Image on Remote Server (Linux).

See, Install Docker Image on Remote Server (Linux)

#### Install Docker Engine on Remote Server (Linux)

Complete the following procedure to manually install docker engine on the remote server of the Linux host:

To install docker engine on CentOS Linux 7 (core), you can refer to the Docker documentation at https://docs.docker.com/engine/install/centos/ .

##### Before you begin

Ensure that the latest version of CentOS Linux 7 (core) is installed.

Ensure that the docker engine version of the host is 24.0.2 (and later) and the docker compose plugin version is 2.21.0 (and
                                          later). For more information, refer to the Docker documentation at https://docs.docker.com/engine/release-notes/25.0/ .

Step 1

Download the docker package (.rpm) file for the required docker version that you want to install from the following location: https://download.docker.com/linux/centos/7/x86_64/stable/Packages/ .

Step 2

Run the following command to install the docker engine in the relevant path of your download location:

```
$ sudo yum install <Path_to_Docker_Package_File>.rpm
```

```
$ sudo yum install *.rpm
```

In case some dependencies are missing during the installation process, you must identify these dependencies and download the
                                                            necessary .rpm files. Once the required files are downloaded, you must again run the command sudo yum install *.rpm .

Step 3

Verify that Docker engine is installed using the following commands:

```
$ docker --version

$ docker compose version
```

Step 4

Run the following command to start the docker engine:

```
$ sudo systemctl start docker
```

If you want Docker to start automatically after a platform reboot, you can register it with the following command:

```
$ sudo systemctl enable docker
```

Step 5

Verify that the installation of the Docker engine is successful by running the hello-world image using the following command:

```
$ sudo docker run hello-world
```

#### Install Docker Compose Plugin on Remote Server (Linux)

Complete the following procedure to install docker compose plugin on the remote server for the linux host.

##### Before you begin

Refer to the docker documentation at https://docs.docker.com/compose/install/standalone/ for installing docker-compose on the Linux host.

Step 1

Perform Steps 1 to 2 of the Install Docker Engine on Remote Server (Linux) procedure. Refer to the Install Docker Engine on Remote Server (Linux) section for more information.

Step 2

Verify that Docker Compose plugin is installed and configured on the remote server of the linux host using the following command.

```
$ docker compose version
```

#### Install Docker Image on Remote Server (Linux)

Complete the following procedure to install the docker image on the linux host:

##### Before you begin

Ensure that you have downloaded the customapis-docker-linux-<version>.zip installer zip file.

Step 1

Download or copy the customapis-docker-linux-<version>.zip installer zip on the linux host.

Step 2

Create directory the following structure on the host: /usr/local/customapis

Step 3

Run the following command to extract the archive (.zip) to the location: /usr/local/customapis , where you need the Installer to be running from:

```
$ unzip customapis-docker-linux-<version>.zip
```

Step 4

Run the following command to provide permission to the launcher.sh file:

```
$ chmod +x launcher.sh
```

Ensure that you have permissions to directory location: /usr/local/customapis

Step 5

Open the Terminal application on the linux host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script.

Step 6

Use the launcher.sh file to initiate creation of external mounted folders by providing the create parameter by running the following command:

```
$ ./launcher.sh create
```

After you run the command, external mount folder gets created at location: /usr/local/customapis

Step 7

Use the launcher.sh file to load the windows docker image and run the container by providing the load parameter by running the following command:

```
$ ./launcher.sh load
```

Step 8

Check the status of the container at: http:// <remote_ip_address> :8080/customapis/actuator/health .

UP status means that the container is running.

Step 9

Use the launcher.sh file to view the status of the container by providing the load parameter by running the following command:

```
$ ./launcher.sh status
```

##### What to do next

Refer to the chapter "Remote Custom API Server Configuration" of the Configuration Guide fore Unified Customer Voice Portal to run the custom code using remote server on windows host.

### Run the Launcher Script

A launcher script file helps you execute commands inside the docker container. The launcher script accepts commands, options,
                              and other arguments to modify its behavior.

On the windows host, after downloading the customapis-docker-windows-<version>.zip installer, you will find a launcher.bat file. To run the launcher script from the C:/Cisco/customapis directory, use the following command:

```
launcher.bat <parameter>
```

On the linux host, after downloading the customapis-docker-linux-<version>.zip installer, you will find a launcher.sh file. To run the launcher script from the /usr/local/customapis directory, use the following command:

```
launcher.sh <parameter>
```

Run the launcher script using the following parameters:

Parameter

Action

create

Creates a directory structure

load

Loads the docker image and run the docker container

run

Run the docker container

stop

Stops the existing docker container

status

Displays the status of running docker container

| Note | Before you install Unified CVP, refer to the licensing information in the Unified CVP Licensing chapter. Ensure that the server chosen for Reporting Server is part of a workgroup. |
|---|---|

| Important | A new Unified CVP 15.0(1) base installer is now available for customers, which has OpenJDK JRE (v17.0.18) as the supporting Java runtime for the Unified
                                    CVP application. This is an upgrade from the previous Unified CVP 12.5(1b) installer, where OpenJDK JRE (1.8.x) was installed
                                    as the Java runtime environment on the Unified CVP components.” |
|---|---|

| Important | In the new 15.0(1) release, CVP Reporting Server has support for IBM Informix version 14.10 FC10W2. For migrating the Reporting Server from 12.x to 15.0(1), see Migrate Unified CVP Reporting Server . |
|---|---|

| Note | If you are testing with the self-signed TLS certificates that are generated as a part of the installation, ensure that you
                                    map the CN/SANs on the certificate to the corresponding IP through DNS or host file entries. |
|---|---|

| Note | In the new 15.0(1) release, TLS ciphers of all the server interfaces of CVP are configured in the sip.properties file. |
|---|---|

| Step 1 | Create the Unified CVP virtual machines using the OVA template. |
|---|---|
| Step 2 | Select the CVP components, as required. |
| Step 3 | Install Windows Server. Note Install .Net Framework 3.5 feature from Server Manager before installing CVP components. | Note | Install .Net Framework 3.5 feature from Server Manager before installing CVP components. |
| Note | Install .Net Framework 3.5 feature from Server Manager before installing CVP components. |
| Step 4 | Install the selected CVP components. |

| Note | Install .Net Framework 3.5 feature from Server Manager before installing CVP components. |
|---|---|

| Step 1 | Mount Unified CVP ISO, and run setup.exe. |
|---|---|
| Step 2 | Review and
                                       			 accept the license agreement, and click Next . |
| Step 3 | On the Select Package screen, choose the Unified CVP component to install on your computer, and click Next . Note Internet Information Server (IIS) is the default Media Server supported by Unified CVP. For details on IIS configuration,
                                                      see the Microsoft documentation. | Note | Internet Information Server (IIS) is the default Media Server supported by Unified CVP. For details on IIS configuration,
                                                      see the Microsoft documentation. |
| Note | Internet Information Server (IIS) is the default Media Server supported by Unified CVP. For details on IIS configuration,
                                                      see the Microsoft documentation. |
| Step 4 | At the Voice
                                          				Prompt Encode Format Type screen, select one of the following
                                       			 options: U-Law Encoded Wave
                                                   						Format A-Law Encoded Wave
                                                   						Format G729 Encoded Wave Format |
| Step 5 | On the Choose Destination Location screen, select the folder where setup will install files. By default, it is C:\Cisco\CVP . |
| Step 6 | On the X.509
                                          				Certificate screen, enter the required information in the form, and
                                       			 click Next . Note In the Common Name field, enter the hostname of the server (for example, cvp-server). The field accepts only alphanumeric characters (A-Z, a-z, 0-9), spaces,
                                                         hyphens (-), and underscores (). To re-create the certificates using FQDN in the Common Name field, after installation, refer to the Unified CVP Security chapter in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . | Note | In the Common Name field, enter the hostname of the server (for example, cvp-server). The field accepts only alphanumeric characters (A-Z, a-z, 0-9), spaces,
                                                         hyphens (-), and underscores (). To re-create the certificates using FQDN in the Common Name field, after installation, refer to the Unified CVP Security chapter in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Note | In the Common Name field, enter the hostname of the server (for example, cvp-server). The field accepts only alphanumeric characters (A-Z, a-z, 0-9), spaces,
                                                         hyphens (-), and underscores (). To re-create the certificates using FQDN in the Common Name field, after installation, refer to the Unified CVP Security chapter in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 7 | Click Install . Note You cannot
                                                      				  cancel the installation when it is in progress. | Note | You cannot
                                                      				  cancel the installation when it is in progress. |
| Note | You cannot
                                                      				  cancel the installation when it is in progress. |
| Step 8 | Choose to restart the computer right after the upgrade or to restart it later, and click Finish . Note After successful installation, the CVP Call Server Service Startup Type is set to Automatic by default. | Note | After successful installation, the CVP Call Server Service Startup Type is set to Automatic by default. |
| Note | After successful installation, the CVP Call Server Service Startup Type is set to Automatic by default. |

| Note | Internet Information Server (IIS) is the default Media Server supported by Unified CVP. For details on IIS configuration,
                                                      see the Microsoft documentation. |
|---|---|

| Note | In the Common Name field, enter the hostname of the server (for example, cvp-server). The field accepts only alphanumeric characters (A-Z, a-z, 0-9), spaces,
                                                         hyphens (-), and underscores (). To re-create the certificates using FQDN in the Common Name field, after installation, refer to the Unified CVP Security chapter in the Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
|---|---|

| Note | You cannot
                                                      				  cancel the installation when it is in progress. |
|---|---|

| Note | After successful installation, the CVP Call Server Service Startup Type is set to Automatic by default. |
|---|---|

| Step 1 | Perform Steps 1 to 6 of the Install CVP Server procedure. |
|---|---|
| Step 2 | From the Ready
                                          				to Install the Program screen, review the component that you
                                       			 selected, and click Install . |
| Step 3 | On the Ops
                                          				Console Password screen, in the Password and Password (for
                                          				verification) fields, enter a password and re-enter it for
                                       			 confirmation, and click Next . Note Adhere to
                                                      				  the password formation criteria that are listed on the Operations Console
                                                      				  Password screen section. Note Operations
                                                      				  Console Administrator and Web Services Administrator (wsmadmin) use the
                                                      				  Operations Console password. | Note | Adhere to
                                                      				  the password formation criteria that are listed on the Operations Console
                                                      				  Password screen section. | Note | Operations
                                                      				  Console Administrator and Web Services Administrator (wsmadmin) use the
                                                      				  Operations Console password. |
| Note | Adhere to
                                                      				  the password formation criteria that are listed on the Operations Console
                                                      				  Password screen section. |
| Note | Operations
                                                      				  Console Administrator and Web Services Administrator (wsmadmin) use the
                                                      				  Operations Console password. |
| Step 4 | Select one of
                                       			 the options to either restart the computer right after installation or later,
                                       			 and click Finish . |

| Note | Adhere to
                                                      				  the password formation criteria that are listed on the Operations Console
                                                      				  Password screen section. |
|---|---|

| Note | Operations
                                                      				  Console Administrator and Web Services Administrator (wsmadmin) use the
                                                      				  Operations Console password. |
|---|---|

| Step 1 | Perform Steps 1 to 4 of the Install Operations Console procedure. |
|---|---|
| Step 2 | Choose to restart the computer right after the upgrade or to restart it later, and click Finish . |

| Step 1 | Right-click My Computer > Manage . |
|---|---|
| Step 2 | In Storage section, click Disk Management . |
| Step 3 | Select the unformatted partition, which is usually Disk 1 . |
| Step 4 | Right-click Online , and initialize the disk. |
| Step 5 | Click Format , and follow the formatting process with NTFS. |

| Note | The ImagePath for CVP Reporting Informix IDS Service in Windows registry is set to c:\db\Informix\bin\onscpah cvp . Because of this, when security scanners are run, the ImagePath changes to "c:\db\Informix\bin\onscpah cvp" . This results in the CVP Reporting Informix IDS Service not starting. Workaround : Set ImagePath for CVP Reporting Informix IDS Service in Windows registry to "c:\db\Informix\bin\onscpah" cvp . |
|---|---|

| Step 1 | Mount the Unified CVP ISO image, and run setup.exe file. |
|---|---|
| Step 2 | Review and accept the license agreement, and click Next . |
| Step 3 | On the Select Package screen, select Reporting Server , and click Next . Note This step takes approximately 30 seconds before moving to the Choose Destination Location window. | Note | This step takes approximately 30 seconds before moving to the Choose Destination Location window. |
| Note | This step takes approximately 30 seconds before moving to the Choose Destination Location window. |
| Step 4 | Select the root drive on which you want the Reporting database data and backup data to reside, and click Next . Note Choose the E drive or the second drive, whose size is more than 400GB, to store the Reporting database data and to keep the
                                                   backup of data. The Database Size Selection screen appears, providing the following options: Standard: Requires a minimum of 250GB of free disk space. Premium: Requires a minimum of 375GB of free disk space. | Note | Choose the E drive or the second drive, whose size is more than 400GB, to store the Reporting database data and to keep the
                                                   backup of data. |
| Note | Choose the E drive or the second drive, whose size is more than 400GB, to store the Reporting database data and to keep the
                                                   backup of data. |
| Step 5 | Choose the appropriate database size for the license that you purchased, and click Next . |
| Step 6 | From the Ready to Install the Program window, review the component that you have selected, and click Install . |
| Step 7 | On the Reporting Password window, enter a password and re-enter it for confirmation, and click Next . Note Adhere to the password formation criteria that are listed on the Operations Console Password screen section. The Reporting password requires that the Minimum Password Age parameter be set to 0 days for both the local and/or domain security policy and is subject to both the Unified CVP password
                                                            policy and the password policy enforced by the operating system of the computer on which the Reporting Server resides. For
                                                            each aspect of the password, the Reporting password must meet the requirement of the more restrictive policy. If you are installing
                                                            CVP Reporting Server please ensure that your local and/or domain security policy for MINIMUM PASSWORD AGE are set to 0 days
                                                            for the installation of the CVP Reporting Server component (In Windows, Control Panel > Administrative Tools > Local Security Policy > Account Policy > Password Policy ). If the reporting password you enter is rejected, review the list of password requirements displayed by the installer and
                                                            consider your operating system's password requirements. You can reconfigure this password repeatedly until an acceptable password
                                                            is found. After installation, add the Unified CVP Reporting Server to the domain, if necessary. | Note | Adhere to the password formation criteria that are listed on the Operations Console Password screen section. The Reporting password requires that the Minimum Password Age parameter be set to 0 days for both the local and/or domain security policy and is subject to both the Unified CVP password
                                                            policy and the password policy enforced by the operating system of the computer on which the Reporting Server resides. For
                                                            each aspect of the password, the Reporting password must meet the requirement of the more restrictive policy. If you are installing
                                                            CVP Reporting Server please ensure that your local and/or domain security policy for MINIMUM PASSWORD AGE are set to 0 days
                                                            for the installation of the CVP Reporting Server component (In Windows, Control Panel > Administrative Tools > Local Security Policy > Account Policy > Password Policy ). If the reporting password you enter is rejected, review the list of password requirements displayed by the installer and
                                                            consider your operating system's password requirements. You can reconfigure this password repeatedly until an acceptable password
                                                            is found. After installation, add the Unified CVP Reporting Server to the domain, if necessary. |
| Note | Adhere to the password formation criteria that are listed on the Operations Console Password screen section. The Reporting password requires that the Minimum Password Age parameter be set to 0 days for both the local and/or domain security policy and is subject to both the Unified CVP password
                                                            policy and the password policy enforced by the operating system of the computer on which the Reporting Server resides. For
                                                            each aspect of the password, the Reporting password must meet the requirement of the more restrictive policy. If you are installing
                                                            CVP Reporting Server please ensure that your local and/or domain security policy for MINIMUM PASSWORD AGE are set to 0 days
                                                            for the installation of the CVP Reporting Server component (In Windows, Control Panel > Administrative Tools > Local Security Policy > Account Policy > Password Policy ). If the reporting password you enter is rejected, review the list of password requirements displayed by the installer and
                                                            consider your operating system's password requirements. You can reconfigure this password repeatedly until an acceptable password
                                                            is found. After installation, add the Unified CVP Reporting Server to the domain, if necessary. |
| Step 8 | Choose to restart the computer right after installation or to restart it later, and click Finish . |

| Note | This step takes approximately 30 seconds before moving to the Choose Destination Location window. |
|---|---|

| Note | Choose the E drive or the second drive, whose size is more than 400GB, to store the Reporting database data and to keep the
                                                   backup of data. |
|---|---|

| Note | Adhere to the password formation criteria that are listed on the Operations Console Password screen section. The Reporting password requires that the Minimum Password Age parameter be set to 0 days for both the local and/or domain security policy and is subject to both the Unified CVP password
                                                            policy and the password policy enforced by the operating system of the computer on which the Reporting Server resides. For
                                                            each aspect of the password, the Reporting password must meet the requirement of the more restrictive policy. If you are installing
                                                            CVP Reporting Server please ensure that your local and/or domain security policy for MINIMUM PASSWORD AGE are set to 0 days
                                                            for the installation of the CVP Reporting Server component (In Windows, Control Panel > Administrative Tools > Local Security Policy > Account Policy > Password Policy ). If the reporting password you enter is rejected, review the list of password requirements displayed by the installer and
                                                            consider your operating system's password requirements. You can reconfigure this password repeatedly until an acceptable password
                                                            is found. After installation, add the Unified CVP Reporting Server to the domain, if necessary. |
|---|---|

| Important | A new Unified CVP 15.0(1) base installer is now available for customers, featuring OpenJDK JRE (v17.0.13) as the supporting
                                          Java runtime for the Unified CVP application. This is an upgrade from the previous 12.5(1) installer, where OpenJDK JRE (v1.8.x)
                                          was installed as the Java runtime environment on the Unified CVP components. |
|---|---|

| Step 1 | Mount the Unified CVP software (including CVP Studio) installer ISO image (under the Installer_Windows folder), and run setup.exe . |
|---|---|
| Step 2 | On the Welcome screen, click Next . Note If you click Cancel here or on the dialog screens that follow before the Ready to Install the Program screen, the installation is canceled. The Exit Setup dialog box appears. | Note | If you click Cancel here or on the dialog screens that follow before the Ready to Install the Program screen, the installation is canceled. The Exit Setup dialog box appears. |
| Note | If you click Cancel here or on the dialog screens that follow before the Ready to Install the Program screen, the installation is canceled. The Exit Setup dialog box appears. |
| Step 3 | Review Copyrights to Products used by Call Studio and click Next . |
| Step 4 | Review and accept the license agreement, and click Next . |
| Step 5 | On the Choose Destination Location screen, select the folder where setup will install files. By default, it is C:\Cisco\CallStudio . |
| Step 6 | On the InstallShield Wizard Complete screen, click Install . |
| Step 7 | Click Finish to exit the wizard. |

| Note | If you click Cancel here or on the dialog screens that follow before the Ready to Install the Program screen, the installation is canceled. The Exit Setup dialog box appears. |
|---|---|

| Note | The SolarWinds TFTP software and AnyConnect (while a VPN connection is enabled) are the known causes for the Call Studio debugger
                                          errors. To resolve the Call Studio debugger errors: If you are using SolarWinds, stop the SolarWinds TFTP software and run the debugger. If you are using AnyConnect, disconnect the VPN connection and run the debugger. |
|---|---|

| Note | Setting up this Windows host is a one-time activity and does not need to be repeated for subsequent Docker releases. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Install Windows Container on Remote Server. See, Install Windows Containers on Remote Server |
| 2 | Install Docker Engine on Remote Server (Windows). See, Install Docker Engine on Remote Server (Windows) |
| 3 | Install Docker Compose Plugin on Remote Server (Windows). See, Install Docker Compose Plugin on Remote Server (Windows) |
| 4 | Install Docker Image on Remote Server (Windows). See, Install Docker Image on Remote Server (Windows) |

| Step 1 | In the remote server machine, go to Server Manager and open Manage > Add Roles and Features . |
|---|---|
| Step 2 | On the Before You Begin screen, click Next . |
| Step 3 | On the Select Installation Type screen, click Next . |
| Step 4 | On the Select Destination Server screen, click Next . |
| Step 5 | On the Select Server Roles screen, click Next . |
| Step 6 | On the Select Features screen, choose the Containers to install on your computer, and click Next . |
| Step 7 | On the Confirm Installation Selections screen, click Install . |
| Step 8 | Click Close . |
| Step 9 | Restart the server. |

| Step 1 | Download the latest version of the docker binary package file (.zip) from the location: https://download.docker.com/win/static/stable/x86_64 . The recommended version for the docker zip file is 25.0.1 (and later). |
|---|---|
| Step 2 | Run the following commands in the PowerShell application to install and extract the archive to your program files on the windows
                                             host: Note All PowerShell commands in this procedure must be run in Administrator mode. PS C:\> Expand-Archive  -Path "<Path_to_zip_file>" -DestinationPath $Env:ProgramFiles For example: PS C:\> Expand-Archive -Path "C:\docker\docker-25.0.1.zip" -DestinationPath $Env:ProgramFiles PS C:\> &$Env:ProgramFiles\Docker\dockerd --register-service | Note | All PowerShell commands in this procedure must be run in Administrator mode. |
| Note | All PowerShell commands in this procedure must be run in Administrator mode. |
| Step 3 | Run the following command in the PowerShell application to start the docker service on the windows host: PS C:\> Start-Service docker Verify whether the Docker Engine Service is started in Window Services. |
| Step 4 | Verify that Docker Engine is installed and configured on the remote server for the windows host. Run the following command in PowerShell application to verify the docker engine is installed on the remote server of the windows
                                                host: &$Env:ProgramFiles\Docker\docker --version For example, the above command shows the version as Docker version v25.0.1 . |

| Note | All PowerShell commands in this procedure must be run in Administrator mode. |
|---|---|

| Step 1 | Run the following commands in the PowerShell application on the windows host as Github now uses TLS 1.2: Note All PowerShell commands in this procedure must be run in Administrator mode. PS C:\> [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 | Note | All PowerShell commands in this procedure must be run in Administrator mode. |
|---|---|---|---|
| Note | All PowerShell commands in this procedure must be run in Administrator mode. |
| Step 2 | Run the following commands in the PowerShell application on the windows host to download the latest release of Compose: The recommended release version for the docker compose plugin zip file is 2.26.1 (and later). PS C:\> Start-BitsTransfer -Source "<Path_To_File_in_Github>" -Destination $Env:<Destination_Path> For example: PS C:\> Start-BitsTransfer -Source "https://github.com/docker/compose/releases/download/v2.26.1/docker-compose-windows-x86_64.exe" -Destination $Env:ProgramFiles\Docker\docker-compose.exe |
| Step 3 | In case of no internet connectivity in the remote server machine, follow the below steps to install docker-compose plugin
                                             on the windows host: Download the binary docker-compose-windows-x86_64.exe file from the following location: https://github.com/docker/compose/releases/download/v2.26.1/docker-compose-windows-x86_64.exe and copy the file to the C:\ProgramFiles\Docker folder. Rename the file docker-compose-windows-x86_64.exe to docker-compose.exe Run the following command in PowerShell application to install the binary file: &$Env:ProgramFiles\Docker\docker-compose.exe . |
| Step 4 | Verify that Docker Compose plugin is installed and configured on the remote server of the windows host. Run the following command in PowerShell application to verify the docker engine is installed on the remote server of the windows
                                                host: &$Env:ProgramFiles\Docker\docker-compose --version |

| Note | All PowerShell commands in this procedure must be run in Administrator mode. |
|---|---|

| Note | For the changes to take effect after adding a system variable, you need to reopen the PowerShell window as an administrator. |
|---|---|

| Step 1 | Download or copy the customapis-windows-docker-<version>.zip installer zip file on the windows host. |
|---|---|
| Step 2 | Create the following directory structure on the host: C:\Cisco\customapis . |
| Step 3 | Extract the archive (.zip) to the following location: C:\Cisco\customapis , where you need the Installer to be running from. |
| Step 4 | Open the PowerShell application on the windows host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script. Note All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . | Note | All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . |
| Note | All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . |
| Step 5 | Use the launcher.bat file to initiate creation of external mounted folders by providing the create parameter by running the following command: PS .\launcher.bat create After you run the command, external mount folder gets created at location: C:\Cisco\customapis |
| Step 6 | Use the launcher.bat file to load the windows docker image and run the container by providing the load parameter by running the following command: PS .\launcher.bat load |
| Step 7 | Check the status of the container at: http:// <remote_ip_address> :8080/customapis/actuator/health . UP status means that the container is running. |
| Step 8 | Use the launcher.bat file to view the status of the container by providing the status parameter by running the following command: PS .\launcher.bat status |

| Note | All PowerShell commands in this procedure must be run in Administrator mode from the following location: C:\Cisco\customapis . |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Install Docker Engine on Remote Server (Linux). See, Install Docker Engine on Remote Server (Linux) |
| 2 | Install Docker Compose Plugin on Remote Server (Linux). See, Install Docker Compose Plugin on Remote Server (Linux) |
| 3 | Install Docker Image on Remote Server (Linux). See, Install Docker Image on Remote Server (Linux) |

| Note | To install docker engine on CentOS Linux 7 (core), you can refer to the Docker documentation at https://docs.docker.com/engine/install/centos/ . |
|---|---|

| Step 1 | Download the docker package (.rpm) file for the required docker version that you want to install from the following location: https://download.docker.com/linux/centos/7/x86_64/stable/Packages/ . |
|---|---|
| Step 2 | Run the following command to install the docker engine in the relevant path of your download location: $ sudo yum install <Path_to_Docker_Package_File>.rpm $ sudo yum install *.rpm Note In case some dependencies are missing during the installation process, you must identify these dependencies and download the
                                                            necessary .rpm files. Once the required files are downloaded, you must again run the command sudo yum install *.rpm . | Note | In case some dependencies are missing during the installation process, you must identify these dependencies and download the
                                                            necessary .rpm files. Once the required files are downloaded, you must again run the command sudo yum install *.rpm . |
| Note | In case some dependencies are missing during the installation process, you must identify these dependencies and download the
                                                            necessary .rpm files. Once the required files are downloaded, you must again run the command sudo yum install *.rpm . |
| Step 3 | Verify that Docker engine is installed using the following commands: $ docker --version

$ docker compose version |
| Step 4 | Run the following command to start the docker engine: $ sudo systemctl start docker If you want Docker to start automatically after a platform reboot, you can register it with the following command: $ sudo systemctl enable docker |
| Step 5 | Verify that the installation of the Docker engine is successful by running the hello-world image using the following command: $ sudo docker run hello-world |

| Note | In case some dependencies are missing during the installation process, you must identify these dependencies and download the
                                                            necessary .rpm files. Once the required files are downloaded, you must again run the command sudo yum install *.rpm . |
|---|---|

| Step 1 | Perform Steps 1 to 2 of the Install Docker Engine on Remote Server (Linux) procedure. Refer to the Install Docker Engine on Remote Server (Linux) section for more information. |
|---|---|
| Step 2 | Verify that Docker Compose plugin is installed and configured on the remote server of the linux host using the following command. $ docker compose version |

| Step 1 | Download or copy the customapis-docker-linux-<version>.zip installer zip on the linux host. |
|---|---|
| Step 2 | Create directory the following structure on the host: /usr/local/customapis |
| Step 3 | Run the following command to extract the archive (.zip) to the location: /usr/local/customapis , where you need the Installer to be running from: $ unzip customapis-docker-linux-<version>.zip |
| Step 4 | Run the following command to provide permission to the launcher.sh file: $ chmod +x launcher.sh Note Ensure that you have permissions to directory location: /usr/local/customapis | Note | Ensure that you have permissions to directory location: /usr/local/customapis |
| Note | Ensure that you have permissions to directory location: /usr/local/customapis |
| Step 5 | Open the Terminal application on the linux host to run the launcher script. Refer to the Run the Launcher Script section for more information on using the launcher script. |
| Step 6 | Use the launcher.sh file to initiate creation of external mounted folders by providing the create parameter by running the following command: $ ./launcher.sh create After you run the command, external mount folder gets created at location: /usr/local/customapis |
| Step 7 | Use the launcher.sh file to load the windows docker image and run the container by providing the load parameter by running the following command: $ ./launcher.sh load |
| Step 8 | Check the status of the container at: http:// <remote_ip_address> :8080/customapis/actuator/health . UP status means that the container is running. |
| Step 9 | Use the launcher.sh file to view the status of the container by providing the load parameter by running the following command: $ ./launcher.sh status |

| Note | Ensure that you have permissions to directory location: /usr/local/customapis |
|---|---|

| Parameter | Action |
|---|---|
| create | Creates a directory structure |
| load | Loads the docker image and run the docker container |
| run | Run the docker container |
| stop | Stops the existing docker container |
| status | Displays the status of running docker container |