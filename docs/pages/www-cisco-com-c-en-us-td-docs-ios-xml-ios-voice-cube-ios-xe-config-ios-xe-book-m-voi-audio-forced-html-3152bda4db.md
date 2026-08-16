---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-audio-forced-html-3152bda4db
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-audio-forced.html
retrieved_at: 2026-08-16T15:51:15.290485+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Video Suppression

## Chapter: Video Suppression

# Video Suppression

## Video
                        	 Suppression

The video suppression feature allows pass-through of only audio and image (for T.38 Fax) media types in SDP and drops all
                           other media capabilities.

## Feature
                        	 Information for Video Suppression

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                          					 Name

Releases

Feature
                                          					 Information

Support
                                          					 for Video Suppression

Cisco IOS
                                          					 15.6(2)T

Cisco IOS XE Denali 16.3.1

This
                                          					 feature allows pass-through of only audio and application (for T.38 Fax) media
                                          					 types and drops all other media types in SDP.

The
                                          					 following commands are introduced: audio forced , voice-class sip audio
                                                						  forced

## Restrictions

Supports only
                                 			 SIP-SIP calls.

Video
                                 			 suppression is not supported in SDP pass-through mode.

Video suppression feature removes both video and application m-lines
                                 			 in the incoming SDP. It is not possible to remove application m-line alone and
                                 			 pass across video m-line parameters.

## Information About
                        	 Video Suppression

Video suppression
                           		feature enables CUBE to interwork with the networks that support only audio and
                           		image media types in SDP and the networks that support video and application
                           		media types in addition to audio and image media types.

By default video
                           		suppression feature is disabled on CUBE and hence the video capabilities are
                           		passed through in SDP. Passing across the video capabilities could cause
                           		interoperability issues if one of the networks do not support video
                           		capabilities.

By enabling video
                           		suppression feature, you can configure CUBE to pass-through audio and image
                           		only, and drop all other capabilities such as video and application m-lines.
                           		This helps enterprises to interwork with audio capable networks and video
                           		capable networks smoothly.

You can enable video
                           		suppression at dial-peer level and at global configuration level.

### Feature
                           	 Behavior

If video
                                    			 suppression is enabled on any of the dial-peers (inbound or outbound), video
                                    			 capabilities are not offered for that particular call.

Configuring voice-class sip audio
                                          				  forced [system] command at a dial-peer level makes use of global
                                    			 configuration level settings for allowing only audio and image media.

Video
                                    			 suppression feature will work as expected even when codec transparent feature
                                    			 is configured.

## Configuring Video
                        	 Suppression

### SUMMARY STEPS

- enable

- configure terminal

- Enter one of
                              			 the following commands:

In the
                                    				  dial-peer configuration mode

In the
                                    				  global VoIP SIP configuration mode

- end

### DETAILED STEPS

Step 1

enable

Enables
                                          				privileged EXEC mode.

Enter
                                                					 your password if prompted.

Step 2

configure terminal

Enters global
                                          				configuration mode.

Step 3

Enter one of
                                       			 the following commands:

In the
                                             				  dial-peer configuration mode

In the
                                             				  global VoIP SIP configuration mode

### Example:

```
!Applying audio-forced to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# voice-class sip audio forced Device (config-dial-peer)# end
```

### Example:

```
! Applying audio forced globally
Device(config)# voice service voip Device (config-voi-serv)# sip Device (config-voi-sip)# audio forced Device (config-voi-sip)# end
```

Enables
                                          				pass-through of only audio and image media types in SDP.

Step 4

end

Exits present
                                          				configuration mode and enters privileged EXEC mode.

## Troubleshooting
                        	 Tips

The following
                           		commands are useful for debugging:

show voip rtp
                                 			 connections

show call active
                                 			 voice brief

show call active
                                 			 video brief

debug voip
                                 			 dialpeer

debug ccsip all

debug voip ccapi
                                 			 inout

| Feature
                                          					 Name | Releases | Feature
                                          					 Information |
|---|---|---|
| Support
                                          					 for Video Suppression | Cisco IOS
                                          					 15.6(2)T Cisco IOS XE Denali 16.3.1 | This
                                          					 feature allows pass-through of only audio and application (for T.38 Fax) media
                                          					 types and drops all other media types in SDP. The
                                          					 following commands are introduced: audio forced , voice-class sip audio
                                                						  forced |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable | Enables
                                          				privileged EXEC mode. Enter
                                                					 your password if prompted. |
| Step 2 | configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | Enter one of
                                       			 the following commands: In the
                                             				  dial-peer configuration mode voice-class sip audio
                                                					 forced In the
                                             				  global VoIP SIP configuration mode audio forced Example: In
                                       			 dial-peer configuration mode !Applying audio-forced to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# voice-class sip audio forced Device (config-dial-peer)# end Example: In global
                                       			 VoIP SIP configuration mode ! Applying audio forced globally
Device(config)# voice service voip Device (config-voi-serv)# sip Device (config-voi-sip)# audio forced Device (config-voi-sip)# end | Enables
                                          				pass-through of only audio and image media types in SDP. |
| Step 4 | end | Exits present
                                          				configuration mode and enters privileged EXEC mode. |