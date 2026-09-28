---
doc_id: ciscodevnet-cvp-sample-code-customervirtualassistant-dftext-readme-md
source_url: https://github.com/CiscoDevNet/cvp-sample-code/blob/master/CustomerVirtualAssistant/DFText/Readme.md
repo: CiscoDevNet/cvp-sample-code
ruta: CustomerVirtualAssistant/DFText/Readme.md
licencia: MIT
retrieved_at: 2026-08-24T09:11:10.357251+00:00
---

# cvp-sample-code — CustomerVirtualAssistant/DFText/Readme.md

Repositorio: CiscoDevNet/cvp-sample-code
Descripcion del repositorio: Sample Code for Customer Voice Portal (CVP)

# Call Studio DFText Application for Dialogflow element
## Preconditions
* Create the Google DialogFlow Agent by defining Intents / Entities (or import DialogflowAgent.zip into Dialogflow account).
* Define the required parameter and corresponding prompts for parameter for each Intent.
* Perform the fulfilment if you want to use DialogFlow Webhook based fulfilment (DFText Flow)
* Configure the Dialogflow Key as suggested in Config guide in "Configuring Google Dialogflow Service" section.
* Configure the TTS Key as suggested in Config guide in "Configuring Google Dialogflow Service" section.

## Application Development
* Play the welcome Prompt using TTS / Wav file.
* Handle the fulfilment response from Dialogflow response and synthesize it using audio element which will play it. Audio element can use [SSML](https://cloud.google.com/text-to-speech/docs/ssml) format to change language, voice etc.
* Handle the exit state to break the loop based on intent.
* Store the values as required from the dialogflow responses and return it with subdialog return callstudio element back to CallServer / ICM, so that based on this routing can happen to right skill set.

---
> Fuente: https://github.com/CiscoDevNet/cvp-sample-code/blob/master/CustomerVirtualAssistant/DFText/Readme.md (licencia MIT)
