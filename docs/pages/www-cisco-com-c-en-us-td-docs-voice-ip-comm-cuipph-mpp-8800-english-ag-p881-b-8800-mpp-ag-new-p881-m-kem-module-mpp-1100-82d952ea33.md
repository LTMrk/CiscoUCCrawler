---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8800-english-ag-p881-b-8800-mpp-ag-new-p881-m-kem-module-mpp-1100-82d952ea33
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8800/english/AG/p881_b_8800-mpp-ag_new/p881_m_kem-module-mpp-1100.html
retrieved_at: 2026-08-21T02:36:04.438025+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phone Administration Guide for Release 11.3(1) and Later

# Cisco IP Phone 8800 Series Multiplatform Phone Administration Guide for Release 11.3(1) and Later

Updated: August 18, 2020

Chapter: Cisco IP Phone Key Expansion Module

## Chapter: Cisco IP Phone Key Expansion Module

# Cisco IP Phone Key Expansion Module

## Cisco IP Phone Key Expansion Module Setup Overview

The Cisco IP Phone 8800 Key Expansion Module adds extra programmable buttons to the phone. The programmable buttons can be set up as phone speed-dial buttons, or phone
                              feature buttons.

Cisco IP Phone 8800 Key Expansion Module —Single LCD screen module, 18 line keys, 2 pages, two-column display only.

Cisco IP Phone 8851/8861 Key Expansion Module —Dual LCD screen module for audio phones, 14 line keys, 2 pages, one-column display only.

Cisco IP Phone 8865 Key Expansion Module —Dual LCD screen module for video phones, 14 line keys, 2 pages, one-column display only.

The Cisco IP Phone 8851/8861 Key Expansion Module and the Cisco IP Phone 8865 Key Expansion Module require Firmware Release 11.2(3) or later.

You can use more than one expansion module per phone. But each module must be the same type. You cannot mix Cisco IP Phone 8800 Key Expansion Module with a Cisco IP Phone 8851/8861 Key Expansion Module or with a Cisco IP Phone 8865 Key Expansion Module . You cannot mix audio expansion modules with video expansion modules. You also cannot use a video expansion module on an
                              audio phone or an audio expansion module on a video phone.

The following table lists the phones and the number of key expansion modules that each model supports.

Cisco IP Phone Model

Supported Number of Key Expansion Modules and Buttons

Cisco IP Phone 8851

2; single LCD screen, 18 line keys, two pages, providing 72 buttons

Cisco IP Phone 8861

3; single LCD screen, 18 line keys, two pages, providing 108 buttons

Cisco IP Phone 8865

3; single LCD screen, 18 line keys, two pages, providing 108 buttons,

Cisco IP Phone Model

Supported Numbers of Key Expansion Modules and Buttons

Cisco IP Phone 8851

2; dual LCD screen, 14 line keys, two pages, providing 56 buttons

Cisco IP Phone 8861

3; dual LCD screen, 14 line keys, two pages, providing 84 buttons

Cisco IP Phone 8865

3; dual LCD screen, 14 line keys, two pages, providing 84 buttons

## Key Expansion Module Power Information

If you use a key expansion module with your IP phone, then Power over Ethernet (PoE) is enough to power your expansion modules.
                              But, your phone must have an IP address in order to charge the expansion module.

A power cube is needed for smartphone or tablet charging when your key expansion module is attached.

A key expansion module uses 48V DC, 5W per module. If you are charging a smartphone or a tablet, note the following:

Side USB: Up to 500mA/2.5W charging

Back USB: Fast charging, Supports up to 2.1A/10.5W charging

Configuration

802.3af Power over Ethernet (PoE)

802.3at PoE

Cisco IP Phone Power Cube 4

8851 with 1 key expansion module

Yes

Yes

Yes

8851with 2 key expansion modules

No

No

See the third note below

Yes

8861 with 1 key expansion module

No

Yes

Yes

8861 with 2 key expansion modules

No

Yes

See the first note below

Yes

8861 with 3 key expansion modules

No

Yes

See the first note below

Yes

The fast-charging feature on the back USB does not work when more than one key expansion module is attached to a Cisco IP
                                                Phone 8861 using 802.3at PoE.

The fast-charging feature on the back USB doesn’t work when more than one key expansion module is attached to a Cisco IP Phone
                                                8861, unless Cisco Universal PoE (UPoE) is used.

Cisco IP Phone 8851 with 2 key expansion modules works on 802.3at PoE only with v08 or later hardware. You can find the phone
                                                version information on the lower back of the phone as part of the TAN and PID label. Version information is also located on
                                                the individual phone packaging.

Configuration

802.3af Power over Ethernet (PoE)

802.3at PoE

Cisco IP Phone Power Cube 4

8851 with 1 key expansion module

Yes

Yes

Yes

8851with 2 key expansion modules

No

Yes

See the third note below

Yes

8861 and 8865 with 1 key expansion module

No

Yes

Yes

8861 and 8865 with 2 key expansion modules

No

Yes

See the first note below

Yes

8861 and 8865 with 3 key expansion modules

No

Yes

See the first note below

Yes

