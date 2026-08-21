---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-bacd-configuration-guide-cme40tcl-40bacd-html-2b53dde4df
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/bacd/configuration/guide/cme40tcl/40bacd.html
retrieved_at: 2026-08-21T23:02:31.430525+00:00
---

Cisco Unified CME B-ACD and Tcl Call-Handling Applications

# Cisco Unified CME B-ACD and Tcl Call-Handling Applications

Updated: June 22, 2010

Chapter: Cisco Unified CME Basic Automatic Call Distribution and Auto-Attendant Service (B-ACD)

## Chapter: Cisco Unified CME Basic Automatic Call Distribution and Auto-Attendant Service (B-ACD)

Revised: November 30, 2016

Note Prior to version 4.1, the name of the product was Cisco CallManager Express.

Basic automatic call distribution (B-ACD) and auto-attendant (AA) service is available to provide the following functionality:

- Automatic answering of outside calls with greetings and menus that allow callers to select the appropriate department or to dial known extension numbers.

- Managed call queues for hunt groups that route calls for different menu options.

- Tools for obtaining call statistics.

The Cisco Unified Communications Manager Express B-ACD and AA service (hereinafter referred to as Cisco Unified CME B-ACD) is described in the following sections:

Note This guide describes Cisco Unified CME applications that use Tcl scripts version 2.1.0.0 or later. These scripts use “param” commands rather than the older “call application voice” commands.

Note For more information about Cisco IOS voice features, see the entire Cisco IOS Voice Configuration Library—including library preface and glossary, feature documents, and troubleshooting information—at http://www.cisco.com/en/US/docs/ios/12_3/vvf_c/cisco_ios_voice_configuration_library_glossary/vcl.htm.

## Information About Cisco Unified CME B-ACD

To configure Cisco Unified CME B-ACD, you should understand the following concepts:

- Cisco Unified CME B-ACD Overview

– Cisco Unified CME B-ACD Limitations

### Cisco Unified CME B-ACD Overview

Cisco Unified CME B-ACD provides automatic answering and call distribution for calls through the use of interactive menus and local hunt groups. Each Cisco Unified CME B-ACD application consists of one or more auto-attendant (AA) services and one call-queue service.

From Unified CME Release 11.5 onwards, Unified CME B-ACD introduces support for voice hunt group that includes SIP, SCCP, PSTN, and FXS. Previously, only ephone hunt groups were supported by Cisco Unified CME B-ACD. The document mentions ephone hunt group and voice hunt group as hunt group, unless otherwise necessary.

To invoke B-ACD services when calling from a local SIP, SCCP, or FXS phone, a loopback call is established. The loopback call invokes the B-ACD application on incoming voip dial-peer. This functionality is supported from Unified CME Release 11.6 onwards.

From Unified CME Release 11.6 onwards, LTI-based transcoding is supported on Cisco 4000 Series Integrated Services Router (ISR). Prior to this release, it was mandatory that the calls on the SIP trunk had the g711ulaw codec. Otherwise, calls were rejected. Also, calls from line side phones were configured with g711ulaw codec. With transcoding support introduced for Unified CME on Cisco 4000 Series ISR, the incoming calls from the SIP trunk or line side phones are successfully placed even if they use a different codec. In this scenario, the calls from a SIP trunk or a line side call is placed as a loopback call. The transcoder is invoked between the incoming SIP trunk or line side call, and the outgoing loopback dial peer of B-ACD.

From Unified CME Release 12.2 onwards, voice hunt groups with sequential, parallel, peer, and longest idle call blast support SIP shared lines and mixed shared lines. Unified CME B-ACD supports SIP shared lines and mixed shared lines in a voice hunt group as part of this enhancement.

T he call flow for a simple Cisco Unified CME B-ACD service is shown in Figure 1 . An incoming call dials the B-ACD AA pilot number and hears a prompt that provides a greeting and instructions to help the caller automatically route the call.

For example, callers to a newspaper might hear: “Thank you for calling the Times. To place an advertisement or to subscribe to the Times, press 1; for the editorial department, press 2; for the operator, press 0; if you know your party’s extension, press 4.” Callers who do not select an option will hear the greeting and menu options repeated.

After a caller presses a digit to be connected to a particular department or service, the call is routed to a call queue for a hunt group that has been set up to answer calls for that department or service. If a phone is available in the hunt group, the call is connected. If no phone is available in the hunt group, the call remains in the call queue. While the call is in the queue, the caller hears music on hold (MOH). At intervals, the caller hears a second greeting audio prompt. From the queue, the call periodically reattempts to connect to a phone in the hunt group. If no phone becomes available within a specified period, the call is routed to an alternate, configurable destination.

The Cisco Unified CME B-ACD application is specified by two Tool Command Language (Tcl) scripts: an AA script that handles the welcome prompt and menu choices, and a call-queue script that manages call routing and queuing behavior.

Note The Cisco Technical Assistance Center (TAC) supports the rerecording of audio prompts used with the Tcl scripts but does not support modification of the scripts themselves. It is recommended that you consider every loopback BACD call as 2 calls for design considerations and call capacity planning. For more information, see the “Custom Cisco Unified CME B-ACD AA and Call-Queue Scripts” section .

Figure 1 illustrates a call flow that is directed by the Tcl AA and call-queue scripts. The example is shown for ephone-hunt group. The example is valid for voice hunt group when ephone hunt group is replaced with voice hunt group.

Figure 1 Cisco Unified CME B-ACD Service Call Flow

### Cisco Unified CME B-ACD Limitations

Use same codec on incoming and outgoing dial peers when transferring calls. Using different codecs are not supported. IOS will not invoke transcoder for the calls handled by any TCL application.

Note Calls can be transcoded on a Unified CME (on Cisco 4000 Series ISR) that supports B-ACD, if you use B-ACD Loopback functionality. For more information, see Cisco Unified CME B-ACD Overview .

### Cisco Unified CME B-ACD Components

As mentioned, the Cisco Unified CME B-ACD application consists of a call-queue service and one or more AA services. The configurable components of these services are described in the following sections:

### P ilot Number

Each AA service has its own AA pilot number that callers dial to reach the AA. This number is specified in the param aa-pilot command. The AA pilot number is not associated with any SIP, SCCP, or physical phone, but you do need to define a dial peer with the AA pilot number as the incoming called number so that this number is reachable by outside callers.

### W elcome Prompt and Other Audio Files

The welcome prompt is an audio file that is played when a call is answered by the pilot number. This audio file is one of a number of audio files that are used with the B-ACD service to inform callers of their status and any actions that they may take. In particular, you will want to create personalized audio files to describe the menu choices that are available to your callers. Cisco Unified CME B-ACD audio files are described in the following sections:

### Rerecording Default Audio Files

Default audio files are provided for each point in the script at which prompts are given to callers. You download the default audio files from the Cisco Unified CME Software Download website and copy them to a place that can be reached by the Cisco Unified CME router, such as flash memory or a TFTP server. The audio files and the script files are bundled in a tar archive called cme-b-acd-x.x.x.tar on the website. The default files and their messages are listed in Table 2-1 . You can rerecord personalized messages over the default messages, but you should not change the names of the audio files, except as specifically described in the “Changing Language Codes and Filenames” section .

To rerecord and install the default audio prompts before using a Cisco Unified CME B-ACD service for the first time, follow the steps in the “Downloading Tcl Scripts and Audio Prompts” section . To rerecord audio prompts in an existing Cisco Unified CME B-ACD service, follow the steps in the “Updating Script Parameters and Audio Prompts” section .

.

Table 2-1 Cisco Unified CME B-ACD Default Audio Files

Default Filename

Default Announcement

Length of Default Announcement

e n_bacd_welcome.au

“Thank you for calling.” Includes a two-second pause after the message.

3 seconds

e n_bacd_options_menu.au

“For sales press 1 (pause), for customer service press 2 (pause), to dial by extension press 3 (pause), to speak to an operator press zero.” Includes a four-second pause after the message.

15 seconds

e n_bacd_disconnect.au

“We are unable to take your call at this time. Please try again at a later time. Thank you for calling.” Includes a four-second pause after the message.

10 seconds

e n_bacd_invalidoption.au

“You have entered an invalid option. Please try again.” Includes a one-second pause after the message. This prompt is played when a caller chooses an invalid menu option or dials an invalid extension.

7 seconds

e n_bacd_enter_dest.au

“Please enter the extension number you want to reach.” Includes a five-second pause after the message. This prompt is played when a caller chooses the dial-by-extension option.

7 seconds

e n_bacd_allagentsbusy.au

“All agents are currently busy assisting other customers. Continue to hold for assistance. Someone will be with you shortly.” Includes a two-second pause after the message. This prompt is also known as the second greeting.

7 seconds

e n_bacd_music_on_hold.au

Music on hold (MOH) is played to Cisco Unified CME B-ACD callers.

60 seconds

If you do rerecord any of the audio files, note that the Cisco Unified CME B-ACD prompts require a G.711 audio file (.au) format with 8-bit, mu-law, and 8-kHz encoding. We recommend the following audio tools or others of similar quality:

- Adobe Audition for Microsoft Windows by Adobe Systems Inc. (formerly called Cool Edit by Syntrillium Software Corp.)

- AudioTool for Solaris by Sun Microsystems Inc.

For more information, see the “Configuring Audio File Properties for TCL IVR and VoiceXML Applications” chapter in the Cisco IOS Tcl IVR and VoiceXML Application Guide .

### C h anging Language Codes and Filenames

Audio prompts can be recorded in any language. Default files are supplied in English (see Table 2-1 ).

The names of audio prompt files consist of two parts: a prefix, which is a language code, and an identifier that tells you the file’s function. For example, en_bacd_welcome.au consists of a prefix, en, and an identifier, _bacd_welcome.au, which indicates that the file contains the welcome prompt. Note that the identifier always begins with an underscore. The prefix can be changed to represent any of the following built-in language packages:

- ch—Chinese

- en—English (default)

- sp—Spanish

- aa—All three

Note Do not change names of audio files except for the following cases:

- The prefix of any filename may be changed to ch, en, sp, or aa. The prefix must match the code that is specified in the language-code parameter in the paramspace language command, regardless of the actual language used in the file.

- Following its prefix, the welcome prompt filename (default is en_bacd_welcome.au) may have any identifying name, as defined in the param welcome-prompt command.

- Following its prefix, the drop-through prompt filename (no default supplied) may have any identifying name, as defined in the param drop-through-prompt command.

In the audio files, you may record a prompt in any language. It is not necessary to change the prefix of a file that contains a prompt in a different language because the language-code prefixes are used for features that are not a part of the Cisco Unified CME B_ACD service. But it is important that the language-code prefixes for your files match the language code that is specified in the language-code parameter in the paramspace language command, regardless of the language actually used in the audio file. For more information, see the “Configuring Audio File Properties for TCL IVR and VoiceXML Applications” chapter in the Cisco IOS Tcl IVR and VoiceXML Application Guide .

The identifier part of the name of an audio file should not be changed, with the exception of the _bacd_welcome.au file, as explained in the following paragraphs. The scripts will be looking for audio files that have the same identifying names as those in Table 2-1 and that have the same prefix that you specify in the paramspace language command.

The two exceptions to the general filenaming rules are the welcome-prompt audio file (default is en_bacd_welcome.au) and the drop-through-option prompt audio file (no default supplied). The identifying parts of the filenames for these two audio prompts are specified explicitly during configuration and are completely user-configurable. These files may use any filenames as long as the names observe the following conventions:

- The prefix part of the filename must be the same as the language code that is specified in the paramspace language command. For example, en.

- The identifier part of the filename must start with an underscore. For example, _welcome_to_xyz.au.

More information about the welcome-prompt file and its contents is available in the “Using Audio Files to Describe Menu Choices” section . More information about the drop-through-prompt file is available in the “Drop-Through Mode” section .

### Usin g Audio Files to Describe Menu Choices

By default, two audio files are supplied to provide initial caller orientation and guidance about the menu choices that are available: en_welcome_prompt.au and en_bacd_options_menu.au. You can rerecord customized messages over the default messages that are supplied in these files, as explained in Table 2-2 .

If your Cisco Unified CME B-ACD service uses a single AA service, record a welcome greeting in en_welcome_prompt.au and record instructions about menu choices in en_bacd_options_menu.au.

If your Cisco Unified CME B-ACD service uses multiple AA services, you will need separate greetings and instructions for each AA, using the following guidelines:

- Record a separate welcome prompt for each AA service, using a different name for the audio file for each welcome prompt. For example, en_welcome_aa1.au and en_welcome_aa2.au. The welcome prompts that you record in these files should include both the greeting and the instructions about menu options.

- Record silence in the audio file en_bacd_options_menu.au. A minimum of one second of silence must be recorded. Note that this file does not contain the menu instructions when there are multiple AA services.

Note To change the language prefix or identifier part of the name of an audio file, follow the guidelines in the “Changing Language Codes and Filenames” section .

Table 2-2 Audio Files That Describe Menu Choices

Filename

Name Specification

How Used

e n_welcome_prompt.au

Filename can be changed; must match the name specified in the param welcome-prompt command.

To change the language prefix or identifier part of the filename, follow the guidelines in the “Changing Language Codes and Filenames” section .

Default is “Thank you for calling.”

When you have a single AA service, use this audio file to record a customized greeting.

When you have multiple AAs, use this audio file to record a customized greeting and menu options for customers to use.

e n_bacd_options_menu.au

Only the language prefix can be changed; the identifying part of the filename must remain the same.

Default is “For sales press 1, (pause) for customer service press 2 (pause), to dial by extension press 3 (pause), to speak to an operator press zero.”

When you have a single AA service, use this audio file to record menu options for customers.

When you have multiple AAs, record silence in this file. A minimum of one second of silence must be recorded.

### M enu Options

The purpose of a Cisco Unified CME B-ACD service is to automatically route calls to the correct destination in your organization. Interactive AA services enable you to provide menu options to callers so that they can make the appropriate choices for their calls. The types of menu options that are available in Cisco Unified CME B-ACD are described in Table 2-3 . Menu options are announced to callers by audio prompts, which are described in the “Welcome Prompt and Other Audio Files” section .

Table 2-3 Types of Menu Choices Available for Cisco Unified CME B-ACD Service

Type

Description

Requirements

Example

Hunt group

Caller presses a specified digit to be connected to a group of extensions that has been designated a hunt group. If all extensions in the hunt group are busy, calls are held in a call queue or sent to an alternate, configurable destination.

A hunt group must be established.

After dialing the number for a computer store, a caller presses 1 to be connected to a hunt group that consists of phones in the sales department, or presses 2 to be connected to the hunt group for technical support, 3 to be connected to the hunt group for billing questions, or 0 to be connected to the operator hunt group.

O perator hunt group

Special case of hunt group; caller presses a specified digit or 0 to be connected to a hunt group with the special purpose of providing operator, or lookup and connection, services to callers.

A hunt group to provide operator services must be established.

D ial-by-extension

Caller presses a digit to be allowed to dial a known extension.

Note The menu number used for this option must not be the same as any menu (aa-hunt) numbers used with the call-queue service.

No requirements.

After hearing the menu choices, a caller dials 4 and is able to dial an internal extension number.

D rop-through mode

Caller is directly connected to a hunt group, following the playing of an optional welcome prompt if one is specified.

Note When drop-through mode is assigned to an AA, it is the only option for that AA. If you want some callers to get drop-through treatment and others to be able to make menu choices, you must set up multiple AAs.

Cisco CME 3.2.1 or a later version must be used.

A hunt group must be established.

A caller dials a special toll-free number for online sales at the computer store and hears a recording (“Thank you for calling. An agent will be with you shortly.”). The caller is put directly through to the online-sales hunt group if an agent is available to take the call or is put in a call queue for the hunt group if all agents are busy.

### H u nt Group Option, Ephone Hunt Groups, and Voice Hunt Groups

Most often, a Cisco Unified CME B-ACD service will connect callers to hunt groups, as shown by menu options 1, 2, and 3 in Figure 1 . To use the newspaper example, one of the hunt groups might be a group of editorial writers who take turns answering the calls that select the option to speak to the editorial group. A maximum of ten hunt groups can be used with a B-ACD call-queue service.

A Cisco Unified CME B-ACD hunt group is a hunt group that has been configured without the final command. The final destination for a call in a hunt group used with the B-ACD service is determined by the configuration of the B-ACD service and is controlled by the call-queue service rather than by the hunt group configuration.

T he hunt group option is configured using the aa-hunt parameter that associates menu numbers with the pilot numbers of hunt groups. For example, the following command associates menu option 2 (aa-hunt2) with the hunt group pilot number 1111. In this example, when callers dial 2 after hearing the menu-choices audio prompt, they are put in the call queue for the hunt group with the pilot number 1111.

param aa-hunt2 1111

An operator hunt group is a special case of hunt group. It is a group of phones that is prepared to provide lookup and connection services to callers. For this purpose, the B-ACD script assumes that the hunt group with the highest aa-hunt number is the operator group and allows this group to be reached when a caller dials 0 or dials the aa-hunt option number. For example, in a B-ACD application with two hunt groups, aa-hunt1 and aa-hunt2, a caller who dials 0 will be connected to aa-hunt2.

Figure 2 shows how B-ACD menu options work together with hunt groups. When a caller selects a menu option associated with a hunt group, the AA service calls the corresponding hunt group pilot number. The B-ACD call-queue service is activated and the call is placed in a queue so that it can be transferred to an ephone-dn (voice register dn for voice hunt group) when one becomes available.

Note Figure 2 describes an ephone hunt group for B-ACD configuration. The example is valid for voice hunt group pilot numbers as well.

It is important to note that, while the hunt group configuration specifies the type of hunt group and its membership, the B-ACD service controls call queuing and the alternate destination of B-ACD calls when a hunt group is unavailable. For more information on call-queue behavior, see the “Call Queues” section . For more information about alternate destinations, see the “Alternate Destination for Unavailable Hunt Groups” section .

Note Shared ephone-dns cannot log in and out of ephone hunt groups. If shared ephone-dns are included as members of hunt groups, they must be listed as fixed members of the group and automatic logout cannot be enabled for the group.

### Call Timeout and Retry in Unified CME B-ACD Hunt Groups

A call placed through a B-ACD service to a hunt group can remain unanswered for a default duration of 180 seconds. However, you can set a custom value for call timeout duration, using the CLI command timeout configured under ephone-hunt (for SCCP phones) and voice hunt-group (for SIP phones). The range for timeout is 3 to 60000 seconds. If the call remains unanswered for the specified duration of timeout, the service retries to connect to a hunt group pilot number or to the alternate destination number. You can use the CLI command call-retry-timer to set the amount of time that calls must wait between retries. The default retry timer is set to 5 seconds. The range is 1 to 30. For more information on the commands timeout and call-retry-timer , see Step 6 in Setting Up Ephone Hunt Groups and Step 28 in Setting Up Call-Queue and AA Services .

Note For better user experience, it is recommended to configure the call-retry-timer value to be higher than the value configured for timeout of hunt groups.

For information about ephone hunt groups and voice hunt group and their configuration, see the “Hunt Groups” section in the “ Configuring Call-Coverage Features ” chapter of the Cisco Unified Communications Manager Express System Administration Guide .

Figure 2 Example of Cisco Unified CME B-ACD Hunt Groups

### D ia l-by-Extension Option

The Cisco Unified CME B-ACD service can also have a dial-by-extension option, which allows callers to dial internal extension numbers when they already know the extension number. The dial-by-extension option is shown as menu option 4 in Figure 1 .

The dial-by-extension option is configured by specifying a menu option number for the dial-by-extension parameter. When the following command is used, callers can dial 1 and then an extension number.

param dial-by-extension-option 1

Within a B-ACD call-queue service, the dial-by-extension option number and the hunt group option numbers must be mutually exclusive. This restriction means that the option number used for the dial-by-extension option cannot be the same as any of the option numbers used with the aa-hunt options. For example, if you use aa-hunt1 to aa-hunt5 to specify hunt groups in your call-queue service configuration, then you can use option 6 for the dial-by-extension option but not any of the numbers 1 to 5. If all ten aa-hunt numbers are used for hunt groups in the call-queue service, there is no option left for the dial-by-extension option. Note that this restriction is based on all the option numbers (aa-hunt numbers) used with the call-queue service and not on the option numbers used with an AA application.

### D rop -Through Mode

Most AAs that are used with Cisco Unified CME B-ACD are set up for interactive mode, in which callers make choices about the routing of their calls on the basis of the menu information that is provided to them in an audio prompt. In Cisco CME 3.2.1 and later versions, an AA can be set up for drop-through mode instead of interactive mode.

