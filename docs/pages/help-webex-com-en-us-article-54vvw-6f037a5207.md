---
doc_id: help-webex-com-en-us-article-54vvw-6f037a5207
source_url: https://help.webex.com/en-us/article/54vvw
retrieved_at: 2026-11-02T13:00:09.169923+00:00
---

## Prerequisites

The minimum supported size for the softphone interface is 500px. Any value lower than 500px may result in display or functionality issues.

Before you integrate Webex Contact Center with the ServiceNow CRM console, ensure that you have the following:

Access to Webex Contact Center.

Administrator access to the Control Hub at https://admin.webex.com and the Webex Contact Center Management Portal. The URLs for the Management Portal are specific to your region.

An agent with access to the Desktop. The URL for the Desktop is specific to your region.

Agent access to the following domain that is added in the Content Security Policy Allowed List:

*.service-now.com

For more information on how to define the allowed list, see the article Security Settings for Webex Contact Center .

A ServiceNow developer portal account. To create an account, go to the ServiceNow developer portal at https://developer.servicenow.com/dev.do and click Sign up and Start Building .

Access to the following files at https://github.com/CiscoDevNet/webex-contact-center-crm-integrations/tree/main/ServiceNow :

ServiceNow Update Set (XML)

ServiceNow Contact Center Desktop Layout (JSON)

- The ServiceNow editions that Webex Contact Center supports are Vancouver, Utah, Tokya, Washington, and Xanadu. For more information, see Webex Contact Center Integration with ServiceNow .

Follow one of the two methods below:

- For developer instances, we recommend following the steps under the developer instance guide.

- If you own an enterprise-licensed instance, follow the guidelines for enterprise-licensed instances.

We do not recommend mixing the enterprise-licensed app with developer sandbox instances.

Digital channels such as chat and email are not supported with CRM connectors. This applies to all CRM integrations using these connectors. Please plan your deployment and customer engagement workflows accordingly.

Install ServiceNow for developer instances

The following sections describe the steps to install the ServiceNow connector for developer instances.

Install the OpenFrame Interface

Sign in to your ServiceNow developer portal account and open the Administration console.

From the My Instance area of the Account menu, click Start Building .

On your developer instance, from the Filter navigator field at the upper left of the window, navigate to Plugins .

Search for the Openframe plugin that has the title Openframe . You may need to scroll through the list.

Click Install to install the Openframe plugin.

In the Activate Plugin dialog box, click Activate .

When the plugin activation is completed, click Close & Reload Form in the Plugin Activation dialog box.

To verify the plugin activation, from the Filter navigator field at the upper left of the window, navigate to OpenFrame .

Click Configurations and ensure that the OpenFrame plugin appears in the OpenFrame Configurations list.

Commit the Update Set

Download the latest System Update Set XML file available on the github repo at this location : https://github.com/CiscoDevNet/webex-contact-center-crm-integrations/tree/main/ServiceNow .

File Name : webexcc-servicenow-update-setV(X).xml

On your ServiceNow instance, from the Filter navigator field at the upper left of the window, navigate to System Update Sets > Update Sets to Commit .

Click the Import Update Set from XML link.

Click Choose File , select the System Update Set XML file, and then click Upload .

The update set appears in the Retrieved Update Sets list and is in the Loaded state.

From the Retrieved Update Sets list, click the Update Set File Name (link) to open the Update Set.

At the upper right of the window, click Preview Update Set to check the update set for issues.

Click Close on the Update Set Preview dialog box once preview is completed.

Click Commit Update Set .

Click Close on the Update Set
                        Commit dialog box once committing of Update Set is
                    completed.

Edit the System Properties

In the Filter navigator field at the upper left of the window, type sys_properties.list and press enter.

On the System Properties page, sort the properties by updated date. Ensure that you can see the following Webex Contact Center properties:

Click agentdesktop_url to open the System Property agentdesktop_url page.

In the Value field, enter the URL for the Webex Contact Center
                    Desktop according to the region of operation.

Click Update to save the changes.

(Optional) To change the Activity table name, edit the webexccactivitytable properties as required.

On the System Properties page, click on webexccactivitytable .

Change the Value field as required.

(Optional) Add User Groups in the following ways:

In the Filter navigator field at the upper left of the window, navigate to Groups under System Security.

Create a new user group or use an existing one.

Click Edit .

Search for sn_openframe_user under Collection and move it to your user group.

Click Save .

Add the user as a group member.

Create the OpenFrame Configuration

From the Filter navigator field, navigate to OpenFrame > Configurations .

Click New .

Enter the following properties for the URL:

Name : Webex Contact Center Desktop

Title : Webex Contact Center

Width : 550 (Recommended)

Height : 600 (Recommended)

To the right of the URL field, click the Lock button and add agentdesktop.do as the URL. (Do this step to point configuration to the UI Page)

(Optional) Select the User / Agent Group(s) to assign the configuration.

Click Submit . The URL appears as a link.

Before you attempt to use the OpenFrame phone, ensure that you upload the ServiceNow custom Desktop Layout JSON file to the Webex Contact Center Management Portal. For more information, see Set Up the ServiceNow Desktop Layout on Webex Contact Center .

Set up the ServiceNow Desktop Layout on Webex Contact Center

Download the Desktop layout for ServiceNow from https://github.com/CiscoDevNet/webex-contact-center-crm-integrations/tree/main/ServiceNow .

Update the properties in the Desktop Layout file, if required.

Go to the Webex Contact Center Management Portal.

From the Management Portal navigation bar, choose Provisioning > Desktop Layout .

Click New Layout and enter the details for the desktop layout.

Upload the ServiceNow Desktop Layout JSON file.

Click Save to save the configuration.

You can now start the Webex Contact Center
                        Desktop within the ServiceNow console.

From the Filter navigator field, navigate to Service Operations Workspace .

Install ServiceNow for licensed enterprise instances

The following sections describe the steps to install the ServiceNow connector for licensed enterprise instances.

Install the OpenFrame Interface

Sign in to your ServiceNow developer portal account and open the Administration console.

From the My Instance area of the Account menu, click Start Building .

On your developer instance, from the Filter navigator field at the upper left of the window, navigate to Plugins .

Search for the Openframe plugin that has the title Openframe . You may need to scroll through the list.

Click Install to install the Openframe plugin.

In the Activate Plugin dialog box, click Activate .

When the plugin activation is completed, click Close & Reload Form in the Plugin Activation dialog box.

To verify the plugin activation, from the Filter navigator field at the upper left of the window, navigate to OpenFrame .

Click Configurations and ensure that the OpenFrame plugin appears in the OpenFrame Configurations list.

Install the Webex Contact Center application

Instances that have enterprise licenses can install the Webex Contact Center application directly from the ServiceNow Store.

Download and install the Webex Contact Center package from the ServiceNow store: https://store.servicenow.com/sn_appstore_store.do#!/store/application/6c8e2a4edbc73410e1c75e25ca961947 .

Edit the System Properties

In the Filter navigator field at the upper left of the window, enter sys_properties.list .

On the System Properties page, sort the properties by updated date. Ensure that you can see the following Webex Contact Center properties:

Click agentdesktop_url to open the System Property agentdesktop_url page.

In the Value field, enter the URL for the Webex Contact Center
                    Desktop according to the region of operation.

Click Update to save the changes.

(Optional) To change the Activity table name, edit the x_caci_webexcc.webexccactivitytable properties as required.

On the System Properties page, click on x_caci_webexcc.webexccactivitytable .

Change the Value field as required.

(Optional) Add User Groups in the following ways:

In the Filter navigator field at the upper left of the window, navigate to Groups under System Security .

