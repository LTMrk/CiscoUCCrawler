---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-user-guide-uccx-b-1251su1-4ab6565a62
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/user/guide/uccx_b_1251su1reporting-user-guide/uccx_b_1252reporting-user-guide_chapter_01.html
retrieved_at: 2026-08-16T20:55:36.257420+00:00
---

Cisco Unified Contact Center Express Reporting User Guide, Release 12.5(1) SU1

# Cisco Unified Contact Center Express Reporting User Guide, Release 12.5(1) SU1

Updated: January 31, 2021

Chapter: Getting Started

## Chapter: Getting Started

# Getting Started

## Overview

Unified CCX users can access reports using Cisco Unified Intelligence Center and Cisco Finesse. Unified Intelligence Center
                           is a comprehensive, end-to-end reporting solution for Unified CCX. You can access Historical and Live Data reports.

With Unified Intelligence Center, you can complete the following tasks:

Generate and view reports.

Filter data in the reports by setting parameters.

View help for a report.

Create and view dashboards.

View permalinks for reports and dashboards.

Configure thresholds for grid data cells.

Schedule reports to run at selected intervals.

Import reports.

Export reports and report folders.

## Authorized
                        	 Users

The following user
                              		  groups can access the reports:

Agents—User can access the Live Data agent reports.

Supervisors—User can access the Live Data agent and supervisor reports.

Reporting users—User can access Historical reports and Live Data reports.

Live Data reports can only be run by agents, supervisors, and reporting users.

For more information on the maximum number of reporting users supported to run Live-Data Reports concurrently on Cisco Unified
                                                Intelligence Center, see the Reporting Scaling Considerations section in Solution Design Guide for Cisco Unified Contact Center Express .

## Start Unified
                        	 Intelligence Center

Access Unified
                              		  Intelligence Center only after the administrator completes the post
                              		  installation tasks for Unified CCX.

Step 1

Open a web
                                       			 browser.

Step 2

Use one of the following methods to access Unified Intelligence Center:

Enter the URL https://<host address> and click Cisco Unified Contact Center Express Reporting .

Enter the URL https://<host address>:8444/cuicui/Main.jsp .

Host address is the DNS name or IP address of the Unified CCX node.

Unified Intelligence Center does not support HTTP.

Step 3

Enter your
                                       			 username and password.

Step 4

Click Sign In .

If your administrator has set up custom logon message in Cisco Unified OS Administration, the message appears in a pop-up
                                                      window. Click OK to log in.

Custom logon messages are not displayed to users signing in with SSO.

## Trust Self-Signed Certificates

### Self-Signed Certificates

Ensure that the pop-ups are enabled for Cisco Unified Intelligence Center.

After you enter the Cisco Unified Intelligence Center URL in your browser, the
                              procedure to add a certificate is as follows:

### Install certificates on Windows operating system:

The procedure to add a certificate varies for each browser. The procedure for each
                              browser is as follows:

Internet Explorer

If you are using a Windows client, signed in as a Windows user, you must run Internet Explorer as an administrator to install
                                          the security certificates. In your Start menu, right-click Internet Explorer and select Run as administrator.

Contact your administrator if you do not have the required permissions to install the security certificates.

A page appears with the warning that there is a problem with the website's security certificate. Click Continue to this website (not recommended) link to open the Cisco Unified Intelligence Center sign in page. The sign in screen appears with a certificate error in the
                                    address bar.

Click on the certificate error that appears in the address bar and then click View Certificates .

In the Certificate dialog box, click Install Certificate to open the Certificate Import Wizard .

On the Certificate Import Wizard , click Next .

Select Place all certificates in the following store and click Browse .

Select Trusted Root Certification Authorities and click OK .

Click Next and then click Finish . A Security Warning dialog box appears.

Click Yes to install the certificate. The Certificate Import dialog box appears.

Click OK and close the Certificate Import dialog box.

Enter your credentials and click Sign In .

To remove the certificate error from the desktop, you must close and reopen your browser.

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

