---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-2e561034dc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_outbound-api_1501.html
retrieved_at: 2026-08-21T16:47:39.356273+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Outbound API

## Chapter: Outbound API

# Outbound API

## Outbound API

Outbound API allows you to use REST APIs to create, modify, and delete Outbound Option campaigns.

Outbound API provides a streamlined mechanism for creating campaigns with a single associated query rule and import rule.
                           As such, if you use the API to create a campaign, that campaign is not available in the Outbound Campaign tool. If a campaign
                           was created with the API, you must use the API to view, edit, or delete it. If a campaign was created with the Outbound Campaign
                           tool, you must use the Outbound Campaign tool to view, edit, or delete it.

Administrative scripts are not required for Outbound Option campaigns created with the Outbound API. If an administrative
                           script is provided, the information in the script overrides the information defined in the API.

Outbound API consists of the following APIs:

Outbound Campaign API: Use this API to define new Outbound Option campaigns, and to view, edit, or delete existing campaigns.

Campaign Status API: Use this API to get the real-time status of running Outbound Option campaigns.

Do Not Call API: Use this API to set the Do Not Call (DNC) import rule configuration for Outbound Option. This prevents the
                                 dialer from dialing numbers on the DNC list.

Import API: Use this API to import customer contact information for an Outbound Option campaign.

Personal Callback API: Use this API to configure your Outbound Option campaign to handle personal callbacks. You can create
                                 personal callback records individually or in bulk. You can also update or delete personal callback records.

Time Zone API: Use this API to list all available time zones and to get information about a specified time zone.

## Outbound Campaign API

An Outbound Campaign makes outgoing calls to customers for a specific purpose or task and delivers these calls to agents.

Use the Outbound Campaign API to define new outbound campaigns, and to view, edit, or delete existing outbound campaigns.

In the Role API, when you enable the CampaignStatus or CampaignContact subfeature in the accessList parameter for a custom
                                       role then the Outbound Campaign API is provided with Update Only Access instead of Full Access. With Update Only Access, you
                                       cannot create and delete a campaign using Outbound Campaign API.

### URL

### Operations

create :
                                    				Creates one campaign and stores it in the database.

delete :
                                    				Deletes one campaign from the database. The campaign is saved under Configuration Manager > Miscellaneous Tools > Deleted Objects .

You can only delete campaigns that were created using the API. You cannot use the API to delete campaigns that were created
                                    in the Outbound Option Campaign tool.

list :
                                    				Retrieves a list of campaigns from the database. 
                                    			 Only campaigns that were created using the Outbound Option API are retrieved. Campaigns created using the Outbound Option
                                    Campaign tool do not appear in the list.

get :
                                    				Returns one campaign from the database using the URL https://<server>/unifiedconfig/config/campaign/<id> .

You must specify the ID for a campaign that was created using the API. If you specify the ID for a campaign created using
                                    the Outbound Option Campaign tool,  the request returns CceDBDataNotFoundException.

update :
                                    				Updates one campaign in the database using the URL https://<server>/unifiedconfig/config/campaign/<id> .

You can only update campaigns that were created using the API. You cannot use the API to update campaigns that were created
                                    in the Outbound Option Campaign tool.

### Parameters

name: Required. The name of the campaign. See Shared Parameters .

You cannot use the system reserved terms such as dnc and none as a campaign name.

department: A reference to the campaign's department, including the refURL and name. See References .

description: Optional description for the campaign. See Shared Parameters .

linesPerAgent: The number of lines dedicated to each agent in the campaign. Range is 1 to 100. Default is 1.5. This parameter
                                    performs as follows in the Outbound Option dialing modes:

Preview mode: Ignored (always 1).

Progressive mode: Used as defined.

Predictive mode: Used as an initial value.

maximumLinesPerAgent: The upper bound for the number of customers the dialer dials for a reserved agent when a campaign is
                                    running in predictive mode. Range is 1 to 100. Default is 2.

abandonEnabled: True or false. Default is true.

abandonPercent: When enabled (abandonEnabled is set to true), you can set the abandoned calls limit for the  percentage of
                                    abandoned calls in the campaign. When disabled (abandonEnabled is set to false), the campaign dials without regard to the
                                    abandon limit. Range is 1 to 100. The granularity is to one 10th of a percent. Default is 3.

predictiveCorrectionPace: A count of the number of live voice connections that must occur before the Dialer adjusts. Increasing
                                    this number results in less frequent adjustments based on larger sample size. Decreasing this number results in more frequent
                                    adjustments using a smaller sample size. Range is 10 to 5000. Default is 70.

predictiveGain: The size of the adjustment to lines per agent each time an adjustment is made. Increasing this number results
                                    in larger lines per agent adjustments. Decreasing this number results in smaller lines per agent adjustments. Range is 0.1
                                    to 3.0. Default is 1.

noAnswerRingLimit: The number of times the software allows a dialed phone number to ring. Range is from  2 to 10. Default
                                    is 4.

maxAttempts: The maximum number of attempts, including callbacks and retries. Range is from 1 to 100. Default is 3.

minimumCallDuration: Minimum duration (in seconds) of an outbound call. If the outbound call is less than the specified value,
                                    Outbound Option considers the call to be customer abandoned and schedules the record for a retry. To disable  this feature,
                                    set the parameter to 0. Range is 0 to 10. Default is 1.

noAnswerDelay: The time (in minutes) that the software waits before calling back a no-answer call. Range is 1 to 99999. Default
                                    is 60.

busySignalDelay: The time (in minutes) that the software waits before calling back a busy phone number. Range is 1 to 99999.
                                    Default is 60.

customerAbandonedDelay: If a customer abandons a call, the time (in minutes) that the Dialer waits before calling the customer
                                    back. Range is 1 to 99999. Default is 30.

dialerAbandonedDelay: If the Dialer abandons a call, the time (in minutes) that the Dialer waits before calling the customer
                                    back. Range is 1 to 99999. Default is 60.

answeringMachineDelay: If an answering machine answers a call, the time (in minutes) that the Dialer waits before calling
                                    the customer back. Range is 1 to 99999. Default is 60.

customerNotHomeDelay: If a customer is not home, the time (in minutes) that the Dialer waits before calling the customer back.
                                    Range is 1 to 99999. Default is 60.

personalizedCallbackEnabled: If enabled, this parameter allows an agent to schedule a callback to a customer for a specific
                                    date and time. A personal callback connects the same agent who initiated the callback to the customer. True or false. Default
                                    is false.

rescheduleCallbackMode: Determines how Outbound Option handles a personal callback if the agent is not available. Default
                                    is useCampaignDN. Options are as follows:

Use campaign DN

Same time next business day

Abandon

