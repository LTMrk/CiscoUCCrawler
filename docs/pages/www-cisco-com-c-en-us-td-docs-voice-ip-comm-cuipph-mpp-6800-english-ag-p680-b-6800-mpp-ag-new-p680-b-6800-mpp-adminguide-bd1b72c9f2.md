---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-6800-english-ag-p680-b-6800-mpp-ag-new-p680-b-6800-mpp-adminguide-bd1b72c9f2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/6800/english/AG/p680_b_6800-mpp-ag_new/p680_b_6800-mpp-adminguide_chapter_010000.html
retrieved_at: 2026-08-21T23:16:30.291652+00:00
---

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide for Release 11.3(1) and Later

# Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide for Release 11.3(1) and Later

Updated: November 21, 2019

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## Feature Troubleshooting

Here is troubleshooting information related to some of the phone features.

### ACD Call Information Missing

#### Problem

A call center phone does not see call information during a call.

#### Solution

Check the phone configuration to determine if Call Information Enable is set to yes.

Check the Broadsoft server configuration to determine if the user's Device Profile is configured with "Support Call Center MIME Type" .

### Phone Doesn't Show ACD Softkeys

#### Problem

The phone doesn't display the Agent Sign In or Agent Sign Out softkeys.

#### Solution

Check Broadsoft server configuration to determine if that user has been configured as a call center agent.

Enable the programmable softkeys (PSK) and add the ACD softkeys to the softkey list. For more information, see Customize Display of the Softkeys .

Check the phone configuration to determine if BroadSoft ACD is set to yes.

### Phone Doesn't Show ACD Agent Availability

#### Problem

The phone doesn't display the Avail or Unavail softkeys for an agent.

#### Solution

Check Broadsoft server configuration to determine if that user has been configured as a call center agent.

Check the phone configuration to determine if BroadSoft ACD is set to yes.

Set up the Agt Status programmable softkey (PSK) and add the ACD softkey to the softkey list. For more information, see Customize Display of the Softkeys .

Instruct users to press the Agt Status key to display the Available , Unavailable , and Wrap-up possible states.

Select the desired agent state.

### Call Doesn't Record

#### Problem

When a user tries to record a call, the recording doesn't takes place.

#### Cause

This is often due to configuration issues.

#### Solution

Set the phone to always record a call.

Make a call.

If the recording doesn't start, there are configuration problems. Check the configuration of the BroadWorks and third-party
                                 recorder.

If the recording does start:

Set the phone to record on demand.

Set up Wireshark to capture a trace of the network traffic between the phone and Broadworks when the problem occurs. When
                                       you have the trace, contact TAC for further assistance.

### An Emergency Call Doesn't Connect to Emergency Services

#### Problem

A user tries to place an emergency call, but the call doesn't connect to the emergency services (fire, police, or emergency
                                 services operator).

#### Solution

Check the emergency call configuration:

Company Identifier or location request URL setup is incorrect. See Configure a Phone to Make Emergency Calls .

An incorrect or blank emergency number exists in the Dial Plan setup. See Edit the Dial Plan on the IP Phone .

The location request servers (emergency call service provider) did not respond with a phone location, after multiple attempts.

### Presence Status Doesn't Work

#### Problem

The phone doesn't show presence information.

#### Solution

Use UC Communicator as a reference to verify that the account works.

### Phone Presence Message: Disconnected from Server

#### Problem

Instead of presence information, the user sees the message Disconnected from server .

#### Solution

Check the Broadsoft server configuration to determine if IM&P service is enabled and assigned to that user.

Check the phone configuration to determine if the phone can connect to the internet and get the XMPP messages.

Check the XMPP Incoming and Outgoing messages printed in the syslog to make sure it can login successfully.

### Phone Cannot Access BroadSoft Directory for XSI

#### Problem

The phone displays XSI directory access error.

#### Solution

Check Broadsoft server configuration for the user login and SIP credentials.

Check error messages in syslog.

Check information on the error on the phone screen.

If HTTPS connection fails, check the error message on the phone screen and in the syslog.

Install custom CA for HTTPS connection if the BroadSoft certificate is not signed from phone built-in root CA.

