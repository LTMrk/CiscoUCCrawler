---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-compat-matrix-cmdp-bk-ccbda741-00-cucm-device-package-compatibility-mat-82ae4e1db5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix_chapter_01.html
retrieved_at: 2026-08-16T23:48:02.467177+00:00
---

Cisco Unified Communications Manager Device Package Compatibility Matrix

# Cisco Unified Communications Manager Device Package Compatibility Matrix

Updated: December 1, 2014

Chapter: End of Software Maintenance Cisco Unified Communications Manager Device Package Releases

## Chapter: End of Software Maintenance Cisco Unified Communications Manager Device Package Releases

# End of Software Maintenance Cisco Unified Communications Manager Device Package Releases

## Cisco Unified
                           				Communications Manager Device Package Compatibility Matrix - End of Software Maintenance

This section provides information about Cisco Unified
                                 				Communications Manager ( Unified CM ) device packages for Unified CM releases that have reached End of Software Maintenance . Hence, there will not be any device packages that are released in future for these Unified CM releases. Use this section to obtain device packages for:

Unified CM 12.0(1)

Unified CM 11.0(1)

Unified CM 10.5(2)

Unified CM 10.5(1)

Unified CM 10.0(1)

Unified CM 9.1(2)

A device package introduces new phone types to Unified CM , and installs the firmware and configuration files that enable features for your Cisco device. New features may be off by
                              default, and have attributes or settings that you must configure.

Device packages are available from the Cisco Unified
                                 				Communications Manager software download page. To obtain a device package, click the Unified CM device package link in the table, and a new browser window or tab opens. You will need your Cisco login.

For the latest device package releases, see Cisco Unified Communications Manager Device Package Compatibility Matrix - Current .

### Cisco Unified
                              				Communications Manager 12.0(1)

This section provides details about the compatible device packages for Cisco Unified
                                    				Communications Manager ( Unified CM ) 12.0(1) release. Each row in a table provides the device package information for a particular device and firmware release.

Unified CM device packages contain both configuration files and firmware files, except in certain cases as indicated in the table titles.

#### Cisco Unified SIP Phone 3905

Device Type

Device Release

Compatible Device Package

3905

9.4(1)SR3

cmterm-devicepack12.0.1

April 27, 2021

9.4(1)SR3

cmterm-devicepack12.0.1

February 4, 2019

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

14.0(1)

cmterm-devicepack12.0.1

April 27, 2021

12.8(1)

cmterm-devicepack12.0.1

August 3, 2020

12.7(1)

cmterm-devicepack12.0.1

March 4, 2019

7832

14.0(1)

cmterm-devicepack12.0.1

April 27, 2021

12.8(1)

cmterm-devicepack12.0.1

August 3, 2020

12.7(1)

cmterm-devicepack12.0.1

March 4, 2019

#### Cisco Unified IP Phone 7900 Series

Device Type

Device Release

Compatible Device Package

7945G, 7965G, and 7975G

9.4(2)SR4

cmterm-devicepack12.0.1

August 3, 2020

7911G, 7931G, 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE,
                                             7962G, 7965G, and 7975G

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

cmterm-devicepack12.0.1

May 28, 2018

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

14.0(1)

cmterm-devicepack12.0.1

April 27, 2021

12.8(1)

cmterm-devicepack12.0.1

August 3, 2020

12.7(1)

cmterm-devicepack12.0.1

March 4, 2019

8832

14.0(1)

cmterm-devicepack12.0.1

April 27, 2021

12.8(1)

cmterm-devicepack12.0.1

August 3, 2020

12.7(1)

cmterm-devicepack12.0.1

March 4, 2019

8831 and 8831NR

14.0(1)

cmterm-devicepack12.0.1

April 27, 2021

10.3(1)SR6

cmterm-devicepack12.0.1

August 3, 2020

10.3(1)SR3

cmterm-devicepack12.0.1

August 7, 2018

8821 and 8821-EX

11.0(6)SR1

cmterm-devicepack12.0.1

April 27, 2021

11.0(6) QED files

cmterm-devicepack12.0.1

November 23, 2020

11.0(5)SR3

cmterm-devicepack12.0.1

August 3, 2020

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

cmterm-devicepack12.0.1

February 4, 2019

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

cmterm-devicepack12.0.1

December 27, 2017

#### Cisco DX Series

After the September 30, 2019 device package, device packages don't contain any CE
                                             firmware.

Device Type

Device Release

Compatible Device Package

DX70 and DX80

CE9.8(1)

cmterm-devicepack12.0.1

September 30, 2019

CE9.7(1)

cmterm-devicepack12.0.1

May 28, 2019

DX650

10.2(5)

Included with Unified CM

10.2(4)

Included with Unified CM

#### Cisco TelePresence IX5000

Device Type

Device Release

Compatible Device Package

Cisco TelePresence IX5000

Software IX 9.0

cmterm-devicepack12.0.1

August 7, 2018

Software IX 8.0

cmterm-devicepack12.0.1

December 27, 2017

#### Cisco TelePresence E, EX, C, SX, and MX Series

After the September 30, 2019 device package, device packages don't contain any CE
                                             firmware.

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

cmterm-devicepack12.0.1

September 30, 2019

CE9.7(1)

cmterm-devicepack12.0.1

May 28, 2019

#### Cisco Webex Room

After the September 30, 2019 device package, device packages don't contain any CE
                                             firmware.

Device Type

Device Release

Compatible Device Package

Cisco Webex Desk Limited Edition

New product QED files

cmterm-devicepack12.0.1

April 27, 2021

Cisco Webex Desk Pro

New product QED files

cmterm-devicepack12.0.1

March 4, 2019

Cisco Webex Room Panorama

New product QED files

cmterm-devicepack12.0.1

March 4, 2019

Cisco Webex Room Panorama 70

New product QED files

cmterm-devicepack12.0.1

March 4, 2019

Cisco Webex Room 70 Single and Cisco Webex Room 70 Dual

CE9.8(1)

cmterm-devicepack12.0.1

September 30, 2019

CE9.7(1)

cmterm-devicepack12.0.1

May 28, 2019

Cisco Webex Room 70 Single G2 and Cisco Webex Room 70 Dual G2

CE9.8(1)

cmterm-devicepack12.0.1

September 30, 2019

CE9.7(1)

cmterm-devicepack12.0.1

May 28, 2019

Cisco Webex Room 55 and Cisco Webex Room 55 Dual

CE9.8(1)

cmterm-devicepack12.0.1

September 30, 2019

CE9.7(1)

cmterm-devicepack12.0.1

May 28, 2019

Cisco Webex Room Kit Mini

CE9.8(1)

cmterm-devicepack12.0.1

Sept. 30, 2019

CE9.7(1)

cmterm-devicepack12.0.1

May 28, 2019

Cisco Webex Room Kit and Cisco Webex Room Kit Plus

CE9.8(1)

cmterm-devicepack12.0.1

September 30, 2019

CE9.7(1)

cmterm-devicepack12.0.1

May 28, 2019

Cisco Webex Room Kit Pro

CE9.8(1)

cmterm-devicepack12.0.1

September 30, 2019

CE9.7(1)

cmterm-devicepack12.0.1

May 28, 2019

Cisco Webex Room Phone

CSV file check in

cmterm-devicepack12.0.1

November 23, 2020

New Product QED File

cmterm-devicepack12.0.1

August 3, 2020

#### Cisco Webex Board

After the September 30, 2019 device package, device packages don't contain any CE
                                             firmware.

Device Type

Device Release

Compatible Device Package

Cisco Webex Board 55, 70, and 85

CE9.8(1)

cmterm-devicepack12.0.1

March 4, 2019

CE9.8(1)

cmterm-devicepack12.0.1

September 30, 2019

#### Cisco Headset 500 Series

Device Type

Device Release

Compatible Device Package

Cisco Headset 500 Series

Cisco Options Package (COP) file: 2.2

Headset release: 2.2(1)

cmterm-devicepack12.0.1

April 27, 2021

COP file: 2.1

Headset release: 2.1(1)

cmterm-devicepack12.0.1

August 3, 2020

#### Cisco Headset 700 Series

Device Type

Device Release

Compatible Device Package

Cisco Headset 700 Series

Cisco Options Package (COP) file: 2.2(1.6)

