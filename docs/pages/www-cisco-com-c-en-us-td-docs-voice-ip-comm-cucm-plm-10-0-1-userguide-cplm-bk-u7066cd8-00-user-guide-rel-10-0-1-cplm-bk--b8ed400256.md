---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-10-0-1-userguide-cplm-bk-u7066cd8-00-user-guide-rel-10-0-1-cplm-bk--b8ed400256
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/10_0_1/userguide/CPLM_BK_U7066CD8_00_user-guide-rel-10-0-1/CPLM_BK_U7066CD8_00_user-guide-rel-10-0-1_chapter_0101.html
retrieved_at: 2026-09-08T05:03:57.476729+00:00
---

Cisco Prime License Manager User Guide, Release 10.0(1)

# Cisco Prime License Manager User Guide, Release 10.0(1)

Updated: July 29, 2014

Chapter: Setup

## Chapter: Setup

# Setup

## About
	 Window

About

The
						About dialog box contains the Cisco Prime License
						  Manager version number, license definition version, and Registration
						ID number.

## Dashboard View
	 Settings

Overview section

Product
						Instances

The
						total number of product instances managed by Cisco Prime License
						  Manager . Clicking Product Instances takes you to the Product
						Instances page.

Last
						License Update

The date
						of the last license update. Clicking Last License Update takes you to the
						Licenses > License Fulfillment page.

Last
						Synchronization

The date
						of the last successful synchronization. Clicking Last Synchronization takes you
						to the Product Instances page where you can view the Synchronization Status and
						Last Successful Synchronization for each product instance. You can also perform
						a synchronization from this page by clicking the Synchronize Now button.

Synchronization occurs when Cisco Prime License
								Manager collects up-to-date licensing information for all license
							 types in the system.

License Alerts section

Type

License
						types that are non-compliant

Status

Provides
						information about the alert (for example, insufficient licenses or when a
						license is due to expire)

License Usage section

Type

Specifies the product type

Required

The
						number of licenses allocated to each of those product types

Product Instance Alerts
						  section

Name

Specifies the product name

Status

Provides
						information about the product

Last
						Synchronization

The date
						and time of the last successful synchronization

## Licenses View
	 Settings

The Licenses view
		  contains three pages that allow you to view licensing information and configure
		  product licenses:

## License Usage Page
	 Settings

The License Usage
		  page provides three distinct views of how licenses are being used:

Table View

Chart View

History

In both Table
				and Chart views, you have the option of synchronizing the licenses by clicking
				the Synchronize Now button.

Table View tab

Type

The name
					 of the license types supported within the product scope. For more information,
					 click on a particular license type in the Type column to open a detailed
					 license type page.

Product
					 Type

The
					 product type

Required

The number
					 of licenses required by the product instances in order to deliver the services
					 you have provisioned on those servers.

Installed

The number
					 of licenses currently installed

Available

The
					 difference between the number of Required and Installed licenses. The numbers
					 in this column are color-coded to represent the state of unused licenses for a
					 particular license type.

If the
					 number is red, the number of licenses is considered insufficient. If the number
					 is black, the number of licenses is considered to be in compliance.

Status

The
					 license status (ex: “Temp Licenses Nearing Expiration”, “In Compliance”)

Synchronize Now button

Synchronizes Cisco Prime License
						Manager with the product instances to obtain the most up-to-date
					 licensing information for all license types in the system

Chart View tab

License
					 Type

The
					 License Type drop down menu allows you to select the type of license you wish
					 to view.

Installed/Borrowed

The
					 Installed/Borrowed licenses are categorized as:

Installed

Borrowed from Upper Tier

Not all
						products support tiering

Required/Loaned

The
					 Required/Loaned licenses are categorized as:

Requested

Loaned
						  to Lower Tier

Moving
						your mouse over the bars in the chart reveals the number of licenses
						installed/borrowed or required/loaned

Synchronize Now button

Synchronizes Cisco Prime License
						Manager with the product instances to obtain the most up-to-date
					 licensing information for all license types in the system

History tab

History
					 tab

You can
					 download the usage history for your licenses into a csv file that can be opened
					 in a spreadsheet application. Usage data is collected at every synchronization
					 with product instance and with each action that changes license usage.

Date Range

Allows you
					 to select the start and end date for the period of time you wish to cover.

Product
					 Type

Specifies
					 the type of product instance

Generate
					 File button

Clicking
					 the Generate File button creates a usage history file for the product type
					 selected. A link to the file appears at the bottom of the screen. When you
					 click on the link, you have the option of opening the file or saving it to your
					 computer.

License Usage details
						page

License
					 Description section

The
					 License Description section provides a description of that license type. There
					 is also a link provided to view descriptions of all license types on Cisco.com.

Usage
					 Chart section

The Usage
					 Chart section provides a graphical representation of how many of that
					 particular license type are available, and of those, how many are installed or
					 borrowed from the upper tier.

It also
					 indicates how many of that license type are being used, and of those, how many
					 are requested or loaned to the lower tier.

Usage by
					 Instance section

The Usage
					 by Instance section lists the systems that are using that particular license
					 type, and identifies the product type of the system, release version, and the
					 number of licenses required for each of those systems.

Installed
					 Licenses by Type section

The
					 Installed Licenses by Type section distinguishes between Permanent and
					 Temporary licenses, the number of licenses that each is limited to, and the
					 expiry date for the temporary licenses.

## License Planning
	 Page Settings

License Planning
						  page

Name

Specifies the name of the license plan

Selecting a license plan name from the list in the History table
						opens the Details window for that license plan. This window contains the
						following information:

Name (editable)

Description (editable)

Type

Created Date

Summary (includes a View Summary link that provides summary
							 information for that license plan)

Description

Provides a brief description of the license plan

Type

Specifies the license plan type: Migration or Add

Creation Date

Specifies the license plan creation date

Action

The
						Action column provides a Delete button to delete a license plan

Create
						an Add Licenses Plan button

Clicking the Create an Add Licenses Plan button opens the Create
						an Add Licenses Plan wizard. For instructions on how to complete the Create an
						Add Licenses Plan wizard, see the Cisco Prime License
						  Manager User Guide.

Create an Add Licenses
						  Plan page

Choose
						Product section

From
						the Choose Product section of the Create an Add Licenses Plan window, you can
						select (from the drop-down menus) the Product Type and the License Version to
						which you want to add licenses.

Specify License Counts section

From
						the Specify License Counts section of the Create an Add Licenses Plan window,
						you can adjust the number of licenses to be allocated to each type of license
						and save your changes for that license type.

