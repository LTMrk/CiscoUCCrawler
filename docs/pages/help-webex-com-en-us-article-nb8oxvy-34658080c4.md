---
doc_id: help-webex-com-en-us-article-nb8oxvy-34658080c4
source_url: https://help.webex.com/en-us/article/nb8oxvy
retrieved_at: 2026-11-02T13:00:35.578815+00:00
---

- Requirements

- Integrate

- Use

## Prerequisites

The CRM connector operates based on the version of the widget specified in the desktop layout JSON. It is extremely important to ensure the widget version within the Desktop Layout is kept updated. As of November 2025 , the latest widget version is 2.1.5 .

Administrators are expected to ensure all desktop layouts for this CRM connector use this widget version. If the layout is not updated to use the latest version, functionality will no longer be supported and may cease to work correctly.

The minimum supported size for the softphone interface is 500px. Any value lower than 500px may result in display or functionality issues.

Before you integrate Webex Contact Center with the Freshdesk CRM console, ensure that you have the following:

Access to Webex Contact Center.

Administrator access to the Control Hub at https://admin.webex.com and the Webex Contact Center Management Portal. The URLs for the Management Portal are specific to your region.

An agent with access to the Desktop. The URL for the Desktop is specific to your region.

Agent access to the following domain that is added to the Content Security Policy Allowed List:

*.freshdesk.com

A valid Freshdesk account login with administrator privileges. To create an account or trial, visit https://freshdesk.com/ and click Start Free Trial .

Access to the Desktop Layout (JSON) for Freshdesk at https://github.com/CiscoDevNet/webex-contact-center-crm-integrations/tree/main/Freshdesk .

SSO is supported via Webex Control Hub if Freshdesk and Webex Contact Center use the same third-party Identity Provider (IDP).

Agents will need to log in into the Freshdesk Desktop web application first and then launch the Webex Contact Center Agent Desktop.

This Desktop integration supports Voice only (both Inbound and Outbound).

To integrate Webex Contact Center with the Freshdesk CRM console, complete the following tasks:

Install Webex Contact Center for Freshdesk

Set up Freshdesk Desktop Layout on Webex Contact Center

Install Webex Contact Center for Freshdesk

Sign in to your Freshdesk account.

Navigate to the Admin screen.

Enter app in the search bar and then click the Apps screen under Support Operations .

Enter webex in the search bar, click the Webex Contact Center application.

Click Install .

On the Settings screen, perform the following tasks:

Enter the correct Webex Contact Center platform URL for your region of operation:

Enter the generated Freshdesk API key.

Click your profile picture icon on the top-right corner and click Profile Settings .

On the right pane, you will find Your API Key .

Copy and paste this API key on the Settings screen.

Enter your Freshdesk subdomain. It's in the URL, the name which appears before (.Freshdesk.com) in the URL.

Choose the correct Screen Pop type.

Choose the correct Phone Number format for your contacts.

The system uses the ANI (Automatic Number Identification) from Webex Contact Center for screen-pop lookups and phone number format.

Click Install .

When installed, you'll see the following screen:

Refresh the Freshdesk CRM and click the Webex Contact Center icon on the bottom-left side of the sidebar to open the Webex Contact Center desktop.

Set up Freshdesk Desktop Layout on Webex Contact Center

Before you begin

You can download the Desktop Layout JSON file for Freshdesk from https://github.com/CiscoDevNet/webex-contact-center-crm-integrations/tree/main/Freshdesk .

Use the latest Freshdesk_Desktop_<version>.json file for the Webex Contact Center Desktop Layout.

For more information about the Webex Contact Center Management Portal Desktop Layout, see the Provisioning chapter of the Cisco Webex Contact Center Setup and Administration Guide .

Sign in to the Webex Contact Center Management Portal with the appropriate credentials.

From the navigation bar, choose Provisioning > Desktop Layout .

Click New Layout and enter the details for the desktop layout.

Upload the Freshdesk Desktop Layout JSON file.

Click Save .

You can now start the Webex Contact Center Desktop within the Freshdesk CRM console.

Uninstall Webex Contact Center for Freshdesk

If you have an older version of the Webex Contact Center for Freshdesk App, uninstall the outdated version before you install the latest version.

Sign in to your Freshdesk account.

Navigate to Settings > Admin on the left pane.

Enter app in the search bar and then click the Apps screen under Support Operations .

Click the Settings icon and then click Uninstall .

Click Uninstall to confirm.

- We support signing into Agent Desktop using WebRTC for Salesforce (SFDC) and Microsoft Dynamics (MS Dynamics) Connectors only.

- Currently, this feature is applicable to agents only.

## Before you make Outdial Calls

Before you make outdial calls, ensure that you do the following:

Create the outdial entry point and set up an outdial entry point strategy.

Enable outdial ANI for the Agent Profile.

Set the outdial ANI to a Dial Number-to-Entry Point mapping.

For more information, see the Provisioning chapter of the Cisco Webex Contact Center Setup and Administration Guide .

For information on how to use Desktop, see the Cisco Webex Contact Center Agent Desktop User Guide .

