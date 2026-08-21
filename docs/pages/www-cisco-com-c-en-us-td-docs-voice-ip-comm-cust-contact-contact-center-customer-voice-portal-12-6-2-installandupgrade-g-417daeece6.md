---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-installandupgrade-g-417daeece6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/installandupgrade/guide/ccvp_b_1262-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal/ccvp_b_1252-installation-and-upgrade-guide-for-cisco-unified-customer-voice-portal_chapter_010.html
retrieved_at: 2026-08-21T11:56:33.963695+00:00
---

Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(2)

# Installation and Upgrade Guide for Cisco Unified Customer Voice Portal, Release 12.6(2)

Updated: April 28, 2023

Chapter: Unified CVP Minor Release Upgrade

## Chapter: Unified CVP Minor Release Upgrade

# Unified CVP Minor Release Upgrade

Unified CVP 12.6(2) MR is an executable file which can be downloaded from CCO. The same executable file can be used to upgrade all Unified CVP
                        components.

Important

Before you install Unified CVP MR:

Refer to the licensing information in the Unified CVP Licensing chapter.

Ensure that the server chosen for Reporting Server is part of a workgroup.

Backup all custom audio files present in <CVP_HOME>/VXMLServer/tomcat/webapps/audio for Unified CVP upgrade.

Take a backup of the OAMP config using Export System Configuration from the system menu before OAMP upgrade.

To export system configuration from 12.6(1):

Export the system configuration files.

Unzip the files using the Winrar.

Select the contents of the unzipped folder to compress it again.

Import the system configuration zip file.

After the successful upgrade, the Certificate Authorities (CAs) that are unapproved by Cisco are removed from the platform
                                    trust store. However, you can add them back, if necessary.

For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle here .

For information about adding a certificate, see here .

## Upgrade Path

The following table lists the upgrade paths to replace the existing Unified CVP version with the MR on Windows Server 2016 or Windows Server 2019 .

Unified CVP

12.5(1) to 12.6(2)

No

Direct upgrade to Unified CVP 12.6(2) through MR.

Unified CVP

12.6(1) to 12.6(2)

No

Direct upgrade to Unified CVP 12.6(2) through MR.

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

## Unified CVP Upgrade Strategies

You can upgrade Unified CVP in a maintenance window. However, when there are a large number of Unified CVP servers to upgrade,
                           it may not be possible to upgrade all of them in one maintenance window. Using the upgrade strategies, you can help large
                           Unified CVP deployments distribute the upgrade process. In addition, you can divide the server upgrades into multiple steps
                           that can be completed over several maintenance windows.

Unified CVP upgrade strategies are described in the following sections.

### Unified CVP Units

A Unified CVP unit is a single virtual machine and may comprise VXML Servers and Call Servers. For Unified CVP deployments
                                 that have multiple Unified CVP units, ensure that you upgrade one unit at a time. For example, you can upgrade a Unified CVP
                                 unit of related servers in a maintenance window. This deployment may be useful for call centers. There may be a need to migrate
                                 to Session Initiation Protocol (SIP) to continue call processing and minimize the risks.

### Multiphased
                           	 Approach

Multiphased approach is a strategy to upgrade a subset of Unified CVP Servers and resume call processing. Using the multiphased
                                 upgrade approach, you can divide the upgrades in phases over time. If a Unified CVP deployment has multiple Unified CVP units,
                                 you can upgrade each unit using the multiphased approach.

Depending on the
                                 		  deployment, choose one of the following multiphased approaches:

Upgrade all
                                       				servers of a certain type in a maintenance window.

Upgrade a
                                       				subset of a server type in a maintenance window.

Upgrade a subset of a server type from a Unified CVP unit in a maintenance window.

Use multiphased
                                 		  approach to upgrade the components in the following sequence:

Operations
                                       				Console

Unified CVP Reporting Server

Unified CVP Server

It is not necessary to upgrade all servers in a category in a single maintenance window; however, you must upgrade all Unified
                                             CVP components of one type before moving to the next set of components in the Unified CVP deployment or the Unified CVP unit.

## Important
                        	 Considerations for Upgrade