The fast-charging feature on the back USB does not work when more than one key expansion module is attached to a Cisco IP
                                                Phone 8861 and 8865 using 802.3at PoE.

The fast-charging feature on the back USB doesn’t work when more than one key expansion module is attached to a Cisco IP Phone
                                                8861 and 8865, unless Cisco Universal PoE (UPoE) is used.

Cisco IP Phone 8851 with 2 key expansion modules works on 802.3at PoE only with v08 or later hardware. You can find the phone
                                                version information on the lower back of the phone as part of the TAN and PID label. Version information is also located on
                                                the individual phone packaging.

## Connect a Key Expansion Module to a Cisco IP Phone

Unplug the Ethernet cable from the phone.

If installed, remove the footstand from the phone.

Locate the accessory connector covers on the side of the phone.

This diagram shows the location.

Remove the two accessory connector covers, as shown in the diagram.

The slots are designed for the spine connector only. Insertion of other objects will cause permanent damage to the phone.

Position the phone so that the front of the phone faces up.

Connect one end of the key expansion module spine connector to the accessory connector on the Cisco IP Phone.

Align the spine connector with the accessory connector ports.

Install the connector in the orientation shown in the following diagrams.

Firmly press the spine connector into the phone.

This diagram shows the spine connector.

This diagram shows the installation of the spine connector.

Connect the other end of the spine connector to the key expansion module as shown in this diagram.

Align the spine connector with the key expansion module accessory connector ports.

Firmly press the key expansion module into the spine connector.

(Optional) Use a second key expansion module spine connector to connect the second key expansion module to the first key expansion module.

(Optional) Use a third key expansion module spine connector to connect the third key expansion module to the second key expansion module.

Use a screwdriver to fasten the screws into the phone.

This step ensures that the phone and key expansion module remain connected at all times. This diagram shows the location of
                                          the screw holes on the phone and one key expansion module.

Make sure that the screws are fully inserted into the phone and tightened.

If you lose any screws, the phone uses a standard M3 0.5x5.0mm screw.

(Optional) Install the footstands on the phone and on the key expansion module, and adjust both footstands to rest evenly on the work
                                       surface.

Plug the Ethernet cable into the phone.

## Connect Two or Three Key Expansion Modules to a Cisco IP Phone

Unplug the Ethernet cable from the phone.

If installed, remove the footstand from the phone.

Locate the accessory connector covers on the side of the phone.

This diagram shows the location.

Remove the two accessory connector covers, as shown in the diagram.

The slots are designed for the spine connector only. Insertion of other objects will cause permanent damage to the phone.

Position the phone so that the front of the phone faces up.

Connect one end of the key expansion module spine connector to the accessory connector on the Cisco IP Phone.

Align the spine connector with the accessory connector ports.

Install the connector in the orientation shown in the following diagrams.

Firmly press the spine connector into the phone.

This diagram shows the spine connector.

This diagram shows the installation of the spine connector.

Connect the other end of the spine connector to the key expansion module as shown in this diagram.

Align the spine connector with the key expansion module accessory connector ports.

Firmly press the key expansion module into the spine connector.

The first key expansion module is now connected to the Cisco IP Phone.

Use a second key expansion module spine connector to connect the second key expansion module to the first key expansion module.

Use a third key expansion module spine connector to connect the third key expansion module to the second (middle) key expansion
                                       module. This figure shows a Cisco IP Phone with three key expansion modules attached.

Use a screwdriver to fasten the screws into the phone and into each key expansion module.

This step ensures that the phone and key expansion modules remain connected at all times. This diagram shows the location
                                          of the screw holes.

Make sure that the screws are fully inserted into the phone and tightened.

(Optional) Install the footstands on the phone and on the key expansion modules, and adjust all footstands to rest evenly on the work
                                       surface.

Plug the Ethernet cable into the phone.

## Auto Detection of Key Expansion Modules

You can configure a new phone to auto-detect the maximum number of key expansion modules that it supports. For these phones,
                              the Number of Units field shows the maximum number of key expansion modules that the phone supports as the default value. When a user adds key
                              expansion modules to these phones, the module lights up and is enabled automatically. Default value of this field is 2 for
                              Cisco IP Phone 8851 and 3 for Cisco IP Phone 8861. Navigate to Admin Login > Advanced > Voice > Att Console to check the value of  the Number of Units field.

If your user has an older release phone and it is upgraded to the current release, you can change the cofiguration of the
                              phone so that when the user adds a key expansion module to the phone, it lights up and is enabled automatically.

## Configure the Key Expansion Module with the Phone Web Interface

You can add number of supported key expansion modules from the phone web interface.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Att Console .

From the Number of Units list, select the number of supported key expansion modules.

You can also configure the parameter in the configuration file (cfg.xml) by entering a string in the following format:

```
<Number_of_Units ua="na">2</Number_of_Units>
```

Default: 0

Click Submit All Changes .

## Access Key Expansion Module Setup

After you install one or more key expansion modules on the phone and configure them in the Configuration Utility page, the
                              phone automatically recognizes the key expansion modules.

When multiple key expansion modules are attached, they are numbered according to the order in which they connect to the phone:

Key expansion module 1 is the expansion module closest to the phone.

