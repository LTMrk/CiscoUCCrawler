---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su3-maintain-and-operate-guid-b776c43568
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su3/maintain_and_operate/guide/uccx_b_1251su3_admin-and-operations-guide/uccx_b_12_5_2admin-and-operations-guide_chapter_01001.html
retrieved_at: 2026-08-16T21:33:33.699486+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1) SU3

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1) SU3

Updated: May 8, 2023

Chapter: Provision of Additional Subsystems

## Chapter: Provision of Additional Subsystems

# Provision of Additional Subsystems

## About Additional
                        	 Subsystems

Your
                              		  Unified CCX system may include some or all of the following additional
                              		  subsystems:

The HTTP
                                    				subsystem—The Unified CCX system uses the HTTP subsystem to enable Unified CCX
                                    				applications to respond to requests from a variety of web clients, including
                                    				computers and IP phones.

The Database
                                    				subsystem—The Unified CCX system uses the Database subsystem to enable Unified
                                    				CCX applications to interact with customer-provided enterprise database servers
                                    				to make database information accessible to contacts.

The eMail
                                    				subsystem—The Unified CCX system uses the eMail subsystem to communicate with
                                    				your email server and enable your applications to create and send email.

If you plan
                              		  to run applications that use any of the additional Unified CCX subsystems
                              		  included in your Unified CCX package, you should now provision those
                              		  subsystems. The Unified CCX system uses these additional subsystems to
                              		  communicate with supporting systems such as 
                              		  web servers, database servers, and email servers.

You need to
                                          			 provision a particular subsystem only if you are using Unified CCX applications
                                          			 that require it.

## Provision of HTTP Subsystem

The HTTP subsystem is available if your system has a license
                                          			 installed for one of the following Cisco product packages: Unified IP IVR or
                                          			 Unified CCX Premium.

The Unified CCX system uses the HTTP subsystem to enable
                              		  Unified CCX applications to respond to requests from a variety of web clients,
                              		  including computers and IP phones.

If you are not using HTTP applications, you do not need to provision
                                          			 the HTTP subsystem.

The Unified CCX system uses subdirectories in the Unified
                              		  CCX installation directory to store text substitution, eXtensible Style
                              		  Language (xsl) templates, static and dynamic web pages, and Java Servlet Pages
                              		  (JSPs).

Use the Document Management page to upload these documents.

To provision the HTTP subsystem, you need to provision HTTP
                              		  triggers. HTTP applications use triggers to activate the application in
                              		  response to an incoming HTTP message.

You cannot change the TCP/IP port numbers used by the HTTP
                                          			 subsystems or triggers in Unified CCX.

### Configure HTTP
                           	 Triggers

You need
                                 		  to create an application using Applications > Application
                                       				Management menu from the Unified CCX Administration
                                 		  menu bar. After you create an application, you can configure HTTP triggers for
                                 		  the application using the following procedure.

Step 1

From the Unified
                                          			 CCXAdministration menu bar, choose Subsystems > HTTP .

The HTTP Trigger
                                             				Configuration web page opens.

Step 2

Specify the
                                          			 following fields:

Field

Description

URL

The
                                                         							 relative URL.

For
                                                         							 example:

Application Name

Select
                                                         							 an application for which you want to add a HTTP trigger from this list box.

Sessions

The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle.

Enabled

Click
                                                         							 the required radio button to accept - Yes (the default).

If
                                                                     								you disable the trigger, the user receives an error message when browsing to
                                                                     								the defined trigger URL.

Step 3

Click Add
                                             				New .

The HTTP Trigger
                                             				Configuration web page closes, and the trigger information appears on the HTTP
                                             				Trigger Configuration summary web page.

You are now
                                             				ready to provision any additional subsystems your Unified CCX applications
                                             				require or to begin configuring Unified CCX applications.

## Provision of Database Subsystem

The Database subsystem is available if your system has a license
                                       		  installed for either the Unified IP IVR or Unified CCX Premium product
                                       		  packages. If you are not using Unified CCX applications that require access to
                                       		  databases, you do not need to provision the Database subsystem.