Upgrade
                                    				Unified CVP during off-peak hours or during a maintenance window to avoid
                                    				service interruptions.

Do not make
                                    				any configuration changes during the upgrade, because the changes are lost
                                    				after the upgrade.

Ensure that a Unified CVP unit remains offline until you upgrade all the components in that unit.

Upgrade
                                    				Unified CVP components in a sequence for a successful deployment. A change in
                                    				upgrade sequence results in loss of call data and error or inability to
                                    				configure properties that are introduced in the new version.

Push the TCL and VXML files (from the location C:\Cisco\CVP\GWDownloads\ ) to their respective ingress and VXML gateways after the Unified CVP Operations Console is upgraded, but before any other Unified CVP components are upgraded.

## Upgrade Unified CVP Components

Unified CVP Server

Operations Console

Remote Operations

Unified CVP Reporting Server

Follow the given steps to install the Unified CVP 12.6(2) MR on each of the above components:

Step 1

Run (double click) CVP12.6.2.exe . A welcome screen is displayed.

Step 2

Click Next to proceed.

Step 3

Review and accept the Software License Agreement , and click Next .

A warning message is displayed to backup all custom audio files. Click OK to proceed.

Step 4

Click Install to start the MR installation.

As soon as the MR set up begins, the following warning may be displayed if any of the 12.5 ESs are installed:

```
Following engineering special(s) installed in the system, are not merged into CVP 12.6(2) <list of ES installed>

Continuing with the upgrade may result in loss of functionality provided by above engineering special(s).
Review available engineering special(s) built on CVP 12.6(2) , for corresponding patches that would need to be applied separately.

Do you want to continue the upgrade?
```

Click Yes to proceed.

For information on Engineering Special (ES) when upgrading to Cisco Unified Customer Voice Portal to 12.6(2), see Important Notes section in the Cisco Unified Customer Voice Portal Chapter of the Release Notes for Cisco Contact Center Enterprise Solutions Release .

Step 5

Click Finish to complete the MR installation. Reboot the machine after the installation.

## Upgrade Unified Call Studio

Step 1

Open Call Studio, right-click any existing project in the Navigator view, choose Export .

The Export wizard opens.

Step 2

Navigate to General > File System , and click Next .

Step 3

Browse to the directory where the projects will be exported and click OK and then click Finish .

Step 4

Uninstall the Call Studio software.

For more information, see the Unified CVP/Call Studio Uninstallation section.

Step 5

Install the Call Studio software.

For more information, see the Install Unified Call Studio section.

The SolarWinds TFTP software and AnyConnect (while a VPN connection is enabled) are the known causes for the Call Studio debugger
                                          errors. To resolve the Call Studio debugger errors:

If you are using SolarWinds, stop the SolarWinds TFTP software and run the debugger.

If you are using AnyConnect, disconnect the VPN connection and run the debugger.

## Postupgrade
                        	 Tasks

After you upgrade the Unified CVP components, synchronize the metadata files using the Sync-up tool.

Initiate metadata synchronization only if you are using the CVP Rest API. For more information, see Initiate Metadata Synchronization for Unified CVP Rest API .

Important

After upgrade, restart the WebServicesManager service to use the system CLI.

If you are using a VRU connection port other than the default port (5000), then click Save and Deploy of Unified CVP Call Server from OAMP.

If you have added the certificates in .ormkeystore , then add them again in .keystore .

Perform the following steps for Smart Licensing to work after upgrading to Unified CVP 12.6(2) :

Redeploy all Call Servers and VXML Servers from OAMP.

Restart the services.

VMWare Tools do not get updated automatically after upgrading to Unified , CVP 12.6(2) on Windows Server 2016/2019 and rebooting the machine.

Workaround : Perform the following steps to update the VMWare Tools manually:

Right-click on the VM.

Go to Guest OS and select Upgrade VMWare Tools .

After you upgrade to Unified CVP 12.6(2) , the WebServiceCredentials schema gets updated with the encryption method.

To encrypt the wsm password in OAMP, do the following:

Stop Cisco CVP OPSConsoleServer and Cisco CVP WebServicesManager services.

