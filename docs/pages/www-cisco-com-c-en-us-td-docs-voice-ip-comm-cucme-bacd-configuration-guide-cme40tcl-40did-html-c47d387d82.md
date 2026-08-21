---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-bacd-configuration-guide-cme40tcl-40did-html-c47d387d82
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/bacd/configuration/guide/cme40tcl/40did.html
retrieved_at: 2026-08-21T23:02:35.180235+00:00
---

Cisco Unified CME B-ACD and Tcl Call-Handling Applications

# Cisco Unified CME B-ACD and Tcl Call-Handling Applications

Updated: November 2, 2007

Chapter: Cisco Unified CME Direct Inward Dial Digit Translation Service

## Chapter: Cisco Unified CME Direct Inward Dial Digit Translation Service

## D irect Inward Dial Digit Translation Service

In Cisco CME 3.2.3 and later versions, a Tcl script is available to provide digit translation for Direct Inward Dial (DID) calls when the DID digits provided by the PSTN Central Office (CO) do not match the digits in the range of Cisco Unified CME extension numbers in the internal dial plan. For example, this script is useful when the CO provides DID digits such as 75 that should map to extension 460.

The Direct Inward Dial Digit Translation Service is described in the following sections:

Note For more information about Cisco IOS voice features, see the entire Cisco IOS Voice Configuration Library—including library preface and glossary, feature documents, and troubleshooting information—at http://www.cisco.com/en/US/docs/ios/12_3/vvf_c/cisco_ios_voice_configuration_library_glossary/vcl.htm .

## Information About DID Digit Translation Service

The Direct Inward Dial Digit Translation Service accepts PSTN DID numbers of any length and maps them to the internal extension numbers that have been assigned by a system administrator. The service also appends a user-specified prefix to the DID digits to complete a valid extension number. The service uses the parameters that you input to determine the valid range of digits to be accepted from the CO, the valid range of digits in the local dial plan, and the prefix to append. The service also handles any DID calls that map to invalid extension numbers by playing a prompt and disconnecting the calls.

When a new DID call is received by the Cisco Unified CME system, the following events occur:

- The DID Digit Translation Service collects the digits and retains only the last n digits, where n is equal to the number of digits allowed in the range of DID digits coming from the CO. The collected digits are compared with the specified CO DID range. For example, if the DID number is 555-0133 and the specified CO DID range is 00 to 49, the received digits (33) are within the range (00 to 49), so they are accepted.

- If the digits are not within the range, the call is disconnected after a prompt has been played to tell the caller that the number is invalid.

- If the digits from the CO are within the specified range, they are transformed to the range that is specified for the Cisco Unified CME extension number digits. The DID Digit Translation Service appends the DID prefix to the received digits to form a valid extension and routes the call to that extension. Consider an example in which the specified DID range is 55 to 79, the range of specified extension number digits is 00 to 24, and the specified prefix is 5. The DID digits actually received on a call from the CO are 62. The service transforms those digits using the following steps:

– The service measures the offset of the actual digits received, 62, from the lower limit of the specified CO range, which is 55. The result is the offset from the lower limit, 07.

– This result is then added to the lower limit of the site extension number range, which is 00. The result is the digit string to be used in the extension number, 07.

– The service finally appends the specified prefix, which is 5. The resulting extension number for this call is 507.

- If the extension does not exist, the call is disconnected after a prompt has been played to tell the caller that the number is invalid. The audio file named en_disconnect.au supplies the prompt. You can rerecord a custom prompt in this file by following the guidelines in the “ Welcome Prompt and Other Audio Files ” section in the “ Cisco Unified CME Basic Automatic Call Distribution and Auto-Attendant Service ” chapter.

Note Do not change the filename of the en_disconnect.au file because the script will be looking for a file with that name.

- If the extension is busy, a busy tone is played and the call is disconnected. If call forward on busy is enabled, the call will be forwarded to a target, such as voice mail.

## How to Configure DID Digit Translation Service

The purpose of this procedure is to enable the DID Digit Translation Service to automatically transform digits sent from a PSTN CO into the correct digits to form valid extension numbers in your Cisco Unified CME system.

### Prerequisites

- The DID Digit Translation Service Tcl script and default audio prompt files must be downloaded from the Cisco Unified CME Software Download Center and installed on the Cisco Unified CME router. For more information, see the “Downloading Tcl Scripts and Audio Prompts” section in the “Cisco Unified CME Basic Automatic Call Distribution and Auto-Attendant Service” chapter.

