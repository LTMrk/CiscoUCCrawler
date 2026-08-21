---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-managed-services-12-5-1-cucm-b-manager-assistant-user-guide-1251-cucm-b-dcc3537425
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/managed_services/12_5_1/cucm_b_manager-assistant-user-guide-1251/cucm_b_manager-assistant-user-guide-1251_chapter_0110.html
retrieved_at: 2026-08-21T01:28:54.854894+00:00
---

Manager Assistant User Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Manager Assistant User Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: January 22, 2019

Chapter:  Configure Manager Features

## Chapter:  Configure Manager Features

# Configure Manager Features

## Configure Manager Features

Managers and
                              		assistants can modify manager preferences from the Manager Configuration
                              		window:

- Managers can access the
                                 		  window from a website.

- Assistants can access the
                                 		  window from the Assistant Console.

Your system
                              		administrator configured your Manager Assistant to operate in the shared-line
                              		or proxy-line mode. For more information, see Shared-Line and Proxy-Line Modes Overview .

The initial default
                              		settings enable managers to use the Manager Assistant without configuring
                              		preferences first.

## For Managers—Accessing the Manager Configuration

Managers access
                              		  the Manager Configuration window using a website. You can obtain the URL from
                              		  your system administrator.

### Before you begin

You can configure Manager Assistant on only one device. You can choose the device on the Manager Configuration window.

On a computer
                                       			 running Microsoft Windows 2000 or later, open a Microsoft Internet Explorer
                                       			 (IE) browser. The browser version must be 5.5 or later.

Open the URL
                                       			 that your system administrator provided. The URL should look like this:
                                       			 http://<ip-address>/ma/desktop/maLogin.jsp

Check the
                                       			 check box to indicate that you agree with this text: "Always trust content from
                                          			 Cisco Systems Inc" . Then click Yes .

Enter your
                                       			 username and password (as provided by your system administrator) and click Sign
                                          				in .

To log out,
                                       			 close the browser window.

## For
                        	 Assistants—Access Manager Configuration

Assistants can access the Manager Configuration window from the Assistant Console .

To access the window for a particular manager, right-click anywhere in
                              		  the row for that manager in the My Managers panel of the Assistant Console and then choose Configure from the popup menu.

To access the window for all of your managers, choose Manager > Configuration from the menu bar. If necessary, choose the manager for whom you want to
                              		  configure features from the Manager drop-down menu.

## Assign a Default
                        	 Assistant to a Manager

Use this procedure to identify one of a manager’s configured
                              		  assistants as the default assistant.

When possible, the Manager Assistant assigns the default assistant as
                              		  the manager’s active assistant. If the default assistant is not logged in, the
                              		  Manager Assistant assigns another available assistant to serve as the active
                              		  assistant. After the default assistant logs in, the Manager Assistant switches
                              		  assistants so that the default assistant is active and handling calls.

From the Manager
                                          			 Configuration window, click the Default Assistant tab (if necessary) to
                                       			 display the Default Assistant Selection window.

Select the appropriate assistant from the assistant drop-down
                                       			 menu and save the change.

## Configure the Divert Target for a Manager

Managers can use configure a divert target in these ways:

- Proxy-line mode—Managers
                                 			 using the Manager Assistant can use the Divert All (DivAll) and Redirect features to send calls to the assistant or to
                                 another phone number
                                 			 (also known as the target). The DivAll feature and the Redirect feature share
                                 			 the same divert target.

- Shared-line mode—Managers
                                 			 using the Manager Assistant in the shared-line mode can set up a divert target
                                 			 and forward calls as the calls come in by using the Redirect softkey. The
                                 			 divert screen displays automatically when you log in.

By initial default, the Divert target is the manager’s active
                              		  assistant. Managers and assistants can use this procedure to change the target.

From the Manager Configuration window, click the Divert tab to display the Divert Configuration window.

(Proxy-line mode only) Select Directory Number or Assistant .

If you selected Directory Number , enter a valid phone number.
                                       			 Enter the number exactly as you would dial it from your office phone and save
                                       			 the change.

## Create Filter
                        	 Lists for a Manager

Filter lists
                              		  enable managers or assistants to customize the manager’s call-filtering
                              		  feature.

By default, filter
                              		  lists are empty. Add numbers to a filter list to customize it. Choose a filter
                              		  mode to toggle between Inclusive or Exclusive filter lists. For the list
                              		  descriptions, refer to Table 1 .

Only one filter
                              		  mode (Inclusive or Exclusive) can be active at any time. Managers can toggle
                              		  between filter modes from the Manager Assistant menu on their phones.
                              		  Assistants can toggle between filter modes for a manager from the Assistant
                              		  Console.

The Manager
                              		  Assistant compares the caller ID of the incoming call to the phone numbers in
                              		  the active filter list.

