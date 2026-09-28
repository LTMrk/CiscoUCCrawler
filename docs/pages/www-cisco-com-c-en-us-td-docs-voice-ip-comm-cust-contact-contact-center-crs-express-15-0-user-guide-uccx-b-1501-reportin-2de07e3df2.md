---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-15-0-user-guide-uccx-b-1501-reportin-2de07e3df2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_15_0/user/guide/uccx_b_1501_reporting_user_guide/uccx_m_1501_getting-started.html
retrieved_at: 2026-08-16T21:22:47.655194+00:00
---

Cisco Unified Contact Center Express Reporting User Guide, Release 15.0

# Cisco Unified Contact Center Express Reporting User Guide, Release 15.0

Updated: April 30, 2025

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

### Customer Journey Analyzer (Trials)

Unified Intelligence Center users can use the reporting platform to launch Customer Journey Analyzer using Analyzer icon from the left navigation pane.

Customer Journey Analyzer mines historical data from multiple data sources and systems to generate specific business views of data. The Analyzer visually
                              displays trends to help you identify patterns and gain insight for continuous improvement.

You can customize the default Analyzer URL using the CLI set cuic analyzer url <urlname> .

For more information on the CLI, see Cisco Unified Contact Center Express Administration and Operations Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

For more information, see Business Metrics chapter in Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html .

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

## Trust Self-Signed Certificate

When you access a server for the first time, the procedure to trust a self-signed certificate
                              				is as follows:

The following steps are for an Windows operating system.

Step 1

Start Unified Intelligence Center.

Step 2

Perform the following steps to trust the self-signed certificate:

If you use Internet Explorer or Microsoft Edge :

A page appears that states there is a problem with the website's security certificate.
                                                         										Click Continue to this website (not
                                                            											recommended) .

The Sign In page opens and a certificate error appears in the address bar of your
                                                         										browser.

Click Certificate Error , and then click View
                                                            											Certificates .

The Certificate dialog box appears.

On the Certificate dialog box, click Install Certificate .

The Certificate Import Wizard appears.

Click Next .

Select Place all certificates in the following store , and then click Browse .

Select Trusted Root Certification Authorities , and click OK .

Click Next .

Click Finish .

A Security Warning dialog box appears that asks if you want to
                                                         										install the certificate.

Click Yes .

A Certificate Import dialog box that states the import was
                                                         										successful appears.

Click OK .

Enter your credentials and click Sign In .

If you use Firefox:

A page appears that states this connection is untrusted.

Click I Understand the Risks , and then click Add
                                                            											Exception .

On the Add Security Exception dialog box, ensure the Permanently store this exception check box is checked.

Click Confirm Security Exception .

The page that states this connection is untrusted automatically closes.

Enter your credentials and click Sign In .

A page appears that states there is a problem with the
                                                         										website's security certificate. Click, Advanced > Proceed to
                                                            											<Hostname> (Unsafe) .

The Sign In page opens and a certificate error appears in the
                                                         										address bar of your browser.

Click on the Certificate Error , and
                                                         										then click, Certificate
                                                            										(Invalid) .

The Certificate dialog box appears.

In the Details tab, click Copy to File .

The Certificate Export Wizard appears.

Click Next .

Keep the default selection DER encoded binary X.509 (.CER) and click Next .

Click Browse and select the folder in which you want to save the certificate.

Enter a recognizable File name and click Save .

Click Next .

Click Finish .

A successful export message appears.

Click OK and close the Certificate Export Wizard .

Browse to the folder where you have saved the certificate (.cer file), right click on the file, and click Install Certificate .

The Certificate Import Wizard appears.

Keep the default selection Current User and click Next .

Select Place all certificates in the following store and click Browse .

The Select Certificate Store dialog box appears.

Select Trusted Root Certification Authorities and click OK .

Click Next .

Click Finish .

A Security Warning dialog box appears that asks if you want to install the certificate.

Click Yes .

A Certificate Import dialog box that states the import was successful appears.

Click OK .

Enter your credentials and click Sign In .

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
| Step 4 | Click Sign In . |

| Note | Host address is the DNS name or IP address of the Unified CCX node. Unified Intelligence Center does not support HTTP. |
|---|---|

| Note | The following steps are for an Windows operating system. |
|---|---|

