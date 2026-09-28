---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmefiles-html-8ab08f0b7e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmefiles.html
retrieved_at: 2026-08-21T07:22:29.894722+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Configuration
	 Files for Phones

## Chapter: Configuration
	 Files for Phones

# Configuration
                     	 Files for Phones

## Information About Configuration Files

### Configuration Files for Phones

When a phone requests service from Cisco Unified CME, the registrar
                              		confirms the username, i.e. the phone number for the phone. The phone accesses
                              		its configuration profile on the TFTP server, typically the Cisco Unified CME
                              		router, and processes the information contained in the file, registers itself,
                              		and puts the phone number on the phone console display.

Minimally, a configuration profile contains the MAC address, the type,
                              		and the phone number that is permitted by the registrar to handle the Register
                              		message for a particular Cisco  Unified IP phone.

Any time you create or modify parameters for either an individual phone
                              		or a directory number, generate a new phone configuration to properly propagate
                              		the parameters.

By default, there is one shared XML configuration file located in
                              		system:/its/ for all Cisco Unified IP phones that are running SCCP. For SIP
                              		phones directly connected to Cisco Unified CME, an individual configuration
                              		profile is created for each phone and stored in system:/cme/sipphone/.

When an IP phone comes online or is rebooted, it automatically gets
                              		information about itself from the appropriate configuration file.

The Cisco universal application loader for phone firmware files allows
                              		you to add additional phone features across all protocols. To do this, a hunt
                              		algorithm searches for multiple configuration files. After a phone is reset or
                              		restarted, the phone automatically selects protocol depending on which matching configuration file is found first. To ensure that
                              		Cisco Unified IP phones download the appropriate configuration for the desired
                              		protocol, SCCP or SIP, you must properly configure the IP phones before connecting or rebooting the phones. The hunt algorithm searches for files in
                              		the following order:

CTLSEP <mac> file for a SCCP phone—For example,
                                    			 CTLSEP003094C25D2E.tlv

SEP <mac> file for a SCCP phone—For example,
                                    			 SEP003094C25D2E.cnf.xml

SIP <mac> file for a SIP phone—For example,
                                    			 SIP003094C25D2E.cnf or gk003069C25D2E

XML default file for SCCP phones—For example, SEPDefault.cnf.xmls

XML default file for SIP phones—For example, SIPDefault.cnf

In Cisco Unified CME 4.0 and later for SCCP and in Cisco CME 3.4 and
                              		later for SIP, you can designate one of the following locations in which to
                              		store configuration files:

System (Default)—For SCCP phones, one configuration file is created,
                                    			 stored, and used for all phones in the system. For SIP phones, an individual
                                    			 configuration profile is created for each phone.

Flash or slot 0—When flash or slot 0 memory on the router is the
                                    			 storage location, you can create additional configuration files to be applied
                                    			 per phone type or per individual phone, such as user or network locales.

TFTP—When an external TFTP server is the storage location, you can
                                    			 create additional configuration files to be applied per phone type or per
                                    			 individual phone, which are required for multiple user and network locales.

### Per-Phone
                           	 Configuration Files

If configurations
                              		files for SCCP phones are to be stored somewhere other than in the default
                              		location, the following individual configuration files can be created for SCCP
                              		phones:

Per phone
                                    			 type—Creates separate configuration files for each phone type and all phones of
                                    			 the same type use the same configuration file. This method is not supported if
                                    			 the configuration files are to be stored in the system location.

Per
                                    			 phone—Creates a separate configuration file for each phone, by MAC address.
                                    			 This method is not supported if the configuration files are to be stored in the
                                    			 system location.

For configuration
                              		information, see Define Per-Phone Configuration Files and Alternate Location for SCCP Phones .

## Generate Configuration Files for Phones

### Generate
                           	 Configuration Files for SCCP Phones

To generate the
                                 		  configuration profile files that are required by the SCCP phones in
                                 		  Cisco Unified CME and write them to either system memory or to the location
                                 		  specified by the cnf-file location command, follow the steps in this section.

Restriction

Externally
                                                   				  stored and per-phone configuration files are not supported on the
                                                   				  Cisco Unified IP Phone 7902G, 7910, 7910G, or 7920, or the Cisco Unified IP
                                                   				  Conference Station 7935 and 7936.

