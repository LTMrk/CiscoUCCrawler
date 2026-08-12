  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Cisco IOS and NX-OS Software](https://www.cisco.com/c/en/us/support/ios-nx-os-software/index.html)


# ROMmon Recovery for the Cisco 2600 Series Router and the VG200
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)
Print
### Available Languages
  * [Arabic - عربي](https://www.cisco.com/c/ar_ae/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)
  * [Brazil - Português](https://www.cisco.com/c/pt_br/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)
  * [Canada - Français](https://www.cisco.com/c/fr_ca/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)
  * [China - 简体中文](https://www.cisco.com/c/zh_cn/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)
  * [China - 繁體中文 (臺灣)](https://www.cisco.com/c/zh_tw/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)
  * [Germany - Deutsch](https://www.cisco.com/c/de_de/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)
  * [Italy - Italiano](https://www.cisco.com/c/it_it/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)
  * [Korea - 한국어](https://www.cisco.com/c/ko_kr/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)
  * [Latin America - Español](https://www.cisco.com/c/es_mx/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)
  * [Netherlands - Nederlands](https://www.cisco.com/c/nl_nl/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)


Updated:September 29, 2014
Document ID:15079
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
## Contents
[Introduction ](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html#intro)
[Before You Begin ](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html#before)
[Conventions ](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html#conv)
[Prerequisites ](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html#prereq)
[Components Used ](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html#hw)
[Check Configuration Register Settings](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html#config_set)
[Look for a Valid Image in Flash](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html#topic1)
[Download using TFTP from ROMmon ](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html#topic2)
[Download using Xmodem from ROMmon ](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html#topic3)
[Related Information](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html#related)
##  Introduction 
This page explains how to recover a Cisco 2600 Series Router and a VG200 stuck in ROMmon (`rommon# ..>` prompt). 
##  Before You Begin 
###  Conventions 
For more information on document conventions, see the [Cisco Technical Tips Conventions](http://www.cisco.com/en/US/tech/tk801/tk36/technologies_tech_note09186a0080121ac5.shtml).
###  Prerequisites 
There are no specific prerequisites for this document.
###  Components Used 
This document is not restricted to specific software and hardware versions.
The information presented in this document was created from devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If you are working in a live network, ensure that you understand the potential impact of any command before using it.
##  Check Configuration Register Settings
If the router is stuck in ROMmon mode, the first setting that should be checked is the value of the configuration register. 
The first four bits of the configuration register comprise the boot field. The value of the boot field defines the source of a default Cisco IOS® software image that will be used to run the router. If the value of the boot field is 0 (configuration register value of XXX0), on startup the system enters and remains in the ROM monitor mode (rommon>), awaiting a user command to boot the system manually. For more information on the software configuration register bit meanings, see [Configuring the Software Configuration Register](http://www.cisco.com/univercd/cc/td/doc/product/core/cis12000/cis12016/icg/hfricgbc.htm#1015930).
If your router keeps entering the ROMmon mode each time the system is restarted, it is probably due to the setting of the configuration register. To verify the configured value of the configuration register, use the **confreg** command as shown below:
> 
```
rommon 2 > **confreg**

    Configuration Summary
enabled are:
load rom after netboot fails
console baud: 9600
**boot: the ROM Monitor**

do you wish to change the configuration? y/n  [n]: 
```

As indicated by the output of the **confreg** command above, the configuration register is set to a value that forces the router to go into the ROMmon mode each time it is reloaded or power-cycled. To make the router boot automatically from a default Cisco IOS software image, change the configuration register value as shown below:
> 
```
rommon 2 > **confreg** 

    Configuration Summary
enabled are:
load rom after netboot fails
console baud: 9600
boot: the ROM Monitor

do you wish to change the configuration? y/n  [n]:  y
enable  "diagnostic mode"? y/n  [n]:
enable  "use net in IP bcast address"? y/n  [n]:
disable "load rom after netboot fails"? y/n  [n]:
enable  "use all zero broadcast"? y/n  [n]:
enable  "break/abort has effect"? y/n  [n]:
enable  "ignore system config info"? y/n  [n]:
change console baud rate? y/n  [n]:
**change the boot characteristics? y/n  [n]:  y**
enter to boot:
 0 = ROM Monitor
 1 = the boot helper image
 2-15 = boot system
    [0]:  **2**

    Configuration Summary
enabled are:
load rom after netboot fails
console baud: 9600
**boot: image specified by the boot system commands
      or default to: cisco2-C2600**

do you wish to change the configuration? y/n  [n]: n
You must reset or power cycle for new config to take effect

```

By doing this, you have changed the configuration register to a value that makes it look for a valid Cisco IOS software image on startup and boot from the same. The router must now be reset.
> 
```
rommon 3 > **reset**

System Bootstrap, Version 11.3(2)XA4, RELEASE SOFTWARE (fc1)
Copyright (c) 1999 by cisco Systems, Inc.
TAC:Home:SW:IOS:Specials for info

<SNIP>
```

The router should now reload with a valid Cisco IOS software image.
##  Look for a Valid Image in Flash
If the configuration register value is set to make the system boot automatically from a default Cisco IOS software image, and if no break signal is sent during start up, the router should boot normally. However, if the router still enters the ROMmon mode, it is probably because the device is unable to locate a valid Cisco IOS software image. 
The first thing you need to do then is to look for a valid Cisco IOS software image. To do this, issue the **dir <device>** command for each available device, and look for a valid Cisco IOS software image. For example, to look for the IOS in the Flash, use the command shown below.
> 
```
rommon 1 > **dir flash:**
         File size         Checksum   File name   
5358032 bytes (0x51c1d0)   0x7b16    c2600-i-mz.122-10b.bin
rommon 2 >

```

Note that if the router returns the "bad device name" message, the device specified probably does not exist. The output above indicates that a valid image is indeed present in the Flash. Try to boot from that image using the **boot** command.
> 
```
rommon 2 > **boot flash:c2600-i-mz.122-10b.bin**
program load complete, entry point: 0x80008000, size: 0x51c0dc
Self decompressing the image : #################################################
##################################
...

```

The router should now boot with the Cisco IOS software image specified in the **boot** command. However, there are times when a valid image does not exist on any of the devices or the image on the Flash might be corrupted. In these cases, a valid image has to be downloaded using Trivial File Transfer Protocol (TFTP) or by using the Xmodem procedure. Both these procedures can be carried out from the ROMmon mode. 
**Note:** There are instances where the system message "Device does not contain a valid magic number" appears. If this happens, in addition to getting a valid Cisco IOS software image, you might need to reseat the Flash or replace it, if it is damaged. 
###  Download using TFTP from ROMmon 
This is the fastest way to re-install a new Cisco IOS software image on the router. Go to [Using the **tftpdnld** Command](http://www.cisco.com/warp/customer/471/76.html).
###  Download using Xmodem from ROMmon 
You can also download a new Cisco IOS software version through the console port, using Xmodem. Go to [Xmodem Console Download Procedure Using ROMmon](http://www.cisco.com/warp/customer/130/xmodem_generic.html). 
##  Related Information 
  * **[Technical Support - Cisco Systems](http://www.cisco.com/cisco/web/support/index.html?referring_site=bodynav) **


### Revision History  
| Revision  | Publish Date  | Comments  |  
| --- | --- | --- |  
| 1.0  |  14-Dec-2001   | Initial Release  |  
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/routers/2600-series-multiservice-platforms/15079-recovery-c2600.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [VG Series Gateways](https://www.cisco.com/c/en/us/support/unified-communications/vg-series-gateways/series.html)


By continuing to use our website, you acknowledge the use of cookies. 
[Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html) Change Settings
![Company Logo](https://cdn.cookielaw.org/logos/03fc55fe-0057-4b2f-817d-763e7ecdb316/a7f4c642-c43c-4666-acea-858c0449029c/cisco-logo-transparent.png)
## Consent Manager
Your opt out preference signal is honored.
## Consent Manager
  * ### Your Privacy
  * ### Strictly Necessary Cookies
  * ### Performance Cookies
  * ### Targeting Cookies
  * ### Functional Cookies


#### Your Privacy
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. From the list on left, please choose whether this site may use Performance and/or Targeting Cookies. By selecting Strictly Necessary Cookies only, you are requesting Cisco not to sell or share your personal data. Note, blocking some types of cookies may impact your experience on the site and the services we are able to offer.
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies provide metrics related to the performance and usability of our site. They are primarily focused on gathering information about how you interact with our site, including: page load times, response times, error messages, and allowing a replay of a visitor’s interactions with our site, which enables us to review and analyze visitor behavior, helping to improve site usability and functionality. These cookies also allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. If you do not allow these cookies we will not know when you have visited our site and will not be able to monitor its performance.
Cookies Details
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Cookies Details
Back Button
### Cookie List
Filter Button
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Clear
  * checkbox label label


Apply Cancel
Save Settings
Allow All
[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/solutions/consent-and-preferences/)
