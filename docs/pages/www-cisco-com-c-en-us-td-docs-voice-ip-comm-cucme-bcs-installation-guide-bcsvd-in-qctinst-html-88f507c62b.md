---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-bcs-installation-guide-bcsvd-in-qctinst-html-88f507c62b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/bcs/installation/guide/bcsvd_in/QCTinst.html
retrieved_at: 2026-08-21T22:58:38.575619+00:00
---

Installing Cisco Business Communications Solution Verified Designs

# Installing Cisco Business Communications Solution Verified Designs

Updated: November 2, 2007

Chapter: Installing Required Software

## Chapter: Installing Required Software

## Installing Required Software

This chapter describes procedures to download and install the required software for installing Cisco BCS Verified Designs. Download all software to your PC before configuring Cisco BCS Verified Designs.

## Contents

This chapter contains the following sections:

• Installing Cisco IPC Express QCT

• Installing Cisco Security Device Manager

• What to Do Next

## Installing Cisco IPC Express QCT

Perform the following steps to install Cisco IPC Express QCT on your PC.

Note Before installing Cisco IPC Express QCT, make sure that you are a member of the Administrators group under Control Panel > User Account settings.

Note This installation procedure assumes the use of Windows XP. If you are using another Windows operating system, your display may differ slightly.

Step 1 Download the Cisco IPC Express QCT 1.5.7 x .zip file from the following location:

http://www.cisco.com/cgi-bin/tablebuild.pl/cme-qct

Note You must have a valid Cisco CCO account to download Cisco IPC Express QCT.

Note Cisco IPC Express QCT is supported only under Windows Internet Explorer version 5.5 or later.

Step 2 Unzip and extract the files into an existing folder on your PC.

Files will automatically install into your specified folder location, creating a number of subfolders (see Figure 3 ):

Figure 3 Cisco IPC Express QCT Extracted Files

Step 3 Open the Cisco IPC Express QCT subfolder NetCommOCX (see Figure 4 ).

Figure 4 QCT NetCommOCX Folder

Step 4 Click SETUP.EXE to install the necessary serial communications drivers (see Figure 5 ).

Figure 5 SETUP.EXE folder

The NetCommOCX Welcome banner appears (see Figure 6 ).

Figure 6 NetCommOCX SETUP.EXE Welcome Banner

Step 5 Click Next .

Step 6 Enter your name and company name in the User Information dialog (see Figure 7 ).

Figure 7 Install User Information Dialog

Step 7 Click Next .

Step 8 Accept the default directory location by clicking Next . Or click Browse to specify a new destination directory on your PC (see Figure 8 ).

Figure 8 Install Choose Destination Location Dialog

Step 9 Specify your program folder location by entering a new name in the Program Folders field or highlight an existing folder in the Existing Folders scroll area (see Figure 9 ).

Figure 9 Install Select Program Folder Dialog

Step 10 Click Next .

Setup is now ready to begin copying files (see Figure 10 ).

Figure 10 Start Copying Files Dialog

Step 11 Click Next .

Step 12 When setup has completed, click Finish (see Figure 11 ).

Figure 11 Install Setup Complete Dialog

Note Do not use the Yes, Launch the program file checkbox with this release. To launch Cisco IPC Express QCT refer to Launching Cisco IPC Express QCT, page 18 .

## Installing Cisco Security Device Manager

This section describes the steps necessary for installing Cisco Security Device Manager (Cisco SDM). For complete information on downloading and installing Cisco SDM, see the SDM Downloading and Installing User Guide at:

http://www.cisco.com/en/US/products/sw/secursw/ps5318/prod_installation_guide09186a00803e4727.html

Step 1 Download the sdm-v nn .zip file at http://www.cisco.com/pcgi-bin/tablebuild.pl/sdm .

Log in using your Cisco.com login user ID and password, and follow the instructions on the Cisco SDM Software page to download the sdm.vnn.zip file and the SDM release notes.

Step 2 Double-click the sdm-v nn .zip file, and extract the files to a directory on your PC.

Step 3 In the directory to which you extracted the contents of the sdm-v nn .zip file, double-click the setup.exe file. The Cisco SDM Welcome dialog appears (see Figure 12 ):

Figure 12 Cisco SDM Welcome Dialog

Step 4 Click Next to display the License screen, accept the license agreement terms, and click Next to continue.

Step 5 When the Install Options dialog appears (see Figure 13 ), specify to install Cisco SDM on your PC (This Computer).

Figure 13 Cisco SDM Install Options Dialog

Step 6 Click Next .

After the components are installed, the Cisco SDM Installation Wizard Complete screen appears (see Figure 14 ):

Figure 14 Cisco SDM Installation Wizard Complete Dialog

Step 7 If you want to start Cisco SDM when you dismiss the wizard, click Launch Cisco SDM . Click Finish to dismiss the wizard.

## What to Do Next

After installing the required Cisco IPC Express QCT and SDM files, you are ready to enter configuration parameters about your system. See "Configuring Cisco Business Communications Solution Verified Designs" chapter.