When an AA is configured for drop-through mode, the AA sends incoming calls directly to a call queue without providing menu choices to callers. Once in the queue, a caller hears ringback if an agent is available or music on hold (MOH) if all agents are busy. If a prompt for drop-through mode is configured, the caller hears the prompt before being sent to the queue as described. The drop-through prompt is simply a greeting to callers; it might say “Thank you for calling XYZ, Inc. An agent will be with you shortly.” Note that customers cannot make interactive choices in drop-through mode; calls are simply answered and routed to a call queue.

### M ultiple Auto-Attendant Services

Cisco Unified CME 3.2.1 and later versions support the creation of multiple Auto-Attendant (AA) services that feed into a single call-queue service that manages up to ten hunt groups (individual call queues). Unified CME 11.5 and later versions support multiple auto-attendant services in a single call queue for both ephone hunt group and voice hunt group.

Each of the AAs can be set up to use different options or to reach different hunt groups, and AAs can also share hunt groups. For instance, you can have three AAs that each use three hunt groups, or you can have five AAs that share some of the ten hunt groups, or ten AAs that each use one hunt group. This flexibility allows companies to create different automatic-attendant treatment for different classes of callers.

For example, you can set up an AA in interactive mode to answer calls using a prerecorded message that offers various menu choices to callers. One type of menu choice is to allow a caller to press a digit to be connected to a department or service (hunt group). Another type of menu choice can allow the caller to dial a known extension number directly.

Alternatively, you can set up an AA in drop-through mode, a new feature with Cisco CME 3.3, which is described in the “Drop-Through Mode” section . An AA that is set up in drop-through mode transfers incoming calls directly into a call queue for a hunt group without allowing any interactive choice by the caller. A prompt is optional in drop-through mode. When you configure multiple AAs, each AA can be independently assigned to interactive or drop-through mode.

When you set up multiple interactive AAs, separate welcome prompts must be recorded for each AA. With multiple AAs, the welcome prompt is used to inform callers about the menu choices that are available to them. (With a single AA, a different audio file performs that function.) For more information, see the “Welcome Prompt and Other Audio Files” section .

A maximum of ten call queues and hunt groups can be used with the call-queue script. An AA can use a maximum of three hunt groups from those ten, but an AA can also use fewer than three hunt groups or several AAs can share one or more hunt groups. A shared operator hunt group is not included in that maximum; you can add a shared operator hunt group in addition to the three hunt groups that an AA uses, or it can be part of the three hunt groups. The maximum number of calls that can be in queue for each of the ten possible hunt groups is 30, so a potential of 300 calls can be queued.

In the Cisco Unified CME B-ACD configuration, hunt groups are labeled aa-hunt1 to aa-hunt10. The digit following the “aa-hunt” part of the label corresponds to a digit that callers are instructed to dial when they reach an interactive AA. For example, if a caller is told to “dial 1 for sales,” the caller will be routed to the hunt group labeled aa-hunt1 after dialing 1.

When a caller presses 0 for the operator, the digit 0 maps to the highest hunt group (aa-hunt1 to aa-hunt10) that has been configured. The hunt group aa-hunt10 is always reserved for the operator, and the default operator option is 0. Therefore, if you have set up hunt group aa-hunt7 to be the operator hunt group, a caller can dial either 7 or 0 to reach the operator hunt group. If you set up ten hunt groups, aa-hunt10 will always be the operator hunt group because it has the highest aa-hunt number.

Figure 3 illustrates a Cisco Unified CME site with multiple AAs. The first AA (AA1) is reached when customers dial the DID number 800 555-0155. AA1 can forward calls to hunt group 1 (pilot number 1010), hunt group 2 (2010), hunt group 3 (3010), or the operator hunt group (hunt group 7 or pilot number 1030).

The second automated attendant service (AA2) is reached when customers dial the DID number 800 555-0177. AA2 can forward calls to hunt group 3 (pilot number 3010), hunt group 4 (1020), hunt group 5 (2020), or the operator hunt group (hunt group 7 or 1030).

The third automated attendant service (AA3) is reached when customers dial the DID number 800 555-0188. AA3 can forward calls to hunt group 6 (pilot number 3020) only.

Figure 3 Multiple AA Hunt Group Assignment

The following characteristics summarize Cisco Unified CME B-ACD properties:

- A maximum of one call-queue service can be used with any number of AA services.

- A maximum of 10 hunt groups can be used with a call-queue service. Each ephone hunt group can have up to 20 extensions, and each voice hunt group can have up to 32 extensions.

- A maximum of three hunt groups (individual call queues) can be used with an AA service; an operator hunt group may be separate or may be one of the three hunt groups.

- A maximum of nine hunt groups can be used across all AA services combined, not including the operator hunt group which is shared by all AA services.

- A hunt group can be reserved for a single AA or can be shared among several AAs.

- The maximum number of calls that can be queued for a hunt group is 30.

- The digit 0 always maps to the hunt group with the highest aa-hunt number in the configuration.

### C all Queues

As shown in Figure 1 , most incoming calls to a Cisco Unified CME B-ACD service are transferred to call queues associated with hunt groups. If a member of the hunt group is available to take a call, the call is connected. If no member of the hunt group is available, the call remains in the call queue for that hunt group. Note that a call queue, although dedicated to a particular hunt group, is managed by the B-ACD call-queue script and not by the hunt group itself.

While a call is in queue, the caller hears music on hold. (Note that for Cisco Unified CME B-ACD, music on hold from a live feed is not available in Cisco CME 3.3.) While in the call queue, the call periodically retries the hunt group to see if a hunt group member is available to answer the call. A second greeting is played to reassure callers that they are still in line to be answered. For example, the second greeting might say: “Thank you for waiting. Calls are answered in the order they are received. Please remain on the line.” For more information about recording a customized second greeting, see the “Welcome Prompt and Other Audio Files” section .

Consider a scenario with multiple calls in a call queue. For sequential hunt groups, when the first incoming call is not answered by agents and the call continues to hunt sequentially through the hunt group, then the second call in the queue will not start hunting until the first call is answered.

When the maximum time in queue expires without a successful retry to connect the call to the hunt group, the call-queue service considers the call unanswerable and sends it to an alternate destination outside the Cisco Unified CME B-ACD service, as described in the “Alternate Destination for Unavailable Hunt Groups” section .

Call-queue parameters are configurable. You can specify the amount of time that passes between hunt-group retries and the maximum amount of time that a call can be held in queue. You can record your own second-greeting audio file. You can also specify the maximum number of calls that queues can contain and enable the collection of information for debugging the call queue.

Figure 4 shows how an AA and a call-queue service handle the following three calls when the call-queue length is set to ten calls (The example is valid for voice hunt group when ephone hunt group is replaced with voice hunt group):

- A call to hunt group 1 goes to call queue 1 and waits for ephone-dn/voice register dn1001, 1002, or 1003 to become available. When one of those directory numbers becomes available, the first call in the queue is transferred to it. Waiting calls advance one space in the queue and continue to retry phones in the hunt group periodically. If the maximum retry time expires before the call is answered, the call is sent to the alternate destination that has been configured.

- A call to hunt group 2 is answered by ephone-dn/voice register dn 2003 or 2004, both of which are available to take calls.

- A call to hunt group 3 receives a busy tone because all of the allotted call-queue slots are occupied.

In summary, B - ACD calls that are intended for a hunt group are handled as follows:

- If all hunt group agent phones are busy, a B-ACD call to the hunt group is sent to the call queue that is dedicated to that hunt group.

- If all hunt group agent phones are in not-ready status or have left the hunt group (there are no agents available to take calls), a B-ACD call to the hunt group is sent to the configured alternate destination (see “Alternate Destination for Unavailable Hunt Groups” section ).

- If some of the hunt group agent phones are busy and other phones are unavailable (in not-ready status or have left the hunt group), a B-ACD call to the hunt group is sent to the call queue.

Figure 4 Cisco Unified CME B-ACD Call Queues with Queue Length Set to 10

### Call Waiting Notification

Cisco Unified CME B-ACD service supports call waiting notification display for both ephone hunt groups (SCCP phones) and voice hunt groups (SIP phones, mix of SIP and SCCP phones). If members of a hunt group are busy or unavailable to attend an incoming call, the call is placed in the call queue for that hunt group. As long as the call queue retries the hunt group to place the call to an agent, the call remains in queue. During this period, all agents in the hunt group receive a call waiting notification. The call waiting notification provides the agents with information on the number of calls placed in queue for that hunt group. If the agent is logged out, the call waiting notification is not displayed.

The call waiting notification is displayed on the home screen of the agent phone. For example, the following message is displayed on the agent phone, 2 calls in queue . The notification enables the agent to know that calls are waiting, and helps to decide on attending incoming calls.

Note In an ephone hunt group, the Hlog softkey can be configured to indicate that there are calls in the queue. The Hlog softkey on the agent phone blinks if there is an active call queue in the hunt group.

The call waiting notification can be configured for three different display preferences:

- Off – If the call waiting notification display preference is set to Off, the agents will not receive any notification about the calls waiting in the call queue. The calls remain in the call queue as long as the agents are busy, but no notification will be sent to the agents.

- Continuous – If the call waiting notification display preference is set to Continuous, the notification about the calls waiting in the call queue is displayed continuously. The notification preference is governed by a preset time period of 7 seconds after which a new notification is pushed based on the latest call queue. That is, if there are deletions or additions to the call queue within the time period of the first notification (0-7 seconds), the new notification (7-14 seconds) will reflect the same. The agent phone displays notifications as long as there are calls in the queue.

- Periodic – If the call waiting notification display preference is set to Periodic, the agents will receive new notifications once within a preset interval of 21 seconds. Hence, a new call waiting notification is pushed to the agent phone every 21 seconds. This notification displays for 7 seconds. The new notification that is generated every 21 seconds reflect the latest call queue status, based on the call queue status for the last 21 seconds.

Use the command callqueue display to set the CME B-ACD call waiting notification display as continuous, periodic, or off. The default form of the command, default callqueue display sets the call waiting notification display to the default state of periodic (for voice hunt group) and continuous (for ephone hunt group). For more details on the command, see the Cisco Unified Communications Manager Express Command Reference .

For the detailed set of steps to configure call waiting display in ephone hunt groups, see “ Setting Up Ephone Hunt Groups ” section.

For the detailed set of commands to configure call waiting display in voice hunt groups, see “ Setting Up Voice Hunt Groups ” section.

Use the command show ephone-hunt to identify the number of calls in queue in an ephone hunt group. The command show voice hunt-group identifies the number of queued calls in a voice hunt group. For more details on the commands, see the Cisco Unified Communications Manager Express Command Reference .

### Call Queue Exit Options

In Cisco Unified CME 7.0(1) and later versions, if the number of calls in a queue reaches the maximum limit, you can specify alternate destinations to send calls, enabling callers to select from up to three different options to exit from the call queue.

You record a customized second greeting to inform callers of up to three options to exit from the call queue. For example, you might record a message that says, “To leave a message, press 6; to hear other options, press 7; to speak to an operator, press 8.”

This second greeting is stored in the audio file named en_bacd_allagentsbusy.au. You can record over the default message in this file, provided you do not change the name of the file. For more information, see the “Welcome Prompt and Other Audio Files” section .

For information on configuring the exit options, see the “Setting Up Call-Queue and AA Services” section .

### Al ternate Destination for Unavailable Hunt Groups

Calls are diverted to an alternate destination in three circumstances (see Figure 1 ):

- T he hunt group to which a call has been transferred is unavailable because all members are logged out or in do-not-disturb (DND) mode.

- The call-queue maximum retry timer has expired.

- The number of calls waiting in the call queue has reached the limit.

Note Call diversion to alternate destination is not supported for voice hunt groups in do-not-disturb (DND) mode.

The alternate destination can be any number at which you can assure call coverage, such as a voice-mail number, a permanently staffed number, or a number that rings an overhead night bell. After a call is diverted to an alternate destination, it is no longer controlled by the B-ACD service.

The B-ACD call-queue service relinquishes control of a call only when the alternate destination answers the call. If the call cannot be connected, it remains in the queue. If no connection can be made to the alternate destination, the call is disconnected.

If the amount of time a call is in the queue exceeds the limit set by the param max-time-call-retry command, the call is routed to the alternate destination set with the param voice-mail command. If the param max-time-vm-retry command is set to a number higher than one, the call-queue service retries to connect that number of times.

In Cisco Unified CME 7.0(1) and later versions, if the number of calls waiting in a B-ACD call queue exceeds the number set with the param queue-len command, the call is routed to the alternate destination set with the param queue-overflow-extension command.

If you send calls to a voice-mail system as an alternate destination, be sure to set up the voice-mail system as specified in the documentation for the system. In addition, see the “ Integrating Voice Mail ” chapter of the Cisco Unified Communications Manager Express System Administrator Guide .

Whatever number is specified for an alternate destination must be associated with a dial peer that is reachable by the Cisco Unified CME system.

### Conf iguring for Voice Mail

An external voice-mail system is not part of a Cisco Unified CME B-ACD application, but if you have such a system, the following steps are used in Cisco Unified CME to enable the voice-mail system to receive calls from the B-ACD service.

### SUMMARY STEPS

1.	Set the Cisco Unified CME B-ACD alternate destination to a voice register dn or ephone dn with Call Forward All set to the voice-mail pilot number.

2.	On the Cisco Unified CME router, configure a dial peer for the voice-mail pilot.

3.	Configure Cisco Unified CME hunt groups.

4.	In the Cisco Unified CME B-ACD call-queue service, define hunt group pilot numbers.

5.	To receive the MWI notification on hunt group agents, include the voice register dn or ephone dn configured with Call Forward All as the secondary dn under the pool or ephone.

6.	In the voice-mail application, set up a group and group delivery mailbox (GDM) for voice register dn or ephone dn that has Call Forward All configured to the voice-mail pilot number.

7.	Create users for hunt group agents who needs to receive the MWI notification. Configure these users as members of the group created in Step 6.

### DETAILED STEPS

Step 1	Set the Cisco Unified CME B-ACD alternate destination to a voice register dn or ephone dn with Call Forward All set to the voice-mail pilot number:

# voice-mail configuration for service

param voice-mail 1010

#Configuration example for Call Forward All to voice-mail (SIP Phones)

voice register dn 2

label gdm

number 1010

call-forward b2bua all 9999

shared-line

# voice-mail configuration for service

param voice-mail 2020

#Configuration example for Call Forward All to voice-mail (SCCP Phones)

ephone-dn 2

descripti		on gdm

number 2020

call-forward all 9999

Note Configure the directory number as shared line if the MWI notification for voice-mail needs to be sent to multiple agents.

Step 2	On the Cisco Unified CME router, configure a dial peer for the voice-mail pilot. In the following example, a dial peer is configured with a destination pattern of 9999:

dial-peer voice 100 voip

destination-pattern 9999

session protocol sipv2

session target ipv4:192.168.10.1

codec g711ulaw

dtmf-relay sip-notify

no v	ad

Note When a Cisco Unity Express or Cisco Unity application is used for voice mail and it sends information to Cisco Unified CME through an H.323 dial peer but receives information from Cisco Unified CME 			through a SIP dial peer, you must also include the following commands in your configuration:

voice service voip

allow-connections h323 to h323

allow-connections h323 to sip

no supplementary-service h450.2

no supplementary-service h450.3

Step 3	Configure Cisco Unified CME hunt groups. In the following sample configuration, ephone hunt group 1 is configured with a pilot number of 1111; ephone hunt group 2 is configured with pilot number 2222:

ephone-hunt 1 longest-idle

pilot 1111

list 1001,1002,1003,1004

timeout 10

ephone-hunt 2 longest-idle

pilot 2222

list 2001,2002,2003,2004, 2005, 2006, 2007, 2008, 2009, 2010

timeout 10

In the following sample configuration, voice hunt group 1 is configured with a pilot number of 3333;

voice hunt group 2 is configured with a pilot number of 4444:

voice hunt-group 1 parallel

pilot 3333

list 3001,3002,3003,3004

timeout 10

voice hunt-group 2 sequential

pilot 4444

list 4001,4002,4003,4004,4005,4006,4007,4008,4009,4010

timeout 10

Note If you are configuring both ephone hunt group and voice hunt group, the ephone hunt pilot and voice hunt pilot should be different.

Step 4	In the Cisco Unified CME B-ACD call-queue service, define hunt group pilot numbers.

param queue aa-hunt1 1111

param queue aa-hunt2 2222

OR

param queue aa-hunt1 3333

param queue aa-hunt2 4444

Step 5	Include the voice register dn or ephone dn configured with Call Forward All as the secondary dn under the pool or ephone configured for hunt group agents.

ephone-dn 1

number 1001

mwi on

ephone 1

mac-address 1111.2222.3333

type 7970

button 1:1 2:2

voice register dn 1

number 3001

mwi

voice register pool 1

id mac 4444.5555.6666

type 7841

number 1 dn 1

number 2 dn 2

Note The configuration is for agents who needs to receive the MWI notification.

Step 6	In the voice-mail application, set up a group and group delivery mailbox (GDM) for voice register dn or ephone dn that has Call Forward All configured to the voice-mail pilot number.

ccn application voicemail

description “voicemail”

enabled

maxsessions 8

script "voicebrowser.aef"

parameter "logoutUri" "http://localhost/voicemail/vxmlscripts/mbxLogout.jsp"

parameter "uri" "http://localhost/voicemail/vxmlscripts/login.vxml"

end application

ccn engine

end engine

ccn subsystem jtapi

ccm-manager address 10.0.0.0

end subsystem

ccn subsystem sip

gateway address "192.168.10.1" ;This is the address used in the Cisco Unified CME

;session target command in the voice-mail dial peer.

end subsystem

ccn trigger sip phonenumber 9999 ;This is the voice-mail pilot number.

application "voicemail"

enabled

maxsessions 8

end trigger

groupname AltDest create

groupname AltDest phonenumber 1010

voicemail mailbox owner “AltDest” size 300

description “AltDest-mailbox”

enable

end mailbox

Step 7	Create users for all hunt group agents who needs to receive MWI notification. Configure these users as members of the group created in Step 6.

username Agent1 create

username Agent1 phonenumber 3001

grouname AltDest member Agent1

voicemail mailbox owner “Agent1” size 300

description “Agent1-mailbox”

enable

end mailbox

Note To retrieve voice messages, hunt agents need to press 9 and then select the correct IVR option to access the GDM.

Restrictions

- Only one GDM can be configured for the ten hunt groups configured under the call queue service.

- Since Unified CME supports a maximum of 16 subscriptions (from different phones) for a shared line directory number, only16 SIP or SCCP hunt agents can get MWI notification for voice-mail.

For more information about configuring mailboxes for your voice-mail application, see the documentation for your application.

For information about integrating with Cisco Unity, see the Cisco Communications Manager Express Integration Guide for Cisco Unity .

For more information about integrating with Cisco Unity Express, see Integrating Cisco CallManager Express with Cisco Unity Express .

### Cisco Unified CME B- A CD Call Activity Reports

Two call report methods allow you to monitor call activity. One is the show ephone-hunt command, which displays call statistics with descriptions. The other uses TFTP to automatically create comma-delimited call-statistics files for reports. The statistics can be merged into charts or graphs for easier reading with applications such as Microsoft Access and Excel.

For example, a newspaper could measure caller response to an editorial by issuing the show ephone-hunt command for a specific period of time. If the newspaper wanted to collect statistics about the occurrence and duration of peak call times, it could use TFTP reports to gather data at hourly intervals. The newspaper could also use either method to gather information about the average time and longest time it took for calls to be answered, the number of callers that hung up or left voice-mail messages, and so forth. For more information, see the “Collecting Statistics” section .

### Cu stom Cisco Unified CME B-ACD AA and Call-Queue Scripts

The set of Cisco IOS software commands that are described in this document allow you to set values for parameters that are used with the Cisco Unified CME B-ACD AA and call-queue Tcl scripts. Direct editing of the Tcl scripts that support the applications is not recommended or supported by the Cisco Technical Assistance Center (TAC).

In Cisco IOS Release 12.4(15)T and later releases, Cisco Unified CME B-ACD AA and call-queue Tcl scripts are embedded in the Cisco IOS software which are functionally the same as the scripts available in the Cisco Unified CME B-ACD tar archives. Use these embedded, or built-in, scripts as a baseline for testing and debugging customized scripts.

Note Cisco IOS Release 12.4(15)T contains version 2.1.2.2 of the Cisco Unified CME B-ACD AA and call-queue Tcl scripts.

## How to Configure Cisco Unified CME B-ACD

This procedure sets up a Cisco Unified CME B-ACD service on the Cisco Unified CME router to handle the automatic receipt and distribution of incoming calls. It consists of the following tasks:

### P lanning the Cisco Unified CME B-ACD Call Flow

