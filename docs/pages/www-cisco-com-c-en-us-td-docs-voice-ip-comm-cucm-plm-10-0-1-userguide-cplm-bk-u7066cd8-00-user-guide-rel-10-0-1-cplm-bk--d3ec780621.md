---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-10-0-1-userguide-cplm-bk-u7066cd8-00-user-guide-rel-10-0-1-cplm-bk--d3ec780621
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/10_0_1/userguide/CPLM_BK_U7066CD8_00_user-guide-rel-10-0-1/CPLM_BK_U7066CD8_00_user-guide-rel-10-0-1_chapter_0100.html
retrieved_at: 2026-09-08T05:03:49.048299+00:00
---

Cisco Prime License Manager User Guide, Release 10.0(1)

# Cisco Prime License Manager User Guide, Release 10.0(1)

Updated: July 29, 2014

Chapter: Configuration

## Chapter: Configuration

# Configuration

The following sections provide information about how to use Cisco Prime License Manager .

## Getting
	 Started

Follow these steps
		  to begin using Cisco Prime License Manager :

Log in to Cisco Prime License Manager . See Log In .

Add a product
				instance. See Add Product Instance .

Use the
				Dashboard or the License Usage page to determine what licenses are required for
				your product. For more information on the Dashboard or the License Usage pages,
				see System Status Information .

Migrate your
				existing licenses if your Cisco Prime License Manager is managing any product
				instances that have been upgraded from a prior version of the product that
				implemented a different licensing methodology.

See Migrate Licenses to Cisco Prime License Manager .

Perform new
				license fulfillment. See License Planning .

## Log In

To log into a
		  standalone Cisco Prime License Manager , enter your username and
		  password. Click Login .

For coresident
		  configurations, use the following procedure to log in:

The "Getting
				  Started" window appears with options for the following:

## Add Product
	 Instance

The following
		  procedure describes how to add a product instance in Cisco Prime License Manager .

Install licenses that are installable at the product
			 instance prior to adding the product instance. This will ensure that   those licenses are eligible for migration.

If you want to add a Cisco Unified Communications Manager instance, check the status of the account using the following command: show accountlocking . The account locking setting must be set to disabled to avoid a 401 error when you attempt  to add the product instance.

- Name

- Description (optional)

- Product Type

- Hostname/IP Address

- Username

- Password

Credentials
				  are the OS Administration username and password of the product.

On the
				  Product Instances page, click the Synchronize Now button to request the licensing information
				  from the new product. If you do not synchronize, current product instance
				  information will not appear in Cisco Prime License Manager .

## Edit Product
	 Instance

The following
		  procedure describes how to edit a product instance in Cisco Prime License Manager .

## Delete Product
	 Instance

## System Status
	 Information

The Cisco Prime License Manager interface provides the
		  following views that enable you to monitor the system status:

## Dashboard
	 View

The Dashboard
		  provides an “at-a-glance” view of the system. Links in the Dashboard navigate
		  to their related pages within Cisco Prime License Manager .

The Dashboard
		  contains the following:

### Overview

Provides
		  information on Product Instances, Last License Update, and Last Synchronization
		  date and time.

### License
		  Usage

Lists the product
		  type and the number of licenses:

Installed

Required

### License
		  Alerts

Lists alerts
		  according to product type, the status of the alert and the number of licenses
		  available. Alerts indicate:

License types
				that are non-compliant

Licenses that
				are nearing expiration

### Product
		  Instance Alerts

Lists the product
		  instance name, status (including product grace period expiration), and last
		  successful synchronization.

## License Usage
	 View

The License Usage
		  view, accessed by selecting Licenses >
			 Usage in the Cisco Prime License Manager interface, identifies the
		  licenses installed on the system and how those licenses have been used at the
		  time of the last synchronization.

There are three
		  views available from the License Usage view:

Table View

Chart View

History

### Table
		  View

The Table View
		  provides the following information for each license type:

Type of
				licenses in use

Product Type

Number of
				licenses required

Number of
				licenses installed

Number of
				licenses available

Status of
				that license type (for example: in compliance, in violation, and so on)

You can also view
		  license properties and usage by selecting one of license types installed on the
		  system. The License Type details page contains the following information:

License
				Description

Usage Chart

Usage by
				Instance

Installed
				Licenses by Type

For a
		  comprehensive view of all license types, click the View All License
			 Type Descriptions and Device Classifications (new window) link under the
		  License Description section.

### Chart
		  View

The Chart View tab
		  presents a graphical view of the number of licenses used for a particular
		  product.

Select the License
			 Type from the drop-down menu to view the chart for that license version.
		  Place your mouse over each of the chart's bars to reveal license count
		  information. The figure below shows a Chart View, customized for each product
		  type, which illustrates the number of licenses:

Installed

Borrowed from
				Upper Tier

Required

Loaned to
				Lower Tier

The Chart View
		  also identifies, with a red “x”, instances where there are insufficient
		  licenses.

### History

This History tab
		  enables you to view how your license usage has changed over time. Usage data is
		  collected at every synchronization with product instance and with each action
		  that changes license usage. To download your usage history, select a date range
		  and the product and click the Generate
			 File button.

Clicking the
		  Generate File button creates a History report that appears at the bottom of the
		  History tab. You can download the History report into a csv file that can be
		  opened in a spreadsheet application. The History report shows licensing
		  installed and license consumption, including the compliance status.

### Substitution
		  and Tiering

License types are
		  categorized into license tiers, where the higher license tiers offer more
		  functionality than the lower tiers. For example, CUWL Professional, the highest
		  Unified CM-tiered type, offers more functionality than CUWL Premium or Advanced
		  (the exact functionality is specified in the License Usage Details screen). The
		  License Usage Table View and Chart View (as shown in the figure above) display
		  the types in order of tier, highest to lowest.

License
		  substitution refers to the Cisco Prime License Manager feature where a higher
		  tier license type can be substituted for a lower-tiered type that would
		  otherwise be in overage. In the Chart View example (in the above figure), there
		  are 50 spare CUWL Professional licenses on loan to Basic. In this example, the
		  50 spare licenses are sufficient to cover the entire Basic overage. If the user
		  installs a license file that adds Basic licenses, the spare CUWL Professional
		  license would then be available for future CUWL Professional requirements.

## License
	 Fulfillment View

Once a product
		  instance has been added (see Add Product Instance ), you must then identify your
		  licensing requirements and plan accordingly.

Cisco Prime License Manager provides two main options
		  for performing license fulfillment:

Electronic
				fulfillment (e-Fulfillment)

Manual
				fulfillment

Under each of
		  these fulfillment options, you may choose to do one of the following:

- New license fulfillment

- License upgrade

e-Fulfillment is the quicker and easier option of the two;
		  however, in deployments where internet connectivity is not available (a
		  locked-down lab for example) Manual fulfillment may be the only option.

e-Fulfillment
		  supports:

- License feature upgrades
			 (for example, a Basic UCL to Enhanced UCL upgrade)

- License version upgrades
			 (for example, a version 9.0 to version 10.0(1) license upgrade)

License Product
		  Authorization Keys (PAKs) can be fulfilled and installed directly from the
		  Cisco Prime License Manager.

### e-Fulfillment

Use the following
		  procedure to add new licenses via e-Fulfillment.

Log in to Cisco Prime License Manager .

Select Licenses
				  > Fulfillment.

If not
				already selected, click the Enable button to enable e-Fulfillment.

Select Fulfill
				  Licenses from PAK . The Fulfill Licenses from PAK window appears.

Select the Add licenses
				  from a new PAK option and enter the Product Authorization Key (PAK) code.

If you have
				previously entered PAKs in Cisco Prime License Manager , you may select the second
				option, "Add licenses from an already-installed PAK that supports partial
				fulfillment". Once you have selected that option, select the existing PAK code
				from the drop-down menu.

Click the Next button. If prompted for your Cisco.com account information, enter the username
				and password you entered when you registered at Cisco.com.

