---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-3pcc-english-9-3-4-admin-guide-8831-3pcc-ag-standard-features-ht-4c8a2d2a04
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/3PCC/english/9_3_4/admin-guide/8831-3pcc-ag/standard-features.html
retrieved_at: 2026-08-21T02:09:18.219875+00:00
---

Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Administration Guide, Release 9.3(4)

# Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Administration Guide, Release 9.3(4)

Updated: October 22, 2014

Chapter: Customize Standard Features

## Chapter: Customize Standard Features

## Configure Phone Information and Display Settings

The phone web user interface allows you to customize settings such as the phone name, background picture, logo, and screen saver.

### Configure the Phone Name

Navigate to Admin Login > advanced > Voice > Phone .

Under General , enter the Station Display Name for the phone. This name displays on the phone LCD GUI in the top left corner.

### Customize the Startup Screen

You can create a text or 128-by-48 pixel by 1-bit deep image logo to display when the conference phone boots up. A logo displays during the boot sequence for a short period after the Cisco logo displays.

To configure a custom logo:

Step 1 Click Admin Login > advanced > Voice > Phone .

To display a text logo, in the Text Logo field enter text as follows:

- Up to two lines of text

- Each line must be less than 32 characters

- Insert a new line character (\n) and escape code (%0a) between the two lines

For example, Super\n%0aTelecom displays:

- Use the + character to add spaces for formatting. You can add multiple + characters before and after the text to center it.

Step 2 To display a picture logo:

a. In the PNG Picture Download URL field, enter the path, for example:

http://192.168.2.244/pictures/image04_128x48.png

(you can also use a TFTP server)

b. Change Select Logo to PNG Picture.

Step 3 Click Submit All Changes . The phone reboots, retrieves the.png file, and displays the picture when it next boots.

Note The phone image file types supported are:

- Bitmap format, 1 bit-per-pixel color, size 128-by-48 pixels.

### Change the Display Background Picture

You can use a picture to customize the background on the phone screen.

When the PNG Picture Download URL is changed, the phone compares the URL to the previous image URL. (If the URLs are the same, the phone does not perform the download.) If the URLs are different, the phone downloads the new image and displays it (providing the Select Background Picture field is set to PNG Picture ).

The phone does not reboot after you change the background image URL.

A background image is displayed while the phone is running. To display a logo during the phone boot sequence.

Step 1 Copy the image to a TFTP or HTTP server that is accessible from the phone.

Step 2 Click Admin Login > advanced > Voice > Phone .

Step 3 Select the background picture in the Select Background Picture menu:

- None–Does not display a background picture.

- PNG Picture–Displays the PNG Picture Download URL picture.

- Text Logo–Displays the text string in the Text Logo field.

Step 4 If you selected None, in Step 3 , go to Step 6 . If you selected Text Logo in Step 3 , go to Otherwise, enter the URL of the image file you want in PNG Picture Download URL . The URL must include the TFTP or HTTP server name (or IP address), directory, and filename, for example:

or

If the HTTP Refresh Timer is set in the server response to PNG Picture Download URL , the phone downloads the picture from the link and displays it on the phone scree. The phone automatically retrieves the picture after the specified number of seconds.

Step 5 If you selected Text Logo , enter a text string in the Text Logo field.

Step 6 Click Submit All Changes .

### Configure the Screen Saver

You can configure a screen saver for the IP conference phone. When the phone is idle for a specified time, it enters screen saver mode.

Any button press returns the phone to normal mode. If a user password is set, the user must enter it to exit screen saver mode.

To configure the screen saver:

Step 1 Click Admin Login > advanced > Voice > Phone .

In the General section, in the Screen Saver Enable field, choose Yes to enable.

Step 2 In the Screen Saver Wait field, enter the number of seconds of idle time to elapse before the screen saver starts.

Step 3 In the Screen Saver Icon field, choose the display type:

- A background picture.

- The station time in the middle of the IP phone screen.

- A moving padlock icon. When the phone is locked, the status line displays a scrolling message “Press any key to unlock your phone.”

- Cisco logo.

- The station date and time on the IP phone screen.

Step 4 Click Submit All Changes .

### Configure the LCD Contrast

You can configure the LCD contrast on the IP conference phone.

To configure the contrast for the IP phone screen on the phone:

Step 1 Click Admin Login > advanced > User .

Step 2 Under LCD , in the LCD Contrast field, enter a number value from 1 to 30. The higher the number, the greater the contrast on the IP phone screen.

Step 3 Click Submit All Changes .

### Configure Back Light Settings

To configure the back light settings for the IP phone screen on the phone:

Step 1 Click Admin Login > advanced > Voice > User .

Step 2 Under LCD in the Back Light Timer field, enter the number of seconds of idle time that can elapse before the back light turns off.