Click Edit and add the following roles:

sn_openframe_user

x_caci_webexcc.agent

agent_workspace_user

x_caci_webexcc.webexcc_imp_activity_user

x_caci_webexcc.webex_contact_center

Create the OpenFrame Configuration

From the Filter navigator field, navigate to OpenFrame > Configurations .

Click New .

Enter the following properties for the URL:

Name : Webex Contact Center Desktop

Title : Webex Contact Center

Width : 550 (Recommended)

Height : 600 (Recommended)

To the right of the URL field, click the Lock button and add x_caci_webexcc_agentdesktop.do as the URL. (Do this step to point configuration to the UI Page)

(Optional) Select the User / Agent Group(s) to assign the configuration.

Click Submit . The URL appears as a link.

From the Filter navigator field, navigate to Service Operations Workspace .

(Optional) In the User Group list, move the user groups that can access the Webex Contact Center
                    Desktop from Available to Selected .

Before you attempt to use the OpenFrame phone, ensure that you upload the ServiceNow custom Desktop Layout JSON file to the Webex Contact Center Management Portal. For more information, see Set Up the ServiceNow Desktop Layout on Webex Contact Center .

Set up the ServiceNow Desktop Layout on Webex Contact Center

Download the Desktop layout for ServiceNow from https://github.com/CiscoDevNet/webex-contact-center-crm-integrations/tree/main/ServiceNow .

Update the properties in the Desktop Layout file, if required.

Go to the Webex Contact Center Management Portal.

From the Management Portal navigation bar, choose Provisioning > Desktop Layout .

Click New Layout and enter the details for the desktop layout.

Upload the ServiceNow Desktop Layout JSON file.

Click Save to save the configuration.

You can now start the Webex Contact Center
                        Desktop within the ServiceNow console.

From the Filter navigator field, navigate to Service Operations Workspace .

Configure Click to Dial on Incident Module

From the Filter navigator field, navigate to Incidents > Open Incident.

Right click on the caller field and click Configure Dictionary .

Add comma separated Attributes “ref_contributions=show_phone, .

You can now start using the Webex Contact Center Desktop within the ServiceNow console.

From the Filter navigator field, navigate to Service Operations Workspace .

- We support signing into Agent Desktop using WebRTC for Salesforce (SFDC) and Microsoft Dynamics (MS Dynamics) Connectors only.

- Currently, this feature is applicable to agents only.

## Agent Desktop in the ServiceNow Console

Before you make outdial calls, ensure that you do the following:

Create the outdial entry point and set up an outdial entry point strategy.

Enable outdial ANI for the Agent Profile.

Set the outdial ANI to a Dial Number-to-Entry Point mapping.

For more information, see the Provisioning chapter of the Cisco Webex Contact Center Setup and Administration Guide .

From the Filter navigator field, navigate to Service Operations Workspace .

For information on how to use Desktop, see the Agent tab in the Webex Contact Center help.

## Overview

This article covers several ways to customize your business rules for the ServiceNow CRM connector. It details how you can customize the use cases based on business rules that are specific to ServiceNow.

The customer must self manage these use cases on ServiceNow. The configuration is specific to ServiceNow and not Webex Contact Center software or expertise.

This is a reference documentation to aid the modification of business rules. The ServiceNow developers will create and manage the business rules, and provide support.

Cisco only provides sample documentation.

Set up and Manage Actions Widget

The following sections provide details about how to set up, enable, and manage Actions widget for developer and enterprise instances.

### Commit the Update Set for Actions Widget

For the licensed enterprise instances, install the latest Webex Contact Center app from the ServiceNow store .

To set up the Actions widget for the developer instances, download the latest System Update Set XML file available on the github repo at this location: https://github.com/CiscoDevNet/webex-contact-center-crm-integrations/tree/main/ServiceNow/ActionsWidget . The file name is webexcc-servicenow-update-setv7-1-ActionsWidget.xml. To commit the update set for the Actions widget, see steps 2 to 9 in Commit the Update Set .

### Enable Actions Widget

Use the isWidgetDisplayEnabled property to enable the Actions widget. You must not modify this property's value in the custom desktop layout's headless section. The property is always set to false in the custom desktop layout's headless section. You should update the property's value only in the panel section of the custom desktop layout.

Once you enable the Actions widget in the custom desktop layout, you can perform the following actions:

- Manage activity records—Click View/Edit Activity Record to view the list of activity records associated with the caller.

- Associate CRM objects—Click Associate to activity records to add CRM objects such as call type (inbound or outbound), call object, call notes, and so on to the activity record.

```
{
              "comp": "md-tab-panel",
              "attributes": { "slot": "panel", "class": "widget-pane" },
              "children": [
                {
                  "comp": "agentx-custom-desktop",
                  "script": "https://cx-crmconnector.ciscoccservice.com/servicenow/v5/dist/index.js",
                  "properties": {
                    "isWidgetDisplayEnabled": true,
                    "typeOfRecord" : "Create Incident" 
                  },
                  "wrapper": {
                    "title": "SNOW Actions !",
                    "maximizeAreaName": "app-maximize-area"
                  }
                }
              ]
            }
```

- Add live call notes—You can capture additional information about the call in the text area and wrap-up the call. You can see these notes added as call notes in the activity record.

Auto open incident on a current interaction record

### Code change on ServiceNow

Go to filter navigator and search for script includes .

Select the Script Includes under System UI .

Filter the Name and search for propUtils .

Change the method UserGetSysId in the Script .

Curent:

```
UserGetSysId : function () {
var opened_for;
var user = new GlideRecord("sys_user");
user.addQuery(this.getParameter('field'),this.getParameter('value'));
user.query();
if (user.next())
opened_for=user.sys_id;
var grInt = new GlideRecord('interaction');
grInt.initialize();
grInt.assigned_to= gs.getUserID();
grInt.type= 'phone';
grInt.opened_for= opened_for;
var sysid=grInt.insert();
return sysid;
},
```

New sample code for the incident:

```
UserGetSysId : function () {
            var opened_for;

        //Incident related changes
             var sysidlist = {};
            var user = new GlideRecordSecure("sys_user");
              user.addQuery(this.getParameter('field'),this.getParameter('value'));
              user.query();
              if(user.next()) {
                 opened_for=user.sys_id;//return user.sys_id;
                    var inc = new GlideRecordSecure('incident');
                            inc.addQuery('caller_id', opened_for);
                            inc.addQuery('state','IN','1,2');
                            inc.orderByDesc('sys_created_on');
                            inc.query();
                                if (inc.next()) {
                                    sysidlist.incsysid=inc.getUniqueValue();
                               }else{
                                    inc.initialize();
                                    inc.caller_id=opened_for;
                                    inc.contact_type='phone';
                                    inc.short_description='Call Received From '+ this.getParameter('value');
                                    sysidlist.incsysid=inc.insert();
                                }
              } 
            var grInt = new GlideRecordSecure('interaction');
                grInt.initialize(); 
                grInt.assigned_to= gs.getUserID(); 
                grInt.type= 'phone'; 
                grInt.opened_for= opened_for; 
            var sysid=grInt.insert();
            sysidlist.sysid=sysid;
            
            return JSON.stringify(sysidlist);
        },
```

Go to filter navigator and search for UI page .

Select UI pages under System UI .

Filter the Name and search for agentdesktop .

Change the screenpop function in Client script .

Current function:

```
// screen pop
function screenpop(callerani,callSessionInfo) {

if(callerani===callSessionInfo.phoneNumber){
callerani=stripPrefixes(callerani);
}
var gaout = new GlideAjax('propUtils');
gaout.addParam('sysparm_name', 'UserGetSysId');
gaout.addParam('field', 'phone');
gaout.addParam('value', callerani);
gaout.getXMLWait();

var sysid = gaout.getAnswer();
  
openFrameAPI.openServiceNowForm({
entity: 'interaction',
query: 'sys_id='+sysid
});
```

Sample code for the incident:

```
// screen pop
function screenpop(callerani,callSessionInfo) {
   

    if(callerani===callSessionInfo.phoneNumber){
        callerani=stripPrefixes(callerani);
    }
    
    var gaout = new GlideAjax('propUtils');
        gaout.addParam('sysparm_name', 'UserGetSysId');
        gaout.addParam('field', 'phone');
        gaout.addParam('value', callerani);
        gaout.getXMLWait();

// For Incident-related change
      var sysObj = JSON.parse(gaout.getAnswer());
    
    if(sysObj.incsysid){
        openFrameAPI.openServiceNowForm({
        entity: 'incident',
        query: 'sys_id='+sysObj.incsysid, 
        'interaction_sys_id': sysObj.sysid  
       });
    }else{
        openFrameAPI.openServiceNowForm({
        entity: 'incident',
        query: 'sys_id=-1',
        'interaction_sys_id': sysObj.sysid //'a2ba0ba62fd121106446cc96f699b6b8'  
       });
    }
   
}
```

### If the caller information exists in CRM, and there is already a new incident opened with this contact, application opens the inprogress incident

### If the caller information does not exist in CRM, the application opens a new incident

### If the caller information exists in CRM, the application opens a new incident with prefilled details

Add CAD variable in phone log table

### Overview

This use case details the process to add an extra column to the ServiceNow table - webexcc_imp_activity and create sn_openframe_phone_log upon the installation of the Webex CC for ServiceNow CRM Connector.

By default, the table contains certain out of the box system fields and values.

You can create more business-specific variables (CAD Variables) inside of the WebexCC Flow designer and add the CAD variables inside of the ServiceNow post call activity log, as well as persist this to the post call activity table data.

This is a reference documentation only - and shows how to do this for a sample CAD variable called Customer Name that stores the customer name inside the IVR and posts this to ServiceNow.

It is expected that the partner+customer ServiceNow developers will configure and manage this configuration as it is a customization to the existing connector.

Cisco only provides the techniques on how to customize and extend the connector.

As of this article, the Cisco team has validated support for the addition of CAD variable to the Activity Log and Activity Table using the technique described below:

### Add Column to WebexCC IMP Activity

Edit the table in the developer version of ServiceNow.

Go to the filter navigator and search for studio.

Select Webex Contact Center

or

Select the WebexCC IMP Activity table

Add a new column, for example, CustomerName

### Add Column to Phone Log

Edit the phone log table.

Add a new column, for example, CustomerName .

### WebexCC Activity Transform Map

Add a new column, for example, CustomerName field mapping.

Personalize List Columns

As Service Now recommends, change the Choice action from create to ignore.

### Configure phone logs list

### Go to Script Include

Add only one line webexcc.u_customername=actInfo.CustomerName to propUtils.

See the line: webexcc.u_customername=actInfo.CustomerName; with a supporting comment.

```
var propUtils = Class.create();
propUtils.prototype = Object.extendsObject(global.AbstractAjaxProcessor,{
         getWebexccProp : function () {
           var webexccprop = {};
           webexccprop.instanceurl= 'https://'+gs.getProperty('instance_name')+'.service-now.com/';
           webexccprop.url=gs.getProperty('x_caci_webexcc.agentdesktop_url');
          // webexccprop.popupurl=gs.getProperty('x_caci_webexcc.screenpop_url');
           return  JSON.stringify(webexccprop);
      
        },
        UserGetSysId : function () {
            var opened_for;
            var user = new GlideRecord("sys_user");
              user.addQuery(this.getParameter('field'),this.getParameter('value'));
              user.query();
              if (user.next())
                 opened_for=user.sys_id;//return user.sys_id;
//            else
//               return null;
            var grInt = new GlideRecord('interaction');
                grInt.initialize();
                grInt.assigned_to= gs.getUserID();
                grInt.type= 'phone';
                grInt.opened_for= opened_for;
            var sysid=grInt.insert();
            return sysid;
        },
        setWebexcctable : function () {
            var sys_id=0;
             
            var actInfo = JSON.parse(this.getParameter('actInfo'));
            var webexcc = new GlideRecordSecure(gs.getProperty('x_caci_webexcc.webexccactivitytable'));
            webexcc.addQuery("callobject", actInfo.CallObject);
            webexcc.query();
            if(!webexcc.next()) {
                webexcc.ani = actInfo.ani;
                webexcc.dnis =actInfo.dnis;
                webexcc.queuename =actInfo.queuename;
                webexcc.wrapuptime =actInfo.wrapuptime;
                webexcc.callduration =actInfo.CallDurationInSeconds;
                webexcc.ringingtime =actInfo.ringingtime;
                webexcc.activitydate =actInfo.ActivityDate;
                webexcc.callobject =actInfo.CallObject;
                webexcc.calltype =actInfo.CallType;
                webexcc.calldisposition=actInfo.CallDisposition;
                 
                // This line is Added - to capture it in the Activity Log
               webexcc.u_customername=actInfo.CustomerName;
                 
                sys_id=webexcc.insert();
 
                //Activities on Incident record;
                var actInfoString =this.getParameter('actInfo');
                var suser = new GlideRecordSecure("sys_user");
                    suser.addQuery("phone", this.getParameter('ani'));
                    suser.query();
                    if(suser.next()) {
                    var inc = new GlideRecordSecure('incident');
                            inc.addQuery('caller_id', suser.sys_id);
                            inc.orderByDesc('sys_created_on');
                            inc.query();
                                if (inc.next()) {
                                    var jsonPretty = JSON.stringify(JSON.parse(actInfoString),null,2); 
                                    inc.comments =jsonPretty;
                                inc.update();
     
                            }
                    }
            }  
            return sys_id;
       },
 
    type: 'propUtils'
});
```

### Create a CAD variable in Flow designer

### Add the CAD variable to the Desktop Layout

Example

```
"CadName1:SnowField1,CadName2:SnowField2"
 CadName1 is CustomerName
 SnowField1 is also used as CustomerName which is part of sample scirpt showen above "actInfo.CustomerName".
```

### Demo screenshots

View the newly added CAD variable in the WebexCC Activity table.

Auto Prefill CAD values in an Incident Record

### Create CAD variable for Flow Designer

Incident impact

### Service Now script update

Updates to the Script Includes

Go to the filter navigator and search for script includes

Select the Script Includes option under System UI .

Filter the Name with propUtils .

Change the method UserGetSysId in the Script field.

Current script:

```
UserGetSysId : function () {
var opened_for;
var user = new GlideRecord("sys_user");
user.addQuery(this.getParameter('field'),this.getParameter('value'));
user.query();
if (user.next())
opened_for=user.sys_id;
var grInt = new GlideRecord('interaction');
grInt.initialize();
grInt.assigned_to= gs.getUserID();
grInt.type= 'phone';
grInt.opened_for= opened_for;
var sysid=grInt.insert();
return sysid;
},
```

New sample code for the incident:

```
UserGetSysId : function () {
            var opened_for;
            
            var sysidlist = {};
            var user = new GlideRecordSecure("sys_user");
              user.addQuery(this.getParameter('field'),this.getParameter('value'));
              user.query();
              if(user.next()) {
                 opened_for=user.sys_id;//return user.sys_id;
                    var inc = new GlideRecordSecure('incident');
                            inc.addQuery('caller_id', opened_for);
                            inc.addQuery('state','IN','1,2');
                            inc.orderByDesc('sys_created_on');
                            inc.query();
                                if (inc.next()) {
                                    sysidlist.incsysid=inc.getUniqueValue();
                               }else{
                                    inc.initialize();
                                    inc.caller_id=opened_for;
                                    inc.contact_type='phone';
                                    inc.urgency=this.getParameter('IncUrgency');
                                    inc.impact=this.getParameter('Impact');
                                    inc.short_description='Call Received From '+ this.getParameter('value');
                                    sysidlist.incsysid=inc.insert();
                                }
              } 
            var grInt = new GlideRecordSecure('interaction');
                grInt.initialize(); 
                grInt.assigned_to= gs.getUserID(); 
                grInt.type= 'phone'; 
                grInt.opened_for= opened_for; 
            var sysid=grInt.insert();
            sysidlist.sysid=sysid;
            
            return JSON.stringify(sysidlist);//sysid;
        },
```

Go to the filter navigator and search for UI pages .

Select the UI Pages option under System UI .

Filter the UI Pages with Name and search for agentdesktop .

Change the screenpop function in the script field.

Current function:

```
// screen pop
function screenpop(callerani,callSessionInfo) {

if(callerani===callSessionInfo.phoneNumber){
callerani=stripPrefixes(callerani);
}
var gaout = new GlideAjax('propUtils');
gaout.addParam('sysparm_name', 'UserGetSysId');
gaout.addParam('field', 'phone');
gaout.addParam('value', callerani);
gaout.getXMLWait();

var sysid = gaout.getAnswer();
  
openFrameAPI.openServiceNowForm({
entity: 'interaction',
query: 'sys_id='+sysid
});

}
```

Sample code for the incident:

```
// screen pop
function screenpop(callerani,callSessionInfo) {
   
    var Impact=3;
    if(callSessionInfo.callAssociatedData.Impact != null && callSessionInfo.callAssociatedData.Impact != undefined)
    {
        Impact=callSessionInfo.callAssociatedData.Impact.value;
    }
    var IncUrgency=3;
    if(callSessionInfo.callAssociatedData.Urgency != null && callSessionInfo.callAssociatedData.Urgency != undefined)
    {
        IncUrgency=callSessionInfo.callAssociatedData.Urgency.value;
    }
    if(callerani===callSessionInfo.phoneNumber){
        callerani=stripPrefixes(callerani);
    }
    
    var gaout = new GlideAjax('propUtils');
        gaout.addParam('sysparm_name', 'UserGetSysId');
        gaout.addParam('field', 'phone');
        gaout.addParam('value', callerani);
        gaout.addParam('IncUrgency', IncUrgency);
        gaout.addParam('Impact', Impact);
        gaout.getXMLWait();
      // var sysid = gaout.getAnswer();
      var sysObj = JSON.parse(gaout.getAnswer());
    
    if(sysObj.incsysid){
        openFrameAPI.openServiceNowForm({
        entity: 'incident',
        query: 'sys_id='+sysObj.incsysid, 
        'interaction_sys_id': sysObj.sysid  
       });
    }else{
        openFrameAPI.openServiceNowForm({
        entity: 'incident',
        query: 'sys_id=-1',
        'interaction_sys_id': sysObj.sysid  
       });
    }
    window.localStorage.setItem("screenpopinteraction",JSON.stringify(sysObj));
   
}
```

### If the caller information exists in CRM, and there is no new or inprogress incident then the application opens a new incident

Insert interaction number and incident number in phone log table

### Change the code on ServiceNow

### Add new columns to the WebexCC IMP Activity table

Click on Update .

### Add new columns to the Phone Log table

Open the Phone Log table

### WebexCC Activity Transform Map

Open transform map from the filter navigator

Click on WebexCC Activity TransformMap

Click Update .

### Changes to Script Includes

Go to filter navigator and search for "script includes".

Select the Script Includes under System UI .

Filter the Name with propUtils .

Change the method setWebexcctable .

New sample code for Incident:

```
setWebexcctable : function () {
            var sys_id=0;
            
            var actInfo = JSON.parse(this.getParameter('actInfo'));
            var webexcc = new GlideRecordSecure(gs.getProperty('webexccactivitytable'));
            webexcc.addQuery("u_callobject", actInfo.CallObject);
            webexcc.query();
            if(!webexcc.next()) {
                
                //Activities on Incident record;
                //var actInfoString =this.getParameter('actInfo');
                var incsysid=actInfo.incident_sys_id;
                var interactionsysid=actInfo.interaction_sys_id;
                var incnum="";
                var intenum="";
                delete actInfo['interaction_sys_id'];
                delete actInfo['incident_sys_id'];
                if( interactionsysid!= null && interactionsysid != undefined){
                    var inte = new GlideRecordSecure('interaction');
                    //inte.get('sys_id', interactionsysid );
                    
                    inte.addQuery('sys_id', interactionsysid );
                    inte.query();
                    if (inte.next()) {
                        intenum=inte.number;
                       // inte.setValue('state','Closed Complete');
                        inte.work_notes='Update State to closed.';
                        inte.update();
    
                    }
                }
                if( incsysid!= null && incsysid != undefined){
                    var inci = new GlideRecordSecure('incident');
                    inci.addQuery('sys_id', incsysid );
                    inci.query();
                    if (inci.next()) {
                        incnum=inci.number;
                        var jsonPretty = JSON.stringify(actInfo,null,2); //JSON.stringify(JSON.parse(actInfoString),null,2);  
                        inci.comments =jsonPretty;
                        inci.update();
    
                    }
                }else{
                  var suser = new GlideRecordSecure("sys_user");
                    suser.addQuery("phone", this.getParameter('ani'));
                    suser.query();
                    if(suser.next()) {
                    var inc = new GlideRecordSecure('incident');
                            inc.addQuery('caller_id', suser.sys_id);
                            inc.addQuery('state','IN','1,2');
                            inc.orderByDesc('sys_created_on');
                            inc.query();
                                if (inc.next()) {
                                    var jsonPretty = JSON.stringify(actInfo,null,2);  
                                    inc.comments =jsonPretty;
                                inc.update();
    
                            }
                    } 
                }
               
                
                webexcc.u_ani = actInfo.ani;
                webexcc.u_dnis =actInfo.dnis;
                webexcc.u_queuename =actInfo.queuename;
                webexcc.u_wrapuptime =actInfo.wrapuptime;
                webexcc.u_callduration =actInfo.CallDurationInSeconds;
                webexcc.u_ringingtime =actInfo.ringingtime;
                webexcc.u_activitydate =actInfo.ActivityDate;
                webexcc.u_callobject =actInfo.CallObject;
                webexcc.u_calltype =actInfo.CallType;
                webexcc.u_calldisposition=actInfo.CallDisposition;
                webexcc.u_incidentnumber=incnum;
                webexcc.u_interactionsnumber=intenum;
                sys_id=webexcc.insert();

                
                            
            }    
            return sys_id;
       },
```

### Method changes on UI pages

Go to filter navigator and search for UI pages

Select the UI Pages option under System UI .

Filter the UI Pages with Name and search for agentdesktop .

Change the nowActivities and screenpop function in the script.

Current function:

```
function nowActivities(actInfo, ani) {
    
    var gaout = new GlideAjax('propUtils');
    gaout.addParam('sysparm_name', 'setWebexcctable');
    gaout.addParam('actInfo', JSON.stringify(actInfo));
    gaout.addParam('ani', stripPrefixes(ani));
    gaout.getXML(SetCCsysId);

}
```