### Executive or Assistant Menu Does Not Appear

#### Problem

The Settings > Executive or Settings > Assistant menu item doesn't appear on an executive's or assistant's phone respectively.

#### Solution

Ensure that synchronization of settings is enabled for the user's extension. See Executive-Assistant Setting Synchronization .

Check if the phone has executives or assistants, or both configured on different extensions.

### Phone Doesn't Show Contacts

#### Problem

The phone doesn't display any contacts in the All directories screen when Search All Enable and Browse Mode Enable are set to Yes .

#### Solution

Check that the personal address book is enabled in the phone.

Check that there are contacts in the local personal address book and the Bluetooth-paired phone.

### SIP Subscription Failure Message

#### Problem

Subscription failure message displays on the phone screen.

#### Solution

Ensure that the sub parameter is correct. The sub parameter needs a correct SIP URI.

For example, the following string has an incomplete URI because the domain part is missing:

fnc=mwi;sub=4085283300;vid=1;

Check if the voicemail PLK monitors a voicemail account that is different from the associated extension’s user ID and the
                                       SIP proxy. If the associated extension's SIP proxy doesn't support this scenario, the subscription will fail.

For example, for extension1, the user ID is 4081009981. The PLK doesn't monitor 4081009981 but it monitors 4085283300 (a hunt
                                       group number or an ACD group number) although the PLK is associated with extension 1. In this case, the monitored voicemail
                                       user 4085283300 is different from the PLK's associated user 4081009981. If the SIP proxy of extension 1 doesn't support this
                                       scenario, the subscription will fail.

### Number of Voicemail Messages Doesn't Display

#### Problem

The phone doesn't display the number of voicemail messages in the voicemail PLK.

#### Solution 1

Ensure there are new messages in the monitored voicemail account.

#### Solution 2

Ensure the SIP proxy sends message-summary events to the phone.

In the phone’s Problem Report Tool (PRT) report, check if the SIP proxy sends a
                                 				message-summary event to the phone.

Find the NOTIFY message containing an message-summary event from the phone logs. If it is not found, the SIP proxy doesn’t
                                 send any message-summary event.

An example of a message-summary event:

6581 NOT May 20 19:54:04.162830 (31949:32029) voice- <===== Recv (UDP) [10.74.53.87]:5060 SIP MSG:: NOTIFY sip:4081009981@10.74.53.82:5065 SIP/2.0

Via: SIP/2.0/UDP 10.74.53.87:5060;branch=z9hG4bK-25824-1-2

From: "80000"<sip:8000@voicemail.sipurash.com>;tag=65737593823-1

To: <sip:4081009981@10.74.53.87>;tag=3855fbedd30b2464

Call-ID: 745bbebd-c35bc038@10.74.53.82

CSeq: 1001 NOTIFY

Max-Forwards: 20

Event: message-summary

Subscription-state: active;expires=3599

User-Agent: UMSIPVoicemail

Content-Length: 213

Content-Type: application/simple-message-summary

Messages-Waiting: yes

Message-Account: 4085283300@10.74.53.87

Voice-Message: 5/5 (2/3)

Fax-Message: 0/0 (0/0)

Pager-Message: 0/0 (0/0)

Multimedia-Message: 0/0 (0/0)

Text-Message: 0/0 (0/0)

None: 0/0 (0/0)

### Unable to Place a Call with Speed Dial for Voicemail Messages

#### Problem

The phone is unable to place a call to the specified speed-dial number.

#### Solution

Ensure that the sd parameter is included in the extension function script.

For example, the sd parameter is missing in this script: fnc=mwi;sub=4085283300@$PROXY;vid=1;ext=3000;

Ensure that the ext parameter is set .

For example, the ext parameter is not set in this function script: fnc=mwi+sd;sub=4085283300@$PROXY;vid=1;

### Failed to Sign Into a Voicemail Account

#### Problem

After the user press a voicemail PLK, the user cannot sign into the voicemail account automatically.

#### Solution

Access the voicemail server’s Interactive Voice Response (IVR) and determine the proper delay for the voicemail ID and PIN
                                       input. Insert or delete one or more commas if needed.

