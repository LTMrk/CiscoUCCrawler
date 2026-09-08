---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-11-5-1-su5-userguide-cplm-b-userguide-1151-su5-cplm-b-userguide-115-bdfb59c53b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/11_5_1_SU5/userguide/CPLM_b_userguide_1151_SU5/CPLM_b_userguide_1151_SU5_chapter_0101.html
retrieved_at: 2026-09-08T04:54:38.420361+00:00
---

Cisco Prime License Manager User Guide, Release 11.5(1)SU5

# Cisco Prime License Manager User Guide, Release 11.5(1)SU5

Updated: June 27, 2018

Chapter: License Management

## Chapter: License Management

# License Management

## Introduction

Determine
                                       				licensing requirements for your product. See License View Settings.

Migrate your
                                       				existing licenses if your Cisco Prime License Manager manages upgraded product
                                       				instances that implement a different licensing methodology. See Migrate Licenses to Cisco Prime License Manager .

Perform new
                                       				license fulfillment. See Create a License Plan .

## Create a License
                        	 Plan

Use the following
                              		  procedure to plan the addition of new licenses.

From the Licenses > Planning window in Cisco Prime License Manager, click Create an Add
                                          				Licenses Plan .

From the Choose
                                          				Product section, select the product type and license version of the
                                       			 product to which you will be adding a licence. Click Next .

From the License Counts section, adjust the number of
                                       			 licenses that will be allocated to each type of license and click Save to
                                       			 save your changes for that license type. You may also choose to run a
                                       			 compliance check by clicking Run
                                          				Compliance Check , or reset the license values by clicking Reset
                                          				Values . After the number of licenses has been set, click Next .

Clicking the
                                          				arrow next to each license type reveals additional information about that
                                          				license type.

If your
                                       			 compliance check fails, you can return to License Counts to make additional changes. If the
                                       			 compliance check passes, click Next to move to the next section.

In Summary and Next Steps section, you can view and
                                       			 save a summary of the changes you made. You can also enter your own summary
                                       			 name and description.

To view the
                                       			 summary, click View
                                          				Summary . The Save
                                          				Summary in Cisco Prime License Manager option is
                                       			 selected by default. A default name for the summary also appears in the Name field using the format
                                       			 <product-type>-add-<date-time-stamp> format. Instructions for
                                       			 placing your order and fulfilling your licenses also appear in this section.

Click Finish

### What to do next

Place your order : Purchase your licenses or use your service contract to get a
                                    				PAK.

Fulfill your licenses :
                                    				Enter your PAK into the License Fulfillment screen of Cisco Prime License
                                    				Manager and, through the e-Fulfillment process, fulfill your licenses. Cisco
                                    				Prime License Manager communicates with Cisco licensing servers and your new
                                    				licenses will be installed and ready to use.

## Use Electronic
                        	 Fulfillment to Add Licenses

Complete the
                              		  following procedure to electronically fulfill your licenses.

### Before you begin

Create a licenses
                              		  plan.

From the
                                       			 Cisco Prime License Manager main menu, choose Licenses > Fulfillment .

In
                                       			 eFulfillment mode, click Fulfill
                                          				Licenses from PAK .

Choose Add licenses
                                          				from a new PAK and enter the Product Authorization Key (PAK) code.

Click Next .

If prompted
                                       			 for your Cisco.com account information, enter the username and password you
                                       			 entered when you registered at Cisco.com.

Click OK .

The licenses
                                       			 within the PAK are listed by SKU name. The numbers of each license are
                                       			 categorized under a number of headings to indicate how many have been fulfilled
                                       			 and how many are remaining.

Specify the
                                       			 count in the Fulfill column, and click Save

Click OK to
                                       			 close the window.

After you
                                       			 have fulfilled your licenses, you may choose to Run
                                          				Compliance Check to ensure that you are in compliance.

Click Next to
                                       			 review your changes. If you are not satisfied with your changes, click Previous to return to the Fulfill Licenses section.

If you are
                                       			 satisfied with your changes, click Next in the Fulfill Licenses section.

In the Transaction Options and License Agreement section,
                                       			 enter a description (optional). You can associate this transaction with a saved
                                       			 license summary by selecting that option and then selecting the name of the
                                       			 license summary from the drop-down list.

Indicate that
                                       			 you accept the conditions of the End
                                          				User License Agreement .

Click Finish .

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

From the
                                       			 Cisco Prime License Manager main menu, select Licenses > Fulfillment .

In
                                       			 eFulfillment mode, click Fulfill
                                          				Licenses from PAK .

Select Add licenses
                                          				from a new PAK and enter the Product Authorization Key (PAK) code.

Click Next . If prompted for your Cisco.com account information, enter the username
                                       			 and password you entered when you registered at Cisco.com.

Click OK .

If there are licenses remaining to be fulfilled (and the PAK username and
                                          			 password are validated), the Fulfill Licenses section appears.

Licenses can only be fulfilled using the cisco.com account to which they were initially issued.

The licenses
                                       			 within the PAK are listed by SKU name. The numbers of each license are
                                       			 categorized under a number of headings to indicate how many have been fulfilled
                                       			 and how many are remaining.

Click Next to review your changes. If you are not satisfied with your changes,
                                       			 click Previous to return to the Fulfill Licenses section. If you are satisfied with the
                                       			 changes, click Next to
                                       			 move to the next section.

Click Next in the Fulfill Licenses section opens the Transaction Options and License
                                       			 Agreement section. In this section, you may enter a description (optional). You
                                       			 may also associate this transaction with a saved license summary by selecting
                                       			 that option and then selecting the name of the license summary from the
                                       			 drop-down list.

Select the
                                       			 checkbox to accept the conditions of the End User License Agreement.

Click Finish .

## Other Fulfillment
                        	 Options

Next to the
                              		  Fulfill Licenses from the PAK option on the License
                                 			 Fulfillment page, there is another option entitled Other
                                 			 Fulfillment Options .

In Manual
                              		  Fulfillment mode, selecting the drop-down arrow under this option reveals only
                              		  one option: Generate License Request.

In eFulfillment
                              		  mode, selecting the drop-down arrow under this option reveals three options:

- Fulfill Licenses from File

- Generate License Request

- Retrieve Fulfilled Licenses

### Fulfill
                              		  Licenses from File

To fulfill
                              		  licenses from a file on your computer:

- Select Other Fulfillment
                                       				  Options > Fulfill Licenses from File .

- The Install License File
                                 			 window opens. Click the Browse button to locate the file on your computer.
                                 			 Select the file and click Open .

- You can add a description
                                 			 and associate the transaction with a saved license plan (optional).

- Click the Install button to install the license file.

### Generate
                              		  License Request

To obtain a new
                              		  license (using Manual fulfillment) generate a license request through the Licenses > Fulfillment page, and then use the
                              		  information generated to submit a request. You receive your license file
                              		  through email. Use the following procedure to generate a license request.

- Log in to Cisco Prime License Manager .

- From the Licenses > Fulfillment window, select Generate License Request from the drop-down list
                                 			 under Other Fulfillment Options.

- Copy the selected text to
                                 			 your clipboard or click Save
                                    				it to a file on your PC .

### Retrieve
                              		  Fulfilled Licenses

