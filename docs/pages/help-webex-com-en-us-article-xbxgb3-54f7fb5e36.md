---
doc_id: help-webex-com-en-us-article-xbxgb3-54f7fb5e36
source_url: https://help.webex.com/en-us/article/xbxgb3
retrieved_at: 2026-11-02T13:07:04.653299+00:00
---

## Register your phone

Depending on how your administrator configures your phone on the call control system, you
      might use one of the following methods to register your phone:

- Method 1 : No action is required during the phone registration. The registration is done automatically.

- Method 2 : A 16-digit activation code is required during the phone registration. You can get it from your administrator in advance. Enter the activation code when you are prompted for it.

- Method 3 : A service domain and user credentials (user ID and password) are required if you select domain  during the phone registration. You can get it from your administrator in advance. Enter the service domain and then user credentials when you are prompted for it.

- Method 4 : An alternate TFTP server address is required if your phone is missing a TFTP address. You can get it from your administrator when this situation occurs. You need to manually enter the alternate TFTP server to continue the registration.

Cisco Desk Phone 9811, 9841NR, 9851NR, 9861NR, and
          9871NR don't support NFC onboarding.

- During registration, the phone checks the DHCP options in the default sequence of 66, 160, 159, and 150 to obtain the URL of the provisioning server. The first valid configuration response it receives (which includes a 401 authorization request), will determine its provisioning server. Ensure that your server is properly configured to process phone registrations successfully.

By default, 802.1X authentication is disabled on your phone.

If your network uses the 802.1X protocol, ensure that you enable 802.1X authentication on your phone by accessing Settings > Network and service > Security settings . Otherwise, your phone will fail to connect to the network.

- If your phone has HTTP connection issues during the registration, you might be prompted to set up an HTTP proxy server on the phone. The HTTP proxy setting is only required for the phones registered to Webex Calling or BroadWorks. For more information about how to set up the HTTP proxy, see HTTP proxy settings .

Your phone gets registered automatically when it boots up and connects to the network. In this scenario of auto registration, you don't need to enter any input as the whole registration proceeds automatically.

Before you begin

- You have turned on your phone.

- Your administrator has configured your phone on the call control system.

Select Start on the Welcome screen.

If you don't take any action, the phone goes to the next step at timeout.

Your phone tries to connect to the network. If you use the wireless network, perform the next step. Otherwise, skip it.

(Optional) Choose your wireless network from the list, enter your credentials, and select Apply .

Cisco Desk Phone 9811, 9841NR, 9851NR, 9861NR, and
          9871NR don't support Wi-Fi.

Select Next when the screen displays that your phone successfully connects to Ethernet or WiFi.

If you don't take any action, the phone goes to the next step at timeout. Then the phone starts checking the configuration, and then starts the registration automatically.

If you are prompted to choose a call service, do one of the following actions:

- If your phone will be registered on the Cisco Unified Communications Manager (Unified CM), select Cisco UCM > Register .

- If your phone will be registered on the Webex Calling, select Cisco cloud service > Register .

Contact your administrator if you don't know which service to select.

Typically, the registration takes about 3 minutes depending on the network condition.

After the registration succeeds, your primary line name or number displays on the top left of the phone screen.

When the registration is complete, you will be prompted to enable or disable the noise removal feature.

If you don't take any action, the phone enables the feature at timeout.

This feature can filter out background noises during a call. If you choose to disable the feature now, you can still enable it later.

After your phone boots up, it checks the configuration automatically, and you will be
        prompted to enter an activation code. Activation codes are used to set up your new phone.
        You can get an activation code from you administrator.

You might be prompted to choose a call service during the registration, depending on your
          network condition and your administrator's configurations on the call control system.

Before you begin

You have turned on your phone.

Your phone connects to a wired or wireless network.

Get an activation code.

Select Start on the Welcome screen.

If you don't take any action, the phone goes to the next step at timeout.

Your phone tries to connect to the network. If you use the wireless network, perform
            the next step. Otherwise, skip it.

(Optional) Choose your wireless network from the list, enter your credentials, and select Apply .