Step 3 Click Submit All Changes .

### Call Appearances Per Line

The IP conference phone is a single-line conference phone.

To expand the call appearances per line:

Step 1 Click Admin Login > advanced > Voice > Phone .

Step 2 In the Miscellaneous Line Key Settings section in the Call Appearance Per Line field, choose how many calls per line to allow from the drop-down.

## Enable Call Features

This section describes how to enable and disable call features on the IP conference phone.

### Enable Call Transfer and Call Forwarding Services

You can transfer or forward a call when the service is enabled.

Step 1 Click Admin Login > advanced > Voice > Phone .

Step 2 Under Supplementary Services , under the transfer type you want to enable, choose Yes :

- Attn Transfer Serv —Attended call transfer service. The user answers the call before transferring it.

- Blind Transfer Serv —Blind call transfer service. The user transfers the call without speaking to the caller.

You can also enable or disable call forwarding:

- Cfwd All —Forwards all calls.

- Cfwd Busy —Forwards calls only if the line is busy.

- Cfwd No Ans —Forwards calls only if the line is not answered.

Step 3 Click Submit All Changes .

### Enable Conferencing

To allow the user to perform call conferencing, navigate to Admin Login > advanced > Voice > Phone . Under Supplementary Services in the Conference Serv field, choose Yes to enable.

### Enable Do Not Disturb

You can allow users to turn the Do Not Disturb feature on or off. This feature plays a message to the caller saying the user is unavailable. On the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control, the users can press the Ignore softkey to divert a ringing call to another destination.

This feature is not configurable on web page, and only applicable using the LCD soft key.

## Configure Ring Tones

Click Admin Login > advanced >Info > Download Status and scroll to the Downloaded Ring Tone section to see the status of the ringtone download.

### Assign a Ring Tone to an Extension

To assign a ring tone to an extension:

Step 1 Click Admin Login > advanced > Voice > Extension tab.

Step 2 Under Call Feature Settings in the Default Ring field, choose from the following:

- No Ring

- 1 through 10

Step 3 Click Submit All Changes .

## Configure Audio Settings

You can configure default audio settings for the phone. The volume settings can be modified by the user by pressing the volume control button on the phone, then pressing the Save soft button.

To configure the audio volume settings:

Step 1 Click Admin Login > advanced > Voice > User .

Step 2 In the Audio Volume section, configure a volume level between 1 and 10, with 1 being the lowest level:

Ringer Volume

Sets the volume for the ringer.

Speaker Volume

Sets the volume for the full-duplex speakerphone.

Step 3 Click Submit All Changes .

### Configure the User Access Control

Only the user access attribute “ua” is respected by the conference phone device. For a specific parameter, the “ua” attribute defines access by the user account to the administration web server. If “ua” attribute is not specified, the factory default user access is applied for the corresponding parameter. Access by the Admin account is unaffected by this attribute.

Note The value of the element attributes must be enclosed by double quotes.

The “ua” attribute must have one of the following values:

- na – no access

- ro – read-only

- rw – read/write

## Enable and Configure the Phone Web Server

The web server allows administrators and users to log in to the phone by using a phone web user interface. Administrators and users have different privileges and see different options for the phone based on their role.

### Configure the Web Server from the Phone Web Interface

To enable the web server:

Step 1 Click Admin Login > advanced > System .

Step 2 Under the System Configuration section in the Enable Web Server field, verify that the parameter is set to Yes to enable the web administration server.

Step 3 In the Web Server Port field, enter the port to access the web server. The default is port 80.

Step 4 In the Enable Web Admin Access field, you can enable or disable local access to the Admin Login of the phone web user interface. Defaults to Yes (enabled.)

Step 5 In the Admin Passwd field, enter a password if you want the system administrator to log in to the phone web user interface with a password. The password prompt appears when an administrator clicks Admin Login . The maximum password length is 32 characters.

Step 6 In the User Password field, enter a password if you want users to log in to the phone web user interface with a password. The password prompt appears when users click User Login . The maximum password length is 32 characters

Step 7 Click Submit All Changes .

### Configure the Web Server from the Phone Screen Interface

To enable the phone web user interface from the Phone tab:

Step 1 Press menu.

Step 2 Select Network and Enable Web Server .

Step 3 Select Edit .

Step 4 Press y/n to toggle the selection to Yes and enable.

Step 5 Click OK > Save .

## Configure LDAP for the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control

The Cisco Unified IP Conference Phone 8831 for Third-Party Call Control supports Lightweight Directory Access Protocol (LDAP) v3. LDAP Corporate Directory Search allows a user to search a specified LDAP directory for a name, phone number, or both. LDAP-based directories, such as Microsoft Active Directory 2003 and OpenLDAP-based databases, are supported.

