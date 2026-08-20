---
doc_id: developer-cisco-com-codeexchange-github-repo-appdynamics-command-watcher-extension-777ee0054d
source_url: https://developer.cisco.com/codeexchange/github/repo/Appdynamics/Command-Watcher-Extension
retrieved_at: 2026-08-20T20:28:37.783538+00:00
---

# Command watcher extension

This extension works only with the standalone machine agent.

## Use Case

An AppDynamics extension that provide metrics from linux commands or script that generates a numeric output.

## Prerequisites

Before the extension is installed, the prerequisites mentioned here need to be met. Please do not proceed with the extension installation if the specified prerequisites are not met

## Installation

- Run "mvn clean install" from "CommandWatcherRepo"

- Unzip the contents of CommandWatcher-<version>.zip file (<CommandWatcherRepo> / targets) and copy the directory to <your-machine-agent-dir>/monitors .

- Edit config.yml file and provide the required configuration (see Configuration section)

- Restart the Machine Agent.

Please place the extension in the "monitors" directory of your Machine Agent installation directory. Do not place the extension in the "extensions" directory of your Machine Agent installation directory.

## Configuration

### Config.yml

Note : Please make sure to not use tab (\t) while editing yaml files

#### Configure metric prefix

Please follow section 2.1 of the Document to set up metric prefix.

```
#Metric prefix used when SIM is enabled for your machine agent
#metricPrefix: "Custom Metrics|Command Watcher|"

#This will publish metrics to specific tier
#Instructions on how to retrieve the Component ID can be found in the Metric Prefix section of https://community.appdynamics.com/t5/Knowledge-Base/How-do-I-troubleshoot-missing-custom-metrics-or-extensions/ta-p/28695
metricPrefix: "Server|Component:<COMPONENT OR TIER ID>|Custom Metrics|Command Watcher|"
```

#### Configure commandToProcess section

commandToProcess section should be configured like below:

```
commandToProcess:

  - displayName: "Home Dir File Count"
    command: "ls -ltr ~ | wc -l"
    isScript: false

  - displayName: "Java Processes List"
    command: "ps aux | grep java | wc -l"
    isScript: false

  - displayName: "Random Script"
    command: "/path/to/random_script.sh"
    isScript: true
```

- displayName: Display name for your command which will be displayed in metric path. It should be unique for all commands

- command: Command for which you want to collect metric. It can either be a command or path to some script file. The command or script must return single numerical value only.

- isScript: It is a flag which tells if the command to execute is a path to script file or a command. It can be "true" or "false"

#### Number of threads

Always include one thread per command + 1 (to run main task)

For e.g. if you have configured 4 commands, then number of threads required are 5 (4 to run commands + 1 to run main task).

```
numberOfThreads: 5
```

#### Thread timeout

It represents timeout for a thread in seconds.

```
threadTimeout: 30
```

#### Yml Validation

Please copy all the contents of the config.yml file and go here . On reaching the website, paste the contents and press the “Validate YAML” button.

### Metrics Provided

We provide metric related to output of the linux command or the script file that generates single numeric output.

For example: ps –ef | grep java |wc –l = 3

## Workbench

Workbench is an inbuilt feature provided with each extension in order to assist you to fine tune the extension setup before you actually deploy it on the controller. Please review the following document on How to use the Extensions WorkBench

## Troubleshooting

Please follow the steps listed in this troubleshooting-document in order to troubleshoot your issue. These are a set of common issues that customers might have faced during the installation of the extension.

## Contributing

Always feel free to fork and contribute any changes directly via GitHub .

## Version

Note : While extensions are maintained and supported by customers under the open-source licensing model, they interact with agents and Controllers that are subject to AppDynamics’ maintenance and support policy . Some extensions have been tested with AppDynamics 4.5.13+ artifacts, but you are strongly recommended against using versions that are no longer supported.

How do you like this sample code?

| Name | Version |
|---|---|
| Extension Version | 2.0.0 |
| Last Update | 05/08/2021 |
| Change List | ChangeLog |