---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-db3d631ece
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_role-api_1501.html
retrieved_at: 2026-08-21T16:47:59.515699+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Role API

## Chapter: Role API

- Role API

- Role API

# Role API

## Role API

Roles specify the
                           		APIs that an administrator can use, and which menus and tools an administrator
                           		can see and use.

Use the Role API to
                           		list the roles currently defined in the database, or edit, delete, or create
                           		new custom roles.

### Roles

Cisco
                              			 Packaged CCE database has four built-in roles for administrators that set the
                              			 access to specific features (APIs and tools). The built-in roles are
                              			 hierarchical in that each role identified in the table below contains the
                              			 access rights of the roles above it. You cannot alter the feature access for
                              			 the built-in roles, but you can create additional roles to define customized
                              			 sets of feature access.

Agent
                                          						APIs and tools only.

Agent,
                                          						Call, and Scripting tools - including Bulk Jobs.

All APIs
                                          						and tools except administrator, departments, and roles.

All
                                          						APIs and tools. Only this role provides access to the Administrator,
                                          						Department, and Role features.

For more information on these roles, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

### URL

https://<server>/unifiedconfig/config/role

### Operations

create :
                                    				Creates one role, given the specified name, description, and featureList.

delete :
                                    				Deletes one role permanently from the database.

get :
                                    				Returns one role using the URL https://<server>/unifiedconfig/config/role/<id> .

Auxiliary get method returns the accessList parameter containing a collection
                                          					 of all features that can be used to define a role. Use the URL https://<server>/unifiedconfig/config/role/available_features .

list :
                                    				Retrieves a list of roles.

update :
                                    				Gets the role item and updates the new configuration entered in the
                                    				<accessList> fields.

### Parameters

refURL: The
                                    				refURL of the role. See Shared Parameters .

name: The role
                                    				name, such as ConfigAdmin. See Shared Parameters .

changeStamp:
                                    				See Shared Parameters .

description:
                                    				See Shared Parameters .

accessList:
                                    				A collection of features that indicates which APIs and tools the administrators
                                    				assigned to this role can access.

feature:
                                          					 Element of the access list that represents access to a feature (API / tool).
                                          					 Includes the following parameters:

name: Feature name. Maps to a valid API / tool.

category: Feature category, such as Agent, Call, System, and
                                                						  Access. This parameter is used only for get and list operations.

administrators: A collection of administrator references ( Administrator API ), including the user name, domain name, and refURL of the administrator. See References .

systemDefined: Read-only parameter. Indicates if this role is a
                                    				system-defined role. Values are true/false.

When you enable the CampaignStatus or CampaignContact subfeature for a custom role then the Outbound Campaign API is provided
                                                with Update Only Access instead of Full Access. With Update Only Access, you cannot create and delete a campaign using Outbound
                                                Campaign API.

When you enable the ManageAgentAttribute or ReSkillAgents subfeature for a custom role then the Agent API is provided with
                                                Update Only Access instead of Full Access. With Update Only Access, you cannot create and delete an agent using Agent API.

Features that are disabled by feature flags will be filtered out in the GET and LIST response. Similarly, adding disabled
                                                features to the payload of a POST or PUT operation will result in 400 BAD REQUEST.

### Search and
                              		  Sort Values

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

name

description

name (default)

description

See Search and Sort .

Advanced search
                                 			 parameters

You can perform a system defined role search on the Role API:

systemDefined:(both/only/none) : Allows searching of roles with the specified value of the systemDefined parameter.

q=systemDefined:only Returns roles with the systemDefined parameter set to true.

q=systemDefined:none Returns roles with the systemDefined parameter set to false.

q=systemDefined:both Returns roles with the systemDefined parameter set to true or false.

### Example Get
                              		  Response

```
<role>
      <changeStamp>15</changeStamp>
      <refURL>/unifiedconfig/config/role/5003</refURL>
      <administrators>
        <administrator>
          <refURL>/unifiedconfig/config/administrator/5002</refURL>
          <domainName>BOSTON.COM</domainName>
          <userName>userAttribute</userName>
        </administrator>
      </administrators>
      <description>testAttribute</description>
      <accessList>
        <feature>
          <category>agent</category>
          <name>attribute</name>
        </feature>
        <feature>
          <category>agent</category>
          <name>reasoncode</name>
        </feature>
        <feature>
          <category>call</category>
          <name>bucketinterval</name>
        </feature>
      </accessList>
      <name>testAttribute</name>
      <systemDefined>false</systemDefined>
</role>
```

| This role | Allows full access to |
|---|---|
| AgentAdmin | Agent
                                          						APIs and tools only. |
| ScriptAdmin | Agent,
                                          						Call, and Scripting tools - including Bulk Jobs. |
| ConfigAdmin | All APIs
                                          						and tools except administrator, departments, and roles. |
| SystemAdmin | All
                                          						APIs and tools. Only this role provides access to the Administrator,
                                          						Department, and Role features. |

| Note | When you enable the CampaignStatus or CampaignContact subfeature for a custom role then the Outbound Campaign API is provided
                                                with Update Only Access instead of Full Access. With Update Only Access, you cannot create and delete a campaign using Outbound
                                                Campaign API. When you enable the ManageAgentAttribute or ReSkillAgents subfeature for a custom role then the Agent API is provided with
                                                Update Only Access instead of Full Access. With Update Only Access, you cannot create and delete an agent using Agent API. Features that are disabled by feature flags will be filtered out in the GET and LIST response. Similarly, adding disabled
                                                features to the payload of a POST or PUT operation will result in 400 BAD REQUEST. |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| name description | name (default) description |