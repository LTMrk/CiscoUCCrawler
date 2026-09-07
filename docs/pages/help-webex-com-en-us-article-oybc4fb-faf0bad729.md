---
doc_id: help-webex-com-en-us-article-oybc4fb-faf0bad729
source_url: https://help.webex.com/en-us/article/oybc4fb
retrieved_at: 2026-09-07T12:42:08.777928+00:00
---

## Overview

The overall goal of data residency (formerly called data locality) in Webex is to store user
      data in regional data centers corresponding with the customer's location. This offering is
      available for new customers and provides the following high-level functionality:

Our systems store your identities, such as email address and user ID, in your geographic
          region. Webex identity service processes client authentication requests locally in your
          region.

Users can continue to meet with, message, and call users in other organizations across
          the globe without the need for separate accounts in foreign clusters. This means that
          Webex doesn't proliferate additional personal data elements

- Encryption keys for your users are created and stored in your organization's geographic
        region, and the Key Management Service (KMS) in your region handles requests for the keys to
        encrypt and decrypt spaces, messages, and content in Webex App.

- Encrypted user-generated content (meetings, messages, whiteboards, files and related
        metadata) is stored in the organization's geographic region.

- AI-generated content for both meetings and messages is stored in the same data center as the user-generated content. This ensures all data remains within the same geographic region.

- We store data about your organization, such as verified domains, preferences, and security
        settings, in one geographic region.

- Webex Partners in one region can create customer organizations in any region that we offer
        the services.

- Webex Hybrid
          Services are supported in the region, including Hybrid Directory, Hybrid Calendar,
        Hybrid Calling, Video Mesh, Hybrid Data Security, and Hybrid Messages.

- Audit log retention is one year (12 months) in most regions and three years in India. When
        searching audit logs, you can only include activities from the past year. For more
        information, see Review your administrator activity log in Control Hub .

### Data center location of Webex services and user-generated content

Webex services and user-generated content

US

EU

Canada

UK

Japan

Australia

Singapore

Saudi Arabia

UAE

Webex Meetings*

✓

✓

✓

✓

✓

✓

✓

✓

Webex Messaging**

✓

✓

✓

Webex Calling***

✓

✓

✓

✓

✓

✓

✓

✓

Common identity

✓

✓

✓

✓

✓

Analytics

✓

✓

Encryption keys

✓

✓

✓

Hybrid Services (data security, calling, calendar, directory, video mesh, and
                  messages)

✓

✓

✓

✓

✓

✓

✓

✓

Webex Contact Center****

✓

✓

✓

✓

✓

✓

✓

* For the list of Webex Meetings data centers for the rest of world, refer to Webex
            Meetings Privacy data sheet .

** For the list of Webex Messaging data centers for the rest of world, refer to Webex
            Messaging Privacy data sheet .

*** For the list of Webex Calling data centers for the rest of world, refer to the Webex
            Calling Privacy data sheet .

**** For the list of Webex Contact Center data for the rest of world, refer to Data Locality in Contact Center .

## How we determine the data residency region

### Messaging data residency

During provisioning, the administrator who sets up an organization sees a Country Selector
        drop-down menu in Control Hub. We determine the geographic region in which the
        organization's data resides based on the mapping of the selected country to its
        corresponding DC. When you create a trial and select a country that maps to the European
        region for example, the organization's user-generated content is stored in the region as
        well as the user identities and encryption keys.

To determine which region a country maps to, you can download the Microsoft Excel file CountryCodeGEOMapping.xlsx and select the country
        name from the drop-down menu. The file begins to download immediately when you access the
        link.

### Meetings Data residency

Meetings data is stored in a data center based on the time zone that you select for a Webex
        Meetings site during provisioning. For example, if you select a time zone from one of the
        European Union cities, then the Meetings data will reside in the data center in Frankfurt.
        Meetings data for other time zones outside of the European Union will reside in whichever
        data center is closest to the selected city. For the list of Webex Meetings data centers for
        the rest of world, refer to Webex
          Meetings Privacy data sheet .

### Webex Calling residency

Calling data is stored in the data center closest to a customer’s principal place of
        business, as provided to Cisco by the Partner during the ordering process. Data residency is
        available in key markets in North America, Europe, and Asia and continue to expand to more
        regions. For the list of Webex Calling data centers, please refer to the Webex
          Calling Privacy data sheet .

### Webex Contact Center residency

Webex Contact Center has achieved data residency in many countries we do business in North
        America, Europe and Asia and continues to expand. Based on the Country of Operation
        drop-down list that you selected on the Contact Center tab in the
        Setup wizard, the system creates the tenant in the closest data center based on the Country
        of Operation to Data Center mapping defined in Data Locality in Contact Center .

### Administrator activity data residency

Administrator activities related to Webex Calling and Contact Center events originating from India are stored within data centers located in India. This
        ensures compliance with regional data residency requirements and legal regulations.

