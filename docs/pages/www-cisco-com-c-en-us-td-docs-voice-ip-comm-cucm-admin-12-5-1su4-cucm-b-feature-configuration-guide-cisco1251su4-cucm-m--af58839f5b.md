---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-cucm-b-feature-configuration-guide-cisco1251su4-cucm-m--af58839f5b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/cucm_b_feature-configuration-guide-cisco1251su4/cucm_m_federal-communications-commission-fcc-emergency.html
retrieved_at: 2026-08-16T17:04:21.835258+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4

Updated: July 31, 2025

Chapter: The US Federal Communications Commission (FCC) Emergency Call Routing Regulations

## Chapter: The US Federal Communications Commission (FCC) Emergency Call Routing Regulations

- The US Federal Communications Commission (FCC) Emergency Call Routing Regulations

- Emergency Call Routing Regulations Overview

- Configure Emergency Call Routing Regulations

# The US Federal Communications Commission (FCC) Emergency Call Routing Regulations

## Emergency Call Routing Regulations Overview

Emergency Call Routing Regulation provides us with information in compliance with the US FCC laws on how the Emergency Calls
                              (911) are configured and routed in the US and non-US time zones.

The US FCC signed the following laws to ease public safety by encouraging and enabling the prompt deployment of a nationwide,
                              seamless communications infrastructure for emergency services.

The US FCC signed the following laws on Emergency Call (911) routing:

Kari's Law—This law applies to Multi-Line Telephone Systems (MLTS) that serve users in settings such as office buildings,
                                    campuses, and hotels. The FCC requires MLTS to enable users to dial 911 directly, without dialing a prefix reach an outside
                                    line and notifies the front desk or security office when emergency calls are made.

Ray Baum's Act—Under section 506 of Ray Baum’s act, dispatch the location details  (a street address, building number, floor
                                    number, room number) with emergency calls regardless of the technological platform used so that the 911 call centers receive
                                    the caller's location automatically and can dispatch responders more quickly.

For more information on FCC laws, see https://www.fcc.gov/mlts-911-requirements

An Emergency Responder effectively manages calls in the telephony network to respond and handle all emergency calls in compliance
                              with local ordinances. It also dispatches location details and notifications are dispatched to the Unified Communications
                              Manager.

The following image shows the connection between the Emergency Responder and Unified Communications Manager.

For more information on Cisco Emergency Responder, see Cisco Emergency Responder Administration Guide .

### Unified Communications Manager as MLTS

The Cisco Unified Communications Manager Administration is an MLTS that has an inbuilt software to detect an absence of a
                              direct 911 dial pattern for systems installed in the US time zone.

If the 911 route pattern isn’t enabled, the Cisco Unified CM Administration home page displays an alert message: You have not configured a direct dial 911 pattern on this system. Federal Communication Commission rules mandate that most
                                 multi-line telephone systems in the US have a direct dial 911 pattern.

If the system installed in a non-US time zone, where FCC laws aren't applicable, Emergency Call Routing Regulations configuration
                              page disabled in the Unified Communications Manager.

You should consult with their legal counselor on the applicability of FCC laws and acknowledge in the system.

## Configure Emergency Call Routing Regulations

Emergency Call Routing Regulation configured on Unified Communications Manager to acknowledge and configure the direct dial
                              911 route pattern in compliance with the laws.

### Before you begin

Step 1

To access the Emergency Call Routing Regulations window, perform either of the following:

From Cisco Unified CM Administration, choose Advanced Features > Emergency Call Routing Regulations

Click the link available in the alert notification to configure the 911 route pattern on the home page.

Step 2

Check the I have read the above notification,and I have consulted my legal counsel to determine my specific obligations check box to acknowledge the notification.

Step 3

Check the Take me to the 911 configuration page check box and click Submit to set up direct 911 notification if the FCC laws are applicable.  You are navigated to the Route Pattern Configuration window and by default, a 911 pattern is configured in the Pattern Definition section.

Step 4

Choose an appropriate gateway, route, or trunk from the Gateway/Route List drop-down list for the configured pattern. For more information on the other fields and their configurations, see Online
                                       Help.