Navigate to C:\Cisco\CVP\bin\ .

Execute the mgr-init.bat -wsm <wsmadmin password> command from the command prompt.

Restart the Cisco Unified CVP Operations Console and Cisco CVP WebServicesManager.

The encryption key, which is a part of OAMP, is absent from the WebServicesCredentials.xml files on the CVP Call Server, VXML Server, and Reporting Servers.

Workaround: To synchronize the WebServicesCredentials.xml with the encryption method, it is necessary to redeploy all the Call Servers, VXML Servers, and Reporting Servers.

### Initiate Metadata Synchronization for Unified CVP Rest API

In the CVP REST API architecture, customers use the REST API to create, update, and delete media files on the media server
                                 and VXML applications on the VXML server. When this process is used, media files on the media server and VXML applications
                                 on the VXML server are saved as metadata in the OpsConsole server’s Derby database. There may be situations where the metadata
                                 becomes out of sync with the files on the media servers and VXML servers. Typical examples include the addition or deletion
                                 of CVP servers, and the deployment of applications and media files using tools other than the REST API.

A command line tool “metasynch.cmd” is available in the C:\Cisco\CVP\wsm\CLI location on the OpsConsole server to enable synchronization of metadata with the files on VXML servers and media servers.
                                 The tool internally uses the Sync Up API to perform synchronization. It takes three arguments: WSM username, WSM user password,
                                 and server type (MEDIA, VXML, or VXML_STANDALONE). Based on the server type specified, all servers of the respective server
                                 type are synchronized with the OpsConsole server as metadata. If the server type argument is not provided, metadata is synchronized
                                 from all media servers and VXML servers configured in the OpsConsole server. In case of an upgrade from an earlier version,
                                 the media files and VXML applications are present on the media servers and VXML servers, but the corresponding metadata information
                                 is not present on the WSM server. The absence of metadata limits the user from using the REST API to access, update, or delete
                                 existing media files and VXML applications on the media server and VXML server.

In case of Upgrade from an earlier version, the media files and vxml applications are present in the media servers and vxml
                                 servers but corresponding metadata information is not present in the WSM server. The absence of metadata information limits
                                 the user from using the REST API to access, update, and delete existing media files and vxml applications on the media server
                                 and the vxml server.

Wsmadmin (CLI) users or any other serviceability/readonly role users cannot login or use OAMP/NOAMP/CLI until an Administrator
                                             or Super Administrator role user updates their password post an install/upgrade.

#### Synchronize
                              	 Metadata Files Using Sync-Up Tool

To invoke metasynch.cmd , complete the following steps.

Step 1

On the Unified CVP OAMP Server, navigate to the C:\Cisco\CVP\wsm\ CLI location.

Step 2

Run the metasynch.cmd file with following arguments:

- wsm
                                                   				  username

- wsm
                                                   				  password

##### Example:

```
metasynch.cmd wsmusername wsmpassword MEDIA
```

servertype : MEDIA/VXML /VXML_STANDALONE

options : -help -? print this help message

C:\Cisco\CVP\wsm\CLI\log\SyncTool.log

| Important | Before you install Unified CVP MR: Refer to the licensing information in the Unified CVP Licensing chapter. Ensure that the server chosen for Reporting Server is part of a workgroup. Backup all custom audio files present in <CVP_HOME>/VXMLServer/tomcat/webapps/audio for Unified CVP upgrade. Take a backup of the OAMP config using Export System Configuration from the system menu before OAMP upgrade. |
|---|---|

| Note | After the successful upgrade, the Certificate Authorities (CAs) that are unapproved by Cisco are removed from the platform
                                    trust store. However, you can add them back, if necessary. For information about the list of CAs that Cisco supports, see the Cisco Trusted External Root Bundle here . For information about adding a certificate, see here . |
|---|---|

| Upgrade Path from Older Release to New Release | Platform Change | Conversion Process | Description |
|---|---|---|---|
| Unified CVP 12.5(1) to 12.6(2) | No | Direct upgrade to Unified CVP 12.6(2) through MR. | Platform change is not required because Unified CVP 12.6(2) is supported on Windows Server 2016 and Windows Server 2019. |
| Unified CVP 12.6(1) to 12.6(2) | No | Direct upgrade to Unified CVP 12.6(2) through MR. | Platform change is not required. |

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