- The valid range of DID numbers sent by the PSTN CO must be known.

- The valid range of extension numbers serviced by the Cisco Unified CME router must be known.

- The quantity of numbers within the range of numbers provided by the CO must equal the quantity of extension numbers specified. The number of digits in each string of digits must match each other, although a prefix can be added to the Cisco Unified CME extension number range to make those numbers the same as the actual extension numbers. A maximum of two digits can be added for the prefix. For example, you could use the following pairs of limits:

– CO range is 00 to 39, and Cisco Unified CME extension number range is 40 to 79 (both ranges contain 40 numbers and are 2 digits in length)

– CO range is 150 to 199, and Cisco Unified CME extension number range is 245 to 294 (both ranges contain 50 numbers and are 3 digits in length)

### SUMMARY STEPS

1. enable

2. configure terminal

3. application

4. service [ alternate | default ] did-application-name location

5. paramspace language-package location url

6. paramspace language-package index number

7. paramspace language-package language language-code

8. param did-prefix digits

9. param secondary-prefix digits

10. param co-did-min min-co-value

11. param co-did-max max-co-value

12. param store-did-min min-site-value

13. param store-did-max max-site-value

14. exit

15. exit

16. dial-peer voice tag pots or dial-peer voice tag voip

17. application aa-app-name

18. Repeat Step 16 through Step 17 for each additional dial peer that will receive incoming calls from the CO.

### DETAILED STEPS

Step 1

enable

Router> enable

Enables privileged EXEC mode.

- Enter your password if prompted.

Step 2

configure terminal

Router# configure terminal

Enters global configuration mode.

Step 3

application

Router(config)# application

Enters application configuration mode to configure packages and services.

Step 4

service [ alternate | default ] did-application-name location

Router(config-app)# service didapp tftp://192.168.254.254/scripts/did/app-cme-did-2.0.0.0.tcl

Enters service parameter configuration mode to configure parameters for the digit-translation service.

- alternate —(Optional) Alternate service to use if the service that is configured on the dial peer fails.

- default —(Optional) Specifies that the default service (“DEFAULT”) on the dial peer is used if the alternate service fails.

- did-application-name —Name of the DID application. This is an arbitrary name that will be used with the commands that set parameters for this application.

- location —Location of the Tcl script or VoiceXML document in URL format. Valid storage locations are TFTP, HTTP, and flash.

Step 5

paramspace language-package location url

Router(config-app-param)# paramspace english location flash:

Defines the location of audio files that are used for dynamic prompts by an IVR application.

- language-package —Name of the language package to be used. There are three built-in language packages: Chinese, English, and Spanish. Other languages may be supported by use a of Tcl language script.

- url —URL of the audio files. Valid URLs can refer to TFTP or HTTP servers or to flash memory.

Step 6

paramspace language-package index number

Router(config-app-param)# paramspace english index 1

Defines the category of audio files that are used for dynamic prompts by an IVR application.

- language-package —Name of the language package to be used. There are three built-in language packages: Chinese, English, and Spanish. Other languages may be supported by use a of Tcl language script.

- number —Category group of the audio files (from 0 to 4). For example, audio files representing the days and months could be category 1, audio files representing units of currency could be category 2, and audio files representing units of time—seconds, minutes, and hours—could be category 3. Range is from 0 to 4; 0 means all categories.

Step 7

paramspace language-package language language-code

Router(config-app-param)# paramspace english language en

Specifies the language for dynamic prompts used by the DID application.

- language-package —Name of the language package to be used. There are three built-in language packages: Chinese, English, and Spanish. Other languages may be supported by use a of Tcl language script.

- language-code —Two-character code that identifies the language of the associated audio files. Valid entries are as follows:

– en —English

– sp —Spanish

– ch —Mandarin

– aa —all

Note This language code must match the two-character language prefix used in the names of your audio prompt files, regardless of the language that is actually used in the files. For more information, see the “Welcome Prompt and Other Audio Files” section in the “Cisco Unified CME Basic Automatic Call Distribution and Auto-Attendant Service” chapter.

Step 8

param did-prefix prefix

Router(config-app-param)# param did-prefix 4

