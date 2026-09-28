---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-3fdfc3d542
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_global-api_1501.html
retrieved_at: 2026-08-21T16:46:48.125233+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Global API

## Chapter: Global API

- Global API

- Global API

# Global API

## Global API

The Global API returns global settings from the following categories:

Call

Agent

Reporting

Script

Labels

Labels are applicable for Packaged CCE 2000 agent deployment only.

### URL

### Operations

list : Retrieves a list of global settings.

update : Updates global settings.

### Parameters

callReporting

defaultBucketInterval: Required. A reference to a bucket interval ( Bucket Interval API ), including refURL and name. See References .

defaultCallType: Required. A reference to a call type, including refURL and name. A call is categorized against this call
                                    type unless it comes into the system on a dialed number that is associated with another call type. See References .

serviceLevelType: Required. This value indicates how the system calculates the service level.

1: Ignore Abandoned Calls.

2: Abandoned Calls have Negative Impact.

3: Abandoned Calls have Positive Impact.

serviceLevelThreshold: Required. Maximum time in seconds that a caller should wait before being connected with an agent. Maximum
                                    is 86,400 seconds (1 day).

abandonCallWaitTime: Required. Configures the minimum time an incoming call must be queued before the call is considered abandoned
                                    if the caller ends the call. Maximum is 14400 seconds (4 hours).

answeredShortCallThreshold: Configures the maximum duration for a short call. Calls with a duration below that value are considered
                                    short. Value is between 0 and 14400 seconds (4 hours).

agent

agentPhoneLineControl: Indicates whether all agents supported on the agent peripheral can have one or more than one line configured.

0: Single Line.

1: All Lines.

nonACDLineImpact: Specifies how the agent state is set when the agent is on a call on a secondary line and agentPhoneLineControl
                                    is set to All Lines.

0: Available agent stays available.

1: Available agent goes not ready.

defaultDeskSetting: A reference to a desk setting ( Agent Desk Settings API ), including refURL and name.

loginNameCaseSensitivity: Identifies whether usernames are case-sensitive. Values are true/false.

minimumPasswordLength: Changing this value affects new passwords only and does not apply to existing ones. Value is between
                                    0 and 32.

reporting

reportingInterval: Configures the system to store historical information in 15-minute or 30-minute summaries. The 15-minute
                                    interval requires a larger amount of database space than the 30-minute interval. Values are 15 or 30.

script

retainScriptVersion: Defines the maximum number of versions of each routing script to maintain in the database. The system
                                    automatically deletes the oldest version when the limit is exceeded. Maximum is 100.

labels

cmLabel: Pattern that matches the Unified CM route pattern. Must be a 10-digit string.

cvpLabels: A collection of labels that include the pattern and routingClientName. The patterns should match the CVP Dialed
                                    Number patterns. Must be a 10-digit string.

outboundLabel: Pattern that matches IOS Voice Gateway dial-peer. Must be a 10-digit string.

datacenterSettings

A collection of data center settings including Agent and Labels categories. The refURL field is required for each data center
                                    setting. Under Agent, you can update the following parameters if Agent PG is created for this data center:

agentPhoneLineControl

nonACDLineImpact

defaultDeskSetting

Under Labels, you can update certain or all labels depending on the type of PGs that exist in the data center. For example,
                                    if only Agent PG is configured in the data center, you can update only cmLabel.

defaultSurveyAppName: Default application name for Cx KPI Survey.

If there is no specific application name (defaultSurveyAppName) in the Survey, it uses the default application name.

### Example Get Request

```
<globalSettings>
        <callReporting>
            <serviceLevelType/>
            <serviceLevelThreshold/>
            <abandonCallWaitTime/>
            <answeredShortCallThreshold/>
            <defaultCallType>
                <refURL/>
                <name/>
            </defaultCallType>
            <defaultBucketInterval>
                <refURL/>
                <name/>
            </defaultBucketInterval>
        </callReporting>
        <agent>
           <nonACDLineImpact/>
            <agentPhoneLineControl/>
            <defaultDeskSetting>
                <refURL>/unifiedconfig/config/agentdesksetting/5000</refURL>
                <name>Default_Agent_Desk_Settings</name>
            <defaultDeskSetting/>
            <loginNameCaseSensitivity/>
            <minimumPasswordLength/>
        </agent>
        <reporting>
            <reportingInterval/>
        </reporting>
        <script>
            <retainScriptVersion/>
        </script>
        <labels>
            <cmLabel>8881111000</cmLabel>
            <outboundLabel>6661111000</outboundLabel>
            <cvpLabels>
                <cvpLabel>
                    <routingClientName/>
                    <pattern/>
             </cvpLabel>
        </labels>
        <datacenterSettings>
            <datacenterSetting>
            <datacenter>
                <refURL> /unifiedconfig/config/datacenter/5000</refURL>
                <name>boston</name>
            </datacenter>
            <agent>
                <nonACDLineImpact/>
                <agentPhoneLineControl/>
                <defaultDeskSetting>
                    <refURL>/unifiedconfig/config/agentdesksetting/5000</refURL>
                    <name>Default_Agent_Desk_Settings</name>
                <defaultDeskSetting/>
            <agent>
            <labels>
                <cmLabel/>
                <outboundLabel/>
                <cvpLabels>
                    <cvpLabel>
                        <routingClientName/>
                        <pattern/>
                    </cvpLabel>
                </cvpLabels>
            </labels>
        </datacenterSetting>
    </datacenterSettings>
<defaultSurveyAppName>DefaultKPISurvey</defaultSurveyAppName>
</globalSettings>
```