Users access LDAP from the Directory menu on their IP phone. There is a limit of 20 records returned from a LDAP search.

The instructions in this section assume you have the following equipment and services:

- A LDAP server, such as OpenLDAP or Microsoft Active Directory Server 2003

To prepare the LDAP Corporate Directory Search:

Step 1 Click Admin Login > advanced > System .

Step 2 In the Optional Network Configuration section, under Primary DNS , enter the IP address of the DNS server. (Only required if using Active Directory with authentication set to MD5.)

Step 3 In the Optional Network Configuration section, under Domain , enter the LDAP domain. (Only required if using Active Directory with authentication set to MD5.)

Some sites might not deploy DNS internally and instead use Active Directory 2003. In this case, it is not necessary to enter a Primary DNS address and an LDAP Domain. However, with Active Directory 2003, the authentication method is restricted to Simple.

Step 4 Click the Phone tab.

Step 5 Under LDAP , in the LDAP Dir Enable field, choose Yes to enable LDAP and cause the name defined in LDAP Corp Dir Name to appear in the phone directory.

Step 6 Configure values for the fields in the following table and click Submit All Changes .

LDAP Corp Dir Name

Enter a free-form text name, such as Corporate Directory .

LDAP Server

Enter a fully qualified domain name or IP address of LDAP server, in the format nnn.nnn.nnn.nnn .

Enter the host name of the LDAP server if the MD5 authentication method is used.

LDAP Auth Method

Select the authentication method that the LDAP server requires:

None—No authentication is used between the client and the server.

Simple—The client sends its fully-qualified domain name and password to the LDAP server. Might create security issues.

Digest-MD5—The LDAP server sends authentication options and a token to the client. The client returns an encrypted response that is decrypted and verified by the server.

LDAP Client DN

Enter the distinguished name domain components [dc] ; for example: dc=cv2bu,dc=com

If using the default Active Directory schema (Name(cn)->Users->Domain), example of the client DN: cn="David Lee",dc=users,dc=cv2bu,dc=com

LDAP Username

Enter the username for a credentialed user on the LDAP server.

LDAP Password

Enter the password for the LDAP username.

LDAP Search Base

Specify a starting point in the directory tree from which to search. Separate domain components [dc] with a comma. For example: dc=cv2bu,dc=com

LDAP Last Name Filter

Define the search for surnames [sn], known as last name in some parts of the world. For example, sn:(sn=*$VALUE*) . This searches for the text string anywhere in the beginning, middle, or at the end of a name.

You must enter a value in both the last name and first name fields so that the LDAP corporate directory option displays on the phone. If both fields are empty, the directory does not display.

LDAP First Name Filter

Define the search for the common name [cn] . For example, cn:(cn=*$VALUE*) . This searches for the text string anywhere in the beginning, middle, or at the end of a name.

You must enter a value in both the last name and first name fields so that the LDAP corporate directory option displays on the phone. If both fields are empty, the directory does not display.

LDAP Search Item 3

Enter a customized search item. Can be blank if not needed.

LDAP Item 3 Filter

Enter a customized filter for the searched item. Can be blank if not needed.

LDAP Search Item 4

Enter a customized search item. Can be blank if not needed.

LDAP Item 4 Filter

Enter a customized filter for the searched item. Can be blank if not needed.

LDAP Display Attrs

Enter the format of LDAP results display on phone where:

- a—Attribute name

- cn—Common name

- sn—Surname (last name)

- telephoneNumber—Phone number

- n—Display name

For example, n=Phone causes Phone: to be displayed in front of the phone number of an LDAP query result when the detail soft button is pressed.

- t—type

When t=p , t is of type phone number and the retrieved number can be dialed. Only one number can be made dialable. If two numbers are defined as dialable, only the first number is used. For example, a=ipPhone, t=p; a=mobile, t=p;

This example results in only the ipPhone number being dialable and the mobile number is ignored.

- p—phone number

When p is assigned to a type attribute, example t=p , the the retrieved number is dialable.

LDAP Number Mapping

With the LDAP number mapping you can manipulate the number that was retrieved from the LDAP server. For example, you can append 9 to the number if your dial plan requires a user to enter 9 before dialing. Add the 9 prefix by adding (<:9>xx.>) to the LDAP Number Mapping field. For example, 555 1212 will become 9555 1212. Can be blank if not needed.

If you do not manipulate the number in this fashion, a user can use the Edit Dial feature to edit the number before dialing out.

## Configure BroadSoft Settings

The BroadSoft directory service enables users to search and view their personal, group, or enterprise contacts. This application feature uses BroadSoft's Extended Services Interface (XSI).

To configure the BroadSoft Directory service:

Step 1 Click Admin Login > advanced > Voice > Phone .