Headset release: 1-6-0-150

USB adapter release: 1-2-33

cmterm-devicepack12.0.1

April 27, 2021

COP file: 2.1

Headset release: 1-5-0-246

USB adapter release: 1-1-59

cmterm-devicepack12.0.1

November 23, 2020

#### Cisco 4000 Series Integrated Services Routers

Device Type

Device Release

Compatible Device Package

Cisco 4461 Integrated Services Routers

Cisco IOS XE 16.9.1

cmterm-devicepack12.0.1

February 4, 2019

Cisco 4000 Series Integrated Services Routers

Cisco IOS XE 16.4.1

cmterm-devicepack12.0.1

November 7, 2017

#### Cisco Jabber

There are no device packages available for Unified CM 12.0(1) release. There are no more device packages that are planned for Jabber.

### Cisco Unified
                              				Communications Manager 11.0(1)

This section provides details about the compatible device packages for Cisco Unified
                                    				Communications Manager ( Unified CM ) 11.0(1) release. Each row in a table provides the device package information for a particular device and firmware release.

Unified CM device packages contain both configuration files and firmware files, except in certain cases as indicated in the table titles.

#### Cisco Unified SIP Phone 3905

Device Type

Device Release

Compatible Device Package

3905

9.4(1)SR3

No device package available

9.4(1)SR2

cmterm-devicepack11.0.1

December 21, 2015

#### Cisco Unified IP Phone 6900 Series

Device Type

Device Release

Compatible Device Package

6901 and 6911

9.3(1)SR2

Included with Unified CM

9.3(1)SR1

Not applicable

6921, 6941, 6945, and 6961

9.4(1)SR2

cmterm-devicepack11.0.1

September 3, 2015

9.4(1)SR1

Included with Unified CM

#### Cisco IP Phone 7800 Series

When upgrading from Firmware Release 10.3(1) to Firmware Release 11.0(1), the K-Factor is removed from the Call Details Record.
                                             This was intentional as Cisco Unified
                                                				Communications Manager does not support RTP-RxStat messages greater than 256 characters in length.

Device Type

Device Release

Compatible Device Package

7811, 7821, 7841, and 7861

12.5(1)SR2

No device package available

12.1(1)

cmterm-devicepack11.0.1

June 11, 2018

7832

12.5(1)SR2

No device package available

12.0(1)

cmterm-devicepack11.0.1

October 4, 2017

#### Cisco Unified IP Phone 7900 Series

Device Type

Device Release

Compatible Device Package

7911G, 7931G, 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE, 7962G, 7965G, and 7975G

9.4(2)SR3

cmterm-devicepack11.0.1

April 4, 2017

9.4(2)SR2

cmterm-devicepack11.0.1

August 24, 2016

7940G and 7960G

8.1(2)SR2 (SCCP)

Included with Unified CM

7915G and 7916G

1.0(4)

Included with Unified CM

7921G

1.4(6)

Included with Unified CM

7925G, 7925G-EX, and 7926G

1.4(8)SR1

cmterm-devicepack11.0.1

June 11, 2018

1.4(8)

cmterm-devicepack11.0.1

May 10, 2016

7937G

1.4(5)

Included with Unified CM

#### Cisco IP Phone 8800 Series

Device Type

Device Release

Compatible Device Package

8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR

12.5(1)SR2

No device package available

12.1(1)

cmterm-devicepack11.0.1

June 11, 2018

8832

12.5(1)SR2

No device package available

12.1(1)

cmterm-devicepack11.0.1

June 11, 2018

8831 and 8831NR

10.3(1)SR3

cmterm-devicepack11.0.1

August 7, 2018

10.3(1)SR2

cmterm-devicepack11.0.1

January 7, 2016

8821

11.0(5)

No device package available

11.0(4)SR2

No device package available

#### Cisco Unified IP Phone 8900 and 9900 Series

Device Type

Device Release

Compatible Device Package

8941 and 8945

9.4(2)SR3

cmterm-devicepack11.0.1

November 30, 2016

9.4(2)SR2

cmterm-devicepack11.0.1

October 28, 2015

8961, 9951, and 9971

9.4(2)SR2

cmterm-devicepack11.0.1

October 1, 2015

9.4(2)

Included with Unified CM

#### Cisco Analog Telephone Adapter

Device Type

Device Release

Compatible Device Package

Cisco VG450 Analog Voice Gateway

Cisco IOS XE 16.10.01a

No device package available

ATA 187

9.2(3) SIP

Included with Unified CM

ATA 190

1.2.2

cmterm-devicepack11.0.1

July 11, 2016

1.2.1

cmterm-devicepack11.0.1

September 3, 2015

ATA 191

12.0(1)

cmterm-devicepack11.0.1

December 27, 2017

#### Cisco DX Series

Device Type

Device Release

Compatible Device Package

DX70 and DX80

CE9.7(1)

No device package available

CE9.6(1)

No device package available

DX650

10.2(5)

cmterm-devicepack11.0.1

September 3, 2015

10.2(4)

Included with Unified CM

#### Cisco TelePresence IX5000

Device Type

Device Release

Compatible Device Package

Cisco TelePresence IX5000

Software IX 9.0

cmterm-devicepack11.0.1

August 7, 2018

Software IX 8.0

cmterm-devicepack11.0.1

December 27, 2017

#### Cisco TelePresence E, EX, C, SX, and MX Series

Device Type

Device Release

Compatible Device Package

Cisco TelePresence MX and SX Series devices

CE9.7(1)

No Device Package available

CE9.4(0)

cmterm-devicepack11.0.1

August 7, 2018

Cisco TelePresence C Series, EX Series, MX200, and MX300

TC7.3(3)

Included with Unified CM

TC7.2(0)

Included with Unified CM

Cisco TelePresence MX200 G2, MX300 G2, MX700, MX800, MX800 Dual, SX10, and SX80

CE9.7(1)

No device package available

CE9.4(0)

cmterm-devicepack11.0.1

August 7, 2018

#### Cisco Webex Room

Device Type

Device Release

Compatible Device Package

Cisco Webex Room 70 (Single) and Cisco Webex Room 70 (Dual)

CE9.7(1)

No device package available

CE9.6(1)

No device package available

Cisco Webex Room 70 Single G2 and Cisco Webex Room 70 Dual G2

CE9.7(1)

No device package available

CE9.4(0)

cmterm-devicepack11.0.1

August 7, 2018

Cisco Webex Room 55

CE9.7(1)

No device package available

CE9.6(1)

No device package available

Cisco Webex Room 55 Dual

CE9.7(1)

No device package available

CE9.4(0)

cmterm-devicepack11.0.1

August 7, 2018

Cisco Webex Room Kit Mini

CE9.7(1)

No device package available

CE9.6(1)

No device package available

Cisco Webex Room Kit and Cisco Webex Room Kit Plus

CE9.7(1)

No device package available

CE9.6(1)

No device package available

Cisco Webex Room Kit Pro

CE9.7(1)

No device package available

CE9.6(1)

No device package available

#### Cisco 4000 Series Integrated Services Routers

Device Type

Device Release

Compatible Device Package

Cisco 4461 Integrated Services Routers

Cisco IOS XE 16.9.1

No device package available

Cisco 4000 Series Integrated Services Routers

Cisco IOS XE 16.4.1

No device package available

#### Cisco Jabber

There were no device packages available for Unified CM 11.0(1) release.

### Cisco Unified
                              				Communications Manager 10.5(2)

This section provides details about the compatible device packages for Cisco Unified
                                    				Communications Manager ( Unified CM ) 10.5(2) release. Each row in a table provides the device package information for a particular device and firmware release.

Unified CM device packages contain both configuration files and firmware files, except in certain cases as indicated in the table titles.

#### Cisco Unified SIP Phone 3905

Device Type

Device Release

Compatible Device Package

3905

9.4(1)SR3

cmterm-devicepack10.5.2

January 24, 2019

9.4(1)SR2

cmterm-devicepack10.5.2

December 21, 2015

#### Cisco Unified IP Phone 6900 Series

Device Type

Device Release

Compatible Device Package

6901 and 6911

9.3(1)SR2

cmterm-devicepack10.5.2

April 23, 2015

9.3(1)SR1

Included with Unified CM

6921, 6941, 6945, and 6961

