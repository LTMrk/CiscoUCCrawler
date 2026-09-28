---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-configuration-guide-f892f99022
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/configuration/guide/ccvp_b_1262-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp_b_1252-configuration-guide-for-cisco-unified-customer-voice-portal-release-1252_chapter_010110.html
retrieved_at: 2026-08-21T11:58:51.633105+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(2)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(2)

Updated: April 28, 2023

Chapter: Webex Experience Management Configuration

## Chapter: Webex Experience Management Configuration

# Webex Experience Management Configuration

## Import Experience Management Certificate to Unified CVP Call Server

Step 1

Export the Experience Management platform certificate:

Open a Chrome browser session and navigate to https://api.getcloudcherry.com/api/Questions/Questionnaire .

Click the lock icon in the address bar and click Certificate (Valid) .

Under the Details tab, click Copy to File to export the certificate and save it as a Base-64 encoded X.509 (.CER) file with the name CloudcherryAPI.cer (the file to be imported in the next step).

Step 2

Import the certificate into the CVP keystore:

Copy the exported certificate to the following directory of all CVP call servers: C:\Cisco\CVP\conf\security

Import these certificates using the command: %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -trustcacerts -alias
                                                {apicloudcherry_name} -file c:\cisco\cvp\conf\security\CloudcherryAPI.cer

Step 3

Export the Experience Management platform Azure certificate:

Open a Chrome browser, navigate to https://learn.microsoft.com/en-us/azure/security/fundamentals/azure-ca-details , and download the DigiCert Global Root G2 certificate.

Check the certificate which is downloaded as DigiCert Global Root G2.crt .

Step 4

Import the certificate into the CVP keystore:

Copy the exported certificate to the following directory of all CVP call servers: C:\Cisco\CVP\conf\security as DigiCert_Global_Root_G2.crt

Import this certificate using the command: %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -trustcacerts -alias
                                                {apicloudcherry_azure} -file c:\cisco\cvp\conf\security\DigiCert_Global_Root_G2.crt

Step 5

Restart the CVP server.

While importing the certificate, CVP requests for a password. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

If the Certificate Authority (CA) signed certificate on Cloud expires as per policy, the new certificate needs to be imported
                                          to the CVP Server.

## Experience Management Voice Survey Thresholds

Experience Management voice survey is used for getting feedback on the overall customer journey experience.

The following default configurations are used for this feature:

In c:\cisco\cvp\conf\ivr.properties file:

Configurable/ Non-Configurable?

Time in seconds after which AuthToken is refreshed

Yes

1800

IVR.SurveyTokenRefresh TimeOut

Time in seconds after which SurveyToken is refreshed

Yes

43200

IVR.SurveyQuestionRefresh TimeOut

Time in seconds after which SurveyQuestions is refreshed

Yes

43200

IVR.WxmSurveyToken ApiUrl

Url to connect to fetch the survey token from Wxm

Yes

https://api.getcloudcherry.com/api/SurveyToken

IVR.WxmSurveyQuestions ApiUrl

Url to connect to fetch the questionnaire from Wxm

Yes

https://api.getcloudcherry.com/api/Questions/ Questionnaire

IVR.WxmSurveyAnswers SubmitApiUrl

Url to connect to submit the answers to Wxm

Yes

https://api.getcloudcherry.com/api/Survey ByToken/

IVR.WxmSurveySettings ApiUrl

Url to connect to fetch the settings of the questionaire from Wxm

Yes

https://api.getcloudcherry.com/api/Settings/

IVR.WxmAudio Url

Url to connect to fetch the audio files from Wxm

Yes

https://api.getcloudcherry.com/api/Stream UserAsset/

IVR.WxmSurveyQuestionnaire Url

Url to connect to fetch the questionnaire settings from Wxm

Yes

https://api.getcloudcherry.com/api/surveyquestionnaire/

In c:\cisco\cvp\conf\sip.properties file:

SIP.CloudCherry.SurveyValidity Time

Time in seconds for which the survey is active

Yes

60000

SIP.CloudConnect.SurveyDispatch EndPointApi

Url for connecting Cloud Connect to get the SurveyDispatch EndPoint

Yes

/cherrypoint/surveydispatch

SIP.CloudConnect.Auth TokenApi

Url for connecting Cloud Connect to get AuthToken for Wxm

Yes

/cherrypoint/authtoken

Sample

## Experience Management SMS/Email Thresholds

Experience Management SMS/Email-based survey is used to send the survey link to the callers for getting feedback on the overall
                              customer journey experience.

The following batch threshold properties which trigger the SMS/Email Cloud Connect API have to be configured (if not already
                              configured) for this feature:

In c:\cisco\cvp\conf\ivr.properties file:

Batch size for triggering the Email/SMS Cloud Connect API

Yes

100

Batch timeout (in seconds) for triggering the Email/SMS Cloud Connect API

Yes

60

Customers can optimize these values based on their deployment requirements.

In c:\cisco\cvp\conf\sip.properties file:

SIP.CloudConnect.Request Timeout

HTTP request connection timeout (in milliseconds) towards Cloud Connect component

Yes

10000

The timeout value can be increased as per environment.

Sample

## HTTP Proxy Settings in VXML Server

For Experience Management to function, the VXML server must be connected to the internet. Enable direct access to the internet
                              or configure HTTP proxy settings in the VXML server. To configure HTTP proxy settings in VXML server, perform the following
                              steps:

Step 1

Open Windows regedit in the VXML server.

Step 2

Go to HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Apache Software Foundation\Procrun 2.0\VXMLServer\Parameters\Java\Options .

Step 3

