---
doc_id: developer-cisco-com-codeexchange-github-repo-ciscodevnet-botkit-template-ca2063e8a2
source_url: https://developer.cisco.com/codeexchange/github/repo/CiscoDevNet/botkit-template
retrieved_at: 2026-08-21T06:01:25.592676+00:00
---

# Botkit template

This project implements a Botkit + Webex adapter bot, based on the generator-botkit Yoeman template, providing a few extra good-practice features, plus several interesting samples:

Optionally use Webex Node.js SDK websockets for incoming events and messages, instead of webhooks

A 'health check' URL: check bot availability, uptime and metadata by browsing to the bot's public URL

Quality-of-life features: fallback/catch-all module; welcome message when user joins a space

'Help' command auto-generation function

Redis/MongoDB storage support for persistent/scalable storage of conversation state

checkAddMention() function to automatically format bot commands for 1:1 or group space usage

## Websockets vs. Webhooks

Most Botkit features can be implemented by using the Webex JS SDK websockets functionality, which establishes a persistent connection to the Webex cloud for outbound and inbound messages/events.

Webex also supports traditional HTTP webhooks for messages/events, which requires that your bot be accessible via a publically reachable URL.  A public URL is also needed if your bot will be serving any web pages/files, e.g. images associated with the cards and buttons feature or the health check URL.

- If you don't need to serve buttons and cards images, you can set the environment variable WEBSOCKET_EVENTS=True and avoid the need for a public URL

- If you are implementing buttons & cards, you will need a public URL (e. g. by using a service like Ngrok, or hosting your bot in the cloud) - configure this via the PUBLIC_URL environment variable

## How to run (local machine)

Assuming you plan to us ngrok to give your bot a publically available URL (optional, see above), you can run this template in a jiffy:

Clone this repo:

```
git clone https://github.com/CiscoDevNet/botkit-template.git cd botkit-template
```

Install the Node.js dependencies:

```
npm install
```

Create a Webex bot account at 'Webex for Developers' , and note/save your bot's access token

Launch Ngrok to expose port 3000 of your local machine to the internet:

```
ngrok http 3000
```

Note/save the 'Forwarding' HTTPS (not HTTP) address that ngrok generates

Rename the env.example file to .env , then edit to configure the settings and info for your bot.

Note: you can also specify any of these settings via environment variables (which will take precedent over any settings configured in the .env file) - often preferred in production environments.

To successfully run all of the sample features, you'll need to specify at minimum a PUBLIC_URL (ngrok HTTPS forwarding URL), and a WEBEX_ACCESS_TOKEN (Webex bot access token).

If running on Glitch.me or Heroku (with Dyno Metadata enbaled), the PUBLIC_URL will be auto-configured.

Additional values in the .env file (like OWNER and CODE ) are used to populate the healthcheck URL meta-data.

Be sure to save the .env file!

You're ready to run your bot:

```
node bot.js
```

## Quick start on Glitch.me

Click

Delete the .env file that Glitch created automatically

Rename .env.example to .env , then open it for editing.

Find the WEBEX_ACCESS_TOKEN variable, paste in your bot's access token

Optional : enter appropriate info in the "Bot meta info..." section

Note that, thanks to the Glitch PROJECT_DOMAIN env variable, you do not need to add a PUBLIC_URL variable pointing to your app domain

You bot is all set, responding in 1-1 and 'group' spaces, and sending a welcome message when added to a space!

You can verify the bot is up and running by browsing to its healthcheck URL (i.e. the app domain.)

## Quick start on Heroku

Create a new project pointing to this repo.

Open your app's Settings tab, and reveal your Config Vars

Add a WEBEX_ACCESS_TOKEN variable with your bot's access token as value

Add a PUBLIC_URL variable pointing to your app's Heroku URL

If your app is using Dyno Metadata , the public URL will be detected automatically

In the upper right under the More dropdown, select Restart all dynos

You bot is all set!  You can invite it to 1-1 and 'group' spaces, see it sending a welcome message when added, and responding to commands (try help .)

You can always verify the bot is operational by browsing to its healthcheck URL (i.e. the app domain.)

How do you like this sample code?