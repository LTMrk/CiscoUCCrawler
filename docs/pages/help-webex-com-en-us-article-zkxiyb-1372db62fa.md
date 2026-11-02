---
doc_id: help-webex-com-en-us-article-zkxiyb-1372db62fa
source_url: https://help.webex.com/en-us/article/zkxiyb
retrieved_at: 2026-11-02T13:11:16.675102+00:00
---

## Verify the network setup

When deploying a new IP telephony system, system administrators and network administrators must complete several initial configuration tasks to prepare the network for IP telephony service. For information and a checklist for setting up and configuring a Cisco IP telephony network, see the documentation for your particular Cisco Unified Communications Manager (Unified CM) release.

For the phone to operate successfully as an endpoint in your network, your network
        must meet specific requirements. One requirement is the appropriate bandwidth. The phones
        require more bandwidth than the recommended 32 kbps when they register to Cisco Unified
        Communications Manager (Unified CM). Consider this higher bandwidth requirement when you
        configure your QoS bandwidth. For more information, refer to Cisco Collaboration Solutions Design
          Guidance .

The phone displays the date and time from Cisco Unified CM. The time displayed on the phone can differ from the Cisco Unified CM time by up to 10 seconds.

Configure a VoIP Network to meet the following requirements:

VoIP is configured on your routers and gateways.

Cisco Unified CM is installed in your network and is configured to handle call processing.

Set up the network to support one of the following:

DHCP support

DNS support

Manual assignment of IP address, gateway, and subnet mask

When there are multiple calling systems deployed in your network, it's recommended to use separate VLAN and DHCP options for each calling system. If you use both cloud-based and on-premise calling systems in the same subnet, cloud-based calling will take priority.

## OOB onboarding flowchart

The following Out-Of-Box (OOB) flowchart shows the process for phone onboarding.

OOB: Phone is just taken out of the phone box and turned on for its initial onboarding to
        the target call control system.

Click the chart to view it in full size.

Near Field Communication (NFC) is only available on Cisco Desk Phone 9841, 9851, 9861, and 9871.

### Provisioning with DHCP options

The phone can automatically locate its configuration server through DHCP options. During a
        resync, the phone queries the following DHCP options:

- IPv4: 66, 160, 159, 150

- IPv6: 17, 160, 159

Based on the DHCP response, the phone behaves as follows:

If a valid file is found, the phone will register in MPP mode using that file.

If the DHCP option does not specify a file name, the phone tries the following default
            paths in sequence:

- /$PSN.xml

- /Cisco/$PN/$MA.cfg

where

- $PSN = Phone Serial Number

- $PN = Phone Product Name

- $MA = Phone MAC Address

If DHCP responds but no valid file is available, the phone will attempt CDA

If DHCP query times out (no server response), the phone will proceed to query DHCP
            150/66 for the default provisioning file to register with CUCM.

## Activation code onboarding for on-premises phones

You can use Activation Code Onboarding to quickly set up new phones without autoregistration. With this approach, you control the phone onboarding process using one of the following:

Cisco Unified Communications Bulk Administration Tool (BAT)

Cisco Unified Communications Manager Administration interface

Administrative XML Web Service (AXL)

Enable this feature from the Device Information section of the Phone Configuration page. Select Require Activation Code for Onboarding if you want this feature to apply to a single on-premises phone.

Users must enter an activation code before their phones can register. Activation Code Onboarding can be applied to individual phones, a group of phones, or across an entire network.

This is an easy way for users to onboard their phones because they only enter a 16-digit activation code.  We recommend that you use a secure method to give users this information. But if a user is assigned to a phone, then this information is available on the Self Care Portal. The audit log records when a user accesses the code from the portal.

Activation codes can only be used once, and they expire after 1 week by default. If a code expires, you’ll have to provide the user with a new one.

You’ll find this approach an easy way to keep your network secure because a phone can’t
        register until the Manufacturing Installed Certificate (MIC) and activation code are
        verified. This method is also a convenient way to bulk onboard phones because it doesn't use
        the Tool for Autoregistered Phone Support (TAPS) or autoregistration. The rate of onboarding
        is one phone per second or about 3600 phones per hour. You can add phones with the Cisco Unified Communications Manager Administration, with Administrative XML Web Service (AXL), or with BAT.

Existing phones reset after they are configured for Activation Code Onboarding. They don't register until the activation code is entered and the phone MIC is verified. Inform current users that you’re moving towards Activation Code Onboarding before you implement it.

For more information, see Device Onboarding with Activation Codes Task Flow in
              On-Premise Mode in System Configuration Guide for Cisco Unified
            Communications Manager, Release 15 and SUs

## Activation code onboarding and Mobile and Remote Access (MRA)