The Retrieve
                                 			 Fulfilled Licenses option is exclusive to e-Fulfillment. This
                              		  feature connects to the Cisco licensing servers to retrieve and install the
                              		  licenses that have been fulfilled for this Cisco
                                 			 Prime License Manager . This feature is useful if you wish to
                              		  synchronize your Cisco
                                 			 Prime License Manager with the Cisco back office regarding licenses
                              		  that have been fulfilled.

Use the following
                              		  procedure to retrieve fulfilled licenses:

Log in to Cisco Prime License Manager .

Select Licenses > Fulfillment .

If not
                                    				already selected, click the Enable button to enable e-Fulfillment.

Under Other
                                    				Fulfillment Options, select Retrieve Fulfilled Licenses . The Retrieve Fulfilled
                                    				Licenses window appears.

Enter your
                                    				Cisco Username and Password. You can add a description (optional) in the
                                    				Transaction Description field.

Click the Retrieve and Install Licenses button.

Your Cisco
                                       				  Prime License Manager is synchronized with the Cisco back office and
                                    				all licenses currently fulfilled are installed.

## Encryption
                        	 License

Unified Communications Manager release 11.5(1)SU3 onwards require Encryption License to turn mixed mode on. The Encryption
                              License can be installed on Prime License Manager 11.5(1)SU2 onwards. Encryption License can be fulfilled  either by eFulfillment
                              mode or Manual Fulfillment mode.

For more details
                              		  on eFulfillment, see Upgrade Existing Licenses and for Manual Fulfillment, see Generate License Request sections of this chapter.

## License
                        	 Rehost

Licenses are fulfilled to a specific Cisco Prime License Manger. If you require licenses to be moved to a new Cisco Prime
                              License Manager, they are to be rehosted.

A rehost may be
                              		  required if:

- A hardware failure occurred and new hardware is required for Cisco Prime License Manager.

- Multiple Cisco Prime License Managers are desired and a subset of fulfillment licenses are to be moved to a new Cisco Prime
                                 License Manager.

License rehosts
                              		  or transfers can be requested at www.cisco.com/go/license and do not require Global
                              		  Licensing Operations (GLO) support.

Perform a rehost, the license registration ID from the source machine and the license request or license registration ID from
                              the target machine is required.

Use the following
                              		  procedure to perform a license rehost.

From Product License Registration ( www.cisco.com/go/license ), select Devices .

Under the Devices tab of a particular device, select one or more licenses that you want to rehost.

In the pop-up that appears, select Rehost/Transfer .

In the Quantity to Assign field, enter the
                                       			 number of licenses you want to transfer.

In the License Request field, enter the License Request from the Cisco Prime License Manager of the target device.

Click Next .

In the Review screen, review your selections.

Enter your email address, select your name
                                       			 from the drop-down list next to End User , and indicate that you agree with the Terms of the License.

Click Submit .

The rehosted license is emailed to you. Manually install it on the target Cisco Prime License Manager.

## Migrate Licenses
                        	 to Cisco Prime License Manager

When you upgrade a product instance from 8.x and earlier to 9.x and later, you must manually migrate your licenses. With the
                              assistance of the Global Licensing Organization (GLO), you must convert licensing from the old paradigm to the new paradigm.
                              For example, you can transfer licenses from Cisco Unified Communications Manager Release 8.x and older to Release 9.x and
                              later.

This section
                              		  describes the different migration paths you can follow using Cisco Prime
                              		  License Manager. 
                              		Cisco Emergency Responder, Cisco Unified Communications Manager, and Cisco Unity Connection each have their own migration
                              paths.

The migration
                                          		  path you follow depends upon a number of factors (for example: the product
                                          		  type, whether servers contain data from a previous version, and so on). The following
                                          		  flow charts provide a guide for the decisions that must be made to successfully
                                          		  complete your migration. For a broader view of the migration process, see the
                                          		  release notes for the product instance in question.

Use the
                              		  following procedure to plan for migration of product instances whose licenses
                              		  have not yet been migrated to Cisco Prime License Manager.

### Cisco Emergency Responder Migration Path

The following flow chart will aid you in migrating Cisco Emergency Responder licenses to Cisco Prime License Manager:

#### Cisco Emergency Responder
                              	 Migration Path with E-Fulfillment Enabled

The term Standard Migration refers specifically to Cisco Emergency Responder. Cisco Unified Communications Manager and Cisco
                                    Unity Connection have their own unique migration paths and are documented separately.

Use the following
                                    		  procedure to plan for migration of product instances whose licenses have not
                                    		  yet been migrated to Cisco Prime License Manager if e-Fulfillment is enabled.

From the Licenses > Fulfillment window in Cisco Prime License Manager, select Fulfillment
                                                   				  Options > Migrate Licenses .

From the Choose Product Type section,
                                             			 select the type of product to upgrade from the drop-down menu and click Next .

From the New License Version section, select the version of the product to which you are migrating licenses.

From the Available Product Instances window, select a product instance and click the arrow to move it to the Product Instances to Migrate window.

Click Next .

From the table, you can reduce (but not
                                             			 increase) your license counts in the Licenses to Migrate column. You may also
                                             			 choose to run a compliance check by clicking Run Compliance Check ,
                                             			 or reset the license values by clicking Reset Values . Click OK to
                                             			 close the dialog box and then click Next to move on to the Summary and Next
                                                			 Steps section.

Specify an
                                             			 optional description for the transaction. Read the End User License Agreement
                                             			 and click Finish &
                                                				Generate Request .

Enter your
                                             			 Cisco user ID in the Cisco.com
                                                				(CCO) User ID field.

#### Cisco Emergency Responder Migration Path with E-Fulfillment Disabled

The term Standard Migration refers specifically to Cisco Emergency Responder. Cisco Unified Communications Manager and Cisco
                                    Unity Connection have their own unique migration paths and are documented separately.

Use the following
                                    		  procedure to plan for migration of product instances whose licenses have not
                                    		  yet been migrated to Cisco Prime License Manager if e-Fulfillment is disabled.

From the Licenses > Fulfillment window in Cisco Prime License Manager, select Fulfillment
                                                   				  Options > Migrate Licenses .

From the Choose Product Type section,
                                             			 select the type of product to upgrade from the drop-down menu and click Next .

From the New License Version section, select the version of the product to which you are migrating licenses.

In
                                             			 the Available Product Instances window, select a product instance and click the arrow to move it to the Product Instances to Migrate window.

Click Next

From the table, you can reduce (but not
                                             			 increase) your license counts in the Licenses to Migrate column. You may also
                                             			 choose to run a compliance check by clicking the Run Compliance Check button,
                                             			 or reset the license values by clicking the Reset Values button. Click OK to
                                             			 close the dialog box and then click Next to move on to the Summary and Next
                                                			 Steps section.

In the Summary
                                             			 and Next Steps section, you can view and save a summary
                                             			 of the changes you made. To view the summary, click View Summary . A default
                                             			 name for the summary also appears in the Name field using the format
                                             			 <productname>-migrate-<date-time-stamp> format. Instructions for
                                             			 placing your order and fulfilling your licenses also appear in this section.
                                             			 Click Finish &
                                                				Generate Request .

Copy the selected text to your
                                             			 clipboard or click Save it to a
                                                				file on your computer .

Select License
                                                				Migration Portal under Step 2 and paste the copied text in the designated
                                             			 field or select the saved file from your computer.

Click Close to
                                             			 return to the License Fulfillment page.

### Cisco Unified
                           	 Communications Manager Migration Path

The following flow
                                 		  chart will aid you in migrating Cisco Unified Communications Manager licenses
                                 		  to Cisco Prime License Manager:

Use the following
                                 		  procedure to plan for migration of all Unified Communication product instances
                                 		  whose licenses have not yet been migrated to Cisco Prime License Manager.

From the Licenses > Fulfilment window in Cisco Prime License Manager, select Fulfillment
                                                				  Options > Migrate Licenses .

In the Migrate
                                             			 Licenses to Cisco Prime License Manager wizard, select Unified CM from the drop-down menu in the Choose Product Type section.

From the New License Version section, select the version of the product to which you are migrating licenses.

The migration process is outlined in this section, and
                                             			 is dependent on the type of product you select.

Click Next .

To upgrade a product instance, select the product instance in
                                          			 the Available Product Instances window and click the arrow to move it to the Product Instances to Migrate window.

Click Next .

The Summary of Pre-Upgrade Product Instance Data table
                                          			 lists the product instances you selected in the previous step. This table
                                          			 cannot be edited. Below the table are a number of fields that require input:

An
                                                      					 estimate of the number of public space phones. Public space phones do not have
                                                      					 users assigned and are typically placed in shared workspaces, lobbies and
                                                      					 meeting rooms. These phones generally require lower level licenses, so
                                                      					 providing an estimate of the number of these phones in your deployment will
                                                      					 help Cisco more accurately determine your license requirements.

A case
                                                      					 number assigned if the report was sent to Cisco Licensing Support

Click Upload
                                                         						Report to open the Upload License Count Utility Report dialog box.
                                                      					 Click Browse to select the report file and then click Upload
                                                         						Report .

The MAC
                                                      					 addresses from the original servers that were upgraded. These MAC addresses will
                                                      					 be used to look up the licenses that were registered on those product
                                                      					 instances.

In this Summary
                                             			 and Next Steps section, indicate how the
                                          			 upgrade was ordered:

- Upgraded using one or more
                                             				service contracts

- Purchased the upgrade

Enter your
                                          			 Cisco user ID in the Cisco.com
                                             				(CCO) User ID field.

Company Name
                                             				and the field used to capture additional information are optional. However, if
                                             				you enter the company name, it is used in the subject line of the email and is
                                             				included in the name of the zip file.

A default name
                                             				for the summary also appears in the Name field using the format
                                             				<productname>-migrate-<date-time-stamp> format. Instructions for
                                             				placing your order and fulfilling your licenses also appear in this section.
                                             				Click Finish &
                                                				  Generate Request .

From the License
                                             			 Migration Request and Next Steps window, download the License Migration
                                          			 Request zip file to your computer.

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

From the Licenses > Fulfillment window in Cisco Prime License Manager, select Fulfillment
                                                				  Options > Migrate Licenses .

In the Migrate
                                             			 Licenses to Cisco Prime License Manager wizard, select Unity Connection from the drop-down menu in the Choose Product Type section.

From the New License Version section, select the version of the product to which you are migrating licenses.

The migration process is outlined in this section, and
                                             			 is dependent on the type of product you select.

Click Next .

To upgrade a product instance, select the product instance in
                                          			 the Available Product Instances window and click the arrow to move it to the Product Instances to Migrate window.

Click Next .

The License
                                             			 Counts section prompts you to select one of two options
                                          			 relating to Cisco Unified Workshop Licenses (CUWL):

Click Next to move on to the Summary and Next Steps section.

You can reduce (but
                                                      					 not increase) your license counts in the Licenses to Migrate column. You may
                                                      					 also choose to run a compliance check by clicking Run Compliance Check , or reset the license values by clicking Reset Values . Click OK to close the dialog box and then click Next to move on to the Summary and Next
                                                         					 Steps section.

The option you selected in Step 4 determines
                                          			 the information displayed in the Summary
                                             			 and Next Steps section.

In this
                                                      					 section you must indicate how the upgrade was ordered:

- Upgraded
                                                      					 using one or more service contracts

-
                                                      					 Purchased the upgrade

If you
                                                      					 select Upgraded using one or more service contracts, enter the 
                                                      					 UCSS/ESW
                                                      						Contract Numbers.

If you
                                                      					 select Purchased the upgrade, enter the 
                                                      					 Sales
                                                      						Order Numbers.

Enter
                                                      					 your Cisco user ID in the Cisco.com (CCO) User ID field.

Company
                                                      					 Name and the field used to capture additional information are optional.
                                                      					 However, if you enter the company name, it is used in the subject line of the
                                                      					 email and is included in the name of the zip file.

A
                                                      					 default name for the summary also appears in the Name field using the format
                                                      					 <productname>-migrate-<date-time-stamp> format. Instructions for
                                                      					 placing your order and fulfilling your licenses also appear in this section.
                                                      					 Click Finish
                                                         						& Generate Request .

From the License Migration Request and Next Steps window, download the License
                                                      					 Migration Request zip file to your computer.

Email
                                                      					 the License Migration Request to Cisco licensing support using the link
                                                      					 provided.

Click Close to return to the License Fulfillment window.

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
                                                      					 summary, click View Summary . A default name for the summary also appears in the Name field using the format <productname>-migrate-<date-time-stamp>
                                                      					 format. Instructions for placing your order and fulfilling your licenses also
                                                      					 appear in this section. Click Finish
                                                         						& Generate Request .

From the License Migration Request and Next Steps window, copy the selected text
                                                      					 to your clipboard or click Save
                                                         						it to a file on your computer .

Select License Migration Portal under Step 2 and paste the copied
                                                      					 text in the designated field or select the saved file from your computer.

Click Close to return to the License Fulfillment window.

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
                                 		  where a product is upgraded to 9.x, 10.x, or 11.x without running License Count Utility on a
                                 		  pre-9.x version. Please contact the Cisco licensing office and have the license
                                 		  file reissued if changes are required.

Fresh install with
                                    			 imported pre-9.x data

A migration may
                                 		  be required following a fresh install in situations where pre-9.0 DLU or
                                 		  license information is not available in Release 9.x, 10.x, or 11.x VM. This may occur when:

- UC Release 8.6 needs to be
                                    			 upgraded as a new VM, with phone data exported

- A new Release 9.x, 10.x, or 11.x VM is
                                    			 created, with phone data imported

The following
                                 		  procedure enables you to perform a migration after a fresh install. This
                                 		  procedure requires that an LCU report be run against pre-upgrade product
                                 		  instance, if still accessible, or that MAC addresses of the pre-upgrade product
                                 		  instances be available.

From the Licenses > Fulfillment window in Cisco Prime License Manager, click Fulfillment
                                                				  Options > Migrate Licenses .

In the Migrate
                                             			 Licenses to Cisco Prime License Manager wizard, select 
                                          			 the type of product to upgrade and the version from the drop-down menus
                                          			 in the Choose Product Type section. The migration process is outlined in this section, and
                                          			 is dependent on the type of product you select.

Click Next .

From the Choose
                                             			 Product Instances section appears,  check the checkbox next to Show
                                             				additional Unified CM product instances . Selecting this option allows you
                                          			 to view products without prior version data.

To migrate a
                                          			 product instance, select it in the Available Product Instances window and click
                                          			 the arrow to move it to the Product Instances to Migrate window. Click Next .

After you have read the
                                          			 contents of the Additional Information Will Be Required window, click Continue to close the window.

Enter the following information in the License
                                          			 Counts section:

- The number of public space
                                             				phones in the Public Space Phones field