9.4(1)SR2

cmterm-devicepack10.5.2

September 3, 2015

9.4(1)SR1

Included with Unified CM

#### Cisco IP Phone 7800 Series

When upgrading from Firmware Release 10.3(1) to Firmware Release 11.0(1) or later, the K-Factor has been removed from the
                                             Call Details Record. This was intentional as Cisco Unified Communications Manager does not support RTP-RxStat messages greater
                                             than 256 characters in length.

Device Type

Device Release

Compatible Device Package

7811, 7821, 7841, and 7861

12.8(1)

cmterm-devicepack10.5.2

August 3, 2020

12.7(1)

cmterm-devicepack10.5.2

March 4, 2020

12.6(1)

cmterm-devicepack10.5.2

October 11, 2019

7832

12.8(1)

cmterm-devicepack10.5.2

August 3, 2020

12.7(1)

cmterm-devicepack10.5.2

March 4, 2020

12.6(1)

cmterm-devicepack10.5.2

October 11, 2019

#### Cisco Unified IP Phone 7900 Series

Device Type

Device Release

Compatible Device Package

7945G, 7965G, and 7975G

9.4(2)SR4

cmterm-devicepack10.5.2

August 3, 2020

7911G, 7931G, 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE,
                                             7962G, 7965G, and 7975G

9.4(2)SR2

cmterm-devicepack10.5.2

August 22, 2016

7940G and 7960G

8.1(2)SR2 (SCCP)

Included with Unified CM

7915G and 7916G

1.0(4)

Included with Unified CM

7921G

1.4(6)

cmterm-devicepack10.5.2

April 23, 2015

1.4(5)

Included with Unified CM

7925G, 7925G-EX, and 7926G

1.4(8)SR1

cmterm-devicepack10.5.2

June 4, 2018

1.4(8)

cmterm-devicepack10.5.2

May 10, 2016

7937G

1.4(5)

Included with Unified CM

#### Cisco IP Phone 8800 Series

Device Type

Device Release

Compatible Device Package

8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR

12.8(1)

cmterm-devicepack10.5.2

August 3, 2020

12.7(1)

cmterm-devicepack10.5.2

March 4, 2020

12.6(1)

cmterm-devicepack10.5.2

October 11, 2019

8832

12.8(1)

cmterm-devicepack10.5.2

August 3, 2020

12.7(1)

cmterm-devicepack10.5.2

March 4, 2020

12.6(1)

cmterm-devicepack10.5.2

October 11, 2019

8831 and 8831NR

10.3(1)SR6

cmterm-devicepack10.5.2

August 3, 2020

10.3(1)SR3

cmterm-devicepack10.5.2

August 13, 2018

10.3(1)SR2

cmterm-devicepack10.5.2

January 7, 2016

8821 and 8821-EX

11.0(5)SR3

cmterm-devicepack10.5.2

August 3, 2020

11.0(5)SR2

cmterm-devicepack10.5.2

March 4, 2020

11.0(5)SR1

cmterm-devicepack10.5.2

October 11, 2019

#### Cisco Unified IP Phone 8900 and 9900 Series

Device Type

Device Release

Compatible Device Package

8941 and 8945

9.4(2)SR3

cmterm-devicepack10.5.2

November 30, 2016

9.4(2)SR2

cmterm-devicepack10.5.2

October 28, 2015

8961, 9951, and 9971

9.4(2)SR2

cmterm-devicepack10.5.2

October 1, 2015

9.4(2)

Included with Unified CM

#### Cisco Analog Telephone Adapter

Device Type

Device Release

Compatible Device Package

Cisco VG450 Analog Voice Gateway

Cisco IOS XE 16.10.01a

cmterm-devicepack10.5.2

January 24, 2019

ATA 187

9.2(3) SIP

Included with Unified CM

ATA 190

1.2.2

cmterm-devicepack10.5.2

July 7, 2016

1.2.1

cmterm-devicepack10.5.2

September 3, 2015

ATA 191

12.0(1)

cmterm-devicepack10.5.2

December 20, 2017

#### Cisco DX Series

After the October 11, 2019 device package, device packages don't contain any CE firmware.

Device Type

Device Release

Compatible Device Package

DX70 and DX80

CE9.8(1)

cmterm-devicepack10.5.2

October 11, 2019

CE9.7(1)

cmterm-devicepack10.5.2

May 28, 2019

DX650

10.2(5)

cmterm-devicepack10.5.2

September 3, 2015

10.2(4)

cmterm-devicepack10.5.2

May 28, 2015

#### Cisco Cius

Device Type

Device Release

Compatible Device Package

Cius

9.2(4)

Included with Unified CM

#### Cisco TelePresence IX5000

Device Type

Device Release

Compatible Device Package

Cisco TelePresence IX5000

Software IX 9.0

cmterm-devicepack10.5.2

August 13, 2018

Software IX 8.0

cmterm-devicepack10.5.2

December 20, 2017

#### Cisco TelePresence E, EX, C, SX, and MX Series

After the October 11, 2019 device package, device packages don't contain any CE
                                             firmware.

Device Type

Device Release

Compatible Device Package

C Series, EX Series, MX200, and MX300

TC7.3(3)

cmterm-devicepack10.5.2

May 28, 2015

TC7.2(0)

Included with Unified CM

MX200 G2, MX300 G2, MX700, MX800, MX800 Dual, SX10, SX20, and
                                             SX80

CE9.8(1)

cmterm-devicepack10.5.2

October 11, 2019

CE9.7(1)

cmterm-devicepack10.5.2

May 28, 2019

#### Cisco TelePresence CTS and TX Series

Device Type

Device Release

Compatible Device Package

Cisco TelePresence CTS and TX series

N/A

Included with Unified CM

#### Cisco Webex Room

After the October 11, 2019 device package, device packages don't contain any CE
                                             firmware.

Device Type

Device Release

Compatible Device Package

Cisco Webex Room Panorama

New product QED files

cmterm-devicepack10.5.2

March 4, 2020

Cisco Webex Room Panorama 70

New product QED files

cmterm-devicepack10.5.2

March 4, 2020

Cisco Webex Desk Pro

New product QED files

cmterm-devicepack10.5.2

March 4, 2020

Cisco Webex Room 70 Single and Cisco Webex Room 70 Dual

CE9.8(1)

cmterm-devicepack10.5.2

October 11, 2019

CE9.7(1)

cmterm-devicepack10.5.2

May 28, 2019

Cisco Webex Room 70 Single G2 and Cisco Webex Room 70 Dual G2

CE9.8(1)

cmterm-devicepack10.5.2

October 11, 2019

CE9.7(1)

cmterm-devicepack10.5.2

May 28, 2019

Cisco Webex Room 55 and Cisco Webex Room 55 Dual

CE9.8(1)

cmterm-devicepack10.5.2

October 11, 2019

CE9.7(1)

cmterm-devicepack10.5.2

May 28, 2019

Cisco Webex Room Kit Mini

CE9.8(1)

cmterm-devicepack10.5.2

October 11, 2019

CE9.7(1)

cmterm-devicepack10.5.2

May 28, 2019

Cisco Webex Room Kit and Cisco Webex Room Kit Plus

CE9.8(1)

cmterm-devicepack10.5.2

October 11, 2019

CE9.7(1)

cmterm-devicepack10.5.2

May 28, 2019

Cisco Webex Room Kit Pro

CE9.8(1)

cmterm-devicepack10.5.2

October 11, 2019

CE9.7(1)

cmterm-devicepack10.5.2

May 28, 2019

Cisco Webex Room Phone

New Product QED File

cmterm-devicepack10.5.2

August 3, 2020

#### Cisco Webex Board

After the October 11, 2019 device package, device packages don't contain any CE
                                             firmware.

Device Type

Device Release

Compatible Device Package

Cisco Webex Board 55, 70, and 85

CE9.8(1)

cmterm-devicepack10.5.2

March 4, 2020

CE9.8(1)

cmterm-devicepack10.5.2

October 11, 2019

#### Cisco Headset 500 Series

Device Type

Device Release

Compatible Device Package

Cisco Headset 500 Series

Cop file: 2.1

Headset release: 2.1(1)

cmterm-devicepack10.5.2

August 3, 2020

2.0

cmterm-devicepack10.5.2