Start the Integrated Webex Contact Center Desktop for Freshdesk

Sign in to the Freshdesk agent console at https://<your-instance>.freshdesk.com/ .

Click the Webex Contact Center icon from the toolbar on the lower left corner of the Freshdesk console.

The integrated Webex Contact Center Desktop appears on the Freshdesk console.

Click Sign In .

Sign in with your Webex Contact Center Desktop credentials.

Enter the Dial Number (DN) and Team information.

You need to enter the DN and Team name the first time you sign into Webex Contact Center for Freshdesk. For subsequent sessions, the same DN and Team name appear in the application automatically.

If you are running Freshdesk in multiple tabs on your browser window, the Webex Contact Center application is active in only one tab.

You can click the Webex Contact Center icon at any time to minimize the application and continue to work on Freshdesk.

Manage Incoming Calls

Sign in to the Freshdesk agent console at https://<your-instance>.freshdesk.com/ .

Click the Webex Contact Center icon from the toolbar on the lower left corner of the Freshdesk console.

The integrated Webex Contact Center Desktop appears on the Freshdesk console.

Click Sign In .

Sign in with your Webex Contact Center Desktop credentials.

The Webex Contact Center application can only run from one Freshdesk tab in your browser window at a time.

Change the agent status to Available .

During inbound calls, the following situations occur:

No customer record match : If no match is found for the ANI (caller number identifier) in the contact’s phone or mobile number, the system creates a new contact and opens a contact or ticket window. This is determined by the configuration settings.

Single match : If a single match is found for the ANI in the contact’s phone or mobile number, then the contact or ticket window opens. This is determined by the configuration settings.

Multiple matches : If multiple matches are found for the ANI in the contact’s phone or mobile number, then a list of contacts will be displayed. The agent needs to select the correct contact on the upper left side and then the corresponding contact or ticket window opens. This is determined by the configuration settings.

Manage Outgoing Calls

Sign in to the Freshdesk agent console at https://<your-instance>.freshdesk.com/ .

Click the Webex Contact Center icon from the toolbar on the lower left corner of the Freshdesk console.

The integrated Webex Contact Center Desktop appears on the Freshdesk console.

Click Sign In .

Sign in with your Webex Contact Center Desktop credentials.

Enter the Dial Number (DN) and Team information.

You need to enter the DN and Team name the first time you sign into Webex Contact Center for Freshdesk. For subsequent sessions, the same DN and Team name appear in the application automatically.

If you’re running Freshdesk in multiple tabs on your browser window, the Webex Contact Center application is active in only one tab.

Search and open the customer or ticket record.

Locate and click the phone number that needs to be dialed.

Webex Contact Center Activity Log

The system creates a private note on the Freshdesk ticket displaying data from the Webex Contact Center interaction.

```
Entity API Name ................ :Task 
Task Subtype ................... :Call 
Status ......................... :Completed 
Call Object .................... :c##d##cb-e###-####-a##a-#c#b##f#a#d# 
Subject ........................ :Call ##.##.#### ##:## PM 
Activity Date .................. :####-##-## ##:##:## 
Call Type ...................... :INBOUND 
Call Disposition ............... :Case Inquiry(e#f#c#c#-cac#-###b-af##-ebf##d#ea###) 
Call Duration In Seconds ....... :## 
Contact Type ................... :Call 
Ringing Time ................... :##:##:## 
Wrapup Time .................... :##:##:## 
ANI ............................ :+########### 
DNIS ........................... :+########### 
Queue Name ..................... :FreshDesk_Demo_Q
```

| 1 | Sign in to your Freshdesk account. |
|---|---|
| 2 | Navigate to the Admin screen. |
| 3 | Enter app in the search bar and then click the Apps screen under Support Operations . |
| 4 | Enter webex in the search bar, click the Webex Contact Center application. |
| 5 | Click Install . |
| 6 | On the Settings screen, perform the following tasks: Enter the correct Webex Contact Center platform URL for your region of operation: Enter the generated Freshdesk API key. To find the Freshdesk API key: Click your profile picture icon on the top-right corner and click Profile Settings . On the right pane, you will find Your API Key . Copy and paste this API key on the Settings screen. Enter your Freshdesk subdomain. It's in the URL, the name which appears before (.Freshdesk.com) in the URL. Choose the correct Screen Pop type. Choose the correct Phone Number format for your contacts. The system uses the ANI (Automatic Number Identification) from Webex Contact Center for screen-pop lookups and phone number format. Click Install . When installed, you'll see the following screen: Refresh the Freshdesk CRM and click the Webex Contact Center icon on the bottom-left side of the sidebar to open the Webex Contact Center desktop. |

| 1 | Sign in to the Webex Contact Center Management Portal with the appropriate credentials. |
|---|---|
| 2 | From the navigation bar, choose Provisioning > Desktop Layout . |
| 3 | Click New Layout and enter the details for the desktop layout. |
| 4 | Upload the Freshdesk Desktop Layout JSON file. |
| 5 | Click Save . You can now start the Webex Contact Center Desktop within the Freshdesk CRM console. |