| Step 1 | Start Unified Intelligence Center. |
|---|---|
| Step 2 | Perform the following steps to trust the self-signed certificate: Option Description If you use Internet Explorer or Microsoft Edge : A page appears that states there is a problem with the website's security certificate.
                                                         										Click Continue to this website (not
                                                            											recommended) . The Sign In page opens and a certificate error appears in the address bar of your
                                                         										browser. Click Certificate Error , and then click View
                                                            											Certificates . The Certificate dialog box appears. On the Certificate dialog box, click Install Certificate . The Certificate Import Wizard appears. Click Next . Select Place all certificates in the following store , and then click Browse . Select Trusted Root Certification Authorities , and click OK . Click Next . Click Finish . A Security Warning dialog box appears that asks if you want to
                                                         										install the certificate. Click Yes . A Certificate Import dialog box that states the import was
                                                         										successful appears. Click OK . Enter your credentials and click Sign In . If you use Firefox: A page appears that states this connection is untrusted. Click I Understand the Risks , and then click Add
                                                            											Exception . On the Add Security Exception dialog box, ensure the Permanently store this exception check box is checked. Click Confirm Security Exception . The page that states this connection is untrusted automatically closes. Enter your credentials and click Sign In . If you use Chrome: A page appears that states there is a problem with the
                                                         										website's security certificate. Click, Advanced > Proceed to
                                                            											<Hostname> (Unsafe) . The Sign In page opens and a certificate error appears in the
                                                         										address bar of your browser. Click on the Certificate Error , and
                                                         										then click, Certificate
                                                            										(Invalid) . The Certificate dialog box appears. In the Details tab, click Copy to File . The Certificate Export Wizard appears. Click Next . Keep the default selection DER encoded binary X.509 (.CER) and click Next . Click Browse and select the folder in which you want to save the certificate. Enter a recognizable File name and click Save . Click Next . Click Finish . A successful export message appears. Click OK and close the Certificate Export Wizard . Browse to the folder where you have saved the certificate (.cer file), right click on the file, and click Install Certificate . The Certificate Import Wizard appears. Keep the default selection Current User and click Next . Select Place all certificates in the following store and click Browse . The Select Certificate Store dialog box appears. Select Trusted Root Certification Authorities and click OK . Click Next . Click Finish . A Security Warning dialog box appears that asks if you want to install the certificate. Click Yes . A Certificate Import dialog box that states the import was successful appears. Click OK . Enter your credentials and click Sign In . | Option | Description | If you use Internet Explorer or Microsoft Edge : | A page appears that states there is a problem with the website's security certificate.
                                                         										Click Continue to this website (not
                                                            											recommended) . The Sign In page opens and a certificate error appears in the address bar of your
                                                         										browser. Click Certificate Error , and then click View
                                                            											Certificates . The Certificate dialog box appears. On the Certificate dialog box, click Install Certificate . The Certificate Import Wizard appears. Click Next . Select Place all certificates in the following store , and then click Browse . Select Trusted Root Certification Authorities , and click OK . Click Next . Click Finish . A Security Warning dialog box appears that asks if you want to
                                                         										install the certificate. Click Yes . A Certificate Import dialog box that states the import was
                                                         										successful appears. Click OK . Enter your credentials and click Sign In . | If you use Firefox: | A page appears that states this connection is untrusted. Click I Understand the Risks , and then click Add
                                                            											Exception . On the Add Security Exception dialog box, ensure the Permanently store this exception check box is checked. Click Confirm Security Exception . The page that states this connection is untrusted automatically closes. Enter your credentials and click Sign In . | If you use Chrome: | A page appears that states there is a problem with the
                                                         										website's security certificate. Click, Advanced > Proceed to
                                                            											<Hostname> (Unsafe) . The Sign In page opens and a certificate error appears in the
                                                         										address bar of your browser. Click on the Certificate Error , and
                                                         										then click, Certificate
                                                            										(Invalid) . The Certificate dialog box appears. In the Details tab, click Copy to File . The Certificate Export Wizard appears. Click Next . Keep the default selection DER encoded binary X.509 (.CER) and click Next . Click Browse and select the folder in which you want to save the certificate. Enter a recognizable File name and click Save . Click Next . Click Finish . A successful export message appears. Click OK and close the Certificate Export Wizard . Browse to the folder where you have saved the certificate (.cer file), right click on the file, and click Install Certificate . The Certificate Import Wizard appears. Keep the default selection Current User and click Next . Select Place all certificates in the following store and click Browse . The Select Certificate Store dialog box appears. Select Trusted Root Certification Authorities and click OK . Click Next . Click Finish . A Security Warning dialog box appears that asks if you want to install the certificate. Click Yes . A Certificate Import dialog box that states the import was successful appears. Click OK . Enter your credentials and click Sign In . |
