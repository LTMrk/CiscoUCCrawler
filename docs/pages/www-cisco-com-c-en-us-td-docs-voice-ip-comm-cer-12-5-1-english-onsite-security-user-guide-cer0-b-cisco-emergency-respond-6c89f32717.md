---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-12-5-1-english-onsite-security-user-guide-cer0-b-cisco-emergency-respond-6c89f32717
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/12_5_1/english/onsite_security_user/guide/cer0_b_cisco-emergency-responder-onsite-security/cer0_b_cisco-emergency-responder-onsite-security_chapter_01.html
retrieved_at: 2026-08-21T15:29:09.599576+00:00
---

Cisco Emergency Responder Onsite Security Guide for Release 12.5(1)

# Cisco Emergency Responder Onsite Security Guide for Release 12.5(1)

Updated: January 22, 2019

Chapter: Cisco Emergency
	 Responder

## Chapter: Cisco Emergency
	 Responder

# Cisco Emergency
                     	 Responder

## Cisco Emergency
                        	 Responder Overview

Cisco Emergency Responder is an emergency communication system
                           		that helps you respond to a crisis quickly and efficiently.

Emergency
                           		Responder also maintains a record of the emergency calls that your system
                           		receives so that you can access this information later.

The
                           		following is a brief overview of what happens when someone places an emergency
                           		call:

Someone places
                                 			 an emergency call.

Emergency
                                 			 Responder receives the call and forwards it to the public safety answering
                                 			 point (PSAP) for your area.

At the same
                                 			 time, Emergency Responder provides information about the emergency call in the
                                 			 Emergency Call Alert window. This information includes the time and date of the
                                 			 emergency call, the extension of the caller, the caller's alerting name, the
                                 			 ERL name, and the phone location. Additional details about the caller location,
                                 			 such as the complete physical address for the ERL and the port description, are
                                 			 displayed after you click on a call record. Depending on how your Administrator
                                 			 sets up your system your Emergency Call Alert Window may show alerts specific
                                 			 from the ERLs assigned to you. You will still have the option to view all
                                 			 alerts in the system.

Emergency
                                             				Responder displays the port description only for automatically tracked phones.
                                             				For manually configured line numbers , this field is empty.

- Depending on how your
                              		  administrator sets up your system, you may receive a voice alert that provides
                              		  you with the caller's extension. You might also receive an email with the
                              		  caller name, the Emergency Response Location (ERL) name, and the time of the
                              		  emergency call.

After you
                                 			 determine the location of the caller, you can respond to the call according to
                                 			 your company emergency response policy.

As soon as the
                                 			 caller places the emergency call, Emergency Responder refreshes the Emergency Call Alert window. If Emergency Responder
                                 			 cannot perform the real-time update, the Emergency Call Alert window refreshes in 30 seconds.

Emergency
                                             				Responder provides you with only the extension of the caller; you cannot listen
                                             				to the actual emergency call.

## Access User Web
                        	 Interface

You must
                              		  log in to Emergency Responder to view web alerts and obtain more information
                              		  about an emergency call.

To log in
                              		  to the Emergency Responder User web interface, follow these steps.

In your browser
                                       			 location field, enter the URL provided by your administrator.

Choose Cisco ER
                                          				User from the Navigation drop-down menu and click Go .

The
                                          				Cisco Emergency Responder User Login window appears.

Enter your
                                       			 username and password. Click Login . If you cannot log in, contact your system
                                       			 administrator.

The Emergency Call Alert window appears.

If you are a
                                                      				  remote user authenticated in Cisco
                                                         					 Unified Communications Manager , a notification message to change the
                                                      				  password is displayed when the expiry is due.

To exit the
                                          				Emergency Responder User web interface from any window, choose the Logout link at the top of the window.

For help with
                                                      				  using a feature on any Emergency Responder User window, choose Help > Help for this
                                                            						Screen .

## Acknowledge
                        	 Emergency Calls

After you
                              		  are notified of an emergency call, the next step is to acknowledge it. To
                              		  acknowledge an emergency call means that:

- You take responsibility to
                                 			 act according to your company emergency response policy on behalf of that call.

- You understand that your
                                 			 policy might require you to go to the physical location of the caller, or it
                                 			 might require that you monitor the emergency situation by telephone.

A red link
                                                				  indicates unacknowledged calls. A black link indicates acknowledged calls.

All security
                                                				  personnel who have access to the Emergency Responder User web interface can see
                                                				  the emergency calls on the Emergency Call Alert window.

