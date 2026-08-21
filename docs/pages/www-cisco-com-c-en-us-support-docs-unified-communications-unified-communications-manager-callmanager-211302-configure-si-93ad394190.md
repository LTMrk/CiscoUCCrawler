---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-211302-configure-si-93ad394190
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/211302-Configure-Single-Sign-On-using-CUCM-and.html
retrieved_at: 2026-08-21T13:56:16.268767+00:00
---

Configure Single Sign-On with CUCM and AD FS 2.0

# Configure Single Sign-On with CUCM and AD FS 2.0

### Download Options

Updated: September 3, 2024

Document ID: 211302

Contents

## Contents

## Introduction

This document describes how to configure Single Sign-On (SSO) on Cisco Unified Communications Manager and Active Directory Federation Service.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communications Manager (CUCM)

- Basic Knowledge of Active Directory Federation Service (AD FS)

In order to enable SSO in your lab environment, you need this configuration:

- Windows Server with AD FS installed.

- CUCM with LDAP sync configured.

- An End User with the Standard CCM Super Users role selected.

### Components Used

The information in this document is based on these software and hardware versions:

- Windows Server with AD FS 2.0

- CUCM 10.5.2

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The procedure for AD FS 2.0 with Windows Server 2008 R2 is provided. These steps also work for AD FS 3.0 on Windows Server 2016.

## Download and Install AD FS 2.0 on your Windows Server

Step 1. Navigate to Download AD FS 2.0 .

Step 2. Ensure that you select the appropriate download based on your Windows Server.

Step 3. Move the downloaded file to your Windows Server.

Step 4. Proceed with the installation:

Step 5. When prompted, choose Federation Server :

Step 6.  Some dependencies are automatically installed. Once that is done, click Finish .

Now that you have AD FS 2.0 installed on your server, you need to add some configuration.

## Configure AD FS 2.0 on Your Windows Server

Step 1. If the AD FS 2.0 window did not automatically open after the install, click Start and search for AD FS 2.0 Management to open it manually.

Step 2. Choose AD FS 2.0 Federation Server Configuration Wizard .

Step 3.  Next, click Create a new Federation Service .

Step 4. For most environments, Stand-alone federation server is sufficient.

Step 5. Next, you are asked to choose a certificate. This field auto-populates as long as the server has a certificate.

Step 6. If you already have an AD FS database on the server, you need to remove it to continue.

Step 7. Finally, you are on a summary screen where you can click Next .

## Import the IdP Metadata to CUCM / Download the CUCM Metadata

Step 1. Update the URL with your Windows server hostname/FQDN and download the metadata from your AD FS server - https://hostname/federationmetadata/2007-06/federa tionmetadata.xml

Step 2. Navigate to Cisco Unified CM Administration > System > SAML Single Sign-On .

Step 3. Click Enable SAML SSO .

Step 4. If you receive an alert about Web Server Connections, click Continue .

Step 5. Next, CUCM instructs you to download the metadata file from your IdP.  In this scenario, your AD FS server is the IdP, and you downloaded the metadata in Step 1, so click Next .

Step 6. Click Browse > Select the .xml from Step 1 > Click Import IdP Metadata .

Step 7. A message indicates that the import was successful:

Step 8. Click Next .

Step 9. Now that you have the IdP metadata imported into CUCM, you need to import CUCM's metadata into your IdP.

Step 10. Click Download Trust Metadata File .

Step 11. Click Next .

Step 12. Move the .zip fileto your Windows Server and extract the contents to a folder.

## Import CUCM Metatdata to AD FS 2.0 Server and Create Claim Rules

Step 1. C lick Start and search for AD FS 2.0 Management .

Step 2. Click Required: Add a trusted relying party .

Note : If you do not see this option, you need to close the window and open it back up.

Step 3. Once you have the Add Relying Party Trust Wizard open, click Start .

Step 4. Here, you need to import the XML files that you extracted in step 12.  Select Import data about the relying party from a file and browse to the folder files and choose the XML for your publisher.

Note : Use the previous steps for any Unified Collaboration server on which you intend to utilize SSO.

Step 5. Click Next .

Step 6. Edit the Display Name and click Next .

Step 7. Choose Permit all users to access this relying party and click Next .

Step 8. Click Next again.

Step 9. On this screen, ensure that you have Open the Edit Claim Rules dialog for this relying party trust when the wizard closes checked, then click Close .

Step 10. The Edit Claim Rules window opens:

Step 11. In this window, click Add Rule .

Step 12. For Claim rule template , choose Send LDAP Attributes as Claims and click Next .

Step 13. On the next page, enter NameID for the Claim rule name .

Step 14. Choose Active Directory for the Attribute store .

Step 15. Choose SAM-Account-Name for the LDAP Attribute .