Click the Ok button. The Fulfill Licenses section appears.

The licenses
				within the PAK are listed by SKU name. The numbers of each license are
				categorized under a number of headings to indicate how many have been fulfilled
				and how many are remaining.

You can
				specify the number of licenses you want to fulfill by selecting Fulfill in the Actions column for that license type. The
				Fulfill Licenses window appears. In this window you can specify the count in
				the Fulfill column, and click Save then click OK to
				close the window. The updated count now appears in the Fulfill column of the
				Fulfill Licenses table.

Some PAKs
				  are not eligible for partial fulfillment.

If licenses
				  are listed as "Fulfilled" (under "Before Fulfillment" in the Fulfill Licenses
				  table), those licenses have been fulfilled by this or another Cisco Prime License Manager .

- Click the Next button to review your changes. If you are not satisfied with your changes,
			 click Previous to return to the Fulfill Licenses section. If you are satisfied with the
			 changes, click Next to
			 move to the next section.

Clicking Next
				in the Fulfill Licenses section opens the Transaction Options and License
				Agreement section. In this section, you may enter a description (optional). You
				may also associate this transaction with a saved license summary by selecting
				that option and then selecting the name of the license summary from the
				drop-down list.

Select the
				checkbox to accept the conditions of the End User License Agreement.

Click the Finish button.

Upon
				successful completion of the e-Fulfillment process, the new fulfillment appears
				in the License Fulfillment table.

Adjust PAK
			 fulfillment

In e-Fulfillment
		  mode, you can perform partial fulfillment of a particular PAK that has already
		  been partially fulfilled on that Cisco Prime License Manager using the following
		  procedure:

In the
				Licenses > Fulfillment page, in the License Fulfillment table, select the
				PAK from the list under the PAK column.

An edit
				  (pencil) icon denotes PAKs which support partial fulfillment.

The PAK
				Details window opens, showing the original number of licenses in the PAK.
				Select Adjust PAK
				  Fulfillment to retrieve the current status of the PAK.

If prompted,
				enter your Cisco.com username and password (the information entered when you
				registered at Cisco.com).

You can
				specify the number of licenses you want to fulfill by selecting Fulfill in the Actions column for that license type. The
				Fulfill Licenses window appears. In this window you can specify the count in
				the Fulfill column, and click Save then click OK to
				close the window. The updated count now appears in the Fulfill column of the
				Fulfill Licenses table.

You have the
				option of entering a description in the Transaction Options field. This allows
				you to track this transaction.

Once you
				have adjusted your PAK fulfillment numbers, click the Update PAK
				  Fulfillment button.

Fulfillment numbers can only be increased, never decreased.

### Manual Fulfillment

Manual
		  fulfillment requires additional steps to perform license fulfillment. In
		  situations where internet connectivity is not available, Manual fulfillment is
		  the only method available. Manual fulfillment is also necessary for license
		  migration, as described below:

Migrate
				existing licenses (if applicable) into Cisco Prime License Manager . To migrate existing
				licenses, see Migrate Licenses to Cisco Prime License Manager

Once any
				existing licenses have been migrated, acquire new licenses using the following
				procedure: License Planning .

## Migrate Licenses
	 to Cisco Prime License Manager

This section
		  describes the different migration paths you can follow using Cisco Prime
		  License Manager.

A standard
		  product is any product type supported by Cisco Prime License Manager other than
		  Cisco Unified Communications Manager or Cisco Unity Connection.

The migration
		  path you follow depends upon a number of factors (For example: the product
		  type, whether servers contain data from a previous version, etc). The following
		  flow charts provide a guide for the decisions that must be made to successfully
		  complete your migration. For a broader view of the migration process, see the
		  release notes for the product instance in question.

Cisco Unified
			 Communications Manager and Cisco Unity Connection each have unique migration
			 processes.

Use the
		  following procedure to plan for migration of product instances whose licenses
		  have not yet been migrated to Cisco Prime License Manager if e-Fulfillment is
		  enabled.

### Standard Product
	 Migration Path with E-Fulfillment Enabled

Click Next.

### Standard Product
	 Migration Path with E-Fulfillment Disabled

Use the following
		  procedure to plan for migration of product instances whose licenses have not
		  yet been migrated to Cisco Prime License Manager if e-Fulfillment is disabled.

Click Next.

### Cisco Unified
	 Communications Manager Migration Path

The following flow
		  chart will aid you in migrating Cisco Unified Communications Manager licenses
		  to Cisco Prime License Manager:

Use the following
		  procedure to plan for migration of all Unified Communication product instances
		  whose licenses have not yet been migrated to Cisco Prime License Manager if
		  e-Fulfillment is disabled.

Click Next.

An
					 estimate of the number of public space phones. Public space phones do not have
					 users assigned and are typically placed in shared workspaces, lobbies and
					 meeting rooms. These phones generally require lower level licenses, so
					 providing an estimate of the number of these phones in your deployment will
					 help Cisco more accurately determine your license requirements.

A case
					 number assigned if the report was sent to Cisco Licensing Support

Click the Upload
						Report button to open the Upload License Count Utility Report dialog box.
					 Click the Browse button to select the report file and then click Upload
						Report .

The MAC
					 addresses from the original servers that were upgraded. These MAC addresses can
					 be used to look up the licenses that were registered on those product
					 instances.

- Upgraded using one or more
				service contracts

- Purchased the upgrade

Company Name
				and the field used to capture additional information are optional. However; if
				you enter the company name, it is used in the subject line of the email and is
				included in the name of the zip file.

A default name
				for the summary also appears in the Name field using the format
				<productname>-migrate-<date-time-stamp> format. Instructions for
				placing your order and fulfilling your licenses also appear in this section.
				Click Finish &
				  Generate Request .

Email the
				License Migration Request to Cisco licensing support using the link provided.

Click Close to
				return to the License Fulfillment page.

### Cisco Unity
	 Connection Migration Path

The following flow
		  chart will aid you in migrating Cisco Unity Connection licenses to Cisco Prime
		  License Manager:

Use the following
		  procedure to plan for migration of all Unity Connection product instances whose
		  licenses have not yet been migrated to Cisco Prime License Manager.

Click Next.

Click Next to move on to the Summary and Next Steps section.

The
					 Licenses to be Migrated dialog box opens. From the table, you can reduce (but
					 not increase) your license counts in the Licenses to Migrate column. You may
					 also choose to run a compliance check by clicking the Run Compliance Check
					 button, or reset the license values by clicking the Reset Values button. Click OK to close the dialog box and then click Next to move on to the Summary and Next
					 Steps section.

In this
					 section you must indicate how the upgrade was ordered:

- Upgraded
					 using one or more service contracts

-
					 Purchased the upgrade

If you
					 select Upgraded using one or more service contracts, enter the UCSS/ESW
						Contract Numbers .

If you
					 select Purchased the upgrade, enter the Sales
						Order Numbers .

Enter
					 your Cisco user ID in the Cisco.com (CCO) User ID field.

Company
					 Name and the field used to capture additional information are optional.
					 However; if you enter the company name, it is used in the subject line of the
					 email and is included in the name of the zip file.

A
					 default name for the summary also appears in the Name field using the format
					 <productname>-migrate-<date-time-stamp> format. Instructions for
					 placing your order and fulfilling your licenses also appear in this section.
					 Click Finish
						& Generate Request .

The
					 License Migration Request and Next Steps window appears. Download the License
					 Migration Request zip file to your PC.

Email
					 the License Migration Request to Cisco licensing support using the link
					 provided.

Click Close to return to the License Fulfillment page.

- Specify an optional
						description for the transaction. Read the end User License Agreement and select
						the check box to confirm.

- Click Finish and Generate .

- Enter your Cisco.com
						login and click OK .

- The request is
						electronically submitted, processed immediately, and your licenses are
						installed automatically.

