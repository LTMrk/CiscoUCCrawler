---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-business-edition-7000-version-15-226133-determine-nfvis-for-uc-56387b75b9
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/business-edition-7000-version-15/226133-determine-nfvis-for-uc-install-volume.html
retrieved_at: 2026-08-21T20:46:29.342491+00:00
---

Determine NFVIS-for-UC Install Volume

# Determine NFVIS-for-UC Install Volume

### Download Options

Updated: July 8, 2026

Document ID: 226133

Contents

## Contents

## Introduction

This document describes the steps required to determine which volume NFVIS-for-UC is currently installed on.

## Problem

Need to determine which volume NFVIS-for-UC is currently installed on.

## Solution

Step 1. Run a RedFish API query against the CIMC of the host to identify how many virtual drives exists via https://< CIMC IP Address> /redfish/v1/Systems/< CIMC Serial Number> /Storage/MRAID/Volumes

Example Output

```
{ "@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes", "@odata.type": "#VolumeCollection.VolumeCollection", "@odata.context": "/redfish/v1/$metadata#VolumeCollection.VolumeCollection", "Description": "Collection of Volumes for this system", "Name": "Volume Collection", "Members@odata.count": 4, "Members": [ { "@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/0" }, { "@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/1" }, { "@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/2" }, { "@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/3" } ] }
```

Step 2. Query the API for each volume, where Number is the number of the volume seen in Step 1 output. https://< CIMC IP Address> /redfish/v1/Systems/< CIMC Serial Number> /Storage/MRAID/Volumes/ Number

Example output from VD-0

```
... Obmitted Output ... "Id": "0", "Name": "NA", "Encrypted": false, "CapacityBytes": 1494996746240, "BlockSizeBytes": 512, "OptimumIOSizeBytes": 131072, "Identifiers": [ { "DurableNameFormat": "UUID", "DurableName": "60027e370b077b003179502a9dc8b57a" } ], "Status": { "Health": "OK", "State": "Enabled" }, "Actions": { "#Volume.Initialize": { "target": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/0/Actions/Volume.Initialize", "InitializeType@Redfish.AllowableValues": [ "Fast", "Slow" ] }, "#Volume.CheckConsistency": { "target": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/0/Actions/Volume.CheckConsistency" }, "Oem": { "#Cisco.StartReconstruction": { "target": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/0/Actions/Oem/Cisco.StartReconstruction", "@odata.type": "#CiscoUCSExtensions.v1_0_0.StartReconstruction", "ReconstructionOp@Redfish.AllowableValues": [ "add", "remove", "none" ] } } }, "RAIDType": "RAID5", "Oem": { "Cisco": { "VolumeAccessPolicy": "ReadWrite", "RequestedWriteCachePolicy": "WriteBack", "ConfiguredWriteCachePolicy": "WriteBack", "VolumeDriveCachePolicy": "NoChange", "VolumeReadAheadPolicy": "ReadAhead", "VolumeIoPolicy": "DirectIo", "VolumeState": "Optimal", "AvailableSizeMiBytes": 0, "Bootable": true, "FullDiskEncryptionCapable": false } } }
```

Step 3. From the output capture, the DurableName value for each which is the UUID.

```
"Identifiers": [ { "DurableNameFormat": "UUID", "DurableName": "60027e370b077b003179502a9dc8b57a" <<- This is the UUID you copy }
```

Step 4. SSH or console connection to the NFVIS-for-UC and execute support show list-units | include Volume-UUID.

Step 5. The Volume that NFVIS-for-UC is installed on contains the device along with device partitions.

Example output of Volume that has NFVIS-for-UC OS installed.

```
BE7KH2-NFVIS# support show list-units | include 60027e370b077b003179502a9dc8b57a dev-disk-by\x2did-scsi\x2d360027e370b077b003179502a9dc8b57a.device loaded active plugged UCSC-RAID12GP-4G dev-disk-by\x2did-scsi\x2d360027e370b077b003179502a9dc8b57a\x2dpart1.device loaded active plugged UCSC-RAID12GP-4G 1 dev-disk-by\x2did-scsi\x2d360027e370b077b003179502a9dc8b57a\x2dpart2.device loaded active plugged UCSC-RAID12GP-4G 2 dev-disk-by\x2did-scsi\x2d360027e370b077b003179502a9dc8b57a\x2dpart3.device loaded active plugged UCSC-RAID12GP-4G 3 dev-disk-by\x2did-wwn\x2d0x60027e370b077b003179502a9dc8b57a.device loaded active plugged UCSC-RAID12GP-4G dev-disk-by\x2did-wwn\x2d0x60027e370b077b003179502a9dc8b57a\x2dpart1.device loaded active plugged UCSC-RAID12GP-4G 1 dev-disk-by\x2did-wwn\x2d0x60027e370b077b003179502a9dc8b57a\x2dpart2.device loaded active plugged UCSC-RAID12GP-4G 2 dev-disk-by\x2did-wwn\x2d0x60027e370b077b003179502a9dc8b57a\x2dpart3.device loaded active plugged UCSC-RAID12GP-4G 3
```

Example of output of Volume that is not NFVIS-for-UC OS Install.

```
BE7KH2-NFVIS# support show list-units | include 60027e370b077b0031790987dc596ab8 dev-disk-by\x2did-scsi\x2d360027e370b077b0031790987dc596ab8.device loaded active plugged UCSC-RAID12GP-4G dev-disk-by\x2did-wwn\x2d0x60027e370b077b0031790987dc596ab8.device loaded active plugged UCSC-RAID12GP-4G
```

{

"@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes",

"@odata.type": "#VolumeCollection.VolumeCollection",

"@odata.context": "/redfish/v1/$metadata#VolumeCollection.VolumeCollection",

"Description": "Collection of Volumes for this system",

"Name": "Volume Collection",

"Members@odata.count": 4,

"Members": [

{

"@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/0"

},

{

"@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/1"

},

{

"@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/2"

},

{

"@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/3"

}

]

}

{

"@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes",

"@odata.type": "#VolumeCollection.VolumeCollection",

"@odata.context": "/redfish/v1/$metadata#VolumeCollection.VolumeCollection",

"Description": "Collection of Volumes for this system",

"Name": "Volume Collection",

"Members@odata.count": 4,

"Members": [

{

"@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/0"

},

{

"@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/1"

},

{

"@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/2"

},

{

"@odata.id": "/redfish/v1/Systems/SERIALNUMBER/Storage/MRAID/Volumes/3"

}

]

}

### Revision History

1.0

08-Jul-2026

Initial Release

### Contributed by Cisco Engineers

Ben Wollak

Technical Consulting Engineering Technical Leader

### This Document Applies to These Products

- Business Edition 7000 Version 15

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 08-Jul-2026 | Initial Release |