March 4, 2020

1.5(1)

cmterm-devicepack10.5.2

October 11, 2019

#### Cisco Headset 700 Series

Device Type

Device Release

Compatible Device Package

Cisco Headset 700 Series

Cop file:2.1

Headset release: 1-3-0-246

cmterm-devicepack10.5.2

August 3, 2020

2.0

cmterm-devicepack10.5.2

March 4, 2020

The Cisco Headset 700 Series can be upgraded only using the
                                                         Cisco Headset mobile app.

#### Cisco 4000 Series Integrated Services Routers

Device Type

Device Release

Compatible Device Package

Cisco 4461 Integrated Services Routers

Cisco IOS XE 16.9.1

cmterm-devicepack10.5.2

January 24, 2019

Cisco 4000 Series Integrated Services Routers

Cisco IOS XE 16.4.1

cmterm-devicepack10.5.2

October 16, 2017

#### Cisco Jabber

There are no device packages available for Unified CM 10.5(2) release. More device packages for Jabber aren't planned.

Device Type

Device Release

Compatible Device Package

Cisco Jabber

10.6(0)

Included with Unified CM

9.1(1)

Included with Unified CM

### Cisco Unified
                              				Communications Manager 10.5(1)

This section provides details about the compatible device packages for Cisco Unified
                                    				Communications Manager ( Unified CM ) 10.5(1) release. Each row in a table provides the device package information for a particular device and firmware release.

Unified CM device packages contain both configuration files and firmware files, except in certain cases as indicated in the table titles.

#### Cisco Unified IP Phone 3900 Series

Device Type

Device Release

Compatible Device Package

3905

9.4(1) SR2

cmterm-devicepack10.5.1

November 25, 2014

9.4(1) SR1

cmterm-devicepack10.5.1

November 25, 2014

#### Cisco Unified IP Phone 6900 Series

Device Type

Device Release

Compatible Device Package

6901 and 6911

9.3(1)SR2

cmterm-devicepack10.5.1

December 22, 2014

9.3(1)SR1

Included with Unified CM

6921, 6941, 6945, and 6961

9.4(1)SR2

No device package available

9.4(1)SR1

Included with Unified CM

#### Cisco IP Phone 7800 Series

Device Type

Device Release

Compatible Device Package

7811, 7821, 7841, and 7861

12.5(1)SR2

No device package available

10.2(1)

cmterm-devicepack10.5.1

February 12, 2015

Configuration files on Unified CM (QED)

No device package available

#### Cisco Unified IP Phone 7900 Series

Device Type

Device Release

Compatible Device Package

7906G, 7911G, 7931G 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE, 7962G, 7965G, 7970G, 7971G-GE, and 7975G

9.4(2)SR3

No device package available

9.4(2)SR2

No device package available

9.4(2)SR1 QED

cmterm-devicepack10.5.1

December 22, 2014

7940G and 7960G

8.1(2)SR2 (SCCP)

Included with Unified CM

7915G and 7916G

1.0(4)

Included with Unified CM

7921G

1.4(6)

cmterm-devicepack10.5.1

September 23, 2014

1.4(5)

Included with Unified CM

7925G, 7925G-EX, and 7926G

1.4(6)

cmterm-devicepack10.5.1

September 23, 2014

1.4(5)

Included with Unified CM

7937G

1.4(5)

cmterm-devicepack10.5.1

September 30, 2014

#### Cisco IP Phone 8800 Series

Device Type

Device Release

Compatible Device Package

8831

10.3(1)SR3

No device package available

10.3(1)

cmterm-devicepack10.5.1

December 22, 2014

8811, 8841, 8851, 8851NR, and 8861

12.0(1)

No device package available

N/A

Resolves caveat CSCur67137

December 22, 2014

cmterm-devicepack10.5.1

Configuration files on Unified CM (QED)

No device package available

8845 and 8865

12.0(1)

No device package available

11.7(1)

No device package available

#### Cisco Unified IP Phone 8900 and 9900 Series

Device Type

Device Release

Compatible Device Package

8941 and 8945

9.4(2)SR3

No device package available

9.4(2)

cmterm-devicepack10.5.1

September 23, 2014

8961, 9951, and 9971

9.4(2)SR3

No device package available

9.4(2)

cmterm-devicepack10.5.1

October 30, 2014

#### Cisco Analog Telephone Adapter

Device Type

Device Release

Compatible Device Package

ATA 187

9.2(3) SIP

Included with Unified CM

ATA 190

1.2.2

No device package available

1.1.2(005)

No device package available

Configuration files on Unified CM (QED)

cmterm-devicepack10.5.1

July 24, 2014

#### Cisco DX Series

Device Type

Device Release

Compatible Device Package

DX70 and DX80

10.2(4)

No device package available

10.2(2)

cmterm-devicepack10.5.1

September 23, 2014

Configuration files on Unified CM (QED)

No device package available

DX650

10.2(4)

No device package available

10.2(2)

cmterm-devicepack10.5.1

September 23, 2014

#### Cisco Cius

Device Type

Device Release

Compatible Device Package

Cius

9.2(4)

No device package available

9.2(3)

No device package available

#### Cisco TelePresence IX5000

Device Type

Device Release

Compatible Device Package

Cisco TelePresence IX5000

Software IX 8.1

No device package available

#### Cisco TelePresence E, EX, C, SX, and MX Series

Device Type

Device Release

Compatible Device Package

MX700 and MX800

CE 8.0

No device package available

TC7.1(2)

cmterm-devicepack10.5.1

February 12, 2015

MX800 Dual

CE 8.0

No device package available

TC7.3(2)

cmterm-devicepack10.5.1

February 12, 2015

MX200 G2

TC7.1

Included with Unified CM

MX300 G2

TC7.0

Included with Unified CM

SX10

TC7.1

Included with Unified CM

SX80

TC7.1(2)

cmterm-devicepack10.5.1

February 12, 2015

#### Cisco TelePresence CTS and TX Series

Device Type

Device Release

Compatible Device Package

Cisco TelePresence CTS and TX series

Configuration files on Unified CM (QED)

Included with Unified CM

Adm. Capability Only

Included with Unified CM

#### Cisco Jabber

Device Type

Device Release

Compatible Device Package

Cisco Jabber

10.6(0)

cmterm-devicepack10.5.1

November 25, 2014

9.1(1)

Included with Unified CM

Adm. Capability Only

Included with Unified CM

### Cisco Unified
                              				Communications Manager 10.0(1)

This section provides details about the compatible device packages for Cisco Unified
                                    				Communications Manager ( Unified CM ) 10.0(1) release. Each row in a table provides the device package information for a particular device and firmware release.

Unified CM device packages contain both configuration files and firmware files, except in certain cases as indicated in the table titles.

#### Cisco Unified IP Phone 3900 Series

Device Type

Device Release

Compatible Device Package

3905

9.4(1) SR2

No device package available

9.4(1) SR1

No device package available

#### Cisco Unified IP Phone 6900 Series

Device Type

Device Release

Compatible Device Package

6901 and 6911

9.3(1)SR2

No device package available

9.3(1)SR1

No device package available

6921, 6941, and 6961

9.4(1)SR2

No device package available

9.4(1)SR1

cmterm-devicepack10.0.1

May 28, 2014

6945

9.4(1)SR2

No device package available

9.4(1)SR1

No device package available

#### Cisco IP Phone 7800 Series

Device Type

Device Release

Compatible Device Package

7811, 7821, 7841, and 7861

12.5(1)SR2

No device package available

10.1(1)SR1

cmterm-devicepack10.0.1

May 7, 2014

Configuration files on Unified CM (QED)

cmterm-devicepack10.0.1

March 18, 2014

#### Cisco Unified IP Phone 7900 Series

Device Type

Device Release

Compatible Device Package

7906G, 7911G, 7931G 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE, 7962G, 7965G, 7970G, 7971G-GE, and 7975G

9.4(2)SR3

No device package available

9.3(1)SR4

cmterm-devicepack10.0.1

March 18, 2014

7940G and 7960G

8.1(2)SR2 (SCCP)

No device package available

7915G and 7916G

1.0(4)

No device package available

7921G

1.4(6)

No device package available

1.4(5)

No device package available

7925G, 7925G-EX, and 7926G

1.4(6)

No device package available

