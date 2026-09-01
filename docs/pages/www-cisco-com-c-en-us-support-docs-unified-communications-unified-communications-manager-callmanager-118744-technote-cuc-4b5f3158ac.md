---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-118744-technote-cuc-4b5f3158ac
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/118744-technote-cucm-00.html
retrieved_at: 2026-09-01T19:46:31.864835+00:00
---

Implement CUCM Versions 8.X/9.X/10.X Time Zone and DST Changes

# Implement CUCM Versions 8.X/9.X/10.X Time Zone and DST Changes

### Download Options

Updated: July 5, 2023

Document ID: 118744

Contents

## Contents

## Introduction

This document describes how time changes and time zone settings are maintained on Cisco UCM and on the most popular Cisco IP phones.

## Implement Time Zone Settings and DST Changes in CUCM

Time zone information in CUCM is based on the Time Zone Database defined on the Internet Assigned Numbers Authority (IANA):

It is sometimes called the Olson database, which refers to the founding contributor, Arthur David Olson.

Paul Eggert is currently its editor and maintainer. Refer to the Time Zone Database for recent timezone updates.

Changes in the Time Zone Database usually happen a couple of times a year; you can check the history of all the recent updates on The tz-announce Archives .

For important changes in the Time Zone Database, Cisco releases the .cop file for CUCM that includes the changes to the Time Zone Database.

Not all of the changes in the Time Zone Database have a respective .cop file for CUCM.

For all currently supported CUCM versions (except the newest Version 10.5 where it was redesigned),

DST change is performed according to schedule, defined by the time zone data version, which can be verified with this CLI command:

```
admin: show timezone config Current timezone: Central European Time (Europe/Warsaw) Timezone version: 2012j
```

In this case, the installed timezone version is 2012j and the system is set in Central European Time (CET) time zone.

You can view the list of available time zones with this command:

```
admin: show timezone list 0 - Africa/Abidjan 1 - Africa/Accra 2 - Africa/Addis_Ababa 3 - Africa/Algiers 4 - Africa/Asmara 5 - Africa/Bamako
[...] 405 - Europe/Warsaw [...]
```

And time zones on CUCM can be set with this command:

```
admin: set timezone 405 Using timezone: Europe/Warsaw A system restart is required
```

In this command, 405 is the mapping of the 405 to the Europe/Warsaw time zone.

Note : After you change the time zone on CUCM, a system restart is required.

The DST change schedule can be updated via DST update .cop files, which are released for specific CUCM versions and every time DST rules are changed.

There are many changes in DST across the globe each year, so it is important that you keep the DST schedule updated. DST update .cop files are named in this format:

```
ciscocm.dst-updater.<tzdata_version>.<UCM Release version>.cop
```

Every DST update .cop file includes a new version of a .csv file ( TzDataCSV.csv ), which contains the DST change schedule update for every time zone.

The file contains this information for every time zone. Here is an example for the Europe/Amsterdam time zone:

```
TIMEZONE_EUROPE_AMSTERDAM,"Europe/Amsterdam"," 60 "," 0/3/0/5,02:00:00:00 "," 0/10/0/4, 03:00:00:00 "," 60 ","Europe/Amsterdam"
```

Here is a description of what the different components of the output mean:

- TIMEZONE_EUROPE_AMSTERDAM - Identifier

- Europe/Amsterdam - Time zone name

- " 60 " - Greenwich Mean Time (GMT) offset

- " 0/3/0/5,02:00:00:00 " - DST starts at 2 AM; 3 means March; 5 means the fifth Sunday of this month

- " 0/10/0/4,03:00:00:00 " - DST stops at 3 AM; 10 means October; 4 means the fourth Sunday of this month

- " 60 " - DST change in minutes

- "Europe/Amsterdam" - Additional time zone marker

After you install the DST update .cop file, all information from TzDataCSV.csv is updated in the CUCM database.

In the CUCM database, the table that stores DST update information is called Typetimezone table.

The content of Typetimezone table can be checked by a CLI Structured Query Language (SQL); here is an example:

```
admin: run sql select * from typetimezone where name ='Europe/Amsterdam' enum name description moniker bias stddate stdbias dstdate dstbias abbreviation legacyname ==== ================ ============================================================ ========================= ==== ==================== ======= =================== ======= ============ ================================ 23 Europe/Amsterdam (GMT+01:00) Amsterdam, Berlin, Stockholm, Rome, Bern, Vienna TIMEZONE_EUROPE_AMSTERDAM -60 0/10/0/4,03:00:00:00 0 0/3/0/5,02:00:00:00 -60 CET W. Europe Standard/Daylight Time
```

Here is a description of what the different components of the output mean:

- stddate - Standard time start

- dstdate - Summer time start

- bias - Offset from GMT

- stdbias - Offset from bias during standard time