The Unified CCX system uses the Database subsystem to enable
                           		Unified CCX applications to interact with database servers to make database
                           		information accessible to contacts.

Caution

The Database subsystem does not support database views or running the store procedures.

### Database Subsystem
                           	 Configuration

The Database
                              		subsystem enables the Unified CCX applications to obtain information from data
                              		sources, which are databases configured to communicate with the Unified CCX
                              		system. You can connect the Unified CCX system with enterprise databases such
                              		as Microsoft SQL Server, Sybase, Oracle, or IBM DB2.

You can
                              		upload JDBC driver files using Subsystems > Database > Drivers menu option.

To determine a list of enterprise databases supported for the Database subsystem, see the Unified CCX Compatibility related
                                          information, located at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .

### Add New
                           	 Datasource

After
                                 		  uploading the JDBC driver, you need to use this to create the datasource in the
                                 		  Database subsystem.

To add a
                                 		  new data source, complete the following steps.

Step 1

From the Unified
                                          			 CCXAdministration menu bar, choose Subsystems > Database > DataSource . Click Add
                                             				New icon that displays in the tool bar in the upper, left corner of
                                          			 the window or the Add
                                             				New button that displays at the bottom of the page.

The Datasource Configuration web page opens. For more information
                                             				on the web page fields, see Datasource Configuration Web Page .

Step 2

Click Add to save the changes.

The Enterprise
                                             				Database Subsystem Configuration web page opens. You are now ready to provision
                                             				any additional subsystems your Unified CCX applications require or to begin
                                             				configuring Unified CCX applications.

#### Datasource Configuration Web Page

Datasource Configuration web page.

Field

Description

Secure Connection

When enabled, encrypts the connections to enterprise database servers. By default, it is disabled.

Data Source Name

Data source name for referring to the datasource. This is a
                                                						mandatory field.

User Name

Username defined for connecting to the enterprise database.
                                                						This is a mandatory field.

Password

Password defined for connecting to the enterprise database.

Confirm Password

Re-enter the password that you provided in the Password
                                                						field.

Maximum Number of Connections

Maximum number of connections allowed to connect to the
                                                						database.

This database is usually an external database to which the
                                                						customer script can connect. While the limit is set by that database and
                                                						governed by your license, if this number in this setting is exceeded, the
                                                						corresponding workflow is aborted and the caller receives an error message.
                                                						However, you can avoid this error by configuring the appropriate number of
                                                						sessions in the corresponding script or application. Also, the script writer
                                                						can provide information about how many connections are used per call (or
                                                						instance of application). This is a mandatory field.

Driver

Displays the list of available drivers for the enterprise
                                                						database. One or more datasources can use the same driver. Select a driver for
                                                						this datasource from this list box. This is a mandatory field.

JDBC URL

JDBC URL that is used to obtain a connection to the enterprise database. This is a mandatory field. The JDBC URL provided
                                                will be used by Unified CCX to connect to the enterprise database using JDBC. The URL to be used is dependent on the database
                                                you are connecting. The examples provided in the Datasource Configuration web page can be used as a reference to define the
                                                URL. Refer to the driver documentation for more information.

If the test connection fails for Oracle JDBC drive connection, try the following connection url: jdbc:oracle:thin:[user/password]@[host][:port]:SID

Encrypted connections to enterprise database servers are supported. This is applicable from Unified CCX release 12.5(1) SU3
                                                                  ES03.

If you enable Secure Connection , ensure that the communication ports on the external database server are configured to be secure. Otherwise, the communication
                                                                  is not restricted.

If you enable FIPS, then the password length must be minimum 14 characters for Oracle users connecting to external datasource
                                                configuration.

### Poll Database Connectivity

To poll connectivity to the database on a periodic basis,
                                 		  complete the following steps.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > Database > Parameters .

The Parameters web page opens to display the parameter-related
                                             				fields.

Step 2

Specify the following fields:

Field

Description

RetryConnectInterval

