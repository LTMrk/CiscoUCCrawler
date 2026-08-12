  * [Skip to content](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/bulletin-c25-2479306.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/bulletin-c25-2479306.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/bulletin-c25-2479306.html)


  * [Cisco.com Worldwide](https://www.cisco.com/site/us/en/index.html)
  * [Products and Services](https://www.cisco.com/c/en/us/products/index.html)
  * [Solutions](https://www.cisco.com/site/us/en/solutions/index.html)
  * [Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Learn](https://www.cisco.com/c/en/us/training-events.html)
  * [Explore Cisco](https://www.cisco.com/c/en/us/about/sitemap.html)
  * [How to Buy](https://www.cisco.com/c/en/us/buy.html)
  * [Partners Home](https://www.cisco.com/site/us/en/partners/index.html?dtid=odicdc001129)
  * [Partner Program](https://www.cisco.com/site/us/en/partners/cisco-partner-program/index.html?ccid=cc000864&dtid=odiprc001129)
  * [Support](https://www.cisco.com/site/us/en/partners/support-help/index.html)
  * [Tools](https://www.cisco.com/site/us/en/partners/tools/index.html?dtid=odiprc001129)
  * [Find a Cisco Partner](https://locatr.cloudapps.cisco.com/WWChannels/LOCATR/pf/index.jsp#/)
  * [Meet our Partners](https://www.cisco.com/site/us/en/partners/connect-with-a-partner/index.html?ccid=cc000864&dtid=odiprc001129)
  * [Become a Cisco Partner](https://www.cisco.com/site/us/en/partners/index.html?dtid=odicdc001129)


  * [](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/bulletin-c25-2479306.html)
  * [...](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/bulletin-c25-2479306.html)Show All Breadcrumbs
  * [Products & Services](https://www.cisco.com/c/en/us/products/index.html)
  * [Unified Communications](https://www.cisco.com/c/en/us/products/unified-communications/index.html)
  * [Communications Gateways](https://www.cisco.com/c/en/us/products/unified-communications/communications-gateways/index.html)
  * [Cisco Unified Border Element](https://www.cisco.com/c/en/us/products/unified-communications/unified-border-element/index.html)
  * [Bulletins](https://www.cisco.com/c/en/us/products/unified-communications/unified-border-element/bulletin-listing.html)


# End of Support for the H.323 call control features in Cisco IOS XE Software
Bulletin
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/products/collateral/unified-communications/unified-border-element/bulletin-c25-2479306.html) to Save Content 
Download
Print
### Available Languages
### Download Options
  * [PDF](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/bulletin-c25-2479306.pdf) (237.3 KB)   
View with Adobe Reader on a variety of devices


Updated:May 27, 2021
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/c/en/us/about/social-justice/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Contact Cisco
  * Contact Cisco
  * [Get a call from Sales](https://www.cisco.com/site/us/en/about/contact-cisco/index.html?linkclickid=luh-contactus)
  * Call Sales: [ 1-800-553-6387 ](tel:18005536387)   
US/CAN | 5am-5pm PT 
  * [Product / Technical Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Training & Certification](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)


Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/products/collateral/unified-communications/unified-border-element/bulletin-c25-2479306.html) to Save Content 
Download
Print
### Available Languages
### Download Options
  * [PDF](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/bulletin-c25-2479306.pdf) (237.3 KB)   
View with Adobe Reader on a variety of devices


Updated:May 27, 2021
#### Table of Contents
![Open Search](https://www.cisco.com/content/dam/eotToc/search-white_28x28.png)
![Close Search](https://www.cisco.com/content/dam/eotToc/close_11x11.png)
#### Table of Contents
  * [Overview](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/bulletin-c25-2479306.html#Overview "Overview")
  * [Product Migration Options](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/bulletin-c25-2479306.html#ProductMigrationOptions "ProductMigrationOptions")
  * [For more information](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/bulletin-c25-2479306.html#Formoreinformation "Formoreinformation")


Overview
Cisco announces the End of Support for H.323 call control features in Cisco IOS XE software.
IOS software for Cisco routers has provided H.323 call control since the introduction of voice features over twenty years ago. Now that most customers use Session Initiation Protocol (SIP) for multimedia session control, there is minimal demand for H.323 functionality.
In acknowledgement of this reduced demand, the Cisco IOS XE Bengaluru 17.5 release will be the last to provide support for H.323 features. No support for H.323 features will be provided from IOS XE release Bengaluru 17.6.1 onwards.
When upgrading to 17.5.1 or a subsequent rebuild, the following message will be displayed at the console during boot:
**WARNING:** ** NOTICE ** This is the final IOS XE release to provide support for the H.323 protocol. Consider switching to SIP for multimedia applications before upgrading to 17.6.1.
**Software maintenance** support for H.323 features will be aligned with the End-of-Life milestones for Cisco IOS XE 17.5.x. No patches or maintenance releases will be provided for H.323 features after those published dates.
Software maintenance requires an active service contract.
Product Migration Options
Customers are encouraged migrate networks to use SIP using the extensive feature set offered in Cisco IOS XE software.
For more information
For more information about the Cisco End-of-Life Policy, go to: <https://www.cisco.com/en/US/products/products_end-of-life_policy.html>.
For more information about the Cisco Product Warranties, go to: <https://www.cisco.com/en/US/products/prod_warranties_listing.html>.
To subscribe to receive end-of-life/end-of-sale information, go to: <https://www.cisco.com/cisco/support/notifications.html>.
Any authorized translation issued by Cisco Systems or affiliates of this end-of-life Product Bulletin is intended to help customers understand the content described in the English version. This translation is the result of a commercially reasonable effort; however, if there are discrepancies between the English version and the translated document, please refer to the English version, which is considered authoritative.
### Our experts recommend
  * [Cisco Unified Border Element (CUBE) Management and Manageability Specification](https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/white_paper_c11-613550.html "Cisco Unified Border Element \(CUBE\) Management and Manageability Specification")


### Learn more
