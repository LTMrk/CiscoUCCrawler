---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-version-125-215014-troubleshoot-c45b0d7bb1
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-version-125/215014-troubleshoot-cisco-headset-5xx-series.html
retrieved_at: 2026-08-21T23:10:59.221997+00:00
---

Troubleshoot Cisco Headset 5XX Series

# Troubleshoot Cisco Headset 5XX Series

### Download Options

Updated: July 19, 2021

Document ID: 215014

Contents

## Contents

## Introduction

This document describes how to troubleshoot the Cisco headset 500 series. In Cisco Unified Communications Manager (CUCM) version 12.5(1)SU1, you are able to provide headset administration, inventory, and configuration management.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communications Manager

- Cisco IP phones

- Cisco headsets

- Packet capture

### Components Used

The information in this document is based on these software versions:

- CUCM: 12.5(1)SU1 (12.5.1.11900-146)

- Phone: CP-8861 (sip88xx.12-5-1SR3-74)

- Headset: 520 (Firmware 15-18-15), 532 (Firmware 15-18-15), 561 (Firmware 1-5-1-15), 562 (Firmware 1-5-1-15)

The information in this document was created from the devices in a specific lab environment. All the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Administrators can manage and troubleshoot all deployed Cisco headset from Cisco Unified Communications Manager (CUCM). Some features included in version 12.5(1)SU1 are:

- View summary and custom reports of all deployed headsets

- View report on headset model and connection status

- View detailed information on headset and endpoints and clients

- End-to-end diagnostics data to detect early detection and troubleshooting of potential problems

- Access headset-related debugging logs through Cisco endpoints and clients

- Headset related call quality data in CUCM Call Management Records (CMR)

In order to review the headset inventory, navigate to CM Administration > Device > Headset > Headset Inventory as shown in the image.

Note :The headset inventory is supported for devices such as 88xx, 78xx phones and Jabber.

## Configure

In order to know the configuration steps for Cisco headsets, you can visit the Configure Cisco Headset 5xx Guide.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

In CUCM 12.5 SU1, you can generate a Problem Report Tool (PRT) log from Cisco Unified Communications Manager Administration. This new feature, allows you to collect the phone logs remotely instead of generating the report from the phone. With this release, headset information is also displayed in the log, which you can use to troubleshoot.

In order to generate a PRT log in to Cisco Unified Communications Manager Administration, navigate to CM Administration > Device > Phone , enable the checkbox of the phone of interest and select Generate PRT for selected , as shown in the image.

In order to use this feature, y ou need to configure the Customer Support Upload URL field on the phone configuration page before you generate the PRT log as shown in the image.

This feature requires Cisco Unified Communications Manager 12.5(1)SU1 or later. More information on how to configure a customer support upload URL here .

### Headset Logs

Each time that a headset is connected or disconnected the headset logs are generated automatically. In order to store and show the headset information in the CUCM, there are some steps that happen as shown in the image.

Step 1. The phone/headset sends the inventory data to CUCM (POST/headset/inventory/<SN>).

Step 2. A Transport Layer Security (TLS) handshake takes place and certificates are exchanged. Call Manager server sends the Tomcat certificate and the phone sends the Manufacturer Installed Certificate (MIC) certificate or Locally Significant Certificate (LSC) if it is installed.

Step 3. If the certificate is validated, CUCM stores the inventory data in the database.

Step 4. Admin can generate an inventory summary report or a query-based custom report.

Note : The headset logs are contained in the phone console logs. In order to download them, you need to enable web access on the phone configuration page. In phones 78xx and 88xx series the console logs are contained in the PRT.

#### Example 1. Headset Logs for the Connected Status

When the headset is connected to the phone some lines are included in the phone console logs, the lines in the output indicate when the POST message was sent and the response provided by CUCM as shown in this example.

1. Headset manager sends the Http_request POST|INVENTORY message for the connected status.