| Option | Description |
| If you use Internet Explorer or Microsoft Edge : | A page appears that states there is a problem with the website's security certificate.
                                                         										Click Continue to this website (not
                                                            											recommended) . The Sign In page opens and a certificate error appears in the address bar of your
                                                         										browser. Click Certificate Error , and then click View
                                                            											Certificates . The Certificate dialog box appears. On the Certificate dialog box, click Install Certificate . The Certificate Import Wizard appears. Click Next . Select Place all certificates in the following store , and then click Browse . Select Trusted Root Certification Authorities , and click OK . Click Next . Click Finish . A Security Warning dialog box appears that asks if you want to
                                                         										install the certificate. Click Yes . A Certificate Import dialog box that states the import was
                                                         										successful appears. Click OK . Enter your credentials and click Sign In . |
| If you use Firefox: | A page appears that states this connection is untrusted. Click I Understand the Risks , and then click Add
                                                            											Exception . On the Add Security Exception dialog box, ensure the Permanently store this exception check box is checked. Click Confirm Security Exception . The page that states this connection is untrusted automatically closes. Enter your credentials and click Sign In . |
| If you use Chrome: | A page appears that states there is a problem with the
                                                         										website's security certificate. Click, Advanced > Proceed to
                                                            											<Hostname> (Unsafe) . The Sign In page opens and a certificate error appears in the
                                                         										address bar of your browser. Click on the Certificate Error , and
                                                         										then click, Certificate
                                                            										(Invalid) . The Certificate dialog box appears. In the Details tab, click Copy to File . The Certificate Export Wizard appears. Click Next . Keep the default selection DER encoded binary X.509 (.CER) and click Next . Click Browse and select the folder in which you want to save the certificate. Enter a recognizable File name and click Save . Click Next . Click Finish . A successful export message appears. Click OK and close the Certificate Export Wizard . Browse to the folder where you have saved the certificate (.cer file), right click on the file, and click Install Certificate . The Certificate Import Wizard appears. Keep the default selection Current User and click Next . Select Place all certificates in the following store and click Browse . The Select Certificate Store dialog box appears. Select Trusted Root Certification Authorities and click OK . Click Next . Click Finish . A Security Warning dialog box appears that asks if you want to install the certificate. Click Yes . A Certificate Import dialog box that states the import was successful appears. Click OK . Enter your credentials and click Sign In . |

| Option | Description |
|---|---|
| If you use Internet Explorer or Microsoft Edge : | A page appears that states there is a problem with the website's security certificate.
                                                         										Click Continue to this website (not
                                                            											recommended) . The Sign In page opens and a certificate error appears in the address bar of your
                                                         										browser. Click Certificate Error , and then click View
                                                            											Certificates . The Certificate dialog box appears. On the Certificate dialog box, click Install Certificate . The Certificate Import Wizard appears. Click Next . Select Place all certificates in the following store , and then click Browse . Select Trusted Root Certification Authorities , and click OK . Click Next . Click Finish . A Security Warning dialog box appears that asks if you want to
                                                         										install the certificate. Click Yes . A Certificate Import dialog box that states the import was
                                                         										successful appears. Click OK . Enter your credentials and click Sign In . |
| If you use Firefox: | A page appears that states this connection is untrusted. Click I Understand the Risks , and then click Add
                                                            											Exception . On the Add Security Exception dialog box, ensure the Permanently store this exception check box is checked. Click Confirm Security Exception . The page that states this connection is untrusted automatically closes. Enter your credentials and click Sign In . |
| If you use Chrome: | A page appears that states there is a problem with the
                                                         										website's security certificate. Click, Advanced > Proceed to
                                                            											<Hostname> (Unsafe) . The Sign In page opens and a certificate error appears in the
                                                         										address bar of your browser. Click on the Certificate Error , and
                                                         										then click, Certificate
                                                            										(Invalid) . The Certificate dialog box appears. In the Details tab, click Copy to File . The Certificate Export Wizard appears. Click Next . Keep the default selection DER encoded binary X.509 (.CER) and click Next . Click Browse and select the folder in which you want to save the certificate. Enter a recognizable File name and click Save . Click Next . Click Finish . A successful export message appears. Click OK and close the Certificate Export Wizard . Browse to the folder where you have saved the certificate (.cer file), right click on the file, and click Install Certificate . The Certificate Import Wizard appears. Keep the default selection Current User and click Next . Select Place all certificates in the following store and click Browse . The Select Certificate Store dialog box appears. Select Trusted Root Certification Authorities and click OK . Click Next . Click Finish . A Security Warning dialog box appears that asks if you want to install the certificate. Click Yes . A Certificate Import dialog box that states the import was successful appears. Click OK . Enter your credentials and click Sign In . |

| Note | Ensure to accept the certificate to view the help content. |
|---|---|

| Step 1 | From the Reports page, click the required report to open the
                                       			 report in the run mode. |
|---|---|
| Step 2 | Click the Template Help icon in the report toolbar. The report template help appears in a new browser window. You can configure template help for the report from the Reports page > Add Help . For more information, see Add Template Help section. |