TFTP does
                                                   				  not support file deletion. When configuration files are updated, they overwrite
                                                   				  any existing configuration files with the same name. If you change the
                                                   				  configuration file location, files are not deleted from the TFTP server.

Generating
                                                   				  configuration files on flash or slot 0 can take up to a minute, depending on
                                                   				  the number of files being generated.

F or smaller
                                                   				  routers such as Cisco 2600 series routers, you must manually enter the squeeze command to erase files after changing the configuration file location or
                                                   				  entering any commands that trigger the deletion of configuration files. Unless
                                                   				  you use the squeeze command, the space used by the moved or deleted configuration files is not
                                                   				  usable by other files.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- create cnf-files

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

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

create cnf-files

#### Example:

```
Router(config-telephony)# create cnf-files
```

Builds the XML
                                             				configuration files required for IP phones.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Configuration Files for SCCP Phones

To verify the Cisco Unified CME phone configuration, perform the
                                 		  following steps.

Step 1

show telephony-service all

Use this command to verify the configuration for phones, directory
                                             				numbers, voice ports, and dial peers in Cisco Unified CME.

#### Example:

```
Router# show telephony-service all CONFIG (Version=4.0(0)) 
			 =====================
			 Version 4.0(0) 
			 Cisco Unified CallManager Express 
			 For on-line documentation please see:
			 www.cisco.com/en/US/products/sw/voicesw/ps4625/tsd_products_support_series_home.html
			 
			 ip source-address 10.0.0.1 port 2000
			 max-ephones 24
			 max-dn 24
			 dialplan-pattern 1 408734....
			 voicemail 11111
			 transfer-pattern 510734....
			 keepalive 30
			 
			 ephone-dn 1
			 number 5001
			 huntstop
			 
			 ephone-dn 2
			 number 5002
			 huntstop
			 call-forward noan 5001 timeout 8
```

Step 2

show telephony-service tftp-bindings

Use this command to display the current configuration files
                                             				accessible to IP phones.

#### Example:

```
Router# show telephony-service tftp-bindings tftp-server system:/its/SEPDEFAULT.cnf 
			tftp-server system:/its/SEPDEFAULT.cnf alias SEPDefault.cnf
			tftp-server system:/its/XMLDefault.cnf.xml alias XMLDefault.cnf.xml
			tftp-server system:/its/ATADefault.cnf.xml
			tftp-server system:/its/XMLDefault7960.cnf.xml alias SEP00036B54BB15.cnf.xml
			tftp-server system:/its/germany/7960-font.xml alias German_Germany/7960-font.xml 
			tftp-server system:/its/germany/7960-dictionary.xml alias German_Germany/7960-dictionary.xml
			tftp-server system:/its/germany/7960-kate.xml alias German_Germany/7960-kate.xml
			tftp-server system:/its/germany/SCCP-dictionary.xml alias German_Germany/SCCP-dictionary.xml
			tftp-server system:/its/germany/7960-tones.xml alias Germany/7960-tones.xml
```

### Generate
                           	 Configuration Profiles for SIP Phones

To generate the
                                 		  configuration profile files that are required by the SIP phones in
                                 		  Cisco Unified CME and write them to the location specified by the tftp-path (voice register
                                       				global) command, follow the steps in this section.

Any time you
                                 		  create or modify parameters under the voice register dn or voice register pool
                                 		  configuration modes, generate a new configuration profile and properly
                                 		  propagate the parameters.

Caution

If your
                                             			 Cisco Unified CME system supports SCCP and also SIP phones, do not connect your
                                             			 SIP phones to the network until after you have verified the phone configuration
                                             			 profiles.

#### Before you begin

Cisco Unified CME 3.4 or a later version.

The mode cme
                                       				command must be enabled in Cisco Unified CME.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- file text

- create profile

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

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Step 4

file text

#### Example:

```
Router(config-register-global)# file text
```

(Optional)
                                             				Generates ASCII text files of the configuration profiles generated for
                                             				Cisco Unified IP Phone 7905s and 7905Gs, Cisco Unified IP Phone 7912s and
                                             				7912Gs, Cisco ATA-186, or Cisco ATA-188.

Default—System generates binary files to save disk space.

Step 5

create profile

#### Example:

```
Router(config-register-global;)# create profile
```

Generates
                                             				configuration profile files required for SIP phones and writes the files to the
                                             				location specified with tftp-path command.

