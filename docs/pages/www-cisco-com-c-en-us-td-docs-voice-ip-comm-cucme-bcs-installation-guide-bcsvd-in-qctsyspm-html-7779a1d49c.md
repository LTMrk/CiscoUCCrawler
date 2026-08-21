---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-bcs-installation-guide-bcsvd-in-qctsyspm-html-7779a1d49c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/bcs/installation/guide/bcsvd_in/QCTsyspm.html
retrieved_at: 2026-08-21T22:58:43.195715+00:00
---

Installing Cisco Business Communications Solution Verified Designs

# Installing Cisco Business Communications Solution Verified Designs

Updated: November 2, 2007

Chapter: Configuring Cisco Business Communications Solution Verified Designs

## Chapter: Configuring Cisco Business Communications Solution Verified Designs

## Configuring Cisco Business Communications Solution Verified Designs

This chapter describes how to enter configuration information for your Cisco BCS Verified Designs system using QCT. Once all the necessary information is entered, QCT generates a configuration file containing all the required CLI commands that you can upload to your router.

## Contents

This chapter provides the following sections:

• Launching Cisco IPC Express QCT

• Default Values

• Navigating in Cisco IPC Express QCT

• Configuring System Parameters

• Configuring IP Phone Parameters

• Generating Configurations

• Selecting System Type and Configuration Type

• Configuring Voice-Mail Parameters

• Configuring Advanced Cisco CME Features Parameters

• Configuring IP Phone Parameters

• Generating Configurations

• Testing the Installation

• What to Do Next

## Launching Cisco IPC Express QCT

Perform the following steps to launch Cisco IPC Express QCT.

Step 1 Ensure that your PC is connected to the router's console port.

Step 2 Open the directory on your PC in which you installed Cisco IPC Express QCT.

Step 3 Click QCT.htm to launch Cisco IPC Express QCT (see Figure 15 ).

Figure 15 QCT.htm File Location

Step 4 Click Accept to acknowledge the licensing agreement (see Figure 16 ).

Figure 16 QCT Licensing Agreement

Cisco IPC Express QCT is now ready to use (see Figure 17 ).

Figure 17 Cisco IPC Express Quick Configuration Tool Window

## Default Values

Cisco IPC Express QCT windows provide recommended, default telephony-service parameters that you can accept to quickly configure your telephony system. Accept these parameters or change any value. These default values may not be appropriate for every system.

Note The installation of Cisco BCS Verified Designs did not use most default values.

## Navigating in Cisco IPC Express QCT

Cisco IPC Express QCT provides navigation buttons to move from one configuration window to the next (see Figure 18 ).

Figure 18 Quick Configuration Tool Navigation Buttons

## Configuring System Parameters

Use the information from your Cisco Business Communications Solution Verified Designs Planning Worksheet and perform these steps to enter your information into the System Parameters window.

Step 1 Click System Parameters to activate the System Parameters window (see Figure 19 ):

Figure 19 Systems Parameters Button

The System Parameters window appears (see Figure 20 ):

Figure 20 System Parameters Window

### Configuring General System Information

Perform the following steps to enter your general Cisco CME information in the General System Information area of the System Parameters window.

Step 2 Enter the name of your company (see Figure 21 ):

Figure 21 Company Name Field

See Figure 22 for an example:

Figure 22 Specifying Company Name (Example)

Step 3 Enter your router's host name (see Figure 23 ):

Figure 23 Router's Host Name Field

See Figure 24 for an example:

Figure 24 Specifying Router Host Name (Example)

Step 4 Specify the number of IP phones deployed at your site (see Figure 25 ). This number is dependent on the type of router that you are using. For example, the Cisco 3825 supports up to a maximum of 168 IP phones. The number of IP phones deployed could be less than the maximum supported. To determine the number of IP phones supported by voice-bundled routers, see "Appendix A: Cisco CallManager Express Bundles" section .

Figure 25 Specifying Number of IP Phones Deployed

Step 5 Enter your administrator's user ID and password (see Figure 26 ). Accept the default user ID and password, or enter new values.

Figure 26 Specifying Administrator User ID and Password

