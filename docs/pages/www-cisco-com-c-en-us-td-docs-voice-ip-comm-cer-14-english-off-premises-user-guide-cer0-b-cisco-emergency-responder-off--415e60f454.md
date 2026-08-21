---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-14-english-off-premises-user-guide-cer0-b-cisco-emergency-responder-off--415e60f454
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/14/english/off-premises_user/guide/cer0_b_cisco-emergency-responder-off-premise-guide-1401/cer0_b_cisco-emergency-responder-off-premise-guide-1251SU2_chapter_01.html
retrieved_at: 2026-08-21T15:28:23.251874+00:00
---

Cisco Emergency Responder Off-Premise Location Management User Guide Release 14

# Cisco Emergency Responder Off-Premise Location Management User Guide Release 14

Updated: March 31, 2021

Chapter: Off-Premise
	 Support for IP Phones

## Chapter: Off-Premise
	 Support for IP Phones

# Off-Premise
                     	 Support for IP Phones

## Off-Premise
                        	 Support for IP Phones Overview

The Cisco
                              		  Emergency Responder Off-Premises User page allows you to verify the
                           		status of your phone and the directory number assigned to that phone. A phone
                           		can be:

The phone is
                                 				on the corporate network. Your administrator specifies a location that you
                                 				cannot change.

The phone is
                                 				outside of the corporate network. You must enter your address in the location
                                 				page and associate a location to the phone.

The phone is
                                 				registered and assigned an Emergency Response Location (ERL), but a location is
                                 				not associated to the phone. Contact your administrator for more information.

The phone is
                                 				not registered or Emergency Responder cannot discover the phone location, and
                                 				the phone is not assigned an ERL. Contact your administrator for more
                                 				information.

Complete the
                           		following tasks if you want to associate a location to an off-premises phone:

On the Configured Locations page, enter and validate your
                                 			 location.

On the Location Associations page, associate your location
                                 			 to your directory number.

After you associate
                           		a directory number to your address, you can make emergency calls from that
                           		phone and you can receive emergency services at that location.

You may be required
                           		to confirm or update your off-premises location. If this is the case, your
                           		phone displays your current off-premises location and you can select another
                           		off-premises location that is set up on the Cisco
                              		  Emergency Responder Off-Premises User page. You must keep your
                           		off-premises location up to date to place emergency calls and receive emergency
                           		services at your off-premises location.

## Confirm and Update
                        	 an Off-Premise Location with the Phone Display

You can confirm
                              		  and update an off-premises location using your phone display if you have
                              		  upgraded to Cisco Unified Communications Manager 9.0 and Cisco Emergency
                              		  Responder 9.0 and later. If your phone supports this feature, when the phone
                              		  registers a screen appears for you to confirm or update your off-premises
                              		  location.

Your
                              		  administrator must configure your phone as off-premises in Cisco Emergency
                              		  Responder, and your company must allow the off-premises location update before
                              		  you can use the off-premises phone.

If you close
                                          			 the phone display before you confirm or update a location, you can return to
                                          			 the display by selecting Running Applications from the Services menu or by
                                          			 resetting the phone.

For list of supported phones, see the Cisco Emergency Responder Release Notes .

Connect and
                                       			 register your phone through an off-premises location.

Perform one
                                       			 of the following actions:

- Select Next on the phone. A list of phone locations is
                                          				displayed. Go to Step 3.

- Select Reject . The phone registration is completed. The
                                          				outgoing facility may not be available depending on the policy enforcement.

Perform one of
                                       			 the following actions:

- Select a location from the
                                          				displayed list. Go to Step 4.

The phone
                                             				  display shows the procedure for adding a new location. For additional
                                             				  information on adding a new location, see the Related Topics section below.
                                             				  Once you have added a new location, select it by choosing the new location from
                                             				  the displayed list. If the new location is not displayed, select Refresh .

- Select Refresh . The list of phone locations refreshes and
                                          				your new locations display.

Select Exit on the Confirmation message screen. Phone
                                       			 registration is completed. Use the phone normally.

## Access Cisco
                        	 Emergency Responder Off-Premises User Page

To access
                              		  the Cisco
                                 			 Emergency Responder Off-Premises User page, follow these steps.