For example, the delay between the voicemail user ID and the PIN is too short: fnc=mwi+sd;sub=4085283300@$PROXY;vid=1;ext=3000 ,3300#,123456#;

Ensure that there is a space between the speed dial number and the DTMFs (containing the voicemail user ID and PIN).

For example, there is no space after "3000" in the string: fnc=mwi+sd;sub=4085283300@$PROXY;vid=1;ext=3000,3300#,123456#;

For example:

Scenario:

Extension 1 User ID is "4081009981" .

PLK function script is as follows:

fnc=mwi+sd;sub=4085283300@$PROXY;vid=1;ext=3000 ,3300#,123456#;

Result:

In this case, insert a star key (*) in the PLK function script, as shown below:

fnc=mwi+sd;sub=4085283300@$PROXY;vid=1;ext=3000 ,*,3300#,123456#;

### Voicemail PLK Options Don't Display on the Phone

#### Problem

After you press and hold the voicemail PLK for 2 seconds, the MWI or MWI + Speed dial , or both options don't display in the Select feature screen.

#### Solution

Ensure that mwi; or mwi;sd; is added to the Customizable PLK Options field under the General section from Voice > Att Console .

### Phone Failed to Upload the PRT Logs to the Remote Server

#### Problem

When you tried to generate the Problem Report Tool (PRT) logs on the phone, the generation of the PRT logs succeeded. However,
                                 the phone failed to upload the PRT logs to the remote server. The phone screen showed the Error: 109 or Report Problem together with an unavailable URL of a compressed file (for example, tar.gz).

#### Solution

Ensure that the web server is enabled on the phone, see Configure the Network from the Phone .

The Error: 109 indicates that the PRT upload rule is incorrect.

The Report problem indicates that the PRT upload rule is empty.

To resolve the issue, you must enter a correct PRT upload rule on the phone administration web page.

### Saved Passwords Become Invalid after Downgrade

#### Problem

You update certain passwords on a phone that uses Firmware Release 11.3(6) or later, and then downgrade the phone to Firmware
                                 Release 11.3(5) or older. In this scenario, the updated or saved passwords become invalid after the downgrade.

On the phone with Firmware Release 11.3(6) or later, even though you change the password back to the original one, this issue
                                 still occurs after the downgrade.

#### Solution

For the Firmware Release 11.3(6) or later, if you update the passwords, you must reconfigure the passwords to avoid the downgrade
                                 issue. If not, this issue doesn’t occur after the downgrade.

The following table shows the passwords that are affected by the downgrade issue:

Category

Password Type

System Configuration

User Password

Admin Password

Wi-Fi Profile (1-4)

Wi-Fi Password

WEP Key

PSK Passphrase

XSI Phone Service

Login Password

SIP Password

Broadsoft XMPP

Password

XML Service

XML Password

LDAP

Password

Call Feature Settings

Auth Page Password

Subscriber Information

Password

XSI Line Service

Login Password

TR-069

ACS Password

Connection Request Password

BACKUP ACS Password

### Failed to Onboard the Phone to Webex

#### Problem

A phone onboards with the EDOS device activation that uses phone MAC address, and it onboards to the Webex cloud. An administrator
                                 deletes the phone user from an organization in Webex Control Hub and then assigns the phone to another user. In this scenario,
                                 the phone fails to onboard to the Webex cloud even though it can connect to Webex Calling service. Specifically, the status
                                 of the phone in Control Hub is shown as "Offline".

#### Solution

Manually perform a factory reset on the phone after a user is deleted in Control Hub. For more information about how to perform
                                 a factory reset, see one of the following topics for details:

Factory Reset the Phone with the Keypad

Perform Factory Reset from Phone Menu

Factory Reset the Phone from Phone Web Page

## Phone Display Problems

Your users may see unusual screen displays. Use the following sections to troubleshoot the problem.

### Phone Displays Irregular Fonts

#### Problem

The phone screen has smaller fonts than expected or there are unusual characters displayed. Examples of unusual characters
                                 are letters from a different alphabet from the characters that the locale uses.

#### Cause

Possible causes are:

TFTP server does not have the correct set of locale and font files

XML files or other files are specified as a font file