Step 6 Specify your time zone from the drop-down menu (see Figure 27 ):

Figure 27 Specifying Time Zone

Step 7 If appropriate, check the check box to enable daylight saving (see Figure 28 ):

Figure 28 Specifying Daylight Saving

Step 8 To save the generated configuration to the start-up configuration on the router, check the following check box (see Figure 29 ):

Figure 29 Specifying Whether to Save Generated Configuration to Start-Up

This completes the General System Information area of the System Parameters window. Proceed to "Hardware Configuration" section .

### Hardware Configuration

The Hardware Configuration area of the System Parameters window provides a visual layout of your router configuration.

Perform the following steps to detect your Cisco CME hardware configuration in the Hardware Configuration area of the System Parameters window.

Step 9 Ensure tht your router is powered on and has been running at least five minutes.

Step 10 Click Auto Detect Hardware Configuration (see Figure 30 ):

Figure 30 Auto Detect Hardware Configuration Button

The Detect Hardware Configuration window appears (see Figure 31 ):

Figure 31 Detect Hardware Configuration Windown

Step 11 Connect a console cable from the PC's serial port to the router's console port and specify from the drop-down menu which PC serial port is being used (see Figure 32 ):

Figure 32 Specifying PC COM Port

Step 12 Press Detect (see Figure 33 ):

Figure 33 Detect Button

Step 13 Confirm that your serial cable is properly connected by clicking OK in the confirmation dialog box (see Figure 34 ):

Figure 34 COM Port Confirmation

Step 14 Click Yes to accept any ActiveX control from an Internet Explorer dialog box (see Figure 35 ):

Figure 35 Detect Hardware Active X Dialog

Cisco IPC Express QCT begins to analyze your installed hardware (see Figure 36 ):

Figure 36 Hardware Detection Analyzing Pop-Up

Following hardware detection, the Hardware Configuration area shows installed hardware in your router. Figure 37 shows an installed AIM-CUE card as an example.

Figure 37 Analyzed Detected Hardware (Example)

### Your Options for System Type and Configuration

You must instruct QCT how your system will be configured. The System Type Configuration area of the System Parameters window provides radio buttons to allow you to specify how your system will be configured and the configuration type (see Figure 38 ) .

Figure 38 System Type and Configuration Type Selection

### Keysystems and PBXs

When setting up a Cisco IPC Express system, you need to decide if call handling should be similar to that of a PBX or similar to that of a keyswitch.

Note Cisco BCS Verified Designs was configured using the PBX:Custom selection.

### Keysystem

In a keysystem, you can set up most of your phones to have a nearly identical configuration, in which each phone is able to answer any incoming PSTN call on any line. For example, you have four incoming PSTN lines that each appear as shared lines on four different phones. Each phone has the same shared lines. Keysystems can be used when no internal call switching is necessary.

In the keysystem model, when an incoming call arrives, it rings all available IP phones. When multiple calls are present within the system at the same time, each individual call (ringing or waiting on hold) is visible and can be directly selected by pressing the corresponding line button on an IP phone. In this model, calls can be moved between phones simply by putting the call on hold at one phone and selecting the call using the line button on another phone.

### PBX

The PBX model allows the IP phones in your system to have a single unique extension number. PBX configurations are usually required for larger companies who need both internal (extension numbers) and external (PSTN) phone capabilities.

The PBX model also enables your configuration to support features such as intercom, call park, hunt groups, and caller ID blocking.

### Typical or Custom Configuration

Choose typical if you are setting up a voice-only system. Choose custom if you want to customize the IP addressing for the system.

Perform the following steps to select how your system will be configured and the configuration type .

Step 15 Click the Configure as a keysystem or Configure as a PBX radio button to select how your system will be configured.

Step 16 Click the Typical Configuration or Custom Configuration radio button to select how your system will be configured.

## Selecting System Type and Configuration Type

Once you select how your system will be configured and the configuration type , see the following sections to help you finish your system-type configuration. If you select:

• Configure as a Keysystem and Typical Configuration, see the "Configuring Keysystem:Typical Configurations" section .

• Configure as a Keysystem and Custom Configuration, see the "Configuring Keysystem:Custom Configurations" section .

