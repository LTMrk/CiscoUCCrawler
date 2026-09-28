---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-dx-series-admin-1024-dx00-bk-c12f3ff5-00-cisco-dx-series-ag1024-dx00-bk-c12f-a42c46ed53
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/dx/series/admin/1024/DX00_BK_C12F3FF5_00_cisco-dx-series-ag1024/DX00_BK_C12F3FF5_00_cisco-dx-series-ag1024_chapter_01011.html
retrieved_at: 2026-08-21T04:58:35.118448+00:00
---

Cisco DX Series Administration Guide, Release 10.2(4)

# Cisco DX Series Administration Guide, Release 10.2(4)

Updated: June 25, 2015

Chapter: Customization

## Chapter: Customization

# Customization

## Wideband Codec Setup

By default, the G.722 codec is enabled for Cisco DX Series devices. If Cisco Unified Communications Manager is configured to use G.722 and if the far endpoint supports G.722, the call
		uses the G.722 codec instead of G.711 to connect.

This situation occurs regardless of whether the user has
		enabled a wideband headset or wideband handset, but if either the headset or
		handset is enabled, the user may notice greater audio sensitivity during the
		call. Greater sensitivity means improved audio clarity but also means that the party at the far end can hear more
		background noise, such as rustling
		papers or nearby conversations. Even without a wideband headset or handset,
		some users may prefer the additional sensitivity of G.722. Other users may find the additional sensitivity of G.722 distracting.

The Advertise G.722 Codec service parameter affects whether wideband support exists for all devices that register with this Cisco Unified Communications Manager server or for a specific device, depending on the Cisco Unified Communications Manager Administration window where the parameter is configured:

Advertise G.722 Codec field: From Cisco Unified Communications Manager Administration, choose System > Enterprise
				  Parameters . The default value of this enterprise
			 parameter is True , which means that all Cisco DX Series devices  that register to this Cisco Unified Communications Manager advertise G.722 to Cisco Unified Communications Manager . If each
			 endpoint in the attempted call supports G.722 in the capabilities set, Cisco Unified Communications Manager chooses that codec for the call whenever possible.

A specific device advertises the G.722 codec: From Cisco Unified Communications Manager Administration, choose Device > Phone .
			 The default value of this product-specific parameter is to use the value
			 that the enterprise parameter specifies. If you want to override this on a
			 per-device basis, choose Enabled or Disabled in the Advertise G.722 Codec
			 parameter in the Product Specific Configuration area of the Phone Configuration window.

## Operating
	 Modes

- Public Mode

- Simple Mode

- Enhanced Mode

The default is Simple Mode.

The following
		  table shows which features are available to the user in each mode.

- Set Operating Mode

### Set Operating Mode

We recommend that you disable Android Debug Bridge (ADB) for devices in Simple or Public Mode. Because the Email application is disabled in Simple or Public Mode, the user is unable to use the Problem Report Tool to email logs to the administrator. The logs must be collected from the serviceability web page.

## Default Wallpaper

You can control whether you or the user can set
the default wallpaper for a device from the
 Cisco Unified Communications Manager
 Administration page for the device.
Each type of DX Series device requires a different size wallpaper image, which stretches across 5 home screens.

- Assign Wallpaper Control

- Specify Default Wallpaper (DX70 and DX80)

- Specify Default Wallpaper (DX650)

### Assign Wallpaper Control

By default, the user is able to change the wallpaper on the device.

### Specify Default Wallpaper (DX70 and DX80)

We recommend an image resolution of 2985x1280 for Cisco DX70 and DX80 wallpaper. The devices crop the image to 2985x1080, meaning that the top and bottom 100px of a 2985x1280 image do not display on the device. The wallpaper is spread across five screens, and each screen is 1920px wide.

- Uncheck Enable End User Access to Phone Background Image Setting .

- Enter the wallpaper image filename in Background Image .

- Check Override Common Settings .

If you have a large network of endpoints apply the configuration to all devices, or restart the Cisco Unified Communications Manager server,  so that all the endpoints get the image.

### Specify Default Wallpaper (DX650)

We recommend an image resolution of 1600x1280 for Cisco DX650 wallpaper. The device crops the image to 1600x600 and the top and bottom 340px of a 1600x1280 image do not display on the device. The wallpaper is spread across five screens, and each screen is 1024px wide.

- Uncheck Enable End User Access to Phone Background Image Setting .

- Enter the wallpaper image filename in Background Image .

- Check Override Common Settings .

If you have a large network of endpoints, apply the configuration to all devices, or restart the Cisco Unified Communications Manager server  so that all the endpoints get the image.

## SSH Access

You can
		  enable or disable access to the SSH daemon through port 22. If you leave port 22
		  open, the device is vulnerable to Denial of Service (DoS) attacks. By
		  default, the SSH daemon is disabled.

