---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-english-admin-guide-at9x-b-ata191-192-admin-mp-at9x-b-ata191-1-ffb1fae44e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/english/admin-guide/at9x_b_ata191-192-admin-mp/at9x_b_ata191-192-admin-mp_chapter_0110.html
retrieved_at: 2026-08-22T01:03:49.272216+00:00
---

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

# Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Updated: January 30, 2026

Chapter: Frequently Asked Questions

## Chapter: Frequently Asked Questions

# Frequently Asked Questions

## I Can't Connect to the Internet Through the ATA

Step 1

Make sure that the ATA is powered on. The Power/Sys LED should be solid green and not flashing.

If the Power LED is flashing, then power off all of your network devices, including the modem, the ATA, and the connected
                                          devices. Wait for 30 seconds. Then power on each device in the following order:

Cable or DSL modem

ATA

Connected Devices

Step 2

Check the cable connections. Ensure that the cable in the INTERNET (WAN) port is securely connected to the device that provides
                                       your Internet access, such as your modem or ADSL line. On the Cisco ATA 192, check the cable connection for the ETHERNET (LAN)
                                       port.

Step 3

Check the settings on the Network Setup > Internet Settings page. Verify that you entered the settings specified by your Internet Service provider.

## I Upgraded my Firmware and the ATA doesn't Work Properly

If the ATA is not working properly after an upgrade, you may need to perform a factory reset. Use the Administration > Factory Defaults page to reset the ATA to the default configuration. Alternatively, press and hold the RESET button for 10 seconds. All user-changeable non-default settings will be lost. This may include network and service provider
                              data.

## I Can't use the DSL Service to Connect Manually to the Internet

After you have installed the ATA, it will automatically connect to your service provider’s network, so you no longer need
                              to connect manually.

## There is no Dial Tone, and the Phone 1 or 2 LED is not Solid Green

Step 1

Make sure the telephone is connected to the appropriate port, PHONE 1 or 2.

Step 2

Disconnect the RJ-11 telephone cable from the PHONE port, and then reconnect it.

Step 3

Make sure your telephone is set to its tone setting (not pulse).

Step 4

Make sure your network has an active Internet connection.

Try to access the Internet, and check to see if the ATA WAN LED is flashing green. If you do not have a connection, then power
                                          off all of your network devices, including the modem, the ATA, and the computers. Wait 30 seconds. Then power on each device
                                          in the following order:

Cable or DSL modem

ATA

Computers and other devices

Step 5

Verify the settings on the Quick Setup page. Verify that you entered the account information and settings required by your
                                       service provider. On the Voice > Info page, Line 1 or Line 2 Status section, verify that the Registration State is registered. If the line is not registered, check
                                       with your ITSP to determine if additional settings are required.

## When I place an Internet Phone Call, the Audio Breaks Up

Consider the following possible causes and solutions:

Network activity—There may be heavy network activity, particularly if you are running a server or using a file sharing program.
                                    Try to limit network or Internet activity during Internet phone calls. For example, if you are running a file sharing program,
                                    files may be uploaded in the background even though you are not downloading any files, so make sure you exit the program before
                                    making Internet phone calls.

Bandwidth—There may insufficient bandwidth available for your Internet phone call. You may want to test your bandwidth by
                                    using one of the bandwidth tests available online. If necessary, access your Internet phone service account and reduce the
                                    bandwidth requirements for your service. For more information, refer to the website of your ITSP.

## When I Open a Web Browser, I am Prompted for a Username and Password. How can I Bypass this Prompt?

Launch the web browser and perform the following steps (these steps are specific to Internet Explorer but are similar for
                              other browsers).

Step 1

Select Tools > Internet Options .

Step 2

Click the Connections tab.

Step 3

Select Never dial a connection .

Step 4

Click OK .

## The DSL Telephone Line Does Not Fit in the ATA WAN (Internet) Port.

The ATA does not replace your modem. You need your DSL modem in order to use the ATA. Connect your telephone line to the DSL
                              modem.

## My Modem Doesn't Have an Ethernet Port

If your modem does not have an Ethernet port, then it is a modem for traditional dial-up service. To use the ATA, you need
                              a cable/DSL modem and a high-speed Internet connection.

## The ATA Doesn't Have a Coaxial port for the Cable Connection

The ATA does not replace your modem. You need your cable modem in order to use the ATA. Connect your cable connection to the
                              cable modem.

## Call Statistics are Not Available in the Server

When Call Statistics are not available in the server, check the following:.

Ensure the Call Statistics parameter is set to Yes in the web based configuration utility of ATA19x. You can check this parameter from Voice > SIP > RTP Parameters

In the configuration file, the parameter must have value:

| Step 1 | Make sure that the ATA is powered on. The Power/Sys LED should be solid green and not flashing. If the Power LED is flashing, then power off all of your network devices, including the modem, the ATA, and the connected
                                          devices. Wait for 30 seconds. Then power on each device in the following order: Cable or DSL modem ATA Connected Devices |
|---|---|
| Step 2 | Check the cable connections. Ensure that the cable in the INTERNET (WAN) port is securely connected to the device that provides
                                       your Internet access, such as your modem or ADSL line. On the Cisco ATA 192, check the cable connection for the ETHERNET (LAN)
                                       port. |
| Step 3 | Check the settings on the Network Setup > Internet Settings page. Verify that you entered the settings specified by your Internet Service provider. |

| Step 1 | Make sure the telephone is connected to the appropriate port, PHONE 1 or 2. |
|---|---|
| Step 2 | Disconnect the RJ-11 telephone cable from the PHONE port, and then reconnect it. |
| Step 3 | Make sure your telephone is set to its tone setting (not pulse). |
| Step 4 | Make sure your network has an active Internet connection. Try to access the Internet, and check to see if the ATA WAN LED is flashing green. If you do not have a connection, then power
                                          off all of your network devices, including the modem, the ATA, and the computers. Wait 30 seconds. Then power on each device
                                          in the following order: Cable or DSL modem ATA Computers and other devices |
| Step 5 | Verify the settings on the Quick Setup page. Verify that you entered the account information and settings required by your
                                       service provider. On the Voice > Info page, Line 1 or Line 2 Status section, verify that the Registration State is registered. If the line is not registered, check
                                       with your ITSP to determine if additional settings are required. |

| Step 1 | Select Tools > Internet Options . |
|---|---|
| Step 2 | Click the Connections tab. |
| Step 3 | Select Never dial a connection . |
| Step 4 | Click OK . |