If a call
                              		  record is removed from the list in the Emergency
                                 			 Call Alert window, Emergency Responder still saves the call
                              		  information. After an emergency call has been acknowledged, you can see the
                              		  call information by viewing the Call History. For information about how to view
                              		  the Call History, see View History of Emergency Calls .

You can also see
                              		  detailed information about that caller location by looking up the phone
                              		  extension. For information about viewing details about a caller location, see
                              		  Emergency Call Information.

### Before you begin

This
                              		  procedure assumes that you are logged in to Emergency Responder and that the Emergency
                                 			 Call Alert window is displayed.

For
                              		  instructions on logging in to Emergency Responder, see the Access User Web Interface .

To display
                              		  the Emergency
                                 			 Call Alert window from any page on the Emergency Responder User
                              		  website, choose Web
                                 			 Alert .

To
                              		  acknowledge an emergency call and remove the emergency call from the list,
                              		  follow these steps:

In the Emergency
                                          				Call Alert window, click ACKNOWLEDGE for the emergency call you want to
                                       			 acknowledge.

Click OK .

## View Emergency
                        	 Calls

To view all
                              		  emergency calls, click Find without entering any criteria.

To narrow your
                              		  search, follow these steps.

Select the
                                       			 field you want to search, select the search relationship, and enter the search
                                       			 string.

To search a
                                          				combination of fields, follow these steps:

- Click More to add additional search fields.

- Select Any at the top of the list to display calls that
                                          				match any search criteria (an OR search).

- Select All to list only calls that match every criteria (an
                                          				AND search).

- Click Fewer to remove the search criterion at the bottom
                                          				of the list. You can view this button only after you click More .

From the
                                       			 drop-down list, choose the number of records per page to be displayed for each
                                       			 search.

After you
                                       			 enter the search criteria, click Find .

### Emergency Call
                           	 Information

To
                                 		  respond to an emergency call, you might need more information than is displayed
                                 		  on the Emergency Call Alert window, or you might need to
                                 		  provide these details to law enforcement or other emergency personnel.

You can
                                 		  click on a call record in the Emergency Call Alert window to view details about a call.

The
                                 		  system administrator sets the displayed fields, such as the street address and
                                 		  the three-digit area code. The PSAP operator also sees these displayed fields.

These
                                 		  details might not describe the exact physical location of the caller, but they
                                 		  should describe the origin of the emergency call. If you find that these
                                 		  details are not helpful in locating the emergency caller, contact your system
                                 		  administrator.

For additional
                                 		  information, see View History of Emergency Calls .

The
                                 		  following table describes the fields you see after you click on a call record
                                 		  from the Emergency Call Alert window.

Field Name

Description

ERL Name

Zone name
                                             					 for the call location set by your system administrator.

House
                                             					 Number

Number
                                             					 from the postal street address for the building.

For
                                             					 example, the 170 in 170 West Tasman Drive.

House
                                             					 Number Suffix

Number
                                             					 extension for the house number, if any.

For
                                             					 example /2.

Street
                                             					 Name

Street
                                             					 name from the postal address for the building.

Street
                                             					 Suffix

Type of
                                             					 street.

For
                                             					 example AV for Avenue.

Prefix
                                             					 Directional

Leading
                                             					 directional indicator if the street name contains one.

For
                                             					 example N for North.

Post
                                             					 Directional

Trailing
                                             					 directional indicator if the street name contains one.

For
                                             					 example N for North.

Community
                                             					 Name

Community
                                             					 name for the address.

For
                                             					 example a city, town, or district name.

State

Two-digit
                                             					 state abbreviation.

Main NPA

Three-digit area code of the main number associated with the
                                             					 calling number.

Customer
                                             					 Name

Subscriber
                                             					 name associated with the ERL.

This is
                                             					 typically your company name.

Class of
                                             					 Service

Class of
                                             					 service for the ERL.

Type of
                                             					 Service

Type of
                                             					 service for the ERL.

Exchange

Local
                                             					 Exchange Carrier (LEC) exchange identifier for the serving telephone office for
                                             					 the phone.

Main
                                             					 Telephone No.

Main phone
                                             					 number associated with the ERL, such as the number of the security office for
                                             					 the ERL.

Order
                                             					 Number

Service
                                             					 order number for establishing or updating this record.

Extract
                                             					 Date

Date this
                                             					 record is created.

County ID

