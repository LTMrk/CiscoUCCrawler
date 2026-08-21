---
doc_id: developer-cisco-com-codeexchange-github-repo-jbsouthe-appdynamics-licensemonitoring-maextension-0bcd704b6d
source_url: https://developer.cisco.com/codeexchange/github/repo/jbsouthe/AppDynamics-LicenseMonitoring-MAExtension
retrieved_at: 2026-08-21T06:01:47.068299+00:00
---

# AppDynamics License Monitoring Machine Agent Extension

## Use Cases

This extension monitors the AppDynamics Controller Licenses and License Rules.

## Prerequisites

- Before the extension is installed, the prerequisites mentioned here need to be met. Please do not proceed with the extension installation if the specified prerequisites are not met.

- Make sure that the machine agent server has access to the Controller URL to be monitored, if different from the machine agent registration controller.

## Configuration

Unzip/Untar the distribution archive into the Machine Agent ./monitors subdirectory

Edit the config.xml within the monitors/LicenseMonitor/ subdirectory

Add the following configuration options:

```
<task-arguments>
        <argument name="controllerURL" is-required="true" default-value="https://customer.saas.appdynamics.com/" />
        <argument name="apiClientId" is-required="true" default-value="APIUser@customer" />
        <argument name="apiClientSecret" is-required="true" default-value="theBigCrazySecretString:)" />
</task-arguments>
```

## Metrics Provided

- Custom Metrics|License Monitor|Applications|< App Name>|vCpuTotal

- Custom Metrics|License Monitor|Applications|< App Name>|< Host Name>|vCPU

- Custom Metrics|License Monitor|Applications|< App Name>|< Host Name>|nodeCount

- Custom Metrics|License Monitor|Rules|< License Rule Name>|provisioned

- Custom Metrics|License Monitor|Rules|< License Rule Name>|inUseCount

- Custom Metrics|License Monitor|Rules|< License Rule Name>|freeCount

- Custom Metrics|License Monitor|Modules|< License Module Name>|provisioned

How do you like this sample code?