Customers with multiple clusters or data centers can view administrator activities
        generated across these locations. The storage location of these events is managed
        automatically by Webex, in accordance with your organizational location and legal requirements. Customers don’t
        have the ability to select or change where administrator activities are stored, ensuring
        compliance with data residency policies.

For more information, see Review your administrator activity log in Control Hub .

## Space ownership and content storage region

We store content in the region of the organization that owns the space where the content appears. Ownership depends on the type of space:

Group space—The owner is the organization of the person who created the space. We store
          content in the region of the owner organization.

Space within a team—The organization of the person who created the team owns spaces
          created within the team. Spaces created outside of the team and then moved into the team
          retain their original ownership. We store content in the region of the space owner's
          organization.

Conversation between two people (nongroup space)—If the people are in different organizations, each organization owns the content that its user posts. If the conversation includes a user from the North America/RoW GEO, we store the conversation content in the North America/RoW GEO.

Space created by a bot—We assign ownership to the organization of the first non-bot
          participant and store the content in the region of the owner's organization.

## Frequently asked questions for data residency

### Where can I find out where my data is located?

Cisco is transparent about the data residency of all the Webex services. Customer or
        partner administrators can verify the location of their Webex Services for Meetings,
        Messaging, and common application data by going to Account > Info > Data Locations in Control Hub.

For Webex Contact Center service, you can confirm data residency
        by going to Contact Center > Settings > Service Details > Country of Operation in Control Hub.

For legacy customers who are eligible for migrating their data to
        the new data centers in their regions, refer to Data center migration plans for your organization’s data in
          Control Hub .

### Why am I seeing a Country Selector during the organization provisioning process?

Cisco Webex is excited to provide customers the ability to localize certain Webex App data within “geo-based” data centers. During provisioning, the Country Selector
        determines which region will store a new customer organization's data. This includes
        organization identity, users' personal identities, encryption keys, and user-generated
        content (encrypted messages, boards, files, and related metadata).

Based on the Webex messages data center mapping pre-defined for each country , EU, Middle
        East, and Africa customers will be provisioned to EU data centers; US, Canada, APAC, and
        South America customers will be provisioned to US data centers.

Note that Webex Meetings sites are local to many global regions. For more details, refer to Webex
          Meetings Privacy data sheet . Customers from Canada can have their common
        application data and user profiles stored in Canadian data centers.

### Which GEO locations are currently supported for Webex Messaging?

We introduced the following locations, with the intention of expanding to more locations
        later:

Europe—Hosted in the data centers in Frankfurt and Amsterdam. This region is mapped
              to countries in Continental Europe, the Middle East, and Africa.

North America and Rest of the World (RoW)—Hosted in data centers in the United States.

### What is the recommendation when selecting a country for the GEO location?

A customer’s organization data is created and maintained in the GEO location where the Webex App service is provisioned. During provisioning, the administrator will see a new option for selecting a country from a drop-down menu. This action permanently sets the GEO location for the organization’s users and encryption keys.

When selecting the country for an organization, consider the following recommendations:

If the organization's users are primarily based in one country, select that country, even if it doesn't match the business address of the organization. This will improve the user experience and minimize latency by utilizing storage in the data centers closest to the users.

If the users are spread across multiple countries, select the country that has the highest user count. Keep in mind that all of the organization's users will have their data stored in the associated GEO location, even those who are not located in that country or GEO.

Ideally, the ship-to country and country of data residency are the same.

We do not currently support migrating between GEO locations. When you create an organization in a GEO, it stays in that GEO.

To check the GEO location that a particular country maps to, download the CountryCodeGEOMapping.xlsx file, open the file in
        Microsoft Excel, and select the country from the drop-down menu.

### Can my organization's users continue to collaborate with users in other regions?

Yes. Data residency strengthens the security and compliance features of Webex App without compromising the simplicity of the user experience. All users on our platform can communicate globally while retaining a single user identity.

### How does data residency impact compliance and visibility across GEOs?

Compliance officers continue to have 100% visibility on user content regardless of where
        the data is stored (based on the Webex App ownership model). This means that compliance capabilities like eDiscovery and cloud
        access security broker (CASB) integrations will continue to allow you to monitor and take
        action on data loss prevention events, even if your users collaborate with those from other
        regions. The administrator controls that are already available allow you to disable external
        communication as needed.

| Webex services and user-generated content | US | EU | Canada | UK | Japan | Australia | Singapore | Saudi Arabia | UAE | India |
|---|---|---|---|---|---|---|---|---|---|---|
| Webex Meetings* | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
| Webex Messaging** | ✓ | ✓ |  |  |  | ✓ |  |  | ✓ |  |
| Webex Calling*** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |
| Common identity | ✓ | ✓ | ✓ |  |  | ✓ | ✓ |  | ✓ |  |
| Analytics | ✓ | ✓ |  |  |  | ✓ |  |  |  |  |
| Encryption keys | ✓ | ✓ |  |  |  | ✓ |  |  | ✓ |  |
| Hybrid Services (data security, calling, calendar, directory, video mesh, and
                  messages) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |
| Webex Contact Center**** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |