---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-user-guide--888915ffcf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/user/guide/ucce_b_cisco-unified-contact-center-enterprise-reporting-user-guide-release1501/ucce_b_cisco-unified-contact-center-enterprise-1261_chapter_01.html
retrieved_at: 2026-08-16T20:33:44.033704+00:00
---

Cisco Unified Contact Center Enterprise Reporting User Guide, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Reporting User Guide, Release 15.0(1)

Updated: April 30, 2025

Chapter: Cisco Unified Intelligence Center

## Chapter: Cisco Unified Intelligence Center

# Cisco Unified Intelligence Center

## Overview

Cisco Unified Intelligence Center is a reporting platform for users of Cisco Contact Center products. It is a web-based application that provides Historical,
                           Real-time, and Live Data reporting and dashboards.

Unified Intelligence Center serves the following primary purposes:

Obtains data from the base solution's database. The base solution can be any of the Contact Center products.

Allows you to create custom queries to obtain specific data.

Customizes the visual presentation of the reports.

Customizes the report data.

Allows different groups of people to view specific data based on their roles.

Unified Intelligence Center users can use the new interface to perform the following tasks:

Create and view Reports.

Schedule reports to run at selected intervals.

Import and export reports and report folders.

### Customer Journey Analyzer

Unified Intelligence Center users can use the reporting platform to launch Customer Journey Analyzer using Analyzer from the left navigation pane.

You can customize the default Analyzer URL using the CLI set cuic analyzer url <urlname> .

For more information on the CLI, see Cisco Unified Intelligence Center Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

The Customer Journey Analyzer mines historical data from multiple data sources and systems to generate specific business views of data. The Analyzer visually
                              displays trends to help you identify patterns and gain insight for continuous improvement.

You must have completed the on boarding process for Cloud Connect to access Customer Journey Analyzer . Cloud Connect allows Cisco Contact Center on premises customers to connect to cloud services, such as Customer Journey Analyzer to use Business Metrics.

For more information, see Business Metrics related information in the corresponding solution Features Guide.

For more information, see Business Metrics related information in Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

## Access Unified Intelligence Center

The URL s for logging in to the Unified Intelligence Center reporting application are :

HTTPS

https://<HOST>:8444/cuicui/Main.jsp

Where HOST is the DNS name of a Unified Intelligence Center node.

By default, Unified Intelligence Center does not support HTTP. From the command-line interface, you can set the cuic properties > http-enabled to on to enable HTTP. With HTTP enabled, Unified Intelligence Center loads the login page with HTTPS. After successful login, Unified Intelligence Center loads the main page with HTTP.

HTTP

http://<HOST>:8081/cuicui/Main.jsp

Where, HOST is the DNS name of a Unified Intelligence Center node.

When http-enabled is off , Unified Intelligence Center redirects all HTTP requests to HTTPS.

Permalinks work in both HTTP and HTTPS.

## Default Locale in Unified Intelligence Center

To specify a locale, install the language pack.

First time access to Cisco Unified Intelligence Center displays the sign in page in the browser locale. To change the locale,
                              click the username on the top-right corner of your screen and select the required locale from the drop-down list.

When you select a locale, the browser retains the locale information even after you sign out and sign in back to Cisco Unified Intelligence Center within the same browser.

When you access both the Unified Intelligence Center interfaces (new and legacy) simultaneously, the legacy interface reflects the current locale. However, when you change the
                                          locale from the new interface, the legacy interface needs a browser refresh to reflect the changed locale.

For Windows, press Fn + F5

For Mac, press command + R

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

## Browser Support and
                           Self-Signed Certificates

Google Chrome 126 or later

Edge Chromium 131 or later

Firefox 134 or later

Chrome support is only for the new user interface.

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

## Stock
                        	 Reports

The following report
                           		bundles are available as stock reports for Cisco Unified Intelligence Center:

Realtime and
                                 			 Historical Transitional templates - Introductory templates designed for new
                                 			 users. These templates are simplified versions of the All Fields templates, and
                                 			 are similar to templates available in other contact center solutions.