In this
					 section you can view and save a summary of the changes you made. To view the
					 summary, click View Summary. A default name for the summary also appears in the
					 Name field using the format <productname>-migrate-<date-time-stamp>
					 format. Instructions for placing your order and fulfilling your licenses also
					 appear in this section. Click Finish
						& Generate Request .

The
					 License Migration Request and Next Steps window appears. Copy the selected text
					 to your clipboard or click Save
						it to a file on your computer .

Select License Migration Portal under Step 2 and paste the copied
					 text in the designated field or select the saved file from your computer.

Click Close to return to the License Fulfillment page.

### Alternate Cisco
	 Unified Communications Manager Migrations Path

The following are
		  alternate migration paths, available for use under specific circumstances:

- Upgrades completed without
			 the License Count Utility (LCU) Report

- Fresh install with
			 imported pre-9.x data

Upgrades completed without
			 LCU Report

The Cisco Prime
		  License Manager Migration Utility relies on DLU and license usage retained
		  during the upgrade.

In situations
		  where a product is upgraded to 10.x without running License Count Utility on
		  a pre-9.x version. Please contact the Cisco licensing office and have the
		  license file reissued if changes are required.

Fresh install with
			 imported pre-9.x data

A migration may
		  be required following a fresh install in situations where pre-9.0 DLU or
		  license information is not available in Release 10.x VM. This may occur
		  when:

- UC Release 8.6 needs to be
			 upgraded as a new VM, with phone data exported

- A new Release10.x VM is
			 created, with phone data imported

The following
		  procedure enables you to perform a migration after a fresh install. This
		  procedure requires that an LCU report be run against pre-upgrade product
		  instance, if still accessible, or that MAC addresses of the pre-upgrade product
		  instances be available.

- The number of public space
				phones in the Public Space Phones field

- Case Numbers

- License Count Utility
				Reports - select the zip file using the Upload Report button

- The MAC address in the MAC
				Addresses field

### Licensing Migration
	 Support

Product licensing has a grace period from the time that users
		  are configured on the system. For Cisco Unified Communications Manager and Unity Connection, the grace
		  period is 60 days.

The Global
		  Licensing Operations (GLO) Team is available 24 x 7 x 365 and has knowledgeable
		  agents that can help process your request and
			 route it to the team best able to assist you. 
		Expect a response within
			 48-72 hours

To obtain
		  migration support, select one of the following options:

- Open your service request
			 through the web: https:/​/​tools.cisco.com/​ServiceRequestTool/​scm/​mgmt/​case

- Open any service request
			 through licensing@cisco.com (include Cisco.com user ID)

- Open a service request by
			 telephone using country-specific numbers: http:/​/​www.cisco.com/​en/​US/​support/​tsd_​cisco_​worldwide_​contacts.html

## New License
	 Planning and Fulfillment

### License
	 Planning

Use the following
		  procedure to plan the addition of new licenses.

Clicking the
				arrow next to each license type reveals additional information about that license
				type.

Place your order: Purchase your licenses or use your service contract to get a
				PAK.

Fulfill your licenses: Enter your PAK into the License Fulfillment screen of Cisco Prime License
				Manager and, through the e-Fulfillment process, fulfill your licenses. Cisco
				Prime License Manager communicates with Cisco licensing servers and your new
				licenses will be installed and ready to use.

### Configure License Fulfillment Electronically

Complete the following procedure to electronically
		  fulfill your licenses.

Create a licenses plan.

## Upgrade Existing
	 Licenses

There are three
		  types of license upgrades:

- License feature upgrades

- License version upgrades

- License feature and version
			 upgrades

Use the following
		  procedure to fulfill a major version upgrade using eFulfillment.

## Other Fulfillment
	 Options

Next to the
		  Fulfill Licenses from PAK option on the License Fulfillment page, there is
		  another option entitled "Other Fulfillment Options".

In Manual
		  Fulfillment mode, selecting the drop-down arrow under this option reveals only
		  one option: Generate License Request.

In eFulfillment
		  mode, selecting the drop-down arrow under this option reveals three options:

- Fulfill Licenses from File

- Generate License Request

- Retrieve Fulfilled Licenses

### Fulfill
		  Licenses From File

To fulfill
		  licenses from a file on your PC:

- Select Other
				Fulfillment Options > Fulfill Licenses from File .

- The Install License File
			 window opens. Click the Browse button to locate the file on your PC. Select the file and click Open .

- You can add a description
			 and associate the transaction with a saved license plan (optional).

- Click the Install button to install the license file.

### Generate
		  License Request

To obtain a new
		  license (using Manual fulfillment), you must first generate a license request
		  through the Licenses > Fulfillment page, and then use the information
		  generated to submit a request. You will then receive your license file via
		  email. Use the following procedure to generate a license request.

- Log in to Cisco Prime License Manager .

- From the Licenses >
			 Fulfillment page, select Generate
				License Request from the drop-down list under Other Fulfillment Options.

- The License Request and
			 Next Steps window appears. Copy the selected text to your clipboard or click Save it to a
				file on your PC .

### Retrieve
		  Fulfilled Licenses

The "Retrieve
		  Fulfilled Licenses" option is exclusive to e-Fulfillment. This feature connects
		  to the Cisco licensing servers to retrieve and install the licenses that have
		  been fulfilled for this Prime License Manager. This feature is useful if you
		  wish to synchronize your Cisco Prime License Manager with the Cisco back office
		  with regard to licenses that have been fulfilled.

Use the following
		  procedure to retrieve fulfilled licenses:

Log in to Cisco Prime License Manager .

Select Licenses
				  > Fulfillment.

If not
				already selected, click the Enable button to enable e-Fulfillment.

Under Other
				Fulfillment Options, select Retrieve
				  Fulfilled Licenses . The Retrieve Fulfilled Licenses window appears.

Enter your
				Cisco Username and Password. You can add a description (optional) in the
				Transaction Description field.

Click the Retrieve and
				  Install Licenses button.

Your Cisco
				Prime License Manager is synchronized with the Cisco back office and all
				licenses currently fulfilled are installed.

| Step 1 | Select Cisco
			 Prime License Manager from the list of installed applications. |
|---|---|
| Step 2 | Enter your
			 username and password. Click Login Note The initial
				login requires the application username and password that you created as part
				of the installation. If you are not sure what username and password to use for
				signing into Cisco Prime License Manager , see Troubleshooting . The "Getting
				  Started" window appears with options for the following: Note The "Getting
				  Started" window will not appear after you add an instance, or install a
				license. You can also select the Do not show
				  this again option to disable the window. If the window appears after you
				have completed these steps, log out of the Cisco Prime License Manager session
				and log in again. | Note | The initial
				login requires the application username and password that you created as part
				of the installation. If you are not sure what username and password to use for
				signing into Cisco Prime License Manager , see Troubleshooting . | Note | The "Getting
				  Started" window will not appear after you add an instance, or install a
				license. You can also select the Do not show
				  this again option to disable the window. If the window appears after you
				have completed these steps, log out of the Cisco Prime License Manager session
				and log in again. |
| Note | The initial
				login requires the application username and password that you created as part
				of the installation. If you are not sure what username and password to use for
				signing into Cisco Prime License Manager , see Troubleshooting . |
| Note | The "Getting
				  Started" window will not appear after you add an instance, or install a
				license. You can also select the Do not show
				  this again option to disable the window. If the window appears after you
				have completed these steps, log out of the Cisco Prime License Manager session
				and log in again. |

| Note | The initial
				login requires the application username and password that you created as part
				of the installation. If you are not sure what username and password to use for
				signing into Cisco Prime License Manager , see Troubleshooting . |
|---|---|

| Note | The "Getting
				  Started" window will not appear after you add an instance, or install a
				license. You can also select the Do not show
				  this again option to disable the window. If the window appears after you
				have completed these steps, log out of the Cisco Prime License Manager session
				and log in again. |
|---|---|

