---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su1-install-guide-uccx-b-1251-6eca01f611
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su1/install/guide/uccx_b_1251su1install-and-upgrade-guide/uccx_b_1252install-and-upgrade-guide_chapter_011.html
retrieved_at: 2026-08-16T21:13:29.319850+00:00
---

Cisco Unified Contact Center Express Install and Upgrade Guide, Release 12.5(1) SU1

# Cisco Unified Contact Center Express Install and Upgrade Guide, Release 12.5(1) SU1

Updated: January 31, 2021

Chapter: Post-Installation Tasks

## Chapter: Post-Installation Tasks

# Post-Installation Tasks

## Configure the First Node

### Before you begin

After a successful installation, perform one of the following:

If the Cisco Unified Communications Manager (CUCM) cluster is using the self-signed certificate, upload Tomcat certificates
                                    from all the nodes of CUCM cluster into the Unified CCX Tomcat trust store. To upload certificates, use the Cisco Unified
                                    OS Administration interface (for example, https://<uccx-hostname>/cmplatform ) or the set cert import trust tomcat CLI.

If the Cisco Unified Communications Manager (CUCM) cluster is using the CA signed certificate, upload the root CA certificate
                                    into Unified CCX Tomcat trust store.

Verify that the following users are added in Unified Communications Manager application:

Unified CM Users - These are end users in Unified Communications Manager, who are assigned in Unified CCX as administrators.
                                    Using administrator credentials, you can login to the following components for Unified CCX:

Unified CCX Application Administration

Cisco Unified CCX Serviceability

Cisco Finesse Administration

Cisco Unified Intelligence Center Administration

Cisco Identity Service

Disaster Recovery System

Cisco Unified Serviceability

These users are
                              		  required to integrate Unified Communications Manager with Unified CCX. For
                              		  information on adding Unified CM users, see topic "Adding Users to a User
                              		  Group" under the "User
                                 			 Management Configuration" section and "User Group
                                 			 Configuration" sub section in the Cisco Unified
                                       				  Communications Manager Administration Guide at:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Step 1

Log in to Cisco
                                          				Unified CCX Administration page on the first node to initiate the
                                       			 configuration using the following URL format:

http://<servername or IP
                                             				  address>/appadmin

User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02.

Step 2

Follow
                                       			 instructions on the screen to complete the configurations.

### What to do next

Add Second Node

## Configure the Second Node

Upload Tomcat certificates from all the nodes of Cisco Unified Communications Manager cluster into the second node and restart
                              it.

Step 1

Log in to
                                       			 Cisco Unified CCX Administration page of the second node to initiate the
                                       			 configuration.

Use the credentials entered for Application User Name and Application User Password during installation.

User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02.

Step 2

In the Welcome
                                          				to Unified CCX Replication Wizard page, enter values for all the
                                       			 fields and click Next .

Step 3

In the Component Activation page, wait until all the
                                       			 components get activated and then click Next .

If you have
                                          				selected Network Deployment Type as LAN, the Cisco
                                             				  Unified CCX Setup Result Information page gets displayed.

Step 4

If you have selected Network Deployment Type as WAN, enter appropriate values in Cisco Unified CM Configuration page. Follow the instructions on the screen to complete the configurations.

Step 5

Restart the first node and then restart the second node.

## Configure Network Protocol
                           	 for the Unified Intelligence Center Cluster

Cisco Unified
                           		Intelligence Center supports Multicast and TCP/IP as the network protocol. The
                           		default configuration is Multicast.

utils
                                       				cuic cluster mode tcp-ip

utils
                                       				cuic cluster show

## Switch Network
                        	 Deployment from LAN to WAN

You can change a LAN-based two-node setup to work over WAN.
                              		  To change the network deployment from LAN to WAN for a two-node setup, do the
                              		  following:

Step 1

Log in to the first node using the Unified CCX Administration web
                                       			 interface.

Step 2

Choose System > Server ,
                                       			 and delete the second node from the list.

Step 3

Add the second node details again on the first node. See Add Second Node .

Step 4

Reinstall node 2. See Install Unified CCX on Second Node

Step 5

Configure the second node, and select the Network Deployment Type as WAN. See Configure Second Node .

Step 6

Add or configure new Unified Communications Manager Telephony Call
                                       			 Control Groups for the second node.

For more information, see the Unified CM Telephony Call Control Group configuration section in Cisco Unified Contact Center Express Admin and Operations Guide .

## Upload Self-Signed Certificate

The same procedure can be followed to upload CCP and Standalone CUIC self-signed
                                          certificates.

Step 1

Log in to Cisco Unified OS Platform CLI using administrator credentials.

Step 2

Enter the show cert own tomcat command to view the CUCM certificate details.

Step 3

Copy the certificate information starting from -----BEGIN
                                          CERTIFICATE----- to -----END CERTIFICATE----- and
                                       press Enter .

### Example:

```
-----BEGIN CERTIFICATE-----
MIID+TCCAuGgAwIBAgIQRMN6rnHtbGwm1nNqJ1pCfTANBgkqhkiG9w0BAQsFADB1
MQswCQYDVQQGEwJJTjEOMAwGA1UECgwFQ0lTQ08xDjAMBgNVBAsMBUNCQUJVMR4w
HAYDVQQDDBVsb2FkdWNjeC1uMS5jaXNjby5jb20xEjAQBgNVBAgMCUtBUk5BVEFL
QTESMBAGA1UEBwwJQkFOR0FMT1JFMB4XDTIwMTAxMjA2NDQzN1oXDTIyMTAxMjA2
NDQzNlowdTELMAkGA1UEBhMCSU4xDjAMBgNVBAoMBUNJU0NPMQ4wDAYDVQQLDAVD
QkFCVTEeMBwGA1UEAwwVbG9hZHVjY3gtbjEuY2lzY28uY29tMRIwEAYDVQQIDAlL
QVJOQVRBS0ExEjAQBgNVBAcMCUJBTkdBTE9SRTCCASIwDQYJKoZIhvcNAQEBBQAD
ggEPADCCAQoCggEBAMPL3K6yC5i7n/KidIpae3KMoet7BA5V+IT0x7Wyz9OV6M+U
rOJPsSryNiDwMYMeUFfpY4pxaA5KD4Hqh5pzWt887fc7nmMZIqb+tJutbeClEFeP
QIAbB1hLRYMGnMyqppVAmrvYwRCDCQfaOVMUDTFACLFtF4xxyJl+ov3AdRuHew7b
rw1wsnhI2dR3z/0CJ53wN5mdPmBEd83n5LIxLEH3HZBffz3anuJeHKkJg0TpTdd+
tWR3I0u/URaKcpci9q06h6bWrBmpYtM/hScYnS0ZuqVU0aO1Za7e7C+v4/CS1rOY
usnI0uLDZv/iVfuxcE0MoS8eqPxtH+0x4eK5lzECAwEAAaOBhDCBgTALBgNVHQ8E
BAMCArQwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMB0GA1UdDgQWBBTt
jixZBx6x+k6rZ0zaqQ4PA+jWHzASBgNVHRMBAf8ECDAGAQH/AgEAMCAGA1UdEQQZ
MBeCFWxvYWR1Y2N4LW4xLmNpc2NvLmNvbTANBgkqhkiG9w0BAQsFAAOCAQEAqhe+
B3duk1inR5pmzIWdjKvYYm4CtNeAn9tRYlK2BijKV6a0qDuZwSpN0dGblRr0epRI
thfkZvQGDzo5VZ45mVfxla+wxT3UrfmsoiKmncXBdaYhSsEoKbmWjHbsxwSklRWb
nZatxwglXTluPbF5F9wJSJHTTwPk3P0pjZENF09S5hY/xDEM7wfOrnKUETHJJPts
z4LArPgdaFbmWv8YLCp1YBcOI9mdxQnUUn4in6G9Nv5c9BYDKctPWKHhX8Hr7gO2
RTyBJc9tnhG4LjD0ykokeSp+5u77Xug9ZCtAgiliHZu7cWpGu9lRToiFklgah23+
XbRBYlZpO5v7rd6HbQ==
-----END CERTIFICATE-----
```

Step 4

Log in to Unified CCX CLI using administrator credentials.

Step 5

Enter the set cert import trust tomcat command to provide the CUCM certificate details.

Paste the copied CUCM certificate details and press Return .

| Step 1 | Log in to Cisco
                                          				Unified CCX Administration page on the first node to initiate the
                                       			 configuration using the following URL format: http://<servername or IP
                                             				  address>/appadmin Note Use the credentials entered for Application User Name and Application User Password during installation. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02. | Note | Use the credentials entered for Application User Name and Application User Password during installation. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02. |
|---|---|---|---|
| Note | Use the credentials entered for Application User Name and Application User Password during installation. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02. |
| Step 2 | Follow
                                       			 instructions on the screen to complete the configurations. Note Use the credentials of the Unified Communications Manager End User having administrator privileges in Unified CCX to configure
                                                   the application users (AXL users). | Note | Use the credentials of the Unified Communications Manager End User having administrator privileges in Unified CCX to configure
                                                   the application users (AXL users). |
| Note | Use the credentials of the Unified Communications Manager End User having administrator privileges in Unified CCX to configure
                                                   the application users (AXL users). |

| Note | Use the credentials entered for Application User Name and Application User Password during installation. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02. |
|---|---|

| Note | Use the credentials of the Unified Communications Manager End User having administrator privileges in Unified CCX to configure
                                                   the application users (AXL users). |
|---|---|

| Step 1 | Log in to
                                       			 Cisco Unified CCX Administration page of the second node to initiate the
                                       			 configuration. Note Use the credentials entered for Application User Name and Application User Password during installation. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02. | Note | Use the credentials entered for Application User Name and Application User Password during installation. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02. |
|---|---|---|---|
| Note | Use the credentials entered for Application User Name and Application User Password during installation. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02. |
| Step 2 | In the Welcome
                                          				to Unified CCX Replication Wizard page, enter values for all the
                                       			 fields and click Next . |
| Step 3 | In the Component Activation page, wait until all the
                                       			 components get activated and then click Next . If you have
                                          				selected Network Deployment Type as LAN, the Cisco
                                             				  Unified CCX Setup Result Information page gets displayed. |
| Step 4 | If you have selected Network Deployment Type as WAN, enter appropriate values in Cisco Unified CM Configuration page. Follow the instructions on the screen to complete the configurations. |
| Step 5 | Restart the first node and then restart the second node. |

| Note | Use the credentials entered for Application User Name and Application User Password during installation. User IDs are case-sensitive when logging into the Unified CCX Administration web interface. To make them case-insensitive,
                                                      you must install 12.5(1) SU1 ES02. |
|---|---|

| Step 1 | Log in to the first node using the Unified CCX Administration web
                                       			 interface. |
|---|---|
| Step 2 | Choose System > Server ,
                                       			 and delete the second node from the list. |
| Step 3 | Add the second node details again on the first node. See Add Second Node . |
| Step 4 | Reinstall node 2. See Install Unified CCX on Second Node |
| Step 5 | Configure the second node, and select the Network Deployment Type as WAN. See Configure Second Node . |
| Step 6 | Add or configure new Unified Communications Manager Telephony Call
                                       			 Control Groups for the second node. For more information, see the Unified CM Telephony Call Control Group configuration section in Cisco Unified Contact Center Express Admin and Operations Guide . |

| Note | The same procedure can be followed to upload CCP and Standalone CUIC self-signed
                                          certificates. |
|---|---|

| Step 1 | Log in to Cisco Unified OS Platform CLI using administrator credentials. |
|---|---|
| Step 2 | Enter the show cert own tomcat command to view the CUCM certificate details. The CUCM certificate is displayed. |
| Step 3 | Copy the certificate information starting from -----BEGIN
                                          CERTIFICATE----- to -----END CERTIFICATE----- and
                                       press Enter . Example: A sample certificate is as
                                       follows: -----BEGIN CERTIFICATE-----
MIID+TCCAuGgAwIBAgIQRMN6rnHtbGwm1nNqJ1pCfTANBgkqhkiG9w0BAQsFADB1
MQswCQYDVQQGEwJJTjEOMAwGA1UECgwFQ0lTQ08xDjAMBgNVBAsMBUNCQUJVMR4w
HAYDVQQDDBVsb2FkdWNjeC1uMS5jaXNjby5jb20xEjAQBgNVBAgMCUtBUk5BVEFL
QTESMBAGA1UEBwwJQkFOR0FMT1JFMB4XDTIwMTAxMjA2NDQzN1oXDTIyMTAxMjA2
NDQzNlowdTELMAkGA1UEBhMCSU4xDjAMBgNVBAoMBUNJU0NPMQ4wDAYDVQQLDAVD
QkFCVTEeMBwGA1UEAwwVbG9hZHVjY3gtbjEuY2lzY28uY29tMRIwEAYDVQQIDAlL
QVJOQVRBS0ExEjAQBgNVBAcMCUJBTkdBTE9SRTCCASIwDQYJKoZIhvcNAQEBBQAD
ggEPADCCAQoCggEBAMPL3K6yC5i7n/KidIpae3KMoet7BA5V+IT0x7Wyz9OV6M+U
rOJPsSryNiDwMYMeUFfpY4pxaA5KD4Hqh5pzWt887fc7nmMZIqb+tJutbeClEFeP
QIAbB1hLRYMGnMyqppVAmrvYwRCDCQfaOVMUDTFACLFtF4xxyJl+ov3AdRuHew7b
rw1wsnhI2dR3z/0CJ53wN5mdPmBEd83n5LIxLEH3HZBffz3anuJeHKkJg0TpTdd+
tWR3I0u/URaKcpci9q06h6bWrBmpYtM/hScYnS0ZuqVU0aO1Za7e7C+v4/CS1rOY
usnI0uLDZv/iVfuxcE0MoS8eqPxtH+0x4eK5lzECAwEAAaOBhDCBgTALBgNVHQ8E
BAMCArQwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMB0GA1UdDgQWBBTt
jixZBx6x+k6rZ0zaqQ4PA+jWHzASBgNVHRMBAf8ECDAGAQH/AgEAMCAGA1UdEQQZ
MBeCFWxvYWR1Y2N4LW4xLmNpc2NvLmNvbTANBgkqhkiG9w0BAQsFAAOCAQEAqhe+
B3duk1inR5pmzIWdjKvYYm4CtNeAn9tRYlK2BijKV6a0qDuZwSpN0dGblRr0epRI
thfkZvQGDzo5VZ45mVfxla+wxT3UrfmsoiKmncXBdaYhSsEoKbmWjHbsxwSklRWb
nZatxwglXTluPbF5F9wJSJHTTwPk3P0pjZENF09S5hY/xDEM7wfOrnKUETHJJPts
z4LArPgdaFbmWv8YLCp1YBcOI9mdxQnUUn4in6G9Nv5c9BYDKctPWKHhX8Hr7gO2
RTyBJc9tnhG4LjD0ykokeSp+5u77Xug9ZCtAgiliHZu7cWpGu9lRToiFklgah23+
XbRBYlZpO5v7rd6HbQ==
-----END CERTIFICATE----- |
| Step 4 | Log in to Unified CCX CLI using administrator credentials. |
| Step 5 | Enter the set cert import trust tomcat command to provide the CUCM certificate details. Paste the copied CUCM certificate details and press Return . The CUCM certificate is imported to Unified CCX Tomcat trust store. |