Key expansion module 2 is the expansion module in the middle.

Key expansion module 3 is the expansion module  farthest to the right.

When the phone automatically recognizes the key expansion modules, you can then choose the Show Details softkey for additional information about the selected key expansion module.

On the phone, press Applications .

Press Status > Accessories .

All properly installed and configured key expansion modules display in the list of accessories.

## Allocate a Key Expansion Module Type

You can assign the type of key expansion module that the phone supports:

BEKEM

CP-8800-Audio

CP-8800-Video

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Att Console .

Set the KEM Type from BEKEM, CP-8800-Audio, and CP-8800-Video

You can also configure the parameter in the configuration file (cfg.xml) by entering a string in the following format:

```
<KEM_Type ua="na">CP-8800-Video</KEM_Type>
```

Options: BEKEM, CP-8800-Audio, and CP-8800-Video

Default: CP-8800-Video

Press Submit All Changes .

## Allocate a Key Expansion Module Type with the Phone Menu

You can assign the type of key expansion module that the phone supports.

Press Applications .

Select User preferences > Attendant console preferences > KEM type .

Select the key expansion module type.

Press Save .

## Reset the Single LCD Screen Key Expansion Module

If you are having technical difficulties with your Cisco IP Phone 8800 Key Expansion Module, you can reset the module to
                              the factory default settings.

Restart the key expansion module by disconnecting the power source, waiting a few seconds, and then reconnecting it.

As the key expansion module powers up, press and hold Page 1 . As the LCD screen turns white, continue pressing Page 1 for at least one second.

Release Page 1 . The LEDs turn red.

Immediately press Page 2 and continue pressing Page 2 for at least one second.

Release Page 2 . The LEDs turn amber.

Press Lines 5 , 14 , 1 , 18 , 10 , and 9 in sequence.

The LCD screen turns blue. A spinning icon is displayed in the center of the screen.

The key expansion module resets.

## Configure a Speed Dial on a Key Expansion Module

You can configure speed dial on a key expansion module line. The user can then press the line key to call a frequently dialed
                              number.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code.

### Before you begin

Access the Phone Web Interface .

Select Voice > Att Console .

Select a key expansion module line key on which to enable the speed dial.

Enter a string in this format:

fnc=sd;ext=9999@$PROXY;vid=n;nme=xxxx

where:

fnc= sd means function=speed dial

ext= 9999 is the phone that the line key calls. Replace 9999 with numbers.

vid=n is the line index of the phone.

nme= XXXX is the name displayed on the phone for the speed-dial line key. Replace XXXX with a name.

You can also configure the parameter in the configuration file (cfg.xml) by entering a string in the following format:

<Unit_n_Key_m>fnc=sd;ext=9999@$PROXY;vid=n;nme=xxxx

Click Submit All Changes .

## Add Call Park on a
                        	 Key Expansion Module Line Key

You can add call
                              		  park to a Key Expansion Module line key to enable the user to temporarily store
                              		  calls to the same phone to which the Key Expansion Module is connected or to
                              		  store calls to a different phone. The user can also unpark the call from the
                              		  line key.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Att
                                             				  Console .

Select a Key
                                       			 Expansion Module line key on which to enable the call park.

Enter a string
                                       			 in this format:

```
fnc=park;sub=$USER@$PROXY;nme=CallPark-Slot1
```

```
fnc=prk;sub=$USER@$PROXY;nme=Call-Park1;orbit=<DN of primary line>
```

where:

fnc= prk means function=call park

sub= 999999 is the phone to which the call parks. Replace 999999 with a numbers.

nme= XXXX is the name displayed on the phone for the call park line key. Replace XXXX with a name.

```
<Unit_1_Key_1_ ua="na">fnc=prk;sub=$USER@$PROXY;nme=CallPark-Slot1</Unit_1_Key_1_>
```

Click Submit
                                          				All Changes .

## Configure the LCD
                        	 Brightness for a Key Expansion Module

You can configure the brightness of the LCD display on the key expansion module from the Attendant Console tab.

You can also configure the parameters in the phone configuration file with XML(cfg.xml) code.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Att
                                             				  Console .

Set the Attendant Console LCD Contrast to a value between 1
                                       			 and 15.

You can also configure the parameter in the configuration file (cfg.xml) by entering a string in the following format:

```
<Attendant_Console_LCD_Brightness ua="na">12</Attendant_Console_LCD_Brightness>
```

The higher the number, the greater the brightness on the key expansion module screen. The default value is 12. If no value
                                          is entered, the LCD brightness level is equal to 1, the dimmest value.

Click Submit All Changes .

## Configure the Busy
                        	 Lamp Field on a Key Expansion Module

You can configure
                              		  the busy lamp field on a key expansion module line so that the user can monitor
                              		  a coworker's availability to receive a call.

### Before you begin

Access the phone
                              		  administration web page. See Access the Phone Web Interface .

Select Voice > Att
                                             				  Console .

Select a key
                                       			 expansion module line key.

Enter a string
                                       			 in this format:

fnc=blf;sub=xxxx@$PROXY;usr=8888@$PROXY .

Where:

- fnc= blf means
                                                				  function=busy lamp field

