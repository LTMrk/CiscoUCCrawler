---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-14su2-admingd-cucm-b-administration-guide-14su2-cucm-b-test-admin-1d5ec8d564
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/14SU2/adminGd/cucm_b_administration-guide-14su2/cucm_b_test-adminguide_chapter_010000.html
retrieved_at: 2026-08-17T00:43:49.893492+00:00
---

Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

# Administration Guide for Cisco Unified Communications Manager, Release 14 and SUs

Updated: April 8, 2025

Chapter: Manage Bulk Certificates

## Chapter: Manage Bulk Certificates

# Manage Bulk Certificates

## Manage Bulk Certificates

Use bulk certificate management if you want to share a set of certificates between clusters. This step is required for system
                              functions that require established trust between clusters, such as extension mobility cross cluster.

Step 1

Export Certificates

This procedure exports the certificates to an SFTP server.

Step 2

Import Certificates

Import the certificates back into the home and remote (visiting) clusters.

### Export Certificates

This procedure exports the certificates to an SFTP server.

Step 1

From Cisco Unified OS Administration, choose Security > Bulk Certificate Management .

Step 2

Configure the settings for a TFTP server that both the home and remote clusters can reach. See the online help for information
                                          about the fields and their configuration options.

Step 3

Click Save .

Step 4

Click Export .

Step 5

In the Bulk Certificate Export window, choose All for the Certificate Type field.

Step 6

Click Export .

Step 7

Click Close .

The preceding steps are performed when certificates are self-signed and there is no common trust in another cluster. If there
                                                         is a common trust or the same signer, then the export of ALL certificates is not needed.

### Import Certificates

Import the certificates back into the home and remote (visiting) clusters.

Import of certificate using bulk certificate management causes phones to reset.

Ensure that you keep all the files that are created during export operations on the SFTP server to ensure a seamless consolidation
                                             between different clusters of Unified Communications Manager.

#### Before you begin

Before the Import button appears, you must complete the following activities:

Export the certificates from at least two clusters to the SFTP server.

Consolidate the exported certificates.

Step 1

From From Cisco Unified OS Administration, choose Security > Bulk Certificate Management > Import > Bulk Certificate Import .

Step 2

From the Certificate Type drop-down list, choose All .

Step 3

Choose Import .

When the bulk certificate import is performed, the certificates are then uploaded to the remote cluster as follows:

CAPF certificate gets uploaded as a CallManager-trust

Tomcat certificate gets uploaded as a Tomcat-trust

CallManager certificate gets uploaded as a CallManager-trust and a Phone-SAST-trust

ITLRecovery certificate gets uploaded as a Phone-SAST-trust and CallManager-trust

The following types of certificates determine phones that are restarted:

CallManager—All phones only if TFTP service is activated on the node that the certificate belongs.

TVS—Some phones based on CallManager group membership.

CAPF—All phones only if CAPF is activated.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Export Certificates | This procedure exports the certificates to an SFTP server. |
| Step 2 | Import Certificates | Import the certificates back into the home and remote (visiting) clusters. |

| Step 1 | From Cisco Unified OS Administration, choose Security > Bulk Certificate Management . |
|---|---|
| Step 2 | Configure the settings for a TFTP server that both the home and remote clusters can reach. See the online help for information
                                          about the fields and their configuration options. |
| Step 3 | Click Save . |
| Step 4 | Click Export . |
| Step 5 | In the Bulk Certificate Export window, choose All for the Certificate Type field. |
| Step 6 | Click Export . |
| Step 7 | Click Close . Note The preceding steps are performed when certificates are self-signed and there is no common trust in another cluster. If there
                                                         is a common trust or the same signer, then the export of ALL certificates is not needed. | Note | The preceding steps are performed when certificates are self-signed and there is no common trust in another cluster. If there
                                                         is a common trust or the same signer, then the export of ALL certificates is not needed. |
| Note | The preceding steps are performed when certificates are self-signed and there is no common trust in another cluster. If there
                                                         is a common trust or the same signer, then the export of ALL certificates is not needed. |

| Note | The preceding steps are performed when certificates are self-signed and there is no common trust in another cluster. If there
                                                         is a common trust or the same signer, then the export of ALL certificates is not needed. |
|---|---|

| Note | Import of certificate using bulk certificate management causes phones to reset. |
|---|---|

| Note | Ensure that you keep all the files that are created during export operations on the SFTP server to ensure a seamless consolidation
                                             between different clusters of Unified Communications Manager. |
|---|---|

| Step 1 | From From Cisco Unified OS Administration, choose Security > Bulk Certificate Management > Import > Bulk Certificate Import . |
|---|---|
| Step 2 | From the Certificate Type drop-down list, choose All . |
| Step 3 | Choose Import . Note When the bulk certificate import is performed, the certificates are then uploaded to the remote cluster as follows: CAPF certificate gets uploaded as a CallManager-trust Tomcat certificate gets uploaded as a Tomcat-trust CallManager certificate gets uploaded as a CallManager-trust and a Phone-SAST-trust ITLRecovery certificate gets uploaded as a Phone-SAST-trust and CallManager-trust Note The following types of certificates determine phones that are restarted: CallManager—All phones only if TFTP service is activated on the node that the certificate belongs. TVS—Some phones based on CallManager group membership. CAPF—All phones only if CAPF is activated. | Note | When the bulk certificate import is performed, the certificates are then uploaded to the remote cluster as follows: CAPF certificate gets uploaded as a CallManager-trust Tomcat certificate gets uploaded as a Tomcat-trust CallManager certificate gets uploaded as a CallManager-trust and a Phone-SAST-trust ITLRecovery certificate gets uploaded as a Phone-SAST-trust and CallManager-trust | Note | The following types of certificates determine phones that are restarted: CallManager—All phones only if TFTP service is activated on the node that the certificate belongs. TVS—Some phones based on CallManager group membership. CAPF—All phones only if CAPF is activated. |
| Note | When the bulk certificate import is performed, the certificates are then uploaded to the remote cluster as follows: CAPF certificate gets uploaded as a CallManager-trust Tomcat certificate gets uploaded as a Tomcat-trust CallManager certificate gets uploaded as a CallManager-trust and a Phone-SAST-trust ITLRecovery certificate gets uploaded as a Phone-SAST-trust and CallManager-trust |
| Note | The following types of certificates determine phones that are restarted: CallManager—All phones only if TFTP service is activated on the node that the certificate belongs. TVS—Some phones based on CallManager group membership. CAPF—All phones only if CAPF is activated. |

| Note | When the bulk certificate import is performed, the certificates are then uploaded to the remote cluster as follows: CAPF certificate gets uploaded as a CallManager-trust Tomcat certificate gets uploaded as a Tomcat-trust CallManager certificate gets uploaded as a CallManager-trust and a Phone-SAST-trust ITLRecovery certificate gets uploaded as a Phone-SAST-trust and CallManager-trust |
|---|---|

| Note | The following types of certificates determine phones that are restarted: CallManager—All phones only if TFTP service is activated on the node that the certificate belongs. TVS—Some phones based on CallManager group membership. CAPF—All phones only if CAPF is activated. |
|---|---|