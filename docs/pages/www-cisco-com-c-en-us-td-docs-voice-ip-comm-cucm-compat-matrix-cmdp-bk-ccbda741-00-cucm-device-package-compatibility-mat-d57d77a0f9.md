---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-compat-matrix-cmdp-bk-ccbda741-00-cucm-device-package-compatibility-mat-d57d77a0f9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix_chapter_00.html
retrieved_at: 2026-08-16T23:47:43.123893+00:00
---

Cisco Unified Communications Manager Device Package Compatibility Matrix

# Cisco Unified Communications Manager Device Package Compatibility Matrix

Updated: December 1, 2014

Chapter: Current Cisco Unified Communications Manager Device Package Releases

## Chapter: Current Cisco Unified Communications Manager Device Package Releases

# Current Cisco Unified Communications Manager Device Package Releases

## Cisco Unified
                           				Communications Manager Device Package Compatibility Matrix - Current

This section provides information about the latest Cisco Unified
                                 				Communications Manager ( Unified CM ) device packages available for:

Unified CM 14.0(1)

Unified CM 12.5(1)

Unified CM 11.5(1)

For information about a previous release, see Cisco Unified Communications Manager Device Package Compatibility Matrix - End of Software Maintenance .

A device package introduces new phone types to Unified CM , and installs the firmware and configuration files that enable features on your Cisco device. New features may be off by
                              default, and have attributes or settings that you must configure.

Device packages are available from the Cisco Unified
                                 				Communications Manager software download page. To obtain a device package, click the Unified CM device package link and a new browser window or tab opens. You'll need your Cisco sign-in.

Apply a device package to all your Unified CM servers, beginning with the publisher server and the TFTP server.

When you apply a device package to enable new device support, you don't perform a cluster-wide reboot for Unified CM 11.5(1) or later. Instead, after you add the device package, do the following in Unified CM :

Restart the Cisco Tomcat service on all cluster nodes.

If you are running 11.5(1)SU4 or lower, 12.0(1) or 12.0(1)SU1, reboot the cluster. If you are running 11.5(1)SU5 or higher,
                                    or 12.0(1)SU2 or higher, reboot the Unified CM service on the publisher node. However, if you are running the Cisco Call Manager service on the subscriber nodes only, you
                                    can skip this task.

For more information about how to install a device package, see the Cisco Unified Communications Manager Device Package Installation Guide .

### Deprecated Phone Models for Cisco Unified Communications Manager

### Cisco Unified Communications Manager 14.0(1)

This section provides details about the compatible device packages for Cisco Unified
                                    				Communications Manager ( Unified CM ) 14.0(1) release. Each row in a table provides the device package information for a particular device and firmware release.

Unified CM device packages contain both configuration files and firmware files, except in certain cases as indicated in the table.

#### Cisco IP Phone 7800 Series

Device Type

Device Release

7811, 7821, 7841, and 7861

14.1(1)

cmterm-devicepack14.0.1

January 21, 2022

7832

14.1(1)

cmterm-devicepack14.0.1

January 21, 2022

#### Cisco IP Phone 8800 Series

Device Type

Device Release

8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR

14.1(1)

cmterm-devicepack14.0.1

January 21, 2022

14.1(1)

cmterm-devicepack14.0.1

January 21, 2022

8831 and 8831NR

10.3(1)SR7.2

cmterm-devicepack14.0.1

January 21, 2022

10.3(1)SR7.2

cmterm-devicepack14.0.1

September 8, 2021

8821 and 8821-EX

11.0(6)SR2

cmterm-devicepack14.0.1

January 21, 2022

#### Cisco Headset 500 Series

Device Type

Device Release

Compatible Device Package

Cisco Headset 500 Series

Cisco Options Package (COP) file: 2.3

Headset release: 2.3(1)

cmterm-devicepack14.0.1

September 8, 2021

#### Cisco Headset 700 Series

Device Type

Device Release

Compatible Device Package

Cisco Headset 700 Series

Cisco Options Package (COP) file: 2.3(1.13)

Headset release: 1-7-0-138

USB adapter release: 1-3-12

cmterm-devicepack14.0.1

January 21, 2022

#### Webex Board

Device Type

Device Release

Compatible Device Package

Webex Board Pro 55 and 75

Cisco Webex RoomOS 10

cmterm-devicepack14.0.1

January 21, 2022

#### Webex Desk

Device Type

Device Release

Compatible Device Package

Webex Desk Mini

QED files

cmterm-devicepack14.0.1

January 21, 2022

QED files

cmterm-devicepack14.0.1

September 8, 2021

New product QED files

cmterm-devicepack14.0.1

September 8, 2021

#### Webex Wireless Phone 840 and 860

Device Type

Device Release

Compatible Device Package

Webex Wireless Phone 840

QED file for 1.4(0)

cmterm-devicepack14.0.1

January 21, 2022

QED file for 1.3(0)

cmterm-devicepack14.0.1

September 8, 2021

Webex Wireless Phone 860

QED file for 1.4(0)

cmterm-devicepack14.0.1

January 21, 2022

QED file for 1.3(0)

cmterm-devicepack14.0.1

September 8, 2021

### Cisco Unified Communications Manager 12.5(1)

This section provides details about the compatible device packages for Cisco Unified
                                    				Communications Manager ( Unified CM ) 12.5(1) release. Each row in a table provides the device package information for a particular device and firmware release.

Unified CM device packages contain both configuration files and firmware files, except in certain cases as indicated in the table titles.

#### Cisco Unified SIP Phone 3905

Device Type

Device Release

Compatible Device Package

3905

9.4(1)SR3

cmterm-devicepack12.5.1

April 27, 2021

9.4(1)SR3

Included with Unified CM

#### Cisco Unified IP Phone 6900 Series

Device Type

Device Release

Compatible Device Package

6901 and 6911

9.3(1)SR2

Included with Unified CM

9.3(1)SR1

Included with Unified CM

6921, 6941, 6945, and 6961

9.4(1)SR2

Included with Unified CM

9.4(1)SR1

Included with Unified CM

