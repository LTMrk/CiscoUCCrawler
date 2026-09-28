---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-all-models-xsi-9-1-1-cuip-bk-p82b3b16-00-phones-services-application--147743851e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/all_models/xsi/9-1-1/CUIP_BK_P82B3B16_00_phones-services-application-development-notes/CUIP_BK_P82B3B16_00_phones-services-application-development-notes_appendix_01011.html
retrieved_at: 2026-08-16T18:02:09.921597+00:00
---

Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones

# Cisco Unified IP Phone Services Application Development Notes for Cisco Unified Communications Manager and Multiplatform Phones

Updated: August 6, 2026

Chapter: CiscoIPPhone XML Object Quick Reference

## Chapter: CiscoIPPhone XML Object Quick Reference

- CiscoIPPhone XML Object Quick Reference

# CiscoIPPhone XML Object Quick Reference

The following sections provide a quick reference of the CiscoIPPhone XML objects and the definitions that are associated with
                           each object.

## CiscoIPPhoneMenu

```
<CiscoIPPhoneMenu>
  <Title>Title text goes here</Title>
  <Prompt>Prompt text goes here</Prompt>
  <MenuItem>
    <Name>The name of each menu item</Name>
    <URL>The URL associated with the menu item</URL>
  </MenuItem>
</CiscoIPPhoneMenu>
```

## CiscoIPPhoneText

```
<CiscoIPPhoneText>
  <Title>Title text goes here</Title>
  <Prompt>The prompt text goes here</Prompt>
  <Text>Text to display as the message body goes here</Text>
</CiscoIPPhoneText>
```

## CiscoIPPhoneInput

```
<CiscoIPPhoneInput>
  <Title>Directory title goes here</Title>
  <Prompt>Prompt text goes here</Prompt>
  <URL>The target URL for the completed input goes here</URL>
  <InputItem>
    <DisplayName>Name of input field to display</DisplayName>
    <QueryStringParam>The parameter to be added to the target URL</QueryStringParam>
    <DefaultValue>Value</DefaultValue>
    <InputFlags>The flag specifying the type of allowable input</InputFlags>
  </InputItem>
</CiscoIPPhoneInput>
```

## CiscoIPPhoneDirectory

```
<CiscoIPPhoneDirectory>
  <Title>Directory title goes here</Title>
  <Prompt>Prompt text goes here</Prompt>
  <DirectoryEntry>
    <Name>The name of the directory entry</Name>
    <Telephone>The telephone number for the entry</Telephone>
  </DirectoryEntry>
</CiscoIPPhoneDirectory>
```

## CiscoIPPhoneImage

```
<CiscoIPPhoneImage WindowMode="XSI window width mode">
  <Title>Image title goes here</Title>
  <Prompt>Prompt text goes here</Prompt>
  <LocationX>Position information of graphic</LocationX>
  <LocationY>Position information of graphic</LocationY>
  <Width>Size information for the graphic</Width>
  <Height>Size information for the graphic</Height>
  <Depth>Number of bits per pixel</Depth>
  <Data>Packed Pixel Data</Data>
   <SoftKeyItem>
    <Name>Name of the soft key</Name>
    <URL>URL of soft key</Name>
    <Position>Numerical position of the soft key</Position>
   </SoftKeyItem>
</CiscoIPPhoneImage>
```

## CiscoIPPhoneImageFile

```
<CiscoIPPhoneImageFile WindowMode="Width Mode of XSI window">
  <Title>Image Title goes here</Title>
  <Prompt>Prompt text goes here</Prompt>
  <LocationX>Horizontal position of graphic</LocationX>
  <LocationY>Vertical position of graphic</LocationY>
  <URL>Points to the PNG image</URL>
</CiscoIPPhoneImageFile>
```

## CiscoIPPhoneGraphicMenu

