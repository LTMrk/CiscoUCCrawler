---
doc_id: webex-webexplaybooks-playbooks-wxcc-graphql-wallboard-docs-upstream-overview-md
source_url: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/wxcc-graphql-wallboard/docs/upstream-overview.md
repo: webex/WebexPlaybooks
ruta: playbooks/wxcc-graphql-wallboard/docs/upstream-overview.md
licencia: NOASSERTION
retrieved_at: 2026-08-24T09:10:29.600481+00:00
---

# WebexPlaybooks — playbooks/wxcc-graphql-wallboard/docs/upstream-overview.md

Repositorio: webex/WebexPlaybooks

# Upstream sample notes

Material from the [graphql-wallboard-sample](https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/reporting-samples/graphql-wallboard-sample) README, kept here so we do not add a second `README.md` under `src/`.

## Video

The upstream repository links to an overview and demo of the GraphQL wallboard sample. See the README in the tree above for the embedded video link.

## Live demo

A hosted instance may be available (free tier; cold starts can delay the first load). Check the upstream README for the current demo URL.

## GraphQL query time windows

This Playbook’s wallboard controllers use `wallboardQueryTimeRange()` in `src/controller/wxccApi.js`, which sets GraphQL `from` / `to` to a rolling window ending at `Date.now()`. Default lookback is **7 days**; set `WALLBOARD_LOOKBACK_DAYS` in `src/.env` and restart the server. Stay within the constraints documented for the [Search API](https://developer.webex.com/webex-contact-center/docs/api/v1/search).

## Related samples

The [graphql-sample](https://github.com/WebexSamples/webex-contact-center-api-samples/tree/main/graphql-sample) folder in the same monorepo includes `wallboard-query-samples` with additional query ideas.

---
> Fuente: https://github.com/webex/WebexPlaybooks/blob/main/playbooks/wxcc-graphql-wallboard/docs/upstream-overview.md (licencia NOASSERTION)