Cisco Desk Phone 9811, 9841NR, 9851NR, 9861NR, and
          9871NR don't support Wi-Fi.

Select Next on the phone screen showing that your phone
          successfully connects to the network.

If you don't take any action, the phone goes to the next step at timeout. Then the
            phone starts checking the configuration, and then starts the registration
            automatically.

If you are prompted to choose a call service, do one of the following actions
          according to your network environment and the platform where the phone will be
          registered:

- If your phone connects to the corporate network and will be registered to the Cisco
              Unified Communications Manager (Unified CM), select Cisco UCM > Register .

- If your phone connects to the corporate network and will be registered to the Webex
              Calling, select Cisco cloud service > Register .

- If your phone uses Mobile and Remote Access (MRA) to connect to the corporate
              network when it's away from the office, select Cisco cloud service > Register .

Contact your administrator if you don't know which service to select.

When prompted for an activation code, enter your activation code, and select Activate .

Your phone starts the registration immediately. Typically, it takes about 3 minutes
            depending on the network condition.

After the registration succeeds, your primary line name or number displays on the top
            left of the phone screen.

When the registration is complete, you will be prompted to enable or disable the noise
          removal feature.

If you don't take any action, the phone enables the feature at timeout.

This feature can filter out background noises during a call. If you choose to disable
          the feature now, you can still enable it later.

After your phone boots up, it checks the configuration automatically. If you're prompted to enter an activation code, but you want to use the domain credentials for this registration, select Domain . If you don't have a valid service domain and user credentials, contact your administrator.

- You might be prompted to choose a call service during the registration, depending on your network condition and your administrator's configurations on the call control system.

- This registration method is only available for the phones registered to Cisco Unified CM.

Before you begin

- You have turned on your phone.

- Your phone connects to a wired or wireless network.

- Get a service domain, user ID, and password from your administrator.

Select Start on the Welcome screen.

If you don't take any action, the phone goes to the next step at timeout.

Your phone tries to connect to the network. If you use the wireless network, perform the next step. Otherwise, skip it.

(Optional) Choose your wireless network from the list, enter your credentials, and select Apply .

Cisco Desk Phone 9811, 9841NR, 9851NR, 9861NR, and
          9871NR don't support Wi-Fi.

Select Next on the phone screen showing that your phone successfully connects to the network.

When prompted to choose a call service, select Cisco cloud service > Register .

When prompted for an activation code, select Domain to switch to the domain activation screen.

Enter a valid service domain, and select Continue .

Enter your user ID and password, and press Sign in (on
            9811/9841/9851/9861) or tap Apply (on 9871/8875).

Your phone starts the registration immediately. Typically, it takes about 3 minutes
            depending on the network condition.

After the registration succeeds, your primary line name or number displays on the top
            left of the phone screen.

When the registration is complete, you will be prompted to enable or disable the noise removal feature.

If you don't take any action, the phone enables the feature at timeout.

This feature can filter out background noises during a call. If you choose to disable the feature now, you can still enable it later.

In some situation, the Cisco DHCP server doesn't contain the network information of the TFTP servers. To accomplish the registration, you need to manually enter an alternate TFTP server address that your administrator provides.

Before you begin

You have turned on your phone.

Your phone connects to a wired or wireless network.

Get a TFTP server address from your administrator.

Get a 16-digit activation code from your administrator, if needed.

Select Start on the Welcome screen.

If you don't take any action, the phone goes to the next step at timeout.

Your phone tries to connect to the network. If you use the wireless network, perform the next step. Otherwise, skip it.

(Optional) Choose your wireless network from the list, enter your credentials, and select Apply .

Cisco Desk Phone 9811, 9841NR, 9851NR, 9861NR, and
          9871NR don't support Wi-Fi.

Select Network .

The screen shows the message depending on how your phone connects to the network.

Select Network settings on the Network connection screen.

Toggle on Alternate TFTP in the IPv4 section.

Enter an IP address in TFTP Server <n> , where <n> represents the type of the TFTP server.

TFTP Server 1 is the primary server, TFTP Server 2 is the secondary server.

