---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-install-guide-uccx-b-125getting-80436d978b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/install/guide/uccx_b_125getting-started-ip-ivr/uccx_b_125getting-started-ip-ivr_chapter_01010.html
retrieved_at: 2026-08-16T21:15:42.478117+00:00
---

Getting Started with IP IVR Guide, Release 12.5(1)

# Getting Started with IP IVR Guide, Release 12.5(1)

Updated: February 10, 2020

Chapter: Unified IP IVR Management

## Chapter: Unified IP IVR Management

- Unified IP IVR Management

- Manage Prompt,                              	 Grammar, and Document Files

- Unified CCX                              	 Datastores

# Unified IP IVR Management

## Manage Prompt,
                        	 Grammar, and Document Files

Unified CCX
                              		  applications might use auxiliary files that interact with callers, such as
                              		  scripts, pre-recorded prompts, grammars, and custom Java classes. Depending on
                              		  each implementation, Unified CCX applications use some or all of the following
                              		  file types:

Prompts .
                                    				Many applications make use of pre-recorded prompts, stored as .wav files, which
                                    				are played back to callers in order to provide information and elicit caller
                                    				response.

Grammars . The Unified CCX
                                    				system uses specific grammars when recognizing and responding to caller
                                    				response to prompts. A grammar is a specific set of all possible spoken phrases
                                    				and/or DTMF digits to be recognized by Unified CCX applications and acted upon
                                    				during run time.

Documents .
                                    				Documents might consist of .txt, .doc, .jsp, or .html files. Documents can also
                                    				include custom classes and Java Archive (JAR) files that allow you to customize
                                    				the performance of your Unified CCX system. Several system-level prompt,
                                    				grammar, and document files are loaded during Unified CCX installation.
                                    				However, any file you create needs to be made available to the Unified CCX
                                    				engine before a Unified CCX application can use them. This is done through the
                                    				Unified CCX cluster’s repository detester, where the prompt, grammar, and
                                    				document files are created, stored, and updated.

The Unified
                                                				  CCX Server local disk prompt, grammar, and document files are synchronized with
                                                				  the central repository during Unified CCX engine startup and during run-time
                                                				  when the Repository detester is modified. For more information, refer to the Cisco Unified Contact Center Express Administration and Operations Guide .

## Unified CCX
                        	 Datastores

Datastores
                              		  are components that allow you to manage and monitor historical, repository, and
                              		  configuration data in the Unified CCX cluster.

The
                              		  Datastore Control Center allows you to configure and manage the following data
                              		  in the cluster:

Historical
                                    				records

Repository data,
                                    				such as prompts, grammars and documents

Configuration
                                    				data for historical reporting

Access the
                              		  Datastore Control Center by selecting Applications > Datastore
                                    				Control from the Unified CCX administration menu bar.

You can use
                              		  the Datastore Control Center to obtain an overview of the datastores in the
                              		  cluster and their relationships, manage the datastore read/write access,
                              		  monitor and control the replication agents (only available for agent,
                              		  historical, and repository datastores), and activate the Publisher.

For more
                                          			 information, refer to the Cisco Unified Contact Center Express Administration and Operations Guide .

| Note | The Unified
                                                				  CCX Server local disk prompt, grammar, and document files are synchronized with
                                                				  the central repository during Unified CCX engine startup and during run-time
                                                				  when the Repository detester is modified. For more information, refer to the Cisco Unified Contact Center Express Administration and Operations Guide . |
|---|---|

| Note | For more
                                          			 information, refer to the Cisco Unified Contact Center Express Administration and Operations Guide . |
|---|---|