County
                                             					 identification code for the zone.

In the
                                             					 United States, use the Federal Information Processing Standard (FIPS) code
                                             					 assigned to the county by the U.S. Census Bureau.

Company
                                             					 ID

Your
                                             					 National Emergency Number Association (NENA)-registered company identification
                                             					 code.

Zip Code

Postal
                                             					 zip code for the address.

Zip Code
                                             					 Extension

Postal
                                             					 zip code plus four numbers.

Customer
                                             					 Code

Your
                                             					 customer code.

If you
                                             					 do not know your customer code, contact your service provider.

Comments

Optional
                                             					 comments, which might be displayed at the PSAP if an emergency call is placed
                                             					 from this ERL.

Longitude

Longitude of the ERL.

Latitude

Latitude
                                             					 of the ERL.

Elevation

Elevation of the ERL.

TAR Code

Taxing
                                             					 area rate code.

Location

Additional location information, in free form, to help identify
                                             					 the exact location of the phone.

For
                                             					 example, this information might repeat the street address that is defined in
                                             					 several separate fields elsewhere in the Emergency Call Alert window.

## View Emergency Call Alert

The Emergency Call Alert page displays a list of emergency calls, with the following fields for each call:

System Call Time

Local Call Time

Line ID

Caller’s Name

ERL

ELIN Used

Location

Street

Phone Location

You need user or system administrator authority to access the Emergency Call Alert window. Java Runtime Environment (JRE) must be installed on your machine to monitor web alerts.

Use the following procedure to view the Emergency Call Alert window.

In the Cisco Emergency Responder User window, click Web Alert .

You may see specific alerts from ERLs assigned to you, depending on how your administrator has set up the system. Click All to view all the alerts in the system.

To view the Call Details window, click on a call record.

The Call Details window appears. For additional information about the displayed fields, see Emergency Call Information .

## Use Phone
                        	 Search

If you
                              		  need to see location details about a call that is no longer visible in the Emergency
                                 			 Call Alert window, use the phone search to look up the extension. If
                              		  you do not know the caller extension number, you can find it in the Call
                                 			 History window. For information about how to view a call history,
                              		  see View History of Emergency Calls .

You can perform
                                          			 both partial string searches and E.164 Dial Plans searches with Phone Search.
                                          			 If you are searching E.164 Dial Plans then a plus sign (+) should come before
                                          			 the number.

- If an emergency call is
                                             				placed immediately after the Emergency Responder server is started, the caller
                                             				location details might not be available right away. Results of a phone search
                                             				using this caller extension say No
                                                				  matching phone for the given extension .

A caller might
                                                				  place an emergency call from one Emergency Response Location (ERL) and then
                                                				  immediately move to a different ERL. If Emergency Responder registers this move
                                                				  before you use the Phone Search feature, the phone search window displays the
                                                				  location details of the second ERL.

If you try to
                                                				  view location details for a phone that shares an extension, the phone search
                                                				  window displays details for all phones for that extension. To refine your
                                                				  search, click Select a phone to view details . Choose the phone
                                                				  whose details you want to view based on the Last
                                                   					 Time of Emergency Call field.

Use the
                              		  following procedure to perform a phone search.

Choose Phone
                                          				Search from the main menu.

In the Phone
                                          				Extension field, enter the extension of the caller about whom you
                                       			 want more information and click Find .

For additional
                                          				information, see Emergency call information.

To return to the Emergency Call Alert window, choose Web
                                             				  Alert from the main menu.

## Locate Phone by
                        	 Extension

Use the Locate
                                 			 Phone by Extension page to search the Call History for a phone by an
                              		  extension number. If a phone is located, the results show the Call Details.

You
                                          			 need user or system administrator authority to perform a Phone Search.

Perform the
                              		  following steps to search for a phone by an extension number.

In the Emergency Call Alert window, click Phone
                                          				Search .

The
                                          				following table describes the Locate Phone by Extension page.

Field
                                                      						  and Button

Description

Phone Extension

Text box into which you enter the extension of the phone
                                                      						  that you want to locate.

You can perform a partial string search of the extension.

Find
                                                      						  button

Starts
                                                      						  the phone search.

Enter a phone
                                       			 extension in the Phone
                                          				Extension field.

Click Find

The search
                                          				results are displayed.

## View History of
                        	 Emergency Calls

Emergency
                              		  Responder maintains history records for 10,000 most recent emergency calls.

