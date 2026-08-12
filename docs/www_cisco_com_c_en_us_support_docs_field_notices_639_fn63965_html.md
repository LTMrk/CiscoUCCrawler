  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63965.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63965.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63965.html)


  * [Cisco.com Worldwide](https://www.cisco.com/site/us/en/index.html)
  * [Products and Services](https://www.cisco.com/site/us/en/products/index.html)
  * [Solutions](https://www.cisco.com/site/us/en/solutions/index.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Learn](https://www.cisco.com/site/us/en/learn/index.html)
  * [Explore Cisco](https://www.cisco.com/site/us/en/about/sitemap.html)
  * [How to Buy](https://www.cisco.com/site/us/en/buy/index.html)
  * [Partners Home](https://www.cisco.com/site/us/en/partners/index.html)
  * [Partner Program](https://www.cisco.com/site/us/en/partners/360-partner-program/partner-program/index.html)
  * [Support](https://www.cisco.com/site/us/en/partners/support-help/index.html)
  * [Tools](https://www.cisco.com/site/us/en/partners/360-partner-program/tools-training/index.html)
  * [Find a Cisco Partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
  * [Meet our Partners](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html)
  * [Become a Cisco Partner](https://www.cisco.com/site/us/en/partners/index.html)


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63965.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63965.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Servers - Unified Computing](https://www.cisco.com/c/en/us/support/servers-unified-computing/category.html)
  * [Cisco UCS C-Series Rack Servers](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/products-field-notices-list.html)


# Field Notice: FN - 63965 - Some Cisco UCS C240 M4 and Cisco UCS C220 M4 Servers Might Fail to Boot - BIOS/Firmware Upgrade Recommended
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/639/fn63965.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63965.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/639/fn63965.html)


Updated:January 18, 2019
Document ID:FN63965
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
|  1.0   |  04-May-15   |  Initial Release   |  
|  10.0   |  13-Oct-17   |  Migration to new field notice system   |  
|  10.1   |  18-Jan-19   |  Fixed Broken Image Links   |  
### Products Affected  
| Affected Product ID  | Comments  |  
| --- | --- |  
|  UCSC-C220-M4L=   |   |  
|  UCSC-C220-M4S   |   |  
|  UCSC-C240-M4L   |   |  
|  UCSC-C240-M4S   |   |  
|  UCSC-C240-M4S2   |   |  
|  UCSC-C240-M4SX   |   |  
### Defect Information  
| Defect ID  | Headline  |  
| --- | --- |  
| [CSCuq97927](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCuq97927)  | Add the latest PSOC firmware - version V3.0a  |  
### Problem Description
Some Cisco Unified Computing System (UCS) C240 M4 and Cisco UCS C220 M4 Series systems might fail to boot up during the initial boot sequence.
### Background
There is an issue with the power sequencer firmware, which makes it appear that no power exists to the system or that there is a low voltage on the 3.3-volt battery. This problem is intermittent and a reboot of the system might allow the system to start. However, the issue might reappear the next time that the system is restarted if the firmware is not updated.
### Problem Symptom
The issue might manifest in these ways:
  * The system fails to initialize.
  * The host fails to power on.
  * A**no memory found** error message is observed during initialization, and the initialization process stops.
  * A low voltage alert for the 3.3v battery is observed during initialization, and the initialization process stops.


### Workaround/Solution
A firmware update is required for the affected systems. UCS C240 M4 and Cisco UCS C220 M4 systems manufactured November 25, 2014 and later will have the newer firmware.
Units that were shipped with the affected power sequencer firmware version can be identified by the chassis serial number (refer to the How to Identify Affected Products section of this document). There are multiple methods that you can use in order to update the firmware. Use one of these procedures for the update:
**Host Upgrade Utility (for standalone systems)**
If you run the Host Upgrade Utility (HUU) Version 2.0(3f) or later, it automatically updates the firmware levels to the correct version. Refer to the [Cisco Host Upgrade Utility 2.0(3) User Guide](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/lomug/2-0-x/b_huu_2_0_3.html) for more information.
**CIMC Update (for standalone systems)**
The Cisco Integrated Management Controller (CIMC) Version 2.0(3f) automatically updates the power sequencer firmware to the correct level. Power on the host from the WebUI and then after powering off the host, you will see the following prompt in the WebUI:  
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/639/fn63965_npqm7t1547512385322.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/639/fn63965_npqm7t1547512385322.png "Related image, diagram or screenshot.")  
After an upgrade to this CIMC version, you are prompted to update the firmware version during the initial boot sequence. You must answer **Yes** at the prompt in order for the update to take place.
**UCSM CLI Update for a UCS-managed C-series server**
Each C-bundle contains a board-controller image for each platform, and it contains low level firmware.

```
 
ucs-c220 #**scope firmware**
ucs-c220 /firmware # **show image type board-controller**
Name                                          Type                 Version
--------------------------------------------- -------------------- -------
ucs-c22-m3-brdprog.5.0.gbin                   Board Controller     5.0
ucs-c220-m3-brdprog.5.0.gbin                  Board Controller     5.0
ucs-c220-m4-brdprog.14.0.gbin                 Board Controller     14.0
ucs-c240-m3-brdprog.5.0.gbin                  Board Controller     5.0
ucs-c240-m4-brdprog.13.0.gbin                 Board Controller     13.0
ucs-c420-m3-brdprog.5.0.gbin                  Board Controller     5.0
ucs-c460-m4-brdprog.12.0.gbin                 Board Controller     12.0

ucs-c220 /firmware # **exit**
ucs-c220 #**scope server 2**  [note that 2 is the server index in this case]
ucs-c220 /server # **scope boardcontroller**
ucs-c220 /server/boardcontroller #**activate firmware 12.0**  [note that 12.0 is the firmware version in this case]
Warning: When committed this command will reset the end-point
ucs-c220 /server/boardcontroller* # **commit-buffer**
...
ucs-c220 /server/boardcontroller # **show version**
BoardController:
    Running-Vers: 12.0
    Package-Vers:
    Activate-Status: Ready

```

**From UCSM GUI**
From the UCSM GUI
  1. Load the C-Series firmware bundle 2.0(3f) or newer into UCS manager
  2. Select the board to update
  3. Right-click on "BoardContoller" and select "activate firmware".


[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/639/fn63965_npqmdg1547512234094.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/639/fn63965_npqmdg1547512234094.png "Related image, diagram or screenshot.")
**From the CIMC CLI on a standalone C-series server**

```
ucs-c220# **scope chassis/firmware**
ucs-c220 /chassis/firmware # **show detail**
Firmware update required on some components, please run update-all (under chassis/firmware scope).
ucs-c220 /chassis/firmware # **update-all**_ _
Starting firmware update process, this will take a while. Check status using show command
ucs-c220 /chassis/firmware # **show detail**
Firmware update process is running, retry to get latest status.
...
ucs-c220 /chassis/firmware # **show detail**
Firmware update completed
ucs-c220 /chassis/firmware # **show detail**
Firmware update not required, all components are up to date
ucs-c220 /chassis/firmware # **exit**
ucs-c220 /chassis # **exit**

```

For more information about how to update the UCS C-Series CIMC and BIOS, refer to the [Cisco UCS C-Series Servers Integrated Management Controller Configuration Guides](http://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-integrated-management-controller/products-installation-and-configuration-guides-list.html).
### How To Identify Affected Products
It is not possible to directly identify the current power sequencer firmware level. The units that were initially shipped from Cisco with the affected power sequencer firmware version can be identified by the chassis serial number. You can enter the suspected serial numbers into the [Serial Number Validation Tool](https://snvui.cisco.com/snv/FN63965) for this Field Notice in order to determine if the unit(s) is potentially affected. Complete these steps in order to determine whether the unit is suspect:
  1. Get the Serial number: 
     * _For CIMC:_ Connect to the Cisco UCS C-Series chassis and log into the CIMC. The Server Summary page appears after the log in:  
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/639/fn63965_nmuxwp1547512257943.jpg)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/639/fn63965_nmuxwp1547512257943.jpg "Related image, diagram or screenshot.")
_For UCSM:_
       1. Go to the Equipment tab in UCS Manager
       2. Select the server you want to look at
       3. Select the Inventory -> Motherboard tab.  
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/639/fn63965_npu9v81547512286717.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/639/fn63965_npu9v81547512286717.png "Related image, diagram or screenshot.")


  1. Confirm that the chassis Product ID (PID) is one of those that are listed in the Products Affected section of this Field Notice (as shown in the previous example).  

  2. Take note of the serial number and enter it into the [FN63965 Serial Number Validation Tool](https://snvui.cisco.com/snv/FN63965) in order to determine if it is affected.  
  
**Note:** More than one serial number can be entered into the tool at one time.


### For More Information
If you require further assistance, or if you have any further questions regarding this field notice, please contact the Cisco Systems [Technical Assistance Center (TAC)](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html) by one of the following methods:
  * [Open a service request on Cisco.com](https://tools.cisco.com/ServiceRequestTool/scm/mgmt/case)
  * [By email](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#email)
  * [By telephone](http://www.cisco.com/en/US/support/tsd_cisco_worldwide_contacts.html#telephone)


### Receive Email Notification For New Field Notices
[Cisco Notification Service](http://www.cisco.com/cisco/support/notifications.html)—Set up a profile to receive email updates about reliability, safety, network security, and end-of-sale issues for the Cisco products you specify.
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63965.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63965.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [UCS C220 M4 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c220-m4-rack-server/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/639/fn63965.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/639/fn63965.html)