The font and locale files did not download successfully.

#### Solution

Font files and locale files must be in the same directory.

Do not add or change files in the locale and font folder structure.

On the phone web page, select Admin Login > Advanced > Info > Status and scroll to the Locale Download Package section to verify that the locale and font files downloaded successfully. If they did not, try the download again.

### Phone Screen Displays Boxes Instead of Asian Characters

#### Problem

The phone is set for an Asian language, but the phone shows square boxes instead of Asian characters.

#### Cause

Possible causes are:

TFTP server does not have the correct set of locale and font files.

The font and locale files did not download successfully.

#### Solution

Font files and locale files must be in the same directory.

On the phone web page, select Admin Login > Advanced > Info > Status and scroll to the Locale Download Package section to verify that the locale and font files downloaded successfully. If they did not, try the download again.

## Report All Phone Issues from Phone Web Page

If you are working
                              		  with Cisco TAC to troubleshoot a problem, they typically require the logs from
                              		  the Problem Reporting Tool to help resolve the issue. You can generate PRT logs
                              		  using the phone web page and upload them to a remote log server.

### Before you begin

Access the phone
                              		  administration web page. See Access the Phone Web Interface .

Select Info > Debug
                                             				  Info .

In the Problem Reports section, click Generate PRT .

Enter the
                                       			 following information in the Report
                                          				Problem screen:

Enter the
                                             				  date that you experienced the problem in the Date field. The current date appears in this field
                                             				  by default.

Enter the
                                             				  time that you experienced the problem in the Time field. The current time appears in this field
                                             				  by default.

In the Select Problem drop-down list box, choose the
                                             				  description of the problem from the available options.

Click Submit in the Report
                                          				Problem screen.

The Submit
                                          				button is enabled only if you select a value in the Select Problem drop-down list box.

You get a
                                          				notification alert on the Phone Web page that indicates if the PRT upload was
                                          				successful or not.

## Report Phone Issues from Webex Control Hub

You can issue a phone problem report remotely from the Webex Control Hub, after the phone successfully onboards to Webex cloud.

### Before you begin

Access the customer view in https://admin.webex.com/ .

Access the phone administration web page. See Access the Phone Web Interface .

Problem Report Tool is configured successfully. URL specified in the PRT Upload Rule field is valid. See, Configure Problem Report Tool .

From the Webex Control Hub, generate the problem report of a phone.

For more information, see Webex for Cisco BroadWorks Solution Guide .

(Optional) Check the PRT generation status in any of the following ways:

Access the phone administration web page, select Info > Status > PRT Status . The PRT Generation Status shows that the Control Hub triggered PRT generation is successful and the PRT Upload Status shows that the uplaod is successful.

On the phone, select Applications > Status > Last problem report info . The screen displays the report status is uploaded. The report generation time, the report upload time, and the PRT file
                                                name have the same value as shown in the phone administration web page.

When you do not generate a PRT or you factory reset the phone, then Last problem report info doesn't appear.

Access the Webex Control Hub Help Desk and check the values of PRT generation. The values are identical with the values shown
                                                on the phone and on the phone administration web page.

## Factory Reset the Phone from Phone Web Page

You can factory reset the phone from the phone web page. The reset only happens if the phone is idle. If the phone is not
                              idle, the phone web page shows a message that the phone is busy and that you need to try again.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Info > Debug Info .

In the Factory Reset section, click Factory Reset .

Click Confirm factory reset .

## Reboot the Phone from the Phone Web Page

Enter the URL in a supported web browser.

You can enter URL in the format:

http://<Phone IP>/admin/reboot

where:

Phone IP = actual or VPN IP address of your phone.

/admin = path to access admin page of your phone.

reboot = command that you need to enter in the phone web page to reboot your phone.

After you enter the URL in the web browser, the phone reboots immediately.

## Reboot the Phone from the Webex Control Hub

You can reboot the phone from the Webex Control Hub remotely, after the phone successfully onboards to Webex cloud. You can
                              only reboot a phone that is in idle state. If it’s in use, such as in a call, the phone doesn’t reboot.

### Before you begin

Access the customer view in https://admin.webex.com/ .

