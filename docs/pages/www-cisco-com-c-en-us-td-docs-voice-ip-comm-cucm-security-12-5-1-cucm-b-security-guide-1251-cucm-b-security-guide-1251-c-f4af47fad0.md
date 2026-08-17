---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-security-12-5-1-cucm-b-security-guide-1251-cucm-b-security-guide-1251-c-f4af47fad0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/12_5_1/cucm_b_security-guide-1251/cucm_b_security-guide-1251_chapter_011010.html
retrieved_at: 2026-08-17T03:58:44.716609+00:00
---

Security Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Security Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: February 24, 2025

Chapter: Cisco Unified Mobility Advantage Server Security Profile Setup

## Chapter: Cisco Unified Mobility Advantage Server Security Profile Setup

# Cisco Unified Mobility Advantage Server Security Profile Setup

This chapter provides information about Cisco Unified Mobility Advantage server security profile setup.

## About Cisco Unified Mobility Advantage Server Security Profile Setup

Unified Communications Manager Administration groups security-related settings to allow you to assign a single security profile to multiple Mobile Communicator clients.
                              Security-related settings include device security mode, incoming transport type, and X.509 subject name. Configuring a Cisco Unified Mobility Advantage server security profile in Unified Communications Manager Administration automatically applies this profile to all configured Mobile Communicator clients on that Unified Communications Manager .

Only the security features that the Cisco Unified Mobility Advantage server supports display in the security profile settings window.

You cannot configure Cisco Unified Mobility Advantage servers in Unified Communications Manager Assistant Administration . For information on setting up a security profile for a Cisco Unified Mobility Advantage server, refer to your Cisco Unified Mobility Advantage documentation. Make sure that the Cisco Unified Mobility Advantage Security Profile you configure on Unified Communications Manager matches the security profile on the Cisco Unified Mobility Advantage servers. For information on configuring a Cisco Unity Cisco Unified Mobility Advantage server security profile, see the Cisco Unified Communications Manager Security Guide .

## Find Cisco Unified Mobility Advantage Server Security Profile

To find a Cisco Unified Mobility Advantage server security profile, perform the following procedure:

Step 1

In Unified Communications Manager Administration , choose System > Security Profile > CUMA Server Security Profile .

The Find and List CUMA Server Security Profile window displays. Records from an active (prior) query may also display in the
                                          window.

Step 2

To find all records in the database, ensure the dialog box is empty; go to Step 3 .

To filter or search records

From the first drop-down list box, choose a search parameter.

From the second drop-down list box, choose a search pattern.

Specify the appropriate search text, if applicable.

To add additional search criteria, click the + button. When you add criteria, the system searches for a record that matches all criteria that you specify. To remove criteria,
                                                            click the – button to remove the last added criterion or click the Clear Filter button to remove all added search criteria.

Step 3

Click Find .

All matching records display. You can change the number of items that display on each page by choosing a different value from
                                          the Rows per Page drop-down list box.

Step 4

From the list of records that display, click the link for the record that you want to view.

To reverse the sort order, click the up or down arrow, if available, in the list header.

The window displays the item that you choose.

## Set Up Cisco Unified Mobility Advantage Server Security Profile

To add, update, or copy a security profile, perform the following procedure:

Step 1

In Unified Communications Manager Administration , choose System > Security Profile > CUMA Server Security Profile .

Step 2

Perform one of the following tasks:

To add a new profile, click Add New in the Find window and continue with Cisco Unified Mobility Advantage Server Security Profile Setup .

To copy an existing security profile, locate the appropriate profile and click the Copy button next to the security profile that you want to copy, and continue with Cisco Unified Mobility Advantage Server Security Profile Setup .

To update an existing profile, locate the appropriate security profile and continue with Cisco Unified Mobility Advantage Server Security Profile Setup .

When you click Add New , the configuration window displays with the default settings for each field. When you click Copy , the configuration window displays with the copied settings.

Step 3

Enter the appropriate settings as described in Table 1

Step 4

Click Save .

## Cisco Unified Mobility Advantage Server Security Profile Settings

The following table describes the settings for the Cisco Unified Mobility Advantage Server security profiles.

Setting

Description

Name

Enter a name for the security profile.

Tip

Description

