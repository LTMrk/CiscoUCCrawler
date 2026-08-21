---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-bbd2bd70b0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_department-api_1501.html
retrieved_at: 2026-08-21T16:46:14.523421+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Department API

## Chapter: Department API

- Department API

- Department                              	 API

# Department API

## Department
                        	 API

Packaged CCE allows
                           		you to create departments, add configuration items to departments, and assign
                           		administrators to departments to limit the scope of their control. For example,
                           		the call center for a hospital might have departments for Radiology, Surgery,
                           		and Cardiology. Use of departments is optional.

For more information on how departments work, see the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Use the Department
                           		API to list the departments currently defined in the database, define new
                           		departments, and view, edit, and delete existing departments.

### URL

### Operations

create :
                                    				Creates one department.

delete :
                                    				Marks one department for deletion.

get :
                                    				Returns one department, using the URL https://<server>/unifiedconfig/config/department/<id> .

list :
                                    				Retrieves a list of departments.

update :
                                    				Updates one department.

When you create, update or delete a department in Packaged CCE, the corresponding operations takes place in the Enterprise
                                          Chat and Email as well.

### Parameters

refURL: The
                                    				refURL of the department. See Shared Parameters .

name: The name
                                    				of this department. See Shared Parameters .

changeStamp:
                                    				See Shared Parameters .

description: Optional field. Valid characters are period (.), hyphen (-), underscore (_), spaces and alphanumeric. The first character
                                       must be alphanumeric. Maximum length is 255 characters. See Shared Parameters .

administrators: A collection of administrator ( Administrator API ) references associated with this department, including the refURL, user name, and domain name. See References .

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

### Example Get
                              		  Response

```
<department>
   <changeStamp>0</changeStamp>
   <refURL>/unifiedconfig/config/department/(id)</refURL>
   <name>department1</name>
   <description>test department1</description>
   <administrators>
      <administrator>
         <refURL>/unifiedconfig/config/administrator/(id_1)</refURL>
         <userName>JohnSmith</userName>
         <domainName>BOSTON.COM</domainName>
      </administrator>
      <administrator>
         <refURL>/unifiedconfig/config/administrator/(id_2)</refURL>
         <userName>JaneDoe</userName>
         <domainName>BOSTON.COM</domainName>
      </administrator>
   </administrators>
</department>
```

| Note | When you create, update or delete a department in Packaged CCE, the corresponding operations takes place in the Enterprise
                                          Chat and Email as well. |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| name description | name (default) description |