In this task, you will make decisions about how incoming calls should be handled. The decisions that you make will determine the type and number of AAs and call queues (hunt groups) that you need to set up, as well as routing options and an alternate destination to offer callers if a hunt group is unavailable.

### SUMMARY STEPS

1.	Select a name to use for the call-queue service.

2.	Decide whether more than one AA application is needed.

3.	Select a name and pilot number to use for each AA application.

4.	Select the number and type of call-routing (menu) options to offer callers for each AA application.

5.	Decide on the wording for your customized prompts.

6.	Decide on the call-retry parameters that you want to set.

7.	Choose an alternate destination for calls that are unanswered because a hunt group is unavailable or because the maximum call-retry timer has expired.

### DETAILED STEPS

Command or Action

Purpose

Step 1

Select a name to use for the call-queue service.

During configuration, the call-queue service name is used in the commands that pertain to the call-queue service. There is only one call-queue service for a Cisco Unified CME B-ACD. You can use any name.

Step 2

Decide whether more than one AA application is needed.

If you want some callers to have different menu options than other callers, set up multiple AA applications. For instance, you might want some callers to be directly connected to a hunt group, and you might want other callers to have the option of dialing an extension or choosing among several hunt groups. For more information about multiple AAs, see the “Cisco Unified CME B-ACD Components” section .

Step 3

Select a name and pilot number to use for each AA application.

During configuration, the AA application name is used to specify that certain commands pertain to an AA application. You can use any name, and you need a different name for each AA that you define.

Each AA needs its own pilot number, which must be reachable from outside the Cisco Unified CME system.

Step 4

Select the number and type of call-routing (menu) options to offer callers for each AA application.

For each AA application, decide what options to offer callers and what hunt groups you will use.

You can designate that an AA application will operate in interactive mode, in which callers make active choices on the basis of the menu choices that you offer. By pressing the specified digit, a caller can take any of the following actions:

- Connect to a hunt group.

- Connect to an operator hunt group.

- Dial a known extension.

Alternatively, you can designate that an AA application will operate in drop-through mode, in which calls are directly sent to a hunt group without giving callers the opportunity to make choices.

There is one call-queue service per B-ACD, which can handle up to ten hunt groups. Each AA application can handle up to three hunt groups, in addition to a shared operator hunt group. For more information, see the “Menu Options” section and the “Hunt Group Option, Ephone Hunt Groups, and Voice Hunt Groups” section .

Step 5

Decide on the wording for your customized prompts.

Each default audio prompt from the Cisco Unified CME Software Download website can be rerecorded with custom information for your application. Plan the wording that you want to use for each prompt. For more information, see the “Welcome Prompt and Other Audio Files” section .

Step 6

Decide on the call-retry parameters that you want to set.

You can change the defaults for the following values:

- Second-greeting time—Amount of time before a second greeting is played or replayed to callers in call queues. Default is 60 seconds.

- Call-retry—Amount of time before a call in queue tries again to transfer to the hunt group. Default is 15 seconds.

- Maximum call-retry timer—Amount of time before a call in queue is considered unanswered because all retry attempts to connect to the hunt group have failed. Default is 600 seconds.

- Alternate destination retries—Number of times that a call in queue attempts to contact an alternate destination number before it is disconnected. Default is 1 time.

For more information, see the “Call Queues” section .

Step 7

Choose an alternate destination for calls that are unanswered because a hunt group is unavailable or because the maximum call-retry timer has expired.

The alternate destination that you choose might be a pilot number for voice mail, or a number that is assigned to an overhead bell, or some other number that you are sure will be answered. For more information, see the “Alternate Destination for Unavailable Hunt Groups” section .

### D ownloading Tcl Scripts and Audio Prompts

In this task, you prepare the script files and prompt files that are necessary for your Cisco Unified CME B-ACD service.

Note Every Loopback BACD service is treated as 2 SIP calls. You should consider the same during capacity planning.

### SUMMARY STEPS

1.	Download the Cisco Unified CME B-ACD tar archives to a TFTP server that is accessible to the Cisco Unified CME router.

2. enable

3. archive tar /xtract source-url flash:

4.	Rerecord audio files if necessary.

### DETAILED STEPS

Command or Action

Purpose

Step 1

Download the Cisco Unified CME B-ACD tar archive to a TFTP server that is accessible to the Cisco Unified CME router.

Go to the Cisco Unified CME Software Download website at http://www.cisco.com/cgi-bin/tablebuild.pl/ip-iostsp .

Download the Cisco Unified CME B-ACD tar archive called cme-b-acd-2.1.0.0.tar (or a later version) to a TFTP server that is accessible to the Cisco Unified CME router.

This tar archive contains the AA Tcl script, the call-queue Tcl script, and the default audio files that you need for Cisco Unified CME B-ACD service.

Note If you have Cisco IOS Release 12.4(15)T or a later release and you use the embedded AA and call-queue Tcl scripts, you still must perform this step to download the audio files in the tar archive.

Step 2

enable

Router> enable

Enables privileged EXEC mode on the Cisco Unified CME router.

- Enter your password if prompted.

Step 3

archive tar /xtract source-url flash:

Router# archive tar /xtract tftp://192.168.1.1/cme-b-acd-x.x.x.tar flash:

Uncompresses the files in the Cisco Unified CME B-ACD file archive and copies them to flash memory. The following files are contained in the cme-b-acd-x.x.x.tar archive:

- app-b-acd-aa-x.x.x.x.tcl (AA script)

- app-b-acd-x.x.x.x.tcl (call-queue script)

- en_bacd_allagentsbusy.au (audio file)

- en_bacd_options_menu.au (audio file)

- en_bacd_disconnect.au (audio file)

- en_bacd_music_on_hold.au (audio file)

- en_bacd_invalidoption.au (audio file)

- en_bacd_welcome.au (audio file)

- en_bacd_enter_dest.au (audio file)

Step 4

Rerecord audio files if necessary.

Rerecord audio files with your custom messages, but do not change the audio filenames except as specified here.

Note that each audio filename is composed of two parts: a language code prefix and an identifier portion that begins with an underscore. (For example, for en_bacd_invalidoption.au, en is the prefix and _bacd_invalidoption.au is the identifier portion.)

The prefix portion of the audio filename can be changed to match any of the language codes that are allowed in the paramspace language command. The prefix must match the language code that you specify in that command, regardless of the language actually used in the audio file. For example, if you use the Spanish language code for the invalid option file, the filename would be sp_bacd_invalidoption.au.

The identifier portion of the filename must not be changed, except for the en_bacd_welcome.au file. That filename must be changed when you have multiple AAs because you need a different welcome message, and therefore a different audio file, for each AA. You can use any name that follows the same format as the default file: start the filename with a prefix that matches the specified language code, and start the identifier portion with an underscore. Use a .au suffix for the filename.

For more information about audio files, see the “Welcome Prompt and Other Audio Files” section .

### Examples

The following example extracts files from the archive called cme-b-acd-2.1.0.0 on the server at 192.168.1.1 and copies them to the Cisco Unified CME router flash memory.

archive tar /xtract tftp://192.168.1.1/cme-b-acd-2.1.0.0.tar flash:

### Se tting Up Incoming Dial Peers for AA Pilot Numbers

In this task, you associate dial peers for incoming calls with the AA service that you want them to use.

Cisco Unified CME B-ACD is available for outside calls through voice ports and trunks, for which dial peers must be set up. When you set up a dial peer, you use the service command to associate it with the name of the Cisco Unified CME B-ACD AA service that you want callers to that dial peer to reach. The service name is the one that you create in Step 3 in the “Planning the Cisco Unified CME B-ACD Call Flow” section and that you assign to the AA script in Step 10 in the “Setting Up Call-Queue and AA Services” section .

Note You must configure a dial peer for each incoming DID voice port. For more information about dial peers, see Understanding Inbound and Outbound Dial Peers Matching on Cisco IOS Platforms .

To determine how many ports or trunks you must have for your Cisco Unified CME B-ACD service, consider the following:

- Total number of phones across all hunt groups

- Total number of slots in the queues across all queues

- Total number of PSTN ports feeding into the queues

The number of simultaneous calls that Cisco Unified CME B-ACD can handle is limited by the number of PSTN ports, but these ports may not always be in use. For example, you could have three queues with ten slots per queue, but configure only 10 ports instead of 30 because you do not expect the three queues to ever be full at one time.

### SUMMARY STEPS

1. enable

2. configure terminal

3. dial-peer voice tag pots or dial-peer voice tag voip

4. service aa-service-name

5. incoming called-number number

6. port slot / port

7. exit

8.	Repeat Step 3 to Step 7 for each additional dial peer that will receive incoming calls to be directed to an AA service.

### DETAILED STEPS

Command or Action

Purpose

Step 1

enable

Router> enable

Enables privileged EXEC mode on the Cisco Unified CME router.

- Enter your password if prompted.

Step 2

configure terminal

Router# configure terminal

Enters global configuration mode.

Step 3

dial-peer voice tag pots

or

dial-peer voice tag voip

Router(config)# dial-peer voice 234 pots

or

Router(config)# dial-peer voice 25 voip

Enters dial-peer configuration mode.

- tag —Number used during configuration tasks to identify this dial peer.

Step 4

service aa-service-name

Router(config-dial-peer)# service aa1

Associates this dial peer with an AA service.

- aa-service-name —AA service name to be used by this dial peer that was chosen in Step 3 in the “Planning the Cisco Unified CME B-ACD Call Flow” section and that will be assigned to the AA script in Step 10 in the “Setting Up Call-Queue and AA Services” section .

Step 5

incoming called-number number

Router(config-dial-peer)# incoming called-number 8005550100

Specifies a digit string that can be matched by an incoming call to associate the call with a dial peer.

- number —Incoming called telephone number to serve as the AA pilot number for this AA service. Valid entries are any series of digits that specify the E.164 telephone number. The default is the calling number pattern.

Step 6

port slot / port

Router(config-dial-peer)# port 1/0:23

Associates a dial peer with a specific voice port.

- slot / port —Use the appropriate platform-specific port designator for the voice port to be associated with this AA service.

Step 7

exit

Router(config-dial-peer)# exit

Exits dial-peer configuration mode.

Step 8

Repeat Step 3 to Step 7 for each additional dial peer that will receive incoming calls to be directed to an AA service.

—

### Examples

The following example enables a Cisco Unified CME B-ACD AA service called aa on dial peers that are associated with incoming voice ports 1/1/0 and 1/1/1. The calls over these voice ports are sent to the Cisco Unified CME B-ACD pilot number (800 555-0100).

dial-peer voice 1000 pots

service aa

incoming called-number 8005550100

port 1/1/0

dial-peer voice 1001 pots

service aa

incoming called-number 8005550101

port 1/1/1

The following example enables a Cisco Unified CME B-ACD AA service called aa on an incoming dial peer that is associated with a T1 voice trunk. The calls over these voice ports are sent to the Cisco Unified CME B-ACD pilot number (800 555-0100).

dial-peer voice 1003 pots

service aa

incoming called-number 8005550100

direct-inward-dial

port 1/0:23

forward digits-all

The following is a VoIP dial peer, and 192.168.1.1 is a loopback IP address defined on the router. This dial peer is associated with the Cisco Unified CME B-ACD AA service called aa.

dial-peer voice 1004 voip

service aa

destination-pattern 8005550100

session target ipv4:192.168.1.1

incoming called-number 8005550100

dtmf-relay h245-alphanumeric

no vad

codec g711ulaw

### S etting Up Ephone Hunt Groups

In this task you set up ephone hunt groups to receive calls from the call-queue service. A maximum of ten hunt groups can be associated with Cisco Unified CME B-ACD call-queue service. Of those ten hunt groups, a maximum of three can be associated with any one AA service, in addition to a shared operator hunt group that is available to all the AAs. Each hunt group can be assigned to a single AA, or it can be shared among multiple AAs. This task describes only the required commands to set up a hunt group. Additional, optional hunt-group commands are described in the “Hunt Groups” section in the “Call-Coverage Features” chapter in the Cisco Unified Communications Manager Express System Administrator Guide.

Note The final command is not used with hunt groups that are part of Cisco Unified CME B-ACD services. Instead, the param voice-mail command specifies the alternate destination for calls that cannot be connected to a hunt group because all hunt-group agents are unavailable or because a hunt-group agent does not become available within the configured maximum retry time.

### SUMMARY STEPS

1. enable

2. configure terminal

3. ephone-hunt hunt-tag { peer | sequential | longest-idle }

4. pilot number [ secondary number ]

5. list dn-number [ , dn-number ...]

6. timeout seconds [, seconds ...]

7. callqueue display { continuous | periodic | off }

### DETAILED STEPS

Command or Action

Purpose

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

ephone-hunt hunt-tag { longest-idle | peer | sequential }

Router(config)# ephone-hunt 25 sequential

Enters ephone-hunt configuration mode.

- hunt-tag —Unique sequence number that identifies a hunt group during all configuration tasks. Range is 1 to 100.

- longest-idle —Calls go to the extension that has been idle the longest. The longest-idle is determined from the last time that a phone registered, reregistered, or went on-hook.

- peer —First extension to ring is the number to the right (in the list) of the extension that was the last one to ring when the hunt group was last called. Ringing proceeds in a circular manner, left to right, for the number of hops specified when the ephone hunt group is defined.

- sequential —Extensions ring in the order in which they are listed, left to right, when the hunt group s defined.

Step 4

pilot number [ secondary number ]

Router(config-ephone-hunt)# pilot 7000

Defines the pilot number, which is the number that callers dial to reach the hunt group.

- number —E.164 number with a maximum length of 27 characters. The dial-plan pattern can be applied to the pilot number.

- secondary —(Optional) Defines the number that follows as an additional pilot number for the ephone hunt group.

Step 5

list dn-number [ , dn-number ...]

Router(config-ephone-hunt)# list 7001, 7002, 7003, 7004

Defines the list of numbers to which the ephone hunt group redirects the incoming calls that are made to the pilot number. There must be from 1 to 20 numbers in the list.

- dn-number—An ephone-dn primary or secondary number. In Cisco Unified CME 4.0 and later versions, an asterisk (*) can take the place of an extension number to represent a wildcard slot. Any agent at an authorized ephone-dn can dynamically join and leave a hunt group if a wildcard slot is available. There can be up to 20 wildcard slots in a hunt group.

Step 6

timeout seconds [, seconds ...]

Router(config-ephone-hunt)# timeout 10

(Optional) Sets the number of seconds after which a call that is not answered at one number is redirected to the next number in the hunt-group list. If this command is not used the default is the time period set by the timeouts ringing command, which has a default of 180 seconds if it is not set to another value.

- seconds —Number of seconds. Range is from 3 to 60000. In Cisco Unified CME 4.0 and later versions, multiple entries can be made, separated by commas; the number of entries must correspond to the number of ephone-dns in the list command. Each number in a multiple entry specifies the time that the corresponding ephone-dn will ring before a call is forwarded to the next number in the list. If a single number is entered, it is used for the no-answer period for each ephone-dn.

Note Although the timeout command is optional, the default of 180 seconds may be greater than you desire.

Step 7

callqueue display { continuous | periodic | off }

(Optional) Defines the call waiting notification display preference for the phones in a hunt group.

- Continuous — The call waiting notification is displayed continuously on the agent phone, as long as there are active calls in the call queue.

- Periodic —The call waiting notification is displayed for a period of 5 seconds on the agent phone, and updated after an interval of 20 seconds based on the latest call queue.

- Off —The call waiting notification is not displayed on the agent phone.

If the no form of this command is used or the command is not configured, the display preference is set to the default state of continuous.

### Examples

The following two hunt groups are defined for a single AA. Note that the final command is not used in these hunt groups. Each group is a sequential hunt group with a pilot number and a secondary number. Each group contains four members.

ephone-hunt 25 sequential

pilot 7000 secondary 4085550100

list 7001, 7002, 7003, 7004

timeout 10

ephone-hunt 26 sequential

pilot 7050 secondary 4085550101

list 7051, 7052, 7053, 7054

timeout 10

### S etting Up Voice Hunt Groups

In this task you set up voice hunt groups to receive calls from the call-queue service. A maximum of ten hunt groups can be associated with Cisco Unified CME B-ACD call-queue service. Of those ten hunt groups, a maximum of three can be associated with any one AA service, in addition to a shared operator hunt group that is available to all the AAs. Each hunt group can be assigned to a single AA, or it can be shared among multiple AAs. This task describes only the required commands to set up a hunt group. Additional, optional hunt-group commands are described in the “Hunt Groups” section in the “Call-Coverage Features” chapter in the Cisco Unified Communications Manager Express System Administrator Guide.

Note The final command is not used with hunt groups that are part of Cisco Unified CME B-ACD services. Instead, the param voice-mail command specifies the alternate destination for calls that cannot be connected to a hunt group because all hunt-group agents are unavailable or because a hunt-group agent does not become available within the configured maximum retry time.

### SUMMARY STEPS

1. enable

2. configure terminal

3.	voice hunt-group hunt-tag { longest idle | parallel | peer | sequential }

4. pilot number [ secondary number ]

5. list number

6. timeout seconds

7. callqueue display { continuous | periodic | off }

### DETAILED STEPS

Command or Action

Purpose

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

voice hunt-group hunt-tag { longest-idle | parallel | peer | sequential }

Router(config)# voice hunt-group 1 longest-idle

Enters voice hunt-group configuration mode to define a hunt group.

- hunt-tag —Unique sequence number of the hunt group to be configured. Range is 1 to 100.

- longest-idle —Hunt group in which calls go to the directory number that has been idle for the longest time.

- parallel —Hunt group in which calls simultaneously ring multiple phones.

- peer —Hunt group in which the first directory number is selected round-robin from the list.

- sequential —Hunt group in which directory numbers ring in the order in which they are listed, left to right.

- To change the hunt-group type, remove the existing hunt group first by using the no form of the command; then, recreate the group.

Step 4

pilot number [ secondary number ]

Router(config-voice-hunt-group)# pilot number 8100

Defines the pilot number, which is the number that callers dial to reach the voice hunt group.

- number —String of up to 16 characters that represents an E.164 telephone number.

- Number string may contain alphabetic characters when the number is to be dialed only by the Cisco Unified CME router, as with an intercom number, and not from telephone keypads.

- secondary number —(Optional) Keyword and argument combination defines the number that follows as an additional pilot number for the voice hunt group.

- Secondary numbers can contain wild cards. A wild card is a period (.), which matches any entered digit.

Step 5

list number

Router(config-voice-hunt-group)# list 8000, 8010, 8020, 8030

Creates a list of extensions that are members of a voice hunt group. To remove a list from a router configuration, use the no form of this command.

- number —List of extensions to be added as members to the voice hunt group. Separate the extensions with commas.

- Add or delete all extensions in a hunt-group list at one time. You cannot add or delete a single number in an existing list.

- There must be from 2 to 10 extensions in the hunt-group list, and each number must be a primary or secondary number.

- Any number in the list cannot be a pilot number of a parallel hunt group.

Step 6

timeout seconds

Router(config-voice-hunt-group)# timeout 100

Defines the number of seconds after which a call that is not answered is redirected to the next directory number in a voice hunt-group list.

- Default: 180 seconds.

Step 7

callqueue display { continuous | periodic | off }

(Optional) Defines the call waiting notification display preference for the phones in a hunt group.

- Continuous — The call waiting notification is displayed continuously on the agent phone, as long as there are active calls in the call queue.

- Periodic —The call waiting notification is displayed for a period of 5 seconds on the agent phone, and updated after an interval of 20 seconds based on the latest call queue.

- Off —The call waiting notification is not displayed on the agent phone.

If the no form of this command is used or the command is not configured, the display preference is set to the default state of periodic.

### Examples

The following two hunt groups are defined for a single AA. Note that the final command is not used in these hunt groups. Each group is a sequential hunt group with a pilot number and a secondary number. Each group contains four members.

voice hunt-group 25 sequential

pilot 7000

list 7001, 7002, 7003, 7004

timeout 10

voice hunt-group 26 sequential

pilot 7050

list 7051, 7052, 7053, 7054

timeout 10

### Setting Up B-ACD for Loopback Calls

In this task, you set up B-ACD to receive calls from locally configured phones (line side phones) using loopback functionality. From Cisco Unified CME Release 11.6 onwards, B-ACD supports line side calls from SIP, SCCP, FXS phones, or a mixed deployment. For line side calls to be supported, you need to have the B-ACD application and hunt groups configured like a standard B-ACD call scenario.

In the standard B-ACD call scenario, the call to the B-ACD application goes through an incoming dialpeer on the SIP trunk. However in a loopback call scenario for B-ACD, the caller is on the line side of the Unified CME. Hence, you need to configure a loopback voip dialpeer (SIP) with codec (g711ulaw), DTMF (rtp-nte), and a proxy B-ACD pilot number as the destination pattern. Also, you need to change the proxy destination pattern to actual B-ACD pilot number before sending out the call invite. You can achieve this using either voice class sip-profiles or translation rules.

