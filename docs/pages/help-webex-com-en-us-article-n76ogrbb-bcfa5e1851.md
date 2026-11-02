---
doc_id: help-webex-com-en-us-article-n76ogrbb-bcfa5e1851
source_url: https://help.webex.com/en-us/article/n76ogrbb
retrieved_at: 2026-11-02T13:12:27.488598+00:00
---

## Find information about your phone

Your administrator may ask for information about your phone. This information uniquely identifies the phone for troubleshooting purposes.

Before you begin

Select Settings .

If prompted, enter the password to access the Settings menu. You can get the password from your administrator.

Select About this device > Product information .

You can view the following information:

- Product name —Name that represents the phone.

- Serial number —Serial number of the phone.

- MAC address —Unique Media Access Control (MAC) address of the
              phone.

- IPv4 address —Internet Protocol Version 4 (IPv4) address of the
              phone.

- IPv6 address —Internet Protocol Version 6 (IPv6) address of the
              phone.

- Active server —IP address of the active Cisco Unified
              Communications Manager (CUCM) server.

- Standby server —IP address of the standby CUCM server.

- Software version —Version number of the phone firmware.

- Last upgrade —Information about the last upgrade or status of
              the software download progress.

- Hardware version —Version number of the phone hardware.

- VID —Version ID of the phone.

- Certificate —The status of certificate installation: Installed
              or Uninstalled. This item is available only on phones registered to Cisco BroadWorks
              or Webex Calling.

The status can be one of the following statuses:

- Aborted : The device has been provisioned through the
                  phone web page or the phone screen. The onboarding process through EDOS and GDS is
                  discarded.

- Acquired : The device has downloaded configuration from
                  the EDOS server.

- GDS-Acquired : The device has downloaded configuration
                  from the GDS server.

Select Back to exit the Product
            information screen.

## Check phone issues and diagnostics

If you are experiencing any issues with your phone (for example, network connection, phone registration, or phone upgrade), then you see an error message displayed under Issues .

Use the information and functions listed under the Issues and diagnostics section to collect data and troubleshoot any problems on your phone. Typically, this section contains the following functions:

Diagnostics

Function

Issues

Diagnostics

Select this item if you want to see the statistics information about the network, service, and calls. The specific statistics vary with the calling system that your phone is deployed to.

Report problem

Select this item if you want to collect and send your device logs to your administrator.

Press Settings .

If prompted, enter the password to access the Settings menu. You can get the password from your administrator.

Select Issues and diagnostics and go to Issues or Diagnostics as you need.

Select the field as you need to see the relevant statistics.

Select Back to return to the upper-level menu.

## Report problem from your phone

When you seek for help on phone issues from your administrator, send your device logs to the administrator for troubleshooting.

Press Settings .

If prompted, enter the password to access the Settings menu. You can get the password from your administrator.

Select Issues and diagnostics > Report problem .

Enter the date and time when the issue occurred.

By default, the current date and time are populated, you can further change them.

Choose a description from the Problem description list.

Select Submit .

After the report is sent, you can see the report file name and the submission
              time.

If your phone can't sent out the problem report, the report file is generated
                locally, and you can download the file from a given IP address.

## Check network status

Check the network connection details when you are troubleshooting a network issue. The Network status screen in the phone menu gives you the details about the Ethernet or Wi-Fi settings.

Cisco Desk Phone 9811, 9841, and 9851 don't support Wi-Fi network. The network status doesn't show wireless network related
          information.

Press Settings .

If prompted, enter the password to access the Settings menu. You can get the password from your administrator.

Do one of the following actions based on your phone model:

Select Network and service > Network status .

In the Network and service section,
            select Network connection .

## Check VPN statistics

You can check the VPN statistics on the phone screen. The VPN connection statistics
        contains the detailed information of current and past connections, and possible reasons of
        the failed connections (if existing).

This VPN connection is only available for the phones registered to Cisco Unified CM.

- Press Settings .

- If prompted, enter the password to access the Settings menu. You can get the password from your administrator.

- Select Issues and diagnostics > Diagnostics > Device status > VPN statistics .

- Select a VPN connection statistics (current, past, or failed) from the list. See the VPN connection statistics table for detailed information.

- VPN Rx bytes—Number of bytes that the phone received in the VPN
                    connection.

- VPN Rx packets—Number of packets that the phone received in the VPN
                    connection.

- VPN Tx bytes— Number of bytes that the phone transmitted in the VPN
                    connection.

- VPN Tx packets—Number of packets that the phone transmitted in the VPN
                    connection.

- Elapsed time—Total time that has elapsed since the connection is
                    established.

Select a time stamp from the list, and view the following information:

- VPN disconnected by user

- VPN concentrator address changed

- VPN authentication method changed

- Alternate TFTP changed

- Secure gateway initiated a VPN logout