You
						may also choose to run a compliance check by clicking the Run Compliance Check
						button, or reset the license values by clicking the Reset Values button.

Summary and Next Steps

From
						the Summary and Next Steps section of the Create an Add Licenses Plan window,
						you can view and save a summary of the changes you made in the Choose Product
						and Specify License Counts sections.

The
						Save Summary in Cisco Prime License Manager option is selected by default. A
						default name for the summary also appears in the Name field using the format
						<product-type>-add-<date-time-stamp> format.

## License
	 Fulfillment Page Settings

e-Migration is disabled if e-Fulfillment is disabled.

Fulfill Licenses from File

Generate License Request

- Migrate Licenses

Retrieve Fulfilled Licenses

The
				  Fulfill Licenses from File option opens the Install License File dialog box.

The
				  Generate License Request option opens the License Request and Next Steps dialog
				  box.

The Migrate License
				  option opens the Migrate Licenses to Cisco Prime License Manager page.

Generate License Request

- Migrate Licenses

The
				  Generate License Request opens the License Request and Next Steps dialog box

Setting

Description

Choose New
				  License Version

From the
				  Choose New License Version section of the Migrate Licenses to Cisco Prime
				  License Manager window, you can select the Product Type and New License Version
				  from the drop-down menus.

Choose
				  Product Instances

From the
				  Choose Product Instances section of the Migrate Licenses to Cisco Prime License
				  Manager window, you can upgrade a product instance by selecting it in the
				  Available Product Instances window and click the arrow to move it to the
				  Product Instances to Upgrade window.

License
				  Counts (Unified CM)

From the
				  License Counts section of the Migrate Licenses to Cisco Prime License Manager
				  window, you can view a summary of pre-upgrade product instance data. This table
				  cannot be edited.

If you
				  selected Unified
					 CM as your product type, the following options appear:

Public
						Space Phones - An estimate of the number of public space phones. Public space
						phones do not have users assigned and are typically placed in shared
						workspaces, lobbies and meeting rooms. These phones generally require lower
						level licenses, so providing an estimate of the number of these phones in your
						deployment will help Cisco more accurately determine your license requirements.

Case
						Numbers (Optional) - A case number assigned if the report was sent to Cisco
						Licensing Support

License Usage Reports - Allows you to upload a License Usage
						Reports from a local drive.

MAC
						addresses - The MAC addresses from the original servers that were upgraded.
						These MAC addresses can be used to look up the licenses that were registered on
						those product instances.

License
				  Counts (Unity Connection)

The
				  content of the License Counts section of the Migrate Licenses to Enterprise
				  License Manager window depends entirely upon the options you have selected in
				  previous sections.

If you
				  selected Unity
					 Connection , the following options appear:

I have
						CUWL licenses to be migrated

I do
						not have CUWL licenses to be migrated

License
				  Counts (standard product)

From the
				  License Counts section of the Migrate Licenses to Cisco Prime License Manager
				  window, you can view a table of the licenses available to migrate. This table
				  is editable. From the table, you can reduce (but not increase) license counts
				  in the Licenses to Migrate column. You can also run a compliance check by
				  clicking the Run
					 Compliance Check button, or reset the license values by clicking the Reset
					 Values button.

Summary
				  and Next Steps (Unified CM or Unity Connection > I have CUWL licenses to be
				  migrated)

The
				  content of the Summary and Next Steps section of the Migrate Licenses to
				  Enterprise License Manager window depends entirely upon the options you have
				  selected in previous sections.

If you
				  selected Unified
					 CM as your product type, or Unity
					 Connection > I have CUWL licenses to be migrated , the following options
				  appear:

In this
				  section you must indicate how the upgrade was ordered:

Upgraded using one or more service contracts

Purchased the upgrade

If you
				  select Upgraded using one or more service contracts, enter the UCSS/ESW
				  Contract Numbers.

If you
				  select Purchased the upgrade, enter the Sales Order Numbers.

The Cisco.com (CCO) User ID field.

Company
				  Name and the field used to capture additional information are optional.
				  However; if you enter the company name, it is used in the subject line of the
				  email and is included in the name of the zip file.

A default
				  name for the summary also appears in the Name field using the format
				  <productname>-migrate-<date-time-stamp> format. Instructions for
				  placing your order and fulfilling your licenses also appear in this section.
				  Click Finish & Generate Request.

The
				  License Migration Request and Next Steps window appears. Download the License
				  Migration Request zip file to your PC.

Email the
				  License Migration Request to Cisco licensing support using the link provided.

Click
				  Close to return to the License Fulfillment page.

Summary
				  and Next Steps (Unity Connection > I do not have CUWL licenses to be
				  migrated) when e-Fulfillment/e-Migration is enabled

If
				  e-Fulfillment is enabled, and you selected Unity
					 Connection > I do not have CUWL license to be migrated , the following
				  options appear: In this section, you can optionally enter a description of the
				  e-Migration transaction.

Read the
				  End User License Agreement and select the checkbox to acknowledge the
				  agreement.

Summary
				  and Next Steps (Unity Connection > I do not have CUWL licenses to be
				  migrated) when e-Fulfillment/e-Migration is disabled

The
				  content of the Summary and Next Steps section of the Migrate Licenses to
				  Enterprise License Manager window depends entirely upon the options you have
				  selected in previous sections.

If you
				  selected Unity
					 Connection > I do not have CUWL licenses to be migrated , the following
				  options appear:

In this
				  section, you can view and save a summary of the changes you made. To view the
				  summary, click View Summary. A default name for the summary also appears in the
				  Name field using the format <productname>-migrate-<date-time-stamp>
				  format. Instructions for placing your order and fulfilling your licenses also
				  appear in this section. Click Finish & Generate Request.

The
				  License Migration Request and Next Steps window appears. Copy the selected text
				  to your clipboard or click Save it to a file on your computer.

Select
				  License Migration Portal under Step 2 and paste the copied text in the
				  designated field or select the saved file from your computer.

Click
				  Close to return to the Add or Upgrade Licenses page.

License
				  Migration Request and Next Steps when e-Fulfillment/e-Migration is enabled

License
				  Migration Request and Next Steps when e-Fulfillment/e-Migration is disabled

Clicking
				  the Finish & Generate Request button in the Summary and Next Steps section
				  of the Migrate Licenses to Cisco Prime License Manager window opens the License
				  Migration Request and Next Steps.

You have
				  the option of copying the selected text or clicking the Save it to a file on
				  your computer link.

Specify
				  PAK

A new PAK

An already-installed PAK that supports partial fulfillment

Only PAKs
				  that support partial fulfillment are displayed in the drop-down menu.

Fulfill
				  Licenses

