---
doc_id: webex-webexplaybooks-playbooks-payment-ai-agent-scripted-docs-upstream-overview-md
source_url: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/payment-ai-agent-scripted/docs/upstream-overview.md
repo: webex/WebexPlaybooks
ruta: playbooks/payment-ai-agent-scripted/docs/upstream-overview.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:10:12.041482+00:00
---

# WebexPlaybooks — playbooks/payment-ai-agent-scripted/docs/upstream-overview.md

Repositorio: webex/WebexPlaybooks

# Upstream Overview - Payment AI Agent Scripted

This document summarizes the source package for developer reference. The canonical source is the [Payment_AI_Agent_Scripted](https://github.com/ciscoAISCG/webex-cx-ai/tree/main/Playbooks/Payment_AI_Agent_Scripted) folder in the `ciscoAISCG/webex-cx-ai` repository.

## Source Package Contents

| Source file | Purpose in this Playbook |
|---|---|
| `exports/Payment_AI_Agent_Scripted.json` | Imported into Webex AI Agent Studio as the scripted AI Agent. |
| `exports/Payment_Flow_Scripted_voiceFlow.json` | Imported into Flow Designer as the main Webex Contact Center voice flow. |
| `exports/checkBalance_subflow.json` | Imported into Flow Designer as a subflow for balance lookup. |
| `exports/makePayment_subflow.json` | Imported into Flow Designer as a subflow for payment processing. |
| `docs/payment_scripted_functionality_details.md` | Source implementation notes used to write this Playbook. |
| `assets/payment-scripted-readable-flow.svg` | Source visual diagram. The WebexPlaybooks version uses a Mermaid diagram in `diagrams/architecture-diagram.md`. |

## Component Roles

| Component | Role |
|---|---|
| `Payment_Agent_Scripted` | Handles scripted conversation, intent detection, entity collection, and caller-facing responses. |
| `Payment_Flow_Scripted` | Main Webex Contact Center voice flow. It receives AI Agent events and routes the call through balance, payment, disconnect, or escalation paths. |
| `AI_Agent_payment` | Flow activity that hands control between Webex Contact Center and the scripted AI Agent. |
| `state_event_decider` | Case activity that routes custom events from the AI Agent. |
| `checkBalance` | Subflow that calls the balance endpoint using `patientID` and `dateOfBirth`. |
| `makePayment` | Subflow that calls the payment endpoint using card details, account number, and balance amount. |

## AI Agent Intents and Entities

The AI Agent export includes these main business intents:

| Intent | Purpose |
|---|---|
| `Payment Balance` | Collects `patientID` and `dateOfBirth`, then asks the flow to look up a balance. |
| `Make_Payment` | Collects `patientID` and `dateOfBirth`, checks balance first, then continues to payment collection. |
| `collectPaymentDetails` | Collects `CardNumber`, `CVV`, and `expiryDate` after the balance has been confirmed. |
| `Talk to an agent` | Escalates to the configured queue. |

The entity names used by the flow are `patientID`, `dateOfBirth`, `CardNumber`, `CVV`, and `expiryDate`.

## Custom Event Contract

| Event | Direction | Purpose |
|---|---|---|
| `Payment_Balance_Response_custom_Event` | AI Agent to voice flow | Starts the balance lookup path. Metadata includes `patientID` and `dateOfBirth`. |
| `make_Payment_Custom_Event` | AI Agent to voice flow | Starts the payment path by checking balance first. Metadata includes `patientID` and `dateOfBirth`. |
| `announceBalanceResponse` | Voice flow to AI Agent | Sends balance data back to the AI Agent. |
| `state_update` | AI Agent and voice flow handoff | Moves the AI Agent into `collectPaymentDetails`. |
| `collectPaymentDetails_customEvent` | AI Agent to voice flow | Sends collected card details to the voice flow. |
| `paymentResultResponse` | Voice flow to AI Agent | Sends payment result data back to the AI Agent. |
| `Bye` | AI Agent to voice flow | Ends the caller conversation and disconnects the call. |
| `Escalated` | AI Agent to voice flow | Routes the caller to the configured queue. |

## Flow Variables

| Variable | Used in | Description |
|---|---|---|
| `eventName` | Main flow | State Event name sent back to the AI Agent. |
| `eventDataJson` | Main flow | JSON payload sent back to the AI Agent. |
| `eventDataTOAIAgent` | Main flow | Intermediate payload populated from subflow output or state update metadata. |
| `patientID` | Main flow and balance subflow | Caller identifier parsed from AI Agent metadata. |
| `dateOfBirth` | Main flow and balance subflow | Caller date of birth parsed from AI Agent metadata. |
| `MainFlowAccountNumber` | Main flow | Account number returned by `checkBalance` and passed to `makePayment`. |
| `MainFlowPaymentBalance` | Main flow | Balance returned by `checkBalance` and passed to `makePayment`. |
| `cardNumber` | Main flow and payment subflow | Card number parsed from AI Agent metadata. |
| `cvv` | Main flow and payment subflow | CVV parsed from AI Agent metadata. |
| `expiry` | Main flow and payment subflow | Expiry date parsed from AI Agent metadata. |

## Billing API Calls

The WebexPlaybooks version removes the concrete source endpoints from the JSON exports. Configure these placeholders before importing or publishing the subflows:

| Subflow | Activity | Method | URL | Request body | Important outputs |
|---|---|---|---|---|---|
| `checkBalance` | `HTTPRequest_p83` | POST | `CONFIGURE_CHECK_BALANCE_ENDPOINT_URL` | `{"patientId":"{{subpatientID}}","dateOfBirth":"{{subDOB}}"}` | `accountNumber: $.accountId`, `paymentBalance: $.balanceAmount`, `error: $.error` |
| `makePayment` | `makePayment` | POST | `CONFIGURE_MAKE_PAYMENT_ENDPOINT_URL` | Account ID, card number, CVV, expiry date, and amount | `status: $.status`, `currency: $.currency`, `subFlowBalanceAmount_makePayment: $.balanceAmount`, `error: $.error` |

The endpoint response shapes must match the JSON path mappings above or the subflows must be updated before testing.

## Test Phrases

| Scenario | Caller says |
|---|---|
| Check balance | "I want to check my balance." |
| Make payment | "I want to make a payment." |
| Escalate | "I need to speak to an agent." |

## Security Notes

- The source sample demonstrates flow orchestration only. It does not provide PCI, HIPAA, fraud, consent, audit, logging, or token-management controls.
- Do not use real card numbers, CVVs, patient identifiers, dates of birth, or account numbers until your endpoint design and Webex Contact Center logging posture have been approved.
- Review every Flow Designer log, transcript, and variable that could contain sensitive information.

---
> Fuente: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/payment-ai-agent-scripted/docs/upstream-overview.md (licencia NOASSERTION)
