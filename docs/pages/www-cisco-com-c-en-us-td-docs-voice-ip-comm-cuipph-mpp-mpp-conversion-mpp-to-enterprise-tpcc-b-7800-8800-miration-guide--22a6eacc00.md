---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-mpp-conversion-mpp-to-enterprise-tpcc-b-7800-8800-miration-guide--22a6eacc00
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/MPP-conversion/mpp-to-enterprise/tpcc_b_7800-8800-miration-guide-mpp-to/tpcc_b_7800-8800-miration-guide-mpp-to_chapter_01.html
retrieved_at: 2026-09-01T17:22:28.928532+00:00
---

Cisco IP Phone 7800 and 8800 Series Migration Guide (Multiplatform Phones to On-Premises)

# Cisco IP Phone 7800 and 8800 Series Migration Guide (Multiplatform Phones to On-Premises)

Find Matches in This Book

## Results

Updated: April 2, 2019

Chapter: Migration Process

## Chapter: Migration Process

# Migration Process

## Conversion Process Workflow

In release 11.3.5 and later, you can migrate the phone in one step without upgrading the phone to an intermediary firmware.

Use this workflow to migrate a multiplatform phone (MPP) to an on-premises phone.

The migration process factory resets the phone, and the phone will lost information such as contacts and call history.

Prepare for the Migration

Set your phone for pre-conversion process.

Upgrade Your Multiplatform Phone with the Latest Firmware

Upgrade your phone with the latest firmware.

Migration Firmware to On-premises Phone Firmware Upgrade

Upgrade the migration firmware of your phone to on-premises phone firmware.

## Prepare for the Migration

You need to prepare your setup before you start with the migration process.

### Before you begin

Migration License files—You can download the files from the License Registration Portal.

Migration firmware files—The eDelivery email instructions you get with the license file contain a URL to the download page.
                                    Use this URL to download the zip file. Extract the files to your computer and upload them to the TFTP or HTTP server.

On-premises phones firmware files—You can download these files from the Cisco's Software Download page.

Valid TFTP or HTTP server address

Upload the following files to the TFTP or HTTP server that you use to transfer the files to your phone.

Migration License files

Migration firmware files

On-premises phones firmware files

See the Before You Begin section to know how to get the files.

Host the firmware files on the server. You can also host the firmware files on the TFTP server.

### Example:

```
http://your-file-server.com/sip88xx.12-5-1SR1-4.loads
```

The above example is only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                      to choose correct firmware file based on the on the phone model.

Host the license files on the server. You can also host the firmware files on the TFTP server.

### Example:

```
http://your-file-server.com/MPP-2-ENT-licenses/AB123456DE78.lic
```

where:

your-file-server.com—server to host the files.

MPP-2-ENT-licenses—name of the directory where multiplatform to on-premises conversion license files are extracted from a
                                          zip file.

AB123456DE78.lic—license file name (upper case MAC address).

If you want to migrate the phones automatically at once, set up the supported DHCP options or EDOS redirection. You can set
                                       up the supported DHCP options or EDOS redirection for out-of-box multiplatform phone provisioning while the phone is running
                                       the migration firmware.

For more information on DHCP options, see DHCP Options Auto Provisioning

For more information on EDOS setup, see Cloud Provisioning (EDOS) References

### Upgrade Your Multiplatform Phone with the Latest Firmware

Your Multiplatform phone must be running with the latest Firmware Release.

Your phone must be running Firmware Release 11.3(5) or higher. Direct migration feature is not supported in releases older
                                 than 11.3(5).

Use the multiplatform phone release notes to obtain the latest firmware.

Cisco IP Phone 7800 Series: https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/products-release-notes-list.html

Cisco IP Phone 8800 Series: https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/products-release-notes-list.html

Refer the Upgrade the Firmware sections of the Multiplatform phones release notes to upgrade the phones.

## Migration Firmware to On-premises Phone Firmware Upgrade

You can upgrade your phone with migration firmware to an on-premises phone firmware in any one of these ways:

Migrate Your Phone to Enterprise Phone Directly —Migrate you phone to Enterpirse phone firmware directly without intermediary migration firmware

Provision the Phone Automatically —Provision the phones automatically when you upgrade multiple phones at once.

### Migrate Your Phone to Enterprise Phone Directly

You can now migrate your phone to enterprise phone easily in one step without using transition firmware load.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Provisioning .

In the Upgrade Rule field, set the Upgrade Rule parameter by entering a firmware upgrade script. For the syntax details, see  that defines upgrade
                                          conditions and associated firmware URLs. It uses the same syntax as Profile Rule. Enter a script and use the following format
                                          to enter the upgrade rule:

```
<tftp|http|https>://<ipaddress>/image/<load name>
```

For example:

```
tftp://192.168.1.5/image/sip78xx.14-1-1MN-366.loads
```

