---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-english-operating-system-guide-1-0-1-iptpch6-html-0d7a69753a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0/english/operating_system/guide/1_0_1/iptpch6.html
retrieved_at: 2026-08-21T02:47:15.683045+00:00
---

Cisco Unified Communications Operating System Administration Guide, Release 1.0(1)

# Cisco Unified Communications Operating System Administration Guide, Release 1.0(1)

Updated: July 17, 2006

Chapter: Security

## Chapter: Security

## Security

This chapter describes Certificate Management and IPSec Management and provides procedures for performing the following tasks:

• Manage Certificates and Certificate Trust Lists

• Display Certificates

• Download a Certificate or CTL

• Delete and Regenerate a Certificate

• Upload a Certificate or Certificate Trust List

• Download a Certificate Signing Request

• Monitor Certificate Expiration Dates

• IPSEC Management

• Display or Change an Existing IPSec Policy

• Set Up a New IPSec Policy

## Set Internet Explorer Security Options

To download certificates from the server, ensure your Internet Explorer security settings are configured as follows:

Step 1 Start Internet Explorer.

Step 2 Navigate to Tools>Internet Options .

Step 3 Click the Advanced tab.

Step 4 Scroll down to the Security section on the Advanced tab.

Step 5 If necessary, clear the Do not save encrypted pages to disk check box.

Step 6 Click OK .

## Manage Certificates and Certificate Trust Lists

The Certificate Management menu options allow you to perform the following functions:

• Display certificates

• Upload certificates and Certificate Trust Lists (CTL)

• Download certificates and CTLs

• Delete certificates

• Regenerate certificates

• Download and generate Certificate Signing Requests (CSR)

• Monitor certificate expiration dates

Note To access the Security menu items, you must re-log in to Cisco Unified Communications Operating System Administration using your Administrator password.

### Display Certificates

To display existing certificates, follow this procedure:

Step 1 Navigate to Security>Certificate Management>Display Cert .

The Select Certificates or Trust Store window displays.

Step 2 Check the check box for the type of certificate that you want to display: Own Certificates or Trust Certificates.

The Display Certificates or Trust Units window displays.

Step 3 Check the check box for the certificate type that you want to display.

The Display Certificates or Trust Store window displays.

Step 4 Check the check box for the certificate of trust store that you want to display.

The Details of a Certificate window displays.

Step 5 After you have viewed the certificate details, choose another menu option to close the Details of Certificate window.

### Download a Certificate or CTL

To download a certificate or CTL from the Cisco Unified Communications Operating System to your PC, follow this procedure:

Step 1 Navigate to Security>Cerificate Management>Download Cert/CTL .

The Select Certificate/CTL/CSR Download windows displays.

Step 2 Check the check box for the appropriate download type: Own Cert, Trust Cert, or CTL file. Click Next .

The Download Certificates or Trust Units window displays.

Step 3 Check the check box for the existing certificate type that you want to download and click Next .

The Display Certificate/CTL/CSR Download window displays.

Step 4 Check the check box for existing certificates that you want to download and click Next .

The Certificate/CTL/CSR Download window displays.

Step 5 Click the Continue link.

A directory listing that shows the certificates that you chose displays.

Step 6 To save the certificate or CTL to your PC, right-click the name of the certificate or CTL and choose Save As .

Step 7 Enter the location where you want to save the certificate or CTL.

Step 8 Click Save .

### Delete and Regenerate a Certificate

### Deleting a Certificate

To delete a trusted certificate, follow this procedure:

Step 1 Navigate to Security>Certificate Management>Delete/Regenerate Cert .

Step 2 Check the Delete Trust Cert check box and click Next .

The Display Certificates or Trust Units For Delete/Regenerate window displays.

Step 3 Check the check box for the existing certificate type that you want to delete and click Next .

The Delete Certificates or Trust Store window displays.

Step 4 Check the Existing Certificate Name check box for the certificate that you want to delete and click Delete.

### Regenerating a Certificate

To regenerate a certificate, follow this procedure:

Step 1 Navigate to Security>Certificate Management>Delete/Regenerate Cert .

The Select Certificates or Trust Store for Deletion window displays.

Step 2 Check the Regenerate Self-Signed Cert check box and click Next .

Step 3 Check the appropriate Existing Certificates Types check box for the certificate that you want to regenerate, and click Next .

Step 4 Check the appropriate Existing Certificate check box and click Regenerate .

### Upload a Certificate or Certificate Trust List

When you save certificates that you obtained from a third-party Certificate Authority (CA) to your PC, Cisco recommends that you use Notepad to open and save the certificate because this method maintains the certificate format.