- sub= the URI to which the
                                                				  SUBSCRIBE message is sent. This name must be identical to the name defined in
                                                				  the List URI: sip: parameter. xxxx is the name that is defined in List URI:
                                                				  sip: parameter. Replace xxxx with the exact defined name. $PROXY is the server.
                                                				  Replace $PROXY with the server address or name.

- usr= the BroadSoft user
                                                				  being monitored by BLF with 8888 as the phone being monitored. Replace 8888
                                                				  with the exact number of the monitored phone. $PROXY is the server. Replace
                                                				  $PROXY with the server address or name.

(Optional)  To enable the
                                       			 busy lamp field to work with both speed dial and call pickup enter a string in
                                       			 the following format:

fnc=blf+sd+cp;sub=xxxx@$PROXY;usr=yyyy@$PROXY .

Where:

sd= speed dial

cp= call
                                          				pickup

You can also
                                          				enable busy lamp field only with call pickup or speed dial. Enter the string in
                                          				the following format:

fnc=blf+cp;sub=xxxx@$PROXY;usr=yyyy@$PROXY

fnc=blf+sd;sub=xxxx@$PROXY;usr=yyyy@$PROXY

You can also configure the parameter in the configuration file (cfg.xml) by entering a string in the following format:

```
<Unit_1_Key_2_ ua="na">fnc=blf;ext=3252@$PROXY;nme=BLF_3252</Unit_1_Key_2_>
```

Click Submit
                                          				All Changes .

## Enable the User to Configure Features on Key Expansion Module Line Keys

You can enable the user to configure features on the line keys of the key expansion module. The user can then add any of the
                                 configured features to a disabled line key. For the supported features, see Configurable Features on Line Keys .

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Att Console .

In the General section, configure the Customizable PLK Options field with the codes of your desired features defined in Configurable Features on Line Keys .

Example : You configure this field with blf;shortcut;dnd; . The user can call up the feature list with a long-press on a key expansion module line key. The feature list looks like:

1 None

2 BLF presence

4 Menu shortcut

3 Do not disturb

The user can then select a feature or a menu shortcut to add to the line key.

```
<Customizable_PLK_Options ua="na">blf;shortcut;dnd;</Customizable_PLK_Options>
```

Click Submit All Changes .

## Add a Menu Shortcut to a Key Expansion Module Line Key

You can add a menu shortcut to a line key of the attached key expansion module. Then, the user can press the configured line
                              key to access the menu.

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Att Console .

Go to the Unit ( n ) section, where n is unit number of the key expansion module.

Configure the Unit n Key m field, where n is unit number of the key expansion module, and m is the key number.

```
fnc=shortcut;url=userpref;nme=User preferences
```

where:

fnc= shortcut means function=phone menu shortcut.

url= userpref is the menu to open with this line key. It's the User preferences menu in this example. For more shortcut mappings, see Menu Shortcuts Mapping on PLK and PSK .

nme= XXXX is the menu shortcut name displayed on the key expansion module screen. If you don't specify a display name, the
                                                line key displays the target menu item. In the example, the line key displays User preferences .

You can also configure the parameter in the configuration file (cfg.xml) with a string in this format:

```
<Unit_ n _Key_ m _ ua="na">fnc=shortcut;url=userpref;nme=User preferences</Unit_ n _Key_ m _>
```

where n is the unit number of the key expansion module, and m is the key number.

Click Submit All Changes .

## Add an Extended Feature to a Key Expansion Module Line Key

You can add a feature to a line key of the attached key expansion module. Then, the user can press the line key to access
                              the feature. For the supported features, see Configurable Features on Line Keys .

### Before you begin

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Att Console .

Go to the Unit ( n ) section, where n is unit number of the key expansion module.

Configure the Unit n Key m field, where n is unit number of the key expansion module, and m is the key number.

```
fnc=dnd
```

The user can turn on or off Do not disturb mode with the line key. For more feature codes, see Configurable Features on Line Keys .

You can also configure the parameter in the configuration file (cfg.xml) with a string in this format:

```
<Unit_ n _Key_ m _ ua="na">fnc=dnd</Unit_ n _Key_ m _>
```

where n is the unit number of the key expansion module, and m is the key number.

Click Submit All Changes .

## Configure the Voicemail PLK on a Key Expansion Module Button

You can configure the voicemail Programmable Line Key (PLK) on a Key Expansion Module button for the users to monitor a specified
                              voicemail account of a user or a group.

The voicemail PLK can monitor both the voicemail of an extension and the voicemail account of another user or a group. Monitoring
                              the voicemail of another user or a group requires the support from the SIP proxy.

For example, if the users belong to a customer service group. This feature allows the users to monitor both their  voicemails
                              and the group's voicemails.

If you configure speed dial for the same button, the users can press the button to make a speed dial to the assigned extension.

### Before you begin

One or more expansion modules have been installed on the phone.

Access the phone administration web page. See Access the Phone Web Interface .

Select Voice > Att Console .

Select an expansion module button on which to configure the voicemail PLK.

Enter a string in this format:

For MWI only:

```
fnc=mwi;sub=group_vm@domain;vid=1;nme=Group;
```