```
0987 NOT Jul 11 22:06:35.950851 (711:938) JAVA-HSMGR JNI| http_request: call from management library, context: <https://10.1.61.140:9444/headset/inventory|POST|INVENTORY|{
                              "time":  1562882795,
                              "key":    "headsetInventory",
                              "value":               {
                                            "host":  {
                                                           "client":               "Cisco IP Phone",
                                                           "serialNumber":               "FCH2133E8B9",
                                                           "deviceName":  "CP-8861-SEP2C3124C9F8E1",
                                                           "model":             "CP-8861",
                                                           "firmwareVersion":         "sip88xx.12-5-1SR3-74",
                                                           "hostOSVersion":             "N/A",
                                                           "userId":              ""
                                            },
                                            "dock": {
                                                           "serialNumber":               "WFG2303M0B5",
                                                           "model":             "MB"
                                            },
                                            "headset":          {
                                                           "serialNumber":               "WFG2303D0D0",
                                                           "firmwareVersion":         "1-5-1-15",
                                                           "vendor":            "Cisco",
                                                           "model":             "561",
                                                           "connectionType":          "DECT Wireless",
                                                           "connectionStatus":        "connected"
                                            }
                              }
               }|0|>
```

2. The headset remote config manager submits the request.

```
0989 NOT Jul 11 22:06:35.951173 (711:938) JAVA-Thread-47|cip.headset.HeadsetRemoteConfigManager:submitRequest - context: https://10.1.61.140:9444/headset/inventory|POST|INVENTORY|{
                              "time":  1562882795,
                              "key":    "headsetInventory",
                              "value":               {
                                            "host":  {
                                                           "client":               "Cisco IP Phone",
                                                           "serialNumber":               "FCH2133E8B9",
                                                           "deviceName":  "CP-8861-SEP2C3124C9F8E1",
                                                           "model":             "CP-8861",
                                                           "firmwareVersion":         "sip88xx.12-5-1SR3-74",
                                                           "hostOSVersion":             "N/A",
                                                           "userId":              ""
                                            },
                                            "dock": {
                                                           "serialNumber":               "WFG2303M0B5",
                                                           "model":             "MB"
                                            },
                                            "headset":          {
                                                           "serialNumber":               "WFG2303D0D0",
                                                           "firmwareVersion":         "1-5-1-15",
                                                           "vendor":            "Cisco",
                                                           "model":             "561",
                                                           "connectionType":          "DECT Wireless",
                                                           "connectionStatus":        "connected"
                                            }
                              }
               }|0|<>
0990 DEB Jul 11 22:06:35.951334 (711:885) JAVA-HeadsetConfigImpl: parse_remote_default_config: Current headset plugged in: 561
0991 NOT Jul 11 22:06:35.951381 (711:938) JAVA-Thread-47|cip.headset.HeadsetRemoteConfigManager:submitRequest - POST:https://UmVxdWlyZWQ=:UmVxdWlyZWQ=@10.1.61.140:9444/headset/inventory
```

3. The Secure Sockets Layer (SSL) connection is attempted.

```
1092 INF Jul 11 22:06:36.106210 (711:853) JAVA-Sec SSL Connection - HTTPS_TLS.
1093 INF Jul 11 22:06:36.106256 (711:853) JAVA-Sec SSL Connection - ciphers:[ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:AES256-SHA:AES128-SHA:DES-CBC3-SHA]
```

4. The certificate is requested.

```
1107 INF Jul 11 22:06:36.156830 (711:853) JAVA-SSL session setup - Requesting Cert
```

5. The phone sends the certificate.

```
1114 DEB Jul 11 22:06:36.207553 (711:853) JAVA-Certificate subject name = /serialNumber=PID:CP-8861 SN:FCH2133E8B9/O=Cisco Systems Inc./OU=CTG/CN=CP-8861-SEP2C3124C9F8E1
1115 DEB Jul 11 22:06:36.207590 (711:853) JAVA-SSL session setup - Certificate issuer name = /O=Cisco/CN=Cisco Manufacturing CA SHA2
```