- dstbias - Offset from bias during summer time

As you can see, there is no information about year in the database.

DST update changes in CUCM are not year-specific; time updates from the Typetimezone table are applied every year and can only be changed by a new DST update .cop file installation.

## Implement Time Zone Settings and DST Changes On Most Popular Cisco IP Phones

This section covers how to handle DST changes for phones in CUCM.

During the start-up process, all phones communicate with the TFTP server and download tzdata information, based on information from the config file.

This process varies and depends on the type of the phone.

After the phone gets information within the configuration file about which file to download, it downloads the file from the same TFTP server.

In the image, <tz file> is either tzupdater.jar, tzdatacsv.csv, or j9-tzdata.jar.

79XX series , 8961 , and 99X1 phones update tzdata information with a download of the tzupdater.jar library based on this section from the config file:

```
<device> <tzdata> <tzolsonversion> version </tzolsonversion> <tzupdater> tzupdater.jar <tzupdater> </tzdata> </device>
```

Here is a description of what the different components of the file mean:

- version - This is the Olson TZ version that comes from the tzupdater.ver file that is dumped into the TFTP folder

- tzupdater.jar - This is the tz update file for Java phones

3911 , 3951 , 69XX series , and 894X phones update tzdata information with a download of the tzdatacsv.csv file based on this section from the config file:

```
<device> <tzdata> <tzolsonversion> version </tzolsonversion> <tzupdater> tzdatacsv.csv <tzupdater> </tzdata> </device>
```

In the file, tzdatacsv.csv means the time zone update file for Lodown/RTL/Gumbo phones.

78XX series and 88XX series phones update tzdata information with a download of the j9-tzdata.jar library based on this section from the config file:

```
<device> <tzdata> <tzolsonversion> version </tzolsonversion> <tzupdater> j9-tzdata.jar <tzupdater> </tzdata> </device>
```

In the file, j9-tzdata.jar means the time zone update file for 78XX series and 88XX series.

Note : Files like tzupdater.jar,  tzdatacsv.csv, and j9-tzdata.jar are updated on the TFTP server during the installation of the DST update .cop file.

## DST Implementation Changes in CUCM Version 10.5

In CUCM Version 10.5, the way that DST changes were handled was changed.

These improvements reduced the number of cases opened when a new DST .cop file installation was required.

In most cases, you do not need to install new .cop files because countries’ government rules do not change every year.

But even then, you need to update your .csv files because the calendar year changes every year.

For example, for some years, the DST start day is the fourth Sunday and sometimes it starts on the fifth Sunday.

At times, the .csv file points to fourth Sunday and at other times, it points to fifth Sunday.

This could be confusing because March can have four or five Sundays.

The aim of this feature is that the .csv file refers to the last Sunday instead of to the fourth or fifth Sunday. So a new .csv file is required.

In CUCM versions before Version 10.5, this change required a new DST .cop file installation. With the changes in CUCM Veresion 10.5, this behavior occurs:

- A DST rules file is generated for the current year at 00:00 hours on January 10 if the CUCM server is powered on.

- If the CUCM server is not powered on, the DST rules file is generated when the servers boot up, on or after January 10.

```
admin: utils update dst Creating backup of existing DST rules file. Backup of DST rules file created. Creating new file for DST rules. This might take several minutes. Do not press Ctrl-C. DST rules file created for the current year. Cisco TFTP will restart now. Service Manager is running Cisco Tftp[STARTED] Cisco tftp restarted. CSV file created succesfully.
```

You must restart the phones in order for the changes to take effect. If you do not restart the phones, it results in incorrect DST start/stop dates.

Note : It is still required to update the DST .cop file if the Time Zone Database for the time zone changes. For example, if a particular country decides that  it does not do DST changes anymore, you need to update the DST .cop file.

## Avoid Problems Related to DST Changes on CUCM and Cisco IP Phones

In order to avoid known problems with DST update changes on phones and CUCM systems (from Version 8.X to Version10.5), remember these concerns:

- You must keep your CUCM system updated with the newest release of DST .cop file available on Cisco.com.

- Every time you update the CUCM system with the new DST .cop file, the tzdata jar files also must be updated.

In order to avoid any compatibility issues with phones that run old firmware, it is highly recommended to keep the system updated with the latest device pack release.

- Every time you see the "Time zone data download failed" message in the phone status messages, you must investigate because it is highly possible that the phone has problems with the correct time display and possibly runs into problems during the DST update.

- Be aware that Cisco cannot predict when DST rules are changed, and this is why there is a need to release and install DST .cop files every time there is an announcement that rules are changed.

### Revision History

2.0

05-Jul-2023

recertification

1.0

17-Feb-2015

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 05-Jul-2023 | recertification |
| 1.0 | 17-Feb-2015 | Initial Release |