---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmeanswr-html-e0aef9360b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeanswr.html
retrieved_at: 2026-08-21T07:23:35.455342+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Headset Auto
	 Answer

## Chapter: Headset Auto
	 Answer

# Headset Auto
                     	 Answer

## Information About
                        	 Headset Auto Answer

### Auto Answering
                           	 Calls Using a Headset

In Cisco Unified CME
                              		4.0 and later versions you can configure lines on specific phones to
                              		automatically connect to incoming calls when the headset key is activated. The
                              		phone cannot be busy with an active call and the headset key must be engaged to
                              		automatically answer calls. Incoming calls are automatically answered one by
                              		one on the phone as long as the headset light remains lit. For each ephone, you
                              		can specify one or more lines for headset auto answer.

After a phone is
                              		configured for headset auto answer, the phone user must press the headset key
                              		to start auto answer. The headset light is lit to indicate that auto answer is
                              		active for the lines that are designated in the configuration. When the phone
                              		auto answers a call, a zip tone is
                              		played to alert the phone user that a call is present. To stop auto answer, the
                              		phone user presses the headset key again and the headset light goes out. At
                              		this time, the phone user can answer calls in a normal manner using the
                              		handset.

### Difference Between
                           	 a Line and a Button

Note that a line is
                              		similar to, but not exactly the same as, a button on the phone. A line
                              		represents a phone’s capability to make a call connection, so each button that
                              		can make a call connection becomes a line. (For example, unoccupied buttons or
                              		speed-dial buttons are not lines.) Note also that a line is not the same as an
                              		ephone-dn. A button with overlaid ephone-dns is only one line, regardless of
                              		whether it has several ephone-dns (extension numbers) associated with it. In
                              		most cases an ephone’s line numbers do match its button numbers, but in a few
                              		cases they do not.

When is a Line
                                 		  the Same as a Button? illustrates a comparison of line numbers and button numbers for different types
                              		of ephone configurations.

## Configure Headset
                        	 Auto Answer

### Enable Headset
                           	 Auto Answer

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- headset auto-answer line line-number

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone phone-tag

#### Example:

```
Router(config)# ephone 25
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks. The maximum number of ephones for a
                                                   					 particular Cisco Unified CME system is version- and platform-specific. For the
                                                   					 range of values, see the CLI help.

Step 4

headset auto-answer line line-number

#### Example:

```
Router(config-ephone)# headset auto-answer line 1
```

Specifies a
                                             				line on an ephone that will be answered automatically when the headset button
                                             				is depressed.

line-number —Number of the phone line that should
                                                   					 be automatically answered.

Repeat this
                                                         				  command to add additional lines.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Headset
                           	 Auto Answer

Step 1

Use the show
                                                				  running-config command to verify your configuration. Headset auto
                                          			 answer is listed in the ephone portion of the output.

```
Router# show running-config ephone  1
			  headset auto-answer line 1
			  headset auto-answer line 2
			  headset auto-answer line 3
			  headset auto-answer line 4
			  username "Front Desk"
			  mac-address 011F.92B0.BE03
			  speed-dial 1 330 label “Billing”
			  type 7960 addon 1 7914
			  no dnd feature-ring
			  keep-conference
			  button  1f40 2f41 3f42 4:30
			  button  5:405 7m20 8m21 9m22
			  button  10m23 11m24 12m25 13m26
			  button  14m499 15:1 16m31 17f498
			  button  18s500
			  night-service bell
```

Step 2

Use the show telephony-service
                                                				  ephone command to display only the ephone configuration portion
                                          			 of the running configuration.

## Configuration
                        	 Example for Headset Auto Answer

### Example for
                           	 Enabling Headset Auto Answer

The following
                                 		  example enables headset auto answer on ephone 3 for line 1 (button 1) and
                                 		  line 4 (button 4).

```
ephone 3
		 button 1:2 2:4 3:6 4o21,22,23,24,25
		 headset auto-answer line 1
		 headset auto-answer line 4
```

The following
                                 		  example enables headset auto answer on ephone 17 for line 2 (button 2), which
                                 		  has overlaid ephone-dns, and line 3 (button 3), which is an overlay rollover
                                 		  line.

```
ephone 17
		 button 1:2 2o21,22,23,24,25 3x2
		 headset auto-answer line 2
		 headset auto-answer line 3
```

The following
                                 		  example enables headset auto answer on ephone 25 for line 2 (button 3) and
                                 		  line 3 (button 5). In this case, the button numbers do not match the line
                                 		  numbers because buttons 2 and 4 are not used.

```
ephone 25
		 button 1:2 3:4 5:6
		 headset auto-answer line 2
		 headset auto-answer line 3
```

## Feature
                        	 Information for Headset Auto Answer

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Cisco Unified CME Version

Feature
                                             					 Information

Headset
                                             					 Auto Answer

4.0

Headset
                                             					 auto answer was introduced.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 25 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks. The maximum number of ephones for a
                                                   					 particular Cisco Unified CME system is version- and platform-specific. For the
                                                   					 range of values, see the CLI help. |
| Step 4 | headset auto-answer line line-number Example: Router(config-ephone)# headset auto-answer line 1 | Specifies a
                                             				line on an ephone that will be answered automatically when the headset button
                                             				is depressed. line-number —Number of the phone line that should
                                                   					 be automatically answered. Note Repeat this
                                                         				  command to add additional lines. | Note | Repeat this
                                                         				  command to add additional lines. |
| Note | Repeat this
                                                         				  command to add additional lines. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Note | Repeat this
                                                         				  command to add additional lines. |
|---|---|

| Step 1 | Use the show
                                                				  running-config command to verify your configuration. Headset auto
                                          			 answer is listed in the ephone portion of the output. Router# show running-config ephone  1
			  headset auto-answer line 1
			  headset auto-answer line 2
			  headset auto-answer line 3
			  headset auto-answer line 4
			  username "Front Desk"
			  mac-address 011F.92B0.BE03
			  speed-dial 1 330 label “Billing”
			  type 7960 addon 1 7914
			  no dnd feature-ring
			  keep-conference
			  button  1f40 2f41 3f42 4:30
			  button  5:405 7m20 8m21 9m22
			  button  10m23 11m24 12m25 13m26
			  button  14m499 15:1 16m31 17f498
			  button  18s500
			  night-service bell |
|---|---|
| Step 2 | Use the show telephony-service
                                                				  ephone command to display only the ephone configuration portion
                                          			 of the running configuration. |

| Feature
                                             					 Name | Cisco Unified CME Version | Feature
                                             					 Information |
|---|---|---|
| Headset
                                             					 Auto Answer | 4.0 | Headset
                                             					 auto answer was introduced. |