---
doc_id: help-webex-com-en-us-article-5eomso-90fcce9c4a
source_url: https://help.webex.com/en-us/article/5eomso
retrieved_at: 2026-09-07T13:04:05.027467+00:00
---

## NFC onboarding data

### NFC data format: Payload

The payload in the NFC record contains the actual data that will be transmitted between NFC reader/writer and phone's NFC tag. You can specify the onboarding information in the NFC payload by configuring key-value pairs. The key and value are separated by a colon symbol, as shown below:

Key-value pair syntax: <Key>:<Value>

Example:

```
onboardingMethod:1
onboardingDetail:http://10.79.130.6/2302005811.xml
mac:A4114E0641C2  
Network_Name_1_:test_ssid
Wi-Fi_User_ID_1_:testuser
Wi-Fi_Password_1_:test12345
Security_Mode_1_:Auto
Frequency_Band_1_:5 GHz
Custom_CA_Rule:http://custom_ca.example.com/custom.ca
```

You can also configure the key-value pairs in the JSON format.

Example:

```
{
    "onboardingMethod": 1,
    "onboardingDetail": "http://10.79.130.6/2302005811.xml",
    "mac": "A4114E0641C2”,
    "onboardingConfig": {
        "Network_Name_1_": "test_ssid",
        "Wi-Fi_User_ID_1_": "testname",
        "Wi-Fi_Password_1_": "test12345",
        "Security_Mode_1_": "Auto",
        "Frequency_Band_1_": "5 GHz",
        "Custom_CA_Rule": "http://custom_ca.example.com/custom.ca"
    }
}
```

The object "onboardingConfig" exists only in JSON format. It contains the information about Wi-Fi profile and custom CA. Cisco Desk Phone 9811, 9841, and 9851 don't support Wi-Fi.

### Supported key-value pairs for NFC onboarding

- 1—Cloud URL

- 2—Cloud CDA Preferred

- 3—Cloud Activation code

- 4—Unified CM

- 5—Unified CM with Alternate TFTP

This pair is mandatory.

Example:

onboardingMethod:1

Example:

```
onboardingMethod:1
onboardingDetail:<url_address>
...
```

Example:

```
onboardingMethod:3
onboardingDetail:<activation_code>
...
```

Example:

```
onboardingMethod:5
onboardingDetail:<alt_tftp_address>
...
```

This key-value pair is mandatory when the transmitted NFC data is signed (signing or signing + encryption).

The phone will accept the NFC data only when the configured MAC address matches with the its own MAC address.

Example:

mac:<mac_address>

For more information about the parameters, see Parameters for Wi-Fi profile .

Network_Name_1_

Example:

Network_Name_1_:<ssid>

Example:

Wi-Fi_User_ID_1_:<user_id>

Example:

Wi-Fi_Password_1_:<password>

Example:

Security_Mode_1_:Auto

NFC onboarding doesn't support EAP-TLS.

Example:

Frequency_Band_1_:5 GHz

This key-value pair is applicable only for the onboarding methods: Cloud URL and Cloud CDA Preferred.

Example:

Custom_CA_Rule:http://<file_address>

## NFC onboarding methods

The following table shows the NFC onboarding methods, string syntax of the methods for configurations in the NFC reader/writer, and the applicable call control systems for the methods:

Cloud URL (1)—Register the phone to the call control system. It uses the cloud URL for fetching the profile rule.

Example 1:

```
onboardingMethod:1
onboardingDetail:<profile_url>
mac:<mac_address>
Network_Name_1_:<ssid>
Wi-Fi_User_ID_1_:<user_id>
Wi-Fi_Password_1_:<user_password>
Security_Mode_1_:Auto
Frequency_Band_1_:5 GHz
Custom_CA_Rule:<file_url>
```

Signing, Encryption + Signing

BroadWorks

Webex Calling

Webex Calling for BroadWorks

Cloud CDA Preferred (2)— CDA takes preference over the local DHCP provisioning.

It's recommended to scan the NFC tag before the phone boots up. Otherwise, the users might miss the configurable time range.

Example 2-1:

```
onboardingMethod:2
mac:<mac_address>
Network_Name_1_:<ssid>
Wi-Fi_User_ID_1_:<user_id>
Wi-Fi_Password_1_:<user_password>
Security_Mode_1_:Auto
Frequency_Band_1_:5 GHz
Custom_CA_Rule:<file_url>
```

Example 2-2:

```
onboardingMethod:2
mac:<mac_address>
```

Example 2-1:

Signing, Encryption + Signing

BroadWorks

Webex Calling

Webex Calling for BroadWorks

Unified CM (if both CDA and DHCP onboard fail)

Example 2-2:

Plain text, Signing, Encryption, Encryption + Signing

Cloud Activation Code (3)—Activation code (for Webex only). The phone can automatically register to the call control system by using this code.

If the users are prompted to enter an activation code on the phone, they can choose to scan the NFC tag to fill in the code.

