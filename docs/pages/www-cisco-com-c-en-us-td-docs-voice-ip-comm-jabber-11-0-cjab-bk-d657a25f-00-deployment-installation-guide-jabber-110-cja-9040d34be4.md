---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-11-0-cjab-bk-d657a25f-00-deployment-installation-guide-jabber-110-cja-9040d34be4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_0/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110_chapter_010.html
retrieved_at: 2026-08-25T21:46:08.104684+00:00
---

Cisco Jabber 11.0 Deployment and Installation Guide

# Cisco Jabber 11.0 Deployment and Installation Guide

Updated: June 25, 2015

Chapter: Configure Directory Integration

## Chapter: Configure Directory Integration

# Configure Directory Integration

## Configure Directory Integration for an On-Premises Deployment

To replicate contact data to Cisco Unified Communications Manager.

Only for Cisco Unified Communications Manager IM and Presence Service release 10.x or later.

Populate the user ID and directory URI from an attribute in the directory.

Synchronize Cisco Unified Communications Manager with the directory server.

Configure Cisco Unified Communications Manager to authenticate with the directory server

### Enable Synchronization

To ensure that contact data in your directory server is replicated to Cisco Unified Communications Manager, you must synchronize with the directory server. Before you can synchronize with the directory server, you must enable synchronization.

The LDAP System Configuration window opens.

Specify an LDAP attribute for the user ID.

### Configure IM
	 Address Scheme

This feature is supported on Cisco Unified Communications Manager IM
		  and Presence Service release 10.x or later. For versions of Cisco Unified
		  Communications Manager IM and Presence Service release 9.x and earlier the
		  default IM address scheme used is UserID@[Default Domain] .

- Open Cisco Unified CM IM and Presence Administration .

- Select Presence > Settings > Advanced Configuration The Advanced Presence Settings window opens.

If you use the UserID, ensure that you configure a default
				  domain. For example, services must be named cups.com and not cups .

Directory URI

- Open Cisco Unified CM Administration .

- Select System > LDAP > LDAP Directory . The Find and List LDAP Directories window opens.

- Find and select the directory from the list. The LDAP Directory window opens.

User ID mapped
				to an LDAP field, the default is sAMAccountName .

Directory URI
				mapped to either mail or msRTCSIP-primaryuseraddress .

### Populate User ID and Directory URI

User ID — You must
				  specify a value for the user ID on Cisco Unified Communications Manager . This value is required for the
				  default IM address scheme and for users to sign in. The default value is sAMAccountName .

Enable
						URI dialing in Cisco Jabber .

Use the
						directory URI address scheme on Cisco Unified Communications Manager IM and Presence Service version 10 and higher.

When 
		  Cisco Unified Communications Manager synchronizes with the directory
		  source, it retrieves the values for the directory URI and user ID and populates
		  them in the end user configuration table in the 
		  Cisco Unified Communications Manager database.

The 
		  Cisco Unified Communications Manager database then synchronizes with the 
		  Cisco Unified Communications Manager IM and Presence Service database. As a result, the values
		  for the directory URI and user ID are populated in the end user configuration
		  table in the 
		  Cisco Unified Communications Manager IM and Presence Service database.

#### Specify an LDAP
	 Attribute for the User ID

When you
		  synchronize from your directory source to Cisco Unified Communications Manager , you can populate
		  the user ID from an attribute in the directory. The default attribute that
		  holds the user ID is sAMAccountName .

If the
					 attribute for the user ID is other than sAMAccountName and you are using the
						default IM address scheme in 
						Cisco Unified Communications Manager IM and Presence Service , you must specify the
					 attribute as the value for the parameter in your client configuration file as
					 follows:

The EDI parameter is UserAccountName .

```
<UserAccountName> attribute-name </UserAccountName>
```

```
<BDIUserAccountName> attribute-name </BDIUserAccountName>
```