Step 16. Enter uid for Outgoing Claim Type .

Note : uid is not an option in the drop down list - it must be entered manually.

Step 17. Click Finish .

Step 18. The first rule is now finished. Click Add Rule again.

Step 19. Choose Send Claims Using a Custom Rule .

Step 20. Enter a Claim rule name .

Step 21. In the Custom rule field, paste this text:

c:[Type == " http://schemas.microsoft.com/ws/2008/06/identity/ claims/windowsaccountname"] => issue(Type = " http://schemas.xmlsoap.org/ws/2005/05/identity/cl aims/nameidentifier", Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = c.Value, ValueType = c.ValueType,Properties[" http://schemas.xmlsoap.org/ws/2005/05/ identity/claimproperties/format"] = "urn:oasis:names:tc:SAML:2.0:nameid-format:transie nt",Properties[" http://schemas.xmlsoap.org/ws/2005/05/ identity/claimproperties/namequalifier"] = " http://ADFS_FEDERATION_SERVICE_NAME/com/adfs/service/trust ", Properties[" http://schemas.xmlsoap.org/ws/2005/05/ identity/claimproperties/spnamequalifier"] = "CUCM_ENTITY_ID");

Step 22. Ensure that you change AD_FS_SERVICE_NAME and CUCM_ENTITY_ID to the appropriate values.

Note : If you are not sure about the AD FS Service Name, you can follow the steps  to find it.  The CUCM Entity ID can be pulled from first line in the CUCM metadata file.  There is an entityID on the first line of the file that looks like this, entityID=1cucm1052.sckiewer.lab,. You need to enter the underlined value into the appropriate section of the claim rule.

Step 23. Click Finish .

Step 24. Click OK .

Note : Claim rules are needed for any Unified Collaboration server on which you intend to utilize SSO.

## Finish SSO Enablement On CUCM And Run The SSO Test

Step 1. Now that the AD FS server is fully configured, you can go back to CUCM.

Step 2. You left off at the final configuration page:

Step 3. Select your End User which has the Standard CCM Super Users role selected and click Run SSO Test...

Step 4. Ensure that your browser allows pop-ups, and enter your credentials into the prompt.

Step 5. Click Close on the pop-up window, and then Finish .

Step 6. After a brief restart of the web applications, SSO is enabled.

## Troubleshoot

### Set SSO Logs to Debug

To set the SSO logs to debug, you have to run this command in the CLI of the CUCM: set samltrace level debug

The SSO logs can be downloaded from RTMT. The name of the log set is Cisco SSO .

### Find The Federation Service Name

To find the federation service name, click Start and search for AD FS 2.0 Management .

• Click on Edit Federation Service Properties… • While on the General tab, look for Federation Service name

### Dotless Certificate And Federation Service Name

If you receive this error message in the AD FS configuration wizard, you need to create a new certificate.

The selected certificate cannot be used to determine the Federation Service name because the selected certificate has a dotless (short-named) Subject name. Select another certificate without a dotless (short-named) Subject name, and then try again.

Step 1. Click Start and search for iis, then open Internet Information Services (IIS) Manager

Step 2. Click your server name.

Step 3. Click Server Certificates.

Step 4. Click Create Self-Signed Certificate.

Step 5. Enter the name you want for the alias of your certificate.

### Time is Out of Sync between the CUCM and IdP Servers

If you receive this error when you run the SSO test from CUCM, you need to configure the Windows Server to use the same NTP server(s) as the CUCM.

Invalid SAML response. This can be caused when time is out of sync between the Cisco Unified Communications Manager and IDP servers. Please verify the NTP configuration on both servers. Run "utils ntp status" from the CLI to check this status on Cisco Unified Communications Manager.

Once the Windows Server has the correct NTP servers specified, you need to perform another SSO test and see if the issue persists.  In some instances, it is necessary to skew the validity period of the assertion.  More detail on that process here.

## Related Information

- Technical Support & Documentation - Cisco Systems

### Revision History

5.0

03-Sep-2024

Machine Translation, Style Requirements, and Formatting, fixed alt text.

4.0

20-Jun-2023

Updated Introduction, Machine Translation, Style Requirements, and Formatting.

3.0

02-Mar-2022

Removing internal info

2.0

15-Nov-2021

Updating grammatical errors and description for SEO.

1.0

30-May-2017

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 5.0 | 03-Sep-2024 | Machine Translation, Style Requirements, and Formatting, fixed alt text. |
| 4.0 | 20-Jun-2023 | Updated Introduction, Machine Translation, Style Requirements, and Formatting. |
| 3.0 | 02-Mar-2022 | Removing internal info |
| 2.0 | 15-Nov-2021 | Updating grammatical errors and description for SEO. |
| 1.0 | 30-May-2017 | Initial Release |