Select Apply .

The registration starts automatically. If your phone requires an activation code to continue, do the following:

Get an activation code from your administrator if you don't receive it yet.

Enter your activation code, and select Activate .

Typically, the registration takes about 3 minutes depending on the network condition.

After the registration succeeds, your primary line name or number displays on the top left of the phone screen.

When the registration is complete, you will be prompted to enable or disable the noise removal feature.

If you don't take any action, the phone enables the feature at timeout.

This feature can filter out background noises during a call. If you choose to disable the feature now, you can still enable it later.

If your phone model contains an NFC chip, you can scan the NFC tag on the phone with an NFC device to provision the onboarding information in advance.

Cisco Desk Phone 9841, 9851, 9861, and 9871 support NFC onboarding. Cisco Desk Phone 9811, 9841NR, 9851NR, 9861NR, and
          9871NR don't support the feature.

When the phone boots up and connects to a network, it will start the initial registration (Out-Of-Box) automatically.

This topic provides a general procedure about onboarding a phone by using NFC. The actual onboarding procedures might vary depending on the NFC onboarding method that is preconfigured in the NFC data and the call control system where the phone will be registered.

For more information about the NFC onboarding methods and how to prepare the NFC data, see Prepare NFC onboarding data for Desk Phone 9800 Series .

Scan the phone's NFC tag.

If the phone is offline, turn on the phone and connect it to a network.

The onboarding process starts automatically.

During the onboarding process, if certain procedure fails you will be prompted to enter an activation code or choose a call service, or both.

If prompted, enter an activation code.

If prompted, choose the call service "Cisco UCM" or "Cisco cloud service".

For "Cisco cloud service", you must enter an activation code or a service domain.

If you select service domain, you must enter valid user credentials.

Wait for the registration to complete.

| 1 | Select Start on the Welcome screen. If you don't take any action, the phone goes to the next step at timeout. Your phone tries to connect to the network. If you use the wireless network, perform the next step. Otherwise, skip it. |
|---|---|
| 2 | (Optional) Choose your wireless network from the list, enter your credentials, and select Apply . Cisco Desk Phone 9811, 9841NR, 9851NR, 9861NR, and
          9871NR don't support Wi-Fi. |
| 3 | Select Next when the screen displays that your phone successfully connects to Ethernet or WiFi. If you don't take any action, the phone goes to the next step at timeout. Then the phone starts checking the configuration, and then starts the registration automatically. If you are prompted to choose a call service, do one of the following actions: If your phone will be registered on the Cisco Unified Communications Manager (Unified CM), select Cisco UCM > Register . If your phone will be registered on the Webex Calling, select Cisco cloud service > Register . Contact your administrator if you don't know which service to select. Typically, the registration takes about 3 minutes depending on the network condition. After the registration succeeds, your primary line name or number displays on the top left of the phone screen. |
| 4 | When the registration is complete, you will be prompted to enable or disable the noise removal feature. If you don't take any action, the phone enables the feature at timeout. This feature can filter out background noises during a call. If you choose to disable the feature now, you can still enable it later. |

| 1 | Select Start on the Welcome screen. If you don't take any action, the phone goes to the next step at timeout. Your phone tries to connect to the network. If you use the wireless network, perform
            the next step. Otherwise, skip it. |
|---|---|
| 2 | (Optional) Choose your wireless network from the list, enter your credentials, and select Apply . Cisco Desk Phone 9811, 9841NR, 9851NR, 9861NR, and
          9871NR don't support Wi-Fi. |
| 3 | Select Next on the phone screen showing that your phone
          successfully connects to the network. If you don't take any action, the phone goes to the next step at timeout. Then the
            phone starts checking the configuration, and then starts the registration
            automatically. If you are prompted to choose a call service, do one of the following actions
          according to your network environment and the platform where the phone will be
          registered: If your phone connects to the corporate network and will be registered to the Cisco
              Unified Communications Manager (Unified CM), select Cisco UCM > Register . If your phone connects to the corporate network and will be registered to the Webex
              Calling, select Cisco cloud service > Register . If your phone uses Mobile and Remote Access (MRA) to connect to the corporate
              network when it's away from the office, select Cisco cloud service > Register . Contact your administrator if you don't know which service to select. |