1.4(5)

No device package available

7937G

1.4(5)

No device package available

#### Cisco IP Phone 8800 Series

Device Type

Device Release

Compatible Device Package

8831

10.3(1)SR3

No device package available

10.3(1)SR2

No device package available

8811, 8841, 8851, 8851NR, and 8861

12.5(1)SR2

No device package available

Configuration files on Unified CM (QED)

cmterm-devicepack10.0.1

May 28, 2014

8845 and 8865

12.5(1)SR2

No device package available

11.7(1)

No device package available

#### Cisco Unified IP Phone 8900 and 9900 Series

Device Type

Device Release

Compatible Device Package

8941 and 8945

9.4(2)SR3

No device package available

9.4(2)SR2

No device package available

8961, 9951, and 9971

9.4(2)SR3

No device package available

9.4(2)SR2

No device package available

#### Cisco Analog Telephone Adapter

Device Type

Device Release

Compatible Device Package

ATA 187

9.2(3) SIP

No device package available

ATA 190

1.2.2

No device package available

1.1.2(005)

No device package available

#### Cisco DX Series

Device Type

Device Release

Compatible Device Package

DX70 and DX80

10.2(4)

No device package available

10.2(2)

No device package available

Configuration files on Unified CM (QED)

cmterm-devicepack10.0.1

May 28, 2014

DX650

10.2(4)

No device package available

10.2(2)

No device package available

10.1(2)

cmterm-devicepack10.0.1

May 28, 2014

#### Cisco Cius

Device Type

Device Release

Compatible Device Package

Cius

9.2(4)

No device package available

9.2(3)

No device package available

#### Cisco TelePresence IX5000

Device Type

Device Release

Compatible Device Package

Cisco TelePresence IX5000

Software IX 8.1

No device package available

#### Cisco TelePresence E, EX, C, SX, and MX Series

Device Type

Device Release

Compatible Device Package

MX700 and MX800

CE 8.0

No device package available

TC7.1(2)

cmterm-devicepack10.0.1

May 28, 2014

MX800 Dual

CE 8.0

No device package available

TC7.3(3)

No device package available

MX300 G2

TC7.0

cmterm-devicepack10.0.1

May 7, 2014

MX200 G2

TC7.1

cmterm-devicepack10.0.1

May 7, 2014

SX10 and SX80

TC7.1

cmterm-devicepack10.0.1

May 7, 2014

Configuration files on Unified CM (QED)

cmterm-devicepack10.0.1

March 18, 2014

#### Cisco TelePresence CTS and TX Series

Device Type

Device Release

Compatible Device Package

Cisco TelePresence CTS and TX series

Configuration files on Unified CM (QED)

Included with Unified CM

Adm. Capability Only

Included with Unified CM

#### Cisco Jabber

Device Type

Device Release

Compatible Device Package

Cisco Jabber

10.6(0)

cmterm-devicepack10.5.1

November 25, 2014

9.1(1)

Included with Unified CM

Adm. Capability Only

Included with Unified CM

### Cisco Unified
                              				Communications Manager 9.1(2)

There are no device packages available for Cisco Unified
                                    				Communications Manager 9.1(2) release.

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 3905 | 9.4(1)SR3 | cmterm-devicepack12.0.1 April 27, 2021 |
| 9.4(1)SR3 | cmterm-devicepack12.0.1 February 4, 2019 |

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
| 7811, 7821, 7841, and 7861 | 14.0(1) | cmterm-devicepack12.0.1 April 27, 2021 |
| 12.8(1) | cmterm-devicepack12.0.1 August 3, 2020 |
| 12.7(1) | cmterm-devicepack12.0.1 March 4, 2019 |
| 7832 | 14.0(1) | cmterm-devicepack12.0.1 April 27, 2021 |
| 12.8(1) | cmterm-devicepack12.0.1 August 3, 2020 |
| 12.7(1) | cmterm-devicepack12.0.1 March 4, 2019 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 7945G, 7965G, and 7975G | 9.4(2)SR4 | cmterm-devicepack12.0.1 August 3, 2020 |
| 7911G, 7931G, 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE,
                                             7962G, 7965G, and 7975G | 9.4(2)SR3 | Included with Unified CM |
| 9.4(2)SR2 | Included with Unified CM |
| 7940G and 7960G | 8.1(2)SR2 (SCCP) | Included with Unified CM |
| 7915G and 7916G | 1.0(4) | Included with Unified CM |
| 7925G, 7925G-EX, and 7926G | 1.4(8)SR1 | cmterm-devicepack12.0.1 May 28, 2018 |
| 1.4(8) | Included with Unified CM |
| 7937G | 1.4(5) | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR | 14.0(1) | cmterm-devicepack12.0.1 April 27, 2021 |
| 12.8(1) | cmterm-devicepack12.0.1 August 3, 2020 |
| 12.7(1) | cmterm-devicepack12.0.1 March 4, 2019 |
| 8832 | 14.0(1) | cmterm-devicepack12.0.1 April 27, 2021 |
| 12.8(1) | cmterm-devicepack12.0.1 August 3, 2020 |
| 12.7(1) | cmterm-devicepack12.0.1 March 4, 2019 |
| 8831 and 8831NR | 14.0(1) | cmterm-devicepack12.0.1 April 27, 2021 |
| 10.3(1)SR6 | cmterm-devicepack12.0.1 August 3, 2020 |
| 10.3(1)SR3 | cmterm-devicepack12.0.1 August 7, 2018 |
| 8821 and 8821-EX | 11.0(6)SR1 | cmterm-devicepack12.0.1 April 27, 2021 |
| 11.0(6) QED files | cmterm-devicepack12.0.1 November 23, 2020 |
| 11.0(5)SR3 | cmterm-devicepack12.0.1 August 3, 2020 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8941 and 8945 | 9.4(2)SR3 | Included with Unified CM |
| 9.4(2)SR2 | Included with Unified CM |
| 8961, 9951, and 9971 | 9.4(2)SR2 | Included with Unified CM |
| 9.4(2) | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco VG450 Analog Voice Gateway | Cisco IOS XE 16.10.01a | cmterm-devicepack12.0.1 February 4, 2019 |
| ATA 187 | 9.2(3) SIP | Included with Unified CM |
| ATA 190 | 1.2.2 | Included with Unified CM |
| 1.2.1 | Included with Unified CM |
| ATA 191 | 12.0(1) | cmterm-devicepack12.0.1 December 27, 2017 |

| Note | After the September 30, 2019 device package, device packages don't contain any CE
                                             firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| DX70 and DX80 | CE9.8(1) | cmterm-devicepack12.0.1 September 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.0.1 May 28, 2019 |
| DX650 | 10.2(5) | Included with Unified CM |
| 10.2(4) | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco TelePresence IX5000 | Software IX 9.0 | cmterm-devicepack12.0.1 August 7, 2018 |
| Software IX 8.0 | cmterm-devicepack12.0.1 December 27, 2017 |

| Note | After the September 30, 2019 device package, device packages don't contain any CE
                                             firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| C Series, EX Series, MX200, and MX300 | TC7.3(3) | Included with Unified CM |
| TC7.2(0) | Included with Unified CM |
| MX200 G2, MX300 G2, MX700, MX800, MX800 Dual, SX10, SX20, and
                                             SX80 | CE9.8(1) | cmterm-devicepack12.0.1 September 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.0.1 May 28, 2019 |

| Note | After the September 30, 2019 device package, device packages don't contain any CE
                                             firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Webex Desk Limited Edition | New product QED files | cmterm-devicepack12.0.1 April 27, 2021 |
