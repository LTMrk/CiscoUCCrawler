---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-english-adminguide-p881-bk-c136782f-00-cisco-ip-phone-880-0288cb130a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/english/adminguide/P881_BK_C136782F_00_cisco-ip-phone-8800_series/P881_BK_C136782F_00_cisco-ip-phone-8811-8841_chapter_01010.html
retrieved_at: 2026-08-21T09:49:13.074862+00:00
---

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

Updated: November 6, 2025

Chapter: Cisco IP Phone Customization

## Chapter: Cisco IP Phone Customization

# Cisco IP Phone Customization

## Custom Phone
                        	 Rings

The phone ships with three ring tones that are
                              		  implemented in hardware: Sunshine, Chirp, Chirp1.

Cisco Unified Communications Manager also provides a default set of additional phone ring sounds that are implemented in software
                              as pulse code modulation (PCM) files. The PCM files, along with an XML file (named Ringlist-wb.xml) that describes the ring
                              list options that are available at your site, exist in the TFTP directory on each Cisco Unified Communications Manager server.

Attention

All file names are case sensitive. If you use Ringlist-wb.xml for the file name, the phone will not apply your changes.

For more information, see the "Custom Phone Rings and Backgrounds" chapter, Feature Configuration Guide for Cisco Unified Communications Manager for Cisco Unified Communications Manager release 12.0(1) or later.

## Custom Background Images

You can customize a Cisco IP phone with a background image or wallpaper. Customized wallpapers are a popular way to display
                           corporate logos or images and many organizations use them to make their phones stand out.

As of Firmware Release 12.7(1), you can customize your wallpaper on both your phones and your key expansion modules. But you
                           need one image for the phone and one image for the expansion module.

The phone analyzes the wallpaper colors, and changes the font colors and icons so you can read
                           them. If your wallpaper is dark, the phone changes the fonts and icons to white. If your
                           wallpaper is light, the phone displays the fonts and icons as black.

It is best to choose a simple image such as a solid color or pattern for your background. Avoid
                           high contrast images.

You add customized wallpaper in one of two ways:

Using the List file

Using a Common Phone Profile

If you want the user to be able to select your image from various wallpapers available on the phone, then modify the List
                           file. But if you want to push the image to the phone, then create or modify an existing Common Phone Profile.

Regardless of your approach, note the following:

Thumbnail images—139 pixels (width) by 109 pixels (height)

Cisco IP Phone 8800 Series—800 pixels by 480 pixels

Cisco IP Phone 8851 and 8861 Key Expansion Module with a dual LCD
                                          screen—320 by 480 pixels

Cisco IP Phone 8865 Key Expansion Module with a dual LCD screen—320
                                          by 480 pixels

Cisco IP Phone 8800 Key Expansion Module with a single LCD screen—272
                                          by 480 pixels

Upload the images, the thumbnails, and List file to your TFTP server. The
                                 directory is:

Cisco IP Phone 8800 Series—Desktops/800x480x24

Cisco IP Phone 8851 and 8861 Key Expansion Module with a dual LCD
                                       screen—Desktops/320x480x24

Cisco IP Phone 8865 Key Expansion Module with a dual LCD
                                       screen—Desktops/320x480x24

Cisco IP Phone 8800 Key Expansion Module with a single LCD
                                       screen—Desktops/272x480x24

After the upload is done, you restart the TFTP server.

If you don't want the user selecting their own wallpaper, then disable Enable End User Access to Phone Background Image
                                    Setting . Save and apply the phone profile. Restart the phones so
                                 your changes take effect.

For more information on customizing wallpaper, refer to the following documentation:

Customized Wallpapers Best Practices Cisco IP
                                    Phone 8800 Series ).

"Custom Phone Rings and Backgrounds" chapter, Feature Configuration Guide for Cisco Unified Communications Manager for Cisco Unified Communications Manager release 12.0(1) or later.

"Settings" chapter in the Cisco IP Phone 8800 Series User Guide .

## Set Up Wideband
                        	 Codec

By
                              		  default, the G.722 codec is enabled for the Cisco IP Phone.
                              		  If Cisco Unified Communications Manager is configured to use G.722 and if the
                              		  far endpoint supports G.722, the call connects using the G.722 codec in place
                              		  of G.711.

This
                              		  situation occurs regardless of whether the user has enabled a wideband headset
                              		  or wideband handset, but if either the headset or handset is enabled, the user
                              		  may notice greater audio sensitivity during the call. Greater sensitivity means
                              		  improved audio clarity but also means that the far endpoint can hear more
                              		  background noise: noise such as rustling papers or nearby conversations. Even
                              		  without a wideband headset or handset, some users may prefer the additional
                              		  sensitivity of G.722 distracting. Other users may prefer the additional
                              		  sensitivity of G.722.

The Advertise
                              		  G.722 and iSAC Codec service parameter affects whether wideband support exists
                              		  for all devices that register with this Cisco Unified Communications Manager
                              		  server or for a specific phone, depending on the Cisco Unified Communications
                              		  Manager Administration window where the parameter is configured.

Step 1

To configure
                                       			 wideband support for all devices:

From
                                             				  Cisco Unified Communications Manager Administration, choose System > Enterprise
                                                   						Parameters

Set the
                                             				  Advertise G.722 and iSAC Codec field

The
                                                					 default value of this enterprise parameter is True , which means that all Cisco IP Phone Models
                                                					 that register to this Cisco Unified Communications Manager advertise G.722 to
                                                					 Cisco Unified Communications Manager. If each endpoint in the attempted call
                                                					 supports G.722 in the capabilities set, Cisco Unified Communications Manager
                                                					 chooses that codec for the call whenever possible.

