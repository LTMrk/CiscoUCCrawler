---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-administrat-babf131399
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/administration/guide/ucce_b_administration-guide-for-cisco-unified_1261/ucce_b_administration-guide-for-cisco-unified_1261_chapter_0101.html
retrieved_at: 2026-08-16T20:46:28.879693+00:00
---

Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.6(1)

# Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.6(1)

Updated: May 14, 2021

Chapter: CCEDataProtect Tool

## Chapter: CCEDataProtect Tool

- CCEDataProtect Tool

- Configure External DBLookUp Registry Value using CCEDataProtect Tool

# CCEDataProtect Tool

## CCEDataProtect Tool

The CCEDataProtect tool is used to encrypt and decrypt sensitive information in SQLLogin registry key located at HKEY_LOCAL_MACHINE\SOFTWARE\Cisco.System,INC.\ICM\<instancename>\RouterA\Router\CurrentVersion\Configuration\Database . The CallRouter uses the external database lookup value in SQLLogin registry to authenticate and access the remote database.

The format of the CallRouter registry is \\{ComputerName}\{DataBaseName}=(domain\account-name,password) . For more information about CallRouter Registry, see the Modify CallRouter Registry to Provide for Database Lookup Authentication section in the Scripting and Media Routing Guide for Cisco Unified Contact Center Enterprise .

Only the administrator, domain user with administrator rights, or a local administrator can run the CCE DataProtect Tool,
                                             using <Install Directory>:\icm\bin\CCEDataProtectTool.exe.

You must run the CCEDataProtect Tool on every server where Dblookup functionality is used.

Following are the features supported with the CCEDataProtect Tool:

DBLookUp - view and edit External DBLookUp SQLLogin registry value.

DBLookUp supports the following options:

Decrypt and View - to view the encrypted password stored in the SQLLogin registry as clear text.

Edit and Encrypt - to configure the registry with encrypted value for first time or edit the existing encrypted value stored in the registry.

Help - information about the DBLookUp options.

Exit - to return to the initial menu.

Rekey - use this functionality with the Common Ground upgrade to re-encrypt the encrypted values based on upgraded software version.
                                 For Technology Refresh upgrade, you must reconfigure the value in the destination machine using the Edit and Encrypt option. It is recommended to use the Rekey option to secure the sensitive information.

Important

Rekey option will be supported in the future releases only.

Help - information about the CCEDataProtect Tool options.

Exit - to exit the CCEDataProtect Tool.

### Configure External DBLookUp Registry Value using CCEDataProtect Tool

Perform this procedure to configure the External DBLookUp registry value using the CCEDataProtect Tool.

Step 1

Run the CCEDataProtect Tool located at <Install Directory>:\icm\bin\CCEDataProtectTool.exe , on every server where DBLookup operations are set up.

Step 2

In the Main menu, press 1 to select DBLookUp , and press Enter .

Step 3

Enter a valid Instance Name for which this option is configured.

You can run only one instance of CCEDataProtect Tool at a time.

Step 4

Press 2 to select Edit and Encrypt , and press Enter .

The tool displays the current encrypted value stored in the registry as clear text, if it is already configured.

Enter a new Registry Value at the system prompt, and press Enter .

The maximum limit for the External DBLookUp registry entry is 2048 characters.

If you press Enter without entering any value, the system removes the encrypted value stored in the registry. You can use this option to remove
                                                               the encrypted entry.

When the system displays the message: Are you sure you want to Edit the Registry Details [Y/N] , press Y and then press Enter .

The system updates the Registry with an encrypted value and the system prompts the message: Registry Updated with Encrypted Data Successfully .

Step 5

Press 1 to select Decrypt and View , to verify the encrypted password.

CCEDataProtect Tool generates the following logs in the C:\temp folder.

CCEDataProtectTool.log - captures the tool usage by the administrator.

CCEDataProtectTool_audit.log - captures the audit details of the tool usage.

| Note | Only the administrator, domain user with administrator rights, or a local administrator can run the CCE DataProtect Tool,
                                             using <Install Directory>:\icm\bin\CCEDataProtectTool.exe. You must run the CCEDataProtect Tool on every server where Dblookup functionality is used. |
|---|---|

| Important | Rekey option will be supported in the future releases only. |
|---|---|

| Step 1 | Run the CCEDataProtect Tool located at <Install Directory>:\icm\bin\CCEDataProtectTool.exe , on every server where DBLookup operations are set up. |
|---|---|
| Step 2 | In the Main menu, press 1 to select DBLookUp , and press Enter . |
| Step 3 | Enter a valid Instance Name for which this option is configured. Note You can run only one instance of CCEDataProtect Tool at a time. | Note | You can run only one instance of CCEDataProtect Tool at a time. |
| Note | You can run only one instance of CCEDataProtect Tool at a time. |
| Step 4 | Press 2 to select Edit and Encrypt , and press Enter . The tool displays the current encrypted value stored in the registry as clear text, if it is already configured. Enter a new Registry Value at the system prompt, and press Enter . Note The maximum limit for the External DBLookUp registry entry is 2048 characters. If you press Enter without entering any value, the system removes the encrypted value stored in the registry. You can use this option to remove
                                                               the encrypted entry. When the system displays the message: Are you sure you want to Edit the Registry Details [Y/N] , press Y and then press Enter . The system updates the Registry with an encrypted value and the system prompts the message: Registry Updated with Encrypted Data Successfully . | Note | The maximum limit for the External DBLookUp registry entry is 2048 characters. If you press Enter without entering any value, the system removes the encrypted value stored in the registry. You can use this option to remove
                                                               the encrypted entry. |
| Note | The maximum limit for the External DBLookUp registry entry is 2048 characters. If you press Enter without entering any value, the system removes the encrypted value stored in the registry. You can use this option to remove
                                                               the encrypted entry. |
| Step 5 | Press 1 to select Decrypt and View , to verify the encrypted password. Note CCEDataProtect Tool generates the following logs in the C:\temp folder. CCEDataProtectTool.log - captures the tool usage by the administrator. CCEDataProtectTool_audit.log - captures the audit details of the tool usage. | Note | CCEDataProtect Tool generates the following logs in the C:\temp folder. CCEDataProtectTool.log - captures the tool usage by the administrator. CCEDataProtectTool_audit.log - captures the audit details of the tool usage. |
| Note | CCEDataProtect Tool generates the following logs in the C:\temp folder. CCEDataProtectTool.log - captures the tool usage by the administrator. CCEDataProtectTool_audit.log - captures the audit details of the tool usage. |

| Note | You can run only one instance of CCEDataProtect Tool at a time. |
|---|---|

| Note | The maximum limit for the External DBLookUp registry entry is 2048 characters. If you press Enter without entering any value, the system removes the encrypted value stored in the registry. You can use this option to remove
                                                               the encrypted entry. |
|---|---|

| Note | CCEDataProtect Tool generates the following logs in the C:\temp folder. CCEDataProtectTool.log - captures the tool usage by the administrator. CCEDataProtectTool_audit.log - captures the audit details of the tool usage. |
|---|---|