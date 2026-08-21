---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmelocal-html-ff13de3239
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmelocal.html
retrieved_at: 2026-08-21T07:22:39.656064+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Localization Support

## Chapter: Localization Support

# Localization Support

This chapter describes the localization support in Cisco Unified
                        		Communications Manager Express (Cisco Unified CME) for languages other than
                        		English and network tones and cadences not specific to the United States.

## Information About Localization

### Localization
                           	 Enhancements in Cisco Unified CME

Cisco Unified CME
                              		supports the French locale but some phrases in France French and Canadian
                              		French differ. In Cisco Unified CME 9.5, Canadian French is supported as a
                              		user-defined locale on Cisco Unified SIP IP phones and Cisco Unified SCCP IP
                              		phones when the correct locale package is installed.

Prerequisites

Cisco Unified
                                    			 CME 9.5 or later version

Locale package
                                    			 version 9.5.2.6 is required

Restriction

All the localization enhancements are supported in Cisco Unified CME only. They are not supported in Cisco Unified SRST. Table 1 shows the language codes used in the filenames of locale files.

Language

Language Code

Canadian French

fr_CA

For configuration information, see Install User-Defined Locales .

### System-Defined
                           	 Locales

Cisco Unified CME
                              		provides built-in, system-defined localization support for 12 languages
                              		including English and 16 countries including the United States. Network locales
                              		specify country-specific tones and cadences; user locales specify the language
                              		to use for text displays.

Configuring
                              		system-defined locales depends on the type of IP phone:

Cisco Unified IP
                                    			 Phone 7905, 7912, 7940, and 7960—System-defined network locales and user
                                    			 locales are preloaded into Cisco IOS software. No external files are required.
                                    			 Use the network-locale and user-locale commands to set the locales for these phones.

Cisco Unified IP
                                    			 Phone 6921, 6945, 7906, 7911, 7921, 7931, 7941, 7961, 7970, 7971, 8941, 8945,
                                    			 and Cisco IP Communicator—You must download locale files to support the
                                    			 system-defined locales and store the files in flash memory, slot 0, or on an
                                    			 external TFTP server. See Install System-Defined Locales for Cisco Unified IP Phone 6921, 6945, 7906, 7911, 7921, 7931, 7941, 7961, 7970, 7971, and
                                       Cisco IP Communicator .

Cisco Unified 3905, 6941, 6945, 8961, 9951, and 9971 SIP IP
                                    			 Phones—You must download locale files to support the system-defined locales and
                                    			 store the files in flash memory, slot 0, or on an external TFTP server.

TFTP aliases for
                                          		  localization are not automatically created for Cisco Unified SIP IP phones in a
                                          		  Cisco Unified CME system. For more information on how to manually create TFTP
                                          		  aliases, see Install System-Defined Locales for Cisco Unified IP Phone 8961, 9951, and 9971 .

Cisco Unified CME
                                          		  10.5 Release onwards, the System defined locales are deprecated and
                                          		  User-defined locales are recommended.

Cisco Unified 3905
                              		SIP IP Phones and Cisco Unified 6945, 8941, and 8945 SCCP IP Phones have
                              		support for all locales up to Cisco Unified CME 8.8.

### Localization
                           	 Support for Cisco Unified SIP IP Phones

Cisco Unified CME
                              		8.6 provides localization support for 12 languages including English and
                              		16 countries including the United States. Network locales specify
                              		country-specific tones and cadences; user locales specify the language to use
                              		for text displays. Create additional localization support with user-defined
                              		locales. For more information about user-defined locales, see User-Defined Locales .

In Cisco Unified CME
                              		9.0 and later versions, localization is enhanced to support Cisco Unified 6941
                              		and 6945 SIP IP Phones.

The load command
                              		supports both user-defined and system-defined locales.

The locale files
                                          		  must be stored in the same location as the configuration files.

### User-Defined
                           	 Locales

The user-defined
                              		locale feature allows you to support network and user locales other than the
                              		system-defined locales that are predefined in Cisco IOS software. For example,
                              		if your site has phones that must use the language and tones for Traditional
                              		Chinese, which is not one of the system-defined choices, you must install the
                              		locale files for Traditional Chinese.

In Cisco Unified CME
                              		4.0 and later versions, you can download files to support a particular user and
                              		network locale and store the files in flash memory, slot 0, or an external TFTP
                              		server. These files cannot be stored in the system location. User-defined
                              		locales can be assigned to all phones or to individual phones.

User-defined
                              		language codes for user locales are based on ISO 639 codes, which are available
                              		at the Library of Congress website at http://www.loc.gov/standards/iso639-2/ .
                              		User-defined country codes for network locales are based on ISO 3166 codes.

For configuration
                              		information, see Install User-Defined Locales .

### Localization Support for Phone Displays

On the Cisco Unified IP Phone 8961, 9951, and 9971, menus and prompts
                              		that are managed by the locale file for the IP phone type (.jar) or the
                              		Cisco Unified CME dictionary file are localized. Display options configured
                              		through Cisco IOS commands are not localized.

The following display items are localized by the IP phone (.jar file):

System menus accessed with feature buttons (for example, messages,
                                    			 directories, services, settings, and information)

Call processing messages

Softkeys (for example, Redial and CFwdALL)

The following display items are localized by the dictionary file for
                              		Cisco Unified CME:

Directory Service (Local Directory, Local Speed Dial, and Personal
                                    			 Speed Dial)

Status Line

Display options configured through Cisco IOS commands are not localized
                              		and can only be displayed in English. For example, this includes features such
                              		as:

Caller ID

Header Bar

Phone Labels

System Message

### Multiple
                           	 Locales

In Cisco Unified CME
                              		8.6 and later versions, you can specify up to five user and network locales and
                              		apply different locales to individual ephones or groups of ephones using ephone
                              		templates. For example, you can specify French for phones A, B, and C; German
                              		for phones D, E, and F; and English for phones G, H, and I. Only one user and
                              		network locale can be applied to each phone.

Each of the five
                              		user and network locales that you can define in a multilocale system is
                              		identified by a locale tag. The locale identified by tag 0 is always the
                              		default locale, although you can define this default to be any supported
                              		locale. For example, if you define user locale 0 to be JP (Japanese), the
                              		default user locale for all phones is JP. If you do not specify a locale for
                              		tag 0, the default is US (United States).

To apply alternative
                              		locales to different phones, you must use per-phone configuration files to
                              		build individual configuration files for each phone. The configuration files
                              		automatically use the default user-locale 0 and network-locale 0. You can
                              		override these defaults for individual phones by configuring alternative locale
                              		codes and then creating ephone-templates to assign the locales to individual
                              		ephones.

For configuration
                              		information, see Configure Multiple Locales on SCCP Phones .

### Locale Installer
                           	 for Cisco Unified SCCP IP Phones

Locale installer
                                       			 that supports a single procedure for all SCCP IP phones.

Cisco Unified CME parses new firmware-load text files and
                                       			 automatically creates the TFTP aliases for localization, eliminating the
                                       			 requirement for you to manually create up to five aliases for files in the TAR
                                       			 file. To use this feature in Cisco Unified CME 7.0(1), you must use the
                                       			 complete filename, including the file suffix, when you configure the load command
                                       			 for phone firmware versions later than version 8-2-2 for all phone types. For
                                       			 example:

```
Router(config-telephony)# load 7941 SCCP41.8-3-3S.loads
```

In
                                             		  Cisco Unified CME 4.3 and earlier versions, you do not include the file suffix
                                             		  for any phone type except Cisco ATA and Cisco Unified IP Phone 7905 and 7912.
                                             		  For example:

```
Router(config-telephony)# load 7941 SCCP41.8-2-2SR2S
```

Backward
                                       			 compatibility with the configuration method in Cisco Unified CME 7.0 and
                                       			 earlier versions.

For configuration
                              		information, see Use the Locale Installer in Cisco Unified CME 7.0(1) and Later Versions .

### Locale Installer
                           	 for Cisco Unified SIP IP Phones

Cisco Unified CME
                              		9.0 and later versions support the following enhancements for installing
                              		locales for Cisco Unified SIP IP phones:

Locale installer
                                    			 that supports a single procedure for all Cisco Unified SIP IP phones.

New load keyword
                                    			 that requires you to use the complete filename, including the file suffix
                                    			 (.tar), when you configure the user-locale command for all Cisco Unified SIP IP phone types. The command syntax is user-locale [ user-locale-tag ] {[ user-defined-code ] country-code }
                                    			 [ load TAR-filename ]. For example,

```
Router(config-register-global)# user-locale 2 DE load CME-locale-de_DE-German-8.6.3.0.tar
```

With the locale
                              		installer, you do not need to perform manual configuration. Instead, you copy
                              		the locale file using the copy command
                              		in privileged EXEC configuration mode.

You must copy the
                                          		  locale file into the /its directory (flash:/its or slot0:/its) when you store
                                          		  the locale files on the Cisco Unified CME router.

For example,

```
Router# copy tftp://12.1.1.100/CME-locale-de_DE-German-8.6.3.0.tar flash:/its
```

For configuration
                              		information, see Use the Locale Installer in Cisco Unified CME 9.0 and Later Versions .

## Configure Localization Support on SCCP Phones

### Install
                           	 System-Defined Locales for Cisco Unified IP Phone 6921, 6945, 7906, 7911, 7921,
                           	 7931, 7941, 7961, 7970, 7971, and Cisco IP Communicator

Network locale
                                 		  files allow an IP phone to play the proper network tone for the specified
                                 		  country. You must download and install a tone file for the country you want to
                                 		  support.

User locale files
                                 		  allow an IP phone to display the menus and prompts in the specified language.
                                 		  You must download and install JAR files and dictionary files for each language
                                 		  you want to support.

To download and
                                 		  install locale files for system-defined locales, perform the following steps.

Tip

Restriction

Localization
                                                   				  is not supported for SIP phones.

Phone
                                                   				  firmware, configuration files, and locale files must be in the same directory,
                                                   				  except the directory file for Japanese and Russian, which must be in flash
                                                   				  memory.

#### Before you begin

Cisco Unified
                                       				CME 4.0(2) or a later version.

You must
                                       				create per-phone configuration files as described in Define Per-Phone Configuration Files and Alternate Location for SCCP Phones .

You must have
                                       				an account on Cisco.com to download locale files.

Step 1

Go to http://www.cisco.com/cgi-bin/tablebuild.pl/CME-Locale .

You must have
                                             				an account on Cisco.com to access the Software Download Center. If you do not
                                             				have an account or if you have forgotten your username or password, click the
                                             				appropriate button at the login dialog box and follow the instructions that
                                             				appear.

Step 2

Navigate to Downloads
                                                				  Home > Products > Unified
                                                				  Communications > Call Control > Mid-Market Call
                                                				  Control > Cisco Unified Communications Manager Express > Unified Communications Manager Express Individual File
                                                				  Set and select your version of Cisco Unified CME.

Step 3

Select the TAR file for the locale you want to install. Each TAR file contains locale files for a specific language and country
                                          and uses the following naming convention: CME-locale- language _ country - CMEversion

#### Example:

For example, CME-locale-de_DE-4.0.2-2.0 is German for Germany for Cisco Unified CME 4.0(2).

Step 4

Download the
                                          			 TAR file to a TFTP server that is accessible to the Cisco Unified CME router.
                                          			 Each file contains all the firmware required for all phone types supported by
                                          			 that version of Cisco Unified CME.

Step 5

Use the archive tar command to extract the files to flash memory, slot 0, or an external TFTP server.

#### Example:

```
Router# archive tar /xtract source-url flash: /file-url
```

#### Example:

For example, to extract the contents of CME-locale-de_DE-4.0.2-2.0.tar from TFTP server 192.168.1.1 to router flash memory,
                                             use this command:

```
Router# archive tar /xtract tftp://192.168.1.1/cme-locale-de_DE-4.0.2-2.0.tar flash:
```

Step 6

See Table 1 and Table 2 for a description of the codes used in the filenames and the list of supported
                                          			 directory names.

Each phone type has a JAR file that uses the following naming convention:

language - phone -sccp.jar

#### Example:

For example, de-td-sccp.jar is for German on the Cisco Unified IP Phone 7970.

Each TAR file also includes the file g3-tones.xml for country-specific network tones and cadences.

Phone Type

Phone Code

6921

rtl

6945

rtl

7906/7911

tc

7931

gp

7941/7961

mk

7970/7971

td

8941/8945

gh

CIPC

ipc

Language

Language Code

User-Locale

Directory Name

Country Code

Network-Locale

Directory Name

English

en

English_United_States 1

US

United_States

UK

United_Kingdom

CA

Canada

Danish

dk

Danish_Denmark

DK

Denmark

Dutch

nl

Dutch_Netherlands

NL

Netherlands

French

fr

French_France

FR

France

CA

Canada

German

de

German_Germany

DE

Germany

AT

Austria

CH

Switzerland

Italian

it

Italian_Italy

IT

Italy

Japanese 2

jp

Japanese_Japan

JP

Japan

Norwegian

no

Norwegian_Norway

NO

Norway

Portuguese

pt

Portuguese_Portugal

PT

Portugal

Russian

ru

Russian_Russia

RU

Russian_Federation

Spanish

es

Spanish_Spain

ES

Spain

Swedish

se

Swedish_Sweden

SE

Sweden

Step 7

If you store
                                          			 the locale files in flash memory or slot 0 on the Cisco Unified CME router,
                                          			 create a TFTP alias for the user locale (text displays) and network locale
                                          			 (tones) using this format:

#### Example:

```
Router(config)# tftp-server flash:/ jar_file alias directory_name /td-sccp.jar
```

```
Router(config)# tftp-server flash:/g3-tones.xml alias directory_name /g3-tones.xml
```

Use the
                                             				appropriate directory name shown in Table 2 and remove the two-letter language code from the JAR file name. For example,
                                             				the TFTP aliases for German and Germany for the Cisco Unified IP Phone 7970
                                             				are:

```
Router(config)# tftp-server flash:/de-td-sccp.jar alias German_Germany/td-sccp.jar
```

```
Router(config)# tftp-server flash:/g3-tones.xml alias Germany/g3-tones.xml
```

Step 8

If you store
                                          			 the locale files on an external TFTP server, create a directory under the TFTP
                                          			 root directory for each user and network locale.

Use the
                                             				appropriate directory name shown in Table 2 and remove the two-letter language code from the JAR file name.

#### Example:

For example,
                                             				the user-locale directory for German and the network-locale directory for
                                             				Germany for the Cisco Unified IP Phone 7970 are:

TFTP-Root/German_Germany/td-sccp.jar
                                             				TFTP-Root/Germany/g3-tones.xml

Step 9

For Russian
                                          			 and Japanese, you must copy the UTF8 dictionary file into flash memory to use
                                          			 special phrases.

Only
                                                   					 flash memory can be used for these locales. Copy russian_tags_utf8_phrases for
                                                   					 Russian; Japanese_tags_utf8_phrases for Japanese.

Use the user-locale
                                                         						  jp and user-locale
                                                         						  ru command to load the UTF8 phrases into Cisco Unified CME.

Step 10

Assign the
                                          			 locales to phones. To set a default locale for all phones, use the user-locale and network-locale commands in telephony-service
                                          			 configuration mode.

Step 11

To support
                                          			 more than one user or network locale, see Configure Multiple Locales on SCCP Phones .

Step 12

Use the create
                                                				  cnf-files command to rebuild the configuration files.

Step 13

Use the reset command to reset the phones and see the localized displays.

### Install
                           	 User-Defined Locales

You must download
                                 		  XML files for locales that are not predefined in the system. To install up to
                                 		  five user-defined locale files to use with phones, perform the following steps.

Restriction

User-defined
                                                   				  locales are not supported on the Cisco Unified IP Phone 7920 or 7936.

User-defined
                                                   				  locales are not supported if the configuration file location is “system:”.

When you use
                                                   				  the setup tool from the telephony-service
                                                         						setup command to provision phones, you can only choose a default
                                                   				  user locale and network locale and you are limited to selecting a locale code
                                                   				  that is supported in the system. You cannot use multiple locales or
                                                   				  user-defined locales with the setup tool.

When using a
                                                   				  user-defined locale, the phone normally displays text using the user-defined
                                                   				  fonts, except for any strings that are interpreted by Cisco Unified CME, such
                                                   				  as “Cisco/Personal Directory,” “Speed Dial/Fast Dial,” and so forth.

