---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-user-guide-ccvp-b-2276373f2d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/user/guide/ccvp_b_1251-user-guide-for-cisco-unified-cvp-vxml-server-and-cisco-unified-call-studio-release-1251/ccvp_b_1251-user-guide-for-cisco-unified-cvp-vxml-server-and-cisco-unified-call-studio-release-1251_appendix_01010.html
retrieved_at: 2026-08-21T03:10:02.468971+00:00
---

User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio Release 12.5(1)

# User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio Release 12.5(1)

Updated: February 3, 2020

Chapter:  Directory
	 Structure

## Chapter:  Directory
	 Structure

- Directory                              	 Structure

# Directory
                     	 Structure

The directory in which
                        		the installation is made (referred to as the INSTALLATION_PATH directory)
                        		contains all the files necessary for the various components of Unified CVP
                        		software. The following table describes what each folder in the
                        		INSTALLATION_PATH is used for. Each folder is described in detail in subsequent
                        		sections.

Folder

Description

VXMLServer

This directory
                                    				contains the files required for VXML Server to run, including all voice
                                    				applications.

CallStudio

This directory
                                    				contains Call Studio and Builder for Call Studio

UninstallerData

The application
                                    				inside this folder is used to uninstall Unified CVP software.

The %CVP_HOME%\VXMLServer folder contains the following
                        		folders:

Folder

Description

admin

This directory
                                    				holds the scripts that perform administrator functions affecting all
                                    				applications on VXML Server.

admin/appScripts

This directory
                                    				holds copies of the application-level administration scripts. If an
                                    				application’s administration scripts require refreshing, the contents of this
                                    				folder can be copied to the applications\[APPNAME]\admin directory.

agent

SNMP agent
                                    				related files.

applications

The voice
                                    				applications built by Builder for Call Studio and hosted by VXML Server are
                                    				stored here. Each application has its own folder bearing the name of the
                                    				application.

applications /
                                    				[APPNAME] / admin

This directory
                                    				holds the scripts that perform administrator functions affecting only the
                                    				application in which the scripts reside.

applications /
                                    				[APPNAME] / data

This directory
                                    				contains the application’s static data files required for VXML Server to load
                                    				the application.

applications /
                                    				[APPNAME] / data / application

This directory
                                    				contains the settings and call flow of the application as well as any
                                    				configurations for application loggers.

applications /
                                    				[APPNAME] / data / configurations

This directory
                                    				holds the static voice, action, and decision element configurations created by
                                    				Builder for Call Studio for this application. Depending on the size of the
                                    				voice application, this directory may end up with many element configuration
                                    				files.

applications /
                                    				[APPNAME] / data / misc

This directory
                                    				holds miscellaneous data files used by Unified CVP decision elements or other
                                    				proprietary files used by the developer.

applications /
                                    				[APPNAME] / java

This directory
                                    				contains all Java related classes or JAR files required for this application
                                    				only. No other application will have access to the Java classes in this
                                    				directory.

applications /
                                    				[APPNAME] / java / application

This directory
                                    				contains all the classes used for this application only. Individual Java
                                    				classes go in the classes directory while complete JAR files go in the lib directory.

applications /
                                    				[APPNAME] / java / util

This directory
                                    				contains utility classes used by the classes in the application directory. Any utility classes that refer
                                    				to Unified CVP API classes must be deployed here or in the application
                                    				directory. Individual Java classes go in the classes directory and JAR files go in the lib directory.

applications /
                                    				[APPNAME] / logs

This directory
                                    				contains the administrator, activity and error logs affiliated with this
                                    				application. Logs are rotated daily so this directory may eventually contain
                                    				many files.

common

This folder
                                    				contains the Java classes and JAR files shared across all voice applications
                                    				hosted on VXML Server. Individual Java classes go in the classes directory and JAR files go in the lib directory.

conf

This directory
                                    				holds settings files used for VXML Server.

docs

This folder
                                    				contains Javadocs and third-party licenses for components used by Unified CVP.
                                    				Download Unified CVP
                                       				  documentation . After downloading, you can place the documentation in the docs folder.

dtds

The DTDs for all
                                    				XML documents used throughout VXML Server are found here. Many are referred to
                                    				in XML documents, though others are provided for reference.

gateways

This folder
                                    				contains all the installed Gateway Adapters for VXML Server. Each subfolder in
                                    				this directory contains a separate Gateway Adapter.

lib

The JAR files
                                    				within this folder are necessary for administration scripts to run. They are
                                    				also used by the developer to compile custom Java code that uses the Unified
                                    				CVP API.

license

The VXML Server
                                    				license files are to be placed here.

logs

Logs affiliated
                                    				with VXML Server are placed here.

management

Files required
                                    				to support the JMX administration interface are found here.

The %CVP_HOME%\CallStudio folder contains the following
                        		directories:

Folder

Description

eclipse

This directory
                                    				holds all the required files for Call Studio and Builder for Call Studio.

eclipse\features

This folder
                                    				contains descriptions of the installed features: Call Studio and Builder for
                                    				Call Studio. Features consist of a set of plug-ins providing certain
                                    				functionality.

eclipse\jre

This folder
                                    				contains the JRE used by Call Studio.

eclipse\plugins

This directory
                                    				contains a set of plug-ins defining the functionality of Call Studio.

eclipse\workspace

The voice
                                    				applications built by Builder for Call Studio are stored here. Each application
                                    				has its own folder bearing the name of the application.

eclipse\workspace\.metadata

