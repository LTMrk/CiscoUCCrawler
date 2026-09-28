---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-15-0-maintain-and-operate-guide-uccx-042f46eadd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_15_0/maintain_and_operate/guide/uccx_b_1501_admin-and-operations-guide/uccx_m_1501_wizards-menu.html
retrieved_at: 2026-08-16T21:28:29.228535+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 15.0

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 15.0

Updated: April 30, 2025

Chapter: Wizards Menu

## Chapter: Wizards Menu

- Wizards Menu

- Application Wizard

- RmCm                              	 Wizard

# Wizards Menu

The Wizards menu of the Unified CCX Administration web
                           		  interface provides access to the wizards available for your Unified CCX system.

In each Wizard web page, you are provided with a list of
                           		  procedures and a description for each procedure in the main pane.

Click 
                           		  the Exit icon in the toolbar in the upper left
                           		  corner of the window or the Exit button that displays at the bottom of the
                           		  window to exit the wizard at any time and to go to the main Unified CCX
                           		  Administration menu bar. Click Next to go to the next wizard menu option.

The Unified CCX system contains the following options in the Wizards menu:

## Application Wizard

Application Configuration is one of the very basic requirements in Unified CCX Administration. You must complete several steps
                              in the following order to successfully complete Application Configuration.

To access the Application Wizard, select Wizards > Application Wizard > Description of Steps from the Unified CCX Administration menu bar. The Application Configuration Wizard: Description of Steps web page opens up,
                              displaying the different steps to perform the configuration, along with a brief description of each step as shown in the following
                              bulleted list.

Click Next to proceed to the subsequent steps from the main Application Configuration Wizard web page or jump directly to any step using Wizards > Application Wizard and clicking the desired submenu (see Configure Unified CCX Applications ).

Scripts —In this step, you can view a list of existing custom scripts. When you click the Next button from the main Application Configuration Wizard web page, you are transferred to Script Management web page, which
                                    lists the available scripts, provides links to create a folder, and uploads custom scripts. Scripts can be uploaded as either
                                    a single script file or a zip file of scripts. You can upload multiple scripts in this step (see Script Management ).

Prompts —In this step, you can view a list of existing custom prompts. The Prompt Management web page lists the available prompts,
                                    provides links to create new folders, and uploads custom prompts. Prompts can be uploaded as either a single prompt file or
                                    a zip file of prompts. You can upload multiple prompts in this step (see Manage Prompt Files ).

Grammars —In this step, you can view a list of existing custom grammar files that are used to recognize and respond to caller prompts.
                                    The Grammar Management web page lists the available grammars, provides the links to create new folders, and uploads custom
                                    grammars. Grammars can be uploaded as either a single grammar file or a zip file of grammars. You can upload multiple grammars
                                    in this step (see Manage Grammar Files ).

Documents —In this step, you can view a list of existing custom documents such as .txt, .doc, .jsp, or .html, custom classes, and Java
                                    Archive (JAR) files that allow you to customize the performance of your Unified CCX system. The Document Management web page
                                    lists the available documents, provides the links to create new folders, and uploads custom documents. Documents can be uploaded
                                    as either a single document file or a zip file of documents. You can upload multiple documents in this step (see Manage Document Files ).

Application Configuration —In this step, you can select the type of application to be configured using Add a New Application page. Click Next to provide configuration details for the selected application type. Each application can be any combination of the scripts,
                                    prompts, grammars, and documents on file. By default, the uploaded script, prompt, document and grammar are selected, if applicable.
                                    You can create multiple applications in this step (see About Unified CCX Applications ).

Triggers —In this step, you can create different types of triggers for the applications that were created in the previous step using
                                    the Trigger Configuration page. More than one trigger can be created for one application. By default, the application configured
                                    in the previous step is automatically selected. On providing the Directory Number, device name and language, the trigger configuration
                                    is complete. You can create multiple triggers in this step (see Application Triggers ).

Selecting the type of the trigger concludes the Application Configuration wizard process.

## RmCm
                        	 Wizard

RmCm Configuration is a commonly performed procedure in the contact center environment. You must complete several steps to
                              successfully complete RmCm Configuration. The RmCm Configuration wizard leads you through the following steps.

The RmCm Wizard
                                          			 option is available with all Unified CCX license packages.

To access
                              		  the Application Wizard, select Wizards > RmCm
                                    				Wizard > Description of Steps from the Unified
                              		  CCXAdministration menu bar. The Application Configuration Wizard: Description
                              		  of Steps web page opens up displaying the different steps in which you can
                              		  perform the configuration along with a brief description of each step as shown
                              		  in the bulleted list below.

Click Next to proceed to the subsequent steps from the
                              		  main RmCm Wizard web page or jump directly to any step using Wizards > RmCm
                                    				Wizard and clicking the desired submenu.

Add a Skill —Choose this
                                    				submenu to configure the skills to be associated with the user. In this step,
                                    				you are transferred to the RmCm > Skills web page. Repeat this step to
                                    				create multiple skills.

Add a Resource
                                       				  Group —Choose this submenu to upload multiple custom scripts. In this step,
                                    				you are transferred to the Resource Group Configuration web page, where you can
                                    				enter the Resource Group Name.

Add Resources —Choose this submenu to create resource groups that will later be assigned to resources. In this step, you are transferred
                                    to RmCm Wizard - User Configuration web page, which has a hyperlink to Add resources in Unified CM . This link invokes Unified CM automatically (see the following related topics):

RmCm Provider Configuration

Add Supervisors —Choose
                                    				this submenu to assign supervisor privileges to a user. In this step, you are
                                    				transferred to the User Management web page, which allows you to search for a
                                    				specific user.

Configure
                                       				  Resources —Choose this submenu to add or remove skills that are associated
                                    				with resources. In this step, you are transferred to the RmCm Configuration
                                    				Resources web page, which lists the configured resources. Resources can be
                                    				modified together to obtain the same skills, or they can be modified separately
                                    				to be assigned different skills.

Modify Existing Contact
                                       				  Service Queues —Choose this submenu to modify skills that are associated
                                    				with a contact service queue. In this step, you are transferred to the RmCm
                                    				Configuration Contact Service Queue web page, which lists the configured CSQs.

Add a Contact Service
                                       				  Queue —Choose this submenu to add contact service queues. Skills or resource
                                    				groups are associated to these contact service queues to filter out the
                                    				resources. In this step, you are transferred to the RmCm Configuration Contact
                                    				Service Queue Configuration web page, which allows you to add CSQs.

Modify Existing
                                       				  Teams —Choose this submenu to modify agents in existing teams. In this step,
                                    				you are transferred to the RmCm Configuration Contact Teams web page, which
                                    				lists the configured teams.

Add a Team —Choose this
                                    				submenu to create new teams and associate those teams with new agents. In this
                                    				step, you are transferred to the RmCm Configuration Team Configuration web
                                    				page, which allows you to create new teams.

Create an
                                       				  Application —On completing the RmCm configuration, you can optionally
                                    				proceed to the Application Wizard configuration.

| Note | The RmCm Wizard
                                          			 option is available with all Unified CCX license packages. |
|---|---|