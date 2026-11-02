---
doc_id: help-webex-com-en-us-article-f6tp57-9877ed7956
source_url: https://help.webex.com/en-us/article/f6tp57
retrieved_at: 2026-11-02T13:00:44.542192+00:00
---

You can use Amazon Web Services (AWS) Direct Connect to connect your on-premises network to
      the AWS hosted Webex Contact Center, bypassing the use of multiple Internet Service Provider
      (ISP) hops. When using AWS Direct Connect, a private network connection transfers data between
      your on-premises network and AWS. Thus, you get consistent network experience and guaranteed
      bandwidth to AWS and to the Webex Contact Center endpoints hosted in AWS.

AWS Direct Connect is available at locations worldwide. Depending on the location of your
      on-premises network, select the nearest AWS Direct Connect location to minimize cost,
      management overhead, and latency.

Prerequisites

To use AWS Direct Connect, you need:

- An AWS account.

- Specific network requirements. See AWS Direct Connect User Guide for details.

How AWS Direct Connect works

AWS Direct Connect connects your on-premises network and the Webex Contact Center solution
      over a standard Ethernet fiber-optic cable. Connect one end of the cable to your router and
      the other end to an AWS Direct Connect router. With this connection, you can create virtual
      interfaces (VIF) directly to public AWS services without using the internet.

Webex Contact Center supports public VIFs only and is not compatible with private VIFs.
          Public VIFs end the connection in the AWS network. From there, traffic to the Webex
          Contact Center endpoints is routed through the AWS network.

For more information about AWS Direct Connect, see AWS Direct Connect User Guide .

Pricing

AWS Direct Connect is a cloud network service available from Amazon. For information related
      to pricing, see AWS Direct Connect Pricing .