---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8832-english-adminguide-cs88-b-conference-8832-admin-guide-cucm-cs88--80aeea3ef5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8832/english/adminguide/cs88_b_conference-8832-admin-guide-cucm/cs88_b_conference-8832-admin-guide-cucm_chapter_01100.html
retrieved_at: 2026-08-21T13:37:24.397526+00:00
---

Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

# Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

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