---
doc_id: ciscodevnet-webexcc-digital-channels-webex-connect-flows-how-to-manually-upgrade-from-v3-1-to-v3-2-workflows-md
source_url: https://github.com/CiscoDevNet/webexcc-digital-channels/blob/main/Webex%20Connect%20Flows/How%20to%20manually%20upgrade%20from%20v3.1%20to%20v3.2%20workflows.MD
repo: CiscoDevNet/webexcc-digital-channels
ruta: Webex Connect Flows/How to manually upgrade from v3.1 to v3.2 workflows.MD
licencia: sin declarar
retrieved_at: 2026-08-24T09:11:33.404135+00:00
---

# webexcc-digital-channels — Webex Connect Flows/How to manually upgrade from v3.1 to v3.2 workflows.MD

Repositorio: CiscoDevNet/webexcc-digital-channels

# How to manually upgrade from v3.1 to v3.2 workflows

In case you have made custom changes to your inbound flows, you can manually upgrade your existing v3.1 flows to v3.2. This ensures that the custom changes are retained and don't have to be repeated. Follow the below steps for the same:

## For Setting Priority to Contacts
- Build custom logic to determine contact priority in the media specific inbound flows.
- Custom logic can be based on any field such as the email subject from incoming message, email ID from incoming message, SMS or Whatsapp phone number, chat form values, text message of the customer, etc.
- Any other custom field can also be used to build the logic. 
- Nodes like Evaluate, Branch or others from the node palette can be used to build the custom logic.
- Once the priority is determined for the contact, it can be set while queuing the contact to a queue, using the Queue Task node.
- Open the Queue Task node and upgrade it to the latest available version (v1.3), where you'll find a new field "Contact Priority".
- Set the contact priority in the "Contact Priority" field if you want to prioritize the contact in the queue, otherwise it can be left empty.

  ![SetContactPriority](v3.5/images/SetContactPriority.png)

- Sample flow is present in [Usage Of Contact Priority in Flows](v3.5/Sample/Usage%20of%20Contact%20Priority%20In%20Flows/).
- For more details refer to [Usage Of Contact Priority in Flows Readme](v3.5/Sample/Usage%20of%20Contact%20Priority%20In%20Flows/README.md).

---
> Fuente: https://github.com/CiscoDevNet/webexcc-digital-channels/blob/main/Webex%20Connect%20Flows/How%20to%20manually%20upgrade%20from%20v3.1%20to%20v3.2%20workflows.MD (licencia sin declarar)
