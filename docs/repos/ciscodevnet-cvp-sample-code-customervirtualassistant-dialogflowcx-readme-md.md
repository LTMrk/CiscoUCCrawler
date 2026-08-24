---
doc_id: ciscodevnet-cvp-sample-code-customervirtualassistant-dialogflowcx-readme-md
source_url: https://github.com/CiscoDevNet/cvp-sample-code/blob/master/CustomerVirtualAssistant/DialogflowCX/README.md
repo: CiscoDevNet/cvp-sample-code
ruta: CustomerVirtualAssistant/DialogflowCX/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:11:10.793850+00:00
---

# cvp-sample-code — CustomerVirtualAssistant/DialogflowCX/README.md

Repositorio: CiscoDevNet/cvp-sample-code
Descripcion del repositorio: Sample Code for Customer Voice Portal (CVP)

# Application DFCX
Demonstrates the capabilities of DialogflowCX Callstudio Element.

## Application Behaviour
* Sends the "welcome_event" to Dialogflow CX to initialize the dialog.
* Streams the user audio to Google Dialogflow CX, receives the audio response and play it and loops the flow.
* Receive the detectIntentResponse from Dialogflow CX, Handle the exit state to break the loop based on exit events (Agent Handoff or End of Session).
* Store the values as required from the dialogflow CX responses and return it with subdialog return callstudio element back to CallServer / ICM, so that based on this routing can happen to right skill set.
## Application Enhancements
* In the Dialogflow element, mention the Config ID in the "Config ID" field. If this field is left blank default config is fetched.
* Store the information which needs to be sent back to CCE and return it in "CVP Subdialog Return_01" element. 

## Dialogflow CX UCCE feature guide
* In the Dialogflow element, mention the Config ID in the "Config ID" field. If this field is left blank default config is fetched.
* Store the information which needs to be sent back to CCE and return it in "CVP Subdialog Return_01" element. 

## Feature guide
* [Dialogflow CX UCCE Feature guide](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/configuration/ucce_b_features-guide-1261/ucce_m_dialogflow_cx-1261.html)
* [Dialogflow CX PCCE Feature guide](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/maintenance/guide/pcce_b_features-guide-1261/ucce_b_features-guide-1261_chapter_01000.pdf)

---
> Fuente: https://github.com/CiscoDevNet/cvp-sample-code/blob/master/CustomerVirtualAssistant/DialogflowCX/README.md (licencia MIT)
