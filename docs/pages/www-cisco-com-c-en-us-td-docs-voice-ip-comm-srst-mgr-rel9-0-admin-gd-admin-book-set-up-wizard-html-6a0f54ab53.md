---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-set-up-wizard-html-6a0f54ab53
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/set_up_wizard.html
retrieved_at: 2026-08-21T23:38:09.202385+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 5, 2014

Chapter: Using the Setup Wizard

## Chapter: Using the Setup Wizard

## Using the Setup Wizard

Use the Setup Wizard to set initial values for the Cisco Unified SRST Manager system.

Before You Begin

Gather the following information before you run the Setup Wizard:

Table 5 System Setup Parameters

Auto-Learn Call Forwarding Settings

Determines whether the system should auto-learn the call forwarding settings.

Pilot Number

The voicemail pilot number for the branch office call agent. The system saves this number to the default site template.

If the “Autolearn call forward settings” option is set to “Yes,” the voicemail pilot number is automatically retrieved from the central call agent during the provisioning process. Enter the voicemail pilot number if you want to override the retrieved pilot number.

TLS Security

Enables security between Cisco Unified SRST Manager and devices at the branch.

- If TLS security is set to On, Cisco Unified SRST Manager uses https and ssh. Ensure that the branch site has generated an encryption certificate.

- If TLS security is set to Off, Cisco Unified SRST Manager uses http and telnet.

Step 1 Select Setup Wizards > Setup .

The system displays the Introduction page of the setup wizard.

Step 2 Click Next to begin the wizard. See Table 5 for descriptions of the parameters configured in the wizard.

Related Topics

- Using the Central Call Agent Wizard to Add Cisco Unified Communications Manager Information

| Parameter | Description |
|---|---|
| Voicemail Pilot |
| Auto-Learn Call Forwarding Settings | Determines whether the system should auto-learn the call forwarding settings. |
| Pilot Number | The voicemail pilot number for the branch office call agent. The system saves this number to the default site template. If the “Autolearn call forward settings” option is set to “Yes,” the voicemail pilot number is automatically retrieved from the central call agent during the provisioning process. Enter the voicemail pilot number if you want to override the retrieved pilot number. |
| TLS Security |
| TLS Security | Enables security between Cisco Unified SRST Manager and devices at the branch. If TLS security is set to On, Cisco Unified SRST Manager uses https and ssh. Ensure that the branch site has generated an encryption certificate. If TLS security is set to Off, Cisco Unified SRST Manager uses http and telnet. |