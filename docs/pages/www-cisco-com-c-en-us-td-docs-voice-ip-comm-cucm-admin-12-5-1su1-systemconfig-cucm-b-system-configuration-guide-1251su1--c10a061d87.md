---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su1-systemconfig-cucm-b-system-configuration-guide-1251su1--c10a061d87
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU1/systemConfig/cucm_b_system-configuration-guide-1251su1/cucm_b_system-configuration-guide-1251su1_restructured_chapter_010110.html
retrieved_at: 2026-08-16T17:49:17.026252+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Updated: July 31, 2025

Chapter: Configure Dial Rules

## Chapter: Configure Dial Rules

# Configure Dial Rules

## Dial Rules
                        	 Overview

The Unified CM supports the following types of dial rules:

Application Dial Rules : The administrator uses application dial rules to add and sort the priority of dialing rules for applications such as Cisco
                                 web dialer and Cisco Unified Communications Manager Assistant .

Directory Lookup Dial Rules : The administrator uses directory lookup dial rules to transform caller identification numbers and perform a directory search
                                 from the assistant console in application such as Cisco Unified Communications Manager Assistant .

SIP Dial Rules : The administrator uses SIP dial rules to perform system digit analysis and routing. The administrator configures SIP dial
                                 rules and adds the SIP dial rule to the Cisco Unified IP Phone before the call processing takes place.

## Dial Rules
                        	 Prerequisites

For SIP dial rules configuration, the devices must be running SIP

The administrator associates the SIP dial rules with the following devices: Cisco IP Phones 7911, 7940, 7941, 7960, 7961

## Dial Rules
                        	 Configuration Task Flow

Step 1

Configure Application Dial Rules

Step 2

Configure Directory Lookup Dial Rules

Step 3

Configure SIP Dial Rules

Step 4

Reprioritize Dial Rule

Optional.
                                          				Change the priority of the dial rules in the Cisco Unified Communications
                                          				Manager Administration window, if more than one dial rule exists.

### Configure
                           	 Application Dial Rules

Cisco Unified
                                    			 Communications Manager supports application dial rules that allow you
                                 		  to add and sort the priority of dialing rules for applications such as Cisco
                                 		  web dialer and Cisco Unified Communications Manager Assistant. Application dial
                                 		  rules automatically strip numbers from or add numbers to telephone numbers that
                                 		  the user dials. For example, the dial rules automatically add the digit 9 in
                                 		  front of a 7-digit telephone number to provide access to an outside line.

Cisco Unified Communications Manager automatically
                                             			 applies application dial rules to all remote destination numbers for CTI remote
                                             			 devices.

Perform the
                                 		  following procedure to add a new application dial rule or update an existing
                                 		  application dial rule.

Step 1

From Cisco
                                          			 Unified Communications Manager Administration, choose Call
                                                				  Routing > Dial Rules > Application Dial
                                                				  Rules .

Step 2

In the Find
                                             				and List Application Dial Rules window, perform one of the following
                                          			 steps:

- Click Add
                                                				  New .

- Click Find and choose an existing application dial rule.

Step 3

Configure the
                                          			 fields in the Application Dial Rule Configuration window. For
                                          			 detailed field descriptions, refer to the online help.

Step 4

Click Save .

#### What to do next

- Configure Directory Lookup Dial Rules

- Configure SIP Dial Rules

### Configure
                           	 Directory Lookup Dial Rules

Directory lookup
                                 		  dial rules transform caller identification numbers into numbers that can be
                                 		  looked up in the directory. Each rule specifies which numbers to transform,
                                 		  based on the beginning digits and length of the number. For example, you can
                                 		  create a directory lookup dial rule that automatically removes the area code
                                 		  and two prefix digits from a 10-digit telephone, which would transform
                                 		  4085551212 into 51212.

Perform the
                                 		  following procedure to add a new directory lookup dial rule or update an
                                 		  existing directory lookup dial rule.

Step 1

From Cisco
                                          			 Unified Communications Manager Administration, choose Call
                                                				  Routing > Dial Rules > Directory Lookup Dial
                                                				  Rules .

Step 2