| Step 1 | Log in to Cisco Prime License Manager . |
|---|---|
| Step 2 | Choose Product
				Instances . |
| Step 3 | Click Add . The
			 Product Add dialog box appears. |
| Step 4 | Enter the
			 following information: Name Description (optional) Product Type Hostname/IP Address Username Password Note Credentials
				  are the OS Administration username and password of the product. | Note | Credentials
				  are the OS Administration username and password of the product. |
| Note | Credentials
				  are the OS Administration username and password of the product. |
| Step 5 | Click OK to add
			 the product instance. |
| Step 6 | Once the
			 product instance has been successfully added, the product appears in the
			 Product Instances table. Note On the
				  Product Instances page, click the Synchronize Now button to request the licensing information
				  from the new product. If you do not synchronize, current product instance
				  information will not appear in Cisco Prime License Manager . Note "Contains Migratable Licenses" appears in the Status field for all product
				  instances whose licenses have not yet been migrated to Cisco Prime License
				  Manager. To make any licenses that are installable at the product instance
				  available in the Cisco Prime License Manager , they must be migrated.
				  For information on migrating licenses, see: Migrate Licenses to Cisco Prime License Manager . | Note | On the
				  Product Instances page, click the Synchronize Now button to request the licensing information
				  from the new product. If you do not synchronize, current product instance
				  information will not appear in Cisco Prime License Manager . | Note | "Contains Migratable Licenses" appears in the Status field for all product
				  instances whose licenses have not yet been migrated to Cisco Prime License
				  Manager. To make any licenses that are installable at the product instance
				  available in the Cisco Prime License Manager , they must be migrated.
				  For information on migrating licenses, see: Migrate Licenses to Cisco Prime License Manager . |
| Note | On the
				  Product Instances page, click the Synchronize Now button to request the licensing information
				  from the new product. If you do not synchronize, current product instance
				  information will not appear in Cisco Prime License Manager . |
| Note | "Contains Migratable Licenses" appears in the Status field for all product
				  instances whose licenses have not yet been migrated to Cisco Prime License
				  Manager. To make any licenses that are installable at the product instance
				  available in the Cisco Prime License Manager , they must be migrated.
				  For information on migrating licenses, see: Migrate Licenses to Cisco Prime License Manager . |

| Note | Credentials
				  are the OS Administration username and password of the product. |
|---|---|

| Note | On the
				  Product Instances page, click the Synchronize Now button to request the licensing information
				  from the new product. If you do not synchronize, current product instance
				  information will not appear in Cisco Prime License Manager . |
|---|---|

| Note | "Contains Migratable Licenses" appears in the Status field for all product
				  instances whose licenses have not yet been migrated to Cisco Prime License
				  Manager. To make any licenses that are installable at the product instance
				  available in the Cisco Prime License Manager , they must be migrated.
				  For information on migrating licenses, see: Migrate Licenses to Cisco Prime License Manager . |
|---|---|

| Step 1 | To edit a
			 product instance, select that instance from the Product Instances table. |
|---|---|
| Step 2 | From the
			 General tab of the Product Instance details page, edit the preferred settings
			 for the product instance. Important: If the hostname or IP address of the product instance changes,
				you need to delete the product instance from the Cisco Prime License Manager prior to changing the
				hostname/IP address. You then re-add it to the Cisco Prime License Manager once you have completed
				the hostname/IP address change. |

| Step 1 | In the Action
			 column for the product instance you wish to delete, click the Delete button. |
|---|---|
| Step 2 | A message
			 appears, confirming that the product instance was successfully deleted. |
| Step 3 | Following a
			 successful deletion, click the Synchronize Now button to obtain the most
			 up-to-date licensing information for all license types in the system. |

| Note | When Cisco Prime License Manager is first installed, it
			 operates in Demo mode until a license file is installed. While Cisco Prime License Manager is in Demo mode, a warning
			 appears at the top of the GUI. |
|---|---|

| Note | Demo mode in Cisco Prime License Manager refers to the fact that no
			 license file has been installed yet. During the first license file installation
			 process, Cisco Prime License Manager is registered with the
			 Cisco licensing back office and is no longer in Demo mode. Product instances
			 managed by Cisco Prime License Manager are not in compliance as
			 long as Cisco Prime License Manager is in Demo mode. Each
			 product type (for example, Unified CM, Unity Connection) has its own version of
			 "demo mode" that operates independently of Cisco Prime License Manager ’s Demo mode. |
|---|---|

