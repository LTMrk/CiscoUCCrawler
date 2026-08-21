---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-150-user-g-5956ea7a99
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_150/user/guide/cuic_b_report-customization-guide-1501/cuic_m_rcg-introduction-to-cuic-1501.html
retrieved_at: 2026-08-21T04:43:02.254751+00:00
---

Cisco Unified Intelligence Center Report Customization Guide, Release 15.0(1)

# Cisco Unified Intelligence Center Report Customization Guide, Release 15.0(1)

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

### Customer Journey Analyzer

Unified Intelligence Center users can use the reporting platform to launch Customer Journey Analyzer using Analyzer from the left navigation pane.

You can customize the default Analyzer URL using the CLI set cuic analyzer url <urlname> .

For more information on the CLI, see Cisco Unified Intelligence Center Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-maintenance-guides-list.html .

The Customer Journey Analyzer mines historical data from multiple data sources and systems to generate specific business views of data. The Analyzer visually
                              displays trends to help you identify patterns and gain insight for continuous improvement.

You must have completed the on boarding process for Cloud Connect to access Customer Journey Analyzer . Cloud Connect allows Cisco Contact Center on premises customers to connect to cloud services, such as Customer Journey Analyzer to use Business Metrics.

For more information, see Business Metrics related information in the corresponding solution Features Guide.

## Get Help on Cisco Unified Intelligence Center

Click the Help icon on the top right corner of each of the entity listing page to view help contents specific to that entity.

Click the Online Help button on the home page to access the help window for Cisco Unified Intelligence Center .

Ensure to accept the certificate to view the help content.

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

| Note | Ensure to accept the certificate to view the help content. |
|---|---|

| Note | If you are using Mac keyboard, then press Option instead of Alt . For example, for Language Selector Drop-Down press Option–Down Arrow. |
|---|---|