For MWI + Speed Dial:

```
fnc=mwi+sd;ext=8000@domain;sub=group_vm@domain;vid=1;nme=Group;
```

For MWI + speed dial + DTMF:

```
fnc=mwi+sd;ext=8000 ,4085283300#,123456#@domain;sub=group_vm@domain;vid=1;nme=Group;
```

For more information about the string syntax, see String Syntax for Voicemail PLK .

You can also configure this parameter in the phone configuration file (cfg.xml). The parameter is line-specific. Enter a string
                                          in this format:

```
<Unit_1_Key_1_ ua="na">fnc=mwi+sd;ext=8000 ,4085283300#,123456#@domain;
sub=group_vm@domain;vid=1;nme=Group;</Unit_1_Key_1_>
```

In the General section, add mwi or mwi;sd in the field Customizable PLK Options .

Parameter in the configuration file (cfg.xml):

```
<Customizable_PLK_Options ua="na">mwi;sd</Customizable_PLK_Options>
```

After the configuration, users can configure the corresponding features on the expansion module button.

Click Submit All Changes .

## Troubleshoot the Key Expansion Module

Open a CLI.

Enter the following command to enter debug mode:

debugsh

Enter ? to see all available commands and options.

Use the applicable commands and options to find the desired information.

To exit debug mode, press Ctrl-C .

## Key Expansion Module Does Not Go Through the Normal Start Up Process

### Problem

When you connect a key expansion module to a phone that is connected to a network port, the key expansion module doesn't start
                              up.

### Cause

Key expansion module type and the attached key expansion module don't match.

The phone has more than one type of expansion module connected.

Power over Ethernet (PoE) doesn't meet the required power-supply.

Connected number of key expansion modules exceed maximum "Number of Units".

### Solution

Change the phone to use the same type of expansion module.

Check the PoE the phone connected to.

Check if the unit number is bigger than the “Number of Units".

|  |  |
|---|---|
| Figure 2. Cisco IP Phone 8851/8861 Key Expansion Module with Dual Screen | Figure 3. Cisco IP Phone 8865 Key Expansion Module with Dual Screen |

| Note | The Cisco IP Phone 8851/8861 Key Expansion Module and the Cisco IP Phone 8865 Key Expansion Module require Firmware Release 11.2(3) or later. |
|---|---|

| Cisco IP Phone Model | Supported Number of Key Expansion Modules and Buttons |
|---|---|
| Cisco IP Phone 8851 | 2; single LCD screen, 18 line keys, two pages, providing 72 buttons |
| Cisco IP Phone 8861 | 3; single LCD screen, 18 line keys, two pages, providing 108 buttons |
| Cisco IP Phone 8865 | 3; single LCD screen, 18 line keys, two pages, providing 108 buttons, |

| Cisco IP Phone Model | Supported Numbers of Key Expansion Modules and Buttons |
|---|---|
| Cisco IP Phone 8851 | 2; dual LCD screen, 14 line keys, two pages, providing 56 buttons |
| Cisco IP Phone 8861 | 3; dual LCD screen, 14 line keys, two pages, providing 84 buttons |
| Cisco IP Phone 8865 | 3; dual LCD screen, 14 line keys, two pages, providing 84 buttons |

| Configuration | 802.3af Power over Ethernet (PoE) | 802.3at PoE | Cisco IP Phone Power Cube 4 |
|---|---|---|---|
| 8851 with 1 key expansion module | Yes | Yes | Yes |
| 8851with 2 key expansion modules | No | No See the third note below | Yes |
| 8861 with 1 key expansion module | No | Yes | Yes |
| 8861 with 2 key expansion modules | No | Yes See the first note below | Yes |
| 8861 with 3 key expansion modules | No | Yes See the first note below | Yes |

| Note | The fast-charging feature on the back USB does not work when more than one key expansion module is attached to a Cisco IP
                                                Phone 8861 using 802.3at PoE. The fast-charging feature on the back USB doesn’t work when more than one key expansion module is attached to a Cisco IP Phone
                                                8861, unless Cisco Universal PoE (UPoE) is used. Cisco IP Phone 8851 with 2 key expansion modules works on 802.3at PoE only with v08 or later hardware. You can find the phone
                                                version information on the lower back of the phone as part of the TAN and PID label. Version information is also located on
                                                the individual phone packaging. |
|---|---|

| Configuration | 802.3af Power over Ethernet (PoE) | 802.3at PoE | Cisco IP Phone Power Cube 4 |
|---|---|---|---|
| 8851 with 1 key expansion module | Yes | Yes | Yes |
| 8851with 2 key expansion modules | No | Yes See the third note below | Yes |
| 8861 and 8865 with 1 key expansion module | No | Yes | Yes |
| 8861 and 8865 with 2 key expansion modules | No | Yes See the first note below | Yes |
| 8861 and 8865 with 3 key expansion modules | No | Yes See the first note below | Yes |