```
<CiscoIPPhoneGraphicMenu WindowMode="Width Mode of XSI window">
  <Title>Menu title goes here</Title>
  <Prompt>Prompt text goes here</Prompt>
  <LocationX>Position information of graphic</LocationX>
  <LocationY>Position information of graphic</LocationY>
  <Width>Size information for the graphic</Width>
  <Height>Size information for the graphic</Height>
  <Depth>Number of bits per pixel</Depth>
  <Data>Packed Pixel Data</Data>
  <MenuItem>
    <Name>The name of each menu item</Name>
    <URL>The URL associated with the menu item</URL>
  </MenuItem>
</CiscoIPPhoneGraphicMenu>
```

## CiscoIPPhoneGraphicFileMenu

```
<CiscoIPPhoneGraphicFileMenu WindowMode="Width Mode of XSI window">
  <Title>Image Title goes here</Title>
  <Prompt>Prompt text goes here</Prompt>
  <LocationX>Horizontal position of graphic</LocationX>
  <LocationY>Vertical position of graphic</LocationY>
  <URL>Points to the PNG background image</URL>
  <MenuItem>
    <Name>Same as CiscoIPPhoneGraphicMenu</Name>
    <URL>Invoked when the TouchArea is touched</URL>
    <TouchArea X1="left edge" Y1="top edge" X2="right edge" Y2="bottom edge"/>
  </MenuItem>
</CiscoIPPhoneGraphicFileMenu>
```

## CiscoIPPhoneIconMenu

```
<CiscoIPPhoneIconMenu>
  <Title>Title text goes here</Title>
  <Prompt>Prompt text goes here</Prompt>
  <MenuItem>
    <IconIndex>Indicates what IconItem to display</IconIndex>
    <Name>The name of each menu item</Name>
    <URL>The URL associated with the menu item</URL>
  </MenuItem>
  <SoftKeyItem>
    <Name>Name of softkey</Name>
    <URL>URL or URI of softkey</URL>
    <Position>Position information of the softkey</Position>
  </SoftKeyItem>
  <IconItem>
    <Index>A unique index from 0 to 9</Index>
    <Height>Size information for the icon</Height>
    <Width>Size information for the icon</Width>
    <Depth>Number of bits per pixel</Depth>
    <Data>Packed Pixel Data</Data>
  </IconItem>
</CiscoIPPhoneIconMenu>
```

## CiscoIPPhoneIconFileMenu

```
<CiscoIPPhoneIconFileMenu>
  <Title>Title text goes here</Title>
  <Prompt>Prompt text goes here</Prompt>
  <MenuItem>
    <IconIndex>Indicates what IconItem to display</IconIndex>
    <Name>The name of each menu item</Name>
    <URL>The URL associated with the menu item</URL>
  </MenuItem>
  <IconItem>
    <Index>A unique index from 0 to 9</Index>
    <URL>location of the PNG icon image</URL>
  </IconItem>
</CiscoIPPhoneIconFileMenu>
```

## CiscoIPPhoneStatus

```
<CiscoIPPhoneStatus>
  <Text>This is the text area</Text>
  <Timer>Timer seed value in seconds</Timer>
  <LocationX>Horizontal alignment</LocationX>
  <LocationY>Vertical alignment</LocationY>
  <Width>Pixel width of graphic</Width>
  <Height>Pixel height of graphic</Height>
  <Depth>Color depth in bits</Depth>
  <Data>Hex binary image data</Data>
</CiscoIPPhoneStatus>
```

## CiscoIPPhoneStatusFile

```
<CiscoIPPhoneStatusFile>
<Text>This is the text area</Text>
<Timer>Timer seed value in seconds</Timer>
<LocationX>Horizontal alignment</LocationX>
<LocationY>Vertical alignment</LocationY>
<URL>location of the PNG image</URL>
</CiscoIPPhoneStatusFile
```

## CiscoIPPhoneExecute

```
<CiscoIPPhoneExecute>
  <ExecuteItem URL=”The URL or URI to be executed”/>
</CiscoIPPhoneExecute>
```

## CiscoIPPhoneError

```
<CiscoIPPhoneError Number=”x”/>
```

## CiscoIPPhoneResponse

```
<CiscoIPPhoneResponse>
  <ResponseItem Status”the success or failure of the action”Data=”the information associated with the request” URL=”the URL or URI specified in the Execute object”/>
</CiscoIPPhoneResponse>
```