In the Directory Lookup Dial Rule Find and List window Directory Lookup Dial Rule Find and List window,
                                          			 perform one of the following steps:

- Click Add
                                                				  New .

- Click Find and choose an existing directory lookup dial
                                             				rule.

Step 3

Configure the
                                          			 fields in the Directory Lookup Dial Rule Configuration window. For
                                          			 detailed field descriptions, refer to the online help.

Step 4

Click Save .

#### What to do next

Configure SIP Dial Rules

### Configure SIP Dial Rules

SIP dial rules provide local dial plans for Cisco IP Phones that are running SIP, so users do not have to press a key or wait
                                 for a timer before the call gets processed. The administrator configures the SIP dial rule and applies it to the phone that
                                 is running SIP.

Step 1

Set Up SIP Dial Rule

Configure and update SIP dial rules and associate them with the phones that are running SIP.

Step 2

Reset SIP Dial Rule

Reset or restart the phone that is running SIP when the SIP dial rule gets updated, so that the phone is updated with the
                                             new SIP dial rule.

Step 3

Synchronize SIP Dial Rules Settings With SIP Phones

(Optional) Synchronize a SIP phone with a SIP dial rule that has undergone configuration changes, which applies any outstanding
                                             configuration settings in the least intrusive manner possible. For example, a reset or restart may not be required on some
                                             affected SIP phones.

#### Pattern
                              	 Formats

Dial Rule
                                                   					 Pattern

Value

7940_7960_OTHER

Period
                                                            						  (.) matches any character

You must configure the pound sign in the pattern field so that it is valid for 7940_7960_OTHER.

Asterisk (*) matches one or more characters and it gets
                                                            						  processed as a wildcard character. You can override this by preceding the *
                                                            						  with a backward slash (\) escape sequence, which results in the sequence \*.
                                                            						  The phone automatically strips the \, so it does not appear in the outgoing
                                                            						  dial string. When * is received as a dial digit, it gets matched by the
                                                            						  wildcard characters * and period (.).

Comma
                                                            						  (,) causes the phone to generate a secondary dial tone.

For
                                                            						  example, 7.... will match any 4-digit DN that starts with 7. 8,..... will match
                                                            						  8, play secondary dial tone (default value), and then match any 5-digit DN.

#### Set Up SIP Dial
                              	 Rule

To configure dial plans for phones that are running SIP.

Step 1

From Cisco
                                             			 Unified Communications Manager Administration, choose Call
                                                   				  Routing > Dial Rules > SIP Dial
                                                   				  Rules .

Step 2

In the Find and List SIP Dial Rules window. Perform one
                                             			 of the following steps:

- Click Add
                                                   				  New

- Click Find and choose an existing SIP Dial Rule

Step 3

Configure the
                                             			 fields in the SIP
                                                				Dial Rule Configuration window. For detailed field descriptions,
                                             			 refer to the online help.

Step 4

Click Save .

When you add
                                                            				  or update a SIP dial rule in Cisco Unified Communications Manager
                                                            				  Administration, be aware that the Cisco TFTP service rebuilds all phone
                                                            				  configuration files, which may cause CPU to spike on the server where the Cisco
                                                            				  TFTP service runs, especially if you have a large system with many phones. To
                                                            				  ensure that CPU does not spike, add or update the SIP dial rule during a
                                                            				  maintenance window or temporarily stop the Cisco TFTP service in Cisco Unified
                                                            				  Serviceability before you make the configuration change. If you stop the Cisco
                                                            				  TFTP service, remember to restart the service in Cisco Unified Serviceability
                                                            				  after you add or update the SIP dial rule.

##### What to do next

Reset SIP Dial Rule

#### Reset SIP Dial
                              	 Rule

Perform the
                                    		  following procedure to reset or restart the phone that is running SIP when the
                                    		  SIP dial rule gets updated, so the phone gets updated with the new SIP dial
                                    		  rule.

##### Before you begin

Step 1

From Cisco
                                             			 Unified Communications Manager Administration, choose Call
                                                   				  Routing > Dial Rules > Application Dial
                                                   				  Rules .

Step 2