You can use Activation Code Onboarding with Mobile and Remote Access (MRA) when deploying your phones for remote users. This feature is a secure way to deploy off-premises phones when autoregistration isn’t required. But you can configure a phone for autoregistration when on-premises, and activation codes when off-premises. This feature is similar to Activation Code Onboarding for on-premises phones, but it makes activation code available for off-premises phones also.

Activation Code Onboarding for MRA requires Cisco Unified Communications Manager 12.5(1)SU1 or later, and Cisco Expressway X12.5 or later. Smart Licensing should be enabled also.

You can enable this feature from the Cisco Unified Communications Manager Administration, but note the following:

Enable this feature from the Device Information section of the Phone Configuration page.

Select Require Activation Code for Onboarding if you want this feature to apply just to a single on-premises phone.

Select Allow Activation Code via MRA and Require Activation Code for Onboarding if you want to use Activation Onboarding for a single off-premises phone. If the phone is on-premises, it changes to MRA mode and uses the Expressway. If the phone can’t reach the Expressway, it doesn’t register until it’s off premises.

For more information, see the following documents:

System Configuration Guide for Cisco Unified Communications Manager, Release 15
                and SUs

Mobile and Remote Access Through Cisco Expressway for Cisco Expressway X12.5 or later

## Domain onboarding and Mobile and Remote Access (MRA)

You can use the service domain onboarding with Mobile and Remote Access (MRA) when deploying your phones for remote users. This feature is a secure way to deploy off-premises phones when autoregistration and activation code onboarding aren't required. When users choose and enter a valid service domain, they will be prompted to enter their user credentials for the MRA authentication.

Domain onboarding for MRA requires Cisco Unified Communications Manager 12.5(1)SU1 or later, and Cisco Expressway X12.5 or later.

You can enable this feature from the Cisco Unified Communications Manager Administration, but note the following:

- Configure the MRA service domain from Advanced Features > Mobile and Remote Access Service Domain .

- Select a service domain from the drop-down list Activation Code MRA Service Domain on the phone device page ( Device > Phone ).

- Create end users and associate the phone with the end users.

- Assign the end users to the access control group "Standard CCM End Users".

- Enable User Credentials Persistent for Express Sign in if you want to make it easier for the users to log in. When enabled, the login credentials are saved on the phone after the first-time sign-in.

For more information, see the following documents:

- System Configuration Guide for Cisco Unified
            Communications Manager, Release 15 and SUs

- Mobile and Remote Access Through Cisco Expressway for Cisco Expressway X12.5 or later

## Enable autoregistration for phones

Before you install your phone, you must choose a method for adding phones to the Cisco Unified Communications Manager (Unified CM) database.

By enabling autoregistration before you install the phones, you can:

Add phones without first gathering MAC addresses from the phones.

Automatically add a phone to the Cisco Unified CM database when you physically connect the phone to your IP telephony network. During
            autoregistration, Cisco Unified CM assigns the next available sequential directory number to the phone.

Quickly enter phones into the Cisco Unified CM database and modify the settings, such as the directory numbers, from Cisco Unified CM.

Move the autoregistered phones to new locations and assign them to different device
            pools without affecting their directory numbers.

### Enable autoregistration on Cisco Unified CM

For the information about how to enable and configure autoregistration, see Enable
            Autoregistration in System Configuration Guide for Cisco Unified
            Communications Manager , Release 15 and SUs .

### Configure TAPS autoregistration on Cisco Unified CM

You can also add phones with autoregistration and the Tool for AutoRegistered Phones Support (TAPS). TAPS works with the Bulk Administration Tool (BAT) to update a batch of phones that were already added to the Cisco Unified Communications Manager database with dummy MAC addresses. Use TAPS to update MAC addresses and to download predefined configurations for phones.

We recommend that you use autoregistration and TAPS to add fewer than 100 phones to your network. To add more than 100 phones to your network, use the Bulk Administration Tool (BAT).

For the information about how to configure TAPS autoregistration, see Configure
            TAPS Autoregistration in Bulk Administration Guide for Cisco Unified
            Communications Manager , Release 15 and SUs .

| 1 | Configure a VoIP Network to meet the following requirements: VoIP is configured on your routers and gateways. Cisco Unified CM is installed in your network and is configured to handle call processing. |
|---|---|
| 2 | Set up the network to support one of the following: DHCP support DNS support Manual assignment of IP address, gateway, and subnet mask When there are multiple calling systems deployed in your network, it's recommended to use separate VLAN and DHCP options for each calling system. If you use both cloud-based and on-premise calling systems in the same subnet, cloud-based calling will take priority. |

## Figuras

![PhoneOS Devices Onboarding Flowchart](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/487001-488000/487668.png)