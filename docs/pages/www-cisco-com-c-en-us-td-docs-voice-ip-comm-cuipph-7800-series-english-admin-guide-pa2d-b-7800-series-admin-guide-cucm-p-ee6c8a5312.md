---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-english-admin-guide-pa2d-b-7800-series-admin-guide-cucm-p-ee6c8a5312
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/english/admin-guide/pa2d_b_7800-series-admin-guide-cucm/pa2d_b_7800-series-admin-guide-cucm_chapter_01010.html
retrieved_at: 2026-08-21T13:26:25.626179+00:00
---

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

Updated: May 29, 2025

Chapter: Cisco IP Phone Customization

## Chapter: Cisco IP Phone Customization

# Cisco IP Phone Customization

## Custom Phone Ringtones

The Cisco IP Phone ships with two default ringtones that are implemented in hardware: Chirp1 and Chirp2. Cisco Unified Communications
                              Manager also provides a default set of additional phone ringtones that are implemented in software as pulse code modulation
                              (PCM) files. The PCM files, along with an XML file that describes the ring list options that are available at your site, exist
                              in the TFTP directory on each Cisco Unified Communications Manager server.

Attention

All file names are case sensitive. If you use the wrong case for the file name, the phone will not apply your changes.

For more information, see the "Custom Phone Rings and Backgrounds" chapter, Feature Configuration Guide for Cisco Unified Communications Manager .

## Set Up Wideband Codec

By default, the G.722 codec is enabled for the 
                              		phone. If Cisco Unified
                                 				Communications Manager is configured to use G.722 and if the far endpoint supports G.722, the call
                              		connects using the G.722 codec in place of G.711.

This situation occurs regardless of whether the user has
                              		enabled a wideband headset or wideband handset, but if either the headset or
                              		handset is enabled, the user may notice greater audio sensitivity during the
                              		call. Greater sensitivity means improved audio clarity but also means that the far endpoint can hear more
                              		background noise:  noise such as rustling
                              		papers or nearby conversations. Even without a wideband headset or handset,
                              		some users may prefer the additional sensitivity of G.722 distracting. Other users may prefer the additional sensitivity
                              of G.722.

The Advertise G.722 Codec service parameter affects whether wideband support exists for all devices that register with this
                              Cisco Unified Communications Manager server or for a specific phone, depending on the Cisco Unified
                                 				Communications Manager Administration window where the parameter is configured:

Step 1

In Cisco Unified
                                          				Communications Manager Administration , choose System > Enterprise
                                             				  Parameters .

Step 2

Set the Advertise G.722 Codec field.

The default value of this enterprise
                                          			 parameter is 
                                          			 Enabled, which means that all Cisco IP
                                          			 Phones  that register to this Cisco Unified Communications
                                          			 Manager advertise G.722 to Cisco Unified Communications Manager. If each
                                          			 endpoint in the attempted call supports G.722 in the capabilities set, Cisco
                                          			 Unified Communications Manager chooses that codec for the call whenever possible.

## Set Up Handset for 7811

The Cisco IP Phone 7811 ships with a narrowband or wideband handset. The administrator must configure the type of the handset
                              for the phone to work.

Step 1

In Cisco Unified Communications Manager Administration, choose Device > Phone .

Step 2

Locate the phone that you need to set up.

Step 3

In the Phone Configuration window set the Wideband Handset field:

For narrowband handset, set the field to Disabled or Use Phone Default .

For wideband handset, set the field to Enabled .

Step 4

Select Save .

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

| Attention | All file names are case sensitive. If you use the wrong case for the file name, the phone will not apply your changes. |
|---|---|

| Step 1 | In Cisco Unified
                                          				Communications Manager Administration , choose System > Enterprise
                                             				  Parameters . |
|---|---|
| Step 2 | Set the Advertise G.722 Codec field. The default value of this enterprise
                                          			 parameter is 
                                          			 Enabled, which means that all Cisco IP
                                          			 Phones  that register to this Cisco Unified Communications
                                          			 Manager advertise G.722 to Cisco Unified Communications Manager. If each
                                          			 endpoint in the attempted call supports G.722 in the capabilities set, Cisco
                                          			 Unified Communications Manager chooses that codec for the call whenever possible. |

| Step 1 | In Cisco Unified Communications Manager Administration, choose Device > Phone . |
|---|---|
| Step 2 | Locate the phone that you need to set up. |
| Step 3 | In the Phone Configuration window set the Wideband Handset field: For narrowband handset, set the field to Disabled or Use Phone Default . For wideband handset, set the field to Enabled . |
| Step 4 | Select Save . |

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