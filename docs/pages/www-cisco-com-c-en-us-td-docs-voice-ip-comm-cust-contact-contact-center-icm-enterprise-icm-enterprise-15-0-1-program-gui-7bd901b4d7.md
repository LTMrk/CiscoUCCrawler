---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-7bd901b4d7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce_m_media-routing-domain-api_1501.html
retrieved_at: 2026-08-16T20:18:15.657817+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

Chapter: Media Routing Domain API

## Chapter: Media Routing Domain API

- Media Routing Domain API

- Topic 2.1

# Media Routing Domain API

## Media Routing
                        	 Domain API

A media routing
                           		domain is a collection of skill groups associated with a common media class. It
                           		is used to organize how requests for different media are routed.

Use the Media
                           		Routing Domain (MRD) API to list the MRDs currently defined in the database,
                           		define new MRDs, and view, edit, and delete existing MRDs.

The built-in Cisco_Voice MRD and legacyMultichannel MRDs are  read-only; they cannot be created, updated, or deleted.  You
                           can perform all API operations on multichannel MRDs.

### URL

### Operations

create :
                                    				Creates an MRD.

delete :
                                    				Permanently deletes one MRD.

list :
                                    				Retrieves a list of MRDs.

get :
                                    				Returns one MRD using the URL https://<server>/unifiedconfig/config/mediaroutingdomain/<id> .

update :
                                    				Updates one MRD.

### Parameters

refURL: The
                                    				refURL of the MRD. See Shared Parameters .

name: Name of
                                    				the MRD. See Shared Parameters .

description:
                                    				See Shared Parameters .

id: The database id of the MRD. Read-only field.

type: The type
                                    				of MRD. Values are as follows:

voice: Used only for the built-in Cisco_Voice MRD. These MRDs are read-only.

legacyMultichannel:  Used for MRDS for the Enterprise Chat and
                                                						Email application. These MRDs are read-only.

multichannel: (Default) 
                                          				  Used for MRDs for Task
                                                					Routing APIs.

taskLife: If
                                    				the connection goes down, the amount of time, in seconds, that the system waits
                                    				before ending all tasks. Default is 1200.

taskStartTimeout: The amount of time, in seconds, that the
                                    				system waits between an agent being selected for a task and an agent being
                                    				offered or beginning the task. When this time is reached, the system makes the
                                    				agent Not Routable. Default is 30.

maxTaskDuration: The maximum duration for a task, in seconds.
                                    				Default is 28800.

serviceLevelThreshold: Maximum time in seconds that a customer
                                    				should wait before being connected with an agent. Default is 30.

interruptible:
                                    				Indicates if an agent can be interrupted by assigned tasks from another MRD.
                                    				Values are true/false.

maxTasksInQueue: The maximum number of tasks allowed to be
                                    				queued at one time.

maxTimeInQueue: The maximum amount of time, in seconds, a task
                                    				can be queued.

### Search and
                              		  Sort Values

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

- name

- description

- id

- name (default)

- description

- id

- interruptible

- maxTasksInQueue

- maxTaskDuration

- maxTimeInQueue

- serviceLevelThreshold

- taskLife

- taskStartTimeout

See Search and Sort .

Advanced search
                                 			 parameters

- nonVoiceOnly : Set this attribute to true in the search query
                                    			 parameter to make the API return only media routing domains other than the
                                    			 Cisco_Voice MRD. For example, q=nonVoiceOnly:true .

### Example Get
                              		  Response

```
<mediaRoutingDomains>
   <mediaRoutingDomain>
      <changeStamp>0</changeStamp>
      <refURL>/unifiedconfig/config/mediaroutingdomain/5001</refURL>
      <description>Media channel for routing Chat tasks</description>
						<id>5001</id>
						<type>multichannel</type>
      <interruptible>false</interruptible>
						<taskLife>1200</taskLife>
						<taskStartTimeout>30</taskStartTimeout>
						<maxTaskDuration>28800</maxTaskDuration>
      <maxTasksInQueue>1000</maxTasksInQueue>
      <maxTimeInQueue>1000</maxTimeInQueue>
      <name>Chat_Task_MRD</name>
      <serviceLevelThreshold>30</serviceLevelThreshold>
   </mediaRoutingDomain>
   <mediaRoutingDomain>
      <changeStamp>0</changeStamp>
      <refURL>/unifiedconfig/config/mediaroutingdomain/1</refURL>
      <description>Default Media Routing Domain for Cisco_Voice</description>
      <id>1</id>
						<type>voice</type>
      <interruptible>false</interruptible>
						<taskLife>1200</taskLife>
						<taskStartTimeout>30</taskStartTimeout>
						<maxTaskDuration>28800</maxTaskDuration>
      <name>Cisco_Voice</name>
      <serviceLevelThreshold>30</serviceLevelThreshold>
    </mediaRoutingDomain>
  </mediaRoutingDomains>
```

### Topic 2.1

| Search parameters | Sort parameters |
|---|---|
| name description id | name (default) description id interruptible maxTasksInQueue maxTaskDuration maxTimeInQueue serviceLevelThreshold taskLife taskStartTimeout |