- VPN configuration changed

- VPN auto network detection mode changed

- LSC changed

- VPN reconnection in progress

- SSL read/write error

- DTLS read/write error

- DTLS Dead Peer Detection error

- DTLS KeepAlive sending error

- DTLS Dead Peer Detection timeout

- SSL Dead Peer Detection timeout

- SSL Dead Peer Detection error

- VPN IP address lease expired

- VPN internal error

- VPN tunnel error

- VPN tunnel read error

- VPN IP address renewal failed

- SSL KeepAlive sending error

- SSL rekeying (reconnection) failed

- SSL rekeying (renegotiation) pending

- SSL rekeying (renegotiation) failed

- SSL rekeying (handshake) failed

- SSL rekeying failed

- DTLS rekeying failed

- SSL compression reset failed

- Unknown VPN failure

- Time closed—Time when the VPN connection is closed.

- Connection duration—Total length of time that the VPN connection remains.

Select a time stamp from the list, and view the following information:

The user credentials (user and
                          password, or just password) are invalid.

The phone
                          doesn't trust the VPN server's certificate.

The phone's certificate is
                          invalid. For example, it's been expired.

The phone can't connect to any VPN servers.

The VPN URL is longer than 255 characters.

The VPN client process on the phone is not
                          running.

The VPN utility process on the phone is not
                          running.

Unknown
                        reason

## Check device security status on the phone

Your phone checks the device security status automatically. If it detects potential security threats on the phone, the Issues and diagnostics menu can show the details of the issues. Based on the reported issues, your administrator can take operations to secure and harden your phone.

The device security status is available before the phone is registered to the call control system (Webex Calling or BroadWorks).

To view details of security issues on the phone screen, do the following:

Press Settings

Select Issues and diagnostics > Issues .

Currently, the device security report contains the following issues:

- Device authentication failed

- SoC tampering detected

- SSH enabled

- Telnet enabled

- Excessive web login attempts

- High UDP traffic detected

- Suspicious ICMP timpstamp requests

- Custom device certificate expiration

Contact your administrator for support to resolve the security issues.

## Restart your phone

You may need to restart your phone to resolve some issues or for some changes to take effect. A phone restart doesn't erase the phone settings. You can restart your phone either from the touch user interface.

Press Settings .

If prompted, enter the password to access the Settings menu. You can get the password from your administrator.

Do one of the following actions based on your phone model:

Select Restart and reset > Restart .

In the Restart and reset section,
            select Restart .

Select Restart in the prompt window.

## Reset security settings (UCM)

The security certificate reset option isn't available on phones that are registered to
          Cisco BroadWorks or Webex Calling.

If you want to change the phone registration from a Cisco Unified Communications Manager (Unified CM) server to another Cisco Unified CM server , we recommend that you delete the security settings on your phone. Security settings reset removes the Certificate Trust List (CTL) file. The phone gets the new CTL file from the new Unified CM cluster so that the phone can register successfully.

Press Settings .

If prompted, enter the password to access the Settings menu. You can get the password from your administrator.

Do one of the following actions based on your phone model:

Select Restart and reset > Reset security certificate .

In the Restart and reset section,
            select Reset security certificate .

Select Reset in the prompt window.

## Reset your phone to the factory settings

A factory reset clears all settings from your phone. You lose your current registration and all the configuration after a factory reset. You must register and set up your phone as you do for a new phone before you can use it again.

Reset your phone using the phone menu

You can use the phone menu to factory reset your phone. If you can't access to the menu from the phone screen, you can use the phone keypad to reset your phone .

Press Settings .

If prompted, enter the password to access the Settings menu. You can get the password from your administrator.

Do one of the following actions based on your phone model:

Select Restart and reset > Factory reset .

In the Restart and reset section,
            select Factory reset .

Select Reset in the prompt window to start the reset.

Your phone reboots when the reset completes.

Reset your phone with the keypad

Use these steps to reset the phone to the factory default settings using the keypad.

Unplug the phone:

- If using Power over Ethernet (PoE), unplug the Ethernet cable.

- If using the power cube, unplug the power cube.

Wait 5 seconds.

Press and hold # and plug the phone back in.

The Headset button, the Speaker button, and the Mute button light up.

As soon as the Mute button goes off, release # and press 123456789*0# in sequence.

When you press 1 , the Headset button goes off.

You have less than 15 seconds to finish pressing the keys. The phone goes into a normal startup if you don't finish the input before it times out or you press the keys out of sequence.

After you finish pressing these keys, the Mute button lights up, indicating the factory reset process has started.

Don’t power down the phone until it completes the factory reset process and the Welcome screen appears.

Reset your phone with the phone web page (BroadWorks or Webex Calling)

You can remote restore your phone to its default settings from the phone web page only when your phone is registered to Cisco BroadWorks or Webex Calling.

