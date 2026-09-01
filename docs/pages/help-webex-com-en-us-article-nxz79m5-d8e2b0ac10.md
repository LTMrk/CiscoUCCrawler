---
doc_id: help-webex-com-en-us-article-nxz79m5-d8e2b0ac10
source_url: https://help.webex.com/en-us/article/nxz79m5
retrieved_at: 2026-09-01T20:26:28.773238+00:00
---

Verify domains

Verify your domains to prove to Webex that you own them. Verifying domains allows you to claim users into your organization if
      they signed up into a different organization. You also must verify your domains before you can
      claim them.

To verify domains, we provide a token to add to your domain host's DNS TXT record. To confirm that you own the domain, we check for this token on the DNS server.

Claim domains

Claim a domain to associate that domain to automatically be created within your
      organization. Users who sign themselves up for Webex are also associate with this domain. Otherwise, users who sign themselves up are created in
      a general organization with all the other "free" users. You cannot manage their services until
      you claim the users into your organization. Keep in mind that you don’t have to claim a domain
      to claim a user into your organization.

Users who exist in the free consumer organization are not automatically converted to your organization. You must convert these users. We recommend that you convert consumer users to your organization before claiming the domain.

Domains aren't claimed for two different organizations. The purpose of the domain claim is to prevent other organizations from using the domain.

You can release a domain if you want to claim it in a different organization (if you own the domain and manage both organizations).

Before you begin

You must own the domains you want to verify and claim.

For Hybrid Calling for users and Webex-registered devices, you must verify domains that are contained in the on-premises
            directory URIs for end user accounts on Unified CM.

You are forced to verify in a particular order to prevent administrator lockout. For example, you must add the administrator domain first, followed by all the other domains.

Sign in to Control Hub .

In the left-hand navigation pane, under Management , click Organization Settings .

Scroll to Domains , and click either Add manually or Add with Entra ID .

There is no limit on the number of domains you can claim for your organization. If
                you have more than 20 claimed domains in a Webex organization, you may encounter issues converting users.

You must have full administrator privilages and have added and
                  configured the Entra ID Wizard App before you can select Add with Entra ID .

If you choose Add with Entra ID , you don’t need to add a TXT
                record to your DNS server, as domain ownership is verified automatically through
                your identity provider.

Enter your domain name and click Add .

Click the ellipsis beside your domain and choose Retrieve
                        verification token .

Copy the verification token into your DNS TXT record.

If your DNS host supports only one TXT record, add the token on a
                                separate line.

If your DNS host supports multiple records, add your token on a
                                single line in its own TXT record.

Choose one:

Add the DNS TXT record to your DNS server.

If your DNS server is configured by another administrator, send the
                                DNS TXT record to your administrator to add to your DNS server.

Click Verify next to each domain.

If the verification fails, the error is cached by your DNS server. Your DNS
                        server clears the cache after the specified length of time in the Time To
                        Live (TTL) setting. You must wait to try again after the DNS server clears
                        the cache. You can add the verification token again and request the
                        verification for the domain.

If the verification token is found and matched, the domain status changes to verified
            in Control Hub. To confirm that your domains are verified, go to Control Hub, click Organization Settings , scroll to Domains , and then confirm that this status appears next to the
            domain entries:

If a domain is verified in multiple organizations, it can’t be claimed by any of them. To claim a
              domain, it must only be verified in your organization.

After the domain is verified, the TXT record is no longer required and you
                        can remove the verification token from your DNS server.

Although you've verified a domain, other organizations may continue to have
                        users with this domain. Old consumer accounts won’t be automatically
                        converted to organization users. If your domains are verified and users
                        signed up for Webex App accounts, you can convert those users to licensed users in your
                        organization.

The steps in Control Hub let you verify domains first, and then claim domains next as a further security measure.

Domain claim means that you're claiming an email domain for use only in your Webex organization .

This step prevents users with the claimed domain from being created in any other organization, including the free consumer organization.

No other Webex organization can add users using your claimed domains.

If you claim a domain, users can still self-register, and Webex creates them in your organization.

You can prevent users from self-registering if you want to control user creation/synchronization in your organization.

You can only claim a domain if it is verified in a single organization. If the same domain is verified in more than one organization, you won’t be able to claim it in any of those organizations. To claim the domain, make sure it is only verified in your organization.

Before you begin

Registration errors can occur as a result of errors that are made in claiming domains. Before you claim any domains, make sure that you understand the following:

Service Providers should not claim the domains of customer organizations that they manage. They should claim only the domains of those users that are in the Service Provider's internal organization. Claiming the domain of users in a separate organization (even one that the Service Provider manages) can result in registration errors for the users in the customer organization as user authentication requests get routed through the Service Provider rather than the customer organization.

