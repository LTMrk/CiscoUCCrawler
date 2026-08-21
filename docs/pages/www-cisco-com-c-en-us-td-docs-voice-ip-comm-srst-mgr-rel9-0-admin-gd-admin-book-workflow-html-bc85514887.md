---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-workflow-html-bc85514887
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/workflow.html
retrieved_at: 2026-08-21T23:37:39.846649+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 16, 2015

Chapter: Cisco Unified SRST Manager Workflow

## Chapter: Cisco Unified SRST Manager Workflow

# Cisco Unified SRST Manager Workflow

This section provides the steps to be followed to set up the Cisco Unified SRST Manager and provision the routers.

Step 1 Download the Open Virtual Appliance (OVA) file from Cisco.com and deploy it on your local system using VMware vSphere.

Step 2 Configure the IP address, Netmask, Gateway, Location, and User and Admin credentials.

Step 3 Log in to the Cisco Unified SRST Manager using the credentials configured in Step 2.

Step 4 Choose System > Trusted TLS Certificates > Add, enter the required details and click Update.

Step 5 Secure the communication between the Cisco Unified SRST Manager and Branch Office.

Note If you opt for secure communication, you should create a secure configuration in the branch router.

Step 6 Choose Setup Wizards > Add Central Call Agent and update the necessary details.

Step 7 Choose Configure > Sites and click Retrieve SRST References to view the Cisco Unified Communication Manager site information.

Step 8 Choose Configure > Sites. Click the corresponding router name, provide the details, and click Update.

Step 9 Choose Troubleshoot > Network Connectivity and click Start Network Connectivity Test to test the connectivity for the configured site.

Step 10 Choose Configure > Sites, select the router name, and click Provision to provision the site.

Step 11 Choose Reports > Site Provisioning History to check the provisioning status.