campaignPurposeType: The type of campaign. Default is agentCampaign. The options are as follows:

Agent Campaign: This type of campaign uses an outbound mode that causes the Dialer to transfer every customer call associated
                                          with a specific skill group to an agent.

IVR Campaign: This type of campaign uses an outbound mode that causes the Dialer to transfer every customer call associated
                                          with a specific skill group to a service control-based IVR instead of an agent. This option allows a contact center to run
                                          unassisted outbound campaigns using prerecorded messages in the IVR.

ipAmdEnabled: When enabled, directs the Dialer to perform a specific action if it detects an answering machine. True or false.
                                    Default is true.

amdTreatmentMode: If  enabled (ipAmdEnabled is set to true), when the Dialer detects an answering machine, it does one of
                                    the following:

Abandon call (default)

Transfer to agent

Transfer to IVR route point

ipTerminatingBeepDetect: When this parameter is set to true, the Dialer transfers the call after detecting the answering machine
                                    beep. True or false. Default is false.

timeZone: Required. The refURL and display name for the selected time zone. The default time zone is UTC (Universal Coordinated
                                    Time). The display name is the text that may be displayed in a user interface and can be localized.

If time zone information changed due to periodic updates and the campaign's configured time zone is no longer valid, the following
                                                information is returned:

```
<timeZone>
   <refURL>/unifiedconfig/config/timezone/INVALID</refURL>
   <displayName>INVALID Time Zone</displayName>
</timeZone>
```

startTime: The time the campaign starts dialing customer numbers. The format for this parameter is hours:minutes. Range is
                                    from 00:00 to 23:59.  The default value is taken from the Blended_Agent_Options table column values for DialStartHours and
                                    DialStartMinutes.

endTime: The time the campaign stops dialing customer numbers. The format for this parameter is hours:minutes. Range is from
                                    00:00 to 23:59.  The default value is taken from the Blended_Agent_Options table column values for DialEndHours and DialEndMinutes.

enabled: Whether the dialer is available to call contacts. True or false. Default is false.

startDate: The date that the campaign starts. The format is YYYY-MM-DD.

endDate: The date that the campaign ends. The format is YYYY-MM-DD.

campaignPrefix: Digits to prefix to each customer number dialed from this campaign.  Maximum length of 15 digits.

dialingMode: The dialing mode to use for the campaign skill groups. Valid values are as follows:

INBOUND

PREDICTIVEONLY

PREVIEWONLY

PROGRESSIVEONLY

PREVIEWDIRECTONLY

reservationPercentage: The percentage of agents to reserve within the skill groups associated with the campaign. Range is
                                    from 0 to 100. Default is 100.

callProgressAnalysis: A collection of parameters for Call Progress Analysis (CPA). Any combination of parameters within this
                                    collection can be set. If none of the parameters are provided and CPA is enabled for the campaign by default, CPA recording
                                    is set to false and default parameter values are set from the Blended_Agent_Options table.

enabled: When set to false, CPA for all calls made from this Dialer is disabled on a campaign-by-campaign basis, including
                                          voice detection, fax/modem detection, and answering machine detection. True or false. Default is true.

record: If enabled is set to true, you can specify this parameter. If you set it to true, the gateway provides a media stream
                                          and the Dialer records .wav files. True or false. Default is false.

minSilencePeriod: The minimum silence period (in milliseconds) required to classify a call as voice detected. If many answering
                                          machine calls are being passed through to agents as voice, then increasing this value accounts for longer pauses in answering
                                          machine greetings. Range is from 100 to 1000. Default is 608.

analysisPeriod: The number of milliseconds spent analyzing this call. If there is a short agent greeting on an answering machine,
                                          then a longer value categorizes that answering machine call as voice. If the call is to a business where the operator has
                                          a longer scripted greeting, a shorter value categorizes the long, live greeting as an answering machine call. Range is from
                                          1000 to 10000. Default is 2500.

minimumValidSpeech: Minimum number of milliseconds of voice required to classify a call as voice detected. Range is 50 to
                                          500. Default is 112.

maxTimeAnalysis: The maximum number of milliseconds allowed for analysis before identifying a problem analysis as dead air/low
                                          volume. Range is 1000 to 10000. Default is 3000.

maxTermToneAnalysis: The maximum number of milliseconds the dialer analyzes an answering machine voice message looking for
                                          a termination tone. If the message has an odd tone and the analysis does not recognize it, the call is not transferred or
                                          dropped until this timeout occurs. Range is 1000 to 60000. Default is 30000.

skillGroupInfos: A collection of information about the skill groups associated with the campaign.

skillGroupInfo: A collection of information about one skill group.

skillGroup: The name and the refURL of the skill group assigned to the campaign.

overflowAgents: This parameter ensures that at least one extra agent is reserved before the dialer begins dialing for a Progressive
                                                campaign. If the parameter is set to 1, at least two agents must be reserved before the dialer begins dialing. Range is 0
                                                to 100. Default is 0.

dialedNumber: The digits that are dialed to reserve an agent in the configured skill group. This parameter can contain letters,
                                                numbers, periods (.), and underscores (_) and can be up to ten characters in length.

recordsToCache: The minimum number of dialing numbers that each dialer caches for each of the Outbound Option skill groups.
                                                Range is 1 to 400. Default is 1.

ivrPorts: The total number of IVR ports allocated for the skill group. This parameter indicates how many ports are available
                                                for the dialer to transfer customer calls. Because this value indicates the total number of ports supported by the IVR for
                                                the current skill group, multiple skill groups can make transfer to IVR calls. One IVR can also be used to play different
                                                messages based on the route point where the contact is transferred. If multiple dialers are associated with the skill group,
                                                each dialer dials a fraction of the total number of ports. Default is 0.

ivrRoutePoint: If the campaign is a Transfer to IVR campaign or is configured to transfer AMD calls to an IVR, this parameter
                                                indicates the route point required to run the transfer to IVR routing script. This parameter must coincide with a route point
                                                configured on Unified Communications Manager and be assigned to a PGUser. Contacts are transferred to the route point, which
                                                points to a routing script. The script transfers the call to an IVR. Maximum length of 32 characters.

abandonedRoutePoint: If the campaign is a Transfer to IVR campaign or is configured to transfer AMD calls to an IVR, this
                                                number allows the dialer to play a message to calls about to be disconnected because no agents are available. This number
                                                must coincide with a route point configured on Unified Communications Manager and be assigned to the agent PG's CTI application
                                                (for example, PGUser). Contacts are transferred to this route point, which points to a routing script. The script transfers
                                                the call to an IVR. Maximum length of ten characters.

