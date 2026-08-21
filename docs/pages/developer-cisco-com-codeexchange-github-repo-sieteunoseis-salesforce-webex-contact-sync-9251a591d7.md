---
doc_id: developer-cisco-com-codeexchange-github-repo-sieteunoseis-salesforce-webex-contact-sync-9251a591d7
source_url: https://developer.cisco.com/codeexchange/github/repo/sieteunoseis/salesforce-webex-contact-sync
retrieved_at: 2026-08-21T06:01:09.282329+00:00
---

# Salesforce to Webex Contact Sync

This is a Node.js app that uses Salesforce and Webex Oauth to sync contacts from Salesforce to Webex.  It is intended to be used as a reference for developers who want to build a similar integration.

## Overview

This project creates a locally running Node.js web server which lets you authenticate using a Webex Integration OAuth redirect URL flow. It then sets up a cron job to continually refresh the access token. In example, the project refreshes the token ever 24 hours.

Project then uses the access token to sync contacts from Salesforce to Webex.

## Setup

### Prerequisites & Dependencies:

- Node 16+

- Webex User Account

- Additional information available here: https://developer.webex.com/docs/integrations

- Salesforce User Account

- Additional information available here: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_authentication.htm

### Installation Steps:

Clone this repository and change directory:

```
git clone https://github.com/sieteunoseis/salesforce-webex-contact-sync.git && cd salesforce-webex-contact-sync
```

Rename the example environment file from .env.example to .env :

```
cp env.example .env
```

Configure the environment file for the Salesforce/Webex OAuth Integration. Additional guide on where to get these values is below

```
SALESFORCE_CLIENT_ID = <CLIENT_ID> SALESFORCE_CLIENT_SECRET = <CLIENT_SECRET> SALESFORCE_USERNAME = <USERNAME> SALESFORCE_PASSWORD = <PASSWORD> SALESFORCE_SECURITYTOKEN = <SECURITY_TOKEN> WEBEX_ORG_ID = <ORG_ID> WEBEX_APP_CLIENT_ID = <CLIENT_ID> WEBEX_APP_CLIENT_SECRET = <CLIENT_SECRET> WEBEX_APP_RETURN_URL = http://localhost:3000 WEBEX_APP_REDIRECT_URL = http://localhost:3000/oauth WEBEX_APP_AUTHORIZATION_URL = https://webexapis.com/v1/authorize WEBEX_APP_TOKEN_URL = https://webexapis.com/v1/access_token WEBEX_APP_SCOPES = Identity:contact PORT = 3000
```

Install project:

```
npm install
```

Start the server in development mode (using a local env file):

```
npm run dev
```

or start the server in production mode:

```
npm run start
```

Navigate using your browser to the link below to begin the OAuth flow which will give this project a refresh and access token based off your Webex Account:

```
http://localhost:3000
```

### Docker Setup:

#### Build and run using Docker:

```
npm run docker:build
npm run docker:run
```

Note: Update the config section of the package.json file to change the name and platform.

#### OR

#### Pull image from Docker.io and run with the following::

```
docker run -d -p 3000:3000 --name salesforce-webex-sync --restart=always --env-file=.env -v ./data:/app/data sieteunoseis/salesforce-webex-contact-sync:latest
```

#### Setup Webex OAuth Integration:

Navigate to this page to create a new Webex Integration using your Webex Account: https://developer.webex.com/my-apps

Click on Create a New App

Click on Integration

Fill out your intergration details, enter any name and decription and select any icon:

- For Redirect URI(s), enter: http://localhost:3000/oauth (or the url where you intend to deploy this code.  The app expects the url to end in /oauth )

- For scopes, select only Identity:contact (or the scopes you intend to use for your integration)

Scroll to the bottom and click Add Integration.

Take a note of the Client ID and Client Secret for the environment file configuration above

#### Setup Salesforce OAuth Integration:

- Navigate to this page to create a new Salesforce Integration using your Salesforce Account: https://login.salesforce.com/

- Click on Setup

- Click on Apps

- Click on App Manager

- Click on New Connected App

- For Callback URL, enter: http://localhost:3000/oauth (or the url where you intend to deploy this code.  The app expects the url to end in /oauth )

- For Selected OAuth Scopes, select only Manage user data via APIs (api) (or the scopes you intend to use for your integration)

- Click on Save

- Once saved click on Manage Consumer Details

- Take a note of the Consumer Key and Consumer Secret for the environment file configuration above

- Click on Manage at the top and then Edit Policies

- Under OAuth Policies select All users may self-authorized

- Under IP Relaxation, select Relax IP restrictions

- Click on Save

- Next select Settings > Identity > OAuth and OpenID Connect Settings.

- Under OAuth and OpenID Connect Settings select Allow OAuth Username-Password Flows

## Screenshots

## License

All contents are licensed under the MIT license. Please see license for details.

## Giving Back

If you would like to support my work and the time I put in creating the code, you can click the image below to get me a coffee. I would really appreciate it (but is not required).

How do you like this sample code?