In the Find
                                                				and List SIP Dial Rules window, click Find and choose an existing SIP dial rule that you
                                             			 want to reset.

Step 3

In the SIP
                                                				Dial Rule Configuration window, click Reset .

Step 4

Perform one of
                                             			 the following tasks in the Device
                                                				Reset dialog box:

To restart
                                                   				  the chosen devices without shutting them down and reregister them with Cisco Unified Communications Manager , click Restart .

- To shut down, and then
                                                				restart the device, click Reset .

- To close the Device Reset
                                                				dialog box without performing any action, click Close .

After the
                                                				administrator configures the SIP dial rule and applies it to the phone that is
                                                				running SIP, the database sends the TFTP server a notification, so it can build
                                                				a new set of configuration files for the phone that is running SIP. The TFTP
                                                				server notifies Cisco
                                                   				  Unified Communications Manager about the new configuration file, and
                                                				the updated configuration file is sent to the phone. See Configure
                                                   				  TFTP Servers for Cisco Unified IP phones that run SIP for more information.

##### What to do next

Synchronize SIP Dial Rules Settings With SIP Phones

#### Synchronize SIP
                              	 Dial Rules Settings With SIP Phones

To synchronize a
                                    		  SIP phone with a SIP dial rule that has undergone configuration changes,
                                    		  perform the following procedure.

##### Before you begin

Step 1

From Cisco
                                             			 Unified Communications Manager Administration, choose Call
                                                   				  Routing > Dial Rules > SIP Dial
                                                   				  Rules .

Step 2

In the Find
                                                				and List SIP Dial Rules window, click Find and choose an existing SIP dial rule to which
                                             			 you want to synchronize applicable SIP phones.

Step 3

Make any
                                             			 additional configuration changes and click Save in the SIP
                                                				Dial Rule Configuration .

Step 4

Click Apply
                                                				Config .

Step 5

Click OK .

### Reprioritize Dial
                           	 Rule

To add and sort the priority of dialing rules in the Dial Rule Configuration window.

Step 1

From Cisco
                                          			 Unified Communications Manager Administration, choose Call
                                                				  Routing > Dial Rules .

Step 2

Select one of
                                          			 the following:

- Application Dial
                                                				  Rules

- Directory Lookup Dial
                                                				  Rules

- SIP Dial Rules

Step 3

In the Find
                                          			 and List window, choose a dial rule and click the dial rule name.

Step 4

Use the up and
                                          			 down arrows to move the dial rule up or down the list.

Step 5

After you
                                          			 complete prioritizing the order, click Save .

## Dial Rules Interactions and Restrictions

### SIP Dial Rules
                           	 Interactions

#### SIP Dial Rules Interactions

Cisco Unified IP Phone

Interaction

7911, 7941, 7961 that are running SIP

These phones use the 7940_7960_OTHER dial rules patterns.
                                             						Key Press Markup Language (KPML) allows for the digits to be sent to Cisco Unified Communications Manager digit
                                             						by digit; SIP dial rules allow for a pattern of digits to be collected locally
                                             						on the phone prior to sending to Cisco Unified Communications Manager. If SIP
                                             						dial rules are not configured, KPML is used. To increase the performance of Cisco Unified Communications Manager (increasing the number of calls that get processed), Cisco recommends that
                                             						administrators configure SIP dial rules.

7940 and 7960 that are running SIP

These phones use the 7940_7960_OTHER dial rules pattern and
                                             						do not support KPML. If the administrator does not configure a SIP dial plan
                                             						for these phones, the user must wait a specified time before the digits are
                                             						sent to Cisco Unified Communications Manager for
                                             						processing. This delays the processing of the actual call.

### Directory Lookup
                           	 Dial Rules Restrictions

#### Directory Lookup Dial Rules Restrictions

Field

Restriction

Number Begins With

This field supports only digits and the characters +,*, and
                                             						#. The length cannot exceed 100 characters.

Number of Digits

This field supports only digits, and the value in this field
                                             						cannot be less than the length of the pattern that is specified in the pattern
                                             						field.

Total Digits to be Removed