Step 6

end

#### Example:

```
Router(config-register-global)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Verify
                           	 Configuration Profiles for SIP Phones

To verify the
                                 		  configuration profiles, perform the following steps. SIP phones to be connected
                                 		  to Cisco Unified CME can register and minimally, have an assigned phone number,
                                 		  only if the configuration is correct.

Step 1

show voice register tftp-bind

Use this
                                             				command to display a list of configuration profiles that are accessible to SIP
                                             				phones using TFTP. The file name includes the MAC address for each SIP phone,
                                             				such as SIP <mac-address>.cnf. Verify that a configuration profile is
                                             				available for each SIP phone in Cisco Unified CME.

The following
                                             				is sample output from this command:

#### Example:

```
Router(config)# show voice register tftp-bind tftp-server SIPDefault.cnf url system:/cme/sipphone/SIPDefault.cnf> 
tftp-server syncinfo.xml url system:/cme/sipphone/syncinfo.xml 
tftp-server SIP0009B7F7532E.cnf url system:/cme/sipphone/SIP0009B7F7532E.cnf 
tftp-server SIP000ED7DF7932.cnf url system:/cme/sipphone/SIP000ED7DF7932.cnf 
tftp-server SIP0012D9EDE0AA.cnf url system:/cme/sipphone/SIP0012D9EDE0AA.cnf 
tftp-server gk123456789012 url system:/cme/sipphone/gk123456789012 
tftp-server gk123456789012.txt url system:/cme/sipphone/gk123456789012.txt
```

Step 2

show voice register profile

Use this
                                             				command to display the contents of the ASCII format configuration profile for a
                                             				particular voice register pool.

To generate
                                                         				  ASCII text files of the configuration profiles for Cisco Unified IP Phone 7905s
                                                         				  and 7905Gs, Cisco Unified IP Phone 7912s and 7912Gs, Cisco ATA-186s, and Cisco
                                                         				  ATA-188s, use the file text command.

#### Example:

The following
                                             				is sample output from this command displaying information in the configuration
                                             				profile for voice register pool 4.

```
Router# show voice register profile text 4 Pool Tag: 4
# txt
AutoLookUp:0
DirectoriesUrl:0
…
CallWaiting:1
CallForwardNumber:0
Conference:1
AttendedTransfer:1
BlindTransfer:1
…
SIPRegOn:1
UseTftp:1
UseLoginID:0
UIPassword:0
NTPIP:0.0.0.0
UID:2468
```

Step 3

more system

Use this
                                             				command to display the contents of the configuration profile for a particular
                                             				Cisco Unified IP Phone 7940, Cisco Unified IP Phone 7905G, Cisco Unified IP
                                             				Phone 7960, or Cisco Unified IP Phone 7960G.

The following
                                             				is sample output from this command displaying information in two SIP
                                             				configuration profile files. The SIPDefault.cnf configuration profile is a
                                             				shared file and SIP < MAC address > .cnf is the SIP configuration profile
                                             				for the SIP phone with the designated MAC address.

```
Router# more system:/cme/sipphone/SIPDefault.cnf image_version: "P0S3-07-4-00";
proxy1_address: "10.1.18.100";
proxy2_address: "";
proxy3_address: "";
proxy4_address: "";
proxy5_address: "";
proxy6_address: "";
proxy1_port: "5060";
proxy2_port: "";
proxy3_port: "";
proxy4_port: "";
proxy5_port: "";
proxy6_port: "";
proxy_register: "1";
time_zone: "EST";
dst_auto_adjust: "1";
dst_start_month: "April";
dst_start_day: "";
dst_start_day_of_week: "Sun";
dst_start_week_of_month: "1";
dst_start_time: "02:00";
dst_stop_month: "October";
dst_stop_day: "";
dst_stop_day_of_week: "Sun";
dst_stop_week_of_month: "8";
dst_stop_time: "02:00";
date_format: "M/D/Y";
time_format_24hr: "0";
local_cfwd_enable: "1";
directory_url: "";
messages_uri: "2000";
services_url: "";
logo_url: "";
stutter_msg_waiting: "0";
sync: "0000200155330856";
telnet_level: "1";
autocomplete: "1";
call_stats: "0";
Domain_Name: "";
dtmf_avt_payload: "101";
dtmf_db_level: "3";
dtmf_inband: "1";
dtmf_outofband: "avt";
dyn_dns_addr_1: "";
dyn_dns_addr_2: "";
dyn_tftp_addr: "";
end_media_port: "32766";
http_proxy_addr: "";
http_proxy_port: "80";
nat_address: "";
nat_enable: "0";
nat_received_processing: "0";
network_media_type: "Auto";
network_port2_type: "Hub/Switch";
outbound_proxy: "";
outbound_proxy_port: "5060";
proxy_backup: "";
proxy_backup_port: "5060";
proxy_emergency: "";
proxy_emergency_port: "5060";
remote_party_id: "0";
sip_invite_retx: "6";
sip_retx: "10";
sntp_mode: "directedbroadcast";
sntp_server: "0.0.0.0";
start_media_port: "16384";
tftp_cfg_dir: "";
timer_invite_expires: "180";
timer_register_delta: "5";
timer_register_expires: "3600";
timer_t1: "500";
timer_t2: "4000";
tos_media: "5";
voip_control_port: "5060";

