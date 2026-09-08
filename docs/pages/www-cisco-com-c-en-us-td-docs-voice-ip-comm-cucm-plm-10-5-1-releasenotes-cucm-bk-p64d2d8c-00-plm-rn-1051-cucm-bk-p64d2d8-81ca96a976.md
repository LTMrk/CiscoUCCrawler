---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-10-5-1-releasenotes-cucm-bk-p64d2d8c-00-plm-rn-1051-cucm-bk-p64d2d8-81ca96a976
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/10_5_1/releasenotes/CUCM_BK_P64D2D8C_00_plm-rn-1051/CUCM_BK_P64D2D8C_00_plm-rn-1051_chapter_011.html
retrieved_at: 2026-09-08T04:53:18.664001+00:00
---

Release Notes for Cisco Prime License Manager Release 10.5(1)

# Release Notes for Cisco Prime License Manager Release 10.5(1)

## Results

Updated: July 15, 2014

Chapter: Caveats

## Chapter: Caveats

- Bug Search	 Tool

- Resolved	 Caveats

- Open Caveats for Cisco Prime License Manager Release 10.5(1)

# Caveats

## Bug Search
	 Tool

- All severity level
			 1 or 2 bugs

- Significant
			 severity level 3 bugs

- All customer-found
			 bugs

You can
		search for problems by using the Cisco Bug Search tool.

- Internet
			 connection

- Web browser

- Cisco.com user ID
			 and password

Follow these
		steps to use Bug Search:

- Access Bug Search.

- Log in with your
			 Cisco.com user ID and password.

- If you are looking
			 for information about a specific problem, enter the bug ID number in the Search
				for: field, and click Go .

Click Help on the Bug Search page for information about
		  how to search for bugs, create saved searches, and create bug groups.

## Resolved
	 Caveats

You can find the latest resolved caveat information for
		  Cisco Prime License Manager by using the Bug Search tool, an online tool
		  available for customers to query defects according to their own needs.

You need an account with Cisco.com to use the Bug Search tool to
			 find open and resolved caveats of any severity for any release.

See https:/​/​tools.cisco.com/​bugsearch/​ .

## Open Caveats for Cisco Prime License Manager Release 10.5(1)

3

prime_lm

Unable to modify hostname or domain name in standalone Cisco Prime License Manager

Perform one of the following steps:

- Modify the hostname or domain name prior to performing an upgrade from standalone Cisco Enterprise License Manager to standalone Cisco Prime License Manager.

- Use a co-resident Cisco Prime License Manager install instead of a standalone  install.

- Reinstall the server with the modified settings and request a rehost of the license files.

3

prime_lm

Cisco Prime License Manager should provide warning when pre-9 PAK is used

If the PAK is not supported by Cisco Prime License Manager , the administrator will not be able to select the number of licenses to fulfill. There is no workaround.

3

prime_lm

Cisco Prime License Manager should warn customer about potential DR failure

- Comply with the more complex password policy by resetting your password using the set password user security command

- Create a new DR backup.

3

prime_lm

Standalone Cisco Prime License Manager CLI login banner unchangeable after Enterprise License Manager upgrade

There is no workaround.

3

prime_lm

Enterprise License Manager DB fails to start - PID created in wrong directory

The Cisco Enterprise License Manager database shows as not running in the CLI and GUI, however this is incorrect. The Cisco Enterprise License Manager database and Cisco Enterprise License Manager are fully functional.

You can correct the display by performing the following steps:

- Log in to the system using a remote account.

- Enter the following: < Is /etc/init.d/ # . Search for a file with the format of postgresql-x.x, where x.x is the release, such as 9.1 or 9.2.

- Enter the following: > touch /var/lock/subsys/postgresql-x.x , where x.x is the release found above.

- Enter the following: > su - <your_admin_account_name>

- In the CLI, execute the following command to restart the ELM DB: utils service restart Cisco Prime LM DB .

3

prime_lm

Cisco Prime License Manager - Sync fails for IPv6 product instance if added using IP address

When adding the IPv6 product instance, use the hostname or place brackets [ ] around the IP address.

| Tip | Click Help on the Bug Search page for information about
		  how to search for bugs, create saved searches, and create bug groups. |
|---|---|

| Tip | You need an account with Cisco.com to use the Bug Search tool to
			 find open and resolved caveats of any severity for any release. |
|---|---|

| Identifier | Severity | Product | Headline | Workaround |
|---|---|---|---|---|
| CSCun22103 | 3 | prime_lm | Unable to modify hostname or domain name in standalone Cisco Prime License Manager | Perform one of the following steps: Modify the hostname or domain name prior to performing an upgrade from standalone Cisco Enterprise License Manager to standalone Cisco Prime License Manager. Use a co-resident Cisco Prime License Manager install instead of a standalone  install. Reinstall the server with the modified settings and request a rehost of the license files. |
| CSCuo13153 | 3 | prime_lm | Cisco Prime License Manager should provide warning when pre-9 PAK is used | If the PAK is not supported by Cisco Prime License Manager , the administrator will not be able to select the number of licenses to fulfill. There is no workaround. |
| CSCun40442 | 3 | prime_lm | Cisco Prime License Manager should warn customer about potential DR failure | Comply with the more complex password policy by resetting your password using the set password user security command Create a new DR backup. |
| CSCum89149 | 3 | prime_lm | Standalone Cisco Prime License Manager CLI login banner unchangeable after Enterprise License Manager upgrade | There is no workaround. |
| CSCun77018 | 3 | prime_lm | Enterprise License Manager DB fails to start - PID created in wrong directory | The Cisco Enterprise License Manager database shows as not running in the CLI and GUI, however this is incorrect. The Cisco Enterprise License Manager database and Cisco Enterprise License Manager are fully functional. You can correct the display by performing the following steps: Log in to the system using a remote account. Enter the following: < Is /etc/init.d/ # . Search for a file with the format of postgresql-x.x, where x.x is the release, such as 9.1 or 9.2. Enter the following: > touch /var/lock/subsys/postgresql-x.x , where x.x is the release found above. Enter the following: > su - <your_admin_account_name> In the CLI, execute the following command to restart the ELM DB: utils service restart Cisco Prime LM DB . |
| CSCuo35143 | 3 | prime_lm | Cisco Prime License Manager - Sync fails for IPv6 product instance if added using IP address | When adding the IPv6 product instance, use the hostname or place brackets [ ] around the IP address. |