Example 3-1:

```
onboardingMethod:3
onboardingDetail:<activation_code>
mac:<mac_address>
Network_Name_1_:<ssid>
Wi-Fi_User_ID_1_:<user_id>
Wi-Fi_Password_1_:<user_password>
Security_Mode_1_:Auto
Frequency_Band_1_:5 GHz
Custom_CA_Rule:<file_url>
```

Example 3-2:

```
onboardingMethod:3
onboardingDetail:<activation_code>
mac:<mac_address>
```

Example 3-1:

- Online NFC: Signing, Encryption + Signing

- Offline NFC: Encryption + Signing

Webex Calling

Webex Calling for BroadWorks

Example 3-2:

- Online NFC: Plain text, Signing, Encryption, Encryption + Signing

- Offline NFC: Encryption, Encryption + Signing

Unified CM (4)—Abort the ongoing registration (if existing), and directly register the phone to Unified CM.

Example 4-1:

```
onboardingMethod:4
mac:<mac_address>
Network_Name_1_:<ssid>
Wi-Fi_User_ID_1_:<user_id>
Wi-Fi_Password_1_:<user_password>
Security_Mode_1_:Auto
Frequency_Band_1_:5 GHz
```

Example 4-2:

```
onboardingMethod:4
mac:<mac_address>
```

Example 4-1:

Signing, Encryption + Signing

Example 4-2:

Plain text, Signing, Encryption,  Encryption + Signing

Unified CM with Alternate TFTP (5)—Abort the ongoing registration (if existing), and directly register the phone to Unified CM with the alternate TFTP server specified.

Can also be used when the users need to enter an alternate TFTP server on the phone.

Example 5:

```
onboardingMethod:5
onboardingDetail:<alt_tftp_address>
mac:<mac_address>
Network_Name_1_:<ssid>
Wi-Fi_User_ID_1_:<user_id>
Wi-Fi_Password_1_:<user_password>
Security_Mode_1_:Auto
Frequency_Band_1_:5 GHz
```

Signing

Encryption + Signing

For the onboarding methods "Cloud CDA Preferred (2)", "Cloud Activation Code (3)", and "Unified CM (4)", when Wi-Fi configurations or custom CA rule, or both are added, the only allowed security levels are: Signing and Signing + Encryption.

## Phases of NFC onboarding

The NFC onboarding can be performed in the following phases:

In this situation, you can use a mobile phone that running a custom app to scan the NFC tag to write onboarding information to the phone. After the phone boots up, it will start the onboarding process automatically based on the written information.

The NFC onboarding info can determine to which call control system (Unified CM or Cloud) the phone will be registered and the deployment preference mode (CDA preferred or local DHCP).

During the phone's onboarding process, the users might be prompted to choose a call service or enter an activation code, or both.

If the phone is still packed in the phone box, you can use an NFC device to scan the NFC marked area on the phone box to write the onboarding information to the phone. The phone will register by itself when it boots up.

You can scan the NFC tag at any time during the onboarding process. To ensure that the NFC onboarding info can be detected in time, it's recommended to scan the NFC tag just after the phone successfully connects to a network.

If the NFC onboarding method is Cloud URL (1) , Unified CM (4) , or Unified CM with Alternate TFTP (5) , the ongoing onboarding process will be aborted immediately when you scan the NFC tag. And a  new onboarding process will start, the phone will be registered to the call control system according to the selected method (UCM or Cloud).

During the phone's onboarding process, you might be prompted to enter some information (for example, TFTP server or activation code) to proceed the process. In this situation, you can choose to scan the NFC tag to automatically fill in the information on the phone.

| Key (case sensitive) | Value | Description |
|---|---|---|
| onboardingMethod | 1–5 | Specifies the onboarding method: 1—Cloud URL 2—Cloud CDA Preferred 3—Cloud Activation code 4—Unified CM 5—Unified CM with Alternate TFTP This pair is mandatory. Example: onboardingMethod:1 |
| onboardingDetail | HTTP address, activation code, or alternate TFTP address corresponding to the onboarding method | Specifies detailed information for the corresponding onboarding method. For onboardingMethod:1 (Cloud URL), the corresponding value is an HTTP address. Example: onboardingMethod:1
onboardingDetail:<url_address>
... For onboardingMethod:3 (Cloud Activation Code), the corresponding value is an activation code. Example: onboardingMethod:3
onboardingDetail:<activation_code>
... For onboardingMethod: 5 (Unified CM with Alternate TFTP), the corresponding value is an alternate TFTP address. Example: onboardingMethod:5
onboardingDetail:<alt_tftp_address>
... |
| mac | MAC address | Specifies the phone's MAC address. This key-value pair is mandatory when the transmitted NFC data is signed (signing or signing + encryption). The phone will accept the NFC data only when the configured MAC address matches with the its own MAC address. Example: mac:<mac_address> |
| Wi-Fi profile For more information about the parameters, see Parameters for Wi-Fi profile . |
| Network_Name_1_ | SSID | Defines the name for the SSID that will display on the phone. Example: Network_Name_1_:<ssid> |
| Wi-Fi_User_ID_1_ | User ID for the network profile | Specifies the user ID for the Wi-Fi network. Example: Wi-Fi_User_ID_1_:<user_id> |
| Wi-Fi_Password_1_ | Password for the user ID | Specifies the password for the user ID to access the Wi-Fi network. Example: Wi-Fi_Password_1_:<password> |
| Security_Mode_1_ | Auto\|EAP-FAST\|\|\|PSK\|\|None\|EAP-PEAP | Selects the authentication method used to secure access to the Wi-Fi network. Example: Security_Mode_1_:Auto NFC onboarding doesn't support EAP-TLS. |
| Frequency_Band_1_ | Auto\|2.4 GHz\|5 GHz | Selects the frequency band on the phone to access the Wi-Fi network. Example: Frequency_Band_1_:5 GHz |
| Custom Certificate Authority (CA) |
| Custom_CA_Rule | Custom CA rule file | Specifies the location of the custom ca rule file. This key-value pair is applicable only for the onboarding methods: Cloud URL and Cloud CDA Preferred. Example: Custom_CA_Rule:http://<file_address> |

