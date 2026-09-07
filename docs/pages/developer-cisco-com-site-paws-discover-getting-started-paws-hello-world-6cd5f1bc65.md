---
doc_id: developer-cisco-com-site-paws-discover-getting-started-paws-hello-world-6cd5f1bc65
source_url: https://developer.cisco.com/site/paws/discover/getting-started/paws-hello-world/
retrieved_at: 2026-09-07T14:17:31.998315+00:00
---

## PAWS "Hello World"

To get started with using PAWS, lets look at a simple example.

Example scenario: You want to upgrade a server which includes preparing the server for the upgrade, doing the actual upgrade and monitoring the upgrade process.

To complete this task, you will need to:

- Activate the PAWS Web Service

- Determine which files are available for the upgrade.

- Prepare the server for the upgrade.

- Start the upgrade.

- Monitor the upgrade process.

Activate the PAWS Web Service The PAWS web service needs to be activated and running before you can begin to use the PAWS APIs. The PAWS service can be activated through  CLI commands or through the Serviceability Administration page.  You find out more about how to activate PAWS in the developer guide.

Determine which files are available for the upgrade You first need to determine which file(s) of those available in the FTP or SFTP directory are valid for the upgrade. You use the upgradeFilter Service for this purpose. First your client application will need to get the list of possible upgrade file names from the FTP or SFTP directory and build of list of those names.  Then the client application will send this list to the upgradeFilter Service, and the upgradeFilter Service will determine which of these upgrades are valid.  Within the Platform Administrative Web Services request message after the header, you enter this code:

<SOAP-ENV:Body> <upgradeFilter xmlns="http://services.api.platform.vos.cisco.com"> <args0>patch</args0> <args1>UCSInstall_UCOS_8.6.0.98000-9002.iso</args1> <args1>UCSInstall_UCOS_8.6.0.98000-9012.iso</args1> <args1>UCSInstall_UCOS_8.6.0.98000-9020.iso</args1> </upgradeFilter> </SOAP-ENV:Body>

Prepare the server for the upgrade. Using the results of this call, UCSInstall_UCOS_8.6.0.98000-9012.iso, you next prepare the server for the upgrade using the PrepareUpgradeService, prepareRemoteUpgrade call. Within this Platform Administrative Web Services request message after the header, you enter this code:

<soapenv:Body> <ser:prepareRemoteUpgrade> <ser:args0> <xsd:name>UCSInstall_UCOS_9.0.0.95045-30.iso</xsd:name> <xsd:password>password</xsd:password> <xsd:path>/ks/sw/ccm/official-patches</xsd:path> <xsd:server>bldr-ccm77</xsd:server> <xsd:upgradeLocation>upgradefile.location.remote.sftp</xsd:upgradeLocation> <xsd:upgradeType>patch</xsd:upgradeType> <xsd:user>root</xsd:user> </ser:args0> <ser:args1>pm123</ser:args1> <ser:args2>false</ser:args2> </ser:prepareRemoteUpgrade> </soapenv:Body>

Start the Upgrade. You are now ready to start the upgrade. Within this Platform Administrative Web Services request message after the header, you enter this code:

<SOAP-ENV:Body> <startUpgrade xmlns="server_url"> <args0>pm238</args0> <args1>false</args1> <args2>false</args2> </startUpgrade> </SOAP-ENV:Body>

Monitor the upgrade process. To monitor the process of the upgrade, use the UpgradeStage Service, upgradeStage request call. Within this Platform Administrative Web Services request message after the header, you enter this code:

<SOAP-ENV:Body> <getUpgradeStage xmlns="http://services.api.platform.vos.cisco.com"/> </SOAP-ENV:Body>

You can see these API calls in action in the sample application:

- PAWS Sample Application

Subscribe to receive the latest news and updates

Subscribe