Specifies the interval between two connection attempts
                                                         							 when a data source is initialized. The default is 15,000 milliseconds.

NumAttempt

Specifies the number of attempts to establish
                                                         							 connections to the database when a data source is initialized. The default is 3
                                                         							 attempts.

LoginTimeout

Sets the maximum time in seconds that a driver will wait
                                                         							 while attempting to connect to a database. The default is 0 (disabled).

Step 3

Click Update to apply changes (or Reset to Default if you prefer to retain the
                                          			 default values).

The window refreshes and Unified CCX updates the parameters with
                                             				your changes. You are now ready to provision any additional subsystems your
                                             				Unified CCX applications require or to begin configuring Unified CCX
                                             				applications.

## Provision eMail Subsystem

The eMail subsystem is available if your system has a license
                                          			 installed for one of the following Cisco product packages: Unified IP IVR or
                                          			 Unified CCX Premium.

The Unified CCX system uses the eMail subsystem to
                              		  communicate with your email server and enable your applications to create and
                              		  send email. You must provision the eMail subsystem if you intend to create
                              		  scripts that use messaging steps to create and send email.

Tip

If your email system is configured to receive acknowledgments, you
                                          			 should process the mailbox you identify in your configuration to determine
                                          			 whether or not an email was successfully sent.

The email configuration process identifies the default email
                              		  address and server to be used for sending email (including e-pages and faxes)
                              		  and for receiving acknowledgments.

If you are not using email applications, you do not need to
                                          			 provision the eMail subsystem.

Complete the following steps.

Step 1

Choose Subsystems > eMail .

The eMail Configuration web page opens.

Step 2

Specify the following fields:

Field

Description

Mail Server

A fully-qualified email server name. (Example:
                                                      							 server.domain.com)

email Address

An existing fully qualified e-mail address for the
                                                      							 administrative account. Example:administrator@domain.com

Step 3

Click Update .

The Unified CCX system saves your changes and the Unified
                                          				CCXAdministration web page opens.

Cisco does not currently support multiple email configurations.
                                                      				  To remove the email information, you must erase the fields and click Update .

You are now ready to provision any additional subsystems your
                                          				Unified CCX applications require, or to begin configuring Unified CCX
                                          				applications.

| Note | You need to
                                          			 provision a particular subsystem only if you are using Unified CCX applications
                                          			 that require it. |
|---|---|

| Note | The HTTP subsystem is available if your system has a license
                                          			 installed for one of the following Cisco product packages: Unified IP IVR or
                                          			 Unified CCX Premium. |
|---|---|

| Note | If you are not using HTTP applications, you do not need to provision
                                          			 the HTTP subsystem. |
|---|---|

| Note | Use the Document Management page to upload these documents. |
|---|---|

| Note | You cannot change the TCP/IP port numbers used by the HTTP
                                          			 subsystems or triggers in Unified CCX. |
|---|---|

| Step 1 | From the Unified
                                          			 CCXAdministration menu bar, choose Subsystems > HTTP . The HTTP Trigger
                                             				Configuration web page opens. |
|---|---|
| Step 2 | Specify the
                                          			 following fields: Field Description URL The
                                                         							 relative URL. For
                                                         							 example: /hello Application Name Select
                                                         							 an application for which you want to add a HTTP trigger from this list box. Sessions The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle. Enabled Click
                                                         							 the required radio button to accept - Yes (the default). Note If
                                                                     								you disable the trigger, the user receives an error message when browsing to
                                                                     								the defined trigger URL. | Field | Description | URL | The
                                                         							 relative URL. For
                                                         							 example: /hello | Application Name | Select
                                                         							 an application for which you want to add a HTTP trigger from this list box. | Sessions | The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle. | Enabled | Click
                                                         							 the required radio button to accept - Yes (the default). Note If
                                                                     								you disable the trigger, the user receives an error message when browsing to
                                                                     								the defined trigger URL. | Note | If
                                                                     								you disable the trigger, the user receives an error message when browsing to
                                                                     								the defined trigger URL. |
| Field | Description |
| URL | The
                                                         							 relative URL. For
                                                         							 example: /hello |