From the
				  Fulfill Licenses section you can choose the licenses in the PAK that you want
				  to fulfill.

The
				  Fulfill option, under the Actions column, allows you to fulfill a particular
				  license. Clicking the Fulfill option opens the Fulfill Licenses window. From
				  that window, you can adjust the number of licenses you wish to fulfill for a
				  particular license type.

You can
				  also perform a compliance check of your licenses by clicking the Run Compliance
				  Check button.

To reset
				  the values you have entered, click the Reset Values button.

Review
				  Contents

From the
				  Review Contents section of the Fulfill Licenses from PAK wizard, you can review
				  the contents of the PAK. If the PAK supports partial fulfillment, you can
				  adjust the license installation counts.

Transaction Options and License Agreement

From the
				  License Options section of the Fulfill Licenses from PAK wizard, you can add a
				  description to the transaction or associate it with a previously generated add
				  or upgrade plan.

Browse
				  button

Allows you
				  to select a license file from your computer.

Options

The
				  Options section of the Install License File dialog box allows you to add a
				  description and associate your transaction with a saved add/migration license
				  summary. This step is optional.

Install
				  button

When the
				  license file has been selected (using the Browse button), it appears in the
				  License File field. The Install button is then used to install that license
				  file.

Copy the
				  selected text

The first
				  step in the License Request and Next Steps dialog box provides the following
				  options: copy the text in the text box to your clipboard or click the link to
				  save the license request file to your computer.

Register
				  your Licenses

The second
				  step instructs you to register your licenses by clicking the link provided.

Install your
				  Licenses

The third
				  step advises you to return to Cisco Prime License Manager and install your licenses
				  once you have received them. License files are generally obtained via email or
				  downloaded from the Cisco portal.

Clicking
				  the Install button returns you to the Licenses page.

specifies the name of a license contained in the file

specifies the license type (ex: Permanent, Time-limited)

specifies the expiry date of time-limited licenses

specifies the total number of that license type in the PAK

- Purchased

- Fulfilled

- Remaining

- Fulfill

- Remaining

- Actions

Transaction Details

Fulfillment Date

Description

Associated Summary

Method
						(File Install, e-Fulfillment, or Retrieve Fulfilled Licenses)

Cisco.com Username

PAK

PAK
						Partial Fulfillment

License
				  Details

Type

Product Type

Total
						on System (the number of that particular license type)

Expiration date

Fulfillment Date

Description

Associated Summary

Method
						(File Install, e-Fulfillment, or Retrieve Fulfilled Licenses)

Cisco.com Username

PAK

PAK
						Partial Fulfillment

The
				  Description and Associated Summary fields can be edited.

## Product Instances
	 View Settings

The Product
		  Instances page allows you to view product license information. From this page,
		  you can add, delete, or synchronize product instances.

Product Instances

Name

Specifies the name of the product instance

Hostname/IP Address

Specifies the hostname or IP address of the product instance

Product
						Type

Specifies the type of product instance

Version

Specifies the product release of the product instance

Status

Specifies the status of the product instance synchronization
						(for example, “Success”, “Registration Conflict”, “Invalid Server Type”,
						“Insufficient Licenses”)

Last
						Successful Synchronization

Specifies the date and time of the last successful
						synchronization.

Add
						button

Clicking
						the Add button on the Product Instances page opens the Product Add dialog box.
						From this dialog box, you can enter the following information:

Name

Description (optional)

Product Type

Hostname/IP Address

Username

Password

Test
						Connection button

From the
						Product Add dialog box, you can click the Test Connection button to test the
						connection to the product instance prior to adding it.

If the
						connection cannot be established, either through the connection test or by
						clicking OK to add a product instance, you may receive one of the following
						error messages:

Instance Unreachable

Login Failed

Certificate Mismatch

Registration Conflict

Invalid Server Type

Product Type Mismatch

Duplicate Product Instance

Delete
						button

You can
						delete a product instance by clicking the Delete link under the Action column
						for the product instance.

Launch
						Admin GUI button

You can
						open the administration GUI for a particular product instance by selecting the
						check box next to the product instance and clicking Launch Admin GUI.

Synchronize Now button

Synchronizes Cisco Prime License
						  Manager with the product instances to obtain the most up-to-date
						licensing information for all license types in the system

Product Instance details
						  page

General
						tab

The
						General tab is divided into two sections:

Product

Administrator Account

The
						Product section contains the following information:

Name

Description

Hostname/IP Address

Product Type

Product Version

The
						Administrator Account section contains the following fields:

Username

Password

Clicking
						the Save button saves your changes.

License
						Usage tab

The
						License Usage tab contains a graphical representation of the license requests
						and a table illustrating the number of licenses requested by license type.

## Administration
	 View Settings

In a standalone
		  deployment, the Administration view allows you to configure the following Cisco Prime License Manager settings:

Administrator
				Accounts

Backup/Restore

Install/Upgrade

License
				Definitions

Diagnostic
				Logs

Restart

A coresident deployment has similar settings but backup/restore and
		  install/upgrade options must be configured using Cisco Unified Communications
		  Manager:

Administrator Accounts

OS Administration

Disaster Recovery

License Definitions

Diagnostic Logs

Restart

For information about OS Administration or Disaster Recovery, see
			 the Cisco Unified Communications Operating System Administration
				Guide or Disaster Recovery System Administration Guide for Cisco Unified
				Communications Manager .

Administrator Accounts

Add
						Administrator button

Selecting the Add Administrator button in the Administrator
						Accounts window opens the Add Administrator Account window.

From
						this window, you can add an administrator account. You are prompted for the
						following information:

Name/Description

Username

Password

Re-enter Password

Change
						Password

Selecting the Change Password link in the Administrators table
						opens the Change Password page. From this page you can change the password of
						an existing administrator account. You are prompted for the following
						information:

New
							 Password

Re-enter New Password

Backup/Restore

Backup
						Server

The
						Backup Server section contains the following fields:

IP
							 Address/Hostname

Username

Password

Directory

The IP
						Address/Hostname specifies the IP Address/Hostname of the server to be backed
						up or restored. Enter your username and passport to connect to the server. The
						Directory field specifies the location of the backed up server (for example:
						/ws/user1-rcd/backup2)

The
						Backup/Restore page also indicates when the last backup was performed.

Run
						Backup button

The Run
						Backup button initiates a backup of the server specified in the IP
						Address/Hostname field.

Run
						Restore button

The Run
						Restore button initiates a restore of the server specified in the Directory
						field.

Test
						Connection

The Test
						Connection button allows you test the connection to the product instance prior
						to performing a backup or restore.