#### Before you begin

Cisco Unified
                                       				CME 4.0(3) or a later version.

You must
                                       				create per-phone configuration files as described in Define Per-Phone Configuration Files and Alternate Location for SCCP Phones .

You must have
                                       				an account on Cisco.com to download locale files.

Step 1

Go to http://www.cisco.com/cgi-bin/tablebuild.pl/CME-Locale .

You must have
                                             				an account on Cisco.com to access the Software Download Center. If you do not
                                             				have an account or if you have forgotten your username or password, click the
                                             				appropriate button at the login dialog box and follow the instructions that
                                             				appear.

Step 2

Navigate to Downloads
                                                				  Home > Products > Unified
                                                				  Communications > Call Control > Mid-Market Call
                                                				  Control > Cisco Unified Communications Manager
                                                				  Express > Unified Communications Manager Express Individual File Set and select your version of Cisco Unified
                                          			 CME.

Step 3

Select the TAR
                                          			 file for the locale that you want to install. Each TAR file contains locale
                                          			 files for a specific language and country and uses the following naming
                                          			 convention: CME-locale- language _ country - CMEversion - fileversion .

#### Example:

For example,
                                             				CME-locale-zh_CN-4.0.3-2.0 is Traditional Chinese for China for
                                             				Cisco Unified CME 4.0(3).

Step 4

Download the
                                          			 TAR file to a TFTP server that is accessible to the Cisco Unified CME router.
                                          			 Each file contains all the firmware required for all phone types supported by
                                          			 that version of Cisco Unified CME.

Step 5

Use the archive tar command to extract the files to slot 0, flash memory, or an external TFTP
                                          			 server.

#### Example:

```
Router# archive tar /xtract source-url flash: /file-url
```

For example,
                                             				to extract the contents of CME-locale-zh_CN-4.0.3-2.0.tar from TFTP server
                                             				192.168.1.1 to router flash memory, use this command:

```
Router# archive tar /xtract tftp://192.168.1.1/cme-locale-zh_CN-4.0.3-2.0.tar flash:
```

Step 6

For Cisco
                                          			 Unified IP Phone 7905, 7912, 7940, or 7960, go to Step 11 .
                                          			 For Cisco Unified IP Phone 7911, 7941, 7961, 7970, or 7971, go to Step 7 .

Step 7

Each phone
                                          			 type has a JAR file that uses the following naming convention: language - type -sccp.jar

#### Example:

For example,
                                             				zh-td-sccp.jar is Traditional Chinese for the Cisco Unified IP Phone 7970.

See Table 1 and Table 2 for a description of the codes used in the filenames.

Phone
                                                         						  Type

Code

6921

rtl

6945

rtl

7906/7911

tc

7931

gp

7941/7961

mk

7970/7971

td

8941/8945

gh

CIPC

ipc

Language

Language Code

Bulgarian

bg

Chinese

zh 3

Croation

hr

Czech Republic

cs

Finnish

fi

Greek

el

Hungarian

hu

Korean

ko

Polish

pl

Portugese (Brazil)

pt

Romanian

ro

Serbian

sr

Slovakian

sk

Slovenian

sl

Turkish

tr

Step 8

If you store
                                          			 the locale files in flash memory or slot 0 on the Cisco Unified CME router,
                                          			 create a TFTP alias using this format:

#### Example:

```
Router(config)# tftp-server flash:/ jar_file alias directory_name /td-sccp.jar
```

Remove the
                                             				two-letter language code from the JAR filename and use one of five supported
                                             				directory names with the following convention:

user_define_ number ,
                                             				where number is 1
                                             				to 5

For example,
                                             				the alias for Chinese on the Cisco Unified IP Phone 7970 is:

```
Router(config)# tftp-server flash:/zh-td-sccp.jar alias user_define_1/td-sccp.jar
```

On Cisco
                                                         				  3800 series routers, you must include /its in the directory name (flash:/its or
                                                         				  slot0:/its). For example, the TFTP alias for Chinese for the Cisco Unified IP
                                                         				  Phone 7970 is:

```
Router(config)# tftp-server flash:/its/zh-td-sccp.jar alias user_define_1/td-sccp.jar
```

Step 9

If you store
                                          			 the locale files on an external TFTP server, create a directory under the TFTP
                                          			 root directory for each locale.

Remove the
                                             				two-letter language code from the JAR filename and use one of five supported
                                             				directory names with the following convention:

user_define_ number ,
                                             				where number is 1
                                             				to 5

#### Example:

For example,
                                             				for Chinese on the Cisco Unified IP Phone 7970, remove “zh” from the JAR
                                             				filename and create the “user_define_1” directory under TFTP-Root on the TFTP
                                             				server:

TFTP-Root/user_define_1/td-sccp.jar

Step 10

Go to Step 13 .

Step 11

Download one
                                          			 or more of the following XML files depending on your selected locale and phone
                                          			 type. All required files are included in the JAR file.

#### Example:

```
7905-dictionary.xml 
			 7905-font.xml  
			 7905-kate.xml  
			 7920-dictionary.xml 
			 7960-dictionary.xml 
			 7960-font.xml 
			 7960-kate.xml  
			 7960-tones.xml 
			 SCCP-dictionary.utf-8.xml 
			 SCCP-dictionary.xml
```

Step 12

Rename these
                                          			 files and copy them to flash memory, slot 0, or an external TFTP server. Rename
                                          			 the files using the format user_define_ number _ filename where number is 1
                                          			 to 5.

#### Example:

For example,
                                             				use the following names if you are setting up the first user-locale:

```
user_define_1_7905-dictionary.xml  
			 user_define_1_7905-font.xml 
			 user_define_1_7905-kate.xml 
			 user_define_1_7920-dictionary.xml 
			 user_define_1_7960-dictionary.xml 
			 user_define_1_7960-font.xml  
			 user_define_1_7960-kate.xml  
			 user_define_1_7960-tones.xml 
			 user_define_1_SCCP-dictionary.utf-8.xml  
			 user_define_1_SCCP-dictionary.xml
```

Step 13

Copy the language _tags_file and language _utf8_tags_file to the location of the
                                          			 other locale files (flash memory, slot 0, or TFTP server). Rename the files to
                                          			 user_define_ number _tags_file and user_define_ number _utf8_tags_file respectively, where number is 1
                                          			 to 5 and matches the user-defined directory.

Step 14

Assign the
                                          			 locales to phones. See Configure Multiple Locales on SCCP Phones .

Step 15

Use the create
                                                				  cnf-files command to rebuild the configuration files.

Step 16

Use the reset command to reset the phones and see the localized displays.

### Use the Locale
                           	 Installer in Cisco Unified CME 7.0(1) and Later Versions

To install and
                                 		  configure locale files to use with SCCP phones in Cisco Unified CME, perform
                                 		  the following steps.

Tip

Restriction

When using an external TFTP server, you must manually create the user locale folders in the root directory. This is a limitation
                                                   of the TFTP server.

Locale support is limited to phone firmware versions that are supported by Cisco Unified CME.

User-defined locales are not supported on the Cisco Unified IP Phone 7920 or 7936.

User-defined locales are not supported if the configuration file location is system.

When you use the setup tool from the telephony-service setup command to provision phones, you can only choose a default user locale and network locale, and you are limited to selecting
                                                   a locale code that is supported in the system. You cannot use multiple locales or user-defined locales with the setup tool.

When using a user-defined locale, the phone normally displays text using the user-defined fonts, except for any strings that
                                                   are interpreted by Cisco Unified CME, such as “Cisco/Personal Directory,” and “Speed Dial/Fast Dial.”

If you install and configure a user-defined locale using country codes U1-U5 and then you install a new locale using the same
                                                   label, the phone retains the original language locale even after the phone is reset. This is a limitation of the IP phone.
                                                   To work around this limitation, you must configure the new package using a different country code.

Each user-defined country code (U1-U5) can be used for only one user-locale-tag at a time. For example:

```
Router(config-telephony)# user-locale 2 U2 load Finnish.pkg Router(config-telephony)# user-locale 1 U2 load Chinese.pkg LOCALE ERROR: User Defined Locale U2 already exists on locale index 2.
```

#### Before you begin

Cisco Unified CME 7.0(1) or a later version.

You must
                                       				configure Cisco Unified CME for per-phone configuration files. See Define Per-Phone Configuration Files and Alternate Location for SCCP Phones .

When the
                                       				storage location specified by the cnf-file
                                             					 location command is flash memory, sufficient space must be on the
                                       				flash file system for extracting the contents of the locale TAR file.

You must have
                                       				an account on Cisco.com to download locale files.

Step 1

Go to http://www.cisco.com/cgi-bin/tablebuild.pl/CME-Locale .

You must have
                                             				an account on Cisco.com to access the Software Download Center. If you do not
                                             				have an account or have forgotten your username or password, click the
                                             				appropriate button at the login dialog box and follow the instructions that
                                             				appear.

Step 2

Navigate to Downloads
                                                				  Home > Products > Unified
                                                				  Communications > Call Control > Mid-Market Call Control > Cisco Unified
                                                				  Communications Manager Express > Unified Communications
                                                				  Manager Express Individual File Set and select your
                                          			 version of Cisco Unified CME.

Step 3

Select the TAR
                                          			 file for the locale you want to install. Each TAR file contains locale files
                                          			 for a specific language and country and uses the following naming convention:
                                          			 CME-locale- language _ country - CMEversion

#### Example:

For example,
                                             				CME-locale-de_DE-7.0.1.0 is German for Germany for Cisco Unified CME 7.0(1).

Step 4

Download the
                                          			 TAR file to the location previously specified by the cnf-file location command. Each file contains all the firmware required
                                          			 for all phone types supported by that version of Cisco Unified CME.

If the
                                                				  cnf-file location is flash memory: Copy the TAR file to the flash:/its
                                                				  directory.

If the
                                                				  cnf-file location is slot0: Copy the TAR file to the slot0:/its directory.

If the cnf-file location is tftp: Create a folder in the root directory of the TFTP server for each locale using the following
                                                format and then copy the TAR file to the TFTP-Root folder. TFTP-Root / TAR-filename

#### Example:

For system-defined locales, use the locale folder name as shown in Table 1 . For example, create the folder for system-defined German as follows:

```
TFTP-Root/de_DE-7.0.1.0.tar
```

For up to five user-defined locales, use the User_Define_ n folder name as shown in Table 1 . A user-defined locale is a language other than the system-defined locales that are predefined in Cisco IOS software. For
                                                   example, create the folder for user-defined locale Chinese (User_Define_1) as follows:

```
TFTP-Root/CME-locale-zh_CN-7.0.1.0.tar
```

Language

Locale Folder Name

Country Code

English

English_United_States

US

English_United_Kingdom

UK

CA

Danish

Danish_Denmark

DK

Dutch

Dutch_Netherlands

NL

French

French_France

FR

CA

German

German_Germany

DE

AT

CH

Italian

Italian_Italy

IT

Japanese 4

Japanese_Japan

JP

Norwegian

Norwegian_Norway

NO

Portuguese

Portuguese_Portugal

PT

Russian

Russian_Russia

RU

Spanish

Spanish_Spain

ES

Swedish

Swedish_Sweden

SE

Un 5

User_Define_n 2

Un 2

Step 5

Use the user-locale [ user-locale-tag ] country-code load TAR-filename command in telephony-service
                                          			 configuration mode to extract the contents of the TAR file. For country codes,
                                          			 see Table 1 .

#### Example:

For example,
                                             				to extract the contents of the CME-locale-zh_CN-7.0.1.0.tar file when U1 is the
                                             				country code for user-defined locale Chinese (User_Define_1), use this command:

```
Router (telephony-service)# user-locale U1 load CME-locale-zh_CN-7.0.1.0.tar
```

Step 6

Assign the
                                          			 locales to phones. See Configure Multiple Locales on SCCP Phones .

Step 7

Use the create cnf-files command to rebuild the configuration files.

Step 8

Use the reset command to reset the phones and see the localized displays.

### Verify
                           	 User-Defined Locales

See Verify Multiple Locales on SCCP Phones .

### Configure Multiple
                           	 Locales on SCCP Phones

To define one or
                                 		  more alternatives to the default user and network locales and apply them to
                                 		  individual phones, perform the following steps.

Restriction

Multiple
                                                   				  user and network locales are not supported on the Cisco Unified IP Phone 7902G,
                                                   				  7910, 7910G, or 7920, or the Cisco Unified IP Conference Stations 7935
                                                   				  and 7936.

When you use
                                                   				  the setup tool from the telephony-service
                                                         						setup command to provision phones, you can only choose a default
                                                   				  user locale and network locale and you must select a locale code that is
                                                   				  predefined in the system. You cannot use multiple or user-defined locales with
                                                   				  the setup tool.

#### Before you begin

Cisco Unified
                                       				CME 4.0 or a later version.

To specify
                                       				alternative user and network locales for individual phones in a
                                       				Cisco Unified CME system, you must use per-phone configuration files. For more
                                       				information, see Define Per-Phone Configuration Files and Alternate Location for SCCP Phones .

You can also
                                       				use user-defined locale codes as alternative locales after you download the
                                       				appropriate XML files. See Install User-Defined Locales .

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- user-locale [ user-locale-tag ] { [ user-defined-code ] country-code }

- network-locale network-locale-tag [ user-defined-code ] country-code

- create
                                       				  cnf-files

- exit

- ephone-template template-tag

- user-locale user-locale-tag

- network-locale network-locale-tag

- exit

- ephone phone-tag

- ephone-template template-tag

- exit

- telephony-service

- reset { all [ time-interval ] | cancel | mac-address mac-address | sequence-all }

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

user-locale [ user-locale-tag ] { [ user-defined-code ] country-code }

#### Example:

```
Router(config-telephony)# user-locale 1 U1 ZH
```

Specifies a
                                             				language for phone displays.

user-locale-tag —Assigns a locale identifier to the
                                                   					 locale. Range is 0 to 4. Default: 0. This argument is required when defining
                                                   					 some locale other than the default (0).

user-defined-code —(Optional) Assigns one of the
                                                   					 user-defined codes to the specified country code. Valid codes are U1 , U2 , U3 , U4 , and U5 .

country-code —Type ? to display
                                                   					 a list of system-defined codes. Default: US (United States). You can assign any
                                                   					 valid ISO 639 code to a user-defined code (U1 to U5).

Step 5

network-locale network-locale-tag [ user-defined-code ] country-code

#### Example:

```
Router(config-telephony)# network-locale 1 FR
```

Specifies a
                                             				country for tones and cadences.

network-locale-tag —Assigns a locale identifier to
                                                   					 the country code. Range is 0 to 4. Default: 0. This argument is required when
                                                   					 defining some locale other than the default (0).

user-defined-code —(Optional) Assigns one of the
                                                   					 user-defined codes to the specified country code. Valid codes are U1 , U2 , U3 , U4 , and U5 .

country-code —Type ? to
                                                   					 display a list of system-defined codes. Default: US (United States). You can
                                                   					 assign any valid ISO 3166 code to a user-defined code (U1 to U5).

Step 6

create
                                                				  cnf-files

#### Example:

```
Router(config-telephony)# create cnf-files
```

Builds the
                                             				required XML configuration files for IP phones. Use this command after you
                                             				update configuration file parameters such as the user locale or network locale.

Step 7

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits
                                             				telephony-service configuration mode.

Step 8

ephone-template template-tag

#### Example:

```
Router(config)# ephone template 1
```

Enters
                                             				ephone-template configuration mode.

template-tag —Unique sequence number that
                                                   					 identifies this template during configuration tasks.

Step 9

user-locale user-locale-tag

#### Example:

```
Router(config-ephone-template)# user-locale 2
```

Assigns a
                                             				user locale to this ephone template.

user-locale-tag —A locale tag that was created in Step 4 .
                                                   					 Range is 0 to 4.

Step 10

network-locale network-locale-tag

#### Example:

```
Router(config-ephone-template)# network-locale 2
```

Assigns a
                                             				network locale to this ephone template.

network-locale-tag —A locale tag that was created
                                                   					 in Step 5 .
                                                   					 Range is 0 to 4.

Step 11

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 12

ephone phone-tag

#### Example:

```
Router(config)# ephone 36
```

Enters
                                             				ephone configuration mode.

phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks.

