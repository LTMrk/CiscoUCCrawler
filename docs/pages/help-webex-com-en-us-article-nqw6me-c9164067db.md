---
doc_id: help-webex-com-en-us-article-nqw6me-c9164067db
source_url: https://help.webex.com/en-us/article/nqw6me
retrieved_at: 2026-11-02T12:59:12.684425+00:00
---

Connect Cisco Headset 300 Series, 500 Series, or 700 Series to Cisco Desk Phone 9800 Series
        or Cisco Desk Phone 8875 with a USB cable. Depending on the headset models, the following
        scenarios may occur.

When headset firmware upgrade is available, the phone
            starts the upgrade process immediately and displays an on-screen upgrade toast. This
            process may complete in 5 to 10 seconds. Upon completion, the toast disappears and the
            headset reboots automatically.

When headset firmware upgrade is
            available, the phone displays an on-screen upgrade alert.

- Press Postpone and the phone will display the upgrade alert again two hours
                later.

- Press Upgrade to start the upgrade process immediately. This process may
                complete in 4 to 16 minutes.

- If you don't take any action, the headset starts the upgrade process once the 30
                seconds countdown is over.

During the upgrade process, the phone displays an animated headset icon on the top-right corner of the screen.

## Configure firmware upgrade on the phone administration page

To upgrade the headset firmware on Cisco Desk Phone 9800 Series or Cisco Desk Phone 8875
        that is registered to Cisco BroadWorks or Webex Calling, you need to set up the Cisco
        Headset upgrade rules on the the phone administration page. After configuration, end users
        can follow the on-screen instructions of the phone to upgrade the firmware of Cisco Headset
        300 Series, 500 Series, and 700 Series.

Download the latest headset firmware package.

Access https://software.cisco.com/download/home/286325648/type/286323289/ .

Select the latest release in the Latest Release list.

(Optional) Place your mouse pointer on the file name to see the file
              details and checksum values.

Download the headset firmware package. For example,
              cmterm-headset.3-3-0001-1.zip.

This package consists of a configuration file (ciscoheadsetfirmware.xml) along with
                all the firmware versions of different headset or accessories models.

Unzip the file and place the files in the appropriate directory on your
              server.

The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on
                the protocol that you want to use for the upgrade.

Access the phone administration web page.

Select Voice > Provisioning .

Under the Cisco Headset Firmware Upgrade section, enter the configuration file
          name in the Cisco Headset Upgrade Rule parameter.

Examples:

<upgrade protocol>://<upgrade server ip
              address>[:<port>]>/<path>/<file name>.xml

http://10.74.10.225/upgrade/ciscoheadsetfirmware.xml

Click Submit All Changes .

## Configure firmware upgrade on Unified CM

To upgrade the headset firmware on Cisco Desk Phone 9800 Series or Cisco Desk Phone 8875
        that is registered to Cisco Unified Communications Manager (Unified CM), you need to set up
        the Cisco Headset Serviceability feature on Unified CM. After configuration, end users can
        follow the on-screen instructions of the phone to upgrade the firmware of Cisco Headset 300
        Series, 500 Series, and 700 Series.

This Help article provides basic guidelines for the Cisco Headset Serviceability feature
          configuration only. For detailed instructions about how to configure user profiles for
          headset users, apply user profiles to end users, and manage headset and accessories
          templates, see the Headset and Accessories Management chapter in Feature Configuration Guide for Cisco Unified
              Communications Manager, Release 15 and SUs .

Download the latest headset firmware COP file.

Access https://software.cisco.com/download/home/286325648/type/286323289/ .

Select the latest release in the Latest Release list.

(Optional) Place your mouse pointer on the file name to see the file
              details and checksum values.

Download the headset firmware COP file to appropriate directory on your server. For
              example, cmterm-headset.3-3-0001-1.k4.cop.sha512.

This file contains all the firmware versions of different headset or accessories
                models along with their configuration data.

Log in to Communications Manager Administration.

On Cisco Unified Communications Manager Administration, select Cisco Unified
            Operating System Administration in the Navigation field and click Go .

Navigate to Software upgrades > Install/Upgrade and install the COP file
          on Unified CM.

Select Cisco Unified Serviceability in the Navigation field and click Go .

Navigate to Tools > Control Center - Feature Services and restart the
          TFTP server.

Select Cisco Unified CM Administration in the Navigation field and click Go .

Navigate to Device > Headset and Accessories > Headset and Accessories
            Template . You can see the firmware settings in the Standard Default Headset
            Configuration Template .

Alternatively, if you hope to use a custom headset configuration template per your
          deployment needs, you need to configure user profiles for headset users, apply user
          profiles to end users, associate phone device to end users, add new headset template
          configuration and assign user profile.

| 1 | Download the latest headset firmware package. Access https://software.cisco.com/download/home/286325648/type/286323289/ . Select the latest release in the Latest Release list. (Optional) Place your mouse pointer on the file name to see the file
              details and checksum values. Download the headset firmware package. For example,
              cmterm-headset.3-3-0001-1.zip. This package consists of a configuration file (ciscoheadsetfirmware.xml) along with
                all the firmware versions of different headset or accessories models. Unzip the file and place the files in the appropriate directory on your
              server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on
                the protocol that you want to use for the upgrade. |
|---|---|
| 2 | Access the phone administration web page. |
| 3 | Select Voice > Provisioning . |
| 4 | Under the Cisco Headset Firmware Upgrade section, enter the configuration file
          name in the Cisco Headset Upgrade Rule parameter. Examples: <upgrade protocol>://<upgrade server ip
              address>[:<port>]>/<path>/<file name>.xml http://10.74.10.225/upgrade/ciscoheadsetfirmware.xml |
| 5 | Click Submit All Changes . |

| 1 | Download the latest headset firmware COP file. Access https://software.cisco.com/download/home/286325648/type/286323289/ . Select the latest release in the Latest Release list. (Optional) Place your mouse pointer on the file name to see the file
              details and checksum values. Download the headset firmware COP file to appropriate directory on your server. For
              example, cmterm-headset.3-3-0001-1.k4.cop.sha512. This file contains all the firmware versions of different headset or accessories
                models along with their configuration data. |
|---|---|
| 2 | Log in to Communications Manager Administration. |
| 3 | On Cisco Unified Communications Manager Administration, select Cisco Unified
            Operating System Administration in the Navigation field and click Go . |
| 4 | Navigate to Software upgrades > Install/Upgrade and install the COP file
          on Unified CM. |
| 5 | Select Cisco Unified Serviceability in the Navigation field and click Go . |
| 6 | Navigate to Tools > Control Center - Feature Services and restart the
          TFTP server. |
| 7 | Select Cisco Unified CM Administration in the Navigation field and click Go . |
| 8 | Navigate to Device > Headset and Accessories > Headset and Accessories
            Template . You can see the firmware settings in the Standard Default Headset
            Configuration Template . Alternatively, if you hope to use a custom headset configuration template per your
          deployment needs, you need to configure user profiles for headset users, apply user
          profiles to end users, associate phone device to end users, add new headset template
          configuration and assign user profile. |

## Figuras

![Headset firmware upgrade icon](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/488001-489000/488024.png)