Install/Upgrade

Install/Upgrade page

Use
						this page to upgrade your Cisco Prime License
						  Manager software or to add options such as language packs to your
						system.

System
						Software

Lists
						the active and inactive system software versions

Install/Upgrade Software wizard

Clicking on the Install/Upgrade Software button opens the
						Install/Upgrade Software wizard. This is a two-step wizard:

Specify File Location

Select File

The
						Specify File Location page provides two options:

Install/Upgrade from Network

Install/Upgrade from DVD/CD drive on Cisco Prime License
								Manager server

The
						Install/Upgrade from Network option requires the following information:

IP
							 Address/Hostname

Username

Password

Directory

Transfer Protocol

The IP
						Address/Hostname field specifies the location of the file to be installed or
						used for the upgrade . Enter your username and password to connect to the
						server. The Directory field specifies the location where the install or upgrade
						will be saved.

The
						Transfer Protocol specifies the method: SFTP or FTP

All
						valid upgrades are listed in the table. Select the appropriate (valid) upgrade
						file from the list and click the Start Installation/Upgrade button to begin the
						upgrade.

License Definitions

License Definitions

The
						License Definitions page contains information about the license types managed
						by Cisco Prime License
						  Manager . The License Definition file should be updated prior to
						upgrading any of your product instances to a new version or before adding a
						product instance of a new type.

Check
						for Latest Version

Clicking Check for Latest Version opens the Cisco Prime License
						  Manager Dashboard, which provides an overview of the license types
						currently in use.

View
						Release Notes

Clicking View Release Notes opens the License Definitions
						Release Notes page, which lists:

Changes Since Previous Version

Supported Products

Install New License Definition File button

Clicking the Install New License Definition File button opens
						the Install License Definitions window. Click the Browse button to locate the
						License Definitions File and then click Fulfill to install the file.

Diagnostic Logs

Log
						Settings tab

The Log
						Settings tab lists the diagnostics categories and log levels. The diagnostic
						categories include:

Cisco Prime License Manager core services

Communication with product instances

The
						Log Level drop-down list for each diagnostic category can be set to one of the
						following:

Error

Warning

Info

Debug

Once the
						log level has been set for each diagnostic category, you can save your changes
						by clicking the Save button. You may also opt to reset your log settings by
						clicking the Reset button.

Download
						Logs tab

The
						Download Logs tab allows you to generate a log file, using the date and time
						range of your choice to include in the log file. The default range is from 12
						AM of the current day until the current time. You can then generate the file by
						clicking the Generate Log File button. The log file is generated and downloaded
						to your computer.

Restart

Restart

Pressing the Restart button below restarts all Cisco Prime License
						  Manager services. This generally takes less than a minute and you
						will automatically be taken to the login screen when the restart is complete.

| Setting | Description |
|---|---|
| About | The
						About dialog box contains the Cisco Prime License
						  Manager version number, license definition version, and Registration
						ID number. Note This information can be used for re-hosting. Re-hosting is the
						  process that customers must follow to move licenses from one instance of Cisco Prime License
							 Manager to another. Licenses that have already been issued and
						  fulfilled in one instance of Cisco Prime License
							 Manager are moved to a new or different instance of Cisco Prime License
							 Manager through the re-hosting process. As part of this process, it
						  is suggested that the version number and Registration ID number be recorded in
						  some fashion following any installation of Cisco Prime License
							 Manager . | Note | This information can be used for re-hosting. Re-hosting is the
						  process that customers must follow to move licenses from one instance of Cisco Prime License
							 Manager to another. Licenses that have already been issued and
						  fulfilled in one instance of Cisco Prime License
							 Manager are moved to a new or different instance of Cisco Prime License
							 Manager through the re-hosting process. As part of this process, it
						  is suggested that the version number and Registration ID number be recorded in
						  some fashion following any installation of Cisco Prime License
							 Manager . |
| Note | This information can be used for re-hosting. Re-hosting is the
						  process that customers must follow to move licenses from one instance of Cisco Prime License
							 Manager to another. Licenses that have already been issued and
						  fulfilled in one instance of Cisco Prime License
							 Manager are moved to a new or different instance of Cisco Prime License
							 Manager through the re-hosting process. As part of this process, it
						  is suggested that the version number and Registration ID number be recorded in
						  some fashion following any installation of Cisco Prime License
							 Manager . |

| Note | This information can be used for re-hosting. Re-hosting is the
						  process that customers must follow to move licenses from one instance of Cisco Prime License
							 Manager to another. Licenses that have already been issued and
						  fulfilled in one instance of Cisco Prime License
							 Manager are moved to a new or different instance of Cisco Prime License
							 Manager through the re-hosting process. As part of this process, it
						  is suggested that the version number and Registration ID number be recorded in
						  some fashion following any installation of Cisco Prime License
							 Manager . |
|---|---|

| Setting | Description |
|---|---|
| Overview section |
| Product
						Instances | The
						total number of product instances managed by Cisco Prime License
						  Manager . Clicking Product Instances takes you to the Product
						Instances page. |
| Last
						License Update | The date
						of the last license update. Clicking Last License Update takes you to the
						Licenses > License Fulfillment page. |
| Last
						Synchronization | The date
						of the last successful synchronization. Clicking Last Synchronization takes you
						to the Product Instances page where you can view the Synchronization Status and
						Last Successful Synchronization for each product instance. You can also perform
						a synchronization from this page by clicking the Synchronize Now button. Note Synchronization occurs when Cisco Prime License
								Manager collects up-to-date licensing information for all license
							 types in the system. | Note | Synchronization occurs when Cisco Prime License
								Manager collects up-to-date licensing information for all license
							 types in the system. |
| Note | Synchronization occurs when Cisco Prime License
								Manager collects up-to-date licensing information for all license
							 types in the system. |
| License Alerts section |
| Type | License
						types that are non-compliant |
| Status | Provides
						information about the alert (for example, insufficient licenses or when a
						license is due to expire) |
| License Usage section |
| Type | Specifies the product type |
| Required | The
						number of licenses allocated to each of those product types |
| Product Instance Alerts
						  section |
| Name | Specifies the product name |
| Status | Provides
						information about the product |
| Last
						Synchronization | The date
						and time of the last successful synchronization |

| Note | Synchronization occurs when Cisco Prime License
								Manager collects up-to-date licensing information for all license
							 types in the system. |
|---|---|

| Note | In both Table
				and Chart views, you have the option of synchronizing the licenses by clicking
				the Synchronize Now button. |
|---|---|

| Setting | Description |
|---|---|
| Table View tab |
| Type | The name
					 of the license types supported within the product scope. For more information,
					 click on a particular license type in the Type column to open a detailed
					 license type page. |