To upload a certificate or CTL to the server, follow this procedure:

Step 1 Navigate to Security>Certificate Management>Delete/Upload Cert/CTL .

The Select Certificate/CTL Upload window displays.

Step 2 Check the existing certificate types check box for the certificate or CTL that you want to upload.

The Select Certificate/CTL Upload window displays.

Step 3 Enter the name of the certificate or CTL that you want to upload or click Browse to browse for the file.

Step 4 To upload the certificate or CTL, click Upload .

Note The system does not distribute trust certificates to other cluster nodes automatically. If you need to have the same certificate on more than one node, you must upload the certificate to each node individually.

### Download a Certificate Signing Request

To download a Certificate Signing Request, follow this procedure:

Step 1 Navigate to Security>Certificate Management>Download/Generate CSR .

The Select Certificate type for CSR window displays.

Step 2 Check the Existing Certificate Types check box for the CSR that you want to download.

Step 3 Check the Download CSR if any check box.

The Certificate/CTL/CSR Download window displays.

Step 4 Click Continue .

A directory listing shows the certificates that you chose.

Step 5 To save the CSR to your PC, right-click the name of the certificate or CTL and choose Save As .

Step 6 Enter the location where you want to save the certificate or CTL.

Step 7 Click Save .

### Monitor Certificate Expiration Dates

The system can automatically send you an e-mail when a certificate is close to its expiration date. To view and configure the Certificate Expiration Monitor, follow this procedure:

Step 1 To view the current Certificate Expiration Monitor configuration, navigate to Security>Certificate Management>Cert Expiry Monitor>Display Config .

The Show Cert Expiry Monitoring Config window, which shows a summary of the current configuration information, displays.

Step 2 To configure the Certificate Expiration Monitor, navigate to Security>Certificate Management>Cert Expiry Monitor>Change Config .

The Change Cert Expiry Monitoring Config window displays.

Step 3 Enter the required configuration information. See Table 6-1 for a description of the Certificate Expiration Monitor fields.

Step 4 To save your changes, click Submit .

Table 6-1 Certificate Expiration Monitor Field Descriptions

Notification/Alert Start Time

Enter the number of days before the certificate expires that you want to be notified.

Initial Frequency of Notification

Enter the frequency for notification, either in hours or days.

Click on the right to Enable/Disable

To turn on e-mail notification, click Enable .

Email IDs entered for Notification

Enter the e-mail address to which you want notifications sent.

Note For the system to send notifications, you must configure an SMTP host.

## IPSEC Management

The IPSec menu options allow you to perform the following functions:

• Display or change an existing IPSec policy

• Set up a new IPSec policy

Note IPSec does not get automatically set up between nodes in the cluster during installation.

### Display or Change an Existing IPSec Policy

To display or change an existing IPSec policy, follow this procedure:

Note Because any changes that you make to an IPSec policy during a system upgrade will get lost, do not modify or create IPSec policies during an upgrade.

Step 1 Navigate to Security>IPSEC Management>Display/Change IPSEC .

Note To access the Security menu items, you must re-log in to Cisco Unified Communications Operating System Administration using your Administrator password.

The Display IPSEC Policy window displays.

Step 2 Check the appropriate Existing Policy check box, and click Next .

Step 3 Perform one of the following actions:

– To view an IPSec policy, click the Display Detail link.

– To delete an IPSec policy, click Delete .

– To activate an IPSec policy, click Enable .

– To deactivate an IPSec policy, click Disable .

Step 4 If you click the Display Detail link, the Association Details window displays. For an explanation of the fields in this window, see Table 6-2 .

### Set Up a New IPSec Policy

To set up a new IPSec policy and association, follow this procedure:

Note Because any changes you make to an IPSec policy during a system upgrade will get lost, do not modify or create IPSec policies during an upgrade.

Step 1 Navigate to Security > IPSEC Management > Setup New IPSEC .

The Setup Select window displays.

Step 2 Check the Certificate or Pre-Shared Key check box.

– If you check Certificate, check Same Type or Different Type node.

– If you check Pre-Shared Key, enter the key name.

Step 3 Click Next .

The Setup IPSEC Policy and Association window displays.

Step 4 Enter the appropriate information on the Setup IPSEC Policy and Association window. For a description of the fields on this window, see Table 6-2 .

Step 5 To set up the new IPSec policy, click Submit .

Table 6-2 IPSEC Policy and Association Field Descriptions

Policy Name

Specifies the name of the IPSec policy.

Dest. Address Type