6. The certificate validity is checked by CUCM.

```
1134 INF Jul 11 22:06:36.860688 (711:853) JAVA-SSL session setup Cert Verification - Certificate is valid.
```

7. If the SSL handshake is successful the connection is established.

```
1140 NOT Jul 11 22:06:37.151072 (711:853) JAVA-Sec SSL Connection - Handshake successful.
1145 DEB Jul 11 22:06:37.151354 (711:853) JAVA-Sec SSL Conn - Adding SSL session reference to cache, label (10.1.61.140:9444)
```

8. CallManager sends the response with code 200.

```
1189 NOT Jul 11 22:06:37.254701 (711:885) JAVA-HSMGR JNI| to_request_context: context: <https://10.1.61.140:9444/headset/inventory|POST|INVENTORY|{
                              "time":  1562882795,
                              "key":    "headsetInventory",
                              "value":               {
                                            "host":  {
                                                           "client":               "Cisco IP Phone",
                                                           "serialNumber":               "FCH2133E8B9",
                                                           "deviceName":  "CP-8861-SEP2C3124C9F8E1",
                                                           "model":             "CP-8861",
                                                           "firmwareVersion":         "sip88xx.12-5-1SR3-74",
                                                           "hostOSVersion":             "N/A",
                                                           "userId":              ""
                                            },
                                            "dock": {
                                                           "serialNumber":               "WFG2303M0B5",
                                                           "model":             "MB"
                                            },
                                            "headset":          {
                                                           "serialNumber":               "WFG2303D0D0",
                                                           "firmwareVersion":         "1-5-1-15",
                                                           "vendor":            "Cisco",
                                                           "model":             "561",
                                                           "connectionType":          "DECT Wireless",
                                                           "connectionStatus":        "connected"
                                            }
                              }
               }|200|<>>
1190 NOT Jul 11 22:06:37.254762 (711:885) JAVA-HSMGR JNI| on_http_response: onHttpResponse (context) <200> callback from java: <<>>
```

Similar messages are expected to be shown in the console logs when the headset is disconnected from the phone and the information is updated in the headset inventory page.

#### Example 2. Headset Logs for a Headset not shown in the Inventory

If the headset is not reported in the headset inventory, unplug and plug the headset from the device, collect the phone console logs (or PRT) and get a Call Manager/phone packet capture. As shown in this example, the headset logs and packet capture indicate a certificate error.

1. The headset manager sends the http_request POST inventory message.

```
7823 NOT Jul 11 20:37:18.220777 (29894:30111) JAVA-HSMGR JNI| http_request: call from management library, context: <https://10.1.61.140:9444/headset/inventory|POST|INVENTORY|{
                              "time":  1562877438,
                              "key":    "headsetInventory",
                              "value":               {
                                            "host":  {
                                                           "client":               "Cisco IP Phone",
                                                           "serialNumber":               "FCH2133E8B9",
                                                           "deviceName":  "CP-8861-SEP2C3124C9F8E1",
                                                           "model":             "CP-8861",
                                                           "firmwareVersion":         "sip88xx.12-5-1SR3-74",
                                                           "hostOSVersion":             "N/A",
                                                           "userId":              ""
                                            },
                                            "dock": {
                                                           "serialNumber":               "WFG2303M07W",
                                                           "model":             "MB"
                                            },
                                            "headset":          {
                                                           "serialNumber":               "WFG2238E0A0",
                                                           "firmwareVersion":         "1-5-1-15",
                                                           "vendor":            "Cisco",
                                                           "model":             "562",
                                                           "connectionType":          "DECT Wireless",
                                                           "connectionStatus":        "connected"
                                            }
                              }
               }|0|>
```

2. The headset remote config manager submits a request.