### SUMMARY STEPS

1. enable

2. configure terminal

3.	voice service voip

4.	allow-connections sip to sip

5.	voice class sip-profiles number | translation-rule

6.	dial-peer voice tag voip

7.	destination-pattern string

8.	session target ipv4: destination-address

9.	session protocol sipv2

10.	voice-class sip profiles number

11.	dtmf-relay rtp-nte

12.	codec g711ulaw

13.	end

### DETAILED STEPS

Command or Action

Purpose

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

voice service voip

Router# voice service voip

Enters voice-service configuration mode to specify voip voice encapsulation type.

Step 4

allow-connections sip to sip

Router# allow-connections sip to sip

Allows connections between specific types of endpoints in a VoIP network. SIP to SIP connection is mandatory for B-ACD loopback call scenario.

Step 5

voice class sip-profiles number | translation-rule

Router(config)# voice class sip-profiles

OR

Router(config)# translation-rule

Configures SIP profiles for a voice class. In B-ACD application, this command is used to modify the proxy number to the actual B-ACD pilot number.

- Translation rule—Associates a translation rule with a voice translation profile. In B-ACD application context, translation-rule is an alternative command for voice class sip-profiles.

Step 6

dial-peer voice tag voip

Router(config)# dial-peer voice 2 voip

Enters dial-peer configuration mode.

- tag —Number used during configuration tasks to identify this dial peer.

Step 7

destination-pattern string

Router(config-dial-peer)# destination-pattern 6001

Specifies either the prefix or the full E.164 telephone number (depending on the dial plan) for a dial peer.

- string—The B-ACD proxy pilot number that needs to be configured.

Step 8

session target ipv4: destination-address

Router(config-dial-peer)# session target ipv4:1.0.0.0

Designates a network-specific address to receive calls from a VoIP dial peer. The destination address should same as the IP address of the Unified CME router used.

- destination—IP address for the Cisco Unified CME interface on this router.

Step 9

session protocol sipv2

Router(config-dial-peer)# session protocol sipv2

Designates a SIP loopback trunk for B-ACD application.

Step 10

voice-class sip profiles number

Router(config-dial-peer)# voice-class sip profiles 1

Associates the SIP profile with the dial peer.

Step 11

dtmf-relay rtp-nte

Router(config-dial-peer)# dtmf-relay rtp-nte

Specifies the method for relaying dual tone multifrequency (DTMF) tones between two devices as per RFC2833.

Step 12

codec g711ulaw

Router(config-dial-peer)# codec g711ulaw

Specifies the voice codec used.

Step 13

end

Router(config-dial-peer)# end

Returns to privileged EXEC mode.

### Examples

The following example has B-ACD set up to support loopback call functionality using voice class sip-profiles. In this example, 6000 is the pilot number of the B-ACD application, and 6001 is the proxy number used by line side phones to access B-ACD application.

voice class sip-profiles 1

request INVITE sip-header SIP-Req-URI modify "6001@" "6000@"

request INVITE sip-header To modify "6001@" "6000@"

request INVITE sip-header Remote-Party-ID remove

request INVITE sip-header From modify "<sip:(.*)@" "<sip:A\1@"

voice class sip-profiles 2

request INVITE sip-header From modify "<sip:A(.*)@" "<sip:(.*)\1@"

dial-peer voice 1 voip

destination-pattern 6001

session protocol sipv2

session target ipv4:1.0.0.1

voice-class sip profiles 1

dtmf-relay rtp-nte

codec g711ulaw

dial-peer voice 2 voip

service aa-bcd

session protocol sipv2

incoming called-number 6000

voice-class sip profiles 2

dtmf-relay rtp-nte

codec g711ulaw

The following example has B-ACD set up to support loopback call functionality using translation-rule command.

translation-rule 1

Rule 1 6001 6000

voice translation-rule 2

rule 2 /(^.*)/ /A\1/

voice translation-rule 3

rule 3 /^A(.*)/ /\1/

voice translation-profile PrefixA

translate calling 2

voice translation-profile RemoveA

translate calling 3

dial-peer voice 2 voip

translation-profile incoming RemoveA

service aa-bcd

translate-outgoing calling 3

session protocol sipv2

incoming called-number 6000

dtmf-relay rtp-nte

codec g711ulaw

dial-peer voice 1 voip

translation-profile outgoing PrefixA

destination-pattern 6001

translate-outgoing called 1

session protocol sipv2

session target ipv4:1.0.0.1

dtmf-relay rtp-nte

codec g711ulaw

### S etting Up Call-Queue and AA Services

To set parameters for the call-queue script and for each AA service that you are using, perform the following steps.

Note The commands that are used to set Tcl script parameters (the param and paramspace commands) do not support the following Cisco IOS CLI features:

- You cannot complete a partial command name entry using the Tab key.

- You do not receive error isolation in the form of an error indicator, the caret symbol (^).

- You do not receive a list of supported parameters when you use the question mark (?) key.

- If you do not enter the parameters with the proper case and spelling, the scripts will fail.

### Prerequisites

In Cisco Unified CME 4.2 and later versions, music on hold (MOH) must be configured for services using MOH. If an MOH server is not available, incoming calls disconnect. For configuration information, see “ Configuring Music on Hold ” in the Cisco Unified CME System Administrator Guide .

### SUMMARY STEPS

1. enable

2. configure terminal

3. application

4. service [ alternate | default ] queue-service-name location

5. param number-of-hunt-grps number

6. param aa-hunt menu-number pilot - number

7. param queue-len number

8. param queue-manager-debugs [ 0 | 1 ]

9. exit

10. service [ alternate | default ] aa-service-name location

11. paramspace language-package location url

12. paramspace language-package index number

13. paramspace language-package language language-code

14. param service-name queue-service-name

15. param handoff-string aa-service-name

16. param aa-pilot aa-pilot-number

17. param welcome-prompt audio-filename

18. param number-of-hunt-grps number

19. param menu-timeout number

20. param dial-by-extension-option menu-number

21. param max-extension-length number

22. param drop-through-option menu-number

23. param drop-through-prompt audio-filename

24. param queue-exit-option option-number menu-number

25. param queue-exit-extension option-number extension-number

26. param queue-overflow-extension extension-number

27. param second-greeting-time seconds

28. param call-retry-timer seconds

29. param max-time-call-retry seconds

30. param max-time-vm-retry number

31. param voice-mail number

32. param send-account [ true | false ]

33. param voice-mail-handoff [ true | false ]

### DETAILED STEPS

Command or Action

Purpose

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

service [ alternate | default ] queue-service-name location

Router(config-app)# service queue flash:app-b-acd-2.1.0.0.tcl

In Cisco IOS Release 12.4(15)T or later releases, to use the embedded call-queue script:

Router(config-app)# service app-b-acd

Enters service parameter configuration mode to configure parameters for the call-queue service.

- alternate —(Optional) Alternate service to use if the service that is configured on the dial peer fails.

- default —(Optional) Specifies that the default service (“DEFAULT”) on the dial peer is used if the alternate service fails.

- queue-service-name —Name of the call-queue service. This arbitrary name is used to identify the call-queue service during configuration tasks.

- location —URL of the Tcl script. Valid URLs can refer to TFTP, HTTP, or HTTPS servers, flash memory, or built-in scripts.

Note Cisco IOS Release 12.4(15)T contains version 2.1.2.2 of the Cisco Unified CME B-ACD AA and call-queue Tcl scripts.

Step 5

param number-of-hunt-grps number

Router(config-app-param)# param number-of-hunt-grps 2

Declares the maximum number of hunt groups supported by the Cisco Unified CME B-ACD call-queue script.

- number— Number of hunt groups used by the call-queue service. Range is from 1 to 10.

Note The number argument declares the number of hunt groups only. It does not count the menu option for dial-by-extension. For example, if you have an AA that uses 2 hunt groups and a dial-by-extension option, and an AA with the drop-through option that uses 1 hunt group, enter 3 in this command.

Step 6

param aa-hunt menu-number pilot - number

Router(config-app-param)# param aa-hunt1 1111

Associates a menu number with hunt group pilot number.

Note Repeat this command to associate additional menu numbers with hunt-group pilot numbers. There should be as many entries of this command as the number of hunt groups that is specified in Step 5 .

- menu-number —Single digit that callers dial to choose this menu option (also referred to as the aa-hunt number). Range is from 1 to 10. Note that the hunt group with the highest aa-hunt number is automatically considered the operator hunt group, and its menu number maps to 0 (zero) for callers in addition to mapping to its aa-hunt number.

- pilot-number —Pilot number of the hunt group to which callers are transferred when they press the menu number.

Step 7

param queue-len number

Router(config-app-param)# param queue-len 15

Sets the maximum number of calls allowed in each hunt group’s call queue used by Cisco Unified CME B-ACD.

- number— Number of calls that can be waiting in the call queue for each hunt group. The range is from 1 to 30. The default is 10.

Step 8

param queue-manager-debugs [ 0 | 1 ]

Router(config-app-param)# param queue-manager-debugs 1

Enables or disables the collection of call-queue debug information from the Cisco Unified CME B-ACD call queue service.

- 0 —(Optional) Disables debugging.

- 1 —(Optional) Enables debugging.

Note This command is used with the debug voip application script command. Both the debug voip application script command and the param queue-manager-debugs command must be enabled together when debug trace files are collected.

Step 9

exit

Router(config-app-param)# exit

Exits service parameter configuration mode for the call-queue service.

Step 10

service [ alternate | default ] aa-service-name location

Router(config-app)# service aa flash:app-b-acd-aa-2.1.0.0.tcl

In Cisco IOS Release 12.4(15)T or later releases, to use the embedded AA script:

Router(config-app)# service app-b-acd-aa

Enters service parameter configuration mode to configure parameters for an AA service.

- alternate —(Optional) Alternate service to use if the service that is configured on the dial peer fails.

- default —(Optional) Specifies that the default service (“DEFAULT”) on the dial peer is used if the alternate service fails.

- aa-service-name —Name of an AA service for which parameters are being set. This arbitrary name is used to identify a specific AA service during configuration tasks.

- location —URL of the Tcl script. Valid URLs can refer to TFTP, HTTP, or HTTPS servers, flash memory, or built-in scripts.

Note Cisco IOS Release 12.4(15)T contains version 2.1.2.2 of the Cisco Unified CME B-ACD AA and call-queue Tcl scripts.

Step 11

paramspace language-package location url

Router(config-app-param)# paramspace english location flash:

Defines the location of audio files that are used for dynamic prompts by an interactive voice response (IVR) application.

- language-package —Name of the language package to be used. There are three built-in language packages: Chinese, English, and Spanish. Other languages may be supported by use of a Tcl language script.

- url —URL of the audio files. Valid URLs can refer to TFTP or HTTP servers or to flash memory.

Step 12

paramspace language-package index number

Router(config-app-param)# paramspace english index 1

Defines the category of audio files that are used for dynamic prompts by an IVR application.

- language-package —Name of the language package to be used. There are three built-in language packages: Chinese, English, and Spanish. Other languages may be supported by use of a Tcl language script.

- number —Category group of the audio files (from 0 to 4). For example, audio files representing the days and months could be category 1, audio files representing units of currency could be category 2, and audio files representing units of time—seconds, minutes, and hours—could be category 3. Range is from 0 to 4; 0 means all categories.

Step 13

paramspace language-package language language-code

Router(config-app-param)# paramspace english language en

Defines the language code of audio files that are used for dynamic prompts by an IVR application.

- language-package —Name of the language package to be used. There are three built-in language packages: Chinese, English, and Spanish. Other languages may be supported by use a of Tcl language script.

- language-code —Two-character code that identifies the language of the associated audio files. Valid entries are as follows:

– ch —Chinese

– en —English

– sp —Spanish

– aa —all

Note This language code must match the two-character language prefix used in the names of your audio prompt files regardless of the language that is actually used in the file. For more information, see the “Welcome Prompt and Other Audio Files” section .

Step 14

param service-name queue-service-name

Router(config-app-param)# param service-name app-b-acd

Associates the Cisco Unified CME B-ACD AA script with the Cisco Unified CME B-ACD call queue script.

- queue-service-name— Service name that was assigned to the call-queue service in Step 4 .

Step 15

param handoff-string aa-service-name

Router(config-app-param)# param handoff-string app-b-acd-aa

Specifies the AA service name to be given to the call-queue script. This is a mandatory parameter.

- aa-service-name —Service name that was assigned to a specific AA service in Step 10 .

Step 16

param aa-pilot aa- pilot-number

Router(config-app-param)# param aa-pilot 8005550123

Associates a telephone number with this AA service.

- aa-pilot-number —Phone number to be dialed to reach this AA service.

Step 17

param welcome-prompt audio-filename

Router(config-app-param)# param welcome-prompt _bacd_welcome.au

(Optional) Assigns an audio file for the welcome greeting used by this AA service.

- audio-filename —Identifier part of the name of the audio file that contains the welcome greeting to be played when callers first reach the Cisco Unified CME B-ACD service. The identifier part of the filename does not include the language prefix, and it must begin with an underscore.

The _bacd_welcome.au audio file is used by default. It announces “Thank you for calling” and includes a 2-second pause after the message. To rerecord a customized greeting in this file, see the instructions in the “Welcome Prompt and Other Audio Files” section .

Step 18

param number-of-hunt-grps number

Router(config-app-param)# param number-of-hunt-grps 2

Specifies the number of hunt groups that are used with this AA service.

- number —Number of hunt groups to be used with this AA service. Range is from 1 to 3.

Note If the AA that you are configuring uses the drop-through option, enter 1 for the number of hunt groups in this step.

Step 19

param menu-timeout number

Router(config-app-param)# param menu-timeout 5

(Optional) Sets the number of times the AA service will loop the menu prompt before connecting the caller to an operator if the caller does not select a menu option.

- number —Number of times to replay menu prompt before connecting a caller to an operator if the caller does not select a menu option. Range: 0 to 10. Default: 4.

Step 20

param dial-by-extension-option menu-number

Router(config-app-param)# param dial-by-extension-option 1

(Optional) Enables callers to dial extension numbers after dialing the specified menu number.

- menu-number —Identifier of a menu option. Range is from 1 to 9. There is no default.

Step 21

param max-extension-length number

Router(config-app-param)# param max-extension-length 4

(Optional) Restricts the number of digits that can be dialed by callers using the dial-by-extension option.

Note This command can be used to prevent toll fraud by restricting the number of digits that can be entered as the transfer destination for the dial-by-extension option.

Step 22

param drop-through-option menu-number

Router(config-app-param)# param drop-through-option 2

(Optional) Assigns the drop-through option to a menu number for this AA service.

- menu-number —Menu option number (aa-hunt number) that was associated with a hunt group in Step 6 .

Note When configuring an AA in drop-through mode, set the number of hunt groups in the AA ( Step 18 ) to 1. If an AA is in drop-through-option mode, it cannot have any other options besides one drop-through-option.

Step 23

param drop-through-prompt audio-filename

Router(config-app-param)# param drop-through-prompt _dt_prompt.au

(Optional) Associates an audio prompt file with the drop-through option for this AA service.

- audio-filename —Identifier part of the filename containing the prompt to be played when calls for the drop-through option are answered. The identifier part of the filename does not include the language prefix, and it must begin with an underscore. No default file is supplied.

To record a customized drop-through prompt, see the instructions in the “Welcome Prompt and Other Audio Files” section .

Step 24

param queue-exit-option option-number menu-number

Router(config-app-param)# param queue-exit-option1 6

Assigns a menu number to a call-queue exit option.

- option-number —Number of the call-queue exit option. Range: 1 to 3. There is no default.

- menu-number —Menu option number associated with the exit option.

- Supported in Cisco Unified CME 7.0(1) and later versions.

Step 25

param queue-exit-extension option-number extension-number

Router(config-app-param)# param queue-exit-extension1 202

Assigns an extension number to a call-queue exit option.

- option-number —Number of the call-queue exit option. Range: 1 to 3. There is no default.

- extension-number —Extension number associated with the exit option.

- Supported in Cisco Unified CME 7.0(1) and later versions.

Step 26

param queue-overflow-extension extension-number

Router(config-app-param)# param queue-overflow-extension 5100

Sets the extension number to route calls to when the call queue for the auto-attendant service is full.

- extension-number —Extension number to which the auto-attendant service forwards calls when the queue is full.

- Supported in Cisco Unified CME 7.0(1) and later versions.

Step 27

param second-greeting-time seconds

Router(config-app-param)# param second-greeting-time 45

(Optional) Defines the time delay before the second greeting is played after a caller joins a Cisco Unified CME B-ACD call queue. The same time period is used for the interval between repeats of the second-greeting message. The second greeting is stored in the audio file named en_bacd_allagentsbusy.au. To record a customized second greeting, see the instructions in the “Welcome Prompt and Other Audio Files” section .

- seconds —Time interval before the second-greeting message is played or replayed, in seconds. The range is from 5 to 120. The default is 60.

Step 28

param call-retry-timer seconds

Router(config-app-param)# param call-retry-timer 10

(Optional) Assigns the amount of time that calls must wait between retries to connect to a hunt group pilot number or to the alternate destination number.

- seconds —Time interval, in seconds. The range is from 1 to 30. The default is 5 seconds.

Step 29

param max-time-call-retry seconds

Router(config-app-param)# param max-time-call-retry 700

(Optional) Sets the maximum amount of time for the call-retry timer. This is the maximum period of time for which a call can stay in a call queue and retry to connect with a hunt group before the call is sent to an alternate destination number.

- seconds —Maximum period of time, in seconds. The range is from 30 to 3600. The default is 600.

Step 30

param max-time-vm-retry number

Router(config-app-param)# param max-time-vm-retry 2

(Optional) Assigns the number of times that calls to Cisco Unified CME B-ACD can attempt to reach the alternate destination number.

- number —Number of attempts. The range is from 1 to 3. The default is 1.

Note In most cases, it is useful to have the number of attempts set at a number greater than 1, which will allow retries if the alternate destination number is busy on first attempt.

Step 31

param voice-mail number

Router(config-app-param)# param voice-mail 5003

Defines an alternate destination for calls that are not answered by a hunt group because all members of the hunt group are logged out or because the call was still in a call queue when the maximum-time call-retry timer expired. This is a mandatory parameter.

- number —Alternate extension number to receive calls that remain unanswered by hunt groups. This number must be associated with a dial peer that is reachable by the Cisco Unified CME system.

Note This number may be a voice-mail number, but it may also be any extension number that is set up to provide reliable coverage for unanswered B-ACD calls, such as a number that rings an overhead night bell.

Note If you specify a number associated with a voice-mail system, be sure to set up the voice-mail system as specified in the documentation for the system. In addition, see the “ Integrating Voice Mail ” chapter of the Cisco Unified Communications Manager Express System Administrator Guide .

Step 32

param send-account true

Router(config-app-param)# param send-account true

(Optional) Generates call detail records for calls that are handled by the Cisco Unified CME B-ACD service.

Step 33

param voice-mail-handoff [true|false]

Router(config-app-param)# param voice-mail-handoff true

(Optional) Toggles handoff support for calls to alternate destination. The default value is true.

### Call-Queue and AA Tcl Scripts in Flash Memory: Example

The following example sets up a single AA service, called aa, and a call-queue service, called queue, using the Tcl scripts in flash memory. The service command specifies the location of the scripts. The call flow for this example is as follows:

- Callers dial an AA pilot number, 800 555-0123, to reach this AA service. They are greeted with the prompt that is stored in the audio file called en_bacd_welcome.au. The en prefix of the filename matches the language code in the paramspace language command. The identifier portion of the filename, _bacd_welcome.au, matches the name specified in the param welcome-prompt command.

- After the welcome prompt is played, the menu options audio file, en_bacd_options_menu.au, tells callers that they have the following options: “Press 1 if you know your party’s extension; press 2 for sales; press 3 for service.”

- A caller who dials 2 is connected to the hunt-group pilot number 1111. If all the phones in that hunt group are busy, the call is put into a queue for that hunt group. Up to 15 calls can be held in each queue. While the call is in the queue, it tries again every 15 seconds to reach a phone in the hunt group. The second-greeting message is played to the caller every 60 seconds while the call is in the queue. If the call is unable to connect to a phone in the hunt group after 700 seconds, the retry timer expires. The call is considered unanswerable and it is deleted from the queue.

- After the call leaves the call queue, it is sent to extension 5003, the alternate destination that is specified in the param voice-mail command. If this number is busy, the call tries twice more to connect with it. If the call is still unable to connect after the retries, the call disconnect prompt (en_bacd_disconnect.au) is played and the call is disconnected.