- Case Numbers

- License Count Utility
                                             				Reports - select the zip file using the Upload Report button

- The MAC address in the MAC
                                             				Addresses field

Download the License Migration
                                          			 Request zip file to your computer.

Email the
                                          			 License Migration Request to Cisco licensing support using the link provided.

Click Close to
                                          			 return to the License Planning window.

### Licensing
                           	 Migration Support

Product licensing
                                 		  has a grace period from the time that users are configured on the system. For
                                 		  Cisco Unified Communications Manager and Unity Connection, the grace period is
                                 		  60 days.

The Global
                                 		  Licensing Operations (GLO) Team is available 24 x 7 x 365 and has knowledgeable
                                 		  agents that can help process your request and route it to the team best able to
                                 		  assist you. Expect a response within 48-72 hours.

- Open your service request
                                       			 through the web: https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case

- Open any service request
                                       			 through licensing@cisco.com (include Cisco.com user ID)

- Open a service request by
                                       			 telephone using country-specific numbers: http://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html

| Step 1 | From the Licenses > Planning window in Cisco Prime License Manager, click Create an Add
                                          				Licenses Plan . |
|---|---|
| Step 2 | From the Choose
                                          				Product section, select the product type and license version of the
                                       			 product to which you will be adding a licence. Click Next . |
| Step 3 | From the License Counts section, adjust the number of
                                       			 licenses that will be allocated to each type of license and click Save to
                                       			 save your changes for that license type. You may also choose to run a
                                       			 compliance check by clicking Run
                                          				Compliance Check , or reset the license values by clicking Reset
                                          				Values . After the number of licenses has been set, click Next . Clicking the
                                          				arrow next to each license type reveals additional information about that
                                          				license type. |
| Step 4 | If your
                                       			 compliance check fails, you can return to License Counts to make additional changes. If the
                                       			 compliance check passes, click Next to move to the next section. |
| Step 5 | In Summary and Next Steps section, you can view and
                                       			 save a summary of the changes you made. You can also enter your own summary
                                       			 name and description. |
| Step 6 | To view the
                                       			 summary, click View
                                          				Summary . The Save
                                          				Summary in Cisco Prime License Manager option is
                                       			 selected by default. A default name for the summary also appears in the Name field using the format
                                       			 <product-type>-add-<date-time-stamp> format. Instructions for
                                       			 placing your order and fulfilling your licenses also appear in this section. |
| Step 7 | Click Finish |

| Step 1 | From the
                                       			 Cisco Prime License Manager main menu, choose Licenses > Fulfillment . |
|---|---|
| Step 2 | In
                                       			 eFulfillment mode, click Fulfill
                                          				Licenses from PAK . |
| Step 3 | Choose Add licenses
                                          				from a new PAK and enter the Product Authorization Key (PAK) code. If you have
                                       			 previously entered PAKs in Cisco Prime License Manager , choose Add
                                          				licenses from an already-installed PAK that supports partial
                                          				fulfillment and select the existing PAK code from the drop-down
                                       			 list. |
| Step 4 | Click Next . |
| Step 5 | If prompted
                                       			 for your Cisco.com account information, enter the username and password you
                                       			 entered when you registered at Cisco.com. |
| Step 6 | Click OK . If
                                       			 there are licenses remaining to be fulfilled (and the PAK username and password
                                       			 are validated), the Fulfill Licenses section appears. |
| Step 7 | The licenses
                                       			 within the PAK are listed by SKU name. The numbers of each license are
                                       			 categorized under a number of headings to indicate how many have been fulfilled
                                       			 and how many are remaining. You can
                                       			 specify the number of licenses you want to fulfill by selecting Fulfill in
                                       			 the Actions column for that license type. The
                                       			 Fulfill Licenses window appears. |
| Step 8 | Specify the
                                       			 count in the Fulfill column, and click Save |
| Step 9 | Click OK to
                                       			 close the window. Important PAKs that are not eligible for partial fulfillment are packaged
                                                      				  together, so they can only be fulfilled at a single Cisco Prime License
                                                      				  Manager. For example, an NFR (not-for-resale) order is sold as a package with
                                                      				  20 CUWL Pro Cisco Unified Communications Manager and Unity Connection licenses
                                                      				  and five TelePresence Room licenses. The
                                       			 updated count now appears in the Fulfill column of the Fulfill Licenses table. | Important | PAKs that are not eligible for partial fulfillment are packaged
                                                      				  together, so they can only be fulfilled at a single Cisco Prime License
                                                      				  Manager. For example, an NFR (not-for-resale) order is sold as a package with
                                                      				  20 CUWL Pro Cisco Unified Communications Manager and Unity Connection licenses
                                                      				  and five TelePresence Room licenses. |
| Important | PAKs that are not eligible for partial fulfillment are packaged
                                                      				  together, so they can only be fulfilled at a single Cisco Prime License
                                                      				  Manager. For example, an NFR (not-for-resale) order is sold as a package with
                                                      				  20 CUWL Pro Cisco Unified Communications Manager and Unity Connection licenses
                                                      				  and five TelePresence Room licenses. |
| Step 10 | After you
                                       			 have fulfilled your licenses, you may choose to Run
                                          				Compliance Check to ensure that you are in compliance. |
| Step 11 | Click Next to
                                       			 review your changes. If you are not satisfied with your changes, click Previous to return to the Fulfill Licenses section. |
| Step 12 | If you are
                                       			 satisfied with your changes, click Next in the Fulfill Licenses section. |
| Step 13 | In the Transaction Options and License Agreement section,
                                       			 enter a description (optional). You can associate this transaction with a saved
                                       			 license summary by selecting that option and then selecting the name of the
                                       			 license summary from the drop-down list. |
| Step 14 | Indicate that
                                       			 you accept the conditions of the End
                                          				User License Agreement . |
| Step 15 | Click Finish . Upon
                                       			 successful completion of the e-Fulfillment process, the new fulfillment appears
                                       			 in the License Fulfillment table. |

| Important | PAKs that are not eligible for partial fulfillment are packaged
                                                      				  together, so they can only be fulfilled at a single Cisco Prime License
                                                      				  Manager. For example, an NFR (not-for-resale) order is sold as a package with
                                                      				  20 CUWL Pro Cisco Unified Communications Manager and Unity Connection licenses
                                                      				  and five TelePresence Room licenses. |
|---|---|

| Note | Upgrade licenses can only be used to convert currently installed licenses. |
|---|---|

| Step 1 | From the
                                       			 Cisco Prime License Manager main menu, select Licenses > Fulfillment . |
|---|---|
| Step 2 | In
                                       			 eFulfillment mode, click Fulfill
                                          				Licenses from PAK . |
| Step 3 | Select Add licenses
                                          				from a new PAK and enter the Product Authorization Key (PAK) code. If you have
                                       			 previously entered PAKs in Cisco Prime License Manager , you can select Add licenses from an already-installed PAK that supports partial
                                          			 fulfillment . After you have selected that option, select the existing PAK code
                                       			 from the drop-down menu. |
| Step 4 | Click Next . If prompted for your Cisco.com account information, enter the username
                                       			 and password you entered when you registered at Cisco.com. |
| Step 5 | Click OK . If there are licenses remaining to be fulfilled (and the PAK username and
                                          			 password are validated), the Fulfill Licenses section appears. Licenses can only be fulfilled using the cisco.com account to which they were initially issued. |