Step 13

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 1
```

Applies an
                                             				ephone template to an ephone.

template-tag —Number of the template to apply to
                                                   					 this ephone.

Step 14

exit

#### Example:

```
Router(config-ephone)# exit
```

Exits ephone
                                             				configuration mode.

Step 15

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 16

reset { all [ time-interval ] | cancel | mac-address mac-address | sequence-all }

#### Example:

```
Router(config-telephony)# reset all
```

Performs a complete reboot of all phones or the specified phone, including contacting the DHCP and TFTP servers for the latest
                                             configuration information.

all —All phones in the Cisco Unified CME system.

time-interval —(Optional) Time interval, in seconds, between each phone reset. Range is 0 to 60. Default is 15.

cancel —Interrupts a sequential reset cycle that was started with a reset sequence-all command.

mac-address mac-address —A specific phone.

sequence-all —Resets all phones in strict one-at-a-time order by waiting for one phone to reregister before starting the reset for the
                                                   next phone.

Step 17

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Multiple Locales on SCCP Phones

Step 1

Use the show telephony-service tftp-bindings command to display a list of configuration files that are accessible to IP
                                          			 phones using TFTP, including the dictionary, language, and tone configuration
                                          			 files.

#### Example:

```
Router(config)# show telephony-service tftp-bindings
```

```
tftp-server system:/its/SEPDEFAULT.cnf
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

Step 2

Ensure that per-phone configuration files are defined with the cnf-file perphone command.

Step 3

Use the show telephony-service ephone-template command to check the user locale and network locale settings in each ephone
                                          			 template.

Step 4

Use the show telephony-service ephone command to
                                          			 check that the correct templates are applied to phones.

Step 5

If the configuration file location is not TFTP, use the debug tftp events command to see which
                                          			 files Cisco Unified CME is looking for and whether the files are found and
                                          			 opened correctly. There are usually three states (“looking for x file,” “opened
                                          			 x file,” and “finished x file”). The file is found when all three states are
                                          			 displayed. For an external TFTP server you can use the logs from the TFTP
                                          			 server.

## Configure Localization Support on SIP Phones

### Install
                           	 System-Defined Locales for Cisco Unified IP Phone 8961, 9951, and 9971

Network locale
                                 		  files allow an IP phone to play the proper network tone for the specified
                                 		  country. You must download and install a tone file for the country you want to
                                 		  support.

User locale files
                                 		  allow an IP phone to display the menus and prompts in the specified language.
                                 		  You must download and install JAR files and dictionary files for each language
                                 		  you want to support.

To download and
                                 		  install locale files for system-defined locales, perform the following steps.

Restriction

#### Before you begin

Cisco Unified
                                       				CME 8.6 or a later version. For Cisco Unified IP Phone 9971, Cisco Unified CME
                                       				8.8 or a later version.

You must have
                                       				an account on Cisco.com to download locale files.

Step 1

Go to http://www.cisco.com/cgi-bin/tablebuild.pl/CME-Locale .

You must have
                                             				an account on Cisco.com to access the Software Download Center. If you do not
                                             				have an account or if you have forgotten your username or password, click the
                                             				appropriate button at the login dialog box and follow the instructions that
                                             				appear.

Step 2

Navigate to Downloads
                                                				  Home > Products > Unified Communications > Call Control > Mid-Market Call
                                                				  Control > Cisco Unified Communications Manager
                                                				  Express > Unified Communications Manager Express Individual File
                                                				  Set and select your version of Cisco Unified CME.

Step 3

Select the TAR
                                          			 file for the locale you want to install. Each TAR file contains locale files
                                          			 for a specific language and country and uses the following naming convention:
                                          			 CME-locale- language _ country - CMEversion

#### Example:

For example,
                                             				CME-locale-de_DE-8.6 is German for Germany for Cisco Unified CME 8.6.

Step 4

Download the
                                          			 TAR file to a TFTP server that is accessible to the Cisco Unified CME router.
                                          			 Each file contains all the firmware required for all phone types supported by
                                          			 that version of Cisco Unified CME.

Step 5

Use the archive tar command to extract the files to flash memory, slot 0, or an external TFTP
                                          			 server.

#### Example:

```
Router# archive tar /xtract source-url flash: /file-url
```

For example,
                                             				to extract the contents of CME-locale-de_DE-8.6.tar from TFTP server
                                             				192.168.1.1 to router flash memory, use this command:

```
Router# archive tar /xtract tftp://192.168.1.1/cme-locale-de_DE-8.6.tar flash:
```

Step 6

See Table 1 and Table 2 for a description of the codes used in the filenames and the list of supported
                                          			 directory names.

Each phone type has a JAR file that uses the following naming convention:

language - phone -sip.jar

#### Example:

For example, de-gh-sip.jar is for German on the Cisco Unified IP Phone 8961.

Each TAR file also includes the file g4-tones.xml for country-specific network tones and cadences.

Phone Type

Phone Code

3905

cin

6941

rtl

6945

rtl

8961

gh

9951

gd

9971

gd

Language

Language Code

User-Locale

Directory Name

Country Code

Network-Locale

Directory Name

English

en

English_United_States 6

US

United_States

English_United_Kingdom

UK

United_Kingdom

GB

United_Kingdom

CA

Canada

AU

Australia

Danish

dk

Danish_Denmark

DK

Denmark

Dutch

nl

Dutch_Netherlands

NL

Netherlands

French

fr

French_France

FR

France

CA

Canada

German

de

German_Germany

DE

Germany

AT

Austria

CH

Switzerland

Italian

it

Italian_Italy

IT

Italy

Japanese

jp

Japanese_Japan

JP

Japan

Norwegian

no

Norwegian_Norway

NO

Norway

Portuguese

pt

Portuguese_Portugal

PT

Portugal

Russian

ru

Russian_Russia

RU

Russian_Federation

Spanish

es

Spanish_Spain

ES

Spain

Swedish

se

Swedish_Sweden

SE

Sweden

Step 7

If you store
                                          			 the locale files in flash memory or slot 0 on the Cisco Unified CME router,
                                          			 create a TFTP alias for the user locale (text displays) and network locale
                                          			 (tones) using this format:

#### Example:

```
Router(config)# tftp-server flash:/ jar_file alias directory_name /gh-sip.jar Router(config)# tftp-server flash:/g4-tones.xml alias directory_name /g4-tones.xml
```

Use the
                                             				appropriate directory name shown in Table 1 and remove the two-letter language code from the JAR file name.

For example,
                                             				the TFTP aliases for German and Germany for the Cisco Unified IP Phone 8961
                                             				are:

```
Router(config)# tftp-server flash:/de-gh-sip.jar alias German_Germany/ Router(config)# tftp-server flash:/g4-tones.xml alias Germany/g4-tones.xml
```

Step 8

If you store
                                          			 the locale files on an external TFTP server, create a directory under the TFTP
                                          			 root directory for each user and network locale.

Use the
                                             				appropriate directory name shown in Table 1 and remove the two-letter language code from the JAR file name.

#### Example:

For example,
                                             				the user-locale directory for German and the network-locale directory for
                                             				Germany for the Cisco Unified IP Phone 8961 are:

TFTP-Root/German_Germany/gh-sip.jar
                                             				TFTP-Root/Germany/g4-tones.xml

Step 9

Assign the
                                          			 locales to the phones. To set a default locale for all phones, use the user-locale and network-locale commands in voice register global
                                          			 configuration mode.

Step 10

To support
                                          			 more than one user or network locale, see Verify Multiple Locales on SIP Phones .

Step 11

Use the create
                                                				  profile command to rebuild the configuration files.

Step 12

Use the reset command to reset the phones and see the localized displays.

### Use the Locale
                           	 Installer in Cisco Unified CME 9.0 and Later Versions

Restriction

When using
                                                   				  an external TFTP server, you must manually create the user locale folders in
                                                   				  the root directory. This is a limitation of the TFTP server.

Locale
                                                   				  support is limited to phone firmware versions that are supported by
                                                   				  Cisco Unified CME.

User-defined
                                                   				  locales are not supported if the configuration file location is “system:”.

If you
                                                   				  install and configure a user-defined locale using country codes U1-U5 and then
                                                   				  you install a new locale using the same label, the phone retains the original
                                                   				  language locale even after the phone is reset. This is a limitation of the IP
                                                   				  phone. To work around this limitation, you must configure the new package using
                                                   				  a different country code.

Each
                                                   				  user-defined country code (U1-U5) can be used for only one user-locale-tag at a
                                                   				  time. For example:

```
Router(config-register-global)# user-locale 2 U2 load Finnish.pkg Router(config-register-global)# user-locale 1 U2 load Chinese.pkg LOCALE ERROR: User Defined Locale U2 already exists on locale index 2.
```

#### Before you begin

Cisco Unified CME 9.0(1) or a later version.

When the
                                       				storage location specified by the cnf-file
                                             					 location command is flash memory, sufficient space must be on the
                                       				flash file system for extracting the contents of the locale TAR file.

You must have
                                       				an account on Cisco.com to download locale files.

Step 1

Go to http://www.cisco.com/cgi-bin/tablebuild.pl/CME-Locale

You must have
                                             				an account on Cisco.com to access the Software Download Center. If you do not
                                             				have an account or have forgotten your username or password, click the
                                             				appropriate button at the login dialog box and follow the instructions that
                                             				appear.

Step 2

Navigate to Downloads
                                                				  Home > Products > Unified
                                                				  Communications > Call Control > Mid-Market Call
                                                				  Control > Cisco Unified Communications Manager
                                                				  Express > Unified Communications Manager Express Individual File
                                                				  Set and select your version of Cisco Unified CME.

Step 3

Select the TAR
                                          			 file for the locale you want to install. Each TAR file contains locale files
                                          			 for a specific language and country and uses the following naming convention:
                                          			 CME-locale- language _ country - CMEversion .tar

#### Example:

For example,
                                             				CME-locale-de_DE-German-8.6.3.0.tar is German for Germany for Cisco Unified
                                             				CME 9.0.

Step 4

Download the
                                          			 TAR file to the location previously specified by the cnf-file location command. Each file contains all the firmware required
                                          			 for all phone types supported by that version of Cisco Unified CME.

With the
                                             				locale installer, you do not need to perform manual configuration. Instead, you
                                             				copy the locale file using the copy command
                                             				in privileged EXEC configuration mode.

You must
                                                         				  copy the locale file into the /its directory (flash:/its or slot0:/its) when
                                                         				  you store the locale files on the Cisco Unified CME router.

If the
                                                				  cnf-file location is flash memory: Copy the TAR file to the flash:/its
                                                				  directory.

#### Example:

For
                                                   					 example,

```
Router# copy tftp://12.1.1.100/CME-locale-de_DE-German-8.6.3.0.tar flash:/its
```

If the
                                                				  cnf-file location is slot0: Copy the TAR file to the slot0:/its directory.

If the
                                                				  cnf-file location is tftp: Create a folder in the root directory of the TFTP
                                                				  server for each locale using the following format and then copy the TAR file to
                                                				  the TFTP-Root folder.

#### Example:

```
TFTP-Root / TAR-filename
```

For
                                                   					 system-defined locales, use the locale folder name as shown in Table 1 .
                                                   					 For example, create the folder for system-defined German as follows:

```
TFTP-Root/de_DE-8.6.3.0.tar
```

For up
                                                   					 to five user-defined locales, use the User_Define_ n folder
                                                   					 name as shown in Table 1 .
                                                   					 A user-defined locale is a language other than the system-defined locales that
                                                   					 are predefined in Cisco IOS software. For example, create the folder for
                                                   					 user-defined locale Chinese (User_Define_1) as follows:

```
TFTP-Root/CME-locale-zh_CN-Chinese-8.6.3.0.tar
```

Language

Locale Folder Name

Country Code

English

English_United_States

US

English_United_Kingdom

UK

CA

Danish

Danish_Denmark

DK

Dutch

Dutch_Netherlands

NL

French

French_France

FR

CA

German

German_Germany

DE

AT

CH

Italian

Italian_Italy

IT

Japanese

Japanese_Japan

JP

Norwegian

Norwegian_Norway

NO

Portuguese

Portuguese_Portugal

PT

Russian

Russian_Russia

RU

Spanish

Spanish_Spain

ES

Swedish

Swedish_Sweden

SE

Un 7

User_Define_n 1

Un 1

Step 5

Use the user-locale [ user-locale-tag ] {[user-defined-code] country-code } [ load TAR-filename ] command in voice register global configuration mode
                                          			 to extract the contents of the TAR file. For country codes, see Table 1 .

Use the
                                                         				  complete filename, including the file suffix (.tar), when you configure the user-locale command for all Cisco Unified SIP IP phone types.

#### Example:

For example,
                                             				to extract the contents of the CME-locale-zh_CN-Chinese-8.6.3.0.tar file when
                                             				U1 is the country code for user-defined locale Chinese (User_Define_1), use
                                             				this command:

```
Router(config-register-global)# user-locale U1 load CME-locale-zh_CN-Chinese-8.6.3.0.tar
```

Step 6

Assign the
                                          			 locales to the phones. See Configure Multiple Locales on SIP Phones .

Step 7

Use the create
                                                				  profile command in voice register global configuration mode to
                                          			 generate the configuration profile files required for Cisco Unified SIP IP
                                          			 phones.

Step 8

Use the reset command to reset the phones and see the localized displays.

### Configure Multiple
                           	 Locales on SIP Phones

To define one or
                                 		  more alternatives to the default user and network locales and apply them to
                                 		  individual phones, perform the following steps.

Restriction

Multiple
                                                   				  user and network locales are supported only on Cisco Unified IP Phone 8961,
                                                   				  9951, and 9971.

#### Before you begin

Cisco Unified
                                       				CME 8.6 or a later version. For Cisco Unified IP Phone 9971, Cisco Unified CME
                                       				8.8 or a later version.

To specify
                                       				alternative user and network locales for individual phones in a
                                       				Cisco Unified CME system, you must use per-phone configuration files. For more
                                       				information, see Install System-Defined Locales for Cisco Unified IP Phone 6921, 6945, 7906, 7911, 7921, 7931, 7941, 7961, 7970, 7971, and
                                          Cisco IP Communicator .

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- user-locale [ user-locale-tag ] { [ user-defined-code ] country-code }

- network-locale network-locale-tag [ user-defined-code ] country-code

- create profile

- exit

- voice register template template-tag

- user-locale user-locale-tag

- network-locale network-locale-tag

- exit

- voice register pool pool-tag

- voice register template template-tag

- exit

- voice register
                                       				  global

- reset

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
Router(config)#voice register global
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Step 4

user-locale [ user-locale-tag ] { [ user-defined-code ] country-code }

#### Example:

```
Router(config-register-global)# user-locale 1 DE
```

Specifies a
                                             				language for phone displays.

user-locale-tag —Assigns a locale identifier to the
                                                   					 locale. Range is 0 to 4. Default: 0. This argument is required when defining
                                                   					 some locale other than the default (0).

country-code —Type ? to display
                                                   					 a list of system-defined codes. Default: US (United States).

Step 5

network-locale network-locale-tag [ user-defined-code ] country-code

#### Example:

```
Router(config-register-global)# network-locale 1 FR
```

Specifies a
                                             				country for tones and cadences.

network-locale-tag —Assigns a locale identifier to
                                                   					 the country code. Range is 0 to 4. Default: 0. This argument is required when
                                                   					 defining some locale other than the default (0).

country-code —Type ? to display
                                                   					 a list of system-defined codes. Default: US (United States). You can assign any
                                                   					 valid ISO 3166 code to a user-defined code (U1 to U5).

Step 6

create profile

#### Example:

```
Router(config-register-global)# create profile
```

Generates
                                             				provisioning files required for SIP phones and writes the file to the location
                                             				specified with the tftp-path command.

Step 7

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits voice
                                             				register global configuration mode.

Step 8

voice register template template-tag

#### Example:

```
Router(config)voice register template 10
```

Enters voice
                                             				register template configuration mode to define a template of common parameters
                                             				for SIP phones in Cisco Unified CME.

Range— 1
                                                   					 to 10.

Step 9

user-locale user-locale-tag

#### Example:

```
Router(config-ephone-template)# user-locale 2
```

Assigns a
                                             				user locale to this ephone template.

user-locale-tag —A locale tag that was created in Step 4 .
                                                   					 Range is 0 to 4.

Step 10

network-locale network-locale-tag

