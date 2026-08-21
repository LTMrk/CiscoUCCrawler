---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-aft-1-1-english-sbc-ameritech-user-guide-user-ame-aftinst-html-4bc6edc7e4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/aft/1_1/english/sbc_ameritech/user/guide/user_ame/AFTinst.html
retrieved_at: 2026-08-21T15:50:54.457527+00:00
---

ALI Formatting Tool User Guide for SBC Ameritech

# ALI Formatting Tool User Guide for SBC Ameritech

Updated: November 2, 2007

Chapter: Installing the ALI Formatting Tool

## Chapter: Installing the ALI Formatting Tool

- System Requirements

- Installing the ALI Formatting Tool

## Installing the ALI Formatting Tool

Use these topics to install ALI Formatting Tool (AFT):

• System Requirements

• Installing the ALI Formatting Tool

## System Requirements

The ALI Formatting Tool (AFT) requires the following software components to operate:

• Cisco Emergency Responder 1.1 (Cisco ER) or later

• Microsoft Windows 2000

The ALI Formatting Tool (AFT) supports all hardware platforms supported by Emergency Responder. Refer to the Cisco Emergency Responder Administration Guide for Cisco ER-supported Cisco Media Convergence Server (MCS) hardware platforms.

Note You must install AFT on the same server with Cisco ER.

Related Topics

• Installing the ALI Formatting Tool

## Installing the ALI Formatting Tool

The ALI Formatting Tool (AFT) is downloadable from the Internet. To install AFT, perform the following steps:

Step 1 Start the Cisco MCS or Cisco certified server and log in to Windows 2000.

Step 2 Use a web browser to access the following URL:

http://www.cisco.com/cgi-bin/tablebuild.pl/aft

Step 3 Download the AFT installation file that is specific to your service provider.

The AFT .exe files are named as shown here:

CER-aft- <serviceprovider>.<mainrelease> - <minorrelease> -<maintrelease> .exe

where serviceprovider is the name of your Service Provider

and mainrelease, minorrelease and maintrelease make up the AFT release number.

For example, to select the SBC Ameritech AFT, click on: CER-aft-SBC_Ameritech.1-1-1.exe

Step 4 Double-click on the downloaded file to launch the installer.

The Welcome to the ALI Formatting Tool (AFT) Installation Wizard screen appears.

Step 5 At this point, the installation checks for the presence of Cisco ER 1.1 or later.

If Cisco ER 1.1 or later is not present, you are prompted to install it. The installation of AFT will not continue until Cisco ER 1.1 or later is present.

Step 6 Click Next .

The License Agreement Screen appears.

Step 7 Select Accept and click Next .

The User Information Screen appears.

Step 8 Enter the user name and organization information and click Next .

Step 9 Select administrator rights by clicking on one of the following choices:

• For me

• For all who use the computer

Step 10 Click Next .

The Ready to Install screen appears.

Step 11 Click Next .

Step 12 To test that the application successfully loaded, install the new shortcut path and launch the AFT application. Go to:

a. Start > Programs > Cisco Emergency Responder > AFT > < serviceprovider ( NENA version) >

For SBC Ameritech, go to:

Start > Programs > Cisco Emergency Responder > AFT > SBC Ameritech (NENA 2.0)

The AFT login screen appears.

b. To log in to AFT, enter your Cisco ER Main Administrator or ERL Administrator login ID and Password.

Related Topics

• System Requirements

• Chapter 3 "Using the ALI Formatting Tool"