This field supports only digits, and the value in this field
                                             						cannot be more than the value in the Number of Digits field.

Prefix with Pattern

The prefix it with field supports only digits and the
                                             						characters +,*, and #. The length cannot exceed 100 characters.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Application Dial Rules | Configure
                                       			 application dial rules to add and sort the priority of dialing rules for
                                       			 applications such as Cisco web dialer and Cisco Unified Communications Manager
                                       			 Assistant. |
| Step 2 | Configure Directory Lookup Dial Rules | Configure
                                       			 directory lookup dial rules to transform caller identification numbers into
                                       			 numbers that can be looked up in the directory. |
| Step 3 | Configure SIP Dial Rules | Use SIP dial
                                       			 rules configuration to configure dial plans for phones that are running SIP. |
| Step 4 | Reprioritize Dial Rule | Optional.
                                          				Change the priority of the dial rules in the Cisco Unified Communications
                                          				Manager Administration window, if more than one dial rule exists. |

| Note | Cisco Unified Communications Manager automatically
                                             			 applies application dial rules to all remote destination numbers for CTI remote
                                             			 devices. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified Communications Manager Administration, choose Call
                                                				  Routing > Dial Rules > Application Dial
                                                				  Rules . |
|---|---|
| Step 2 | In the Find
                                             				and List Application Dial Rules window, perform one of the following
                                          			 steps: Click Add
                                                				  New . Click Find and choose an existing application dial rule. |
| Step 3 | Configure the
                                          			 fields in the Application Dial Rule Configuration window. For
                                          			 detailed field descriptions, refer to the online help. |
| Step 4 | Click Save . |

| Step 1 | From Cisco
                                          			 Unified Communications Manager Administration, choose Call
                                                				  Routing > Dial Rules > Directory Lookup Dial
                                                				  Rules . |
|---|---|
| Step 2 | In the Directory Lookup Dial Rule Find and List window Directory Lookup Dial Rule Find and List window,
                                          			 perform one of the following steps: Click Add
                                                				  New . Click Find and choose an existing directory lookup dial
                                             				rule. |
| Step 3 | Configure the
                                          			 fields in the Directory Lookup Dial Rule Configuration window. For
                                          			 detailed field descriptions, refer to the online help. |
| Step 4 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Set Up SIP Dial Rule | Configure and update SIP dial rules and associate them with the phones that are running SIP. |
| Step 2 | Reset SIP Dial Rule | Reset or restart the phone that is running SIP when the SIP dial rule gets updated, so that the phone is updated with the
                                             new SIP dial rule. |
| Step 3 | Synchronize SIP Dial Rules Settings With SIP Phones | (Optional) Synchronize a SIP phone with a SIP dial rule that has undergone configuration changes, which applies any outstanding
                                             configuration settings in the least intrusive manner possible. For example, a reset or restart may not be required on some
                                             affected SIP phones. |

| Dial Rule
                                                   					 Pattern | Value |
