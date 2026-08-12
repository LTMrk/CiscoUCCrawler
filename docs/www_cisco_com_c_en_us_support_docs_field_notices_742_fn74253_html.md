  * [Skip to content](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74253.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74253.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74253.html)


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


  * [](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74253.html)
  * [...](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74253.html)Show All Breadcrumbs
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Product Support](https://www.cisco.com/c/en/us/support/all-products.html)
  * [Servers - Unified Computing](https://www.cisco.com/c/en/us/support/servers-unified-computing/category.html)
  * [Cisco UCS C-Series Rack Servers](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/series.html)
  * [Field Notices](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-rack-servers/products-field-notices-list.html)


# Field Notice: FN74253 - Specific NVMe Drives or Solid-State Drives in Cisco UCS Servers May Experience Operational Failures in Certain Conditions - BIOS/Firmware Upgrade Recommended
  * Products Affected
  * Problem Description
  * Problem Symptom
  * Workaround/Solution


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/742/fn74253.html) to Save Content 
[ Translations ](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74253.html)
Print
### Available Languages
  * [Japan - 日本語](https://www.cisco.com/c/ja_jp/support/docs/field-notices/742/fn74253.html)


Updated:December 5, 2025
Document ID:FN74253
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
High
**Impact Rating:**
High
**First Published:**
2025-May-23
**Last Published:**
2025-Dec-05
**Revision:**
2.1
**Cisco Bug IDs:**
  * [CSCwo08959](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwo08959), 
  * [CSCwo20489](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwo20489), 
  * [CSCwo19083](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwo19083)

[More](javascript:void\(0\);)
### Notice
**THIS FIELD NOTICE IS PROVIDED ON AN "AS IS" BASIS AND DOES NOT IMPLY ANY KIND OF GUARANTEE OR WARRANTY, INCLUDING THE WARRANTY OF MERCHANTABILITY. YOUR USE OF THE INFORMATION ON THE FIELD NOTICE OR MATERIALS LINKED FROM THE FIELD NOTICE IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS FIELD NOTICE AT ANY TIME.**
### Products Affected
  
  
| Affected Product Name  | Description  | Comments  |  
| --- | --- | --- |  
 |  
| HCI-M2-I240GB  | 240GB M.2 Boot SATA Intel SSD  |   |  
| HCI-M2-I240GB-M6  | 240GB SATA M.2 SSD  |   |  
| HCI-M2-I480GB  | 480GB M.2 Boot SATA Intel SSD  |   |  
| HCI-M2240OA1V  | 240GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| HCI-M2240OA1VM6  | 240GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| HCI-M2480OA1V  | 480GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| HCI-M2480OA1VM6  | 480GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| HCI-NVB15TO1V  | 15.3TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X NVMe  |   |  
| HCI-NVB15TO1VM6  | 15.3TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X NVMe  |   |  
| HCI-NVME4-1920  | 1.9TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| HCI-NVME4-1920-M6  | 1.9TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| HCI-NVME4-3200  | 3.2TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End NVMe (3X)  |   |  
| HCI-NVME4-3200-M6  | 3.2TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End NVMe (3X)  |   |  
| HCI-NVME4-3840  | 3.8TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| HCI-NVME4-3840-M6  | 3.8TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| HCI-NVMEI4I1920M6  | 1.9TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| HCI-NVMEI4I3840M6  | 3.8TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| HCI-NVMEI4I7680M6  | 7.6TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| HCI-SD38T6I1X-EV  | 3.8TB 2.5in Enter Value 6G SATA Intel SSD  |   |  
| HCI-SD38T6I1XEVM6  | 3.8TB 2.5in Enter Value 6G SATA Intel SSD  |   |  
| HCI-SDB480OA1P  | 480GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| HCI-SDB480OA1PM6  | 480GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| HCIX-M2-I240GB  | 240GB M.2 Boot SATA Intel SSD  |   |  
| HCIX-M2-I480GB  | 480GB M.2 Boot SATA Intel SSD  |   |  
| HCIX-M2240OA1V  | 240GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| HCIX-M2480OA1V  | 480GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| HCIX-NVB15TO1V  | 15.3TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X NVMe  |   |  
| HCIX-NVME4-1920  | 1.9TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| HCIX-NVME4-3200  | 3.2TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End NVMe (3X)  |   |  
| HCIX-NVME4-3840  | 3.8TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| HX-HY960G63X-EP  | ^960GB 3.5in Enterprise performance 6GSATA SSD(3X endurance)  |   |  
| HX-M2-I240GB  | 240GB SATA M.2 SSD  |   |  
| HX-M2-I480GB  | 480GB SATA M.2 SSD  |   |  
| HX-NVME4-1920  | 1.9TB 2.5in U.2 P5520 NVMe High Perf Medium Endurance  |   |  
| HX-NVME4-3200  | ^3.2TB 2.5in U.2 P5620 NVMe High Perf High Endurance  |   |  
| HX-NVME4-3840  | 3.8TB 2.5in U.2 P5520 NVMe High Perf Medium Endurance  |   |  
| HX-NVMEI4-I1600  | 1.6TB 2.5in U.2 Intel P5600 NVMe High Perf Medium Endurance  |   |  
| HX-NVMEI4-I1920  | 1.9TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| HX-NVMEI4-I3200  | 3.2TB 2.5in U.2 Intel P5600 NVMe High Perf Medium Endurance  |   |  
| HX-NVMEI4-I3840  | 3.8TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| HX-NVMEI4-I6400  | 6.4TB 2.5in U.2 Intel P5600 NVMe High Perf Medium Endurance  |   |  
| HX-NVMEI4-I7680  | 7.6TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| HX-SD38T63X-EP  | ^3.8TB 2.5 in Enterprise performance 6GSATA SSD(3X endurance)  |   |  
| HX-SD38T6I1X-EV  | 3.8TB 2.5 inch Enterprise Value 6G SATA SSD  |   |  
| HX-SD38TI6-EV  | ^3.8TB 2.5 inch Enterprise Value 6G SATA SSD  |   |  
| HX-SD480GBIS6-EV  | 480GB 2.5 inch Enterprise Value 6G SATA SSD  |   |  
| HX-SD960G63X-EP  | 960GB 2.5in Enterprise performance 6GSATA SSD(3X endurance)  |   |  
| HX-SD960G6I1X-EV  | 960GB 2.5 inch Enterprise Value 6G SATA SSD  |   |  
| HX-SD960GIS3-EP  | ^960GB 2.5in Enterprise performance 6GSATA SSD(3X endurance)  |   |  
| HXE-NVME4-3840  | Cisco HX Express 3.8TB2.5inU.2 P5520NVMeHighPerf Med Endur  |   |  
| HXE-NVMEI4-I3840  | Cisco HX Express 3.8TB 2.5in U.2 Intel P5500 NVMe HPer MEnd  |   |  
| HXE-NVMEI4-I7680  | Cisco HX Express 7.6TB 2.5in U.2 Intel P5500 NVMe HPer MEnd  |   |  
| IWA-SDB480OA1PM6  | 480GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| UCS-HY960G63X-EP  | 960GB 3.5in Enterprise performance 6GSATA SSD(3X endurance)  |   |  
| UCS-M2-I240GB  | 240GB M.2 Boot SATA Intel SSD  |   |  
| UCS-M2-I240GB-D  | 240GB M.2 Boot SATA Intel SSD  |   |  
| UCS-M2-I480GB  | 480GB M.2 Boot SATA Intel SSD  |   |  
| UCS-M2-I480GB-D  | 480GB M.2 Boot SATA Intel SSD  |   |  
| UCS-M2240OA1V  | 240GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| UCS-M2240OA1VM6  | 240GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| UCS-M2480OA1V  | 480GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| UCS-M2480OA1VM6  | 480GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| UCS-NVB12T8O1P  | 12.8TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End 3X NVMe  |   |  
| UCS-NVB15TO1V  | 15.3TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X NVMe  |   |  
| UCS-NVB15TO1VM6  | 15.3TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X NVMe  |   |  
| UCS-NVB1T6O1P  | 1.6TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End 3X NVMe  |   |  
| UCS-NVB1T9O1V  | 1.9TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X NVMe  |   |  
| UCS-NVB3T2O1P  | 3.2TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End 3X NVMe  |   |  
| UCS-NVB3T8O1V  | 3.8TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X NVMe  |   |  
| UCS-NVB6T4O1P  | 6.4TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End 3X NVMe  |   |  
| UCS-NVB7T6O1V  | 7.6TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X NVMe  |   |  
| UCS-NVME4-15360  | 15.3TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| UCS-NVME4-1600  | 1.6TB 2.5in U.2 15mm P5620 Hg Perf Hg End NVMe (3X)  |   |  
| UCS-NVME4-1920  | 1.9TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| UCS-NVME4-1920-D  | 1.9TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| UCS-NVME4-3200  | 3.2TB 2.5in U.2 15mm P5620 Hg Perf Hg End NVMe (3X)  |   |  
| UCS-NVME4-3200-D  | 3.2TB 2.5in U.2 15mm P5620 Hg Perf Hg End NVMe (3X)  |   |  
| UCS-NVME4-3840  | 3.8TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| UCS-NVME4-3840-D  | 3.8TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| UCS-NVME4-6400  | 6.4TB 2.5in U.2 15mm P5620 Hg Perf Hg End NVMe (3X)  |   |  
| UCS-NVME4-7680  | 7.6TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| UCS-NVMEI4-I1600  | 1.6TB 2.5in U.2 Intel P5600 NVMe High Perf Medium Endurance  |   |  
| UCS-NVMEI4-I1920  | ^1.9TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| UCS-NVMEI4-I3200  | 3.2TB 2.5in U.2 Intel P5600 NVMe High Perf Medium Endurance  |   |  
| UCS-NVMEI4-I3840  | ^3.8TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| UCS-NVMEI4-I6400  | 6.4TB 2.5in U.2 Intel P5600 NVMe High Perf Medium Endurance  |   |  
| UCS-NVMEI4-I7680  | ^7.6TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| UCS-SD19T63X-EP  | 1.9TB 2.5in Enter Perf 6G SATA Intel SSD (3X)  |   |  
| UCS-SD19TBI6-EP  | 1.9TB 2.5in Enterprise performance 6GSATA SSD(3X endurance)  |   |  
| UCS-SD19TIS3-EP  | 1.9TB 2.5in Enterprise performance 6GSATA SSD(3X endurance)  |   |  
| UCS-SD38T63X-EP  | 3.8TB 2.5in Enter Perf 6G SATA Intel SSD (3X)  |   |  
| UCS-SD38T63X-EP-D  | 3.8TB 2.5in Enter Perf 6G SATA Intel SSD (3X)  |   |  
| UCS-SD38T6I1X-EV  | 3.8TB 2.5in Enter Value 6G SATA Intel SSD  |   |  
| UCS-SD38T6I1XEV-D  | 3.8TB 2.5in Enter Value 6G SATA Intel SSD  |   |  
| UCS-SD38TBIS6-EV  | 3.8TB 2.5 inch Enterprise Value 6G SATA SSD  |   |  
| UCS-SD38TI6-EV  | 3.8TB 2.5 inch Enterprise Value 6G SATA SSD  |   |  
| UCS-SD480G63X-EP  | 480GB 2.5in Enter Perf 6G SATA Intel SSD (3X)  |   |  
| UCS-SD480G6I1X-EV  | 480 GB 2.5in Enter Value 6G SATA Intel SSD  |   |  
| UCS-SD480GBI6-EP  | 480GB 2.5in Enterprise performance 6GSATA SSD(3X endurance)  |   |  
| UCS-SD480GBIS6-EV  | 480GB 2.5 inch Enterprise Value 6G SATA SSD  |   |  
| UCS-SD480GI6-EV  | 480 GB 2.5 inch Enterprise Value 6G SATA SSD  |   |  
| UCS-SD480GIS3-EP  | 480GB 2.5in Enterprise performance 6GSATA SSD(3X endurance)  |   |  
| UCS-SD960G63X-EP  | 960GB 2.5in Enter Perf 6G SATA Intel SSD (3X)  |   |  
| UCS-SD960G63XEP-D  | 960GB 2.5in Enter Perf 6G SATA Intel SSD (3X)  |   |  
| UCS-SD960G6I1X-EV  | 960GB 2.5in Enter Value 6G SATA Intel SSD  |   |  
| UCS-SD960GBI6-EP  | 960GB 2.5in Enterprise performance 6GSATA SSD(3X endurance)  |   |  
| UCS-SD960GBIS6-EV  | 960GB 2.5 inch Enterprise Value 6G SATA SSD  |   |  
| UCS-SD960GI6-EV  | 960GB 2.5 inch Enterprise Value 6G SATA SSD  |   |  
| UCS-SD960GIS3-EP  | 960GB 2.5in Enterprise performance 6GSATA SSD(3X endurance)  |   |  
| UCS-SDB1T9OA1P  | 1.9TB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| UCS-SDB3T8OA1P  | 3.8TB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| UCS-SDB3T8OA1V  | 3.8TB 2.5in 15mm Solidigm S4520 Enter Value 6G SATA 1X SSD  |   |  
| UCS-SDB480OA1P  | 480GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| UCS-SDB480OA1PM6  | 480GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| UCS-SDB480OA1V  | 480GB 2.5in 15mm Solidigm S4520 Enter Value 6G SATA 1X SSD  |   |  
| UCS-SDB960OA1P  | 960GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| UCS-SDB960OA1V  | 960GB 2.5in 15mm Solidigm S4520 Enter Value 6G SATA 1X SSD  |   |  
| UCSB-NVA15TO1V  | 15.3TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X NVMe  |   |  
| UCSB-NVA1T6O1P  | 1.6TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End 3X NVMe  |   |  
| UCSB-NVA1T9O1V  | 1.9TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X NVMe  |   |  
| UCSB-NVA3T2O1P  | 3.2TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End 3X NVMe  |   |  
| UCSB-NVA3T8O1V  | 3.8TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X NVMe  |   |  
| UCSB-NVA6T4O1P  | 6.4TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End 3X NVMe  |   |  
| UCSB-NVA7T6O1V  | 7.6TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X NVMe  |   |  
| UCSB-NVME4-15360  | 15.3TB 2.5in U.2 Intel P5520 NVMe High Perf Medium Endurance  |   |  
| UCSB-NVME4-1600  | 1.6TB 2.5in U.2 Intel P5620 NVMe High Perf High Endurance  |   |  
| UCSB-NVME4-1920  | 1.9TB 2.5in U.2 Intel P5520 NVMe High Perf Medium Endurance  |   |  
| UCSB-NVME4-3200  | 3.2TB 2.5in U.2 Intel P5620 NVMe High Perf High Endurance  |   |  
| UCSB-NVME4-3840  | 3.8TB 2.5in U.2 Intel P5520 NVMe High Perf Medium Endurance  |   |  
| UCSB-NVME4-6400  | 6.4TB 2.5in U.2 Intel P5620 NVMe High Perf High Endurance  |   |  
| UCSB-NVME4-7680  | 7.6TB 2.5in U.2 Intel P5520 NVMe High Perf Medium Endurance  |   |  
| UCSB-SDA1T9OA1P  | 1.9TB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| UCSB-SDA3T8OA1V  | 960GB 2.5in 15mm Solidigm S4520 Enter Perf 6G SATA 1X SSD  |   |  
| UCSB-SDA480OA1P  | 480GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| UCSB-SDA480OA1V  | 3.8TB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| UCSB-SDA960OA1P  | 960GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| UCSB-SDA960OA1V  | 480GB 2.5in 15mm Solidigm S4520 Enter Perf 6G SATA 1X SSD  |   |  
| UCSB-SDC1T9OA1P  | 1.9TB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| UCSB-SDC3T8OA1V  | 3.8TB 2.5in 15mm Solidigm S4520 Enter Perf 6G SATA 1X SSD  |   |  
| UCSB-SDC480OA1P  | 480GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| UCSB-SDC480OA1V  | 480GB 2.5in 15mm Solidigm S4520 Enter Perf 6G SATA 1X SSD  |   |  
| UCSB-SDC960OA1P  | 960GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| UCSB-SDC960OA1V  | 960GB 2.5in 15mm Solidigm S4520 Enter Perf 6G SATA 1X SSD  |   |  
| UCSSD960G6I1XEV-D  | 960GB 2.5in Enter Value 6G SATA Intel SSD  |   |  
| UCSX-M2-I240GB  | 240GB M.2 Boot SATA Intel SSD  |   |  
| UCSX-M2-I240GB-D  | 240GB M.2 Boot SATA Intel SSD  |   |  
| UCSX-M2-I480GB  | 480GB M.2 Boot SATA Intel SSD  |   |  
| UCSX-M2-I480GB-D  | 480GB M.2 Boot SATA Intel SSD  |   |  
| UCSX-M2240OA1V  | 240GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| UCSX-M2240OA1VM6  | 240GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| UCSX-M2480OA1V  | 480GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| UCSX-M2480OA1VM6  | 480GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| UCSX-NVB12T8O1P  | 12.8TB 2.5in U.2 15mm Solidigm P5620 Hg Perf Hg End 3X NVMe  |   |  
| UCSX-NVB15TO1V  | 15.3TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X NVMe  |   |  
| UCSX-NVB15TO1VM6  | 15.3TB 2.5in U.2 15mm Solidigm P5520 Hg Perf Med End 1X NVMe  |   |  
| UCSX-NVME4-1920  | 1.9TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| UCSX-NVME4-1920-D  | 1.9TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| UCSX-NVME4-3200  | 3.2TB 2.5in U.2 15mm P5620 Hg Perf Hg End NVMe (3X)  |   |  
| UCSX-NVME4-3200-D  | 3.2TB 2.5in U.2 15mm P5620 Hg Perf Hg End NVMe (3X)  |   |  
| UCSX-NVME4-3840  | 3.8TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| UCSX-NVME4-3840-D  | 3.8TB 2.5in U.2 15mm P5520 Hg Perf Med End NVMe  |   |  
| UCSX-NVMEI4-I1600  | 1.6TB 2.5in U.2 Intel P5600 NVMe High Perf High Endurance  |   |  
| UCSX-NVMEI4-I1920  | ^1.9TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| UCSX-NVMEI4-I3200  | 3.2TB 2.5in U.2 Intel P5600 NVMe High Perf High Endurance  |   |  
| UCSX-NVMEI4-I3840  | ^3.8TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| UCSX-NVMEI4-I6400  | 6.4TB 2.5in U.2 Intel P5600 NVMe High Perf High Endurance  |   |  
| UCSX-NVMEI4-I7680  | ^7.6TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| UCSX-SD38T63X-EP  | 3.8TB 2.5in Enter Perf 6G SATA Intel SSD (3X)  |   |  
| UCSX-SD38T63XEP-D  | 3.8TB 2.5in Enter Perf 6G SATA Intel SSD (3X)  |   |  
| UCSX-SD38T6I1X-EV  | 3.8TB 2.5in Enter Value 6G SATA Intel SSD  |   |  
| UCSX-SD960G63X-EP  | 960GB 2.5in Enter Perf 6G SATA Intel SSD (3X)  |   |  
| UCSX-SD960G6I1XEV  | 960GB 2.5in Enter Value 6G SATA Intel SSD  |   |  
| UCSX-SDB480OA1P  | 480GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| UCSX-SDB480OA1PM6  | 480GB 2.5in 15mm Solidigm S4620 Enter Perf 6G SATA 3X SSD  |   |  
| UCSXE-M2240OA1V  | 240GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| UCSXE-M2480OA1V  | 480GB M.2 Boot Solidigm S4520 SATA 1X SSD  |   |  
| UCSXNVMEI4I1600-D  | ^1.6TB 2.5in U.2 Intel P5600 NVMe High Perf High Endurance  |   |  
| UCSXNVMEI4I1920-D  | ^1.9TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| UCSXNVMEI4I3200-D  | ^3.2TB 2.5in U.2 Intel P5600 NVMe High Perf High Endurance  |   |  
| UCSXNVMEI4I3840-D  | ^3.8TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| UCSXNVMEI4I6400-D  | ^6.4TB 2.5in U.2 Intel P5600 NVMe High Perf High Endurance  |   |  
| UCSXNVMEI4I7680-D  | ^7.6TB 2.5in U.2 Intel P5500 NVMe High Perf Medium Endurance  |   |  
| UCSXS960G6I1XEV-D  | 960GB 2.5 inch Enterprise Value 6G SATA Intel SSD  |   |  
| UCSXSD38T6I1XEV-D  | 3.8TB 2.5in Enter Value 6G SATA Intel SSD  |   |  
| UCSXSD960G63XEP-D  | 960GB 2.5in Enter Perf 6G SATA Intel SSD (3X)  |   |  
| UCSXSD960G6I1XEVD  | 960GB 2.5in Enter Value 6G SATA Intel SSD  |   |  
| UCSXSD960G6S1XEVD  | 960GB 2.5in Enter Value 6G SATA Samsung SSD  |   |  
  
  

  

### Defect Information
  
  
| **Defect ID**  | **Headline**  |  
| --- | --- |  
| [CSCwo08959](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwo08959)  | In some circumstances, NVMe drives may fail or go missing  |  
| [CSCwo20489](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwo20489)  | In some circumstances, SSD Drives may fail or go missing  |  
| [CSCwo19083](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwo19083)  | In some circumstances, SSD drives may fail or go missing  |  
  

### Problem Description
  

Under certain conditions, specific NVMe or SATA solid-state drives (SSDs) that are used in Cisco UCS X-Series Servers, Cisco UCS B-Series Blade Servers, and Cisco UCS C-Series Rack Servers might experience operational failures.
**Note** : HX Servers are included in this field notice as part of Cisco UCS C-Series Rack Servers.
  

### Background
  

Cisco has identified a firmware-related defect in certain NVMe and SATA SSDs that are used in Cisco UCS Servers that may result in drive failures due to improper voltage handling. A firmware upgrade is required to address this issue. For a list of affected product identifiers (PIDs), see the **Products Affected** section of this field notice.
  

### Problem Symptom
  

When a drive fails, the initial symptom is typically an alert or alarm in Cisco Integrated Management Controller (IMC), Cisco UCS Manager, or Cisco Intersight. The logs will display a message that is similar to the following:
> 
```
NVME disk FRONT-NVME-8 is inoperable: reseat or replace the NVME drive FRONT-NVME-8
```

A subsequent reboot will result in the drive being marked as missing. Once the drive has failed, it must be replaced.
  

### Workaround/Solution
  

**Workaround**
There is no workaround to address this issue. Once the drive fails, recovery is not possible.
**Solution**
To prevent this failure, upgrade drives to the appropriate fixed firmware release, depending on drive model and PID:
  * **NVMe drives:** 2CV1C036 / 9CV10490
  * **SATA SSD drives:** 7CV1CS05


The fixed firmware releases for Cisco UCS C-Series Rack Servers, Cisco UCS Manager, and Cisco IMM are available in the software releases that are listed in the following table.  
  
**Note:** For classic Cisco IMC and UCS Manager releases that are mapped to Intersight, see [Cisco UCS Equivalency Matrix for Cisco Intersight, Cisco IMC, and Cisco UCS Manager](https://www.cisco.com/c/dam/en/us/td/docs/unified_computing/ucs/c/sw/UCS-Equivalency-Matrix/index.html) for help finding the proper releases.
**Note:** Firmware release 7CV1CS05 is not in the 4.2(3) release train. Upgrade to Release 4.3 or use the 4.3 release bundle to upgrade the drive firmware only.  
| Affected Cisco Software Product  | Affected Release  | First Fixed Release  |  
| --- | --- | --- |  
| UCS C-Series Standalone Rack Servers  
**Note:** HX Servers are included in this field notice.  | 4.2(3m) and earlier  
4.3(2.240090) and earlier  
4.3(4.242038) and earlier  
4.3(5.250001)  | 4.2(3p)  
4.3(2.250016)  
4.3(4.242066)  
4.3(5.250030)  
4.3(6.250044)  |  
| Cisco UCS Manager connected C-Series, B-Series, and X-Series Servers  
**Note:** HX Servers are included in this field notice.  | 4.2(3n) and earlier  
4.3(5c) and earlier  | 4.2(3p)  
4.3(5d)  
4.3(6a)  |  
| Cisco Intersight Managed Mode C-Series, B-Series, and X-Series Servers  
**Note:** HX Servers are included in this field notice.  |  **C-Series:**  
4.3(2.240090) and earlier  
4.3(4.242038) and earlier  
4.3(5.250001) and earlier  
  
**B-Series and X-Series:**  
5.3(0.250001) and earlier  |  **C-Series:**  
4.3(2.250016)  
4.3(4.242066)  
4.3(5.250030)  
4.3(6.250044)  
  
**B-Series and X-Series:**  
X-Series M8 (X210c): 5.4(0.250037)  
X-Series M8 (X215c): 5.3(0.250021)  
B-Series and X-Series M6/M7: 5.3(0.250021)  |  
  

### How to Identify Affected Products
  

**Use Cisco IMC for NVMe Drives**
To identify the PID and firmware release of NVMe drives on a Cisco UCS C-Series Standalone Rack Server using Cisco IMC, complete the following steps:
  1. Log in to the Cisco IMC GUI.
  2. **PID Identification:** Choose **Computer > PID Catalog > HDD**. Note the PID under **Product ID** (see the image **Example of PID Catalog Page**). If the Product ID matches one of the PIDs in the **Products Affected** section of this field notice, continue to Step 3. If it does not match, the device is not affected.
  3. **Firmware Identification:** From the left-side menu, choose **Admin > Storage**.
  4. Choose the controller to which the NVMe drives are attached (see the image **Example of Physical Drive Info Page**).
  5. From the right-side pane, choose Physical Drive Info.
  6. Look under the Firmware Version column.


If the firmware starts with 2CV1C03*, 7CV1CS0*, or 9CV10*** and is earlier than 2CV1C036, 7CV1CS05, or 9CV10490, the firmware needs to be upgraded. The fixed firmware versions are 2CV1C036 (NVMe), 7CV1CS05 (SSD), and 9CV10490 (NVMe), depending on drive model and PID.
Upgrade the firmware if necessary. If you are unsure how to upgrade to a fixed release, contact the Cisco Technical Assistance Center (TAC) for assistance. For additional information, see [Identifying SSD/HDD Vendor Model and Drive Firmware](https://www.cisco.com/c/en/us/support/docs/servers-unified-computing/ucs-infrastructure-ucs-manager-software/215833-identifying-ssd-hdd-vendor-model-and-dri.html).
**  
  
Example of PID Catalog Page**
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/742/fn74253_4e910da68311ae10fceb70326daad308.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/742/fn74253_4e910da68311ae10fceb70326daad308.png "Related image, diagram or screenshot.")
**Example of Physical Drive Info Page**
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/742/fn74253_c3f9889183512a10fceb70326daad355.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/742/fn74253_c3f9889183512a10fceb70326daad355.png "Related image, diagram or screenshot.")
**Use Cisco IMC for SSD Drives**
To identify the PID and firmware release of SSD drives on a Cisco UCS C-Series Standalone Rack Server using Cisco IMC, complete the following steps:
  1. Log in to the Cisco IMC GUI.
  2. **PID Identification:** Click the menu in the top left corner and choose **Compute > PID Catalog > HDD**. Note the PID in the **Product ID** column (see the image **Example of PID Catalog Page**).
  3. If the Product ID matches one of the PIDs in the **Products Affected** section of this field notice, continue to Step 3. If it does not match, the device is not affected.
  4. **Firmware Identification:** From the left-side menu, choose **Admin > Storage**.
  5. Choose the controller to which the SSD drives are attached (see the image **Example of Physical Drive Info Page**).
  6. From the right-side pane, choose Physical Drive Info.
  7. Look under the Firmware Version column.


If the firmware starts with 2CV1C03*, 7CV1CS0*, or 9CV10*** and is earlier than 2CV1C036, 7CV1CS05, or 9CV10490, the firmware needs to be upgraded. The fixed firmware releases are 2CV1C036 (NVMe), 7CV1CS05 (SSD), and 9CV10490 (NVMe), depending on drive model and PID.
Upgrade the firmware if necessary. If you are unsure how to upgrade to a fixed release, contact Cisco TAC for assistance. For additional information, see [Identifying SSD/HDD Vendor Model and Drive Firmware](https://www.cisco.com/c/en/us/support/docs/servers-unified-computing/ucs-infrastructure-ucs-manager-software/215833-identifying-ssd-hdd-vendor-model-and-dri.html).
**Example of PID Catalog Page**
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/742/fn74253_4e910da68311ae10fceb70326daad308.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/742/fn74253_4e910da68311ae10fceb70326daad308.png "Related image, diagram or screenshot.")
**Example of Physical Drive Info Page**
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/742/fn74253_2643581d83512a10fceb70326daad3ea.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/742/fn74253_2643581d83512a10fceb70326daad3ea.png "Related image, diagram or screenshot.")
**Use Cisco UCS Manager**
To identify the PID and firmware release of NVMe or SSD drives using Cisco UCS Manager, complete the following steps:
  1. Log in to Cisco UCS Manager.
  2. From the left-side menu, choose **Equipment > Chassis > Chassis 1 > Servers** or **Equipment > Rack-Mounts > Servers**.
  3. Choose a server.
  4. In the right pane, choose **Inventory > Storage > Disks**.
  5. Find the storage controller that the disks are connected to and click the arrow to expand the section. (See the following image for reference.)
  6. Look at the Firmware Version column.


If the firmware starts with 2CV1C03*, 7CV1CS0*, or 9CV10*** and is earlier than 2CV1C036, 7CV1CS05, or 9CV10490, the firmware needs to be upgraded. The fixed firmware releases are 2CV1C036 (NVMe), 7CV1CS05 (SSD), and 9CV10490 (NVMe), depending on drive model and PID.
**Note:** It may be necessary to update the Host Firmware Policy (HFP) to include disks when upgrading.
**Example of Disk Information Page**
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/742/fn74253_df21f64ec3d922502f7fdbbf050131d2.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/742/fn74253_df21f64ec3d922502f7fdbbf050131d2.png "Related image, diagram or screenshot.")
**Use Cisco Intersight**
To identify the PID and firmware release of NVMe or SSD drives using Cisco Intersight, complete the following steps:
  1. Log in to Cisco Intersight with Account Administrator or Server Administrator role.
  2. In the left-side menu, under **Operate** choose **Servers**.
  3. In the right pane, choose the specific server to check.
  4. In the right pane, choose **Inventory > Storage Controllers > Physical Drives**.
  5. Look at the Firmware Version column.