```
7824 NOT Jul 11 20:37:18.221377 (29894:30111) JAVA-Thread-58|cip.headset.HeadsetRemoteConfigManager:submitRequest - context: https://10.1.61.140:9444/headset/inventory|POST|INVENTORY|{
                              "time":  1562877438,
                              "key":    "headsetInventory",
                              "value":               {
                                            "host":  {
                                                           "client":               "Cisco IP Phone",
                                                           "serialNumber":               "FCH2133E8B9",
                                                           "deviceName":  "CP-8861-SEP2C3124C9F8E1",
                                                           "model":             "CP-8861",
                                                           "firmwareVersion":         "sip88xx.12-5-1SR3-74",
                                                           "hostOSVersion":             "N/A",
                                                           "userId":              ""
                                            },
                                            "dock": {
                                                           "serialNumber":               "WFG2303M07W",
                                                           "model":             "MB"
                                            },
                                            "headset":          {
                                                           "serialNumber":               "WFG2238E0A0",
                                                           "firmwareVersion":         "1-5-1-15",
                                                           "vendor":            "Cisco",
                                                           "model":             "562",
                                                           "connectionType":          "DECT Wireless",
                                                           "connectionStatus":        "connected"
                                            }
                              }
               }|0|<>
7825 INF Jul 11 20:37:18.221554 (29894:30030) JAVA-HTTP JNI| Curl_readwrite: go ahead with socket check
```

3. The SSL connection is attempted.

```
7950 INF Jul 11 20:37:18.382089 (29894:30031) JAVA-Sec SSL Connection - HTTPS_TLS.
```

4. The certificate of the phone is requested.

```
7965 INF Jul 11 20:37:18.432971 (29894:30031) JAVA-SSL session setup - Requesting Cert
```

5. The phone sends the certificate.

```
7972 DEB Jul 11 20:37:18.483944 (29894:30031) JAVA-Certificate subject name = /serialNumber=PID:CP-8861 SN:FCH2133E8B9/C=MX/O=Cisco/OU=Voice/CN=CP-8861-SEP2C3124C9F8E1
7973 DEB Jul 11 20:37:18.483994 (29894:30031) JAVA-SSL session setup - Certificate issuer name = /C=MX/O=Cisco/OU=Voice/CN=CAPF-0992727f/ST=Mexico City/L=Mexico City
```

In this example, the certificate is not found in the trust list of CUCM.

```
7988 ERR Jul 11 20:37:18.587580 (366:32531) SECUREAPP-No match found in trust list against the item
```

The certificate of the phone is still valid (not expired).

```
7990 INF Jul 11 20:37:19.088525 (29894:30031) JAVA-SSL session setup Cert Verification - Certificate is valid.
```

In this example, the handshake failed with reason 19.

```
7996 ERR Jul 11 20:37:19.380225 (29894:30031) JAVA-Sec SSL Connection - Handshake failed.
8028 NOT Jul 11 20:37:19.386375 (29894:30061) JAVA-HSMGR JNI| to_request_context: context: <https://10.1.61.140:9444/headset/inventory|POST|INVENTORY|{
                              "time":  1562877438,
                              "key":    "headsetInventory",
                              "value":               {
                                            "host":  {
                                                           "client":               "Cisco IP Phone",
                                                           "serialNumber":               "FCH2133E8B9",
                                                           "deviceName":  "CP-8861-SEP2C3124C9F8E1",
                                                           "model":             "CP-8861",
                                                           "firmwareVersion":         "sip88xx.12-5-1SR3-74",
                                                           "hostOSVersion":             "N/A",
                                                           "userId":              ""
                                            },
                                            "dock": {
                                                           "serialNumber":               "WFG2303M07W",
                                                           "model":             "MB"
                                            },
                                            "headset":          {
                                                           "serialNumber":               "WFG2238E0A0",
                                                           "firmwareVersion":         "1-5-1-15",
                                                           "vendor":            "Cisco",
                                                           "model":             "562",
                                                           "connectionType":          "DECT Wireless",
                                                           "connectionStatus":        "connected"
                                             }
                              }
               }|19|<>>
8029 NOT Jul 11 20:37:19.386452 (29894:30061) JAVA-HSMGR JNI| on_http_response: onHttpResponse (context) <19> callback from java: <<>>
```

