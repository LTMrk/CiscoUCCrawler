---
doc_id: www-cisco-com-c-en-us-td-docs-telepresence-cucm-cts-cucm-cts-admin-book-guide-cucm-cts-admin-cucm-cts-admin-satellite-ht-a1cb53286c
source_url: https://www.cisco.com/c/en/us/td/docs/telepresence/cucm_cts/cucm_cts_admin_book/guide/cucm_cts_admin/cucm_cts_admin_satellite.html
retrieved_at: 2026-08-17T00:10:11.844502+00:00
---

Cisco Unified Communications Manager Configuration Guide for the Cisco TelePresence System

# Cisco Unified Communications Manager Configuration Guide for the Cisco TelePresence System

Updated: April 15, 2014

Chapter: Satellite Licenses for the Cisco TelePresence System

## Chapter: Satellite Licenses for the Cisco TelePresence System

Revised: June 9, 2015, OL-21851-01

## Cisco TelePresence over Satellite Networks

The Cisco TelePresence over Satellite Networks solution extends the reach of Cisco TelePresence to remote, tactical locations where terrestrial bandwidth is not available. This solution incorporates existing Cisco TelePresence endpoint and infrastructure products with new software releases designed to function more effectively on poor, high-delay networks.

The following features and benefits are supported:

- Relaxed latency, jitter, and packet-loss thresholds allow the Cisco TelePresence meeting application to function effectively over poor, high-delay, real-world satellite networks.

- Qualification and testing of Type 1 encryption devices with the Cisco TelePresence application enable military-grade security for Cisco TelePresence calls.

- New network and environment recommendations provide guidance for remote, tactical, and even mobile deployments of the Cisco TelePresence System (CTS).

This section contains the following information:

### Supported CTS Devices

The CTS 500, CTS 1000, CTS 1100, and CTS 1300 endpoint models are supported as the remote endpoint on the far end of a satellite link.

Other endpoint models (CTS 3000 Series and CTS 3200 Series) have not been qualified to work on the remote side of a satellite link because the bandwidth needed for these three-screen systems quickly becomes cost-prohibitive to run over satellite networks. Any Cisco TelePresence endpoint or mix of endpoints (for a multipoint call) can be used on the terrestrial side of the satellite link.

### Supported CTS Software

You must be running CTS software version 1.5 or a later release on all Cisco TelePresence endpoints, Cisco TelePresence Multipoint Switches, and Cisco TelePresence Managers within your network to participate in a satellite call.

Note CTS Release Software is backward compatible up to two prior releases.

### Supported Satellite Bandwidth

You will need a minimum of 3-MB bandwidth (at 720p, good motion handling) in a single-channel-per-carrier (SCPC) configuration over a single-hop satellite link.

Note Because the Cisco TelePresence video and audio are traveling up to the satellite and back down to an earth station, significant (500 ms or more) latency is introduced into the signal. The result is noticeable delay in the conversation. In addition, atmospheric conditions or other interference may impact satellite-link performance and introduce jitter or packet loss into the call. The result may be noticeable degradation of the video quality.

CTS software release 1.5 and later releases support satellite deployment configurations that significantly raise the thresholds for network warning messages and call termination. When a satellite endpoint joins a call (point-to-point or multipoint), all other endpoints in the call negotiate the new threshold setting, so no one in the call gets warning messages or gets dropped just because a satellite-based endpoint joins the call.

For information about Cisco TelePresence service level requirements including bandwidth, latency (delay), jitter (variations in delay), and packet loss, see the Cisco TelePresence Network Systems 2.0 Design Guide on Cisco.com.

### Satellite Security

The Cisco TelePresence application  Transport Layer Security (TLS) and Secure Real-Time Transport Protocol (SRTP) encryption for signaling and media paths.

## Ordering a Satellite License

You can order satellite licenses when you initially order your CTS, or you can purchase separate satellite licenses to upgrade an existing CTS. Note the following details when you order a satellite license:

- The product authorization key (PAK) will either be physically delivered to your location or electronically delivered via E-mail.

- Product Number:

–	Physical: CTS-SATELLITE=

–	Electronic: L-CTS-SATELLITE=

## Loading a Satellite License on Unified CM

After you have received the satellite license, load it on Unified CM by following these steps:

Step 1	Load the license file into the Unified CM TFTP directory.

Step 2	After making sure that the license is available on your computer, log in to the Unified CM Administration interface and follow these steps:

a.	From the Navigation drop-down menu in the upper right corner, choose Cisco Unified OS Administration and click Go .

b.	Log in to Cisco Unified OS Administration interface .

c.	From the Software Upgrades drop-down menu , choose TFTP File Management and click the Upload File button. A dialog box appears.

d.	Browse to find the appropriate license and upload the license. Leave the Directory field blank.

Step 3	Restart the Unified CM TFTP server and complete these steps:

a.	From the Navigation drop-down menu, choose Cisco Unified Serviceability and click Go.

b.	Log into Cisco Unified Serviceability .

c. From the Tools drop-down menu , choose Control Center - Feature Services .

d.	In the Select Server box , choose the TFTP server from the drop-down menu and click Go .

e. In the CM Services box, click the Cisco TFTP radio button.

f.	Click Restart .

g.	Repeat Step c through Step e for all TFTP servers.

## Identifying the CTS Satellite Endpoints

After you have loaded the satellite license on Unified CM, identify the CTS satellite endpoints so that they can retrieve the satellite licenses.

To identify the CTS satellite endpoints using the Cisco Unified CM Administration interface:

Step 1	Log in to the Cisco Unified CM Administration interface.

Step 2 From the Device drop-down menu, choose Phone.

Step 3	Using the Find search fields, locate the CTS that will be used as a satellite endpoint.

Step 4 Click Reset to bring up a new dialog box, and then click Restart .

Step 5	Repeat Step 2 through Step 4 for each CTS satellite endpoint.

## Enabling the Satellite Feature

After the satellite license has been loaded on Unified CM, and the CTS satellite endpoints have been identified, you are ready to enable the satellite feature using CTS command-line interface (CLI) commands. For information about using CTS CLI commands, see the Cisco TelePresence System Command-Line Interface Reference Guide .

To enable the satellite feature:

Step 1	Check to see that the satellite license is available. From the CTS CLI admin command prompt, enter the following command:

admin: show license status

License feature status

satellite:

Valid license found

License feature is disabled

Feature is currently not running

Step 2	Enable the satellite feature using the following command:

admin: set license satellite enable

License for satellite feature changed to enabled

Step 3	Restart the calling services using the following command:

admin: utils service restart Calling

Calling_Services   Restarting...done

## Additional Licensing Information

See the Cisco TelePresence Administration Software Licensing Information page on Cisco.com.