| Onboarding method | Allowed security level | Call control system |
|---|---|---|
| Cloud URL (1)—Register the phone to the call control system. It uses the cloud URL for fetching the profile rule. Example 1: onboardingMethod:1
onboardingDetail:<profile_url>
mac:<mac_address>
Network_Name_1_:<ssid>
Wi-Fi_User_ID_1_:<user_id>
Wi-Fi_Password_1_:<user_password>
Security_Mode_1_:Auto
Frequency_Band_1_:5 GHz
Custom_CA_Rule:<file_url> | Signing, Encryption + Signing | BroadWorks Webex Calling Webex Calling for BroadWorks |
| Cloud CDA Preferred (2)— CDA takes preference over the local DHCP provisioning. It's recommended to scan the NFC tag before the phone boots up. Otherwise, the users might miss the configurable time range. Example 2-1: onboardingMethod:2
mac:<mac_address>
Network_Name_1_:<ssid>
Wi-Fi_User_ID_1_:<user_id>
Wi-Fi_Password_1_:<user_password>
Security_Mode_1_:Auto
Frequency_Band_1_:5 GHz
Custom_CA_Rule:<file_url> Example 2-2: onboardingMethod:2
mac:<mac_address> | Example 2-1: Signing, Encryption + Signing | BroadWorks Webex Calling Webex Calling for BroadWorks Unified CM (if both CDA and DHCP onboard fail) |
| Example 2-2: Plain text, Signing, Encryption, Encryption + Signing |
| Cloud Activation Code (3)—Activation code (for Webex only). The phone can automatically register to the call control system by using this code. If the users are prompted to enter an activation code on the phone, they can choose to scan the NFC tag to fill in the code. Example 3-1: onboardingMethod:3
onboardingDetail:<activation_code>
mac:<mac_address>
Network_Name_1_:<ssid>
Wi-Fi_User_ID_1_:<user_id>
Wi-Fi_Password_1_:<user_password>
Security_Mode_1_:Auto
Frequency_Band_1_:5 GHz
Custom_CA_Rule:<file_url> Example 3-2: onboardingMethod:3
onboardingDetail:<activation_code>
mac:<mac_address> | Example 3-1: Online NFC: Signing, Encryption + Signing Offline NFC: Encryption + Signing | Webex Calling Webex Calling for BroadWorks |
| Example 3-2: Online NFC: Plain text, Signing, Encryption, Encryption + Signing Offline NFC: Encryption, Encryption + Signing |
| Unified CM (4)—Abort the ongoing registration (if existing), and directly register the phone to Unified CM. Example 4-1: onboardingMethod:4
mac:<mac_address>
Network_Name_1_:<ssid>
Wi-Fi_User_ID_1_:<user_id>
Wi-Fi_Password_1_:<user_password>
Security_Mode_1_:Auto
Frequency_Band_1_:5 GHz Example 4-2: onboardingMethod:4
mac:<mac_address> | Example 4-1: Signing, Encryption + Signing | Unified CM |
| Example 4-2: Plain text, Signing, Encryption,  Encryption + Signing |
| Unified CM with Alternate TFTP (5)—Abort the ongoing registration (if existing), and directly register the phone to Unified CM with the alternate TFTP server specified. Can also be used when the users need to enter an alternate TFTP server on the phone. Example 5: onboardingMethod:5
onboardingDetail:<alt_tftp_address>
mac:<mac_address>
Network_Name_1_:<ssid>
Wi-Fi_User_ID_1_:<user_id>
Wi-Fi_Password_1_:<user_password>
Security_Mode_1_:Auto
Frequency_Band_1_:5 GHz | Signing Encryption + Signing | Unified CM |