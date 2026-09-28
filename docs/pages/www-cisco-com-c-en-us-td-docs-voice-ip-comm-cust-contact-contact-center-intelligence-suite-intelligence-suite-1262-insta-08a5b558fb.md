---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1262-insta-08a5b558fb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1262/install/guide/cuic_b_install-and-upgrade-guide-1262/cuic_m_language-pack-for-cuic-1261.html
retrieved_at: 2026-08-21T16:14:46.162239+00:00
---

Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 12.6(2)

# Installation and Upgrade Guide for Cisco Unified Intelligence Center, Release 12.6(2)

Updated: April 28, 2023

Chapter: Language Pack for Unified Intelligence Center

## Chapter: Language Pack for Unified Intelligence Center

- Language Pack for Unified Intelligence Center

- Install Language Pack

# Language Pack for Unified Intelligence Center

## Install Language Pack

Post successful install or upgrade, if you want to use the Cisco Unified Intelligence Center interface in a language other than English, you have to download and install the language pack COP.

The language pack for Cisco Unified Intelligence Center is delivered as a single Cisco Option Package (COP) file. The file is available to download from Cisco.com and contains a
                              single installer for all language variants.

You can download the language pack for Cisco Unified Intelligence Center at:

https://software.cisco.com/download/home/282163829/type/282377062/release/12.6(1)

COP files can generally be installed on an active, running system. However, language COP files cannot be removed or rolled
                              back.

Step 1

Download the Cisco Unified Intelligence Center Language Pack COP file from the Cisco Software site to a local source or an SFTP server that can be accessed by the Cisco Unified Intelligence Center server.

Step 2

Use SSH to log in to your Cisco Unified Intelligence Center system with the platform administration account.

Step 3

Use the CLI to run the command utils system upgrade initiate .

Step 4

Follow the instructions provided by the utils system upgrade initiate command.

Step 5

Reboot the server.

Step 6

Repeat step 2 through step 5 on the secondary Cisco Unified Intelligence Center server.

Step 7

When the installation is complete on both Cisco Unified Intelligence Center servers, and all Cisco Unified Intelligence Center users must clear their browser cache and cookies.

| Step 1 | Download the Cisco Unified Intelligence Center Language Pack COP file from the Cisco Software site to a local source or an SFTP server that can be accessed by the Cisco Unified Intelligence Center server. |
|---|---|
| Step 2 | Use SSH to log in to your Cisco Unified Intelligence Center system with the platform administration account. |
| Step 3 | Use the CLI to run the command utils system upgrade initiate . |
| Step 4 | Follow the instructions provided by the utils system upgrade initiate command. |
| Step 5 | Reboot the server. |
| Step 6 | Repeat step 2 through step 5 on the secondary Cisco Unified Intelligence Center server. |
| Step 7 | When the installation is complete on both Cisco Unified Intelligence Center servers, and all Cisco Unified Intelligence Center users must clear their browser cache and cookies. |