You can
                              		  use this information to track specific details about emergency calls, such as
                              		  how many emergency calls were placed on a date, from a caller, or that contain
                              		  a specific keyword. This information can also be used for reporting purposes or
                              		  to set staffing levels. For example, you could use this information to
                              		  determine the number of on-site-alert personnel needed for a time period.

You can also use
                              		  this feature to provide recent call-history information to law enforcement
                              		  agencies or to other emergency personnel.

If
                              		  needed, you can enter or view additional information about an emergency call in
                              		  the Comments field.

If you need to
                                          			 obtain call details for earlier emergency calls, ask your system administrator
                                          			 to provide this information. Your system administrator may have saved these
                                          			 records.

To view
                              		  Call History, follow these steps:

Choose Call
                                          				History from the main menu.

Use the
                                       			 drop-down lists and text field to enter specific call-search conditions. Click More to add conditions, or click Fewer to remove the last condition that you added.

If you specify
                                                      				  more than one call-search condition, you must indicate if you want all or any
                                                      				  of the conditions satisfied. For example, if you want to view all medical
                                                      				  emergency calls that came from your company office in San Jose on July 6, your
                                                      				  conditions might look like this:

Find Details of calls where
                                                         					 all of the conditions are satisfied and where Date is 07/06/2013 and where ERL
                                                         					 Name is Exactly SanJose Building and Comments contains medical.

Click Find .

Information
                                          				appears about those calls that meet the specified search conditions.

If the
                                          				information does not fit in one window, Emergency Responder uses more than one
                                          				window to list the calls.

To see more
                                          				information, click the links or enter a specific page number in the Page field and click the Page link.

To enter or
                                       			 modify comments about an emergency call, click the Edit
                                          				Link in the Comments field for that call record.

The Call
                                             				  Details window appears.

Comments appear
                                          				in the Comments About the Call field of the Call
                                             				  Details window:

- If the comment is longer than
                                          				the field, use the right and left arrow keys on your computer keyboard to
                                          				scroll through the comment.

- To add or modify a comment,
                                          				enter the information and click Update .

- To return a comment to its
                                          				last saved value, click Reset .

Click Close to close the Call
                                          				Details window.

### Call History
                           	 Fields

The Call
                                    			 History page appears when you select Call
                                    			 History .

#### Authorization Requirements

You
                                 		  need user or system administrator authority to access this page.

#### Description

Use the Call
                                    			 History page to view the history of emergency calls that were made
                                 		  from your network.

The
                                 		  following table describes the Call
                                    			 History page.

Button
                                             					 or Field

Description

Search
                                             					 criteria

Allows
                                             					 you to enter search criteria to select the emergency calls you want to view.

Call
                                             					 records

Provides
                                             					 a list of emergency calls that match your search criteria:

- ERL Name - Click the name
                                                						to view details about the emergency response location (ERL).

- Caller’s Extension - The
                                                						extension used to place the emergency call.

Caller’s name - The alerting name of the caller.

- Time - The time the call
                                                						is made.

- Date - The date the call
                                                						is made.

- ELIN Used - The route
                                                						pattern and Emergency Location Identification Number (ELIN) combination used
                                                						for the call.

- Location - The phone
                                                						location, based on whether the phone is configured manually, or if it's
                                                						configured automatically based on the switch port or IP subnet.

- Call Acknowledged - The
                                                						acknowledged status of a call on the Web Alert page.

- Acknowledged By - The ID
                                                						of the user who acknowledged the call.

- Time Acknowledged - The
                                                						time that the call is acknowledged.

- Date Acknowledged - The
                                                						date that the call is acknowledged.

Click the First , Previous , Next , and Last links to move between pages

Enter a specific page number in the Page field and press Enter to move to that page

Update

Click Update to include your comments in the call history
                                             					 for the call.

You
                                                         						can only perform this action from the Call Details page.

Reset

Click Reset to remove unsaved comments. You can then
                                             					 reenter comments.

You
                                                         						can only perform this action from the Call Details page.

Close

Click Close to close the Call Details page.

You
                                                         						can only perform this action from the Call Details page.

The following
                                 		  table describes the fields you see when you view a history of emergency calls.

Field
                                             					 name

Description

ERL Name

Zone
                                             					 name that your system administrator set for that call location.

Caller’s
                                             					 Extension

Extension from which the emergency call is placed.

Caller’s
                                             					 Name

Alerting
                                             					 name set on Unified Communications Manager for the caller.

Time