If you
					 do not specify the attribute in your configuration, and the attribute is other
					 than sAMAccountName , the client cannot resolve contacts in
					 your directory. As a result, users do not get presence and cannot send or
					 receive instant messages.

#### Specify an LDAP Attribute for the Directory URI

On Cisco Unified Communications Manager release 9.0(1)
		  and later, you can populate the directory URI from an attribute in the
		  directory.

Enable Synchronization .

msRTCSIP-primaryuseraddress —This attribute is populated in
					 the AD when Microsoft Lync or Microsoft OCS are used. This is the default attribute.

mail

### Perform
	 Synchronization

After you add a directory server and specify the required
		  parameters, you can synchronize Cisco Unified Communications Manager with the
		  directory server.

Cisco
				Unified Presence — Cisco UP Sync Agent

Cisco
				  Unified Communications Manager IM and Presence Service — Cisco Sync Agent

This service
		  keeps data synchronized between the presence server and Cisco Unified Communications Manager . When you perform
		  the synchronization with your directory server, Cisco Unified Communications Manager then synchronizes
		  the data with the presence server. However, the Cisco
			 Sync Agent service must be activated and started.

The LDAP
				  Directory window opens.

See the Cisco
				  Unified Communications Manager Administration Guide for more information
				about the values and formats you can specify.

The
					 amount of time it takes for the synchronization process to complete depends on
					 the number of users that exist in your directory. If you synchronize a large
					 directory with thousands of users, you should expect the process to take some
					 time.

User data from your directory server is synchronized to the Cisco Unified Communications Manager database. Cisco Unified Communications Manager then synchronizes
		  the user data to the presence server database.

### Authenticate with
	 the LDAP Server

Perform this procedure if you want to enable LDAP authentication so that end user passwords are authenticated against the password that is assigned in the company LDAP directory. LDAP authentication gives system administrators the ability to assign an end user a single password for all company applications. This configuration applies to end user passwords only and does not apply to end user PINs or application user passwords. When users sign in to the client, the presence service routes that authentication to Cisco Unified Communications Manager . Cisco Unified Communications Manager then sends that authentication to the directory server.

See the Cisco Unified Communications Manager Administration Guide for
				information about the fields on the LDAP Authentication window.

## Configure Directory Integration for Cloud-Based Deployments

Review the topics.

Configure your
			 organization information.

Create and
			 provision users.

### Add Directory
	 Groups

Directory groups,
		  or enterprise groups, provide contact groups that administrators define for
		  users.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable Synchronization . | To replicate contact data to Cisco Unified Communications Manager. |
| Step 2 | Configure IM Address Scheme | Only for Cisco Unified Communications Manager IM and Presence Service release 10.x or later. |
| Step 3 | Populate User ID and Directory URI | Populate the user ID and directory URI from an attribute in the directory. |
| Step 4 | Perform Synchronization | Synchronize Cisco Unified Communications Manager with the directory server. |
| Step 5 | Authenticate with the LDAP Server . | Configure Cisco Unified Communications Manager to authenticate with the directory server |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > LDAP > LDAP System . The LDAP System Configuration window opens. |
| Step 3 | Locate the LDAP System Information section. |
| Step 4 | Select Enable Synchronizing from LDAP Server . |
| Step 5 | Select  the type of directory server from which you are synchronizing  data from the LDAP Server Type drop-down list. |

| Step 1 | Choose the IM Address Scheme . Open Cisco Unified CM IM and Presence Administration . Select Presence > Settings > Advanced Configuration The Advanced Presence Settings window opens. Select IM Address Scheme and from the list choose one of the following: UserID@[Default
				Domain] If you use the UserID, ensure that you configure a default
				  domain. For example, services must be named cups.com and not cups . Directory URI |