| Note | The product
		  grace period expiration provides additional information for products with
		  insufficient licenses. Clicking on the red "x" or alert symbol in the Status
		  column provides more detailed information (for example: "This product instance
		  is consuming more licenses than are available in Cisco Prime License Manager
		  and may experience service degradation until you install sufficient licenses to
		  cover its usage. Check your product documentation for more information."). |
|---|---|

| Note | License
		  versions are shown as “9.x” rather than “9.0”. This reduces confusion as 9.0
		  licenses are valid for all 9.x licenses. |
|---|---|

| Note | The chart you
		  see depends largely on the license type you select from the drop-down menu. For
		  example, Unified CM and has borrowing and tiering whereas Emergency Responder
		  does not. The legend is hidden for product types that do not support license
		  substitution. |
|---|---|

| Note | Substitution and tiering does not apply to all products
			 supported by Cisco Prime License Manager . If your product supports
			 substitution and tiering, refer to the following description and examples. |
|---|---|

| Note | You may wish
			 to check your Dashboard or License Usage page first, to determine what licenses
			 are required for your product. For more information on the Dashboard or the
			 License Usage pages, see System Status Information . |
|---|---|

| Note | If licenses
				  are listed as "Fulfilled" (under "Before Fulfillment" in the Fulfill Licenses
				  table), those licenses have been fulfilled by this or another Cisco Prime License Manager . |
|---|---|

| Note | Once you
				have fulfilled your licenses as selected, you may wish to click the Run
				  Compliance Check button to ensure that you are in compliance. |
|---|---|

| Note | An edit
				  (pencil) icon denotes PAKs which support partial fulfillment. |
|---|---|

| Note | Fulfillment numbers can only be increased, never decreased. |
|---|---|

| Note |  |
|---|---|

| Note | If Cisco
		  Prime License Manager is in demo mode, do not create multiple migration
		  requests. Complete the first migration, including installation of the license,
		  prior to initiating a second migration. If a migration request results in
		  multiple license files, install all of them, in order, before proceeding. |
|---|---|

| Note | Cisco Unified
			 Communications Manager and Cisco Unity Connection each have unique migration
			 processes. |
|---|---|

| Step 1 | From the Licenses > Fulfillment page in Cisco Prime License Manager, choose Fulfillment
				  Options > Migrate Licenses . The Migrate
			 Licenses to Cisco Prime License Manager wizard window appears. |
|---|---|
| Step 2 | From the Choose Product Type section,
			 choose the type of product to upgrade from the drop-down menu and click Next . The Choose
			 Product Instances section appears. |
| Step 3 | From the Available Product Instances window, choose a product instance and click the arrow to move it to the Product Instances to Migrate window. Click Next. The Licenses
			 to be Migrated dialog box opens. |
| Step 4 | From the table, you can reduce (but not
			 increase) your license counts in the Licenses to Migrate column. You may also
			 choose to run a compliance check by clicking Run Compliance Check ,
			 or reset the license values by clicking Reset Values . Click OK to
			 close the dialog box and then click Next to move on to the Summary and Next
			 Steps section. |
| Step 5 | Specify an
			 optional description for the transaction. Read the End User License Agreement
			 and click Finish &
				Generate Request . |
| Step 6 | Enter your
			 Cisco user ID in the Cisco.com
				(CCO) User ID field. The request
			 is electronically submitted, and processed immediately. Your licenses are
			 installed automatically. |

| Step 1 | From the Licenses > Fulfillment page in Cisco Prime License Manager, choose Fulfillment
				  Options > Migrate Licenses . The Migrate
			 Licenses to Cisco Prime License Manager wizard window appears. |
|---|---|
| Step 2 | From the Choose Product Type section,
			 choose the type of product to upgrade from the drop-down menu and click Next . The Choose
			 Product Instances section appears. |
| Step 3 | In
			 the Available Product Instances window, choose a product instance and click the arrow to move it to the Product Instances to Migrate window. Click Next. The Licenses
			 to be Migrated dialog box opens. |
| Step 4 | From the table, you can reduce (but not
			 increase) your license counts in the Licenses to Migrate column. You may also
			 choose to run a compliance check by clicking the Run Compliance Check button,
			 or reset the license values by clicking the Reset Values button. Click OK to
			 close the dialog box and then click Next to move on to the Summary and Next
			 Steps section. |
| Step 5 | In the Summary
			 and Next Steps section, you can view and save a summary
			 of the changes you made. To view the summary, click View Summary . A default
			 name for the summary also appears in the Name field using the format
			 <productname>-migrate-<date-time-stamp> format. Instructions for
			 placing your order and fulfilling your licenses also appear in this section.
			 Click Finish &
				Generate Request . The License
			 Migration Request and Next Steps window appears. |
| Step 6 | Copy the selected text to your
			 clipboard or click Save it to a
				file on your computer . |
| Step 7 | Choose License
				Migration Portal under Step 2 and paste the copied text in the designated
			 field or select the saved file from your computer. |
| Step 8 | Click Close to
			 return to the License Fulfillment page. |

| Step 1 | From the
			 Licences > Fulfilment page in Cisco Prime License Manager, click Fulfillment
				  Options > Migrate Licenses . |
|---|---|
| Step 2 | The Migrate
			 Licenses to Cisco Prime License Manager wizard window appears. The first step
			 involves choosing the product type. From the Choose Product Type section,
			 select Unified CM from the drop-down menu. The migration process is outlined in this section, and
			 is dependent on the type of product you select. Click Next . |
| Step 3 | The Choose
			 Product Instances section appears. To upgrade a product instance, select it in
			 the Available Product Instances window and click the arrow to move it to the
			 Product Instances to Migrate window. Note By
				  default, only product instances containing license data from a previous version
				  of Cisco Unified Communications Manager are displayed in the Available Product
				  Instances table. If the product instance you upgraded does not appear in the
				  list, click the “Show additional Unified CM product instances” check box.
				  Selecting this check box adds to the list those product instances that contain
				  no prior license data and those that were included in prior license migration
				  requests. Click Next. | Note | By
				  default, only product instances containing license data from a previous version
				  of Cisco Unified Communications Manager are displayed in the Available Product
				  Instances table. If the product instance you upgraded does not appear in the
				  list, click the “Show additional Unified CM product instances” check box.
				  Selecting this check box adds to the list those product instances that contain
				  no prior license data and those that were included in prior license migration
				  requests. |
| Note | By
				  default, only product instances containing license data from a previous version
				  of Cisco Unified Communications Manager are displayed in the Available Product
				  Instances table. If the product instance you upgraded does not appear in the
				  list, click the “Show additional Unified CM product instances” check box.
				  Selecting this check box adds to the list those product instances that contain
				  no prior license data and those that were included in prior license migration
				  requests. |
| Step 4 | The License
			 Counts section appears. The Summary of Pre-Upgrade Product Instance Data table
			 lists the product instances you selected in the previous step. This table
			 cannot be edited. Below the table are a number of fields that require input: Field Input Public Space
				  Phones An
					 estimate of the number of public space phones. Public space phones do not have
					 users assigned and are typically placed in shared workspaces, lobbies and
					 meeting rooms. These phones generally require lower level licenses, so
					 providing an estimate of the number of these phones in your deployment will
					 help Cisco more accurately determine your license requirements. Case Numbers
				  (Optional) A case
					 number assigned if the report was sent to Cisco Licensing Support License Count Utility
				  Reports (Optional) Click the Upload
						Report button to open the Upload License Count Utility Report dialog box.
					 Click the Browse button to select the report file and then click Upload
						Report . MAC Addresses
				  (Optional) The MAC
					 addresses from the original servers that were upgraded. These MAC addresses can
					 be used to look up the licenses that were registered on those product
					 instances. Once you have
			 selected the appropriate option and entered the necessary information, click Next . | Field | Input | Public Space
				  Phones | An
					 estimate of the number of public space phones. Public space phones do not have
					 users assigned and are typically placed in shared workspaces, lobbies and
					 meeting rooms. These phones generally require lower level licenses, so
					 providing an estimate of the number of these phones in your deployment will
					 help Cisco more accurately determine your license requirements. | Case Numbers
				  (Optional) | A case
					 number assigned if the report was sent to Cisco Licensing Support | License Count Utility
				  Reports (Optional) | Click the Upload
						Report button to open the Upload License Count Utility Report dialog box.
					 Click the Browse button to select the report file and then click Upload
						Report . | MAC Addresses
				  (Optional) | The MAC
					 addresses from the original servers that were upgraded. These MAC addresses can
					 be used to look up the licenses that were registered on those product
					 instances. |
| Field | Input |
| Public Space
				  Phones | An
					 estimate of the number of public space phones. Public space phones do not have
					 users assigned and are typically placed in shared workspaces, lobbies and
					 meeting rooms. These phones generally require lower level licenses, so
					 providing an estimate of the number of these phones in your deployment will
					 help Cisco more accurately determine your license requirements. |
| Case Numbers
				  (Optional) | A case
					 number assigned if the report was sent to Cisco Licensing Support |
| License Count Utility
				  Reports (Optional) | Click the Upload
						Report button to open the Upload License Count Utility Report dialog box.
					 Click the Browse button to select the report file and then click Upload
						Report . |
| MAC Addresses
				  (Optional) | The MAC
					 addresses from the original servers that were upgraded. These MAC addresses can
					 be used to look up the licenses that were registered on those product
					 instances. |
| Step 5 | The Summary
			 and Next Steps section appears. In this section you must indicate how the
			 upgrade was ordered: Upgraded using one or more
				service contracts Purchased the upgrade If you select
			 "Upgraded using one or more service contracts", enter the UCSS/ESW Contract
				Numbers . 
		   If you select
			 "Purchased the upgrade", enter the Sales Order
				Numbers . |
| Step 6 | Enter your
			 Cisco user ID in the Cisco.com
				(CCO) User ID field. Company Name
				and the field used to capture additional information are optional. However; if
				you enter the company name, it is used in the subject line of the email and is
				included in the name of the zip file. A default name
				for the summary also appears in the Name field using the format
				<productname>-migrate-<date-time-stamp> format. Instructions for
				placing your order and fulfilling your licenses also appear in this section.
				Click Finish &
				  Generate Request . |
| Step 7 | The License
			 Migration Request and Next Steps window appears. Download the License Migration
			 Request zip file to your PC. Email the
				License Migration Request to Cisco licensing support using the link provided. Click Close to
				return to the License Fulfillment page. |

| Note | By
				  default, only product instances containing license data from a previous version
				  of Cisco Unified Communications Manager are displayed in the Available Product
				  Instances table. If the product instance you upgraded does not appear in the
				  list, click the “Show additional Unified CM product instances” check box.
				  Selecting this check box adds to the list those product instances that contain
				  no prior license data and those that were included in prior license migration
				  requests. |
|---|---|

| Field | Input |
|---|---|
| Public Space
				  Phones | An
					 estimate of the number of public space phones. Public space phones do not have
					 users assigned and are typically placed in shared workspaces, lobbies and
					 meeting rooms. These phones generally require lower level licenses, so
					 providing an estimate of the number of these phones in your deployment will
					 help Cisco more accurately determine your license requirements. |
| Case Numbers
				  (Optional) | A case
					 number assigned if the report was sent to Cisco Licensing Support |
| License Count Utility
				  Reports (Optional) | Click the Upload
						Report button to open the Upload License Count Utility Report dialog box.
					 Click the Browse button to select the report file and then click Upload
						Report . |
| MAC Addresses
				  (Optional) | The MAC
					 addresses from the original servers that were upgraded. These MAC addresses can
					 be used to look up the licenses that were registered on those product
					 instances. |

| Step 1 | From the
			 Licenses > Fulfillment page in Cisco Prime License Manager, click Fulfillment
				  Options > Migrate Licenses . |
|---|---|
| Step 2 | The Migrate
			 Licenses to Cisco Prime License Manager wizard window appears. The first step
			 involves choosing the product type. From the Choose Product Type section,
			 select Unity
				Connection from the drop-down menu. The migration process is outlined in
			 this section, and is dependent on the type of product you select. Click Next . |
| Step 3 | The Choose
			 Product Instances section appears. To upgrade a product instance, select it in
			 the Available Product Instances window and click the arrow to move it to the
			 Product Instances to Migrate window. Click Next. |
| Step 4 | The License
			 Counts section appears. This section prompts you to choose between two options
			 relating to Cisco Unified Workshop Licenses (CUWL): Option Input I have CUWL licenses to be
				  migrated Click Next to move on to the Summary and Next Steps section. I do not have CUWL licenses
				  to be migrated. The
					 Licenses to be Migrated dialog box opens. From the table, you can reduce (but
					 not increase) your license counts in the Licenses to Migrate column. You may
					 also choose to run a compliance check by clicking the Run Compliance Check
					 button, or reset the license values by clicking the Reset Values button. Click OK to close the dialog box and then click Next to move on to the Summary and Next
					 Steps section. | Option | Input | I have CUWL licenses to be
				  migrated | Click Next to move on to the Summary and Next Steps section. | I do not have CUWL licenses
				  to be migrated. | The
					 Licenses to be Migrated dialog box opens. From the table, you can reduce (but
					 not increase) your license counts in the Licenses to Migrate column. You may
					 also choose to run a compliance check by clicking the Run Compliance Check
					 button, or reset the license values by clicking the Reset Values button. Click OK to close the dialog box and then click Next to move on to the Summary and Next
					 Steps section. |
| Option | Input |
| I have CUWL licenses to be
				  migrated | Click Next to move on to the Summary and Next Steps section. |
| I do not have CUWL licenses
				  to be migrated. | The
					 Licenses to be Migrated dialog box opens. From the table, you can reduce (but
					 not increase) your license counts in the Licenses to Migrate column. You may
					 also choose to run a compliance check by clicking the Run Compliance Check
					 button, or reset the license values by clicking the Reset Values button. Click OK to close the dialog box and then click Next to move on to the Summary and Next
					 Steps section. |
| Step 5 | The Summary
			 and Next Steps section appears. The option you selected in Step 4 determines
			 the information displayed in this section. Option Description I have CUWL licenses to be
				  migrated In this
					 section you must indicate how the upgrade was ordered: - Upgraded
					 using one or more service contracts -
					 Purchased the upgrade If you
					 select Upgraded using one or more service contracts, enter the UCSS/ESW
						Contract Numbers . If you
					 select Purchased the upgrade, enter the Sales
						Order Numbers . Enter
					 your Cisco user ID in the Cisco.com (CCO) User ID field. Company
					 Name and the field used to capture additional information are optional.
					 However; if you enter the company name, it is used in the subject line of the
					 email and is included in the name of the zip file. A
					 default name for the summary also appears in the Name field using the format
					 <productname>-migrate-<date-time-stamp> format. Instructions for
					 placing your order and fulfilling your licenses also appear in this section.
					 Click Finish
						& Generate Request . The
					 License Migration Request and Next Steps window appears. Download the License
					 Migration Request zip file to your PC. Email
					 the License Migration Request to Cisco licensing support using the link
					 provided. Click Close to return to the License Fulfillment page. I do not have CUWL
				  licenses to be migrated and e-Fulfillment is enabled Specify an optional
						description for the transaction. Read the end User License Agreement and select
						the check box to confirm. Click Finish and Generate . Enter your Cisco.com
						login and click OK . The request is
						electronically submitted, processed immediately, and your licenses are
						installed automatically. I do not have CUWL
				  licenses to be migrated and e-Fulfillment is disabled In this
					 section you can view and save a summary of the changes you made. To view the
					 summary, click View Summary. A default name for the summary also appears in the
					 Name field using the format <productname>-migrate-<date-time-stamp>
					 format. Instructions for placing your order and fulfilling your licenses also
					 appear in this section. Click Finish
						& Generate Request . The
					 License Migration Request and Next Steps window appears. Copy the selected text
					 to your clipboard or click Save
						it to a file on your computer . Select License Migration Portal under Step 2 and paste the copied
					 text in the designated field or select the saved file from your computer. Click Close to return to the License Fulfillment page. Note Only
					 e-Migration transactions are accessible on the License Fulfillment page. Since
					 this is a manual Migration, the migration plan is accessible only on the
					 License Planning page. | Option | Description | I have CUWL licenses to be
				  migrated | In this
					 section you must indicate how the upgrade was ordered: - Upgraded
					 using one or more service contracts -
					 Purchased the upgrade If you
					 select Upgraded using one or more service contracts, enter the UCSS/ESW
						Contract Numbers . If you
					 select Purchased the upgrade, enter the Sales
						Order Numbers . Enter
					 your Cisco user ID in the Cisco.com (CCO) User ID field. Company
					 Name and the field used to capture additional information are optional.
					 However; if you enter the company name, it is used in the subject line of the
					 email and is included in the name of the zip file. A
					 default name for the summary also appears in the Name field using the format
					 <productname>-migrate-<date-time-stamp> format. Instructions for
					 placing your order and fulfilling your licenses also appear in this section.
					 Click Finish
						& Generate Request . The
					 License Migration Request and Next Steps window appears. Download the License
					 Migration Request zip file to your PC. Email
					 the License Migration Request to Cisco licensing support using the link
					 provided. Click Close to return to the License Fulfillment page. | I do not have CUWL
				  licenses to be migrated and e-Fulfillment is enabled | Specify an optional
						description for the transaction. Read the end User License Agreement and select
						the check box to confirm. Click Finish and Generate . Enter your Cisco.com
						login and click OK . The request is
						electronically submitted, processed immediately, and your licenses are
						installed automatically. | I do not have CUWL
				  licenses to be migrated and e-Fulfillment is disabled | In this
					 section you can view and save a summary of the changes you made. To view the
					 summary, click View Summary. A default name for the summary also appears in the
					 Name field using the format <productname>-migrate-<date-time-stamp>
					 format. Instructions for placing your order and fulfilling your licenses also
					 appear in this section. Click Finish
						& Generate Request . The
					 License Migration Request and Next Steps window appears. Copy the selected text
					 to your clipboard or click Save
						it to a file on your computer . Select License Migration Portal under Step 2 and paste the copied
					 text in the designated field or select the saved file from your computer. Click Close to return to the License Fulfillment page. Note Only
					 e-Migration transactions are accessible on the License Fulfillment page. Since
					 this is a manual Migration, the migration plan is accessible only on the
					 License Planning page. | Note | Only
					 e-Migration transactions are accessible on the License Fulfillment page. Since
					 this is a manual Migration, the migration plan is accessible only on the
					 License Planning page. |
| Option | Description |
| I have CUWL licenses to be
				  migrated | In this
					 section you must indicate how the upgrade was ordered: - Upgraded
					 using one or more service contracts -
					 Purchased the upgrade If you
					 select Upgraded using one or more service contracts, enter the UCSS/ESW
						Contract Numbers . If you
					 select Purchased the upgrade, enter the Sales
						Order Numbers . Enter
					 your Cisco user ID in the Cisco.com (CCO) User ID field. Company
					 Name and the field used to capture additional information are optional.
					 However; if you enter the company name, it is used in the subject line of the
					 email and is included in the name of the zip file. A
					 default name for the summary also appears in the Name field using the format
					 <productname>-migrate-<date-time-stamp> format. Instructions for
					 placing your order and fulfilling your licenses also appear in this section.
					 Click Finish
						& Generate Request . The
					 License Migration Request and Next Steps window appears. Download the License
					 Migration Request zip file to your PC. Email
					 the License Migration Request to Cisco licensing support using the link
					 provided. Click Close to return to the License Fulfillment page. |
| I do not have CUWL
				  licenses to be migrated and e-Fulfillment is enabled | Specify an optional
						description for the transaction. Read the end User License Agreement and select
						the check box to confirm. Click Finish and Generate . Enter your Cisco.com
						login and click OK . The request is
						electronically submitted, processed immediately, and your licenses are
						installed automatically. |
| I do not have CUWL
				  licenses to be migrated and e-Fulfillment is disabled | In this
					 section you can view and save a summary of the changes you made. To view the
					 summary, click View Summary. A default name for the summary also appears in the
					 Name field using the format <productname>-migrate-<date-time-stamp>
					 format. Instructions for placing your order and fulfilling your licenses also
					 appear in this section. Click Finish
						& Generate Request . The
					 License Migration Request and Next Steps window appears. Copy the selected text
					 to your clipboard or click Save
						it to a file on your computer . Select License Migration Portal under Step 2 and paste the copied
					 text in the designated field or select the saved file from your computer. Click Close to return to the License Fulfillment page. Note Only
					 e-Migration transactions are accessible on the License Fulfillment page. Since
					 this is a manual Migration, the migration plan is accessible only on the
					 License Planning page. | Note | Only
					 e-Migration transactions are accessible on the License Fulfillment page. Since
					 this is a manual Migration, the migration plan is accessible only on the
					 License Planning page. |
| Note | Only
					 e-Migration transactions are accessible on the License Fulfillment page. Since
					 this is a manual Migration, the migration plan is accessible only on the
					 License Planning page. |

| Option | Input |
|---|---|
| I have CUWL licenses to be
				  migrated | Click Next to move on to the Summary and Next Steps section. |
| I do not have CUWL licenses
				  to be migrated. | The
					 Licenses to be Migrated dialog box opens. From the table, you can reduce (but
					 not increase) your license counts in the Licenses to Migrate column. You may
					 also choose to run a compliance check by clicking the Run Compliance Check
					 button, or reset the license values by clicking the Reset Values button. Click OK to close the dialog box and then click Next to move on to the Summary and Next
					 Steps section. |

| Option | Description |
|---|---|
| I have CUWL licenses to be
				  migrated | In this
					 section you must indicate how the upgrade was ordered: - Upgraded
					 using one or more service contracts -
					 Purchased the upgrade If you
					 select Upgraded using one or more service contracts, enter the UCSS/ESW
						Contract Numbers . If you
					 select Purchased the upgrade, enter the Sales
						Order Numbers . Enter
					 your Cisco user ID in the Cisco.com (CCO) User ID field. Company
					 Name and the field used to capture additional information are optional.
					 However; if you enter the company name, it is used in the subject line of the
					 email and is included in the name of the zip file. A
					 default name for the summary also appears in the Name field using the format
					 <productname>-migrate-<date-time-stamp> format. Instructions for
					 placing your order and fulfilling your licenses also appear in this section.
					 Click Finish
						& Generate Request . The
					 License Migration Request and Next Steps window appears. Download the License
					 Migration Request zip file to your PC. Email
					 the License Migration Request to Cisco licensing support using the link
					 provided. Click Close to return to the License Fulfillment page. |
| I do not have CUWL
				  licenses to be migrated and e-Fulfillment is enabled | Specify an optional
						description for the transaction. Read the end User License Agreement and select
						the check box to confirm. Click Finish and Generate . Enter your Cisco.com
						login and click OK . The request is
						electronically submitted, processed immediately, and your licenses are
						installed automatically. |
| I do not have CUWL
				  licenses to be migrated and e-Fulfillment is disabled | In this
					 section you can view and save a summary of the changes you made. To view the
					 summary, click View Summary. A default name for the summary also appears in the
					 Name field using the format <productname>-migrate-<date-time-stamp>
					 format. Instructions for placing your order and fulfilling your licenses also
					 appear in this section. Click Finish
						& Generate Request . The
					 License Migration Request and Next Steps window appears. Copy the selected text
					 to your clipboard or click Save
						it to a file on your computer . Select License Migration Portal under Step 2 and paste the copied
					 text in the designated field or select the saved file from your computer. Click Close to return to the License Fulfillment page. Note Only
					 e-Migration transactions are accessible on the License Fulfillment page. Since
					 this is a manual Migration, the migration plan is accessible only on the
					 License Planning page. | Note | Only
					 e-Migration transactions are accessible on the License Fulfillment page. Since
					 this is a manual Migration, the migration plan is accessible only on the
					 License Planning page. |
| Note | Only
					 e-Migration transactions are accessible on the License Fulfillment page. Since
					 this is a manual Migration, the migration plan is accessible only on the
					 License Planning page. |

| Note | Only
					 e-Migration transactions are accessible on the License Fulfillment page. Since
					 this is a manual Migration, the migration plan is accessible only on the
					 License Planning page. |
|---|---|

| Step 1 | From the
			 Licenses > Fulfillment page in Cisco Prime License Manager, click Fulfillment
				  Options > Migrate Licenses . |
|---|---|
| Step 2 | The Migrate
			 Licenses to Cisco Prime License Manager wizard window appears. The first step
			 involves choosing the product type. From the Choose Product Type section,
			 select the type of product to upgrade and the version from the drop-down menus.
			 Click Next . |
| Step 3 | The Choose
			 Product Instances section appears. Check the checkbox next to Show
				additional Unified CM product instances . Selecting this option allows you
			 to view products without prior version data. |
| Step 4 | To migrate a
			 product instance, select it in the Available Product Instances window and click
			 the arrow to move it to the Product Instances to Migrate window. Click Next . |
| Step 5 | The
			 Additional Information Will Be Required window appears. Once you have read the
			 contents of the window, click Continue to close the window. |
| Step 6 | The License
			 Counts section appears. Enter the following information The number of public space
				phones in the Public Space Phones field Case Numbers License Count Utility
				Reports - select the zip file using the Upload Report button The MAC address in the MAC
				Addresses field Click Next . |
| Step 7 | The License
			 Migration Request and Next Steps window appears. Download the License Migration
			 Request zip file to your PC. |
| Step 8 | Email the
			 License Migration Request to Cisco licensing support using the link provided. |
| Step 9 | Click Close to
			 return to the License Planning page. |

| Step 1 | From the Licenses > Planning page, click Create an Add
				Licenses Plan . The Create an
			 Add Licenses Plan wizard window appears. |
|---|---|
| Step 2 | From the Choose Product section, choose the product type and license version of the product to
			 which you will be adding a licence. Click Next . |
| Step 3 | From the License
			 Counts section, adjust the number of licenses that
			 will be allocated to each type of license and click Save to
			 save your changes for that license type. You may also choose to run a
			 compliance check by clicking Run Compliance Check , or reset the
			 license values by clicking Reset Values . After the number of licenses
			 has been set, click Next . Clicking the
				arrow next to each license type reveals additional information about that license
				type. A window appears to indicate
			 whether the compliance check passed or failed. |
| Step 4 | If your compliance check fails,
			 you can return to License Counts to make additional changes. If the compliance
			 check passed, click Continue to move to the next section. |
| Step 5 | In Summary
			 and Next Steps section,  you can view and save a summary
			 of the changes you made. You can also enter your own summary name and
			 description. |
| Step 6 | To view the
			 summary, click View
				Summary . The Save Summary in Cisco Prime License Manager option is selected by
			 default. A default name for the summary also appears in the Name field using
			 the format <product-type>-add-<date-time-stamp> format.
			 Instructions for placing your order and fulfilling your licenses also appear in
			 this section. |
| Step 7 | Click Finish |

| Step 1 | From the
			 Cisco Prime License Manager main menu, select Licenses >
				Fulfillment . The License Fulfillment page opens. |
|---|---|
| Step 2 | In
			 eFulfillment mode, click Fulfill
				Licenses from PAK . The Fulfill Licenses from PAK window appears. |
| Step 3 | Choose the Add licenses
				from a new PAK option and enter the Product Authorization Key (PAK) code. If you have
			 previously entered PAKs in Cisco Prime License Manager , you may select the second
			 option, "Add licenses from an already-installed PAK that supports partial
			 fulfillment". After you have chosen that option, select the existing PAK code
			 from the drop-down menu. |
| Step 4 | Click Next . |
| Step 5 | If prompted for your Cisco.com account information, enter the username
			 and password you entered when you registered at Cisco.com. |
| Step 6 | Click OK . If there are licenses remaining to be fulfilled (and the PAK username and password are validated), the Fulfill Licenses section appears. |
| Step 7 | The licenses
			 within the PAK are listed by SKU name. The numbers of each license are
			 categorized under a number of headings to indicate how many have been fulfilled
			 and how many are remaining. You can
			 specify the number of licenses you want to fulfill by selecting Fulfill in
			 the Actions column for that license type. The Fulfill Licenses window appears.
			 In this window you can specify the count in the Fulfill column, and click Save , then
			 click OK to
			 close the window. The updated count now appears in the Fulfill column of the
			 Fulfill Licenses table. Important: Some PAKs are not eligible for partial fulfillment. These PAKs
				  are packaged together, so they can only be fulfilled at a single Cisco Prime
				  License Manager. For example, an NFR (not-for-resale) order is sold as a
				  package with 20 CUWL Pro Unified CM and Unity Connection licenses and five
				  TelePresence Room licenses. Note If
				  licenses are listed as "Fulfilled" (under "Before Fulfillment" in the Fulfill
				  Licenses table), those licenses have been fulfilled by this or another Cisco Prime License Manager . Note Once you
				  have fulfilled your licenses as selected, you may wish to Run
					 Compliance Check to ensure that you are in compliance. | Note | If
				  licenses are listed as "Fulfilled" (under "Before Fulfillment" in the Fulfill
				  Licenses table), those licenses have been fulfilled by this or another Cisco Prime License Manager . | Note | Once you
				  have fulfilled your licenses as selected, you may wish to Run
					 Compliance Check to ensure that you are in compliance. |
| Note | If
				  licenses are listed as "Fulfilled" (under "Before Fulfillment" in the Fulfill
				  Licenses table), those licenses have been fulfilled by this or another Cisco Prime License Manager . |
| Note | Once you
				  have fulfilled your licenses as selected, you may wish to Run
					 Compliance Check to ensure that you are in compliance. |
| Step 8 | Click Next to review your changes. If you are not satisfied with your changes,
			 click Previous to return to the Fulfill Licenses section. If you are satisfied with the
			 changes, click Next to
			 move to the next section. |
| Step 9 | Click Next in the Fulfill Licenses section. |
| Step 10 | In the Transaction Options and License
			 Agreement section, you may enter a description (optional). You
			 may also associate this transaction with a saved license summary by selecting
			 that option and then selecting the name of the license summary from the
			 drop-down list. |
| Step 11 | Indicate that you accept the conditions of the End User License Agreement. |
| Step 12 | Click Finish . Upon
			 successful completion of the e-Fulfillment process, the new fulfillment appears
			 in the License Fulfillment table. |

| Note | If
				  licenses are listed as "Fulfilled" (under "Before Fulfillment" in the Fulfill
				  Licenses table), those licenses have been fulfilled by this or another Cisco Prime License Manager . |
|---|---|

| Note | Once you
				  have fulfilled your licenses as selected, you may wish to Run
					 Compliance Check to ensure that you are in compliance. |
|---|---|

| Note | The content of
		  the PAK determines whether a license can be upgraded by feature or version. |
|---|---|

| Step 1 | From the
			 Cisco Prime License Manager main menu, select Licenses >
				Fulfillment . The License Fulfillment page opens. |
|---|---|
| Step 2 | In
			 eFulfillment mode, click the Fulfill
				Licenses from PAK button. The Fulfill Licenses from PAK window appears. |
| Step 3 | Select the Add licenses
				from a new PAK option and enter the Product Authorization Key (PAK) code. If you have
			 previously entered PAKs in Cisco Prime License Manager , you may select the second
			 option, "Add licenses from an already-installed PAK that supports partial
			 fulfillment". Once you have selected that option, select the existing PAK code
			 from the drop-down menu. |
| Step 4 | Click the Next button. If prompted for your Cisco.com account information, enter the username
			 and password you entered when you registered at Cisco.com. |
| Step 5 | Click the Ok button.
			 If there are licenses remaining to be fulfilled (and the PAK username and
			 password are validated), the Fulfill Licenses section appears. |
| Step 6 | The licenses
			 within the PAK are listed by SKU name. The numbers of each license are
			 categorized under a number of headings to indicate how many have been fulfilled
			 and how many are remaining. You can
			 specify the number of licenses you want to fulfill by selecting Fulfill in
			 the Actions column for that license type. The Fulfill Licenses window appears.
			 In this window you can specify the license version, feature, or both, and click Save then
			 click OK to
			 close the window. The updated count now appears in the Fulfill column of the
			 Fulfill Licenses table. Important: Some PAKs are not eligible for partial fulfillment. These PAKs
				  are packaged together, so they can only be fulfilled at a single Cisco Prime
				  License Manager. For example, an NFR (not-for-resale) order is sold as a
				  package with 20 CUWL Pro Unified CM and Unity Connection licenses and five
				  TelePresence Room licenses. Note If
				  licenses are listed as "Fulfilled" (under "Before Fulfillment" in the Fulfill
				  Licenses table), those licenses have been fulfilled by this or another Cisco Prime License Manager . Note Once you
				  have fulfilled your licenses as selected, you may wish to click the Run
					 Compliance Check button to ensure that you are in compliance. | Note | If
				  licenses are listed as "Fulfilled" (under "Before Fulfillment" in the Fulfill
				  Licenses table), those licenses have been fulfilled by this or another Cisco Prime License Manager . | Note | Once you
				  have fulfilled your licenses as selected, you may wish to click the Run
					 Compliance Check button to ensure that you are in compliance. |
| Note | If
				  licenses are listed as "Fulfilled" (under "Before Fulfillment" in the Fulfill
				  Licenses table), those licenses have been fulfilled by this or another Cisco Prime License Manager . |
| Note | Once you
				  have fulfilled your licenses as selected, you may wish to click the Run
					 Compliance Check button to ensure that you are in compliance. |
| Step 7 | Click the Next button to review your changes. If you are not satisfied with your changes,
			 click Previous to return to the Fulfill Licenses section. If you are satisfied with the
			 changes, click Next to
			 move to the next section. |
| Step 8 | Clicking Next
			 in the Fulfill Licenses section opens the Transaction Options and License
			 Agreement section. In this section, you may enter a description (optional). You
			 may also associate this transaction with a saved license summary by selecting
			 that option and then selecting the name of the license summary from the
			 drop-down list. |
| Step 9 | Select the
			 checkbox to accept the conditions of the End User License Agreement. |
| Step 10 | Click the Finish button. |
| Step 11 | Upon
			 successful completion of the e-Fulfillment process, the new fulfillment appears
			 in the License Fulfillment table. |

| Note | If
				  licenses are listed as "Fulfilled" (under "Before Fulfillment" in the Fulfill
				  Licenses table), those licenses have been fulfilled by this or another Cisco Prime License Manager . |
|---|---|

| Note | Once you
				  have fulfilled your licenses as selected, you may wish to click the Run
					 Compliance Check button to ensure that you are in compliance. |
|---|---|