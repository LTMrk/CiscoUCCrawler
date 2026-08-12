[](https://developer.webex.com/)
[Getting Started](https://developer.webex.com/create/docs)Documentation![](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers)[AI in Webex](https://developer.webex.com/mcp/docs/webex-mcp-server-overview)Blog![](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers)[Support](https://developer.webex.com/explore/support)Resources![](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers)
[Log in](https://developer.webex.com/login)[Sign up](https://developer.webex.com/signup)
[Home](https://developer.webex.com/)/Overview
AI in Webex
  * Webex MCP Servers
  * Security Guides
  * Cisco Onboarded MCP Servers
  * Federated through External Registery
  * Agentic Apps
  * Connect Webex MCP Servers to External Clients
    * [Overview](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers)
    * [Amazon Quick](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers-amazon-quick)
    * [Claude Code](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers-claude-code)
    * [Claude Desktop](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers-claude-desktop)
    * [Codex](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers-codex)
    * [Copilot Studio](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers-copilot-studio)
    * [Cursor](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers-cursor)
    * [Gemini CLI](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers-gemini-cli)
    * [VS Code](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers-vscode)
  * Connect External MCP Servers to Webex AI
  * [Beta Program Overview](https://developer.webex.com/mcp/docs/webex-developer-beta-program)


## AI in Webex
### Overview
This guide helps developers integrate Webex MCP (Model Context Protocol) servers with popular AI clients. MCP enables AI agents to securely access Webex capabilities through the Model Context Protocol.
####  anchorOverview
anchor
Webex provides MCP servers that enable AI agents to securely access various Webex functionalities through the Model Context Protocol. These servers act as a bridge between your AI client and Webex services, allowing AI agents to perform actions and retrieve information on your behalf.
####  anchorAuthentication
anchor
Webex MCP servers support two authorization methods: Token-Based authentication and OAuth 2.0. Please verify the required authentication approach before generating the token.
###### 1. Token-Based Authentication
Use a WCIT (Webex Client Identity Token) to authenticate with Webex MCP servers. The WCIT is issued with only the `spark:mcp` scope which will allow to connect to MCP server. Additional scopes required by specific tools are requested at runtime via MCP elicitation during too call.
> **Note** : This method only works with clients that support MCP elicitation. If your client does not support elicitation, use OAuth 2.0 instead.
> **What is MCP elicitation?** Elicitation is a capability in the MCP protocol that allows an MCP server to request additional information from the user during a tool call — for example, prompting the user to grant consent for specific OAuth scopes. When using a WCIT token, the initial connection uses only the `spark:mcp` scope. When a tool requires additional scopes (e.g., `meeting:schedules_read`), the server uses elicitation to ask the user to authorize those scopes in real time. Clients that support elicitation can handle this flow seamlessly; clients that do not will fail on tools requiring additional scopes.
  1. Navigate to the [Generate WCIT Token](https://developer.webex.com/agentic-token) page in the Webex Developer Portal
  2. Enter an appropriate name for your token
  3. Click **Generate New Token**
  4. Copy the generated token and store it securely (you'll need this for configuration)


> **Important** : Keep your token secure and never commit it to version control.
###### 2. OAuth 2.0
OAuth 2.0 can be used by clients that do not support elicitation. This requires creating a Webex Integration with the appropriate scopes.
  1. Navigate to the [Create a New Integration](https://developer.webex.com/my-apps/new/integration) page
  2. Fill in the form:
     * **Will this integration use a mobile SDK?** No
     * **Integration name:** Give any name
     * **Icon:** Choose one of the default icons
     * **App Hub Description:** Give any description
     * **Redirect URI(s):** You'll get this from the OAuth configuration page in your client
     * **Scopes:** Select the scopes required by your MCP server along with `spark:mcp`. To find the required scopes, go to the [Agentic Apps](https://apphub.webex.com/agentic-apps) page, choose your server, and click **Learn More** to open the MCP Server product page in Developer Portal where the required scopes are listed.
  3. Click **Add Integration** to create your integration
  4. On the following screen note down the **Client ID** and **Client Secret** — you won't be able to read your Client Secret again once you leave this page


####  anchorConfigure Your AI Client
anchor
Choose your AI client below and follow the configuration guide:
  * [Amazon Quick](https://developer.webex.com/docs/webex-agentic-mcp-servers-amazon-quick)
  * [Claude Code](https://developer.webex.com/docs/webex-agentic-mcp-servers-claude-code)
  * [Claude Desktop](https://developer.webex.com/docs/webex-agentic-mcp-servers-claude-desktop)
  * [Codex](https://developer.webex.com/docs/webex-agentic-mcp-servers-codex)
  * [Copilot Studio](https://developer.webex.com/docs/webex-agentic-mcp-servers-copilot-studio)
  * [Cursor](https://developer.webex.com/docs/webex-agentic-mcp-servers-cursor)
  * [Gemini CLI](https://developer.webex.com/docs/webex-agentic-mcp-servers-gemini-cli)
  * [VS Code](https://developer.webex.com/docs/webex-agentic-mcp-servers-vscode)


* * *
####  anchorTroubleshooting
anchor
###### Common Issues
###### Connection Failed
**Problem** : MCP server fails to connect
**Solutions** :
  * Verify your WCIT token is valid and not expired
  * Check that the endpoint URL is correct
  * Ensure you have an active internet connection


###### Authentication Error
**Problem** : "401 Unauthorized" or authentication errors
**Solutions** :
  * Regenerate your WCIT token from the Developer Portal
  * Ensure the token is properly formatted with "Bearer " prefix in the configuration
  * Check that the token hasn't been revoked


###### Server Not Responding
**Problem** : MCP server is not responding to requests
**Solutions** :
  * Verify your firewall isn't blocking the connection
  * Try restarting your AI client


###### Tools Not Appearing
**Problem** : Webex tools don't show up in the AI client
**Solutions** :
  * Confirm the configuration file syntax is correct (valid JSON)
  * Restart the AI client completely
  * Check the AI client's console/logs for error messages
  * Verify you're using the latest version of your AI client:
    * **Claude Desktop** : Check for updates via Claude menu > "Check for Updates..."
    * **VS Code** : Ensure GitHub Copilot extension is up to date
    * **Cursor** : Check for IDE updates in Cursor settings


###### Getting Help
If you continue to experience issues, visit the [Webex Developer Support](https://developer.webex.com/explore/support).
####  anchorManaging Your MCP Connection
anchor
###### Unlinking an MCP Server
If you need to remove an MCP server from your AI client:
**Claude Desktop:**
  1. Open Settings > Developer tab
  2. Click "Edit Config" to open `claude_desktop_config.json`
  3. Remove the server entry from the `mcpServers` object
  4. Save the file and restart Claude Desktop


**VS Code:**
  1. Use Command Palette: **MCP: Remove Server** and select the server to remove, or
  2. Manually edit `mcp.json` (global or workspace) and remove the server entry from the `servers` object
  3. Reload the VS Code window


**Cursor IDE:**
  1. Open Cursor Settings > Tools & Integrations > MCP Tools
  2. Remove the server entry from `~/.cursor/mcp.json`
  3. Save the file (Cursor will automatically detect the change)


###### Revoking Your WCIT Token
If your token is compromised or you no longer need it:
  1. Navigate to the **Manage WCIT Tokens** page in the Webex Developer Portal
  2. Locate the token you want to revoke in the list
  3. Click the **Delete** button next to the token
  4. Confirm the revocation


> **Important** : After revoking a token, any AI clients using that token will immediately lose access to Webex MCP servers. You'll need to generate a new token and update your client configurations.
####  anchorNext Steps
anchor
Now that you've connected your Webex MCP server, you can:
  * Explore the available Webex capabilities in your AI client
  * Build custom workflows using Webex messaging and collaboration features
  * Create intelligent agents that interact with your Webex organization


* * *
**Last Updated** : February 2, 2026
**Questions or Feedback?** Visit the [Webex Developer Community](https://community.cisco.com/t5/webex-for-developers/bd-p/disc-webex-developers) or contact support through the Developer Portal.
##### In This Article
  * [Overview](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers#overview)
  * [Authentication](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers#authentication)
  * [Configure Your AI Client](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers#configure-your-ai-client)
  * [Troubleshooting](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers#troubleshooting)
  * [Managing Your MCP Connection](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers#managing-your-mcp-connection)
  * [Next Steps](https://developer.webex.com/mcp/docs/webex-agentic-mcp-servers#next-steps)


##### Related Resources
  * [Webex Developer Portal](https://developer.webex.com "Webex Developer Portal")
  * [Model Context Protocol Specification](https://modelcontextprotocol.io "Model Context Protocol Specification")


## Connect
[Support](https://developer.webex.com/support)
[Developer Community](https://community.cisco.com/t5/webex-for-developers/bd-p/disc-webex-developers)
[Developer Events](https://developer.webex.com/blog/categories/events)
[Contact Sales](https://www.webex.com/contact-sales.html?TrackID=1017639&hbxref=&goid=us_contact_sales)
## Handy Links
[Webex Ambassadors](https://www.essentials.webex.com/programs/ambassadors)
[Webex App Hub](https://www.essentials.webex.com/programs/ambassadors)
## Resources
[Open Source Bot Starter Kits](https://ciscowebexteamsambassadors.github.io/StarterKits/)
[Download Webex](https://ciscowebexteamsambassadors.github.io/StarterKits/)
[DevNet Learning Labs](https://www.webex.com)
[Terms of Service](https://developer.webex.com/terms-of-service)
[Privacy Policy](https://www.cisco.com/c/en/us/about/legal/privacy.html)
[Cookie Policy](https://www.cisco.com/c/en/us/about/legal/privacy.html#cookies)
[Trademarks](https://www.cisco.com/c/en/us/about/legal/trademarks.html)
© 2026 Cisco and/or its affiliates. All rights reserved.
[](https://github.com/webex)[](https://www.facebook.com/CiscoCollab/)[](https://twitter.com/webexdevs)[](https://www.youtube.com/playlist?list=PL2k86RlAekM_bIUrvVw4Haq_0xxTez9zU)[](https://www.linkedin.com/company/webex/)
By continuing to use our website, you acknowledge the use of cookies. 
[Privacy Statement](https://www.cisco.com/c/en/us/about/legal/privacy-full.html) Change Settings
![Company Logo](https://cdn.cookielaw.org/logos/03fc55fe-0057-4b2f-817d-763e7ecdb316/a7f4c642-c43c-4666-acea-858c0449029c/cisco-logo-transparent.png)
## Consent Manager
Your opt out preference signal is honored.
## Consent Manager
  * ### Your Privacy
  * ### Strictly Necessary Cookies
  * ### Performance Cookies
  * ### Targeting Cookies
  * ### Functional Cookies


#### Your Privacy
When you visit any website, it may store or retrieve information on your browser, mostly in the form of cookies. This information might be about you, your preferences or your device and is mostly used to make the site work as you expect it to. The information does not usually directly identify you, but it can give you a more personalized web experience. Because we respect your right to privacy, you can choose not to allow some types of cookies. From the list on left, please choose whether this site may use Performance and/or Targeting Cookies. By selecting Strictly Necessary Cookies only, you are requesting Cisco not to sell or share your personal data. Note, blocking some types of cookies may impact your experience on the site and the services we are able to offer.
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies provide metrics related to the performance and usability of our site. They are primarily focused on gathering information about how you interact with our site, including: page load times, response times, error messages, and allowing a replay of a visitor’s interactions with our site, which enables us to review and analyze visitor behavior, helping to improve site usability and functionality. These cookies also allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. If you do not allow these cookies we will not know when you have visited our site and will not be able to monitor its performance.
Cookies Details
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Cookies Details
Back Button
### Cookie List
Filter Button
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Clear
  * checkbox label label


Apply Cancel
Save Settings
Allow All
[![Powered by Onetrust](https://cdn.cookielaw.org/logos/static/powered_by_logo.svg)](https://www.onetrust.com/solutions/consent-and-preferences/)