#### Cisco IP Phone 7800 Series

When upgrading from Firmware Release 10.3(1) to Firmware Release 11.0(1) or later, the K-Factor has been removed from the
                                             Call Details Record. This was intentional as Unified CM does not support RTP-RxStat messages greater than 256 characters in length.

Device Type

Device Release

Compatible Device Package

7811, 7821, 7841, and 7861

14.1(1)

cmterm-devicepack12.5.1

January 21, 2022

14.0(1)

cmterm-devicepack12.5.1

April 27, 2021

12.8(1)

cmterm-devicepack12.5.1

August 3, 2020

7832

14.1(1)

cmterm-devicepack12.5.1

January 21, 2022

14.0(1)

cmterm-devicepack12.5.1

April 27, 2021

12.8(1)

cmterm-devicepack12.5.1

August 3, 2020

#### Cisco Unified IP Phone 7900 Series

Device Type

Device Release

Compatible Device Package

7945G, 7965G, and 7975G

9.4(2)SR4

cmterm-devicepack12.5.1

August 3, 2020

7911G, 7931G, 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE, 7962G, 7965G, and 7975G

9.4(2)SR3

Included with Unified CM

9.4(2)SR2

Included with Unified CM

7940G and 7960G

8.1(2)SR2 (SCCP)

Included with Unified CM

7915G and 7916G

1.0(4)

Included with Unified CM

7925G, 7925G-EX, and 7926G

1.4(8)SR1

Included with Unified CM

1.4(8)

Included with Unified CM

7937G

1.4(5)

Included with Unified CM

#### Cisco IP Phone 8800 Series

Device Type

Device Release

8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR

14.1(1)

cmterm-devicepack12.5.1

January 21, 2022

14.0(1)

cmterm-devicepack12.5.1

April 27, 2021

12.8(1)

cmterm-devicepack12.5.1

August 3, 2020

8832

14.1(1)

cmterm-devicepack12.5.1

January 21, 2022

14.0(1)

cmterm-devicepack12.5.1

April 27, 2021

12.8(1)

cmterm-devicepack12.5.1

August 3, 2020

8831 and 8831NR

10.3(1)SR7.2

cmterm-devicepack12.5.1

January 21, 2022

10.3(1)SR7.2

cmterm-devicepack12.5.1

September 8, 2021

14.0(1)

cmterm-devicepack12.5.1

April 27, 2021

8821 and 8821-EX

11.0(6)SR2

cmterm-devicepack12.5.1

January 21, 2022

11.0(6)SR1

cmterm-devicepack12.5.1

April 27, 2021

11.0(6) QED files

cmterm-devicepack12.5.1

November 23, 2020

#### Cisco Unified IP Phone 8900 and 9900 Series

Device Type

Device Release

Compatible Device Package

8941 and 8945

9.4(2)SR3

Included with Unified CM

9.4(2)SR2

Included with Unified CM

8961, 9951, and 9971

9.4(2)SR2

Included with Unified CM

9.4(2)

Included with Unified CM

#### Cisco Analog Telephone Adapter

Device Type

Device Release

Compatible Device Package

Cisco VG450 Analog Voice Gateway

Cisco IOS XE 16.10.01a

Included with Unified CM

ATA 187

9.2(3) SIP

Included with Unified CM

ATA 190

1.2.2

Included with Unified CM

1.2.1

Included with Unified CM

ATA 191

12.0(1)

Included with Unified CM

#### Cisco DX Series

After the September 30, 2019 device package, device packages don't contain any CE firmware.

Device Type

Device Release

Compatible Device Package

DX70 and DX80

New xAPIformat files for the CE product line

cmterm-devicepack12.5.1

August 3, 2020

CE9.8(1)

Included with Unified CM

CE9.7(1)

Included with Unified CM

DX650

10.2(5)

Included with Unified CM

10.2(4)

Included with Unified CM

Cisco Webex DX80 and Cisco Telepresence DX80 are different names for the same product.

#### Cisco TelePresence IX5000

Device Type

Device Release

Compatible Device Package

Cisco TelePresence IX5000

Software IX 9.0

Included with Unified CM

Software IX 8.0

Included with Unified CM

#### Cisco TelePresence E, EX, C, SX, and MX Series

After the September 30, 2019 device package, device packages don't contain any CE firmware.

Device Type

Device Release

Compatible Device Package

C Series, EX Series, MX200, and MX300

TC7.3(3)

Included with Unified CM

TC7.2(0)

Included with Unified CM

MX200 G2, MX300 G2, MX700, MX800, MX800 Dual, SX10, SX20, and SX80

New xAPIformat files for the CE product line

cmterm-devicepack12.5.1

August 3, 2020

CE9.8(1)

cmterm-devicepack12.5.1

September 30, 2019

CE9.7(1)

cmterm-devicepack12.5.1

May 28, 2019

#### Cisco Headset 500 Series

Device Type

Device Release

Compatible Device Package

Cisco Headset 500 Series

Cisco Options Package (COP) file: 2.3

Headset release: 2.3(1)

cmterm-devicepack12.5.1

September 8, 2021

COP file: 2.2

Headset release: 2.2(1)

cmterm-devicepack12.5.1

April 27, 2021

#### Cisco Headset 700 Series

Device Type

Device Release

Compatible Device Package

Cisco Headset 700 Series

Cisco Options Package (COP) file: 2.3(1.13)

Headset release: 1-7-0-138

USB adapter release: 1-3-12

cmterm-devicepack12.5.1

January 21, 2022

COP file: 2.2(1.6)

Headset release: 1-6-0-150

USB adapter release: 1-2-33

cmterm-devicepack12.5.1

April 27, 2021

COP file: 2.1

Headset release: 1-5-0-246

USB adapter release: 1-1-59

cmterm-devicepack12.5.1

November 23, 2020

#### Webex Board

After the September 30, 2019 device package, device packages don't contain any CE firmware.

Device Type

Device Release

Compatible Device Package

Webex Board Pro 55 and 75

Cisco Webex RoomOS 10

cmterm-devicepack12.5.1

January 21, 2022

Cisco Webex Board 55, 70, and 85

New xAPIformat files for the CE product line

cmterm-devicepack12.5.1

August 3, 2020

CE9.8(1)

cmterm-devicepack12.5.1

March 4, 2020

CE9.8(1)

cmterm-devicepack12.5.1

September 30, 2019

#### Webex Desk

Device Type

Device Release

Compatible Device Package

Webex Desk Mini

QED files

cmterm-devicepack12.5.1

January 21, 2022

Webex Desk

QED files

cmterm-devicepack12.5.1

September 8, 2021

Webex Desk Hub

New product QED files

cmterm-devicepack12.5.1

September 8, 2021

Cisco Webex Desk Limited Edition

New product QED files

cmterm-devicepack12.5.1

April 27, 2021

#### Webex Room

After the September 30, 2019 device package, device packages don't contain any CE firmware.

Device Type

Device Release

Compatible Device Package

All Webex Room devices with CE firmware

New xAPIformat files for the CE product line

cmterm-devicepack12.5.1

August 3, 2020

Cisco Webex Desk Pro

New product QED files

cmterm-devicepack12.5.1

March 4, 2020

Cisco Webex Room Panorama

New product QED files

cmterm-devicepack12.5.1

March 4, 2020

Cisco Webex Room Panorama 70

New product QED files

cmterm-devicepack12.5.1

March 4, 2020

Cisco Webex Room 70 Single and Cisco Webex Room 70 Dual

CE9.8(1)

cmterm-devicepack12.5.1

September 30, 2019

CE9.7(1)

cmterm-devicepack12.5.1

May 28, 2019

Cisco Webex Room 70 Single G2 and Cisco Webex Room 70 Dual G2

CE9.8(1)

cmterm-devicepack12.5.1

September 30, 2019

CE9.7(1)

cmterm-devicepack12.5.1

May 28, 2019

Cisco Webex Room 55 and Cisco Webex Room 55 Dual

CE9.8(1)

cmterm-devicepack12.5.1

September 30, 2019

CE9.7(1)

cmterm-devicepack12.5.1

May 28, 2019

Cisco Webex Room Kit Mini

CE9.8(1)

cmterm-devicepack12.5.1

September 30, 2019

CE9.7(1)

cmterm-devicepack12.5.1

May 28, 2019

Cisco Webex Room Kit and Cisco Webex Room Kit Plus

CE9.8(1)

cmterm-devicepack12.5.1

September 30, 2019

CE9.7(1)

cmterm-devicepack12.5.1

May 28, 2019

Cisco Webex Room Kit Pro

CE9.8(1)

cmterm-devicepack12.5.1

September 30, 2019

CE9.7(1)

cmterm-devicepack12.5.1

May 28, 2019

Cisco Webex Room Phone

CSV file check in

cmterm-devicepack12.5.1

November 23, 2020

New Product QED File

cmterm-devicepack12.5.1

August 3, 2020

#### Webex Wireless Phone 840 and 860

Device Type

Device Release

Compatible Device Package

Webex Wireless Phone 840

QED file for 1.4(0)

cmterm-devicepack12.5.1

January 21, 2022

QED file for 1.3(0)

cmterm-devicepack12.5.1

September 8, 2021

New product QED file 1.2(0)

cmterm-devicepack12.5.1

April 27, 2021

Webex Wireless Phone 860

QED file for 1.4(0)

cmterm-devicepack12.5.1

January 21, 2022

QED file for 1.3(0)

cmterm-devicepack12.5.1

September 8, 2021

New product QED file 1.1(0)

cmterm-devicepack12.5.1

April 27, 2021

#### Cisco 4000 Series Integrated Services Routers

Device Type

Device Release

Compatible Device Package

Cisco 4461 Integrated Services Routers

Cisco IOS XE 16.9.1

Included with Unified CM

Cisco 4000 Series Integrated Services Routers

Cisco IOS XE 16.4.1

Included with Unified CM

#### Cisco Jabber

There are no device packages available for Unified CM 12.5(1) release. More device packages aren't planned for Jabber.

### Cisco Unified Communications Manager 11.5(1)

This section provides details about the compatible device packages for Cisco Unified
                                    				Communications Manager ( Unified CM ) 11.5(1) release. Each row in a table provides the device package information for a particular device and firmware release.

Unified CM device packages contain both configuration files and firmware files.

#### Cisco Unified SIP Phone 3905

Device Type

Device Release

Compatible Device Package

3905

9.4(1)SR3

cmterm-devicepack11.5.1

April 27, 2021

9.4(1)SR3

cmterm-devicepack11.5.1

January 24, 2019

#### Cisco Unified IP Phone 6900 Series

Device Type

Device Release

Compatible Device Package

6901 and 6911

9.3(1)SR2

Included with Unified CM

9.3(1)SR1

Included with Unified CM

6921, 6941, 6945, and 6961

9.4(1)SR2

Included with Unified CM

9.4(1)SR1

Included with Unified CM

#### Cisco IP Phone 7800 Series

When upgrading from Firmware Release 10.3(1) to Firmware Release 11.0(1) or later, the K-Factor has been removed from the
                                             Call Details Record. This was intentional as Unified CM does not support RTP-RxStat messages greater than 256 characters in length.

Device Type

Device Release

Compatible Device Package

7811, 7821, 7841, and 7861

14.1(1)

cmterm-devicepack11.5.1

January 21, 2022

14.0(1)

cmterm-devicepack11.5.1

April 27, 2021

12.8(1)

cmterm-devicepack11.5.1

August 3, 2020

7832

14.1(1)

cmterm-devicepack11.5.1

January 21, 2022

14.0(1)

cmterm-devicepack11.5.1

April 27, 2021

12.8(1)

cmterm-devicepack11.5.1

August 3, 2020

#### Cisco Unified IP Phone 7900 Series

Device Type

Device Release

Compatible Device Package

7945G, 7965G, and 7975G

9.4(2)SR4

cmterm-devicepack11.5.1

August 3, 2020

7911G, 7931G, 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE,
                                             7962G, 7965G, and 7975G

9.4(2)SR3

cmterm-devicepack11.5.1

April 4, 2017

9.4(2)SR2

cmterm-devicepack11.5.1

August 22, 2016

7940G and 7960G

8.1(2)SR2

(SCCP)

Included with Unified CM

7915G and 7916G

1.0(4)

Included with Unified CM

7921G

1.4(6)

Included with Unified CM

1.4(5)

Included with Unified CM

7925G, 7925G-EX, and 7926G

1.4(8)SR1

cmterm-devicepack11.5.1

June 4, 2018

1.4(8)

Included with Unified CM

7937G

1.4(5)

Included with Unified CM

#### Cisco IP Phone 8800 Series

Device Type

Device Release

Compatible Device Package

8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR

14.1(1)

cmterm-devicepack11.5.1

January 21, 2022

14.0(1)

cmterm-devicepack11.5.1

April 27, 2021

12.8(1)

cmterm-devicepack11.5.1

August 3, 2020

8832

14.1(1)

cmterm-devicepack11.5.1

January 21, 2022

14.0(1)

cmterm-devicepack11.5.1

April 27, 2021

12.8(1)

cmterm-devicepack11.5.1

August 3, 2020

8831 and 8831NR

10.3(1)SR7.2

cmterm-devicepack11.5.1

January 19, 2022

10.3(1)SR7.2

cmterm-devicepack11.5.1

September 8, 2021

14.0(1)

cmterm-devicepack11.5.1

April 27, 2021

8821 and 8821-EX

11.0(6)SR2

cmterm-devicepack11.5.1

January 21, 2022

11.0(6)SR1

cmterm-devicepack11.5.1

April 27, 2021

11.0(6) QED files

cmterm-devicepack11.5.1

November 23, 2020

#### Cisco Unified IP Phone 8900 and 9900 Series

Device Type

Device Release

Compatible Device Package

8941 and 8945

9.4(2)SR3

cmterm-devicepack11.5.1

November 30, 2016

9.4(2)SR2

Included with Unified CM

8961, 9951, and 9971

9.4(2)SR2

Included with Unified CM

9.4(2)

Included with Unified CM

#### Cisco Analog Telephone Adapter

Device Type

Device Release

Compatible Device Package

Cisco VG450 Analog Voice Gateway

Cisco IOS XE 16.10.01a

cmterm-devicepack11.5.1

January 24, 2019

ATA 187

9.2(3)

SIP

Included with Unified CM

ATA 190

1.2.2

Included with Unified CM

1.2.1

Included with Unified CM

ATA 191

12.0(1)

cmterm-devicepack11.5.1

December 20, 2017

#### Cisco DX Series

After the October 11, 2019 device package, device packages don't contain any CE firmware.

Device Type

Device Release

Compatible Device Package

DX70 and DX80

CE9.8(1)

cmterm-devicepack11.5.1

October 11, 2019

CE9.7(1)

May 28, 2019

cmterm-devicepack11.5.1

DX650

10.2(5)

Included with Unified CM

10.2(4)

Included with Unified CM

#### Cisco TelePresence E, EX, C, SX, and MX Series

After the October 11, 2019 device package, device packages don't contain any CE firmware.

Device Type

Device Release

Compatible Device Package

C Series, EX Series, MX200, and MX300

TC7.3(3)

Included with Unified CM

TC7.2(0)

Included with Unified CM

MX200 G2, MX300 G2, MX700, MX800, MX800 Dual, SX10, SX20, and
                                             SX80

CE9.8(1)

cmterm-devicepack11.5.1

October 11, 2019

CE9.7(1)

cmterm-devicepack11.5.1

May 28, 2019

#### Cisco TelePresence IX5000

Device Type

Device Release

Compatible Device Package

Cisco TelePresence IX5000

Software IX 9.0

cmterm-devicepack11.5.1

August 13, 2018

Software IX 8.0

cmterm-devicepack11.5.1

December 20, 2017

#### Cisco Headset 500 Series

Device Type

Device Release

Compatible Device Package

Cisco Headset 500 Series

Cisco Options Package (COP) file: 2.3

Headset release: 2.3(1)

cmterm-devicepack11.5.1

September 8, 2021

COP file: 2.2

Headset release: 2.2(1)

cmterm-devicepack11.5.1

April 27, 2021

#### Cisco Headset 700 Series

Device Type

Device Release

Compatible Device Package

Cisco Options Package (COP) file: 2.3(1.13)

Headset release: 1-7-0-138

USB adapter release: 1-3-12

cmterm-devicepack11.5.1

January 21, 2022

COP file: 2.2(1.6)

Headset release: 1-6-0-150

USB adapter release: 1-2-33

cmterm-devicepack11.5.1

April 27, 2021

COP file: 2.1

Headset release: 1-5-0-246

USB adapter release: 1-1-59

cmterm-devicepack11.5.1

November 23, 2020

#### Webex Board

After the October 11, 2019 device package, device packages don't contain any CE firmware.

Device Type

Device Release

Compatible Device Package

Webex Board Pro 55 and 75

Cisco Webex RoomOS 10

cmterm-devicepack11.5.1

January 21, 2022

Cisco Webex Board 55, 70, and 85

CE9.8(1)

cmterm-devicepack11.5.1

March 4, 2020

CE9.8(1)

cmterm-devicepack11.5.1

October 11, 2019

#### Webex Desk

Device Type

Device Release

Compatible Device Package

Webex Desk Mini

QED files

cmterm-devicepack11.5.1

January 21, 2022

Webex Desk

QED files

cmterm-devicepack11.5.1

September 8, 2021

Webex Desk Hub

New product QED files

cmterm-devicepack11.5.1

September 8, 2021

Cisco Webex Desk Limited Edition

New product QED files

cmterm-devicepack11.5.1

April 27, 2021

Cisco Webex Desk Pro

New product QED files

cmterm-devicepack11.5.1

March 4, 2020

#### Webex Room

After the October 11, 2019 device package, device packages don't contain any CE
                                             firmware.

Device Type

Device Release

Compatible Device Package

Cisco Webex Room Panorama

