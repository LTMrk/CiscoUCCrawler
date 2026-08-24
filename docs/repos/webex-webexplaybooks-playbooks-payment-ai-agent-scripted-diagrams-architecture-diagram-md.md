---
doc_id: webex-webexplaybooks-playbooks-payment-ai-agent-scripted-diagrams-architecture-diagram-md
source_url: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/payment-ai-agent-scripted/diagrams/architecture-diagram.md
repo: webex/WebexPlaybooks
ruta: playbooks/payment-ai-agent-scripted/diagrams/architecture-diagram.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:10:11.646744+00:00
---

# WebexPlaybooks — playbooks/payment-ai-agent-scripted/diagrams/architecture-diagram.md

Repositorio: webex/WebexPlaybooks

# Architecture Diagram

```mermaid
sequenceDiagram
    autonumber
    actor Caller
    participant Entry as Webex Contact Center Entry Point
    participant Flow as Payment_Flow_Scripted
    participant Agent as Payment_Agent_Scripted
    participant Balance as checkBalance subflow
    participant Payment as makePayment subflow
    participant Billing as Configured Billing APIs
    participant Queue as Escalation Queue

    Caller->>Entry: Inbound voice call
    Entry->>Flow: Start voice flow
    Flow->>Agent: AI_Agent_payment starts scripted conversation
    Agent->>Caller: Collect intent and caller details

    alt Balance lookup
        Agent->>Flow: Payment_Balance_Response_custom_Event<br/>patientID, dateOfBirth
        Flow->>Flow: Parse_checkBanalnceData
        Flow->>Balance: subpatientID, subDOB
        Balance->>Billing: POST configured balance endpoint
        Billing-->>Balance: accountId, balanceAmount
        Balance-->>Flow: accountNumber, paymentBalance,<br/>announceBalanceResponse
        Flow->>Agent: State Event announceBalanceResponse
        Agent->>Caller: Announces balance
        Agent->>Flow: Bye
        Flow-->>Caller: DisconnectContact_gse
    else Make payment
        Agent->>Flow: make_Payment_Custom_Event<br/>patientID, dateOfBirth
        Flow->>Balance: Check balance first
        Balance->>Billing: POST configured balance endpoint
        Billing-->>Balance: accountId, balanceAmount
        Balance-->>Flow: accountNumber and balance
        Flow->>Agent: State Event announceBalanceResponse
        Agent->>Caller: Announces balance and asks for payment details
        Agent->>Flow: state_update<br/>intent: collectPaymentDetails
        Flow->>Agent: State Event state_update
        Agent->>Caller: Collect card number, CVV, expiry date
        Agent->>Flow: collectPaymentDetails_customEvent
        Flow->>Payment: card details, account number, balance
        Payment->>Billing: POST configured payment endpoint
        Billing-->>Payment: status, currency, balanceAmount
        Payment-->>Flow: paymentResultResponse payload
        Flow->>Agent: State Event paymentResultResponse
        Agent->>Caller: Announces payment result
        Agent->>Flow: Bye
        Flow-->>Caller: DisconnectContact_gse
    else Human escalation
        Agent->>Flow: Escalated
        Flow->>Queue: QueueContact_a09
        Queue-->>Caller: Live agent queue
    end
```

---
> Fuente: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/payment-ai-agent-scripted/diagrams/architecture-diagram.md (licencia NOASSERTION)
