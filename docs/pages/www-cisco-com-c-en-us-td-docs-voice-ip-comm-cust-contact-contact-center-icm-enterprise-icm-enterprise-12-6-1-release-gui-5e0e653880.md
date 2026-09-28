---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-release-gui-5e0e653880
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/release/guide/rcct_b_cce-solution-rns-12-6/rcct_m_ccdm_12_6.html
retrieved_at: 2026-08-16T19:38:32.822482+00:00
---

Release Notes for Cisco Contact Center Enterprise Solutions Release 12.6(1)

# Release Notes for Cisco Contact Center Enterprise Solutions Release 12.6(1)

Updated: May 14, 2021

Chapter: Cisco Unified Contact Center Domain Manager

## Chapter: Cisco Unified Contact Center Domain Manager

# Cisco Unified Contact Center Domain Manager

## New Features

None.

## Updated Features

### Platform—Infrastructure

All new installations and systems upgrading to Release 12.6(1) must use Windows 2019 and Microsoft SQL Server 2019.

### Agent Desk Settings Enhancements

Agents can now use multiple device types or shared lines while accessing the Cisco Finesse desktop. For example, an agent
                              can use a physical phone while working at the contact center and a softphone, such as Jabber, while working at home.

Agent Desk Settings has two new options:

ACD shared line usage: If enabled, this option allows agents to participate in a shared line experience.

Tone for auto answer: This option enables a zip tone when the agent connects. The zip tone can only be enabled if auto-answer is enabled in the
                                    desk settings.

### Agent Assist Services Enhancements

Agent Assist services can now be enabled per agent. Agent Assist services allow agents to use Cisco Answers and provide seamless
                              responses and suggestions to customer queries.

### Call Manager Provisioning Enhancements

This release includes enhanced provisioning for CUCM person, controlled devices and IP Phone provisioning with owner person,
                              and controlled device mapping.

### Deletion of Unified CCE Resources Referenced in Scripts

When you attempt to delete Unified CCE resources from the Resource Manager gadget, the system now checks whether the resources
                              are referenced in any scripts. If so, a message is displayed, prompting you to remove the resource from any scripts before
                              proceeding.

### Supported Browsers

This release supports the following browsers:

Microsoft Edge (Chromium)

Google Chrome

Mozilla Firefox

Unified CCDM Release 12.6(1) does not support any version of Internet Explorer.

### Improved Version Information for Application

The About Unified CCDM page in the application now shows more detail and in a more user-friendly format. The page includes
                              information about the release name, release version number, and the patch history for the installation.

## Deprecated Features

The following features are deprecated in this release.

### SOAP Support for Resource Manager APIs

SOAP support for resource manager APIs will be removed post release 12.6(1). Only REST-based access will be supported.

### Legacy Resource Manager

Legacy Resource Manager, the traditional three-pane view to manage and maintain resources on Unified CCE, will be removed
                              post release 12.6(1). There will be no new features, enhancements, or bug fixes for Legacy Resource Manager. We recommend
                              that you use the Resource Manager gadgets available with Unified CCDM for resource management-related tasks.

### XML Format Support for Web Service APIs

Web Service APIs will now only support the JSON format as the support for the XML format will be removed post release 12.6(1).