| Note | It is not necessary to upgrade all servers in a category in a single maintenance window; however, you must upgrade all Unified
                                             CVP components of one type before moving to the next set of components in the Unified CVP deployment or the Unified CVP unit. |
|---|---|

| Step 1 | Run (double click) CVP12.6.2.exe . A welcome screen is displayed. |
|---|---|
| Step 2 | Click Next to proceed. |
| Step 3 | Review and accept the Software License Agreement , and click Next . A warning message is displayed to backup all custom audio files. Click OK to proceed. |
| Step 4 | Click Install to start the MR installation. Note As soon as the MR set up begins, the following warning may be displayed if any of the 12.5 ESs are installed: Following engineering special(s) installed in the system, are not merged into CVP 12.6(2) <list of ES installed>

Continuing with the upgrade may result in loss of functionality provided by above engineering special(s).
Review available engineering special(s) built on CVP 12.6(2) , for corresponding patches that would need to be applied separately.

Do you want to continue the upgrade? Click Yes to proceed. For information on Engineering Special (ES) when upgrading to Cisco Unified Customer Voice Portal to 12.6(2), see Important Notes section in the Cisco Unified Customer Voice Portal Chapter of the Release Notes for Cisco Contact Center Enterprise Solutions Release . | Note | As soon as the MR set up begins, the following warning may be displayed if any of the 12.5 ESs are installed: Following engineering special(s) installed in the system, are not merged into CVP 12.6(2) <list of ES installed>

Continuing with the upgrade may result in loss of functionality provided by above engineering special(s).
Review available engineering special(s) built on CVP 12.6(2) , for corresponding patches that would need to be applied separately.

Do you want to continue the upgrade? Click Yes to proceed. For information on Engineering Special (ES) when upgrading to Cisco Unified Customer Voice Portal to 12.6(2), see Important Notes section in the Cisco Unified Customer Voice Portal Chapter of the Release Notes for Cisco Contact Center Enterprise Solutions Release . |
| Note | As soon as the MR set up begins, the following warning may be displayed if any of the 12.5 ESs are installed: Following engineering special(s) installed in the system, are not merged into CVP 12.6(2) <list of ES installed>

Continuing with the upgrade may result in loss of functionality provided by above engineering special(s).
Review available engineering special(s) built on CVP 12.6(2) , for corresponding patches that would need to be applied separately.

Do you want to continue the upgrade? Click Yes to proceed. For information on Engineering Special (ES) when upgrading to Cisco Unified Customer Voice Portal to 12.6(2), see Important Notes section in the Cisco Unified Customer Voice Portal Chapter of the Release Notes for Cisco Contact Center Enterprise Solutions Release . |
| Step 5 | Click Finish to complete the MR installation. Reboot the machine after the installation. |

| Note | As soon as the MR set up begins, the following warning may be displayed if any of the 12.5 ESs are installed: Following engineering special(s) installed in the system, are not merged into CVP 12.6(2) <list of ES installed>

Continuing with the upgrade may result in loss of functionality provided by above engineering special(s).
Review available engineering special(s) built on CVP 12.6(2) , for corresponding patches that would need to be applied separately.

Do you want to continue the upgrade? Click Yes to proceed. For information on Engineering Special (ES) when upgrading to Cisco Unified Customer Voice Portal to 12.6(2), see Important Notes section in the Cisco Unified Customer Voice Portal Chapter of the Release Notes for Cisco Contact Center Enterprise Solutions Release . |
|---|---|

| Step 1 | Open Call Studio, right-click any existing project in the Navigator view, choose Export . The Export wizard opens. |
|---|---|
| Step 2 | Navigate to General > File System , and click Next . Note From the list displayed by the Export wizard, select multiple projects to export them simultaneously. | Note | From the list displayed by the Export wizard, select multiple projects to export them simultaneously. |
| Note | From the list displayed by the Export wizard, select multiple projects to export them simultaneously. |
| Step 3 | Browse to the directory where the projects will be exported and click OK and then click Finish . |
| Step 4 | Uninstall the Call Studio software. For more information, see the Unified CVP/Call Studio Uninstallation section. |
| Step 5 | Install the Call Studio software. For more information, see the Install Unified Call Studio section. |