#### Example:

```
Router(config-ephone-template)# network-locale 2
```

Assigns a
                                             				network locale to this ephone template.

network-locale-tag —A locale tag that was created
                                                   					 in Step 5 .
                                                   					 Range is 0 to 4.

Step 11

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits voice
                                             				register template configuration mode.

Step 12

voice register pool pool-tag

#### Example:

```
Router(config)#voice register pool 5
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

Step 13

voice register template template-tag

#### Example:

```
Router(config)voice register template 10
```

Enters voice
                                             				register template configuration mode to define a template of common parameters
                                             				for SIP phones in Cisco Unified CME.

Range— 1
                                                   					 to 10.

Step 14

exit

#### Example:

```
Router(config-ephone)# exit
```

Exits voice
                                             				register template configuration mode.

Step 15

voice register
                                                				  global

#### Example:

```
Router(config)#voice register global
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Step 16

reset

#### Example:

```
Router(config-register-global)# reset
```

Performs a
                                             				complete reboot of all phones or the specified phone, including contacting the
                                             				DHCP and TFTP servers for the latest configuration information.

Step 17

end

#### Example:

```
Router(config-register-global)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Multiple Locales on SIP Phones

Step 1

Use the show voice register tftp-bind command to
                                          			 display a list of configuration files that are accessible to IP phones using
                                          			 TFTP, including the dictionary, language, and tone configuration files.

#### Example:

```
Router#sh voice register tftp-bind tftp-server syncinfo.xml url system:/cme/sipphone/syncinfo.xml
			 tftp-server SIPDefault.cnf url system:/cme/sipphone/SIPDefault.cnf
			 tftp-server softkeyDefault_kpml.xml url system:/cme/sipphone/softkeyDefault_kpml
			 .xml
			 tftp-server softkeyDefault.xml url system:/cme/sipphone/softkeyDefault.xml
			 tftp-server softkey2_kpml.xml url system:/cme/sipphone/softkey2_kpml.xml
			 tftp-server softkey2.xml url system:/cme/sipphone/softkey2.xml
			 tftp-server featurePolicyDefault.xml url system:/cme/sipphone/featurePolicyDefau
			 lt.xml
			 tftp-server featurePolicy2.xml url system:/cme/sipphone/featurePolicy2.xml
			 tftp-server SEPACA016FDC1BD.cnf.xml url system:/cme/sipphone/SEPACA016FDC1BD.cnf
			 .xml
```

Step 2

Use the show voice register template all command to
                                          			 check the user locale and network locale settings in each ephone template.

Step 3

Use the show voice register pool all command to
                                          			 check that the correct templates are applied to phones.

Step 4

If the configuration file location is not TFTP, use the debug tftp events command to see which
                                          			 files Cisco Unified CME is looking for and whether the files are found and
                                          			 opened correctly. There are usually three states (“looking for x file,” “opened
                                          			 x file,” and “finished x file”). The file is found when all three states are
                                          			 displayed. For an external TFTP server, you can use the logs from the TFTP
                                          			 server.

## Configuration Examples for Localization

### Example for Configuring Multiple User and Network Locales

The following example sets the default locale of 0 to Germany, which
                                 		  defines Germany as the default user and network locale. Germany is used for all
                                 		  phones unless you apply a different locale to individual phones using ephone
                                 		  templates.

```
telephony service
		   cnf-file location flash:
		   cnf-file perphone
		   user-locale 0 DE
		   network-locale 0 DE
```

After using the previous commands to define Germany as the default
                                 		  user and network locale, use the following commands to return the default value
                                 		  of 0 to US:

```
telephony service
		   no user-locale 0 DE
		   no network-locale 0 DE
```

Another way to define Germany as the default user and network locale
                                 		  is to use the following commands:

```
telephony service
		   cnf-file location flash:
		  cnf-file perphone
		   user-locale DE
		   network-locale DE
```

After using the previous commands, use the following commands to
                                 		  return the default to US:

```
telephony service
		   no user-locale DE
		   no network-locale DE
```

The following example defines three alternative locales: JP (Japan),
                                 		  FR (France), and ES (Spain). The default is US for all phones that do not have
                                 		  an alternative applied using ephone templates. In this example, ephone 11 uses
                                 		  JP for its locales, ephone 12 uses FR, ephone 13 uses ES, and ephone 14 uses
                                 		  the default, US.

```
telephony-service
		   cnf-file location flash:
		   cnf-file perphone
		   create cnf-files
		   user-locale 1 JP
		   user-locale 2 FR
		   user-locale 3 ES
		   network-locale 1 JP
		   network-locale 2 FR
		   network-locale 3 ES
		   create cnf-files
		  
		  ephone-template 1
		  user-locale 1
		   network-locale 1
		  
		  ephone-template 2
		   user-locale 2
		   network-locale 2
		  
		  ephone-template 3
		   user-locale 3
		   network-locale 3
		  
		  ephone 11
		   button 1:25
		   ephone-template 1
		  
		  ephone 12
		   button 1:26
		   ephone-template 2
		  
		  ephone 13
		   button 1:27
		   ephone-template 3
		  
		  ephone 14
		  button 1:28
```

### Example for Configuring User-Defined Locales

The following example shows user-locale tag 1 assigned to code U1,
                                 		  which is defined as ZH for Traditional Chinese. Traditional Chinese is not
                                 		  predefined in the system so you must download the appropriate XML files to
                                 		  support this language.

In this example, ephone 11 uses Traditional Chinese (ZH) and ephone 12
                                 		  uses the default, US English. The default is US English for all phones that do
                                 		  not have an alternative applied using ephone templates.

```
telephony-service
		 cnf-file location flash:
		 cnf-file perphone
		 user-locale 1 U1 ZH
		 network-locale 1 U1 CN
		
		ephone-template 2
		 user-locale 1
		 network-locale 1
	
		ephone 11
		 button 1:25
		 ephone-template 2
		
		ephone 12
		 button 1:26
```

### Example for Configuring Chinese as the User-Defined Locale

The following is a sample output from the user-locale command when you configure the
                                 		  Chinese language as the user-defined locale in Cisco Unified CME:

```
Router(config-register-global)# user-locale U1 load chinese.pkg Updating CNF files

LOCALE INSTALLER MESSAGE: VER:1
LOCALE INSTALLER MESSAGE: Langcode:zh
LOCALE INSTALLER MESSAGE: Language:Chinese
LOCALE INSTALLER MESSAGE: Filename: 7905-dictionary.xml
LOCALE INSTALLER MESSAGE: Filename: 7905-font.xml
LOCALE INSTALLER MESSAGE: Filename: 7905-kate.xml
LOCALE INSTALLER MESSAGE: Filename: 7960-tones.xml
LOCALE INSTALLER MESSAGE: Filename: mk-sccp.jar
LOCALE INSTALLER MESSAGE: Filename: td-sccp.jar
LOCALE INSTALLER MESSAGE: Filename: tc-sccp.jar
LOCALE INSTALLER MESSAGE: Filename: 7921-font.dat
LOCALE INSTALLER MESSAGE: Filename: 7921-kate.utf-8.xml
LOCALE INSTALLER MESSAGE: Filename: 7921-kate.xml
LOCALE INSTALLER MESSAGE: Filename: SCCP-dictionary.utf-8.xml
LOCALE INSTALLER MESSAGE: Filename: SCCP-dictionary.xml
LOCALE INSTALLER MESSAGE: Filename: SCCP-dictionary-ext.xml
LOCALE INSTALLER MESSAGE: Filename: 7921-dictionary.xml
LOCALE INSTALLER MESSAGE: Filename: g3-tones.xml
LOCALE INSTALLER MESSAGE: Filename: utf8_tags_file
LOCALE INSTALLER MESSAGE: Filename: tags_file
LOCALE INSTALLER MESSAGE: New Locale configured

Processing file:flash:/its/user_define_1_tags_file

Processing file:flash:/its/user_define_1_utf8_tags_file

CNF-FILES: Clock is not set or synchronized, retaining old versionStamps
CNF files updating complete
```

### Example for Configuring Swedish as the System-Defined Locale

The following is a sample output from the user-locale command when you configure the
                                 		  Swedish language as the system-defined locale in Cisco Unified CME:

```
Router(config-register-global)# user-locale SE load swedish.pkg Updating CNF files

LOCALE INSTALLER MESSAGE: VER:1
LOCALE INSTALLER MESSAGE: Langcode:se
LOCALE INSTALLER MESSAGE: Language:swedish
LOCALE INSTALLER MESSAGE: Filename: g3-tones.xml
LOCALE INSTALLER MESSAGE: Filename: gp-sccp.jar
LOCALE INSTALLER MESSAGE: Filename: ipc-sccp.jar
LOCALE INSTALLER MESSAGE: Filename: mk-sccp.jar
LOCALE INSTALLER MESSAGE: Filename: tc-sccp.jar
LOCALE INSTALLER MESSAGE: Filename: td-sccp.jar
LOCALE INSTALLER MESSAGE: New Locale configured

CNF-FILES: Clock is not set or synchronized, retaining old versionStamps
CNF files updating complete
```

## Configuration Examples for Locale Installer on SCCP Phones

### System-Defined Locale is the Default Applied to All Phones

The following example is the output from the user-locale command when you configure a
                                 		  system-defined locale for Cisco Unified CME and the locale is on the default
                                 		  locale index (user-locale-tag 0). The user-locale-tag argument is required only
                                 		  when using multiple locales; otherwise, the specified language is the default
                                 		  applied to all SCCP phones.

```
Router(config-telephony)# user-locale SE load CME-locale-sv_SV-7.0.1.1a.tar Updating CNF files 
		   
		  LOCALE INSTALLER MESSAGE: VER:1 
		  LOCALE INSTALLER MESSAGE: Langcode:se 
		  LOCALE INSTALLER MESSAGE: Language:swedish 
		  LOCALE INSTALLER MESSAGE: Filename: g3-tones.xml 
		  LOCALE INSTALLER MESSAGE: Filename: gp-sccp.jar 
		  LOCALE INSTALLER MESSAGE: Filename: ipc-sccp.jar 
		  LOCALE INSTALLER MESSAGE: Filename: mk-sccp.jar 
		  LOCALE INSTALLER MESSAGE: Filename: tc-sccp.jar 
		  LOCALE INSTALLER MESSAGE: Filename: td-sccp.jar 
		  LOCALE INSTALLER MESSAGE: New Locale configured 
		  
		  CNF-FILES: Clock is not set or synchronized, retaining old versionStamps 
		  CNF files updating complete 
		  Router(config-telephony)# create cnf-files Router(config-telephony)# ephone 3 Router(config-ephone)# reset
```

### User-Defined Locale is Default Language to be Applied to All
                           	 Phones

The following example is the output from the user-locale command when you configure a
                                 		  user-defined locale for Cisco Unified CME and the locale is on the default
                                 		  locale index (user-locale-tag 0). The user-locale-tag argument is required when
                                 		  using multiple locales, otherwise the specified language is the default applied
                                 		  to all SCCP phones.

```
Router(config-telephone)# user-locale U1 load CME-locale-xh_CN-7.0.1.1.tar Updating CNF files
		LOCALE INSTALLER MESSAGE: VER:1
		LOCALE INSTALLER MESSAGE: Langcode:fi
		LOCALE INSTALLER MESSAGE: Language:Finnish
		LOCALE INSTALLER MESSAGE: Filename: 7905-dictionary.xml
		LOCALE INSTALLER MESSAGE: Filename: 7905-kate.xml
		LOCALE INSTALLER MESSAGE: Filename: 7920-dictionary.xml
		LOCALE INSTALLER MESSAGE: Filename: 7960-dictionary.xml
		LOCALE INSTALLER MESSAGE: Filename: 7960-font.xml
		LOCALE INSTALLER MESSAGE: Filename: 7960-kate.xml
		LOCALE INSTALLER MESSAGE: Filename: 7960-tones.xml
		LOCALE INSTALLER MESSAGE: Filename: mk-sccp.jar
		LOCALE INSTALLER MESSAGE: Filename: tc-sccp.jar
		LOCALE INSTALLER MESSAGE: Filename: td-sccp.jar
		LOCALE INSTALLER MESSAGE: Filename: tags_file
		LOCALE INSTALLER MESSAGE: Filename: utf8_tags_file
		LOCALE INSTALLER MESSAGE: Filename: g3-tones.xml
		LOCALE INSTALLER MESSAGE: Filename: SCCP-dictionary.utf-8.xml
		LOCALE INSTALLER MESSAGE: Filename: SCCP-dictionary.xml
		LOCALE INSTALLER MESSAGE: Filename: ipc-sccp.jar
		LOCALE INSTALLER MESSAGE: Filename: gp-sccp.jar
		LOCALE INSTALLER MESSAGE: New Locale configured
		
		Processing file:flash:/its/user_define_2_tags_file
		
		Processing file:flash:/its/user_define_2_utf8_tags_file
		
		CNF-FILES: Clock is not set or synchronized, retaining old versionStamps
		CNF files updating complete
		
		Router(config-telephony)# create cnf-files Router(config-telephony)# ephone 3 Router(config-ephone)# reset
```

### Locale on a Non-default Locale Index

The following example is the output from the user-locale command if you configure a
                                 		  user-defined locale as an alternate locale for a particular SCCP phone (ephone
                                 		  1) in Cisco Unified CME. The user-locale-tag argument is required only
                                 		  when using multiple locales. In this configuration, the locale is user-defined
                                 		  Finnish (U2) on user-locale index 2.

```
Router(config-telephony)# user-locale 2 U2 load CME-locale-fi_FI-7.0.1.1.tar Updating CNF files
		
		LOCALE INSTALLER MESSAGE: VER:1
		LOCALE INSTALLER MESSAGE: Langcode:fi
		LOCALE INSTALLER MESSAGE: Language:Finnish
		LOCALE INSTALLER MESSAGE: Filename: 7905-dictionary.xml
		LOCALE INSTALLER MESSAGE: Filename: 7905-kate.xml
		LOCALE INSTALLER MESSAGE: Filename: 7920-dictionary.xml
		LOCALE INSTALLER MESSAGE: Filename: 7960-dictionary.xml
		LOCALE INSTALLER MESSAGE: Filename: 7960-font.xml
		LOCALE INSTALLER MESSAGE: Filename: 7960-kate.xml
		LOCALE INSTALLER MESSAGE: Filename: 7960-tones.xml
		LOCALE INSTALLER MESSAGE: Filename: mk-sccp.jar
		LOCALE INSTALLER MESSAGE: Filename: tc-sccp.jar
		LOCALE INSTALLER MESSAGE: Filename: td-sccp.jar
		LOCALE INSTALLER MESSAGE: Filename: tags_file
		LOCALE INSTALLER MESSAGE: Filename: utf8_tags_file
		LOCALE INSTALLER MESSAGE: Filename: g3-tones.xml
		LOCALE INSTALLER MESSAGE: Filename: SCCP-dictionary.utf-8.xml
		LOCALE INSTALLER MESSAGE: Filename: SCCP-dictionary.xml
		LOCALE INSTALLER MESSAGE: Filename: ipc-sccp.jar
		LOCALE INSTALLER MESSAGE: Filename: gp-sccp.jar
		LOCALE INSTALLER MESSAGE: New Locale configured
		
		Processing file:flash:/its/user_define_2_tags_file
		
		Processing file:flash:/its/user_define_2_utf8_tags_file
		
		CNF-FILES: Clock is not set or synchronized, retaining old versionStamps
		CNF files updating complete
		
		Router(config-telephony)# ephone-template 1 Router(config-ephone-template)# user-locale 2 Router(config-ephone-template)# ephone 1 Router(config-ephone)# ephone-template 1 The ephone template tag has been changed under this ephone, please restart or reset ephone to take effect.
		Router(config-ephone)# telephony-service Router(config-telephony)# create cnf-files Router(config-telephony)# ephone 1 Router(config-ephone)# reset
```

### Examples for Configuring Multiple User and Network Locales on SIP
                           	 Phones

The following example sets the default locale of 0 to Germany, which
                                 		  defines Germany as the default user and network locale. Germany is used for all
                                 		  phones unless you apply a different locale to individual phones using ephone
                                 		  templates.

```
voice register global
		  user-locale 0 DE
		 network-locale 0 DE