Access the phone administration web page. See Access the Phone Web Interface .

From the Webex Control Hub, reboot a phone.

For more information, see Webex for Cisco BroadWorks Solution Guide .

(Optional) You can check the reboot reason from any of the following ways after the phone reboots successfully:

Access the phone administration web page, select Info > Status > Reboot History . The reboot reason shows as cloud triggered.

On the phone, select Applications > Status > Reboot history . The Reboot history screen shows that the reboot is cloud triggered.

## Report a Phone Problem Remotely

You can initiate a phone problem report remotely. The phone generates a problem report using the Cisco Problem Report Tool
                              (PRT), with the problem description "Remote PRT Trigger" . If you have configured an upload rule for problem reports, the phone uploads the problem report according to the upload
                              rule.

You can see the status of the problem report generation and upload on the phone administration web page. When a problem report
                              is successfully generated, you can download the problem report from the phone administration web page.

To initiate a phone problem report remotely, initiate a SIP-NOTIFY message from the server to the phone, with the Event specified as prt-gen .

## Capture Packets

For troubleshooting purposes you may need to gather a packet capture from an IP Phone.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Info > Debug Info .

In the Problem Report Tool section, click the Start Packet Capture button in the Packet Capture field.

Choose All to capture all packets that the phone receives and select Host IP Address to capture packets only when source or destination is the IP address of the phone.

Make phone calls to and from the selected phone.

When you want to stop the packet capture, click Stop Packet Capture .

Click Submit .

## Voice Quality Troubleshooting Tips

When you observe significant and persistent changes to metrics, use the following table for general troubleshooting information.

Metric Change

Condition

Conceal Ratio and Conceal Seconds increase significantly

Network impairment from packet loss or high jitter.

Conceal Ratio is near or at zero, but the voice quality is poor.

- Noise or distortion in the audio channel such as echo or audio levels.

- Tandem calls that undergo multiple encode/decode such as calls to a cellular network or calling card network.

- Acoustic problems coming from a speakerphone, handsfree cellular phone or wireless headset.

Check packet transmit (TxCnt) and packet receive (RxCnt) counters to verify that voice packets are flowing.

MOS LQK scores decrease significantly

Network impairment from packet loss or high jitter levels:

- Average MOS LQK decreases may indicate widespread and uniform impairment.

- Individual MOS LQK decreases may indicate bursty impairment.

Cross-check the conceal ratio and conceal seconds for evidence of packet loss and jitter.

MOS LQK scores increase significantly

- Check to see if the phone is using a different codec than expected (RxType and TxType).

- Check to see if the MOS LQK version changed after a firmware upgrade.

Voice quality metrics do not account for noise or distortion, only frame loss.

### Phone Behavior During Times of Network Congestion

Anything that degrades network performance can affect Cisco IP Phone audio quality, and in some cases, can cause a call to
                                 drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan

Attacks that occur on your network, such as a Denial of Service attack

To reduce or eliminate any adverse effects to the phones, schedule administrative network tasks during a time when the phones
                                 are not being used or exclude the phones from testing.

## Where to Find Additional Information

If you have additional questions about troubleshooting your phone, see the Cisco IP Phone 6800, 7800, and 8800 Series Multiplatform Phones Troubleshooting FAQ in the the following Cisco website:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/products-tech-notes-list.html

| Category | Password Type |
|---|---|
| System Configuration | User Password |
| Admin Password |
| Wi-Fi Profile (1-4) | Wi-Fi Password |
| WEP Key |
| PSK Passphrase |
| XSI Phone Service | Login Password |
| SIP Password |
| Broadsoft XMPP | Password |
| XML Service | XML Password |
| LDAP | Password |
| Call Feature Settings | Auth Page Password |
| Subscriber Information | Password |
| XSI Line Service | Login Password |
| TR-069 | ACS Password |
| Connection Request Password |
| BACKUP ACS Password |

| Step 1 | Select Info > Debug
                                             				  Info . |
