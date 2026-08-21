---
doc_id: developer-cisco-com-codeexchange-github-repo-appdynamics-netscaler-monitoring-extension-93ec4b431a
source_url: https://developer.cisco.com/codeexchange/github/repo/Appdynamics/netscaler-monitoring-extension
retrieved_at: 2026-08-21T06:01:34.242269+00:00
---

# AppDynamics Monitoring Extension for Citrix NetScaler

### Use Case

Citrix NetScaler is an all-in-one web application delivery controller (ADC) that makes applications run up to five times faster, cuts web application ownership costs with server offloading, and makes sure that applications are always available with its application load balancing capabilities.

NetScaler VPX provides the complete NetScaler web and application load balancing, secure and remote access, acceleration, security and offload feature set in a simple, easy-to-install virtual appliance.

The AppDynamics monitoring extension for NetScaler provides metrics collected by the NetScaler appliance about the usage of its features and corresponding resources using the NITRO API. These metrics can be classified under the following groups:

Core System Metrics

Service Resource metrics

Load Balancing metrics

### Prerequisites

Before the extension is installed, the prerequisites mentioned here need to be met. Please do not proceed with the extension installation if the specified prerequisites are not met.

The NetScaler extension connects to the Citrix Netscaler appliance using the NITRO REST API.

The extension needs to be able to connect to the NetScaler NITRO API in order to be able to collect and send the metrics. To do this, you will have to either establish a remote connection in between the extension and the product, or have an agent on the same machine running the product in order for the extension to collect and send the metrics.

### Installation

- To build from source, clone this repository and run 'mvn clean install'. This will produce a NetScalerMonitor-VERSION.zip in the target directory

- Unzip the file NetScalerMonitor-[version].zip into <MACHINE_AGENT_HOME>/monitors/

- In the newly created directory "NetScalerMonitor", edit the config.yml configuring the parameters (See Configuration section below)

- Restart the machine agent

Please place the extension in the "monitors" directory of your Machine Agent installation directory. Do not place the extension in the "extensions" directory of your Machine Agent installation directory.

### Configuration

Configure the NetScaler parameters by editing the config.yml file in <MACHINE_AGENT_HOME>/monitors/NetScalerMonitor/ .

Here is a sample config.yml file

```
# Please refer to Extensions Troubleshooting Document (https://community.appdynamics.com/t5/Knowledge-Base/How-do-I-troubleshoot-missing-custom-metrics-or-extensions/ta-p/28695) for instructions on how to configure metric prefix

#Metric prefix when SIM is enabled
#metricPrefix: Custom Metrics|NetScaler Monitor|

#This will create this metric in the tier, under this path
metricPrefix: "Server|Component:<Tier ID>|Custom Metrics|Netscaler Monitor|"

# Configure your Netscaler ADX servers here
servers:
 - name: ""
   host: ""
   port: ""
   username: ""
   password: ""
   encryptedPassword: ""

#Please refer to the Password Encryption Documentation for instructions on how to configure an encryptionKey & encryptedPassword
encryptionKey:

numberOfThreads: 20
```

Configure the path to the config.yml & metrics.xml by editing the  in the monitor.xml file in the <MACHINE_AGENT_HOME>/monitors/NetScalerMonitor/ directory. Below is the sample

```
<task-arguments>
    <!-- config file-->
    <argument name="config-file" is-required="true" default-value="monitors/NetScalerMonitor/config.yml" />
    <argument name="metric-file" is-required="true" default-value="monitors/NetScalerMonitor/metrics.xml" />
     ....
</task-arguments>
```

Restart the machine agent.

### Metrics

Here is a summary of the metrics published by this extension. You can add/remove metrics of your choosing by modifying the provided metrics.xml file by using the correct stat names as per the Citrix documentation

### Credentials Encryption

Please visit this page to get detailed instructions on password encryption. The steps in this document will guide you through the whole process.

### Extensions Workbench

Workbench is an inbuilt feature provided with each extension in order to assist you to fine tune the extension setup before you actually deploy it on the controller. Please review the following document for how to use the Extensions WorkBench

### Troubleshooting

Please follow the steps listed in the troubleshooting document in order to troubleshoot your issue. These are a set of common issues that customers might have faced during the installation of the extension.

### Contributing

Always feel free to fork and contribute any changes directly via GitHub .

## Version

Note : While extensions are maintained and supported by customers under the open-source licensing model, they interact with agents and Controllers that are subject to AppDynamics’ maintenance and support policy . Some extensions have been tested with AppDynamics 4.5.13+ artifacts, but you are strongly recommended against using versions that are no longer supported.

How do you like this sample code?

