---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-1-maintenance-guide-pcce-b-report-3aa1538c32
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_1/maintenance/guide/pcce_b_Reporting-User-Guide-12_6_1/pcce_b_cisco-packaged-contact-center-enterprise_chapter_01.html
retrieved_at: 2026-08-21T16:53:25.801280+00:00
---

Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.6(1)

# Cisco Packaged Contact Center Enterprise Reporting User Guide, Release 12.6(1)

Updated: May 10, 2021

Chapter: Introduction to Cisco Unified Intelligence Center

## Chapter: Introduction to Cisco Unified Intelligence Center

# Introduction to Cisco Unified Intelligence Center

## Overview

Cisco Unified Intelligence Center is a reporting platform for users of Cisco Contact Center products. It is a web-based application that provides Historical,
                           Real-time, and Live Data reporting and dashboards.

Unified Intelligence Center serves the following primary purposes:

Obtains data from the base solution's database. The base solution can be any of the Contact Center products.

Allows you to create custom queries to obtain specific data.

Customizes the visual presentation of the reports.

Customizes the report data.

Allows different groups of people to view specific data based on their roles.

### Customer Journey Analyzer

Unified Intelligence Center users can use the reporting platform to launch Customer Journey Analyzer using Analyzer from the left navigation pane.

You can customize the default Analyzer URL using the CLI set cuic analyzer url <urlname> .

For more information on the CLI, see Cisco Unified Intelligence Center Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

The Customer Journey Analyzer mines historical data from multiple data sources and systems to generate specific business views of data. The Analyzer visually
                              displays trends to help you identify patterns and gain insight for continuous improvement.

You must have completed the on boarding process for Cloud Connect to access Customer Journey Analyzer . Cloud Connect allows Cisco Contact Center on premises customers to connect to cloud services, such as Customer Journey Analyzer to use Business Metrics.

For more information, see Business Metrics related information in Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

For more information, see Business Metrics related information in Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

## Access Unified Intelligence Center

The URL for logging in to the Unified Intelligence Center reporting application is :

HTTPS

https://<HOST>:8444/cuicui/Main.jsp

Where HOST is the DNS name of a Unified Intelligence Center node.

Cisco Unified Intelligence Center does not support HTTP.

## Default Locale in Unified Intelligence Center

To specify a locale, install the language pack.

First time access to Cisco Unified Intelligence Center displays the sign in page in the browser locale. To change the locale,
                              click the username on the top-right corner of your screen and select the required locale from the drop-down list.

When you select a locale, the browser retains the locale information even after you sign out and sign in back to Cisco Unified Intelligence Center within the same browser.

Brazilian Portuguese

Chinese (Simplified)

Chinese (Traditional)

Danish

Dutch

English (U.S.)

French (France)

German

Italian

Japanese

Korean

Russian

Spanish (Spain)

Swedish

Polish

Turkish

Finnish

Norwegian

Čeština (Czech)

Bulgarian

Català (Catalan)

Hrvatski (Croatian)

Magyar (Hungarian)

Slovenčina (Slovak)

Slovenščina (Slovenian)

Српски (Serbian)

Română  (Romanian)

## Synchronize Cluster

System Configuration Administrator can use the Synchronize Cluster feature (link below the username on the top-right corner
                           of your user interface screen) to notify all nodes in the cluster to clear their local cache. This action synchronizes and
                           empties all caches in the cluster. Clearing the locale cache forces each node to go directly to the database for the requested
                           information.

Each node gets fresh data from the database. The data is automatically put into the local cache and accessed during future
                           requests. Data remains consistent in the database and hence there is no loss of information.

For more information, see Unified Intelligence Center Cache section in the Administration Console User Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

## Browser Support and
                           Self-Signed Certificates

Unified Intelligence Center supports:

Firefox ESR 68 and higher ESRs

Edge Chromium (Microsoft Edge V79 and later)

Chrome 76.0.3809 and higher

In the above mentioned browsers, ensure to manually close the certificate acceptance window to load the Live Data reports.

### Self-Signed Certificates

Ensure that the pop-ups are enabled for Cisco Unified Intelligence Center.

After you enter the Cisco Unified Intelligence Center URL in your browser, the
                              procedure to add a certificate is as follows:

### Install certificates on Windows operating system:

The procedure to add a certificate varies for each browser. The procedure for each
                              browser is as follows:

Firefox

A page appears with the warning that states this connection is untrusted.

On the browser tab, click I Understand the Risks > Add Exception .

On the Add Exception dialog box, ensure that Permanently store this exception box is
                                    checked.

Click Confirm Security Exception .

The warning page closes automatically.

Enter your credentials and click Sign In .

Repeat the preceding steps for all the certificate links. After you accept all the
                              certificates, the sign-in process is complete.

Chrome and Edge Chromium
                                    (Microsoft Edge)

A page appears with the warning that states that there is a problem with your
                                    website's security certificate.

