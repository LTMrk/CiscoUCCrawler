---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-attendant-console-advanced-217614-solve-cryptokey-erro-edec5a3dfa
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-attendant-console-advanced/217614-solve-cryptokey-error-at-cuac-a-subscrib.html
retrieved_at: 2026-09-07T15:49:02.983367+00:00
---

Troubleshoot "Crypto Key" Error at CUAC-A Subscriber Installation

# Troubleshoot "Crypto Key" Error at CUAC-A Subscriber Installation

### Download Options

Updated: January 3, 2022

Document ID: 217614

Contents

## Contents

## Introduction

This document describes how to troubleshoot the "Crypto Key" error at Cisco Unified Attendant Console Advanced (CUAC-A) Subscriber Installation.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUAC-A

- Windows Server

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

At the time of the CUAC-A Subscriber installation, the system checks if the Crypto Key is installed or not. The installer prompts for the Crypto Key that requires to be exported from the CUAC-A Publisher. If it already exists, it shows this one line within the CUACAInstall.log :

```
ImportCryptoKeyFile:IsCryptoRegAndKeyFileExist()
```

## Problem

When the CUAC-A Subscriber server fails to import the Crypto Key File in the installation process, this error is displayed at the install prompt: "The Cryptography information does not match Publisher Cryptography information. Please check details and try again", as shown in this image:

## Solution

- Export Crypto File from the publisher as described on the CUAC-A Admin Guide on page 5-7 (Page 50 from the document).

Note : You can use the Cisco Unified Attendant Administration to back up the Publisher’s cryptographic keys and registries. This UI only appears on Publisher, but the backup-up key archive must be copied to Subscriber.

To export the cryptographic key file to your computer:

Step 1. Log in to the Cisco Unified Attendant Administration .

Step 2. Navigate to Help > Export Crypto Key File .

Step 3. Type your passphrase and choose Export .

Step 4. Choose a location on your computer to save the file in a .zip format.

- To manually implement the crypto data from the publisher on the subscriber with the exported zip file:

Step 1. Copy the .zip file from the CUAC-A Publisher to the CUAC-A Subscriber.

Step 2. Unzip the Crypto Key file that was moved over from the CUAC-A Publisher.

Step 3. Find the keyreg file.

Step 4. Double-click the keyreg file to add the entries to the local registry.

Step 5. Copy the key file to the KeyFilePath designated in the registry HKLM/software/wow6432node/arc solutions/call connect/crypto/security/registry entry.

Step 6. Re-run the CUAC-A installer on the Subscriber server.

If the issue persists, verify:

Step 1. Add the Antivirus Exceptions as per the CUAC-A Admin Guide on page 3-6 (Page 31 from the document) .

Step 2. Copy the aesKey.dat from the CUAC-A Publisher server into the CUAC-A Subscriber server. The file is located in C://Windows/SysWOW64/config/systemprofile/AppData/Local/Arc/Crypto/Keys .

Step 3. Reboot the CUAC-A Subscriber server and ensure the file is still there.

Step 4. Proceed with the CUAC-A Subscriber installation.

At this point, if the issue persists, it means that the file ( aesKey.dat ) continues to get removed/corrupted even though the Antivirus Exceptions are already set into place. These exceptions need to be set in the antivirus, anti-malware, and/or any type of security software that would interfere with the CUAC-A install directory files.

The final steps to solve the problem are:

Step 5. Confirm whether there is any other type of security software that can modify the directory files.

Step 6. Confirm that all the changes applied were made with an Administrator account.

Step 7. Verify that the CUAC-A Publisher is installed as per the guide.

Note : Keep in mind that, if the issue persists, this behavior is caused by the Windows environment and the Microsoft team requires to be involved for further validation and the troubleshoot of the problem.

### Revision History

1.0

03-Jan-2022

Initial Release

### Contributed by Cisco Engineers

Yani Saavedra Chimal

Cisco TAC Engineer

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 03-Jan-2022 | Initial Release |