Time
                                             					 that the emergency call is placed.

Date

Date
                                             					 that the emergency call is placed.

ELIN
                                             					 Used

Call-back number your PSAP operator uses to contact an emergency
                                             					 caller if the emergency call gets disconnected.

Location

The
                                             					 phone location, based on whether the phone is configured manually, or if it's
                                             					 configured automatically based on the switch port or IP subnet.

Call
                                             					 Acknowledged

The
                                             					 acknowledged status of a call on the Web Alert window.

Acknowledged By

The ID
                                             					 of the user who acknowledged the call.

Time
                                             					 Acknowledged

The time
                                             					 that the call is acknowledged.

Date
                                             					 Acknowledged

The date
                                             					 that the call is acknowledged.

Comments

This
                                             					 field that contains an Edit Link that allows you to enter comments about
                                             					 the call. See View History of Emergency Calls for details about entering
                                             					 comments.

| Note | Emergency
                                             				Responder displays the port description only for automatically tracked phones.
                                             				For manually configured line numbers , this field is empty. |
|---|---|

| Note | Emergency
                                             				Responder provides you with only the extension of the caller; you cannot listen
                                             				to the actual emergency call. |
|---|---|

| Step 1 | In your browser
                                       			 location field, enter the URL provided by your administrator. The main
                                       			 Emergency Responder User web interface appears. |
|---|---|
| Step 2 | Choose Cisco ER
                                          				User from the Navigation drop-down menu and click Go . The
                                          				Cisco Emergency Responder User Login window appears. |
| Step 3 | Enter your
                                       			 username and password. Click Login . If you cannot log in, contact your system
                                       			 administrator. The Emergency Call Alert window appears. Note If you are a
                                                      				  remote user authenticated in Cisco
                                                         					 Unified Communications Manager , a notification message to change the
                                                      				  password is displayed when the expiry is due. To exit the
                                          				Emergency Responder User web interface from any window, choose the Logout link at the top of the window. Tip For help with
                                                      				  using a feature on any Emergency Responder User window, choose Help > Help for this
                                                            						Screen . | Note | If you are a
                                                      				  remote user authenticated in Cisco
                                                         					 Unified Communications Manager , a notification message to change the
                                                      				  password is displayed when the expiry is due. | Tip | For help with
                                                      				  using a feature on any Emergency Responder User window, choose Help > Help for this
                                                            						Screen . |
| Note | If you are a
                                                      				  remote user authenticated in Cisco
                                                         					 Unified Communications Manager , a notification message to change the
                                                      				  password is displayed when the expiry is due. |
| Tip | For help with
                                                      				  using a feature on any Emergency Responder User window, choose Help > Help for this
                                                            						Screen . |

| Note | If you are a
                                                      				  remote user authenticated in Cisco
                                                         					 Unified Communications Manager , a notification message to change the
                                                      				  password is displayed when the expiry is due. |
|---|---|

| Tip | For help with
                                                      				  using a feature on any Emergency Responder User window, choose Help > Help for this
                                                            						Screen . |
|---|---|

| Note | A red link
                                                				  indicates unacknowledged calls. A black link indicates acknowledged calls. All security
                                                				  personnel who have access to the Emergency Responder User web interface can see
                                                				  the emergency calls on the Emergency Call Alert window. |
|---|---|

| Step 1 | In the Emergency
                                          				Call Alert window, click ACKNOWLEDGE for the emergency call you want to
                                       			 acknowledge. A message
                                       			 appears and prompts you to confirm your acknowledgment. |
|---|---|
| Step 2 | Click OK . Emergency
                                       			 Responder refreshes the Emergency
                                          				Call Alert window and the Emergency
                                          				Call Alert window of all on-site-alert personnel in your system,
                                       			 removing the call you just acknowledged. |

| Step 1 | Select the
                                       			 field you want to search, select the search relationship, and enter the search
                                       			 string. To search a
                                          				combination of fields, follow these steps: Click More to add additional search fields. Select Any at the top of the list to display calls that
                                          				match any search criteria (an OR search). Select All to list only calls that match every criteria (an
                                          				AND search). Click Fewer to remove the search criterion at the bottom
                                          				of the list. You can view this button only after you click More . |
|---|---|
| Step 2 | From the
                                       			 drop-down list, choose the number of records per page to be displayed for each
                                       			 search. |
| Step 3 | After you
                                       			 enter the search criteria, click Find . |