| Application Name | Select
                                                         							 an application for which you want to add a HTTP trigger from this list box. |
| Sessions | The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle. |
| Enabled | Click
                                                         							 the required radio button to accept - Yes (the default). Note If
                                                                     								you disable the trigger, the user receives an error message when browsing to
                                                                     								the defined trigger URL. | Note | If
                                                                     								you disable the trigger, the user receives an error message when browsing to
                                                                     								the defined trigger URL. |
| Note | If
                                                                     								you disable the trigger, the user receives an error message when browsing to
                                                                     								the defined trigger URL. |
| Step 3 | Click Add
                                             				New . The HTTP Trigger
                                             				Configuration web page closes, and the trigger information appears on the HTTP
                                             				Trigger Configuration summary web page. You are now
                                             				ready to provision any additional subsystems your Unified CCX applications
                                             				require or to begin configuring Unified CCX applications. |

| Field | Description |
|---|---|
| URL | The
                                                         							 relative URL. For
                                                         							 example: /hello |
| Application Name | Select
                                                         							 an application for which you want to add a HTTP trigger from this list box. |
| Sessions | The
                                                         							 maximum amount of simultaneous sessions (instances) that the application can
                                                         							 handle. |
| Enabled | Click
                                                         							 the required radio button to accept - Yes (the default). Note If
                                                                     								you disable the trigger, the user receives an error message when browsing to
                                                                     								the defined trigger URL. | Note | If
                                                                     								you disable the trigger, the user receives an error message when browsing to
                                                                     								the defined trigger URL. |
| Note | If
                                                                     								you disable the trigger, the user receives an error message when browsing to
                                                                     								the defined trigger URL. |

| Note | If
                                                                     								you disable the trigger, the user receives an error message when browsing to
                                                                     								the defined trigger URL. |
|---|---|

| Note | The Database subsystem is available if your system has a license
                                       		  installed for either the Unified IP IVR or Unified CCX Premium product
                                       		  packages. If you are not using Unified CCX applications that require access to
                                       		  databases, you do not need to provision the Database subsystem. |
|---|---|

| Caution | The Database subsystem does not support database views or running the store procedures. |
|---|---|

| Note | To determine a list of enterprise databases supported for the Database subsystem, see the Unified CCX Compatibility related
                                          information, located at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html . |
|---|---|

| Step 1 | From the Unified
                                          			 CCXAdministration menu bar, choose Subsystems > Database > DataSource . Click Add
                                             				New icon that displays in the tool bar in the upper, left corner of
                                          			 the window or the Add
                                             				New button that displays at the bottom of the page. The Datasource Configuration web page opens. For more information
                                             				on the web page fields, see Datasource Configuration Web Page . |
|---|---|
| Step 2 | Click Add to save the changes. The Enterprise
                                             				Database Subsystem Configuration web page opens. You are now ready to provision
                                             				any additional subsystems your Unified CCX applications require or to begin
                                             				configuring Unified CCX applications. |

| Field | Description |
|---|---|
| Secure Connection | When enabled, encrypts the connections to enterprise database servers. By default, it is disabled. |
| Data Source Name | Data source name for referring to the datasource. This is a
                                                						mandatory field. |
| User Name | Username defined for connecting to the enterprise database.
                                                						This is a mandatory field. |
| Password | Password defined for connecting to the enterprise database. |
| Confirm Password | Re-enter the password that you provided in the Password
                                                						field. |
| Maximum Number of Connections | Maximum number of connections allowed to connect to the
                                                						database. This database is usually an external database to which the
                                                						customer script can connect. While the limit is set by that database and
                                                						governed by your license, if this number in this setting is exceeded, the
                                                						corresponding workflow is aborted and the caller receives an error message.
                                                						However, you can avoid this error by configuring the appropriate number of
                                                						sessions in the corresponding script or application. Also, the script writer
                                                						can provide information about how many connections are used per call (or
                                                						instance of application). This is a mandatory field. |
