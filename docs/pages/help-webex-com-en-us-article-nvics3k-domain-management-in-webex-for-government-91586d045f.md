---
doc_id: help-webex-com-en-us-article-nvics3k-domain-management-in-webex-for-government-91586d045f
source_url: https://help.webex.com/en-us/article/nvics3k/Domain-management-in-Webex-for-Government
retrieved_at: 2026-11-02T12:58:47.270847+00:00
---

We’re rolling out the domain management feature in phases. If you’re interested in this capability for your organization, contact your Cisco support team to have it enabled.

This article applies only to customers who are using Webex for Government. If you’re managing any other Webex organization, see Manage your domains .

You can choose whether to claim specific email domains for your Webex organization. This flexibility is important when you share a domain with other groups who have separate Webex organizations. When users in a claimed domain join Webex, they always onboard to the claiming organization. If no organization claims a given domain, each organization can onboard its own users in that domain.

When you don't want to claim a shared domain, you can instead reserve the domain
      for use only by Webex for Government organizations. When you reserve a domain, those email addresses can only onboard to a Webex for Government organization. Users can't create an account with those addresses in a commercial Webex
      organization, including the self-signup organization.

If you don't claim or reserve your domain, all user emails with that email domain are shared with the Webex commercial environment in encrypted form. To prevent email addresses from leaving the  authorized Webex for Government boundary, have your administrators claim or reserve your domains.

- Manage your domains

- Sharing with commercial Webex

- Domain states

The tasks in this section are in the natural sequence of a typical domain ownership
      lifecycle. Perform those that meet your needs.

See Domain states in this article to understand how these tasks change domain
      states, and how the actions affect your compliance.

Add and verify a domain

Sign in to https://admin-usgov.webex.com .

Under Management in the left-hand navigation pane, click Organization Settings .

Enter your domain name and click Add .

Click the ellipsis (…) beside your domain and choose Retrieve verification
            token .

Copy the verification token into your DNS TXT record.

- If your DNS host supports only one TXT record, add the token on a separate
            line.

- If your DNS host supports multiple records, add your token on a single line in its
            own TXT record.

Add the DNS TXT record to your DNS server.

If another administrator configures your DNS server, send the DNS TXT record to your
          administrator to add to your DNS server.

Click Verify next to each added domain.

Reserve a domain

Reserving a domain means that organizations outside of Webex for Government can’t add users with email addresses in this domain. However, any Webex for Government organization can have users in that domain. If any user existed in commercial Webex before you reserved the domain, you can trigger a mandatory email change for that users. These two rules enable different Webex for Government organizations to share domains.

Before you begin

Add and verify a domain to your organization.

Sign in to https://admin-usgov.webex.com .

Under Management in the left-hand navigation pane, click Organization Settings .

In the Domains section, find the verified domain that you want to reserve.

Click the ellipsis (…), then select Reserve domain .

If this domain includes users that exist in organizations that aren't in Webex for Government, Control Hub displays a message.

Read and acknowledge the message that reservation triggers removal of users with this domain from the commercial Webex organizations.

By accepting, you're committing to change those email addresses in the other organizations, so that your users don't lose their (presumably non-sensitive) data.

Click Continue .

Claim a domain

Sign in to https://admin-usgov.webex.com .

Under Management in the left-hand navigation pane, click Organization Settings .

Scroll to Domains and click the ellipsis (...) next to the
          domain that you want to claim, then select Claim verified
          domain .

Select Claim .

After you claim a domain, Control Hub marks it with a green dot.

What to do next

After you claim a domain, administrators outside of your organization can't add users with the claimed domain, and will receive an error message if they try to do so. Users who exist in another organization before you claim the domain aren't affected.

Release a reserved domain

You can release a reserved domain.

If you release a reserved domain, users in that domain can potentially join organizations that aren't in Webex for Government. Releasing the reservation shares your users’ email addresses in this domain with the commercial Webex environment (outside of Webex for Government). Although the commercial environment encrypts at-rest email addresses, most Webex for Government customers prefer to comply with their organizational mandate to keep all Webex data within the Webex for Government boundary.

You can only unreserve a domain if there are no users from that domain in any other Webex for Government organizations. You can’t unilaterally share the user email addresses of other Webex for Government organizations with the commercial Webex environment.

Sign in to https://admin-usgov.webex.com .

Under Management in the left-hand navigation pane, click Organization Settings .

In the Domains section, find the reserved domain that you want
          to release.

Click the ellipsis (...), then select Release reserved
          domain .