Router# more system:/cme/sipphone/SIP000CCE62BCED.cnf image_version: "P0S3-07-4-00";
user_info: "phone";
line1_name: "1051";
line1_displayname: "";
line1_shortname: "";
line1_authname: "1051";
line1_password: "ww";
line2_name: "";
line2_displayname: "";
line2_shortname: "";
line2_authname: "";
line2_password: "";
auto_answer: "0";
speed_line1: "";
speed_label1: "";
speed_line2: "";
speed_label2: "";
speed_line3: "";
speed_label3: "";
speed_line4: "";
speed_label4: "";
speed_line5: "";
speed_label5: "";
call_hold_ringback: "0";
dnd_control: "0";
anonymous_call_block: "0";
callerid_blocking: "0";
enable_vad: "0";
semi_attended_transfer: "1";
call_waiting: "1";
cfwd_url: "";
cnf_join_enable: "1";
phone_label: "";
preferred_codec: "g711ulaw";
```

## Where To Go
                        	 Next

After you generate a
                           		configuration file for a Cisco Unified IP phone connected to the Cisco Unified
                           		CME router, you are ready to download the file to the phone. See Reset and Restart Phones .

| Restriction | Externally
                                                   				  stored and per-phone configuration files are not supported on the
                                                   				  Cisco Unified IP Phone 7902G, 7910, 7910G, or 7920, or the Cisco Unified IP
                                                   				  Conference Station 7935 and 7936. TFTP does
                                                   				  not support file deletion. When configuration files are updated, they overwrite
                                                   				  any existing configuration files with the same name. If you change the
                                                   				  configuration file location, files are not deleted from the TFTP server. Generating
                                                   				  configuration files on flash or slot 0 can take up to a minute, depending on
                                                   				  the number of files being generated. F or smaller
                                                   				  routers such as Cisco 2600 series routers, you must manually enter the squeeze command to erase files after changing the configuration file location or
                                                   				  entering any commands that trigger the deletion of configuration files. Unless
                                                   				  you use the squeeze command, the space used by the moved or deleted configuration files is not
                                                   				  usable by other files. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | create cnf-files Example: Router(config-telephony)# create cnf-files | Builds the XML
                                             				configuration files required for IP phones. |
| Step 5 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Step 1 | show telephony-service all Use this command to verify the configuration for phones, directory
                                             				numbers, voice ports, and dial peers in Cisco Unified CME. Example: Router# show telephony-service all CONFIG (Version=4.0(0)) 
			 =====================
			 Version 4.0(0) 
			 Cisco Unified CallManager Express 
			 For on-line documentation please see:
			 www.cisco.com/en/US/products/sw/voicesw/ps4625/tsd_products_support_series_home.html
			 
			 ip source-address 10.0.0.1 port 2000
			 max-ephones 24
			 max-dn 24
			 dialplan-pattern 1 408734....
			 voicemail 11111
			 transfer-pattern 510734....
			 keepalive 30
			 
			 ephone-dn 1
			 number 5001
			 huntstop
			 
			 ephone-dn 2
			 number 5002
			 huntstop
			 call-forward noan 5001 timeout 8 |
|---|---|
| Step 2 | show telephony-service tftp-bindings Use this command to display the current configuration files
                                             				accessible to IP phones. Example: Router# show telephony-service tftp-bindings tftp-server system:/its/SEPDEFAULT.cnf 
			tftp-server system:/its/SEPDEFAULT.cnf alias SEPDefault.cnf
			tftp-server system:/its/XMLDefault.cnf.xml alias XMLDefault.cnf.xml
			tftp-server system:/its/ATADefault.cnf.xml
			tftp-server system:/its/XMLDefault7960.cnf.xml alias SEP00036B54BB15.cnf.xml
			tftp-server system:/its/germany/7960-font.xml alias German_Germany/7960-font.xml 
			tftp-server system:/its/germany/7960-dictionary.xml alias German_Germany/7960-dictionary.xml
			tftp-server system:/its/germany/7960-kate.xml alias German_Germany/7960-kate.xml
			tftp-server system:/its/germany/SCCP-dictionary.xml alias German_Germany/SCCP-dictionary.xml
			tftp-server system:/its/germany/7960-tones.xml alias Germany/7960-tones.xml |

| Caution | If your
                                             			 Cisco Unified CME system supports SCCP and also SIP phones, do not connect your
                                             			 SIP phones to the network until after you have verified the phone configuration
                                             			 profiles. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. |
| Step 4 | file text Example: Router(config-register-global)# file text | (Optional)
                                             				Generates ASCII text files of the configuration profiles generated for
                                             				Cisco Unified IP Phone 7905s and 7905Gs, Cisco Unified IP Phone 7912s and
                                             				7912Gs, Cisco ATA-186, or Cisco ATA-188. Default—System generates binary files to save disk space. |
| Step 5 | create profile Example: Router(config-register-global;)# create profile | Generates
                                             				configuration profile files required for SIP phones and writes the files to the
                                             				location specified with tftp-path command. |
| Step 6 | end Example: Router(config-register-global)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Step 1 | show voice register tftp-bind Use this
                                             				command to display a list of configuration profiles that are accessible to SIP
                                             				phones using TFTP. The file name includes the MAC address for each SIP phone,
                                             				such as SIP <mac-address>.cnf. Verify that a configuration profile is
                                             				available for each SIP phone in Cisco Unified CME. The following
                                             				is sample output from this command: Example: Router(config)# show voice register tftp-bind tftp-server SIPDefault.cnf url system:/cme/sipphone/SIPDefault.cnf> 
tftp-server syncinfo.xml url system:/cme/sipphone/syncinfo.xml 
tftp-server SIP0009B7F7532E.cnf url system:/cme/sipphone/SIP0009B7F7532E.cnf 
tftp-server SIP000ED7DF7932.cnf url system:/cme/sipphone/SIP000ED7DF7932.cnf 
tftp-server SIP0012D9EDE0AA.cnf url system:/cme/sipphone/SIP0012D9EDE0AA.cnf 
tftp-server gk123456789012 url system:/cme/sipphone/gk123456789012 
tftp-server gk123456789012.txt url system:/cme/sipphone/gk123456789012.txt |
|---|---|
| Step 2 | show voice register profile Use this
                                             				command to display the contents of the ASCII format configuration profile for a
                                             				particular voice register pool. Note To generate
                                                         				  ASCII text files of the configuration profiles for Cisco Unified IP Phone 7905s
                                                         				  and 7905Gs, Cisco Unified IP Phone 7912s and 7912Gs, Cisco ATA-186s, and Cisco
                                                         				  ATA-188s, use the file text command. Example: The following
                                             				is sample output from this command displaying information in the configuration
                                             				profile for voice register pool 4. Router# show voice register profile text 4 Pool Tag: 4
# txt
AutoLookUp:0
DirectoriesUrl:0
…
CallWaiting:1
CallForwardNumber:0
Conference:1
AttendedTransfer:1
BlindTransfer:1
…
SIPRegOn:1
UseTftp:1
UseLoginID:0
UIPassword:0
NTPIP:0.0.0.0
UID:2468 | Note | To generate
                                                         				  ASCII text files of the configuration profiles for Cisco Unified IP Phone 7905s
                                                         				  and 7905Gs, Cisco Unified IP Phone 7912s and 7912Gs, Cisco ATA-186s, and Cisco
                                                         				  ATA-188s, use the file text command. |
| Note | To generate
                                                         				  ASCII text files of the configuration profiles for Cisco Unified IP Phone 7905s
                                                         				  and 7905Gs, Cisco Unified IP Phone 7912s and 7912Gs, Cisco ATA-186s, and Cisco
                                                         				  ATA-188s, use the file text command. |
| Step 3 | more system Use this
                                             				command to display the contents of the configuration profile for a particular
                                             				Cisco Unified IP Phone 7940, Cisco Unified IP Phone 7905G, Cisco Unified IP
                                             				Phone 7960, or Cisco Unified IP Phone 7960G. The following
                                             				is sample output from this command displaying information in two SIP
                                             				configuration profile files. The SIPDefault.cnf configuration profile is a
                                             				shared file and SIP < MAC address > .cnf is the SIP configuration profile
                                             				for the SIP phone with the designated MAC address. Router# more system:/cme/sipphone/SIPDefault.cnf image_version: "P0S3-07-4-00";
proxy1_address: "10.1.18.100";
proxy2_address: "";
proxy3_address: "";
proxy4_address: "";
proxy5_address: "";
proxy6_address: "";
proxy1_port: "5060";
proxy2_port: "";
proxy3_port: "";
proxy4_port: "";
proxy5_port: "";
proxy6_port: "";
proxy_register: "1";
time_zone: "EST";
dst_auto_adjust: "1";
dst_start_month: "April";
dst_start_day: "";
dst_start_day_of_week: "Sun";
dst_start_week_of_month: "1";
dst_start_time: "02:00";
dst_stop_month: "October";
dst_stop_day: "";
dst_stop_day_of_week: "Sun";
dst_stop_week_of_month: "8";
dst_stop_time: "02:00";
date_format: "M/D/Y";
time_format_24hr: "0";
local_cfwd_enable: "1";
directory_url: "";
messages_uri: "2000";
services_url: "";
logo_url: "";
stutter_msg_waiting: "0";
sync: "0000200155330856";
telnet_level: "1";
autocomplete: "1";
call_stats: "0";
Domain_Name: "";
dtmf_avt_payload: "101";
dtmf_db_level: "3";
dtmf_inband: "1";
dtmf_outofband: "avt";
dyn_dns_addr_1: "";
dyn_dns_addr_2: "";
dyn_tftp_addr: "";
end_media_port: "32766";
http_proxy_addr: "";
http_proxy_port: "80";
nat_address: "";
nat_enable: "0";
nat_received_processing: "0";
network_media_type: "Auto";
network_port2_type: "Hub/Switch";
outbound_proxy: "";
outbound_proxy_port: "5060";
proxy_backup: "";
proxy_backup_port: "5060";
proxy_emergency: "";
proxy_emergency_port: "5060";
remote_party_id: "0";
sip_invite_retx: "6";
sip_retx: "10";
sntp_mode: "directedbroadcast";
sntp_server: "0.0.0.0";
start_media_port: "16384";
tftp_cfg_dir: "";
timer_invite_expires: "180";
timer_register_delta: "5";
timer_register_expires: "3600";
timer_t1: "500";
timer_t2: "4000";
tos_media: "5";
voip_control_port: "5060";

Router# more system:/cme/sipphone/SIP000CCE62BCED.cnf image_version: "P0S3-07-4-00";
user_info: "phone";
line1_name: "1051";
line1_displayname: "";
line1_shortname: "";
line1_authname: "1051";
line1_password: "ww";
line2_name: "";
line2_displayname: "";
line2_shortname: "";
line2_authname: "";
line2_password: "";
auto_answer: "0";
speed_line1: "";
speed_label1: "";
speed_line2: "";
speed_label2: "";
speed_line3: "";
speed_label3: "";
speed_line4: "";
speed_label4: "";
speed_line5: "";
speed_label5: "";
call_hold_ringback: "0";
dnd_control: "0";
anonymous_call_block: "0";
callerid_blocking: "0";
enable_vad: "0";
semi_attended_transfer: "1";
call_waiting: "1";
cfwd_url: "";
cnf_join_enable: "1";
phone_label: "";
preferred_codec: "g711ulaw"; |

| Note | To generate
                                                         				  ASCII text files of the configuration profiles for Cisco Unified IP Phone 7905s
                                                         				  and 7905Gs, Cisco Unified IP Phone 7912s and 7912Gs, Cisco ATA-186s, and Cisco
                                                         				  ATA-188s, use the file text command. |
|---|---|