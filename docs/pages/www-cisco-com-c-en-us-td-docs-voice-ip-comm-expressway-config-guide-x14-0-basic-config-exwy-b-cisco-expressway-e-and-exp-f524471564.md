---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-basic-config-exwy-b-cisco-expressway-e-and-exp-f524471564
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0/basic_config/exwy_b_cisco-expressway-e-and-expressway-c-basic-configuration-deployment-guide-x14-0/exwy_m_run-the-service-setup-wizard.html
retrieved_at: 2026-08-16T15:27:32.555806+00:00
---

Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

# Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide (X14.0)

Updated: April 14, 2021

Chapter: Run the Service Setup Wizard

## Chapter: Run the Service Setup Wizard

# Run the Service Setup Wizard

## Overview

The Service Setup Wizard makes it easier to configure the Expressway system for its chosen purpose in your environment. It
                           also simplifies the user interface. The wizard starts when you first launch the web user interface. In the wizard, you select
                           the system series (Expressway series or VCS series) and system type ( Cisco Expressway-C or Cisco Expressway-E). Based on the series and type, you select the services. And if you use PAK-based licensing, you also apply
                           the relevant option keys for your licenses.

You can also use the wizard to review and edit the Expressway basic network settings (typically already configured during
                           initial installation). When you restart, the user interface is tailored to match your service selections and you only see
                           menus and pages for the services you chose. Examples of services include:

Cisco Webex Hybrid Services (renamed from Cisco Spark Hybrid Services)

Mobile and Remote Access including Meeting Server Web Proxy

Jabber Guest Services

Microsoft gateway service - this service is only for when you want this system to adapt between Microsoft SIP and standards-based
                                 SIP variants. If a different system (such as Cisco Meeting Server) is doing that adaptation in your deployment, you don't
                                 need this service.

Registrar

Collaboration Meeting Rooms (CMR) Cloud

Business to business calls

### Services That Can Be Hosted Together

Some services are incompatible and cannot be selected together. The following table provides a matrix of compatible services.
                              The matrix specifies which services you can use together on the same system or cluster.

Cisco Webex Hybrid Services (Connectors)

Mobile and Remote Access

Jabber Guest Services

Microsoft Gateway Service

Registrar

CMR Cloud

Business to Business calling (includes Hybrid Call Service)

Cisco Webex Hybrid Services (Connectors)

Y

N

N

N

N

Y

Y

Mobile and Remote Access and/or (from X8.9) Meeting Server Web Proxy

N

Y

N

N

Y

Y

Y

Jabber Guest Services

N

N

Y

N

Y

Y

Y

Microsoft gateway service

N

N

N

Y

N

N

N

Registrar

N

Y

Y

N

Y

Y

Y

CMR Cloud

Y

Y

Y

N

Y

Y

Y

Business to Business calling

(includes Hybrid Call Service)

Y

Y

Y

N

Y

Y

Y

Key to Table

Y: Yes, these services can be hosted on the same system or cluster

N: No, these services may not be hosted on the same system or cluster

Rules

Hybrid Services connectors may co-reside with the Cisco Expressway-C of a traversal pair used for Call Service, subject to user number limitations.

* If your Hybrid Call Service (or B2B) traversal pair is also used for MRA, then the Hybrid Services connectors must be on
                                    a separate Expressway-C. This is because we do not support the connectors being hosted on the Expressway-C that is used for
                                    MRA.

Microsoft gateway service requires a dedicated VCS Control or Expressway-C (called "Gateway VCS" or "Gateway Expressway" in the help and documentation).

Jabber Guest cannot work with MRA (technical limitation).

MRA is currently not supported in IPv6 only mode. If you want IPv6 B2B calling to co-reside with IPv4 MRA on the same Expressway
                                    traversal pair, the  Expressway-E and  Expressway-C must both be in dual stack mode.

### CE1200 Physical Appliances

The following points apply if you are deploying a Cisco Expressway CE1200:

The Series option is not relevant. This appliance does not support the Cisco VCS, and is always a Cisco Expressway system.

The CE1200 can operate as a Cisco Expressway-C or a Cisco Expressway-E.

By default it always ships with Expressway-C. If you want to deploy the server as an Expressway-E, you need to specify the
                                    system Type as Expressway-E. You must restart Expressway for the changes to take effect.

### What If I Don't Want to Use the Wizard?

A skip option exists if you don't want to use the wizard. If you change your mind later, you can go back and run it at any
                              time ( Status > Overview page; click Run service setup ).