| Field Name | Description |
|---|---|
| ERL Name | Zone name
                                             					 for the call location set by your system administrator. |
| House
                                             					 Number | Number
                                             					 from the postal street address for the building. For
                                             					 example, the 170 in 170 West Tasman Drive. |
| House
                                             					 Number Suffix | Number
                                             					 extension for the house number, if any. For
                                             					 example /2. |
| Street
                                             					 Name | Street
                                             					 name from the postal address for the building. |
| Street
                                             					 Suffix | Type of
                                             					 street. For
                                             					 example AV for Avenue. |
| Prefix
                                             					 Directional | Leading
                                             					 directional indicator if the street name contains one. For
                                             					 example N for North. |
| Post
                                             					 Directional | Trailing
                                             					 directional indicator if the street name contains one. For
                                             					 example N for North. |
| Community
                                             					 Name | Community
                                             					 name for the address. For
                                             					 example a city, town, or district name. |
| State | Two-digit
                                             					 state abbreviation. |
| Main NPA | Three-digit area code of the main number associated with the
                                             					 calling number. |
| Customer
                                             					 Name | Subscriber
                                             					 name associated with the ERL. This is
                                             					 typically your company name. |
| Class of
                                             					 Service | Class of
                                             					 service for the ERL. |
| Type of
                                             					 Service | Type of
                                             					 service for the ERL. |
| Exchange | Local
                                             					 Exchange Carrier (LEC) exchange identifier for the serving telephone office for
                                             					 the phone. |
| Main
                                             					 Telephone No. | Main phone
                                             					 number associated with the ERL, such as the number of the security office for
                                             					 the ERL. |
| Order
                                             					 Number | Service
                                             					 order number for establishing or updating this record. |
| Extract
                                             					 Date | Date this
                                             					 record is created. |
| County ID | County
                                             					 identification code for the zone. In the
                                             					 United States, use the Federal Information Processing Standard (FIPS) code
                                             					 assigned to the county by the U.S. Census Bureau. |
| Company
                                             					 ID | Your
                                             					 National Emergency Number Association (NENA)-registered company identification
                                             					 code. |
| Zip Code | Postal
                                             					 zip code for the address. |
| Zip Code
                                             					 Extension | Postal
                                             					 zip code plus four numbers. |
| Customer
                                             					 Code | Your
                                             					 customer code. If you
                                             					 do not know your customer code, contact your service provider. |
| Comments | Optional
                                             					 comments, which might be displayed at the PSAP if an emergency call is placed
                                             					 from this ERL. |
| Longitude | Longitude of the ERL. |
| Latitude | Latitude
                                             					 of the ERL. |
| Elevation | Elevation of the ERL. |
| TAR Code | Taxing
                                             					 area rate code. |
| Location | Additional location information, in free form, to help identify
                                             					 the exact location of the phone. For
                                             					 example, this information might repeat the street address that is defined in
                                             					 several separate fields elsewhere in the Emergency Call Alert window. |

| Note | You need user or system administrator authority to access the Emergency Call Alert window. Java Runtime Environment (JRE) must be installed on your machine to monitor web alerts. |
|---|---|

| Step 1 | In the Cisco Emergency Responder User window, click Web Alert . The Emergency Call Alert window appears. |
|---|---|
| Step 2 | You may see specific alerts from ERLs assigned to you, depending on how your administrator has set up the system. Click All to view all the alerts in the system. |
| Step 3 | To view the Call Details window, click on a call record. The Call Details window appears. For additional information about the displayed fields, see Emergency Call Information . |

| Note | You can perform
                                          			 both partial string searches and E.164 Dial Plans searches with Phone Search.
                                          			 If you are searching E.164 Dial Plans then a plus sign (+) should come before
                                          			 the number. |
|---|---|

| Tip | If an emergency call is
                                             				placed immediately after the Emergency Responder server is started, the caller
                                             				location details might not be available right away. Results of a phone search
                                             				using this caller extension say No
                                                				  matching phone for the given extension . A caller might
                                                				  place an emergency call from one Emergency Response Location (ERL) and then
                                                				  immediately move to a different ERL. If Emergency Responder registers this move
                                                				  before you use the Phone Search feature, the phone search window displays the
                                                				  location details of the second ERL. If you try to
                                                				  view location details for a phone that shares an extension, the phone search
                                                				  window displays details for all phones for that extension. To refine your
                                                				  search, click Select a phone to view details . Choose the phone
                                                				  whose details you want to view based on the Last
                                                   					 Time of Emergency Call field. |