Enter a description for the security profile. The description can include up to 50 characters in any language, but it cannot
                                          include double-quotes ("), percentage sign (%), ampersand (&), back-slash (\), or angle brackets (<>).

Device Security Mode

From the drop-down list box, choose one of the following options:

- Non Secure —No security features except image authentication exist for the Cisco Unified Mobility Advantage server. A TCP connection opens to Unified Communications Manager .

- Authenticated — Unified Communications Manager provides integrity and authentication for the Cisco Unified Mobility Advantage server. A TLS connection that uses NULL/SHA opens for signaling.

- Encrypted — Unified Communications Manager provides integrity, authentication, and encryption for the Cisco Unified Mobility Advantage server. A TLS connection that uses AES128/SHA opens for signaling, and SRTP carries the media for all mobile calls.

Transport Type

When Device Security Mode is Non Secure , choose the following option from the drop-down list box:

- TCP —Choose the Transmission Control Protocol to ensure that packets get received in the same order as the order in which they
                                             are sent. This protocol ensures that no packets get dropped, but the protocol does not provide any security.

When Device Security Mode is Authenticated or Encrypted , TLS specifies the Transport Type. TLS provides signaling integrity, device authentication, and signaling encryption (encrypted
                                          mode only).

Secure Certificate Subject or Subject Alternate Name

(Required for Authenticated or Encrypted Device Security Mode setting.) This field applies if you configured TLS as the transport
                                          type.

Secure Certificate Subject or Subject Alternate Name is an ITU Telecommunication Standardization Sector standard for Public
                                          Key Infrastructure in cryptography. The subject name corresponds to the source connection TLS certificate.

If multiple Secure Certificate Subject or Subject Alternate Name exists, enter one of the following characters to separate
                                          the names: space, comma, semicolon, or a colon.

You can enter up to 4096 characters in this field.

## Cisco Unified Mobility Advantage Server Security Profile Client Application

No "Device Security Profile" field exists on the device configuration window for a Mobile Communicator client, which means that you do not have to manually
                              apply the Cisco Unified Mobility Advantage Server Security profile to a client.

Configuring a Cisco Unified Mobility Advantage server security profile in Unified Communications Manager Administration automatically applies this profile to all configured Mobile Communicator clients on that Unified Communications Manager .

## Delete Cisco Unified Mobility Advantage Server Security Profile

This section describes how to delete a Cisco Unified Mobility Advantage server security profile from the Unified Communications Manager database.

Step 1

Find the security profile to delete.

Step 2

To delete a security profile, perform the following task:

In the Find and List window, check the check box next to the appropriate security profile; then, click Delete Selected .

Step 3

When prompted to confirm the delete operation, click OK to delete or Cancel to cancel the delete operation.

## Where to Find More Information About Cisco Unified Mobility Advantage Server Security Profile

| Note | You cannot configure Cisco Unified Mobility Advantage servers in Unified Communications Manager Assistant Administration . For information on setting up a security profile for a Cisco Unified Mobility Advantage server, refer to your Cisco Unified Mobility Advantage documentation. Make sure that the Cisco Unified Mobility Advantage Security Profile you configure on Unified Communications Manager matches the security profile on the Cisco Unified Mobility Advantage servers. For information on configuring a Cisco Unity Cisco Unified Mobility Advantage server security profile, see the Cisco Unified Communications Manager Security Guide . |
|---|---|

| Step 1 | In Unified Communications Manager Administration , choose System > Security Profile > CUMA Server Security Profile . The Find and List CUMA Server Security Profile window displays. Records from an active (prior) query may also display in the
                                          window. |
|---|---|
| Step 2 | To find all records in the database, ensure the dialog box is empty; go to Step 3 . To filter or search records From the first drop-down list box, choose a search parameter. From the second drop-down list box, choose a search pattern. Specify the appropriate search text, if applicable. Note To add additional search criteria, click the + button. When you add criteria, the system searches for a record that matches all criteria that you specify. To remove criteria,
                                                            click the – button to remove the last added criterion or click the Clear Filter button to remove all added search criteria. | Note | To add additional search criteria, click the + button. When you add criteria, the system searches for a record that matches all criteria that you specify. To remove criteria,
                                                            click the – button to remove the last added criterion or click the Clear Filter button to remove all added search criteria. |
| Note | To add additional search criteria, click the + button. When you add criteria, the system searches for a record that matches all criteria that you specify. To remove criteria,
                                                            click the – button to remove the last added criterion or click the Clear Filter button to remove all added search criteria. |
| Step 3 | Click Find . All matching records display. You can change the number of items that display on each page by choosing a different value from
                                          the Rows per Page drop-down list box. |
| Step 4 | From the list of records that display, click the link for the record that you want to view. Note To reverse the sort order, click the up or down arrow, if available, in the list header. The window displays the item that you choose. | Note | To reverse the sort order, click the up or down arrow, if available, in the list header. |
| Note | To reverse the sort order, click the up or down arrow, if available, in the list header. |

| Note | To add additional search criteria, click the + button. When you add criteria, the system searches for a record that matches all criteria that you specify. To remove criteria,
                                                            click the – button to remove the last added criterion or click the Clear Filter button to remove all added search criteria. |
|---|---|

| Note | To reverse the sort order, click the up or down arrow, if available, in the list header. |
|---|---|

| Step 1 | In Unified Communications Manager Administration , choose System > Security Profile > CUMA Server Security Profile . |
|---|---|
| Step 2 | Perform one of the following tasks: To add a new profile, click Add New in the Find window and continue with Cisco Unified Mobility Advantage Server Security Profile Setup . To copy an existing security profile, locate the appropriate profile and click the Copy button next to the security profile that you want to copy, and continue with Cisco Unified Mobility Advantage Server Security Profile Setup . To update an existing profile, locate the appropriate security profile and continue with Cisco Unified Mobility Advantage Server Security Profile Setup . When you click Add New , the configuration window displays with the default settings for each field. When you click Copy , the configuration window displays with the copied settings. |
| Step 3 | Enter the appropriate settings as described in Table 1 |
| Step 4 | Click Save . |

| Setting | Description |
|---|---|
| Name | Enter a name for the security profile. Tip Include the device model in the security profile name to help you find the correct profile when you are searching for or updating
                                                   a profile. | Tip | Include the device model in the security profile name to help you find the correct profile when you are searching for or updating
                                                   a profile. |
| Tip | Include the device model in the security profile name to help you find the correct profile when you are searching for or updating
                                                   a profile. |
| Description | Enter a description for the security profile. The description can include up to 50 characters in any language, but it cannot
                                          include double-quotes ("), percentage sign (%), ampersand (&), back-slash (\), or angle brackets (<>). |
| Device Security Mode | From the drop-down list box, choose one of the following options: Non Secure —No security features except image authentication exist for the Cisco Unified Mobility Advantage server. A TCP connection opens to Unified Communications Manager . Authenticated — Unified Communications Manager provides integrity and authentication for the Cisco Unified Mobility Advantage server. A TLS connection that uses NULL/SHA opens for signaling. Encrypted — Unified Communications Manager provides integrity, authentication, and encryption for the Cisco Unified Mobility Advantage server. A TLS connection that uses AES128/SHA opens for signaling, and SRTP carries the media for all mobile calls. |
| Transport Type | When Device Security Mode is Non Secure , choose the following option from the drop-down list box: TCP —Choose the Transmission Control Protocol to ensure that packets get received in the same order as the order in which they
                                             are sent. This protocol ensures that no packets get dropped, but the protocol does not provide any security. When Device Security Mode is Authenticated or Encrypted , TLS specifies the Transport Type. TLS provides signaling integrity, device authentication, and signaling encryption (encrypted
                                          mode only). |
| Secure Certificate Subject or Subject Alternate Name | (Required for Authenticated or Encrypted Device Security Mode setting.) This field applies if you configured TLS as the transport
                                          type. Secure Certificate Subject or Subject Alternate Name is an ITU Telecommunication Standardization Sector standard for Public
                                          Key Infrastructure in cryptography. The subject name corresponds to the source connection TLS certificate. If multiple Secure Certificate Subject or Subject Alternate Name exists, enter one of the following characters to separate
                                          the names: space, comma, semicolon, or a colon. You can enter up to 4096 characters in this field. |

| Tip | Include the device model in the security profile name to help you find the correct profile when you are searching for or updating
                                                   a profile. |
|---|---|

| Step 1 | Find the security profile to delete. |
|---|---|
| Step 2 | To delete a security profile, perform the following task: In the Find and List window, check the check box next to the appropriate security profile; then, click Delete Selected . |
| Step 3 | When prompted to confirm the delete operation, click OK to delete or Cancel to cancel the delete operation. |