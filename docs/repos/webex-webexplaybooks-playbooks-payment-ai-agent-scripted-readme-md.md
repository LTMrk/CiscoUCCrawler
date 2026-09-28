---
doc_id: webex-webexplaybooks-playbooks-payment-ai-agent-scripted-readme-md
source_url: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/payment-ai-agent-scripted/README.md
repo: webex/WebexPlaybooks
ruta: playbooks/payment-ai-agent-scripted/README.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:10:10.850261+00:00
---

# WebexPlaybooks — playbooks/payment-ai-agent-scripted/README.md

Repositorio: webex/WebexPlaybooks

# Payment AI Agent Scripted for Webex Contact Center

> This Playbook is adapted from the [Payment AI Agent Scripted](https://github.com/ciscoAISCG/webex-cx-ai/tree/main/Playbooks/Payment_AI_Agent_Scripted) sample in the `ciscoAISCG/webex-cx-ai` repository on GitHub.

---

## Use Case Overview

Contact center developers and administrators can use this Playbook to deploy a scripted Webex Contact Center AI Agent for an inbound hospital payment line. The caller can check an outstanding balance or make a payment in a guided voice conversation. The scripted AI Agent collects the caller's `patientID`, `dateOfBirth`, and, when needed, payment card details; the Webex Contact Center flow receives the agent's custom state events, calls the matching subflow, and returns balance or payment results to the AI Agent so it can continue the caller conversation.

The main business outcome is faster self-service for routine billing calls. Callers can complete a balance lookup or payment flow without waiting for a live agent, while the implementation team gets a concrete example of the Webex AI Agent Studio scripted-agent plus Flow Designer state-event pattern.

**Target persona:** Webex Contact Center developer or administrator building voice self-service for healthcare billing, payment support, or similar authenticated account-service workflows.

**Estimated implementation time:** 2-4 hours, assuming an existing Webex Contact Center org with AI Agent Studio access, Flow Designer permissions, and a test entry point.

## Architecture

The integration uses Webex Contact Center and Webex AI Agent Studio components working together:

1. **Webex Contact Center Entry Point** receives the inbound caller and starts `Payment_Flow_Scripted`.
2. **Flow Designer** hosts the main voice flow and two subflows: `checkBalance` and `makePayment`.
3. **Webex AI Agent Studio** hosts `Payment_Agent_Scripted`, a scripted AI Agent with intents for `Payment Balance`, `Make_Payment`, and `collectPaymentDetails`.
4. **Billing API endpoints** are called by the subflows through Flow Designer HTTP Request activities. The JSON exports use placeholder URLs that must be replaced before import or publish.

For a visual representation of this data flow, see [diagrams/architecture-diagram.md](diagrams/architecture-diagram.md).

At runtime, the main flow hands the conversation to the scripted AI Agent through the Virtual Agent activity `AI_Agent_payment`. When the caller asks to check a balance, the AI Agent collects `patientID` and `dateOfBirth`, then sends `Payment_Balance_Response_custom_Event` to the flow. The flow parses the metadata, calls the `checkBalance` subflow, maps the returned balance to `eventDataTOAIAgent`, and resumes the AI Agent with `announceBalanceResponse`.

When the caller asks to make a payment, the first half of the path is intentionally the same: the flow checks the balance before collecting card details. After the balance response is returned, the AI Agent sends a `state_update` event with `{"intent":"collectPaymentDetails"}`. The flow echoes that state update back to the agent, the agent collects card data, and then it sends `collectPaymentDetails_customEvent`. The main flow calls the `makePayment` subflow and returns `paymentResultResponse` with payment status, currency, and amount. The `Bye` event disconnects the call.

## Prerequisites

### Webex Requirements

- A **Webex Contact Center** organization with an active Contact Center license.
- **Webex AI Agent Studio** access with scripted AI Agent support enabled for the org.
- Permission to import and publish Webex Contact Center flows and subflows in Flow Designer.
- Control Hub access to configure:
  - A telephony **Entry Point** for inbound voice.
  - An **Entry Point Mapping** from a test phone number to the entry point.
  - A human-agent **Queue** for escalation paths, with a Team assigned.
- Permission to create or import the `Payment_Agent_Scripted` AI Agent in AI Agent Studio.

### Developer Environment

- A browser with access to Control Hub, Flow Designer, and Webex AI Agent Studio.
- A JSON-aware text editor, such as VS Code, for replacing org-specific IDs before import.
- No local Node.js, Python, or SDK runtime is required. This sample is deployed through Webex Contact Center configuration exports.

### Billing API Requirements

- A reachable balance lookup endpoint that accepts `patientId` and `dateOfBirth`, then returns account and balance data matching the subflow mappings.
- A reachable payment endpoint that accepts account number, payment amount, card number, CVV, and expiry date, then returns payment status, currency, and amount data matching the subflow mappings.
- Use only fictitious caller, patient, and card data until your organization has approved the security controls for real payment or healthcare data.

## Code Scaffold

The `src/` directory contains importable Webex Contact Center and Webex AI Agent Studio exports. There is no runtime application code in this Playbook.

```text
src/
├── Payment_AI_Agent_Scripted.json          # Scripted AI Agent export for Webex AI Agent Studio
├── Payment_Flow_Scripted_voiceFlow.json    # Main Webex Contact Center voice flow
├── checkBalance_subflow.json               # Flow Designer subflow for balance lookup
├── makePayment_subflow.json                # Flow Designer subflow for payment processing
└── env.template                            # Org-specific values to replace before import
```

**`Payment_AI_Agent_Scripted.json`** defines the scripted AI Agent intents and slot collection for balance lookup, payment initiation, and payment-detail collection.

**`Payment_Flow_Scripted_voiceFlow.json`** defines the inbound voice flow. Key activities include `AI_Agent_payment`, `state_event_decider`, `Parse_checkBanalnceData`, `checkBalance_pp0`, `Parse_makePaymentData`, `makePayment_pgv`, `dataBacktoAI`, and `DisconnectContact_gse`.

**`checkBalance_subflow.json`** calls the configured balance API with `patientId` and `dateOfBirth`, then returns `paymentBalance`, `accountNumber`, and `announceBalanceResponse` data to the main flow.

**`makePayment_subflow.json`** calls the configured payment API with account number, amount, card number, CVV, and expiry date, then returns `paymentResultResponse` data to the main flow.

**`env.template`** lists every org-specific value that must be replaced in the JSON exports before import. The exported files contain sample IDs and endpoint placeholders; do not import or publish until those values are set for your environment.

For additional implementation notes, event names, variable mappings, and test phrases from the source package, see [docs/upstream-overview.md](docs/upstream-overview.md).

## Deployment Guide

### Part 1 - Import the Scripted AI Agent

1. Open Webex AI Agent Studio from Control Hub or your Webex Contact Center environment.
2. Create or import a scripted AI Agent using `src/Payment_AI_Agent_Scripted.json`.
3. Review the intents: `Payment Balance`, `Make_Payment`, `collectPaymentDetails`, `Talk to an agent`, and the default conversational intents.
4. Review the entity collection for `patientID`, `dateOfBirth`, `CardNumber`, `CVV`, and `expiryDate`.
5. Publish the AI Agent.
6. Copy the AI Agent ID and display name. You will use them when editing the main voice flow JSON.

### Part 2 - Configure Webex Contact Center Routing

7. In Control Hub, go to **Contact Center > Customer Experience > Queues** and create or confirm the escalation queue that callers should reach when they ask for an agent or when the flow errors.
8. Copy the queue ID from the queue detail page URL and note the queue display name.
9. Create or confirm a telephony entry point under **Contact Center > Customer Experience > Entry Points**.
10. Create or confirm an entry point mapping that assigns a test phone number to the entry point.

### Part 3 - Prepare the Export Files

11. Open `src/env.template` and collect the replacement values for your org.
12. Open `src/Payment_Flow_Scripted_voiceFlow.json` in a JSON-aware editor.
13. Replace the sample `orgId` value with your Webex org ID if your import process does not automatically reassign it.
14. Replace `virtualAgentId` in the `AI_Agent_payment` activity with the AI Agent ID from Step 6.
15. Replace `virtualAgentId_name` and `virtualAgentId:name` with the published AI Agent display name from Step 6.
16. Replace the `destination`, `destination_name`, and `destination:name` values in `QueueContact_a09` with your queue ID and queue name from Steps 7-8.
17. Review the `state_event_decider` branches. Keep the event names aligned with the AI Agent export: `Payment_Balance_Response_custom_Event`, `make_Payment_Custom_Event`, `state_update`, `collectPaymentDetails_customEvent`, `Bye`, and `Escalated`.
18. Open `src/checkBalance_subflow.json` and replace `CONFIGURE_CHECK_BALANCE_ENDPOINT_URL` in `HTTPRequest_p83` with your balance lookup endpoint.
19. Open `src/makePayment_subflow.json` and replace `CONFIGURE_MAKE_PAYMENT_ENDPOINT_URL` in the `makePayment` HTTP Request activity with your payment endpoint.

### Part 4 - Import and Publish the Webex Contact Center Artifacts

20. In Flow Designer, import `src/checkBalance_subflow.json` from the **Subflows** area.
21. In Flow Designer, import `src/makePayment_subflow.json` from the **Subflows** area.
22. In Flow Designer, import `src/Payment_Flow_Scripted_voiceFlow.json` from the **Flows** area.
23. Open the imported main flow and rebind the `AI_Agent_payment` activity to your published scripted AI Agent if Flow Designer does not bind it automatically.
24. Rebind the `checkBalance_pp0` activity to the imported `checkBalance` subflow if required.
25. Rebind the `makePayment_pgv` activity to the imported `makePayment` subflow if required.
26. Confirm that `QueueContact_a09` points to your escalation queue.
27. Validate the main flow and both subflows in Flow Designer.
28. Publish the subflows and then publish the main voice flow.

### Part 5 - Map and Test the Flow

29. Assign the published main flow to the entry point from Step 9.
30. Save the entry point configuration.
31. Dial the phone number mapped to the entry point.
32. For the balance path, say "I want to check my balance." Provide a test patient ID and date of birth when prompted. Verify the AI Agent announces the returned balance and disconnects cleanly.
33. For the payment path, call again and say "I want to make a payment." Provide the requested patient details and payment details. Verify the AI Agent announces the balance, collects payment details, returns payment status, and disconnects cleanly.
34. Ask to speak with an agent and verify the `Escalated` branch routes the call to the configured queue.

## Known Limitations

- **Sample IDs must be replaced.** The JSON exports include sample `orgId`, `virtualAgentId`, and queue destination values from the source environment. Replace them before import.
- **Endpoint placeholders must be replaced.** The subflow exports intentionally use `CONFIGURE_CHECK_BALANCE_ENDPOINT_URL` and `CONFIGURE_MAKE_PAYMENT_ENDPOINT_URL` placeholders. The flows will not run until those values are updated.
- **Payment and patient data need extra controls.** The sample demonstrates flow mechanics, not PCI, HIPAA, or production-grade payment processing. Do not collect real card data, patient identifiers, or dates of birth until your organization has approved the design.
- **No authentication is configured on the placeholder HTTP Request activities.** Real endpoints should use an approved authentication method, TLS, secret storage, token rotation, and response logging controls.
- **Custom event names must match exactly.** If you rename events in the AI Agent, update `state_event_decider` and the State Event values in the voice flow.
- **Subflows must be imported from the Subflows area.** Importing `checkBalance_subflow.json` or `makePayment_subflow.json` as normal flows will break the main flow handoff.
- **Voice only.** The sample is designed for inbound voice. Digital channels, outbound campaigns, and agent-desktop screen pop require additional design.
- **License.** This Playbook is adapted from source material published under the MIT License. This repository's license is available at [LICENSE](../../LICENSE).
- **Webex disclaimer.** This Playbook is provided as a starting point. Webex does not guarantee the functional accuracy of the source code. Test thoroughly before use in a production environment.

---
> Fuente: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/payment-ai-agent-scripted/README.md (licencia NOASSERTION)