application

service queue flash:app-b-acd-2.1.0.0.tcl

param number-of-hunt-grps 2

param aa-hunt2 1111

param aa-hunt3 1222

param queue-len 15

param queue-manager-debugs 1

!

service aa flash:app-b-acd-aa-2.1.0.0.tcl

paramspace english index 1

paramspace english language en

paramspace english location flash:

param service-name queue

param handoff-string aa

param aa-pilot 8005550123

param welcome-prompt _bacd_welcome.au

param number-of-hunt-grps 2

param dial-by-extension-option 1

param second-greeting-time 60

param call-retry-timer 15

param max-time-call-retry 700

param max-time-vm-retry 2

param voice-mail 5003

!

dial-peer voice 222 voip

service aa

destination-pattern 8005550123

session target ipv4:192.168.1.1

incoming called-number 8005550123

dtmf-relay h245-alphanumeric

codec g711ulaw

no vad

### Embedded Call-Queue and AA Tcl Scripts: Example

The following example sets up the same single AA service, called app-b-acd-aa, and call-queue service, called app-b-acd, as in the previous example but uses embedded Tcl scripts. The service command specifies the location of the scripts. All other configuration and call flow is the same as in the previous example.

application

service app-b-acd

param number-of-hunt-grps 2

param aa-hunt2 1111

param aa-hunt3 1222

param queue-len 15

param queue-manager-debugs 1

!

service app-b-acd-aa

paramspace english index 1

paramspace english language en

paramspace english location flash:

param service-name app-b-acd

param handoff-string app-b-acd-aa

param aa-pilot 8005550123

param welcome-prompt _bacd_welcome.au

param number-of-hunt-grps 2

param dial-by-extension-option 1

param second-greeting-time 60

param call-retry-timer 15

param max-time-call-retry 700

param max-time-vm-retry 2

param voice-mail 5003

!

dial-peer voice 222 voip

service app-b-acd-aa

destination-pattern 8005550123

session target ipv4:192.168.1.1

incoming called-number 8005550123

dtmf-relay h245-alphanumeric

codec g711ulaw

no vad

## Monitoring and Maintaining Cisco Unified CME B-ACD Service

The following tasks may be used during ongoing operation of a Cisco Unified CME B-ACD service.

### Verif ying Cisco Unified CME B-ACD Status

Use the show call application sessions command to verify that Cisco Unified CME B-ACD is active.

The following example shows a session with active AA and call-queue applications. Note that the “App” field is the service name that was specified in the service command for the call-queue script in Step 4 and for the AA script in Step 10 in the “Setting Up Call-Queue and AA Services” section . The “Url” field is the location of the script file for the application.

Router# show call application sessions

Session ID 16

App: Default

Type: Service

Url: builtin:Session_Service.C

Session ID 4

App: Default

Type: Service

Url: builtin:Session_Service.C

Session ID 8

App: Default

Type: Service

Url: builtin:Session_Service.C

Session ID 17

App: aa

Type: Service

Url: flash:app-b-acd-aa-2.1.0.0.tcl

Session ID 12

App: queue

Type: Service

Url: flash:app-b-acd-2.1.0.0.tcl

The following example shows a session with only the queue application active. Note that the AA script does not appear in the output from the show call application sessions command because there are no active calls. The name of the AA service appears in the output only when there is an active call. The call-queue script activates after the first incoming call and stays active even if there are no active calls.

Router# show call application sessions

Session ID 4

App: Default

Type: Service

Url: builtin:Session_Service.C

Session ID 8

App: Default

Type: Service

Url: builtin:Session_Service.C

Session ID 12

App: queue

Type: Service

Url: flash:app-b-acd-2.1.0.0.tcl

### Upd ating Script Parameters and Audio Prompts

You can update Cisco Unified CME B-ACD script parameters by making changes to the Cisco IOS configuration that was described in the “How to Configure Cisco Unified CME B-ACD” section . For the parameter changes to take effect, you must stop and reload the Cisco Unified CME B-ACD scripts to which you have made changes as explained in the following steps. If you rerecord audio prompts, you must reload the audio prompt files that have changed.

### SUMMARY STEPS

1.	Determine the session IDs of any active sessions.

2.	Stop the B-ACD AA and call-queue service sessions if necessary.

3.	Reload the AA script and call-queue scripts.

4.	If an audio prompt file has been changed, reload it.

### DETAILED STEPS

Step 1 Determine the session IDs of any active sessions.

Use the show call application sessions command in privileged EXEC mode to obtain session ID (SID) numbers of AA and call-queue services. If the AA session has no active calls, the AA script name does not appear in the output from the show call application sessions command.

The following example shows a session with active calls. Note that the “App” field is the service name given to the call-queue script and AA script in Step 4 and Step 10 in the “Setting Up Call-Queue and AA Services” section . You can also see the service names in the output for the show running-config command.

Router# show call application sessions

Session ID 16

App: Default

Type: Service

Url: builtin:Session_Service.C

Session ID 4

App: Default

Type: Service

Url: builtin:Session_Service.C

Session ID 8

App: Default

Type: Service

Url: builtin:Session_Service.C

Session ID 17

App: aa

Type: Service

Url: flash:app-b-acd-aa-2.1.0.0.tcl

Session ID 12

App: queue

Type: Service

Url: flash:app-b-acd-2.1.0.0.tcl

Step 2	Stop the B-ACD AA and call-queue service sessions if necessary.

Using the session ID numbers from Step 1 , stop the Cisco Unified CME B-ACD AA service and call-queue service sessions. Use the call application session stop command in privileged EXEC mode to stop the AA and call-queue sessions. In the following example, the IDs are the SID numbers from the example in Step 1 .

Router# call application session stop id 17

Router# call application session stop id 12

When you use the call application session stop command for an AA service, the following actions occur:

- The AA service is stopped.

- All calls actively connected to the AA service are disconnected.

- The AA service name is removed from the output for the show call application sessions command.

Note To eliminate the possibility of disconnecting calls, you may prefer to wait until the calls are not coming in before reloading the script, such as after work hours.

If an AA service name does not appear in the output for the show call application sessions command, it means that there are no call sessions and you do not have to issue a call application session stop command for it.

Step 3 Reload the AA script and call-queue scripts.

Use the call application voice load command in privileged EXEC mode to reload the scripts.

Router# call application voice load aa

Router# call application voice load queue

Step 4	If an audio prompt file has been changed, reload it.

Use the audio-prompt load command in privileged EXEC mode to reload an audio file. Repeat this command for each audio file that has been changed.

Router# audio-prompt load flash:en_bacd_welcome.au

Reload of flash:en_bacd_welcome.au successful

### C ollecting Statistics

Several different types of statistics can help you determine whether your current Cisco Unified CME B-ACD service is meeting your call-coverage needs or whether some adjustment is necessary. Statistics collection is a two-step process: you first start the collection at the beginning of the statistics-collection period, and then you obtain the statistics at the end of the period. If the collection of normal hunt group statistics is interrupted, perhaps because of TFTP server failure, you can write out all the hunt group statistics for the past seven days.

Call statistics tasks are described in the following sections:

### Starting Statistics Collection

At the start of the period for which you want to collect statistics, you must enable the statistics collect command. A maximum of one week (168 hours) of statistics can be stored.

Statistics for different categories include:

- Direct Calls for the Hunt Group

–	average time for a call

–	average time a call spends on hold

- Direct Calls and Queued Calls for each Agent in the Hunt Group

–	average time in a call (direct calls)

–	average time a call is in the queue (queued calls)

–	total calls on hold (queued calls)

–	average hold time (queued calls)

–	longest hold time (queued calls)

- Queued Calls for the Hunt Group

–	total number of calls presented to the queue

–	average time a call was in the queue

–	longest time a call was in the queue

Note •	Each year on the day that daylight saving time adjusts the time back by one hour at 2 a.m., the original 1 a.m. to 2 a.m. statistics for that day are lost because they are overwritten by the new 1 a.m. to 2 a.m. statistics.

Note When you enable statistics collection, Cisco Unified CME captures a snapshot of what occurs during the requested time period. Events that occur before the start time of the collection period are not reflected in the report. See the section Obtaining Call Statistics for voice hunt group .

To display the collected statistics, see the Obtaining Call Statistics for ephone hunt group and Obtaining Call Statistics for voice hunt group .

To transfer statistics automatically to files using TFTP, see the “Obtaining Call Statistics Using TFTP” section .

### O btaining Call Statistics for ephone hunt group

To obtain call statistics, perform the following steps for ephone hunt group for which you want to capture statistics.

### Restrictions

If agents use Call Pickup to answer calls to a hunt group, instead of letting the B-ACD application handle the calls, call statistics are not captured correctly. Do not use Call Pickup to answer calls to hunt group phones if you want the call statistics to be accurately reported.

### SUMMARY STEPS

1. enable

2. configure terminal

3. ephone-hunt hunt-tag { longest-idle | peer | sequential }

4. statistics collect

5. end

6. show ephone-hunt [ tag ] statistics [ last hours hours | start day time [ to day time ]]

### DETAILED STEPS

Command or Action

Purpose

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

ephone-hunt hunt-tag { longest-idle | peer | sequential }

Router(config)# ephone-hunt 1 peer

Enters ephone-hunt configuration mode.

- For a description of the different types of hunt groups, see the “Setting Up Ephone Hunt Groups” section .

Step 4

statistics collect

Router(config-hunt-group)# statistics collect

Enables the collection of Cisco Unified CME B-ACD call statistics for an ephone hunt group.

Step 5

end

Router(config-hunt-group)# end

Returns to privileged EXEC mode.

Step 6

show ephone-hunt [ tag ] statistics [ last hours hours | start day time [ to day time ]]

Router# show ephone-hunt 1 statistics last 1 hours

Displays ephone-hunt configuration information and current status and statistic information.

- tag —(Optional) The hunt-tag number configured in the ephone-hunt command. Range is from 1 to 100.

- statistics —Displays statistical information.

- last hours hours—(Optional) Displays information for the previous number of specified hours, counting backward from the current hour. Range is 1 to 167.

- start—Output start time. Default duration is one hour.

- to —(Optional) Output stop time.

- day —Day of week. Use sun , mon , tue , wed , thu , fri , or sat .

- time —Hour of the day. Range is 0 to 23.

### O btaining Call Statistics for voice hunt group

To obtain call statistics, perform the following steps for voice hunt group for which you want to capture statistics.

### Restrictions

If agents use Call Pickup to answer calls to a hunt group, instead of letting the B-ACD application handle the calls, call statistics are not captured correctly. Do not use Call Pickup to answer calls to hunt group phones if you want the call statistics to be accurately reported.

### SUMMARY STEPS

1. enable

2. configure terminal

3. voice hunt-group hunt-tag { parallel | longest-idle | peer | sequential }

4. statistics collect

5. end

6. show voice hunt-group [ tag ] statistics [ last hours hours | start day time [ to day time ]]

### DETAILED STEPS

Command or Action

Purpose

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

voice hunt-group hunt-tag { parallel | longest-idle | peer | sequential }

Router(config)# voice hunt-group 1 peer

Enters voice hunt-group configuration mode.

- For a description of the different types of hunt groups, see the “Setting Up Voice Hunt Groups” section .

Step 4

statistics collect

Router(config-voice-hunt-group)# statistics collect

Enables the collection of Cisco Unified CME B-ACD call statistics for a voice hunt group.

Step 5

end

Router(config-voice-hunt-group)# end

Returns to privileged EXEC mode.

Step 6

show voice hunt-group [ tag ] statistics [ last hours hours | start day time [ to day time ]]

Router# show voice hunt-group 1 statistics last 1 hours

Displays voice hunt-group configuration information and current status and statistic information.

- tag —(Optional) The hunt-tag number configured in the voice hunt-group command. Range is from 1 to 100.

- statistics —Displays statistical information.

- last hours hours—(Optional) Displays information for the previous number of specified hours, counting backward from the current hour. Range is 1 to 167.

- start—Output start time. Default duration is one hour.

- to —(Optional) Output stop time.

- day —Day of week. Use sun , mon , tue , wed , thu , fri , or sat .

- time —Hour of the day. Range is 0 to 23.

### Examples

The section contains examples for collecting statistics for both ephone hunt group and voice hunt group.

The following example shows output from the show ephone-hunt [ tag ] statistics command. Note that in this example, the total calls answered by agents is more than the number of calls presented to the queue. This is because one call arrived before 13:00:00, which is when statistic collection started, but was not answered until after 13:00:00.

Router# show ephone-hunt 2 statistics last 1 hours

Tue 13:00 - 14:00

Max Agents: 3

Min Agents: 3

Total Calls: 9

Answered Calls: 7

Abandoned Calls: 2

Average Time to Answer (secs): 6

Longest Time to Answer (secs): 13

Average Time in Call (secs): 75

Longest Time in Call (secs): 161

Average Time before Abandon (secs): 8

Calls on Hold: 2

Average Time in Hold (secs): 16

Longest Time in Hold (secs): 21

Per agent statistics:

Agent: 8004

From Direct Call:

Total Calls Answered : 3:

Average Time in Call (secs) : 70

Longest Time in Call (secs) : 150

Total Calls on Hold : 1:

Average Hold Time (secs) : 21

Longest Hold Time (secs) : 21

From Queue:

Total Calls Answered : 3

Average Time in Call (secs) : 55

Longest Time in Call (secs) : 78

Total Calls on Hold : 2:

Average Hold Time (secs) : 19

Longest Hold Time (secs) : 26

Total logged in Time (secs) : 3000

Total logged out Time (secs) : 600

Agent: 8006

From Direct Call:

Total Calls Answered : 3:

Average Time in Call (secs) : 51

Longest Time in Call (secs) : 118

Total Calls on Hold : 1:

Average Hold Time (secs) : 11

Longest Hold Time (secs) : 11

From Queue:

Total Calls Answered : 1

Average Time in Call (secs) : 4

Longest Time in Call (secs) : 4

Total logged in Time (secs) : 3000

Total logged out Time (secs) : 600

Agent: 8044

From Direct Call:

Total Calls Answered : 1:

Average Time in Call (secs) : 161

Longest Time in Call (secs) : 161

From Queue:

Total Calls Answered : 1

Average Time in Call (secs) : 658

Longest Time in Call (secs) : 658

Total logged in Time (secs) : 3000

Total logged out Time (secs) : 600

Queue related statistics:

Total calls presented to the queue:  5

Calls answered by agents: 6

Number of calls in the queue:  0

Average time to answer (secs):  2

Longest time to answer (secs):  3

Number of abandoned calls:  0

Average time before abandon (secs):  0

Calls forwarded to voice mail:  0

The following example shows output from the show voice hunt-group [ tag ] statistics command for direct and queued calls.

Router# show voice hunt-group 1 statistics last 1 hours

Fri 01:00 - 02:00

Max Agents: 2

Min Agents: 2

Total Calls: 2

Answered Calls: 2

Abandoned Calls: 0

Average Time to Answer (secs): 3

Longest Time to Answer (secs): 6

Average Time in Call (secs): 8

Longest Time in Call (secs): 8

Average Time before Abandon (secs): 0

Calls on Hold: 2

Average Time in Hold (secs): 2

Longest Time in Hold (secs): 2

Per agent statistics:

Agent: 2001

From Direct Call:

Total Calls Answered : 1

Average Time in Call (secs) : 7

Longest Time in Call (secs) : 7

Total Calls on Hold : 1

Average Hold Time (secs) : 2

Longest Hold Time (secs) : 2

From Queue:

Total Calls Answered : 1

Average Time in Call (secs) : 10

Longest Time in Call (secs) : 10

Total Calls on Hold : 1

Average Hold Time (secs) : 2

Longest Hold Time (secs) : 2

Total logged in Time (secs) : 3000

Total logged out Time (secs) : 600

Agent: 2002

From Direct Call:

Total Calls Answered : 1

Average Time in Call (secs) : 8

Longest Time in Call (secs) : 8

Total Calls on Hold : 1

Average Hold Time (secs) : 2

Longest Hold Time (secs) : 2

From Queue:

Total Calls Answered : 1

Average Time in Call (secs) : 7

Longest Time in Call (secs) : 7

Total Calls on Hold : 1

Average Hold Time (secs) : 2

Longest Hold Time (secs) : 2

Total logged in Time (secs) : 3000

Total logged out Time (secs) : 600

Queue related statistics:

Total calls presented to the queue: 2

Calls answered by agents: 2

Number of calls in the queue: 0

Average time to answer (secs): 10

Longest time to answer (secs): 12

Number of abandoned calls: 0

Average time before abandon (secs): 0

Calls forwarded to voice mail: 0

Calls abandoned in less that 10 s: 0

Calls abandoned between 11 to 30 s: 0

Calls abandoned between 31 to 50 s: 0

Calls abandoned between 50 to 300 s: 0

Calls abandoned after 300 s: 0

Calls waited upto 10 s: 1

Calls waited between 11 to 30 s: 1

Calls waited between 31 to 50 s: 0

Calls waited between 50 to 300 s: 0

Calls waited more than 300 s: 0

Number of error calls: 0

The statistics collection must be active for each hunt group. Otherwise, there will be no statistics and the show ephone-hunt command and show voice hunt-group command will have nothing to display. If the statistics collect command is not issued for an ephone hunt group or a voice hunt group, an error message will occur.

An example for ephone hunt group:

Router# show ephone-hunt 1 stat last 1 h

Hunt Group 1 stat collect not enabled

An example for voice hunt group:

Router# show voice hunt-group 1 stat last 1 h

Hunt Group 1 stat collect not enabled

The show ephone-hunt and show voice hunt-group command is described in the Cisco Unified Communications Manager Express Command Reference. In addition to B-ACD data, this command provides hunt group information such as search method (parallel, longest idle, peer, or sequential), preference order, and the number to which unanswered calls were routed.

### Ob taining Call Statistics Using TFTP

To transfer statistics to a set of files using TFTP, you must do the following:

1.	Create a group of files to which the statistics will be sent.

2.	Enable statistics collection for the desired hunt groups.

3.	Configure the statistics-gathering parameters.

You can create up to 201 files to which statistics can be sent, and you can configure the intervals in which the statistics are collected. The files must be blank, read-and-write files. The filename extension does not matter. The data transfer mechanism searches for files with a prefix and numeric suffix that match the parameters configured in the hunt-group report url command. For example, for the configuration that requires that a file start with “data” and end with a numeric range of 0 to 9, you must have a set of files named data1, data2, ... data9. For a suffix range of 1 to 30, you must have a set of files named data01, data02, ... data30. For a suffix range of 1 to 100, you must have a set of files named data001, data002, ... data100.

The location of the files must match the directory configured in the hunt-group report url command. For example, if the file location were configured to be tftp://239.1.1.1/dirname1/dirname2/filename, the files would have to be located in dirname1/dirname2.

To configure how and when statistics are transferred, you must use the hunt-group report url command to name the files to which the data is transferred and the hunt-group report every hours command to set the intervals of time at which the statistics are collected. The statistics are sent every n hour(s) with the hunt-group report every hours command. (The range for n is from 1 to 84.) For example, if you configure hunt-group report every 2 hours , statistics are sent to a file every two hours.

The time interval of the hunt-group report every hours command is based on the time at which you initially enable the command or you enable the statistics collect command. If you change the value of the hunt-group report every hours command, you must disable the statistics collect command and enable it again before the new timestamp is set. Otherwise, the system uses the timestamp that was set when you originally enabled the command.

For example, if you enable the hunt-group report every 1 hour command at 2 p.m., and then you change it to hunt-group report every 2 hours at 2:30 p.m., TFTP collects the statistics at 4 p.m. (two hours from the time when you originally set the hunt-group report every hours command). The timestamp is not updated until you disable and re-enable the statistics collect command.

You can also configure statistics collection to begin one or more hours later with the hunt-group report delay hours command. The reason that you may want to delay data collection is that calls are counted when they end.

For example, if there is a call from 1:35 p.m. to 3:30 p.m., the interval is every 1 hour, and there is no delay, TFTP will write the 1 p.m. to 2 p.m. statistics at 3 p.m. However, at 3 p.m., the 1:35 p.m. call is still active, so the call will not be counted at that time as occurring in the 1 p.m. to 2 p.m. time slot. When the call finishes at 3:30 p.m., it will then be counted as occurring from 1 p.m. to 2 p.m. The show ephone-hunt or show voice hunt-group command will report it, but TFTP will have already sent out its report. To include the 1:35 p.m. call, you could use the hunt-group report delay hours command to delay TFTP statistics reporting for an extra hour so that the 1 p.m. to 2 p.m. report will be written at 4 p.m. instead of at 3 p.m.

The following is an example of the statistics that are sent to a file:

04:00:00 UTC Thu Mar 15 2007,

,

02, Thu 02:00 - 03:00, HuntGp, 03, 03, 00009, 00007, 00002, 0006, 0013, 000075, 000161, 0008, 00002, 000016, 000021,

02, Thu 02:00 - 03:00, Agent, 8004, 00003, 000070, 000150, 00001, 000021, 000021, 00003, 000055, 000078, 00002, 000019, 000026,

02, Thu 02:00 - 03:00, Agent, 8006, 00003, 000051, 000118, 00001, 000011, 000011, 00001, 000004, 000004, 00000, 000000, 000000,

02, Thu 02:00 - 03:00, Agent, 8044, 00001, 000161, 000161, 00000, 000000, 000000, 00001, 000658, 000658, 00000, 000000, 000000,

02, Thu 02:00 - 03:00, Queue, 00005, 00005, 00000, 00002, 00003, 00000, 00000, 00000, 00000,

These statistics can be sent to an application such as Microsoft Access or Microsoft Excel, so they can be merged into a chart or graph for easier reading. The TFTP statistics correspond to the show ephone-hunt or show voice hunt-group output as follows:

04:00:00 UTC Thu Mar 15 2007, ;This is the time that the data was collected

,

02, Thu 02:00 - 03:00, HuntGp, ;Thu 02:00 - 03:00

03     ;Max Agents:3

03     ;Min Agents:3

00009  ;Total Calls:9

00007  ;Answered Calls:7

00002  ;Abandoned Calls:2

0006   ;Average Time to Answer [secs]:6

0013   ;Longest Time to Answer [secs]:13

000075 ;Average Time in Call [secs]:75

000161 ;Longest Time in Call [secs]:161

0008   ;Average Time before Abandon [secs]:8

00002  ;Total Calls on Hold:2

000016 ;Average Hold Time [secs]:16

000021 ;Longest Hold Time [secs]:21

02, Thu 02:00 - 03:00, Agent, 8004,

00003  ;From direct call: Total calls answered :3:

000070 ;From direct call: Average Time in Call [secs] :70

000150 ;From direct call: Longest Time in Call [secs] :150

00001  ;From direct call: Total Calls on Hold :1:

000021 ;From direct call: Average Hold Time (secs) :21

000021 ;From direct call: Longest Hold Time (secs) :21

00003  ;From queue: Total calls answered :3:

000055 ;From queue: Average Time in Call [secs] :55

000078 ;From queue: Longest Time in Call [secs] :78

00002  ;From queue: Total Calls on Hold :2:

000019 ;From queue: Average Hold Time (secs) :19

000026 ;From queue: Longest Hold Time (secs) :26

02, Thu 02:00 - 03:00, Agent,8006,

00003  ;From direct call: Total calls answered :3:

000051 ;From direct call: Average Time in Call [secs] :51

000118 ;From direct call: Longest Time in Call [secs] :118

00001  ;From direct call: Total Calls on Hold :1:

000011 ;From direct call: Average Hold Time (secs) :11

000011 ;From direct call: Longest Hold Time (secs) :11

00001  ;From queue: Total calls answered :1:

000004 ;From queue: Average Time in Call [secs] :4

000004 ;From queue: Longest Time in Call [secs] :4

00000  ;From queue: Nothing appeared in the show output because no calls were answered

000000 ;From queue: Nothing appeared in the show output because no calls were answered

000000 ;From queue: Nothing appeared in the show output because no calls were answered

02, Thu 02:00 - 03:00, Agent,8044,

00001  ;From direct call: Total calls answered :1:

000161 ;From direct call: Average Time in Call [secs] :161

000161 ;From direct call: Longest Time in Call [secs] :161

00000  ;From queue: Nothing appeared in the show output because no calls were answered

000000 ;From queue: Nothing appeared in the show output because no calls were answered

000000 ;From queue: Nothing appeared in the show output because no calls were answered

00001  ;From queue: Total calls answered :1:

000658 ;From queue: Average Time in Call [secs] :658

000658 ;From queue: Longest Time in Call [secs] :658

00000  ;From queue: Nothing appeared in the show output because no calls were answered

000000 ;From queue: Nothing appeared in the show output because no calls were answered

000000 ;From queue: Nothing appeared in the show output because no calls were answered

02, Thu 02:00 - 03:00, Queue,

00005  ;Total calls presented to the queue:5

00005  ;Calls answered by agents: 5

00000  ;Calls exited the queue: 0

00002  ;Average time to answer [secs]: 2

00003  ;Longest time to answer [secs]: 3

00000  ;Number of abandoned calls: 0

00000  ;Average time before call abandoned (secs): 0

00000  ;Calls forwarded to voice mail: 0

To obtain call statistics using TFTP, perform the following steps for each ephone hunt group (or voice hunt group) for which you want to collect statistics.

### SUMMARY STEPS

1. enable

2. configure terminal

3. ephone-hunt hunt-tag ( voice hunt-group hunt-tag)

4. statistics collect

5. exit

6. telephony-service