| Metric Class | Description |
|---|---|
| Load Balancing | Metric Description tothits Total number of hits totalrequests Total number of requests totalresponses Total number of responses cursrvrconnections Number of connections to the server behind the virtual server curclntconnections Number of client connections state Current state of the system. Possible values: 
    - Down: 0
    - Up: 1
    - Unknown: 2 
    - Out of Service: 3
    - Transition out of service: 4
    - Down when going out of service: 5 | Metric | Description | tothits | Total number of hits | totalrequests | Total number of requests | totalresponses | Total number of responses | cursrvrconnections | Number of connections to the server behind the virtual server | curclntconnections | Number of client connections | state | Current state of the system. Possible values: 
    - Down: 0
    - Up: 1
    - Unknown: 2 
    - Out of Service: 3
    - Transition out of service: 4
    - Down when going out of service: 5 |
| Metric | Description |
| tothits | Total number of hits |
| totalrequests | Total number of requests |
| totalresponses | Total number of responses |
| cursrvrconnections | Number of connections to the server behind the virtual server |
| curclntconnections | Number of client connections |
| state | Current state of the system. Possible values: 
    - Down: 0
    - Up: 1
    - Unknown: 2 
    - Out of Service: 3
    - Transition out of service: 4
    - Down when going out of service: 5 |
| Service Resource | Metric Description throughput Throughput in mbps avgsvrttfb Average time to first byte totalrequests Total number of responses totalresponses Total number of responses cursrvrconnections Number of connections to the server curclntconnections Number of client connections activetransactions Number of active transactions handled by the service state Current state of the system. Possible values: 
    - Down: 0
    - Up: 1
    - Unknown: 2 
    - Out of Service: 3
    - Transition out of service: 4
    - Down when going out of service: 5 | Metric | Description | throughput | Throughput in mbps | avgsvrttfb | Average time to first byte | totalrequests | Total number of responses | totalresponses | Total number of responses | cursrvrconnections | Number of connections to the server | curclntconnections | Number of client connections | activetransactions | Number of active transactions handled by the service | state | Current state of the system. Possible values: 
    - Down: 0
    - Up: 1
    - Unknown: 2 
    - Out of Service: 3
    - Transition out of service: 4
    - Down when going out of service: 5 |
| Metric | Description |
| throughput | Throughput in mbps |
| avgsvrttfb | Average time to first byte |
| totalrequests | Total number of responses |
| totalresponses | Total number of responses |
| cursrvrconnections | Number of connections to the server |
| curclntconnections | Number of client connections |
| activetransactions | Number of active transactions handled by the service |
| state | Current state of the system. Possible values: 
    - Down: 0
    - Up: 1
    - Unknown: 2 
    - Out of Service: 3
    - Transition out of service: 4
    - Down when going out of service: 5 |
| System | Metric Description cpuusagepcnt CPU Utilization Percentage memsizemb Currently allocated memory in MB memusagepcnt Percentage of memory utilization | Metric | Description | cpuusagepcnt | CPU Utilization Percentage | memsizemb | Currently allocated memory in MB | memusagepcnt | Percentage of memory utilization |
| Metric | Description |
| cpuusagepcnt | CPU Utilization Percentage |
| memsizemb | Currently allocated memory in MB |
| memusagepcnt | Percentage of memory utilization |

| Metric | Description |
|---|---|
| tothits | Total number of hits |
| totalrequests | Total number of requests |
| totalresponses | Total number of responses |
| cursrvrconnections | Number of connections to the server behind the virtual server |
| curclntconnections | Number of client connections |
| state | Current state of the system. Possible values: 
    - Down: 0
    - Up: 1
    - Unknown: 2 
    - Out of Service: 3
    - Transition out of service: 4
    - Down when going out of service: 5 |

| Metric | Description |
|---|---|
| throughput | Throughput in mbps |
| avgsvrttfb | Average time to first byte |
| totalrequests | Total number of responses |
| totalresponses | Total number of responses |
| cursrvrconnections | Number of connections to the server |
| curclntconnections | Number of client connections |
| activetransactions | Number of active transactions handled by the service |
| state | Current state of the system. Possible values: 
    - Down: 0
    - Up: 1
    - Unknown: 2 
    - Out of Service: 3
    - Transition out of service: 4
    - Down when going out of service: 5 |

| Metric | Description |
|---|---|
| cpuusagepcnt | CPU Utilization Percentage |
| memsizemb | Currently allocated memory in MB |
| memusagepcnt | Percentage of memory utilization |

| Name | Version |
|---|---|
| Extension Version | 1.0.3 |
| Product Tested On | NetScaler VPX 10.x on AWS |
| Last Update | 01/08/2021 |
| Change List | ChangeLog |