| Step 6 | The licenses
                                       			 within the PAK are listed by SKU name. The numbers of each license are
                                       			 categorized under a number of headings to indicate how many have been fulfilled
                                       			 and how many are remaining. You can
                                       			 specify the number of licenses you want to fulfill by selecting Fulfill in
                                       			 the Actions column for that license type. In the Fulfill Licenses window you can specify the license version, feature, or both, and click Save then
                                       			 click OK to
                                       			 close the window. The updated count now appears in the Fulfill column of the
                                       			 Fulfill Licenses table. Note Some PAKs are not eligible for partial fulfillment. These PAKs
                                                      				  are packaged together, so they can only be fulfilled at a single Cisco Prime
                                                      				  License Manager in a single transaction. For example, an NFR (not-for-resale) order is sold as a
                                                      				  package with 20 CUWL Pro Unified CM and Unity Connection licenses and five
                                                      				  TelePresence Room licenses. Note If
                                                      				  licenses are listed as "Fulfilled" (under "Before Fulfillment" in the Fulfill
                                                      				  Licenses table), those licenses have previously been fulfilled by this or another Cisco Prime License Manager . Note Once you
                                                      				  have fulfilled your licenses as selected, you may wish to click Run
                                                         					 Compliance Check to ensure that you are in compliance. | Note | Some PAKs are not eligible for partial fulfillment. These PAKs
                                                      				  are packaged together, so they can only be fulfilled at a single Cisco Prime
                                                      				  License Manager in a single transaction. For example, an NFR (not-for-resale) order is sold as a
                                                      				  package with 20 CUWL Pro Unified CM and Unity Connection licenses and five
                                                      				  TelePresence Room licenses. | Note | If
                                                      				  licenses are listed as "Fulfilled" (under "Before Fulfillment" in the Fulfill
                                                      				  Licenses table), those licenses have previously been fulfilled by this or another Cisco Prime License Manager . | Note | Once you
                                                      				  have fulfilled your licenses as selected, you may wish to click Run
                                                         					 Compliance Check to ensure that you are in compliance. |
| Note | Some PAKs are not eligible for partial fulfillment. These PAKs
                                                      				  are packaged together, so they can only be fulfilled at a single Cisco Prime
                                                      				  License Manager in a single transaction. For example, an NFR (not-for-resale) order is sold as a
                                                      				  package with 20 CUWL Pro Unified CM and Unity Connection licenses and five
                                                      				  TelePresence Room licenses. |
| Note | If
                                                      				  licenses are listed as "Fulfilled" (under "Before Fulfillment" in the Fulfill
                                                      				  Licenses table), those licenses have previously been fulfilled by this or another Cisco Prime License Manager . |
| Note | Once you
                                                      				  have fulfilled your licenses as selected, you may wish to click Run
                                                         					 Compliance Check to ensure that you are in compliance. |
| Step 7 | Click Next to review your changes. If you are not satisfied with your changes,
                                       			 click Previous to return to the Fulfill Licenses section. If you are satisfied with the
                                       			 changes, click Next to
                                       			 move to the next section. |
| Step 8 | Click Next in the Fulfill Licenses section opens the Transaction Options and License
                                       			 Agreement section. In this section, you may enter a description (optional). You
                                       			 may also associate this transaction with a saved license summary by selecting
                                       			 that option and then selecting the name of the license summary from the
                                       			 drop-down list. |
| Step 9 | Select the
                                       			 checkbox to accept the conditions of the End User License Agreement. |
| Step 10 | Click Finish . Upon
                                       			 successful completion of the e-Fulfillment process, the new fulfillment appears
                                       			 in the License Fulfillment table. |

| Note | Some PAKs are not eligible for partial fulfillment. These PAKs
                                                      				  are packaged together, so they can only be fulfilled at a single Cisco Prime
                                                      				  License Manager in a single transaction. For example, an NFR (not-for-resale) order is sold as a
                                                      				  package with 20 CUWL Pro Unified CM and Unity Connection licenses and five
                                                      				  TelePresence Room licenses. |
|---|---|

| Note | If
                                                      				  licenses are listed as "Fulfilled" (under "Before Fulfillment" in the Fulfill
                                                      				  Licenses table), those licenses have previously been fulfilled by this or another Cisco Prime License Manager . |
|---|---|

| Note | Once you
                                                      				  have fulfilled your licenses as selected, you may wish to click Run
                                                         					 Compliance Check to ensure that you are in compliance. |
|---|---|

| Remember | Once you have your license request information saved either to
                                       		  your clipboard or to your computer, access the Cisco License Registration site
                                       		  and paste it into the appropriate field. When you receive your license file
                                       		  through email, install your new license file in Cisco Prime License Manager using the Fulfill Licenses from File procedure. |
|---|---|

| Note | In order to use the rehost portal, you must use the same Cisco.com
                                       		  user ID that initially ordered or fulfilled the licenses. |
|---|---|

| Step 1 | From Product License Registration ( www.cisco.com/go/license ), select Devices . |
|---|---|
| Step 2 | Under the Devices tab of a particular device, select one or more licenses that you want to rehost. |
| Step 3 | In the pop-up that appears, select Rehost/Transfer . |
| Step 4 | In the Quantity to Assign field, enter the
                                       			 number of licenses you want to transfer. |
| Step 5 | In the License Request field, enter the License Request from the Cisco Prime License Manager of the target device. |
| Step 6 | Click Next . |
| Step 7 | In the Review screen, review your selections. |
| Step 8 | Enter your email address, select your name
                                       			 from the drop-down list next to End User , and indicate that you agree with the Terms of the License. |
| Step 9 | Click Submit . |
| Step 10 | The rehosted license is emailed to you. Manually install it on the target Cisco Prime License Manager. Note The license can also be downloaded to your machine by clicking Download Target on the License Request Status window and choosing the download location. | Note | The license can also be downloaded to your machine by clicking Download Target on the License Request Status window and choosing the download location. |
| Note | The license can also be downloaded to your machine by clicking Download Target on the License Request Status window and choosing the download location. |

| Note | The license can also be downloaded to your machine by clicking Download Target on the License Request Status window and choosing the download location. |
|---|---|

| Note | The migration
                                          		  path you follow depends upon a number of factors (for example: the product
                                          		  type, whether servers contain data from a previous version, and so on). The following
                                          		  flow charts provide a guide for the decisions that must be made to successfully
                                          		  complete your migration. For a broader view of the migration process, see the
                                          		  release notes for the product instance in question. |
|---|---|

| Note | If Cisco
                                       		  Prime License Manager is in demo mode, do not create multiple migration
                                       		  requests. Complete the first migration, including installation of the license,
                                       		  prior to initiating a second migration. If a migration request results in
                                       		  multiple license files, install all of them, in order, before proceeding. |
|---|---|

| Step 1 | From the Licenses > Fulfillment window in Cisco Prime License Manager, select Fulfillment
                                                   				  Options > Migrate Licenses . |
|---|---|
| Step 2 | From the Choose Product Type section,
                                             			 select the type of product to upgrade from the drop-down menu and click Next . |
| Step 3 | From the New License Version section, select the version of the product to which you are migrating licenses. |
| Step 4 | From the Available Product Instances window, select a product instance and click the arrow to move it to the Product Instances to Migrate window. Click Next . |
| Step 5 | From the table, you can reduce (but not
                                             			 increase) your license counts in the Licenses to Migrate column. You may also
                                             			 choose to run a compliance check by clicking Run Compliance Check ,
                                             			 or reset the license values by clicking Reset Values . Click OK to
                                             			 close the dialog box and then click Next to move on to the Summary and Next
                                                			 Steps section. |