| Note | From the list displayed by the Export wizard, select multiple projects to export them simultaneously. |
|---|---|

| Note | The SolarWinds TFTP software and AnyConnect (while a VPN connection is enabled) are the known causes for the Call Studio debugger
                                          errors. To resolve the Call Studio debugger errors: If you are using SolarWinds, stop the SolarWinds TFTP software and run the debugger. If you are using AnyConnect, disconnect the VPN connection and run the debugger. |
|---|---|

| Important | After upgrade, restart the WebServicesManager service to use the system CLI. If you are using a VRU connection port other than the default port (5000), then click Save and Deploy of Unified CVP Call Server from OAMP. If you have added the certificates in .ormkeystore , then add them again in .keystore . Perform the following steps for Smart Licensing to work after upgrading to Unified CVP 12.6(2) : Redeploy all Call Servers and VXML Servers from OAMP. Restart the services. VMWare Tools do not get updated automatically after upgrading to Unified , CVP 12.6(2) on Windows Server 2016/2019 and rebooting the machine. Workaround : Perform the following steps to update the VMWare Tools manually: Right-click on the VM. Go to Guest OS and select Upgrade VMWare Tools . After you upgrade to Unified CVP 12.6(2) , the WebServiceCredentials schema gets updated with the encryption method. To encrypt the wsm password in OAMP, do the following: Stop Cisco CVP OPSConsoleServer and Cisco CVP WebServicesManager services. Navigate to C:\Cisco\CVP\bin\ . Execute the mgr-init.bat -wsm <wsmadmin password> command from the command prompt. Restart the Cisco Unified CVP Operations Console and Cisco CVP WebServicesManager. The encryption key, which is a part of OAMP, is absent from the WebServicesCredentials.xml files on the CVP Call Server, VXML Server, and Reporting Servers. Workaround: To synchronize the WebServicesCredentials.xml with the encryption method, it is necessary to redeploy all the Call Servers, VXML Servers, and Reporting Servers. |
|---|---|

| Note | Wsmadmin (CLI) users or any other serviceability/readonly role users cannot login or use OAMP/NOAMP/CLI until an Administrator
                                             or Super Administrator role user updates their password post an install/upgrade. |
|---|---|

| Step 1 | On the Unified CVP OAMP Server, navigate to the C:\Cisco\CVP\wsm\ CLI location. |
|---|---|
| Step 2 | Run the metasynch.cmd file with following arguments: wsm
                                                   				  username wsm
                                                   				  password Example: metasynch.cmd wsmusername wsmpassword MEDIA Usage : metasynch [options] username password [servertype] servertype : MEDIA/VXML /VXML_STANDALONE options : -help -? print this help message Note The server type argument should be MEDIA, VXML , or VXML_STANDALONE type. If the server type argument is not provided, the metadata is synched with all the VXML applications on VXML servers
                                                         and all media files on Media servers. Logs for synch command tool can be found at the following location: C:\Cisco\CVP\wsm\CLI\log\SyncTool.log | Note | The server type argument should be MEDIA, VXML , or VXML_STANDALONE type. If the server type argument is not provided, the metadata is synched with all the VXML applications on VXML servers
                                                         and all media files on Media servers. Logs for synch command tool can be found at the following location: |
| Note | The server type argument should be MEDIA, VXML , or VXML_STANDALONE type. If the server type argument is not provided, the metadata is synched with all the VXML applications on VXML servers
                                                         and all media files on Media servers. Logs for synch command tool can be found at the following location: |

| Note | The server type argument should be MEDIA, VXML , or VXML_STANDALONE type. If the server type argument is not provided, the metadata is synched with all the VXML applications on VXML servers
                                                         and all media files on Media servers. Logs for synch command tool can be found at the following location: |
|---|---|