If two customer organizations (Company A and Company B) share the same domain and Company A has claimed the domain, registration for Company B users may fail due to the fact that user authentication requests are routed through the organization that has the domain claimed (Company A).

Before a domain claim, you must ensure that your domains are verified. Otherwise,
                    your request may be rejected for security reasons. For example, you cannot claim
                    a domain that belongs to another enterprise.

Sign in to Control Hub .

Under Management , click Organization Settings .

Scroll to Domains , click , then select Claim verified domain .

Select Claim .

After a domain is claimed, the status appears next to the domain entries as:

After a domain is claimed, admins outside of the organization who attempt to add users using a claimed domain will receive an error message. Users who exist within another organization before the domain was claimed are not affected.

What to do next

If you verified or claimed domains and want your Webex App users to be in a Verified state before they sign in for the first time,
                        you can replace the email validation by doing the following:

Use Cisco Directory Connector to
                                synchronize users from an Active Directory into Webex App.

Configure Single Sign-On (SSO) by
                                integrating your organization's identity provider (IdP) with your
                                    Webex organization.

Suppress automated emails .

Activated users appear with a Verified status in Control Hub. After they sign in, they appear as Active. For more information about user statuses, see Users list in Control Hub .

You may want to prevent users from self-registering with your claimed domains. For more information, see Prevent users from self-registering with your domain .

Assign services to your users. While domain claim aligns users to your
                        organization, these users only have free services until you add extra paid
                        services to each user.

You may need to remove a verified domain or release a claimed domain from your organization. For example, if your organization sold a domain or you ran a trial with a test domain and the trial finished. You can remove a domain at any time.

Before you begin

If your organization uses Webex Hybrid Call Service, you may affect the service if you remove a verified domain that is contained
                    in your users' on-premises directory URIs.

Sign in to Control Hub .

Under Management , click Organization Settings .

Scroll to Domains , click beside the domain you want to remove, and choose one:

- For a claimed domain, click Release domain , read the prompt, then click Release . This step retains the domain as a verified entry.

- For a verified domain, click Remove domain , read the prompt, then click Remove . This step completely removes the domain from the list in Control Hub.

After you release a claimed domain, it's possible for new users with that domain to join an organization than your own. This behavior does not affect users who are already in your organization.

Removing a domain means that it's no longer verified or claimed in your organization.

For information on domain management for Webex for Government, see Domain management in Webex for Government .

If you experience problems with domain verification in Control Hub, refer to Domain Verification Failed in Control Hub to help you verify your
        domains more effectively.

For more information, see Add, Verify, and Troubleshoot a Domain for Control Hub to ensure smooth domain management in your organization.

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | In the left-hand navigation pane, under Management , click Organization Settings . |
| 3 | Scroll to Domains , and click either Add manually or Add with Entra ID . There is no limit on the number of domains you can claim for your organization. If
                you have more than 20 claimed domains in a Webex organization, you may encounter issues converting users. You must have full administrator privilages and have added and
                  configured the Entra ID Wizard App before you can select Add with Entra ID . If you choose Add with Entra ID , you don’t need to add a TXT
                record to your DNS server, as domain ownership is verified automatically through
                your identity provider. |
| 4 | Enter your domain name and click Add . |
| 5 | Click the ellipsis beside your domain and choose Retrieve
                        verification token . |
| 6 | Copy the verification token into your DNS TXT record. If your DNS host supports only one TXT record, add the token on a
                                separate line. If your DNS host supports multiple records, add your token on a
                                single line in its own TXT record. |
| 7 | Choose one: Add the DNS TXT record to your DNS server. If your DNS server is configured by another administrator, send the
                                DNS TXT record to your administrator to add to your DNS server. |
| 8 | Click Verify next to each domain. |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Under Management , click Organization Settings . |
| 3 | Scroll to Domains , click , then select Claim verified domain . |
| 4 | Select Claim . After a domain is claimed, the status appears next to the domain entries as: After a domain is claimed, admins outside of the organization who attempt to add users using a claimed domain will receive an error message. Users who exist within another organization before the domain was claimed are not affected. |

| 1 | Sign in to Control Hub . |
|---|---|
| 2 | Under Management , click Organization Settings . |
| 3 | Scroll to Domains , click beside the domain you want to remove, and choose one: For a claimed domain, click Release domain , read the prompt, then click Release . This step retains the domain as a verified entry. For a verified domain, click Remove domain , read the prompt, then click Remove . This step completely removes the domain from the list in Control Hub. After you release a claimed domain, it's possible for new users with that domain to join an organization than your own. This behavior does not affect users who are already in your organization. Removing a domain means that it's no longer verified or claimed in your organization. |