---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-213516-configure-si-3a789e894f
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/213516-configure-sip-normalization-script-in-cc.html
retrieved_at: 2026-08-20T21:33:35.494463+00:00
---

Configure SIP Normalization Script in CCM

# Configure SIP Normalization Script in CCM

Updated: July 26, 2018

Document ID: 213516

Contents

## Contents

## Introduction

This document describes how to use Session Initiation Protocol (SIP) Normalization Script in Cisco Call Manager (CCM) with few basic examples.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communications Manager (CUCM) version 8.x and later

- SIP protocol

- Scripting Knowledge

### Components Used

The information in this document is based on CCM version 11.5.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configure

### Apply Script on Trunk in CUCM

In case of SIP Trunk, the script needs to be applied on the SIP trunk directly. The use of script on SIP profile instead of Trunk will not work.

Here are the steps that you need to follow:

- Navigate to Device > Device Setting > SIP Normalization Script Configuration and add a new Script as shown in the image.

2. Navigate to Device > Trunk .

Select the Trunk on which you want to apply the script and on the configuration page of it, select the script created earlier. Select the Enable Trace option and it will print the changes done by the script in the Signal Distribution Layer (SDL) logs as shown in the image. Save the configuration, Apply Config followed by reset of the trunk in order for the changes to take effect.

### Apply Script on SIP Phone

In case of SIP Phones, you have to use the Script on SIP Profile of the Phones.

Here are the steps that you need to follow.

- Navigate to Device > Device Setting > SIP Normalization Script and add the New Script.

- Navigate to Device > Device Setting > SIP profile . Select the SIP Profile on which you want to apply the script or create a new one by copying the Standard SIP Profile.

- On the Configuration Page of SIP Profile, select the Script followed by Apply Config and Reset the profile.

- Navigate to Device > Phone . Select the Phone on which you want to apply the script and change the SIP Profile of it with the one created one followed by saving it, apply the config and reset the Phone in order to take changes.

## Develop Script for Common Scenarios

The main source for detailed steps on how to develop SIP normalization script is here: Developer Guide for SIP Transparency and Normalization .

This guide contains different functions which are available to do manipulation in SIP messages and Session Description Protocol (SDP) content and other advanced APIs.

Here are few basic example script:

### Modify Header

Here you replace the anonymous from From Header of outgoing SIP INVITE/REINVITE message.

```
M = {}

 function M.outbound_INVITE(msg)

     -- Replacing the Anonymous from From Header

     local from = msg:getHeader("From")

     local newfrom = string.gsub(from, "anonymous" ,"1111")

     msg:modifyHeader("From", newfrom)

 end

 return M
```

Lua function which is applied to M(SIP Message) in outbound direction INVITE/REINVITE message. The direction is always decided in terms of CUCM, whether it is incoming or outgoing to it. Message type can be of different types like INVITE, 183, 200.

For more details, refer to the Overview Section of the Developers Guide for SIP Normalization.

### Remove Header

Here, you remove Cisco-Guide header from incoming SIP INVITE/REINVITE message:

```
M = {}

      function M.inbound_INVITE(msg)   

          msg:removeHeader("Cisco-Guid")

      end

    return M
```

### Add Header

Here, you add the INFO in the content of Allow header.

This is added in the original content of Allow after a comma.

```
M = {}

      function M.outbound_INVITE(msg)   

           msg:addHeader("Allow", "INFO")

      end

    return M
```

### Manipulate SDP Content

There are APIs available in order to modify the SDP content from a SIP Message. In order to modify SDP, it must obtain the SDP content body from the Lua SIP Message object with the getSdp() API provided by the SIP Message object. The script can then use the string library which includes Cisco's APIs in order to manipulate the SDP. On modification, the SDP is written back to the SIP Message object with the setSdp(sdp) API provided by the SIP Message object. Refer SIP Messages APIs for further information of these APIs.

```
local sdp = msg:getSdp()

-- modification of the SDP happens at this point

-- Update the SDP associated with the SIP message

msg: etSdp(sdp)
```

Note : The code changes a= line for G.722 codec to be G722 without the dot.

```
M = {}

function M.inbound_INVITE(msg)
        local sdp = msg:getSdp()

 

        if sdp
        then
               local g722_line = sdp:getLine("a=","G.722")

 

               if g722_line
               then
                      --Replace G.722 with G722. The dot is special and must be escaped using % when using gsub.
                      g722_line = g722_line:gsub("G%.722", "G722")
                      sdp = sdp:modifyLine("a=", "G.722", g722_line)
                      msg:setSdp(sdp)
                end
          end
end

return M
```

## Verify

Use this section in order to confirm that your configuration works properly.

Enable Trace Option when you apply the script in order to verify if the Script works or not from the SDL logs.

## Troubleshoot

This section provides information you can use in order to troubleshoot your configuration.

Here are a few checks if the script do not work as expected:

- If the script do not get executed by itself (Look for Before Normalization/After Normalization in the SDL logs) then most likely, it has not been applied correctly on the device or some syntax error.

- Verify the CUCM normalizations functions from developers guide and for Lua, use any available Compiler in order to verify it.

- If the script do gets executed but it does not make any changes, then check for the direction, Message type and the logic used in the script.

## Related Information

- https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/sip_tn/8_5_1/sip_t_n/8-trace.html

- https://supportforums.cisco.com/t5/collaboration-voice-and-video/a-guide-to-sip-normalization-on-cucm-and-lua-scripting/ba-p/3099409

- Technical Support & Documentation - Cisco Systems

| Code | Explanation |
|---|---|
| M={} | Initialization of the Message Content. M gets all the content of SIP Message here |
| function M.outbound_INVITE(msg) | Lua function which is applied to M(SIP Message) in outbound direction INVITE/REINVITE message. The direction is always decided in terms of CUCM, whether it is incoming or outgoing to it. Message type can be of different types like INVITE, 183, 200. For more details, refer to the Overview Section of the Developers Guide for SIP Normalization. |
| local from = msg:getHeader("From") | Stores the content of From message in local variable form |
| getHeader | One of the functions available for normalization in CCM in order to get the content of a Header in variable |
| string.gsub | A Lua Function in order to replace a particular content from string |
| modifyHeader | Again, a function available in CCM in order to modify the content of header |