| Cisco Webex Desk Pro | New product QED files | cmterm-devicepack12.0.1 March 4, 2019 |
| Cisco Webex Room Panorama | New product QED files | cmterm-devicepack12.0.1 March 4, 2019 |
| Cisco Webex Room Panorama 70 | New product QED files | cmterm-devicepack12.0.1 March 4, 2019 |
| Cisco Webex Room 70 Single and Cisco Webex Room 70 Dual | CE9.8(1) | cmterm-devicepack12.0.1 September 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.0.1 May 28, 2019 |
| Cisco Webex Room 70 Single G2 and Cisco Webex Room 70 Dual G2 | CE9.8(1) | cmterm-devicepack12.0.1 September 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.0.1 May 28, 2019 |
| Cisco Webex Room 55 and Cisco Webex Room 55 Dual | CE9.8(1) | cmterm-devicepack12.0.1 September 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.0.1 May 28, 2019 |
| Cisco Webex Room Kit Mini | CE9.8(1) | cmterm-devicepack12.0.1 Sept. 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.0.1 May 28, 2019 |
| Cisco Webex Room Kit and Cisco Webex Room Kit Plus | CE9.8(1) | cmterm-devicepack12.0.1 September 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.0.1 May 28, 2019 |
| Cisco Webex Room Kit Pro | CE9.8(1) | cmterm-devicepack12.0.1 September 30, 2019 |
| CE9.7(1) | cmterm-devicepack12.0.1 May 28, 2019 |
| Cisco Webex Room Phone | CSV file check in | cmterm-devicepack12.0.1 November 23, 2020 |
| New Product QED File | cmterm-devicepack12.0.1 August 3, 2020 |

| Note | After the September 30, 2019 device package, device packages don't contain any CE
                                             firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Webex Board 55, 70, and 85 | CE9.8(1) | cmterm-devicepack12.0.1 March 4, 2019 |
| CE9.8(1) | cmterm-devicepack12.0.1 September 30, 2019 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Headset 500 Series | Cisco Options Package (COP) file: 2.2 Headset release: 2.2(1) | cmterm-devicepack12.0.1 April 27, 2021 |
| COP file: 2.1 Headset release: 2.1(1) | cmterm-devicepack12.0.1 August 3, 2020 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Headset 700 Series | Cisco Options Package (COP) file: 2.2(1.6) Headset release: 1-6-0-150 USB adapter release: 1-2-33 | cmterm-devicepack12.0.1 April 27, 2021 |
| COP file: 2.1 Headset release: 1-5-0-246 USB adapter release: 1-1-59 | cmterm-devicepack12.0.1 November 23, 2020 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco 4461 Integrated Services Routers | Cisco IOS XE 16.9.1 | cmterm-devicepack12.0.1 February 4, 2019 |
| Cisco 4000 Series Integrated Services Routers | Cisco IOS XE 16.4.1 | cmterm-devicepack12.0.1 November 7, 2017 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 3905 | 9.4(1)SR3 | No device package available |
| 9.4(1)SR2 | cmterm-devicepack11.0.1 December 21, 2015 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 6901 and 6911 | 9.3(1)SR2 | Included with Unified CM |
| 9.3(1)SR1 | Not applicable |
| 6921, 6941, 6945, and 6961 | 9.4(1)SR2 | cmterm-devicepack11.0.1 September 3, 2015 |
| 9.4(1)SR1 | Included with Unified CM |

| Note | When upgrading from Firmware Release 10.3(1) to Firmware Release 11.0(1), the K-Factor is removed from the Call Details Record.
                                             This was intentional as Cisco Unified
                                                				Communications Manager does not support RTP-RxStat messages greater than 256 characters in length. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 7811, 7821, 7841, and 7861 | 12.5(1)SR2 | No device package available |
| 12.1(1) | cmterm-devicepack11.0.1 June 11, 2018 |
| 7832 | 12.5(1)SR2 | No device package available |
| 12.0(1) | cmterm-devicepack11.0.1 October 4, 2017 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 7911G, 7931G, 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE, 7962G, 7965G, and 7975G | 9.4(2)SR3 | cmterm-devicepack11.0.1 April 4, 2017 |
| 9.4(2)SR2 | cmterm-devicepack11.0.1 August 24, 2016 |
| 7940G and 7960G | 8.1(2)SR2 (SCCP) | Included with Unified CM |
| 7915G and 7916G | 1.0(4) | Included with Unified CM |
| 7921G | 1.4(6) | Included with Unified CM |
| 7925G, 7925G-EX, and 7926G | 1.4(8)SR1 | cmterm-devicepack11.0.1 June 11, 2018 |
| 1.4(8) | cmterm-devicepack11.0.1 May 10, 2016 |
| 7937G | 1.4(5) | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR | 12.5(1)SR2 | No device package available |
| 12.1(1) | cmterm-devicepack11.0.1 June 11, 2018 |
| 8832 | 12.5(1)SR2 | No device package available |
| 12.1(1) | cmterm-devicepack11.0.1 June 11, 2018 |
| 8831 and 8831NR | 10.3(1)SR3 | cmterm-devicepack11.0.1 August 7, 2018 |
| 10.3(1)SR2 | cmterm-devicepack11.0.1 January 7, 2016 |
| 8821 | 11.0(5) | No device package available |
| 11.0(4)SR2 | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8941 and 8945 | 9.4(2)SR3 | cmterm-devicepack11.0.1 November 30, 2016 |
| 9.4(2)SR2 | cmterm-devicepack11.0.1 October 28, 2015 |
| 8961, 9951, and 9971 | 9.4(2)SR2 | cmterm-devicepack11.0.1 October 1, 2015 |
| 9.4(2) | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco VG450 Analog Voice Gateway | Cisco IOS XE 16.10.01a | No device package available |
| ATA 187 | 9.2(3) SIP | Included with Unified CM |
| ATA 190 | 1.2.2 | cmterm-devicepack11.0.1 July 11, 2016 |
| 1.2.1 | cmterm-devicepack11.0.1 September 3, 2015 |
| ATA 191 | 12.0(1) | cmterm-devicepack11.0.1 December 27, 2017 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| DX70 and DX80 | CE9.7(1) | No device package available |
| CE9.6(1) | No device package available |
| DX650 | 10.2(5) | cmterm-devicepack11.0.1 September 3, 2015 |
| 10.2(4) | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco TelePresence IX5000 | Software IX 9.0 | cmterm-devicepack11.0.1 August 7, 2018 |
| Software IX 8.0 | cmterm-devicepack11.0.1 December 27, 2017 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco TelePresence MX and SX Series devices | CE9.7(1) | No Device Package available |
| CE9.4(0) | cmterm-devicepack11.0.1 August 7, 2018 |
| Cisco TelePresence C Series, EX Series, MX200, and MX300 | TC7.3(3) | Included with Unified CM |
| TC7.2(0) | Included with Unified CM |
| Cisco TelePresence MX200 G2, MX300 G2, MX700, MX800, MX800 Dual, SX10, and SX80 | CE9.7(1) | No device package available |
| CE9.4(0) | cmterm-devicepack11.0.1 August 7, 2018 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Webex Room 70 (Single) and Cisco Webex Room 70 (Dual) | CE9.7(1) | No device package available |
| CE9.6(1) | No device package available |
| Cisco Webex Room 70 Single G2 and Cisco Webex Room 70 Dual G2 | CE9.7(1) | No device package available |
| CE9.4(0) | cmterm-devicepack11.0.1 August 7, 2018 |
| Cisco Webex Room 55 | CE9.7(1) | No device package available |
| CE9.6(1) | No device package available |
| Cisco Webex Room 55 Dual | CE9.7(1) | No device package available |
| CE9.4(0) | cmterm-devicepack11.0.1 August 7, 2018 |
| Cisco Webex Room Kit Mini | CE9.7(1) | No device package available |
| CE9.6(1) | No device package available |
| Cisco Webex Room Kit and Cisco Webex Room Kit Plus | CE9.7(1) | No device package available |
| CE9.6(1) | No device package available |
| Cisco Webex Room Kit Pro | CE9.7(1) | No device package available |
| CE9.6(1) | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco 4461 Integrated Services Routers | Cisco IOS XE 16.9.1 | No device package available |
| Cisco 4000 Series Integrated Services Routers | Cisco IOS XE 16.4.1 | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 3905 | 9.4(1)SR3 | cmterm-devicepack10.5.2 January 24, 2019 |
| 9.4(1)SR2 | cmterm-devicepack10.5.2 December 21, 2015 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 6901 and 6911 | 9.3(1)SR2 | cmterm-devicepack10.5.2 April 23, 2015 |
| 9.3(1)SR1 | Included with Unified CM |
| 6921, 6941, 6945, and 6961 | 9.4(1)SR2 | cmterm-devicepack10.5.2 September 3, 2015 |
| 9.4(1)SR1 | Included with Unified CM |