| Driver | Displays the list of available drivers for the enterprise
                                                						database. One or more datasources can use the same driver. Select a driver for
                                                						this datasource from this list box. This is a mandatory field. |
| JDBC URL | JDBC URL that is used to obtain a connection to the enterprise database. This is a mandatory field. The JDBC URL provided
                                                will be used by Unified CCX to connect to the enterprise database using JDBC. The URL to be used is dependent on the database
                                                you are connecting. The examples provided in the Datasource Configuration web page can be used as a reference to define the
                                                URL. Refer to the driver documentation for more information. Note If the test connection fails for Oracle JDBC drive connection, try the following connection url: jdbc:oracle:thin:[user/password]@[host][:port]:SID Encrypted connections to enterprise database servers are supported. This is applicable from Unified CCX release 12.5(1) SU3
                                                                  ES03. If you enable Secure Connection , ensure that the communication ports on the external database server are configured to be secure. Otherwise, the communication
                                                                  is not restricted. | Note | If the test connection fails for Oracle JDBC drive connection, try the following connection url: jdbc:oracle:thin:[user/password]@[host][:port]:SID Encrypted connections to enterprise database servers are supported. This is applicable from Unified CCX release 12.5(1) SU3
                                                                  ES03. If you enable Secure Connection , ensure that the communication ports on the external database server are configured to be secure. Otherwise, the communication
                                                                  is not restricted. |
| Note | If the test connection fails for Oracle JDBC drive connection, try the following connection url: jdbc:oracle:thin:[user/password]@[host][:port]:SID Encrypted connections to enterprise database servers are supported. This is applicable from Unified CCX release 12.5(1) SU3
                                                                  ES03. If you enable Secure Connection , ensure that the communication ports on the external database server are configured to be secure. Otherwise, the communication
                                                                  is not restricted. |

| Note | If the test connection fails for Oracle JDBC drive connection, try the following connection url: jdbc:oracle:thin:[user/password]@[host][:port]:SID Encrypted connections to enterprise database servers are supported. This is applicable from Unified CCX release 12.5(1) SU3
                                                                  ES03. If you enable Secure Connection , ensure that the communication ports on the external database server are configured to be secure. Otherwise, the communication
                                                                  is not restricted. |
|---|---|

| Note | If you enable FIPS, then the password length must be minimum 14 characters for Oracle users connecting to external datasource
                                                configuration. |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > Database > Parameters . The Parameters web page opens to display the parameter-related
                                             				fields. |
|---|---|
| Step 2 | Specify the following fields: Field Description RetryConnectInterval Specifies the interval between two connection attempts
                                                         							 when a data source is initialized. The default is 15,000 milliseconds. NumAttempt Specifies the number of attempts to establish
                                                         							 connections to the database when a data source is initialized. The default is 3
                                                         							 attempts. LoginTimeout Sets the maximum time in seconds that a driver will wait
                                                         							 while attempting to connect to a database. The default is 0 (disabled). | Field | Description | RetryConnectInterval | Specifies the interval between two connection attempts
                                                         							 when a data source is initialized. The default is 15,000 milliseconds. | NumAttempt | Specifies the number of attempts to establish
                                                         							 connections to the database when a data source is initialized. The default is 3
                                                         							 attempts. | LoginTimeout | Sets the maximum time in seconds that a driver will wait
                                                         							 while attempting to connect to a database. The default is 0 (disabled). |
| Field | Description |
| RetryConnectInterval | Specifies the interval between two connection attempts
                                                         							 when a data source is initialized. The default is 15,000 milliseconds. |
| NumAttempt | Specifies the number of attempts to establish
                                                         							 connections to the database when a data source is initialized. The default is 3
                                                         							 attempts. |
| LoginTimeout | Sets the maximum time in seconds that a driver will wait
                                                         							 while attempting to connect to a database. The default is 0 (disabled). |
| Step 3 | Click Update to apply changes (or Reset to Default if you prefer to retain the
                                          			 default values). The window refreshes and Unified CCX updates the parameters with
                                             				your changes. You are now ready to provision any additional subsystems your
                                             				Unified CCX applications require or to begin configuring Unified CCX
                                             				applications. |