| Step 6 | Specify an
                                             			 optional description for the transaction. Read the End User License Agreement
                                             			 and click Finish &
                                                				Generate Request . |
| Step 7 | Enter your
                                             			 Cisco user ID in the Cisco.com
                                                				(CCO) User ID field. The request
                                             			 is electronically submitted, and processed immediately. Your licenses are
                                             			 installed automatically. |

| Step 1 | From the Licenses > Fulfillment window in Cisco Prime License Manager, select Fulfillment
                                                   				  Options > Migrate Licenses . |
|---|---|
| Step 2 | From the Choose Product Type section,
                                             			 select the type of product to upgrade from the drop-down menu and click Next . |
| Step 3 | From the New License Version section, select the version of the product to which you are migrating licenses. |
| Step 4 | In
                                             			 the Available Product Instances window, select a product instance and click the arrow to move it to the Product Instances to Migrate window. Click Next |
| Step 5 | From the table, you can reduce (but not
                                             			 increase) your license counts in the Licenses to Migrate column. You may also
                                             			 choose to run a compliance check by clicking the Run Compliance Check button,
                                             			 or reset the license values by clicking the Reset Values button. Click OK to
                                             			 close the dialog box and then click Next to move on to the Summary and Next
                                                			 Steps section. |
| Step 6 | In the Summary
                                             			 and Next Steps section, you can view and save a summary
                                             			 of the changes you made. To view the summary, click View Summary . A default
                                             			 name for the summary also appears in the Name field using the format
                                             			 <productname>-migrate-<date-time-stamp> format. Instructions for
                                             			 placing your order and fulfilling your licenses also appear in this section.
                                             			 Click Finish &
                                                				Generate Request . |
| Step 7 | Copy the selected text to your
                                             			 clipboard or click Save it to a
                                                				file on your computer . |
| Step 8 | Select License
                                                				Migration Portal under Step 2 and paste the copied text in the designated
                                             			 field or select the saved file from your computer. |
| Step 9 | Click Close to
                                             			 return to the License Fulfillment page. |

| Step 1 | From the Licenses > Fulfilment window in Cisco Prime License Manager, select Fulfillment
                                                				  Options > Migrate Licenses . |
|---|---|
| Step 2 | In the Migrate
                                             			 Licenses to Cisco Prime License Manager wizard, select Unified CM from the drop-down menu in the Choose Product Type section. |
| Step 3 | From the New License Version section, select the version of the product to which you are migrating licenses. The migration process is outlined in this section, and
                                             			 is dependent on the type of product you select. |
| Step 4 | Click Next . |
| Step 5 | To upgrade a product instance, select the product instance in
                                          			 the Available Product Instances window and click the arrow to move it to the Product Instances to Migrate window. Note By
                                                         				  default, only product instances containing license data from a previous version
                                                         				  of Cisco Unified Communications Manager are displayed in the Available Product
                                                         				  Instances table. If the product instance you upgraded does not appear in the
                                                         				  list, click the Show additional Unified CM product instances check box.
                                                         				  Selecting this check box adds product instances that contain
                                                         				  no prior license data to the list as well as those that were included in prior license migration
                                                         				  requests. | Note | By
                                                         				  default, only product instances containing license data from a previous version
                                                         				  of Cisco Unified Communications Manager are displayed in the Available Product
                                                         				  Instances table. If the product instance you upgraded does not appear in the
                                                         				  list, click the Show additional Unified CM product instances check box.
                                                         				  Selecting this check box adds product instances that contain
                                                         				  no prior license data to the list as well as those that were included in prior license migration
                                                         				  requests. |
| Note | By
                                                         				  default, only product instances containing license data from a previous version
                                                         				  of Cisco Unified Communications Manager are displayed in the Available Product
                                                         				  Instances table. If the product instance you upgraded does not appear in the
                                                         				  list, click the Show additional Unified CM product instances check box.
                                                         				  Selecting this check box adds product instances that contain
                                                         				  no prior license data to the list as well as those that were included in prior license migration
                                                         				  requests. |
| Step 6 | Click Next . |
| Step 7 | The Summary of Pre-Upgrade Product Instance Data table
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
                                                   				  Reports (Optional) Click Upload
                                                         						Report to open the Upload License Count Utility Report dialog box.
                                                      					 Click Browse to select the report file and then click Upload
                                                         						Report . MAC Addresses
                                                   				  (Optional) The MAC
                                                      					 addresses from the original servers that were upgraded. These MAC addresses will
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
                                                   				  Reports (Optional) | Click Upload
                                                         						Report to open the Upload License Count Utility Report dialog box.
                                                      					 Click Browse to select the report file and then click Upload
                                                         						Report . | MAC Addresses
                                                   				  (Optional) | The MAC
                                                      					 addresses from the original servers that were upgraded. These MAC addresses will
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
                                                   				  Reports (Optional) | Click Upload
                                                         						Report to open the Upload License Count Utility Report dialog box.
                                                      					 Click Browse to select the report file and then click Upload
                                                         						Report . |
| MAC Addresses
                                                   				  (Optional) | The MAC
                                                      					 addresses from the original servers that were upgraded. These MAC addresses will
                                                      					 be used to look up the licenses that were registered on those product
                                                      					 instances. |
| Step 8 | In this Summary
                                             			 and Next Steps section, indicate how the
                                          			 upgrade was ordered: Upgraded using one or more
                                             				service contracts Purchased the upgrade If you select
                                          			 "Upgraded using one or more service contracts", enter the UCSS/ESW Contract
                                          				Numbers. If you select
                                          			 "Purchased the upgrade", enter the 
                                          			 Sales Order
                                          				Numbers. |
| Step 9 | Enter your
                                          			 Cisco user ID in the Cisco.com
                                             				(CCO) User ID field. Company Name
                                             				and the field used to capture additional information are optional. However, if
                                             				you enter the company name, it is used in the subject line of the email and is
                                             				included in the name of the zip file. A default name
                                             				for the summary also appears in the Name field using the format
                                             				<productname>-migrate-<date-time-stamp> format. Instructions for
                                             				placing your order and fulfilling your licenses also appear in this section.
                                             				Click Finish &
                                                				  Generate Request . |
| Step 10 | From the License
                                             			 Migration Request and Next Steps window, download the License Migration
                                          			 Request zip file to your computer. Email the
                                             				License Migration Request to Cisco licensing support using the link provided. Click Close to
                                             				return to the License Fulfillment page. |

| Note | By
                                                         				  default, only product instances containing license data from a previous version
                                                         				  of Cisco Unified Communications Manager are displayed in the Available Product
                                                         				  Instances table. If the product instance you upgraded does not appear in the
                                                         				  list, click the Show additional Unified CM product instances check box.
                                                         				  Selecting this check box adds product instances that contain
                                                         				  no prior license data to the list as well as those that were included in prior license migration
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
                                                   				  Reports (Optional) | Click Upload
                                                         						Report to open the Upload License Count Utility Report dialog box.
                                                      					 Click Browse to select the report file and then click Upload
                                                         						Report . |
| MAC Addresses
                                                   				  (Optional) | The MAC
                                                      					 addresses from the original servers that were upgraded. These MAC addresses will
                                                      					 be used to look up the licenses that were registered on those product
                                                      					 instances. |