If you can’t release the reserved domain, an error message appears. In that case, contact Cisco TAC, who can coordinate with other organizations who are using the domain.

Read the warning, then check the box to acknowledge that you understand and agree to proceed.

Click Continue .

Remove a domain

Sign in to https://admin-usgov.webex.com .

Under Management in the left-hand navigation pane, click Organization Settings .

Scroll to Domains and click the ellipsis (…) beside the domain
          that you want to remove.

Click Remove domain , read the prompt, then click Remove .

This section covers how to check what emails and domains that you share from Webex for Government to the commercial Webex environments. It also covers what to do to stop sharing information with the commercial Webex environment.

Only an encrypted hash of the email or domain that is verified in Webex for Government is shared with the commercial Webex environment. Webex uses the hash to ensure that users are unique and routed to the right environment for authentication and authorization. Webex only shares the emails from your verified domains or consumer domains; for example, joe@gmail.com .

If you need to add domains, we strongly recommend reserving or claiming them. If you need to
      add users, issue their email addresses from an organization with a reserved or claimed
      domain.

Check what you share with commercial Webex

Sign in to https://admin-usgov.webex.com .

Under Management in the left-hand navigation pane, click Organization Settings .

Check your status in the FedRAMP compliance section.

- If your organization is FedRAMP Compliant , there’s nothing
            to do.

- Continue with this task if your organization is Out of FedRAMP
              Compliance .

Click Check my compliance and wait for Control Hub to show you
          the report.

- You can create users from commercial domains in your organization. If you temporarily enable this state so you can convert users to your organization, keeping it on keeps you out of compliance.

- Lists email addresses that are shared in the commercial Webex environment. These email addresses end in domains that are public, aren't reserved in Webex for Government, or aren't claimed by your organization.

- Lists domains in your organization that are shared in the commercial Webex environment. These domains are either pending or verified in your organization.

Click Continue .

Use the information from the report to understand what data you share with
          commercial Webex. (The other tasks in this section offer more detail). Complete the tasks
          that apply to your organization's situation and check your report again.

When the report shows green for all three categories, click Update FedRAMP
            status to declare that your organization doesn't share user emails and
          domains with commercial Webex.

Prevent sharing of user emails and domains with commercial Webex

Sign in to https://admin-usgov.webex.com .

Under Management in the left-hand navigation pane, click Organization Settings .

Find Sharing Email with Commercial Environment and turn it
          off.

Users whose email addresses aren’t in reserved or claimed domains can’t join your organization. A full administrator or user administrator can only create users in your organization from a reserved or claimed domain.

Review users and domains shared with commercial Webex

If users identified by your domains exist in commercial organizations, your Webex for Government organization is out of compliance. Remove or rename the users from all commercial organizations to bring your organization into compliance.

This procedure assumes you want to reuse those identities to create the users in your Webex for Governmentorganization.

Bringing data from commercially homed users into your Webex for Government organization is prohibited, as it violates our authorization to operate.

Sign in to https://admin-usgov.webex.com .

Under Management in the left-hand navigation pane, click Organization Settings .

Find all users from the previous report whose email addresses contain your Webex for Government domains.

If you don't manage the commercial organization where these users exist, contact Cisco
          TAC.

(Optional) As appropriate, choose what to do for each user:

- Source alternative addresses for the affected users if they are permitted to
            continue using that organization.

- Change those users' email addresses.

- Delete those users.

What to do next

Retest your compliance to confirm you have addressed everything in the report.

Manage domains shared with commercial Webex

Sign in to https://admin-usgov.webex.com .

Under Management in the left-hand navigation pane, click Organization Settings .

Read each of your domains' status.

Domains that are pending or verified can cause your organization to share information about their users with the commercial Webex environment. Users from those domains can sign up for a commercial licensed service.

For each pending domain, check you’ve met the requirements for verifying domain
          ownership. If the pending status persists, contact Cisco TAC.

For each verified domain, reserve or claim the verified domains.

If you can't reserve or claim a verified domain, you or another entity might previously
            have verified or claimed that domain.

The other entity needs to release and remove the domain before you can reserve it.

(Optional) You can also remove any out-of-compliance domains that you don't use.

## How the domain states relate to Webex for Government compliance

This isn't a real state, in Control Hub or elsewhere in Webex. It's a convenient term for third-party owned domains in which any members of the public may have email addresses. These domains include gmail.com, outlook.com, and aol.com.

You can't manage these domains in your organization.

If people with these email addresses belong to your organization, then the
                  organization is out of compliance.

