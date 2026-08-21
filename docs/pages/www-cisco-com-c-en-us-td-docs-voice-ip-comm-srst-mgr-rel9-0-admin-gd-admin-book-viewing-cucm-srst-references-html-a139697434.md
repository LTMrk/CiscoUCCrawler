---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-viewing-cucm-srst-references-html-a139697434
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/viewing_cucm_srst_references.html
retrieved_at: 2026-08-21T23:38:26.166374+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 5, 2014

Chapter: Viewing the Cisco Unified SRST References

## Chapter: Viewing the Cisco Unified SRST References

## Viewing the Cisco Unified SRST References

Step 1 Select Configure > Central Call Agents .

The system displays the Central Call Agents page, containing the name of the central call agent that you have configured.

Step 2 To view the details of the central call agent, click the underlined name.

The system displays the CUCM Profile page. Click the SRST References tab to view a list of the Cisco Unified SRST references.

Step 3 To retrieve additional Cisco Unified SRST references, do the following:

a. Click Retrieve SRST References . The system displays a warning message stating that the system will automatically contact the Cisco Unified Communications Manager and download all configured SRST references.

b. Click OK to retrieve the references.

The system automatically creates new branch office sites for each Cisco Unified SRST reference.

Note When Cisco Unified SRST Manager retrieves a new SRST reference from the Cisco Unified Communications Manager, provisioning for the new site is disabled by default. An administrator must enable provisioning for the site manually. See Changing the Information for a Single Cisco Unified SRST Site and Changing the Information for Multiple Cisco Unified SRST Sites at Once .

When finished, the system displays the Sites page. (You can also select Configure > Sites to view the Sites page.)

The page contains the following information for each site:

- Site name

- Indication of whether provisioning is enabled

- Branch Call Agent

- Site Template Name

- SRST Type

- Indication of whether dial plan configuration is enabled

For more information about the information displayed on the Sites page, see Viewing and Provisioning Sites .

Related Topics