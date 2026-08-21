---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-bbe1abb2e3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_mp_f5020a69_00_ftp_client.html
retrieved_at: 2026-08-21T17:25:18.776175+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter: FTP_Client

## Chapter: FTP_Client

# FTP_Client

The FTP_Client element is used to upload a
                        local file to one or more FTP servers. If there are multiple FTP servers
                        specified, the file is uploaded concurrently to the FTP servers.

## Settings

Name
                                             (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Validation Enforced by Call
                                             Studio

Notes

filename

(Name of file to be transferred)

string

Yes

true

true

None

Must be a valid Windows
                                          filename.

This setting specifies
                                          the full pathname of the file to transfer. Alternatively, a path relative to
                                          the application directory can be used.

remote_filename

(Remote Filename)

string

No

true

true

None

If specified, must be a
                                          valid Windows filename.

This is the
                                          FTP server target filename. If a remote filename is not specified, the remote
                                          filename will be the same as the input filename.

ftp_hosts

(FTP Server or FTP
                                          Servers)

string

Yes

true

true

None

Must conform to the
                                          format listed in "Notes".

Validation will fail if the password is
                                          set, but the username is not.

This is
                                          the list of FTP server host names or IP addresses to transfer the file to. Each
                                          FTP server entry may optionally specify a port number (default port:21),
                                          username and password in the format host|port|username|password . Server entries are
                                          delimited by a space character. You can enter multiple hosts on one line or
                                          separate lines or both. If any field requires spaces, vertical bars (|) or
                                          equals symbols (=), they may be escaped with \s, \p or \e, respectively.

ftp_user

(Default Username)

string

Yes

true

true

None

Validation will fail if the password field is set while this field is not
                                          set.

User name to use when
                                          transferring the file. This value may be overridden on a per-server basis. If
                                          left blank, "anonymous" will be assumed.

ftp_password

(Default
                                          Password)

string

No

true

true

None

n/a

This is the password to use when transferring the
                                          file. This value can be overridden on a per-server basis.

ftp_path

(FTP
                                          Path)

string

No

true

true

None

Must be a valid Windows
                                          pathname.

This is the directory on
                                          the FTP server where to transfer the file. Use the forward slash as the
                                          directory delimiter dir/subdir . The directory will
                                          be created if it does not already exist.

delete_file_on_success

(Delete file if
                                          file transferred successfully)

boolean

No

true

true

true

n/a

This setting deletes the
                                          file after it has been successfully transferred to all FTP
                                          Server(s).

## Element Data

Element data is created only when the exit state setting is not done . If the exit state is done , no element data is
                                          created.

Name

Type

Notes

failed_servers

string

One or more space
                                          delimited host names or IP addresses of Server(s) where the input file was not
                                          successfully transferred. This data is created only if the exit state is
                                          not done .

failed_server_reasons

string

One or more
                                          space delimited reason codes indicating why a file was not successfully
                                          transferred:

connection_error: There was an error connecting to the FTP
                                                server. This may be caused by an invalid or blocked port.

extraneous_data: There were extra fields for
                                                a given server in the ftp_hosts setting.

invalid_filename: The name of the file to
                                                transfer is invalid or the file doesn't exist.

invalid_port: The port for an FTP server is
                                                invalid.

missing_username: The
                                                password for an FTP server was specified, but the username was left blank. They
                                                must either both be specified or both left blank.

unknown: An unknown error has
                                                occurred.

unknown_host: An FTP
                                                server could not be reached. Possible reasons include an incorrect hostname or
                                                network connectivity problems. A three-digit number: An FTP server sent back an
                                                unexpected reply code. Additional information will appear in the error
                                                log.

A three-digit number: An
                                                FTP server sent back an unexpected reply code. Additional information will
                                                appear in the error log.

A Java
                                                   exception: An unexpected exception was handled. Additional
                                                information will appear in the error log.

failed_servers_count

string

Number of failed FTP transfers. This data is created only if the exit
                                          state is not done .

## Exit States

Name

Notes

error

This exit state is used if an error occurred and the file was not
                                          transferred to any FTP Server(s).

partial_success

This exit state is used when not all FTP transfers were
                                          successful.

done

This exit state means the
                                          file was successfully transferred to all FTP Server(s).

## Other

Studio Element Folder: Integration

Class Name: com.cisco.cvp.vxml.custelem.FTP

## Events

Name (Label)

Notes

Event Type

You can
                                          				  select Java Exception as event handler type.

The output of the Customer_Lookup element can be in JSON format . To know more about parsing the JSON Data refer to "Parsing
                              JSON Data" section in User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio.

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Validation Enforced by Call
                                             Studio | Notes |
|---|---|---|---|---|---|---|---|
| filename (Name of file to be transferred) | string | Yes | true | true | None | Must be a valid Windows
                                          filename. | This setting specifies
                                          the full pathname of the file to transfer. Alternatively, a path relative to
                                          the application directory can be used. |
| remote_filename (Remote Filename) | string | No | true | true | None | If specified, must be a
                                          valid Windows filename. | This is the
                                          FTP server target filename. If a remote filename is not specified, the remote
                                          filename will be the same as the input filename. |
| ftp_hosts (FTP Server or FTP
                                          Servers) | string | Yes | true | true | None | Must conform to the
                                          format listed in "Notes". Validation will fail if the password is
                                          set, but the username is not. | This is
                                          the list of FTP server host names or IP addresses to transfer the file to. Each
                                          FTP server entry may optionally specify a port number (default port:21),
                                          username and password in the format host\|port\|username\|password . Server entries are
                                          delimited by a space character. You can enter multiple hosts on one line or
                                          separate lines or both. If any field requires spaces, vertical bars (\|) or
                                          equals symbols (=), they may be escaped with \s, \p or \e, respectively. |
| ftp_user (Default Username) | string | Yes | true | true | None | Validation will fail if the password field is set while this field is not
                                          set. | User name to use when
                                          transferring the file. This value may be overridden on a per-server basis. If
                                          left blank, "anonymous" will be assumed. |
| ftp_password (Default
                                          Password) | string | No | true | true | None | n/a | This is the password to use when transferring the
                                          file. This value can be overridden on a per-server basis. |
| ftp_path (FTP
                                          Path) | string | No | true | true | None | Must be a valid Windows
                                          pathname. | This is the directory on
                                          the FTP server where to transfer the file. Use the forward slash as the
                                          directory delimiter dir/subdir . The directory will
                                          be created if it does not already exist. |
| delete_file_on_success (Delete file if
                                          file transferred successfully) | boolean | No | true | true | true | n/a | This setting deletes the
                                          file after it has been successfully transferred to all FTP
                                          Server(s). |

| Note | Default
                                       ftp_user/ftp_password will be used if ftp_hosts setting does not include a
                                       username/password in its definition. |
|---|---|

| Note | It is important to ensure
                                       that the FTP Server(s) are open for write access. |
|---|---|

| Note | The file to be
                                       uploaded is assumed to be a binary file. |
|---|---|

| Note | If a large file is to be
                                       transferred and the network connection to the FTP servers is slow and
                                       there are multiple FTP servers, consider implementing VXML 'fetchaudio'
                                       functionality in the element before the FTP element so that the caller does not
                                       hear silence while the FTP operation is in progress. |
|---|---|

| Note | The http
                                       client response timeout setting on the gateway must be set to accommodate the
                                       time it takes to complete the largest anticipated FTP file transfer. If an FTP
                                       file transfer takes longer than the configured duration in seconds for http
                                       client response timeout, the FTP transfer will complete correctly, but the call will drop as soon as the configured timeout duration is
                                          met . |
|---|---|

| Element data is created only when the exit state setting is not done . If the exit state is done , no element data is
                                          created. |
|---|

| Name | Type | Notes |
|---|---|---|
| failed_servers | string | One or more space
                                          delimited host names or IP addresses of Server(s) where the input file was not
                                          successfully transferred. This data is created only if the exit state is
                                          not done . |
| failed_server_reasons | string | One or more
                                          space delimited reason codes indicating why a file was not successfully
                                          transferred: connection_error: There was an error connecting to the FTP
                                                server. This may be caused by an invalid or blocked port. extraneous_data: There were extra fields for
                                                a given server in the ftp_hosts setting. invalid_filename: The name of the file to
                                                transfer is invalid or the file doesn't exist. invalid_port: The port for an FTP server is
                                                invalid. missing_username: The
                                                password for an FTP server was specified, but the username was left blank. They
                                                must either both be specified or both left blank. unknown: An unknown error has
                                                occurred. unknown_host: An FTP
                                                server could not be reached. Possible reasons include an incorrect hostname or
                                                network connectivity problems. A three-digit number: An FTP server sent back an
                                                unexpected reply code. Additional information will appear in the error
                                                log. A three-digit number: An
                                                FTP server sent back an unexpected reply code. Additional information will
                                                appear in the error log. A Java
                                                   exception: An unexpected exception was handled. Additional
                                                information will appear in the error log. |
| failed_servers_count | string | Number of failed FTP transfers. This data is created only if the exit
                                          state is not done . |

| Name | Notes |
|---|---|
| error | This exit state is used if an error occurred and the file was not
                                          transferred to any FTP Server(s). |
| partial_success | This exit state is used when not all FTP transfers were
                                          successful. |
| done | This exit state means the
                                          file was successfully transferred to all FTP Server(s). |

| Name (Label) | Notes |
|---|---|
| Event Type | You can
                                          				  select Java Exception as event handler type. |