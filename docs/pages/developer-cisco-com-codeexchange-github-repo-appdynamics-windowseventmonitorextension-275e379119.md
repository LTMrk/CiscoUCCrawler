---
doc_id: developer-cisco-com-codeexchange-github-repo-appdynamics-windowseventmonitorextension-275e379119
source_url: https://developer.cisco.com/codeexchange/github/repo/Appdynamics/WindowsEventMonitorExtension
retrieved_at: 2026-08-20T20:28:19.497554+00:00
---

# Windows Event Log Monitor

Windows Event Log Monitor works with .NET Agent Extension Manager to capture and report specific windows events.

## Contents

Windows Event Log monitor require extension.xml and WindowsEventMonitor.dll file to be placed in a new folder under <Extension Manager Root Directory>/Extensions

## Prerequisites

- .NET Agent Extension Manager

- The AppDynamics .NET Agent

- .NET 4.0 or later

## Installation

Download, unzip and copy extension.xml and WindowsEventMonitor.dll in a new folder under Extensions directory of .Net Extension Manager. Please refer to the next section for detailed steps.

## Getting Started

- Create a new folder under Extension Manager root directory. We can name it according to type of events we want to capture like IISEventMonitor or simply WindowsEventMonitor

- Copy extension.xml to this folder.

```
<extension type="Event" name="WindowsEventLogMonitor" enabled="true">
```

```
<controller-info user="username" account="customer1" password="password" />
```

```
<controller-event-properties>
    <add key="bt" value="/MyBT.aspx"></add>
    <add key="node" value="MyNodeName"></add>
    <add key="tier" value="MyTier"></add>
  </controller-event-properties>
```

- EventLogPath: Possible values are Application or System or Setup, etc . It is required and we can not remove this parameter.

- EventSources: We can provide any event source. Multiple values can be provided as comma separated strings. If we leave it empty it will report all event sources.

- EventID: We can provide any event Id. Multiple values can be provided as comma separated strings. If we leave it empty it will report all event id.

- EventLogEntryType: Possible values are Error, Information or Warning. If we leave it empty it will report all event types.

- EventLogMessageContains: We can provide any strings to be matched in event message. Multiple values can be provided as comma separated strings. This parameter can be left empty or commented.

- Save the file and launch Extension Manager UI. We should be able to see WindowsEventMonitor extension listed under "List of extensions loaded"

- We will see new custom events sent to the controller. We should be able to view link to Custom Events on Application Dashboard. For more details https://docs.appdynamics.com/21.10/en/appdynamics-essentials/monitor-events.

## Troubleshooting

If you're not seeing events reported to the controller, check to make sure the controller credentials are correct and try removing node/tier or BT mapping if added. If this doesn't help, check the Logs folder for any errors.

## Upgrade

- Upgrade to latest version of extension manager.

- Copy new extension.xml and make appropriate changes.

- Start Extension Service to use latest version.

## Release Notes

2.0.0

- Support for non-classic event sources.

- Make event source filter optional to capture all events.

## Notice and Disclaimer

All Extensions published by AppDynamics are governed by the Apache License v2 and are excluded from the definition of covered software under any agreement between AppDynamics and the User governing AppDynamics Pro Edition, Test & Dev Edition, or any other Editions.

How do you like this sample code?