| Note | When upgrading from Firmware Release 10.3(1) to Firmware Release 11.0(1) or later, the K-Factor has been removed from the
                                             Call Details Record. This was intentional as Cisco Unified Communications Manager does not support RTP-RxStat messages greater
                                             than 256 characters in length. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 7811, 7821, 7841, and 7861 | 12.8(1) | cmterm-devicepack10.5.2 August 3, 2020 |
| 12.7(1) | cmterm-devicepack10.5.2 March 4, 2020 |
| 12.6(1) | cmterm-devicepack10.5.2 October 11, 2019 |
| 7832 | 12.8(1) | cmterm-devicepack10.5.2 August 3, 2020 |
| 12.7(1) | cmterm-devicepack10.5.2 March 4, 2020 |
| 12.6(1) | cmterm-devicepack10.5.2 October 11, 2019 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 7945G, 7965G, and 7975G | 9.4(2)SR4 | cmterm-devicepack10.5.2 August 3, 2020 |
| 7911G, 7931G, 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE,
                                             7962G, 7965G, and 7975G | 9.4(2)SR2 | cmterm-devicepack10.5.2 August 22, 2016 |
| 7940G and 7960G | 8.1(2)SR2 (SCCP) | Included with Unified CM |
| 7915G and 7916G | 1.0(4) | Included with Unified CM |
| 7921G | 1.4(6) | cmterm-devicepack10.5.2 April 23, 2015 |
| 1.4(5) | Included with Unified CM |
| 7925G, 7925G-EX, and 7926G | 1.4(8)SR1 | cmterm-devicepack10.5.2 June 4, 2018 |
| 1.4(8) | cmterm-devicepack10.5.2 May 10, 2016 |
| 7937G | 1.4(5) | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR | 12.8(1) | cmterm-devicepack10.5.2 August 3, 2020 |
| 12.7(1) | cmterm-devicepack10.5.2 March 4, 2020 |
| 12.6(1) | cmterm-devicepack10.5.2 October 11, 2019 |
| 8832 | 12.8(1) | cmterm-devicepack10.5.2 August 3, 2020 |
| 12.7(1) | cmterm-devicepack10.5.2 March 4, 2020 |
| 12.6(1) | cmterm-devicepack10.5.2 October 11, 2019 |
| 8831 and 8831NR | 10.3(1)SR6 | cmterm-devicepack10.5.2 August 3, 2020 |
| 10.3(1)SR3 | cmterm-devicepack10.5.2 August 13, 2018 |
| 10.3(1)SR2 | cmterm-devicepack10.5.2 January 7, 2016 |
| 8821 and 8821-EX | 11.0(5)SR3 | cmterm-devicepack10.5.2 August 3, 2020 |
| 11.0(5)SR2 | cmterm-devicepack10.5.2 March 4, 2020 |
| 11.0(5)SR1 | cmterm-devicepack10.5.2 October 11, 2019 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8941 and 8945 | 9.4(2)SR3 | cmterm-devicepack10.5.2 November 30, 2016 |
| 9.4(2)SR2 | cmterm-devicepack10.5.2 October 28, 2015 |
| 8961, 9951, and 9971 | 9.4(2)SR2 | cmterm-devicepack10.5.2 October 1, 2015 |
| 9.4(2) | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco VG450 Analog Voice Gateway | Cisco IOS XE 16.10.01a | cmterm-devicepack10.5.2 January 24, 2019 |
| ATA 187 | 9.2(3) SIP | Included with Unified CM |
| ATA 190 | 1.2.2 | cmterm-devicepack10.5.2 July 7, 2016 |
| 1.2.1 | cmterm-devicepack10.5.2 September 3, 2015 |
| ATA 191 | 12.0(1) | cmterm-devicepack10.5.2 December 20, 2017 |

| Note | After the October 11, 2019 device package, device packages don't contain any CE firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| DX70 and DX80 | CE9.8(1) | cmterm-devicepack10.5.2 October 11, 2019 |
| CE9.7(1) | cmterm-devicepack10.5.2 May 28, 2019 |
| DX650 | 10.2(5) | cmterm-devicepack10.5.2 September 3, 2015 |
| 10.2(4) | cmterm-devicepack10.5.2 May 28, 2015 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cius | 9.2(4) | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco TelePresence IX5000 | Software IX 9.0 | cmterm-devicepack10.5.2 August 13, 2018 |
| Software IX 8.0 | cmterm-devicepack10.5.2 December 20, 2017 |

| Note | After the October 11, 2019 device package, device packages don't contain any CE
                                             firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| C Series, EX Series, MX200, and MX300 | TC7.3(3) | cmterm-devicepack10.5.2 May 28, 2015 |
| TC7.2(0) | Included with Unified CM |
| MX200 G2, MX300 G2, MX700, MX800, MX800 Dual, SX10, SX20, and
                                             SX80 | CE9.8(1) | cmterm-devicepack10.5.2 October 11, 2019 |
| CE9.7(1) | cmterm-devicepack10.5.2 May 28, 2019 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco TelePresence CTS and TX series | N/A | Included with Unified CM |

| Note | After the October 11, 2019 device package, device packages don't contain any CE
                                             firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Webex Room Panorama | New product QED files | cmterm-devicepack10.5.2 March 4, 2020 |
| Cisco Webex Room Panorama 70 | New product QED files | cmterm-devicepack10.5.2 March 4, 2020 |
| Cisco Webex Desk Pro | New product QED files | cmterm-devicepack10.5.2 March 4, 2020 |
| Cisco Webex Room 70 Single and Cisco Webex Room 70 Dual | CE9.8(1) | cmterm-devicepack10.5.2 October 11, 2019 |
| CE9.7(1) | cmterm-devicepack10.5.2 May 28, 2019 |
| Cisco Webex Room 70 Single G2 and Cisco Webex Room 70 Dual G2 | CE9.8(1) | cmterm-devicepack10.5.2 October 11, 2019 |
| CE9.7(1) | cmterm-devicepack10.5.2 May 28, 2019 |
| Cisco Webex Room 55 and Cisco Webex Room 55 Dual | CE9.8(1) | cmterm-devicepack10.5.2 October 11, 2019 |
| CE9.7(1) | cmterm-devicepack10.5.2 May 28, 2019 |
| Cisco Webex Room Kit Mini | CE9.8(1) | cmterm-devicepack10.5.2 October 11, 2019 |
| CE9.7(1) | cmterm-devicepack10.5.2 May 28, 2019 |
| Cisco Webex Room Kit and Cisco Webex Room Kit Plus | CE9.8(1) | cmterm-devicepack10.5.2 October 11, 2019 |
| CE9.7(1) | cmterm-devicepack10.5.2 May 28, 2019 |
| Cisco Webex Room Kit Pro | CE9.8(1) | cmterm-devicepack10.5.2 October 11, 2019 |
| CE9.7(1) | cmterm-devicepack10.5.2 May 28, 2019 |
| Cisco Webex Room Phone | New Product QED File | cmterm-devicepack10.5.2 August 3, 2020 |

| Note | After the October 11, 2019 device package, device packages don't contain any CE
                                             firmware. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Webex Board 55, 70, and 85 | CE9.8(1) | cmterm-devicepack10.5.2 March 4, 2020 |
| CE9.8(1) | cmterm-devicepack10.5.2 October 11, 2019 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Headset 500 Series | Cop file: 2.1 Headset release: 2.1(1) | cmterm-devicepack10.5.2 August 3, 2020 |
| 2.0 | cmterm-devicepack10.5.2 March 4, 2020 |
| 1.5(1) | cmterm-devicepack10.5.2 October 11, 2019 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Headset 700 Series | Cop file:2.1 Headset release: 1-3-0-246 | cmterm-devicepack10.5.2 August 3, 2020 |
| 2.0 | cmterm-devicepack10.5.2 March 4, 2020 Note The Cisco Headset 700 Series can be upgraded only using the
                                                         Cisco Headset mobile app. | Note | The Cisco Headset 700 Series can be upgraded only using the
                                                         Cisco Headset mobile app. |
| Note | The Cisco Headset 700 Series can be upgraded only using the
                                                         Cisco Headset mobile app. |

| Note | The Cisco Headset 700 Series can be upgraded only using the
                                                         Cisco Headset mobile app. |