New product QED files

cmterm-devicepack11.5.1

March 4, 2020

Cisco Webex Room Panorama 70

New product QED files

cmterm-devicepack11.5.1

March 4, 2020

Cisco Webex Room 70 Single and Cisco Webex Room 70 Dual

CE9.8(1)

cmterm-devicepack11.5.1

October 11, 2019

CE9.7(1)

cmterm-devicepack11.5.1

May 28, 2019

Cisco Webex Room 70 Single G2 and Cisco Webex Room 70 Dual G2

CE9.8(1)

cmterm-devicepack11.5.1

Oct. 11, 2019

CE9.7(1)

cmterm-devicepack11.5.1

May 28, 2019

Cisco Webex Room 55 and Cisco Webex Room 55 Dual

CE9.8(1)

cmterm-devicepack11.5.1

October 11, 2019

CE9.7(1)

cmterm-devicepack11.5.1

May 28, 2019

Cisco Webex Room Kit Mini

CE9.8(1)

cmterm-devicepack11.5.1

October 11, 2019

CE9.7(1)

cmterm-devicepack11.5.1

May 28, 2019

Cisco Webex Room Kit and Cisco Webex Room Kit Plus

CE9.8(1)

cmterm-devicepack11.5.1

October 11, 2019

CE9.7(1)

cmterm-devicepack11.5.1

May 28, 2019

Cisco Webex Room Kit Pro

CE9.8(1)

cmterm-devicepack11.5.1

October 11, 2019

CE9.7(1)

cmterm-devicepack11.5.1

May 28, 2019

Cisco Webex Room Phone

CSV file check in

cmterm-devicepack11.5.1

November 23, 2020

New Product QED File

cmterm-devicepack11.5.1

August 3, 2020

#### Webex Wireless Phone 840 and 860

Device Type

Device Release

Compatible Device Package

Webex Wireless Phone 840

QED file for 1.4(0)

cmterm-devicepack11.5.1

January 21, 2022

QED file for 1.3(0)

cmterm-devicepack11.5.1

September 8, 2021

New product QED file 1.2(0)

cmterm-devicepack11.5.1

April 27, 2021

Webex Wireless Phone 860

QED file for 1.4(0)

cmterm-devicepack11.5.1

January 21, 2022

QED file for 1.3(0)

cmterm-devicepack11.5.1

September 8, 2021

New product QED file 1.1(0)

cmterm-devicepack11.5.1

April 27, 2021

#### Cisco 4000 Series Integrated Services Routers

Device Type

Device Release

Compatible Device Package

Cisco 4461 Integrated Services Routers

Cisco IOS XE 16.9.1

cmterm-devicepack11.5.1

January 24, 2019

Cisco 4000 Series Integrated Services Routers

Cisco IOS XE 16.4.1

cmterm-devicepack11.5.1

October 18, 2017

#### Cisco Jabber

There are no device packages available for Unified CM 11.5(1) release. There are no more device packages that are planned for Jabber.

| Note | For information about a previous release, see Cisco Unified Communications Manager Device Package Compatibility Matrix - End of Software Maintenance . |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 7811, 7821, 7841, and 7861 | 14.1(1) | cmterm-devicepack14.0.1 January 21, 2022 |
| 7832 | 14.1(1) | cmterm-devicepack14.0.1 January 21, 2022 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR | 14.1(1) | cmterm-devicepack14.0.1 January 21, 2022 |
| 8832 | 14.1(1) | cmterm-devicepack14.0.1 January 21, 2022 |
| 8831 and 8831NR | 10.3(1)SR7.2 | cmterm-devicepack14.0.1 January 21, 2022 |
| 10.3(1)SR7.2 | cmterm-devicepack14.0.1 September 8, 2021 |
| 8821 and 8821-EX | 11.0(6)SR2 | cmterm-devicepack14.0.1 January 21, 2022 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Headset 500 Series | Cisco Options Package (COP) file: 2.3 Headset release: 2.3(1) | cmterm-devicepack14.0.1 September 8, 2021 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Headset 700 Series | Cisco Options Package (COP) file: 2.3(1.13) Headset release: 1-7-0-138 USB adapter release: 1-3-12 | cmterm-devicepack14.0.1 January 21, 2022 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Webex Board Pro 55 and 75 | Cisco Webex RoomOS 10 | cmterm-devicepack14.0.1 January 21, 2022 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Webex Desk Mini | QED files | cmterm-devicepack14.0.1 January 21, 2022 |
| Webex Desk | QED files | cmterm-devicepack14.0.1 September 8, 2021 |
| Webex Desk Hub | New product QED files | cmterm-devicepack14.0.1 September 8, 2021 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Webex Wireless Phone 840 | QED file for 1.4(0) | cmterm-devicepack14.0.1 January 21, 2022 |
| QED file for 1.3(0) | cmterm-devicepack14.0.1 September 8, 2021 |
| Webex Wireless Phone 860 | QED file for 1.4(0) | cmterm-devicepack14.0.1 January 21, 2022 |
| QED file for 1.3(0) | cmterm-devicepack14.0.1 September 8, 2021 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 3905 | 9.4(1)SR3 | cmterm-devicepack12.5.1 April 27, 2021 |
| 9.4(1)SR3 | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 6901 and 6911 | 9.3(1)SR2 | Included with Unified CM |
| 9.3(1)SR1 | Included with Unified CM |
| 6921, 6941, 6945, and 6961 | 9.4(1)SR2 | Included with Unified CM |
| 9.4(1)SR1 | Included with Unified CM |

| Note | When upgrading from Firmware Release 10.3(1) to Firmware Release 11.0(1) or later, the K-Factor has been removed from the
                                             Call Details Record. This was intentional as Unified CM does not support RTP-RxStat messages greater than 256 characters in length. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 7811, 7821, 7841, and 7861 | 14.1(1) | cmterm-devicepack12.5.1 January 21, 2022 |