Realtime and
                                 			 Historical All Fields templates - Templates that provide data from all fields
                                 			 in a database. These templates are most useful as a basis for creating custom
                                 			 reports, and include templates for precision queue routing data.

Realtime and
                                 			 Historical Outbound templates - Templates for reporting on Outbound Option
                                 			 activity. Import these templates if your deployment includes Outbound Option.

Live Data templates - Templates for reports that use the Live Data stream processing system as a data source. Refresh rates
                                 for these reports are much faster than the Realtime or Historical reports--usually less than every 3 seconds. Reports are
                                 available for Agent, Agent Skill Group, Precision Queue, Skill Group, Recent State History and Recent Call History.

Contact Sharing
                                 			 templates - Templates for reporting on a Contact Sharing system. You can use
                                 			 the Contact Sharing reports to understand the current configuration and
                                 			 behavior of the Contact Sharing system. You can view data on the active
                                 			 configuration of the Contact Sharing routing, the number of calls routed to
                                 			 each target system for each group, and the calls that have errors during the
                                 			 routing process.

Cisco Unified
                                 			 Intelligence Center Admin Security templates - Templates to report on Cisco
                                 			 Unified Intelligence Server audit trails, permissions, and template ownership.

Realtime and Historical Customer Collaboration Platform templates - Templates for reporting on Customer Collaboration Platform activity. Import these templates if your deployment includes Customer Collaboration Platform .

The report bundles are available as downloads from Cisco.com. Click the Intelligence Center Reports link on the downloads page ( https://software.cisco.com/download/type.html?mdfid=282163829&catid=null ). Depending on how it was deployed, your installation of Unified Intelligence Center may include all or a subset of these
                           reports.

For information on importing report bundles or custom reports, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/prod_installation_guides_list.html . Navigate to Initial Configuration>Configure Cisco Unified Intelligence Center>Import Report Bundles.

## Customize Report
                        	 Templates

You can modify
                           		existing report templates or create custom reports templates if you determine
                           		that the stock report templates do not meet your reporting needs. For example,
                           		you might customize an existing report template to monitor a department's
                           		activity and performance by creating a collection with objects from only that
                           		department.

See the Cisco Unified Intelligence Center Report Customization Guide at https://www.cisco.com/en/US/products/ps9755/tsd_products_support_series_home.html for directions on customizing report templates.

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

| Note | You must have completed the on boarding process for Cloud Connect to access Customer Journey Analyzer . Cloud Connect allows Cisco Contact Center on premises customers to connect to cloud services, such as Customer Journey Analyzer to use Business Metrics. |
|---|---|

| Note | Permalinks work in both HTTP and HTTPS. |
|---|---|

| Note | To specify a locale, install the language pack. |
|---|---|

| Note | When you access both the Unified Intelligence Center interfaces (new and legacy) simultaneously, the legacy interface reflects the current locale. However, when you change the
                                          locale from the new interface, the legacy interface needs a browser refresh to reflect the changed locale. For Windows, press Fn + F5 For Mac, press command + R |
|---|---|

| Brazilian Portuguese | Chinese (Simplified) | Chinese (Traditional) | Danish | Dutch |
|---|---|---|---|---|
| English (U.S.) | French (France) | German | Italian | Japanese |
| Korean | Russian | Spanish (Spain) | Swedish | Polish |
| Turkish | Finnish | Norwegian | Čeština (Czech) | Bulgarian |
| Català (Catalan) | Hrvatski (Croatian) | Magyar (Hungarian) | Slovenčina (Slovak) | Slovenščina (Slovenian) |
| Српски (Serbian) | Română  (Romanian) |  |  |  |

| Note | Chrome support is only for the new user interface. |
|---|---|

| Note | If .crt file option is not available, select .der option to
                                                save the certificate. |
|---|---|

| Note | If you are using Mac keyboard, then press Option instead of Alt . For example, for Language Selector Drop-Down press Option–Down Arrow. |
|---|---|