| Product
					 Type | The
					 product type |
| Required | The number
					 of licenses required by the product instances in order to deliver the services
					 you have provisioned on those servers. |
| Installed | The number
					 of licenses currently installed |
| Available | The
					 difference between the number of Required and Installed licenses. The numbers
					 in this column are color-coded to represent the state of unused licenses for a
					 particular license type. If the
					 number is red, the number of licenses is considered insufficient. If the number
					 is black, the number of licenses is considered to be in compliance. |
| Status | The
					 license status (ex: “Temp Licenses Nearing Expiration”, “In Compliance”) |
| Synchronize Now button | Synchronizes Cisco Prime License
						Manager with the product instances to obtain the most up-to-date
					 licensing information for all license types in the system |
| Chart View tab |
| License
					 Type | The
					 License Type drop down menu allows you to select the type of license you wish
					 to view. |
| Installed/Borrowed | The
					 Installed/Borrowed licenses are categorized as: Installed Borrowed from Upper Tier Important: Not all
						products support tiering |
| Required/Loaned | The
					 Required/Loaned licenses are categorized as: Requested Loaned
						  to Lower Tier Note Moving
						your mouse over the bars in the chart reveals the number of licenses
						installed/borrowed or required/loaned | Note | Moving
						your mouse over the bars in the chart reveals the number of licenses
						installed/borrowed or required/loaned |
| Note | Moving
						your mouse over the bars in the chart reveals the number of licenses
						installed/borrowed or required/loaned |
| Synchronize Now button | Synchronizes Cisco Prime License
						Manager with the product instances to obtain the most up-to-date
					 licensing information for all license types in the system |
| History tab |
| History
					 tab | You can
					 download the usage history for your licenses into a csv file that can be opened
					 in a spreadsheet application. Usage data is collected at every synchronization
					 with product instance and with each action that changes license usage. |
| Date Range | Allows you
					 to select the start and end date for the period of time you wish to cover. |
| Product
					 Type | Specifies
					 the type of product instance |
| Generate
					 File button | Clicking
					 the Generate File button creates a usage history file for the product type
					 selected. A link to the file appears at the bottom of the screen. When you
					 click on the link, you have the option of opening the file or saving it to your
					 computer. |
| License Usage details
						page Note Clicking on a license in the Table View in the License Usage
						page opens this License Usage details page | Note | Clicking on a license in the Table View in the License Usage
						page opens this License Usage details page |
| Note | Clicking on a license in the Table View in the License Usage
						page opens this License Usage details page |
| License
					 Description section | The
					 License Description section provides a description of that license type. There
					 is also a link provided to view descriptions of all license types on Cisco.com. |
| Usage
					 Chart section | The Usage
					 Chart section provides a graphical representation of how many of that
					 particular license type are available, and of those, how many are installed or
					 borrowed from the upper tier. It also
					 indicates how many of that license type are being used, and of those, how many
					 are requested or loaned to the lower tier. |
| Usage by
					 Instance section | The Usage
					 by Instance section lists the systems that are using that particular license
					 type, and identifies the product type of the system, release version, and the
					 number of licenses required for each of those systems. |
| Installed
					 Licenses by Type section | The
					 Installed Licenses by Type section distinguishes between Permanent and
					 Temporary licenses, the number of licenses that each is limited to, and the
					 expiry date for the temporary licenses. |

| Note | Moving
						your mouse over the bars in the chart reveals the number of licenses
						installed/borrowed or required/loaned |
|---|---|

| Note | Clicking on a license in the Table View in the License Usage
						page opens this License Usage details page |
|---|---|

| Setting | Description |
|---|---|
| License Planning
						  page |
| Name | Specifies the name of the license plan Selecting a license plan name from the list in the History table
						opens the Details window for that license plan. This window contains the
						following information: Name (editable) Description (editable) Type Created Date Summary (includes a View Summary link that provides summary
							 information for that license plan) |
| Description | Provides a brief description of the license plan |
| Type | Specifies the license plan type: Migration or Add |
| Creation Date | Specifies the license plan creation date |
| Action | The
						Action column provides a Delete button to delete a license plan |
| Create
						an Add Licenses Plan button | Clicking the Create an Add Licenses Plan button opens the Create
						an Add Licenses Plan wizard. For instructions on how to complete the Create an
						Add Licenses Plan wizard, see the Cisco Prime License
						  Manager User Guide. |
| Create an Add Licenses
						  Plan page |
| Choose
						Product section | From
						the Choose Product section of the Create an Add Licenses Plan window, you can
						select (from the drop-down menus) the Product Type and the License Version to
						which you want to add licenses. |
| Specify License Counts section | From
						the Specify License Counts section of the Create an Add Licenses Plan window,
						you can adjust the number of licenses to be allocated to each type of license
						and save your changes for that license type. You
						may also choose to run a compliance check by clicking the Run Compliance Check
						button, or reset the license values by clicking the Reset Values button. |
| Summary and Next Steps | From
						the Summary and Next Steps section of the Create an Add Licenses Plan window,
						you can view and save a summary of the changes you made in the Choose Product
						and Specify License Counts sections. The
						Save Summary in Cisco Prime License Manager option is selected by default. A
						default name for the summary also appears in the Name field using the format
						<product-type>-add-<date-time-stamp> format. |

| Setting | Description |
|---|---|
| Enable button | Allows you to enable
				e-Fulfillment. This is the default state. |
| Disable button | Allows you to disable
				e-Fulfillment. If e-Fulfillment is disabled, by selecting the Disable button,
				only Manual Fulfillment options are visible. Note e-Migration is disabled if e-Fulfillment is disabled. | Note | e-Migration is disabled if e-Fulfillment is disabled. |
| Note | e-Migration is disabled if e-Fulfillment is disabled. |
| Fulfill Licenses from PAK
				button (e-Fulfillment) | Opens the Add/Install
				Licenses wizard (e-Fulfillment) |
| Other Fulfillment options
				(e-Fulfillment) | Clicking
				  the Other Fulfillment Options drop-down menu, visible when e-Fulfillment is
				  enabled, allows you to select: Fulfill Licenses from File Generate License Request Migrate Licenses Retrieve Fulfilled Licenses Note Only the Generate License
				  Request and Migrate License options are available under Manual fulfillment. The
				  Fulfill Licenses from File option opens the Install License File dialog box. The
				  Generate License Request option opens the License Request and Next Steps dialog
				  box. The Migrate License
				  option opens the Migrate Licenses to Cisco Prime License Manager page. | Note | Only the Generate License
				  Request and Migrate License options are available under Manual fulfillment. |