```

After using the previous commands to define Germany as the default
                                 		  user and network locale, use the following commands to return the default value
                                 		  of 0 to US:

```
voice register global
		 no user-locale 0 DE
		no network-locale 0 DE
```

Another way to define Germany as the default user and network locale
                                 		  is to use the following commands:

```
voice register global
		 user-locale DE
		 network-locale DE
```

After using the previous commands, use the following commands to
                                 		  return the default to US:

```
voice register global
		 no user-locale DE
		 no network-locale DE
```

SIP: Alternative Locales

The following example defines three alternative locales: JP (Japan),
                                 		  FR (France), and ES (Spain). The default is US for all phones that do not have
                                 		  an alternative applied using ephone templates. In this example, ephone 11 uses
                                 		  JP for its locales, ephone 12 uses FR, ephone 13 uses ES, and ephone 14 uses
                                 		  the default, US.

```
voice register global
		 create profile
		 user-locale 1 JP
		 user-locale 2 FR
		 user-locale 3 ES
		 network-locale 1 JP
		 network-locale 2 FR
		 network-locale 3 ES
		 create profile
		
		voice register template 1
		 user-locale 1
		 network-locale 1
		
		voice register template 2
		 user-locale 2
		 network-locale 2
		
		voice register pool 1
		  number 1 dn 1
		  template 1
		 user-locale 3
		network-locale 3
		
		voice register pool 2
		  number 2 dn 2
		  template 2
		
		voice register pool 6
		  number 3 dn 3
		   template 3
