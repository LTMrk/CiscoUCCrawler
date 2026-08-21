---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be6000-installationguide-12-5-cucm-b-installation-guide-m5-14-cucm-m-ci-316936c2d6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE6000/InstallationGuide/12_5/cucm_b_installation-guide-m5-14/cucm_m_cisco-smart-licensing-for-cucm.html
retrieved_at: 2026-08-21T22:54:53.670889+00:00
---

Installation Guide for Cisco Business Edition 6000H/M (M5), Release 12.5(CSR 12.7)

# Installation Guide for Cisco Business Edition 6000H/M (M5), Release 12.5(CSR 12.7)

Updated: February 19, 2021

Chapter: Cisco Smart Licensing for CUCM 12.5  BE6000-specific Licenses

## Chapter: Cisco Smart Licensing for CUCM 12.5  BE6000-specific Licenses

- Cisco Smart Licensing for CUCM 12.5  BE6000-specific Licenses

- Cisco Smart Licensing for Unified Communications Manager 12.5 BE6000-specific Licenses

# Cisco Smart Licensing for CUCM 12.5  BE6000-specific Licenses

## Cisco Smart Licensing for Unified Communications Manager 12.5 BE6000-specific Licenses

For a general overview of Cisco Smart Licensing, and how it is used with Unified Communications Manager 12.0 and higher, see
                              the Cisco Smart Software Licensing with Cisco Unified Communications Manager Solution Overview.

The instructions in this appendix only apply if you have purchased BE6000-specific UCL and UWL 12.5 starter packs and add
                              on user licenses. These licenses are described in the Business Edition 6000 Ordering Guide available to partners and Cisco employees.

If you are using a different license offer  (such as non-BE6000-specific UCL, UWL, Enterprise Agreement, or Collaboration
                                    Flex Plan), stop now and see the Cisco Smart Software Licensing with Cisco Unified Communications Manager Solution Overview for instructions.

Smart Licensing for BE6000-specific licenses are only available for Collaboration System Release from 12.5 and above.

Unified Communications Manager 12.5 in BE6000-specific licensing requires use of Cisco Smart Licensing, and for the UCM 12.5
                                    Publisher to have 'BE6000 mode' enabled using the CLI.

Remember that Unified Communications Manager 11.5 in BE6000-specific licensing continues to require the use of Cisco Product
                                    Authorization Keys (PAKs) and Cisco Prime License Manager, not Cisco Smart Licensing.

You must create a Cisco Smart Account (this can be done prior to installation). You must deposit the newly purchased BE6000
                                    12.5 licenses in this account. Installed base customers must migrate licenses to 12.5 and deposit in this account.

Obtain your BE6000-specific 12.5 licenses. These instructions assume that you have already completed the required purchase/fulfillment
                                    processes. Partners and Cisco employees may consult the Business Edition 6000 12.5 Ordering Guide.

Provision your Smart Account / Virtual Account in Cisco Smart Software Manager; ensure that your BE6000-specific licenses
                                    are assigned to your Smart Account / Virtual Account.

For more information, see the Cisco Smart Software Licensing with Cisco Unified Communications Manager Solution Overview .

Ensure that your BE6000-specific licenses for starter packs and add-on users are properly assigned to your Smart Account /
                                    Virtual Account.

See the following screenshot of Cisco Smart Software Manager showing a Smart Account/Virtual Account that has BE6000 12.5
                                    specific and starter pack licenses assigned to it:

Obtain a Registration Token for Unified Communications Manager 12.5 from Cisco Smart Software Manager.

For more information, see the Cisco Smart Software Licensing with Cisco Unified Communications Manager Solution Overview.

See the following screenshot of where the Registration Token is copied or downloaded from (you need this in step 6):

Install Unified Communications Manager 12.5 (or version-upgrade Unified Communications Manager from an older release to 12.5).

When Unified Communications Manager in BE6000 is initially installed as 12.5, or version-upgraded from an older release to
                                    12.5, Unified Communications Manager 12.5 immediately enters the following modes:

Registration Status 'Unregistered'.

