---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-mpp-conversion-enterprise-to-mpp-cuip-b-conversion-guide-ipphone--e9bfb0e592
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/MPP-conversion/enterprise-to-mpp/cuip_b_conversion-guide-ipphone/cuip_b_conversion-guide-ipphone_chapter_01.html
retrieved_at: 2026-08-25T16:53:40.438560+00:00
---

Cisco IP Phone 7800 and 8800 Series Migration Guide (On-Premises to Multiplatform Phones)

# Cisco IP Phone 7800 and 8800 Series Migration Guide (On-Premises to Multiplatform Phones)

Find Matches in This Book

## Results

Updated: March 29, 2019

Chapter: Migration Process

## Chapter: Migration Process

# Migration Process

## Conversion Process Workflow

You can migrate the phone in one step without upgrading the phone to an intermediary firmware.

Use this workflow to migrate an on-premises phone to a multiplatform phone (MPP).

The migration process factory resets the phone, and the phone will lost information such as contacts and call history.

Prepare for the Migration

Set up your phone for the pre-conversion process.

Upgrade Your Enterprise Phone with the Latest On-Premises Firmware

Upgrade your phone with the latest firmware.

Migration to Multiplatform Phone Firmware Upgrade

Upgrade the migration firmware of your phone to multiplatform phone firmware.

## Prepare for the Migration

You need to prepare your phone before you start with the migration process.

### Before you begin

Migration License files—You can download the files from the License Registration Portal.

Migration firmware files—The eDelivery email instructions you get with the license file contain a URL to the download page.
                                    Use this URL to download the zip file. Extract the files to your computer and upload them to the TFTP or HTTP server.

Multiplatform phones firmware files—You can download these files from the Cisco's Software Download page.

Valid TFTP or HTTP server address

Upload the following files to your TFTP or HTTP server that you use to transfer the files to your phone.

Migration License files

Migration firmware files

MPP phones firmware files

See the Before You Begin section to know how to get the files.

Host the firmware files on the server. You can also host the firmware files on the TFTP server.

```
http://your-file-server.com/sip88xx.11-2-3MPP-398.loads
```

The above example is only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                      to choose correct firmware file based on the on the phone model.

Host the license files on the server. You can also host the license files on the TFTP server.

```
http://your-file-server.com/Ent-2-Mpp-licenses/AB123456DE78.lic
```

where:

your-file-server.com —server to host the files.

Ent-2-Mpp-licenses —name of the directory where enterprise to MPP conversion license files are extracted from a zip file.

AB123456DE78.lic —license file name (upper case MAC address).

If you want to migrate the phones automatically at once, set up the supported DHCP options or EDOS redirection.

For more information on DHCP options, see DHCP Options Auto Provisioning

For more information on EDOS setup, see Cloud Provisioning (EDOS) References

Migration firmware is a flavour of MPP firmware. Hence, in this setup, you can use the same DHCP options and EDOS redirection
                                          that is supported in any MPP phones.

### Upgrade Your Enterprise Phone with the Latest On-Premises Firmware

Your enterprise phone must be running Firmware Release 12.5(1) or later.

Use the on-premises release notes to obtain the latest firmware.

Cisco IP Phone 7800 Series: https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-7800-series/products-release-notes-list.html

Cisco IP Phone 8800 Series: https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-release-notes-list.html

Use this document to upgrade individual on-premises phone to the firmware load 12.5 or later.

https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213288-upgrade-ip-phone-firmware-individually.html

### Migration  to Multiplatform Phone Firmware Upgrade

You can upgrade your phone with migration firmware to a Multiplatform phone firmware in one of these ways:

You can upgrade your phone to a Multiplatform phone firmware in one of these ways:

Migrate your Phone to a Multiplatform Phone Directly —Migrates the phone directly in one-step.

Provision the Phone Automatically —Provision the phones automatically when you upgrade multiple phones at once.

#### Migrate your Phone to a Multiplatform Phone Directly

You can now migrate your enterprise phone to a multiplatform phone easily in one step without using transition firmware load.

##### Before you begin

Valid FTP server address