| Step 1 | From the Licenses > Fulfillment window in Cisco Prime License Manager, select Fulfillment
                                                				  Options > Migrate Licenses . |
|---|---|
| Step 2 | In the Migrate
                                             			 Licenses to Cisco Prime License Manager wizard, select Unity Connection from the drop-down menu in the Choose Product Type section. |
| Step 3 | From the New License Version section, select the version of the product to which you are migrating licenses. The migration process is outlined in this section, and
                                             			 is dependent on the type of product you select. |
| Step 4 | Click Next . |
| Step 5 | To upgrade a product instance, select the product instance in
                                          			 the Available Product Instances window and click the arrow to move it to the Product Instances to Migrate window. |
| Step 6 | Click Next . |
| Step 7 | The License
                                             			 Counts section prompts you to select one of two options
                                          			 relating to Cisco Unified Workshop Licenses (CUWL): Option Input I have CUWL licenses to be
                                                   				  migrated Click Next to move on to the Summary and Next Steps section. I do not have CUWL licenses
                                                   				  to be migrated. You can reduce (but
                                                      					 not increase) your license counts in the Licenses to Migrate column. You may
                                                      					 also choose to run a compliance check by clicking Run Compliance Check , or reset the license values by clicking Reset Values . Click OK to close the dialog box and then click Next to move on to the Summary and Next
                                                         					 Steps section. | Option | Input | I have CUWL licenses to be
                                                   				  migrated | Click Next to move on to the Summary and Next Steps section. | I do not have CUWL licenses
                                                   				  to be migrated. | You can reduce (but
                                                      					 not increase) your license counts in the Licenses to Migrate column. You may
                                                      					 also choose to run a compliance check by clicking Run Compliance Check , or reset the license values by clicking Reset Values . Click OK to close the dialog box and then click Next to move on to the Summary and Next
                                                         					 Steps section. |
| Option | Input |
| I have CUWL licenses to be
                                                   				  migrated | Click Next to move on to the Summary and Next Steps section. |
| I do not have CUWL licenses
                                                   				  to be migrated. | You can reduce (but
                                                      					 not increase) your license counts in the Licenses to Migrate column. You may
                                                      					 also choose to run a compliance check by clicking Run Compliance Check , or reset the license values by clicking Reset Values . Click OK to close the dialog box and then click Next to move on to the Summary and Next
                                                         					 Steps section. |
| Step 8 | The option you selected in Step 4 determines
                                          			 the information displayed in the Summary
                                             			 and Next Steps section. Option Description I have CUWL licenses to be
                                                   				  migrated In this
                                                      					 section you must indicate how the upgrade was ordered: - Upgraded
                                                      					 using one or more service contracts -
                                                      					 Purchased the upgrade If you
                                                      					 select Upgraded using one or more service contracts, enter the 
                                                      					 UCSS/ESW
                                                      						Contract Numbers. If you
                                                      					 select Purchased the upgrade, enter the 
                                                      					 Sales
                                                      						Order Numbers. Enter
                                                      					 your Cisco user ID in the Cisco.com (CCO) User ID field. Company
                                                      					 Name and the field used to capture additional information are optional.
                                                      					 However, if you enter the company name, it is used in the subject line of the
                                                      					 email and is included in the name of the zip file. A
                                                      					 default name for the summary also appears in the Name field using the format
                                                      					 <productname>-migrate-<date-time-stamp> format. Instructions for
                                                      					 placing your order and fulfilling your licenses also appear in this section.
                                                      					 Click Finish
                                                         						& Generate Request . From the License Migration Request and Next Steps window, download the License
                                                      					 Migration Request zip file to your computer. Email
                                                      					 the License Migration Request to Cisco licensing support using the link
                                                      					 provided. Click Close to return to the License Fulfillment window. I do not have CUWL
                                                   				  licenses to be migrated and e-Fulfillment is enabled Specify an optional
                                                         						description for the transaction. Read the end User License Agreement and select
                                                         						the check box to confirm. Click Finish and Generate . Enter your Cisco.com
                                                         						login and click OK . The request is
                                                         						electronically submitted, processed immediately, and your licenses are
                                                         						installed automatically. I do not have CUWL
                                                   				  licenses to be migrated and e-Fulfillment is disabled In this
                                                      					 section you can view and save a summary of the changes you made. To view the
                                                      					 summary, click View Summary . A default name for the summary also appears in the Name field using the format <productname>-migrate-<date-time-stamp>
                                                      					 format. Instructions for placing your order and fulfilling your licenses also
                                                      					 appear in this section. Click Finish
                                                         						& Generate Request . From the License Migration Request and Next Steps window, copy the selected text
                                                      					 to your clipboard or click Save
                                                         						it to a file on your computer . Select License Migration Portal under Step 2 and paste the copied
                                                      					 text in the designated field or select the saved file from your computer. Click Close to return to the License Fulfillment window. Note Only
                                                               					 e-Migration transactions are accessible on the License Fulfillment window. Since
                                                               					 this is a manual migration, the migration plan is accessible only on the License Planning window. | Option | Description | I have CUWL licenses to be
                                                   				  migrated | In this
                                                      					 section you must indicate how the upgrade was ordered: - Upgraded
                                                      					 using one or more service contracts -
                                                      					 Purchased the upgrade If you
                                                      					 select Upgraded using one or more service contracts, enter the 
                                                      					 UCSS/ESW
                                                      						Contract Numbers. If you
                                                      					 select Purchased the upgrade, enter the 
                                                      					 Sales
                                                      						Order Numbers. Enter
                                                      					 your Cisco user ID in the Cisco.com (CCO) User ID field. Company
                                                      					 Name and the field used to capture additional information are optional.
                                                      					 However, if you enter the company name, it is used in the subject line of the
                                                      					 email and is included in the name of the zip file. A
                                                      					 default name for the summary also appears in the Name field using the format
                                                      					 <productname>-migrate-<date-time-stamp> format. Instructions for
                                                      					 placing your order and fulfilling your licenses also appear in this section.
                                                      					 Click Finish
                                                         						& Generate Request . From the License Migration Request and Next Steps window, download the License
                                                      					 Migration Request zip file to your computer. Email
                                                      					 the License Migration Request to Cisco licensing support using the link
                                                      					 provided. Click Close to return to the License Fulfillment window. | I do not have CUWL
                                                   				  licenses to be migrated and e-Fulfillment is enabled | Specify an optional
                                                         						description for the transaction. Read the end User License Agreement and select
                                                         						the check box to confirm. Click Finish and Generate . Enter your Cisco.com
                                                         						login and click OK . The request is
                                                         						electronically submitted, processed immediately, and your licenses are
                                                         						installed automatically. | I do not have CUWL
                                                   				  licenses to be migrated and e-Fulfillment is disabled | In this
                                                      					 section you can view and save a summary of the changes you made. To view the
                                                      					 summary, click View Summary . A default name for the summary also appears in the Name field using the format <productname>-migrate-<date-time-stamp>
                                                      					 format. Instructions for placing your order and fulfilling your licenses also
                                                      					 appear in this section. Click Finish
                                                         						& Generate Request . From the License Migration Request and Next Steps window, copy the selected text
                                                      					 to your clipboard or click Save
                                                         						it to a file on your computer . Select License Migration Portal under Step 2 and paste the copied
                                                      					 text in the designated field or select the saved file from your computer. Click Close to return to the License Fulfillment window. Note Only
                                                               					 e-Migration transactions are accessible on the License Fulfillment window. Since
                                                               					 this is a manual migration, the migration plan is accessible only on the License Planning window. | Note | Only
                                                               					 e-Migration transactions are accessible on the License Fulfillment window. Since
                                                               					 this is a manual migration, the migration plan is accessible only on the License Planning window. |