skillGroupInfosAdded: A collection of skill group references
                                    				to be added to the campaign, including the skill group refURL. This parameter is update only. This parameter can be used
                                    with
                                    				the skillGroupInfosRemoved parameter. See References .

skillGroupInfosRemoved: A collection of skill group references
                                    				to be removed from the campaign, including the skill group refURL of each skill group. This parameter is update only.
                                    This parameter can be used with
                                    				the skillGroupInfosAdded parameter. See References .

### Search and Sort Parameters

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

Search parameters

Sort parameters

name

description

name (default)

description

startDate

endDate

enabled

campaignPurposeType

timezone

dialingMode

See Search and Sort .

### Disable All Campaigns (Emergency Stop)

The Outbound Campaign API provides a method to immediately disable all outbound campaigns that are currently enabled. To disable
                              all of the campaigns, perform a PUT on the following URL:

https://<server>/unifiedconfig/config/campaign/disable

This request retrieves a list of all campaigns created using the Outbound Campaign API that are currently enabled and sets
                              the enabled parameter to false. The Campaign Manager stops sending out records to the Dialer for these campaigns. All active
                              records in the Dialer's memory are removed.

### Example Get Response

```
<campaign> <department>
          <refURL>/unifiedconfig/config/department/5001</refURL>
          <name>Sales</name>
         </department> <changeStamp>48</changeStamp>
    <refURL>/unifiedconfig/config/campaign/5168</refURL>
    <import>
        <refURL>/unifiedconfig/config/import/5000</refURL>
    </import>
    <abandonEnabled>true</abandonEnabled>
    <abandonPercent>3.0</abandonPercent>
    <amdTreatmentMode>abandonCall</amdTreatmentMode>
    <campaignPrefix>978</campaignPrefix>
    <campaignPurposeType>agentCampaign</campaignPurposeType>
    <dialingMode>PREVIEWONLY</dialingMode>
    <enabled>true</enabled>
    <endDate>2016-01-15</endDate>
    <endTime>17:00</endTime>
    <ipAMDEnabled>true</ipAmdEnabled>
    <ipTerminatingBeepDetect>false</ipTerminatingBeepDetect>
    <linesPerAgent>1.5</linesPerAgent>
    <maxAttempts>3</maxAttempts>
    <maximumLinesPerAgent>100.0</maximumLinesPerAgent>
    <minimumCallDuration>1</minimumCallDuration>
    <name>APIoct1</name>
    <noAnswerRingLimit>4</noAnswerRingLimit>
    <personalizedCallbackEnabled>false</personalizedCallbackEnabled>
    <predictiveCorrectionPace>70</predictiveCorrectionPace>
    <predictiveGain>1.0</predictiveGain>
    <rescheduleCallbackMode>useCampaignDN</rescheduleCallbackMode>
    <reservationPercentage>100</reservationPercentage>
    <retries>
        <answeringMachineDelay>60</answeringMachineDelay>
        <busySignalDelay>60</busySignalDelay>
        <customerAbandonedDelay>30</customerAbandonedDelay>
        <customerNotHomeDelay></customerNotHomeDelay>
        <dialerAbandonedDelay>60</dialerAbandonedDelay>
        <noAnswerDelay>60</noAnswerDelay>
    </retries>    
    <skillGroupInfos>
    <skillGroupInfo> 
        <ivrPorts>0</ivrPorts>
        <overflowAgents>0</overflowAgents>
        <recordsToCache>1</recordsToCache>
        <abandonedRoutePoint>12345</abandonedRoutePoint>
        <dialedNumber>123</dialedNumber>
        <ivrRoutePoint>91234</ivrRoutePoint>
        <skillGroup>
            <refURL>/unifiedconfig/config/skillgroup/5004</refURL>
            <name>errorDetailsRouteScript</name>
        </skillGroup>
    </skillGroupInfo>
    </skillGroupInfos>
    <startDate>2016-01-14</startDate>
    <startTime>09:00</startTime>
    <timeZone>
        <displayName>(UTC-05:00) Eastern Time (US & Canada)</displayName>        
        <refURL>/unifiedconfig/config/timezone/Eastern%20Standard%20Time</refURL>                
    </timeZone>
    <callProgressAnalysis>
        <enabled>true</enabled>
        <record>false</record>
        <minSilencePeriod>608</minSilencePeriod>
        <analysisPeriod>2500</analysisPeriod>
        <minimumValidSpeech>112</minimumValidSpeech>
        <maxTimeAnalysis>3000</maxTimeAnalysis>
        <maxTermToneAnalysis>30000</maxTermToneAnalysis>
    </callProgressAnalysis>
</campaign>
```

### Example Create Request

```
<campaign> <department>
          <refURL>/unifiedconfig/config/department/5001</refURL>
          <name>Sales</name>
         </department> <name>APIOct1</name>
    <description>APIOct1</description>
    <dialingMode>PREVIEWONLY</dialingMode>
    <skillGroupInfos>
        <skillGroupInfo>
            <ivrPorts>0</ivrPorts>
            <overflowAgents>0</overflowAgents>
            <recordsToCache>1</recordsToCache>
            <skillGroup>
                <refURL>/unifiedconfig/config/skillgroup/5001</refURL>
                <name>sgcampaign</name>
            </skillGroup>
        </skillGroupInfo>
    </skillGroupInfos>
    <timeZone>
        <refURL>/unifiedconfig/config/timezone/UTC</refURL>
    </timeZone>
    <callProgressAnalysis>
        <enabled>true</enabled>
        <record>false</record>
        <minSilencePeriod>608</minSilencePeriod>
        <analysisPeriod>2500</analysisPeriod>
        <minimumValidSpeech>112</minimumValidSpeech>
        <maxTimeAnalysis>3000</maxTimeAnalysis>
        <maxTermToneAnalysis>30000</maxTermToneAnalysis>
    </callProgressAnalysis>
</campaign>
```

## Campaign Status
                        	 API

Use the Campaign
                           		Status API to get the real-time status of running Outbound Option campaigns.

### URL

You must specify
                                          			 the ID for a campaign that was created using the Outbound Campaign API (see Outbound Campaign API ).
                                          			 If you specify the ID for a campaign created using the Outbound Option Campaign
                                          			 tool, the request returns CceDBDataNotFoundException.

### Operations

get :
                                    				Returns the runtime status of a campaign.

### Response
                              		  Parameters

abandonDetectCount: The number of calls abandoned by the dialer.

abandonToIvrCount: The number of calls that were abandoned by
                                    				the dialer and transferred to IVR.

agentClosedCount: The number of preview and callback calls that
                                    				were closed by the agent.

agentRejectedCount: The number of preview and callback calls
                                    				that were rejected by the agent.

answeringMachineCount: The number of calls that detected an
                                    				answering machine.