Step 5

Click Save .

If the system installed in the US time zone where FCC laws aren't applicable, acknowledge the law and check the Disable any further notification regarding my 911 obligation check box in the Emergency Call Routing Regulations window and click Submit to disable the 911 notifications.

If the laws aren't applicable, the administrator waives the notifications for future upgrades and new installations of the
                                                      911 route pattern.

The configured settings get preserved for future upgrade. The alert notification disappears on the home page and the Emergency Call Routing Regulations window gets disabled.

If the system has already created a 911 route pattern during upgrade or  the time zone changed from non-US to US timezone
                                                      then the acknowledge page is grayed out.

| Note | You should consult with their legal counselor on the applicability of FCC laws and acknowledge in the system. |
|---|---|

| Step 1 | To access the Emergency Call Routing Regulations window, perform either of the following: From Cisco Unified CM Administration, choose Advanced Features > Emergency Call Routing Regulations Click the link available in the alert notification to configure the 911 route pattern on the home page. |
|---|---|
| Step 2 | Check the I have read the above notification,and I have consulted my legal counsel to determine my specific obligations check box to acknowledge the notification. |
| Step 3 | Check the Take me to the 911 configuration page check box and click Submit to set up direct 911 notification if the FCC laws are applicable.  You are navigated to the Route Pattern Configuration window and by default, a 911 pattern is configured in the Pattern Definition section. |
| Step 4 | Choose an appropriate gateway, route, or trunk from the Gateway/Route List drop-down list for the configured pattern. For more information on the other fields and their configurations, see Online
                                       Help. |
| Step 5 | Click Save . Note If the system installed in the US time zone where FCC laws aren't applicable, acknowledge the law and check the Disable any further notification regarding my 911 obligation check box in the Emergency Call Routing Regulations window and click Submit to disable the 911 notifications. If the laws aren't applicable, the administrator waives the notifications for future upgrades and new installations of the
                                                      911 route pattern. The configured settings get preserved for future upgrade. The alert notification disappears on the home page and the Emergency Call Routing Regulations window gets disabled. If the system has already created a 911 route pattern during upgrade or  the time zone changed from non-US to US timezone
                                                      then the acknowledge page is grayed out. | Note | If the system installed in the US time zone where FCC laws aren't applicable, acknowledge the law and check the Disable any further notification regarding my 911 obligation check box in the Emergency Call Routing Regulations window and click Submit to disable the 911 notifications. If the laws aren't applicable, the administrator waives the notifications for future upgrades and new installations of the
                                                      911 route pattern. The configured settings get preserved for future upgrade. The alert notification disappears on the home page and the Emergency Call Routing Regulations window gets disabled. If the system has already created a 911 route pattern during upgrade or  the time zone changed from non-US to US timezone
                                                      then the acknowledge page is grayed out. |
| Note | If the system installed in the US time zone where FCC laws aren't applicable, acknowledge the law and check the Disable any further notification regarding my 911 obligation check box in the Emergency Call Routing Regulations window and click Submit to disable the 911 notifications. If the laws aren't applicable, the administrator waives the notifications for future upgrades and new installations of the
                                                      911 route pattern. The configured settings get preserved for future upgrade. The alert notification disappears on the home page and the Emergency Call Routing Regulations window gets disabled. If the system has already created a 911 route pattern during upgrade or  the time zone changed from non-US to US timezone
                                                      then the acknowledge page is grayed out. |

| Note | If the system installed in the US time zone where FCC laws aren't applicable, acknowledge the law and check the Disable any further notification regarding my 911 obligation check box in the Emergency Call Routing Regulations window and click Submit to disable the 911 notifications. If the laws aren't applicable, the administrator waives the notifications for future upgrades and new installations of the
                                                      911 route pattern. The configured settings get preserved for future upgrade. The alert notification disappears on the home page and the Emergency Call Routing Regulations window gets disabled. If the system has already created a 911 route pattern during upgrade or  the time zone changed from non-US to US timezone
                                                      then the acknowledge page is grayed out. |
|---|---|