## View Cisco Unified Intelligence Center Help

In Cisco Unified Intelligence Center , two types of help are available:

Application-specific help : This help content explains how to use Unified Intelligence Center in general.

Report-specific help/Template help : This help content explains how to use the report. The help can describe the fields or provide details of the relationship
                                 between the fields, or it can explain how to interpret the data in the report. This help is available only if it has been
                                 created for the report.

For more information on how to add the template help to report, see Add Template Help section.

## Get Help on Cisco Unified Intelligence Center

Click the Help icon on the top right corner of each of the entity listing page to view help contents specific to that entity.

Click the Online Help button on the home page to access the help window for Cisco Unified Intelligence Center .

Ensure to accept the certificate to view the help content.

## Get Help on a
                        	 Report

To get help on a
                              		  report, perform the following steps

Step 1

From the Reports page, click the required report to open the
                                       			 report in the run mode.

Step 2

Click the Template Help icon in the report toolbar.

You can configure template help for the report from the Reports page > Add Help . For more information, see Add Template Help section.

| Note | To access Unified Intelligence Center Live Data reports, the supervisor should be assigned an agent extension. |
|---|---|

| Note | Live Data reports can only be run by agents, supervisors, and reporting users. For more information on the maximum number of reporting users supported to run Live-Data Reports concurrently on Cisco Unified
                                                Intelligence Center, see the Reporting Scaling Considerations section in Solution Design Guide for Cisco Unified Contact Center Express . |
|---|---|

| Step 1 | Open a web
                                       			 browser. |
|---|---|
| Step 2 | Use one of the following methods to access Unified Intelligence Center: Enter the URL https://<host address> and click Cisco Unified Contact Center Express Reporting . Enter the URL https://<host address>:8444/cuicui/Main.jsp . Note Host address is the DNS name or IP address of the Unified CCX node. Unified Intelligence Center does not support HTTP. | Note | Host address is the DNS name or IP address of the Unified CCX node. Unified Intelligence Center does not support HTTP. |
| Note | Host address is the DNS name or IP address of the Unified CCX node. Unified Intelligence Center does not support HTTP. |
| Step 3 | Enter your
                                       			 username and password. |
| Step 4 | Click Sign In . Note If your administrator has set up custom logon message in Cisco Unified OS Administration, the message appears in a pop-up
                                                      window. Click OK to log in. Custom logon messages are not displayed to users signing in with SSO. | Note | If your administrator has set up custom logon message in Cisco Unified OS Administration, the message appears in a pop-up
                                                      window. Click OK to log in. Custom logon messages are not displayed to users signing in with SSO. |
| Note | If your administrator has set up custom logon message in Cisco Unified OS Administration, the message appears in a pop-up
                                                      window. Click OK to log in. Custom logon messages are not displayed to users signing in with SSO. |

| Note | Host address is the DNS name or IP address of the Unified CCX node. Unified Intelligence Center does not support HTTP. |
|---|---|

| Note | If your administrator has set up custom logon message in Cisco Unified OS Administration, the message appears in a pop-up
                                                      window. Click OK to log in. Custom logon messages are not displayed to users signing in with SSO. |
|---|---|

| Note | If you are using a Windows client, signed in as a Windows user, you must run Internet Explorer as an administrator to install
                                          the security certificates. In your Start menu, right-click Internet Explorer and select Run as administrator. Contact your administrator if you do not have the required permissions to install the security certificates. |
|---|---|

| Note | To remove the certificate error from the desktop, you must close and reopen your browser. |
|---|---|

| Note | If .crt file option is not available, select .der option to
                                                save the certificate. |
|---|---|

| Note | Ensure to accept the certificate to view the help content. |
|---|---|

| Step 1 | From the Reports page, click the required report to open the
                                       			 report in the run mode. |
|---|---|
| Step 2 | Click the Template Help icon in the report toolbar. The report template help appears in a new browser window. You can configure template help for the report from the Reports page > Add Help . For more information, see Add Template Help section. |