• Configure as a PBX and Typical Configuration, see the "Configuring PBX:Typical Configurations" section .

• Configure as a PBX and Custom Configuration, see the "Configuring PBX:Custom Configurations" section .

### Configuring Keysystem:Typical Configurations

If you selected Keysystem and Typical Configuration from the System Type Configuration area of the QCT Systems Parameters window, enter PSTN connectivity information (see Figure 39 ).

Figure 39 Keysystem:Typical Configuration Fields

### Configuring PSTN Connectivity Parameters

Perform the following steps to configure optional PSTN connectivity parameters.

Step 1 Specify the number of available trunk phone numbers (see Figure 40 ):

Figure 40 Specifying Available Trunk Phone Numbers

Step 2 Enter the trunk phone numbers (see Figure 41 ):

Figure 41 Specifying Trunk Phone Numbers

After entering your PSTN connectivity parameters, you are ready to perform any necessary configuration for your IP phones.

Step 3 Add voice-mail parameters (see the "Configuring IP Phone Parameters" section ).

### Configuring Keysystem:Custom Configurations

If you selected Keysystem and Custom Configuration from the System Type Configuration area of the QCT Systems Parameters window, new information fields appears as shown in Figure 42 .

Figure 42 Keysystem:Custom Configuration Fields

### Configuring General Phone Parameters

Perform the following steps to configure general phone information.

Step 1 Enter the first extension number (see Figure 43 ):

Note Do not use the digit 9 as the first digit of any extension number. The digit 9 is reserved for secondary dial tone.

Figure 43 Specifying General Phone Parameters

Step 2 Specify if this extension is a dual-line phone (two phone extensions, same number for each IP phone) by checking the dual-line check box (see Figure 44 ):

Figure 44 Specifying Dual-Line

### Configuring Network Parameters

Perform the following steps to configure network parameters for your IP phones.

Step 1 Enter the IP address and subnet mask of your Dynamic Host Configuration Server (DHCP) server (see Figure 45 ):

Note The IP addresses shown in Figure 45 are examples only. Enter your DHCP server IP address information from your Cisco Business Communications Solution Verified Designs Planning Worksheet .

Figure 45 Specifying DHCP Network IP Address and Subnet Mask

Step 2 Specify your DHCP excluded address range (see Figure 46 ):

Figure 46 Specifying DHCP Excluded Addresses

Step 3 Specify your Cisco CME router's IP address and subnet mask (see Figure 47 ):

Figure 47 Specifying Cisco CME Router IP Address and Subnet Mask

Step 4 If required, enter the IP addresses for your Network Time Protocol (NTP) servers (see Figure 48 ). NTP allows you to synchronize your Cisco CME router to a single clock on a network, which is known as the clock master. NTP is disabled on all interfaces by default.

Note NTP is not required for Cisco Business Communications Solution Verified Designs.

Figure 48 Specifying NTP Server IP Address (Optional)

### Configuring PSTN Connectivity Parameters

Perform the following steps to configure optional PSTN connectivity parameters.

Step 1 Enter a digit that you would press to select secondary dial tone (see Figure 49 ):

Figure 49 Specifying Secondary Dial Tone Digit

Step 2 Specify the emergency number (see Figure 50 ):

Figure 50 Specifying Emergency Number

Step 3 Specify the number of available trunk phone numbers (see Figure 51 ):

Figure 51 Specifying Available Trunk Phone Number

Step 4 Enter the trunk phone numbers (see Figure 52 ):

Figure 52 Specifying Trunk Phone Numbers

### Configuring Voice-Mail Parameters

If you have an installed AIM card, enter voice-mail configuration information.

Step 1 Specify whether to configure a general delivery mailbox for Cisco CUE by checking the check box (see Figure 53 ):

Figure 53 Specifying General Delivery Mailbox

If you are configuring a general delivery mailbox, enter additional voice-mail parameters as illustrated in Figure 54 :

Figure 54 Voicemail Parameters Fields

Step 2 For detailed information on adding voice-mail parameters, see the "Configuring Voice-Mail Parameters" section .

### Configuring PBX:Typical Configurations