Sample code for the incident:

```
function nowActivities(actInfo, ani) {
    var sysObjstr = window.localStorage.getItem("screenpopinteraction");
    if(sysObjstr != null && sysObjstr != undefined)
    {
        var sysObjjson=JSON.parse(sysObjstr);
        actInfo.interaction_sys_id=sysObjjson.sysid;
        actInfo.incident_sys_id=sysObjjson.incsysid;
    }
    var gaout = new GlideAjax('propUtils');
    gaout.addParam('sysparm_name', 'setWebexcctable');
    gaout.addParam('actInfo', JSON.stringify(actInfo));
    gaout.addParam('ani', stripPrefixes(ani));
    gaout.getXML(SetCCsysId);

}

function screenpop(callerani,callSessionInfo) {
   

    if(callerani===callSessionInfo.phoneNumber){
        callerani=stripPrefixes(callerani);
    }
    
    var gaout = new GlideAjax('propUtils');
        gaout.addParam('sysparm_name', 'UserGetSysId');
        gaout.addParam('field', 'phone');
        gaout.addParam('value', callerani);
        gaout.getXMLWait();
      // var sysid = gaout.getAnswer();
      var sysObj = JSON.parse(gaout.getAnswer());
    
    if(sysObj.incsysid){
        openFrameAPI.openServiceNowForm({
        entity: 'incident',
        query: 'sys_id='+sysObj.incsysid, 
        'interaction_sys_id': sysObj.sysid  
       });
    }else{
        openFrameAPI.openServiceNowForm({
        entity: 'incident',
        query: 'sys_id=-1',
        'interaction_sys_id': sysObj.sysid  
       });
    }
    window.localStorage.setItem("screenpopinteraction",JSON.stringify(sysObj));
        
   
}
```

### Results after the update

Customizations for legacy versions

The following customizations apply to versions 1.0.5 and below. For the customizations for the newer versions 1.0.7 and above, follow the steps above.

### Customization # 1 - Add custom business rules for call flow use cases

For every new call into the WebexCC CRM connector in ServiceNow, create a New Incident Record.

Search for Business Rules on the Filter navigator

Click New.

Sample code for reference:

```
function customcti() {
            var url = null;
            var name = sysparm_caller_name;
            eid = sysparm_caller_id;
            var phone = sysparm_caller_phone;
            var taskID = sysparm_task_id;
            var fQuery = sysparm_query;
            if (fQuery == null)
               fQuery = '';
            var view = sysparm_view;
            if (view == null || view == '')
                view = "itil";
 
            var userID = null;
            if (eid != null && eid != '') {
                userID = UserGetSysId("employee_number",eid);
            }
            if (userID == null && name != null && name != '') {
                userID = UserGetSysId("name", name);                
            }
            if (userID == null && phone != null && phone != '') {
                userID = UserGetSysId("phone", phone);
            }
 
            if (userID != null) {
                if (fQuery.length > 0)
                    fQuery += "^";
                fQuery += "caller_id=" + userID;
            }
            if (url == null) {
                url = "incident.do?sys_id=-1";
                if (fQuery != null)
                   url += "&sysparm_query=" + fQuery;
            }
            answer = url;
            return url;
}
 
function UserGetSysId(field, value) {
  var user = new GlideRecord("sys_user");
  user.addQuery(field, value);
  user.query();
  if (user.next())
     return user.sys_id;
  else
     return null;
}
```

Sample configuration of the business rule

Enable Client callable

Computer Telephony Integration (CTI) Processing For Incident is marked as True .

Update the screenpop url with the custom CTI Rule " cti.do?sysparm_cti_rule=createIncident&sysparm_caller_phone= "

The sysparm_cti_rule=name where ' name ' is the name of a function is to be invoked for CTI Processing rather than using the default script.

Define the function in a sys_script entry marked client callable .

If you must insert, update, or delete any GlideRecord(s) in the function, call a separate nonclient callable function to perform the updates.

To make a script client-callable, you must check the client-callable check box on the form that displays when the sys_script entry is displayed.

The client-callable check box doesn't show up by default. To view, you must modify the fields that show on the form using the gear icon and slush bucket mechanism.

https://docs.servicenow.com/en-US/bundle/tokyo-application-development/page/script/business-rules/concept/c_BusinessRules.html

https://docs.servicenow.com/bundle/tokyo-platform-administration/page/integrate/incident/reference/r_ComputerTelephonyIntegration.html

### Customization # 2 - Add CAD variable in Webex Contact Center activity table

This article details the process to add an additional column to the ServiceNow table - webexcc_activity that is created upon the installation of the Webex CC for ServiceNow CRM Connector.

By default, the table contains out-of-box system fields and values.

You can potentially create more business-specific variables (CAD Variables) inside the WebexCC Flow designer and add those CAD variables inside the ServiceNow post call activity log , and persist this to the post call activity table data.

This is reference documentation only - and shows how to do this for a sample CAD variable called Customer Name that stores the customer name inside the IVR and posts this to ServiceNow.

The partner+customer ServiceNow developers will configure and manage this configuration as it is a customization to the existing connector.

Cisco will only provide the techniques on how to customize and extend the connector.

As of this article, the Cisco team has validated support for the addition of CAD variable to the Activity Log and Activity Table using the technique described below.

Edit the table in the developer version of ServiceNow.

Go to the Studio > Webex Contact Center .

Select WebexCC Activity table.

For example, CustomerName .

Select List Layout for WebexCC Activity .

This step is not required if you are using the Update Set XML - Only one line is required to be added " webexcc.u_customername=actInfo.CustomerName " to propUtils.

Sample script

See the line with: webexcc.u_customername=actInfo.CustomerName; with a supporting comment.

```
var propUtils2 = Class.create();
propUtils2.prototype = Object.extendsObject(global.AbstractAjaxProcessor,{
         getWebexccProp : function () {
           var webexccprop = {};
           webexccprop.instanceurl= 'https://'+gs.getProperty('instance_name')+'.service-now.com/';
           webexccprop.url=gs.getProperty('x_caci_webexcc.agentdesktop_url');
           webexccprop.popupurl=gs.getProperty('x_caci_webexcc.screenpop_url');
           return  JSON.stringify(webexccprop);
      
        },
        setWebexcctable : function () {
            var sys_id=0;
             
            var actInfo = JSON.parse(this.getParameter('actInfo'));
            var webexcc = new GlideRecordSecure(gs.getProperty('x_caci_webexcc.webexccactivitytable'));
            webexcc.addQuery("callobject", actInfo.CallObject);
            webexcc.query();
            if(!webexcc.next()) {
                webexcc.ani = actInfo.ani;
                webexcc.dnis =actInfo.dnis; 
                webexcc.queuename =actInfo.queuename;
                webexcc.wrapuptime =actInfo.wrapuptime;
                webexcc.callduration =actInfo.CallDurationInSeconds;
                webexcc.ringingtime =actInfo.ringingtime;
                webexcc.activitydate =actInfo.ActivityDate;
                webexcc.callobject =actInfo.CallObject;
                webexcc.calltype =actInfo.CallType;
                webexcc.calldisposition=actInfo.CallDisposition;
 
               // This line is Added - to capture it in the Activity Log
               webexcc.u_customername=actInfo.CustomerName;
 
                sys_id=webexcc.insert();
  
                // Activities on Incident record;
                var actInfoString =this.getParameter('actInfo');
                var suser = new GlideRecordSecure("sys_user");
                    suser.addQuery("phone", this.getParameter('ani'));
                    suser.query();
                    if(suser.next()) {
                    var inc = new GlideRecordSecure('incident');
                            inc.addQuery('caller_id', suser.sys_id);
                            inc.orderByDesc('sys_created_on');
                            inc.query();
                                if (inc.next()) {
                                    var jsonPretty = JSON.stringify(JSON.parse(acting string),null,2);  
                                    inc.comments =jsonPretty;
                                inc.update();
                                 }
                    } 
            }    
            return sys_id;
       },
 
    type: 'propUtils2'
});
```

