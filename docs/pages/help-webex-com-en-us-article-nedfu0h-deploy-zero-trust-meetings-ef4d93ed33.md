---
doc_id: help-webex-com-en-us-article-nedfu0h-deploy-zero-trust-meetings-ef4d93ed33
source_url: https://help.webex.com/en-us/article/nedfu0h/Deploy-Zero-Trust-Meetings
retrieved_at: 2026-11-02T12:57:09.338984+00:00
---

User experience

Users choose the meeting type when they schedule a meeting. When admitting participants from the lobby, as well as during the meeting, the host can see the identity verification status of each participant. There is also a meeting code that is common to all current participants in the meeting, which they can use to verify that their meeting has not been intercepted by an unwanted third party Meddler In The Middle (MITM) attack.

Share the following information with your meeting hosts:

Identity Verification with Internal or External CA

### Verify identity

End-to-end encryption with identity verification provides additional security to an end-to-end encrypted meeting.

When participants or devices join a shared MLS (Messaging Layer Security) group, they present their certificates to the other group members, who then validate the certificates against the issuing Certificate Authorities (CA). By confirming that the certificates are valid, the CA verifies the identity of the participants, and the meeting shows the participants/devices as verified.

Webex App users authenticate themselves against the Webex identity store, which issues them an access token when authentication succeeds. If they need a certificate to verify their identity in an end-to-end encrypted meeting, the Webex CA issues them a certificate based on their access token. At this time, we do not provide a way for Webex Meetings users to get a certificate issued by a third-party/external CA.

Devices can authenticate themselves using a certificate issued by the internal (Webex) CA, or a certificate issued by an external CA:

Internal CA—Webex issues an internal certificate based on the access token of the device's machine account. The certificate is signed by the Webex CA. Devices do not have user IDs in the same way that users do, so Webex uses (one of) your organization's domains when writing the device certificate's identity (Common Name (CN)).

External CA—Request and purchase device certificates directly from your chosen issuer. You must encrypt, directly upload, and authorize the certificates using a secret known only to you.

Cisco is not involved, which makes this the way to guarantee true end-to-end encryption and verified identity, and prevent the theoretical possibility that Cisco could eavesdrop on your meeting/decrypt your media.

### Internally issued device certificate

Webex issues a certificate to the device when it registers after startup, and renews it when necessary. For devices, the certificate includes the account ID and a domain.

If your organization does not have a domain, the Webex CA issues the certificate without a domain.

If your organization has multiple domains, you can use Control Hub to tell Webex which domain the device to use for its identity. You could also use the API xConfiguration Conference EndToEndEncryption Identity PreferredDomain: "example.com" .

If you have multiple domains and do not set the preferred domain for the device, then Webex chooses one for you.

### Externally issued device certificate

An administrator can provision a device with their own certificate that has been signed with one of the public CAs.

The certificate must be based on an ECDSA P-256 key pair, although it can be signed by an RSA key.

The values in the certificate are at the discretion of the organization. The Common Name (CN) and Subject Alternative Name (SAN) will be displayed in the Webex meeting user interface, as described in End-to-end encryption with identity verification for Webex Meetings .

We recommend using a separate certificate per device and to have a unique CN per device. For example, “meeting-room-1.example.com” for the organization that owns the “example.com” domain.

In order to fully protect the external certificate from tampering, a client-secret feature is used to encrypt and sign various xcommands.

When using the client secret, it is possible to securely manage the external Webex identity certificate via the xAPI. This is currently limited to online devices.

Webex currently provides API commands for managing this.

Features and limitations

### Devices

Cloud-registered Cisco Board, Desk, and  Room Series devices can join E2EE meetings.

The following devices cannot join E2EE meetings:

Third-party SIP devices

### Software clients

Webex App for desktop and mobile clients can join E2EE meetings.

The Webex web client cannot join E2EE meetings.

Third-party SIP soft clients cannot join E2EE meetings.

### Identity

By design, we do not provide Control Hub options for you to manage externally-verified device identity. For true end-to-end encryption, only you should know/access the secrets and keys. If we introduced a cloud service to manage those keys, there is a chance of them being intercepted.

Currently we provide a 'recipe' for you to design your own tools, based on industry-standard encryption techniques, to assist with requesting or encrypting your device identity certificates and their private keys. We do not want to have any real or perceived access to your secrets or keys.

### Meetings

E2EE meetings currently support a maximum of 1000 participants.

- In E2EE meetings, users can't access whiteboards created outside the meeting, including private whiteboards, whiteboards shared by others, and whiteboards from Webex spaces.

- Whiteboards created in E2EE meetings are only available during the meeting. They are not saved and are not accessible after the meeting has ended.

- If someone shares content in an E2EE meeting, you can annotate it. For more information on annotation, see Webex App | Mark up shared content with annotations .

### Management interface

We highly recommend that you use Control Hub to manage your Meetings site, as Control Hub organizations have centralized identity for the whole organization.

Prerequisites

Webex Meetings 41.7.

Cloud-registered Cisco Board, Desk, and Room Series devices, running 10.6.1-RoomOS_August_2021 or later.

Administrative access to the meeting site in Control Hub.