Reset your phone from the phone web page with one of the methods:

http://<Phone IP>/admin/factory-reset

where:

Phone IP = the actual IP address of your phone.

/admin = the path to access admin page of your phone.

/factory-reset = the command that you must enter in the phone web page to factory-reset your phone.

An administration access to the phone web page is required to use this method.

On the phone web page, select Admin Login > Advanced > Info > Debug Info .

Click Factory Reset in the Factory Reset section.

Click CONFIRM FACTORY RESET on the next page.

## Limited features available notification

When the connection to Webex cloud is unreachable or breaks, you will see the Limited features available notification at the header of the phone home screen. For example:

On Cisco Desk Phone 9871 and Cisco Video Phone 8875, only the warning icon displays on the home screen. You can tap the icon to show more information.

During this situation, phone gets connected to the Site Survivability Gateway (SGW) so that you can use at least basic calling features. SGW services are deployed within your local network, hence, the phone supports only basic calling features.

You can find out which lines are impacted by the issue under the Settings > Issues and diagnostics > Limited service . For example:

When you experience this issue, your administrator can help troubleshoot.

| 1 | Select Settings . |
|---|---|
| 2 | If prompted, enter the password to access the Settings menu. You can get the password from your administrator. |
| 3 | Select About this device > Product information . You can view the following information: Product name —Name that represents the phone. Serial number —Serial number of the phone. MAC address —Unique Media Access Control (MAC) address of the
              phone. IPv4 address —Internet Protocol Version 4 (IPv4) address of the
              phone. IPv6 address —Internet Protocol Version 6 (IPv6) address of the
              phone. Active server —IP address of the active Cisco Unified
              Communications Manager (CUCM) server. Standby server —IP address of the standby CUCM server. Software version —Version number of the phone firmware. Last upgrade —Information about the last upgrade or status of
              the software download progress. Hardware version —Version number of the phone hardware. VID —Version ID of the phone. Certificate —The status of certificate installation: Installed
              or Uninstalled. This item is available only on phones registered to Cisco BroadWorks
              or Webex Calling. Customization —The status of onboarding with EDOS or GDS. This
              item is available only on phones registered to Cisco BroadWorks or Webex Calling. The status can be one of the following statuses: Aborted : The device has been provisioned through the
                  phone web page or the phone screen. The onboarding process through EDOS and GDS is
                  discarded. Acquired : The device has downloaded configuration from
                  the EDOS server. GDS-Acquired : The device has downloaded configuration
                  from the GDS server. |
| 4 | Select Back to exit the Product
            information screen. |

| Diagnostics | Function |
|---|---|
| Issues | Select this item to view the detected issues. When issues are found, it shows the number of issues. If no issues are detected. it shows None. |
| Diagnostics | Select this item if you want to see the statistics information about the network, service, and calls. The specific statistics vary with the calling system that your phone is deployed to. |
| Report problem | Select this item if you want to collect and send your device logs to your administrator. |

| 1 | Press Settings . |
|---|---|
| 2 | If prompted, enter the password to access the Settings menu. You can get the password from your administrator. |
| 3 | Select Issues and diagnostics and go to Issues or Diagnostics as you need. |
| 4 | Select the field as you need to see the relevant statistics. |
| 5 | Select Back to return to the upper-level menu. |

| 1 | Press Settings . |
|---|---|
| 2 | If prompted, enter the password to access the Settings menu. You can get the password from your administrator. |
| 3 | Select Issues and diagnostics > Report problem . |
| 4 | Enter the date and time when the issue occurred. By default, the current date and time are populated, you can further change them. |
| 5 | Choose a description from the Problem description list. |
| 6 | Select Submit . After the report is sent, you can see the report file name and the submission
              time. If your phone can't sent out the problem report, the report file is generated
                locally, and you can download the file from a given IP address. |

| 1 | Press Settings . |
|---|---|
| 2 | If prompted, enter the password to access the Settings menu. You can get the password from your administrator. |
| 3 | Do one of the following actions based on your phone model: Select Network and service > Network status . In the Network and service section,
            select Network connection . |

| VPN connection statistics | Description |
|---|---|
| Current connection | VPN Rx bytes—Number of bytes that the phone received in the VPN
                    connection. VPN Rx packets—Number of packets that the phone received in the VPN
                    connection. VPN Tx bytes— Number of bytes that the phone transmitted in the VPN
                    connection. VPN Tx packets—Number of packets that the phone transmitted in the VPN
                    connection. Elapsed time—Total time that has elapsed since the connection is
                    established. |
