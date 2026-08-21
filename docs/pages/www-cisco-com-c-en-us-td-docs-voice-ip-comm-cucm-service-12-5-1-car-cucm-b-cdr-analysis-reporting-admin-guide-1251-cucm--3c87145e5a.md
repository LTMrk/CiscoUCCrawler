---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-service-12-5-1-car-cucm-b-cdr-analysis-reporting-admin-guide-1251-cucm--3c87145e5a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/service/12_5_1/Car/cucm_b_cdr-analysis-reporting-admin-guide-1251/cucm_b_cdr-analysis-reporting-admin-guide-1251_chapter_011101.html
retrieved_at: 2026-08-21T01:37:24.560095+00:00
---

Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

# Cisco Unified CDR Analysis and Reporting Administration Guide, Release 12.5(1)

Updated: January 22, 2019

Chapter: CAR System Parameters

## Chapter: CAR System Parameters

# CAR System Parameters

Before you start generating reports with CAR, configure the
                        		system. In most cases, CAR provides default values; however, review the topics
                        		in this chapter to learn more about customizing CAR.

Unless you want to use the default values, you should customize
                        		a number of system parameters before you generate any reports. This section
                        		describes the system parameters that affect CAR. Because default values are
                        		provided for all system parameters, Cisco recommends customizing but does not
                        		require it.

## Set Up Mail Server Parameters

To send e-mail alerts and reports by e-mail, you must specify
                              		  the mail server configuration information. CAR uses the configuration
                              		  information to successfully connect to the e-mail server.

This section describes how to specify e-mail server
                              		  information.

Choose System > System Parameters > Mail
                                             				  Parameters .

The Mail Parameters window displays.