Signed MPP COP file (Firmware Release 11.3(5) or later

CUCM server access

An enterprise phone running SIP Firmware Release 14.(1) or later. But phone running with SIP Firmware Release earlier than
                                          14.(1) still needs E2M COP file for the migration.

To upgrade your phone with latest firmware load, see Upgrade Your Enterprise Phone with the Latest On-Premises Firmware .

In the CUCM server, select Device > Phone , find the specific phone and enter the MPP load file name as the Phone Load Name .

In the Load Server parameter, enter the load server IP address and save the settings.

Click Apply Config .

The Requested Load ID parameter displays the MPP load provided by you. If you access the Phone information screen on the phone, you can view the the same MPP firmware load. After the MPP firmware migration completes, the Status > Product information > Software version displays the MPP firmware load used for the process and indicates successful migration. The phone might ask for the migration
                                                license to authorize.

On the phone web interface of the migrated MPP phone, select Voice > Provisioning .

In the Firmware Upgrade section, configure the Transition Authorization Rule parameter by entering a value to obtain and authorize the licence from the server.

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<Trans_Auth_Rule ua="na">http://10.74.51.81/prov/migration/E2312.lic</Trans_Auth_Rule>
```

In the Transition Authorization Type parameter, set the license type.

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<Trans_Auth_Type ua="na">Classic</Trans_Auth_Type>
```

Select Ext(n) > Proxy and Registration , and enter the corresponding proxy in the Proxy parameter. Then add the User ID under the Subscriber Information section.

Click Submit All Changes .

To verify if the migration is successful, check the Software Version and Transition Authorization Type values from the Info > Status > Product Information . You can also access Transition Authorization Status parameter from Info > Download Status to check if the authorization is successful.

#### Provision the Phone Automatically

Provision your phone that is running migration firmware using DHCP options 66,160,159,150 or with EDOS cloud provisioning.

Ensure both authorization (license) file URL and upgrade URL are specified in your XML configurations in this format:

```
<Upgrade_Ruleua="na">http://your-file-server.com/sip88xx.11-2-3MPP-398.loads</Upgrade_Rule>
```

```
<Trans_Auth_Ruleua="na">http://your-file-server.com/$MAU.lic</Trans_Auth_Rule>
```

```
<Trans_Auth_Type ua="na">Classic</Trans_Auth_Type>
```

The above examples are only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                            to choose correct firmware file based on the on the phone model.

For more information on DHCP options, see DHCP Options Auto Provisioning

For more information on EDOS setup, see Cloud Provisioning (EDOS) References

##### DHCP Options Auto Provisioning

This DHCP option based auto provisioning works only if the Profile Rule starts with "/" character. For new phones or during the factory reset of a multiplatform phone, the Profile Rule is set to /$PSN.xml to ensure
                                       successful auto provisioning. The phone supports DHCP options 66,160,159,150,60,43, and 125.

The supported DHCP options can be configured manually in one of the formats:

```
<schema>://<domain><:port>/<path>
```

```
<schema>://<domain><:port>
```

<ip address>

Multiformat: <url1 or ip1>;<url2 or ip2>

For example: DHCP Option 66 uses IP Format1, DHCP Option 150 uses multiformat with IP1; IP2, DHCP Option 160 and option 159
                                       uses URL format 1 or URL format 2.

The following tail options are added in subsequent attempts if some URL does not work.

tail 1: Profile Rule($PSN.xml)

tail 2: /Cisco/$PN/$MA.cfg

For all supported DHCP options, the DHCP auto provision URL will be attempted in the following way:

```
https://10.23.45.67/path
```

```
https://10.23.45.67/path
```

```
https://10.23.45.67/path/$PSN.xml
```

For example

```
https://10.23.45.67/path/8851-3PCC.xml
```

```
https://10.23.45.67/path/Cisco/$PN/$MA.cfg
```

For example

```
https://10.23.45.67/path/Cisco/CP-8851-3PCC/001234ab45de.cfg
```

```
https://10.23.45.67
```

```
https://10.23.45.67/$PSN.xml
```

```
https://10.23.45.67/8851-3PCC.xml
```

```
https://10.23.45.67/Cisco/$PN/$MA.xml
```

```
https://10.23.45.67/Cisco/CP-8851-3PCC/001234ab45de.cfg
```

For example: IP: 10.23.45.67 is specified as DHCP option for Cisco IP Phone Cisco 8851 with MAC 001234ab45de, the following
                                             attempts are made.

```
tftp://10.23.45.67/$PSN.xml
```

```
tftp://10.23.45.67/8851-3PCC.xml
```

```
tftp://10.23.45.67/Cisco/$PN/$MA.cfg
```

```
tftp://10.23.45.67/Cisco/CP-8851-3PCC/001234ab45de.cfg
```

```
http://10.23.45.67/$PSN.xml
```

```
http://10.23.45.67/8851-3PCC.xml
```

```
http://10.23.45.67/Cisco/$PN/$MA.cfg
```

```
http://10.23.45.67/Cisco/CP-8851-3PCC/001234ab45de.cfg
```

```
https://10.23.45.67/$PSN.xml
```

```
https://10.23.45.67/8851-3PCC.xml
```

```
https://10.23.45.67/Cisco/$PN/$MA.cfg
```

```
https://10.23.45.67/Cisco/CP-8851-3PCC/001234ab45de.cfg
```

The first part of URL1 or IP1 is attempted based on the above DHCP options.

The second part URL2 or IP2 is attempted based on the above DHCP options.

##### Cloud Provisioning (EDOS) References

| Important | The migration process factory resets the phone, and the phone will lost information such as contacts and call history. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Prepare for the Migration | Set up your phone for the pre-conversion process. |
| Step 2 | Upgrade Your Enterprise Phone with the Latest On-Premises Firmware | Upgrade your phone with the latest firmware. |
| Step 3 | Migration to Multiplatform Phone Firmware Upgrade | Upgrade the migration firmware of your phone to multiplatform phone firmware. |

| Step 1 | Upload the following files to your TFTP or HTTP server that you use to transfer the files to your phone. Migration License files Migration firmware files MPP phones firmware files See the Before You Begin section to know how to get the files. |
|---|---|
| Step 2 | Host the firmware files on the server. You can also host the firmware files on the TFTP server. http://your-file-server.com/sip88xx.11-2-3MPP-398.loads Note The above example is only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                      to choose correct firmware file based on the on the phone model. | Note | The above example is only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                      to choose correct firmware file based on the on the phone model. |
| Note | The above example is only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                      to choose correct firmware file based on the on the phone model. |
| Step 3 | Host the license files on the server. You can also host the license files on the TFTP server. http://your-file-server.com/Ent-2-Mpp-licenses/AB123456DE78.lic where: your-file-server.com —server to host the files. Ent-2-Mpp-licenses —name of the directory where enterprise to MPP conversion license files are extracted from a zip file. AB123456DE78.lic —license file name (upper case MAC address). |
| Step 4 | If you want to migrate the phones automatically at once, set up the supported DHCP options or EDOS redirection. For more information on DHCP options, see DHCP Options Auto Provisioning For more information on EDOS setup, see Cloud Provisioning (EDOS) References Migration firmware is a flavour of MPP firmware. Hence, in this setup, you can use the same DHCP options and EDOS redirection
                                          that is supported in any MPP phones. |

| Note | The above example is only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                      to choose correct firmware file based on the on the phone model. |
|---|---|

| Step 1 | Use the on-premises release notes to obtain the latest firmware. Cisco IP Phone 7800 Series: https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-7800-series/products-release-notes-list.html Cisco IP Phone 8800 Series: https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-release-notes-list.html |
|---|---|
| Step 2 | Use this document to upgrade individual on-premises phone to the firmware load 12.5 or later. https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213288-upgrade-ip-phone-firmware-individually.html |

| Step 1 | In the CUCM server, select Device > Phone , find the specific phone and enter the MPP load file name as the Phone Load Name . |
|---|---|
| Step 2 | In the Load Server parameter, enter the load server IP address and save the settings. |
| Step 3 | Click Apply Config . The Requested Load ID parameter displays the MPP load provided by you. If you access the Phone information screen on the phone, you can view the the same MPP firmware load. After the MPP firmware migration completes, the Status > Product information > Software version displays the MPP firmware load used for the process and indicates successful migration. The phone might ask for the migration
                                                license to authorize. |
| Step 4 | On the phone web interface of the migrated MPP phone, select Voice > Provisioning . |
| Step 5 | In the Firmware Upgrade section, configure the Transition Authorization Rule parameter by entering a value to obtain and authorize the licence from the server. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Trans_Auth_Rule ua="na">http://10.74.51.81/prov/migration/E2312.lic</Trans_Auth_Rule> |
| Step 6 | In the Transition Authorization Type parameter, set the license type. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Trans_Auth_Type ua="na">Classic</Trans_Auth_Type> |
| Step 7 | Select Ext(n) > Proxy and Registration , and enter the corresponding proxy in the Proxy parameter. Then add the User ID under the Subscriber Information section. |
| Step 8 | Click Submit All Changes . To verify if the migration is successful, check the Software Version and Transition Authorization Type values from the Info > Status > Product Information . You can also access Transition Authorization Status parameter from Info > Download Status to check if the authorization is successful. |

| Provision your phone that is running migration firmware using DHCP options 66,160,159,150 or with EDOS cloud provisioning. Ensure both authorization (license) file URL and upgrade URL are specified in your XML configurations in this format: <Upgrade_Ruleua="na">http://your-file-server.com/sip88xx.11-2-3MPP-398.loads</Upgrade_Rule> <Trans_Auth_Ruleua="na">http://your-file-server.com/$MAU.lic</Trans_Auth_Rule> <Trans_Auth_Type ua="na">Classic</Trans_Auth_Type> Note The above examples are only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                            to choose correct firmware file based on the on the phone model. For more information on DHCP options, see DHCP Options Auto Provisioning For more information on EDOS setup, see Cloud Provisioning (EDOS) References | Note | The above examples are only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                            to choose correct firmware file based on the on the phone model. |
|---|---|---|
| Note | The above examples are only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                            to choose correct firmware file based on the on the phone model. |

| Note | The above examples are only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                            to choose correct firmware file based on the on the phone model. |
|---|---|