7. hunt-group report url [ prefix tftp:// ip-address / directory-name... / prefix | suffix from-number to to-number ]

8. hunt-group report every number hours

9. hunt-group report delay number hours

10. exit

### DETAILED STEPS

Command or Action

Purpose

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

ephone-hunt hunt-tag

voice hunt-group hunt-tag

Router(config)# ephone-hunt 1

Router(config)# voice hunt-group 1

Enters ephone-hunt (or voice hunt-group) configuration mode.

- hunt-tag —Unique sequence number that identifies this hunt group during all configuration tasks. Range is from 1 to 100.

Step 4

statistics collect

Router(config-hunt-group)# statistics collect

Enables the collection of Cisco Unified CME B-ACD statistics data for an ephone hunt group.

Step 5

exit

Router(config-hunt-group)# exit

Exits ephone-hunt configuration mode.

Step 6

telephony-service

Router(config)# telephony-service

Enters telephony-service configuration mode.

Step 7

hunt-group report url [ prefix tftp:// ip-address / directory-name... / prefix | suffix from-number to to-number ]

Router(config-telephony)# hunt-group report url prefix tftp://239.1.1.1/dirname1/dirname2/data

Router(config-telephony)# hunt-group report url suffix 0 to 100

Sets filename parameters and the URL path where call data is to be sent using TFTP.

Note The hunt-group report url prefix command and the hunt-group report url suffix command must both be configured.

- prefix —(Optional) Sets the parameters for how the filenames must start.

- tftp:// ip-address / —(Optional) IP address to the files where AA call data is sent using TFTP.

- directory-name... / —(Optional) Names of directories separated by forward slashes (/) to declare the path to the files where AA call data is sent.

- prefix —(Optional) Declares parameters for how the filenames must start.

- suffix —(Optional) Sets numeric parameters for how the filenames must end.

- from-number —(Optional) Number at which the suffix range starts. The range is from 0 to 1. There is no default.

- to to-number —(Optional) Number at which the suffix range ends. The range is from 1 to 200. There is no default.

Step 8

hunt-group report every number hours

Router(config-telephony)# hunt-group report every 2 hours

Sets the hourly interval at which Cisco Unified CME B-ACD call statistics are collected for a report.

- number —Number of hours for which AA call data is collected and reported. The range is from 1 to 84.

Step 9

hunt-group report delay number hours

Router(config-telephony)# hunt-group report delay 2 hours

(Optional) Delays the stop time configured with the hunt-group report every hours command and continues to collect Cisco Unified CME B-ACD overflow call statistics.

- number —Number of hours for which data collection can be extended for the data collection periods configured with the hunt-group report every hours command. The range is from 1 to 10.

Step 10

exit

Router(config-telephony)# exit

Exits telephony-service configuration mode.

### Examples

The following example sets up the hunt-group report mechanism to use TFTP to send call statistics every three hours to the files named data000, data002, ... data200, located at the 239.10.10.10 IP address under dirname1/dirname2. No delay has been configured.

telephony-service

hunt-group report url prefix tftp://239.10.10.10/dirname1/dirname2/data

hunt-group report url suffix 0 to 200

hunt-group report every 3 hours

The following is an example of a report that the previous configuration might send to a file if the statistics collect command was entered at 18:20:

22:00:00 UTC Tue Dec 20 2004,

,

01, Tue 18:00 - 19:00, HuntGp, 02, 01, 00005, 00002, 0003, 0006, 000001, 000001, 0011,

01, Tue 19:00 - 20:00, HuntGp, 02, 02, 00000, 00000, 0000, 0000, 000000, 000000, 0000,

01, Tue 20:00 - 21:00, HuntGp, 02, 02, 00006, 00003, 0003, 0009, 000001, 000003, 0012,

Statistics collection has to take place for at least three hours for the statistics to be written to a file. The following is a chronology of events:

- At 19:00, the statistics collection was active for 40 minutes, so no statistics were written to file.

- At 20:00, the statistics collection was active for 1 hour and 40 minutes, so no statistics were written to file.

- At 21:00, the statistics collection was active for 2 hours and 40 minutes, so no statistics were written to file.

- At 22:00, the statistics collection was active for 3 hours and 40 minutes, so statistics were written to a file using TFTP.

If the previous example were configured for a delay of one hour using the hunt-group report delay 1 hours command, the statistics would be written one hour later at 23:00.

### W riting Out Statistics for Ephone Hunt and Voice Hunt Group When Normal Collection is Interrupted

The hunt-group statistics write-all command writes out in hourly increments all the ephone hunt group and voice hunt group statistics for the past seven days. This command is intended be used when normal hunt group statistics collection is interrupted, perhaps due to TFTP server failure. Use this command when the connection to your TFTP server is restored after a long down-time to capture statistics from that period.

The hunt-group statistics write-all command writes out the whole statistics buffer at one time (24 hours a day for 7 days). You do not have to enable statistics collection to use this feature. Statistics are written out starting from the current time. For example, if the command is used at 9:30 a.m. on Monday, statistics are written out from Mon 9:00 - 10:00, Mon 10:00 - 11:00, and so forth, finally to Mon 8:00 - 9:00. The data and formatting for the reports generated by this command are identical to the reports that are written to file using TFTP, which is described in the “Obtaining Call Statistics Using TFTP” section .

As mentioned, the hunt-group statistics write-all command is intended for use during interruptions to normal statistics collection. The commands that provide normal statistics collection allow you to specify shorter, more precise reporting periods and file-naming conventions. These commands are described in the “Starting Statistics Collection” section , the “Obtaining Call Statistics for ephone hunt group” section , and the “Obtaining Call Statistics Using TFTP” section .

### SUMMARY STEPS

1. enable

2. hunt-group statistics write-all location

### DETAILED STEPS

Command or Action

Purpose

Step 1

enable

Router> enable

Enables privileged EXEC mode.

- Enter your password if prompted.

Step 2

hunt-group statistics write-all location

Router# hunt-group statistics write-all flash:huntstats

Writes ephone-hunt statistics information to a file.

- location —The URL or filename to which the statistics should be written.

### Examples

The following example writes the ephone hunt (and voice hunt group) statistics buffer to a file in flash called “huntstats.” See the hunt-group report url command for explanations of the output fields.

Router# hunt-group statistics write-all flash:huntstats

Writing out all hunt statistics to tftp now.

11:13:58 UTC Fri Mar 11 2016,

, 01, Fri 11:00 - 12:00, HuntGp, 01, 01, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,

01, Fri 12:00 - 13:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,

01, Fri 13:00 - 14:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,

01, Fri 14:00 - 15:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,

01, Fri 15:00 - 16:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,

.

.

### T ro ubleshooting Tips for Cisco Unified CME B-ACD

- Use the debug voip application script command to display debugging messages for the AA script. Note that you must first enable the collection of call-queue data from the Cisco Unified CME B-ACD call-queue script using the param queue-manager-debug s command. See Step 8 in the “Setting Up Call-Queue and AA Services” section .

- To remove an AA service from a dial peer, issue the no service command under the dial peer associated with the AA. See the “Setting Up Incoming Dial Peers for AA Pilot Numbers” section .

- To stop the AA script, use the call application session stop command. See the “Updating Script Parameters and Audio Prompts” section .

## C onfiguration Examples

This section contains the following examples:

### Cisco Unified CME B-ACD with One AA: Example

The following configuration is for a Cisco Unified CME B-ACD service with two hunt group menu options. When callers press 3, they will be transferred to the pilot number for hunt group 1; pressing 4 transfers callers to the pilot number for hunt group 2. When callers press 5, they will be transferred to the pilot number for hunt group 3; pressing 5 transfers callers to the pilot number for hunt group 4.

The AA pilot number to the Cisco Unified CME B-ACD AA script is 800 555-0100. Hunt group 1 supports four directory numbers ( list 1001...1004 command); hunt group 2 supports ten directory numbers ( list 2001...2010 command). Hunt group 3 supports four directory numbers (list 3001...3004 command); hunt group 4 supports ten directory numbers (list 4001...4010 command).Each of set of hunt group’s directory numbers are overlaid on button 1 and button 2 on phones 1 to 28.

If callers press 7, they will be permitted to enter their extension directly. If 3 is pressed, the call will go to hunt group pilot number 1111 (and then go to one of hunt group 1’s directory numbers). If 4 is pressed, the call will go to hunt group pilot number 2222 (and then go to one of hunt group 2’s directory numbers). If 5 is pressed, the call will go to hunt group pilot number 3333 (and then go to one of hunt group 3’s directory numbers). If 6 is pressed, the call will go to hunt group pilot number 4444 (and then go to one of hunt group 4’s directory numbers). Directory numbers are selected by their availability and by the search methods used by each hunt group. For this example, calls to hunt group 1 will go to the available directory number that has been idle for the longest ( ephone-hunt 1 longest-idle or voice hunt-group 1 longest-idle command).

If callers press 3,4,5, or 6, their calls will be transferred to the corresponding hunt group’s call queue. In this example, each hunt group is configured to have up to ten calls in its individual queues. If all of the directory numbers are unavailable, the calls will wait in queues and try to transfer to the hunt group pilot numbers every 15 seconds. As they are waiting, they will hear a second greeting every 60 seconds. After 600 seconds have elapsed, they will be sent to voice mail (5000). If voice mail is busy, the call will attempt twice more to reach voice mail after 15-second intervals. If voice mail is still unavailable, the caller will hear a busy signal.

Because the directory numbers in this example are overlaid (for example, button 1o1,2,3,4 ), calls that go through will ring on all available phones configured with the available directory numbers.

Note The hunt group automatic logout feature is not available for this example because the ephone-dns in this example are shared.

dial-peer voice 1000 pots

service aa

incoming called-number 8005550100

port 1/0:23

#If ephone hunt groups needs to be configured, use the following steps:

ephone-dn 1

number 1001

.

.

.

ephone-dn 4

number 1004

ephone-dn 5

number 2001

.

.

.

ephone-dn 14

number 2010

ephone 1

mac-address 1111.1111.1111

button 1o1,2,3,4

ephone 4

mac-address 2222.2222.2222

button 1o1,2,3,4

ephone 5

mac-address 4444.4444.4444

button 1o5,6,7,8,9

button 2o10,11,12,13,14

.

.

.

ephone 14

mac-address 1414.1414.1414

button 1o5,6,7,8,9

button 2o10,11,12,13,14

ephone-hunt 1 longest-idle

pilot 1111

list 1001,1002,1003,1004

timeout 10

ephone-hunt 2 longest-idle

pilot 2222

list 2001,2002,2003,2004,2005,2006,2007,2008,2009,2010

timeout 10

#If voice hunt groups needs to be configured, use the following steps (If you are configuring both ephone hunt group and voice hunt group, the ephone hunt pilot and voice hunt pilot should be different.):

voice register dn 1

number 3001

.

.

.

voice register dn 4

number 3004

voice register dn 5

number 4001

.

.

.

voice register dn 14

number 4010

voice register pool 1

id mac 1111.1111.1111

number 1 dn 1

voice register pool 4

id mac 2222.2222.2222

number 1 dn 4

voice register pool 5

id mac 4444.4444.4444

number 1 dn 5

.

.

.

voice register pool 14

id mac 1414.1414.1414

number 1 dn 14

voice hunt-group 1 longest-idle

pilot 3333

list 3001,3004

timeout 10

voice hunt-group 2 longest-idle

pilot 4444

list 4001,4010

timeout 10

application

service queue flash:app_b_acd_x.x.x.x.tcl        ;Defines the service-name of the

;the call-queue script as “queue.”

param queue-len 10                              ;Declares the queue length per

;hunt group.

param aa-hunt3 1111                             ;Declares menu option 3 and associates

;it with the hunt group pilot

;number 1111.

param aa-hunt4 2222

param number-of-hunt-grps 2                     ;Number of hunt-group menu options.

param queue-manager-debugs 1                    ;Enables collection of call statistics

;for debugging.

service aa flash:app_b_acd_aa_x.x.x.x.tcl        ;Defines the service name of

;the AA script as “aa.”

paramspace english location flash:              ;Declares use of English package

;and location of audio files.

paramspace english index 1                      ;Defines category 1 for English.

paramspace english language en                  ;Specifies language code to be en.

param aa-pilot 8005550100                       ;Access number to Cisco Unified CME                                                     ;B-ACD.

param call-retry-timer 15                       ;Time interval in which call in queue

;can attempt to access available

;directory numbers and voice mail.

param second-greeting-time 60                   ;Delay before second greeting is played.

param max-time-call-retry 600                   ;Maximum time calls can wait in queue.

param max-time-vm-retry 2                       ;Maximum time calls can attempt to be

;transferred to voice mail.

param service-name queue                        ;Associates AA script with queue script.

param dial-by-extension-option 5                ;Declares menu option number for

;extension dial.

param voice-mail  5000                          ;Declares B-ACD alternate destination.

param number-of-hunt-grps 2                     ;Declares the number of hunt

;group menu options.

param handoff-string aa                         ;Passes AA name to queue script.

### Cisco Unified CME B-ACD with Drop-Through Option: Example

The following example sets parameters for an AA service called aa and a call-queue service called callq. The direct-dial number to reach the AA service is 800 555-0100. Callers to this number drop through to the hunt group that has a pilot number of 5071 (6071 for voice hunt group) after hearing the initial prompt from the file en_dt_prompt.au.

dial-peer voice 1000 pots

service aa

port 1/1/0

incoming called-number 8005550100

#If ephone hunt groups needs to be configured, use the following steps:

ephone-hunt 10 sequential

pilot 5071

list 5011, 5012, 5013, 5014, 5015

timeout 10

#If voice hunt groups needs to be configured, use the following steps (If you are configuring both ephone hunt group and voice hunt group, the ephone hunt pilot and voice hunt pilot should be different.):

voice hunt-group 10 sequential

pilot 6071

list 6011, 6012, 6013, 6014, 6015

timeout 10

application

service callq tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl

param queue-manager-debugs 1

param aa-hunt1 5071

param number-of-hunt-grps 1

param queue-len 10

service aa tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl

paramspace english location tftp://192.168.254.254/user1/prompts/

paramspace english index 0

paramspace english language en

param aa-pilot 8005550100

param number-of-hunt-grps 1

param service-name callq

param handoff-string aa

param second-greeting-time 60

param drop-through-option 1

param drop-through-prompt _dt_prompt.au

param call-retry-timer 15

param max-time-call-retry 700

param voice-mail 5000

param max-time-vm-retry 2

### Cisco Unified CME B-ACD with Two AAs Set Up for Drop-Through Option: Example

The following example shows two AA services, both of which are configured in drop-through mode. Callers who dial 800 555-0121 reach the first AA service, named acdaa, and hear a welcome prompt before they drop through to the call queue for ephone hunt group 11. Callers to 800 555-0123 reach the second AA service, named aa-bcd, and directly drop through to the call queue for ephone hunt group 10. Both AA services are handled by the same call-queue service, which is named callq.

dial-peer voice 1010 pots

service acdaa

port 1/1/0

incoming called-number 8005550121

dial-peer voice 1020 pots

service aa-bcd

port 1/1/1

incoming called-number 8005550123

#If ephone hunt groups needs to be configured, use the following steps:

ephone-hunt 10 sequential

pilot 5071

list 5011, 5012, 5013, 5014, 5015

timeout 10

ephone-hunt 11 sequential

pilot 5072

list 5021, 5022, 5023, 5024, 5025

timeout 10

#If voice hunt groups needs to be configured, use the following steps (If you are configuring both ephone hunt group and voice hunt group, the ephone hunt pilot and voice hunt pilot should be different.):

voice hunt-group 10 sequential

pilot 6071

list 6011, 6012, 6013, 6014, 6015

timeout 10

voice hunt-group 11 sequential

pilot 6072

list 6021, 6022, 6023, 6024, 6025

timeout 10

application

service callq tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl

param queue-manager-debugs 1

param aa-hunt1 5071

param aa-hunt2 5072

param number-of-hunt-grps 2

param queue-len 10

!

service acdaa tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl

paramspace english location tftp://192.168.254.254/user1/prompts/

paramspace english index 0

paramspace english language en

param aa-pilot 8005550121

param service-name callq

param max-time-vm-retry 2

param voice-mail 5007

param call-retry-timer 10

param number-of-hunt-grps 1

param drop-through-prompt _bacd_welcome.au

param drop-through-option 2

param acdaa second-greeting-time 60

param handoff-string acdaa

param max-time-call-retry 60

!

service aa-bcd tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl

paramspace english location tftp://192.168.254.254/user1/prompts/

paramspace english index 0

paramspace english language en

param aa-pilot 8005550123

param service-name callq

param second-greeting-time 60

param max-time-call-retry 180

param max-time-vm-retry 2

param voice-mail 5007

param call-retry-timer 5

param handoff-string aa-bcd

param drop-through-option 1

param number-of-hunt-grps 1

### Cisco Unified CME B-ACD with Multiple AAs and Drop-Through Option: Example

The following extended example demonstrates a Cisco Unified CME site with three AA services, two of which use drop-through mode.

- XYZ Inc. has three AA services (AA1, AA2, and AA3). Each AA is reached by a telephone number that callers dial: AA1 is 800 555-0111, AA2 is 800 555-0122, and AA3 is 800 555-0133. The services are assigned to dial peers as follows:

dial-peer voice 1000 pots

service AA1

port 1/1/0

incoming called-number 8005550111

dial-peer voice 1002 pots

service AA2

port 1/1/1

incoming called-number 8005550122

dial-peer voice 1003 pots

service AA3

port 1/1/2

incoming called-number 8005550133

- Five ephone hunt groups are set up to receive calls from the call-queue service as follows:

ephone-hunt 10 sequential

pilot 1001

list 1011, 1012, 1013, 1014, 1015

timeout 10

ephone-hunt 11 sequential

pilot 2001

list 2011, 2012, 2013, 2014, 2015

timeout 10

ephone-hunt 12 sequential

pilot 3001

list 3011, 3012, 3013, 3014, 3015

timeout 10

ephone-hunt 13 sequential

pilot 4001

list 4011, 4012, 4013, 4014, 4015

timeout 10

ephone-hunt 14 sequential

pilot 5001

list 5011, 5012, 5013, 5014, 5015

timeout 10

If you are using voice hunt group, five voice hunt groups are set up to receive calls from the call-queue service as follows (If you are configuring both ephone hunt group and voice hunt group, the ephone hunt pilot and voice hunt pilot should be different.):

voice hunt-group 10 sequential

pilot 1501

list 1511, 1512, 1513, 1514, 1515

timeout 10

voice hunt-group 11 sequential

pilot 2501

list 2511, 2512, 2513, 2514, 2515

timeout 10

voice hunt-group 12 sequential

pilot 3501

list 3511, 3512, 3513, 3514, 3515

timeout 10

voice hunt-group 13 sequential

pilot 4501

list 4511, 4512, 4513, 4514, 4515

timeout 10

voice hunt-group 14 sequential

pilot 5501

list 5511, 5512, 5513, 5514, 5515

timeout 10

- A call-queue service called CQ is set up to work with the three AA services and five hunt groups.

application

service CQ tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl

param queue-manager-debugs 1

param aa-hunt1 1001

param aa-hunt2 2001

param aa-hunt3 3001

param aa-hunt4 4001

param aa-hunt5 5001

param number-of-hunt-grps 5

param queue-len 10

- The first AA service, AA1, is associated with the incoming called number 800 555-0111. AA1 is not configured with drop-through mode. When customers dial 800 555-0111 they hear the welcome prompt that was recorded in the audio file en_bacd_welcome.au: “Thank you for calling XYZ Inc.” The prompt containing the menu options was recorded in the audio file called en_bacd_options_menu.au: “Press 1 for sales, press 2 for service, press 0 for the operator.” Note that there is no explicit command to specify the name of the menu options audio file because this file is always played in all B-ACD services that are not drop-through services. After pressing a digit, a caller hears MOH until connected to an agent.

service AA1 tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl

paramspace english location tftp://192.168.254.254/user1/prompts/

paramspace english index 0

paramspace english language en

param aa-pilot 8005550111

param number-of-hunt-grps 3

param service-name CQ

param welcome-prompt _bacd_welcome.au

param handoff-string AA1

- The second AA service, AA2, is associated with the incoming called number 800 555-0122. AA2 is configured with drop-through mode and no initial prompt. When customers dial 800 555-0122, they hear ringback if an agent is available and MOH if no agent is available.

service AA2 tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl

paramspace english location tftp://192.168.254.254/user1/prompts/

paramspace english index 0

paramspace english language en

param aa-pilot 8005550122

param number-of-hunt-grps 1

param service-name CQ

param drop-through-option 4

param handoff-string AA2

- The third AA service, AA3, is associated with the incoming called number 800 555-0133. AA3 is configured with drop-through mode and an initial prompt. When callers dial 800 555-0133, they hear the initial prompt, which tells them “Thank you for calling XYZ Inc. An agent will be with you shortly.” If an agent is available, callers hear ringback. If no agent is available, they hear MOH.

service AA3 tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl

paramspace english location tftp://192.168.254.254/user1/prompts/

paramspace english index 0

paramspace english language en

param aa-pilot 8005550133

param number-of-hunt-grps 1

param service-name CQ

param drop-through-option 5

param drop-through-prompt _dt_prompt.au

param handoff-string AA3

| Default Filename | Default Announcement | Length of Default Announcement |
|---|---|---|
| e n_bacd_welcome.au | “Thank you for calling.” Includes a two-second pause after the message. | 3 seconds |
| e n_bacd_options_menu.au | “For sales press 1 (pause), for customer service press 2 (pause), to dial by extension press 3 (pause), to speak to an operator press zero.” Includes a four-second pause after the message. | 15 seconds |
| e n_bacd_disconnect.au | “We are unable to take your call at this time. Please try again at a later time. Thank you for calling.” Includes a four-second pause after the message. | 10 seconds |
| e n_bacd_invalidoption.au | “You have entered an invalid option. Please try again.” Includes a one-second pause after the message. This prompt is played when a caller chooses an invalid menu option or dials an invalid extension. | 7 seconds |
| e n_bacd_enter_dest.au | “Please enter the extension number you want to reach.” Includes a five-second pause after the message. This prompt is played when a caller chooses the dial-by-extension option. | 7 seconds |
| e n_bacd_allagentsbusy.au | “All agents are currently busy assisting other customers. Continue to hold for assistance. Someone will be with you shortly.” Includes a two-second pause after the message. This prompt is also known as the second greeting. | 7 seconds |
| e n_bacd_music_on_hold.au | Music on hold (MOH) is played to Cisco Unified CME B-ACD callers. | 60 seconds |

| Filename | Name Specification | How Used |
|---|---|---|
| e n_welcome_prompt.au | Filename can be changed; must match the name specified in the param welcome-prompt command. To change the language prefix or identifier part of the filename, follow the guidelines in the “Changing Language Codes and Filenames” section . | Default is “Thank you for calling.” When you have a single AA service, use this audio file to record a customized greeting. When you have multiple AAs, use this audio file to record a customized greeting and menu options for customers to use. |
| e n_bacd_options_menu.au | Only the language prefix can be changed; the identifying part of the filename must remain the same. | Default is “For sales press 1, (pause) for customer service press 2 (pause), to dial by extension press 3 (pause), to speak to an operator press zero.” When you have a single AA service, use this audio file to record menu options for customers. When you have multiple AAs, record silence in this file. A minimum of one second of silence must be recorded. |

| Type | Description | Requirements | Example |
|---|---|---|---|
| Hunt group | Caller presses a specified digit to be connected to a group of extensions that has been designated a hunt group. If all extensions in the hunt group are busy, calls are held in a call queue or sent to an alternate, configurable destination. | A hunt group must be established. | After dialing the number for a computer store, a caller presses 1 to be connected to a hunt group that consists of phones in the sales department, or presses 2 to be connected to the hunt group for technical support, 3 to be connected to the hunt group for billing questions, or 0 to be connected to the operator hunt group. |
| O perator hunt group | Special case of hunt group; caller presses a specified digit or 0 to be connected to a hunt group with the special purpose of providing operator, or lookup and connection, services to callers. | A hunt group to provide operator services must be established. |
| D ial-by-extension | Caller presses a digit to be allowed to dial a known extension. Note The menu number used for this option must not be the same as any menu (aa-hunt) numbers used with the call-queue service. | No requirements. | After hearing the menu choices, a caller dials 4 and is able to dial an internal extension number. |
| D rop-through mode | Caller is directly connected to a hunt group, following the playing of an optional welcome prompt if one is specified. Note When drop-through mode is assigned to an AA, it is the only option for that AA. If you want some callers to get drop-through treatment and others to be able to make menu choices, you must set up multiple AAs. | Cisco CME 3.2.1 or a later version must be used. A hunt group must be established. | A caller dials a special toll-free number for online sales at the computer store and hears a recording (“Thank you for calling. An agent will be with you shortly.”). The caller is put directly through to the online-sales hunt group if an agent is available to take the call or is put in a call queue for the hunt group if all agents are busy. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Select a name to use for the call-queue service. | During configuration, the call-queue service name is used in the commands that pertain to the call-queue service. There is only one call-queue service for a Cisco Unified CME B-ACD. You can use any name. |
| Step 2 | Decide whether more than one AA application is needed. | If you want some callers to have different menu options than other callers, set up multiple AA applications. For instance, you might want some callers to be directly connected to a hunt group, and you might want other callers to have the option of dialing an extension or choosing among several hunt groups. For more information about multiple AAs, see the “Cisco Unified CME B-ACD Components” section . |
| Step 3 | Select a name and pilot number to use for each AA application. | During configuration, the AA application name is used to specify that certain commands pertain to an AA application. You can use any name, and you need a different name for each AA that you define. Each AA needs its own pilot number, which must be reachable from outside the Cisco Unified CME system. |
| Step 4 | Select the number and type of call-routing (menu) options to offer callers for each AA application. | For each AA application, decide what options to offer callers and what hunt groups you will use. You can designate that an AA application will operate in interactive mode, in which callers make active choices on the basis of the menu choices that you offer. By pressing the specified digit, a caller can take any of the following actions: Connect to a hunt group. Connect to an operator hunt group. Dial a known extension. Alternatively, you can designate that an AA application will operate in drop-through mode, in which calls are directly sent to a hunt group without giving callers the opportunity to make choices. There is one call-queue service per B-ACD, which can handle up to ten hunt groups. Each AA application can handle up to three hunt groups, in addition to a shared operator hunt group. For more information, see the “Menu Options” section and the “Hunt Group Option, Ephone Hunt Groups, and Voice Hunt Groups” section . |
| Step 5 | Decide on the wording for your customized prompts. | Each default audio prompt from the Cisco Unified CME Software Download website can be rerecorded with custom information for your application. Plan the wording that you want to use for each prompt. For more information, see the “Welcome Prompt and Other Audio Files” section . |
| Step 6 | Decide on the call-retry parameters that you want to set. | You can change the defaults for the following values: Second-greeting time—Amount of time before a second greeting is played or replayed to callers in call queues. Default is 60 seconds. Call-retry—Amount of time before a call in queue tries again to transfer to the hunt group. Default is 15 seconds. Maximum call-retry timer—Amount of time before a call in queue is considered unanswered because all retry attempts to connect to the hunt group have failed. Default is 600 seconds. Alternate destination retries—Number of times that a call in queue attempts to contact an alternate destination number before it is disconnected. Default is 1 time. For more information, see the “Call Queues” section . |
| Step 7 | Choose an alternate destination for calls that are unanswered because a hunt group is unavailable or because the maximum call-retry timer has expired. | The alternate destination that you choose might be a pilot number for voice mail, or a number that is assigned to an overhead bell, or some other number that you are sure will be answered. For more information, see the “Alternate Destination for Unavailable Hunt Groups” section . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Download the Cisco Unified CME B-ACD tar archive to a TFTP server that is accessible to the Cisco Unified CME router. | Go to the Cisco Unified CME Software Download website at http://www.cisco.com/cgi-bin/tablebuild.pl/ip-iostsp . Download the Cisco Unified CME B-ACD tar archive called cme-b-acd-2.1.0.0.tar (or a later version) to a TFTP server that is accessible to the Cisco Unified CME router. This tar archive contains the AA Tcl script, the call-queue Tcl script, and the default audio files that you need for Cisco Unified CME B-ACD service. Note If you have Cisco IOS Release 12.4(15)T or a later release and you use the embedded AA and call-queue Tcl scripts, you still must perform this step to download the audio files in the tar archive. |
| Step 2 | enable Router> enable | Enables privileged EXEC mode on the Cisco Unified CME router. Enter your password if prompted. |
| Step 3 | archive tar /xtract source-url flash: Router# archive tar /xtract tftp://192.168.1.1/cme-b-acd-x.x.x.tar flash: | Uncompresses the files in the Cisco Unified CME B-ACD file archive and copies them to flash memory. The following files are contained in the cme-b-acd-x.x.x.tar archive: app-b-acd-aa-x.x.x.x.tcl (AA script) app-b-acd-x.x.x.x.tcl (call-queue script) en_bacd_allagentsbusy.au (audio file) en_bacd_options_menu.au (audio file) en_bacd_disconnect.au (audio file) en_bacd_music_on_hold.au (audio file) en_bacd_invalidoption.au (audio file) en_bacd_welcome.au (audio file) en_bacd_enter_dest.au (audio file) |
| Step 4 | Rerecord audio files if necessary. | Rerecord audio files with your custom messages, but do not change the audio filenames except as specified here. Note that each audio filename is composed of two parts: a language code prefix and an identifier portion that begins with an underscore. (For example, for en_bacd_invalidoption.au, en is the prefix and _bacd_invalidoption.au is the identifier portion.) The prefix portion of the audio filename can be changed to match any of the language codes that are allowed in the paramspace language command. The prefix must match the language code that you specify in that command, regardless of the language actually used in the audio file. For example, if you use the Spanish language code for the invalid option file, the filename would be sp_bacd_invalidoption.au. The identifier portion of the filename must not be changed, except for the en_bacd_welcome.au file. That filename must be changed when you have multiple AAs because you need a different welcome message, and therefore a different audio file, for each AA. You can use any name that follows the same format as the default file: start the filename with a prefix that matches the specified language code, and start the identifier portion with an underscore. Use a .au suffix for the filename. For more information about audio files, see the “Welcome Prompt and Other Audio Files” section . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Router> enable | Enables privileged EXEC mode on the Cisco Unified CME router. Enter your password if prompted. |
| Step 2 | configure terminal Router# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag pots or dial-peer voice tag voip Router(config)# dial-peer voice 234 pots or Router(config)# dial-peer voice 25 voip | Enters dial-peer configuration mode. tag —Number used during configuration tasks to identify this dial peer. |
| Step 4 | service aa-service-name Router(config-dial-peer)# service aa1 | Associates this dial peer with an AA service. aa-service-name —AA service name to be used by this dial peer that was chosen in Step 3 in the “Planning the Cisco Unified CME B-ACD Call Flow” section and that will be assigned to the AA script in Step 10 in the “Setting Up Call-Queue and AA Services” section . |
| Step 5 | incoming called-number number Router(config-dial-peer)# incoming called-number 8005550100 | Specifies a digit string that can be matched by an incoming call to associate the call with a dial peer. number —Incoming called telephone number to serve as the AA pilot number for this AA service. Valid entries are any series of digits that specify the E.164 telephone number. The default is the calling number pattern. |
| Step 6 | port slot / port Router(config-dial-peer)# port 1/0:23 | Associates a dial peer with a specific voice port. slot / port —Use the appropriate platform-specific port designator for the voice port to be associated with this AA service. |
| Step 7 | exit Router(config-dial-peer)# exit | Exits dial-peer configuration mode. |
| Step 8 | Repeat Step 3 to Step 7 for each additional dial peer that will receive incoming calls to be directed to an AA service. | — |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Router# configure terminal | Enters global configuration mode. |
| Step 3 | ephone-hunt hunt-tag { longest-idle \| peer \| sequential } Router(config)# ephone-hunt 25 sequential | Enters ephone-hunt configuration mode. hunt-tag —Unique sequence number that identifies a hunt group during all configuration tasks. Range is 1 to 100. longest-idle —Calls go to the extension that has been idle the longest. The longest-idle is determined from the last time that a phone registered, reregistered, or went on-hook. peer —First extension to ring is the number to the right (in the list) of the extension that was the last one to ring when the hunt group was last called. Ringing proceeds in a circular manner, left to right, for the number of hops specified when the ephone hunt group is defined. sequential —Extensions ring in the order in which they are listed, left to right, when the hunt group s defined. |
| Step 4 | pilot number [ secondary number ] Router(config-ephone-hunt)# pilot 7000 | Defines the pilot number, which is the number that callers dial to reach the hunt group. number —E.164 number with a maximum length of 27 characters. The dial-plan pattern can be applied to the pilot number. secondary —(Optional) Defines the number that follows as an additional pilot number for the ephone hunt group. |
| Step 5 | list dn-number [ , dn-number ...] Router(config-ephone-hunt)# list 7001, 7002, 7003, 7004 | Defines the list of numbers to which the ephone hunt group redirects the incoming calls that are made to the pilot number. There must be from 1 to 20 numbers in the list. dn-number—An ephone-dn primary or secondary number. In Cisco Unified CME 4.0 and later versions, an asterisk (*) can take the place of an extension number to represent a wildcard slot. Any agent at an authorized ephone-dn can dynamically join and leave a hunt group if a wildcard slot is available. There can be up to 20 wildcard slots in a hunt group. |
| Step 6 | timeout seconds [, seconds ...] Router(config-ephone-hunt)# timeout 10 | (Optional) Sets the number of seconds after which a call that is not answered at one number is redirected to the next number in the hunt-group list. If this command is not used the default is the time period set by the timeouts ringing command, which has a default of 180 seconds if it is not set to another value. seconds —Number of seconds. Range is from 3 to 60000. In Cisco Unified CME 4.0 and later versions, multiple entries can be made, separated by commas; the number of entries must correspond to the number of ephone-dns in the list command. Each number in a multiple entry specifies the time that the corresponding ephone-dn will ring before a call is forwarded to the next number in the list. If a single number is entered, it is used for the no-answer period for each ephone-dn. Note Although the timeout command is optional, the default of 180 seconds may be greater than you desire. |
| Step 7 | callqueue display { continuous \| periodic \| off } | (Optional) Defines the call waiting notification display preference for the phones in a hunt group. Continuous — The call waiting notification is displayed continuously on the agent phone, as long as there are active calls in the call queue. Periodic —The call waiting notification is displayed for a period of 5 seconds on the agent phone, and updated after an interval of 20 seconds based on the latest call queue. Off —The call waiting notification is not displayed on the agent phone. If the no form of this command is used or the command is not configured, the display preference is set to the default state of continuous. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice hunt-group hunt-tag { longest-idle \| parallel \| peer \| sequential } Router(config)# voice hunt-group 1 longest-idle | Enters voice hunt-group configuration mode to define a hunt group. hunt-tag —Unique sequence number of the hunt group to be configured. Range is 1 to 100. longest-idle —Hunt group in which calls go to the directory number that has been idle for the longest time. parallel —Hunt group in which calls simultaneously ring multiple phones. peer —Hunt group in which the first directory number is selected round-robin from the list. sequential —Hunt group in which directory numbers ring in the order in which they are listed, left to right. To change the hunt-group type, remove the existing hunt group first by using the no form of the command; then, recreate the group. |
| Step 4 | pilot number [ secondary number ] Router(config-voice-hunt-group)# pilot number 8100 | Defines the pilot number, which is the number that callers dial to reach the voice hunt group. number —String of up to 16 characters that represents an E.164 telephone number. Number string may contain alphabetic characters when the number is to be dialed only by the Cisco Unified CME router, as with an intercom number, and not from telephone keypads. secondary number —(Optional) Keyword and argument combination defines the number that follows as an additional pilot number for the voice hunt group. Secondary numbers can contain wild cards. A wild card is a period (.), which matches any entered digit. |
| Step 5 | list number Router(config-voice-hunt-group)# list 8000, 8010, 8020, 8030 | Creates a list of extensions that are members of a voice hunt group. To remove a list from a router configuration, use the no form of this command. number —List of extensions to be added as members to the voice hunt group. Separate the extensions with commas. Add or delete all extensions in a hunt-group list at one time. You cannot add or delete a single number in an existing list. There must be from 2 to 10 extensions in the hunt-group list, and each number must be a primary or secondary number. Any number in the list cannot be a pilot number of a parallel hunt group. |
| Step 6 | timeout seconds Router(config-voice-hunt-group)# timeout 100 | Defines the number of seconds after which a call that is not answered is redirected to the next directory number in a voice hunt-group list. Default: 180 seconds. |
| Step 7 | callqueue display { continuous \| periodic \| off } | (Optional) Defines the call waiting notification display preference for the phones in a hunt group. Continuous — The call waiting notification is displayed continuously on the agent phone, as long as there are active calls in the call queue. Periodic —The call waiting notification is displayed for a period of 5 seconds on the agent phone, and updated after an interval of 20 seconds based on the latest call queue. Off —The call waiting notification is not displayed on the agent phone. If the no form of this command is used or the command is not configured, the display preference is set to the default state of periodic. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Router# voice service voip | Enters voice-service configuration mode to specify voip voice encapsulation type. |
| Step 4 | allow-connections sip to sip Router# allow-connections sip to sip | Allows connections between specific types of endpoints in a VoIP network. SIP to SIP connection is mandatory for B-ACD loopback call scenario. |
| Step 5 | voice class sip-profiles number \| translation-rule Router(config)# voice class sip-profiles OR Router(config)# translation-rule | Configures SIP profiles for a voice class. In B-ACD application, this command is used to modify the proxy number to the actual B-ACD pilot number. Translation rule—Associates a translation rule with a voice translation profile. In B-ACD application context, translation-rule is an alternative command for voice class sip-profiles. |
| Step 6 | dial-peer voice tag voip Router(config)# dial-peer voice 2 voip | Enters dial-peer configuration mode. tag —Number used during configuration tasks to identify this dial peer. |
| Step 7 | destination-pattern string Router(config-dial-peer)# destination-pattern 6001 | Specifies either the prefix or the full E.164 telephone number (depending on the dial plan) for a dial peer. string—The B-ACD proxy pilot number that needs to be configured. |
| Step 8 | session target ipv4: destination-address Router(config-dial-peer)# session target ipv4:1.0.0.0 | Designates a network-specific address to receive calls from a VoIP dial peer. The destination address should same as the IP address of the Unified CME router used. destination—IP address for the Cisco Unified CME interface on this router. |
| Step 9 | session protocol sipv2 Router(config-dial-peer)# session protocol sipv2 | Designates a SIP loopback trunk for B-ACD application. |
| Step 10 | voice-class sip profiles number Router(config-dial-peer)# voice-class sip profiles 1 | Associates the SIP profile with the dial peer. |
| Step 11 | dtmf-relay rtp-nte Router(config-dial-peer)# dtmf-relay rtp-nte | Specifies the method for relaying dual tone multifrequency (DTMF) tones between two devices as per RFC2833. |
| Step 12 | codec g711ulaw Router(config-dial-peer)# codec g711ulaw | Specifies the voice codec used. |
| Step 13 | end Router(config-dial-peer)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Router# configure terminal | Enters global configuration mode. |
| Step 3 | application Router(config)# application | Enters application configuration mode to configure packages and services. |
| Step 4 | service [ alternate \| default ] queue-service-name location Router(config-app)# service queue flash:app-b-acd-2.1.0.0.tcl In Cisco IOS Release 12.4(15)T or later releases, to use the embedded call-queue script: Router(config-app)# service app-b-acd | Enters service parameter configuration mode to configure parameters for the call-queue service. alternate —(Optional) Alternate service to use if the service that is configured on the dial peer fails. default —(Optional) Specifies that the default service (“DEFAULT”) on the dial peer is used if the alternate service fails. queue-service-name —Name of the call-queue service. This arbitrary name is used to identify the call-queue service during configuration tasks. location —URL of the Tcl script. Valid URLs can refer to TFTP, HTTP, or HTTPS servers, flash memory, or built-in scripts. Note Cisco IOS Release 12.4(15)T contains version 2.1.2.2 of the Cisco Unified CME B-ACD AA and call-queue Tcl scripts. |
| Step 5 | param number-of-hunt-grps number Router(config-app-param)# param number-of-hunt-grps 2 | Declares the maximum number of hunt groups supported by the Cisco Unified CME B-ACD call-queue script. number— Number of hunt groups used by the call-queue service. Range is from 1 to 10. Note The number argument declares the number of hunt groups only. It does not count the menu option for dial-by-extension. For example, if you have an AA that uses 2 hunt groups and a dial-by-extension option, and an AA with the drop-through option that uses 1 hunt group, enter 3 in this command. |
| Step 6 | param aa-hunt menu-number pilot - number Router(config-app-param)# param aa-hunt1 1111 | Associates a menu number with hunt group pilot number. Note Repeat this command to associate additional menu numbers with hunt-group pilot numbers. There should be as many entries of this command as the number of hunt groups that is specified in Step 5 . menu-number —Single digit that callers dial to choose this menu option (also referred to as the aa-hunt number). Range is from 1 to 10. Note that the hunt group with the highest aa-hunt number is automatically considered the operator hunt group, and its menu number maps to 0 (zero) for callers in addition to mapping to its aa-hunt number. pilot-number —Pilot number of the hunt group to which callers are transferred when they press the menu number. |
| Step 7 | param queue-len number Router(config-app-param)# param queue-len 15 | Sets the maximum number of calls allowed in each hunt group’s call queue used by Cisco Unified CME B-ACD. number— Number of calls that can be waiting in the call queue for each hunt group. The range is from 1 to 30. The default is 10. |
| Step 8 | param queue-manager-debugs [ 0 \| 1 ] Router(config-app-param)# param queue-manager-debugs 1 | Enables or disables the collection of call-queue debug information from the Cisco Unified CME B-ACD call queue service. 0 —(Optional) Disables debugging. 1 —(Optional) Enables debugging. Note This command is used with the debug voip application script command. Both the debug voip application script command and the param queue-manager-debugs command must be enabled together when debug trace files are collected. |
| Step 9 | exit Router(config-app-param)# exit | Exits service parameter configuration mode for the call-queue service. |
| Step 10 | service [ alternate \| default ] aa-service-name location Router(config-app)# service aa flash:app-b-acd-aa-2.1.0.0.tcl In Cisco IOS Release 12.4(15)T or later releases, to use the embedded AA script: Router(config-app)# service app-b-acd-aa | Enters service parameter configuration mode to configure parameters for an AA service. alternate —(Optional) Alternate service to use if the service that is configured on the dial peer fails. default —(Optional) Specifies that the default service (“DEFAULT”) on the dial peer is used if the alternate service fails. aa-service-name —Name of an AA service for which parameters are being set. This arbitrary name is used to identify a specific AA service during configuration tasks. location —URL of the Tcl script. Valid URLs can refer to TFTP, HTTP, or HTTPS servers, flash memory, or built-in scripts. Note Cisco IOS Release 12.4(15)T contains version 2.1.2.2 of the Cisco Unified CME B-ACD AA and call-queue Tcl scripts. |
| Step 11 | paramspace language-package location url Router(config-app-param)# paramspace english location flash: | Defines the location of audio files that are used for dynamic prompts by an interactive voice response (IVR) application. language-package —Name of the language package to be used. There are three built-in language packages: Chinese, English, and Spanish. Other languages may be supported by use of a Tcl language script. url —URL of the audio files. Valid URLs can refer to TFTP or HTTP servers or to flash memory. |
| Step 12 | paramspace language-package index number Router(config-app-param)# paramspace english index 1 | Defines the category of audio files that are used for dynamic prompts by an IVR application. language-package —Name of the language package to be used. There are three built-in language packages: Chinese, English, and Spanish. Other languages may be supported by use of a Tcl language script. number —Category group of the audio files (from 0 to 4). For example, audio files representing the days and months could be category 1, audio files representing units of currency could be category 2, and audio files representing units of time—seconds, minutes, and hours—could be category 3. Range is from 0 to 4; 0 means all categories. |
| Step 13 | paramspace language-package language language-code Router(config-app-param)# paramspace english language en | Defines the language code of audio files that are used for dynamic prompts by an IVR application. language-package —Name of the language package to be used. There are three built-in language packages: Chinese, English, and Spanish. Other languages may be supported by use a of Tcl language script. language-code —Two-character code that identifies the language of the associated audio files. Valid entries are as follows: – ch —Chinese – en —English – sp —Spanish – aa —all Note This language code must match the two-character language prefix used in the names of your audio prompt files regardless of the language that is actually used in the file. For more information, see the “Welcome Prompt and Other Audio Files” section . |
| Step 14 | param service-name queue-service-name Router(config-app-param)# param service-name app-b-acd | Associates the Cisco Unified CME B-ACD AA script with the Cisco Unified CME B-ACD call queue script. queue-service-name— Service name that was assigned to the call-queue service in Step 4 . |
| Step 15 | param handoff-string aa-service-name Router(config-app-param)# param handoff-string app-b-acd-aa | Specifies the AA service name to be given to the call-queue script. This is a mandatory parameter. aa-service-name —Service name that was assigned to a specific AA service in Step 10 . |
| Step 16 | param aa-pilot aa- pilot-number Router(config-app-param)# param aa-pilot 8005550123 | Associates a telephone number with this AA service. aa-pilot-number —Phone number to be dialed to reach this AA service. |
| Step 17 | param welcome-prompt audio-filename Router(config-app-param)# param welcome-prompt _bacd_welcome.au | (Optional) Assigns an audio file for the welcome greeting used by this AA service. audio-filename —Identifier part of the name of the audio file that contains the welcome greeting to be played when callers first reach the Cisco Unified CME B-ACD service. The identifier part of the filename does not include the language prefix, and it must begin with an underscore. The _bacd_welcome.au audio file is used by default. It announces “Thank you for calling” and includes a 2-second pause after the message. To rerecord a customized greeting in this file, see the instructions in the “Welcome Prompt and Other Audio Files” section . |
| Step 18 | param number-of-hunt-grps number Router(config-app-param)# param number-of-hunt-grps 2 | Specifies the number of hunt groups that are used with this AA service. number —Number of hunt groups to be used with this AA service. Range is from 1 to 3. Note If the AA that you are configuring uses the drop-through option, enter 1 for the number of hunt groups in this step. |
| Step 19 | param menu-timeout number Router(config-app-param)# param menu-timeout 5 | (Optional) Sets the number of times the AA service will loop the menu prompt before connecting the caller to an operator if the caller does not select a menu option. number —Number of times to replay menu prompt before connecting a caller to an operator if the caller does not select a menu option. Range: 0 to 10. Default: 4. |
| Step 20 | param dial-by-extension-option menu-number Router(config-app-param)# param dial-by-extension-option 1 | (Optional) Enables callers to dial extension numbers after dialing the specified menu number. menu-number —Identifier of a menu option. Range is from 1 to 9. There is no default. |
| Step 21 | param max-extension-length number Router(config-app-param)# param max-extension-length 4 | (Optional) Restricts the number of digits that can be dialed by callers using the dial-by-extension option. Note This command can be used to prevent toll fraud by restricting the number of digits that can be entered as the transfer destination for the dial-by-extension option. |
| Step 22 | param drop-through-option menu-number Router(config-app-param)# param drop-through-option 2 | (Optional) Assigns the drop-through option to a menu number for this AA service. menu-number —Menu option number (aa-hunt number) that was associated with a hunt group in Step 6 . Note When configuring an AA in drop-through mode, set the number of hunt groups in the AA ( Step 18 ) to 1. If an AA is in drop-through-option mode, it cannot have any other options besides one drop-through-option. |
| Step 23 | param drop-through-prompt audio-filename Router(config-app-param)# param drop-through-prompt _dt_prompt.au | (Optional) Associates an audio prompt file with the drop-through option for this AA service. audio-filename —Identifier part of the filename containing the prompt to be played when calls for the drop-through option are answered. The identifier part of the filename does not include the language prefix, and it must begin with an underscore. No default file is supplied. To record a customized drop-through prompt, see the instructions in the “Welcome Prompt and Other Audio Files” section . |
| Step 24 | param queue-exit-option option-number menu-number Router(config-app-param)# param queue-exit-option1 6 | Assigns a menu number to a call-queue exit option. option-number —Number of the call-queue exit option. Range: 1 to 3. There is no default. menu-number —Menu option number associated with the exit option. Supported in Cisco Unified CME 7.0(1) and later versions. |
| Step 25 | param queue-exit-extension option-number extension-number Router(config-app-param)# param queue-exit-extension1 202 | Assigns an extension number to a call-queue exit option. option-number —Number of the call-queue exit option. Range: 1 to 3. There is no default. extension-number —Extension number associated with the exit option. Supported in Cisco Unified CME 7.0(1) and later versions. |
| Step 26 | param queue-overflow-extension extension-number Router(config-app-param)# param queue-overflow-extension 5100 | Sets the extension number to route calls to when the call queue for the auto-attendant service is full. extension-number —Extension number to which the auto-attendant service forwards calls when the queue is full. Supported in Cisco Unified CME 7.0(1) and later versions. |
| Step 27 | param second-greeting-time seconds Router(config-app-param)# param second-greeting-time 45 | (Optional) Defines the time delay before the second greeting is played after a caller joins a Cisco Unified CME B-ACD call queue. The same time period is used for the interval between repeats of the second-greeting message. The second greeting is stored in the audio file named en_bacd_allagentsbusy.au. To record a customized second greeting, see the instructions in the “Welcome Prompt and Other Audio Files” section . seconds —Time interval before the second-greeting message is played or replayed, in seconds. The range is from 5 to 120. The default is 60. |
| Step 28 | param call-retry-timer seconds Router(config-app-param)# param call-retry-timer 10 | (Optional) Assigns the amount of time that calls must wait between retries to connect to a hunt group pilot number or to the alternate destination number. seconds —Time interval, in seconds. The range is from 1 to 30. The default is 5 seconds. |
| Step 29 | param max-time-call-retry seconds Router(config-app-param)# param max-time-call-retry 700 | (Optional) Sets the maximum amount of time for the call-retry timer. This is the maximum period of time for which a call can stay in a call queue and retry to connect with a hunt group before the call is sent to an alternate destination number. seconds —Maximum period of time, in seconds. The range is from 30 to 3600. The default is 600. |
| Step 30 | param max-time-vm-retry number Router(config-app-param)# param max-time-vm-retry 2 | (Optional) Assigns the number of times that calls to Cisco Unified CME B-ACD can attempt to reach the alternate destination number. number —Number of attempts. The range is from 1 to 3. The default is 1. Note In most cases, it is useful to have the number of attempts set at a number greater than 1, which will allow retries if the alternate destination number is busy on first attempt. |
| Step 31 | param voice-mail number Router(config-app-param)# param voice-mail 5003 | Defines an alternate destination for calls that are not answered by a hunt group because all members of the hunt group are logged out or because the call was still in a call queue when the maximum-time call-retry timer expired. This is a mandatory parameter. number —Alternate extension number to receive calls that remain unanswered by hunt groups. This number must be associated with a dial peer that is reachable by the Cisco Unified CME system. Note This number may be a voice-mail number, but it may also be any extension number that is set up to provide reliable coverage for unanswered B-ACD calls, such as a number that rings an overhead night bell. Note If you specify a number associated with a voice-mail system, be sure to set up the voice-mail system as specified in the documentation for the system. In addition, see the “ Integrating Voice Mail ” chapter of the Cisco Unified Communications Manager Express System Administrator Guide . |
| Step 32 | param send-account true Router(config-app-param)# param send-account true | (Optional) Generates call detail records for calls that are handled by the Cisco Unified CME B-ACD service. |
| Step 33 | param voice-mail-handoff [true\|false] Router(config-app-param)# param voice-mail-handoff true | (Optional) Toggles handoff support for calls to alternate destination. The default value is true. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Router# configure terminal | Enters global configuration mode. |
| Step 3 | ephone-hunt hunt-tag { longest-idle \| peer \| sequential } Router(config)# ephone-hunt 1 peer | Enters ephone-hunt configuration mode. For a description of the different types of hunt groups, see the “Setting Up Ephone Hunt Groups” section . |
| Step 4 | statistics collect Router(config-hunt-group)# statistics collect | Enables the collection of Cisco Unified CME B-ACD call statistics for an ephone hunt group. |
| Step 5 | end Router(config-hunt-group)# end | Returns to privileged EXEC mode. |
| Step 6 | show ephone-hunt [ tag ] statistics [ last hours hours \| start day time [ to day time ]] Router# show ephone-hunt 1 statistics last 1 hours | Displays ephone-hunt configuration information and current status and statistic information. tag —(Optional) The hunt-tag number configured in the ephone-hunt command. Range is from 1 to 100. statistics —Displays statistical information. last hours hours—(Optional) Displays information for the previous number of specified hours, counting backward from the current hour. Range is 1 to 167. start—Output start time. Default duration is one hour. to —(Optional) Output stop time. day —Day of week. Use sun , mon , tue , wed , thu , fri , or sat . time —Hour of the day. Range is 0 to 23. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice hunt-group hunt-tag { parallel \| longest-idle \| peer \| sequential } Router(config)# voice hunt-group 1 peer | Enters voice hunt-group configuration mode. For a description of the different types of hunt groups, see the “Setting Up Voice Hunt Groups” section . |
| Step 4 | statistics collect Router(config-voice-hunt-group)# statistics collect | Enables the collection of Cisco Unified CME B-ACD call statistics for a voice hunt group. |
| Step 5 | end Router(config-voice-hunt-group)# end | Returns to privileged EXEC mode. |
| Step 6 | show voice hunt-group [ tag ] statistics [ last hours hours \| start day time [ to day time ]] Router# show voice hunt-group 1 statistics last 1 hours | Displays voice hunt-group configuration information and current status and statistic information. tag —(Optional) The hunt-tag number configured in the voice hunt-group command. Range is from 1 to 100. statistics —Displays statistical information. last hours hours—(Optional) Displays information for the previous number of specified hours, counting backward from the current hour. Range is 1 to 167. start—Output start time. Default duration is one hour. to —(Optional) Output stop time. day —Day of week. Use sun , mon , tue , wed , thu , fri , or sat . time —Hour of the day. Range is 0 to 23. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Router# configure terminal | Enters global configuration mode. |
| Step 3 | ephone-hunt hunt-tag voice hunt-group hunt-tag Router(config)# ephone-hunt 1 Router(config)# voice hunt-group 1 | Enters ephone-hunt (or voice hunt-group) configuration mode. hunt-tag —Unique sequence number that identifies this hunt group during all configuration tasks. Range is from 1 to 100. |
| Step 4 | statistics collect Router(config-hunt-group)# statistics collect | Enables the collection of Cisco Unified CME B-ACD statistics data for an ephone hunt group. |
| Step 5 | exit Router(config-hunt-group)# exit | Exits ephone-hunt configuration mode. |
| Step 6 | telephony-service Router(config)# telephony-service | Enters telephony-service configuration mode. |
| Step 7 | hunt-group report url [ prefix tftp:// ip-address / directory-name... / prefix \| suffix from-number to to-number ] Router(config-telephony)# hunt-group report url prefix tftp://239.1.1.1/dirname1/dirname2/data Router(config-telephony)# hunt-group report url suffix 0 to 100 | Sets filename parameters and the URL path where call data is to be sent using TFTP. Note The hunt-group report url prefix command and the hunt-group report url suffix command must both be configured. prefix —(Optional) Sets the parameters for how the filenames must start. tftp:// ip-address / —(Optional) IP address to the files where AA call data is sent using TFTP. directory-name... / —(Optional) Names of directories separated by forward slashes (/) to declare the path to the files where AA call data is sent. prefix —(Optional) Declares parameters for how the filenames must start. suffix —(Optional) Sets numeric parameters for how the filenames must end. from-number —(Optional) Number at which the suffix range starts. The range is from 0 to 1. There is no default. to to-number —(Optional) Number at which the suffix range ends. The range is from 1 to 200. There is no default. |
| Step 8 | hunt-group report every number hours Router(config-telephony)# hunt-group report every 2 hours | Sets the hourly interval at which Cisco Unified CME B-ACD call statistics are collected for a report. number —Number of hours for which AA call data is collected and reported. The range is from 1 to 84. |
| Step 9 | hunt-group report delay number hours Router(config-telephony)# hunt-group report delay 2 hours | (Optional) Delays the stop time configured with the hunt-group report every hours command and continues to collect Cisco Unified CME B-ACD overflow call statistics. number —Number of hours for which data collection can be extended for the data collection periods configured with the hunt-group report every hours command. The range is from 1 to 10. |
| Step 10 | exit Router(config-telephony)# exit | Exits telephony-service configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | hunt-group statistics write-all location Router# hunt-group statistics write-all flash:huntstats | Writes ephone-hunt statistics information to a file. location —The URL or filename to which the statistics should be written. |