|---|---|
| Step 2 | Select the required mapping. Open Cisco Unified CM Administration . Select System > LDAP > LDAP Directory . The Find and List LDAP Directories window opens. Find and select the directory from the list. The LDAP Directory window opens. In the Standard User Fields To Be Synchronized section choose the mapping: User ID mapped
				to an LDAP field, the default is sAMAccountName . Directory URI
				mapped to either mail or msRTCSIP-primaryuseraddress . |

| Step 1 | Locate the LDAP
				Attribute for User ID drop-down list on the LDAP
				System Configuration window. |
|---|---|
| Step 2 | Specify an
			 attribute for the user ID as appropriate and then select Save . Important: If the
					 attribute for the user ID is other than sAMAccountName and you are using the
						default IM address scheme in 
						Cisco Unified Communications Manager IM and Presence Service , you must specify the
					 attribute as the value for the parameter in your client configuration file as
					 follows: The EDI parameter is UserAccountName . <UserAccountName> attribute-name </UserAccountName> The BDI parameter is BDIUserAccountName . <BDIUserAccountName> attribute-name </BDIUserAccountName> If you
					 do not specify the attribute in your configuration, and the attribute is other
					 than sAMAccountName , the client cannot resolve contacts in
					 your directory. As a result, users do not get presence and cannot send or
					 receive instant messages. |

| Step 1 | Select System > LDAP > LDAP
				  Directory . |
|---|---|
| Step 2 | Select the
			 appropriate LDAP directory or select Add
				New to add an LDAP directory. |
| Step 3 | Locate the Standard User Fields To Be Synchronized section. |
| Step 4 | Select one of
			 the following LDAP attributes from the Directory URI drop-down list: msRTCSIP-primaryuseraddress —This attribute is populated in
					 the AD when Microsoft Lync or Microsoft OCS are used. This is the default attribute. mail |
| Step 5 | Select Save . |

| Step 1 | Select System > LDAP > LDAP
				  Directory . |
|---|---|
| Step 2 | Select Add
				New . The LDAP
				  Directory window opens. |
| Step 3 | Specify the
			 required details on the LDAP
				Directory window. See the Cisco
				  Unified Communications Manager Administration Guide for more information
				about the values and formats you can specify. |
| Step 4 | Create an
			 LDAP Directory Synchronization Schedule to ensure that your information is
			 synchronized regularly. |
| Step 5 | Select Save . |
| Step 6 | Select Perform Full Sync Now . Note The
					 amount of time it takes for the synchronization process to complete depends on
					 the number of users that exist in your directory. If you synchronize a large
					 directory with thousands of users, you should expect the process to take some
					 time. | Note | The
					 amount of time it takes for the synchronization process to complete depends on
					 the number of users that exist in your directory. If you synchronize a large
					 directory with thousands of users, you should expect the process to take some
					 time. |
| Note | The
					 amount of time it takes for the synchronization process to complete depends on
					 the number of users that exist in your directory. If you synchronize a large
					 directory with thousands of users, you should expect the process to take some
					 time. |

| Note | The
					 amount of time it takes for the synchronization process to complete depends on
					 the number of users that exist in your directory. If you synchronize a large
					 directory with thousands of users, you should expect the process to take some
					 time. |
|---|---|

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > LDAP > LDAP
				  Authentication . |
| Step 3 | Select Use
				LDAP Authentication for End Users . |
| Step 4 | Specify LDAP
			 credentials and a user search base as appropriate. See the Cisco Unified Communications Manager Administration Guide for
				information about the fields on the LDAP Authentication window. |
| Step 5 | Select Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Review Directory Integration . | Review the topics. |
| Step 2 | See Understanding the Configuration Tab . | Configure your
			 organization information. |
| Step 3 | See Overview of
				User Management . | Create and
			 provision users. |
| Step 4 | Add Directory Groups . |  |

| Step 1 | Set up
			 directory integration. |
|---|---|
| Step 2 | Define your
			 directory groups in a comma-separated values ( .csv ) file. |
| Step 3 | Import your
			 directory groups using the 
			 Cisco WebEx Administration Tool. |