| Field | Description |
|---|---|
| RetryConnectInterval | Specifies the interval between two connection attempts
                                                         							 when a data source is initialized. The default is 15,000 milliseconds. |
| NumAttempt | Specifies the number of attempts to establish
                                                         							 connections to the database when a data source is initialized. The default is 3
                                                         							 attempts. |
| LoginTimeout | Sets the maximum time in seconds that a driver will wait
                                                         							 while attempting to connect to a database. The default is 0 (disabled). |

| Note | The eMail subsystem is available if your system has a license
                                          			 installed for one of the following Cisco product packages: Unified IP IVR or
                                          			 Unified CCX Premium. |
|---|---|

| Tip | If your email system is configured to receive acknowledgments, you
                                          			 should process the mailbox you identify in your configuration to determine
                                          			 whether or not an email was successfully sent. |
|---|---|

| Note | If you are not using email applications, you do not need to
                                          			 provision the eMail subsystem. |
|---|---|

| Step 1 | Choose Subsystems > eMail . The eMail Configuration web page opens. |
|---|---|
| Step 2 | Specify the following fields: Field Description Mail Server A fully-qualified email server name. (Example:
                                                      							 server.domain.com) email Address An existing fully qualified e-mail address for the
                                                      							 administrative account. Example:administrator@domain.com Note Unified CCX supports alphanumeric IDs and special characters (only hyphen "-" , underscore "_", and dot "."). | Field | Description | Mail Server | A fully-qualified email server name. (Example:
                                                      							 server.domain.com) | email Address | An existing fully qualified e-mail address for the
                                                      							 administrative account. Example:administrator@domain.com Note Unified CCX supports alphanumeric IDs and special characters (only hyphen "-" , underscore "_", and dot "."). | Note | Unified CCX supports alphanumeric IDs and special characters (only hyphen "-" , underscore "_", and dot "."). |
| Field | Description |
| Mail Server | A fully-qualified email server name. (Example:
                                                      							 server.domain.com) |
| email Address | An existing fully qualified e-mail address for the
                                                      							 administrative account. Example:administrator@domain.com Note Unified CCX supports alphanumeric IDs and special characters (only hyphen "-" , underscore "_", and dot "."). | Note | Unified CCX supports alphanumeric IDs and special characters (only hyphen "-" , underscore "_", and dot "."). |
| Note | Unified CCX supports alphanumeric IDs and special characters (only hyphen "-" , underscore "_", and dot "."). |
| Step 3 | Click Update . The Unified CCX system saves your changes and the Unified
                                          				CCXAdministration web page opens. Note Cisco does not currently support multiple email configurations.
                                                      				  To remove the email information, you must erase the fields and click Update . You are now ready to provision any additional subsystems your
                                          				Unified CCX applications require, or to begin configuring Unified CCX
                                          				applications. | Note | Cisco does not currently support multiple email configurations.
                                                      				  To remove the email information, you must erase the fields and click Update . |
| Note | Cisco does not currently support multiple email configurations.
                                                      				  To remove the email information, you must erase the fields and click Update . |

| Field | Description |
|---|---|
| Mail Server | A fully-qualified email server name. (Example:
                                                      							 server.domain.com) |
| email Address | An existing fully qualified e-mail address for the
                                                      							 administrative account. Example:administrator@domain.com Note Unified CCX supports alphanumeric IDs and special characters (only hyphen "-" , underscore "_", and dot "."). | Note | Unified CCX supports alphanumeric IDs and special characters (only hyphen "-" , underscore "_", and dot "."). |
| Note | Unified CCX supports alphanumeric IDs and special characters (only hyphen "-" , underscore "_", and dot "."). |

| Note | Unified CCX supports alphanumeric IDs and special characters (only hyphen "-" , underscore "_", and dot "."). |
|---|---|

| Note | Cisco does not currently support multiple email configurations.
                                                      				  To remove the email information, you must erase the fields and click Update . |
|---|---|