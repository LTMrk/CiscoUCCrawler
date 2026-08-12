  * [Skip to content](https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/unified-contact-center-enterprise/bulletin-c25-740815.html#eot-doc-wrapper)
  * [Skip to search](https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/unified-contact-center-enterprise/bulletin-c25-740815.html)
  * [Skip to footer](https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/unified-contact-center-enterprise/bulletin-c25-740815.html)


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


  * [](https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/unified-contact-center-enterprise/bulletin-c25-740815.html)
  * [Products & Services](https://www.cisco.com/c/en/us/products/index.html)
  * [Contact Center](https://www.cisco.com/c/en/us/products/contact-center/index.html)
  * [Cisco Unified Contact Center Enterprise](https://www.cisco.com/c/en/us/products/contact-center/unified-contact-center-enterprise/index.html)
  * [Bulletins](https://www.cisco.com/c/en/us/products/contact-center/unified-contact-center-enterprise/bulletin-listing.html)


# Cisco Contact Center Performance Effects from Side-Channel Information Disclosure Vulnerabilities Product Bulletin
Save
[Log in](https://www.cisco.com/c/login/index.html?referer=/c/en/us/products/collateral/customer-collaboration/unified-contact-center-enterprise/bulletin-c25-740815.html) to Save Content 
Download
Print
### Available Languages
### Download Options
  * [PDF](https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/unified-contact-center-enterprise/bulletin-c25-740815.pdf) (211.8 KB)   
View with Adobe Reader on a variety of devices


Updated:June 4, 2018
Document ID:1528140541316147
Bias-Free Language
### Bias-Free Language
The documentation set for this product strives to use bias-free language. For the purposes of this documentation set, bias-free is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity, sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that is used by a referenced third-party product. [Learn more](https://www.cisco.com/site/us/en/about/purpose/social-impact/inclusive-language-policy.html) about how Cisco is using Inclusive Language.
Under normal conditions, the Cisco® Unified Contact Center Enterprise (UCCE) Team has instructed customers to assess and apply Microsoft security updates as they see fit. Here is an excerpt of our policy from the link below: <https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/unified-contact-center-enterprise/product_bulletin_c25-455396.html>.
“Customers are responsible for reviewing any security update released by Microsoft for Windows, IIS, and SQL Server, and assessing their security exposure to the vulnerability. If deemed necessary, customers should follow Microsoft's guidelines to apply these updates to the relevant systems as soon as possible.”
Recent microprocessor side-channel vulnerabilities have been publicized in the media, dubbed “Meltdown” and “Spectre.” The Cisco impact is described in a PSIRT Advisory here: <https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180104-cpusidechannel>.
Because the root cause of these issues is the microprocessor design, a hardware fix is not practical. As a result, software and firmware updates from the vendors of the microprocessors, hardware, operating systems, and hypervisors are becoming available.
The primary concern with these fixes is that they may reduce processor performance, impacting contact center capacity. Intel has stated1 that the processing impacts are workload dependent and that initial testing2 has shown little performance impact, but there have also been reports3 that the impact could range from 5 to 30 percent, leading to customer concerns.
Cisco’s performance testing of contact center solutions with the available fixes shows a 2 to 5 percent increase in disk IOPS,4 as well as a reduction in memory page usage. These changes are not significant enough to require restructuring of the VM definitions or capacity changes.
**Notes:**
1) <https://newsroom.intel.com/news-releases/industry-testing-shows-recently-released-security-updates-not-impacting-performance-real-world-deployments/>
2) <https://newsroom.intel.com/news-releases/industry-testing-shows-recently-released-security-updates-not-impacting-performance-real-world-deployments/>
3) <https://www.theregister.co.uk/2018/01/02/intel_cpu_design_flaw/>
4) <https://blogs.technet.microsoft.com/srd/2018/03/23/kva-shadow-mitigating-meltdown-on-windows/>
### Contact Cisco
  * [Get a call from Sales](https://www.cisco.com/site/us/en/about/contact-cisco/index.html?linkclickid=luh-contactus)
  * ##### Call Sales:
  * [ 1-800-553-6387 ](tel:18005536387)
  * US/CAN | 5am-5pm PT
  * [Product / Technical Support](https://www.cisco.com/c/en/us/support/index.html)
  * [Training & Certification](https://www.cisco.com/site/us/en/learn/training-certifications/index.html)


### Was this Document Helpful?
Yes No [ ![Feedback](https://www.cisco.com/c/dam/cdc/i/Feedback_OceanBlue.png)Feedback](javascript:%20void\(0\);)
