---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7832-english-adminguide-cs78-b-conference-7832-admin-guide-cucm-cs78--19c7597130
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7832/english/adminguide/cs78_b_conference-7832-admin-guide-cucm/cs78_b_conference-7832-admin-guide-cucm_chapter_01100.html
retrieved_at: 2026-08-21T13:27:48.913571+00:00
---

Cisco IP Conference Phone 7832 Administration Guide for Cisco Unified Communication Manager

# Cisco IP Conference Phone 7832 Administration Guide for Cisco Unified Communication Manager

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

Chinese (China)

Chinese (Hong Kong)

Chinese (Taiwan)

Japanese (Japan)

Korean (Korea Republic)

The default English (United States) KATE is presented to the user instead.

For example, the phone screen will show text in Korean, but the 2 key on the keypad will display a b c 2 A B C .

| Note | The latest
                                          			 Locale Installer may not be immediately available; continue to check the
                                          			 website for updates. |
|---|---|