| 14.0(1) | cmterm-devicepack12.5.1 April 27, 2021 |
| 12.8(1) | cmterm-devicepack12.5.1 August 3, 2020 |
| 7832 | 14.1(1) | cmterm-devicepack12.5.1 January 21, 2022 |
| 14.0(1) | cmterm-devicepack12.5.1 April 27, 2021 |
| 12.8(1) | cmterm-devicepack12.5.1 August 3, 2020 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 7945G, 7965G, and 7975G | 9.4(2)SR4 | cmterm-devicepack12.5.1 August 3, 2020 |
| 7911G, 7931G, 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE, 7962G, 7965G, and 7975G | 9.4(2)SR3 | Included with Unified CM |
| 9.4(2)SR2 | Included with Unified CM |
| 7940G and 7960G | 8.1(2)SR2 (SCCP) | Included with Unified CM |
| 7915G and 7916G | 1.0(4) | Included with Unified CM |
| 7925G, 7925G-EX, and 7926G | 1.4(8)SR1 | Included with Unified CM |
| 1.4(8) | Included with Unified CM |
| 7937G | 1.4(5) | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR | 14.1(1) | cmterm-devicepack12.5.1 January 21, 2022 |
| 14.0(1) | cmterm-devicepack12.5.1 April 27, 2021 |
| 12.8(1) | cmterm-devicepack12.5.1 August 3, 2020 |
| 8832 | 14.1(1) | cmterm-devicepack12.5.1 January 21, 2022 |
| 14.0(1) | cmterm-devicepack12.5.1 April 27, 2021 |
| 12.8(1) | cmterm-devicepack12.5.1 August 3, 2020 |
| 8831 and 8831NR | 10.3(1)SR7.2 | cmterm-devicepack12.5.1 January 21, 2022 |
| 10.3(1)SR7.2 | cmterm-devicepack12.5.1 September 8, 2021 |
| 14.0(1) | cmterm-devicepack12.5.1 April 27, 2021 |
| 8821 and 8821-EX | 11.0(6)SR2 | cmterm-devicepack12.5.1 January 21, 2022 |
| 11.0(6)SR1 | cmterm-devicepack12.5.1 April 27, 2021 |
| 11.0(6) QED files | cmterm-devicepack12.5.1 November 23, 2020 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8941 and 8945 | 9.4(2)SR3 | Included with Unified CM |
| 9.4(2)SR2 | Included with Unified CM |
| 8961, 9951, and 9971 | 9.4(2)SR2 | Included with Unified CM |
| 9.4(2) | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco VG450 Analog Voice Gateway | Cisco IOS XE 16.10.01a | Included with Unified CM |
| ATA 187 | 9.2(3) SIP | Included with Unified CM |
| ATA 190 | 1.2.2 | Included with Unified CM |
| 1.2.1 | Included with Unified CM |
| ATA 191 | 12.0(1) | Included with Unified CM |

| Note | After the September 30, 2019 device package, device packages don't contain any CE firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| DX70 and DX80 | New xAPIformat files for the CE product line | cmterm-devicepack12.5.1 August 3, 2020 |
| CE9.8(1) | Included with Unified CM |
| CE9.7(1) | Included with Unified CM |
| DX650 | 10.2(5) | Included with Unified CM |
| 10.2(4) | Included with Unified CM |

| Note | Cisco Webex DX80 and Cisco Telepresence DX80 are different names for the same product. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco TelePresence IX5000 | Software IX 9.0 | Included with Unified CM |
| Software IX 8.0 | Included with Unified CM |

| Note | After the September 30, 2019 device package, device packages don't contain any CE firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| C Series, EX Series, MX200, and MX300 | TC7.3(3) | Included with Unified CM |
| TC7.2(0) | Included with Unified CM |
| MX200 G2, MX300 G2, MX700, MX800, MX800 Dual, SX10, SX20, and SX80 | New xAPIformat files for the CE product line | cmterm-devicepack12.5.1 August 3, 2020 |
| CE9.8(1) | cmterm-devicepack12.5.1 September 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.5.1 May 28, 2019 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Headset 500 Series | Cisco Options Package (COP) file: 2.3 Headset release: 2.3(1) | cmterm-devicepack12.5.1 September 8, 2021 |
| COP file: 2.2 Headset release: 2.2(1) | cmterm-devicepack12.5.1 April 27, 2021 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Headset 700 Series | Cisco Options Package (COP) file: 2.3(1.13) Headset release: 1-7-0-138 USB adapter release: 1-3-12 | cmterm-devicepack12.5.1 January 21, 2022 |
| COP file: 2.2(1.6) Headset release: 1-6-0-150 USB adapter release: 1-2-33 | cmterm-devicepack12.5.1 April 27, 2021 |
| COP file: 2.1 Headset release: 1-5-0-246 USB adapter release: 1-1-59 | cmterm-devicepack12.5.1 November 23, 2020 |

| Note | After the September 30, 2019 device package, device packages don't contain any CE firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Webex Board Pro 55 and 75 | Cisco Webex RoomOS 10 | cmterm-devicepack12.5.1 January 21, 2022 |
| Cisco Webex Board 55, 70, and 85 | New xAPIformat files for the CE product line | cmterm-devicepack12.5.1 August 3, 2020 |
| CE9.8(1) | cmterm-devicepack12.5.1 March 4, 2020 |
| CE9.8(1) | cmterm-devicepack12.5.1 September 30, 2019 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Webex Desk Mini | QED files | cmterm-devicepack12.5.1 January 21, 2022 |
| Webex Desk | QED files | cmterm-devicepack12.5.1 September 8, 2021 |
| Webex Desk Hub | New product QED files | cmterm-devicepack12.5.1 September 8, 2021 |
| Cisco Webex Desk Limited Edition | New product QED files | cmterm-devicepack12.5.1 April 27, 2021 |