If you selected PBX and Typical Configuration from the System Type Configuration area of the QCT Systems Parameters window, enter additional configuration parameters as shown in Figure 55 .

Figure 55 PBX:Typical Configuration Fields

### Configuring PSTN Connectivity Parameters

If your hardware configuration contains a 4-port FXO card, perform the following steps to enter optional PSTN connectivity parameters.

Step 1 Enter a digit that you would press to select secondary dial tone (see Figure 56 ):

Figure 56 Specifying Secondary Dial Tone Digit

Step 2 Specify the emergency number (see Figure 57 ):

Figure 57 Specifying Emergency Number

Step 3 Specify if there are Direct Inward Dial (DID) phone numbers available (see Figure 58 ):

Figure 58 Specifying Available DIDs

Step 4 If DIDs are available, enter the first phone numbers (see Figure 59 ):

Figure 59 Specifying First Phone Numbers

Step 5 Specify the number of available phone numbers (see Figure 60 ):

Figure 60 Specifying Available Phone Number

### Configuring Voice-Mail Parameters

If you have an installed AIM card, enter voice-mail configuration information.

Step 1 Specify if you are using Cisco Unity Express voice mail by checking the check box (see Figure 61 ):

Figure 61 Specifying Cisco Voice Mail

If you are using Cisco Unity Express voice mail, additional information fields appear (see Figure 62 ):

Figure 62 Cisco Voice-Mail Parameters Fields

Step 2 For detailed information on adding voice-mail parameters, see the "Configuring Voice-Mail Parameters" section ).

### Configuring PBX:Custom Configurations

If you selected PBX and Custom Configuration from the System Type Configuration area of the Systems Parameters window, enter additional configuration parameters as illustrated in Figure 63 .

Figure 63 PBX:Custom Parameters

### Configuring General Phone Parameters

Perform the following steps to configure general phone information.

Step 1 Enter the first extension number of your IP phones (see Figure 64 ):

Figure 64 Specifying First Extension Number

Step 2 Specify if this extension is a dual-line phone by checking the dual-line check box (see Figure 65 ):

Figure 65 Specifying Dual-Line Phone

### Configuring Network Parameters

Perform the following steps to configure network parameters.

Step 1 Enter the IP address and subnet mask of your DHCP server (see Figure 66 ):

Note The following IP addresses are examples only. Enter your DHCP server IP address information from your Cisco Business Communications Solution Verified Designs Planning Worksheet .

Figure 66 Specifying DHCP IP Address and Subnet Mask

Step 2 Specify your DHCP Excluded Address range (see Figure 67 ):

Figure 67 Specifying DHCP Excluded Addresses

Step 3 Specify your Cisco CME router's IP address and subnet mask (see Figure 68 ):

Figure 68 Specifying Cisco CME Router IP Address and Subnet Mask

Step 4 Enter the IP addresses and subnet masks for your NTP servers (see Figure 69 ):

Figure 69 Specifying NTP Server IP Addresses

### Configuring PSTN Connectivity Parameters

Perform the following steps to configure optional PSTN connectivity parameters.

Step 1 Enter a digit you would press to select secondary dial tone (see Figure 70 ):

Figure 70 Specifying Secondary Dialtone Digit

Step 2 Specify the emergency number (see Figure 71 ):

Figure 71 Specifying Emergency Number

Step 3 Specify if there are Direct Inward Dial (DID) phone numbers available by checking the check box (see Figure 72 ):

Figure 72 Specifying Available DIDs

Step 4 If DIDs are available, enter the first phone numbers (see Figure 73 ):

Figure 73 Specifying First Phone Numbers

Step 5 Specify the number of available phone numbers (see Figure 74 ):

Figure 74 Specifying Available Phone Numbers

Step 6 Add voice-mail parameters (see the "Configuring Voice-Mail Parameters" section ).

## Configuring Voice-Mail Parameters

Perform the following steps to configure voice-mail parameters.

Step 1 Specify if you are using Cisco Unity Express voice mail by checking the check box (see Figure 75 ):

Figure 75 Specifying Cisco Voicemail Parameters