| Note | Only the Generate License
				  Request and Migrate License options are available under Manual fulfillment. |
| Fulfill Licenses from
				File button (Manual Fulfillment) | Opens the Install License
				File page |
| Other Fulfillment options
				(Manual Fulfillment) | Drop-down
				  menu, visible when e-Fulfillment is disabled, that allows you to: Generate License Request Migrate Licenses The
				  Generate License Request opens the License Request and Next Steps dialog box |
| Fulfillment Date | Specifies the date of
				license fulfillment |
| Description | The description,
				specified by the user in the wizard, of the license fulfillment |
| Method | Specifies the type of
				license fulfillment used (e-Fulfillment or File Install) |
| PAK | Specifies the PAK ID (in
				e-Fulfillment mode, the PAK IDs are clickable links that open the PAK detail
				window which allows you to adjust PAK fulfillment for that particular PAK) |

| Note | e-Migration is disabled if e-Fulfillment is disabled. |
|---|---|

| Note | Only the Generate License
				  Request and Migrate License options are available under Manual fulfillment. |
|---|---|

| Setting | Description |
|---|---|
| Choose New
				  License Version | From the
				  Choose New License Version section of the Migrate Licenses to Cisco Prime
				  License Manager window, you can select the Product Type and New License Version
				  from the drop-down menus. |
| Choose
				  Product Instances | From the
				  Choose Product Instances section of the Migrate Licenses to Cisco Prime License
				  Manager window, you can upgrade a product instance by selecting it in the
				  Available Product Instances window and click the arrow to move it to the
				  Product Instances to Upgrade window. |
| License
				  Counts (Unified CM) | From the
				  License Counts section of the Migrate Licenses to Cisco Prime License Manager
				  window, you can view a summary of pre-upgrade product instance data. This table
				  cannot be edited. If you
				  selected Unified
					 CM as your product type, the following options appear: Public
						Space Phones - An estimate of the number of public space phones. Public space
						phones do not have users assigned and are typically placed in shared
						workspaces, lobbies and meeting rooms. These phones generally require lower
						level licenses, so providing an estimate of the number of these phones in your
						deployment will help Cisco more accurately determine your license requirements. Case
						Numbers (Optional) - A case number assigned if the report was sent to Cisco
						Licensing Support License Usage Reports - Allows you to upload a License Usage
						Reports from a local drive. MAC
						addresses - The MAC addresses from the original servers that were upgraded.
						These MAC addresses can be used to look up the licenses that were registered on
						those product instances. Note The
						MAC Addresses field is only displayed if pre-upgrade license usage information
						is not available. For more information, see Alternate Cisco Unified Communications Manager Migrations Path . | Note | The
						MAC Addresses field is only displayed if pre-upgrade license usage information
						is not available. For more information, see Alternate Cisco Unified Communications Manager Migrations Path . |
| Note | The
						MAC Addresses field is only displayed if pre-upgrade license usage information
						is not available. For more information, see Alternate Cisco Unified Communications Manager Migrations Path . |
| License
				  Counts (Unity Connection) | The
				  content of the License Counts section of the Migrate Licenses to Enterprise
				  License Manager window depends entirely upon the options you have selected in
				  previous sections. If you
				  selected Unity
					 Connection , the following options appear: I have
						CUWL licenses to be migrated I do
						not have CUWL licenses to be migrated |
| License
				  Counts (standard product) | From the
				  License Counts section of the Migrate Licenses to Cisco Prime License Manager
				  window, you can view a table of the licenses available to migrate. This table
				  is editable. From the table, you can reduce (but not increase) license counts
				  in the Licenses to Migrate column. You can also run a compliance check by
				  clicking the Run
					 Compliance Check button, or reset the license values by clicking the Reset
					 Values button. |
| Summary
				  and Next Steps (Unified CM or Unity Connection > I have CUWL licenses to be
				  migrated) | The
				  content of the Summary and Next Steps section of the Migrate Licenses to
				  Enterprise License Manager window depends entirely upon the options you have
				  selected in previous sections. If you
				  selected Unified
					 CM as your product type, or Unity
					 Connection > I have CUWL licenses to be migrated , the following options
				  appear: In this
				  section you must indicate how the upgrade was ordered: Upgraded using one or more service contracts Purchased the upgrade If you
				  select Upgraded using one or more service contracts, enter the UCSS/ESW
				  Contract Numbers. If you
				  select Purchased the upgrade, enter the Sales Order Numbers. The Cisco.com (CCO) User ID field. Company
				  Name and the field used to capture additional information are optional.
				  However; if you enter the company name, it is used in the subject line of the
				  email and is included in the name of the zip file. A default
				  name for the summary also appears in the Name field using the format
				  <productname>-migrate-<date-time-stamp> format. Instructions for
				  placing your order and fulfilling your licenses also appear in this section.
				  Click Finish & Generate Request. The
				  License Migration Request and Next Steps window appears. Download the License
				  Migration Request zip file to your PC. Email the
				  License Migration Request to Cisco licensing support using the link provided. Click
				  Close to return to the License Fulfillment page. |
| Summary
				  and Next Steps (Unity Connection > I do not have CUWL licenses to be
				  migrated) when e-Fulfillment/e-Migration is enabled | The content of the
				Summary and Next Steps section of the Migrate Licenses to Enterprise License
				Manager window depends entirely upon the options you have selected in previous
				sections. If
				  e-Fulfillment is enabled, and you selected Unity
					 Connection > I do not have CUWL license to be migrated , the following
				  options appear: In this section, you can optionally enter a description of the
				  e-Migration transaction. Read the
				  End User License Agreement and select the checkbox to acknowledge the
				  agreement. |
| Summary
				  and Next Steps (Unity Connection > I do not have CUWL licenses to be
				  migrated) when e-Fulfillment/e-Migration is disabled | The
				  content of the Summary and Next Steps section of the Migrate Licenses to
				  Enterprise License Manager window depends entirely upon the options you have
				  selected in previous sections. If you
				  selected Unity
					 Connection > I do not have CUWL licenses to be migrated , the following
				  options appear: In this
				  section, you can view and save a summary of the changes you made. To view the
				  summary, click View Summary. A default name for the summary also appears in the
				  Name field using the format <productname>-migrate-<date-time-stamp>
				  format. Instructions for placing your order and fulfilling your licenses also
				  appear in this section. Click Finish & Generate Request. The
				  License Migration Request and Next Steps window appears. Copy the selected text
				  to your clipboard or click Save it to a file on your computer. Select
				  License Migration Portal under Step 2 and paste the copied text in the
				  designated field or select the saved file from your computer. Click
				  Close to return to the Add or Upgrade Licenses page. |