Step 2

To configure
                                       			 wideband support for a specific device:

From Cisco
                                             				  Unified Communications Manager Administration, choose Device > Phone .

Set the
                                             				  Advertise G.722 and iSAC Codec parameter in the Product Specific Configuration
                                             				  area.

The
                                                					 default value of this product-specific parameter is to use the value that the
                                                					 enterprise parameter specifies. If you want to override this on a per-phone
                                                					 basis, choose Enabled or Disabled

## Set Up Idle
                        	 Display

You can
                              		  specify an idle display (text only; text file size should not exceed 1M bytes)
                              		  that appears on the phone screen. The idle display is an XML service that the
                              		  phone invokes when the phone is idle (not in use) for a designated period and
                              		  no feature menu is open.

For
                              		  detailed instructions about creating and displaying the idle display, see Creating Idle
                                 			 URL Graphics on Cisco IP Phone at this URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_tech_note09186a00801c0764.shtml

In
                              		  addition, see the 
                              		  documentation for your particular Cisco Unified Communications Manager release for the following
                              		  information:

Specifying the
                                    				URL of the idle display XML service:

For a
                                          					 single phone: Idle field in the Phone Configuration window in Cisco Unified
                                          					 Communications Manager Administration.

For
                                          					 multiple phones simultaneously: URL Idle field in the Enterprise Parameters
                                          					 Configuration window, or the Idle field in the Bulk Administration Tool (BAT)

Specifying the length of time that the phone is not used before
                                    						  the idle display XML service is invoked:

For a
                                          					 single phone: Idle Timer field in the Phone configuration window in Cisco
                                          					 Unified Communications Manager Administration.

For
                                          					 multiple phones simultaneously: URL Idle Time field in the Enterprise
                                          					 Parameters Configuration window, or the Idle Timer field in the Bulk
                                          					 Administration Tool (BAT)

Step 1

In Cisco
                                       			 Unified Communications Manager Administration, select Device > Phone

Step 2

In the Idle field, enter the URL to the idle display XML Service.

Step 3

In the Idle
                                       			 Timer field, enter the time that the idle phone waits before displaying the
                                       			 idle display XML service.

Step 4

Select Save .

## Customize the Dial Tone

You can set up your phones so that users hear different dial tones for internal and external calls. Depending upon your needs,
                              you can choose from three dial tone options:

Default: A different dial tone for inside and outside calls.

Inside: The inside dial tone is used for all calls.

Outside: The outside dial tone is used for all calls.

Always Use Dial Tone is a required field on Cisco Unified Communications Manager.

Step 1

In Cisco Unified Communications Manager Administration, select System > Service Parameters .

Step 2

Select the appropriate Server.

Step 3

Select Cisco CallManager as the Service.

Step 4

Scroll to the Clusterwide Parameters pane.

Step 5

Set Always Use Dial Tone to one of the following:

- Outside

- Inside

- Default

Step 6

Select Save .

Step 7

Restart your phones.

| Attention | All file names are case sensitive. If you use Ringlist-wb.xml for the file name, the phone will not apply your changes. |
|---|---|

| Note | You can apply the phone background images in bulk with the Common
                                             Phone Profile . But bulk configuration requires you to disable Enable End User Access to Phone Background Image
                                             Setting . For more information on bulk configuration of
                                          background images, refer to the "Configure the Common Phone Profile" chapter of Customized Wallpapers Best Practices Cisco IP
                                             Phone 8800 Series .) |
|---|---|

| Step 1 | To configure
                                       			 wideband support for all devices: From
                                             				  Cisco Unified Communications Manager Administration, choose System > Enterprise
                                                   						Parameters Set the
                                             				  Advertise G.722 and iSAC Codec field The
                                                					 default value of this enterprise parameter is True , which means that all Cisco IP Phone Models
                                                					 that register to this Cisco Unified Communications Manager advertise G.722 to
                                                					 Cisco Unified Communications Manager. If each endpoint in the attempted call
                                                					 supports G.722 in the capabilities set, Cisco Unified Communications Manager
                                                					 chooses that codec for the call whenever possible. |
|---|---|
| Step 2 | To configure
                                       			 wideband support for a specific device: From Cisco
                                             				  Unified Communications Manager Administration, choose Device > Phone . Set the
                                             				  Advertise G.722 and iSAC Codec parameter in the Product Specific Configuration
                                             				  area. The
                                                					 default value of this product-specific parameter is to use the value that the
                                                					 enterprise parameter specifies. If you want to override this on a per-phone
                                                					 basis, choose Enabled or Disabled |

| Step 1 | In Cisco
                                       			 Unified Communications Manager Administration, select Device > Phone |
|---|---|
| Step 2 | In the Idle field, enter the URL to the idle display XML Service. |
| Step 3 | In the Idle
                                       			 Timer field, enter the time that the idle phone waits before displaying the
                                       			 idle display XML service. |
| Step 4 | Select Save . |

| Step 1 | In Cisco Unified Communications Manager Administration, select System > Service Parameters . |
|---|---|
| Step 2 | Select the appropriate Server. |
| Step 3 | Select Cisco CallManager as the Service. |
| Step 4 | Scroll to the Clusterwide Parameters pane. |
| Step 5 | Set Always Use Dial Tone to one of the following: Outside Inside Default |
| Step 6 | Select Save . |
| Step 7 | Restart your phones. |