A Call Studio
                                    				internal system folder containing configuration and settings files.

eclipse\workspace\ [PROJECT NAME]\callflow

This directory
                                    				contains the configuration files for the given voice application. Those files
                                    				are used by Builder for Call Studio to properly render the call flow.

eclipse\workspace\ [PROJECT NAME]\deploy

This folder
                                    				holds all the resources that will be deployed along with the given application.
                                    				It can contain such components as custom Java classes and libraries as well as
                                    				custom data files.

| Folder | Description |
|---|---|
| VXMLServer | This directory
                                    				contains the files required for VXML Server to run, including all voice
                                    				applications. |
| CallStudio | This directory
                                    				contains Call Studio and Builder for Call Studio |
| UninstallerData | The application
                                    				inside this folder is used to uninstall Unified CVP software. |

| Folder | Description |
|---|---|
| admin | This directory
                                    				holds the scripts that perform administrator functions affecting all
                                    				applications on VXML Server. |
| admin/appScripts | This directory
                                    				holds copies of the application-level administration scripts. If an
                                    				application’s administration scripts require refreshing, the contents of this
                                    				folder can be copied to the applications\[APPNAME]\admin directory. |
| agent | SNMP agent
                                    				related files. |
| applications | The voice
                                    				applications built by Builder for Call Studio and hosted by VXML Server are
                                    				stored here. Each application has its own folder bearing the name of the
                                    				application. |
| applications /
                                    				[APPNAME] / admin | This directory
                                    				holds the scripts that perform administrator functions affecting only the
                                    				application in which the scripts reside. |
| applications /
                                    				[APPNAME] / data | This directory
                                    				contains the application’s static data files required for VXML Server to load
                                    				the application. |
| applications /
                                    				[APPNAME] / data / application | This directory
                                    				contains the settings and call flow of the application as well as any
                                    				configurations for application loggers. |
| applications /
                                    				[APPNAME] / data / configurations | This directory
                                    				holds the static voice, action, and decision element configurations created by
                                    				Builder for Call Studio for this application. Depending on the size of the
                                    				voice application, this directory may end up with many element configuration
                                    				files. |
| applications /
                                    				[APPNAME] / data / misc | This directory
                                    				holds miscellaneous data files used by Unified CVP decision elements or other
                                    				proprietary files used by the developer. |
| applications /
                                    				[APPNAME] / java | This directory
                                    				contains all Java related classes or JAR files required for this application
                                    				only. No other application will have access to the Java classes in this
                                    				directory. |
| applications /
                                    				[APPNAME] / java / application | This directory
                                    				contains all the classes used for this application only. Individual Java
                                    				classes go in the classes directory while complete JAR files go in the lib directory. |
| applications /
                                    				[APPNAME] / java / util | This directory
                                    				contains utility classes used by the classes in the application directory. Any utility classes that refer
                                    				to Unified CVP API classes must be deployed here or in the application
                                    				directory. Individual Java classes go in the classes directory and JAR files go in the lib directory. |
| applications /
                                    				[APPNAME] / logs | This directory
                                    				contains the administrator, activity and error logs affiliated with this
                                    				application. Logs are rotated daily so this directory may eventually contain
                                    				many files. |
| common | This folder
                                    				contains the Java classes and JAR files shared across all voice applications
                                    				hosted on VXML Server. Individual Java classes go in the classes directory and JAR files go in the lib directory. |
| conf | This directory
                                    				holds settings files used for VXML Server. |
| docs | This folder
                                    				contains Javadocs and third-party licenses for components used by Unified CVP.
                                    				Download Unified CVP
                                       				  documentation . After downloading, you can place the documentation in the docs folder. |
| dtds | The DTDs for all
                                    				XML documents used throughout VXML Server are found here. Many are referred to
                                    				in XML documents, though others are provided for reference. |
| gateways | This folder
                                    				contains all the installed Gateway Adapters for VXML Server. Each subfolder in
                                    				this directory contains a separate Gateway Adapter. |
| lib | The JAR files
                                    				within this folder are necessary for administration scripts to run. They are
                                    				also used by the developer to compile custom Java code that uses the Unified
                                    				CVP API. |
| license | The VXML Server
                                    				license files are to be placed here. |
| logs | Logs affiliated
                                    				with VXML Server are placed here. |
| management | Files required
                                    				to support the JMX administration interface are found here. |

| Folder | Description |
|---|---|
| eclipse | This directory
                                    				holds all the required files for Call Studio and Builder for Call Studio. |
| eclipse\features | This folder
                                    				contains descriptions of the installed features: Call Studio and Builder for
                                    				Call Studio. Features consist of a set of plug-ins providing certain
                                    				functionality. |
| eclipse\jre | This folder
                                    				contains the JRE used by Call Studio. |
| eclipse\plugins | This directory
                                    				contains a set of plug-ins defining the functionality of Call Studio. |
| eclipse\workspace | The voice
                                    				applications built by Builder for Call Studio are stored here. Each application
                                    				has its own folder bearing the name of the application. |
| eclipse\workspace\.metadata | A Call Studio
                                    				internal system folder containing configuration and settings files. |
| eclipse\workspace\ [PROJECT NAME]\callflow | This directory
                                    				contains the configuration files for the given voice application. Those files
                                    				are used by Builder for Call Studio to properly render the call flow. |
| eclipse\workspace\ [PROJECT NAME]\deploy | This folder
                                    				holds all the resources that will be deployed along with the given application.
                                    				It can contain such components as custom Java classes and libraries as well as
                                    				custom data files. |