Sets a prefix to add to the DID digits that are forwarded by the PSTN to create an extension number on the primary Cisco Unified CME router.

- prefix —Prefix to add. Range is from 0 to 99.

Step 9

param secondary-prefix secondary-prefix

Router(config-app-param)# param secondary-prefix 7

(Optional) Sets a prefix to add to the DID digits that are forwarded by the PSTN for use with a secondary Cisco Unified CME router. This prefix is used to route calls to the primary Cisco Unified CME router.

When there are insufficient DID ports on a Cisco Unified CME router, a secondary Cisco Unified CME router or Cisco IOS gateway can be established to receive DID calls. Incoming DID calls to the secondary router are routed across H.323 to the primary router. The DID Digit Translation Service appends the DID prefix that was set in Step 6 to the incoming DID digits, and then appends a secondary prefix to route the call to the primary Cisco Unified CME router. For example, an incoming DID call is for extension 325. The incoming DID digits from the CO are 25, the DID prefix is 3, and the secondary prefix is 7. The number as transformed by the service is 7325. The transformed number matches a VoIP dial peer that routes the call to the primary router. A translation rule is used to send only the relevant digits, 325, to the primary Cisco Unified CME router for further routing to the extension.

- secondary-prefix —Prefix to add to digits in order to route calls to the primary Cisco Unified CME router. Range is from 0 to 99.

Step 10

param co-did-min min-co-value

Router(config-app-param)# param co-did-min 00

Sets the lower boundary of the valid range of digits coming from the PSTN CO.

- min-co-value —Minimum value of digits coming from the CO. The digit string can be any length, but the string length must be the same in the param co-did-min , param co-did-max , param store-did-min , and param store-did-max commands.

Step 11

param co-did-max max-co-value

Router(config-app-param)# param co-did-max 39

Sets the upper boundary of the valid range of digits coming from the PSTN CO.

- max-co-value —Maximum value of digits coming from the CO. The digit string can be any length, but the string length must be the same in the param co-did-min , param co-did-max , param store-did-min , and param store-did-max commands.

Step 12

param store-did-min min-store-value

Router(config-app-param)# param store-did-min 00

Sets the lower boundary of the range of digits that are valid in the Cisco Unified CME numbering plan.

- min-store-value —Minimum value of digits in the Cisco Unified CME dial plan. The digit string can be any length, but the string length must be the same in the param co-did-min , param co-did-max , param store-did-min , and param store-did-max commands.

Step 13

param store-did-max max-store-value

Router(config-app-param)# param store-did-max 39

Sets the upper boundary of the range of digits that are valid in the Cisco Unified CME numbering plan.

- did-name —Application name that was assigned to the DID script with the service command in Step 4 .

- max-store-value —Maximum value of digits in the Cisco Unified CME dial plan. The digit string can be any length, but the string length must be the same in the param co-did-min , param co-did-max , param store-did-min , and param store-did-max commands.

Step 14

exit

Router(config-app-param)# exit

Exits service parameter configuration mode.

Step 15

exit

Router(config-app)# exit

Exits application configuration mode.

Step 16

dial-peer voice tag pots

or

dial-peer voice tag voip

Router(config)# dial-peer voice 234 pots

or

Router(config)# dial-peer voice 25 voip

Enters dial-peer configuration mode.

- tag —Number used during configuration tasks to identify this dial peer.

Step 17

application did-name

Router(config-dial-peer)# application aa1

Associates this dial peer with the DID Digit Translation application.

- did-name —Application name that was assigned to the DID script with the service command in Step 4 .

Step 18

Repeat Step 16 through Step 17 for each additional dial peer that will receive incoming calls from the CO.

## C onfiguration Examples

The following examples are included in this section:

Example: DID Numbers in the Same Range as Extension Numbers

In the following example, the application is named did . A range of DID numbers from 00 to 39 is assigned by the PSTN CO. The range of extensions is from 300 to 339. A prefix of 3 is added to the CO digits, which are forwarded without being changed.

application

service did tftp://192.168.254.254/scripts/did/app-cme-did-2.0.0.0.tcl

paramspace english index 1

paramspace english language en

paramspace english location tftp://192.168.254.254/apps/dir25/

param did-prefix 3

param co-did-min 00

param co-did-max 39

param store-did-min 00

param store-did-max 39

voice-port 2/0/0

signal did immediate

dial-peer voice 4000 pots

application did