This is the default state for a domain after you add it to your organization.

If they aren’t already in another organization, users with this domain can join
                  your organization.

There are no restrictions preventing users with this domain joining other organizations. If any commercial Webex organizations have users identified by this domain, then your organization is out of compliance.

This means Webex has confirmed your ownership of the domain.

This state doesn’t prevent users with this domain from being members of other
                  organizations.

If those users are in organizations outside of Webex for Government, then your organization is out of compliance. For example, they used that email address to join Webex for free.

You can pull these users into your organization.

This state is only available for domains in Webex for Government.

Your organization reserved the domain, but on behalf of all other Webex for Government organizations.

Any Webex for Government organization may contain users with email addresses in that domain.

Organizations outside of Webex for Government can’t add new users identified by email addresses from reserved domains.

Your organization could potentially be out of compliance, even after you reserve
                  a domain, if users with that domain existed outside of Webex for Government before you reserved it.

You can correct that issue to maintain future compliance.

This state is the most restrictive, and can complicate user management in Webex for Government.

Only the organization that owns this domain can add users whose email addresses
                  end in the domain.

You can't reserve a claimed domain, but you can release the claim and then
                  reserve it, if other Webex for Government organizations need to add such users.

## Actions required to change domain states

This table shows which actions to take to move domains into the preferred state for your
        organization's compliance.

| 1 | Sign in to https://admin-usgov.webex.com . |
|---|---|
| 2 | Under Management in the left-hand navigation pane, click Organization Settings . |
| 3 | Enter your domain name and click Add . |
| 4 | Click the ellipsis (…) beside your domain and choose Retrieve verification
            token . |
| 5 | Copy the verification token into your DNS TXT record. If your DNS host supports only one TXT record, add the token on a separate
            line. If your DNS host supports multiple records, add your token on a single line in its
            own TXT record. |
| 6 | Add the DNS TXT record to your DNS server. If another administrator configures your DNS server, send the DNS TXT record to your
          administrator to add to your DNS server. |
| 7 | Click Verify next to each added domain. |

| 1 | Sign in to https://admin-usgov.webex.com . |
|---|---|
| 2 | Under Management in the left-hand navigation pane, click Organization Settings . |
| 3 | In the Domains section, find the verified domain that you want to reserve. |
| 4 | Click the ellipsis (…), then select Reserve domain . If this domain includes users that exist in organizations that aren't in Webex for Government, Control Hub displays a message. |
| 5 | Read and acknowledge the message that reservation triggers removal of users with this domain from the commercial Webex organizations. By accepting, you're committing to change those email addresses in the other organizations, so that your users don't lose their (presumably non-sensitive) data. |
| 6 | Click Continue . |

| 1 | Sign in to https://admin-usgov.webex.com . |
|---|---|
| 2 | Under Management in the left-hand navigation pane, click Organization Settings . |
| 3 | Scroll to Domains and click the ellipsis (...) next to the
          domain that you want to claim, then select Claim verified
          domain . |
| 4 | Select Claim . After you claim a domain, Control Hub marks it with a green dot. |

| 1 | Sign in to https://admin-usgov.webex.com . |
|---|---|
| 2 | Under Management in the left-hand navigation pane, click Organization Settings . |
| 3 | In the Domains section, find the reserved domain that you want
          to release. |
| 4 | Click the ellipsis (...), then select Release reserved
          domain . If you can’t release the reserved domain, an error message appears. In that case, contact Cisco TAC, who can coordinate with other organizations who are using the domain. |
| 5 | Read the warning, then check the box to acknowledge that you understand and agree to proceed. |
| 6 | Click Continue . |

| 1 | Sign in to https://admin-usgov.webex.com . |
|---|---|
| 2 | Under Management in the left-hand navigation pane, click Organization Settings . |
| 3 | Scroll to Domains and click the ellipsis (…) beside the domain
          that you want to remove. |
| 4 | Click Remove domain , read the prompt, then click Remove . |

| 1 | Sign in to https://admin-usgov.webex.com . |
|---|---|
| 2 | Under Management in the left-hand navigation pane, click Organization Settings . |
| 3 | Check your status in the FedRAMP compliance section. If your organization is FedRAMP Compliant , there’s nothing
            to do. Continue with this task if your organization is Out of FedRAMP
              Compliance . |
| 4 | Click Check my compliance and wait for Control Hub to show you
          the report. The report shows the following compliance categories: You can create users from commercial domains in your organization. If you temporarily enable this state so you can convert users to your organization, keeping it on keeps you out of compliance. Lists email addresses that are shared in the commercial Webex environment. These email addresses end in domains that are public, aren't reserved in Webex for Government, or aren't claimed by your organization. Lists domains in your organization that are shared in the commercial Webex environment. These domains are either pending or verified in your organization. |