|---|---|

| Step 1 | Choose Phone
                                          				Search from the main menu. The Locate
                                          				Phone by Extension window appears. |
|---|---|
| Step 2 | In the Phone
                                          				Extension field, enter the extension of the caller about whom you
                                       			 want more information and click Find . For additional
                                          				information, see Emergency call information. To return to the Emergency Call Alert window, choose Web
                                             				  Alert from the main menu. Detailed
                                       			 information about the caller appears at the bottom of the window. |

| Note | You
                                          			 need user or system administrator authority to perform a Phone Search. |
|---|---|

| Step 1 | In the Emergency Call Alert window, click Phone
                                          				Search . The Locate
                                          				Phone By Extension window appears. The
                                          				following table describes the Locate Phone by Extension page. Table 2. Locate
                                                				Phone by Extension Page Field
                                                      						  and Button Description Phone Extension Text box into which you enter the extension of the phone
                                                      						  that you want to locate. You can perform a partial string search of the extension. Find
                                                      						  button Starts
                                                      						  the phone search. | Field
                                                      						  and Button | Description | Phone Extension | Text box into which you enter the extension of the phone
                                                      						  that you want to locate. You can perform a partial string search of the extension. | Find
                                                      						  button | Starts
                                                      						  the phone search. |
|---|---|---|---|---|---|---|---|
| Field
                                                      						  and Button | Description |
| Phone Extension | Text box into which you enter the extension of the phone
                                                      						  that you want to locate. You can perform a partial string search of the extension. |
| Find
                                                      						  button | Starts
                                                      						  the phone search. |
| Step 2 | Enter a phone
                                       			 extension in the Phone
                                          				Extension field. |
| Step 3 | Click Find The search
                                          				results are displayed. |

| Field
                                                      						  and Button | Description |
|---|---|
| Phone Extension | Text box into which you enter the extension of the phone
                                                      						  that you want to locate. You can perform a partial string search of the extension. |
| Find
                                                      						  button | Starts
                                                      						  the phone search. |

| Tip | If you need to
                                          			 obtain call details for earlier emergency calls, ask your system administrator
                                          			 to provide this information. Your system administrator may have saved these
                                          			 records. |
|---|---|

| Step 1 | Choose Call
                                          				History from the main menu. The Call
                                          				History window appears. |
|---|---|
| Step 2 | Use the
                                       			 drop-down lists and text field to enter specific call-search conditions. Click More to add conditions, or click Fewer to remove the last condition that you added. Note If you specify
                                                      				  more than one call-search condition, you must indicate if you want all or any
                                                      				  of the conditions satisfied. For example, if you want to view all medical
                                                      				  emergency calls that came from your company office in San Jose on July 6, your
                                                      				  conditions might look like this: Find Details of calls where
                                                         					 all of the conditions are satisfied and where Date is 07/06/2013 and where ERL
                                                         					 Name is Exactly SanJose Building and Comments contains medical. | Note | If you specify
                                                      				  more than one call-search condition, you must indicate if you want all or any
                                                      				  of the conditions satisfied. For example, if you want to view all medical
                                                      				  emergency calls that came from your company office in San Jose on July 6, your
                                                      				  conditions might look like this: Find Details of calls where
                                                         					 all of the conditions are satisfied and where Date is 07/06/2013 and where ERL
                                                         					 Name is Exactly SanJose Building and Comments contains medical. |
| Note | If you specify
                                                      				  more than one call-search condition, you must indicate if you want all or any
                                                      				  of the conditions satisfied. For example, if you want to view all medical
                                                      				  emergency calls that came from your company office in San Jose on July 6, your
                                                      				  conditions might look like this: Find Details of calls where
                                                         					 all of the conditions are satisfied and where Date is 07/06/2013 and where ERL
                                                         					 Name is Exactly SanJose Building and Comments contains medical. |
| Step 3 | Click Find . Information
                                          				appears about those calls that meet the specified search conditions. If the
                                          				information does not fit in one window, Emergency Responder uses more than one
                                          				window to list the calls. To see more
                                          				information, click the links or enter a specific page number in the Page field and click the Page link. |
| Step 4 | To enter or
                                       			 modify comments about an emergency call, click the Edit
                                          				Link in the Comments field for that call record. The Call
                                             				  Details window appears. Comments appear
                                          				in the Comments About the Call field of the Call
                                             				  Details window: If the comment is longer than
                                          				the field, use the right and left arrow keys on your computer keyboard to
                                          				scroll through the comment. To add or modify a comment,
                                          				enter the information and click Update . To return a comment to its
                                          				last saved value, click Reset . |