| Note | The fast-charging feature on the back USB does not work when more than one key expansion module is attached to a Cisco IP
                                                Phone 8861 and 8865 using 802.3at PoE. The fast-charging feature on the back USB doesn’t work when more than one key expansion module is attached to a Cisco IP Phone
                                                8861 and 8865, unless Cisco Universal PoE (UPoE) is used. Cisco IP Phone 8851 with 2 key expansion modules works on 802.3at PoE only with v08 or later hardware. You can find the phone
                                                version information on the lower back of the phone as part of the TAN and PID label. Version information is also located on
                                                the individual phone packaging. |
|---|---|

| Step 1 | Unplug the Ethernet cable from the phone. |
|---|---|
| Step 2 | If installed, remove the footstand from the phone. |
| Step 3 | Locate the accessory connector covers on the side of the phone. This diagram shows the location. |
| Step 4 | Remove the two accessory connector covers, as shown in the diagram. Caution The slots are designed for the spine connector only. Insertion of other objects will cause permanent damage to the phone. | Caution | The slots are designed for the spine connector only. Insertion of other objects will cause permanent damage to the phone. |
| Caution | The slots are designed for the spine connector only. Insertion of other objects will cause permanent damage to the phone. |
| Step 5 | Position the phone so that the front of the phone faces up. |
| Step 6 | Connect one end of the key expansion module spine connector to the accessory connector on the Cisco IP Phone. Align the spine connector with the accessory connector ports. Note Install the connector in the orientation shown in the following diagrams. Firmly press the spine connector into the phone. This diagram shows the spine connector. This diagram shows the installation of the spine connector. | Note | Install the connector in the orientation shown in the following diagrams. |
| Note | Install the connector in the orientation shown in the following diagrams. |
| Step 7 | Connect the other end of the spine connector to the key expansion module as shown in this diagram. Align the spine connector with the key expansion module accessory connector ports. Firmly press the key expansion module into the spine connector. |
| Step 8 | (Optional) Use a second key expansion module spine connector to connect the second key expansion module to the first key expansion module. |
| Step 9 | (Optional) Use a third key expansion module spine connector to connect the third key expansion module to the second key expansion module. |
| Step 10 | Use a screwdriver to fasten the screws into the phone. This step ensures that the phone and key expansion module remain connected at all times. This diagram shows the location of
                                          the screw holes on the phone and one key expansion module. Note Make sure that the screws are fully inserted into the phone and tightened. If you lose any screws, the phone uses a standard M3 0.5x5.0mm screw. | Note | Make sure that the screws are fully inserted into the phone and tightened. If you lose any screws, the phone uses a standard M3 0.5x5.0mm screw. |
| Note | Make sure that the screws are fully inserted into the phone and tightened. If you lose any screws, the phone uses a standard M3 0.5x5.0mm screw. |
| Step 11 | (Optional) Install the footstands on the phone and on the key expansion module, and adjust both footstands to rest evenly on the work
                                       surface. |
| Step 12 | Plug the Ethernet cable into the phone. |

| Caution | The slots are designed for the spine connector only. Insertion of other objects will cause permanent damage to the phone. |
|---|---|

| Note | Install the connector in the orientation shown in the following diagrams. |
|---|---|

| Note | Make sure that the screws are fully inserted into the phone and tightened. If you lose any screws, the phone uses a standard M3 0.5x5.0mm screw. |
|---|---|

| Step 1 | Unplug the Ethernet cable from the phone. |
|---|---|
| Step 2 | If installed, remove the footstand from the phone. |
| Step 3 | Locate the accessory connector covers on the side of the phone. This diagram shows the location. |
| Step 4 | Remove the two accessory connector covers, as shown in the diagram. Caution The slots are designed for the spine connector only. Insertion of other objects will cause permanent damage to the phone. | Caution | The slots are designed for the spine connector only. Insertion of other objects will cause permanent damage to the phone. |
| Caution | The slots are designed for the spine connector only. Insertion of other objects will cause permanent damage to the phone. |
| Step 5 | Position the phone so that the front of the phone faces up. |
| Step 6 | Connect one end of the key expansion module spine connector to the accessory connector on the Cisco IP Phone. Align the spine connector with the accessory connector ports. Note Install the connector in the orientation shown in the following diagrams. Firmly press the spine connector into the phone. This diagram shows the spine connector. This diagram shows the installation of the spine connector. | Note | Install the connector in the orientation shown in the following diagrams. |
| Note | Install the connector in the orientation shown in the following diagrams. |
| Step 7 | Connect the other end of the spine connector to the key expansion module as shown in this diagram. Align the spine connector with the key expansion module accessory connector ports. Firmly press the key expansion module into the spine connector. The first key expansion module is now connected to the Cisco IP Phone. |
| Step 8 | Use a second key expansion module spine connector to connect the second key expansion module to the first key expansion module. |
| Step 9 | Use a third key expansion module spine connector to connect the third key expansion module to the second (middle) key expansion
                                       module. This figure shows a Cisco IP Phone with three key expansion modules attached. |
| Step 10 | Use a screwdriver to fasten the screws into the phone and into each key expansion module. This step ensures that the phone and key expansion modules remain connected at all times. This diagram shows the location
                                          of the screw holes. Note Make sure that the screws are fully inserted into the phone and tightened. | Note | Make sure that the screws are fully inserted into the phone and tightened. |