Configure the Transition Authorization Rule parameter by entering a value to obtain and authorize the licence from the server.

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<Trans_Auth_Rule ua="na">http://10.74.51.81/prov/migration/E2312.lic</Trans_Auth_Rule>
```

In the Transition Authorization Type parameter, set the license type as Classic .

You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format:

```
<Trans_Auth_Type ua="na">Classic</Trans_Auth_Type>
```

Click Submit All Changes .

### Provision the Phone Automatically

Provision your phone, which is running migration firmware, using DHCP options 66,160,159,150 or with EDOS cloud provisioning.

Ensure both authorization (license) file URL and upgrade URL are specified in your XML configurations in this format:

```
<Upgrade_Rule ua="na">http://your-file-server.com/sip88xx.12-5-1SR1-4.loads</Upgrade_Rule>
```

```
<Trans_Auth_Rule ua="na">http://your-file-server.com/$MAU.lic</Trans_Auth_Rule>
```

```
<Trans_Auth_Type ua="na">Classic</Trans_Auth_Type>
```

Ensure that Transition authorization Type parameter is set every time you set the Transition Authorization Rule .

For more information on DHCP options, see DHCP Options Auto Provisioning

For more information on EDOS setup, see Cloud Provisioning (EDOS) References

#### DHCP Options Auto Provisioning

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

#### Cloud Provisioning (EDOS) References

### Customers Also Viewed

- Cisco IP Phone 7800 and 8800 Series Migration Guide (Multiplatform Phones to On-Premises) --- Support Information

| Important | The migration process factory resets the phone, and the phone will lost information such as contacts and call history. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Prepare for the Migration | Set your phone for pre-conversion process. |
| Step 2 | Upgrade Your Multiplatform Phone with the Latest Firmware | Upgrade your phone with the latest firmware. |
| Step 3 | Migration Firmware to On-premises Phone Firmware Upgrade | Upgrade the migration firmware of your phone to on-premises phone firmware. |

| Step 1 | Upload the following files to the TFTP or HTTP server that you use to transfer the files to your phone. Migration License files Migration firmware files On-premises phones firmware files See the Before You Begin section to know how to get the files. |
|---|---|
| Step 2 | Host the firmware files on the server. You can also host the firmware files on the TFTP server. Example: http://your-file-server.com/sip88xx.12-5-1SR1-4.loads Note The above example is only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                      to choose correct firmware file based on the on the phone model. | Note | The above example is only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                      to choose correct firmware file based on the on the phone model. |
| Note | The above example is only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                      to choose correct firmware file based on the on the phone model. |
| Step 3 | Host the license files on the server. You can also host the firmware files on the TFTP server. Example: http://your-file-server.com/MPP-2-ENT-licenses/AB123456DE78.lic where: your-file-server.com—server to host the files. MPP-2-ENT-licenses—name of the directory where multiplatform to on-premises conversion license files are extracted from a
                                          zip file. AB123456DE78.lic—license file name (upper case MAC address). |
| Step 4 | If you want to migrate the phones automatically at once, set up the supported DHCP options or EDOS redirection. You can set
                                       up the supported DHCP options or EDOS redirection for out-of-box multiplatform phone provisioning while the phone is running
                                       the migration firmware. For more information on DHCP options, see DHCP Options Auto Provisioning For more information on EDOS setup, see Cloud Provisioning (EDOS) References |

| Note | The above example is only applicable for the Cisco IP Phone 8800 Series Multiplatform phones with audio features. You need
                                                      to choose correct firmware file based on the on the phone model. |
|---|---|

| Step 1 | Use the multiplatform phone release notes to obtain the latest firmware. Cisco IP Phone 7800 Series: https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/products-release-notes-list.html Cisco IP Phone 8800 Series: https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/products-release-notes-list.html |
|---|---|
| Step 2 | Refer the Upgrade the Firmware sections of the Multiplatform phones release notes to upgrade the phones. |

| Step 1 | Select Voice > Provisioning . |
|---|---|
| Step 2 | In the Upgrade Rule field, set the Upgrade Rule parameter by entering a firmware upgrade script. For the syntax details, see  that defines upgrade
                                          conditions and associated firmware URLs. It uses the same syntax as Profile Rule. Enter a script and use the following format
                                          to enter the upgrade rule: <tftp\|http\|https>://<ipaddress>/image/<load name> For example: tftp://192.168.1.5/image/sip78xx.14-1-1MN-366.loads |
| Step 3 | Configure the Transition Authorization Rule parameter by entering a value to obtain and authorize the licence from the server. You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Trans_Auth_Rule ua="na">http://10.74.51.81/prov/migration/E2312.lic</Trans_Auth_Rule> |
| Step 4 | In the Transition Authorization Type parameter, set the license type as Classic . You can also configure this parameter in the configuration file (cfg.xml) by entering a string in this format: <Trans_Auth_Type ua="na">Classic</Trans_Auth_Type> |
| Step 5 | Click Submit All Changes . |

| Provision your phone, which is running migration firmware, using DHCP options 66,160,159,150 or with EDOS cloud provisioning. Ensure both authorization (license) file URL and upgrade URL are specified in your XML configurations in this format: <Upgrade_Rule ua="na">http://your-file-server.com/sip88xx.12-5-1SR1-4.loads</Upgrade_Rule> <Trans_Auth_Rule ua="na">http://your-file-server.com/$MAU.lic</Trans_Auth_Rule> <Trans_Auth_Type ua="na">Classic</Trans_Auth_Type> Note Ensure that Transition authorization Type parameter is set every time you set the Transition Authorization Rule . For more information on DHCP options, see DHCP Options Auto Provisioning For more information on EDOS setup, see Cloud Provisioning (EDOS) References | Note | Ensure that Transition authorization Type parameter is set every time you set the Transition Authorization Rule . |
|---|---|---|
| Note | Ensure that Transition authorization Type parameter is set every time you set the Transition Authorization Rule . |

| Note | Ensure that Transition authorization Type parameter is set every time you set the Transition Authorization Rule . |
|---|---|