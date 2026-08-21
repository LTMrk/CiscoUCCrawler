---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b02licfu-html-b4914350c1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b02licfu.html
retrieved_at: 2026-08-21T16:10:55.392608+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: License File Upload

## Chapter: License File Upload

## License File Upload

The license file contains the information that is needed to enforce licenses for the Cisco Unified Presence Server application. This chapter contains the following topics:

• Obtaining a License File

• License File Contents

• Uploading a License file

• Related Topics

Note Use this window to upload a license for the Cisco Presence Engine and the SIP proxy server. You must also upload the appropriate end-user license through the Cisco Unified CallManager Administration window. For more information, see the Cisco Unified CallManager Administration Guide .

## Obtaining a License File

Use the following steps to obtain a license file for a new installation of Cisco Unified Presence Server.

Step 1 When you place an order for Cisco devices, Cisco provides a Product Authorization Key (PAK).

Step 2 Register the PAK that you received with Cisco Unified Presence Server by using the License Registration web tool that is provided on CCO.

Step 3 You must enter the MAC address of the Cisco Unified Presence Server for which you are requesting the licenses, and a valid e-mail address. You must enter the number of nodes and phone units for which you want licenses.

Step 4 CCO generates a license file with the number of unit licenses that you requested and sends it to you via e-mail by using the e-mail address that you provided in step Step 3

Step 5 You must upload the license file to the server with the matching MAC address that you provided in Step 3 See the "Uploading a License file" section . This server then takes on the functionality of the license manager.

Note For updating the licenses when you buy new phones, go to the License Registration web tool that is provided on CCO and follow the Steps 3 through 5 .

Note The license file gets uploaded into the database only if the version specified in the license file is greater than or equal to the Cisco Unified Presence Server version that is running in the cluster. If the version check fails, an alarm gets generated, and you should get a new license file with the correct version. The system bases the version check only on major releases.

Note You can use the licenses that are specified in the license file only within the cluster on which the license file is uploaded.

Additional Information

See the "Related Topics" section .

## License File Contents

The license file contains the following information:

• Number of Cisco Unified Presence Server nodes that are licensed: This indicates number of Cisco Unified Presence Server servers in a cluster that are licensed to the customer.

• Versions of the Cisco Unified Presence Server that are supported.

• Number of phone units that are licensed: Instead of creating a separate license for each phone type, a concept of unit license is used. Each phone type corresponds to a fixed number of license units.

• MAC address of the server, where the license file can be installed.

To upload a license file to the license server, see the "Uploading a License file" section .

Sample License Files

The following examples describe license files for permanent IP phone licenses and permanent Cisco Unified Presence Server node licenses:

Example 4-1 Permanent IP Phone Licenses

```
INCREMENT PHONE_UNIT cisco 5.0 permanent uncounted \
```

```
VENDOR_STRING=<Count>1000</Count><OrigMacId>000BCD4EE59D</OrigMacId><LicFileVersion>1.0</L
icFileVersion> \
```

```
HOSTID=000bcd4ee59d OVERDRAFT=50 \
```

```
NOTICE="<LicFileID>20050826140539162</LicFileID><LicLineID>2</LicLineID> \
```

```
<PAK></PAK>" SIGN="112D 17E4 A755 5EDC F616 0F2B B820 AA9C \
```

```
0313 A36F B317 F359 1E08 5E15 E524 1915 66EA BC9F A82B CBC8 \
```

```
4CAF 2930 017F D594 3E44 EBA3 04CD 01BF 38BA BF1B"
```

The preceding license file includes following information:

• No expiration date for this license exists as indicated by the keyword permanent.

• This license file provides 1000 PHONE_UNIT licenses.

• OVERDRAFT=50 indicates (5% of 1000) allowed overdraft. Cisco determines the overdraft value.

• The Cisco-specific fieldLicFileID identifies this license file.

• You can add multiple increment lines for same feature (phone unit license or node license) in a license file to increase the license count. None of the INCREMENT lines should be identical and each of them should be signed independently.

Example 4-2 Permanent CCM_Node licenses

```
# Optional usage agreement, legal language, tracking information
```

```
# Some other comments
```

```
INCREMENT CCM_NODE cisco 5.0 permanent uncounted \
```

```
VENDOR_STRING=<Count>3</Count><OrigMacId>000BCD4EE59D</OrigMacId><LicFileVersion>1.0</LicF
ileVersion> \
```

```
HOSTID=000bcd4ee59d \
```

```
NOTICE="<LicFileID>20050826140539162</LicFileID><LicLineID>1</LicLineID> \
```

```
<PAK></PAK>" SIGN="19B3 4C6C 25AC 6D22 4D75 DE6A 656B 08C5 \
```

```
30E4 16DB 771B 1393 9DC1 DBC4 C5AA 15CC 6E6C B7B8 895A DCBA \
```

```
B40F C551 2625 1C97 F20D 9977 6CFF 3603 081E 6FF2"
```

The preceding license file includes the following information:

• No expiration date for this license exists as indicated by the keyword permanent.

• This license file provides three licenses for the version 5.0 of the feature CCM_NODES.

• The Cisco-specific fieldLicFileID identifies this license file.

• You can add multiple increment lines for same feature in a license file to increase the license count. None of the INCREMENT lines should be identical, and each of them should be signed independently.

Additional Information

See the "Related Topics" section .

## Uploading a License file

Use the following procedure to upload a license file to the Cisco Unified Presence Server node with the matching MAC address that is provided a license file is requested. For information about obtaining a license file, see the "Obtaining a License File" section . The Cisco Unified Presence Server node where the license file is loaded takes on the functionality of the license manager.

Note Upload the license file only on the first node of Cisco Unified Presence Server cluster.

Step 1 Choose System > License > Upload License File .

The License File Upload window displays.

Step 2 The Existing License Files drop-down list box displays the license files that are already uploaded to the server.

Note To view the file content of any existing files, click View File .

Step 3 To choose a new license file to upload, click Upload License File .

The Upload File pop-up window displays.

Step 4 Browse and choose a license file to upload to the server.

Step 5 Click Upload License File .

After the upload process is complete, the Upload Result file displays.

Step 6 Click Close .

Step 7 In the License File Upload window, the status of the uploaded file displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Obtaining a License File

• License File Contents

• Uploading a License file