|---|---|

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco 4461 Integrated Services Routers | Cisco IOS XE 16.9.1 | cmterm-devicepack10.5.2 January 24, 2019 |
| Cisco 4000 Series Integrated Services Routers | Cisco IOS XE 16.4.1 | cmterm-devicepack10.5.2 October 16, 2017 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Jabber | 10.6(0) | Included with Unified CM |
| 9.1(1) | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 3905 | 9.4(1) SR2 | cmterm-devicepack10.5.1 November 25, 2014 |
| 9.4(1) SR1 | cmterm-devicepack10.5.1 November 25, 2014 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 6901 and 6911 | 9.3(1)SR2 | cmterm-devicepack10.5.1 December 22, 2014 |
| 9.3(1)SR1 | Included with Unified CM |
| 6921, 6941, 6945, and 6961 | 9.4(1)SR2 | No device package available |
| 9.4(1)SR1 | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 7811, 7821, 7841, and 7861 | 12.5(1)SR2 | No device package available |
| 10.2(1) | cmterm-devicepack10.5.1 February 12, 2015 |
| Configuration files on Unified CM (QED) | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 7906G, 7911G, 7931G 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE, 7962G, 7965G, 7970G, 7971G-GE, and 7975G | 9.4(2)SR3 | No device package available |
| 9.4(2)SR2 | No device package available |
| 9.4(2)SR1 QED | cmterm-devicepack10.5.1 December 22, 2014 |
| 7940G and 7960G | 8.1(2)SR2 (SCCP) | Included with Unified CM |
| 7915G and 7916G | 1.0(4) | Included with Unified CM |
| 7921G | 1.4(6) | cmterm-devicepack10.5.1 September 23, 2014 |
| 1.4(5) | Included with Unified CM |
| 7925G, 7925G-EX, and 7926G | 1.4(6) | cmterm-devicepack10.5.1 September 23, 2014 |
| 1.4(5) | Included with Unified CM |
| 7937G | 1.4(5) | cmterm-devicepack10.5.1 September 30, 2014 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8831 | 10.3(1)SR3 | No device package available |
| 10.3(1) | cmterm-devicepack10.5.1 December 22, 2014 |
| 8811, 8841, 8851, 8851NR, and 8861 | 12.0(1) | No device package available |
| N/A | Resolves caveat CSCur67137 December 22, 2014 cmterm-devicepack10.5.1 |
| Configuration files on Unified CM (QED) | No device package available |
| 8845 and 8865 | 12.0(1) | No device package available |
| 11.7(1) | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8941 and 8945 | 9.4(2)SR3 | No device package available |
| 9.4(2) | cmterm-devicepack10.5.1 September 23, 2014 |
| 8961, 9951, and 9971 | 9.4(2)SR3 | No device package available |
| 9.4(2) | cmterm-devicepack10.5.1 October 30, 2014 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| ATA 187 | 9.2(3) SIP | Included with Unified CM |
| ATA 190 | 1.2.2 | No device package available |
| 1.1.2(005) | No device package available |
| Configuration files on Unified CM (QED) | cmterm-devicepack10.5.1 July 24, 2014 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| DX70 and DX80 | 10.2(4) | No device package available |
| 10.2(2) | cmterm-devicepack10.5.1 September 23, 2014 |
| Configuration files on Unified CM (QED) | No device package available |
| DX650 | 10.2(4) | No device package available |
| 10.2(2) | cmterm-devicepack10.5.1 September 23, 2014 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cius | 9.2(4) | No device package available |
| 9.2(3) | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco TelePresence IX5000 | Software IX 8.1 | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| MX700 and MX800 | CE 8.0 | No device package available |
| TC7.1(2) | cmterm-devicepack10.5.1 February 12, 2015 |
| MX800 Dual | CE 8.0 | No device package available |
| TC7.3(2) | cmterm-devicepack10.5.1 February 12, 2015 |
| MX200 G2 | TC7.1 | Included with Unified CM |
| MX300 G2 | TC7.0 | Included with Unified CM |
| SX10 | TC7.1 | Included with Unified CM |
| SX80 | TC7.1(2) | cmterm-devicepack10.5.1 February 12, 2015 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco TelePresence CTS and TX series | Configuration files on Unified CM (QED) | Included with Unified CM |
| Adm. Capability Only | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Jabber | 10.6(0) | cmterm-devicepack10.5.1 November 25, 2014 |
| 9.1(1) | Included with Unified CM |
| Adm. Capability Only | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 3905 | 9.4(1) SR2 | No device package available |
| 9.4(1) SR1 | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 6901 and 6911 | 9.3(1)SR2 | No device package available |
| 9.3(1)SR1 | No device package available |
| 6921, 6941, and 6961 | 9.4(1)SR2 | No device package available |
| 9.4(1)SR1 | cmterm-devicepack10.0.1 May 28, 2014 |
| 6945 | 9.4(1)SR2 | No device package available |
| 9.4(1)SR1 | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 7811, 7821, 7841, and 7861 | 12.5(1)SR2 | No device package available |
| 10.1(1)SR1 | cmterm-devicepack10.0.1 May 7, 2014 |
| Configuration files on Unified CM (QED) | cmterm-devicepack10.0.1 March 18, 2014 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 7906G, 7911G, 7931G 7941G, 7941G-GE, 7942G, 7945G, 7961G, 7961G-GE, 7962G, 7965G, 7970G, 7971G-GE, and 7975G | 9.4(2)SR3 | No device package available |
| 9.3(1)SR4 | cmterm-devicepack10.0.1 March 18, 2014 |
| 7940G and 7960G | 8.1(2)SR2 (SCCP) | No device package available |
| 7915G and 7916G | 1.0(4) | No device package available |
| 7921G | 1.4(6) | No device package available |
| 1.4(5) | No device package available |
| 7925G, 7925G-EX, and 7926G | 1.4(6) | No device package available |
| 1.4(5) | No device package available |
| 7937G | 1.4(5) | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8831 | 10.3(1)SR3 | No device package available |
| 10.3(1)SR2 | No device package available |
| 8811, 8841, 8851, 8851NR, and 8861 | 12.5(1)SR2 | No device package available |
| Configuration files on Unified CM (QED) | cmterm-devicepack10.0.1 May 28, 2014 |
| 8845 and 8865 | 12.5(1)SR2 | No device package available |
| 11.7(1) | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| 8941 and 8945 | 9.4(2)SR3 | No device package available |
| 9.4(2)SR2 | No device package available |
| 8961, 9951, and 9971 | 9.4(2)SR3 | No device package available |
| 9.4(2)SR2 | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| ATA 187 | 9.2(3) SIP | No device package available |
| ATA 190 | 1.2.2 | No device package available |
| 1.1.2(005) | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| DX70 and DX80 | 10.2(4) | No device package available |
| 10.2(2) | No device package available |
| Configuration files on Unified CM (QED) | cmterm-devicepack10.0.1 May 28, 2014 |
| DX650 | 10.2(4) | No device package available |
| 10.2(2) | No device package available |
| 10.1(2) | cmterm-devicepack10.0.1 May 28, 2014 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cius | 9.2(4) | No device package available |
| 9.2(3) | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco TelePresence IX5000 | Software IX 8.1 | No device package available |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| MX700 and MX800 | CE 8.0 | No device package available |
| TC7.1(2) | cmterm-devicepack10.0.1 May 28, 2014 |
| MX800 Dual | CE 8.0 | No device package available |
| TC7.3(3) | No device package available |
| MX300 G2 | TC7.0 | cmterm-devicepack10.0.1 May 7, 2014 |
| MX200 G2 | TC7.1 | cmterm-devicepack10.0.1 May 7, 2014 |
| SX10 and SX80 | TC7.1 | cmterm-devicepack10.0.1 May 7, 2014 |
| Configuration files on Unified CM (QED) | cmterm-devicepack10.0.1 March 18, 2014 |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco TelePresence CTS and TX series | Configuration files on Unified CM (QED) | Included with Unified CM |
| Adm. Capability Only | Included with Unified CM |

| Device Type | Device Release | Compatible Device Package |
|---|---|---|
| Cisco Jabber | 10.6(0) | cmterm-devicepack10.5.1 November 25, 2014 |
| 9.1(1) | Included with Unified CM |
| Adm. Capability Only | Included with Unified CM |