attemptedCount: Summary total of the number of calls attempted.

busyCount: The
                                    				number of calls that detected a busy signal.

callBackCount:
                                    				The number of callback contacts.

cancelledDetectCount: The number of calls where the dialer
                                    				canceled a ringing customer call.

closedCount:
                                    				The number of contacts closed for any reason other than reaching a live
                                    				customer.

customerAbandonDetectCount: The number of calls where the
                                    				customer hung up immediately after picking up the phone.

customerNotHomeCount: The number of contacts where the party who
                                    				answered the phone was not the customer.

dateTime: The
                                    				date and time when this data was updated last. The format is
                                    				yyyy-MM-ddTHH:mm:ss (for example, 2016-03-13T04:50:31).

faxDetectCount: The number of calls that detected a fax machine.

networkAnsMachineCount: The number of calls that detected a
                                    				network answering machine.

noAnswerDetectCount: The number of calls that were not answered.

noDialToneDetectCount: The number of calls that did not detect a
                                    				dial tone.

noRingBackDetectCount: The number of calls that did not detect a
                                    				ring back.

personalCallbackCount: The number of callback contacts
                                    				scheduled.

sitToneDetectCount: The number of calls that detected a special
                                    				information tone (SIT).

talkTimeCount:
                                    				The total number of seconds that agents spent talking on the phone since
                                    				midnight.

totalCount:
                                    				The total number of records available to dial for the current campaign.

totalVoiceCount: The number of live customers that have been
                                    				reached for this campaign since the last time the imported dialing list was
                                    				overwritten.

voiceCount:
                                    				The number of calls for the day that ended in successful customer contact.

wrapupTimeCount: The number of seconds that agents spent in
                                    				wrap-up mode since midnight.

wrongNumberCount: The number of contacts where the party who
                                    				answered the phone indicated that the customer did not live there.

### Example Get
                              		  Response

```
<runtimeStatus>
    <abandonDetectCount>0</abandonDetectCount>
    <abandonToIvrCount>0</abandonToIvrCount>
    <agentClosedCount>0</agentClosedCount>
    <agentRejectedCount>0</agentRejectedCount>
    <answeringMachineCount>0</answeringMachineCount>
    <attemptedCount>1</attemptedCount>
    <busyCount>0</busyCount>
    <callBackCount>0<callBackCount>
    <cancelledDetectCount>0</cancelledDetectCount>
    <closedCount>0</closedCount>
    <customerAbandonDetectCount>0</customerAbandonDetectCount>
    <customerNotHomeCount>0</customerNotHomeCount>
    <dateTime>2016-01-15T13:43:00</dateTime>
    <faxDetectCount>0</faxDetectCount>
    <networkAnsMachineCount>0</networkAnsMachineCount>
    <noAnswerDetectCount>0</noAnswerDetectCount>
    <noDialToneDetectCount>0</noDialToneDetectCount>
    <noRingBackDetectCount>0</noRingBackDetectCount>
    <personalCallbackCount>0</personalCallbackCount>
    <sitToneDetectCount>0</sitToneDetectCount>
    <talkTimeCount>1</talkTimeCount>
    <totalCount>0</totalCount>
    <totalVoiceCount>1</totalVoiceCount>
    <voiceCount>1</voiceCount>
    <wrapupTimeCount>0</wrapupTimeCount>
    <wrongNumberCount>0</wrongNumberCount>
</runtimeStatus>
```

## Do Not Call
                        	 API

Use the Do Not Call
                           		API to set the Do Not Call (DNC) import rule configuration for Outbound Option
                           		so that the campaign dialer doesn't dial the numbers in the DNC list.

The DNC import is
                           		automatically scheduled to start when the file is available. After the import
                           		is complete, the file is RENAMED or DELETED based on the boolean value for the
                           		renameFileAfterImport field.

### URL

### Operations

create :
                                    				Sets the configuration in the database. Returns the refURL if the configuration
                                    				is set.

delete :
                                    				Deletes the specific DNC configuration using the URL https://<server>/unifiedconfig/config/dnc/<id> .
                                    				This does not delete the DNC import file that is present at the location of the
                                    				filePath.

list :
                                    				Retrieves a list available DNC import rules.

get :
                                    				Returns the DNC import configuration from the database using the URL https://<server>/unifiedconfig/config/dnc/<id> .

update :
                                    				Updates the specific DNC import configuration with the new values using the URL https://<server>/unifiedconfig/config/dnc/<id> .

### Parameters

name: Name of
                                    				the DNC import. See Shared Parameters .

filePath: Path
                                    				to a file on the logger or accessible from the logger. Maximum length of 255
                                    				characters.

overwrite:
                                    				Whether the new DNC import overwrites the phone numbers from the previous DNC
                                    				import. True or false. Default is false.

renameFileAfterImport: Whether to delete the DNC import file
                                    				after the import is complete. True or false. Default is true. If the parameter
                                    				is set to true, the DNC file is renamed. If the parameter is set to false, the
                                    				DNC import file is deleted.

### Search and
                              		  Sort Parameters

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

Search
                                          						parameters

Sort
                                          						parameters

name

name

See Search and Sort .

### Example Get
                              		  Response

```
<dnc>
    <refURL>/unifiedconfig/config/dnc/unifiedconfig/config/dnc/5001</refURL>
    <name>dnc1</name>
    <filePath>\\CCE-ROGGER-A\C$\Users\boston\Desktop\dnc.txt</filePath>
    <overwrite>false</overwrite>
    <renameFileAfterImport>true</renameFileAfterImport>
</dnc>
```

### Create Do Not Call
                           	 List

When creating a
                                 		  Do_Not_Call list file, format it correctly using the following instructions.

Step 1

Using a text
                                          			 editor, create a text file that contains all the do-not-call phone numbers.

Step 2

Enter a phone
                                          			 number for each Do Not Call entry on a new line.

Step 3

Observe the
                                          			 following characteristics for each Do Not Call entry:

Each phone
                                                   					 number can be a maximum of 20 characters long.

The Do Not
                                                   					 Call table can support up to 60 million entries, but note that the information
                                                   					 is stored in memory in the Campaign Manager process.

Step 4

Save the text
                                          			 file to the local server.

The following is an
                                 		  example of a Do_Not_Call list:

2225554444

2225556666

2225559999

To add a customer to
                                 		  this list, import a Do Not Call list.

To save file path of Do Not Call list import file:

In Unified CCE Administration, choose Organization > Campaigns to open the Campaigns page.

Click the Do Not Call - Settings link.

The Do Not Call - Settings pop-up window appears.

In the File Path with Name field, you must enter the DNC list import file path on the logger or the path accessible from the logger.

Click Save .