Create a CAD variable in Flow designer

Add the CAD variable to the Desktop Layout

Demo screenshots

View the newly added CAD variable in the WebexCC Activity table.

The CRM connector operates based on the version of the widget specified in the desktop layout JSON. It is extremely important to ensure the widget version within the Desktop Layout is kept updated.

Administrators are expected to ensure all desktop layouts for this CRM connector use this widget version. If the layout is not updated to use the latest version, functionality will no longer be supported and may cease to work correctly.

- Last ServiceNow update—ServiceNow_Desktop_0.1.0_v5.0.3.json. As of March 2024, package version is 1.0.9

- Last XML update—webexcc-servicenow-update-setv7-1-ActionsWidget.xml, June 2024

| 1 | Sign in to your ServiceNow developer portal account and open the Administration console. |
|---|---|
| 2 | From the My Instance area of the Account menu, click Start Building . |
| 3 | On your developer instance, from the Filter navigator field at the upper left of the window, navigate to Plugins . |
| 4 | Search for the Openframe plugin that has the title Openframe . You may need to scroll through the list. |
| 5 | Click Install to install the Openframe plugin. |
| 6 | In the Activate Plugin dialog box, click Activate . |
| 7 | When the plugin activation is completed, click Close & Reload Form in the Plugin Activation dialog box. |
| 8 | To verify the plugin activation, from the Filter navigator field at the upper left of the window, navigate to OpenFrame . |
| 9 | Click Configurations and ensure that the OpenFrame plugin appears in the OpenFrame Configurations list. |

| 1 | Download the latest System Update Set XML file available on the github repo at this location : https://github.com/CiscoDevNet/webex-contact-center-crm-integrations/tree/main/ServiceNow . File Name : webexcc-servicenow-update-setV(X).xml |
|---|---|
| 2 | On your ServiceNow instance, from the Filter navigator field at the upper left of the window, navigate to System Update Sets > Update Sets to Commit . |
| 3 | Click the Import Update Set from XML link. |
| 4 | Click Choose File , select the System Update Set XML file, and then click Upload . The update set appears in the Retrieved Update Sets list and is in the Loaded state. |
| 5 | From the Retrieved Update Sets list, click the Update Set File Name (link) to open the Update Set. |
| 6 | At the upper right of the window, click Preview Update Set to check the update set for issues. |
| 7 | Click Close on the Update Set Preview dialog box once preview is completed. |
| 8 | Click Commit Update Set . |
| 9 | Click Close on the Update Set
                        Commit dialog box once committing of Update Set is
                    completed. |

| 1 | In the Filter navigator field at the upper left of the window, type sys_properties.list and press enter. |
|---|---|
| 2 | On the System Properties page, sort the properties by updated date. Ensure that you can see the following Webex Contact Center properties: |
| 3 | Click agentdesktop_url to open the System Property agentdesktop_url page. |
| 4 | In the Value field, enter the URL for the Webex Contact Center
                    Desktop according to the region of operation. |
| 5 | Click Update to save the changes. |
| 6 | (Optional) To change the Activity table name, edit the webexccactivitytable properties as required. On the System Properties page, click on webexccactivitytable . Change the Value field as required. |
| 7 | (Optional) Add User Groups in the following ways: In the Filter navigator field at the upper left of the window, navigate to Groups under System Security. Create a new user group or use an existing one. Click Edit . Search for sn_openframe_user under Collection and move it to your user group. Click Save . Add the user as a group member. |

| 1 | From the Filter navigator field, navigate to OpenFrame > Configurations . |
|---|---|
| 2 | Click New . |
| 3 | Enter the following properties for the URL: Name : Webex Contact Center Desktop Title : Webex Contact Center Width : 550 (Recommended) Height : 600 (Recommended) |
| 4 | To the right of the URL field, click the Lock button and add agentdesktop.do as the URL. (Do this step to point configuration to the UI Page) |
| 5 | (Optional) Select the User / Agent Group(s) to assign the configuration. |
| 6 | Click Submit . The URL appears as a link. |
| 7 | Before you attempt to use the OpenFrame phone, ensure that you upload the ServiceNow custom Desktop Layout JSON file to the Webex Contact Center Management Portal. For more information, see Set Up the ServiceNow Desktop Layout on Webex Contact Center . |

| 1 | Download the Desktop layout for ServiceNow from https://github.com/CiscoDevNet/webex-contact-center-crm-integrations/tree/main/ServiceNow . |
|---|---|
| 2 | Update the properties in the Desktop Layout file, if required. |
| 3 | Go to the Webex Contact Center Management Portal. |
| 4 | From the Management Portal navigation bar, choose Provisioning > Desktop Layout . |
| 5 | Click New Layout and enter the details for the desktop layout. |
| 6 | Upload the ServiceNow Desktop Layout JSON file. |
| 7 | Click Save to save the configuration. You can now start the Webex Contact Center
                        Desktop within the ServiceNow console. |
| 8 | From the Filter navigator field, navigate to Service Operations Workspace . |

| 1 | Sign in to your ServiceNow developer portal account and open the Administration console. |
|---|---|
| 2 | From the My Instance area of the Account menu, click Start Building . |
| 3 | On your developer instance, from the Filter navigator field at the upper left of the window, navigate to Plugins . |
| 4 | Search for the Openframe plugin that has the title Openframe . You may need to scroll through the list. |
| 5 | Click Install to install the Openframe plugin. |
| 6 | In the Activate Plugin dialog box, click Activate . |
| 7 | When the plugin activation is completed, click Close & Reload Form in the Plugin Activation dialog box. |
| 8 | To verify the plugin activation, from the Filter navigator field at the upper left of the window, navigate to OpenFrame . |
| 9 | Click Configurations and ensure that the OpenFrame plugin appears in the OpenFrame Configurations list. |

| Download and install the Webex Contact Center package from the ServiceNow store: https://store.servicenow.com/sn_appstore_store.do#!/store/application/6c8e2a4edbc73410e1c75e25ca961947 . |
|---|

| 1 | In the Filter navigator field at the upper left of the window, enter sys_properties.list . |
|---|---|
| 2 | On the System Properties page, sort the properties by updated date. Ensure that you can see the following Webex Contact Center properties: |
| 3 | Click agentdesktop_url to open the System Property agentdesktop_url page. |
| 4 | In the Value field, enter the URL for the Webex Contact Center
                    Desktop according to the region of operation. |
| 5 | Click Update to save the changes. |
| 6 | (Optional) To change the Activity table name, edit the x_caci_webexcc.webexccactivitytable properties as required. On the System Properties page, click on x_caci_webexcc.webexccactivitytable . Change the Value field as required. |
| 7 | (Optional) Add User Groups in the following ways: In the Filter navigator field at the upper left of the window, navigate to Groups under System Security . Click Edit and add the following roles: sn_openframe_user x_caci_webexcc.agent agent_workspace_user x_caci_webexcc.webexcc_imp_activity_user x_caci_webexcc.webex_contact_center |