| Note | Make sure that the screws are fully inserted into the phone and tightened. |
| Step 11 | (Optional) Install the footstands on the phone and on the key expansion modules, and adjust all footstands to rest evenly on the work
                                       surface. |
| Step 12 | Plug the Ethernet cable into the phone. |

| Caution | The slots are designed for the spine connector only. Insertion of other objects will cause permanent damage to the phone. |
|---|---|

| Note | Install the connector in the orientation shown in the following diagrams. |
|---|---|

| Note | Make sure that the screws are fully inserted into the phone and tightened. |
|---|---|

| Step 1 | Select Voice > Att Console . |
|---|---|
| Step 2 | From the Number of Units list, select the number of supported key expansion modules. You can also configure the parameter in the configuration file (cfg.xml) by entering a string in the following format: <Number_of_Units ua="na">2</Number_of_Units> Default: 0 |
| Step 3 | Click Submit All Changes . |

| Step 1 | On the phone, press Applications . |
|---|---|
| Step 2 | Press Status > Accessories . All properly installed and configured key expansion modules display in the list of accessories. |

| Step 1 | Select Voice > Att Console . |
|---|---|
| Step 2 | Set the KEM Type from BEKEM, CP-8800-Audio, and CP-8800-Video You can also configure the parameter in the configuration file (cfg.xml) by entering a string in the following format: <KEM_Type ua="na">CP-8800-Video</KEM_Type> Options: BEKEM, CP-8800-Audio, and CP-8800-Video Default: CP-8800-Video |
| Step 3 | Press Submit All Changes . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select User preferences > Attendant console preferences > KEM type . |
| Step 3 | Select the key expansion module type. |
| Step 4 | Press Save . |

| Step 1 | Restart the key expansion module by disconnecting the power source, waiting a few seconds, and then reconnecting it. |
|---|---|
| Step 2 | As the key expansion module powers up, press and hold Page 1 . As the LCD screen turns white, continue pressing Page 1 for at least one second. |
| Step 3 | Release Page 1 . The LEDs turn red. |
| Step 4 | Immediately press Page 2 and continue pressing Page 2 for at least one second. |
| Step 5 | Release Page 2 . The LEDs turn amber. |
| Step 6 | Press Lines 5 , 14 , 1 , 18 , 10 , and 9 in sequence. The LCD screen turns blue. A spinning icon is displayed in the center of the screen. The key expansion module resets. |

| Step 1 | Select Voice > Att Console . |
|---|---|
| Step 2 | Select a key expansion module line key on which to enable the speed dial. |
| Step 3 | Enter a string in this format: fnc=sd;ext=9999@$PROXY;vid=n;nme=xxxx where: fnc= sd means function=speed dial ext= 9999 is the phone that the line key calls. Replace 9999 with numbers. vid=n is the line index of the phone. nme= XXXX is the name displayed on the phone for the speed-dial line key. Replace XXXX with a name. You can also configure the parameter in the configuration file (cfg.xml) by entering a string in the following format: <Unit_n_Key_m>fnc=sd;ext=9999@$PROXY;vid=n;nme=xxxx |
| Step 4 | Click Submit All Changes . |

| Step 1 | Select Voice > Att
                                             				  Console . |
|---|---|
| Step 2 | Select a Key
                                       			 Expansion Module line key on which to enable the call park. |
| Step 3 | Enter a string
                                       			 in this format: For a private line, enter fnc=park;sub=$USER@$PROXY;nme=CallPark-Slot1 For a shared line, enter fnc=prk;sub=$USER@$PROXY;nme=Call-Park1;orbit=<DN of primary line> where: fnc= prk means function=call park sub= 999999 is the phone to which the call parks. Replace 999999 with a numbers. nme= XXXX is the name displayed on the phone for the call park line key. Replace XXXX with a name. You can also configure the line-specific parameter in the configuration file (cfg.xml). Enter a string in the following format: <Unit_1_Key_1_ ua="na">fnc=prk;sub=$USER@$PROXY;nme=CallPark-Slot1</Unit_1_Key_1_> |
| Step 4 | Click Submit
                                          				All Changes . |

| Step 1 | Select Voice > Att
                                             				  Console . |
|---|---|
| Step 2 | Set the Attendant Console LCD Contrast to a value between 1
                                       			 and 15. You can also configure the parameter in the configuration file (cfg.xml) by entering a string in the following format: <Attendant_Console_LCD_Brightness ua="na">12</Attendant_Console_LCD_Brightness> The higher the number, the greater the brightness on the key expansion module screen. The default value is 12. If no value
                                          is entered, the LCD brightness level is equal to 1, the dimmest value. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Att
                                             				  Console . |
|---|---|
| Step 2 | Select a key
                                       			 expansion module line key. |
| Step 3 | Enter a string
                                       			 in this format: fnc=blf;sub=xxxx@$PROXY;usr=8888@$PROXY . Where: fnc= blf means
                                                				  function=busy lamp field sub= the URI to which the
                                                				  SUBSCRIBE message is sent. This name must be identical to the name defined in
                                                				  the List URI: sip: parameter. xxxx is the name that is defined in List URI:
                                                				  sip: parameter. Replace xxxx with the exact defined name. $PROXY is the server.
                                                				  Replace $PROXY with the server address or name. usr= the BroadSoft user
                                                				  being monitored by BLF with 8888 as the phone being monitored. Replace 8888
                                                				  with the exact number of the monitored phone. $PROXY is the server. Replace
                                                				  $PROXY with the server address or name. |