port 2/0/0

Example: DID Numbers Not in the Same Range as Extension Numbers

In the following example, the application is named didapp . The range of DID numbers that is sent from the CO is not identical to the range of extension numbers used at the Cisco Unified CME site, so they must be converted by the application. The quantity of numbers in the CO range that you input to the application using the co parameters must equal the quantity of extension numbers in the local site plan, which you also input to the application using the store parameters. The following formula is used to ensure this equality:

co-did-max - co-did-min = store-did-max - store-did-min

In this example, the digits that are provided by the CO fall in the range from 55 to 74. The local site uses extensions in the range from 400 to 419. The formula verifies that these are valid ranges for the script: (74-55) = 19 = (419-400). Note that this formula is used only to verify equality. The actual number of extensions is 20.

To implement the plan in this example, the DID application is given a prefix digit of 4 and the range parameters shown in the following example. Note that the number of digits in the minimum-maximum digit strings is the same (2) for the CO and for the site commands.

Example: Secondary Router

In the following example, the application is called didapp . Calls are received by a secondary Cisco Unified CME router and are sent to the primary Cisco Unified CME router, which is identified in the session target command under dial peer 1000. The prefix 5 is appended to two incoming digits from the CO to create an extension number. The secondary prefix 4 is then appended to the resulting extension number to route the call to the H.323 VoIP dial peer. The dial peer uses a translation rule to forward only the three relevant digits, (the extension number) to the primary router. For more information about translation rules, see the “ Voice Translation Rules ” technical note at http://www.cisco.com/en/US/tech/tk652/tk90/technologies_tech_note09186a0080325e8e.shtml .

application

service didapp tftp://192.168.254.254/scripts/did/app-cme-did-2.0.0.0.tcl

paramspace english index 1

paramspace english language en

paramspace english location tftp://192.168.254.254/apps/dir25/

param secondary-prefix 4

param did-prefix 5

param co-did-min 00

param co-did-max 39

param store-did-min 00

param store-did-max 39

!

voice-port 2/0/0

signal did immediate

!

dial-peer voice 4000 pots

application didapp

port 2/0/0

!

voice translation-rule 1

rule 1 /^45/ /5/

!

voice translation-profile drop-secondary-prefix

translate called 1

!

dial-peer voice 1000 voip

translation-profile outgoing drop-secondary-prefix

destination-pattern 45..

session target ipv4:10.1.1.1

dtmf-relay h245-alphanumeric

codec g711ulaw