| 1 | From the Filter navigator field, navigate to OpenFrame > Configurations . |
|---|---|
| 2 | Click New . |
| 3 | Enter the following properties for the URL: Name : Webex Contact Center Desktop Title : Webex Contact Center Width : 550 (Recommended) Height : 600 (Recommended) |
| 4 | To the right of the URL field, click the Lock button and add x_caci_webexcc_agentdesktop.do as the URL. (Do this step to point configuration to the UI Page) |
| 5 | (Optional) Select the User / Agent Group(s) to assign the configuration. |
| 6 | Click Submit . The URL appears as a link. |
| 7 | From the Filter navigator field, navigate to Service Operations Workspace . |
| 8 | (Optional) In the User Group list, move the user groups that can access the Webex Contact Center
                    Desktop from Available to Selected . |
| 9 | Before you attempt to use the OpenFrame phone, ensure that you upload the ServiceNow custom Desktop Layout JSON file to the Webex Contact Center Management Portal. For more information, see Set Up the ServiceNow Desktop Layout on Webex Contact Center . |

| 1 | Download the Desktop layout for ServiceNow from https://github.com/CiscoDevNet/webex-contact-center-crm-integrations/tree/main/ServiceNow . |
|---|---|
| 2 | Update the properties in the Desktop Layout file, if required. |
| 3 | Go to the Webex Contact Center Management Portal. |
| 4 | From the Management Portal navigation bar, choose Provisioning > Desktop Layout . |
| 5 | Click New Layout and enter the details for the desktop layout. |
| 6 | Upload the ServiceNow Desktop Layout JSON file. |
| 7 | Click Save to save the configuration. You can now start the Webex Contact Center
                        Desktop within the ServiceNow console. |
| 8 | From the Filter navigator field, navigate to Service Operations Workspace . |

| 1 | From the Filter navigator field, navigate to Incidents > Open Incident. |
|---|---|
| 2 | Right click on the caller field and click Configure Dictionary . |
| 3 | Add comma separated Attributes “ref_contributions=show_phone, . You can now start using the Webex Contact Center Desktop within the ServiceNow console. |
| 4 | From the Filter navigator field, navigate to Service Operations Workspace . |

## Figuras

![ServiceNow developer portal screenshot with ‘Start Building’ button highlighted.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/461001-462000/461682.jpg)

![ServiceNow developer instance showing a search for ‘plugins’ filter navigator.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/461001-462000/461681.jpg)

![ServiceNow developer instance on the Applications screen, showing the search and results for ‘OpenFrame.’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/461001-462000/461680.jpg)

![ServiceNow developer instance showing OpenFrame plugin popup with the ‘Activate’ button highlighted.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469969.jpg)

![ServiceNow developer instance showing OpenFrame plugin activation loading.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469970.jpg)

![ServiceNow developer instance showing OpenFrame plugin activation success window with the ‘Close & Reload Form’ button highlighted.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469971.jpg)

![ServiceNow developer instance showing OpenFrame Configurations in the filter navigator search.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469972.jpg)

![Github repo screenshot for Webex Contact Center CRM integrations – ServiceNow.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473069.jpg)

![ServiceNow developer instance showing a search in the filter navigator on the ‘All’ tab for ‘Update set’ and ‘Update Sets to Commit’ option highlighted.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469973.jpg)

![ServiceNow developer instance on the Update Sets results page with ‘Related Links: Import Update Set from XML’ highlighted.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/461001-462000/461671.jpg)

![ServiceNow developer instance import XML screen.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469976.jpg)

![ServiceNow developer portal retrieved update sets list.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472988.jpg)

![ServiceNow developer portal retrieved update sets list for an updated file.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469978.jpg)

![ServiceNow developer portal retrieved update sets list for an updated file with the ‘Preview Update Set’ button highlighted.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469979.jpg)

![ServiceNow developer portal with the update set preview success notification.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469980.jpg)

![ServiceNow developer portal retrieved update sets list for an updated file with the ‘Commit Update Set’ button highlighted.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469981.jpg)

![ServiceNow developer portal with the update set commit success notification.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469982.jpg)

![ServiceNow developer instance showing a search in the filter navigator on the ‘All’ tab for ‘sys_properties.list’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469983.jpg)

![ServiceNow developer instance system properties page.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472989.jpg)

![ServiceNow developer instance system property details for agentdesktop_url.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/462001-463000/462007.jpg)

![ServiceNow developer instance system property details for webexactivitytable.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472990.jpg)

![ServiceNow developer instance filter navigator search for ‘Groups’ under ‘System Security’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472992.jpg)

![ServiceNow developer instance group page for WebexccAgentsGroup.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472993.jpg)

![ServiceNow developer instance group edit members page showing a search for a collection.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472994.jpg)

![ServiceNow developer instance group edit members page showing a collection moved into the roles list.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472995.jpg)

![ServiceNow developer instance group page with user roles assigned.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472996.jpg)

![ServiceNow developer instance filters navigator with ‘openframe’ in the search field and ‘Configurations’ under ‘OpenFrame’ highlighted in the results.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469993.jpg)

![ServiceNow developer instance OpenFrame Configurations page with ‘New’ highlighted.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469994.jpg)

![ServiceNow developer instance OpenFrame Configurations – New Record page with the lock icon highlighted.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469995.jpg)

![ServiceNow developer instance OpenFrame Configurations – New Record user group selection.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469996.jpg)

![ServiceNow developer instance OpenFrame Configurations – New Record page showing the URL link that appears after submitting the user group selections.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/470001-471000/470038.jpg)

![Github screen for Webex Contact Center CRM Integrations – Desktop Layouts – ServiceNow.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/470001-471000/470002.jpg)

![Webex Contact Center Management Portal provisioning page with Desktop Layout highlighted in the left navigation.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/470001-471000/470003.jpg)

![ServiceNow home page with Webex Contact Center Agent Desktop integrated with ServiceNow.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/480001-490000/483001-484000/483243.jpg)

![ServiceNow store with ‘webex contact center’ in the search field.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/470001-471000/470005.jpg)

![ServiceNow developer instance system properties page results.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/473000.jpg)

![ServiceNow developer instance system property details page for agentdesktop_url.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473001.jpg)

![ServiceNow developer instance system properties page results for x_caci_webexcc.webexccactivitytable.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473002.jpg)

![ServiceNow developer instance system property page for x_caci_webexcc.webexccactivitytable.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473003.jpg)

![ServiceNow developer instance filter navigator results for ‘Groups.’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473004.jpg)

![SeviceNow developer instance group page for webexccagentsgroup.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473005.jpg)

![SeviceNow developer instance group page for webexccagentsgroup with rolls added.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473010.jpg)

![ServiceNow developer instance OpenFrame Configurations – New Record with URL added.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/460001-470000/469001-470000/469997.jpg)

![ServiceNow developer instance Incidents window with the Configure Directory option highlighted.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/470001-471000/470007.jpg)

![ServiceNow developer instance call incident window for a Directory Entry.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/470001-471000/470006.jpg)

![ServiceNow developer instance WebexCC IMP activity table.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473071.png)

![ServiceNow developer instance filter navigator on the All tab with ‘studio’ entered in the filter.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473072.png)

![Studio app for ServiceNow with the Select Application window open.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473073.png)

![Studio app for ServiceNow with the Select Application window open and ‘Select Store App to Customize’ selected.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473074.png)

![Studio app for ServiceNow with the ‘Select Store App to Customize’ window open and ‘Webex Contact Center’ selected.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473075.png)

![Studio app for ServiceNow with Webex Contact Center application file details.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473076.png)

![Studio app for ServiceNow WebexCC IMP Activity table.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473077.png)

![Studio app for ServiceNow WebexCC IMP Activity table new column example.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473078.png)