The solution import the DNC phone numbers to Do_Not_Call table in BA database. The name of DNC list import file is renamed
                                       after the successful import.

On the Campaigns page, you can save only one DNC list import file path at a time.

The campaign validates that a number in the dialing list is not in the Do Not Call list before sending it to a dialer. The
                                       solution checks the list at the last minute before placing the call. You can update a Do Not Call list while a campaign is
                                       running.

The Campaign Manager
                                 		  reads from the Do_Not_Call table. Dialing List entries are marked as Do Not
                                 		  Call entries only when the Campaign Manager fetches the Dialing List entry and only when
                                    			 there is an exact, digit-for-digit match . This allows Do Not Call imports
                                 		  to happen while a Campaign is running without rebuilding the Dialing List.

When the
                                 		  Campaign Manager starts it automatically imports from the DoNotCall.restore
                                 		  file that is stored in the <drive>\icm\<instance>\la\bin directory. When
                                 		  reading Do Not Call import files, the Campaign Manager appends the data to the
                                 		  DoNotCall.restore file. This restore file allows recovery of Do Not Call
                                 		  records after the Campaign Manager stops unexpectedly or for planned
                                 		  maintenance, such as a Service Release installation.

The
                                 		  restore file can grow to approximately 1 GB if 60 million DNC records are
                                 		  imported, each having ten-digit numbers plus five-digit extensions. Sufficient
                                 		  disk space must be available on LoggerA to store the DoNotCall.restore file.

To edit the DNC phone numbers import file path:

Click the Do Not Call - Settings link. The solution displays the existing file path of the DNC list import file in the File Path with Name field

Enter the file path of the new or updated DNC list import file in the File Path with Name field.

(Optional) Check the Delete existing "Do Not Call" Phone Numbers check box to delete the existing phone numbers from the Do_Not_Call table.

If this check box is not selected, the existing DNC phone numbers are appended to the new or updated DNC phone numbers in
                                       the Do_Not_Call table.

Click Save .

## Import API

Use the Import API to import customer contact information for an outbound campaign. You can import up to 10,000 records in
                           one create request.

You can queue up to 30 requests. If the queue has 30 requests and you submit another request, the response is HTTP 503 Service
                                             Unavailable with the boundary error condition "Request processing queue is at capacity."

If you receive this error, wait until a few requests are processed and submit the next request when the queue has less than
                                             30 requests.

If a particular integration is doing multiple small inserts per second for a campaign and this error appears, it is more efficient
                                             to batch up the records into larger imports.

Avoid performing a bulk job transaction during a maintainence window.

Only administrators can use the Import API. For
                                             						this reason, Import API user roles are authorized with the Active Directory,
                                             						and the local cache is updated every 30 minutes (the interval cannot be
                                             						modified).

### URL

You must specify
                                          			 the ID for a campaign that was created using the Outbound Campaign API. If you
                                          			 specify the ID for a campaign created using the Outbound Option Campaign tool,
                                          			 the request returns CceDBDataNotFoundException.

### Operations

create :
                                    				Imports customer contacts for a specific campaign.

delete :
                                    				Deletes the imported contacts for a specific campaign.

The delete
                                                				  operation deletes all imported contacts for the campaign. You cannot delete an
                                                				  individual record.

get (template): Returns a sample CSV template for contacts, which is provided by
                                    				the API, using the URL https://<server>/unifiedconfig/config/campaign/import/template .
                                    				The response contains the CSV template as a file attachment.

get :
                                    				Retrieves the details of a single import record using the URL
                                    				https://<server>/unifiedconfig/config/campaign/<campaignId>/import/<id>.
                                    				The <id> is the ID of the imported contact.

get (csv file): Returns a CSV file for the contacts of the campaign, which is provided by the API, using the URL https://<server>/unifiedconfig/config/campaign/<campaignId>/import with header as "Accept" and value as "text/csv". The response contains the Contacts.csv as a file attachment.

get (csv file): Returns a CSV file for the contacts of the campaign, which is provided by the API, using the URL https://<server>/unifiedconfig/config/campaign/<campaignId>/import/csv . The response contains the Contacts.csv as a file attachment. In this operation, you do not need to send "Accept" header.

list :
                                    				Retrieves a list of all imported contacts for the campaign.

Query parameters

Summary list: See list .

### Parameters

Response Parameters for
                                 			 get:

accountNumber:
                                    				The customer's account number.

callsMade: The
                                    				number of calls made.

callStatus:
                                    				The call status of the last call placed for this record. Possible values
                                    				include the following:

active (A)

callbackRequested (B)

closed (C)

agentRejected (J)

maxAttemptsReached (M)

pending
                                          					 (P)

retry (R)

personalCallbackRequested (S)

unknown
                                          					 (U)

For more information about these values, see the CallStatusZone Values section of the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

callResultOverall: The call result from the last call placed for
                                    				this record.

firstName: The
                                    				customer's first name.

lastName:
                                    				The customer's last name.

importDate:
                                    				The date and time that the record was imported.

phone01
                                    				through phone10: A collection of information about the customer's phones. Each
                                    				phone contains the following parameters:

number:
                                          					 The phone number.

callResult: The call result from the last call placed for this
                                          					 phone number.

For more information about possible callResult values, see the CallResult Codes and Values section of the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

dstObserved: Whether DST is observed for this phone's location.
                                          					 True or false.

gmtOffset: The number of minutes that the customer's time zone
                                          					 is offset from GMT. When you create import records, you can optionally provide
                                          					 a TimeZoneBias. The TimeZoneBias parameter represents the way information about
                                          					 time zones is stored in the Windows registry. You can use the following formula
                                          					 to convert TimeZoneBias to gmtOffset:

```
if timeZoneBias is postive:
    gmtOffset = 1440 - timeZoneBias (where 1440 is the number of minutes in 24 hours)
else if timeZoneBias is negative:
    gmtOffset = -1 * timeZoneBias
else if timeZoneBias is 0
    gmtOffset = timeZoneBias
```

Parameters for
                                 			 create:

fileContent:
                                    				Required. Comma-separated or pipe-separated list of data embedded within a
                                    				CDATA section.

overwriteData:
                                    				True or false. If set to true, the existing import data in the database is
                                    				overwritten by the new import data. If set to false, the new import data is
                                    				appended to the existing data. Default is false.

You cannot
                                                				  modify or remove existing fields or append a new field to existing data.

delimiter:
                                    				Comma (,) or pipe (|). Default is comma (,).

header fields:
                                    				The following header fields are allowed:

AccountNumber: Can contain any characters, including
                                          					 internationalized characters, except the delimiter specified in the input XML.
                                          					 Maximum length of 30 bytes.

