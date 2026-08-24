---
doc_id: ciscodevnet-cvp-sample-code-customervirtualassistant-dfremote-readme-md
source_url: https://github.com/CiscoDevNet/cvp-sample-code/blob/master/CustomerVirtualAssistant/DFRemote/README.md
repo: CiscoDevNet/cvp-sample-code
ruta: CustomerVirtualAssistant/DFRemote/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:11:09.895251+00:00
---

# cvp-sample-code — CustomerVirtualAssistant/DFRemote/README.md

Repositorio: CiscoDevNet/cvp-sample-code
Descripcion del repositorio: Sample Code for Customer Voice Portal (CVP)

# Call Studio DFRemote Application for DialogflowIntent / DialogflowParam element

## Preconditions
* Create the Google DialogFlow Agent by defining Intents / Entities (or import DialogflowAgent.zip into Dialogflow account).
* Do not set any parameter as Required for parameter for any Intent.
* Do not Perform the fulfilment of intent in Dialogflow.
* Configure the Dialogflow/Google TTS/Google ASR Key as suggested in Config guide in "Configuring Google Dialogflow Service" section.

## Application Development
* Play the welcome Prompt using TTS / Wav file.
* Handle the Intent using the DialogflowIntent callstudio element.
* Define the Parameters using the DialogFlowParam callstudio elements.
* DialogflowParam element can take user input in DTMF / Audio both.
* DialogflowIntent should be used to take DTMF input only in case it does not have any follow up parameter.
* Define the last parameter of the Intent by setting the "Last Parameter" property to "true", this will clear the context for the intent once its done.
* Handle the Intent Change exit state to handle the change in intent during the parameter value fetching. Point it to DialogflowIntent element.
* Store the values as required from the dialogflow responses and return it with subdialog return callstudio element back to CallServer / ICM, so that based on this routing can happen to right skill set.

---
> Fuente: https://github.com/CiscoDevNet/cvp-sample-code/blob/master/CustomerVirtualAssistant/DFRemote/README.md (licencia MIT)
