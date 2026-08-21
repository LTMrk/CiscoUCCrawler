---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-bat-15-cucm-b-bulk-administration-guide-15-cucm-b-bulk-administration-g-580be93957
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/bat/15/cucm_b_bulk-administration-guide-15/cucm_b_bulk-administration-guide-1251su2_chapter_0111.html
retrieved_at: 2026-08-21T09:16:34.894231+00:00
---

Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Bulk Administration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: October 1, 2024

Chapter: Phone Updates

## Chapter: Phone Updates

# Phone Updates

This chapter provides information about how to use the Update
                        		Phones option to update phone settings, such as changing or adding the device
                        		pool or calling search space for a group of similar phones. You can locate
                        		existing phone records that you want to update using either a query or a custom
                        		file. After locating the phone records, you can proceed to define the update
                        		parameters.

## Update Phones Using
                        	 Query

Step 1

Choose Bulk
                                             				  Administration > Phones > Update Phones > Query .

The Update
                                             				  Phones Query window displays.

To update all
                                                      				  phones, click Find and do not specify a query. Skip the rest of
                                                      				  this procedure and proceed to choose the update parameters for the phones.

Step 2

From the first Find
                                          				Phone where drop-down list box, choose one of the following
                                       			 criteria:

- Device Name

- Description

- Directory Number

- Calling Search Space

- Device Pool

- Device Type

- Call Pickup Group

- LSC Status

- LSC Expires

- LSC Issued by

- LSC Issuer Expires by

- Authentication String

- Location

- Phone Load Name

- Device Protocol

- Security Profile

Last Active

Last Registered

The status of LSC
                                                         					 Expires and LSC
                                                         					 Issuer Expires by fields are set to "NA" when
                                                      				  there is no LSC issued on a new device.

The status of LSC Expires and LSC Issuer Expires by fields are set to " Unknown" when the LSC is issued to a device before the upgrade to Unified Communications Manager 11.5(1).

From the second Find
                                             				  Phone where drop-down list box, choose one of the following
                                          				criteria:

- is before

- is exactly

- is after

- begins with

- contains

- ends with

- is exactly

- is empty

- is not empty

Step 3

Specify the
                                       			 appropriate search text, if applicable.

Tip

To find all
                                                      				  phones that are registered in the database, click Find without entering any search text.

Step 4

To further
                                       			 define your query and to add multiple filters, check the Search
                                          				Within Results check box, choose AND or OR from the drop-down box, and repeat Step 2 and Step 3 .

Step 5

Click Find .

### What to do next

To complete the
                              		  procedure for updating phones, continue to the Choose Update Parameters .

## Update Phones Using Custom File

Create a custom file to locate phones to update. After
                              		  locating phones following this procedure, you must proceed to choose the update
                              		  parameters.

Do not use the insert or export transaction files that are created
                                          			 with bat.xlt for the update transaction. Instead, you must create a custom file
                                          			 with details of the phone records that need to be updated. Use only this file
                                          			 for the update transaction.

### Before you begin

- Identify the devices that
                                    			 you need to update.

- Device names

- Directory numbers

- Description

Enter values for device name, description, or directory number
                                                   				  in the custom update file. You do not need to include a header in the custom
                                                   				  update file.

- Upload the text file to the Unified Communications Manager server. See Upload File to Server .

Step 1

Choose Bulk
                                             				  Administration > Phones > Update
                                             				  Phones > Use Custom File .

The Update Phones Custom Configuration window
                                          				displays.

Step 2

In the Update Phones where drop-down list box, choose
                                       			 the type of custom file that you have created from the following criteria:

- Device Name

- Directory Number

- Description

Step 3

In the list of custom files, choose the filename of the custom
                                       			 file for this update.

Step 4

Click Find .

If the query results are not what you expected, you can change the
                                          				custom file selections.

### What to do next

To complete the procedure for updating phones, continue to the Choose Update Parameters .

## Choose Update Parameters

After you have located the phones to update, you can choose
                              		  the parameters and define values for updating those phones.

Step 1

In the Update Phones Query window, click Next .

Step 2

Choose the Logout Users before Update check
                                       			 box to log out the users prior to the update.

Step 3

Specify the setting that you want to update for all the records
                                       			 that you have defined in your query or custom file. You can choose multiple
                                       			 parameters to update. See the Table 1 for descriptions of parameters.

Step 4

Select the update check box to the left of the field that you want
                                       			 to update.

This tells BAT to overwrite the existing value for the field.

Be aware that BAT updates only those fields for which you have
                                                      				  selected the update check box.

Step 5

In the Value field for the checked parameter, enter
                                       			 the new value or choose a value from the list box.

Step 6

In the Reset/Restart Phones area, check one of the
                                       			 following choices:

- Don't
                                                				Reset/Restart phones/Apply Config —To reset/restart devices at a later
                                             			 time.

- Reset
                                                				phones —To reset (power-cycle) the phones

- Restart
                                                				phones —To reset phones without power-cycling

- Apply
                                                				Config —To reset only the settings that have changed since the last
                                             			 reset

Step 7

Update the required phone parameters. See Table 1 for field descriptions.

Step 8

To create a job for updating the records, click Submit .

## Phone Update Field
                        	 Descriptions

The
                              		  following table provides descriptions for all possible fields that display when
                              		  you are updating phones. Some device types do not require all the phone
                              		  settings.

Values that appear in some fields display from Unified Communications Manager . You must configure these values by using Unified Communications Manager Administration.

Be aware that
                                          			 some fields have two check boxes. The first check box determines if you need to
                                          			 update the field; the second check box determines the value (checked or
                                          			 unchecked) to use for the field.

Tip

Check the first
                                          			 check box if you need to update the field and the second check box to apply a
                                          			 checked value to the phones you select. For example, if you check the first
                                          			 check box for Do Not Disturb and leave the second one unchecked, you update
                                          			 phones with an unchecked value for Do Not Disturb.

Field

Description

Description