Basically, the phone has an LSC installed which was signed by a Certificate Authority Proxy Function (CAPF) of a different cluster, so CUCM does not trust and reject the SSL connection. A factory reset on the phone eliminates the LSC and solves this problem.

The packet capture for this example indicates the SSL handshake failure with " Alert (Level: Fatal, Description Unknown CA) " as shown in the image.

### Common Issues

You can experience issues related to these scenarios:

- Your headset cannot communicate with your selected call device

- The sound in your headset speakers is poor

- You cannot be understood when you speak into the headset microphone

If you experience problems with the headsets you can follow these actions:

Step 1. Ensure that your headset is powered on. In order to restart your wireless headset, press and hold the Call button (on the wireless headsets) for four seconds to power your headset off and on.

Step 2. Check if your headset is detected.

- On a Cisco IP Phone connected to Cisco Unified Communications Manager, navigate to Applications and select Accessories

- On a Cisco IP Phone with Multiplatform phone firmware, navigate to Applications > Status and select Accessories

- On a Cisco Webex, DX70 or DX80, tap on the screen and select from the available audio devices in the upper right corner

- On Cisco Jabber, navigate to Menu > Options > Audio

- On the Cisco Webex Meetings , navigate to Audio > Computer Audio Settings

Step 3. Test with a different headset.

Step 4. Confirm if the headset firmware is up-to-date. If the headset is not updated, follow the steps listed in the COP file installation section.

If the problems detected are more related to the headset audio, verify if you have one of these conditions:

- For not alerts on incoming calls: This is a known limitation Cisco Headset 500 Series with Firmware Release 1.0(2) or older. Update your headset firmware to the latest firmware release

- For broken or inconsistent sound in your Cisco Headset 560 Series: Ensure that your base does not receive interference from other headset bases. For best call quality, ensure that your headset base is at least one foot (0.3 meters) away from another Cisco headset base. Ensure that your wireless headset is paired with its base. Place the headset into the base to pair the headset and base. Ensure that the headset is properly seated

- For echo issues on Cisco 560 headset when is connected thru the Y-cable with a 7900 series phone, disable the headset sidetone level on the phone web page. Navigate to CM Administration > Devices > Phones , select the 7900 phones and configure the Headset Sidetone Level as Off . Select Save and Apply config as shown in the image:

For the 8851 there is no sidetone configuration on the phone page, but you can configure it manually on the physical phone. Navigate to Settings > Accessories > Cisco Headset > Speaker > Sidetone and configure it as off

In order to modify the sidetone configuration for multiple phones, you can modify or create a new headset template. Navigate to CM Admin > Device > Headset > Headset template and select Create new . Configure the settings for the 560 with sidetone as off.

More common issues and tips to troubleshoot here .

### COP File Installation Process for Headsets Upgrade

It is highly recommended to have the latest firmware version installed on the phones and the headsets. Perform this procedure to install the COP file for headsets:

Step 1. Select the URL: http://www.cisco.com/cisco/web/support/index.html

Step 2. Log in to the support and downloads the software page.

Step 3. Choose the collaboration endpoints and phone category.

Step 4. Choose the Headset 500 Series.

Step 5. Choose the Headset 560 (or the one that applies).

Step 6. Select the Downloads tab.

Step 7. Choose the latest release.

Step 8. Download the files that are listed.

Step 9. Use your web browser, log in to the Cisco Unified OS Administration web page.

Step 10. Under the Software Upgrades menu, select Install/Upgrade .

Step 11. Enter the appropriate values in the software location section for the downloaded.

Step 12. In the Options/Upgrades drop-down box, select the file you downloaded and select Next .

Step 13. Select Next .

Step 14. Check the installation log and verify the file installed successfully.

Step 15. Log in to Cisco Unified Serviceability web page.

Step 16. Under the Tools menu, select Control Center - Feature Services .

Step 17. Select the Cisco Tftp service, and select Restart .