no vad

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Router# configure terminal | Enters global configuration mode. |
| Step 3 | application Router(config)# application | Enters application configuration mode to configure packages and services. |
| Step 4 | service [ alternate \| default ] did-application-name location Router(config-app)# service didapp tftp://192.168.254.254/scripts/did/app-cme-did-2.0.0.0.tcl | Enters service parameter configuration mode to configure parameters for the digit-translation service. alternate —(Optional) Alternate service to use if the service that is configured on the dial peer fails. default —(Optional) Specifies that the default service (“DEFAULT”) on the dial peer is used if the alternate service fails. did-application-name —Name of the DID application. This is an arbitrary name that will be used with the commands that set parameters for this application. location —Location of the Tcl script or VoiceXML document in URL format. Valid storage locations are TFTP, HTTP, and flash. |
| Step 5 | paramspace language-package location url Router(config-app-param)# paramspace english location flash: | Defines the location of audio files that are used for dynamic prompts by an IVR application. language-package —Name of the language package to be used. There are three built-in language packages: Chinese, English, and Spanish. Other languages may be supported by use a of Tcl language script. url —URL of the audio files. Valid URLs can refer to TFTP or HTTP servers or to flash memory. |
| Step 6 | paramspace language-package index number Router(config-app-param)# paramspace english index 1 | Defines the category of audio files that are used for dynamic prompts by an IVR application. language-package —Name of the language package to be used. There are three built-in language packages: Chinese, English, and Spanish. Other languages may be supported by use a of Tcl language script. number —Category group of the audio files (from 0 to 4). For example, audio files representing the days and months could be category 1, audio files representing units of currency could be category 2, and audio files representing units of time—seconds, minutes, and hours—could be category 3. Range is from 0 to 4; 0 means all categories. |
| Step 7 | paramspace language-package language language-code Router(config-app-param)# paramspace english language en | Specifies the language for dynamic prompts used by the DID application. language-package —Name of the language package to be used. There are three built-in language packages: Chinese, English, and Spanish. Other languages may be supported by use a of Tcl language script. language-code —Two-character code that identifies the language of the associated audio files. Valid entries are as follows: – en —English – sp —Spanish – ch —Mandarin – aa —all Note This language code must match the two-character language prefix used in the names of your audio prompt files, regardless of the language that is actually used in the files. For more information, see the “Welcome Prompt and Other Audio Files” section in the “Cisco Unified CME Basic Automatic Call Distribution and Auto-Attendant Service” chapter. |
| Step 8 | param did-prefix prefix Router(config-app-param)# param did-prefix 4 | Sets a prefix to add to the DID digits that are forwarded by the PSTN to create an extension number on the primary Cisco Unified CME router. prefix —Prefix to add. Range is from 0 to 99. |
| Step 9 | param secondary-prefix secondary-prefix Router(config-app-param)# param secondary-prefix 7 | (Optional) Sets a prefix to add to the DID digits that are forwarded by the PSTN for use with a secondary Cisco Unified CME router. This prefix is used to route calls to the primary Cisco Unified CME router. When there are insufficient DID ports on a Cisco Unified CME router, a secondary Cisco Unified CME router or Cisco IOS gateway can be established to receive DID calls. Incoming DID calls to the secondary router are routed across H.323 to the primary router. The DID Digit Translation Service appends the DID prefix that was set in Step 6 to the incoming DID digits, and then appends a secondary prefix to route the call to the primary Cisco Unified CME router. For example, an incoming DID call is for extension 325. The incoming DID digits from the CO are 25, the DID prefix is 3, and the secondary prefix is 7. The number as transformed by the service is 7325. The transformed number matches a VoIP dial peer that routes the call to the primary router. A translation rule is used to send only the relevant digits, 325, to the primary Cisco Unified CME router for further routing to the extension. secondary-prefix —Prefix to add to digits in order to route calls to the primary Cisco Unified CME router. Range is from 0 to 99. |
| Step 10 | param co-did-min min-co-value Router(config-app-param)# param co-did-min 00 | Sets the lower boundary of the valid range of digits coming from the PSTN CO. min-co-value —Minimum value of digits coming from the CO. The digit string can be any length, but the string length must be the same in the param co-did-min , param co-did-max , param store-did-min , and param store-did-max commands. |
| Step 11 | param co-did-max max-co-value Router(config-app-param)# param co-did-max 39 | Sets the upper boundary of the valid range of digits coming from the PSTN CO. max-co-value —Maximum value of digits coming from the CO. The digit string can be any length, but the string length must be the same in the param co-did-min , param co-did-max , param store-did-min , and param store-did-max commands. |
| Step 12 | param store-did-min min-store-value Router(config-app-param)# param store-did-min 00 | Sets the lower boundary of the range of digits that are valid in the Cisco Unified CME numbering plan. min-store-value —Minimum value of digits in the Cisco Unified CME dial plan. The digit string can be any length, but the string length must be the same in the param co-did-min , param co-did-max , param store-did-min , and param store-did-max commands. |
| Step 13 | param store-did-max max-store-value Router(config-app-param)# param store-did-max 39 | Sets the upper boundary of the range of digits that are valid in the Cisco Unified CME numbering plan. did-name —Application name that was assigned to the DID script with the service command in Step 4 . max-store-value —Maximum value of digits in the Cisco Unified CME dial plan. The digit string can be any length, but the string length must be the same in the param co-did-min , param co-did-max , param store-did-min , and param store-did-max commands. |
| Step 14 | exit Router(config-app-param)# exit | Exits service parameter configuration mode. |
| Step 15 | exit Router(config-app)# exit | Exits application configuration mode. |
| Step 16 | dial-peer voice tag pots or dial-peer voice tag voip Router(config)# dial-peer voice 234 pots or Router(config)# dial-peer voice 25 voip | Enters dial-peer configuration mode. tag —Number used during configuration tasks to identify this dial peer. |
| Step 17 | application did-name Router(config-dial-peer)# application aa1 | Associates this dial peer with the DID Digit Translation application. did-name —Application name that was assigned to the DID script with the service command in Step 4 . |
| Step 18 | Repeat Step 16 through Step 17 for each additional dial peer that will receive incoming calls from the CO. |  |