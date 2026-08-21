---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-150-user-g-644dbc4bed
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_150/user/guide/cuic_b_1501_user-guide/cuic_m_1501_introduction-to-cisco-unified-intelligence-center.html
retrieved_at: 2026-08-21T04:42:24.845758+00:00
---

Cisco Unified Intelligence Center User Guide, Release 15.0(1)

# Cisco Unified Intelligence Center User Guide, Release 15.0(1)

Updated: April 30, 2025

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

## Access Unified Intelligence Center

The URL for logging in to the Unified Intelligence Center reporting application is :

HTTPS

https://<HOST>:8444/cuicui/Main.jsp

Where HOST is the DNS name of a Unified Intelligence Center node.

Cisco Unified Intelligence Center does not support HTTP. From Cisco Unified Intelligence Center Release 12.6(1), port 8081 is not supported.

From release 12.6(1), Cisco Unified Intelligence Center supports custom logon message for users. If your administrator has defined the custom logon messages, then the message is
                              displayed in the Sign In page.

Custom logon messages are not displayed to users signing in with SSO.

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

Google Chrome 126 or later

Edge Chromium 131 or later

Firefox 134 or later

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

## Accessibility

Cisco Unified Intelligence Center supports a robust set of accessibility features to ensure that all users can interact with
                           the platform effectively. The following sections outline the new enhancements and best practices that align with the Web Content
                           Accessibility Guidelines (WCAG) and other accessibility standards.

Cisco Unified Intelligence Center adopts the Web Content Accessibility Guidelines (WCAG) 2.1, Level A and Level AA. For more
                           information, refer to https://www.cisco.com/c/en/us/about/accessibility.html . They provide recommendations to make web content more accessible to users with vision, hearing, and cognitive impairments,
                           enhancing overall usability.

The following are the various accessibility enhancements in Cisco Unified Intelligence Center:

Screen Reader Support

Localization

Color Contrast

Focus Indicators

Display Headers, Titles and Accessible Labels

Display Tool-tips on Hover

Search Gadget

Skip to Content, Landmarks

If you are using Mac keyboard, then press Option instead of Alt . For example, for Language Selector Drop-Down press Option–Down Arrow.

### Screen Reader Support

Cisco Unified Intelligence Center also supports JAWS screen reading software for the following elements.

For more information on the supported JAWS version, see Voluntary Product Accessibility Templates (VPAT) report for Contact
                              Center at https://www.cisco.com/c/en/us/about/accessibility/voluntary-product-accessibility-templates.html .

### Localization

Cisco Unified Intelligence Center supports the localization of labels. This ensures that users who rely on screen readers
                              or other assistive technologies can accurately identify and interact with these elements, regardless of the language or regional
                              settings.

### Color Contrast

High color contrast is crucial for users with visual impairments, including color blindness. Cisco Unified Intelligence Center
                              ensures text and interactive elements maintain a contrast ratio of at least 4.5:1, as recommended by WCAG. The application
                              avoids using color as the sole method of conveying information and conducts regular testing to ensure compliance with contrast
                              requirements.

### Focus Indicators

Focus indicators are visual markers that help users navigate through the application using a keyboard. Cisco Unified Intelligence
                              Center provides clear and consistent focus indicators for all interactive elements.

Keyboard Navigation : Users can navigate through all interactive elements using the Tab key or other keyboard shortcuts.

Visible Focus Indicators : When an element receives focus, a visible outline or highlight is displayed to indicate that it is active.

### Display Headers, Titles, and Accessible Labels

Properly structured headers, titles, and labels are crucial for accessibility, as they help users navigate content more easily.
                              Cisco Unified Intelligence Center ensures that all pages and sections are appropriately labeled and organized.

Hierarchical Structure : Headers are used to organize content hierarchically, allowing screen reader users to navigate through sections efficiently.

Descriptive Titles : Page titles and section headers are descriptive, providing users with a clear understanding of the content.

Accessible Labels : Form fields and interactive elements are labeled with clear and descriptive text, ensuring that all users can understand
                                    their purpose.

Cisco Unified Intelligence Center provides accessible labels for drop-down list with values identical to their visual labels
                                    to provide a consistent experience for all users, including those using screen readers. This alignment helps both visual and
                                    non-visual users to have the same experience, making training and usage more intuitive.

### Display Tooltips on Hover

Tooltips provide additional information about interface elements when a user hovers over them. Cisco Unified Intelligence
                              Center supports accessible tooltips that are easily readable and discoverable.

Tooltips appear when users hover over or focus on an element, making them accessible to both mouse users and those navigating
                              via keyboard. They are designed with sufficient contrast and displayed in a readable font size, ensuring readability. Additionally,
                              tooltips are announced by screen readers when the associated element receives focus, providing access to the same information
                              for users relying on assistive technology.

### Search Gadget

Ensuring that users can locate content in various ways is a key aspect of accessibility, particularly under the WCAG SC 2.4.5
                              guidelines. This emphasizes providing multiple methods for users to find information, catering to diverse needs and preferences.

Use the search functionality in the Cisco Unified Intelligence Center to quickly find and access components, or tabs from
                              the list. The items are organized by their respective tabs, with the tab name appearing first, followed by the component name.

### Skip to Content, Landmarks

The "Skip to Content" link aligns with the WCAG 2.4.1 Bypass Blocks guideline, part of the Web Content Accessibility Guidelines
                              (WCAG). This guideline ensures users can bypass repetitive content blocks and directly access the main content, enhancing
                              the overall accessibility and usability of the Cisco Unified Intelligence Center.

Users relying on keyboards, screen readers, switch controls, and other assistive technologies use 'Skip to Content' links
                              to navigate to the main content or other important sections more easily and quickly.

Landmarks enable visually challenged users with screen readers to easily navigate to different sections of a webpage. The
                              Cisco Unified Intelligence Center effectively utilizes these landmarks, including a header section (HTML element <header> ) at the top of the desktop page, a main section (HTML element <main> ) for all the main content, and a navigation bar section (HTML element <nav> within <navbar> ) on the left side of the desktop page.

| Note | Cisco Unified Intelligence Center does not support HTTP. From Cisco Unified Intelligence Center Release 12.6(1), port 8081 is not supported. |
|---|---|

| Note | Custom logon messages are not displayed to users signing in with SSO. |
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

| Note | If you are using Mac keyboard, then press Option instead of Alt . For example, for Language Selector Drop-Down press Option–Down Arrow. |
|---|---|