| 4 | When prompted for an activation code, enter your activation code, and select Activate . Your phone starts the registration immediately. Typically, it takes about 3 minutes
            depending on the network condition. After the registration succeeds, your primary line name or number displays on the top
            left of the phone screen. |
| 5 | When the registration is complete, you will be prompted to enable or disable the noise
          removal feature. If you don't take any action, the phone enables the feature at timeout. This feature can filter out background noises during a call. If you choose to disable
          the feature now, you can still enable it later. |

| 1 | Select Start on the Welcome screen. If you don't take any action, the phone goes to the next step at timeout. Your phone tries to connect to the network. If you use the wireless network, perform the next step. Otherwise, skip it. |
|---|---|
| 2 | (Optional) Choose your wireless network from the list, enter your credentials, and select Apply . Cisco Desk Phone 9811, 9841NR, 9851NR, 9861NR, and
          9871NR don't support Wi-Fi. |
| 3 | Select Next on the phone screen showing that your phone successfully connects to the network. |
| 4 | When prompted to choose a call service, select Cisco cloud service > Register . |
| 5 | When prompted for an activation code, select Domain to switch to the domain activation screen. |
| 6 | Enter a valid service domain, and select Continue . |
| 7 | Enter your user ID and password, and press Sign in (on
            9811/9841/9851/9861) or tap Apply (on 9871/8875). Your phone starts the registration immediately. Typically, it takes about 3 minutes
            depending on the network condition. After the registration succeeds, your primary line name or number displays on the top
            left of the phone screen. |
| 8 | When the registration is complete, you will be prompted to enable or disable the noise removal feature. If you don't take any action, the phone enables the feature at timeout. This feature can filter out background noises during a call. If you choose to disable the feature now, you can still enable it later. |

| 1 | Select Start on the Welcome screen. If you don't take any action, the phone goes to the next step at timeout. Your phone tries to connect to the network. If you use the wireless network, perform the next step. Otherwise, skip it. |
|---|---|
| 2 | (Optional) Choose your wireless network from the list, enter your credentials, and select Apply . Cisco Desk Phone 9811, 9841NR, 9851NR, 9861NR, and
          9871NR don't support Wi-Fi. |
| 3 | Select Network . The screen shows the message depending on how your phone connects to the network. |
| 4 | Select Network settings on the Network connection screen. |
| 5 | Toggle on Alternate TFTP in the IPv4 section. |
| 6 | Enter an IP address in TFTP Server <n> , where <n> represents the type of the TFTP server. TFTP Server 1 is the primary server, TFTP Server 2 is the secondary server. |
| 7 | Select Apply . The registration starts automatically. If your phone requires an activation code to continue, do the following: Get an activation code from your administrator if you don't receive it yet. Enter your activation code, and select Activate . Typically, the registration takes about 3 minutes depending on the network condition. After the registration succeeds, your primary line name or number displays on the top left of the phone screen. |
| 8 | When the registration is complete, you will be prompted to enable or disable the noise removal feature. If you don't take any action, the phone enables the feature at timeout. This feature can filter out background noises during a call. If you choose to disable the feature now, you can still enable it later. |

| 1 | Scan the phone's NFC tag. |
|---|---|
| 2 | If the phone is offline, turn on the phone and connect it to a network. The onboarding process starts automatically. During the onboarding process, if certain procedure fails you will be prompted to enter an activation code or choose a call service, or both. |
| 3 | If prompted, enter an activation code. |
| 4 | If prompted, choose the call service "Cisco UCM" or "Cisco cloud service". For "Cisco cloud service", you must enter an activation code or a service domain. If you select service domain, you must enter valid user credentials. |
| 5 | Wait for the registration to complete. |

## Figuras

![the Settings key](https://cisco-api.ingeniuxondemand.com/DITA/content/en/us/td/i/400001-500000/470001-480000/478001-479000/478218.png)