| Step 5 | Click Close to close the Call
                                          				Details window. |

| Note | If you specify
                                                      				  more than one call-search condition, you must indicate if you want all or any
                                                      				  of the conditions satisfied. For example, if you want to view all medical
                                                      				  emergency calls that came from your company office in San Jose on July 6, your
                                                      				  conditions might look like this: Find Details of calls where
                                                         					 all of the conditions are satisfied and where Date is 07/06/2013 and where ERL
                                                         					 Name is Exactly SanJose Building and Comments contains medical. |
|---|---|

| Button
                                             					 or Field | Description |
|---|---|
| Search
                                             					 criteria | Allows
                                             					 you to enter search criteria to select the emergency calls you want to view. |
| Call
                                             					 records | Provides
                                             					 a list of emergency calls that match your search criteria: ERL Name - Click the name
                                                						to view details about the emergency response location (ERL). Caller’s Extension - The
                                                						extension used to place the emergency call. Caller’s name - The alerting name of the caller. Time - The time the call
                                                						is made. Date - The date the call
                                                						is made. ELIN Used - The route
                                                						pattern and Emergency Location Identification Number (ELIN) combination used
                                                						for the call. Location - The phone
                                                						location, based on whether the phone is configured manually, or if it's
                                                						configured automatically based on the switch port or IP subnet. Call Acknowledged - The
                                                						acknowledged status of a call on the Web Alert page. Acknowledged By - The ID
                                                						of the user who acknowledged the call. Time Acknowledged - The
                                                						time that the call is acknowledged. Date Acknowledged - The
                                                						date that the call is acknowledged. Comments - All comments
                                                						entered about the call. Click Edit to enter or change comments about the call in
                                                						the Call Details page. If a large number of calls match
                                                						your search criteria, Emergency Responder uses several pages to display them: Click the First , Previous , Next , and Last links to move between pages Enter a specific page number in the Page field and press Enter to move to that page |
| Update | Click Update to include your comments in the call history
                                             					 for the call. Note You
                                                         						can only perform this action from the Call Details page. | Note | You
                                                         						can only perform this action from the Call Details page. |
| Note | You
                                                         						can only perform this action from the Call Details page. |
| Reset | Click Reset to remove unsaved comments. You can then
                                             					 reenter comments. Note You
                                                         						can only perform this action from the Call Details page. | Note | You
                                                         						can only perform this action from the Call Details page. |
| Note | You
                                                         						can only perform this action from the Call Details page. |
| Close | Click Close to close the Call Details page. Note You
                                                         						can only perform this action from the Call Details page. | Note | You
                                                         						can only perform this action from the Call Details page. |
| Note | You
                                                         						can only perform this action from the Call Details page. |

| Note | You
                                                         						can only perform this action from the Call Details page. |
|---|---|

| Note | You
                                                         						can only perform this action from the Call Details page. |
|---|---|

| Note | You
                                                         						can only perform this action from the Call Details page. |
|---|---|

| Field
                                             					 name | Description |
|---|---|
| ERL Name | Zone
                                             					 name that your system administrator set for that call location. |
| Caller’s
                                             					 Extension | Extension from which the emergency call is placed. |
| Caller’s
                                             					 Name | Alerting
                                             					 name set on Unified Communications Manager for the caller. |
| Time | Time
                                             					 that the emergency call is placed. |
| Date | Date
                                             					 that the emergency call is placed. |
| ELIN
                                             					 Used | Call-back number your PSAP operator uses to contact an emergency
                                             					 caller if the emergency call gets disconnected. |
| Location | The
                                             					 phone location, based on whether the phone is configured manually, or if it's
                                             					 configured automatically based on the switch port or IP subnet. |
| Call
                                             					 Acknowledged | The
                                             					 acknowledged status of a call on the Web Alert window. |
| Acknowledged By | The ID
                                             					 of the user who acknowledged the call. |
| Time
                                             					 Acknowledged | The time
                                             					 that the call is acknowledged. |
| Date
                                             					 Acknowledged | The date
                                             					 that the call is acknowledged. |
| Comments | This
                                             					 field that contains an Edit Link that allows you to enter comments about
                                             					 the call. See View History of Emergency Calls for details about entering
                                             					 comments. |