One or more verified domains in your Control Hub organization (if you're using the Webex CA to issue device certificates for verified identity).

Collaboration Meeting Rooms must be turned on so that people can join from their video system. For more information, see Allow video systems to join meetings and events on your Webex site .

Get device certificates

You can skip this step if you do not need externally-verified identities.

For the highest level of security and for identity verification, each device should have a unique certificate issued by a trusted public Certificate Authority (CA).

You need to interact with the CA to request, purchase, and receive the digital certificates and create the associated private keys. When requesting the certificate, use these parameters:

The certificate must be issued and signed by a well-known public CA.

Unique: We strongly recommend using a unique certificate for each device. If you use one certificate for all devices, you are compromising your security.

Common Name (CN) and Subject Alternate Name/s (SAN/s): These are not important to Webex, but should be values that humans can read and associate with the device. The CN will show to other meeting participants as the primary verified identity of the device, and if users inspect the certificate through the meeting UI, they'll see the SAN/s. You might want to use names like name.model@example.com .

File format: The certificates and keys must be in the .pem format.

Purpose: The certificate purpose must be Webex Identity.

Generating keys: The certificates must be based on ECDSA P-256 key pairs (Elliptical Curve Digital Signature Algorithm using the P-256 curve).

This requirement does not extend to the signing key. The CA can use an RSA key to sign the certificate.

Prepare to onboard devices

You can skip this step if you do not want to use externally-verified identity with your devices.

If you are using new devices, do not register them to Webex yet. To be safe, don't connect them to the network at this point.

If you have existing devices that you want to upgrade to use externally-verified identity, you must factory- reset the devices.

Save the existing configuration if you want to keep it.

Schedule a window when the devices are not being used, or use a phased approach. Notify users of the changes they can expect.

Ensure physical access to devices. If you must access devices over the network, be aware that secrets are travelling in plain text and you are compromising your security.

Once you have completed these steps, allow video systems to join meetings and events on your Webex site .

Understand the external identity process for devices

To ensure that your device media cannot be encrypted by anyone except the device, you must encrypt the private key on the device. We designed APIs for the device to enable management of the encrypted key and certificate, using JSON Web Encryption (JWE).

To ensure true end-to-end encryption through our cloud, we cannot be involved in encrypting and uploading the certificate and key. If you need this level of security, you must:

Request your certificates.

Generate your certificates' key pairs.

Create (and protect) an initial secret for each device, to seed the device's encryption capability.

Develop and maintain your own tool for encrypting files using the JWE standard.

The process and the (non-secret) parameters you'll need is explained below, as well as a recipe to follow in your development tools of choice. We also provide some test data and the resulting JWE blobs as we expect them, to help you verify your process.

An unsupported reference implementation using Python3 and the JWCrypto library is available from Cisco on request.

Concatenate and encrypt the certificate and key using your tool and the device's initial secret.

Upload the resulting JWE blob to the device.

Set the purpose of the encrypted certificate to be used for Webex identity, and activate the certificate.

(Recommended) Provide an interface to (or distribute) your tool to enable device users to change the initial secret and protect their media from you.

### How we use the JWE format

This section describes how we expect the JWE to be created as input to the devices, so that you can build your own tool to create the blobs from your certificates and keys.

Refer to JSON Web Encryption (JWE) https://datatracker.ietf.org/doc/html/rfc7516 and JSON Web Signature (JWS) https://datatracker.ietf.org/doc/html/rfc7515 .

We use the Compact Serialization of a JSON document to create JWE blobs. The parameters you need to include when creating the JWE blobs are:

JOSE Header (protected). In the JSON Object Signing and Encryption header, you MUST include the following key-value pairs:

"alg":"dir"

The direct algorithm is the only one we support for encrypting the payload, and you must use the device's initial client secret.

"enc":"A128GCM" or "enc":"A256GCM"

We support these two encryption algorithms.

"cisco-action": "add" or "cisco-action": "populate" or "cisco-action": "activate" or "cisco-action": "deactivate"

This is a proprietary key and four values it can take. We introduced this key to signal the purpose of the encrypted data to the target device. The values are named after the xAPI commands on the device where you are using the encrypted data.

We named it cisco-action to mitigate potential clashes with future JWE extensions.

"cisco-kdf": { "version": "1", "salt": "base64URLEncodedRandom4+Bytes" }

Another proprietary key. We use the values you provide as inputs for key derivation on the device. The version must be 1 (the version of our key derivation function). The value of salt must be a base64 URL-encoded sequence of at least 4 bytes, which you must choose randomly.

JWE Encrypted Key . This field is empty. The device derives it from the initial ClientSecret .

JWE Initialization Vector . You must supply a base64url encoded initialization vector for decrypting the payload. The IV MUST be a random 12 byte value (we are using the AES-GCM cipher family, which requires the IV to be 12 bytes long).

JWE AAD (additional authenticated data). You must omit this field because it is not supported in the Compact Serialization.

JWE Ciphertext : This is the encrypted payload that you want to keep secret.

The payload MAY be empty. For example, to reset the client secret, you need to overwrite it with an empty value.

There are different types of payloads, depending on what you are trying to do on the device. Different xAPI commands expect different payloads, and you must specify the purpose of the payload with the cisco-action key, as follows:

With "cisco-action":"populate" the ciphertext is the new ClientSecret .

With " "cisco-action":"add" the ciphertext is a PEM blob carrying the certificate and its private key (concatenated).

With " "cisco-action":"activate" the ciphertext is the fingerprint (hexadecimal representation of sha-1) of the certificate we are activating for device identitiy verification.

With " "cisco-action":"deactivate" the ciphertext is the fingerprint (hexadecimal representation of sha-1) of the certificate we are deactivating from being used for device identity verification.

JWE authentication tag: This field contains the authentication tag to ascertain the integrity of the entire JWE compactly serialized blob

### How we derive the encryption key from the ClientSecret

After the first population of the secret, we do not accept or output the secret as plain text. This is to prevent potential dictionary attacks by someone who could access the device.

The device software uses the client secret as an input to a key derivation function (kdf) and then uses the derived key for content decryption/encryption on the device.

What this means for you is that your tool to produce JWE blobs must follow the same procedure to derive the same encryption/decryption key from the client secret.

The devices use scrypt for key derivation (see https://en.wikipedia.org/wiki/Scrypt ), with the following parameters:

CostFactor (N) is 32768

BlockSizeFactor (r) is 8

ParallelizationFactor (p) is 1

Salt is a random sequence of at least 4 bytes; you must supply this same salt when specifying the cisco-kdf parameter.

Key lengths are either 16 bytes (if you select the AES-GCM 128 algorithm), or 32 bytes (if you select the AES-GCM 256 algorithm)

Max memory cap is 64MB

This set of parameters is the only configuration of scrypt that is compatible with the key derivation function on the devices. This kdf on the devices is called "version":"1" , which is the only version currently taken by the cisco-kdf parameter.

### Worked example

Here is an example that you can follow to verify that your JWE encryption process works the same as the process we created on the devices.

The example scenario is adding a PEM blob to the device (mimics adding a certificate, with a very short string instead of a full cert + key). The client secret in the example is ossifrage .

Choose an encryption cipher. This example uses A128GCM (AES with 128-bit keys in the Galois Counter Mode). Your tool could use A256GCM if you prefer.

Choose a salt (must be a random sequence of at least 4 bytes). This example uses (hex bytes) E5 E6 53 08 03 F8 33 F6 . Base64url encode the sequence to get 5eZTCAP4M_Y (remove the base64 padding).

Here is a sample scrypt call to create the content encryption key (cek):

cek=scrypt(password="ossifrage", salt=4-byte-sequence, N=32768, r=8, p=1, keylength=16)

The derived key should be 16 bytes (hex) as follows: 95 9e ba 6d d1 22 01 05 78 fe 6a 9d 22 78 ff ac which base64url encodes to lZ66bdEiAQV4_mqdInj_rA .

Choose a random sequence of 12 bytes to use as an initialization vector. This example uses (hex) 34 b3 5d dd 5f 53 7b af 2d 92 95 83 which base64url encodes to NLNd3V9Te68tkpWD .

Create the JOSE header with compact serialization (follow the same order of parameters we use here) and then base64url encode it:

{"alg":"dir","cisco-action":"add","cisco-kdf":{"salt":"5eZTCAP4M_Y","version":"1"},"enc":"A128GCM"}

The base64url encoded JOSE header is eyJhbGciOiJkaXIiLCJjaXNjby1hY3Rpb24iOiJhZGQiLCJjaXNjby1rZGYiOnsic2FsdCI6IjVlWlRDQVA0TV9ZIiwidmVyc2lvbiI6IjEifSwiZW5jIjoiQTEyOEdDTSJ9

This will be the first element of the JWE blob.

The second element of the JWE blob is empty, because we are not supplying a JWE encryption key.

The third element of the JWE blob is the initialization vector NLNd3V9Te68tkpWD .

The encryption parameters you should use are:

Payload is this is a PEM file

Encryption cipher is AES 128 GCM

The base64url encoded JOSE header as Additional Authenticated Data (AAD)

Base64url encode the encrypted payload, which should result in f5lLVuWNfKfmzYCo1YJfODhQ

This is the fourth element (JWE Ciphertext) in the JWE blob.

Base64url encode the tag you produced in step 8, which should result in PE-wDFWGXFFBeo928cfZ1Q

This is the fifth element in the JWE blob.

Concatenate the five elements of the JWE blob with dots (JOSEheader..IV.Ciphertext.Tag) to get:

eyJhbGciOiJkaXIiLCJjaXNjby1hY3Rpb24iOiJhZGQiLCJjaXNjby1rZGYiOnsic2FsdCI6IjVlWlRDQVA0TV9ZIiwidmVyc2lvbiI6IjEifSwiZW5jIjoiQTEyOEdDTSJ..9NLNd3V9Te68tkpWD.f5lLVuWNfKfmzYCo1YJfODhQ.PE-wDFWGXFFBeo928cfZ1Q

If you derived the same base64url encoded values as we show here, using your own tools, you are ready to use them to secure the E2E encryption and verified identity of your devices.

This example won't actually work, but in principle your next step would be to use the JWE blob you created above as the input to the xcommand on the device that adds the certificate:

xCommand Security Certificates Add eyJhbGciOiJkaXIiLCJjaXNjby1hY3Rpb24iOiJhZGQiLCJjaXNjby1rZGYiOnsic2FsdCI6IjVlWlRDQVA0TV9ZIiwidmVyc2lvbiI6IjEifSwiZW5jIjoiQTEyOEdDTSJ..9NLNd3V9Te68tkpWD.f5lLVuWNfKfmzYCo1YJfODhQ.PE-wDFWGXFFBeo928cfZ1Q

Session types for zero-trust meetings are available to all meetings sites at no additional cost. One of these session types is called Pro-End to End Encryption_VOIPonly . This is the Public Service Name , which we may change in the future. For the current names of the session types, see Session Type IDs in the Reference section of this article.

There is nothing you need to do to get this capability for your site; you do need to grant the new session type (also called Meeting Privilege ) to users. You can do this individually through the user's configuration page, or in bulk with a CSV export/import.

Verify the new session type

Sign in to Control Hub , and go to Services > Meeting .

Click Sites , choose the Webex site for which you want to change the settings, then click Settings .

Under Common Settings , select Session
            Types .

There is an older session type with a very similar name: Pro-End to End Encryption . This session type includes non-encrypted PSTN access to meetings. Make sure you have the _VOIPonly version to ensure end-to-end encryption. You can check by hovering over the PRO link in the session code column; for this example, the target of the link should be javascript:ShowFeature(652) .

We may change the Public Service Names for these session types in the future.

If you don’t have the new session type yet, contact your Webex representative.

What to do next

Enable this session type / meeting privilege to some or all of your users.

Enable E2EE meetings for individual users

Sign in to Control Hub , and go to Management > Users .

Select a user account to update, then select Meetings .

From the Settings apply to drop-down list, select the meeting site to update.

Check the box next to Pro-End to End Encryption_VOIPonly .

Close the user configuration panel.

Repeat for other users if necessary.

To assign this to many users, use the next option, Enable E2EE meetings for multiple users .

Enable E2EE meetings for multiple users

Sign in to Control Hub , and go to Services > Meeting .

Click Sites , choose the Webex site for which you want to change the settings.

In the Licenses and Users section, click Bulk Manage .

Click Generate Report , and wait while we prepare the file.

When the file is ready, click Export Results and then Download . (You have to manually close that pop-up window after you click Download .)

Open the downloaded CSV file for editing.

There is a row for each user, and the MeetingPrivilege column contains their session type IDs as a comma-delimited list.

For each user you wish to grant the new session type, add 1561 as a new value in the comma-delimited list in the MeetingPrivilege cell.

The Webex CSV File Format Reference contains details on the purpose and contents of the CSV file.

Open the Meeting site configuration panel in Control Hub.

If you were already on the Meeting site list page, you may need to refresh it.

In the Licenses and Users section, click Bulk Manage .

Click Import and select the edited CSV, then click Import . Wait while the file is uploaded.

When the import is finished, you can click Import Results to review if there were any errors.

Go to the Users page and open one of the users to verify they have the new session type.

Add an audio watermark for security

You can add a watermark to meeting recordings with the Webex Meetings Pro-End to End Encryption_VOIPonly session type, which allows you to identify the source client or device of unauthorized recordings of confidential meetings.

When this feature is enabled, the meeting audio includes a unique identifier for each participating client or device. You can upload audio recordings to Control Hub, which then analyzes the recording and looks up the unique identifiers. You can look at the results to see which source client or device recorded the meeting.

- In order to be analyzed, the recording must be an AAC, MP3, M4A, WAV, MP4, AVI, or MOV file no larger than 500MB.

- The recording must be longer than 100 seconds.

- You can only analyze recordings for meetings hosted by people in your organization.

- Watermark information is retained for the same duration as the organization's meeting information.

### Add audio watermarks to E2EE meetings

- Sign in to Control Hub , then under Management , select Organization Settings .

Some time after this is toggled on, users scheduling meetings with the Webex Meetings Pro-End to End Encryption_VOIPonly session type see a Digital Watermarking option in the Security section.

### Upload and analyze a watermarked meeting

- In Control Hub, under Monitoring , select Troubleshooting .

- Click Watermark Analysis .

- Search for or select the meeting in the list, then click Analyze .

- In the Analyze audio watermark window, enter a name for your analysis.

- (Optional) Enter a note for your analysis.

- Drag and drop the audio file to be analyzed, or click Choose file to browse to the audio file.

When the analysis is complete, it will be shown in the list of results on the Analyze watermark page.

- Select the meeting in the list to see the results of the analysis. Click to download the results.

### Features and Limitations

Factors involved in successfully decoding a recorded watermark include the distance between the recording device and the speaker outputting the audio, the volume of that audio, environmental noise, etc. Our watermarking technology has additional resiliency to being encoded multiple times, as might happen when the media is shared.

This feature is designed to enable successful decoding of the watermark identifier in a broad but reasonable set of circumstances. Our goal is for a recording device, such as a mobile phone, that is lying on a desk near a personal endpoint or laptop client, should always create a recording that results in a successful analysis. As the recording device is moved away from the source, or is obscured from hearing the full audio spectrum, the chances of a successful analysis are decreased.

In order to successfully analyze a recording, a reasonable capture of the meeting audio is needed. If a meeting's audio is recorded on the same computer that is hosting the client, limitations should not apply.

Onboard devices (Internal CA)

If your devices are already onboarded to your Control Hub organization and you want to use the Webex CA to auto-generate their identifying certificates, you do not need to factory reset the devices.

This procedure selects which domain the device uses to identify itself, and is only required if you have multiple domains in your Control Hub organization. If you have more than one domain, we recommend you do this for all your devices that will have "Cisco-verified" identity. If you don't tell Webex which domain identifies the device, one is automatically chosen, and it may look wrong to other meeting participants.

Before you begin

If your devices are not yet onboarded, follow Register a Device to Cisco Webex Using API or Local Web Interface or Cloud onboarding for Board, Desk, and Room Series . You should also verify the domain/s you want to use to identify the devices in Manage your domains .

Sign in to Control Hub , and under Management , select Devices .

Select a device to open its configuration panel.

Select the domain you want to use to identify this device.

Repeat for other devices.

Onboard devices (External CA)

Before you begin

Get a CA-signed certificate and private key, in .pem format, for each device.

Under the Prepare tab, read the topic Understanding External Identity Process for Devices ,

Prepare a JWE encryption tool with respect to the information there.

Make sure you have a tool to generate random byte sequences of given lengths.

Make sure you have a tool to base64url encode bytes or text.

Make sure you have a scrypt implementation.

Make sure you have a secret word or phrase for each device.

Populate the device's ClientSecret with a plain text secret:

The first time you populate the Secret , you supply it in plain text. That's why we recommend doing this at the physical device console.

Base64url encode the secret phrase for this device.

Open the TShell on the device.

Run xcommand Security ClientSecret Populate Secret: "MDEyMzQ1Njc4OWFiY2RlZg"

The example command above populates the Secret with the phrase 0123456789abcdef . You need to choose your own.

The device has its initial secret. Don't forget this; you can't recover it and must factory-reset the device to start again.

Concatenate your certificate and private key:

Using a text editor, open the .pem files, paste the key blob the certificate blob, and save it as a new .pem file.

This is the payload text you'll encrypt and put in your JWE blob.

Create a JWE blob to use as input to the certificate add command:

Create a random sequence of at least 4 bytes. This is your salt.

Derive a content encryption key with your scrypt tool.

For this you need the secret, the salt, and a keylength to match your chosen encryption cipher. There are some other fixed values to supply (N=32768, r=8, p=1). The device uses the same process and values to derive the same content encryption key.

Create a random sequence of exactly 12 bytes. This is your initialization vector.

Create a JOSE header, setting alg , enc , and cisco-kdf keys as described in Understanding External Identity Process for Devices . Set the "add" action using the key:value "cisco-action":"add" in your JOSE header (because we're adding the certificate to the device).

Base64url encode the JOSE header.

Use your JWE encryption tool with the chosen cipher and the base64url encoded JOSE header to encrypt the text from the concatenated pem file.

Base64url encode the initialization vector, the encrypted PEM payload, and the authentication tag.

Construct the JWE blob as follows (all values are base64url encoded):

JOSEHeader..InitVector.EncryptedPEM.AuthTag

Open the TShell on the device and run the (multiline) add command:

```
xcommand Security Certificates Services Add IsEncrypted: True
your..JWE.str.ing\n
.\n
```

Verify the certificate is added by running xcommand Security Certificates Services Show

Copy the new certificate's fingerprint.

Activate the certificate for the purpose WebexIdentity :

Read the fingerprint of the certificate, either from the certificate itself or from the output of xcommand Security Certificates Services Show .

Create a random sequence of at least 4 bytes, and base64url encode that sequence. This is your salt.

Derive a content encryption key with your scrypt tool.

For this you need the secret, the salt, and a keylength to match your chosen encryption cipher. There are some other fixed values to supply (N=32768, r=8, p=1). The device uses the same process and values to derive the same content encryption key.

Create a random sequence of exactly 12 bytes, and base64url encode that sequence. This is your initialization vector.

Create a JOSE header, setting alg , enc , and cisco-kdf keys as described in Understanding External Identity Process for Devices . Set the "activate" action using the key:value "cisco-action":"activate" in your JOSE header (because we're activating the certificate on the device).

Base64url encode the JOSE header.

Use your JWE encryption tool with the chosen cipher and the base64url encoded JOSE header to encrypt the certificate fingerprint.

The tool should output a 16 or 32 byte sequence, depending on whether you chose 128 or 256 bit AES-GCM, and an authentication tag.

Base64urlencode the encrypted fingerprint, and the authentication tag.

Construct the JWE blob as follows (all values are base64url encoded):

JOSEHeader..InitVector.EncryptedFingerprint.AuthTag

Open the TShell on the device and run the following activate command:

```
xcommand Security Certificates Services Activate Purpose: WebexIdentity Fingerprint: "Your..JWE.encrypted.fingerprint"
```

The device has an encrypted, active, CA-issued certificate, ready to be used for identifying it in end-to-end encrypted Webex meetings.

Onboard the device to your Control Hub organization.

Test end-to-end encryption with identity verification

Schedule a meeting of the correct type ( Webex Meetings Pro-End to End Encryption_VOIPonly ).

See Schedule a Webex Meeting with End-to-End Encryption .

Join the meeting as the host, from a Webex Meetings client.

See Join a Webex Meeting with End-to-End Encryption .

Join the meeting from a device that has its identity verified by the Webex CA.

As the host, verify this device appears in the lobby with the correct identity icon.

See Join a Webex Meeting with End-to-End Encryption .

Join the meeting from a device that has its identity verified by an external CA.

As the host, verify this device appears in the lobby with the correct identity icon. Learn more about identity icons .

Join the meeting as an unauthenticated meetings participant.

As the host, verify this participant appears in the lobby with the correct identity icon.

As the host, admit or reject people / devices.

Validate participant/device identities where possible by checking the certificates.

Check that everyone in the meeting sees the same meeting security code.

Join the meeting with a new participant.

Check that everyone sees  the same, new meeting security code.

Set Scope and Expectations

Are you going to make end-to-end encrypted meetings the default meeting option, or enable it only for some users, or allow all hosts to decide? When you have decided how you are going to use this feature, prepare those users who will use it, especially with respect to the limitations and what to expect in the meeting.

Do you need to ensure that neither Cisco nor anyone else can decrypt your content or impersonate your devices? If so, you need certificates from a public CA.

If you have varying levels of identity verification, empower users to verify each other with certificate-backed identity. Even though there are circumstances where participants can appear as Unverified, and participants should know how to check, unverified people may not be impostors.

Identity Management

If you are using an external CA to issue your device certificates, the onus is on you to monitor, refresh, and reapply certificates.

If you created the initial secret, understand that your users may want to change their device's secret. You may need to create an interface/distribute a tool to enable them to do this.

Session Type IDs

Session Type ID

Public Service Name

638

E2E Encryption+VoIP only

652

Pro-End to End Encryption_VOIPonly

660

Pro 3 Free-End to End Encryption_VOIPonly

E2E Encryption + Identity

672

Pro 3 Free50-End to End Encryption_VOIPonly

673

Education Instructor E2E Encryption_VOIPonly

676

Broadworks Standard plus end to end encryption

677

Broadworks Premium plus end to end encryption

681

Schoology Free plus end to end encryption

Related xAPI Commands

These tables describe Webex devices API commands we added for end-to-end encrypted meetings and verified identity. For more information about how to use the API, see Access the API for Board, Desk, and Room Series devices .

These xAPI commands are only available on devices that are either:

Registered to Webex

Registered on-premises and linked to Webex with Webex Edge for Devices

API call

Description

xConfiguration Conference EndToEndEncryption Identity PreferredDomain: "example.com"

This configuration is made when the admin sets the device's preferred domain from Control Hub. Only necessary if the organization has more than one domain.

The device uses this domain when it requests a certificate from the Webex CA. The domain then  identifies the device.

This configuration is not applicable when the device has an active, externally-issued certificate to identify itself.

xStatus Conference EndToEndEncryption Availability

Indicates if the device can join an end-to-end encrypted meeting. The cloud API calls it so that a paired app knows whether it can use the device to join.

xStatus Conference EndToEndEncryption ExternalIdentity Verification

Indicates if the device uses External verification (has an externally-issued certificate).

xStatus Conference EndToEndEncryption ExternalIdentity Identity

The identity of the device as read from the externally-issued certificate's Common Name.

xStatus Conference EndToEndEncryption ExternalIdentity CertificateChain Certificate # specificinfo

Reads specific information from an externally-issued certificate.

In the command shown, replace # with the number of the certificate. Replace specificinfo with one of:

Fingerprint

NotAfter Validity end date

NotBefore Validity start date

PrimaryName

PublicKeyAlgorithm

SerialNumber

SignatureAlgorithm

Subject # Name A list of the subjects for the certificate (e.g. email address or domain name)

Validity Gives the validity status of this certificate (e.g. valid or expired )

xStatus Conference EndToEndEncryption ExternalIdentity Status

The status of the device’s external identity (e.g. valid or error ).

xStatus Conference EndToEndEncryption InternalIdentity Verification

Indicates if the device has a valid certificate issued by the Webex CA.

xStatus Conference EndToEndEncryption InternalIdentity Identity

The identity of the device as read from the Webex-issued certificate's Common Name.

Contains a domain name if the organization has a domain.

Is empty if the organization does not have a domain.

If the device is in an organization that has multiple domains, this is the value from the PreferredDomain .

xStatus Conference EndToEndEncryption InternalIdentity CertificateChain Certificate # specificinfo

Reads specific information from the Webex-issued certificate.

In the command shown, replace # with the number of the certificate. Replace specificinfo with one of:

Fingerprint

NotAfter Validity end date

NotBefore Validity start date

PrimaryName

PublicKeyAlgorithm

SerialNumber

SignatureAlgorithm

Subject # Name A list of the subjects for the certificate (e.g. email address or domain name)

Validity Gives the validity status of this certificate (e.g. valid or expired )

API call

Description

xEvent Conference ParticipantList ParticipantAdded

xEvent Conference ParticipantList ParticipantUpdated

xEvent Conference ParticipantList ParticipantDeleted

These three events now include EndToEndEncryptionStatus , EndToEndEncryptionIdentity , and EndToEndEncryptionCertInfo for the affected participant.

API call

Description

xCommand Security ClientSecret Populate Secret: "base64url-encoded"

or

xCommand Security ClientSecret Populate Secret: JWEblob

Accepts a base64url encoded plain text value for seeding the client secret on the device for the first time.

To update the secret after that first time, you must supply a JWE blob containing the new secret encrypted by the old secret.

xCommand Security Certificates Services Add JWEblob

Adds a certificate (with private key).

We extended this command to accept a JWE blob containing the encrypted PEM data.

xCommand Security Certificates Services Activate Purpose:WebexIdentity FingerPrint: JWEblob

Activates a specific certificate for WebexIdentity. For this Purpose ,   the command requires the identifying fingerprint to be encrypted and serialized in a JWE blob.

xCommand Security Certificates Services Deactivate Purpose:WebexIdentity FingerPrint: JWEblob

Deactivates a specific certificate for WebexIdentity. For this Purpose ,   the command requires the identifying fingerprint to be encrypted and serialized in a JWE blob.

| 1 | Sign in to Control Hub , and go to Services > Meeting . |
|---|---|
| 2 | Click Sites , choose the Webex site for which you want to change the settings, then click Settings . |
| 3 | Under Common Settings , select Session
            Types . You should see one or more end-to-end encryption session types. Refer to the list of Session Type IDs in the Reference section of this article. For example, you may see Pro-End to End Encryption_VOIPonly . There is an older session type with a very similar name: Pro-End to End Encryption . This session type includes non-encrypted PSTN access to meetings. Make sure you have the _VOIPonly version to ensure end-to-end encryption. You can check by hovering over the PRO link in the session code column; for this example, the target of the link should be javascript:ShowFeature(652) . We may change the Public Service Names for these session types in the future. |
| 4 | If you don’t have the new session type yet, contact your Webex representative. |

| 1 | Sign in to Control Hub , and go to Management > Users . |
|---|---|
| 2 | Select a user account to update, then select Meetings . |
| 3 | From the Settings apply to drop-down list, select the meeting site to update. |
| 4 | Check the box next to Pro-End to End Encryption_VOIPonly . |
| 5 | Close the user configuration panel. |
| 6 | Repeat for other users if necessary. To assign this to many users, use the next option, Enable E2EE meetings for multiple users . |

| 1 | Sign in to Control Hub , and go to Services > Meeting . |
|---|---|
| 2 | Click Sites , choose the Webex site for which you want to change the settings. |
| 3 | In the Licenses and Users section, click Bulk Manage . |
| 4 | Click Generate Report , and wait while we prepare the file. |
| 5 | When the file is ready, click Export Results and then Download . (You have to manually close that pop-up window after you click Download .) |
| 6 | Open the downloaded CSV file for editing. There is a row for each user, and the MeetingPrivilege column contains their session type IDs as a comma-delimited list. |
| 7 | For each user you wish to grant the new session type, add 1561 as a new value in the comma-delimited list in the MeetingPrivilege cell. The Webex CSV File Format Reference contains details on the purpose and contents of the CSV file. |
| 8 | Open the Meeting site configuration panel in Control Hub. If you were already on the Meeting site list page, you may need to refresh it. |
| 9 | In the Licenses and Users section, click Bulk Manage . |
| 10 | Click Import and select the edited CSV, then click Import . Wait while the file is uploaded. |
| 11 | When the import is finished, you can click Import Results to review if there were any errors. |
| 12 | Go to the Users page and open one of the users to verify they have the new session type. |

| 1 | Sign in to Control Hub , and under Management , select Devices . |
|---|---|
| 2 | Select a device to open its configuration panel. |
| 3 | Select the domain you want to use to identify this device. |
| 4 | Repeat for other devices. |

| 1 | Populate the device's ClientSecret with a plain text secret: The first time you populate the Secret , you supply it in plain text. That's why we recommend doing this at the physical device console. Base64url encode the secret phrase for this device. Open the TShell on the device. Run xcommand Security ClientSecret Populate Secret: "MDEyMzQ1Njc4OWFiY2RlZg" The example command above populates the Secret with the phrase 0123456789abcdef . You need to choose your own. The device has its initial secret. Don't forget this; you can't recover it and must factory-reset the device to start again. |
|---|---|
| 2 | Concatenate your certificate and private key: Using a text editor, open the .pem files, paste the key blob the certificate blob, and save it as a new .pem file. This is the payload text you'll encrypt and put in your JWE blob. |
| 3 | Create a JWE blob to use as input to the certificate add command: Create a random sequence of at least 4 bytes. This is your salt. Derive a content encryption key with your scrypt tool. For this you need the secret, the salt, and a keylength to match your chosen encryption cipher. There are some other fixed values to supply (N=32768, r=8, p=1). The device uses the same process and values to derive the same content encryption key. Create a random sequence of exactly 12 bytes. This is your initialization vector. Create a JOSE header, setting alg , enc , and cisco-kdf keys as described in Understanding External Identity Process for Devices . Set the "add" action using the key:value "cisco-action":"add" in your JOSE header (because we're adding the certificate to the device). Base64url encode the JOSE header. Use your JWE encryption tool with the chosen cipher and the base64url encoded JOSE header to encrypt the text from the concatenated pem file. Base64url encode the initialization vector, the encrypted PEM payload, and the authentication tag. Construct the JWE blob as follows (all values are base64url encoded): JOSEHeader..InitVector.EncryptedPEM.AuthTag |
| 4 | Open the TShell on the device and run the (multiline) add command: xcommand Security Certificates Services Add IsEncrypted: True
your..JWE.str.ing\n
.\n |
| 5 | Verify the certificate is added by running xcommand Security Certificates Services Show Copy the new certificate's fingerprint. |
| 6 | Activate the certificate for the purpose WebexIdentity : Read the fingerprint of the certificate, either from the certificate itself or from the output of xcommand Security Certificates Services Show . Create a random sequence of at least 4 bytes, and base64url encode that sequence. This is your salt. Derive a content encryption key with your scrypt tool. For this you need the secret, the salt, and a keylength to match your chosen encryption cipher. There are some other fixed values to supply (N=32768, r=8, p=1). The device uses the same process and values to derive the same content encryption key. Create a random sequence of exactly 12 bytes, and base64url encode that sequence. This is your initialization vector. Create a JOSE header, setting alg , enc , and cisco-kdf keys as described in Understanding External Identity Process for Devices . Set the "activate" action using the key:value "cisco-action":"activate" in your JOSE header (because we're activating the certificate on the device). Base64url encode the JOSE header. Use your JWE encryption tool with the chosen cipher and the base64url encoded JOSE header to encrypt the certificate fingerprint. The tool should output a 16 or 32 byte sequence, depending on whether you chose 128 or 256 bit AES-GCM, and an authentication tag. Base64urlencode the encrypted fingerprint, and the authentication tag. Construct the JWE blob as follows (all values are base64url encoded): JOSEHeader..InitVector.EncryptedFingerprint.AuthTag Open the TShell on the device and run the following activate command: xcommand Security Certificates Services Activate Purpose: WebexIdentity Fingerprint: "Your..JWE.encrypted.fingerprint" The device has an encrypted, active, CA-issued certificate, ready to be used for identifying it in end-to-end encrypted Webex meetings. |
| 7 | Onboard the device to your Control Hub organization. |

| 1 | Schedule a meeting of the correct type ( Webex Meetings Pro-End to End Encryption_VOIPonly ). See Schedule a Webex Meeting with End-to-End Encryption . |
|---|---|
| 2 | Join the meeting as the host, from a Webex Meetings client. See Join a Webex Meeting with End-to-End Encryption . |
| 3 | Join the meeting from a device that has its identity verified by the Webex CA. |
| 4 | As the host, verify this device appears in the lobby with the correct identity icon. See Join a Webex Meeting with End-to-End Encryption . |
| 5 | Join the meeting from a device that has its identity verified by an external CA. |
| 6 | As the host, verify this device appears in the lobby with the correct identity icon. Learn more about identity icons . |
| 7 | Join the meeting as an unauthenticated meetings participant. |
| 8 | As the host, verify this participant appears in the lobby with the correct identity icon. |
| 9 | As the host, admit or reject people / devices. |
| 10 | Validate participant/device identities where possible by checking the certificates. |
| 11 | Check that everyone in the meeting sees the same meeting security code. |
| 12 | Join the meeting with a new participant. |
| 13 | Check that everyone sees  the same, new meeting security code. |

| Session Type ID | Public Service Name |
|---|---|
| 638 | E2E Encryption+VoIP only |
| 652 | Pro-End to End Encryption_VOIPonly |
| 660 | Pro 3 Free-End to End Encryption_VOIPonly E2E Encryption + Identity |
| 672 | Pro 3 Free50-End to End Encryption_VOIPonly |
| 673 | Education Instructor E2E Encryption_VOIPonly |
| 676 | Broadworks Standard plus end to end encryption |
| 677 | Broadworks Premium plus end to end encryption |
| 681 | Schoology Free plus end to end encryption |

| API call | Description |
|---|---|
| xConfiguration Conference EndToEndEncryption Identity PreferredDomain: "example.com" | This configuration is made when the admin sets the device's preferred domain from Control Hub. Only necessary if the organization has more than one domain. The device uses this domain when it requests a certificate from the Webex CA. The domain then  identifies the device. This configuration is not applicable when the device has an active, externally-issued certificate to identify itself. |
| xStatus Conference EndToEndEncryption Availability | Indicates if the device can join an end-to-end encrypted meeting. The cloud API calls it so that a paired app knows whether it can use the device to join. |
| xStatus Conference EndToEndEncryption ExternalIdentity Verification | Indicates if the device uses External verification (has an externally-issued certificate). |
| xStatus Conference EndToEndEncryption ExternalIdentity Identity | The identity of the device as read from the externally-issued certificate's Common Name. |
| xStatus Conference EndToEndEncryption ExternalIdentity CertificateChain Certificate # specificinfo | Reads specific information from an externally-issued certificate. In the command shown, replace # with the number of the certificate. Replace specificinfo with one of: Fingerprint NotAfter Validity end date NotBefore Validity start date PrimaryName PublicKeyAlgorithm SerialNumber SignatureAlgorithm Subject # Name A list of the subjects for the certificate (e.g. email address or domain name) Validity Gives the validity status of this certificate (e.g. valid or expired ) |
| xStatus Conference EndToEndEncryption ExternalIdentity Status | The status of the device’s external identity (e.g. valid or error ). |
| xStatus Conference EndToEndEncryption InternalIdentity Verification | Indicates if the device has a valid certificate issued by the Webex CA. |
| xStatus Conference EndToEndEncryption InternalIdentity Identity | The identity of the device as read from the Webex-issued certificate's Common Name. Contains a domain name if the organization has a domain. Is empty if the organization does not have a domain. If the device is in an organization that has multiple domains, this is the value from the PreferredDomain . |
| xStatus Conference EndToEndEncryption InternalIdentity CertificateChain Certificate # specificinfo | Reads specific information from the Webex-issued certificate. In the command shown, replace # with the number of the certificate. Replace specificinfo with one of: Fingerprint NotAfter Validity end date NotBefore Validity start date PrimaryName PublicKeyAlgorithm SerialNumber SignatureAlgorithm Subject # Name A list of the subjects for the certificate (e.g. email address or domain name) Validity Gives the validity status of this certificate (e.g. valid or expired ) |
|  |

| API call | Description |
|---|---|
| xEvent Conference ParticipantList ParticipantAdded xEvent Conference ParticipantList ParticipantUpdated xEvent Conference ParticipantList ParticipantDeleted | These three events now include EndToEndEncryptionStatus , EndToEndEncryptionIdentity , and EndToEndEncryptionCertInfo for the affected participant. |
|  |

| API call | Description |
|---|---|
| xCommand Security ClientSecret Populate Secret: "base64url-encoded" or xCommand Security ClientSecret Populate Secret: JWEblob | Accepts a base64url encoded plain text value for seeding the client secret on the device for the first time. To update the secret after that first time, you must supply a JWE blob containing the new secret encrypted by the old secret. |
| xCommand Security Certificates Services Add JWEblob | Adds a certificate (with private key). We extended this command to accept a JWE blob containing the encrypted PEM data. |
| xCommand Security Certificates Services Activate Purpose:WebexIdentity FingerPrint: JWEblob | Activates a specific certificate for WebexIdentity. For this Purpose ,   the command requires the identifying fingerprint to be encrypted and serialized in a JWE blob. |
| xCommand Security Certificates Services Deactivate Purpose:WebexIdentity FingerPrint: JWEblob | Deactivates a specific certificate for WebexIdentity. For this Purpose ,   the command requires the identifying fingerprint to be encrypted and serialized in a JWE blob. |
|  |

## Figuras

![Download button](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469792.jpg)