---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-2-installation-guide-pcce-b-1262--e026971fc5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_2/installation/guide/pcce_b_1262_cisco_pcce_installationandupgrade_guide/pcce_m_uninstall-packaged-cce-release-126.html
retrieved_at: 2026-08-21T04:50:56.501028+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

Updated: March 9, 2026

Chapter: Uninstallation

## Chapter: Uninstallation

- Uninstallation

- Prerequisite for Uninstallation of CCE                               12.6(2)                              Maintenance Release

# Uninstallation

## Uninstallation of Unified ICM/CCE base version 12.5(1)

Uninstallation of Unified ICM/CCE base of 12.5(1) is not supported for Unified CCE components that are deployed on Windows Server using the ICM-CCE-Installer. However, support
                           for uninstallation and re-installation of client installer packages like Administration Client and Internet Script Editor
                           continues.

### Prerequisite for Uninstallation of CCE 12.6(2) Maintenance Release

If you have enabled the optional feature Outbound Option High Availability, you must disable it before you uninstall Unified ICM 12.6(2) . From Unified CCE Web Setup, choose Component Management > Loggers . Select a logger that is enabled for High Availability, and click Next until the Additional Options page appears. Uncheck the Enable High Availability check box. Perform this action for each logger enabled for Outbound Option High Availability.

If you are planning to roll back to previous version of CCE Release 12.6(2) , do the following:

```
keytool -export -keystore <ICM install Dir>\ssl\cacerts -alias <alias of the component> -file <filepath>.cer
```

Enter the truststore password when prompted.

After the roll back, do the following:

```
keytool -import -keystore <Oracle/OpenJDK JRE path>\lib\security\cacerts -file <filepath>.cer -alias <alias>
```

Enter the keystore password when prompted.

Enter yes when prompted to trust the certificate.

| Note | The option to roll back to previous versions is only available with minor and maintenance
                                    releases. |
|---|---|

| Note | You don't need to reimport the certificates if you are rolling back to CCE 12.5(1a) or 12.6(1). Also, if you have already
                                       installed ES55 (mandatory OpenJDK ES), you don't need to reimport the certificate when you roll back to CCE 12.5(1). |
|---|---|