At the moment of the elaboration of this document, the latest version is cmterm-1-5-1-15.cop https://software.cisco.com/download/home/286323239/type/286323289/release/1.5(1)

This headset firmware version is supported on Cisco Unified Communications Manager 10.5(2) and later. The recommended firmware version for the Cisco IP Phone 7800/8800 series is 12.5(1) or above.

The headset firmware upgrade is decoupled from phone firmware and the upgrade happens when the headset is plugged into the phone, as shown in the image.

Settings of speaker tuning and sidetone, and microphone gain are stored in the headset; you do not need to adjust again when you plug it into a new phone. These settings are not erased by a phone factory reset.

In order to reset the configuration in the headset uses the phone menu. With this method, you can revert all the settings to default, navigate to Settings > Accessories > Cisco Wireless Headset > Reset settings > Reset .

Note : If you do not have access to the Cisco Unified Communications Manager, you can use the online tool to upgrade your Cisco Headset ( 560 Series only) : Headset Upgrade Tool

### Reinstall the Windows driver

Follow these steps to clean the configuration in Windows registry and reinstall the USB audio driver:

Step 1. Right-click the Windows start button and open the Windows Device Manager , as shown in this image.

Step 2. Find the Cisco headset in the device manager under Audio input and outputs and select the microphone or speaker, as shown in this image.

Step 3. Under Device Manager , navigate to View > Devices by connection , as shown in this image.

Step 4. As shown in this image, right-click USB Composite Device and select Uninstall device .

Step 5. Unplug and plug the Cisco headset USB cable, Windows will re-install the driver.

## CP-HS-5xx Wired / Wireless - Warranty

The warranty for the Cisco Headsets depends on the headset model.

- Wired headset: 2-year warranty

- Wireless headset: 1-year warranty

Note : If you open a TAC case, provide a valid contract or serial number.

## Defects / Known Limitations

### Open Defects

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of open defects or to view specific bugs, access the Bug Search Toolkit.

- CSCvn41271 : Volume changed when playing music on MacBook, both usb1 and usb2.

- CSCvp96968 : DX70, DX80 CE9.7 User Guide has an incorrect image for Join a Scheduled Meeting.

- CSCvp32795 : Volume is louder in HFP than A2DP at the same level.

- CSCvq03392 : Jabber setting rendering is incorrect when the active source is not Jabber.

- CSCvn47014 : The Bluetooth connect tone does not play or is too soft with the PC or Mobile source selected.

- CSCvn66483 : Bluetooth doesn't reconnect when the call source comes back into range.

- CSCvn73816 : Power off tone is too low when music is playing on a Windows 10 source.

### Resolved Caveats

The list contains the defects that are resolved for the Cisco Headset 500 Series that use Firmware Release 1.5(1).

- CSCvo70826 : Headset Does Not Alert to Incoming Calls on IP Phone.

- CSCvp97802 : Rarely the voice volume gets louder but decreases immediately while pressing the volume+ button quickly.

- CSCvo01194 : There is noise in the headset when the multi-base switches from an IP-Phone source to the Bluetooth source.

- CSCvn79632 : There is noise in the headset during an active call through Bluetooth.

- CSCvn77884 : Headset and base disconnect and reconnect unprompted.

CSCvn76631 : Sometimes no tone when end call by long pressing call button.

Visit the Series Accessories Guide for Cisco Unified Communications Manager to get more details on the headset compatibility and configuration.

Visit Cisco IP Phone 8800 supported accessories for more information on the headset compatibility with the 8800 series phone.

## Related information:

Visit the Configure Configure Cisco Headset 5xx Series for more information on the configuration in CUCM.

Visit the Series Accessories Guide for Cisco Unified Communications Manager to get more details on the headset compatibility and configuration.

Visit Cisco IP Phone 8800 supported accessories for more information on the headset compatibility with the 8800 series phone.

### Revision History

1.0

31-Oct-2019

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 31-Oct-2019 | Initial Release |