| License
				  Migration Request and Next Steps when e-Fulfillment/e-Migration is enabled | Clicking Finish
				  & Generate Request in the Summary and Next Steps section of the Migrate
				License Manager window initiates the e-Migration. Enter your Cisco user ID and
				password. The request is electronically submitted, and processed immediately.
				Your licenses are installed automatically. |
| License
				  Migration Request and Next Steps when e-Fulfillment/e-Migration is disabled | Clicking
				  the Finish & Generate Request button in the Summary and Next Steps section
				  of the Migrate Licenses to Cisco Prime License Manager window opens the License
				  Migration Request and Next Steps. You have
				  the option of copying the selected text or clicking the Save it to a file on
				  your computer link. |

| Note | The
						MAC Addresses field is only displayed if pre-upgrade license usage information
						is not available. For more information, see Alternate Cisco Unified Communications Manager Migrations Path . |
|---|---|

| Setting | Description |
|---|---|
| Specify
				  PAK | From the Specify PAK section of the Fulfill Licenses from PAK wizard, you can
				  add licenses from: A new PAK An already-installed PAK that supports partial fulfillment Only PAKs
				  that support partial fulfillment are displayed in the drop-down menu. |
| Fulfill
				  Licenses | From the
				  Fulfill Licenses section you can choose the licenses in the PAK that you want
				  to fulfill. The
				  Fulfill option, under the Actions column, allows you to fulfill a particular
				  license. Clicking the Fulfill option opens the Fulfill Licenses window. From
				  that window, you can adjust the number of licenses you wish to fulfill for a
				  particular license type. You can
				  also perform a compliance check of your licenses by clicking the Run Compliance
				  Check button. To reset
				  the values you have entered, click the Reset Values button. |
| Review
				  Contents | From the
				  Review Contents section of the Fulfill Licenses from PAK wizard, you can review
				  the contents of the PAK. If the PAK supports partial fulfillment, you can
				  adjust the license installation counts. |
| Transaction Options and License Agreement | From the
				  License Options section of the Fulfill Licenses from PAK wizard, you can add a
				  description to the transaction or associate it with a previously generated add
				  or upgrade plan. |

| Setting | Description |
|---|---|
| Browse
				  button | Allows you
				  to select a license file from your computer. |
| Options | The
				  Options section of the Install License File dialog box allows you to add a
				  description and associate your transaction with a saved add/migration license
				  summary. This step is optional. |
| Install
				  button | When the
				  license file has been selected (using the Browse button), it appears in the
				  License File field. The Install button is then used to install that license
				  file. |

| Setting | Description |
|---|---|
| Copy the
				  selected text | The first
				  step in the License Request and Next Steps dialog box provides the following
				  options: copy the text in the text box to your clipboard or click the link to
				  save the license request file to your computer. |
| Register
				  your Licenses | The second
				  step instructs you to register your licenses by clicking the link provided. |
| Install your
				  Licenses | The third
				  step advises you to return to Cisco Prime License Manager and install your licenses
				  once you have received them. License files are generally obtained via email or
				  downloaded from the Cisco portal. Clicking
				  the Install button returns you to the Licenses page. |

| Setting | Description |
|---|---|
| Adjust PAK Fulfillment
				option | Clicking the Adjust PAK
				Fulfillment link at the top of the PAK Details page retrieves the latest PAK
				details, changes the table from read-only to editable, and allows you to adjust
				the PAK fulfillment for Cisco Prime License Manager . |
| PAK Contents table | The PAK
				  Contents table contains the following columns: SKU
						Name specifies the name of a license contained in the file Type specifies the license type (ex: Permanent, Time-limited) Expiration specifies the expiry date of time-limited licenses Purchased specifies the total number of that license type in the PAK If you
				  select the Adjust PAK Fulfillment option, the following additional columns
				  appear in the table: Before Fulfillment Purchased Fulfilled Remaining Fulfill Remaining Actions |

| Setting | Description |
|---|---|
| Transaction Details | The File
				  Details section contains the following information: Fulfillment Date Description Associated Summary Method
						(File Install, e-Fulfillment, or Retrieve Fulfilled Licenses) Cisco.com Username PAK PAK
						Partial Fulfillment |
| License
				  Details | The
				  Licenses Fulfilled section contains a table that lists license files under the
				  following categories: Type Product Type Total
						on System (the number of that particular license type) Expiration date |

| Setting | Description |
|---|---|
| Edit Transaction Details | Clicking
				  the Edit Transaction Details button in the View <File ID> window opens
				  the Edit Transaction Details dialog box, which contains the following
				  information: Fulfillment Date Description Associated Summary Method
						(File Install, e-Fulfillment, or Retrieve Fulfilled Licenses) Cisco.com Username PAK PAK
						Partial Fulfillment The
				  Description and Associated Summary fields can be edited. |

| Setting | Description |
|---|---|
| Product Instances |
| Name | Specifies the name of the product instance |
| Hostname/IP Address | Specifies the hostname or IP address of the product instance |
| Product
						Type | Specifies the type of product instance |
| Version | Specifies the product release of the product instance |
| Status | Specifies the status of the product instance synchronization
						(for example, “Success”, “Registration Conflict”, “Invalid Server Type”,
						“Insufficient Licenses”) |
| Last
						Successful Synchronization | Specifies the date and time of the last successful
						synchronization. |
| Add
						button | Clicking
						the Add button on the Product Instances page opens the Product Add dialog box.
						From this dialog box, you can enter the following information: Name Description (optional) Product Type Hostname/IP Address Username Password Note Once you have added your new product instance, be sure to click
						  the Synchronize Now button to extract current licensing information from the
						  product. If you do not synchronize, current product instance information may
						  not appear in Cisco Prime License
							 Manager . | Note | Once you have added your new product instance, be sure to click
						  the Synchronize Now button to extract current licensing information from the
						  product. If you do not synchronize, current product instance information may
						  not appear in Cisco Prime License
							 Manager . |
| Note | Once you have added your new product instance, be sure to click
						  the Synchronize Now button to extract current licensing information from the
						  product. If you do not synchronize, current product instance information may
						  not appear in Cisco Prime License
							 Manager . |
| Test
						Connection button | From the
						Product Add dialog box, you can click the Test Connection button to test the
						connection to the product instance prior to adding it. If the
						connection cannot be established, either through the connection test or by
						clicking OK to add a product instance, you may receive one of the following
						error messages: Instance Unreachable Login Failed Certificate Mismatch Registration Conflict Invalid Server Type Product Type Mismatch Duplicate Product Instance Note You
						  may also skip the Test Connection button and click OK on the Add Product
						  Instance dialog box. | Note | You
						  may also skip the Test Connection button and click OK on the Add Product
						  Instance dialog box. |