If you are using Cisco Unity Express voice mail, additional information fields appear (see Figure 76 ):

Figure 76 Cisco Voice-Mail Parameter Fields

Step 2 In the Voice Mail System Type drop-down menu, select Cisco Unity Express (see Figure 77 ):

Figure 77 Specifying Voice Mail System Type

Step 3 Specify the Cisco CUE Feature License by selecting the number of mailboxes from the drop-down menu (see Figure 78 ):

Figure 78 Specifying Cisco CUE Licensing

Step 4 Specify the IP address of the Cisco CUE router (see Figure 79 ):

Figure 79 Specifying Cisco CUE IP Address

Step 5 Specify the Auto Attendant pilot number (see Figure 80 ):

Note Remember not to use digit 9 for any extension.

Figure 80 Specifying Auto Attendant Pilot Number

Step 6 Specify your voice-mail access number (see Figure 81 ):

Figure 81 Specifying Voice-Mail Access Number

Step 7 Specify the voice-mail timeout from the drop-down menu (see Figure 82 ):

Figure 82 Specifying Voice-Mail Timeout

Step 8 Specify your message-waiting indicator (MWI) On number (see Figure 83 ):

Figure 83 Specifying MWI On

Step 9 Specify your message-waiting indicator (MWI) Off number (see Figure 84 ):

Figure 84 Specifying MWI Off

This completes the voice-mail parameters section.

Step 10 Enter advanced Cisco CME features (see the "Configuring Advanced Cisco CME Features Parameters" section ).

## Configuring Advanced Cisco CME Features Parameters

Follow the procedure in this section if you wish to configure additional features for your telephony network (see Figure 85 ).

Figure 85 Advanced Cisco CME Feature Parameter Fields

Additional Cisco CME features include the following:

• Paging (see the "Configuring Paging" section )

• Intercom (see the "Configuring Intercom" section )

• Call Park (see the "Configuring Call Park" section )

• Hunt Group (see the "Configuring Hunt Groups" section )

• Caller ID Blocking (see the "Configuring Caller ID Blocking Parameters" section )

### Configuring Paging

Step 1 To enable paging, check in the Paging check box (see Figure 86 ):

Figure 86 Specifying Paging Parameters

a. Specify the number of paging groups from the drop-down menu.

b. Enter the paging group extension numbers.

### Configuring Intercom

Step 1 To enable intercom between IP phones, check Intercom check box (see Figure 87 ):

Figure 87 Specifying Intercom

### Configuring Call Park

Step 1 To enable call park, check the Call Park check box (see Figure 88 ):

Figure 88 Specifying Call Park

a. Specify the number of park slots from the drop-down menu (see Figure 89 ):

Figure 89 Specifying Number of Park Slots

b. Enter your park slot extension numbers (see Figure 90 ):

Figure 90 Specifying Park Slot Extension Numbers

### Configuring Hunt Groups

Step 1 Enable hunt groups by checking the Hunt Group check box (see Figure 91 ):

Figure 91 Specifying Hunt Groups

Step 2 Specify the number of hunt groups from the drop-down menu (see Figure 92 ):

Figure 92 Specifying Number of Hunt Groups

Step 3 Enter the hunt timeout value in seconds (see Figure 93 ):

Figure 93 Specifying Hunt Group TImeout

Step 4 Enter your hunt group pilot numbers (see Figure 94 ):

Figure 94 Specifying Hunt Group Pilot Number

Step 5 Specify your hunt type from the drop-down menu (see Figure 95 ):

Figure 95 Specifying Hunt Type

Step 6 Enable whether to send the hunt groups to voice mail by checking the Forware to VM check box (see Figure 96 ):

Figure 96 Specifying Hunt Group to Voice-Mail

### Configuring Caller ID Blocking Parameters

Step 1 To enable caller ID blocking parameters, check the Caller ID Blocking check box (see Figure 97 ):

Figure 97 Specifying Call ID Blocking

Step 2 Enter your caller ID block code (see Figure 98 ):

Figure 98 Specifying Caller ID Block Code

Note Enter an asterisk (*) before the caller ID block code.

This completes the configuration of Advanced CME features parameters.