| Step 4 | (Optional)  To enable the
                                       			 busy lamp field to work with both speed dial and call pickup enter a string in
                                       			 the following format: fnc=blf+sd+cp;sub=xxxx@$PROXY;usr=yyyy@$PROXY . Where: sd= speed dial cp= call
                                          				pickup You can also
                                          				enable busy lamp field only with call pickup or speed dial. Enter the string in
                                          				the following format: fnc=blf+cp;sub=xxxx@$PROXY;usr=yyyy@$PROXY fnc=blf+sd;sub=xxxx@$PROXY;usr=yyyy@$PROXY You can also configure the parameter in the configuration file (cfg.xml) by entering a string in the following format: <Unit_1_Key_2_ ua="na">fnc=blf;ext=3252@$PROXY;nme=BLF_3252</Unit_1_Key_2_> |
| Step 5 | Click Submit
                                          				All Changes . |

| Step 1 | Select Voice > Att Console . |
|---|---|
| Step 2 | In the General section, configure the Customizable PLK Options field with the codes of your desired features defined in Configurable Features on Line Keys . Example : You configure this field with blf;shortcut;dnd; . The user can call up the feature list with a long-press on a key expansion module line key. The feature list looks like: 1 None 2 BLF presence 4 Menu shortcut 3 Do not disturb The user can then select a feature or a menu shortcut to add to the line key. You can also configure this parameter in the configuration file (cfg.xml) with a string in this format: <Customizable_PLK_Options ua="na">blf;shortcut;dnd;</Customizable_PLK_Options> |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Att Console . |
|---|---|
| Step 2 | Go to the Unit ( n ) section, where n is unit number of the key expansion module. |
| Step 3 | Configure the Unit n Key m field, where n is unit number of the key expansion module, and m is the key number. fnc=shortcut;url=userpref;nme=User preferences where: fnc= shortcut means function=phone menu shortcut. url= userpref is the menu to open with this line key. It's the User preferences menu in this example. For more shortcut mappings, see Menu Shortcuts Mapping on PLK and PSK . nme= XXXX is the menu shortcut name displayed on the key expansion module screen. If you don't specify a display name, the
                                                line key displays the target menu item. In the example, the line key displays User preferences . You can also configure the parameter in the configuration file (cfg.xml) with a string in this format: <Unit_ n _Key_ m _ ua="na">fnc=shortcut;url=userpref;nme=User preferences</Unit_ n _Key_ m _> where n is the unit number of the key expansion module, and m is the key number. |
| Step 4 | Click Submit All Changes . |

| Step 1 | Select Voice > Att Console . |
|---|---|
| Step 2 | Go to the Unit ( n ) section, where n is unit number of the key expansion module. |
| Step 3 | Configure the Unit n Key m field, where n is unit number of the key expansion module, and m is the key number. fnc=dnd The user can turn on or off Do not disturb mode with the line key. For more feature codes, see Configurable Features on Line Keys . You can also configure the parameter in the configuration file (cfg.xml) with a string in this format: <Unit_ n _Key_ m _ ua="na">fnc=dnd</Unit_ n _Key_ m _> where n is the unit number of the key expansion module, and m is the key number. |
| Step 4 | Click Submit All Changes . |

| Step 1 | Select Voice > Att Console . |
|---|---|
| Step 2 | Select an expansion module button on which to configure the voicemail PLK. |
| Step 3 | Enter a string in this format: For MWI only: fnc=mwi;sub=group_vm@domain;vid=1;nme=Group; For MWI + Speed Dial: fnc=mwi+sd;ext=8000@domain;sub=group_vm@domain;vid=1;nme=Group; For MWI + speed dial + DTMF: fnc=mwi+sd;ext=8000 ,4085283300#,123456#@domain;sub=group_vm@domain;vid=1;nme=Group; For more information about the string syntax, see String Syntax for Voicemail PLK . You can also configure this parameter in the phone configuration file (cfg.xml). The parameter is line-specific. Enter a string
                                          in this format: <Unit_1_Key_1_ ua="na">fnc=mwi+sd;ext=8000 ,4085283300#,123456#@domain;
sub=group_vm@domain;vid=1;nme=Group;</Unit_1_Key_1_> |
| Step 4 | In the General section, add mwi or mwi;sd in the field Customizable PLK Options . Parameter in the configuration file (cfg.xml): <Customizable_PLK_Options ua="na">mwi;sd</Customizable_PLK_Options> After the configuration, users can configure the corresponding features on the expansion module button. |
| Step 5 | Click Submit All Changes . |

| Step 1 | Open a CLI. |
|---|---|
| Step 2 | Enter the following command to enter debug mode: debugsh |
| Step 3 | Enter ? to see all available commands and options. |
| Step 4 | Use the applicable commands and options to find the desired information. |
| Step 5 | To exit debug mode, press Ctrl-C . |