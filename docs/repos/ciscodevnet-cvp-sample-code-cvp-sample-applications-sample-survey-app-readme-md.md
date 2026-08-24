---
doc_id: ciscodevnet-cvp-sample-code-cvp-sample-applications-sample-survey-app-readme-md
source_url: https://github.com/CiscoDevNet/cvp-sample-code/blob/master/CVP-Sample-Applications/Sample_Survey_App/README.md
repo: CiscoDevNet/cvp-sample-code
ruta: CVP-Sample-Applications/Sample_Survey_App/README.md
licencia: MIT
retrieved_at: 2026-08-24T09:11:01.427085+00:00
---

# cvp-sample-code — CVP-Sample-Applications/Sample_Survey_App/README.md

Repositorio: CiscoDevNet/cvp-sample-code
Descripcion del repositorio: Sample Code for Customer Voice Portal (CVP)

**Introduction**

This call studio application is a sample (post call) survey application. It supports 3 standard types of surveys - CSAT, CES and NPS.

**Customization**

This app can be customized in multiple ways:

1. Provide the the prompts to be played for each survey type by placing these files using names *cx_\*.wav* corresponding to the names specified in the application. Make sure to record the audio files using the same codec that was chosen during CVP installation. 

2. Customize this application to suit your custom survey needs, by including new/different survey types or new/more audio files. Make sure to deploy the new/updated app(s) on your CVP VXML Server(s).

**Testing**

By default, this application will be testable only in a comprehensive setup with the usual PCS configurations in place. To test it using a standalone call, add a session variable called *surveyList* in the '*Data*' tab of the '*Welcome*' audio prompt element configuration, with values like *2:3:1* or *1:3:2*. The convention is: *1 = CSAT, 2 = CES, 3 = NPS*.

---
> Fuente: https://github.com/CiscoDevNet/cvp-sample-code/blob/master/CVP-Sample-Applications/Sample_Survey_App/README.md (licencia MIT)