If the firmware starts with 2CV1C03*, 7CV1CS0*, or 9CV10*** and is earlier than 2CV1C036, 7CV1CS05, or 9CV10490, the firmware needs to be upgraded. The fixed firmware releases are 2CV1C036 (NVMe), 7CV1CS05 (SSD), and 9CV10490 (NVMe), depending on drive model and PID.
For additional information, see [Identifying SSD/HDD Vendor Model and Drive Firmware](https://www.cisco.com/c/en/us/support/docs/servers-unified-computing/ucs-infrastructure-ucs-manager-software/215833-identifying-ssd-hdd-vendor-model-and-dri.html).
**Example of Server Inventory Page**
[![](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/742/fn74253_1fb103c6c35d22502f7fdbbf05013155.png)](https://www.cisco.com/c/dam/en/us/support/docs/field-notices/742/fn74253_1fb103c6c35d22502f7fdbbf05013155.png "Related image, diagram or screenshot.")
  

### Revision History
  
  
| **Version**  | **Description**  | **Section**  | **Date**  |  
| --- | --- | --- | --- |  
| 2.1  | Updated identification steps for brevity and clarity.  | How to Identify Affected Products  | 2025-DEC-05  |  
| 2.0  | Added additional affected products to PID list.  | Products Affected  | 2025-AUG-15  |  
| 1.1  | Updated information throughout field notice.  | Problem Description, Background, Problem Symptom, Workaround/Solution  | 2025-JUN-17  |  
| 1.0  | Initial Release  | —  | 2025-MAY-23  |  
  

### For More Information
For further assistance or for more information about this field notice, contact the Cisco Technical Assistance Center (TAC) using one of the following methods:
  * [Open a service request on Cisco.com](https://mycase.cloudapps.cisco.com/case)
  * [By email or telephone](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html)


### Receive Email Notification About New Field Notices
To receive email updates about Field Notices (reliability and safety issues), Security Advisories (network security issues), and end-of-life announcements for specific Cisco products, set up a profile in [My Notifications](https://cway.cisco.com/mynotifications).
[![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)Back to Top](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74253.html "Back to Top")
### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
### Contact Cisco
  * [Open a Support Case ![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)](https://mycase.cloudapps.cisco.com/start?prodDocUrl=https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74253.html)
  * (Requires a [Cisco Service Contract](https://www.cisco.com/c/en/us/services/order-services.html))


### This Document Applies to These Products
  * [UCS C220 M4 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c220-m4-rack-server/model.html)
  * [UCS C220 M5 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c220-m5-rack-server/model.html)
  * [UCS C220 M6 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c220-m6-rack-server/model.html)
  * [UCS C240 M4 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c240-m4-rack-server/model.html)
  * [UCS C240 M5 Rack Server](https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c240-m5-rack-server/model.html)


Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/login/index.html?referer=/c/en/us/support/docs/field-notices/742/fn74253.html)
Unleash the Power of TAC's Virtual Assistance
Unleash the Power of TAC's Virtual Assistance
[Login to enable assistance](https://www.cisco.com/c/en/us/support/docs/field-notices/742/fn74253.html)
