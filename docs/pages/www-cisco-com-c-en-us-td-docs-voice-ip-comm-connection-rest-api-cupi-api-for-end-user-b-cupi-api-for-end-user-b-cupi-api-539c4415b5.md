---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-539c4415b5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_0101.html
retrieved_at: 2026-08-21T08:04:38.217924+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 18, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Enabling and Disabling Greetings

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Enabling and Disabling Greetings

- Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Enabling and Disabling Greetings

- About Enabling and Disabling Greetings

- Examples

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Enabling and Disabling Greetings

Links to Other API pages: Cisco_Unity_Connection_APIs

## About Enabling and Disabling Greetings

Every user with a mailbox has an associated call handler, and thus a full compliment of greetings. The settings for each greeting
                              can be read by the following GET request:

```
GET /vmrest/user/greetings/{greeting type}
```

The GET request would produce the following response:

```
200
OK
<?xml version="1.0" encoding="UTF-8"?>
<Greeting>
  <TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
  <GreetingType>{greeting type}</GreetingType>
</Greeting>
```

## Examples

The different types of greetings available for every user and call handler are:

Alternae

Busy

Error

Internal

Off Hours

Standard

Holiday

Each greeting can be accessed through the following various GET requests:

```
GET /vmrest/user/greetings/Alternate
GET /vmrest/user/greetings/Busy
GET /vmrest/user/greetings/Error
GET /vmrest/user/greetings/Internal
GET /vmrest/user/greetings/Off%20Hours
GET /vmrest/user/greetings/Standard
GET /vmrest/user/greetings/Holiday
```

TimeExpires is the field that determines whether a greeting is enabled or disabled. To enable a greeting, TimeExpires needs
                              to be set to a future date, which is the date on which the greeting will expire (be disabled). To disable a greeting, simply
                              set TimeExpires to a date in the past. Also, if TimeExpires is set to null that means it is enabled indefinitely (currently
                              CUPI offers no ability to set this field to null).

TimeExpires is always calculated as GMT. Any time zone conversion is the responsibility of the client.

To enable the Holiday greeting until March 9th 2020, you would use the following PUT request:

```
PUT /vmrest/user/greetings/Holiday

<?xml version="1.0" encoding="UTF-8"?>
<Greeting>
  <TimeExpires>2020-03-09 00:00:00.0</TimeExpires>
</Greeting>
```

To disable the Holiday greeting you would do a PUT request with the TimeExpires field set to a date in the past, as follows:

```
PUT /vmrest/user/greetings/Holiday

<?xml version="1.0" encoding="UTF-8"?>
<Greeting>
  <TimeExpires>1970-01-01 00:00:00.0</TimeExpires>
</Greeting>
```

| GET /vmrest/user/greetings/{greeting type} |
|---|

| 200
OK
<?xml version="1.0" encoding="UTF-8"?>
<Greeting>
  <TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
  <GreetingType>{greeting type}</GreetingType>
</Greeting> |
|---|

| GET /vmrest/user/greetings/Alternate
GET /vmrest/user/greetings/Busy
GET /vmrest/user/greetings/Error
GET /vmrest/user/greetings/Internal
GET /vmrest/user/greetings/Off%20Hours
GET /vmrest/user/greetings/Standard
GET /vmrest/user/greetings/Holiday |
|---|

| PUT /vmrest/user/greetings/Holiday

<?xml version="1.0" encoding="UTF-8"?>
<Greeting>
  <TimeExpires>2020-03-09 00:00:00.0</TimeExpires>
</Greeting> |
|---|

| PUT /vmrest/user/greetings/Holiday

<?xml version="1.0" encoding="UTF-8"?>
<Greeting>
  <TimeExpires>1970-01-01 00:00:00.0</TimeExpires>
</Greeting> |
|---|