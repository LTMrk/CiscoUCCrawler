---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-15-0-1-adminconfig-guide-ccvb-b-15-89363f31e6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/vvb_15_0_1/adminconfig/guide/ccvb_b_150_cisco-virtualized-voice-browser-administration-and-configuration-guide/cisco_vvb_introduction.html
retrieved_at: 2026-08-21T16:30:14.540878+00:00
---

Cisco Virtualized Voice Browser Administration and Configuration Guide, Release 15.0(1)

# Cisco Virtualized Voice Browser Administration and Configuration Guide, Release 15.0(1)

Updated: December 12, 2025

Chapter: Cisco VVB Introduction

## Chapter: Cisco VVB Introduction

# Cisco VVB Introduction

Cisco Virtualized Voice Browser (VVB) is designed to facilitate concurrent multimedia communication processing.

Cisco VVB has the following features:

Facilitates self-service options such as access to check account information or user-directed call routing by processing user
                              commands through touchtone input or speech-recognition technologies.

Allows customers to retrieve the required information through voice commands without interacting with an agent, to navigate
                              to the correct department, or to get help from an agent.

Provides multilingual support for Cisco VVB server prompts for automated speech recognition (ASR) and text-to-speech (TTS)
                              capabilities.

Provides more comprehensive and effective customer service by efficiently handling call traffic with self-service or fast
                              transfer to the correct agent the first time.

## Cisco VVB Web
                        	 Interfaces

You can
                           		use a web browser to administer Cisco VVB. Cisco VVB provides the following two
                           		web interfaces:

Cisco VVB Administration — Based on the selected mode configuration, you can use this web interface to configure system parameters, configure media gateway or configure applications, or both, configure subsystems, and so on.

Cisco VVB Serviceability —Use this web interface to view alarm and trace definitions for Cisco VVB services, start and stop engine or media gateway depending on the configured mode, change mode, monitor engine activity, and so on.

If you are
                                                   					 using Microsoft Internet Explorer or Mozilla Firefox, ensure that the popup
                                                   					 blocker is disabled.

Multiple Web sessions for same user are not supported.

The current mode for Cisco VVB Administration and Cisco VVB Serviceability is displayed on the top right corner of the window.

### Accept security certificates

Ensure that the pop-ups are enabled for Cisco VVB Administration .

If you receive a certificate expiry notification, it means that the validity of your CA certificate is about to expire. You
                                 can delete the certificate after expiry. If you use any CA to sign your certificates, you must upload the new certificates
                                 to ensure that your system remains operational. It isn’t required to upload certain CA certificates that come with the platform
                                 and can be deleted when they expire. For the complete list of CAs that can be safely deleted after expiry, refer to the Manage Expired CA Certificates section in the Cisco Unified Contact Center Express Administration and Operations Guide . This update is available from release 12.5(1) SU1 onwards.

After you enter Cisco VVB Administration URL in your browser, the procedure to add a certificate is as follows:

#### Install certificates on Windows operating system:

The procedure to add a certificate varies for each browser. The procedure for each
                                 browser is as follows:

Internet Explorer

If you’re using a Windows client, signed in as a Windows user, you must run Internet Explorer as an administrator to install
                                                the security certificates. In your Start menu, right-click Internet Explorer and select Run as administrator.

Contact your administrator if you don’t have the required permissions to install the security certificates.

A page appears that states there’s a problem with the website's security certificate. Click Continue to this website (not recommended) link to open the Cisco VVB Administration sign in page. the Cisco VVB Administration sign in screen appears with a certificate error in the address bar.

Click on the certificate error that appears in the address bar and then click View Certificates .

In the Certificate dialog box, click Install Certificate to open the Certificate Import Wizard .

Select Current User to install the certificate for the current user only, or select Local Machine to install the certificate for all Windows users.

On the Certificate Import Wizard , click Next .

Select Place all certificates in the following store and click Browse .

Select Trusted Root Certification Authorities and click OK .

Click Next and then click Finish . A Security Warning dialog box appears.

Click Yes to install the certificate. The Certificate Import dialog box appears.

Click OK and close the Certificate Import dialog box.

Close the browser tab. The accepted certificate link is removed from the SSL Certificate Not Accepted dialog box.

Repeat the preceding steps for all the certificate links. After you accept all the certificates, the sign-in process is complete.

To remove the certificate error from the desktop, you must close and reopen your browser.

Firefox

On the Your connection is not secure page, click Advanced > Add Exception .

Ensure that the Permanently store this exception box is checked.

Click Confirm Security Exception .

On Cisco VVB Administration sign in page, enter your username and password, and click Sign In .

In the SSL Certificate Not Accepted dialog box, click
                                       the certificate link. A browser tab opens for the certificate that you must
                                       accept.

On the browser tab, click I Understand the Risks > Add Exception . Ensure that the Permanently store this exception box is
                                       checked.

Click Confirm Security Exception . The browser tab closes after you accept the certificate and the accepted certificate link is removed from the SSL Certificate Not Accepted dialog box. Close the browser tab if it doesn’t automatically close.

Repeat the preceding steps for all the certificate links. After you accept all the
                                 certificates, the sign-in process is complete.

Chrome and Edge Chromium (Microsoft Edge)

A page appears that states your connection isn’t private. To open Cisco VVB Administration sign in page,

In Chrome, click Advanced > Proceed to
                                          <Hostname> (unsafe) .

In Microsoft Edge, click Advanced > Continue to <Hostname> (unsafe) .

Enter your agent ID or username, password, and extension, and then click Sign In .

In the SSL Certificate Not Accepted dialog box, click
                                       the certificate link. A browser tab opens for the certificate that you must
                                       accept.