| Note | After the September 30, 2019 device package, device packages don't contain any CE firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| All Webex Room devices with CE firmware | New xAPIformat files for the CE product line | cmterm-devicepack12.5.1 August 3, 2020 |
| Cisco Webex Desk Pro | New product QED files | cmterm-devicepack12.5.1 March 4, 2020 |
| Cisco Webex Room Panorama | New product QED files | cmterm-devicepack12.5.1 March 4, 2020 |
| Cisco Webex Room Panorama 70 | New product QED files | cmterm-devicepack12.5.1 March 4, 2020 |
| Cisco Webex Room 70 Single and Cisco Webex Room 70 Dual | CE9.8(1) | cmterm-devicepack12.5.1 September 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.5.1 May 28, 2019 |
| Cisco Webex Room 70 Single G2 and Cisco Webex Room 70 Dual G2 | CE9.8(1) | cmterm-devicepack12.5.1 September 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.5.1 May 28, 2019 |
| Cisco Webex Room 55 and Cisco Webex Room 55 Dual | CE9.8(1) | cmterm-devicepack12.5.1 September 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.5.1 May 28, 2019 |
| Cisco Webex Room Kit Mini | CE9.8(1) | cmterm-devicepack12.5.1 September 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.5.1 May 28, 2019 |
| Cisco Webex Room Kit and Cisco Webex Room Kit Plus | CE9.8(1) | cmterm-devicepack12.5.1 September 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.5.1 May 28, 2019 |
| Cisco Webex Room Kit Pro | CE9.8(1) | cmterm-devicepack12.5.1 September 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.5.1 May 28, 2019 |
| Cisco Webex Room Phone | CSV file check in | cmterm-devicepack12.5.1 November 23, 2020 |
| New Product QED File | cmterm-devicepack12.5.1 August 3, 2020 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Webex Wireless Phone 840 | QED file for 1.4(0) | cmterm-devicepack12.5.1 January 21, 2022 |
| QED file for 1.3(0) | cmterm-devicepack12.5.1 September 8, 2021 |
| New product QED file 1.2(0) | cmterm-devicepack12.5.1 April 27, 2021 |
| Webex Wireless Phone 860 | QED file for 1.4(0) | cmterm-devicepack12.5.1 January 21, 2022 |
| QED file for 1.3(0) | cmterm-devicepack12.5.1 September 8, 2021 |
| New product QED file 1.1(0) | cmterm-devicepack12.5.1 April 27, 2021 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco 4461 Integrated Services Routers | Cisco IOS XE 16.9.1 | Included with Unified CM |
| Cisco 4000 Series Integrated Services Routers | Cisco IOS XE 16.4.1 | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 3905 | 9.4(1)SR3 | cmterm-devicepack11.5.1 April 27, 2021 |
| 9.4(1)SR3 | cmterm-devicepack11.5.1 January 24, 2019 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 6901 and 6911 | 9.3(1)SR2 | Included with Unified CM |
| 9.3(1)SR1 | Included with Unified CM |
| 6921, 6941, 6945, and 6961 | 9.4(1)SR2 | Included with Unified CM |
| 9.4(1)SR1 | Included with Unified CM |

| Note | When upgrading from Firmware Release 10.3(1) to Firmware Release 11.0(1) or later, the K-Factor has been removed from the
                                             Call Details Record. This was intentional as Unified CM does not support RTP-RxStat messages greater than 256 characters in length. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 7811, 7821, 7841, and 7861 | 14.1(1) | cmterm-devicepack11.5.1 January 21, 2022 |
| 14.0(1) | cmterm-devicepack11.5.1 April 27, 2021 |
| 12.8(1) | cmterm-devicepack11.5.1 August 3, 2020 |
| 7832 | 14.1(1) | cmterm-devicepack11.5.1 January 21, 2022 |
| 14.0(1) | cmterm-devicepack11.5.1 April 27, 2021 |
| 12.8(1) | cmterm-devicepack11.5.1 August 3, 2020 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 7945G, 7965G, and 7975G | 9.4(2)SR4 | cmterm-devicepack11.5.1 August 3, 2020 |
| 7911G, 7931G, 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE,
                                             7962G, 7965G, and 7975G | 9.4(2)SR3 | cmterm-devicepack11.5.1 April 4, 2017 |
| 9.4(2)SR2 | cmterm-devicepack11.5.1 August 22, 2016 |
| 7940G and 7960G | 8.1(2)SR2 (SCCP) | Included with Unified CM |
| 7915G and 7916G | 1.0(4) | Included with Unified CM |
| 7921G | 1.4(6) | Included with Unified CM |
| 1.4(5) | Included with Unified CM |
| 7925G, 7925G-EX, and 7926G | 1.4(8)SR1 | cmterm-devicepack11.5.1 June 4, 2018 |
| 1.4(8) | Included with Unified CM |
| 7937G | 1.4(5) | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR | 14.1(1) | cmterm-devicepack11.5.1 January 21, 2022 |
| 14.0(1) | cmterm-devicepack11.5.1 April 27, 2021 |
| 12.8(1) | cmterm-devicepack11.5.1 August 3, 2020 |
| 8832 | 14.1(1) | cmterm-devicepack11.5.1 January 21, 2022 |
| 14.0(1) | cmterm-devicepack11.5.1 April 27, 2021 |
| 12.8(1) | cmterm-devicepack11.5.1 August 3, 2020 |
| 8831 and 8831NR | 10.3(1)SR7.2 | cmterm-devicepack11.5.1 January 19, 2022 |
| 10.3(1)SR7.2 | cmterm-devicepack11.5.1 September 8, 2021 |
| 14.0(1) | cmterm-devicepack11.5.1 April 27, 2021 |
| 8821 and 8821-EX | 11.0(6)SR2 | cmterm-devicepack11.5.1 January 21, 2022 |
| 11.0(6)SR1 | cmterm-devicepack11.5.1 April 27, 2021 |
| 11.0(6) QED files | cmterm-devicepack11.5.1 November 23, 2020 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8941 and 8945 | 9.4(2)SR3 | cmterm-devicepack11.5.1 November 30, 2016 |
| 9.4(2)SR2 | Included with Unified CM |
| 8961, 9951, and 9971 | 9.4(2)SR2 | Included with Unified CM |
| 9.4(2) | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco VG450 Analog Voice Gateway | Cisco IOS XE 16.10.01a | cmterm-devicepack11.5.1 January 24, 2019 |
| ATA 187 | 9.2(3) SIP | Included with Unified CM |
| ATA 190 | 1.2.2 | Included with Unified CM |
| 1.2.1 | Included with Unified CM |
| ATA 191 | 12.0(1) | cmterm-devicepack11.5.1 December 20, 2017 |