Filter lists can
                              		  include these wildcards:

Besides wildcards,
                              		  filter lists can contain hyphens (–), periods (.), and blank spaces.

Filter lists can
                              		  be empty. By initial default, the filter is enabled and the Inclusive filter
                              		  list is empty. This means that all of a manager’s incoming calls are redirected
                              		  to the assistant.

Managers can
                              		  activate your filter lists from your phone. Open the Manager
                                 			 Assistant menu on your phone. Press 1 to toggle the Filter feature on and off. Press 2 to toggle between Inclusive and Exclusive filter
                              		  modes.

Managers and
                              		  assistants can use the following procedure to create filter lists.

If you have both
                              		  call filtering and Divert All (DivAll) enabled, the Manager Assistant first
                              		  applies call filtering to an incoming call. Call filtering directs the call to
                              		  you or to your assistant (depending on filter settings). Next, the Manager
                              		  Assistant applies DivAll to those calls that filtering has directed to you. The
                              		  DivAll feature redirects those calls to the DivAll target.

For the
                              		  call-filtering icons in the Manager
                                 			 Assistant status window, see Table 2 table.

### Create Filter
                           	 Lists for a Manager

From the Manager Configuration window, click the Inclusive or the Exclusive tab to display the appropriate configuration window.

In the Filter field, enter a partial or complete
                                          			 phone number.

You can add, replace, or delete filters:

To add a new filter, enter a filter in the Filter field and click add . The new filter appears in the Filter List .

To replace an existing filter with a new one, select the
                                                				  existing filter that you want to modify in the Filter List . Change the filter in the Filter field and click replace . The modified filter appears in
                                                				  the Filter List .

To delete a filter, select the filter in the Filter List and click delete . The deleted filter is removed from
                                                				  the Filter List .

Save your changes.

## Update Manager and Assistant Configuration

The administrator follows this procedure for updating device/phone
                              		  information for existing Manager Assistant configuration. The  modification to device information happens when you:

- update a device name

- update directory number
                                 			 for a phone

- delete a phone

- line modification

Perform these steps in Unified Communications Manager Administration

Delete manager or assistant configuration

Disassociate device

Update device

Associate device

Recreate the manager or assistant configuration

| Note | You can configure Manager Assistant on only one device. You can choose the device on the Manager Configuration window. |
|---|---|

| Step 1 | On a computer
                                       			 running Microsoft Windows 2000 or later, open a Microsoft Internet Explorer
                                       			 (IE) browser. The browser version must be 5.5 or later. |
|---|---|
| Step 2 | Open the URL
                                       			 that your system administrator provided. The URL should look like this:
                                       			 http://<ip-address>/ma/desktop/maLogin.jsp A
                                       			 popup window asks whether you want to install the Manager Assistant
                                       			 software. |
| Step 3 | Check the
                                       			 check box to indicate that you agree with this text: "Always trust content from
                                          			 Cisco Systems Inc" . Then click Yes . The Login window appears. |
| Step 4 | Enter your
                                       			 username and password (as provided by your system administrator) and click Sign
                                          				in . The Manager
                                          				Configuration window appears |
| Step 5 | To log out,
                                       			 close the browser window. |

| Step 1 | From the Manager
                                          			 Configuration window, click the Default Assistant tab (if necessary) to
                                       			 display the Default Assistant Selection window. |
|---|---|
| Step 2 | Select the appropriate assistant from the assistant drop-down
                                       			 menu and save the change. |

| Step 1 | From the Manager Configuration window, click the Divert tab to display the Divert Configuration window. |
|---|---|
| Step 2 | (Proxy-line mode only) Select Directory Number or Assistant . |
| Step 3 | If you selected Directory Number , enter a valid phone number.
                                       			 Enter the number exactly as you would dial it from your office phone and save
                                       			 the change. |

| Step 1 | From the Manager Configuration window, click the Inclusive or the Exclusive tab to display the appropriate configuration window. |
|---|---|
| Step 2 | In the Filter field, enter a partial or complete
                                          			 phone number. If you need help, click the More Info link to see example filters. |
| Step 3 | You can add, replace, or delete filters: To add a new filter, enter a filter in the Filter field and click add . The new filter appears in the Filter List . To replace an existing filter with a new one, select the
                                                				  existing filter that you want to modify in the Filter List . Change the filter in the Filter field and click replace . The modified filter appears in
                                                				  the Filter List . To delete a filter, select the filter in the Filter List and click delete . The deleted filter is removed from
                                                				  the Filter List . |
| Step 4 | Save your changes. |

| Step 1 | Delete manager or assistant configuration |
|---|---|
| Step 2 | Disassociate device |
| Step 3 | Update device |
| Step 4 | Associate device |
| Step 5 | Recreate the manager or assistant configuration |