Add the following entries:

```
-Dhttp.proxyHost=<proxy IP>
-Dhttp.proxyPort=<proxy port>
-Dorg.asynchttpclient.useProxyProperties=true
-Dhttp.nonProxyHosts=<hostname>
```

Step 4

Restart the CVP VXML server from Windows services.

| Step 1 | Export the Experience Management platform certificate: Open a Chrome browser session and navigate to https://api.getcloudcherry.com/api/Questions/Questionnaire . Click the lock icon in the address bar and click Certificate (Valid) . Under the Details tab, click Copy to File to export the certificate and save it as a Base-64 encoded X.509 (.CER) file with the name CloudcherryAPI.cer (the file to be imported in the next step). |
|---|---|
| Step 2 | Import the certificate into the CVP keystore: Copy the exported certificate to the following directory of all CVP call servers: C:\Cisco\CVP\conf\security Import these certificates using the command: %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -trustcacerts -alias
                                                {apicloudcherry_name} -file c:\cisco\cvp\conf\security\CloudcherryAPI.cer |
| Step 3 | Export the Experience Management platform Azure certificate: Open a Chrome browser, navigate to https://learn.microsoft.com/en-us/azure/security/fundamentals/azure-ca-details , and download the DigiCert Global Root G2 certificate. Check the certificate which is downloaded as DigiCert Global Root G2.crt . |
| Step 4 | Import the certificate into the CVP keystore: Copy the exported certificate to the following directory of all CVP call servers: C:\Cisco\CVP\conf\security as DigiCert_Global_Root_G2.crt Import this certificate using the command: %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -trustcacerts -alias
                                                {apicloudcherry_azure} -file c:\cisco\cvp\conf\security\DigiCert_Global_Root_G2.crt |
| Step 5 | Restart the CVP server. |

| Note | While importing the certificate, CVP requests for a password. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
|---|---|

| Note | If the Certificate Authority (CA) signed certificate on Cloud expires as per policy, the new certificate needs to be imported
                                          to the CVP Server. |
|---|---|

| Property | Description | Configurable/ Non-Configurable? | Value |
|---|---|---|---|
| IVR.AuthTokenRefresh TimeOut | Time in seconds after which AuthToken is refreshed | Yes | 1800 |
| IVR.SurveyTokenRefresh TimeOut | Time in seconds after which SurveyToken is refreshed | Yes | 43200 |
| IVR.SurveyQuestionRefresh TimeOut | Time in seconds after which SurveyQuestions is refreshed | Yes | 43200 |
| IVR.WxmSurveyToken ApiUrl | Url to connect to fetch the survey token from Wxm | Yes | https://api.getcloudcherry.com/api/SurveyToken |
| IVR.WxmSurveyQuestions ApiUrl | Url to connect to fetch the questionnaire from Wxm | Yes | https://api.getcloudcherry.com/api/Questions/ Questionnaire |
| IVR.WxmSurveyAnswers SubmitApiUrl | Url to connect to submit the answers to Wxm | Yes | https://api.getcloudcherry.com/api/Survey ByToken/ |
| IVR.WxmSurveySettings ApiUrl | Url to connect to fetch the settings of the questionaire from Wxm | Yes | https://api.getcloudcherry.com/api/Settings/ |
| IVR.WxmAudio Url | Url to connect to fetch the audio files from Wxm | Yes | https://api.getcloudcherry.com/api/Stream UserAsset/ |
| IVR.WxmSurveyQuestionnaire Url | Url to connect to fetch the questionnaire settings from Wxm | Yes | https://api.getcloudcherry.com/api/surveyquestionnaire/ |

| Property | Description | Configurable/Non-Configurable? | Value |
|---|---|---|---|
| SIP.CloudCherry.SurveyValidity Time | Time in seconds for which the survey is active | Yes | 60000 |
| SIP.CloudConnect.SurveyDispatch EndPointApi | Url for connecting Cloud Connect to get the SurveyDispatch EndPoint | Yes | /cherrypoint/surveydispatch |
| SIP.CloudConnect.Auth TokenApi | Url for connecting Cloud Connect to get AuthToken for Wxm | Yes | /cherrypoint/authtoken |

| Sample |
|---|

| Property | Description | Configurable/ Non-Configurable? | Default Value |
|---|---|---|---|
| IVR.CloudCherryBatchSize | Batch size for triggering the Email/SMS Cloud Connect API | Yes | 100 |
| IVR.CloudCherryBatch Timeout | Batch timeout (in seconds) for triggering the Email/SMS Cloud Connect API | Yes | 60 |

| Note | Customers can optimize these values based on their deployment requirements. |
|---|---|

| Property | Description | Configurable/ Non-Configurable? | Value |
|---|---|---|---|
| SIP.CloudConnect.Request Timeout | HTTP request connection timeout (in milliseconds) towards Cloud Connect component | Yes | 10000 Note The timeout value can be increased as per environment. | Note | The timeout value can be increased as per environment. |
| Note | The timeout value can be increased as per environment. |

| Note | The timeout value can be increased as per environment. |
|---|---|

| Sample |
|---|

| Step 1 | Open Windows regedit in the VXML server. |
|---|---|
| Step 2 | Go to HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Apache Software Foundation\Procrun 2.0\VXMLServer\Parameters\Java\Options . |
| Step 3 | Add the following entries: -Dhttp.proxyHost=<proxy IP>
-Dhttp.proxyPort=<proxy port>
-Dorg.asynchttpclient.useProxyProperties=true
-Dhttp.nonProxyHosts=<hostname> |
| Step 4 | Restart the CVP VXML server from Windows services. |