| 1 | Sign in to your Freshdesk account. |
|---|---|
| 2 | Navigate to Settings > Admin on the left pane. |
| 3 | Enter app in the search bar and then click the Apps screen under Support Operations . |
| 4 | Click the Settings icon and then click Uninstall . |
| 5 | Click Uninstall to confirm. |

| 1 | Sign in to the Freshdesk agent console at https://<your-instance>.freshdesk.com/ . |
|---|---|
| 2 | Click the Webex Contact Center icon from the toolbar on the lower left corner of the Freshdesk console. The integrated Webex Contact Center Desktop appears on the Freshdesk console. |
| 3 | Click Sign In . |
| 4 | Sign in with your Webex Contact Center Desktop credentials. |
| 5 | Enter the Dial Number (DN) and Team information. You need to enter the DN and Team name the first time you sign into Webex Contact Center for Freshdesk. For subsequent sessions, the same DN and Team name appear in the application automatically. If you are running Freshdesk in multiple tabs on your browser window, the Webex Contact Center application is active in only one tab. You can click the Webex Contact Center icon at any time to minimize the application and continue to work on Freshdesk. |

| 1 | Sign in to the Freshdesk agent console at https://<your-instance>.freshdesk.com/ . |
|---|---|
| 2 | Click the Webex Contact Center icon from the toolbar on the lower left corner of the Freshdesk console. The integrated Webex Contact Center Desktop appears on the Freshdesk console. |
| 3 | Click Sign In . |
| 4 | Sign in with your Webex Contact Center Desktop credentials. The Webex Contact Center application can only run from one Freshdesk tab in your browser window at a time. |
| 5 | Change the agent status to Available . During inbound calls, the following situations occur: No customer record match : If no match is found for the ANI (caller number identifier) in the contact’s phone or mobile number, the system creates a new contact and opens a contact or ticket window. This is determined by the configuration settings. Single match : If a single match is found for the ANI in the contact’s phone or mobile number, then the contact or ticket window opens. This is determined by the configuration settings. Multiple matches : If multiple matches are found for the ANI in the contact’s phone or mobile number, then a list of contacts will be displayed. The agent needs to select the correct contact on the upper left side and then the corresponding contact or ticket window opens. This is determined by the configuration settings. |

| 1 | Sign in to the Freshdesk agent console at https://<your-instance>.freshdesk.com/ . |
|---|---|
| 2 | Click the Webex Contact Center icon from the toolbar on the lower left corner of the Freshdesk console. The integrated Webex Contact Center Desktop appears on the Freshdesk console. |
| 3 | Click Sign In . |
| 4 | Sign in with your Webex Contact Center Desktop credentials. |
| 5 | Enter the Dial Number (DN) and Team information. You need to enter the DN and Team name the first time you sign into Webex Contact Center for Freshdesk. For subsequent sessions, the same DN and Team name appear in the application automatically. If you’re running Freshdesk in multiple tabs on your browser window, the Webex Contact Center application is active in only one tab. |
| 6 | Search and open the customer or ticket record. |
| 7 | Locate and click the phone number that needs to be dialed. |

## Figuras

![Freshdesk login screen for Webex Contact Center integration.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469055.jpg)

![Freshdesk screen pointing to the Admin icon in the left navigation.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469056.jpg)

![Freshdesk screen pointing to 'app' in the search bar and 'Apps' in the results under 'Support Operations.'](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469057.jpg)

![Freshdesk screen on the Apps page showing 'webexc' in the search bar and pointing to the Webex Contact Center option in under results.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469058.jpg)

![Freshdesk screen on the Webex Contact Center app page pointing to the 'Install' button.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469059.jpg)

![Freshdesk My Dashboard screen showing the profile picture drop-down menu, pointing to 'Profile settings.'](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469063.jpg)

![Freshdesk Profile settings screen pointing to 'Your API Key.'](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469064.jpg)

![Freshdesk Configuration screen showing the settings tab for the Webexcc Platform URL, Freshdesk API Key, and Freshdesk Sub-Domain.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469060.jpg)

![Freshdesk Apps screen showing Webex Contact Center under installed apps.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469061.jpg)

![Freshdesk screen showing Webex Contact Center icon in the bottom, left navigation.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469062.jpg)

![Freshdesk My Dashboard screen showing the Admin tab in the left navigation.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469065.jpg)

![Freshdesk Admin screen showing 'apps' in the search bar and 'Apps' in the results under 'Support Operations.'](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469066.jpg)

![Freshdesk Apps screen showing Webex Contact Center under installed apps, pointing to the settings icon and the option to 'Uninstall.'](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469067.jpg)

![Freshdesk screen with Webex Contact Center integration showing an inbound call example while in the Available state (single match).](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469070.jpg)

![Freshdesk screen with Webex Contact Center integration showing an inbound call example while in the Available state (multiple matches).](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469071.jpg)

![Freshdesk screen with Webex Contact Center integration showing a customer ticket and a phone number highlighted to click to dial.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469072.jpg)