Step 3 Configure your IP phones (see the "Configuring IP Phone Parameters" section ).

## Configuring IP Phone Parameters

After configuring all your system parameters, proceed to the Phone Parameters window of Cisco IPC Express QCT.

Step 1 Click Go To Phone Parameters button (see Figure 99 ) :

Figure 99 Go To Phone Parameters Button

QCT begins to automatically generate your phone parameters information (see Figure 100 ):

Figure 100 Analyzing IP Phone Parameters

The IP Phone Parameters window appears (see Figure 101 ):

Figure 101 IP Phone Parameters Window

The IP Phone Parameters window allows you to enter specific telephony information for each IP phone in your system. The IP Phone Parameters window contains slightly different information depending on the system configuration type you chose.

Step 2 If you chose:

• Keysystem, see the "Configuring Keysystem IP Phone Parameters" section .

• PBX, see the "Configuring PBX IP Phone Parameters" section .

### Configuring Keysystem IP Phone Parameters

Perform the following steps to enter keysystem IP phone parameters.

Step 1 Click the Phone Parameters button to activate the IP Phone Parameters window.

The Keysystem IP Phone Parameters window appears (see Figure 102 ):

Figure 102 Keysystem IP Phone Parameters Window

Each input field is tab indexed to allow you to flow from one field to the next to enter information.

Tip You may use a bar-code scanner to enter IP phone Mac address and phone type.

Step 2 Edit any default phone parameter to suit your network.

Table 4 Keysystem IP Phone Parameters Screen Fields

MAC Address

Enter, or scan, the MAC address of each IP phone. MAC addresses are located on the bottom of the IP phone.

Phone Type

Specify the IP phone type.

Dual-Line

Enter a check next to the IP phone you want to have two lines for each extension.

Extension Number

Enter the extension number for each IP phone.

Paging Group

Specify from the drop-down menu the paging group you want to associate with each IP phone.

Name

Enter the name to associate with each IP phone. The name will appear in the IP phone display.

User ID

Enter a user ID for each IP phone.

Password

Enter a password for each IP phone.

CO

Specify with a check the CO trunk phone numbers associated with each IP phone.

### What to Do Next

Once you finish entering your keysystem configuration parameters, generate the configuration (see the "Generating Configurations" section ).

### Configuring PBX IP Phone Parameters

Perform the following steps to enter PBX IP phone parameters.

Step 1 Click the Phone Parameters button to activate the IP Phone Parameters screen.

The PBX IP Phone Parameters window appears (see Figure 103 ):

Figure 103 PBX IP Phone Parameters Window

The fields on the IP Phone Parameters window are tab indexed to flow from one field to the next.

Tip QCT supports the use of a bar-code scanner to enter IP phone MAC addresses and phone types. Cisco BCS Verified Designs has tested a bar-code scanner from Flic™.

Step 2 Edit any default phone parameter to suit your network (see Table 5 ).

Table 5 PBX IP Phone Parameters Screen Fields

MAC Address

Enter, or scan, the MAC address of each IP phone. MAC addresses are located on the bottom of the IP phone.

Phone Type

Specify the IP phone type.

Dual-Line

Enter a check next to the IP phone you want to have two lines for each extension.

Extension Number

Enter the extension number for each IP phone.

Paging Group

Specify from the drop-down menu the paging group you want to associate with each IP phone.

Intercom

Specify from the drop-down menu the IP phone you want to intercom with this IP phone.

Hunt Group

Specify from the drop-down menu the hunt group associated with each IP phone.

DID Number

Enter the Direct Inward Dial number for each IP phone. DID numbers accept both 7- and 10-digit numbers.

Name

Enter the name to associate with each IP phone. The name will appear in the IP phone display.

User ID

Enter a user ID for each IP phone.

Password

Enter a password for each IP phone.

Voicemail

Enter a check to specify voicemail for each IP phone.

Call Forward Busy

Enter the extension number where you want to transfer calls to if an incoming call to an extension is busy.

Call Forward No Answer

Enter the extension number where you want to transfer calls to if an incoming call to an extension is not answered.

Ringing Timeout

Specify a value in seconds before transferring an unanswered call to another extension.

