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