In Chrome, click Advanced > Proceed to
                                       <Hostname> (unsafe) .

In Microsoft Edge, click Advanced > Continue to <Hostname> (unsafe) .

The sign in page opens and a certificate error appears in the address bar of
                                    your browser.

Click on the Certificate Error , and then,

In Chrome, click Certificate (Invalid) .

In Microsoft Edge, click Certificate (not valid) .

The Certificate dialog box appears.

In the Details tab, click Copy to
                                       File .

The Certificate Export Wizard dialog box appears.

Click Next .

Keep the default selection DER encoded binary X.509 (.CER) and click Next .

Click Browse and select the folder in which you want
                                    to save the certificate.

Enter a recognizable File name and click Save .

Click Next .

Click Finish .

A successful export message appears.

Click OK and close the Certificate Export
                                       Wizard .

Browse to the folder where you have saved the certificate file (.cer file),
                                    right click on the file, and click Install
                                       Certificate .

The Certificate Import Wizard dialog box appears.

Keep the default selection Current User and click Next .

Select Place all certificates in the following store and click Browse .

The Select Certificate Store dialog box appears.

Select Trusted Root Certification Authorities and
                                    click OK .

Click Next .

Click Finish .

A Security Warning dialog box appears asking if you
                                    want to install the certificate.

Click Yes . A Certificate Import dialog box states that the import was successful appears.

Click OK .

Enter your credentials and click Sign In .

Close the browser and sign in to Cisco Unified Intelligence Center. The security
                              error does not appear in the address bar.

### Install certificates on macOS:

The procedure to download a certificate varies for each browser. The procedure for
                              each browser is as follows:

Chrome and Edge Chromium
                                    (Microsoft Edge)

A warning page appears which states that your connection is not private. To
                                    open the Cisco Unified Intelligence Center sign in page,

In Chrome, click Advanced > Proceed to
                                       <Hostname> (unsafe) .

In Microsoft Edge, click Advanced > Continue to <Hostname> (unsafe) .

Click on the certificate error that appears in the address bar and then,

In Chrome, select Certificate (Invalid) .

In Microsoft Edge, select Certificate (Not Valid) .

A certificate dialog box appears with the certificate details.

Drag the Certificate icon to the desktop.

Double-click the certificate. The Keychain Access application
                                    opens.

In the right pane of Keychains dialog, browse to the certificate, right-click
                                    on the certificate, and select Get Info from the
                                    options that are listed. A dialog appears with more information about the
                                    certificate.

Expand Trust . From the When using this
                                       certificate drop-down, select Always
                                       Trust .

Close the dialog box that has more information about the certificate. A
                                    confirmation dialog box appears.

Authenticate the modification of Keychains by providing a password.

The certificate is now trusted, and the certificate error does not appear on
                                    the address bar.

Firefox

In your Firefox browser, enter the Cisco Unified Intelligence Center URL. A
                                    warning page appears which states that there is a security risk.

Click Advanced and then click View
                                       Certificate link. The Certificate
                                       Viewer dialog box appears.

Click Details and then click Export . Save the certificate ( .crt file)
                                    in a local folder.

If .crt file option is not available, select .der option to
                                                save the certificate.

From the menu, select Firefox > Preferences . The Preferences page is displayed.

In the left pane, select Privacy & Security .

Scroll to the Certificates section and click View Certificates ... . The Certificate
                                       Manager window is displayed.

Click Import and select the certificate.

The certificate is now authorized, and the certificate error does not appear
                                    on the address bar.

### Screen Resolution Support

Supported screen resolution for Cisco Unified Intelligence Center: 1366 x 768 or
                              higher.

| Note | You must have completed the on boarding process for Cloud Connect to access Customer Journey Analyzer . Cloud Connect allows Cisco Contact Center on premises customers to connect to cloud services, such as Customer Journey Analyzer to use Business Metrics. |
|---|---|

| Note | Cisco Unified Intelligence Center does not support HTTP. |
|---|---|

| Note | To specify a locale, install the language pack. |
|---|---|

| Brazilian Portuguese | Chinese (Simplified) | Chinese (Traditional) | Danish | Dutch |
|---|---|---|---|---|
| English (U.S.) | French (France) | German | Italian | Japanese |
| Korean | Russian | Spanish (Spain) | Swedish | Polish |
| Turkish | Finnish | Norwegian | Čeština (Czech) | Bulgarian |
| Català (Catalan) | Hrvatski (Croatian) | Magyar (Hungarian) | Slovenčina (Slovak) | Slovenščina (Slovenian) |
| Српски (Serbian) | Română  (Romanian) |  |  |  |

| Note | In the above mentioned browsers, ensure to manually close the certificate acceptance window to load the Live Data reports. |
|---|---|

| Note | If .crt file option is not available, select .der option to
                                                save the certificate. |
|---|---|