### Example Update Request

```
<globalSettings>
              <changeStamp>59</changeStamp>
              <callReporting>
                     <serviceLevelType>2</serviceLevelType>
                     <serviceLevelThreshold>10</serviceLevelThreshold>
                     <abandonCallWaitTime>300</abandonCallWaitTime>
                     <answeredShortCallThreshold>30</answeredShortCallThreshold>
                     <defaultCallType>
                            <refURL>/unifiedconfig/config/calltype/5000</refURL>
                     </defaultCallType>
                     <defaultBucketInterval>
                            <refURL>/unifiedconfig/config/bucketinterval/5001</refURL>
                     </defaultBucketInterval>
              </callReporting>
              <agent>
                    <agentPhoneLineControl>1</agentPhoneLineControl>
                    <nonACDLineImpact>0</nonACDLineImpact>
                    <defaultDeskSetting>
                         <refURL>/unifiedconfig/config/agentdesksetting/5003</refURL>
                    </defaultDeskSetting>
                   <loginNameCaseSensitivity>true</loginNameCaseSensitivity>
                    <minimumPasswordLength>8</minimumPasswordLength>
              </agent>
              <reporting>
                     <reportingInterval>15</reportingInterval>
              </reporting>
              <script>
                     <retainScriptVersion>5</retainScriptVersion>
              </script>
              <labels>
                      <cmLabel>8881111000</cmLabel>
                      <outboundLabel>6661111000</outboundLabel>
                      <cvpLabels>
                           <cvpLabel>
                               <routingClientName>CVP_PG_1A</routingClientName>
                               <pattern>7777777771</pattern>
                           </cvpLabel>
                           <cvpLabel>
                               <routingClientName>CVP_PG_1B</routingClientName>
                               <pattern>7777777772</pattern>
                            </cvpLabel>
                       </cvpLabels>
														</labels>
              <datacenterSettings>
                 <datacenterSetting>
                     <datacenter>
                            <refURL> /unifiedconfig/config/datacenter/5000</refURL>
                     </datacenter>
                     <agent>
                            <agentPhoneLineControl>1</agentPhoneLineControl>
                            <nonACDLineImpact>0</nonACDLineImpact>
                            <defaultDeskSetting>
														<refURL>/unifiedconfig/config/agentdesksetting/5003</refURL>
                            														</defaultDeskSetting>
              </agent>
              <labels>
                     <cmLabel>8881111000</cmLabel>
                     <outboundLabel>6661111000</outboundLabel>
                     <cvpLabels>
																					<cvpLabel>
														<routingClientName>boston_CVP_PG_1A</routingClientName>
                                          <pattern>7777777771</pattern>
                                   </cvpLabel>
																																			<cvpLabel>
														<routingClientName>boston_CVP_PG_1B</routingClientName>
                                          <pattern>7777777772</pattern>
                                   </cvpLabel>
                            </cvpLabels>
                     </labels>
              </datacenterSetting>
       </datacenterSettings>
<defaultSurveyAppName>DefaultKPISurvey</defaultSurveyAppName>
 </globalSettings>
```

### Example Get/Update Request for Packaged CCE 4000 Agents and 12000 Agents Deployment

```
<globalSettings>
<changeStamp>59</changeStamp>
<callReporting>
<serviceLevelType>2</serviceLevelType>
<serviceLevelThreshold>10</serviceLevelThreshold>
<abandonCallWaitTime>300</abandonCallWaitTime>
<answeredShortCallThreshold>30</answeredShortCallThreshold>
<defaultCallType>
<refURL>/unifiedconfig/config/calltype/5000</refURL>
</defaultCallType>
<defaultBucketInterval>
<refURL>/unifiedconfig/config/bucketinterval/5001</refURL>
</defaultBucketInterval>
</callReporting>
<agent>
<agentPhoneLineControl>1</agentPhoneLineControl>
<nonACDLineImpact>0</nonACDLineImpact>
<defaultDeskSetting>
<refURL>/unifiedconfig/config/agentdesksetting/5003</refURL>
</defaultDeskSetting>
<loginNameCaseSensitivity>true</loginNameCaseSensitivity>
<minimumPasswordLength>8</minimumPasswordLength>
</agent>
<reporting>
<reportingInterval>15</reportingInterval>
</reporting>
<script>
<retainScriptVersion>5</retainScriptVersion>
</script>
</globalSettings>
```

| Note | Labels are applicable for Packaged CCE 2000 agent deployment only. |
|---|---|