On the browser tab,

In Chrome, click Advanced > Proceed to
                                          <Hostname> (unsafe) .

In Microsoft Edge, click Advanced > Continue to <Hostname> (unsafe) .

The browser tab closes after you accept the certificate and the accepted certificate link is removed from the SSL Certificate Not Accepted dialog box. Close the browser tab if it doesn’t automatically close.

If you click the certificate link and don’t accept it, the certificate link stays enabled in the SSL Certificate Not Accepted dialog box. The certificate error appears every time you sign in. The procedure to permanently accept the certificate is
                                                   as follows.

Click on the certificate error that appears in the address bar and then,

In Chrome, select Certificate (Invalid) .

In Microsoft Edge, select Certificate (not valid) .

The Certificate dialog box appears.

In the Details tab, click Copy to
                                          File . The Certificate Export Wizard appears.

Click Next .

Keep the default selection DER encoded binary X.509
                                          (.CER) and click Next .

Click Browse and select the folder in which you want to save the certificate, enter a recognizable filename and click Save .

Browse to the folder where you’ve saved the certificate ( .cer file), right-click on the file, and click Install Certificate . The Certificate Import Wizard appears.

Keep the default selection Current User and click Next .

Select Place all certificates in the following store and click Browse . The Select Certificate
                                          Store dialog box appears.

Select Trusted Root Certification Authorities and
                                       click OK .

Click Next and then click Finish . A Security Warning dialog box appears that asks if you want to install the certificate.

Click Yes . A Certificate Import dialog box that states the import was successful appears.

Close the browser and sign in to Cisco VVB Administration . The security error doesn’t appear in the address bar.

#### Install certificates on macOS:

The procedure to download a certificate varies for each browser. The procedure for
                                 each browser is as follows:

Chrome

A warning page appears which states that your connection isn’t private. To open Cisco VVB Administration sign in page.

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

In the right pane of the Keychains dialog, browse to the certificate, right-click on the certificate, and select Get Info from the options that are listed. A dialog appears with more information about the certificate.

Expand Trust . From the When using this
                                          certificate drop-down, select Always
                                          Trust .

Close the dialog box that has more information about the certificate. A
                                       confirmation dialog box appears.

Authenticate the modification of Keychains by providing a password.

The certificate is now trusted, and the certificate error doesn’t appear on the address bar.

Firefox

In your Firefox browser enter Cisco VVB Administration URL . A warning page appears which states that there’s a security risk.

Click Advanced and then click the View Certificate link. The Certificate Viewer dialog box appears.

Click Details and then click Export . Save the certificate ( .crt file)
                                       in a local folder.

If the .crt file option isn’t available, select the .der option to save the certificate.

From the menu, select Firefox > Preferences . The Preferences page is displayed.

In the left pane, select Privacy & Security .

Scroll to the Certificates section and click View Certificates ... . The Certificate
                                          Manager window is displayed.

Click Import and select the certificate.

The certificate is now authorized, and the certificate error doesn’t appear on the address bar.

## Configure System
                        	 Parameters

The initial system parameter configuration is part of the Setup Wizard procedure (during installation).

G711A for A-law

G711U for u-law

G729

You can change the codec anytime after installation by navigating to System > System Parameters .

Only one codec can be configured.

G711 and G729 audio codecs with a sampling rate of 8K are supported.

G729 is not supported for ASR and TTS integrations.

## Pre-configured
                        	 Cisco VVB Applications

The following
                           		applications are pre-configured on the Cisco VVB:

Script

Description

Pre-configured Dial Number

CVPComprehensive

Used for
                                       					 comprehensive calls.

7777777777*

Ringtone

Used for
                                       					 playing ringtone and whisper.

919191*

Error

Used for
                                       					 playing error tone.

929292*

VRUComprehensive

Used for VRU-only calls

Customer can configure the dial number.

| Note | If you are
                                                   					 using Microsoft Internet Explorer or Mozilla Firefox, ensure that the popup
                                                   					 blocker is disabled. Multiple Web sessions for same user are not supported. The current mode for Cisco VVB Administration and Cisco VVB Serviceability is displayed on the top right corner of the window. |
|---|---|

| Note | If you’re using a Windows client, signed in as a Windows user, you must run Internet Explorer as an administrator to install
                                                the security certificates. In your Start menu, right-click Internet Explorer and select Run as administrator. Contact your administrator if you don’t have the required permissions to install the security certificates. |
|---|---|

| Note | To remove the certificate error from the desktop, you must close and reopen your browser. |
|---|---|

| Note | Ensure that the Permanently store this exception box is checked. |
|---|---|

| Note | If you click the certificate link and don’t accept it, the certificate link stays enabled in the SSL Certificate Not Accepted dialog box. The certificate error appears every time you sign in. The procedure to permanently accept the certificate is
                                                   as follows. |
|---|---|

| Note | If the .crt file option isn’t available, select the .der option to save the certificate. |
|---|---|

| Note | You can change the codec anytime after installation by navigating to System > System Parameters . Only one codec can be configured. G711 and G729 audio codecs with a sampling rate of 8K are supported. G729 is not supported for ASR and TTS integrations. |
|---|---|

| Script | Description | Pre-configured Dial Number |
|---|---|---|
| CVPComprehensive | Used for
                                       					 comprehensive calls. | 7777777777* |
| Ringtone | Used for
                                       					 playing ringtone and whisper. | 919191* |
| Error | Used for
                                       					 playing error tone. | 929292* |
| VRUComprehensive | Used for VRU-only calls | Customer can configure the dial number. |