- The Secure Shell User and
			 Secure Shell Password given in the Secure Shell Information section of Cisco Unified Communications Manager configuration

- The debug userid and
			 password

Common Phone
				Profile Configuration ( Device > Device
					 Settings > Common Phone Profile )

Phone
				Configuration ( Device > Phone
					 windows )

## Unified Communications Manager Endpoints Locale Installer

By default, devices are set up for the English (United States) locale. To use the devices in other locales, you must install the locale-specific version of the
		  Unified Communications Manager Endpoints Locale Installer on every Cisco Unified Communications Manager server in the cluster. The Locale Installer
		  installs the latest translated text for the phone user interface and
		  country-specific phone tones on your system so that they are available for the
		  devices.

To access the
		  Locale Installer required for a release, access http:/​/​software.cisco.com/​download/​navigator.html?mdfid=286037605&flowid=46245 , navigate to your device model, and
		  select the Unified Communications Manager Endpoints Locale Installer link.

For more
		  information, see the "Locale
			 Installer" section in the Cisco Unified
			 Communications Operating System Administration Guide .

The latest
			 Locale Installer may not be immediately available; continue to check the
			 website for updates.

## International Call Logging Support

If your phone system is configured for international call logging (calling party normalization), the call logs, redial, or call directory entries may display a "+" symbol to represent the international escape code for your location. Depending on the configuration for your phone system, the "+" may be replaced with the correct international dialing code, or you may need to edit the number before dialing to manually replace the "+" with the international escape code for your location. In addition, while the call log or directory entry may display the full international number for the received call, the phone display may show the shortened local version of the number, without international or country codes.

| Feature | Public Mode | Simple Mode | Enhanced Mode |
|---|---|---|---|
| Call application | Yes | Yes | Yes |
| Lock Screen | No | Yes | Yes |
| Network configuration | No | Yes | Yes |
| Home screen | No | Yes | Yes |
| Add or remove widgets and shortcuts | No | Yes | Yes |
| Visual Voicemail | No | Yes | Yes |
| Cisco User Data Service | Yes | Yes | Yes |
| Bluetooth | Yes | Yes | Yes |
| Set date and time | No | Yes | Yes |
| Recent applications list | No | Yes | Yes |
| External storage devices | No | No | Yes |
| Jabber IM | No | No | Yes |
| Android applications | No | No | Yes |

| Step 1 | Install the latest device packs on your Cisco Unified Communications Manager servers. See Release Notes for Cisco DX Series for more information on installing device packs. |
|---|---|
| Step 2 | In the Enterprise Phone Configuration window, the Common Phone Profile window, or the Phone Configuration window, set Device UI Profile to the desired mode. |
| Step 3 | Check Override Common Settings . The device reboots when you switch from Enhanced Mode to Public Mode or Simple Mode. The device also reboots when you switch from Public Mode or Simple Mode to Enhanced Mode. The device does not reboot when you switch between Public Mode and Simple Mode. |

| Step 1 | Go to Device > Device Settings > Common Phone Profile . |
|---|---|
| Step 2 | To restrict wallpaper control to the administrator, uncheck Enable End User Access to Phone Background Image Settings . |

| Step 1 | Upload the wallpaper image to the Desktops/2985x1080x24 folder on all nodes running the TFTP service. |
|---|---|
| Step 2 | Restart the TFTP service on all nodes running TFTP. |
| Step 3 | Go to the DX70 and DX80 Common Phone Profile in Cisco Unified Communications Manager administration and change the following: Uncheck Enable End User Access to Phone Background Image Setting . Enter the wallpaper image filename in Background Image . Check Override Common Settings . |
| Step 4 | Save and Apply the configuration to the common phone profile. |
| Step 5 | Go to the phone device page and apply the configuration to the devices you want the wallpaper to be loaded on. If you have a large network of endpoints apply the configuration to all devices, or restart the Cisco Unified Communications Manager server,  so that all the endpoints get the image. |

| Step 1 | Upload the wallpaper image to the Desktops/1600x1280x24 folder on all nodes running the TFTP service. |
|---|---|
| Step 2 | Restart the TFTP service on all nodes running TFTP. |
| Step 3 | Go to the DX650 Common Phone Profile in Cisco Unified Communications Manager administration and change the following: Uncheck Enable End User Access to Phone Background Image Setting . Enter the wallpaper image filename in Background Image . Check Override Common Settings . |
| Step 4 | Save and Apply the configuration to the common phone profile. |
| Step 5 | Go to the phone device page and apply the configuration to the devices you want the wallpaper to be loaded on. If you have a large network of endpoints, apply the configuration to all devices, or restart the Cisco Unified Communications Manager server  so that all the endpoints get the image. |

| Note | The latest
			 Locale Installer may not be immediately available; continue to check the
			 website for updates. |
|---|---|