![Studio app for ServiceNow WebexCC IMP Activity table new column example with new column added.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473079.png)

![ServiceNow developer instance search for a phone log table.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473080.png)

![ServiceNow developer instance phone log table.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473081.png)

![ServiceNow developer instance phone log table new column examples.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473082.png)

![ServiceNow developer instance phone log table new column example with new column added.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473083.png)

![Studio app for ServiceNow WebexCC Activity Transform Map.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473084.png)

![Studio app for ServiceNow WebexCC Activity Transform Map new column example for CustomerName field mapping.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473085.png)

![Studio app for ServiceNow WebexCC Activity Transform Map new column example with CustomeName selected in the Target field.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473086.png)

![Studio app for ServiceNow WebexCC Activity Transform Map with popup window to personalized list columns. Choice action option is highlighted in the Selected column.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473087.png)

![Studio app for ServiceNow WebexCC Activity Transform Map with the Choice action column, showing the dropdown to choose ‘ignore’ or ‘create.’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473088.png)

![Studio app for ServiceNow WebexCC Activity Transform Map with the Choice action column and ‘ignore’ highlighted for the customer name source field.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473089.png)

![Studio app for ServiceNow configuring phone log list with CustomerName highlighted in the Selected column.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473090.png)

![ServiceNow developer instance filter navigator search for ‘script includes.’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473091.png)

![ServiceNow developer instance Script Includes page.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473093.png)

![Webex Contact Center CAD variable flow designer with Add Flow Variable popup for CustomerName.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473094.png)

![Example source code for adding the CAD variable to the Desktop Layout.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473095.png)

![ServiceNow example of the newly added CAD variable in the WebexCC Activity table, showing ‘Customer Name’ in the Cisco WebexCC popup.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473096.png)

![ServiceNow example of the newly added CAD variable in the WebexCC Activity table, showing ‘CustomerName’ in the comments section under ‘Activity’ and ‘System Administrator.’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473097.png)

![ServiceNow developer instance example of the newly added CAD variable in the WebexCC Activity table, showing the ‘CustomerName’ column.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473098.png)

![Webex Contact Center flow designer create CAD variable screen showing the edit flow variable popup for an incident urgency flow variable.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473360.png)

![Webex Contact Center flow designer create CAD variable screen showing the edit flow variable popup for an incident urgency flow variable.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473361.png)

![ServiceNow developer instance filter navigator search for ‘script includes’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473362.png)

![ServiceNow developer instance Script Includes name filter by ‘propUtils’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473363.png)

![ServiceNow developer instance Script Includes – propUtils details page.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473364.png)

![ServiceNow developer instance filter navigator search for ‘Ui page’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473365.png)

![ServiceNow developer instance UI Pages name filter to search ‘agentdesktop’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473366.png)

![ServiceNow developer instance UI Page – agentdesktop details page.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473367.png)

![ServiceNow example of an incident.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473368.png)

![ServiceNow example of an interaction.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473369.png)

![ServiceNow developer instance WebexCC Activity TransformMap.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473278.png)

![ServiceNow developer instance WebexCC Activity TransformMap details page.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473279.png)

![ServiceNow developer instance WebexCC Activity TransformMap new column, InteractionNumber.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473280.png)

![ServiceNow developer instance WebexCC Activity TransformMap details page showing the new ‘interactionnumber’ column added.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473281.png)

![ServiceNow developer instance WebexCC Activity TransformMap details page showing adding a new ‘incidentnumber’ column.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473282.png)

![ServiceNow developer instance WebexCC Activity TransformMap details page showing editing the max length for the IncidentNumber column.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473283.png)

![ServiceNow developer instance WebexCC Activity TransformMap details page showing the new ‘incidentnumber’ column added.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473284.png)

![ServiceNow developer instance Phone Log table.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473285.png)

![ServiceNow developer instance Directory Entry – New Record page showing a new column for InteractionsNumber.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473286.png)

![ServiceNow Developer instance Phone Log table with InteractionsNumber column added.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473287.png)

![ServiceNow developer instance Directory Entry – New Record page showing a new column for IncidentNumber.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473288.png)

![ServiceNow Developer instance Phone Log table with IncidentNumber column added.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473289.png)

![ServiceNow developer instance filter navigator search for ‘transform map’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473290.png)

![ServiceNow developer instance Table Transform Maps showing WebexCC Activity TransformMap in results.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473291.png)

![ServiceNow developer instance WebexCC Activity TransformMap.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473292.png)

![ServiceNow developer instance WebexCC Activity TransformMap with ‘InteractionNumber’ entered into the ‘Target field’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473293.png)

![ServiceNow developer instance WebexCC Activity TransformMap with ‘InteractionNumber’ added.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473294.png)

![ServiceNow developer instance WebexCC Activity TransformMap with ‘IncidentNumber’ entered into the ‘Target field’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473295.png)

![ServiceNow developer instance WebexCC Activity TransformMap with ‘IncidentNumber’ added.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473296.png)

![ServiceNow developer instance filter navigator with search for ‘script includes’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473297.png)

![ServiceNow developer instance Script Includes with Name filter applied to search and  ‘propUtils’ entered into the search field.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473298.png)

![ServiceNow developer instance Script includes - propUtils page](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473299.png)

![ServiceNow developer instance filter navigator with search for ‘Ui page’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473300.png)

![ServiceNow developer instance UI Pages with Name filter applied to search.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473301.png)

![ServiceNow developer instance UI Page – agentdesktop.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473302.png)

![ServiceNow developer instance Phone Logs page.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/473001-474000/473303.png)

![ServiceNow developer instance Business Rules page header.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472333.png)

![ServiceNow developer instance Business Rule – New Record.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472334.png)

![ServiceNow developer instance Business Rule – CTI Processing For Incident page as a sample configuration of the business rule.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472335.png)

![ServiceNow developer instance Business Rules page with the Personalized List Columns popup screen showing ‘Client callable’ in the ‘Selected’ column.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472336.png)

![ServiceNow developer instance Business Rules page showing the Client callable column with options to select ‘true’ or ‘false’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472337.png)

![System Property page for screenpop_url showing update to the custom CTI rule in the ‘Value’ field.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472338.png)

![ServiceNow developer instance Table – WebexCC Activity page.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472339.png)

![ServiceNow developer instance filter navigator search for ‘studio’  highlighting the cross launch search result for ‘App Engine Studio’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472340.png)

![App Engine Studio Select Application screen showing Webex Contact Center in the search results.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472341.png)

![App Engine Studio Webex Contact Center screen.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472342.png)

![App Engine Studio WebexCC Activity table.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472343.png)

![App Engine Studio WebexCC Activity table column edit example for ‘CustomerName’ column.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472344.png)

![App Engine Studio WebexCC Activity table screen.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472345.png)

![App Engine Studio WebexCC Activity table list layout showing ‘CustomerName’ highlighted in the ‘Selected’ column.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472346.png)

![ServiceNow developer instance filter navigator search for ‘script includes’](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472347.png)

![ServiceNow developer instance Script Includes page with ‘Application’ in the filter.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472348.png)

![ServiceNow developer instance Script Includes – New Record page.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472349.png)

![App Engine Studio agentdesktop UI page with new script name.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472350.png)

![Webex Contact Center flow designer with Add Flow Variable popup showing adding a CustomerName variable.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472351.png)

![Webex Contact Center CAD variable to the desktop layout script with ‘CustomerName:CustomerName’ highlighted.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472352.png)

![ServiceNow developer instance showing newly added CAD variable in the WebexCC Activity table.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472353.png)

![ServiceNow developer instance WebexCC Activities screen.](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/472001-473000/472354.png)