| 5 | Click Continue . Use the information from the report to understand what data you share with
          commercial Webex. (The other tasks in this section offer more detail). Complete the tasks
          that apply to your organization's situation and check your report again. |
| 6 | When the report shows green for all three categories, click Update FedRAMP
            status to declare that your organization doesn't share user emails and
          domains with commercial Webex. |

| 1 | Sign in to https://admin-usgov.webex.com . |
|---|---|
| 2 | Under Management in the left-hand navigation pane, click Organization Settings . |
| 3 | Find Sharing Email with Commercial Environment and turn it
          off. Users whose email addresses aren’t in reserved or claimed domains can’t join your organization. A full administrator or user administrator can only create users in your organization from a reserved or claimed domain. |

| 1 | Sign in to https://admin-usgov.webex.com . |
|---|---|
| 2 | Under Management in the left-hand navigation pane, click Organization Settings . |
| 3 | Find all users from the previous report whose email addresses contain your Webex for Government domains. If you don't manage the commercial organization where these users exist, contact Cisco
          TAC. |
| 4 | (Optional) As appropriate, choose what to do for each user: Source alternative addresses for the affected users if they are permitted to
            continue using that organization. Change those users' email addresses. Delete those users. |

| 1 | Sign in to https://admin-usgov.webex.com . |
|---|---|
| 2 | Under Management in the left-hand navigation pane, click Organization Settings . |
| 3 | Read each of your domains' status. Domains that are pending or verified can cause your organization to share information about their users with the commercial Webex environment. Users from those domains can sign up for a commercial licensed service. |
| 4 | For each pending domain, check you’ve met the requirements for verifying domain
          ownership. If the pending status persists, contact Cisco TAC. |
| 5 | For each verified domain, reserve or claim the verified domains. If you can't reserve or claim a verified domain, you or another entity might previously
            have verified or claimed that domain. The other entity needs to release and remove the domain before you can reserve it. |
| 6 | (Optional) You can also remove any out-of-compliance domains that you don't use. |

| State | Description |
|---|---|
| Public | This isn't a real state, in Control Hub or elsewhere in Webex. It's a convenient term for third-party owned domains in which any members of the public may have email addresses. These domains include gmail.com, outlook.com, and aol.com. You can't manage these domains in your organization. If people with these email addresses belong to your organization, then the
                  organization is out of compliance. |
| None | This is the default state for a domain after you add it to your organization. If they aren’t already in another organization, users with this domain can join
                  your organization. There are no restrictions preventing users with this domain joining other organizations. If any commercial Webex organizations have users identified by this domain, then your organization is out of compliance. |
| Pending | You have taken steps to verify this domain, and Webex is confirming your ownership. This is a temporary state before the domain becomes verified. |
| Verified | This means Webex has confirmed your ownership of the domain. This state doesn’t prevent users with this domain from being members of other
                  organizations. If those users are in organizations outside of Webex for Government, then your organization is out of compliance. For example, they used that email address to join Webex for free. You can pull these users into your organization. |
| Reserved | This state is only available for domains in Webex for Government. Your organization reserved the domain, but on behalf of all other Webex for Government organizations. Any Webex for Government organization may contain users with email addresses in that domain. Organizations outside of Webex for Government can’t add new users identified by email addresses from reserved domains. Your organization could potentially be out of compliance, even after you reserve
                  a domain, if users with that domain existed outside of Webex for Government before you reserved it. You can correct that issue to maintain future compliance. |
| Claimed | This state is the most restrictive, and can complicate user management in Webex for Government. Only the organization that owns this domain can add users whose email addresses
                  end in the domain. You can't reserve a claimed domain, but you can release the claim and then
                  reserve it, if other Webex for Government organizations need to add such users. |

| Begin state | Action | End state | Possible errors |
|---|---|---|---|
| Public | Not applicable | Public | You can't add this domain |
| Not in your organization | Add | None | Domain is claimed |
| None | Verify | Pending, then Verified | — |
| Verified | Claim | Claimed |  |
| Verified | Reserve | Reserved | Domain is claimed |
| Reserved | Claim | Claimed | — |
| Reserved | Release | Verified | Option unavailable because other organizations share the reserved
                domain |
| Claimed | Release | Verified | — |
| Verified or None | Remove | Not in your organization | — |