| Note | You
						  may also skip the Test Connection button and click OK on the Add Product
						  Instance dialog box. |
| Delete
						button | You can
						delete a product instance by clicking the Delete link under the Action column
						for the product instance. |
| Launch
						Admin GUI button | You can
						open the administration GUI for a particular product instance by selecting the
						check box next to the product instance and clicking Launch Admin GUI. |
| Synchronize Now button | Synchronizes Cisco Prime License
						  Manager with the product instances to obtain the most up-to-date
						licensing information for all license types in the system |
| Product Instance details
						  page Note Clicking on a product instance in the Product Instance table
						  opens the following details page | Note | Clicking on a product instance in the Product Instance table
						  opens the following details page |
| Note | Clicking on a product instance in the Product Instance table
						  opens the following details page |
| General
						tab | The
						General tab is divided into two sections: Product Administrator Account The
						Product section contains the following information: Name Description Hostname/IP Address Product Type Product Version The
						Administrator Account section contains the following fields: Username Password Clicking
						the Save button saves your changes. Note Prior to clicking the Save button, you have the option of
						  clicking the Test Connection button to ensure that the connection is
						  established. | Note | Prior to clicking the Save button, you have the option of
						  clicking the Test Connection button to ensure that the connection is
						  established. |
| Note | Prior to clicking the Save button, you have the option of
						  clicking the Test Connection button to ensure that the connection is
						  established. |
| License
						Usage tab | The
						License Usage tab contains a graphical representation of the license requests
						and a table illustrating the number of licenses requested by license type. |

| Note | Once you have added your new product instance, be sure to click
						  the Synchronize Now button to extract current licensing information from the
						  product. If you do not synchronize, current product instance information may
						  not appear in Cisco Prime License
							 Manager . |
|---|---|

| Note | You
						  may also skip the Test Connection button and click OK on the Add Product
						  Instance dialog box. |
|---|---|

| Note | Clicking on a product instance in the Product Instance table
						  opens the following details page |
|---|---|

| Note | Prior to clicking the Save button, you have the option of
						  clicking the Test Connection button to ensure that the connection is
						  established. |
|---|---|

| Note | For information about OS Administration or Disaster Recovery, see
			 the Cisco Unified Communications Operating System Administration
				Guide or Disaster Recovery System Administration Guide for Cisco Unified
				Communications Manager . |
|---|---|

| Setting | Description |
|---|---|
| Administrator Accounts |
| Add
						Administrator button | Selecting the Add Administrator button in the Administrator
						Accounts window opens the Add Administrator Account window. From
						this window, you can add an administrator account. You are prompted for the
						following information: Name/Description Username Password Re-enter Password |
| Change
						Password | Selecting the Change Password link in the Administrators table
						opens the Change Password page. From this page you can change the password of
						an existing administrator account. You are prompted for the following
						information: New
							 Password Re-enter New Password |
| Backup/Restore |
| Backup
						Server | The
						Backup Server section contains the following fields: IP
							 Address/Hostname Username Password Directory The IP
						Address/Hostname specifies the IP Address/Hostname of the server to be backed
						up or restored. Enter your username and passport to connect to the server. The
						Directory field specifies the location of the backed up server (for example:
						/ws/user1-rcd/backup2) The
						Backup/Restore page also indicates when the last backup was performed. |
| Run
						Backup button | The Run
						Backup button initiates a backup of the server specified in the IP
						Address/Hostname field. |
| Run
						Restore button | The Run
						Restore button initiates a restore of the server specified in the Directory
						field. |
| Test
						Connection | The Test
						Connection button allows you test the connection to the product instance prior
						to performing a backup or restore. |
| Install/Upgrade |
| Install/Upgrade page | Use
						this page to upgrade your Cisco Prime License
						  Manager software or to add options such as language packs to your
						system. |
| System
						Software | Lists
						the active and inactive system software versions |
| Install/Upgrade Software wizard | Clicking on the Install/Upgrade Software button opens the
						Install/Upgrade Software wizard. This is a two-step wizard: Specify File Location Select File The
						Specify File Location page provides two options: Install/Upgrade from Network Install/Upgrade from DVD/CD drive on Cisco Prime License
								Manager server The
						Install/Upgrade from Network option requires the following information: IP
							 Address/Hostname Username Password Directory Transfer Protocol The IP
						Address/Hostname field specifies the location of the file to be installed or
						used for the upgrade . Enter your username and password to connect to the
						server. The Directory field specifies the location where the install or upgrade
						will be saved. The
						Transfer Protocol specifies the method: SFTP or FTP All
						valid upgrades are listed in the table. Select the appropriate (valid) upgrade
						file from the list and click the Start Installation/Upgrade button to begin the
						upgrade. |
| License Definitions |
| License Definitions | The
						License Definitions page contains information about the license types managed
						by Cisco Prime License
						  Manager . The License Definition file should be updated prior to
						upgrading any of your product instances to a new version or before adding a
						product instance of a new type. |
| Check
						for Latest Version | Clicking Check for Latest Version opens the Cisco Prime License
						  Manager Dashboard, which provides an overview of the license types
						currently in use. |
| View
						Release Notes | Clicking View Release Notes opens the License Definitions
						Release Notes page, which lists: Changes Since Previous Version Supported Products |
| Install New License Definition File button | Clicking the Install New License Definition File button opens
						the Install License Definitions window. Click the Browse button to locate the
						License Definitions File and then click Fulfill to install the file. |
| Diagnostic Logs |
| Log
						Settings tab | The Log
						Settings tab lists the diagnostics categories and log levels. The diagnostic
						categories include: Cisco Prime License Manager core services Communication with product instances The
						Log Level drop-down list for each diagnostic category can be set to one of the
						following: Error Warning Info Debug Once the
						log level has been set for each diagnostic category, you can save your changes
						by clicking the Save button. You may also opt to reset your log settings by
						clicking the Reset button. |
| Download
						Logs tab | The
						Download Logs tab allows you to generate a log file, using the date and time
						range of your choice to include in the log file. The default range is from 12
						AM of the current day until the current time. You can then generate the file by
						clicking the Generate Log File button. The log file is generated and downloaded
						to your computer. |
| Restart |
| Restart | Pressing the Restart button below restarts all Cisco Prime License
						  Manager services. This generally takes less than a minute and you
						will automatically be taken to the login screen when the restart is complete. |