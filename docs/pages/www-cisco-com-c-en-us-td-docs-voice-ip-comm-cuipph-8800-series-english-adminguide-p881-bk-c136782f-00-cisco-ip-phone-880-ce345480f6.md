---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-english-adminguide-p881-bk-c136782f-00-cisco-ip-phone-880-ce345480f6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/english/adminguide/P881_BK_C136782F_00_cisco-ip-phone-8800_series/P881_BK_C136782F_00_cisco-ip-phone-8811-8841_chapter_010000.html
retrieved_at: 2026-08-21T09:49:36.091227+00:00
---

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

Updated: November 6, 2025

Chapter: International User Support

## Chapter: International User Support

# International User Support

## Unified
                        	 Communications Manager Endpoints Locale Installer

By default, Cisco IP Phones are set up for the English (United States) locale. To use the Cisco IP Phones in other locales,
                              you must install the locale-specific version of the Unified Communications Manager Endpoints Locale Installer on every Cisco Unified
                                 				Communications Manager server in the cluster. The Locale Installer installs the latest translated text for the phone user interface and country-specific
                              phone tones on your system so that they are available for the Cisco IP Phones.

To access the Locale Installer required for a release, access the Software Download page, navigate to your phone model, and select the Unified Communications Manager Endpoints Locale Installer link.

For more information, see the documentation for your particular Cisco Unified
                                 				Communications Manager release.

The latest
                                          			 Locale Installer may not be immediately available; continue to check the
                                          			 website for updates.

## International Call Logging Support

If your phone system is configured for international call logging (calling party normalization), the call logs, redial, or
                              call directory entries may display a plus (+) symbol to represent the international escape code for your location. Depending
                              on the configuration for your phone system, the + may be replaced with the correct international dialing code, or you may
                              need to edit the number before dialing to manually replace the + with the international escape code for your location. In
                              addition, while the call log or directory entry may display the full international number for the received call, the phone
                              display may show the shortened local version of the number, without international or country codes.

## Language Limitation

There is no localized Keyboard
                              Alphanumeric Text Entry (KATE) support for the following Asian
                              locales:

Chinese (Hong Kong)

Chinese (Taiwan)

Japanese (Japan)

Korean (Korea Republic)

The default English (United States) KATE is presented to the user instead.

For example, the phone screen will show text in Korean, but the 2 key on the keypad will display a b c 2 A B C .

Chinese input works similar to PCs and mobile phones in Chinese. The Chinese locale installer is required for Chinese input
                              to function.

| Note | The latest
                                          			 Locale Installer may not be immediately available; continue to check the
                                          			 website for updates. |
|---|---|