Obtain the User
                                       			 Options URL, the name that identifies the Emergency Responder Off-Premises user
                                       			 in the Navigation drop-down box, the user ID, and the default password from
                                       			 your system administrator.

### Example:

User Options
                                          				URL: <http://server_name/ccmuser/logon.asp>, where server_name is the
                                          				host on which the web server is installed (the host is usually the same IP
                                          				address or name as the CiscoUnified Communications Manager server).

User ID:
                                          				<your user ID>

Default
                                          				Password: <your password>

Open a web
                                       			 browser on your computer, enter the URL (provided by your system
                                       			 administrator), and log in.

If you are a
                                                      				  remote user authenticated in Cisco
                                                         					 Unified Communications Manager , a notification message to change the
                                                      				  password is displayed when the expiry is due.

If you are
                                       			 prompted to accept security settings, click Yes or Install
                                          				Certificate .

The Cisco
                                             				  Unified Communications Manager User Options page appears.

Choose the Emergency
                                          				Responder Off-Premises User page from the Navigation drop-down list
                                       			 in the top right corner. If this page is not listed in the drop-down menu,
                                       			 contact your system administrator.

The Cisco
                                             				  Emergency Responder Off-Premises User page appears.

## Location
                        	 Fields

Cisco Emergency
                              		  Responder requires that you enter locations in the correct format. Review the
                              		  information in the following table before you add or update a location,
                              		  including the information in the Value Type column and any limitations noted in
                              		  the Description column.