If you opt to skip the wizard, you need to deal with the Expressway licensing setup requirements manually before you start
                              the configuration tasks in this guide. Also, the user interface isn't customized to reflect your specific service selections.

## Task 1: Accessing and Navigating Service Setup Wizard

The first time you log in to the Expressway web user interface you'll automatically see the Service Setup Wizard. (For subsequent
                           log ins you'll see the Status > Overview page, and from that page you can click Run service setup at anytime.)

To navigate the wizard:

Click Continue to save and move to the next wizard page.

Click Back to return to the previous wizard page.

Click Skip Service Setup Wizard if you want to back out of the wizard completely.

If you use appliance-based Expressways, when you click Continue , the settings configured on the page are not saved on the appliance . The settings are saved only after you click Finish on the Confirm core configuration page.

If you use Smart Licensing, you cannot change the Series setting from the Service Selection page/wizard (to convert an Expressway to a VCS product). Instead this process must start with a factory reset (to disable Smart Licensing
                                       because it's not supported on VCS). Some of the other settings shown in this example are unnecessary with Smart Licensing
                                       and do not appear in the wizard on Expressways that use Smart Licensing.

## Task 2: Running the Service Setup Wizard and Applying Licenses

The instructions described here differ depending on whether the system uses classic (PAK-based) licensing or Smart Licensing.
                           Use the appropriate process for your deployment's licensing method.

65 option key limit

If you try to add more than 65 option keys (licenses), they appear as normal on the Option keys page. However, only the first 65 keys take effect. Additional keys from 66 onwards appear to be added, but actually the Expressway
                           does not process them. CDETS CSCvf78728 refers.

### Process With Classic (PAK-based) Licensing

Choose Expressway series in Select Series .

Choose Expressway-C or Expressway-E in Select Type . We recommend that you select Expressway-C first and run the wizard for it. Then run the wizard on the Expressway-E.

The list of services changes to match what's available on your chosen Series and Type.

Select Services. Check the boxes next to the services you want to use on this system. For the compatible services that you
                                          can use together on the same system or cluster, see Services That Can Be Hosted Together .

If you want to keep all the menu options, or if you want to use the wizard for applying licenses but don't want to choose
                                             services yet, check Proceed without selecting services .

Click Continue to move to the Option keys page of the wizard. This page helps you to identify and acquire the appropriate licenses for your chosen selections. Worked
                                          examples are provided in Examples for Running the Service Setup Wizard .

The Licensing help section at the top of the page explains how to use the Product Authorization Key (PAK) in the Cisco Product License Registration
                                             Portal. The License status section at the bottom of the page lists the actual licenses that you need and their status (loaded / not loaded). The exact
                                             entries vary by deployment - this example is for the Cisco Expressway-C Registrar service:

On the Option keys page:

Copy the serial number, which you need for the next step.

Click the Product License Registration Portal link to go to the licensing portal. ( For this step you need to work away from the wizard to obtain the necessary licenses .) In the licensing portal, enter the necessary details for the required licenses. For example, if you want to register desktop
                                                systems like the EX90, you’ll need to add Desktop System registration licenses.

Detailed information about using the licensing portal is in the online help or the Expressway Administrator Guide . An ordering guide for Cisco products is available on the Cisco Collaboration Ordering Guides page.

Paste the text from the option keys email into the text area. The system reads the option keys out of the pasted text and
                                          displays them next to the text area.

Add new text areas if you have more email text to paste in, such as your room or desktop system registration license keys.

Click Add Keys .

The License status table groups the keys that are possible on this system, and indicates whether they are loaded or not loaded. The keys are
                                             grouped as follows:

Required : If any keys in this section are not yet loaded, you see status Required and will not be able to continue through the wizard.

Optional : Shows keys that may or may not be useful, but are not strictly required for the services you chose.

Unrelated : These keys won't harm the system if they are loaded, but will not provide any benefit for the services you chose.

Incompatible : These keys cannot work with the selected services. You must remove them or choose different services before you can continue.

Click Continue .

Review the network configuration and modify the settings if necessary. Save any changes before you continue the wizard.

Click Finish .

Restart the system when prompted.

### Process With Smart Licensing

Choose Expressway series in Select Series .

Choose Expressway-C or Expressway-E in Select Type . We recommend that you select Expressway-C first and run the wizard for it. Then run the wizard on the Expressway-E.

The list of services changes to match what's available on your chosen Series and Type.

Select Services. Check the boxes next to the services you want to use on this system. For the compatible services that you
                                          can use together on the same system or cluster, see Services That Can Be Hosted Together .

If you want to keep all the menu options, or if you want to use the wizard for applying licenses but don't want to choose
                                             services yet, check Proceed without selecting services .

You now need to configure Smart Licensing for the Expressway. To do this please follow the instructions in the Expressway Administrator Guide section "Configure Smart Licensing".

Click Continue .

Review the network configuration and modify the settings if necessary. Save any changes before you continue the wizard.

Click Finish .

Restart the system when prompted.

#### What to do next

The wizard is complete for the Expressway-C element. Now you need to run it on the Expressway-E. For typical deployments with
                                 the Expressway-E the services you are most likely to select with the wizard include Mobile and remote access and Business to business calls . When the Expressway-E is done, go to the next section in this guide, " Expressway System Configuration" .

### If the Application Menu is Missing from the Web User Interface

In some cases, depending on the combination of services selected, the Applications menu may be missing from the web interface. If this happens and you want to restore the menu, do the following:

Go to Status > Overview and click Run service setup , to go back to the service setup options.

Check the option Proceed without selecting services and click Continue .

### Examples for Running the Service Setup Wizard

#### Example for Expressway Registrar With Classic, PAK Licenisng

Click Expressway Series .

Click Expressway-C .

Check Registrar .

Check any other compatible services that you have bought for this system. For this example, let's assume Business to business calls . (The matrix of compatible services is in the online help and the Expressway Administrator Guide .)

Click Continue . The wizard takes you to the licensing and options page.

Create a new paste area and paste in your room or desktop system registration license keys (and any option keys you have for
                                             this system).

Click Add Keys .

Click Continue .

Review the networking configuration and click Finish .

Restart the system when prompted.

This completes the service setup and licensing for the Expressway-C part of your desired outcome. However, since we chose Business to business calls , we would have to use the Service Selection page again to set up and license an Expressway-E, because the business to business
                                                calling deployment requires firewall traversal.

#### Example for Hybrid Services

Click Expressway Series .

Click Expressway-C .

Check Cisco Webex Hybrid Services .

Click Continue .

The wizard asks you to review your network configuration. It skipped the licensing page because you don't need licenses or
                                                option keys to register for Hybrid Services.

Review the network configuration and modify the settings if necessary. Save any changes before you continue the wizard.

Click Finish .

The wizard opens the Connector Management page where you can register the Expressway for Hybrid Services.

|  | Cisco Webex Hybrid Services (Connectors) | Mobile and Remote Access | Jabber Guest Services | Microsoft Gateway Service | Registrar | CMR Cloud | Business to Business calling (includes Hybrid Call Service) |
|---|---|---|---|---|---|---|---|
| Cisco Webex Hybrid Services (Connectors) | Y | N | N | N | N | Y | Y |
| Mobile and Remote Access and/or (from X8.9) Meeting Server Web Proxy | N | Y | N | N | Y | Y | Y * |
| Jabber Guest Services | N | N | Y | N | Y | Y | Y |
| Microsoft gateway service | N | N | N | Y | N | N | N |
| Registrar | N | Y | Y | N | Y | Y | Y |
| CMR Cloud | Y | Y | Y | N | Y | Y | Y |
| Business to Business calling (includes Hybrid Call Service) | Y | Y * | Y | N | Y | Y | Y |

| Note | If you use Smart Licensing, you cannot change the Series setting from the Service Selection page/wizard (to convert an Expressway to a VCS product). Instead this process must start with a factory reset (to disable Smart Licensing
                                       because it's not supported on VCS). Some of the other settings shown in this example are unnecessary with Smart Licensing
                                       and do not appear in the wizard on Expressways that use Smart Licensing. |
|---|---|

| Step 1 | Choose Expressway series in Select Series . |
|---|---|
| Step 2 | Choose Expressway-C or Expressway-E in Select Type . We recommend that you select Expressway-C first and run the wizard for it. Then run the wizard on the Expressway-E. The list of services changes to match what's available on your chosen Series and Type. |
| Step 3 | Select Services. Check the boxes next to the services you want to use on this system. For the compatible services that you
                                          can use together on the same system or cluster, see Services That Can Be Hosted Together . If you want to keep all the menu options, or if you want to use the wizard for applying licenses but don't want to choose
                                             services yet, check Proceed without selecting services . |
| Step 4 | Click Continue to move to the Option keys page of the wizard. This page helps you to identify and acquire the appropriate licenses for your chosen selections. Worked
                                          examples are provided in Examples for Running the Service Setup Wizard . The Licensing help section at the top of the page explains how to use the Product Authorization Key (PAK) in the Cisco Product License Registration
                                             Portal. The License status section at the bottom of the page lists the actual licenses that you need and their status (loaded / not loaded). The exact
                                             entries vary by deployment - this example is for the Cisco Expressway-C Registrar service: Figure 2. Service Setup Wizard Example - Option Keys Page |
| Step 5 | On the Option keys page: Copy the serial number, which you need for the next step. Click the Product License Registration Portal link to go to the licensing portal. ( For this step you need to work away from the wizard to obtain the necessary licenses .) In the licensing portal, enter the necessary details for the required licenses. For example, if you want to register desktop
                                                systems like the EX90, you’ll need to add Desktop System registration licenses. Detailed information about using the licensing portal is in the online help or the Expressway Administrator Guide . An ordering guide for Cisco products is available on the Cisco Collaboration Ordering Guides page. |
| Step 6 | Paste the text from the option keys email into the text area. The system reads the option keys out of the pasted text and
                                          displays them next to the text area. |
| Step 7 | Add new text areas if you have more email text to paste in, such as your room or desktop system registration license keys. |
| Step 8 | Click Add Keys . The License status table groups the keys that are possible on this system, and indicates whether they are loaded or not loaded. The keys are
                                             grouped as follows: Required : If any keys in this section are not yet loaded, you see status Required and will not be able to continue through the wizard. Optional : Shows keys that may or may not be useful, but are not strictly required for the services you chose. Unrelated : These keys won't harm the system if they are loaded, but will not provide any benefit for the services you chose. Incompatible : These keys cannot work with the selected services. You must remove them or choose different services before you can continue. |
| Step 9 | Click Continue . |
| Step 10 | Review the network configuration and modify the settings if necessary. Save any changes before you continue the wizard. |
| Step 11 | Click Finish . |
| Step 12 | Restart the system when prompted. Result: When you log in, the user interface is tailored to match your service selections. You only see menus and pages for the services
                                          you chose. |

| Step 1 | Choose Expressway series in Select Series . |
|---|---|
| Step 2 | Choose Expressway-C or Expressway-E in Select Type . We recommend that you select Expressway-C first and run the wizard for it. Then run the wizard on the Expressway-E. The list of services changes to match what's available on your chosen Series and Type. |
| Step 3 | Select Services. Check the boxes next to the services you want to use on this system. For the compatible services that you
                                          can use together on the same system or cluster, see Services That Can Be Hosted Together . If you want to keep all the menu options, or if you want to use the wizard for applying licenses but don't want to choose
                                             services yet, check Proceed without selecting services . |
| Step 4 | You now need to configure Smart Licensing for the Expressway. To do this please follow the instructions in the Expressway Administrator Guide section "Configure Smart Licensing". |
| Step 5 | Click Continue . |
| Step 6 | Review the network configuration and modify the settings if necessary. Save any changes before you continue the wizard. |
| Step 7 | Click Finish . |
| Step 8 | Restart the system when prompted. Result: When you log in, the user interface is tailored to match your service selections. You only see menus and pages for the services
                                          you chose. |

| Step 1 | Click Expressway Series . |
|---|---|
| Step 2 | Click Expressway-C . |
| Step 3 | Check Registrar . |
| Step 4 | Check any other compatible services that you have bought for this system. For this example, let's assume Business to business calls . (The matrix of compatible services is in the online help and the Expressway Administrator Guide .) |
| Step 5 | Click Continue . The wizard takes you to the licensing and options page. |
| Step 6 | Create a new paste area and paste in your room or desktop system registration license keys (and any option keys you have for
                                             this system). |
| Step 7 | Click Add Keys . |
| Step 8 | Click Continue . |
| Step 9 | Review the networking configuration and click Finish . |
| Step 10 | Restart the system when prompted. This completes the service setup and licensing for the Expressway-C part of your desired outcome. However, since we chose Business to business calls , we would have to use the Service Selection page again to set up and license an Expressway-E, because the business to business
                                                calling deployment requires firewall traversal. |

| Step 1 | Click Expressway Series . |
|---|---|
| Step 2 | Click Expressway-C . |
| Step 3 | Check Cisco Webex Hybrid Services . |
| Step 4 | Click Continue . The wizard asks you to review your network configuration. It skipped the licensing page because you don't need licenses or
                                                option keys to register for Hybrid Services. |
| Step 5 | Review the network configuration and modify the settings if necessary. Save any changes before you continue the wizard. |
| Step 6 | Click Finish . The wizard opens the Connector Management page where you can register the Expressway for Hybrid Services. |