| Option | Description |
| I have CUWL licenses to be
                                                   				  migrated | In this
                                                      					 section you must indicate how the upgrade was ordered: - Upgraded
                                                      					 using one or more service contracts -
                                                      					 Purchased the upgrade If you
                                                      					 select Upgraded using one or more service contracts, enter the 
                                                      					 UCSS/ESW
                                                      						Contract Numbers. If you
                                                      					 select Purchased the upgrade, enter the 
                                                      					 Sales
                                                      						Order Numbers. Enter
                                                      					 your Cisco user ID in the Cisco.com (CCO) User ID field. Company
                                                      					 Name and the field used to capture additional information are optional.
                                                      					 However, if you enter the company name, it is used in the subject line of the
                                                      					 email and is included in the name of the zip file. A
                                                      					 default name for the summary also appears in the Name field using the format
                                                      					 <productname>-migrate-<date-time-stamp> format. Instructions for
                                                      					 placing your order and fulfilling your licenses also appear in this section.
                                                      					 Click Finish
                                                         						& Generate Request . From the License Migration Request and Next Steps window, download the License
                                                      					 Migration Request zip file to your computer. Email
                                                      					 the License Migration Request to Cisco licensing support using the link
                                                      					 provided. Click Close to return to the License Fulfillment window. |
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
                                                      					 summary, click View Summary . A default name for the summary also appears in the Name field using the format <productname>-migrate-<date-time-stamp>
                                                      					 format. Instructions for placing your order and fulfilling your licenses also
                                                      					 appear in this section. Click Finish
                                                         						& Generate Request . From the License Migration Request and Next Steps window, copy the selected text
                                                      					 to your clipboard or click Save
                                                         						it to a file on your computer . Select License Migration Portal under Step 2 and paste the copied
                                                      					 text in the designated field or select the saved file from your computer. Click Close to return to the License Fulfillment window. Note Only
                                                               					 e-Migration transactions are accessible on the License Fulfillment window. Since
                                                               					 this is a manual migration, the migration plan is accessible only on the License Planning window. | Note | Only
                                                               					 e-Migration transactions are accessible on the License Fulfillment window. Since
                                                               					 this is a manual migration, the migration plan is accessible only on the License Planning window. |
| Note | Only
                                                               					 e-Migration transactions are accessible on the License Fulfillment window. Since
                                                               					 this is a manual migration, the migration plan is accessible only on the License Planning window. |

| Option | Input |
|---|---|
| I have CUWL licenses to be
                                                   				  migrated | Click Next to move on to the Summary and Next Steps section. |
| I do not have CUWL licenses
                                                   				  to be migrated. | You can reduce (but
                                                      					 not increase) your license counts in the Licenses to Migrate column. You may
                                                      					 also choose to run a compliance check by clicking Run Compliance Check , or reset the license values by clicking Reset Values . Click OK to close the dialog box and then click Next to move on to the Summary and Next
                                                         					 Steps section. |

| Option | Description |
|---|---|
| I have CUWL licenses to be
                                                   				  migrated | In this
                                                      					 section you must indicate how the upgrade was ordered: - Upgraded
                                                      					 using one or more service contracts -
                                                      					 Purchased the upgrade If you
                                                      					 select Upgraded using one or more service contracts, enter the 
                                                      					 UCSS/ESW
                                                      						Contract Numbers. If you
                                                      					 select Purchased the upgrade, enter the 
                                                      					 Sales
                                                      						Order Numbers. Enter
                                                      					 your Cisco user ID in the Cisco.com (CCO) User ID field. Company
                                                      					 Name and the field used to capture additional information are optional.
                                                      					 However, if you enter the company name, it is used in the subject line of the
                                                      					 email and is included in the name of the zip file. A
                                                      					 default name for the summary also appears in the Name field using the format
                                                      					 <productname>-migrate-<date-time-stamp> format. Instructions for
                                                      					 placing your order and fulfilling your licenses also appear in this section.
                                                      					 Click Finish
                                                         						& Generate Request . From the License Migration Request and Next Steps window, download the License
                                                      					 Migration Request zip file to your computer. Email
                                                      					 the License Migration Request to Cisco licensing support using the link
                                                      					 provided. Click Close to return to the License Fulfillment window. |
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
                                                      					 summary, click View Summary . A default name for the summary also appears in the Name field using the format <productname>-migrate-<date-time-stamp>
                                                      					 format. Instructions for placing your order and fulfilling your licenses also
                                                      					 appear in this section. Click Finish
                                                         						& Generate Request . From the License Migration Request and Next Steps window, copy the selected text
                                                      					 to your clipboard or click Save
                                                         						it to a file on your computer . Select License Migration Portal under Step 2 and paste the copied
                                                      					 text in the designated field or select the saved file from your computer. Click Close to return to the License Fulfillment window. Note Only
                                                               					 e-Migration transactions are accessible on the License Fulfillment window. Since
                                                               					 this is a manual migration, the migration plan is accessible only on the License Planning window. | Note | Only
                                                               					 e-Migration transactions are accessible on the License Fulfillment window. Since
                                                               					 this is a manual migration, the migration plan is accessible only on the License Planning window. |
| Note | Only
                                                               					 e-Migration transactions are accessible on the License Fulfillment window. Since
                                                               					 this is a manual migration, the migration plan is accessible only on the License Planning window. |

| Note | Only
                                                               					 e-Migration transactions are accessible on the License Fulfillment window. Since
                                                               					 this is a manual migration, the migration plan is accessible only on the License Planning window. |
|---|---|

| Step 1 | From the Licenses > Fulfillment window in Cisco Prime License Manager, click Fulfillment
                                                				  Options > Migrate Licenses . |
|---|---|
| Step 2 | In the Migrate
                                             			 Licenses to Cisco Prime License Manager wizard, select 
                                          			 the type of product to upgrade and the version from the drop-down menus
                                          			 in the Choose Product Type section. The migration process is outlined in this section, and
                                          			 is dependent on the type of product you select. |
| Step 3 | Click Next . |
| Step 4 | From the Choose
                                             			 Product Instances section appears,  check the checkbox next to Show
                                             				additional Unified CM product instances . Selecting this option allows you
                                          			 to view products without prior version data. |
| Step 5 | To migrate a
                                          			 product instance, select it in the Available Product Instances window and click
                                          			 the arrow to move it to the Product Instances to Migrate window. Click Next . |
| Step 6 | After you have read the
                                          			 contents of the Additional Information Will Be Required window, click Continue to close the window. |
| Step 7 | Enter the following information in the License
                                          			 Counts section: The number of public space
                                             				phones in the Public Space Phones field Case Numbers License Count Utility
                                             				Reports - select the zip file using the Upload Report button The MAC address in the MAC
                                             				Addresses field Click Next . |
| Step 8 | Download the License Migration
                                          			 Request zip file to your computer. |
| Step 9 | Email the
                                          			 License Migration Request to Cisco licensing support using the link provided. |
| Step 10 | Click Close to
                                          			 return to the License Planning window. |