Step 2 Under Broadsoft Settings , configure the following:

- Directory Enable: Set to Yes .

- XSI Host Server: Enter the name of the server; for example, xsp.xdp.com .

- Directory Name: Name of the directory. Displays on the user phone as a directory choice (for example, John’s Personal Directory ).

- Directory Type: Select the type of BroadSoft directory:

– Enterprise (default): Allows users to search on last name, first name, user or group ID, phone number, extension, department, or email address.

– Group: Allows users to search on last name, first name, user ID, phone number, extension, department, or email address.

– Personal: Allows users to search on last name, first name, or telephone number.

- Directory UserID: BroadSoft User ID of the phone user; for example, johndoe@xdp.com.

- Directory Password: Alphanumeric password associated with the User ID.

To improve security, the phone firmware places access restrictions on the host server and directory name entry fields.

Dir. Name

Admin password required (if set)

Host Server

Admin password required (if set)

Type

None

User ID

None

Password

None

Step 3 Click Submit All Changes .

| Parameter | Description |
|---|---|
| Ringer Volume | Sets the volume for the ringer. |
| Speaker Volume | Sets the volume for the full-duplex speakerphone. |

| Parameter | Description |
|---|---|
| LDAP Corp Dir Name | Enter a free-form text name, such as Corporate Directory . |
| LDAP Server | Enter a fully qualified domain name or IP address of LDAP server, in the format nnn.nnn.nnn.nnn . Enter the host name of the LDAP server if the MD5 authentication method is used. |
| LDAP Auth Method | Select the authentication method that the LDAP server requires: None—No authentication is used between the client and the server. Simple—The client sends its fully-qualified domain name and password to the LDAP server. Might create security issues. Digest-MD5—The LDAP server sends authentication options and a token to the client. The client returns an encrypted response that is decrypted and verified by the server. |
| LDAP Client DN | Enter the distinguished name domain components [dc] ; for example: dc=cv2bu,dc=com If using the default Active Directory schema (Name(cn)->Users->Domain), example of the client DN: cn="David Lee",dc=users,dc=cv2bu,dc=com |
| LDAP Username | Enter the username for a credentialed user on the LDAP server. |
| LDAP Password | Enter the password for the LDAP username. |
| LDAP Search Base | Specify a starting point in the directory tree from which to search. Separate domain components [dc] with a comma. For example: dc=cv2bu,dc=com |
| LDAP Last Name Filter | Define the search for surnames [sn], known as last name in some parts of the world. For example, sn:(sn=*$VALUE*) . This searches for the text string anywhere in the beginning, middle, or at the end of a name. You must enter a value in both the last name and first name fields so that the LDAP corporate directory option displays on the phone. If both fields are empty, the directory does not display. |
| LDAP First Name Filter | Define the search for the common name [cn] . For example, cn:(cn=*$VALUE*) . This searches for the text string anywhere in the beginning, middle, or at the end of a name. You must enter a value in both the last name and first name fields so that the LDAP corporate directory option displays on the phone. If both fields are empty, the directory does not display. |
| LDAP Search Item 3 | Enter a customized search item. Can be blank if not needed. |
| LDAP Item 3 Filter | Enter a customized filter for the searched item. Can be blank if not needed. |
| LDAP Search Item 4 | Enter a customized search item. Can be blank if not needed. |
| LDAP Item 4 Filter | Enter a customized filter for the searched item. Can be blank if not needed. |
| LDAP Display Attrs | Enter the format of LDAP results display on phone where: a—Attribute name cn—Common name sn—Surname (last name) telephoneNumber—Phone number n—Display name For example, n=Phone causes Phone: to be displayed in front of the phone number of an LDAP query result when the detail soft button is pressed. t—type When t=p , t is of type phone number and the retrieved number can be dialed. Only one number can be made dialable. If two numbers are defined as dialable, only the first number is used. For example, a=ipPhone, t=p; a=mobile, t=p; This example results in only the ipPhone number being dialable and the mobile number is ignored. p—phone number When p is assigned to a type attribute, example t=p , the the retrieved number is dialable. |
| LDAP Number Mapping | With the LDAP number mapping you can manipulate the number that was retrieved from the LDAP server. For example, you can append 9 to the number if your dial plan requires a user to enter 9 before dialing. Add the 9 prefix by adding (<:9>xx.>) to the LDAP Number Mapping field. For example, 555 1212 will become 9555 1212. Can be blank if not needed. If you do not manipulate the number in this fashion, a user can use the Edit Dial feature to edit the number before dialing out. |

| Field | Access Restriction |
|---|---|
| Dir. Name | Admin password required (if set) |
| Host Server | Admin password required (if set) |
| Type | None |
| User ID | None |
| Password | None |