| Note | After the October 11, 2019 device package, device packages don't contain any CE firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| DX70 and DX80 | CE9.8(1) | cmterm-devicepack11.5.1 October 11, 2019 |
| CE9.7(1) | May 28, 2019 cmterm-devicepack11.5.1 |
| DX650 | 10.2(5) | Included with Unified CM |
| 10.2(4) | Included with Unified CM |

| Note | After the October 11, 2019 device package, device packages don't contain any CE firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| C Series, EX Series, MX200, and MX300 | TC7.3(3) | Included with Unified CM |
| TC7.2(0) | Included with Unified CM |
| MX200 G2, MX300 G2, MX700, MX800, MX800 Dual, SX10, SX20, and
                                             SX80 | CE9.8(1) | cmterm-devicepack11.5.1 October 11, 2019 |
| CE9.7(1) | cmterm-devicepack11.5.1 May 28, 2019 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco TelePresence IX5000 | Software IX 9.0 | cmterm-devicepack11.5.1 August 13, 2018 |
| Software IX 8.0 | cmterm-devicepack11.5.1 December 20, 2017 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Headset 500 Series | Cisco Options Package (COP) file: 2.3 Headset release: 2.3(1) | cmterm-devicepack11.5.1 September 8, 2021 |
| COP file: 2.2 Headset release: 2.2(1) | cmterm-devicepack11.5.1 April 27, 2021 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Headset 700 Series | Cisco Options Package (COP) file: 2.3(1.13) Headset release: 1-7-0-138 USB adapter release: 1-3-12 | cmterm-devicepack11.5.1 January 21, 2022 |
| COP file: 2.2(1.6) Headset release: 1-6-0-150 USB adapter release: 1-2-33 | cmterm-devicepack11.5.1 April 27, 2021 |
| COP file: 2.1 Headset release: 1-5-0-246 USB adapter release: 1-1-59 | cmterm-devicepack11.5.1 November 23, 2020 |

| Note | After the October 11, 2019 device package, device packages don't contain any CE firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Webex Board Pro 55 and 75 | Cisco Webex RoomOS 10 | cmterm-devicepack11.5.1 January 21, 2022 |
| Cisco Webex Board 55, 70, and 85 | CE9.8(1) | cmterm-devicepack11.5.1 March 4, 2020 |
| CE9.8(1) | cmterm-devicepack11.5.1 October 11, 2019 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Webex Desk Mini | QED files | cmterm-devicepack11.5.1 January 21, 2022 |
| Webex Desk | QED files | cmterm-devicepack11.5.1 September 8, 2021 |
| Webex Desk Hub | New product QED files | cmterm-devicepack11.5.1 September 8, 2021 |
| Cisco Webex Desk Limited Edition | New product QED files | cmterm-devicepack11.5.1 April 27, 2021 |
| Cisco Webex Desk Pro | New product QED files | cmterm-devicepack11.5.1 March 4, 2020 |

| Note | After the October 11, 2019 device package, device packages don't contain any CE
                                             firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Webex Room Panorama | New product QED files | cmterm-devicepack11.5.1 March 4, 2020 |
| Cisco Webex Room Panorama 70 | New product QED files | cmterm-devicepack11.5.1 March 4, 2020 |
| Cisco Webex Room 70 Single and Cisco Webex Room 70 Dual | CE9.8(1) | cmterm-devicepack11.5.1 October 11, 2019 |
| CE9.7(1) | cmterm-devicepack11.5.1 May 28, 2019 |
| Cisco Webex Room 70 Single G2 and Cisco Webex Room 70 Dual G2 | CE9.8(1) | cmterm-devicepack11.5.1 Oct. 11, 2019 |
| CE9.7(1) | cmterm-devicepack11.5.1 May 28, 2019 |
| Cisco Webex Room 55 and Cisco Webex Room 55 Dual | CE9.8(1) | cmterm-devicepack11.5.1 October 11, 2019 |
| CE9.7(1) | cmterm-devicepack11.5.1 May 28, 2019 |
| Cisco Webex Room Kit Mini | CE9.8(1) | cmterm-devicepack11.5.1 October 11, 2019 |
| CE9.7(1) | cmterm-devicepack11.5.1 May 28, 2019 |
| Cisco Webex Room Kit and Cisco Webex Room Kit Plus | CE9.8(1) | cmterm-devicepack11.5.1 October 11, 2019 |
| CE9.7(1) | cmterm-devicepack11.5.1 May 28, 2019 |
| Cisco Webex Room Kit Pro | CE9.8(1) | cmterm-devicepack11.5.1 October 11, 2019 |
| CE9.7(1) | cmterm-devicepack11.5.1 May 28, 2019 |
| Cisco Webex Room Phone | CSV file check in | cmterm-devicepack11.5.1 November 23, 2020 |
| New Product QED File | cmterm-devicepack11.5.1 August 3, 2020 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Webex Wireless Phone 840 | QED file for 1.4(0) | cmterm-devicepack11.5.1 January 21, 2022 |
| QED file for 1.3(0) | cmterm-devicepack11.5.1 September 8, 2021 |
| New product QED file 1.2(0) | cmterm-devicepack11.5.1 April 27, 2021 |
| Webex Wireless Phone 860 | QED file for 1.4(0) | cmterm-devicepack11.5.1 January 21, 2022 |
| QED file for 1.3(0) | cmterm-devicepack11.5.1 September 8, 2021 |
| New product QED file 1.1(0) | cmterm-devicepack11.5.1 April 27, 2021 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco 4461 Integrated Services Routers | Cisco IOS XE 16.9.1 | cmterm-devicepack11.5.1 January 24, 2019 |
| Cisco 4000 Series Integrated Services Routers | Cisco IOS XE 16.4.1 | cmterm-devicepack11.5.1 October 18, 2017 |