Specifies the Destination Address Type:

• IP—Dotted IP address of the destination

• FQDN—Fully qualified domain name of the destination

Source Address Type

Specifies the Source Address Type:

• IP—Dotted IP address of the source

• FQDN—Fully qualified domain name of the source

Tunnel/Transport

Specifies tunnel or transport.

Protocol

Specifies the specific protocol, or Any:

• TCP

• UDP

• Any

Dest. Port

Specifies the port number to use at the destination.

Phase 1 Life Time in Seconds

Specifies the lifetime for phase 1, IKE negotiation, in seconds.

Hash Algorithm

Specifies the hash algorithm:

• SHA1—Hash algorithm that is used in phase 1 IKE negotiation

• MD5—Hash algorithm that is used in phase 1 IKE negotiation

Phase 2 Life Time in Seconds

Specifies the lifetime for phase 2, IKE negotiation, in seconds.

AH Algorithm

Specifies the AH algorithm:

• HMAC_MD5—Authentication algorithm that is used to authenticate IP packets

• HMAC_SHA1—Authentication algorithm that is used to authenticate IP packets

Assoc. Name

Specifies the association name that is given to each IPSec association.

Dest. Address

Specifies the IP address or FQDN of the destination.

Source Address

Specifies the IP address or FQDN of the source.

Remote Port

Specifies the port number at the destination.

Source Port

Specifies the port number at the source.

Encryption Algorithm

From the drop-down list, choose the encryption algorithm. Choices include:

• DES

• 3DES

Phase 1 DH Value

From the drop-down list, choose the phase 1 DH value. Choices include: 2, 1, 5, 14, 16, 17, and 18.

ESP Algorithm

From the drop-down list, choose the ESP algorithm. Choices include:

• NULL_ENC

• DES

• 3DES

• BLOWFISH

• RIJNDAEL

Phase 2 DH Value

From the drop-down list, choose the phase 2 DH value. Choices include: 2, 1, 5, 14, 16, 17, and 18.

| Field | Description |
|---|---|
| Notification/Alert Start Time | Enter the number of days before the certificate expires that you want to be notified. |
| Initial Frequency of Notification | Enter the frequency for notification, either in hours or days. |
| Click on the right to Enable/Disable | To turn on e-mail notification, click Enable . |
| Email IDs entered for Notification | Enter the e-mail address to which you want notifications sent. Note For the system to send notifications, you must configure an SMTP host. |

| Field | Description |
|---|---|
| Policy Name | Specifies the name of the IPSec policy. |
| Dest. Address Type | Specifies the Destination Address Type: • IP—Dotted IP address of the destination • FQDN—Fully qualified domain name of the destination |
| Source Address Type | Specifies the Source Address Type: • IP—Dotted IP address of the source • FQDN—Fully qualified domain name of the source |
| Tunnel/Transport | Specifies tunnel or transport. |
| Protocol | Specifies the specific protocol, or Any: • TCP • UDP • Any |
| Dest. Port | Specifies the port number to use at the destination. |
| Phase 1 Life Time in Seconds | Specifies the lifetime for phase 1, IKE negotiation, in seconds. |
| Hash Algorithm | Specifies the hash algorithm: • SHA1—Hash algorithm that is used in phase 1 IKE negotiation • MD5—Hash algorithm that is used in phase 1 IKE negotiation |
| Phase 2 Life Time in Seconds | Specifies the lifetime for phase 2, IKE negotiation, in seconds. |
| AH Algorithm | Specifies the AH algorithm: • HMAC_MD5—Authentication algorithm that is used to authenticate IP packets • HMAC_SHA1—Authentication algorithm that is used to authenticate IP packets |
| Assoc. Name | Specifies the association name that is given to each IPSec association. |
| Dest. Address | Specifies the IP address or FQDN of the destination. |
| Source Address | Specifies the IP address or FQDN of the source. |
| Remote Port | Specifies the port number at the destination. |
| Source Port | Specifies the port number at the source. |
| Encryption Algorithm | From the drop-down list, choose the encryption algorithm. Choices include: • DES • 3DES |
| Phase 1 DH Value | From the drop-down list, choose the phase 1 DH value. Choices include: 2, 1, 5, 14, 16, 17, and 18. |
| ESP Algorithm | From the drop-down list, choose the ESP algorithm. Choices include: • NULL_ENC • DES • 3DES • BLOWFISH • RIJNDAEL |
| Phase 2 DH Value | From the drop-down list, choose the phase 2 DH value. Choices include: 2, 1, 5, 14, 16, 17, and 18. |