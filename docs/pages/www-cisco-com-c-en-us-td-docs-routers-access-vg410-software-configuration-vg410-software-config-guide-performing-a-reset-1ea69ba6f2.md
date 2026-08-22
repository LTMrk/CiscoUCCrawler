---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg410-software-configuration-vg410-software-config-guide-performing-a-reset-1ea69ba6f2
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg410/software-configuration/vg410-software-config-guide/performing-a-reset.html
retrieved_at: 2026-08-22T01:18:34.400171+00:00
---

Cisco VG410 Voice Gateway Software Configuration Guide

# Cisco VG410 Voice Gateway Software Configuration Guide

Updated: August 27, 2024

Chapter: Performing a Reset

## Chapter: Performing a Reset

- Performing a Reset

# Performing a Reset

You can reset the Cisco VG410 Voice Gateway by using the reset button that is present on the I/O side of the device.​ To reset the device, press the reset button for
                        more than 10 seconds. This action triggers a reload, removes the startup configuration, and recovers the process.​

During the Cisco VG410 Voice Gateway manufacturing process, the nvram:golden.cfg is duplicated from the startup configuration.

When you perform a front panel reset in the field, the next router reload utilizes the information in the nvram:gold.cfg file for the router's startup configuration. If a golden.cfg file is not present, an empty startup configuration is used during startup, and the day0 autoinstall/pnp/initial configuration
                        dialog appears.

When you press the reset button, it only affects the startup configuration. The contents in the bootflash: remains intact.

| Note | When you press the reset button, it only affects the startup configuration. The contents in the bootflash: remains intact. |
|---|---|