|---|---|
| Step 2 | In the Problem Reports section, click Generate PRT . |
| Step 3 | Enter the
                                       			 following information in the Report
                                          				Problem screen: Enter the
                                             				  date that you experienced the problem in the Date field. The current date appears in this field
                                             				  by default. Enter the
                                             				  time that you experienced the problem in the Time field. The current time appears in this field
                                             				  by default. In the Select Problem drop-down list box, choose the
                                             				  description of the problem from the available options. |
| Step 4 | Click Submit in the Report
                                          				Problem screen. The Submit
                                          				button is enabled only if you select a value in the Select Problem drop-down list box. You get a
                                          				notification alert on the Phone Web page that indicates if the PRT upload was
                                          				successful or not. |

| Step 1 | From the Webex Control Hub, generate the problem report of a phone. For more information, see Webex for Cisco BroadWorks Solution Guide . |
|---|---|
| Step 2 | (Optional) Check the PRT generation status in any of the following ways: Access the phone administration web page, select Info > Status > PRT Status . The PRT Generation Status shows that the Control Hub triggered PRT generation is successful and the PRT Upload Status shows that the uplaod is successful. On the phone, select Applications > Status > Last problem report info . The screen displays the report status is uploaded. The report generation time, the report upload time, and the PRT file
                                                name have the same value as shown in the phone administration web page. When you do not generate a PRT or you factory reset the phone, then Last problem report info doesn't appear. Access the Webex Control Hub Help Desk and check the values of PRT generation. The values are identical with the values shown
                                                on the phone and on the phone administration web page. |

| Step 1 | Select Info > Debug Info . |
|---|---|
| Step 2 | In the Factory Reset section, click Factory Reset . |
| Step 3 | Click Confirm factory reset . |

| Enter the URL in a supported web browser. You can enter URL in the format: http://<Phone IP>/admin/reboot where: Phone IP = actual or VPN IP address of your phone. /admin = path to access admin page of your phone. reboot = command that you need to enter in the phone web page to reboot your phone. After you enter the URL in the web browser, the phone reboots immediately. |
|---|

| Step 1 | From the Webex Control Hub, reboot a phone. For more information, see Webex for Cisco BroadWorks Solution Guide . |
|---|---|
| Step 2 | (Optional) You can check the reboot reason from any of the following ways after the phone reboots successfully: Access the phone administration web page, select Info > Status > Reboot History . The reboot reason shows as cloud triggered. On the phone, select Applications > Status > Reboot history . The Reboot history screen shows that the reboot is cloud triggered. |

| To initiate a phone problem report remotely, initiate a SIP-NOTIFY message from the server to the phone, with the Event specified as prt-gen . |
|---|

| Step 1 | Select Info > Debug Info . |
|---|---|
| Step 2 | In the Problem Report Tool section, click the Start Packet Capture button in the Packet Capture field. |
| Step 3 | Choose All to capture all packets that the phone receives and select Host IP Address to capture packets only when source or destination is the IP address of the phone. |
| Step 4 | Make phone calls to and from the selected phone. |
| Step 5 | When you want to stop the packet capture, click Stop Packet Capture . |
| Step 6 | Click Submit . You see a file in the Capture File field. This file contains the filtered packets. |

| Metric Change | Condition |
|---|---|
| Conceal Ratio and Conceal Seconds increase significantly | Network impairment from packet loss or high jitter. |
| Conceal Ratio is near or at zero, but the voice quality is poor. | Noise or distortion in the audio channel such as echo or audio levels. Tandem calls that undergo multiple encode/decode such as calls to a cellular network or calling card network. Acoustic problems coming from a speakerphone, handsfree cellular phone or wireless headset. Check packet transmit (TxCnt) and packet receive (RxCnt) counters to verify that voice packets are flowing. |
| MOS LQK scores decrease significantly | Network impairment from packet loss or high jitter levels: Average MOS LQK decreases may indicate widespread and uniform impairment. Individual MOS LQK decreases may indicate bursty impairment. Cross-check the conceal ratio and conceal seconds for evidence of packet loss and jitter. |
| MOS LQK scores increase significantly | Check to see if the phone is using a different codec than expected (RxType and TxType). Check to see if the MOS LQK version changed after a firmware upgrade. |

| Note | Voice quality metrics do not account for noise or distortion, only frame loss. |
|---|---|