Enter a description that makes the device easy to recognize. The description can include up to 50 characters in any language,
                                          but it cannot include double-quotes ("), percentage sign ( % ), ampersand (&), back-slash ( \ ), or angle brackets (<>).

DevicePool

Choose the device pool to which this group of phones/ports should belong.

A devicepool defines sets of common characteristics for devices, such as region, date/time group, Unified Communications Manager group, and calling search space for auto-registration.

Common Device Configuration

Choose the common device configuration to which you want this phone assigned. The common device configuration includes the
                                          attributes (services or features) that are associated with a particular user.

To see the common device configuration settings, click the View Details link.

Phone Button Template

Choose the appropriate phone button template. The phone button template determines the configuration of buttons on a phone
                                          and identifies which feature (line, speed dial, and so on) is used for each button.

Unified Communications Manager does not make this field available for H.323 clients or CTI ports.

Softkey Template

Choose the softkey template to be used for all phones in this group.

Common Phone Profile

From the drop-down list, choose a common phone profile from the list of available common phone profiles.

Calling Search Space

Choose the calling search space to which this group of phones/ports should belong.

A calling search space specifies the collection of route partitions that are searched to determine how a dialed number should
                                          be routed.

AAR Calling Search Space

Choose the appropriate calling search space for the device to use when it performs automated alternate routing (AAR). The
                                          AAR calling search space specifies the collection of route partitions that are searched to determine how to route a collected
                                          (originating) number that is otherwise blocked due to insufficient bandwidth.

Media Resource Group List

Choose the media resource group list (MRGL) to which this group of phones/ports should belong.

An MRGL specifies a list of prioritized media resource groups. An application can choose required media resources among the
                                          available ones according to the priority order that is defined in the MRGL.

User Hold MOH Audio Source

Choose the user-hold audio source for this group of phones or ports.

The user-hold audio source plays music when a user places a call on hold.

Network Hold MOH Audio Source

Choose the network hold audio source that this group of IP phones or CTI ports should use.

The network-hold audio source plays music when the system places a call on hold, such as when the user transfers or parks
                                          a call.

Location

Choose the location to which this group of phones/ports should belong.

A location indicates the remote location that is accessed by using restricted bandwidth connections.

AAR Group

Choose the automated alternate routing (AAR) group for this device. The AAR group provides the prefix digits that are used
                                          to route calls that are otherwise blocked due to insufficient bandwidth. If no AAR group is specified, Unified Communications Manager uses the AAR group that is associated with Device Pool or Line.

User Locale

Choose the country and language set that you want to associate with this user.

This choice determines which cultural-dependent attributes exist for this user and which language displays for the user in
                                          the Unified Communications Manager user windows and phones.

Network Locale

Choose the network locale that you want to associate with this user.

The Network Locale comprises a set of tones and cadences that Cisco gateways and phones use when they are communicating with
                                          the PSTN and other networks in a specific geographical area.

Built in Bridge

Enable or disable the built-in conference bridge for the barge feature by using the Built In Bridge drop-down list (choose
                                          On, Off, or Default).

Privacy

For each phone that wants Privacy, choose On in the Privacy drop-down list.

For more configuration information, refer to Barge and Privacy Features in the Feature Configuration Guide for Cisco Unified Communications Manager .

Device Mobility Mode

From the drop-down list, turn the device mobility feature on or off for this device or choose Default to use the default device
                                          mobility mode.

Click View Current Device Mobility Settings to display the current values of these device mobility parameters:

Cisco Unified Communications Manager Group

Roaming Device Pool

Location

Region

Network Locale

AAR Group

AAR Calling Search Space

Device Calling Search Space

Media Resource Group List

SRST

Mobility User ID

From the drop-down list, choose the user ID of the person to whom this dual-mode phone is assigned.

Be aware that the Mobility User ID configuration is used for Mobile Connect and Mobile Voice Access for dual mode phones.

The Owner User ID and Mobility User ID can differ.

Owner User ID

Enter a user ID for the primary phone user.

Phone Personalization

From the drop-down list, enable or disable the Cisco Unified Phone Designer feature for this device or choose Default to use
                                          the phone personalization that is set in the Common Phone Profile.

Disabled—None of the Cisco Unified Phone Application Suite features get activated.

Enabled—This setting accepts a personalized background image file, which is used for the phone screen; it accepts a preview
                                                image file for temporary display; and it accepts a personalized tone file, so the default ring tone can be personalized.

Default—Use the phone personalization setting that is in the Common Phone Profile.

Services Provisioning

From the drop-down list, choose the Services Provisioning setting that you want to use from the following values:

Internal

External URLs

Both

Default: Internal

This parameter controls whether the phone uses the services provisioned from the configuration file (Internal), services received
                                          from the Services URLs (External URLs), or both. The External URLs option provides backward compatibility with third party
                                          provisioning servers. The Both option allows users to subscribe to the services specified in the configuration file while
                                          also appending services from an external provisioning server.

This is a required field.

Phone Load Name

Enter the custom phone load, if applicable.

Any value that is entered in this field overrides the default value for the chosen model and specifies the custom software
                                                      for a CiscoUnifiedIPPhone.

Single Button Barge

From the drop-down list, enable or disable the Single Button Barge/cBarge feature for this device or choose Default to use
                                          the service parameter setting.

Off—This setting disables the Single Button Barge/cBarge feature; however, the regular Barge or cBarge features will still
                                                work.

Barge—This setting enables the Singe Button Barge feature.

cBarge—This setting enables the Single Button cBarge feature.

Default—This setting uses the Single Button Barge/cBarge setting that is in the service parameter.

Join Across Lines

From the drop-down list, enable or disable the Join Across Lines feature for this device or choose Default to use the service
                                          parameter setting.

Off—This setting disables the Join Across Lines feature.

On—This setting enables the Join Across Lines feature.

Default—This setting uses the Join Across Lines setting that is in the service parameter.

Use Trusted Relay Point

From the drop-down list, enable or disable whether Unified Communications Manager inserts a trusted relay point (TRP) device with this media endpoint. Choose one of the following values:

Default—If you choose this value, the device uses the Use Trusted Relay Point setting from the common device configuration
                                                with which this device associates.

Off—Choose this value to disable the use of a TRP with this device. This setting overrides the Use Trusted Relay Point setting
                                                in the common device configuration with which this device associates.

On—Choose this value to enable the use of a TRP with this device. This setting overrides the Use Trusted Relay Point setting
                                                in the common device configuration with which this device associates.

A Trusted Relay Point (TRP) device designates an MTP or transcoder device that is labeled as Trusted Relay Point.

Unified Communications Manager places the TRP closest to the associated endpoint device if more than one resource is needed for the endpoint (for example,
                                          a transcoder or RSVP Agent).

If both TRP and MTP are required for the endpoint, TRP gets used as the required MTP.

Calling Party Transformation CSS

This setting allows you to localize the calling party number on the device. Make sure that the Calling Party Transformation
                                          CSS that you choose contains the calling party transformation pattern that you want to assign to this device.

The device takes on the attributes of the Calling Party Transformation Pattern when you assign the pattern to a partition
                                          where the Calling Party Transformation CSS exists.

Geolocation

From the drop-down list, choose a geolocation.

You can choose the Unspecified geolocation, which designates that this device does not associate with a geolocation.

You can also choose a geolocation that has been configured with the System > Geolocation Configuration menu option.

Emergency Location (ELIN) Group

Choose the Emergency Location (ELIN) group to which this group of phones should belong. An ELIN group identifies a location
                                          to which ELINs under this ELIN group must be mapped in the ALI database.

Feature Control Policy

Choose the Feature Control Policy for this group of phones.

A feature control policy specifies the appearance of features and the associated softkeys that display on the phone.

BLF Audible Alert Setting (Phone Idle)

For this required field, from the drop-down list, choose the BLF Audible Alert setting that you want to use from the following
                                          values:

On

Off

Default

This parameter provides an audible alert in addition to a visual alert on a phone that is currently idle when a call comes
                                          in to one of the lines that is monitored by way of a busy lamp field (BLF) button.

BLF Audible Alert Setting (Phone Busy)

For this required field, this parameter provides an audible alert in addition to a visual alert on a phone that is currently
                                          in use when a call comes in to one of the lines that is monitored by way of a busy lamp field (BLF) button.

From the drop-down list, choose the BLF Audible Alert setting that you want to use from the following values:

On

Off

Default

Always Use Prime Line

From the drop-down list, choose the Always Use Prime Line setting that you want to use from the following values:

On

Off

Default

Always Use Prime Line for Voice Message

From the drop-down list, choose the Always Use Prime Line for Voice Message setting that you want to use from the following
                                          values:

On

Off

Default

Use Device Pool Calling Party Transformation CSS

To use the Calling Party Transformation CSS that is configured in the device pool that is assigned to this device, check this
                                          check box. If you do not check this check box, the device uses the Calling Party Transformation CSS that you configured in
                                          the device configuration window.

Ignore Presentation Indicators

Check this check box if the system must ignore presentation indicators.

Retry Video Call as Audio

Check this check box to retry a video call as an audio call.

Allow Control of Device from CTI

Check this check box to allow CTI to control and monitor this device.

If the associated directory number specifies a shared line, the check box should remain enabled as long as at least one associated
                                          device specifies a combination of device type and protocol that CTI supports.

Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                      controlled. However, devices operating in GSM mode cannot be monitored or controlled.

Logged into Hunt Group

This check box, which gets checked by default for all phones, indicates that the phone is currently logged in to a hunt list
                                          (group). When the phone gets added to a hunt list, the administrator can log the user in or out by checking (and unchecking)
                                          this check box.

Users use the softkey on the phone to log their phone in or out of the hunt list.

Remote Device

If you are experiencing delayed connect times over SCCP to remote sites, check the Remote Device check box in the Phone Configuration window. Checking this check box tells Unified Communications Manager to allocate a buffer for the phone device when it registers and to bundle SCCP messages to the phone.

Because this feature consumes resources, be sure to check this check box only when you are experiencing signaling delays for
                                                      phones that run SCCP. Most users do not require this option.

Protected Device

Check this check box to designate a phone as "protected." This enables the phone to play a two-second tone notifying the user when a call is both encrypted and both phones are configured
                                          as protected devices. The tone plays for both parties when the call is answered. The tone does not play unless both phones
                                          are "protected" and the call occurs over encrypted media.

Protocol Specific Information

Packet Capture Mode

From the drop-down list, choose the mode that you want to set for signal packet capture:

None—Choose None if you do not want to specify a mode.

Real-Time Mode—Use this mode for real-time signal packet capture.

Batch Processing Mode—Use this mode for batch processing signal packet capture mode.

Packet Capture Duration

Enter the time for packet capture in minutes. You can enter a maximum duration of 300 minutes. The default duration specifies
                                          60 minutes.

Presence Group

Used with the Presence feature, the phones that is running SIP or SCCP serves as a watcher because it requests status about
                                          the presence entity, for example, directory number, that is configured as a BLF speed dial button on the phone.

If you want the phone to receive the status of the presence entity, choose a Presence Group that is allowed to view the status
                                          of the Presence Group that is applied to the directory number, as indicated in the Presence Group Configuration window.

Device Security Profile

For phones that run SCCP and SIP, choose the security profile that you want to apply to the device.

All phones require that you apply a security profile. If the phone does not support security, choose a nonsecure profile.

Tip

SUBSCRIBE Calling Search Space

Used with the Presence feature, the SUBSCRIBE Calling Search Space determines how Unified Communications Manager routes the subscription requests that come from the phone. From the drop-down list, choose the calling search space that
                                          you want to use for this purpose.

Outbound Call Rollover

From the drop-down list, choose the rollover option that you want to use for outbound calls.

No Rollover—Choose this option to Switch off the rollover feature. Conference and transfer will not work in this mode.

Rollover within the same DN—Choose this option to use rollover within the same DN. Conferences and call transfers complete
                                          by using the same directory number (on different lines).

Rollover to any line—Choose this option to roll over to any line. Conferences and call transfers complete by using a different
                                          directory number and line than the original call.

Unattended Port

Check this check box to indicate an unattended port on this device.

Require DTMF Reception

For phones that run SIP and SCCP, check this check box to require DTMF reception for this phone.

External Data Locations Information

Information

Enter the help text URL for the information button.

Directory

Enter the URL of the directory server.

Messages

Enter the voice-messaging access pilot number.

Services

Enter the URL for the services menu.

Authentication Server

Enter the URL that the phone uses to validate requests that are made to the phones web server. If you do not provide an authentication
                                          URL, the advanced features on CiscoUnifiedIPPhones that require authentication will not function. Leave this field blank to
                                          accept the default setting.

By default, this URL accesses a CiscoUnifiedIPPhone Self Care Portal window that was configured during installation.

Proxy Server

Enter the host and port (for example, proxy.cisco.com:80) that are used to proxy HTTP requests for access to non-local host
                                          addresses from the phones HTTP client.

If the phone receives a URL such as www.cisco.com in a service and the phone is not configured in the cisco.com domain, the
                                          phone uses the proxy server to access the URL. If the phone is configured in the cisco.com domain, the phone accesses the
                                          URL without using the proxy because it is in the same domain as the URL.

Leave this field blank to accept the default setting.

Idle

Enter the URL to display on the CiscoUnifiedIPPhone screen when the phone has not been used for the time that is specified
                                          in the Idle Time field. For example, you can display a logo on the screen when the phone has not been used for 5 minutes.
                                          Leave this field blank to use the default value.

Idle Timer

Enter the seconds that you want to elapse before the phone displays the URL that is specified in the Idle field. Leave this
                                          field blank to use the default value.

Secure Authentication URL

Enter the secure URL that the phone uses to validate requests that are made to the phone web server.

If you do not provide a Secure Authentication URL, the device uses the nonsecure URL. If you provide both a secure URL and
                                                      a nonsecure URL, the device chooses the appropriate URL, based on its capabilities.

By default, this URL accesses a CiscoUnifiedIPPhone Self Care Portal window that was configured during installation.

Leave this field blank to accept the default setting.

Maximum length specifies 255 characters.

Secure Directory URL

Enter the secure URL for the server from which the phone obtains directory information. This parameter specifies the URL that
                                          secured Cisco Unified IP Phones use when you press the Directory button.

If you do not provide a Secure Directory URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities.

Leave this field blank to accept the default setting.

Maximum length specifies 255 characters.

Secure Idle URL

Enter the secure URL for the information that displays on the Cisco Unified IP Phone display when the phone is idle, as specified in the Idle Timer field. For example, you can display a logo on the LCD when
                                          the phone has not been used for 5 minutes.

If you do not provide a Secure Idle URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities.

To accept the default setting, leave this field blank.

Maximum length specifies 255 characters.

Secure Information URL

Enter the secure URL for the server location where the Cisco Unified IP Phone can find help text information. This information
                                          displays when the user presses the information (i) button or the question mark ( ? ) button.

If you do not provide a Secure Information URL, the device uses the nonsecure URL. If you provide both a secure URL and a
                                                      nonsecure URL, the device chooses the appropriate URL, based on its capabilities.

To accept the default setting, leave this field blank.

Maximum length specifies 255 characters.

Secure Messages URL

Enter the secure URL for the messages server. The Cisco Unified IP Phone contacts this URL when the user presses the Messages
                                          button.

If you do not provide a Secure Messages URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities.

To accept the default setting, leave this field blank.

Maximum length specifies 255 characters.

Secure Services URL

Enter the secure URL for Cisco Unified IP Phone services. This setting specifies the location that the secure Cisco Unified IP Phone contacts when the user presses the Services button.

If you do not provide a Secure Services URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities.

To accept the default setting, leave this field blank.

Maximum length specifies 255 characters.

Hotline Device

Enter T or F. Hotline devices can connect only to other Hotline devices. This feature extends the PLAR feature, which configures
                                          a phone to automatically dial one directory number when it goes off-hook. Hotline provides additional restrictions that you
                                          can apply to devices that use PLAR.

To implement Hotline, you must also create a softkey template without supplementary service softkeys and apply the softkey
                                          template to the Hotline device.

Extension Information

Enable Extension Mobility

Check this check box to enable extension mobility.

Choose 0-Off to disable this feature, or choose 1-On to enable this feature.

Extension mobility allows a user to log in and out of a Cisco Unified IP Phone .

IP Services1

Use Unified Communications Manager to choose any services that have been configured.

IP Services2

Use Unified Communications Manager to choose any services that have been configured.

Using Unified Communications Manager Bulk Administration (BAT), you cannot update more than two IP services in one transaction.

Certification Authority Proxy Function (CAPF) Information

(These parameters display only for devices with the capability to support authentication or encryption.)

Certificate Operation

From the drop-down list, choose the Certification Operation that you want to perform from the following options:

No Pending Operation—No pending Certification Operation lists exist for this device. Choosing this option disables the remaining
                                                CAPF fields.

Install/Upgrade—Install or upgrade a Certification Operation.

Delete—Delete a Certification Operation.

Troubleshoot—Troubleshoot a Certification Operation.

Generate Unique Authentication String for Each Device

Check this check box if you want a unique authentication string to be generated for each device.

Authentication String

If Authentication Mode is By Authentication String, enter the Authentication String. Alternately, to get a system-generated
                                          string, click Generate String .

Operation Completes By

Enter the date by which the Certification Operation will complete. The date format specifies YYYY: MM: DD: HH. The default
                                          completion date specifies 10 days from the current system date.

MultiLevel Precedence and Preemption (MLPP) Information

MLPP Indication

If available, this setting specifies whether a device that is capable of playing precedence tones will use the capability
                                          when it places an MLPP precedence call.

From the drop-down list, choose a setting to assign to this device from the following options:

Default—This device inherits its MLPP indication setting from its device pool.

Off—This device does not send indication of an MLPP precedence call.

On—This device does send indication of an MLPP precedence call.

Do not configure a device with the following combination of settings: MLPP Indication is set to Off while MLPP Preemption
                                                      is set to Forceful.

MLPP Preemption

If available, this setting specifies whether a device that is capable of preempting calls in progress will use the capability
                                          when it places an MLPP precedence call.

From the drop-down list, choose a setting to assign to this device from the following options:

Default—This device inherits its MLPP preemption setting from its device pool.

Disabled—This device does not preempt calls in progress when it places an MLPP precedence call.

Forceful—This device preempts calls in progress when it places an MLPP precedence call.

Do not configure a device with the following combination of settings: MLPP Indication is set to Off while MLPP Preemption
                                                      is set to Forceful.

MLPP Domain (e.g., "0000FF")

Enter a hexadecimal value for the MLPP domain that is associated with this device. Ensure that this value is blank or a value
                                          between 0 and FFFFFF.

Do Not Disturb (DND)

Do Not Disturb

If you want to enable the DND feature, check this check box.

DND Option

From the drop-down list, choose a DND option from the following options:

None

Ringer Off

Call Reject

Use Common Phone Profile Setting

DND Incoming Call Alert

From the drop-down list, choose one of the following options:

None

Disable

Flash Only

Beep Only

Secure Shell Information

Secure Shell User

Enter a user ID for the secure shell user. If the phone that you are configuring does not support secure shell access, this
                                          field does not display. Cisco Technical Assistance Center (TAC) uses secure shell for troubleshooting. Contact TAC for further
                                          assistance.

Secure Shell Password

Enter the password for a secure shell user. If the phone that you are configuring does not support secure shell access, this
                                          field does not display. Contact TAC for further assistance.

Assign IP Phone Services

Add All Services From This Template

From the drop-down list, choose the template that contains list of services with which you want to update the phones.

You can click the Edit IP Phone Service link to update the subscribed CiscoUnifiedIP Phones services on the template.

Remove Duplicate

Check this check box to remove duplicate IP phone services. If you check this check box, the system removes the duplicate
                                          service subscriptions from phones and user device profiles. The IP system deletes services based on the IP service name.

Product Specific Information

Device Security Mode

From the drop-down list, choose the mode that you want to set for the device:

Use System Default—The phone uses the value that you specified for the enterprise parameter, Device Security Mode.

Non-secure—No security features exist for the phone. A TCP connection opens to Unified Communications Manager .

Authenticated— Unified Communications Manager provides integrity and authentication for the phone. A TLS connection that uses NULL/SHA opens.

Encrypted— Unified Communications Manager provides integrity, authentication, and encryption for the phone. A TLS connection that uses AES128/SHA opens

This field applies only if the phone model supports authentication or encryption.

Remove Duplicate IP Services from all Phones and Device Profiles

Check this check box to remove duplicate IP phone services. If you check this check box, the system removes the duplicate
                                          service subscriptions from phones and user device profiles. The IP system deletes services based on the IP service name.

Disable SpeakerPhone

Check this check box to disable the speakerphone.

Disable Speakerphone and Headset

Check this check box to disable the speakerphone and headset.

Forwarding Delay

Use this field to enable or disable forwarding delay. Choose enable when you want the port to wait a few seconds before forwarding
                                          a call.

PC Port

Use this field to enable or disable the PC port on phones that have internal switches. Users can connect a PC or workstation
                                          to the phone by using the port labeled "10 / 100 PC" on the back of the phone.

Setting Access

Use this field to choose whether the user has access to phone settings. The options include Enabled and Disable.

Gratuitous ARP

Choose Enabled or Disabled to control gratuitous ARP.

PC Voice VLAN Access

Choose Enabled or Disabled to control access to a PC voice VLAN.

Video Capabilities

Choose Enabled or Disabled to control video capabilities access.

Auto Line Select

Choose Enabled or Disabled to allow or disallow automatic line selection on the phone.

Web Access

Choose Enabled or Disabled to allow web access on the phone.

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Update Phones > Query . The Update
                                             				  Phones Query window displays. Note To update all
                                                      				  phones, click Find and do not specify a query. Skip the rest of
                                                      				  this procedure and proceed to choose the update parameters for the phones. | Note | To update all
                                                      				  phones, click Find and do not specify a query. Skip the rest of
                                                      				  this procedure and proceed to choose the update parameters for the phones. |
|---|---|---|---|
| Note | To update all
                                                      				  phones, click Find and do not specify a query. Skip the rest of
                                                      				  this procedure and proceed to choose the update parameters for the phones. |
| Step 2 | From the first Find
                                          				Phone where drop-down list box, choose one of the following
                                       			 criteria: Device Name Description Directory Number Calling Search Space Device Pool Device Type Call Pickup Group LSC Status LSC Expires LSC Issued by LSC Issuer Expires by Authentication String Location Phone Load Name Device Protocol Security Profile Last Active Last Registered Note The status of LSC
                                                         					 Expires and LSC
                                                         					 Issuer Expires by fields are set to "NA" when
                                                      				  there is no LSC issued on a new device. The status of LSC Expires and LSC Issuer Expires by fields are set to " Unknown" when the LSC is issued to a device before the upgrade to Unified Communications Manager 11.5(1). From the second Find
                                             				  Phone where drop-down list box, choose one of the following
                                          				criteria: is before is exactly is after begins with contains ends with is exactly is empty is not empty | Note | The status of LSC
                                                         					 Expires and LSC
                                                         					 Issuer Expires by fields are set to "NA" when
                                                      				  there is no LSC issued on a new device. The status of LSC Expires and LSC Issuer Expires by fields are set to " Unknown" when the LSC is issued to a device before the upgrade to Unified Communications Manager 11.5(1). |
| Note | The status of LSC
                                                         					 Expires and LSC
                                                         					 Issuer Expires by fields are set to "NA" when
                                                      				  there is no LSC issued on a new device. The status of LSC Expires and LSC Issuer Expires by fields are set to " Unknown" when the LSC is issued to a device before the upgrade to Unified Communications Manager 11.5(1). |
| Step 3 | Specify the
                                       			 appropriate search text, if applicable. Tip To find all
                                                      				  phones that are registered in the database, click Find without entering any search text. | Tip | To find all
                                                      				  phones that are registered in the database, click Find without entering any search text. |
| Tip | To find all
                                                      				  phones that are registered in the database, click Find without entering any search text. |
| Step 4 | To further
                                       			 define your query and to add multiple filters, check the Search
                                          				Within Results check box, choose AND or OR from the drop-down box, and repeat Step 2 and Step 3 . |
| Step 5 | Click Find . A list of
                                       			 discovered phones displays. The Update
                                          				Phones window displays the details of the phones that you choose. |

| Note | To update all
                                                      				  phones, click Find and do not specify a query. Skip the rest of
                                                      				  this procedure and proceed to choose the update parameters for the phones. |
|---|---|

| Note | The status of LSC
                                                         					 Expires and LSC
                                                         					 Issuer Expires by fields are set to "NA" when
                                                      				  there is no LSC issued on a new device. The status of LSC Expires and LSC Issuer Expires by fields are set to " Unknown" when the LSC is issued to a device before the upgrade to Unified Communications Manager 11.5(1). |
|---|---|

| Tip | To find all
                                                      				  phones that are registered in the database, click Find without entering any search text. |
|---|---|

| Note | Do not use the insert or export transaction files that are created
                                          			 with bat.xlt for the update transaction. Instead, you must create a custom file
                                          			 with details of the phone records that need to be updated. Use only this file
                                          			 for the update transaction. |
|---|---|

| Note | Enter values for device name, description, or directory number
                                                   				  in the custom update file. You do not need to include a header in the custom
                                                   				  update file. |
|---|---|

| Step 1 | Choose Bulk
                                             				  Administration > Phones > Update
                                             				  Phones > Use Custom File . The Update Phones Custom Configuration window
                                          				displays. |
|---|---|
| Step 2 | In the Update Phones where drop-down list box, choose
                                       			 the type of custom file that you have created from the following criteria: Device Name Directory Number Description |
| Step 3 | In the list of custom files, choose the filename of the custom
                                       			 file for this update. |
| Step 4 | Click Find . If the query results are not what you expected, you can change the
                                          				custom file selections. |

| Step 1 | In the Update Phones Query window, click Next . The Update Phones shows the type of query that you
                                       			 chose. If you want to change the type of query, click Back . |
|---|---|
| Step 2 | Choose the Logout Users before Update check
                                       			 box to log out the users prior to the update. You can also use this option to bulk log out users if no fields
                                       			 are chosen. |
| Step 3 | Specify the setting that you want to update for all the records
                                       			 that you have defined in your query or custom file. You can choose multiple
                                       			 parameters to update. See the Table 1 for descriptions of parameters. |
| Step 4 | Select the update check box to the left of the field that you want
                                       			 to update. This tells BAT to overwrite the existing value for the field. Note Be aware that BAT updates only those fields for which you have
                                                      				  selected the update check box. | Note | Be aware that BAT updates only those fields for which you have
                                                      				  selected the update check box. |
| Note | Be aware that BAT updates only those fields for which you have
                                                      				  selected the update check box. |
| Step 5 | In the Value field for the checked parameter, enter
                                       			 the new value or choose a value from the list box. |
| Step 6 | In the Reset/Restart Phones area, check one of the
                                       			 following choices: Don't
                                                				Reset/Restart phones/Apply Config —To reset/restart devices at a later
                                             			 time. Reset
                                                				phones —To reset (power-cycle) the phones Restart
                                                				phones —To reset phones without power-cycling Apply
                                                				Config —To reset only the settings that have changed since the last
                                             			 reset |
| Step 7 | Update the required phone parameters. See Table 1 for field descriptions. |
| Step 8 | To create a job for updating the records, click Submit . Use the Job Scheduler option in the Bulk Administration main
                                       			 menu to schedule and activate this job. |

| Note | Be aware that BAT updates only those fields for which you have
                                                      				  selected the update check box. |
|---|---|

| Note | Be aware that
                                          			 some fields have two check boxes. The first check box determines if you need to
                                          			 update the field; the second check box determines the value (checked or
                                          			 unchecked) to use for the field. |
|---|---|

| Tip | Check the first
                                          			 check box if you need to update the field and the second check box to apply a
                                          			 checked value to the phones you select. For example, if you check the first
                                          			 check box for Do Not Disturb and leave the second one unchecked, you update
                                          			 phones with an unchecked value for Do Not Disturb. |
|---|---|

| Field | Description |
|---|---|
| Description | Enter a description that makes the device easy to recognize. The description can include up to 50 characters in any language,
                                          but it cannot include double-quotes ("), percentage sign ( % ), ampersand (&), back-slash ( \ ), or angle brackets (<>). |
| DevicePool | Choose the device pool to which this group of phones/ports should belong. A devicepool defines sets of common characteristics for devices, such as region, date/time group, Unified Communications Manager group, and calling search space for auto-registration. |
| Common Device Configuration | Choose the common device configuration to which you want this phone assigned. The common device configuration includes the
                                          attributes (services or features) that are associated with a particular user. To see the common device configuration settings, click the View Details link. |
| Phone Button Template | Choose the appropriate phone button template. The phone button template determines the configuration of buttons on a phone
                                          and identifies which feature (line, speed dial, and so on) is used for each button. Unified Communications Manager does not make this field available for H.323 clients or CTI ports. |
| Softkey Template | Choose the softkey template to be used for all phones in this group. |
| Common Phone Profile | From the drop-down list, choose a common phone profile from the list of available common phone profiles. |
| Calling Search Space | Choose the calling search space to which this group of phones/ports should belong. A calling search space specifies the collection of route partitions that are searched to determine how a dialed number should
                                          be routed. |
| AAR Calling Search Space | Choose the appropriate calling search space for the device to use when it performs automated alternate routing (AAR). The
                                          AAR calling search space specifies the collection of route partitions that are searched to determine how to route a collected
                                          (originating) number that is otherwise blocked due to insufficient bandwidth. |
| Media Resource Group List | Choose the media resource group list (MRGL) to which this group of phones/ports should belong. An MRGL specifies a list of prioritized media resource groups. An application can choose required media resources among the
                                          available ones according to the priority order that is defined in the MRGL. |
| User Hold MOH Audio Source | Choose the user-hold audio source for this group of phones or ports. The user-hold audio source plays music when a user places a call on hold. |
| Network Hold MOH Audio Source | Choose the network hold audio source that this group of IP phones or CTI ports should use. The network-hold audio source plays music when the system places a call on hold, such as when the user transfers or parks
                                          a call. |
| Location | Choose the location to which this group of phones/ports should belong. A location indicates the remote location that is accessed by using restricted bandwidth connections. |
| AAR Group | Choose the automated alternate routing (AAR) group for this device. The AAR group provides the prefix digits that are used
                                          to route calls that are otherwise blocked due to insufficient bandwidth. If no AAR group is specified, Unified Communications Manager uses the AAR group that is associated with Device Pool or Line. |
| User Locale | Choose the country and language set that you want to associate with this user. This choice determines which cultural-dependent attributes exist for this user and which language displays for the user in
                                          the Unified Communications Manager user windows and phones. |
| Network Locale | Choose the network locale that you want to associate with this user. The Network Locale comprises a set of tones and cadences that Cisco gateways and phones use when they are communicating with
                                          the PSTN and other networks in a specific geographical area. |
| Built in Bridge | Enable or disable the built-in conference bridge for the barge feature by using the Built In Bridge drop-down list (choose
                                          On, Off, or Default). |
| Privacy | For each phone that wants Privacy, choose On in the Privacy drop-down list. For more configuration information, refer to Barge and Privacy Features in the Feature Configuration Guide for Cisco Unified Communications Manager . |
| Device Mobility Mode | From the drop-down list, turn the device mobility feature on or off for this device or choose Default to use the default device
                                          mobility mode. Click View Current Device Mobility Settings to display the current values of these device mobility parameters: Cisco Unified Communications Manager Group Roaming Device Pool Location Region Network Locale AAR Group AAR Calling Search Space Device Calling Search Space Media Resource Group List SRST |
| Mobility User ID | From the drop-down list, choose the user ID of the person to whom this dual-mode phone is assigned. Note Be aware that the Mobility User ID configuration is used for Mobile Connect and Mobile Voice Access for dual mode phones. Note The Owner User ID and Mobility User ID can differ. | Note | Be aware that the Mobility User ID configuration is used for Mobile Connect and Mobile Voice Access for dual mode phones. | Note | The Owner User ID and Mobility User ID can differ. |
| Note | Be aware that the Mobility User ID configuration is used for Mobile Connect and Mobile Voice Access for dual mode phones. |
| Note | The Owner User ID and Mobility User ID can differ. |
| Owner User ID | Enter a user ID for the primary phone user. |
| Phone Personalization | From the drop-down list, enable or disable the Cisco Unified Phone Designer feature for this device or choose Default to use
                                          the phone personalization that is set in the Common Phone Profile. Disabled—None of the Cisco Unified Phone Application Suite features get activated. Enabled—This setting accepts a personalized background image file, which is used for the phone screen; it accepts a preview
                                                image file for temporary display; and it accepts a personalized tone file, so the default ring tone can be personalized. Default—Use the phone personalization setting that is in the Common Phone Profile. |
| Services Provisioning | From the drop-down list, choose the Services Provisioning setting that you want to use from the following values: Internal External URLs Both Default: Internal This parameter controls whether the phone uses the services provisioned from the configuration file (Internal), services received
                                          from the Services URLs (External URLs), or both. The External URLs option provides backward compatibility with third party
                                          provisioning servers. The Both option allows users to subscribe to the services specified in the configuration file while
                                          also appending services from an external provisioning server. This is a required field. |
| Phone Load Name | Enter the custom phone load, if applicable. Note Any value that is entered in this field overrides the default value for the chosen model and specifies the custom software
                                                      for a CiscoUnifiedIPPhone. | Note | Any value that is entered in this field overrides the default value for the chosen model and specifies the custom software
                                                      for a CiscoUnifiedIPPhone. |
| Note | Any value that is entered in this field overrides the default value for the chosen model and specifies the custom software
                                                      for a CiscoUnifiedIPPhone. |
| Single Button Barge | From the drop-down list, enable or disable the Single Button Barge/cBarge feature for this device or choose Default to use
                                          the service parameter setting. Off—This setting disables the Single Button Barge/cBarge feature; however, the regular Barge or cBarge features will still
                                                work. Barge—This setting enables the Singe Button Barge feature. cBarge—This setting enables the Single Button cBarge feature. Default—This setting uses the Single Button Barge/cBarge setting that is in the service parameter. |
| Join Across Lines | From the drop-down list, enable or disable the Join Across Lines feature for this device or choose Default to use the service
                                          parameter setting. Off—This setting disables the Join Across Lines feature. On—This setting enables the Join Across Lines feature. Default—This setting uses the Join Across Lines setting that is in the service parameter. |
| Use Trusted Relay Point | From the drop-down list, enable or disable whether Unified Communications Manager inserts a trusted relay point (TRP) device with this media endpoint. Choose one of the following values: Default—If you choose this value, the device uses the Use Trusted Relay Point setting from the common device configuration
                                                with which this device associates. Off—Choose this value to disable the use of a TRP with this device. This setting overrides the Use Trusted Relay Point setting
                                                in the common device configuration with which this device associates. On—Choose this value to enable the use of a TRP with this device. This setting overrides the Use Trusted Relay Point setting
                                                in the common device configuration with which this device associates. A Trusted Relay Point (TRP) device designates an MTP or transcoder device that is labeled as Trusted Relay Point. Unified Communications Manager places the TRP closest to the associated endpoint device if more than one resource is needed for the endpoint (for example,
                                          a transcoder or RSVP Agent). If both TRP and MTP are required for the endpoint, TRP gets used as the required MTP. |
| Calling Party Transformation CSS | This setting allows you to localize the calling party number on the device. Make sure that the Calling Party Transformation
                                          CSS that you choose contains the calling party transformation pattern that you want to assign to this device. The device takes on the attributes of the Calling Party Transformation Pattern when you assign the pattern to a partition
                                          where the Calling Party Transformation CSS exists. |
| Geolocation | From the drop-down list, choose a geolocation. You can choose the Unspecified geolocation, which designates that this device does not associate with a geolocation. You can also choose a geolocation that has been configured with the System > Geolocation Configuration menu option. |
| Emergency Location (ELIN) Group | Choose the Emergency Location (ELIN) group to which this group of phones should belong. An ELIN group identifies a location
                                          to which ELINs under this ELIN group must be mapped in the ALI database. |
| Feature Control Policy | Choose the Feature Control Policy for this group of phones. A feature control policy specifies the appearance of features and the associated softkeys that display on the phone. |
| BLF Audible Alert Setting (Phone Idle) | For this required field, from the drop-down list, choose the BLF Audible Alert setting that you want to use from the following
                                          values: On Off Default This parameter provides an audible alert in addition to a visual alert on a phone that is currently idle when a call comes
                                          in to one of the lines that is monitored by way of a busy lamp field (BLF) button. |
| BLF Audible Alert Setting (Phone Busy) | For this required field, this parameter provides an audible alert in addition to a visual alert on a phone that is currently
                                          in use when a call comes in to one of the lines that is monitored by way of a busy lamp field (BLF) button. From the drop-down list, choose the BLF Audible Alert setting that you want to use from the following values: On Off Default |
| Always Use Prime Line | From the drop-down list, choose the Always Use Prime Line setting that you want to use from the following values: On Off Default |
| Always Use Prime Line for Voice Message | From the drop-down list, choose the Always Use Prime Line for Voice Message setting that you want to use from the following
                                          values: On Off Default |
| Use Device Pool Calling Party Transformation CSS | To use the Calling Party Transformation CSS that is configured in the device pool that is assigned to this device, check this
                                          check box. If you do not check this check box, the device uses the Calling Party Transformation CSS that you configured in
                                          the device configuration window. |
| Ignore Presentation Indicators | Check this check box if the system must ignore presentation indicators. |
| Retry Video Call as Audio | Check this check box to retry a video call as an audio call. |
| Allow Control of Device from CTI | Check this check box to allow CTI to control and monitor this device. If the associated directory number specifies a shared line, the check box should remain enabled as long as at least one associated
                                          device specifies a combination of device type and protocol that CTI supports. Note Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                      controlled. However, devices operating in GSM mode cannot be monitored or controlled. | Note | Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                      controlled. However, devices operating in GSM mode cannot be monitored or controlled. |
| Note | Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                      controlled. However, devices operating in GSM mode cannot be monitored or controlled. |
| Logged into Hunt Group | This check box, which gets checked by default for all phones, indicates that the phone is currently logged in to a hunt list
                                          (group). When the phone gets added to a hunt list, the administrator can log the user in or out by checking (and unchecking)
                                          this check box. Users use the softkey on the phone to log their phone in or out of the hunt list. |
| Remote Device | If you are experiencing delayed connect times over SCCP to remote sites, check the Remote Device check box in the Phone Configuration window. Checking this check box tells Unified Communications Manager to allocate a buffer for the phone device when it registers and to bundle SCCP messages to the phone. Note Because this feature consumes resources, be sure to check this check box only when you are experiencing signaling delays for
                                                      phones that run SCCP. Most users do not require this option. | Note | Because this feature consumes resources, be sure to check this check box only when you are experiencing signaling delays for
                                                      phones that run SCCP. Most users do not require this option. |
| Note | Because this feature consumes resources, be sure to check this check box only when you are experiencing signaling delays for
                                                      phones that run SCCP. Most users do not require this option. |
| Protected Device | Check this check box to designate a phone as "protected." This enables the phone to play a two-second tone notifying the user when a call is both encrypted and both phones are configured
                                          as protected devices. The tone plays for both parties when the call is answered. The tone does not play unless both phones
                                          are "protected" and the call occurs over encrypted media. |
| Protocol Specific Information |
| Packet Capture Mode | From the drop-down list, choose the mode that you want to set for signal packet capture: None—Choose None if you do not want to specify a mode. Real-Time Mode—Use this mode for real-time signal packet capture. Batch Processing Mode—Use this mode for batch processing signal packet capture mode. |
| Packet Capture Duration | Enter the time for packet capture in minutes. You can enter a maximum duration of 300 minutes. The default duration specifies
                                          60 minutes. |
| Presence Group | Used with the Presence feature, the phones that is running SIP or SCCP serves as a watcher because it requests status about
                                          the presence entity, for example, directory number, that is configured as a BLF speed dial button on the phone. If you want the phone to receive the status of the presence entity, choose a Presence Group that is allowed to view the status
                                          of the Presence Group that is applied to the directory number, as indicated in the Presence Group Configuration window. |
| Device Security Profile | For phones that run SCCP and SIP, choose the security profile that you want to apply to the device. All phones require that you apply a security profile. If the phone does not support security, choose a nonsecure profile. Tip The CAPF settings that are configured in the profile relate to the Certificate Authority Proxy Function settings that display
                                                   in the Phone Configuration window. If you want to manage manufacture-installed certificates (MICs) or locally significant certificates (LSC), you must
                                                   configure the CAPF settings in the profile and in the Phone Configuration window. | Tip | The CAPF settings that are configured in the profile relate to the Certificate Authority Proxy Function settings that display
                                                   in the Phone Configuration window. If you want to manage manufacture-installed certificates (MICs) or locally significant certificates (LSC), you must
                                                   configure the CAPF settings in the profile and in the Phone Configuration window. |
| Tip | The CAPF settings that are configured in the profile relate to the Certificate Authority Proxy Function settings that display
                                                   in the Phone Configuration window. If you want to manage manufacture-installed certificates (MICs) or locally significant certificates (LSC), you must
                                                   configure the CAPF settings in the profile and in the Phone Configuration window. |
| SUBSCRIBE Calling Search Space | Used with the Presence feature, the SUBSCRIBE Calling Search Space determines how Unified Communications Manager routes the subscription requests that come from the phone. From the drop-down list, choose the calling search space that
                                          you want to use for this purpose. |
| Outbound Call Rollover | From the drop-down list, choose the rollover option that you want to use for outbound calls. No Rollover—Choose this option to Switch off the rollover feature. Conference and transfer will not work in this mode. Rollover within the same DN—Choose this option to use rollover within the same DN. Conferences and call transfers complete
                                          by using the same directory number (on different lines). Rollover to any line—Choose this option to roll over to any line. Conferences and call transfers complete by using a different
                                          directory number and line than the original call. |
| Unattended Port | Check this check box to indicate an unattended port on this device. |
| Require DTMF Reception | For phones that run SIP and SCCP, check this check box to require DTMF reception for this phone. |
| External Data Locations Information |
| Information | Enter the help text URL for the information button. |
| Directory | Enter the URL of the directory server. |
| Messages | Enter the voice-messaging access pilot number. |
| Services | Enter the URL for the services menu. |
| Authentication Server | Enter the URL that the phone uses to validate requests that are made to the phones web server. If you do not provide an authentication
                                          URL, the advanced features on CiscoUnifiedIPPhones that require authentication will not function. Leave this field blank to
                                          accept the default setting. By default, this URL accesses a CiscoUnifiedIPPhone Self Care Portal window that was configured during installation. |
| Proxy Server | Enter the host and port (for example, proxy.cisco.com:80) that are used to proxy HTTP requests for access to non-local host
                                          addresses from the phones HTTP client. If the phone receives a URL such as www.cisco.com in a service and the phone is not configured in the cisco.com domain, the
                                          phone uses the proxy server to access the URL. If the phone is configured in the cisco.com domain, the phone accesses the
                                          URL without using the proxy because it is in the same domain as the URL. Leave this field blank to accept the default setting. |
| Idle | Enter the URL to display on the CiscoUnifiedIPPhone screen when the phone has not been used for the time that is specified
                                          in the Idle Time field. For example, you can display a logo on the screen when the phone has not been used for 5 minutes.
                                          Leave this field blank to use the default value. |
| Idle Timer | Enter the seconds that you want to elapse before the phone displays the URL that is specified in the Idle field. Leave this
                                          field blank to use the default value. |
| Secure Authentication URL | Enter the secure URL that the phone uses to validate requests that are made to the phone web server. Note If you do not provide a Secure Authentication URL, the device uses the nonsecure URL. If you provide both a secure URL and
                                                      a nonsecure URL, the device chooses the appropriate URL, based on its capabilities. By default, this URL accesses a CiscoUnifiedIPPhone Self Care Portal window that was configured during installation. Leave this field blank to accept the default setting. Maximum length specifies 255 characters. | Note | If you do not provide a Secure Authentication URL, the device uses the nonsecure URL. If you provide both a secure URL and
                                                      a nonsecure URL, the device chooses the appropriate URL, based on its capabilities. |
| Note | If you do not provide a Secure Authentication URL, the device uses the nonsecure URL. If you provide both a secure URL and
                                                      a nonsecure URL, the device chooses the appropriate URL, based on its capabilities. |
| Secure Directory URL | Enter the secure URL for the server from which the phone obtains directory information. This parameter specifies the URL that
                                          secured Cisco Unified IP Phones use when you press the Directory button. Note If you do not provide a Secure Directory URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. Leave this field blank to accept the default setting. Maximum length specifies 255 characters. | Note | If you do not provide a Secure Directory URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
| Note | If you do not provide a Secure Directory URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
| Secure Idle URL | Enter the secure URL for the information that displays on the Cisco Unified IP Phone display when the phone is idle, as specified in the Idle Timer field. For example, you can display a logo on the LCD when
                                          the phone has not been used for 5 minutes. Note If you do not provide a Secure Idle URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. To accept the default setting, leave this field blank. Maximum length specifies 255 characters. | Note | If you do not provide a Secure Idle URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
| Note | If you do not provide a Secure Idle URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
| Secure Information URL | Enter the secure URL for the server location where the Cisco Unified IP Phone can find help text information. This information
                                          displays when the user presses the information (i) button or the question mark ( ? ) button. Note If you do not provide a Secure Information URL, the device uses the nonsecure URL. If you provide both a secure URL and a
                                                      nonsecure URL, the device chooses the appropriate URL, based on its capabilities. To accept the default setting, leave this field blank. Maximum length specifies 255 characters. | Note | If you do not provide a Secure Information URL, the device uses the nonsecure URL. If you provide both a secure URL and a
                                                      nonsecure URL, the device chooses the appropriate URL, based on its capabilities. |
| Note | If you do not provide a Secure Information URL, the device uses the nonsecure URL. If you provide both a secure URL and a
                                                      nonsecure URL, the device chooses the appropriate URL, based on its capabilities. |
| Secure Messages URL | Enter the secure URL for the messages server. The Cisco Unified IP Phone contacts this URL when the user presses the Messages
                                          button. Note If you do not provide a Secure Messages URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. To accept the default setting, leave this field blank. Maximum length specifies 255 characters. | Note | If you do not provide a Secure Messages URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
| Note | If you do not provide a Secure Messages URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
| Secure Services URL | Enter the secure URL for Cisco Unified IP Phone services. This setting specifies the location that the secure Cisco Unified IP Phone contacts when the user presses the Services button. Note If you do not provide a Secure Services URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. To accept the default setting, leave this field blank. Maximum length specifies 255 characters. | Note | If you do not provide a Secure Services URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
| Note | If you do not provide a Secure Services URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
| Hotline Device | Enter T or F. Hotline devices can connect only to other Hotline devices. This feature extends the PLAR feature, which configures
                                          a phone to automatically dial one directory number when it goes off-hook. Hotline provides additional restrictions that you
                                          can apply to devices that use PLAR. To implement Hotline, you must also create a softkey template without supplementary service softkeys and apply the softkey
                                          template to the Hotline device. |
| Extension Information |
| Enable Extension Mobility | Check this check box to enable extension mobility. Choose 0-Off to disable this feature, or choose 1-On to enable this feature. Extension mobility allows a user to log in and out of a Cisco Unified IP Phone . |
| IP Services1 | Use Unified Communications Manager to choose any services that have been configured. |
| IP Services2 | Use Unified Communications Manager to choose any services that have been configured. Using Unified Communications Manager Bulk Administration (BAT), you cannot update more than two IP services in one transaction. |
| Certification Authority Proxy Function (CAPF) Information (These parameters display only for devices with the capability to support authentication or encryption.) |
| Certificate Operation | From the drop-down list, choose the Certification Operation that you want to perform from the following options: No Pending Operation—No pending Certification Operation lists exist for this device. Choosing this option disables the remaining
                                                CAPF fields. Install/Upgrade—Install or upgrade a Certification Operation. Delete—Delete a Certification Operation. Troubleshoot—Troubleshoot a Certification Operation. |
| Generate Unique Authentication String for Each Device | Check this check box if you want a unique authentication string to be generated for each device. |
| Authentication String | If Authentication Mode is By Authentication String, enter the Authentication String. Alternately, to get a system-generated
                                          string, click Generate String . |
| Operation Completes By | Enter the date by which the Certification Operation will complete. The date format specifies YYYY: MM: DD: HH. The default
                                          completion date specifies 10 days from the current system date. |
| MultiLevel Precedence and Preemption (MLPP) Information |
| MLPP Indication | If available, this setting specifies whether a device that is capable of playing precedence tones will use the capability
                                          when it places an MLPP precedence call. From the drop-down list, choose a setting to assign to this device from the following options: Default—This device inherits its MLPP indication setting from its device pool. Off—This device does not send indication of an MLPP precedence call. On—This device does send indication of an MLPP precedence call. Note Do not configure a device with the following combination of settings: MLPP Indication is set to Off while MLPP Preemption
                                                      is set to Forceful. | Note | Do not configure a device with the following combination of settings: MLPP Indication is set to Off while MLPP Preemption
                                                      is set to Forceful. |
| Note | Do not configure a device with the following combination of settings: MLPP Indication is set to Off while MLPP Preemption
                                                      is set to Forceful. |
| MLPP Preemption | If available, this setting specifies whether a device that is capable of preempting calls in progress will use the capability
                                          when it places an MLPP precedence call. From the drop-down list, choose a setting to assign to this device from the following options: Default—This device inherits its MLPP preemption setting from its device pool. Disabled—This device does not preempt calls in progress when it places an MLPP precedence call. Forceful—This device preempts calls in progress when it places an MLPP precedence call. Note Do not configure a device with the following combination of settings: MLPP Indication is set to Off while MLPP Preemption
                                                      is set to Forceful. | Note | Do not configure a device with the following combination of settings: MLPP Indication is set to Off while MLPP Preemption
                                                      is set to Forceful. |
| Note | Do not configure a device with the following combination of settings: MLPP Indication is set to Off while MLPP Preemption
                                                      is set to Forceful. |
| MLPP Domain (e.g., "0000FF") | Enter a hexadecimal value for the MLPP domain that is associated with this device. Ensure that this value is blank or a value
                                          between 0 and FFFFFF. |
| Do Not Disturb (DND) |
| Do Not Disturb | If you want to enable the DND feature, check this check box. |
| DND Option | From the drop-down list, choose a DND option from the following options: None Ringer Off Call Reject Use Common Phone Profile Setting |
| DND Incoming Call Alert | From the drop-down list, choose one of the following options: None Disable Flash Only Beep Only |
| Secure Shell Information |
| Secure Shell User | Enter a user ID for the secure shell user. If the phone that you are configuring does not support secure shell access, this
                                          field does not display. Cisco Technical Assistance Center (TAC) uses secure shell for troubleshooting. Contact TAC for further
                                          assistance. |
| Secure Shell Password | Enter the password for a secure shell user. If the phone that you are configuring does not support secure shell access, this
                                          field does not display. Contact TAC for further assistance. |
| Assign IP Phone Services |
| Add All Services From This Template | From the drop-down list, choose the template that contains list of services with which you want to update the phones. You can click the Edit IP Phone Service link to update the subscribed CiscoUnifiedIP Phones services on the template. |
| Remove Duplicate | Check this check box to remove duplicate IP phone services. If you check this check box, the system removes the duplicate
                                          service subscriptions from phones and user device profiles. The IP system deletes services based on the IP service name. |
| Product Specific Information |
| Device Security Mode | From the drop-down list, choose the mode that you want to set for the device: Use System Default—The phone uses the value that you specified for the enterprise parameter, Device Security Mode. Non-secure—No security features exist for the phone. A TCP connection opens to Unified Communications Manager . Authenticated— Unified Communications Manager provides integrity and authentication for the phone. A TLS connection that uses NULL/SHA opens. Encrypted— Unified Communications Manager provides integrity, authentication, and encryption for the phone. A TLS connection that uses AES128/SHA opens This field applies only if the phone model supports authentication or encryption. |
| Remove Duplicate IP Services from all Phones and Device Profiles | Check this check box to remove duplicate IP phone services. If you check this check box, the system removes the duplicate
                                          service subscriptions from phones and user device profiles. The IP system deletes services based on the IP service name. |
| Disable SpeakerPhone | Check this check box to disable the speakerphone. |
| Disable Speakerphone and Headset | Check this check box to disable the speakerphone and headset. |
| Forwarding Delay | Use this field to enable or disable forwarding delay. Choose enable when you want the port to wait a few seconds before forwarding
                                          a call. |
| PC Port | Use this field to enable or disable the PC port on phones that have internal switches. Users can connect a PC or workstation
                                          to the phone by using the port labeled "10 / 100 PC" on the back of the phone. |
| Setting Access | Use this field to choose whether the user has access to phone settings. The options include Enabled and Disable. |
| Gratuitous ARP | Choose Enabled or Disabled to control gratuitous ARP. |
| PC Voice VLAN Access | Choose Enabled or Disabled to control access to a PC voice VLAN. |
| Video Capabilities | Choose Enabled or Disabled to control video capabilities access. |
| Auto Line Select | Choose Enabled or Disabled to allow or disallow automatic line selection on the phone. |
| Web Access | Choose Enabled or Disabled to allow web access on the phone. |

| Note | Be aware that the Mobility User ID configuration is used for Mobile Connect and Mobile Voice Access for dual mode phones. |
|---|---|

| Note | The Owner User ID and Mobility User ID can differ. |
|---|---|

| Note | Any value that is entered in this field overrides the default value for the chosen model and specifies the custom software
                                                      for a CiscoUnifiedIPPhone. |
|---|---|

| Note | Cisco dual-mode devices (Jabber) such as Android, iPhone, and iPad operating in WiFi mode are monitored through CTI and not
                                                      controlled. However, devices operating in GSM mode cannot be monitored or controlled. |
|---|---|

| Note | Because this feature consumes resources, be sure to check this check box only when you are experiencing signaling delays for
                                                      phones that run SCCP. Most users do not require this option. |
|---|---|

| Tip | The CAPF settings that are configured in the profile relate to the Certificate Authority Proxy Function settings that display
                                                   in the Phone Configuration window. If you want to manage manufacture-installed certificates (MICs) or locally significant certificates (LSC), you must
                                                   configure the CAPF settings in the profile and in the Phone Configuration window. |
|---|---|

| Note | If you do not provide a Secure Authentication URL, the device uses the nonsecure URL. If you provide both a secure URL and
                                                      a nonsecure URL, the device chooses the appropriate URL, based on its capabilities. |
|---|---|

| Note | If you do not provide a Secure Directory URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
|---|---|

| Note | If you do not provide a Secure Idle URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
|---|---|

| Note | If you do not provide a Secure Information URL, the device uses the nonsecure URL. If you provide both a secure URL and a
                                                      nonsecure URL, the device chooses the appropriate URL, based on its capabilities. |
|---|---|

| Note | If you do not provide a Secure Messages URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
|---|---|

| Note | If you do not provide a Secure Services URL, the device uses the nonsecure URL. If you provide both a secure URL and a nonsecure
                                                      URL, the device chooses the appropriate URL, based on its capabilities. |
|---|---|

| Note | Do not configure a device with the following combination of settings: MLPP Indication is set to Off while MLPP Preemption
                                                      is set to Forceful. |
|---|---|

| Note | Do not configure a device with the following combination of settings: MLPP Indication is set to Off while MLPP Preemption
                                                      is set to Forceful. |
|---|---|