FirstName:
                                          					 Can contain any characters, including internationalized characters, except the
                                          					 delimiter specified in the input XML. Maximum length of 50 characters.

LastName:
                                          					 Can contain any characters, including internationalized characters, except the
                                          					 delimiter specified in the input XML. Maximum length of 50 characters.

Phone01
                                          					 through Phone10: Can contain digits 0-9, pound sign (#), and asterisk (*).
                                          					 Maximum length of 20 bytes. At least one Phone field is required.

TimeZoneBias: Specifies the offset of the customer's time zone
                                          					 from UTC in minutes. Integer. Range is from –780 to 720 (–13 to 12 hours from
                                          					 UTC).

DstObserved: Specifies whether DST is observed for the
                                          					 customer's location. True or false. Default is false.

If the
                                                      						TimeZoneBias parameter is provided but the DstObserved parameter is not,
                                                      						DstObserved is set to false. If the DstObserved parameter is provided but not
                                                      						TimeZoneBias, a validation error is returned.

If
                                                      						TimeZoneBias is not provided, time zone and Daylight Saving Time information is
                                                      						assigned by matching phone numbers to region prefix strings. If a phone number
                                                      						for a contact does not match a configured region prefix, the default time zone
                                                      						for the campaign is used.

If a
                                                      						customer record contains multiple phone numbers, the value for TimeZoneBias and
                                                      						DstObserved are applied to all of that customer's phone numbers.

You
                                                      						can use the Time Zone API to look up the values for TimeZoneBias and
                                                      						DstObserved for the target time zone. For more information, see Time Zone API .

### Search and
                              		  Sort

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

accountNumber

firstName

lastName

accountNumber (default)

firstName

lastName

See Search and Sort .

### Example Get
                              		  Response

```
<importContact>
    <refURL>/unifiedconfig/config/campaign/5000/import/1</refURL>
    <accountNumber>4019</accountNumber>
    <callsMade>1</callsMade>
    <callStatus>pending</callStatus>
    <callResultOverall>0</callResultOverall>
    <firstName>Mir</firstName>
    <lastName>Ali</lastName>
    <importDate>2016-03-28T01:09:40</importDate>
    <phone01>        
        <callResult>0</callResult>
        <dstObserved>true</dstObserved>
        <gmtOffset>720</gmtOffset>
        <number>9789360001</number>
    </phone01>
    <phone02>      
        <callResult>0</callResult>
        <dstObserved>true</dstObserved>
        <gmtOffset>720</gmtOffset>
        <number>9789360002</number>
    </phone02>
    <phone03>...</phone03>
    <phone04>...</phone04>
    <phone05>...</phone05>
    <phone06>...</phone06>
    <phone07>...</phone07>
    <phone08>...</phone08>
    <phone09>...</phone09>
    <phone10>
        <callResult>0</callResult>
        <dstObserved>true</dstObserved>
        <gmtOffset>330</gmtOffset>
        <number>9789360010</number>
    </phone10>
</importContact>
```

### Example Create
                              		  Request

```
<import>
    <fileContent>
        <![CDATA[
        AccountNumber,FirstName,LastName,Phone01,Phone02,TimeZoneBias,DstObserved
        6782,Henry,Martin,2225554444,2225556262,720,false
        3456,Michele,Smith,2225559999,2225551234,540,true
        4569,Walker,Evans,2225552000,2225557890,-600,true
        ]]> 
    </fileContent>
    <delimiter>,</delimiter>
</import>
```

## Personal Callback
                        	 API

Use the Personal
                           		Callback API to configure your Outbound Option campaign to handle personal
                           		callbacks. The Personal Callback feature allows an agent to schedule a callback
                           		to a customer for a specific date and time.

### URL

### Operations

create :
                                    				Creates a single PersonalCallback record and stores it in the BA database.

create (bulk): Creates PersonalCallback records in bulk and stores them in the BA
                                    				database using the URL https://<server>/unifiedconfig/config/personalcallback/import .

delete :
                                    				Deletes one or more PersonalCallback records from the PersonalCallback list
                                    				using the URL https://<server>/unifiedconfig/config/personalcallback/<id> .

get (template): Retrieves a sample CSV template for contacts, which is provided by
                                    				the API, using the URL https://<server>/unifiedconfig/config/personalcallback/template .

get (record): Retrieves one PersonalCallback record from the database using the URL https://<server>/unifiedconfig/config/personalcallback/<id> .

list :
                                    				Retrieves a list of PersonalCallback records from the database.

update :
                                    				Updates one PersonalCallback record in the database using the URL https://<server>/unifiedconfig/config/personalcallback/<id> .

### Parameters

Parameters for create
                                 			 (single record), get, and update operations:

campaign: A
                                    				reference to a specific campaign, including the refURL and campaign ID.

agent: A
                                    				reference to a specific agent, including the refURL and agent ID.

campaignId:
                                    				Read only. The ID for the campaign.

peripheralId: Read only. ID for the peripheral on which the
                                    				agent would be available.

agentId:
                                    				Read only. ID of the agent to whom to connect the call.

campaignDn:
                                    				The Dialed Number (DN) to use if the original agent is not available.

phone:
                                    				Required. The phone number to call back. Can contain digits 0 to 9, pound sign
                                    				(3), and asterisk (*). Maximum length of 20 bytes.

accountNumber:
                                    				The customer's account number. Internationalized characters are allowed.
                                    				Maximum length of 30 bytes.

maxAttempts:
                                    				Required. The maximum number of times to attempt a call (decrements at each
                                    				attempt). An attempt is the Dialer's attempt to reserve the agent and call the
                                    				customer. Because the Dialer places multiple customer call attempts (such as
                                    				busy, no answer), individual call attempts are not tracked here; only the
                                    				result at the end of the callback time range. After this parameter is set to 0,
                                    				no more attempts are made. Must be a positive integer value.

callbackDateTime: Required. The time to attempt the customer
                                    				callback is normalized to the logger GMT zone. For example, the Campaign
                                    				Manager is in Boston and the customer is in California. The customer wants to
                                    				be called back at 3 p.m. The time in this column is 6 p.m. The format for this
                                    				parameter is yyyy-MM-ddTHH:mm:ss (for example, 2016-03-13T04:50:31).

The
                                    				following rules apply to the callbackDateTime parameter:

The
                                          					 callbackDateTime that is used is local to the time zone of the Logger. You need
                                          					 to consider this if the client machine on which you are using this API is in a
                                          					 different time zone than the Logger machine.

The setting of the callbackDateTime by this API reads the CallbackDateTimeLimit in the registry. For more information, see
                                          the Registry Settings section of the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

The
                                          					 Campaign Manager uses the CallbackDateTimeLimit registry value to select
                                          					 Personal Callback records to queue to the Dialer.

The
                                          					 default CallbackDateTimeLimit in the registry is 15 minutes. For create and
                                          					 update operations, you cannot set the callbackDateTime to 15 minutes or more
                                          					 before the current time. For example, if it is currently 4:00, you cannot set
                                          					 the callbackDateTime to 3:30.

For
                                          					 update operations, the new callbackDateTime value can only be set if the
                                          					 current callbackDateTime is 15 minutes or more after the current Logger time.
                                          					 For example, if the current Logger time is 4:00 and the current
                                          					 callbackDateTime is 4:30, the new callbackDateTime can be set to 4:10. However,
                                          					 if the current callbackDateTime is 4:10, it cannot be set to 4:00.

callStatus:
                                    				The status of the personal callback. Possible values include the following:

active
                                          					 (A)

callbackRequested (B)

closed
                                          					 (C)

agentRejected (J)

maxAttemptsReached (M)

pending
                                          					 (P)

retry
                                          					 (R)

personalCallbackRequested (S)

unknown
                                          					 (U)

agentNotAvailable (X)

For more information about these values, see the CallStatusZone Values section of the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

callResult:
                                    				Read only. Corresponds to the CallResult value in the Dialer_Detail table.

For more information about possible callResult values, see the CallResult Codes and Values section of the Outbound Option Guide for Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

lastName:
                                    				The customer's last name. Internationalized characters are allowed. Maximum
                                    				length of 50 characters.

firstName:
                                    				The customer's first name. Internationalized characters are allowed. Maximum
                                    				length of 50 characters.

Bulk parameters:

fileContent:
                                    				Comma-separated or pipe-separated list of data embedded within a CDATA section.

overwriteData: True or false. If set to true, the existing
                                    				personal callback data in the database is overwritten by the new personal
                                    				callback data. If set to false, the new personal callback data is appended to
                                    				the existing data. Default is false.

You cannot
                                                				  modify or remove existing fields or append a new field to existing data.

If
                                                				  overwriteData is set to true, any agent scheduled personal callback records are
                                                				  also overwritten.

Avoid performing a bulk job transaction during a maintainence window.

delimiter:
                                    				Comma (,) or pipe (|). Default is comma (,).

Bulk fileContent
                                 			 parameters:

The
                                          			 descriptions for these parameters are the same as the descriptions for the
                                          			 parameters for create (single record), get, and update operations. Only the
                                          			 case is different.

CampaignId
                                    				(must be a valid campaign ID in the database)

AgentSkillTargetId (must be a valid SkillTargetID in the
                                    				database)

CampaignDn

Phone

AccountNumber

MaxAttempts

CallbackDateTime

LastName

FirstName

### Search and
                              		  Sort Values

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

- agentId

- accountNumber

- firstName

- lastName

- agentId

- accountNumber

- firstName

- lastName

See Search and Sort .

Advanced search
                                 			 parameters

There are
                              		  several advanced searches you can perform on the Personal Callback API,
                              		  including agentId, accountNumber, firstName, and lastName. All search terms are
                              		  case-insensitive.

agentId:<ID> finds all personal callback records where the agent ID contains a specified ID.
                                    				For example, agentId:123 returns all records where the agent ID contains
                                    				the string "123".

lastName:<name> finds all personal callback records where the last name contains the specified
                                    				name. For example, lastName:smith returns all records where the last name
                                    				includes "smith".

firstName:<name> finds all personal callback records
                                    				where the firstName contains the specified name. For example, firstName:John returns all records where the first name
                                    				includes "john".

accountNumber:<number> finds all personal callback
                                    				records where the accountNumber contains the specified number. For example, accountNumber:456 returns all records where the account number includes "456".

### Example
                              		  Create Request (Single Record)

```
<personalCallback>
    <campaign>
        <refURL>/unifiedconfig/config/campaign/5000</refURL>
    </campaign>
    <agent>
        <refURL>/unifiedconfig/config/agent/5050</refURL>
    </agent>
    <campaignDn>222222</campaignDn>
    <phone>999333</phone>
    <accountNumber>23334343334</accountNumber>
    <maxAttempts>1</maxAttempts>
    <callbackDateTime>2016-01-15T11:37:00</callbackDateTime>
    <callStatus>pending</callStatus>
    <lastName>Kumar</lastName>
    <firstName>Akshaya</firstName>
</personalCallback>
```

### Example Create
                              		  Request (Bulk)

```
<personalCallback>
    <fileContent>
        <![CDATA[
        AccountNumber,FirstName,LastName,Phone,AgentSkillTargetId,CampaignId,CampaignDn, 
        CallbackDateTime,MaxAttempts
        6782,Henry,Martin,2225554444,1004,5000,2222222221,2016-01-25T05:12:00,1
        3444,Thomas,Edison,2225554555,1004,5000,2222222222,2016-01-25T05:23:00,1
        5444,Tom,Hilfiger,2225554666,1004,5000,2222222223,2016-01-25T05:37:00,1
        ]]>
    </fileContent>
</personalCallback>
```

### Example Get
                              		  (Record) Response

```
<personalCallback>
    <changeStamp>48</changeStamp>
    <refURL>/unifiedconfig/config/campaign/personalcallback/2</refURL>
    <campaign>
        <refURL>/unifiedconfig/config/campaign/5000</refURL>
    </campaign>
    <agent>
        <refURL>/unifiedconfig/config/agent/5050</refURL>
    </agent>
    <campaignId>5000</campaignId>
    <peripheralId>5000</peripheralId>
    <agentId>1001</agentId>
    <campaignDn>222222</campaignDn>
    <phone>999333</phone>
    <accountNumber>23334343334</accountNumber>
    <maxAttempts>1</maxAttempts>
    <callbackDateTime>2016-01-15T11:37:00</callbackDateTime>
    <callStatus>pending</callStatus>
    <callResult>0</callResult>
    <lastName>Kumar</lastName>
    <firstName>Akshaya</firstName>
</personalCallback>
```

## Time Zone API

Use the Time Zone API  to list all available time zones and to get time zone information for a specified zone. Time zone information
                           is stored in the registry of the Windows operating system.

Important

Microsoft periodically releases cumulative time zone updates. These updates include worldwide changes to time zone names,
                                       bias (the amount of time in minutes that a time zone is offset from Coordinated Universal Time (UTC)), and observance of daylight
                                       saving time. These patches update the information in the Windows registry. When these updates are available, apply them to
                                       all virtual machines in the deployment that are running a Microsoft Windows operating system.

Use this API with the Outbound Campaign API to set the default time zone for an Outbound Option campaign. An Outbound Option
                           campaign uses the time zone when the location of the customer number being dialed is unknown.

This API is read-only.

### URL

https://<server>/unifiedconfig/config/timezone

### Operations

list :
                                    				Retrieves a list of available time zones. 
                                    			 The list is sorted by UTC offset from the International Date Line from west to east.

get :
                                    				Returns information for a specific time zone using the URL https://<server>/unifiedconfig/config/timezone/<id> , where <id> is the URL-encoded version of the name parameter.

### Response Parameters

name: The name of the time zone.

displayName: Specific bias and location information about the time zone, such as the offset from UTC and one or more places
                                    located within the time zone.

Example: "(UTC+5:30) Chennai, Kolkata, Mumbai, New Delhi"

stdName: The time zone name during standard time.

Example: Malay Peninsula Standard Time

dstName: The time zone name during daylight saving time.

Example: Malay Peninsula Daylight Time

dstObserved: Indicates whether daylight saving time is observed for the time zone. True or false.

bias: The current bias for local time translation on the server (in minutes). That is, the number of minutes to add to the
                                    local time to yield UTC.

### Example Get Response

```
<timeZone>
   <refURL>       
     /unifiedconfig/config/timezone/Pacific%20Standard%20Time%20%28Mexico%29
   </refURL>
   <name>Pacific Standard Time (Mexico)</name> 
   <displayName>(UTC-08:00) Baja California</displayName>
   <stdName>Pacific Standard Time (Mexico)</stdName>
   <dstName>Pacific Daylight Time (Mexico)</dstName>
   <dstObserved>true</dstObserved>
   <bias>480</bias>
</timeZone>
```

| Note | In the Role API, when you enable the CampaignStatus or CampaignContact subfeature in the accessList parameter for a custom
                                       role then the Outbound Campaign API is provided with Update Only Access instead of Full Access. With Update Only Access, you
                                       cannot create and delete a campaign using Outbound Campaign API. |
|---|---|

| Note | You cannot use the system reserved terms such as dnc and none as a campaign name. |
|---|---|

| Note | If time zone information changed due to periodic updates and the campaign's configured time zone is no longer valid, the following
                                                information is returned: <timeZone>
   <refURL>/unifiedconfig/config/timezone/INVALID</refURL>
   <displayName>INVALID Time Zone</displayName>
</timeZone> |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| name description | name (default) description startDate endDate enabled campaignPurposeType timezone dialingMode |

| Note | You must specify
                                          			 the ID for a campaign that was created using the Outbound Campaign API (see Outbound Campaign API ).
                                          			 If you specify the ID for a campaign created using the Outbound Option Campaign
                                          			 tool, the request returns CceDBDataNotFoundException. |
|---|---|

| Search
                                          						parameters | Sort
                                          						parameters |
|---|---|
| name | name |

| Step 1 | Using a text
                                          			 editor, create a text file that contains all the do-not-call phone numbers. |
|---|---|
| Step 2 | Enter a phone
                                          			 number for each Do Not Call entry on a new line. |
| Step 3 | Observe the
                                          			 following characteristics for each Do Not Call entry: Each phone
                                                   					 number can be a maximum of 20 characters long. The Do Not
                                                   					 Call table can support up to 60 million entries, but note that the information
                                                   					 is stored in memory in the Campaign Manager process. |
| Step 4 | Save the text
                                          			 file to the local server. |

| Note | On the Campaigns page, you can save only one DNC list import file path at a time. |
|---|---|

| Note | If the Dialing
                                          		  List includes a base number plus extension, this entry must match a Do Not Call
                                          		  entry for that same base number and same extension. The dialer will not dial
                                          		  the extension. |
|---|---|

| Note | To clear the Do
                                          		  Not Call list, import a blank file with the Overwrite table option enabled. |
|---|---|

| Note | You can queue up to 30 requests. If the queue has 30 requests and you submit another request, the response is HTTP 503 Service
                                             Unavailable with the boundary error condition "Request processing queue is at capacity." If you receive this error, wait until a few requests are processed and submit the next request when the queue has less than
                                             30 requests. If a particular integration is doing multiple small inserts per second for a campaign and this error appears, it is more efficient
                                             to batch up the records into larger imports. Avoid performing a bulk job transaction during a maintainence window. Only administrators can use the Import API. For
                                             						this reason, Import API user roles are authorized with the Active Directory,
                                             						and the local cache is updated every 30 minutes (the interval cannot be
                                             						modified). |
|---|---|

| Note | You must specify
                                          			 the ID for a campaign that was created using the Outbound Campaign API. If you
                                          			 specify the ID for a campaign created using the Outbound Option Campaign tool,
                                          			 the request returns CceDBDataNotFoundException. |
|---|---|

| Note | The delete
                                                				  operation deletes all imported contacts for the campaign. You cannot delete an
                                                				  individual record. |
|---|---|

| Note | You cannot
                                                				  modify or remove existing fields or append a new field to existing data. |
|---|---|

| Note | If the
                                                      						TimeZoneBias parameter is provided but the DstObserved parameter is not,
                                                      						DstObserved is set to false. If the DstObserved parameter is provided but not
                                                      						TimeZoneBias, a validation error is returned. If
                                                      						TimeZoneBias is not provided, time zone and Daylight Saving Time information is
                                                      						assigned by matching phone numbers to region prefix strings. If a phone number
                                                      						for a contact does not match a configured region prefix, the default time zone
                                                      						for the campaign is used. If a
                                                      						customer record contains multiple phone numbers, the value for TimeZoneBias and
                                                      						DstObserved are applied to all of that customer's phone numbers. You
                                                      						can use the Time Zone API to look up the values for TimeZoneBias and
                                                      						DstObserved for the target time zone. For more information, see Time Zone API . |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| accountNumber firstName lastName | accountNumber (default) firstName lastName |

| Note | You cannot
                                                				  modify or remove existing fields or append a new field to existing data. If
                                                				  overwriteData is set to true, any agent scheduled personal callback records are
                                                				  also overwritten. |
|---|---|

| Note | Avoid performing a bulk job transaction during a maintainence window. |
|---|---|

| Note | The
                                          			 descriptions for these parameters are the same as the descriptions for the
                                          			 parameters for create (single record), get, and update operations. Only the
                                          			 case is different. |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| agentId accountNumber firstName lastName | agentId accountNumber firstName lastName |

| Important | Microsoft periodically releases cumulative time zone updates. These updates include worldwide changes to time zone names,
                                       bias (the amount of time in minutes that a time zone is offset from Coordinated Universal Time (UTC)), and observance of daylight
                                       saving time. These patches update the information in the Windows registry. When these updates are available, apply them to
                                       all virtual machines in the deployment that are running a Microsoft Windows operating system. |
|---|---|