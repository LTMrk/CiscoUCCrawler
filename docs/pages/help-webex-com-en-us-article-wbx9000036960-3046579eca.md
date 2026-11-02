---
doc_id: help-webex-com-en-us-article-wbx9000036960-3046579eca
source_url: https://help.webex.com/en-us/article/WBX9000036960
retrieved_at: 2026-11-02T12:59:03.171234+00:00
---

Contributed by Owen Mettam, Cisco TAC Engineer

ISSUE When verifying your domain in Control Hub, you receive the error ' Domain Verification Failed ' along with an ATLAS Tracking ID. RESOLUTION A successful domain verification relies on a correctly configured DNS TXT record. The dig or nslookup command will allow you to query your DNS name servers and verify that your TXT record value exists and matches the value shown in Control Hub. Review the tabs below for multiple ways to find and validate this information.

- Google Dig Tool

- Nslookup Command (Windows)

- Dig Command (Mac/Linux)

- Open the Google Admin Toolbox TXT Record Lookup tool .

- Enter your domain name (this is the same domain that you entered in Control Hub).

- The output will show automatically.

- Verify that the ' cisco-ci-domain-verification ' entry exists and matches the value shown in Control Hub.

- Open the Command Prompt or PowerShell.

- Enter the following command nslookup -type=txt domain.com . Replace 'domain.com' with the domain name you entered in Control Hub.

- Verify that the ' cisco-ci-domain-verification ' entry exists and matches the value shown in Control Hub.

- Open the terminal

- Enter the following command dig domain.com txt . Replace 'domain.com' with the domain name you entered in Control Hub.

- Verify that the ' cisco-ci-domain-verification ' entry exists and matches the value shown in Control Hub.

CAUSE Mismatching verification tokens or non-existent TXT records will cause domain verification to fail in the Control Hub.

## Figuras

Figura: DomainVerificationFailed.png

Figura: nslookup.png

Figura: dig.png