In the Mail ID field, only enter the e-mail identifier that will
                                       			 be used in the From field when e-mails are sent (for example, smith1@abc.com,
                                       			 enter smith1 in the Mail ID field.

CAR does not support SMTP authentication. You must disable
                                                      				  authentication on the SMTP mail server.

In the Mail Server Name field, enter the domain name for the
                                       			 server that runs the e-mail system (that is, abc.com from the previous example.

To make the changes, click the Update button.

## Set Up Dial
                        	 Plan

The default
                              		  dial plan in CAR specifies the North American numbering plan (NANP). Make sure
                              		  that the dial plan is properly configured, so call classifications display
                              		  correctly in the reports.

If you have modified the default NANP that is provided in Cisco Unified CM Administration , or if you are outside the NANP, be sure to configure the dial plan in CAR according to your Unified Communications Manager dial plan. At least one condition must exist to configure the Dial Plan.

For more
                                          			 information about dial plan, see the Cisco Unified Communications Manager Online Help and the Cisco Unified Communications Manager System Guide .

To
                              		  configure the dial plan, define the parameters for the outgoing call
                              		  classifications. Call classifications include International, Local, Long
                              		  Distance, On Net, and so on. For example, if local calls in your area equal six
                              		  digits in length, you would specify a row in the dial plan as follows:

Condition

No of
                                          				  Digits

Pattern

Call
                                          				  Type

=

6

!

Local

This
                              		  section describes how to update the CAR dial plan configuration.

Choose System > System
                                             				  Parameters > Dial Plan Configuration .

The Dial Plan
                                          				Configuration window displays.

In the Toll Free
                                       			 Numbers field, enter the numbers in your dial plan that can be placed without a
                                       			 charge.

Update the
                                       			 values in the table by using the following fields:

Condition -
                                             				  Select the condition of the rule where > represents greater than, < represents less than, and = represents a value that is equal to the specified value in the No of Digits
                                             				  field.

No of Digits
                                             				  - Choose the number of digits in the directory number to which this rule should
                                             				  be applied. If the number of digits does not impact the rule, specify NA.

Pattern -
                                             				  Enter the pattern that is used for the call classification, where

- G - Signifies classified as
                                                   						specified in the rule (G equals a wildcard for the gateway area code that is
                                                   						specified.

- K - Signifies classified as
                                                   						specified in the rule (K equals a wildcard for the trunk area code that is
                                                   						specified)

- T - Retrieves the toll-free
                                                   						numbers that are configured in CAR.

- ! - Signifies multiple digits
                                                   						(any number that is more than 1 digit in length, such as 1234 or 5551234).

- X - Signifies a single-digit
                                                   						number (such as 0, 1, or 9).

Call Type -
                                             				  Choose the call type if the condition is satisfied.

To add more
                                       			 rows, check the check box in the row below where you want to add rows and click
                                       			 the Add
                                          				Rows link. The system adds a row above the row that you chose. To
                                       			 delete a row, check the check box by the row that you want to delete and click
                                       			 the Delete
                                          				Rows link.

CAR classifies
                                                      				  calls on the basis of the dialed number as stored in the CDRs. If the dialed
                                                      				  digits differ from the digits that are written in CDRs (due to number
                                                      				  transformations), configure the Dial Plan in CAR on the basis of how the digits
                                                      				  show up in CDRs.

To make the
                                       			 changes, click the Update button.

## Restore Default Values

If you have modified the default dial plan in CAR, you can
                              		  restore the default values that are based on the North American numbering plan
                              		  (NANP).

The following table provides the default NANP values.

Row

Condition

No of Digits

Pattern

Call Type

1

=

5

!

OnNet

2

=

7

!

Local

3

=

10

T!

Others

4

=

10

G!

Local

5

=

10

K!

Local

6

=

10

!

Long Distance

7

=

11

T!

Others

8

=

11

XG!

Local

9

=

11

XK!

Local

10

=

11

!

Long Distance

11

>

3

011!

International

The following information explains the default table values.

- Row 1 - If the number of
                                 			 digits dialed equals 5 and the pattern is! (more than one digit, in this case,
                                 			 5 digits), the call gets classified as On Net.

- Row 2 - If the number of
                                 			 digits dialed equals 7 and the pattern is ! (more than one digit, in this case,
                                 			 7 digits), the call gets classified as Local.

- Row 3 - If the number of
                                 			 digits dialed equals 10 and the pattern is T! (more than one digit, in this
                                 			 case a 10-digit number that starts with a Toll Free number code), the call gets
                                 			 classified as Others.

- Row 4 - If the number of
                                 			 digits dialed equals 10 and the pattern is G! (more than one digit, in this
                                 			 case a 10-digit number that starts with a gateway code), the call gets
                                 			 classified as Local.

- Row 5 - If the number of
                                 			 digits dialed equals 10 and the pattern is K! (more than one digit, in this
                                 			 case a 10-digit number that starts with a trunk code), the call gets classified
                                 			 as Local.

- Row 6 - If the number of
                                 			 digits dialed equals 10 and the pattern is! (more than one digit, in this case
                                 			 a 10-digit number), the call gets classified as Long Distance.

- Row 7 - If the number of
                                 			 digits dialed equals 11 and the pattern is T! (more than one digit, in this
                                 			 case an 11-digit number that starts with a toll-free number code), the call
                                 			 gets classified as Others.

- Row 8 - If the number of
                                 			 digits dialed equals 11 and the pattern is XG! (more than one digit, in this
                                 			 case an 11-digit number that starts with any single digit followed by a gateway
                                 			 code), the call gets classified as Local.

- Row 9 - If the number of
                                 			 digits dialed equals 11 and the pattern is XK! (more than one digit, in this
                                 			 case an 11-digit number that starts with any single digit followed by a trunk
                                 			 code), the call gets classified as Local.

- Row 10 - If the number of
                                 			 digits dialed equals 11 and the pattern is! (more than one digit, in this case
                                 			 an 11-digit number), the call gets classified as Long Distance.

- Row 11 - If the number of
                                 			 digits dialed is greater than 3 and starts with 011, the call gets classified as International.

If none of the conditions gets satisfied, the call gets
                              		  classified as Others. This section describes how to restore the NANP dial plan
                              		  values in CAR.

The combination of characters, such as '!!', 'GG', 'KK', 'TT', 'GK',
                                          			 'KG' is not allowed in dialplan configuration.

Choose System > System
                                                					 Parameters > Dial Plan
                                                					 Configuration .

The Dial Plan Configuration window displays.

Click the Restore Defaults button.

The restoration takes effect at midnight. To make changes take
                                          				effect immediately, restart the Cisco CAR Scheduler service. For information on
                                          				restarting services, see the Cisco Unified Serviceability Administration Guide .

## Set Up Gateway

Configure the gateways in CAR for existing Unified Communications Manager system gateways. After you add gateways to Cisco Unified CM Administration , configure the new gateways in CAR. When gateways are deleted from the Unified Communications Manager system, the system automatically removes the gateways (and any configuration settings that you specified) from CAR.

CAR uses the area code information to determine whether
                              		  calls are local or long distance. You must provide the Number of Ports
                              		  information for each gateway to enable CAR to generate the Utilization reports.

"G" acts as a wildcard for the gateway area codes that are used
                                          			 in Dial Plan configuration.

This section describes how to configure gateways in CAR.

Choose System > System
                                                					 Parameters > Gateway
                                                					 Configuration .

The Gateway Configuration window displays.

If you have not configured gateways in Cisco Unified CM Administration , a message displays that indicates that you have not configured gateways for the system.

Perform one of the following tasks:

To update the area code for all gateways, enter the area code
                                             				  in the Area Code field and click the Set Area Code button.

A message displays that indicates that you must click Update
                                                					 to save changes. Click OK .

To update the area code for specific gateways, enter the area
                                             				  code for each gateway that you want to configure in the area code field for
                                             				  that gateway.

In the Max No. of Ports field, enter the number of ports for each
                                       			 gateway that you want to configure. The Max No of Ports range goes from 1 to
                                       			 999.

CAR uses the values that were provided for the gateway when it was added in Cisco Unified CM Administration . Therefore, some gateways will already have an area code setting or have a zero for maximum number of ports, depending on
                                                      the details that were specified when the gateway was added in Cisco Unified CM Administration . CAR does not accept 0 as a value for the maximum number of ports; you may be prompted to change the maximum number of ports
                                                      for all gateways with a value of zero.

To make the changes, click the Update button.

You can run reports in CAR on any or all of the configured
                                          				gateways.

## Set Up Trunk

Configure the trunks in CAR for existing Unified Communications Manager system trunks. After you add trunks to Cisco Unified CM Administration , configure the new trunks in CAR. When trunks are deleted from the Unified Communications Manager system, the system automatically removes the trunks (and any configuration settings that you specified) from CAR.

CAR uses the area code information to determine whether
                              		  calls are local or long distance. You must provide the Number of Ports
                              		  information for each trunk to enable CAR to generate the Utilization reports.

This section describes how to configure trunks in CAR.

Choose System > System
                                             				  Parameters > Trunk Configuration .

The Trunk Configuration window displays.

If you have not configured trunks in Cisco Unified CM Administration , a message displays that indicates that you have not configured trunks for the system.

Perform one of the following tasks:

To update the area code for all trunks, enter the area code in
                                             				  the Area Code field and click the Set Area Code button.

A message displays that indicates that you must click Update
                                                					 to save changes. Click OK .

To update the area code for specific trunks, enter the area
                                             				  code for each trunk that you want to configure in the area code field for that
                                             				  trunk.

In the Max No. of Ports field, enter the number of ports for each
                                       			 trunk that you want to configure. The Max No of Ports range goes from 1 to
                                       			 999.

CAR uses the values that were provided for the trunk when it was added in Cisco Unified CM Administration . Therefore, some trunks will already have a zero for maximum number of ports, depending on the details that were specified
                                                      when the trunk was added in Cisco Unified CM Administration . CAR does not accept zero as a value for the maximum number of ports; you may be prompted to change the maximum number of
                                                      ports for all trunks with a value of zero.

To make the changes, click the Update button.

You can run reports in CAR on any or all of the configured trunks.

## Set Up System Preferences

CAR provides default system preferences; however, you may
                              		  customize the system by specifying values for the system parameters.

This section describes how to specify values for system
                              		  preferences.

Choose System > System
                                                					 Parameters > System
                                                					 Preferences .

The System Preferences window displays. The list of available
                                          				system parameters displays in the Parameter Name list.

In the Parameter Value field, enter the desired value for the
                                       			 parameter as described in the following table.

Parameter

Description

COMPANY_NAME

Enter the company name that is used as header
                                                      						  information in reports. The company name cannot exceed 64 characters in length.

Click the Update button.

## Related Topics

## Additional
                        	 Documentation

Administration Guide for
                                    				Cisco Unified Communications Manager

Cisco Unified Serviceability Administration Guide

Cisco Unified Communications Manager Call Detail Records
                                       				  Administration Guide

| Step 1 | Choose System > System Parameters > Mail
                                             				  Parameters . The Mail Parameters window displays. |
|---|---|
| Step 2 | In the Mail ID field, only enter the e-mail identifier that will
                                       			 be used in the From field when e-mails are sent (for example, smith1@abc.com,
                                       			 enter smith1 in the Mail ID field. Note CAR does not support SMTP authentication. You must disable
                                                      				  authentication on the SMTP mail server. | Note | CAR does not support SMTP authentication. You must disable
                                                      				  authentication on the SMTP mail server. |
| Note | CAR does not support SMTP authentication. You must disable
                                                      				  authentication on the SMTP mail server. |
| Step 3 | In the Mail Server Name field, enter the domain name for the
                                       			 server that runs the e-mail system (that is, abc.com from the previous example. |
| Step 4 | To make the changes, click the Update button. |

| Note | CAR does not support SMTP authentication. You must disable
                                                      				  authentication on the SMTP mail server. |
|---|---|

| Note | If you have modified the default NANP that is provided in Cisco Unified CM Administration , or if you are outside the NANP, be sure to configure the dial plan in CAR according to your Unified Communications Manager dial plan. At least one condition must exist to configure the Dial Plan. For more
                                          			 information about dial plan, see the Cisco Unified Communications Manager Online Help and the Cisco Unified Communications Manager System Guide . |
|---|---|

| Condition | No of
                                          				  Digits | Pattern | Call
                                          				  Type |
|---|---|---|---|
| = | 6 | ! | Local |

| Step 1 | Choose System > System
                                             				  Parameters > Dial Plan Configuration . The Dial Plan
                                          				Configuration window displays. |
|---|---|
| Step 2 | In the Toll Free
                                       			 Numbers field, enter the numbers in your dial plan that can be placed without a
                                       			 charge. |
| Step 3 | Update the
                                       			 values in the table by using the following fields: Condition -
                                             				  Select the condition of the rule where > represents greater than, < represents less than, and = represents a value that is equal to the specified value in the No of Digits
                                             				  field. No of Digits
                                             				  - Choose the number of digits in the directory number to which this rule should
                                             				  be applied. If the number of digits does not impact the rule, specify NA. Pattern -
                                             				  Enter the pattern that is used for the call classification, where G - Signifies classified as
                                                   						specified in the rule (G equals a wildcard for the gateway area code that is
                                                   						specified. K - Signifies classified as
                                                   						specified in the rule (K equals a wildcard for the trunk area code that is
                                                   						specified) T - Retrieves the toll-free
                                                   						numbers that are configured in CAR. ! - Signifies multiple digits
                                                   						(any number that is more than 1 digit in length, such as 1234 or 5551234). X - Signifies a single-digit
                                                   						number (such as 0, 1, or 9). Call Type -
                                             				  Choose the call type if the condition is satisfied. |
| Step 4 | To add more
                                       			 rows, check the check box in the row below where you want to add rows and click
                                       			 the Add
                                          				Rows link. The system adds a row above the row that you chose. To
                                       			 delete a row, check the check box by the row that you want to delete and click
                                       			 the Delete
                                          				Rows link. Note CAR classifies
                                                      				  calls on the basis of the dialed number as stored in the CDRs. If the dialed
                                                      				  digits differ from the digits that are written in CDRs (due to number
                                                      				  transformations), configure the Dial Plan in CAR on the basis of how the digits
                                                      				  show up in CDRs. | Note | CAR classifies
                                                      				  calls on the basis of the dialed number as stored in the CDRs. If the dialed
                                                      				  digits differ from the digits that are written in CDRs (due to number
                                                      				  transformations), configure the Dial Plan in CAR on the basis of how the digits
                                                      				  show up in CDRs. |
| Note | CAR classifies
                                                      				  calls on the basis of the dialed number as stored in the CDRs. If the dialed
                                                      				  digits differ from the digits that are written in CDRs (due to number
                                                      				  transformations), configure the Dial Plan in CAR on the basis of how the digits
                                                      				  show up in CDRs. |
| Step 5 | To make the
                                       			 changes, click the Update button. |

| Note | CAR classifies
                                                      				  calls on the basis of the dialed number as stored in the CDRs. If the dialed
                                                      				  digits differ from the digits that are written in CDRs (due to number
                                                      				  transformations), configure the Dial Plan in CAR on the basis of how the digits
                                                      				  show up in CDRs. |
|---|---|

| Row | Condition | No of Digits | Pattern | Call Type |
|---|---|---|---|---|
| 1 | = | 5 | ! | OnNet |
| 2 | = | 7 | ! | Local |
| 3 | = | 10 | T! | Others |
| 4 | = | 10 | G! | Local |
| 5 | = | 10 | K! | Local |
| 6 | = | 10 | ! | Long Distance |
| 7 | = | 11 | T! | Others |
| 8 | = | 11 | XG! | Local |
| 9 | = | 11 | XK! | Local |
| 10 | = | 11 | ! | Long Distance |
| 11 | > | 3 | 011! | International |

| Note | The combination of characters, such as '!!', 'GG', 'KK', 'TT', 'GK',
                                          			 'KG' is not allowed in dialplan configuration. |
|---|---|

| Step 1 | Choose System > System
                                                					 Parameters > Dial Plan
                                                					 Configuration . The Dial Plan Configuration window displays. |
|---|---|
| Step 2 | Click the Restore Defaults button. The restoration takes effect at midnight. To make changes take
                                          				effect immediately, restart the Cisco CAR Scheduler service. For information on
                                          				restarting services, see the Cisco Unified Serviceability Administration Guide . |

| Tip | Configure the gateways in CAR for existing Unified Communications Manager system gateways. After you add gateways to Cisco Unified CM Administration , configure the new gateways in CAR. When gateways are deleted from the Unified Communications Manager system, the system automatically removes the gateways (and any configuration settings that you specified) from CAR. |
|---|---|

| Note | "G" acts as a wildcard for the gateway area codes that are used
                                          			 in Dial Plan configuration. |
|---|---|

| Step 1 | Choose System > System
                                                					 Parameters > Gateway
                                                					 Configuration . The Gateway Configuration window displays. Note If you have not configured gateways in Cisco Unified CM Administration , a message displays that indicates that you have not configured gateways for the system. | Note | If you have not configured gateways in Cisco Unified CM Administration , a message displays that indicates that you have not configured gateways for the system. |
|---|---|---|---|
| Note | If you have not configured gateways in Cisco Unified CM Administration , a message displays that indicates that you have not configured gateways for the system. |
| Step 2 | Perform one of the following tasks: To update the area code for all gateways, enter the area code
                                             				  in the Area Code field and click the Set Area Code button. A message displays that indicates that you must click Update
                                                					 to save changes. Click OK . To update the area code for specific gateways, enter the area
                                             				  code for each gateway that you want to configure in the area code field for
                                             				  that gateway. |
| Step 3 | In the Max No. of Ports field, enter the number of ports for each
                                       			 gateway that you want to configure. The Max No of Ports range goes from 1 to
                                       			 999. Note CAR uses the values that were provided for the gateway when it was added in Cisco Unified CM Administration . Therefore, some gateways will already have an area code setting or have a zero for maximum number of ports, depending on
                                                      the details that were specified when the gateway was added in Cisco Unified CM Administration . CAR does not accept 0 as a value for the maximum number of ports; you may be prompted to change the maximum number of ports
                                                      for all gateways with a value of zero. | Note | CAR uses the values that were provided for the gateway when it was added in Cisco Unified CM Administration . Therefore, some gateways will already have an area code setting or have a zero for maximum number of ports, depending on
                                                      the details that were specified when the gateway was added in Cisco Unified CM Administration . CAR does not accept 0 as a value for the maximum number of ports; you may be prompted to change the maximum number of ports
                                                      for all gateways with a value of zero. |
| Note | CAR uses the values that were provided for the gateway when it was added in Cisco Unified CM Administration . Therefore, some gateways will already have an area code setting or have a zero for maximum number of ports, depending on
                                                      the details that were specified when the gateway was added in Cisco Unified CM Administration . CAR does not accept 0 as a value for the maximum number of ports; you may be prompted to change the maximum number of ports
                                                      for all gateways with a value of zero. |
| Step 4 | To make the changes, click the Update button. You can run reports in CAR on any or all of the configured
                                          				gateways. |

| Note | If you have not configured gateways in Cisco Unified CM Administration , a message displays that indicates that you have not configured gateways for the system. |
|---|---|

| Note | CAR uses the values that were provided for the gateway when it was added in Cisco Unified CM Administration . Therefore, some gateways will already have an area code setting or have a zero for maximum number of ports, depending on
                                                      the details that were specified when the gateway was added in Cisco Unified CM Administration . CAR does not accept 0 as a value for the maximum number of ports; you may be prompted to change the maximum number of ports
                                                      for all gateways with a value of zero. |
|---|---|

| Tip | Configure the trunks in CAR for existing Unified Communications Manager system trunks. After you add trunks to Cisco Unified CM Administration , configure the new trunks in CAR. When trunks are deleted from the Unified Communications Manager system, the system automatically removes the trunks (and any configuration settings that you specified) from CAR. |
|---|---|

| Step 1 | Choose System > System
                                             				  Parameters > Trunk Configuration . The Trunk Configuration window displays. Note If you have not configured trunks in Cisco Unified CM Administration , a message displays that indicates that you have not configured trunks for the system. | Note | If you have not configured trunks in Cisco Unified CM Administration , a message displays that indicates that you have not configured trunks for the system. |
|---|---|---|---|
| Note | If you have not configured trunks in Cisco Unified CM Administration , a message displays that indicates that you have not configured trunks for the system. |
| Step 2 | Perform one of the following tasks: To update the area code for all trunks, enter the area code in
                                             				  the Area Code field and click the Set Area Code button. A message displays that indicates that you must click Update
                                                					 to save changes. Click OK . To update the area code for specific trunks, enter the area
                                             				  code for each trunk that you want to configure in the area code field for that
                                             				  trunk. |
| Step 3 | In the Max No. of Ports field, enter the number of ports for each
                                       			 trunk that you want to configure. The Max No of Ports range goes from 1 to
                                       			 999. Note CAR uses the values that were provided for the trunk when it was added in Cisco Unified CM Administration . Therefore, some trunks will already have a zero for maximum number of ports, depending on the details that were specified
                                                      when the trunk was added in Cisco Unified CM Administration . CAR does not accept zero as a value for the maximum number of ports; you may be prompted to change the maximum number of
                                                      ports for all trunks with a value of zero. | Note | CAR uses the values that were provided for the trunk when it was added in Cisco Unified CM Administration . Therefore, some trunks will already have a zero for maximum number of ports, depending on the details that were specified
                                                      when the trunk was added in Cisco Unified CM Administration . CAR does not accept zero as a value for the maximum number of ports; you may be prompted to change the maximum number of
                                                      ports for all trunks with a value of zero. |
| Note | CAR uses the values that were provided for the trunk when it was added in Cisco Unified CM Administration . Therefore, some trunks will already have a zero for maximum number of ports, depending on the details that were specified
                                                      when the trunk was added in Cisco Unified CM Administration . CAR does not accept zero as a value for the maximum number of ports; you may be prompted to change the maximum number of
                                                      ports for all trunks with a value of zero. |
| Step 4 | To make the changes, click the Update button. You can run reports in CAR on any or all of the configured trunks. |

| Note | If you have not configured trunks in Cisco Unified CM Administration , a message displays that indicates that you have not configured trunks for the system. |
|---|---|

| Note | CAR uses the values that were provided for the trunk when it was added in Cisco Unified CM Administration . Therefore, some trunks will already have a zero for maximum number of ports, depending on the details that were specified
                                                      when the trunk was added in Cisco Unified CM Administration . CAR does not accept zero as a value for the maximum number of ports; you may be prompted to change the maximum number of
                                                      ports for all trunks with a value of zero. |
|---|---|

| Step 1 | Choose System > System
                                                					 Parameters > System
                                                					 Preferences . The System Preferences window displays. The list of available
                                          				system parameters displays in the Parameter Name list. |
|---|---|
| Step 2 | In the Parameter Value field, enter the desired value for the
                                       			 parameter as described in the following table. Table 2. System Preferences Parameter Parameter Description COMPANY_NAME Enter the company name that is used as header
                                                      						  information in reports. The company name cannot exceed 64 characters in length. | Parameter | Description | COMPANY_NAME | Enter the company name that is used as header
                                                      						  information in reports. The company name cannot exceed 64 characters in length. |
| Parameter | Description |
| COMPANY_NAME | Enter the company name that is used as header
                                                      						  information in reports. The company name cannot exceed 64 characters in length. |
| Step 3 | Click the Update button. |

| Parameter | Description |
|---|---|
| COMPANY_NAME | Enter the company name that is used as header
                                                      						  information in reports. The company name cannot exceed 64 characters in length. |