| Past connections | Select a time stamp from the list, and view the following information: Reason closed—Possible reason for the event, including but no limited to: VPN disconnected by user VPN concentrator address changed VPN authentication method changed Alternate TFTP changed Secure gateway initiated a VPN logout VPN configuration changed VPN auto network detection mode changed LSC changed VPN reconnection in progress SSL read/write error DTLS read/write error DTLS Dead Peer Detection error DTLS KeepAlive sending error DTLS Dead Peer Detection timeout SSL Dead Peer Detection timeout SSL Dead Peer Detection error VPN IP address lease expired VPN internal error VPN tunnel error VPN tunnel read error VPN IP address renewal failed SSL KeepAlive sending error SSL rekeying (reconnection) failed SSL rekeying (renegotiation) pending SSL rekeying (renegotiation) failed SSL rekeying (handshake) failed SSL rekeying failed DTLS rekeying failed SSL compression reset failed Unknown VPN failure Time closed—Time when the VPN connection is closed. Connection duration—Total length of time that the VPN connection remains. |
| Failed connections | Select a time stamp from the list, and view the following information: Failure reason—Possible reason for the issue, including but no limited to: Failed to validate the user credentials. The user credentials (user and
                          password, or just password) are invalid. Failed to connect to VPN due to an invalid certificate. The phone
                          doesn't trust the VPN server's certificate. Failed to authenticate the phone certificate The phone's certificate is
                          invalid. For example, it's been expired. All concentrators failed The phone can't connect to any VPN servers. VPN URL too long The VPN URL is longer than 255 characters. VPN client not running The VPN client process on the phone is not
                          running. VPN process not running The VPN utility process on the phone is not
                          running. VPN connection momentarily lost. Retry in progress. Unknown
                        reason |

| 1 | Press Settings |
|---|---|
| 2 | Select Issues and diagnostics > Issues . Currently, the device security report contains the following issues: Device trust Device authentication failed SoC tampering detected Vulnerable configuration SSH enabled Telnet enabled Network anomaly event detected Excessive web login attempts High UDP traffic detected Suspicious ICMP timpstamp requests Certificate issue Custom device certificate expiration |
| 3 | Contact your administrator for support to resolve the security issues. |

| 1 | Press Settings . |
|---|---|
| 2 | If prompted, enter the password to access the Settings menu. You can get the password from your administrator. |
| 3 | Do one of the following actions based on your phone model: Select Restart and reset > Restart . In the Restart and reset section,
            select Restart . |
| 4 | Select Restart in the prompt window. |

| 1 | Press Settings . |
|---|---|
| 2 | If prompted, enter the password to access the Settings menu. You can get the password from your administrator. |
| 3 | Do one of the following actions based on your phone model: Select Restart and reset > Reset security certificate . In the Restart and reset section,
            select Reset security certificate . |
| 4 | Select Reset in the prompt window. |

| 1 | Press Settings . |
|---|---|
| 2 | If prompted, enter the password to access the Settings menu. You can get the password from your administrator. |
| 3 | Do one of the following actions based on your phone model: Select Restart and reset > Factory reset . In the Restart and reset section,
            select Factory reset . |
| 4 | Select Reset in the prompt window to start the reset. Your phone reboots when the reset completes. |

| 1 | Unplug the phone: If using Power over Ethernet (PoE), unplug the Ethernet cable. If using the power cube, unplug the power cube. |
|---|---|
| 2 | Wait 5 seconds. |
| 3 | Press and hold # and plug the phone back in. The Headset button, the Speaker button, and the Mute button light up. |
| 4 | As soon as the Mute button goes off, release # and press 123456789*0# in sequence. When you press 1 , the Headset button goes off. You have less than 15 seconds to finish pressing the keys. The phone goes into a normal startup if you don't finish the input before it times out or you press the keys out of sequence. After you finish pressing these keys, the Mute button lights up, indicating the factory reset process has started. Don’t power down the phone until it completes the factory reset process and the Welcome screen appears. |

| Reset your phone from the phone web page with one of the methods: In your web browser, enter the URL in the following format and click Confirm Factory Reset . http://<Phone IP>/admin/factory-reset where: Phone IP = the actual IP address of your phone. /admin = the path to access admin page of your phone. /factory-reset = the command that you must enter in the phone web page to factory-reset your phone. An administration access to the phone web page is required to use this method. On the phone web page, select Admin Login > Advanced > Info > Debug Info . Click Factory Reset in the Factory Reset section. Click CONFIRM FACTORY RESET on the next page. |
|---|

## Figuras

![the Settings key](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478218.png)

![For 9811, 9841,9851, and 9861](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/489001-490000/489180.png)

![Icon for 9871 and 8875 for common topics](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/485001-486000/485950.png)

![Settings button](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478218.png)

![the Settings hard key](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/300001-400000/370001-380000/371001-372000/371845.jpg)

![Limited features notification for Webex Calling Survivability on 9861](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487501.png)

![Warning icon on the phone home screen](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487502.png)

![Screenshot of the limited service issue on the desk phone](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487513.png)