License Authorization Status 'Evaluation Mode'. Unified Communications Manager 12.5 remains in 'Evaluation Mode' for either
                                          90 days, or until it is registered with Cisco Smart Software Manager (whichever comes first).

Licensing Mode 'Enterprise'.

The following is a screenshot of what the initial mode settings look like immediately after you install of Unified Communications
                                    Manager 12.5 and configured devices in it:

If 'Evaluation Mode' ends after 90 days without registration, then Unified Communications Manager 12.5 enters 'Enforced Mode',
                                    and administrative changes are disabled.

After registration, Unified Communications Manager 12.5 periodically syncs with Cisco Smart Software Manager (CSSM) to verify
                                    authorization status of Unified Communications Manager 12.5 and validates the customer’s registered licenses with locally
                                    consumed or used licenses for this Unified Communications Manager 12.5 cluster. If CSSM reports 'Authorization Expired' or
                                    insufficient quantity of registered licenses vs. consumed/used licenses then Unified Communications Manager 12.5 enters 'Out
                                    of Compliance' status. You have an overage period of 90 days to bring licensing back into compliance, at the end of which
                                    Unified Communications Manager 12.5 enters 'Enforced Mode', and administrative changes are disabled.

For more information, see the Cisco Smart Software Licensing with Cisco Unified Communications Manager Solution Overview.

Set the Unified Communications Manager 12.5 cluster to 'BE6000 mode' and specify which BE6000 starter pack you want to use.

On the Unified Communications Manager 12.5 Publisher node, run the platform CLI command utils BE6000Mode enable and specify which BE6000 starter pack license you use for your install of or version-upgrade to 12.5.

BE6000 UCL Starter Bundle (for UCL Enhanced + voicemail)

BE6000 UWL Starter Bundle (for UWL Standard)

NONE

The following is a screenshot of the command line to use:

As an example, see the following screenshot about what Unified Communications Manager 12.5 displays immediately after being
                                    placed into 'BE6000 mode' with 'BE6000 UCL starter bundle' (shows consuming or using one unit that has not yet been requested
                                    from registered licenses in Cisco Smart Software Manager):

Register the BE6000 Unified Communications Manager 12.5 with Cisco Smart Software Manager, using the Registration Token.

For more information, see Cisco Smart Software Licensing with Cisco Unified Communications Manager Solution Overview.

Enter the Registration Token obtained in Step 3 on the Unified Communications Manager 12.5 Publisher.

The Unified Communications Manager 12.5 Publisher then attempts to request and consume or use a single BE6000 Starter Bundle
                                    from your registered license inventory on Cisco Smart Software Manager. The starter bundle feature-level requested is the
                                    one you specified at the time of running the platform command line interface utils BE6000Mode enable . A Unified Communications Manager 12.5 cluster with its Publisher in 'BE6000 mode' may only request and consume or use a
                                    single BE6000 starter pack license. The cluster may request and consume or use any number of BE6000-specific or non-BE6000-specific
                                    addon user licenses, subject to capacity limits of BE6000 solutions.

As an example, for a successfully registered and authorized Unified Communications Manager 12.5 in 'BE6000 mode' using a BE6000
                                    UCL starter pack, see the following screenshots of what you would see on the Unified Communications Manager 12.5 Publisher
                                    and on Cisco Smart Software Manager (showing consuming or using one unit that is authorized and registered):

Unified Communications Manager:

Cisco Smart Software Manager:

### Starter Bundle License Consumption

The following is a screenshot of what the initial mode settings look like immediately once you install Unified Communications
                              Manager, after customer configuring the devices in 12.5:

When the user runs utils BE6000Mode enable and select BE6000 UCL Starter Bundle

The following image shows the change in the License consumption for the above selection:

When the user runs utils BE6000Mode enable and select BE6000 UWL Starter Bundle

The following image shows the change in the License consumption for the above selection:

When the user runs utils BE6000Mode enable and select None

The following image shows the change in the License consumption for the above selection:

### Addon User License Consumption

In BE6000 mode, Unified Communications Manager 12.5 consumes BE6000 Starter Bundle addons along with Enterprise addons.