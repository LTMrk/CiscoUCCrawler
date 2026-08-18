---
doc_id: developer-cisco-com-codeexchange-github-repo-appdynamics-dotnetagentextensionmanager-7b35357ba5
source_url: https://developer.cisco.com/codeexchange/github/repo/Appdynamics/DotNetAgentExtensionManager
retrieved_at: 2026-08-18T23:45:56.017239+00:00
---

AppDynamics Manager for .Net Agent Extension works with the .Net Agent to capture and report metrics not gathered out of the box. It can be used to capture metrics such as: Windows Event Log data, current Windows Service states, Windows reboot times, or kick off custom scripts to gather metrics from any source.

## Contents

- /Extensions - contains configuration data for each extension.

- /Logs - contains logs for each extension

- * AppDynamics.Extension.Manager.exe - The Extension Manager UI, use this to enable and configure extensions and to install/remove the AppDynamics.Agent.Extension Windows service.

- * ExtensionService.exe - The AppDynamics.Agent.Extension Windows service executable, a lightweight Windows service which continuously collects metric data for all .NET extensions and stores this data in Windows Performance Counters. These Performance Counters are polled continuously and their values are sent to the Controller by the AppDynamics.Agent.Coordinator service.

- * AppDynamics.Extension.CCT.exe - Configures which Windows Performance Counter metrics will be sent to the AppDynamics Controller via the AppDynamics.Agent.Coordinator Windows service.

- * ExtensionService.bat - Manages extension service without UI. This file can be used for unattended installation and managing of extension service.

## Prerequisites

- The AppDynamics .NET Agent

- .NET 4.5 or later

## Installation

Download and unzip the archive to any fixed location, such as %ProgramData%\Appdynamics or just C:\ Once unzipped, you should see previously mentioned files and folders, along with other required configuration or library files.

## Overview of Extension Types

Presently, the .NET agent extension service supports following extensions types:

- Event extensions - Event extensions are used to send custom Events to the controller. https://docs.appdynamics.com/21.10/en/appdynamics-essentials/monitor-events .

- Metric extensions - Metric extensions are used to extend the capability of agent to collect any metric from the machine or any other running application. These metrics can then be seen in the controller Metric Browser under following path: Application Infrastructure Performance - [Any Tier] - Custom Metrics - Performance Monitor - [Extensioin Name]. Additionally health rules can be created for these metrics to trigger Alerts when necessary.

Some commonly used extensions have been bundled along with the Extension Manager.

- Windows Event log Watcher (Event extension)

- Windows Reboot Watcher (Event extension)

- Windows Service Status Monitor (Metric extension)

- Script Monitor (Metric extension)

By default, all provided extensions are disabled. You can enable them by editing their corresponding XML configuration file. Please visit their respective extension pages for more details to enable.c

## Getting Started

- * Click the Install button to install the AppDynamics.Agent.Extension Windows service.

- * By defualt we dont have any extensions loaded. We need to create a new folder for any extension, under [Extension Manager]/Extensions directory. Extension folder must have valid extension.xml file in it. Once copied we should be able to see extension loaded upon relaunching extension manager ui.

- * Click the "Manage" button next to any extension to edit the XML configuration file located as /Extensions/[Extension Name]/extension.xml . Alternatively the XML editor of your choice can be used to edit and save these files.

- * Now click Start to start extension service.

- EVENT extensions make use of the AppDynamics Controller REST API and require controller user credentials to be added to their configuration file.

- METRIC extensions create Windows Performance Counters to store metric data until it's sent to the Controller via the AppDynamics.Agent.Coordinator service. In step #4 below, we'll add these Performance Counters to the AppDynamics.Agent.Coordinator configuration file (config.xml).

- Once you've updated the configuration for these extensions, you'll want to recycle the AppDynamics.Agent.Extension Windows Service for these changes to take effect. Note : it could take up to a minute for the service to stop. This time is necessary to terminate and clean all the resources effectively.

- Restart the AppDynamics.Agent.Coordinator service for the changes made in config.xml to take effect.

- For EVENT extensions, you should see new custom events sent to the controller. https://docs.appdynamics.com/21.10/en/appdynamics-essentials/monitor-events.

- For METRIC extensions, you can find the new metrics in the Metric Browser under Application Infrastructure Performance - [Any Tier] - Custom Metrics - Performance Monitor - [Extensioin Name].

## Unattended Installation

Extension Service can be managed using following commands-

- start

- stop

- restart

- install

- uninstall

- encrypt [data-to-encrypt]

Usage:

## Encrypt Password

To avoid using password in plain text, we can use encrypted passwords in extension.xml for any event type extensions.

Encrypt password-

- Run following command:

ExtensionService.bat encrypt mYp@ssW0rd!

- Output would be similar to:

Encrypting password -> mYp@ssW0rd! JDZwM2ZvNlc=

- Here JDZwM2ZvNlc= is the encrypted value for given password, which we can copy and use in extension.xml

Once we get encrypted password, we need to copy it in extension.xml along with attribute encrypted="true". As following

<controller-info user="admin" account="anurag" password="JDZwM2ZvNlc=" encrypted="true" />

Default value for attribute encrypted is false. To use password in plain text, set the encrypted to false or remove the attribute.

## Troubleshooting

If you're not seeing metrics reported to the controller, check to make sure the custom Windows Performance Counters created by the Extension Service have been added to the AppDynamics.Agent.Coordinator configuration file (config.xml). If the Performance Counters have been added, try restarting the Coordinator to ensure the configuration has been picked up. If this doesn't help, check the Logs folder for any errors.

## Upgrade

- Download and extract latest version of extension manager

- Stop extension service and uninstall

- Copy Extensions directory from old install location

- Launch Appdynamics.Extension.Manager.exe from new installation and install extension service.

- Start Extension Service to use latest version.

## Releases Notes

1.4.2

- Support for custom location for config.xml file.

- Use of encrypted password for controller communication.

1.5.0

- Support for TLS1.2.

- Upgraded project to .NET 4.5.

1.5.1

- Improved and fixed issues with encryption.

- Improved logging for event based extension.

1.5.2

- Windows event properties (eventid, eventsource, machinename) are now part of controller properties.

- Removed event message limit.

## Notice and Disclaimer

All Extensions published by AppDynamics are governed by the Apache License v2 and are excluded from the definition of covered software under any agreement between AppDynamics and the User governing AppDynamics Pro Edition, Test & Dev Edition, or any other Editions.