|---|---|
| 7940_7960_OTHER | Period
                                                            						  (.) matches any character Pound sign (#) acts as the terminating key, and you can apply termination only after matching hits. Alternatively asterisk
                                                            (*) can also be used as a terminating key as well. Note You must configure the pound sign in the pattern field so that it is valid for 7940_7960_OTHER. Asterisk (*) matches one or more characters and it gets
                                                            						  processed as a wildcard character. You can override this by preceding the *
                                                            						  with a backward slash (\) escape sequence, which results in the sequence \*.
                                                            						  The phone automatically strips the \, so it does not appear in the outgoing
                                                            						  dial string. When * is received as a dial digit, it gets matched by the
                                                            						  wildcard characters * and period (.). Comma
                                                            						  (,) causes the phone to generate a secondary dial tone. For
                                                            						  example, 7.... will match any 4-digit DN that starts with 7. 8,..... will match
                                                            						  8, play secondary dial tone (default value), and then match any 5-digit DN. | Note | You must configure the pound sign in the pattern field so that it is valid for 7940_7960_OTHER. |
| Note | You must configure the pound sign in the pattern field so that it is valid for 7940_7960_OTHER. |

| Note | You must configure the pound sign in the pattern field so that it is valid for 7940_7960_OTHER. |
|---|---|

| Step 1 | From Cisco
                                             			 Unified Communications Manager Administration, choose Call
                                                   				  Routing > Dial Rules > SIP Dial
                                                   				  Rules . |
|---|---|
| Step 2 | In the Find and List SIP Dial Rules window. Perform one
                                             			 of the following steps: Click Add
                                                   				  New Click Find and choose an existing SIP Dial Rule |
| Step 3 | Configure the
                                             			 fields in the SIP
                                                				Dial Rule Configuration window. For detailed field descriptions,
                                             			 refer to the online help. |
| Step 4 | Click Save . Note When you add
                                                            				  or update a SIP dial rule in Cisco Unified Communications Manager
                                                            				  Administration, be aware that the Cisco TFTP service rebuilds all phone
                                                            				  configuration files, which may cause CPU to spike on the server where the Cisco
                                                            				  TFTP service runs, especially if you have a large system with many phones. To
                                                            				  ensure that CPU does not spike, add or update the SIP dial rule during a
                                                            				  maintenance window or temporarily stop the Cisco TFTP service in Cisco Unified
                                                            				  Serviceability before you make the configuration change. If you stop the Cisco
                                                            				  TFTP service, remember to restart the service in Cisco Unified Serviceability
                                                            				  after you add or update the SIP dial rule. | Note | When you add
                                                            				  or update a SIP dial rule in Cisco Unified Communications Manager
                                                            				  Administration, be aware that the Cisco TFTP service rebuilds all phone
                                                            				  configuration files, which may cause CPU to spike on the server where the Cisco
                                                            				  TFTP service runs, especially if you have a large system with many phones. To
                                                            				  ensure that CPU does not spike, add or update the SIP dial rule during a
                                                            				  maintenance window or temporarily stop the Cisco TFTP service in Cisco Unified
                                                            				  Serviceability before you make the configuration change. If you stop the Cisco
                                                            				  TFTP service, remember to restart the service in Cisco Unified Serviceability
                                                            				  after you add or update the SIP dial rule. |
| Note | When you add
                                                            				  or update a SIP dial rule in Cisco Unified Communications Manager
                                                            				  Administration, be aware that the Cisco TFTP service rebuilds all phone
                                                            				  configuration files, which may cause CPU to spike on the server where the Cisco
                                                            				  TFTP service runs, especially if you have a large system with many phones. To
                                                            				  ensure that CPU does not spike, add or update the SIP dial rule during a
                                                            				  maintenance window or temporarily stop the Cisco TFTP service in Cisco Unified
                                                            				  Serviceability before you make the configuration change. If you stop the Cisco
                                                            				  TFTP service, remember to restart the service in Cisco Unified Serviceability
                                                            				  after you add or update the SIP dial rule. |

| Note | When you add
                                                            				  or update a SIP dial rule in Cisco Unified Communications Manager
                                                            				  Administration, be aware that the Cisco TFTP service rebuilds all phone
                                                            				  configuration files, which may cause CPU to spike on the server where the Cisco
                                                            				  TFTP service runs, especially if you have a large system with many phones. To
                                                            				  ensure that CPU does not spike, add or update the SIP dial rule during a
                                                            				  maintenance window or temporarily stop the Cisco TFTP service in Cisco Unified
                                                            				  Serviceability before you make the configuration change. If you stop the Cisco
                                                            				  TFTP service, remember to restart the service in Cisco Unified Serviceability
                                                            				  after you add or update the SIP dial rule. |
|---|---|

| Step 1 | From Cisco
                                             			 Unified Communications Manager Administration, choose Call
                                                   				  Routing > Dial Rules > Application Dial
                                                   				  Rules . |
|---|---|
| Step 2 | In the Find
                                                				and List SIP Dial Rules window, click Find and choose an existing SIP dial rule that you
                                             			 want to reset. |
| Step 3 | In the SIP
                                                				Dial Rule Configuration window, click Reset . |
| Step 4 | Perform one of
                                             			 the following tasks in the Device
                                                				Reset dialog box: To restart
                                                   				  the chosen devices without shutting them down and reregister them with Cisco Unified Communications Manager , click Restart . To shut down, and then
                                                				restart the device, click Reset . To close the Device Reset
                                                				dialog box without performing any action, click Close . After the
                                                				administrator configures the SIP dial rule and applies it to the phone that is
                                                				running SIP, the database sends the TFTP server a notification, so it can build
                                                				a new set of configuration files for the phone that is running SIP. The TFTP
                                                				server notifies Cisco
                                                   				  Unified Communications Manager about the new configuration file, and
                                                				the updated configuration file is sent to the phone. See Configure
                                                   				  TFTP Servers for Cisco Unified IP phones that run SIP for more information. |

| Step 1 | From Cisco
                                             			 Unified Communications Manager Administration, choose Call
                                                   				  Routing > Dial Rules > SIP Dial
                                                   				  Rules . |
|---|---|
| Step 2 | In the Find
                                                				and List SIP Dial Rules window, click Find and choose an existing SIP dial rule to which
                                             			 you want to synchronize applicable SIP phones. |
| Step 3 | Make any
                                             			 additional configuration changes and click Save in the SIP
                                                				Dial Rule Configuration . |
| Step 4 | Click Apply
                                                				Config . |
| Step 5 | Click OK . |

| Step 1 | From Cisco
                                          			 Unified Communications Manager Administration, choose Call
                                                				  Routing > Dial Rules . |
|---|---|
| Step 2 | Select one of
                                          			 the following: Application Dial
                                                				  Rules Directory Lookup Dial
                                                				  Rules SIP Dial Rules |
| Step 3 | In the Find
                                          			 and List window, choose a dial rule and click the dial rule name. The Dial
                                             				Rule Configuration window appears. |
| Step 4 | Use the up and
                                          			 down arrows to move the dial rule up or down the list. |
| Step 5 | After you
                                          			 complete prioritizing the order, click Save . |

| Cisco Unified IP Phone | Interaction |
|---|---|
| 7911, 7941, 7961 that are running SIP | These phones use the 7940_7960_OTHER dial rules patterns.
                                             						Key Press Markup Language (KPML) allows for the digits to be sent to Cisco Unified Communications Manager digit
                                             						by digit; SIP dial rules allow for a pattern of digits to be collected locally
                                             						on the phone prior to sending to Cisco Unified Communications Manager. If SIP
                                             						dial rules are not configured, KPML is used. To increase the performance of Cisco Unified Communications Manager (increasing the number of calls that get processed), Cisco recommends that
                                             						administrators configure SIP dial rules. |
| 7940 and 7960 that are running SIP | These phones use the 7940_7960_OTHER dial rules pattern and
                                             						do not support KPML. If the administrator does not configure a SIP dial plan
                                             						for these phones, the user must wait a specified time before the digits are
                                             						sent to Cisco Unified Communications Manager for
                                             						processing. This delays the processing of the actual call. |

| Field | Restriction |
|---|---|
| Number Begins With | This field supports only digits and the characters +,*, and
                                             						#. The length cannot exceed 100 characters. |
| Number of Digits | This field supports only digits, and the value in this field
                                             						cannot be less than the length of the pattern that is specified in the pattern
                                             						field. |
| Total Digits to be Removed | This field supports only digits, and the value in this field
                                             						cannot be more than the value in the Number of Digits field. |
| Prefix with Pattern | The prefix it with field supports only digits and the
                                             						characters +,*, and #. The length cannot exceed 100 characters. Note You cannot allow both the Total Digits to be Removed field and
                                                      						the Prefix with Pattern field to be blank
                                                      						for a dial rule. | Note | You cannot allow both the Total Digits to be Removed field and
                                                      						the Prefix with Pattern field to be blank
                                                      						for a dial rule. |
| Note | You cannot allow both the Total Digits to be Removed field and
                                                      						the Prefix with Pattern field to be blank
                                                      						for a dial rule. |

| Note | You cannot allow both the Total Digits to be Removed field and
                                                      						the Prefix with Pattern field to be blank
                                                      						for a dial rule. |
|---|---|