(A =
                                          					 Alphabets, N = Numeric, S = Special Characters [# @ & * ( ) - _ + , . : ; "
                                          					 ' /] )

Location
                                          					 Name

This name
                                          					 is used to identify the address associated to your phone.

A

House
                                          					 Number

The number
                                          					 from the postal street address for the building. For example, 170 in 170 West
                                          					 Tasman Dr.

AN
                                          					 -(hyphen)

Prefix
                                          					 Directional

A leading
                                          					 directional indicator, if the street name contains one. For example, N for
                                          					 North.

N

S

E

W

NE

NW

SE

SW

Street
                                          					 Suffix

The street
                                          					 type.

Select the
                                          					 type from the drop-down list; the field is filled with one of the abbreviations
                                          					 accepted by the United States Postal Service Publication 28.

For
                                          					 example, AVE for Avenue.

A

You can
                                          					 also type in the suffix. You are limited to 4 characters.

Location

Additional
                                          					 location information used to identify the location of the phone.

ANS

You are
                                          					 limited to 60 characters.

State

The
                                          					 two-digit state abbreviation.

A

You are
                                          					 limited to 2 characters.

Zip Code

The postal
                                          					 zip code for the address.

AN -
                                          					 (Hyphen)

House
                                          					 Number Suffix

The number
                                          					 extension for the house number.

For
                                          					 example, /2.

ANS

Street
                                          					 Name

The
                                          					 street name from the postal address for the building. You are limited to 60
                                          					 characters.

ANS

Post
                                          					 Directional

A
                                          					 trailing directional indicator if the street name contains one.

For
                                          					 example, N for North.

N

S

E

W

NE

NW

SE

SW

Community
                                          					 Name

The
                                          					 community name for the address, for example, a city, town, or district name.

ANS

You are
                                          					 limited to 32 characters.

Time Zone

Select a time zone for the Emergency Response Location (ERL). The time zone can be selected from the drop-down containing
                                          all the available time zones.

When a 911 call is placed from a phone tracked under this ERL, the Email, Web, and Pager alert indicates a local call time
                                          based on the time zone set for the ERL. If the time zone is not selected, the CER Server time is displayed.

ANS

Zip Code
                                          					 Extension

The postal zip code plus four numbers.

AN -
                                          					 (Hyphen)

You are
                                          					 limited to 4 characters.

### Add New
                           	 Location

Before
                                 		  you can associate a location to a phone, you must first enter the location into
                                 		  Emergency Responder. When you have multiple locations, you must have a unique
                                 		  name to identify each unique location.

To add a
                                 		  location to Emergency Responder, follow these steps.

#### Before you begin

Cisco Emergency
                                 		  Responder requires that you enter locations in the correct format. Review the
                                 		  Location Fields section before you add a new location.

From the Cisco
                                             				Emergency Responder Off-Premises User page, choose Location . The Configured Locations page appears.

Click Add
                                             				New Locations .

Enter your
                                          			 Preferred Location Name in the mandatory field. Use this name to identify this
                                          			 address when you associate your phone with this address.

Enter your
                                          			 House Number in the mandatory field.

Enter your
                                          			 Street Name in the mandatory field.

Enter your
                                          			 Community Name in the mandatory field.

Enter your
                                          			 State in the mandatory field.

Enter your Time Zone in the optional field. The Time Zone lists all the available time zones.

When you dial 911, the selected time zone is set as the local call time in the Pager and Emergency Alerts. If a time zone
                                                         is not selected, then the local call time is same as the system call time.

Enter your Zip
                                          			 Code in the mandatory field.

Click Save .

To validate
                                          			 your address, click Validate .

### Update Your
                           	 Location

When you
                                 		  have an existing location record, you can just update the information for that
                                 		  one record.

Before
                                 		  you can associate a location to a phone, you must first enter the location into
                                 		  Emergency Responder. When you have multiple locations, you must have a unique
                                 		  name to identify each unique location.

To update
                                 		  a location, follow these steps.

#### Before you begin

Cisco Emergency
                                 		  Responder requires that you enter locations in the correct format. Review the
                                 		  Location Fields section before you update a new location.

From the Cisco
                                             				Emergency Responder Off-Premises User page, choose Location .

The Configured Locations page appears.

Click the Edit icon for the location that you want to update.

The Update Locations page appears.

Enter your
                                          			 Preferred Location Name in the mandatory field. Use this name to identify this
                                          			 address when you associate your phone with this address.

Enter your
                                          			 House Number in the mandatory field.

Enter your
                                          			 Community Name in the mandatory field.

Enter your
                                          			 State in the mandatory field.

Enter your Time Zone in the optional field. The Time Zone lists all the available time zones.

When you dial 911, the selected time zone is set as the local call time in the Pager and Emergency Alerts. If a time zone
                                                         is not selected, then the local call time is same as the system call time.

Enter your Zip
                                          			 Code in the mandatory field.

Click Update .

Updating the
                                                         				  information in the location record only updates the Emergency Responder and not
                                                         				  the information at Intrado. To update the information at Intrado, you must
                                                         				  associate the location to the phone again.

To verify the
                                          			 validity of your address with Intrado, click Validate .

## Associate Your
                        	 Location to Your Phone

After you
                              		  add a location to Emergency Responder, you can associate the location to your
                              		  phone.

To
                              		  associate your location to your phone, follow these steps.

From the Cisco
                                          				Emergency Responder Off-Premises User page, choose Phones . The Location
                                          				Association page appears.

To associate a
                                       			 location to a phone, click the corresponding Assign link.

Choose a
                                       			 location from the Select
                                          				Location drop-down list.

Click Associate Location .

## Delete a Location
                        	 Associated with Your Phone

To delete a location
                              		  that is associated with a phone, follow these steps.

From the Cisco
                                          				Emergency Responder Off-Premises User page, choose Phones . The Location
                                          				Association page appears.

To delete a
                                       			 location that is associated to a phone, click the Delete link that corresponds to the directory
                                       			 number.

The status of
                                       			 the delete operation is displayed at the top of the web page and the Associated
                                       			 Location field for this phone displays "No associated
                                          				locations."

| Note | If you dismiss
                                       		  the display before confirming or updating your off-premises location, you can
                                       		  recover the display by selecting Running
                                             				Applications from the Services menu or by resetting the phone. |
|---|---|

| Note | If you close
                                          			 the phone display before you confirm or update a location, you can return to
                                          			 the display by selecting Running Applications from the Services menu or by
                                          			 resetting the phone. |
|---|---|

| Step 1 | Connect and
                                       			 register your phone through an off-premises location. A
                                       			 disclaimer message appears. If the disclaimer message does not appear, this
                                       			 feature may not be configured correctly. Contact your administrator. |
|---|---|
| Step 2 | Perform one
                                       			 of the following actions: Select Next on the phone. A list of phone locations is
                                          				displayed. Go to Step 3. Select Reject . The phone registration is completed. The
                                          				outgoing facility may not be available depending on the policy enforcement. |
| Step 3 | Perform one of
                                       			 the following actions: Select a location from the
                                          				displayed list. Go to Step 4. Select Add
                                             				  New . The phone
                                             				  display shows the procedure for adding a new location. For additional
                                             				  information on adding a new location, see the Related Topics section below.
                                             				  Once you have added a new location, select it by choosing the new location from
                                             				  the displayed list. If the new location is not displayed, select Refresh . Select Refresh . The list of phone locations refreshes and
                                          				your new locations display. |
| Step 4 | Select Exit on the Confirmation message screen. Phone
                                       			 registration is completed. Use the phone normally. Note As you
                                                   				confirm or update an off-premises location using your phone display, an error
                                                   				message might appear. Note the contents of the error message and contact your
                                                   				administrator for assistance. You can make outgoing calls from your phone, but
                                                   				911 calls might be treated as defined by the administrator setting. | Note | As you
                                                   				confirm or update an off-premises location using your phone display, an error
                                                   				message might appear. Note the contents of the error message and contact your
                                                   				administrator for assistance. You can make outgoing calls from your phone, but
                                                   				911 calls might be treated as defined by the administrator setting. |
| Note | As you
                                                   				confirm or update an off-premises location using your phone display, an error
                                                   				message might appear. Note the contents of the error message and contact your
                                                   				administrator for assistance. You can make outgoing calls from your phone, but
                                                   				911 calls might be treated as defined by the administrator setting. |

| Note | As you
                                                   				confirm or update an off-premises location using your phone display, an error
                                                   				message might appear. Note the contents of the error message and contact your
                                                   				administrator for assistance. You can make outgoing calls from your phone, but
                                                   				911 calls might be treated as defined by the administrator setting. |
|---|---|

| Step 1 | Obtain the User
                                       			 Options URL, the name that identifies the Emergency Responder Off-Premises user
                                       			 in the Navigation drop-down box, the user ID, and the default password from
                                       			 your system administrator. Example: User Options
                                          				URL: <http://server_name/ccmuser/logon.asp>, where server_name is the
                                          				host on which the web server is installed (the host is usually the same IP
                                          				address or name as the CiscoUnified Communications Manager server). User ID:
                                          				<your user ID> Default
                                          				Password: <your password> |
|---|---|
| Step 2 | Open a web
                                       			 browser on your computer, enter the URL (provided by your system
                                       			 administrator), and log in. Note If you are a
                                                      				  remote user authenticated in Cisco
                                                         					 Unified Communications Manager , a notification message to change the
                                                      				  password is displayed when the expiry is due. | Note | If you are a
                                                      				  remote user authenticated in Cisco
                                                         					 Unified Communications Manager , a notification message to change the
                                                      				  password is displayed when the expiry is due. |
| Note | If you are a
                                                      				  remote user authenticated in Cisco
                                                         					 Unified Communications Manager , a notification message to change the
                                                      				  password is displayed when the expiry is due. |
| Step 3 | If you are
                                       			 prompted to accept security settings, click Yes or Install
                                          				Certificate . The Cisco
                                             				  Unified Communications Manager User Options page appears. |
| Step 4 | Choose the Emergency
                                          				Responder Off-Premises User page from the Navigation drop-down list
                                       			 in the top right corner. If this page is not listed in the drop-down menu,
                                       			 contact your system administrator. The Cisco
                                             				  Emergency Responder Off-Premises User page appears. |

| Note | If you are a
                                                      				  remote user authenticated in Cisco
                                                         					 Unified Communications Manager , a notification message to change the
                                                      				  password is displayed when the expiry is due. |
|---|---|

| Field | Description | Value Type (A =
                                          					 Alphabets, N = Numeric, S = Special Characters [# @ & * ( ) - _ + , . : ; "
                                          					 ' /] ) |
|---|---|---|
| Location
                                          					 Name | This name
                                          					 is used to identify the address associated to your phone. | A |
| House
                                          					 Number | The number
                                          					 from the postal street address for the building. For example, 170 in 170 West
                                          					 Tasman Dr. | AN
                                          					 -(hyphen) |
| Prefix
                                          					 Directional | A leading
                                          					 directional indicator, if the street name contains one. For example, N for
                                          					 North. | Can be
                                          					 one of these directions: N S E W NE NW SE SW |
| Street
                                          					 Suffix | The street
                                          					 type. Select the
                                          					 type from the drop-down list; the field is filled with one of the abbreviations
                                          					 accepted by the United States Postal Service Publication 28. For
                                          					 example, AVE for Avenue. | A You can
                                          					 also type in the suffix. You are limited to 4 characters. |
| Location | Additional
                                          					 location information used to identify the location of the phone. | ANS You are
                                          					 limited to 60 characters. |
| State | The
                                          					 two-digit state abbreviation. | A You are
                                          					 limited to 2 characters. |
| Zip Code | The postal
                                          					 zip code for the address. | AN -
                                          					 (Hyphen) |
| House
                                          					 Number Suffix | The number
                                          					 extension for the house number. For
                                          					 example, /2. | ANS |
| Street
                                          					 Name | The
                                          					 street name from the postal address for the building. You are limited to 60
                                          					 characters. | ANS |
| Post
                                          					 Directional | A
                                          					 trailing directional indicator if the street name contains one. For
                                          					 example, N for North. | Can be
                                          					 one of these directions: N S E W NE NW SE SW |
| Community
                                          					 Name | The
                                          					 community name for the address, for example, a city, town, or district name. | ANS You are
                                          					 limited to 32 characters. |
| Time Zone | Select a time zone for the Emergency Response Location (ERL). The time zone can be selected from the drop-down containing
                                          all the available time zones. When a 911 call is placed from a phone tracked under this ERL, the Email, Web, and Pager alert indicates a local call time
                                          based on the time zone set for the ERL. If the time zone is not selected, the CER Server time is displayed. | ANS |
| Zip Code
                                          					 Extension | The postal zip code plus four numbers. | AN -
                                          					 (Hyphen) You are
                                          					 limited to 4 characters. |

| Step 1 | From the Cisco
                                             				Emergency Responder Off-Premises User page, choose Location . The Configured Locations page appears. |
|---|---|
| Step 2 | Click Add
                                             				New Locations . |
| Step 3 | Enter your
                                          			 Preferred Location Name in the mandatory field. Use this name to identify this
                                          			 address when you associate your phone with this address. |
| Step 4 | Enter your
                                          			 House Number in the mandatory field. |
| Step 5 | Enter your
                                          			 Street Name in the mandatory field. |
| Step 6 | Enter your
                                          			 Community Name in the mandatory field. |
| Step 7 | Enter your
                                          			 State in the mandatory field. |
| Step 8 | Enter your Time Zone in the optional field. The Time Zone lists all the available time zones. Note When you dial 911, the selected time zone is set as the local call time in the Pager and Emergency Alerts. If a time zone
                                                         is not selected, then the local call time is same as the system call time. | Note | When you dial 911, the selected time zone is set as the local call time in the Pager and Emergency Alerts. If a time zone
                                                         is not selected, then the local call time is same as the system call time. |
| Note | When you dial 911, the selected time zone is set as the local call time in the Pager and Emergency Alerts. If a time zone
                                                         is not selected, then the local call time is same as the system call time. |
| Step 9 | Enter your Zip
                                          			 Code in the mandatory field. Note Emergency
                                                         				  Responder can automatically populate the fields on the form. Search for your
                                                         				  information at Intrado by entering the search criteria, clicking on Search , and choosing your address from the generated
                                                         				  list of locations. | Note | Emergency
                                                         				  Responder can automatically populate the fields on the form. Search for your
                                                         				  information at Intrado by entering the search criteria, clicking on Search , and choosing your address from the generated
                                                         				  list of locations. |
| Note | Emergency
                                                         				  Responder can automatically populate the fields on the form. Search for your
                                                         				  information at Intrado by entering the search criteria, clicking on Search , and choosing your address from the generated
                                                         				  list of locations. |
| Step 10 | Click Save . |
| Step 11 | To validate
                                          			 your address, click Validate . |

| Note | When you dial 911, the selected time zone is set as the local call time in the Pager and Emergency Alerts. If a time zone
                                                         is not selected, then the local call time is same as the system call time. |
|---|---|

| Note | Emergency
                                                         				  Responder can automatically populate the fields on the form. Search for your
                                                         				  information at Intrado by entering the search criteria, clicking on Search , and choosing your address from the generated
                                                         				  list of locations. |
|---|---|

| Step 1 | From the Cisco
                                             				Emergency Responder Off-Premises User page, choose Location . The Configured Locations page appears. |
|---|---|
| Step 2 | Click the Edit icon for the location that you want to update. The Update Locations page appears. |
| Step 3 | Enter your
                                          			 Preferred Location Name in the mandatory field. Use this name to identify this
                                          			 address when you associate your phone with this address. |
| Step 4 | Enter your
                                          			 House Number in the mandatory field. |
| Step 5 | Enter your
                                          			 Community Name in the mandatory field. |
| Step 6 | Enter your
                                          			 State in the mandatory field. |
| Step 7 | Enter your Time Zone in the optional field. The Time Zone lists all the available time zones. Note When you dial 911, the selected time zone is set as the local call time in the Pager and Emergency Alerts. If a time zone
                                                         is not selected, then the local call time is same as the system call time. | Note | When you dial 911, the selected time zone is set as the local call time in the Pager and Emergency Alerts. If a time zone
                                                         is not selected, then the local call time is same as the system call time. |
| Note | When you dial 911, the selected time zone is set as the local call time in the Pager and Emergency Alerts. If a time zone
                                                         is not selected, then the local call time is same as the system call time. |
| Step 8 | Enter your Zip
                                          			 Code in the mandatory field. Note To have
                                                         				  Emergency Responder automatically populate the fields on the form, you can
                                                         				  search for existing information by entering the search criteria, clicking on Search , and choosing your address from the list of
                                                         				  locations that is returned from the search. | Note | To have
                                                         				  Emergency Responder automatically populate the fields on the form, you can
                                                         				  search for existing information by entering the search criteria, clicking on Search , and choosing your address from the list of
                                                         				  locations that is returned from the search. |
| Note | To have
                                                         				  Emergency Responder automatically populate the fields on the form, you can
                                                         				  search for existing information by entering the search criteria, clicking on Search , and choosing your address from the list of
                                                         				  locations that is returned from the search. |
| Step 9 | Click Update . Important Updating the
                                                         				  information in the location record only updates the Emergency Responder and not
                                                         				  the information at Intrado. To update the information at Intrado, you must
                                                         				  associate the location to the phone again. | Important | Updating the
                                                         				  information in the location record only updates the Emergency Responder and not
                                                         				  the information at Intrado. To update the information at Intrado, you must
                                                         				  associate the location to the phone again. |
| Important | Updating the
                                                         				  information in the location record only updates the Emergency Responder and not
                                                         				  the information at Intrado. To update the information at Intrado, you must
                                                         				  associate the location to the phone again. |
| Step 10 | To verify the
                                          			 validity of your address with Intrado, click Validate . |

| Note | When you dial 911, the selected time zone is set as the local call time in the Pager and Emergency Alerts. If a time zone
                                                         is not selected, then the local call time is same as the system call time. |
|---|---|

| Note | To have
                                                         				  Emergency Responder automatically populate the fields on the form, you can
                                                         				  search for existing information by entering the search criteria, clicking on Search , and choosing your address from the list of
                                                         				  locations that is returned from the search. |
|---|---|

| Important | Updating the
                                                         				  information in the location record only updates the Emergency Responder and not
                                                         				  the information at Intrado. To update the information at Intrado, you must
                                                         				  associate the location to the phone again. |
|---|---|

| Step 1 | From the Cisco
                                          				Emergency Responder Off-Premises User page, choose Phones . The Location
                                          				Association page appears. |
|---|---|
| Step 2 | To associate a
                                       			 location to a phone, click the corresponding Assign link. |
| Step 3 | Choose a
                                       			 location from the Select
                                          				Location drop-down list. |
| Step 4 | Click Associate Location . |

| Step 1 | From the Cisco
                                          				Emergency Responder Off-Premises User page, choose Phones . The Location
                                          				Association page appears. |
|---|---|
| Step 2 | To delete a
                                       			 location that is associated to a phone, click the Delete link that corresponds to the directory
                                       			 number. |
| Step 3 | The status of
                                       			 the delete operation is displayed at the top of the web page and the Associated
                                       			 Location field for this phone displays "No associated
                                          				locations." |