```

### Example for
                           	 Configuring Locale Installer on SIP Phones

The following
                                 		  example shows how the locale installer only requires you to copy the locale
                                 		  file using the copy command
                                 		  in privileged EXEC configuration mode to configure a locale on a Cisco Unified
                                 		  SIP IP phone. The example also shows that the locale file has been copied in
                                 		  the /its directory.

```
Router# copy tftp://100.1.1.1/CME-locale-de_DE-German-8.6.3.0.tar flash:/its Destination filename [/its/CME-locale-de_DE-German-8.6.3.0.tar]? 
Router# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)# voice register global
Router(config-register-global)# user-locale DE load CME-locale-de_DE-German-8.6.3.0.tar LOCALE INSTALLER MESSAGE (SIP):Loading Locale Package...
LOCALE INSTALLER MESSAGE: VER:3
LOCALE INSTALLER MESSAGE: Langcode:de_DE
LOCALE INSTALLER MESSAGE: Language:German
LOCALE INSTALLER MESSAGE: Filename: g3-tones.xml
LOCALE INSTALLER MESSAGE: Filename: tags_file
LOCALE INSTALLER MESSAGE: Filename: utf8_tags_file
LOCALE INSTALLER MESSAGE: Filename: gd-sip.jar
LOCALE INSTALLER MESSAGE: Filename: gh-sip.jar
LOCALE INSTALLER MESSAGE: Filename: g4-tones.xml
LOCALE INSTALLER MESSAGE: New Locale configured
Router(config-register-global)#
```

## Where to  Go Next

Ephone Templates

For more information about ephone templates, see Templates .

## Feature
                        	 Information for Localization Support

The following table
                           		provides release information about the feature or features described in this
                           		module. This table lists only the software release that introduced support for
                           		a given feature in a given software release train. Unless noted otherwise,
                           		subsequent releases of that software release train also support that feature.

Use Cisco Feature
                           		Navigator to find information about platform support and Cisco software image
                           		support. To access Cisco Feature Navigator, go to www.cisco.com/go/cfn .
                           		An account on Cisco.com is not required.

Feature Name

Cisco Unified CME Version

Feature
                                       				  Information

Localization
                                       				  Enhancements for Cisco Unified SIP IP Phones

10.5

Cisco
                                       				  Unified CME 10.5 provides support for additional languages.

Localization
                                       				  Enhancements for Cisco Unified SIP IP Phones

9.0

Provides the
                                       				  following enhanced localization support for Cisco Unified SIP IP phones:

Localization support for Cisco Unified 6941 and 6945 SIP IP
                                             						Phones.

Locale
                                             						installer that supports a single procedure for all Cisco Unified SIP IP phones.

Localization
                                       				  Enhancement

8.8

Adds
                                       				  localization support for Cisco Unified 3905 SIP and Cisco Unified 6945, 8941,
                                       				  and 8945 SCCP IP Phones.

Usability
                                       				  Enhancement

8.6

Adds
                                       				  localization support for SIP IP Phones.

Cisco Unified CME Usability Enhancement

7.0(1)

Locale
                                             						installer that supports a single procedure for all SCCP IP phones.

Parses
                                             						firmware-load text files and automatically creates the required TFTP aliases
                                             						for localization.

Backward
                                             						compatibility with the configuration method in Cisco Unified CME 7.0 and
                                             						earlier versions.

Multiple
                                       				  Locales

4.0

Multiple
                                       				  user and network locales were introduced.

User-Defined
                                       				  Locales

4.0

User-defined
                                       				  locales were introduced.

| Note | Some abbreviations such as BLF, SNR, and CME are not localized. |
|---|---|

| Restriction | All the localization enhancements are supported in Cisco Unified CME only. They are not supported in Cisco Unified SRST. Table 1 shows the language codes used in the filenames of locale files. Table 1. Language Codes for User-Defined Locales Language Language Code Canadian French fr_CA For configuration information, see Install User-Defined Locales . | Language | Language Code | Canadian French | fr_CA |
|---|---|---|---|---|---|
| Language | Language Code |
| Canadian French | fr_CA |

| Language | Language Code |
|---|---|
| Canadian French | fr_CA |

| Note | TFTP aliases for
                                          		  localization are not automatically created for Cisco Unified SIP IP phones in a
                                          		  Cisco Unified CME system. For more information on how to manually create TFTP
                                          		  aliases, see Install System-Defined Locales for Cisco Unified IP Phone 8961, 9951, and 9971 . |
|---|---|

| Note | Cisco Unified CME
                                          		  10.5 Release onwards, the System defined locales are deprecated and
                                          		  User-defined locales are recommended. |
|---|---|

| Note | The locale files
                                          		  must be stored in the same location as the configuration files. |
|---|---|

| Note | In
                                             		  Cisco Unified CME 4.3 and earlier versions, you do not include the file suffix
                                             		  for any phone type except Cisco ATA and Cisco Unified IP Phone 7905 and 7912.
                                             		  For example: Router(config-telephony)# load 7941 SCCP41.8-2-2SR2S |
|---|---|

| Note | You must copy the
                                          		  locale file into the /its directory (flash:/its or slot0:/its) when you store
                                          		  the locale files on the Cisco Unified CME router. |
|---|---|

| Tip | The locale installer simplifies the installation and configuration of system- and user-defined locales in Cisco Unified CME
                                          7.0(1) and later versions. To use the locale installer in Cisco Unified CME 7.0(1) and later versions, see Use the Locale Installer in Cisco Unified CME 7.0(1) and Later Versions . |
|---|---|

| Restriction | Localization
                                                   				  is not supported for SIP phones. Phone
                                                   				  firmware, configuration files, and locale files must be in the same directory,
                                                   				  except the directory file for Japanese and Russian, which must be in flash
                                                   				  memory. |
|---|---|

| Step 1 | Go to http://www.cisco.com/cgi-bin/tablebuild.pl/CME-Locale . You must have
                                             				an account on Cisco.com to access the Software Download Center. If you do not
                                             				have an account or if you have forgotten your username or password, click the
                                             				appropriate button at the login dialog box and follow the instructions that
                                             				appear. |
|---|---|
| Step 2 | Navigate to Downloads
                                                				  Home > Products > Unified
                                                				  Communications > Call Control > Mid-Market Call
                                                				  Control > Cisco Unified Communications Manager Express > Unified Communications Manager Express Individual File
                                                				  Set and select your version of Cisco Unified CME. |
| Step 3 | Select the TAR file for the locale you want to install. Each TAR file contains locale files for a specific language and country
                                          and uses the following naming convention: CME-locale- language _ country - CMEversion Example: For example, CME-locale-de_DE-4.0.2-2.0 is German for Germany for Cisco Unified CME 4.0(2). |
| Step 4 | Download the
                                          			 TAR file to a TFTP server that is accessible to the Cisco Unified CME router.
                                          			 Each file contains all the firmware required for all phone types supported by
                                          			 that version of Cisco Unified CME. |
| Step 5 | Use the archive tar command to extract the files to flash memory, slot 0, or an external TFTP server. Example: Router# archive tar /xtract source-url flash: /file-url Example: For example, to extract the contents of CME-locale-de_DE-4.0.2-2.0.tar from TFTP server 192.168.1.1 to router flash memory,
                                             use this command: Router# archive tar /xtract tftp://192.168.1.1/cme-locale-de_DE-4.0.2-2.0.tar flash: |
| Step 6 | See Table 1 and Table 2 for a description of the codes used in the filenames and the list of supported
                                          			 directory names. Each phone type has a JAR file that uses the following naming convention: language - phone -sccp.jar Example: For example, de-td-sccp.jar is for German on the Cisco Unified IP Phone 7970. Each TAR file also includes the file g3-tones.xml for country-specific network tones and cadences. Table 2. Phone-Type Codes for Locale JAR Files Phone Type Phone Code 6921 rtl 6945 rtl 7906/7911 tc 7931 gp 7941/7961 mk 7970/7971 td 8941/8945 gh CIPC ipc Table 3. System-Defined User and Network Locales Language Language Code User-Locale Directory Name Country Code Network-Locale Directory Name English en English_United_States 1 US United_States English_United_Kingdom UK United_Kingdom CA Canada Danish dk Danish_Denmark DK Denmark Dutch nl Dutch_Netherlands NL Netherlands French fr French_France FR France CA Canada German de German_Germany DE Germany AT Austria CH Switzerland Italian it Italian_Italy IT Italy Japanese 2 jp Japanese_Japan JP Japan Norwegian no Norwegian_Norway NO Norway Portuguese pt Portuguese_Portugal PT Portugal Russian ru Russian_Russia RU Russian_Federation Spanish es Spanish_Spain ES Spain Swedish se Swedish_Sweden SE Sweden 1 English for the United States is the default language. You do not need to install the JAR file for U.S. English unless you
                                                assign a different language to a phone and then want to reassign English. 2 Katakana is supported by Cisco Unified IP Phone 7905, 7912, 7940, and 7960. Kanji is supported by Cisco Unified IP Phone 7911,
                                                7941, 7961, 7970, and 7971. | Phone Type | Phone Code | 6921 | rtl | 6945 | rtl | 7906/7911 | tc | 7931 | gp | 7941/7961 | mk | 7970/7971 | td | 8941/8945 | gh | CIPC | ipc | Language | Language Code | User-Locale Directory Name | Country Code | Network-Locale Directory Name | English | en | English_United_States 1 | US | United_States | English_United_Kingdom | UK | United_Kingdom |  | CA | Canada | Danish | dk | Danish_Denmark | DK | Denmark | Dutch | nl | Dutch_Netherlands | NL | Netherlands | French | fr | French_France | FR | France | CA | Canada | German | de | German_Germany | DE | Germany | AT | Austria | CH | Switzerland | Italian | it | Italian_Italy | IT | Italy | Japanese 2 | jp | Japanese_Japan | JP | Japan | Norwegian | no | Norwegian_Norway | NO | Norway | Portuguese | pt | Portuguese_Portugal | PT | Portugal | Russian | ru | Russian_Russia | RU | Russian_Federation | Spanish | es | Spanish_Spain | ES | Spain | Swedish | se | Swedish_Sweden | SE | Sweden |
| Phone Type | Phone Code |
| 6921 | rtl |
| 6945 | rtl |
| 7906/7911 | tc |
| 7931 | gp |
| 7941/7961 | mk |
| 7970/7971 | td |
| 8941/8945 | gh |
| CIPC | ipc |
| Language | Language Code | User-Locale Directory Name | Country Code | Network-Locale Directory Name |
| English | en | English_United_States 1 | US | United_States |
| English_United_Kingdom | UK | United_Kingdom |
|  | CA | Canada |
| Danish | dk | Danish_Denmark | DK | Denmark |
| Dutch | nl | Dutch_Netherlands | NL | Netherlands |
| French | fr | French_France | FR | France |
| CA | Canada |
| German | de | German_Germany | DE | Germany |
| AT | Austria |
| CH | Switzerland |
| Italian | it | Italian_Italy | IT | Italy |
| Japanese 2 | jp | Japanese_Japan | JP | Japan |
| Norwegian | no | Norwegian_Norway | NO | Norway |
| Portuguese | pt | Portuguese_Portugal | PT | Portugal |
| Russian | ru | Russian_Russia | RU | Russian_Federation |
| Spanish | es | Spanish_Spain | ES | Spain |
| Swedish | se | Swedish_Sweden | SE | Sweden |
| Step 7 | If you store
                                          			 the locale files in flash memory or slot 0 on the Cisco Unified CME router,
                                          			 create a TFTP alias for the user locale (text displays) and network locale
                                          			 (tones) using this format: Example: Router(config)# tftp-server flash:/ jar_file alias directory_name /td-sccp.jar Router(config)# tftp-server flash:/g3-tones.xml alias directory_name /g3-tones.xml Use the
                                             				appropriate directory name shown in Table 2 and remove the two-letter language code from the JAR file name. For example,
                                             				the TFTP aliases for German and Germany for the Cisco Unified IP Phone 7970
                                             				are: Router(config)# tftp-server flash:/de-td-sccp.jar alias German_Germany/td-sccp.jar Router(config)# tftp-server flash:/g3-tones.xml alias Germany/g3-tones.xml Note On Cisco 3800 series routers, you must include /its in the directory name (flash:/its or slot0:/its). For example, the TFTP
                                                      alias for German for the Cisco Unified IP Phone 7970 is: Router# tftp-server flash:/its/de-td-sccp.jar alias German_Germany/td-sccp.jar | Note | On Cisco 3800 series routers, you must include /its in the directory name (flash:/its or slot0:/its). For example, the TFTP
                                                      alias for German for the Cisco Unified IP Phone 7970 is: Router# tftp-server flash:/its/de-td-sccp.jar alias German_Germany/td-sccp.jar |
| Note | On Cisco 3800 series routers, you must include /its in the directory name (flash:/its or slot0:/its). For example, the TFTP
                                                      alias for German for the Cisco Unified IP Phone 7970 is: Router# tftp-server flash:/its/de-td-sccp.jar alias German_Germany/td-sccp.jar |
| Step 8 | If you store
                                          			 the locale files on an external TFTP server, create a directory under the TFTP
                                          			 root directory for each user and network locale. Use the
                                             				appropriate directory name shown in Table 2 and remove the two-letter language code from the JAR file name. Example: For example,
                                             				the user-locale directory for German and the network-locale directory for
                                             				Germany for the Cisco Unified IP Phone 7970 are: TFTP-Root/German_Germany/td-sccp.jar
                                             				TFTP-Root/Germany/g3-tones.xml |
| Step 9 | For Russian
                                          			 and Japanese, you must copy the UTF8 dictionary file into flash memory to use
                                          			 special phrases. Only
                                                   					 flash memory can be used for these locales. Copy russian_tags_utf8_phrases for
                                                   					 Russian; Japanese_tags_utf8_phrases for Japanese. Use the user-locale
                                                         						  jp and user-locale
                                                         						  ru command to load the UTF8 phrases into Cisco Unified CME. |
| Step 10 | Assign the
                                          			 locales to phones. To set a default locale for all phones, use the user-locale and network-locale commands in telephony-service
                                          			 configuration mode. |
| Step 11 | To support
                                          			 more than one user or network locale, see Configure Multiple Locales on SCCP Phones . |
| Step 12 | Use the create
                                                				  cnf-files command to rebuild the configuration files. |
| Step 13 | Use the reset command to reset the phones and see the localized displays. |

| Phone Type | Phone Code |
|---|---|
| 6921 | rtl |
| 6945 | rtl |
| 7906/7911 | tc |
| 7931 | gp |
| 7941/7961 | mk |
| 7970/7971 | td |
| 8941/8945 | gh |
| CIPC | ipc |

| Language | Language Code | User-Locale Directory Name | Country Code | Network-Locale Directory Name |
|---|---|---|---|---|
| English | en | English_United_States 1 | US | United_States |
| English_United_Kingdom | UK | United_Kingdom |
|  | CA | Canada |
| Danish | dk | Danish_Denmark | DK | Denmark |
| Dutch | nl | Dutch_Netherlands | NL | Netherlands |
| French | fr | French_France | FR | France |
| CA | Canada |
| German | de | German_Germany | DE | Germany |
| AT | Austria |
| CH | Switzerland |
| Italian | it | Italian_Italy | IT | Italy |
| Japanese 2 | jp | Japanese_Japan | JP | Japan |
| Norwegian | no | Norwegian_Norway | NO | Norway |
| Portuguese | pt | Portuguese_Portugal | PT | Portugal |
| Russian | ru | Russian_Russia | RU | Russian_Federation |
| Spanish | es | Spanish_Spain | ES | Spain |
| Swedish | se | Swedish_Sweden | SE | Sweden |

| Note | On Cisco 3800 series routers, you must include /its in the directory name (flash:/its or slot0:/its). For example, the TFTP
                                                      alias for German for the Cisco Unified IP Phone 7970 is: Router# tftp-server flash:/its/de-td-sccp.jar alias German_Germany/td-sccp.jar |
|---|---|

| Note | From Cisco
                                          		  Unified CME 10.5 Release onwards, the System defined locales are deprecated and
                                          		  User-defined locales are recommended. However, the older locale packages can be
                                          		  still used but some phrases may be displayed in English. |
|---|---|

| Restriction | User-defined
                                                   				  locales are not supported on the Cisco Unified IP Phone 7920 or 7936. User-defined
                                                   				  locales are not supported if the configuration file location is “system:”. When you use
                                                   				  the setup tool from the telephony-service
                                                         						setup command to provision phones, you can only choose a default
                                                   				  user locale and network locale and you are limited to selecting a locale code
                                                   				  that is supported in the system. You cannot use multiple locales or
                                                   				  user-defined locales with the setup tool. When using a
                                                   				  user-defined locale, the phone normally displays text using the user-defined
                                                   				  fonts, except for any strings that are interpreted by Cisco Unified CME, such
                                                   				  as “Cisco/Personal Directory,” “Speed Dial/Fast Dial,” and so forth. |
|---|---|

| Step 1 | Go to http://www.cisco.com/cgi-bin/tablebuild.pl/CME-Locale . You must have
                                             				an account on Cisco.com to access the Software Download Center. If you do not
                                             				have an account or if you have forgotten your username or password, click the
                                             				appropriate button at the login dialog box and follow the instructions that
                                             				appear. |
|---|---|
| Step 2 | Navigate to Downloads
                                                				  Home > Products > Unified
                                                				  Communications > Call Control > Mid-Market Call
                                                				  Control > Cisco Unified Communications Manager
                                                				  Express > Unified Communications Manager Express Individual File Set and select your version of Cisco Unified
                                          			 CME. |
| Step 3 | Select the TAR
                                          			 file for the locale that you want to install. Each TAR file contains locale
                                          			 files for a specific language and country and uses the following naming
                                          			 convention: CME-locale- language _ country - CMEversion - fileversion . Example: For example,
                                             				CME-locale-zh_CN-4.0.3-2.0 is Traditional Chinese for China for
                                             				Cisco Unified CME 4.0(3). |
| Step 4 | Download the
                                          			 TAR file to a TFTP server that is accessible to the Cisco Unified CME router.
                                          			 Each file contains all the firmware required for all phone types supported by
                                          			 that version of Cisco Unified CME. |
| Step 5 | Use the archive tar command to extract the files to slot 0, flash memory, or an external TFTP
                                          			 server. Example: Router# archive tar /xtract source-url flash: /file-url For example,
                                             				to extract the contents of CME-locale-zh_CN-4.0.3-2.0.tar from TFTP server
                                             				192.168.1.1 to router flash memory, use this command: Router# archive tar /xtract tftp://192.168.1.1/cme-locale-zh_CN-4.0.3-2.0.tar flash: |
| Step 6 | For Cisco
                                          			 Unified IP Phone 7905, 7912, 7940, or 7960, go to Step 11 .
                                          			 For Cisco Unified IP Phone 7911, 7941, 7961, 7970, or 7971, go to Step 7 . |
| Step 7 | Each phone
                                          			 type has a JAR file that uses the following naming convention: language - type -sccp.jar Example: For example,
                                             				zh-td-sccp.jar is Traditional Chinese for the Cisco Unified IP Phone 7970. See Table 1 and Table 2 for a description of the codes used in the filenames. Table 4. Phone-Type
                                                   				Codes for Locale Files Phone
                                                         						  Type Code 6921 rtl 6945 rtl 7906/7911 tc 7931 gp 7941/7961 mk 7970/7971 td 8941/8945 gh CIPC ipc Table 5. Language
                                                   				Codes for User-Defined Locales Language Language Code Bulgarian bg Chinese zh 3 Croation hr Czech Republic cs Finnish fi Greek el Hungarian hu Korean ko Polish pl Portugese (Brazil) pt Romanian ro Serbian sr Slovakian sk Slovenian sl Turkish tr 3 For
                                                							 Cisco Unified IP Phone 7931, code for Chinese Simplified is chs; Chinese
                                                							 Traditional is cht. | Phone
                                                         						  Type | Code | 6921 | rtl | 6945 | rtl | 7906/7911 | tc | 7931 | gp | 7941/7961 | mk | 7970/7971 | td | 8941/8945 | gh | CIPC | ipc | Language | Language Code | Bulgarian | bg | Chinese | zh 3 | Croation | hr | Czech Republic | cs | Finnish | fi | Greek | el | Hungarian | hu | Korean | ko | Polish | pl | Portugese (Brazil) | pt | Romanian | ro | Serbian | sr | Slovakian | sk | Slovenian | sl | Turkish | tr |
| Phone
                                                         						  Type | Code |
| 6921 | rtl |
| 6945 | rtl |
| 7906/7911 | tc |
| 7931 | gp |
| 7941/7961 | mk |
| 7970/7971 | td |
| 8941/8945 | gh |
| CIPC | ipc |
| Language | Language Code |
| Bulgarian | bg |
| Chinese | zh 3 |
| Croation | hr |
| Czech Republic | cs |
| Finnish | fi |
| Greek | el |
| Hungarian | hu |
| Korean | ko |
| Polish | pl |
| Portugese (Brazil) | pt |
| Romanian | ro |
| Serbian | sr |
| Slovakian | sk |
| Slovenian | sl |
| Turkish | tr |
| Step 8 | If you store
                                          			 the locale files in flash memory or slot 0 on the Cisco Unified CME router,
                                          			 create a TFTP alias using this format: Example: Router(config)# tftp-server flash:/ jar_file alias directory_name /td-sccp.jar Remove the
                                             				two-letter language code from the JAR filename and use one of five supported
                                             				directory names with the following convention: user_define_ number ,
                                             				where number is 1
                                             				to 5 For example,
                                             				the alias for Chinese on the Cisco Unified IP Phone 7970 is: Router(config)# tftp-server flash:/zh-td-sccp.jar alias user_define_1/td-sccp.jar Note On Cisco
                                                         				  3800 series routers, you must include /its in the directory name (flash:/its or
                                                         				  slot0:/its). For example, the TFTP alias for Chinese for the Cisco Unified IP
                                                         				  Phone 7970 is: Router(config)# tftp-server flash:/its/zh-td-sccp.jar alias user_define_1/td-sccp.jar | Note | On Cisco
                                                         				  3800 series routers, you must include /its in the directory name (flash:/its or
                                                         				  slot0:/its). For example, the TFTP alias for Chinese for the Cisco Unified IP
                                                         				  Phone 7970 is: Router(config)# tftp-server flash:/its/zh-td-sccp.jar alias user_define_1/td-sccp.jar |
| Note | On Cisco
                                                         				  3800 series routers, you must include /its in the directory name (flash:/its or
                                                         				  slot0:/its). For example, the TFTP alias for Chinese for the Cisco Unified IP
                                                         				  Phone 7970 is: Router(config)# tftp-server flash:/its/zh-td-sccp.jar alias user_define_1/td-sccp.jar |
| Step 9 | If you store
                                          			 the locale files on an external TFTP server, create a directory under the TFTP
                                          			 root directory for each locale. Remove the
                                             				two-letter language code from the JAR filename and use one of five supported
                                             				directory names with the following convention: user_define_ number ,
                                             				where number is 1
                                             				to 5 Example: For example,
                                             				for Chinese on the Cisco Unified IP Phone 7970, remove “zh” from the JAR
                                             				filename and create the “user_define_1” directory under TFTP-Root on the TFTP
                                             				server: TFTP-Root/user_define_1/td-sccp.jar |
| Step 10 | Go to Step 13 . |
| Step 11 | Download one
                                          			 or more of the following XML files depending on your selected locale and phone
                                          			 type. All required files are included in the JAR file. Example: 7905-dictionary.xml 
			 7905-font.xml  
			 7905-kate.xml  
			 7920-dictionary.xml 
			 7960-dictionary.xml 
			 7960-font.xml 
			 7960-kate.xml  
			 7960-tones.xml 
			 SCCP-dictionary.utf-8.xml 
			 SCCP-dictionary.xml |
| Step 12 | Rename these
                                          			 files and copy them to flash memory, slot 0, or an external TFTP server. Rename
                                          			 the files using the format user_define_ number _ filename where number is 1
                                          			 to 5. Example: For example,
                                             				use the following names if you are setting up the first user-locale: user_define_1_7905-dictionary.xml  
			 user_define_1_7905-font.xml 
			 user_define_1_7905-kate.xml 
			 user_define_1_7920-dictionary.xml 
			 user_define_1_7960-dictionary.xml 
			 user_define_1_7960-font.xml  
			 user_define_1_7960-kate.xml  
			 user_define_1_7960-tones.xml 
			 user_define_1_SCCP-dictionary.utf-8.xml  
			 user_define_1_SCCP-dictionary.xml |
| Step 13 | Copy the language _tags_file and language _utf8_tags_file to the location of the
                                          			 other locale files (flash memory, slot 0, or TFTP server). Rename the files to
                                          			 user_define_ number _tags_file and user_define_ number _utf8_tags_file respectively, where number is 1
                                          			 to 5 and matches the user-defined directory. |
| Step 14 | Assign the
                                          			 locales to phones. See Configure Multiple Locales on SCCP Phones . |
| Step 15 | Use the create
                                                				  cnf-files command to rebuild the configuration files. |
| Step 16 | Use the reset command to reset the phones and see the localized displays. |

| Phone
                                                         						  Type | Code |
|---|---|
| 6921 | rtl |
| 6945 | rtl |
| 7906/7911 | tc |
| 7931 | gp |
| 7941/7961 | mk |
| 7970/7971 | td |
| 8941/8945 | gh |
| CIPC | ipc |

| Language | Language Code |
|---|---|
| Bulgarian | bg |
| Chinese | zh 3 |
| Croation | hr |
| Czech Republic | cs |
| Finnish | fi |
| Greek | el |
| Hungarian | hu |
| Korean | ko |
| Polish | pl |
| Portugese (Brazil) | pt |
| Romanian | ro |
| Serbian | sr |
| Slovakian | sk |
| Slovenian | sl |
| Turkish | tr |

| Note | On Cisco
                                                         				  3800 series routers, you must include /its in the directory name (flash:/its or
                                                         				  slot0:/its). For example, the TFTP alias for Chinese for the Cisco Unified IP
                                                         				  Phone 7970 is: Router(config)# tftp-server flash:/its/zh-td-sccp.jar alias user_define_1/td-sccp.jar |
|---|---|

| Tip | Cisco Unified CME 7.0(1) provides backward compatibility with the configuration method in Cisco Unified CME 4.3/7.0 and earlier
                                          versions. To use the same procedures as you used with earlier versions of Cisco Unified CME, see Install System-Defined Locales for Cisco Unified IP Phone 6921, 6945, 7906, 7911, 7921, 7931, 7941, 7961, 7970, 7971, and
                                             Cisco IP Communicator . |
|---|---|

| Restriction | When using an external TFTP server, you must manually create the user locale folders in the root directory. This is a limitation
                                                   of the TFTP server. Locale support is limited to phone firmware versions that are supported by Cisco Unified CME. User-defined locales are not supported on the Cisco Unified IP Phone 7920 or 7936. User-defined locales are not supported if the configuration file location is system. When you use the setup tool from the telephony-service setup command to provision phones, you can only choose a default user locale and network locale, and you are limited to selecting
                                                   a locale code that is supported in the system. You cannot use multiple locales or user-defined locales with the setup tool. When using a user-defined locale, the phone normally displays text using the user-defined fonts, except for any strings that
                                                   are interpreted by Cisco Unified CME, such as “Cisco/Personal Directory,” and “Speed Dial/Fast Dial.” If you install and configure a user-defined locale using country codes U1-U5 and then you install a new locale using the same
                                                   label, the phone retains the original language locale even after the phone is reset. This is a limitation of the IP phone.
                                                   To work around this limitation, you must configure the new package using a different country code. Each user-defined country code (U1-U5) can be used for only one user-locale-tag at a time. For example: Router(config-telephony)# user-locale 2 U2 load Finnish.pkg Router(config-telephony)# user-locale 1 U2 load Chinese.pkg LOCALE ERROR: User Defined Locale U2 already exists on locale index 2. |
|---|---|

| Step 1 | Go to http://www.cisco.com/cgi-bin/tablebuild.pl/CME-Locale . You must have
                                             				an account on Cisco.com to access the Software Download Center. If you do not
                                             				have an account or have forgotten your username or password, click the
                                             				appropriate button at the login dialog box and follow the instructions that
                                             				appear. |
|---|---|
| Step 2 | Navigate to Downloads
                                                				  Home > Products > Unified
                                                				  Communications > Call Control > Mid-Market Call Control > Cisco Unified
                                                				  Communications Manager Express > Unified Communications
                                                				  Manager Express Individual File Set and select your
                                          			 version of Cisco Unified CME. |
| Step 3 | Select the TAR
                                          			 file for the locale you want to install. Each TAR file contains locale files
                                          			 for a specific language and country and uses the following naming convention:
                                          			 CME-locale- language _ country - CMEversion Example: For example,
                                             				CME-locale-de_DE-7.0.1.0 is German for Germany for Cisco Unified CME 7.0(1). |
| Step 4 | Download the
                                          			 TAR file to the location previously specified by the cnf-file location command. Each file contains all the firmware required
                                          			 for all phone types supported by that version of Cisco Unified CME. If the
                                                				  cnf-file location is flash memory: Copy the TAR file to the flash:/its
                                                				  directory. If the
                                                				  cnf-file location is slot0: Copy the TAR file to the slot0:/its directory. If the cnf-file location is tftp: Create a folder in the root directory of the TFTP server for each locale using the following
                                                format and then copy the TAR file to the TFTP-Root folder. TFTP-Root / TAR-filename Example: For system-defined locales, use the locale folder name as shown in Table 1 . For example, create the folder for system-defined German as follows: TFTP-Root/de_DE-7.0.1.0.tar For up to five user-defined locales, use the User_Define_ n folder name as shown in Table 1 . A user-defined locale is a language other than the system-defined locales that are predefined in Cisco IOS software. For
                                                   example, create the folder for user-defined locale Chinese (User_Define_1) as follows: TFTP-Root/CME-locale-zh_CN-7.0.1.0.tar Note For a list of user-defined languages supported in Cisco Unified CME, see Cisco Unified CME Localization Matrix . Table 6. System-Defined and User-Defined Locales Language Locale Folder Name Country Code English English_United_States US English_United_Kingdom UK CA Danish Danish_Denmark DK Dutch Dutch_Netherlands NL French French_France FR CA German German_Germany DE AT CH Italian Italian_Italy IT Japanese 4 Japanese_Japan JP Norwegian Norwegian_Norway NO Portuguese Portuguese_Portugal PT Russian Russian_Russia RU Spanish Spanish_Spain ES Swedish Swedish_Sweden SE Un 5 User_Define_n 2 Un 2 4 Katakana is supported by Cisco Unified IP Phone 7905, 7912, 7940, and 7960. Kanji is supported by Cisco Unified IP Phone 7911,
                                                      7941, 7961, 7970, and 7971. 5 Where “n” is a number from 1 to 5. | Note | For a list of user-defined languages supported in Cisco Unified CME, see Cisco Unified CME Localization Matrix . | Language | Locale Folder Name | Country Code | English | English_United_States | US | English_United_Kingdom | UK | CA | Danish | Danish_Denmark | DK | Dutch | Dutch_Netherlands | NL | French | French_France | FR | CA | German | German_Germany | DE | AT | CH | Italian | Italian_Italy | IT | Japanese 4 | Japanese_Japan | JP | Norwegian | Norwegian_Norway | NO | Portuguese | Portuguese_Portugal | PT | Russian | Russian_Russia | RU | Spanish | Spanish_Spain | ES | Swedish | Swedish_Sweden | SE | Un 5 | User_Define_n 2 | Un 2 |
| Note | For a list of user-defined languages supported in Cisco Unified CME, see Cisco Unified CME Localization Matrix . |
| Language | Locale Folder Name | Country Code |
| English | English_United_States | US |
| English_United_Kingdom | UK |
| CA |
| Danish | Danish_Denmark | DK |
| Dutch | Dutch_Netherlands | NL |
| French | French_France | FR |
| CA |
| German | German_Germany | DE |
| AT |
| CH |
| Italian | Italian_Italy | IT |
| Japanese 4 | Japanese_Japan | JP |
| Norwegian | Norwegian_Norway | NO |
| Portuguese | Portuguese_Portugal | PT |
| Russian | Russian_Russia | RU |
| Spanish | Spanish_Spain | ES |
| Swedish | Swedish_Sweden | SE |
| Un 5 | User_Define_n 2 | Un 2 |
| Step 5 | Use the user-locale [ user-locale-tag ] country-code load TAR-filename command in telephony-service
                                          			 configuration mode to extract the contents of the TAR file. For country codes,
                                          			 see Table 1 . Example: For example,
                                             				to extract the contents of the CME-locale-zh_CN-7.0.1.0.tar file when U1 is the
                                             				country code for user-defined locale Chinese (User_Define_1), use this command: Router (telephony-service)# user-locale U1 load CME-locale-zh_CN-7.0.1.0.tar |
| Step 6 | Assign the
                                          			 locales to phones. See Configure Multiple Locales on SCCP Phones . |
| Step 7 | Use the create cnf-files command to rebuild the configuration files. |
| Step 8 | Use the reset command to reset the phones and see the localized displays. |

| Note | For a list of user-defined languages supported in Cisco Unified CME, see Cisco Unified CME Localization Matrix . |
|---|---|

| Language | Locale Folder Name | Country Code |
|---|---|---|
| English | English_United_States | US |
| English_United_Kingdom | UK |
| CA |
| Danish | Danish_Denmark | DK |
| Dutch | Dutch_Netherlands | NL |
| French | French_France | FR |
| CA |
| German | German_Germany | DE |
| AT |
| CH |
| Italian | Italian_Italy | IT |
| Japanese 4 | Japanese_Japan | JP |
| Norwegian | Norwegian_Norway | NO |
| Portuguese | Portuguese_Portugal | PT |
| Russian | Russian_Russia | RU |
| Spanish | Spanish_Spain | ES |
| Swedish | Swedish_Sweden | SE |
| Un 5 | User_Define_n 2 | Un 2 |

| Restriction | Multiple
                                                   				  user and network locales are not supported on the Cisco Unified IP Phone 7902G,
                                                   				  7910, 7910G, or 7920, or the Cisco Unified IP Conference Stations 7935
                                                   				  and 7936. When you use
                                                   				  the setup tool from the telephony-service
                                                         						setup command to provision phones, you can only choose a default
                                                   				  user locale and network locale and you must select a locale code that is
                                                   				  predefined in the system. You cannot use multiple or user-defined locales with
                                                   				  the setup tool. |
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
| Step 4 | user-locale [ user-locale-tag ] { [ user-defined-code ] country-code } Example: Router(config-telephony)# user-locale 1 U1 ZH | Specifies a
                                             				language for phone displays. user-locale-tag —Assigns a locale identifier to the
                                                   					 locale. Range is 0 to 4. Default: 0. This argument is required when defining
                                                   					 some locale other than the default (0). user-defined-code —(Optional) Assigns one of the
                                                   					 user-defined codes to the specified country code. Valid codes are U1 , U2 , U3 , U4 , and U5 . country-code —Type ? to display
                                                   					 a list of system-defined codes. Default: US (United States). You can assign any
                                                   					 valid ISO 639 code to a user-defined code (U1 to U5). |
| Step 5 | network-locale network-locale-tag [ user-defined-code ] country-code Example: Router(config-telephony)# network-locale 1 FR | Specifies a
                                             				country for tones and cadences. network-locale-tag —Assigns a locale identifier to
                                                   					 the country code. Range is 0 to 4. Default: 0. This argument is required when
                                                   					 defining some locale other than the default (0). user-defined-code —(Optional) Assigns one of the
                                                   					 user-defined codes to the specified country code. Valid codes are U1 , U2 , U3 , U4 , and U5 . country-code —Type ? to
                                                   					 display a list of system-defined codes. Default: US (United States). You can
                                                   					 assign any valid ISO 3166 code to a user-defined code (U1 to U5). |
| Step 6 | create
                                                				  cnf-files Example: Router(config-telephony)# create cnf-files | Builds the
                                             				required XML configuration files for IP phones. Use this command after you
                                             				update configuration file parameters such as the user locale or network locale. |
| Step 7 | exit Example: Router(config-telephony)# exit | Exits
                                             				telephony-service configuration mode. |
| Step 8 | ephone-template template-tag Example: Router(config)# ephone template 1 | Enters
                                             				ephone-template configuration mode. template-tag —Unique sequence number that
                                                   					 identifies this template during configuration tasks. |
| Step 9 | user-locale user-locale-tag Example: Router(config-ephone-template)# user-locale 2 | Assigns a
                                             				user locale to this ephone template. user-locale-tag —A locale tag that was created in Step 4 .
                                                   					 Range is 0 to 4. |
| Step 10 | network-locale network-locale-tag Example: Router(config-ephone-template)# network-locale 2 | Assigns a
                                             				network locale to this ephone template. network-locale-tag —A locale tag that was created
                                                   					 in Step 5 .
                                                   					 Range is 0 to 4. |
| Step 11 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 12 | ephone phone-tag Example: Router(config)# ephone 36 | Enters
                                             				ephone configuration mode. phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks. |
| Step 13 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 1 | Applies an
                                             				ephone template to an ephone. template-tag —Number of the template to apply to
                                                   					 this ephone. |
| Step 14 | exit Example: Router(config-ephone)# exit | Exits ephone
                                             				configuration mode. |
| Step 15 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 16 | reset { all [ time-interval ] \| cancel \| mac-address mac-address \| sequence-all } Example: Router(config-telephony)# reset all | Performs a complete reboot of all phones or the specified phone, including contacting the DHCP and TFTP servers for the latest
                                             configuration information. all —All phones in the Cisco Unified CME system. time-interval —(Optional) Time interval, in seconds, between each phone reset. Range is 0 to 60. Default is 15. cancel —Interrupts a sequential reset cycle that was started with a reset sequence-all command. mac-address mac-address —A specific phone. sequence-all —Resets all phones in strict one-at-a-time order by waiting for one phone to reregister before starting the reset for the
                                                   next phone. |
| Step 17 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Step 1 | Use the show telephony-service tftp-bindings command to display a list of configuration files that are accessible to IP
                                          			 phones using TFTP, including the dictionary, language, and tone configuration
                                          			 files. Example: Router(config)# show telephony-service tftp-bindings tftp-server system:/its/SEPDEFAULT.cnf
tftp-server system:/its/SEPDEFAULT.cnf alias SEPDefault.cnf
tftp-server system:/its/XMLDefault.cnf.xml alias XMLDefault.cnf.xml 
tftp-server system:/its/ATADefault.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEP00036B54BB15.cnf.xml 
tftp-server system:/its/germany/7960-font.xml alias German_Germany/7960-font.xml
tftp-server system:/its/germany/7960-dictionary.xml alias German_Germany/7960-dictionary.xml
tftp-server system:/its/germany/7960-kate.xml alias German_Germany/7960-kate.xml
tftp-server system:/its/germany/SCCP-dictionary.xml alias German_Germany/SCCP-dictionary.xml
tftp-server system:/its/germany/7960-tones.xml alias Germany/7960-tones.xml |
|---|---|
| Step 2 | Ensure that per-phone configuration files are defined with the cnf-file perphone command. |
| Step 3 | Use the show telephony-service ephone-template command to check the user locale and network locale settings in each ephone
                                          			 template. |
| Step 4 | Use the show telephony-service ephone command to
                                          			 check that the correct templates are applied to phones. |
| Step 5 | If the configuration file location is not TFTP, use the debug tftp events command to see which
                                          			 files Cisco Unified CME is looking for and whether the files are found and
                                          			 opened correctly. There are usually three states (“looking for x file,” “opened
                                          			 x file,” and “finished x file”). The file is found when all three states are
                                          			 displayed. For an external TFTP server you can use the logs from the TFTP
                                          			 server. |

| Restriction | Phone firmware, configuration files, and locale files must be in the same directory. |
|---|---|

| Step 1 | Go to http://www.cisco.com/cgi-bin/tablebuild.pl/CME-Locale . You must have
                                             				an account on Cisco.com to access the Software Download Center. If you do not
                                             				have an account or if you have forgotten your username or password, click the
                                             				appropriate button at the login dialog box and follow the instructions that
                                             				appear. |
|---|---|
| Step 2 | Navigate to Downloads
                                                				  Home > Products > Unified Communications > Call Control > Mid-Market Call
                                                				  Control > Cisco Unified Communications Manager
                                                				  Express > Unified Communications Manager Express Individual File
                                                				  Set and select your version of Cisco Unified CME. |
| Step 3 | Select the TAR
                                          			 file for the locale you want to install. Each TAR file contains locale files
                                          			 for a specific language and country and uses the following naming convention:
                                          			 CME-locale- language _ country - CMEversion Example: For example,
                                             				CME-locale-de_DE-8.6 is German for Germany for Cisco Unified CME 8.6. |
| Step 4 | Download the
                                          			 TAR file to a TFTP server that is accessible to the Cisco Unified CME router.
                                          			 Each file contains all the firmware required for all phone types supported by
                                          			 that version of Cisco Unified CME. |
| Step 5 | Use the archive tar command to extract the files to flash memory, slot 0, or an external TFTP
                                          			 server. Example: Router# archive tar /xtract source-url flash: /file-url For example,
                                             				to extract the contents of CME-locale-de_DE-8.6.tar from TFTP server
                                             				192.168.1.1 to router flash memory, use this command: Router# archive tar /xtract tftp://192.168.1.1/cme-locale-de_DE-8.6.tar flash: |
| Step 6 | See Table 1 and Table 2 for a description of the codes used in the filenames and the list of supported
                                          			 directory names. Each phone type has a JAR file that uses the following naming convention: language - phone -sip.jar Example: For example, de-gh-sip.jar is for German on the Cisco Unified IP Phone 8961. Each TAR file also includes the file g4-tones.xml for country-specific network tones and cadences. Table 7. Phone-Type Codes for Locale JAR Files Phone Type Phone Code 3905 cin 6941 rtl 6945 rtl 8961 gh 9951 gd 9971 gd Table 8. System-Defined User and Network Locales Language Language Code User-Locale Directory Name Country Code Network-Locale Directory Name English en English_United_States 6 US United_States English_United_Kingdom UK United_Kingdom GB United_Kingdom CA Canada AU Australia Danish dk Danish_Denmark DK Denmark Dutch nl Dutch_Netherlands NL Netherlands French fr French_France FR France CA Canada German de German_Germany DE Germany AT Austria CH Switzerland Italian it Italian_Italy IT Italy Japanese jp Japanese_Japan JP Japan Norwegian no Norwegian_Norway NO Norway Portuguese pt Portuguese_Portugal PT Portugal Russian ru Russian_Russia RU Russian_Federation Spanish es Spanish_Spain ES Spain Swedish se Swedish_Sweden SE Sweden 6 English for the United States is the default language. You do not need to install the JAR file for U.S. English unless you
                                                assign a different language to a phone and then want to reassign English. | Phone Type | Phone Code | 3905 | cin | 6941 | rtl | 6945 | rtl | 8961 | gh | 9951 | gd | 9971 | gd | Language | Language Code | User-Locale Directory Name | Country Code | Network-Locale Directory Name | English | en | English_United_States 6 | US | United_States | English_United_Kingdom | UK | United_Kingdom | GB | United_Kingdom | CA | Canada | AU | Australia | Danish | dk | Danish_Denmark | DK | Denmark | Dutch | nl | Dutch_Netherlands | NL | Netherlands | French | fr | French_France | FR | France | CA | Canada | German | de | German_Germany | DE | Germany | AT | Austria | CH | Switzerland | Italian | it | Italian_Italy | IT | Italy | Japanese | jp | Japanese_Japan | JP | Japan | Norwegian | no | Norwegian_Norway | NO | Norway | Portuguese | pt | Portuguese_Portugal | PT | Portugal | Russian | ru | Russian_Russia | RU | Russian_Federation | Spanish | es | Spanish_Spain | ES | Spain | Swedish | se | Swedish_Sweden | SE | Sweden |
| Phone Type | Phone Code |
| 3905 | cin |
| 6941 | rtl |
| 6945 | rtl |
| 8961 | gh |
| 9951 | gd |
| 9971 | gd |
| Language | Language Code | User-Locale Directory Name | Country Code | Network-Locale Directory Name |
| English | en | English_United_States 6 | US | United_States |
| English_United_Kingdom | UK | United_Kingdom |
| GB | United_Kingdom |
| CA | Canada |
| AU | Australia |
| Danish | dk | Danish_Denmark | DK | Denmark |
| Dutch | nl | Dutch_Netherlands | NL | Netherlands |
| French | fr | French_France | FR | France |
| CA | Canada |
| German | de | German_Germany | DE | Germany |
| AT | Austria |
| CH | Switzerland |
| Italian | it | Italian_Italy | IT | Italy |
| Japanese | jp | Japanese_Japan | JP | Japan |
| Norwegian | no | Norwegian_Norway | NO | Norway |
| Portuguese | pt | Portuguese_Portugal | PT | Portugal |
| Russian | ru | Russian_Russia | RU | Russian_Federation |
| Spanish | es | Spanish_Spain | ES | Spain |
| Swedish | se | Swedish_Sweden | SE | Sweden |
| Step 7 | If you store
                                          			 the locale files in flash memory or slot 0 on the Cisco Unified CME router,
                                          			 create a TFTP alias for the user locale (text displays) and network locale
                                          			 (tones) using this format: Example: Router(config)# tftp-server flash:/ jar_file alias directory_name /gh-sip.jar Router(config)# tftp-server flash:/g4-tones.xml alias directory_name /g4-tones.xml Use the
                                             				appropriate directory name shown in Table 1 and remove the two-letter language code from the JAR file name. For example,
                                             				the TFTP aliases for German and Germany for the Cisco Unified IP Phone 8961
                                             				are: Router(config)# tftp-server flash:/de-gh-sip.jar alias German_Germany/ Router(config)# tftp-server flash:/g4-tones.xml alias Germany/g4-tones.xml |
| Step 8 | If you store
                                          			 the locale files on an external TFTP server, create a directory under the TFTP
                                          			 root directory for each user and network locale. Use the
                                             				appropriate directory name shown in Table 1 and remove the two-letter language code from the JAR file name. Example: For example,
                                             				the user-locale directory for German and the network-locale directory for
                                             				Germany for the Cisco Unified IP Phone 8961 are: TFTP-Root/German_Germany/gh-sip.jar
                                             				TFTP-Root/Germany/g4-tones.xml |
| Step 9 | Assign the
                                          			 locales to the phones. To set a default locale for all phones, use the user-locale and network-locale commands in voice register global
                                          			 configuration mode. |
| Step 10 | To support
                                          			 more than one user or network locale, see Verify Multiple Locales on SIP Phones . |
| Step 11 | Use the create
                                                				  profile command to rebuild the configuration files. |
| Step 12 | Use the reset command to reset the phones and see the localized displays. |

| Phone Type | Phone Code |
|---|---|
| 3905 | cin |
| 6941 | rtl |
| 6945 | rtl |
| 8961 | gh |
| 9951 | gd |
| 9971 | gd |

| Language | Language Code | User-Locale Directory Name | Country Code | Network-Locale Directory Name |
|---|---|---|---|---|
| English | en | English_United_States 6 | US | United_States |
| English_United_Kingdom | UK | United_Kingdom |
| GB | United_Kingdom |
| CA | Canada |
| AU | Australia |
| Danish | dk | Danish_Denmark | DK | Denmark |
| Dutch | nl | Dutch_Netherlands | NL | Netherlands |
| French | fr | French_France | FR | France |
| CA | Canada |
| German | de | German_Germany | DE | Germany |
| AT | Austria |
| CH | Switzerland |
| Italian | it | Italian_Italy | IT | Italy |
| Japanese | jp | Japanese_Japan | JP | Japan |
| Norwegian | no | Norwegian_Norway | NO | Norway |
| Portuguese | pt | Portuguese_Portugal | PT | Portugal |
| Russian | ru | Russian_Russia | RU | Russian_Federation |
| Spanish | es | Spanish_Spain | ES | Spain |
| Swedish | se | Swedish_Sweden | SE | Sweden |

| Restriction | When using
                                                   				  an external TFTP server, you must manually create the user locale folders in
                                                   				  the root directory. This is a limitation of the TFTP server. Locale
                                                   				  support is limited to phone firmware versions that are supported by
                                                   				  Cisco Unified CME. User-defined
                                                   				  locales are not supported if the configuration file location is “system:”. If you
                                                   				  install and configure a user-defined locale using country codes U1-U5 and then
                                                   				  you install a new locale using the same label, the phone retains the original
                                                   				  language locale even after the phone is reset. This is a limitation of the IP
                                                   				  phone. To work around this limitation, you must configure the new package using
                                                   				  a different country code. Each
                                                   				  user-defined country code (U1-U5) can be used for only one user-locale-tag at a
                                                   				  time. For example: Router(config-register-global)# user-locale 2 U2 load Finnish.pkg Router(config-register-global)# user-locale 1 U2 load Chinese.pkg LOCALE ERROR: User Defined Locale U2 already exists on locale index 2. |
|---|---|

| Step 1 | Go to http://www.cisco.com/cgi-bin/tablebuild.pl/CME-Locale You must have
                                             				an account on Cisco.com to access the Software Download Center. If you do not
                                             				have an account or have forgotten your username or password, click the
                                             				appropriate button at the login dialog box and follow the instructions that
                                             				appear. |
|---|---|
| Step 2 | Navigate to Downloads
                                                				  Home > Products > Unified
                                                				  Communications > Call Control > Mid-Market Call
                                                				  Control > Cisco Unified Communications Manager
                                                				  Express > Unified Communications Manager Express Individual File
                                                				  Set and select your version of Cisco Unified CME. |
| Step 3 | Select the TAR
                                          			 file for the locale you want to install. Each TAR file contains locale files
                                          			 for a specific language and country and uses the following naming convention:
                                          			 CME-locale- language _ country - CMEversion .tar Example: For example,
                                             				CME-locale-de_DE-German-8.6.3.0.tar is German for Germany for Cisco Unified
                                             				CME 9.0. |
| Step 4 | Download the
                                          			 TAR file to the location previously specified by the cnf-file location command. Each file contains all the firmware required
                                          			 for all phone types supported by that version of Cisco Unified CME. With the
                                             				locale installer, you do not need to perform manual configuration. Instead, you
                                             				copy the locale file using the copy command
                                             				in privileged EXEC configuration mode. Note You must
                                                         				  copy the locale file into the /its directory (flash:/its or slot0:/its) when
                                                         				  you store the locale files on the Cisco Unified CME router. If the
                                                				  cnf-file location is flash memory: Copy the TAR file to the flash:/its
                                                				  directory. Example: For
                                                   					 example, Router# copy tftp://12.1.1.100/CME-locale-de_DE-German-8.6.3.0.tar flash:/its If the
                                                				  cnf-file location is slot0: Copy the TAR file to the slot0:/its directory. If the
                                                				  cnf-file location is tftp: Create a folder in the root directory of the TFTP
                                                				  server for each locale using the following format and then copy the TAR file to
                                                				  the TFTP-Root folder. Example: TFTP-Root / TAR-filename For
                                                   					 system-defined locales, use the locale folder name as shown in Table 1 .
                                                   					 For example, create the folder for system-defined German as follows: TFTP-Root/de_DE-8.6.3.0.tar For up
                                                   					 to five user-defined locales, use the User_Define_ n folder
                                                   					 name as shown in Table 1 .
                                                   					 A user-defined locale is a language other than the system-defined locales that
                                                   					 are predefined in Cisco IOS software. For example, create the folder for
                                                   					 user-defined locale Chinese (User_Define_1) as follows: TFTP-Root/CME-locale-zh_CN-Chinese-8.6.3.0.tar Note For
                                                            					 a list of user-defined languages supported in Cisco Unified CME, see
                                                            					 Cisco Unified CME Localization Matrix. Table 9. System-Defined and User-Defined Locales Language Locale Folder Name Country Code English English_United_States US English_United_Kingdom UK CA Danish Danish_Denmark DK Dutch Dutch_Netherlands NL French French_France FR CA German German_Germany DE AT CH Italian Italian_Italy IT Japanese Japanese_Japan JP Norwegian Norwegian_Norway NO Portuguese Portuguese_Portugal PT Russian Russian_Russia RU Spanish Spanish_Spain ES Swedish Swedish_Sweden SE Un 7 User_Define_n 1 Un 1 7 Where “n” is a number from 1 to 5. | Note | You must
                                                         				  copy the locale file into the /its directory (flash:/its or slot0:/its) when
                                                         				  you store the locale files on the Cisco Unified CME router. | Note | For
                                                            					 a list of user-defined languages supported in Cisco Unified CME, see
                                                            					 Cisco Unified CME Localization Matrix. | Language | Locale Folder Name | Country Code | English | English_United_States | US | English_United_Kingdom | UK | CA | Danish | Danish_Denmark | DK | Dutch | Dutch_Netherlands | NL | French | French_France | FR | CA | German | German_Germany | DE | AT | CH | Italian | Italian_Italy | IT | Japanese | Japanese_Japan | JP | Norwegian | Norwegian_Norway | NO | Portuguese | Portuguese_Portugal | PT | Russian | Russian_Russia | RU | Spanish | Spanish_Spain | ES | Swedish | Swedish_Sweden | SE | Un 7 | User_Define_n 1 | Un 1 |
| Note | You must
                                                         				  copy the locale file into the /its directory (flash:/its or slot0:/its) when
                                                         				  you store the locale files on the Cisco Unified CME router. |
| Note | For
                                                            					 a list of user-defined languages supported in Cisco Unified CME, see
                                                            					 Cisco Unified CME Localization Matrix. |
| Language | Locale Folder Name | Country Code |
| English | English_United_States | US |
| English_United_Kingdom | UK |
| CA |
| Danish | Danish_Denmark | DK |
| Dutch | Dutch_Netherlands | NL |
| French | French_France | FR |
| CA |
| German | German_Germany | DE |
| AT |
| CH |
| Italian | Italian_Italy | IT |
| Japanese | Japanese_Japan | JP |
| Norwegian | Norwegian_Norway | NO |
| Portuguese | Portuguese_Portugal | PT |
| Russian | Russian_Russia | RU |
| Spanish | Spanish_Spain | ES |
| Swedish | Swedish_Sweden | SE |
| Un 7 | User_Define_n 1 | Un 1 |
| Step 5 | Use the user-locale [ user-locale-tag ] {[user-defined-code] country-code } [ load TAR-filename ] command in voice register global configuration mode
                                          			 to extract the contents of the TAR file. For country codes, see Table 1 . Note Use the
                                                         				  complete filename, including the file suffix (.tar), when you configure the user-locale command for all Cisco Unified SIP IP phone types. Example: For example,
                                             				to extract the contents of the CME-locale-zh_CN-Chinese-8.6.3.0.tar file when
                                             				U1 is the country code for user-defined locale Chinese (User_Define_1), use
                                             				this command: Router(config-register-global)# user-locale U1 load CME-locale-zh_CN-Chinese-8.6.3.0.tar | Note | Use the
                                                         				  complete filename, including the file suffix (.tar), when you configure the user-locale command for all Cisco Unified SIP IP phone types. |
| Note | Use the
                                                         				  complete filename, including the file suffix (.tar), when you configure the user-locale command for all Cisco Unified SIP IP phone types. |
| Step 6 | Assign the
                                          			 locales to the phones. See Configure Multiple Locales on SIP Phones . |
| Step 7 | Use the create
                                                				  profile command in voice register global configuration mode to
                                          			 generate the configuration profile files required for Cisco Unified SIP IP
                                          			 phones. |
| Step 8 | Use the reset command to reset the phones and see the localized displays. |

| Note | You must
                                                         				  copy the locale file into the /its directory (flash:/its or slot0:/its) when
                                                         				  you store the locale files on the Cisco Unified CME router. |
|---|---|

| Note | For
                                                            					 a list of user-defined languages supported in Cisco Unified CME, see
                                                            					 Cisco Unified CME Localization Matrix. |
|---|---|

| Language | Locale Folder Name | Country Code |
|---|---|---|
| English | English_United_States | US |
| English_United_Kingdom | UK |
| CA |
| Danish | Danish_Denmark | DK |
| Dutch | Dutch_Netherlands | NL |
| French | French_France | FR |
| CA |
| German | German_Germany | DE |
| AT |
| CH |
| Italian | Italian_Italy | IT |
| Japanese | Japanese_Japan | JP |
| Norwegian | Norwegian_Norway | NO |
| Portuguese | Portuguese_Portugal | PT |
| Russian | Russian_Russia | RU |
| Spanish | Spanish_Spain | ES |
| Swedish | Swedish_Sweden | SE |
| Un 7 | User_Define_n 1 | Un 1 |

| Note | Use the
                                                         				  complete filename, including the file suffix (.tar), when you configure the user-locale command for all Cisco Unified SIP IP phone types. |
|---|---|

| Restriction | Multiple
                                                   				  user and network locales are supported only on Cisco Unified IP Phone 8961,
                                                   				  9951, and 9971. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)#voice register global | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. |
| Step 4 | user-locale [ user-locale-tag ] { [ user-defined-code ] country-code } Example: Router(config-register-global)# user-locale 1 DE | Specifies a
                                             				language for phone displays. user-locale-tag —Assigns a locale identifier to the
                                                   					 locale. Range is 0 to 4. Default: 0. This argument is required when defining
                                                   					 some locale other than the default (0). country-code —Type ? to display
                                                   					 a list of system-defined codes. Default: US (United States). |
| Step 5 | network-locale network-locale-tag [ user-defined-code ] country-code Example: Router(config-register-global)# network-locale 1 FR | Specifies a
                                             				country for tones and cadences. network-locale-tag —Assigns a locale identifier to
                                                   					 the country code. Range is 0 to 4. Default: 0. This argument is required when
                                                   					 defining some locale other than the default (0). country-code —Type ? to display
                                                   					 a list of system-defined codes. Default: US (United States). You can assign any
                                                   					 valid ISO 3166 code to a user-defined code (U1 to U5). |
| Step 6 | create profile Example: Router(config-register-global)# create profile | Generates
                                             				provisioning files required for SIP phones and writes the file to the location
                                             				specified with the tftp-path command. |
| Step 7 | exit Example: Router(config-telephony)# exit | Exits voice
                                             				register global configuration mode. |
| Step 8 | voice register template template-tag Example: Router(config)voice register template 10 | Enters voice
                                             				register template configuration mode to define a template of common parameters
                                             				for SIP phones in Cisco Unified CME. Range— 1
                                                   					 to 10. |
| Step 9 | user-locale user-locale-tag Example: Router(config-ephone-template)# user-locale 2 | Assigns a
                                             				user locale to this ephone template. user-locale-tag —A locale tag that was created in Step 4 .
                                                   					 Range is 0 to 4. |
| Step 10 | network-locale network-locale-tag Example: Router(config-ephone-template)# network-locale 2 | Assigns a
                                             				network locale to this ephone template. network-locale-tag —A locale tag that was created
                                                   					 in Step 5 .
                                                   					 Range is 0 to 4. |
| Step 11 | exit Example: Router(config-ephone-template)# exit | Exits voice
                                             				register template configuration mode. |
| Step 12 | voice register pool pool-tag Example: Router(config)#voice register pool 5 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. |
| Step 13 | voice register template template-tag Example: Router(config)voice register template 10 | Enters voice
                                             				register template configuration mode to define a template of common parameters
                                             				for SIP phones in Cisco Unified CME. Range— 1
                                                   					 to 10. |
| Step 14 | exit Example: Router(config-ephone)# exit | Exits voice
                                             				register template configuration mode. |
| Step 15 | voice register
                                                				  global Example: Router(config)#voice register global | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. |
| Step 16 | reset Example: Router(config-register-global)# reset | Performs a
                                             				complete reboot of all phones or the specified phone, including contacting the
                                             				DHCP and TFTP servers for the latest configuration information. |
| Step 17 | end Example: Router(config-register-global)# end | Returns to
                                             				privileged EXEC mode. |

| Step 1 | Use the show voice register tftp-bind command to
                                          			 display a list of configuration files that are accessible to IP phones using
                                          			 TFTP, including the dictionary, language, and tone configuration files. Example: Router#sh voice register tftp-bind tftp-server syncinfo.xml url system:/cme/sipphone/syncinfo.xml
			 tftp-server SIPDefault.cnf url system:/cme/sipphone/SIPDefault.cnf
			 tftp-server softkeyDefault_kpml.xml url system:/cme/sipphone/softkeyDefault_kpml
			 .xml
			 tftp-server softkeyDefault.xml url system:/cme/sipphone/softkeyDefault.xml
			 tftp-server softkey2_kpml.xml url system:/cme/sipphone/softkey2_kpml.xml
			 tftp-server softkey2.xml url system:/cme/sipphone/softkey2.xml
			 tftp-server featurePolicyDefault.xml url system:/cme/sipphone/featurePolicyDefau
			 lt.xml
			 tftp-server featurePolicy2.xml url system:/cme/sipphone/featurePolicy2.xml
			 tftp-server SEPACA016FDC1BD.cnf.xml url system:/cme/sipphone/SEPACA016FDC1BD.cnf
			 .xml |
|---|---|
| Step 2 | Use the show voice register template all command to
                                          			 check the user locale and network locale settings in each ephone template. |
| Step 3 | Use the show voice register pool all command to
                                          			 check that the correct templates are applied to phones. |
| Step 4 | If the configuration file location is not TFTP, use the debug tftp events command to see which
                                          			 files Cisco Unified CME is looking for and whether the files are found and
                                          			 opened correctly. There are usually three states (“looking for x file,” “opened
                                          			 x file,” and “finished x file”). The file is found when all three states are
                                          			 displayed. For an external TFTP server, you can use the logs from the TFTP
                                          			 server. |

| Feature Name | Cisco Unified CME Version | Feature
                                       				  Information |
|---|---|---|
| Localization
                                       				  Enhancements for Cisco Unified SIP IP Phones | 10.5 | Cisco
                                       				  Unified CME 10.5 provides support for additional languages. |
| Localization
                                       				  Enhancements for Cisco Unified SIP IP Phones | 9.0 | Provides the
                                       				  following enhanced localization support for Cisco Unified SIP IP phones: Localization support for Cisco Unified 6941 and 6945 SIP IP
                                             						Phones. Locale
                                             						installer that supports a single procedure for all Cisco Unified SIP IP phones. |
| Localization
                                       				  Enhancement | 8.8 | Adds
                                       				  localization support for Cisco Unified 3905 SIP and Cisco Unified 6945, 8941,
                                       				  and 8945 SCCP IP Phones. |
| Usability
                                       				  Enhancement | 8.6 | Adds
                                       				  localization support for SIP IP Phones. |
| Cisco Unified CME Usability Enhancement | 7.0(1) | Locale
                                             						installer that supports a single procedure for all SCCP IP phones. Parses
                                             						firmware-load text files and automatically creates the required TFTP aliases
                                             						for localization. Backward
                                             						compatibility with the configuration method in Cisco Unified CME 7.0 and
                                             						earlier versions. |
| Multiple
                                       				  Locales | 4.0 | Multiple
                                       				  user and network locales were introduced. |
| User-Defined
                                       				  Locales | 4.0 | User-defined
                                       				  locales were introduced. |