### What to Do Next

Once you finish entering your PBX configuration parameters, generate the configuration (see the "Generating Configurations" section ).

## Generating Configurations

Once you enter all your system and phone parameters, generate your router configuration:

Step 1 Click the Generate Configuration button (see Figure 104 ):

Figure 104 Generate Configuration Button

Once your configuration generates, it will automatically display (see Figure 105 ):

Figure 105 Display of Generated Configuration

Note The generated configuration displays if the Display Configuration check box is selected on the QCT Options window (see the "Display Configuration" section ).

Step 2 Save the router configuration.

Step 3 When prompted, click Yes to push the configuration to the router (see Figure 106 ):

Figure 106 Confirming Pushing Configuration to Router

QCT begins to generate your configuration (see Figure 107 ).

Figure 107 Generating Configuration

QCT continues to generate your Cisco CUE voice-mail configuration (see Figure 108 ).

Figure 108 Generating Cisco CUE Voice Mail

QCT informs you when it is finished (see Figure 109 ):

Figure 109 Confirming Generated Configuration

Step 4 Click OK .

Your router is now configured. See Appendix C: Cisco BCS Verified Designs Configuration Example for an example of a typical Cisco Business Communications Solution configuration file.

You can upload any saved configuration to your router (see the "Uploading Saved Configurations" section ).

## Testing the Installation

Perform the following steps to test the initial Cisco BCS Verified Designs configuration.

Step 1 Reboot the router.

Step 2 Connect the router to a nonconfigured switch (default switch configuration only).

Step 3 Connect preconfigured (MAC address previously entered in the IP Phone Parameters window) IP phones to the switch.

Step 4 Press the settings button on the IP phone and look under Network Configuration to make sure that the IP phones are receiving the appropriate IP addressing from the DHCP server.

Once the IP addressing is received (this could take several minutes), two connected IP phones should be able to call each other.

## What to Do Next

After entering configuration parameters for Cisco SOCC, you are ready to use the command line interface (CLI) to continue your installation. See the "Continuing the Cisco BCS Verified Designs Configuration Using CLI" section .

| Field | To Set |
|---|---|
| MAC Address | Enter, or scan, the MAC address of each IP phone. MAC addresses are located on the bottom of the IP phone. |
| Phone Type | Specify the IP phone type. |
| Dual-Line | Enter a check next to the IP phone you want to have two lines for each extension. |
| Extension Number | Enter the extension number for each IP phone. |
| Paging Group | Specify from the drop-down menu the paging group you want to associate with each IP phone. |
| Name | Enter the name to associate with each IP phone. The name will appear in the IP phone display. |
| User ID | Enter a user ID for each IP phone. |
| Password | Enter a password for each IP phone. |
| CO | Specify with a check the CO trunk phone numbers associated with each IP phone. |

| Field | To Set |
|---|---|
| MAC Address | Enter, or scan, the MAC address of each IP phone. MAC addresses are located on the bottom of the IP phone. |
| Phone Type | Specify the IP phone type. |
| Dual-Line | Enter a check next to the IP phone you want to have two lines for each extension. |
| Extension Number | Enter the extension number for each IP phone. |
| Paging Group | Specify from the drop-down menu the paging group you want to associate with each IP phone. |
| Intercom | Specify from the drop-down menu the IP phone you want to intercom with this IP phone. |
| Hunt Group | Specify from the drop-down menu the hunt group associated with each IP phone. |
| DID Number | Enter the Direct Inward Dial number for each IP phone. DID numbers accept both 7- and 10-digit numbers. |
| Name | Enter the name to associate with each IP phone. The name will appear in the IP phone display. |
| User ID | Enter a user ID for each IP phone. |
| Password | Enter a password for each IP phone. |
| Voicemail | Enter a check to specify voicemail for each IP phone. |
| Call Forward Busy | Enter the extension number where you want to transfer calls to if an incoming call to an extension is busy. |
| Call Forward No Answer | Enter the extension number where you want to transfer calls to if an incoming call to an extension is not answered. |
| Ringing Timeout | Specify a value in seconds before transferring an unanswered call to another extension. |