---
doc_id: developer-cisco-com-docs-finesse-client-integration-4d3439c5ed
source_url: https://developer.cisco.com/docs/finesse/client-integration/
retrieved_at: 2026-09-07T14:07:04.625606+00:00
---

# Client Integration

Clients can use the Finesse REST APIs in SSO mode. For thick client integrations, the
                following are browser like behaviors that thick clients must ensure to exhibit:

Follow server issued redirects.

Store and forward cookies.

Honor the various cookie attributes.

Run JavaScript in HTML responses.

Step 1

Use the API to get the system's authentication mode. The authentication mode can be found in the response as the value of the systemAuthMode.

If the system's authentication mode is SSO, then you can skip step 2.

Step 2

Use the Single Sign-On—Get User Authentication Mode to get a specific user's authentication mode.

You must use browser components that allow redirections and IdP form submissions. You cannot use Postman or AJAX for the Single Sign-On APIs.

Step 3

Use the Single Sign-On—Get User Authentication Mode with the return_user query parameter set to yes to get the user's access token.

The username must be provided in a cookie or a URL query parameter with a key of cc_username. The value is a URL encoded username, which can be the loginName or peripheralId for whom the token is requested.

Example:

Code Snippet

```
https://finesse1.xyz.com/desktop/sso/token?return_refresh_token=true
```

The result of the API request will redirect the request to the IdS page which then redirects to the IdP page.

Step 4

On the IdP page, enter the username and the password .

On successful authentication, the response body contains the access token and user_id value. The access token returns the token in the JWT format.

Example Response:

Code Snippet

```
{"token":"eyJjdHkiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ
pc3MiOiJpZHMuYXV0b2JvdC5jdnAiLCJzdWIiOiJ7XCJzY29wZVwiOltcImN
jY19vbnByZW1fYXBwc1wiXSxcInJ0XCI6XCJlMTRkNDIzY2E1MjNmZDkzNGRkN
zg0MDZjNTI2ZjZjMmI1MmIxZGMwXCIsXCJ1c2VyX2lkXCI6XCJzamVmZmVyc29
uXCIsXCJyZWFsbVwiOlwiZmluZXNzZS5jb21cIixcInVwblwiOlwic2plZmZlcnN
vbkBmaW5lc3NlLmNvbVwiLFwiaWRzX2lkXCI6XCJpZHMuYXV0b2JvdC5jdnBcIixcI
mNsaWVudF9pZFwiOlwiYmVkYmM1NWVlODY0Yjk5YzhmNTQwODg2YjIzYWUzN2M1MTg5
NDA3ZVwiLFwidG9rZW5cIjpcImQxYjIwMWMzN2JkYTY2OTQ5ZjM2YzU5OTMzNjgyZTE
4Mzg1NDAxZWVcIixcImV4cGlyeVwiOjE2NzE3MTM1NjE3NDcsXCJ1c2FnZVwiOlwiYWN
jZXNzXCIsXCJ2ZXJcIjpcIjEuMFwifSIsImV4cCI6MTY3MTcxMzU2MSwiaWF0IjoxN
jcxNzEzMjYxLCJqdGkiOiJkMWIyMDFjMzdiZGE2Njk0OWYzNmM1OTkzMzY4MmUxODM4
NTQwMWVlIn0.AbDCVEiLlzJ4t8m4dhtvapRzcYu_lz5zwKwasjlKxUcw2Mz3wYlgYcoF
g74v22xrX-BugWsEkIIDXnEctCbSrFBLfz4jYwMvhIyYu6KOIsW8qtm6fibFCkb_qRMr
AekMTUpeJxUJ8rnsZkXRh1vyzY2efJBHKSB5yBteOESryj1Nw1_kPV3evxhvLuOnaAp_
ewVDJniSM3AdLtW6yh_eAiuIMT4CeUju8ZPEdyUFOycT2B1JKUWbMchJqwZ8shpZPwHNH
0jTeGvvCp-gQqnCwffj_TxfD3UB1SL5y634eQ-zHTIO3IuUTA-uZVU6dioYRoM_zbE9NW
22FYNkZhFALg","refresh_token":"eyJjdHkiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.
eyJpc3MiOiJpZHMuYXV0b2JvdC5jdnAiLCJzdWIiOiJ7XCJpZHNfaWRcIjpcImlkcy5
hdXRvYm90LmN2cFwiLFwiY2xpZW50X2lkXCI6XCJiZWRiYzU1ZWU4NjRiOTljOGY1NDA
4ODZiMjNhZTM3YzUxODk0MDdlXCIsXCJ0b2tlblwiOlwiZTE0ZDQyM2NhNTIzZmQ5MzRk
ZDc4NDA2YzUyNmY2YzJiNTJiMWRjMFwiLFwiZXhwaXJ5XCI6MTY3MTcyMDQ2MTc0Nyxc
InVzYWdlXCI6XCJyZWZyZXNoXCIsXCJ2ZXJcIjpcIjEuMFwifSIsImV4cCI6MTY3MTcy
MDQ2MSwiaWF0IjoxNjcxNzEzMjYxLCJqdGkiOiJlMTRkNDIzY2E1MjNmZDkzNGRkNzg
0MDZjNTI2ZjZjMmI1MmIxZGMwIn0.XlFitxdlNE0KKyD9uUIF_KHQNv0AR-JO7V9Ncl9G24
yuK66U-BGYXrK1h67larnVPmpDeDRm-g5C5ApLXTx-MT0RuhQZPc6hU6TBpyKkvk0FhYyf2
LU48j0seI5XuvS3_i_vDQxPY_Q6TXeaANBYjcgsNAHKoXvIO0K3YaZOUsx1yeVkPIFeCl8H3
iJgXCD5gOF4OUK_g8lda7-92ARiqIAFtobwYqa-a-ramXyXncG81ihFNL7ngXC6V50hTC
zOduZYGvFxTGaLV753GAErrLNyKiKSm--txpoiBH5rf7w3JaJE9G98B64nHVhTm8nm4BysEV
gF3UNLhcNb0C0Vtw","expires_in":300,"user_id":"sjefferson","realm":
"finesse.com","user_principal":"sjefferson@finesse.com"}
```

The response also contains the token expiry time in seconds.

In a Unified CCX deployment, the username, loginName, and loginId can be
                            used interchangeably for the Finesse REST API calls.

Step 5

This step is for Unified CCE deployments only. In a Unified CCE deployment, the user_id obtained from the IdS token can be either the loginName or the peripheralId (loginId). The Finesse REST APIs can only accept the loginId. Use the User—Get User Id from loginName API to get the loginId from the user_id of the IdS token.

Example:

Code Snippet

```
https://finesse1.xyz.com/finesse/api/User/sjefferson
```

Example Response:

Code Snippet

```
< User > < dialogs > /finesse/api/User/1001002/Dialogs </ dialogs > < extension > </ extension > < firstName > AGENT </ firstName > < lastName > 98411 </ lastName > < loginId > 98411 </ loginId > < loginName > sjefferson </ loginName > < mediaType > 1 </ mediaType > < pendingState > </ pendingState > < reasonCodeId > -1 </ reasonCodeId > < roles > < role > Agent </ role > </ roles > < settings > < wrapUpOnIncoming > OPTIONAL </ wrapUpOnIncoming > </ settings > < state > LOGOUT </ state > < stateChangeTime > </ stateChangeTime > < teamId > 5000 </ teamId > < teamName > FunctionalAgents </ teamName > < uri > /finesse/api/User/sjefferson </ uri > < wrapUpTimer > 30 </ wrapUpTimer > </ User >
```

Step 6

Get the loginId from the loginId field.

All subsequent Finesse REST API requests must use the loginId from the
                        <User> response, instead of the username/user_id/loginName.

Example:

To login the agent sjefferson using the Finesse REST API,
                        you must use the loginId of 98411.

Code Snippet

Code Snippet - 1

```
https://finesse1.xyz.com/finesse/api/User/98411
```

```
< User > < state > LOGIN </ state > < extension > 98411 </ extension > </ User >
```

Step 7

To avoid the authentication and authorization flow again, the access token must be refreshed before the expiry time. Use the Single Sign-On—Refresh Existing Access Token with the return_user query parameter set to yes to refresh the user's access token.

The username must be provided in a cookie or a URL query parameter with a key of cc_username. The value is a URL encoded username, which can be the loginName or peripheralId for whom the token is requested.

Example Response:

Code Snippet

```
{"token":"eyJjdHkiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3M
iOiJpZHMuYXV0b2JvdC5jdnAiLCJzdWIiOiJ7XCJzY29wZVwiOltcImNjY19vbnB
yZW1fYXBwc1wiXSxcInJ0XCI6XCI4MmY1M2RhZGMwMWM2ODlkMGJiZjMyN2Q1MGI1
MmQyZjAzNmQzM2M3XCIsXCJ1c2VyX2lkXCI6XCJzamVmZmVyc29uXCIsXCJyZWFsb
VwiOlwiZmluZXNzZS5jb21cIixcInVwblwiOlwic2plZmZlcnNvbkBmaW5lc3NlL
mNvbVwiLFwiaWRzX2lkXCI6XCJpZHMuYXV0b2JvdC5jdnBcIixcImNsaWVudF9pZF
wiOlwiYmVkYmM1NWVlODY0Yjk5YzhmNTQwODg2YjIzYWUzN2M1MTg5NDA3ZVwiLF
widG9rZW5cIjpcIjk1OGQyODM1ODRmOGU2MDc5NjBlYzcyNjc4Nzk5NjE3YjA1Y
zMyOTNcIixcImV4cGlyeVwiOjE2NzE3MTM2MDEwNjQsXCJ1c2FnZVwiOlwiYWNjZXN
zXCIsXCJ2ZXJcIjpcIjEuMFwifSIsImV4cCI6MTY3MTcxMzYwMSwiaWF0IjoxNjcxN
zEzMzAxLCJqdGkiOiI5NThkMjgzNTg0ZjhlNjA3OTYwZWM3MjY3ODc5OTYxN2IwNWM
zMjkzIn0.aT0vf5GWKgfx1xUxZy4l4OS8yI4ACqmPZeOtNd6ZbToRqngOCsZJqMZ
tnmUBhXAOfBzeJjjYQOY2h74QQo88Bs4YZSc5WrWAnuUibI7cLhWYn8erb9fxB_
OD6FSIehWBzv3-S3mJiVJEnQ91FnhOv9JjocZDFxGVDGj3BwTU5o75DhIYtJd_G_RG
jFtRYIa6Jq8PThC-sfFBQD0P0AnViycLgKGQ7kpzEHvIUBsvyAzuCAfWzAQ_uK9ME
mjANCvni7aeFsEohVSKzG-pbECC4_rWCvZmLlm9qHL8KXzjF7ZybchmRZbl_sN3
fBxciLsYifbdwkhe5U1k8J_P9TdmtQ","expires_in":300,"user_id":"sjefferson",
"realm":"finesse.com","user_principal":"sjefferson@finesse.com"}
```

| Step 1 | Use the API to get the system's authentication mode. The authentication mode can be found in the response as the value of the systemAuthMode. Note If the system's authentication mode is SSO, then you can skip step 2. | Note | If the system's authentication mode is SSO, then you can skip step 2. |
|---|---|---|---|
| Note | If the system's authentication mode is SSO, then you can skip step 2. |
| Step 2 | Use the Single Sign-On—Get User Authentication Mode to get a specific user's authentication mode. Note You must use browser components that allow redirections and IdP form submissions. You cannot use Postman or AJAX for the Single Sign-On APIs. | Note | You must use browser components that allow redirections and IdP form submissions. You cannot use Postman or AJAX for the Single Sign-On APIs. |
| Note | You must use browser components that allow redirections and IdP form submissions. You cannot use Postman or AJAX for the Single Sign-On APIs. |
| Step 3 | Use the Single Sign-On—Get User Authentication Mode with the return_user query parameter set to yes to get the user's access token. The username must be provided in a cookie or a URL query parameter with a key of cc_username. The value is a URL encoded username, which can be the loginName or peripheralId for whom the token is requested. Example: Code Snippet https://finesse1.xyz.com/desktop/sso/token?return_refresh_token=true The result of the API request will redirect the request to the IdS page which then redirects to the IdP page. |
| Step 4 | On the IdP page, enter the username and the password . On successful authentication, the response body contains the access token and user_id value. The access token returns the token in the JWT format. Example Response: Code Snippet {"token":"eyJjdHkiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ
pc3MiOiJpZHMuYXV0b2JvdC5jdnAiLCJzdWIiOiJ7XCJzY29wZVwiOltcImN
jY19vbnByZW1fYXBwc1wiXSxcInJ0XCI6XCJlMTRkNDIzY2E1MjNmZDkzNGRkN
zg0MDZjNTI2ZjZjMmI1MmIxZGMwXCIsXCJ1c2VyX2lkXCI6XCJzamVmZmVyc29
uXCIsXCJyZWFsbVwiOlwiZmluZXNzZS5jb21cIixcInVwblwiOlwic2plZmZlcnN
vbkBmaW5lc3NlLmNvbVwiLFwiaWRzX2lkXCI6XCJpZHMuYXV0b2JvdC5jdnBcIixcI
mNsaWVudF9pZFwiOlwiYmVkYmM1NWVlODY0Yjk5YzhmNTQwODg2YjIzYWUzN2M1MTg5
NDA3ZVwiLFwidG9rZW5cIjpcImQxYjIwMWMzN2JkYTY2OTQ5ZjM2YzU5OTMzNjgyZTE
4Mzg1NDAxZWVcIixcImV4cGlyeVwiOjE2NzE3MTM1NjE3NDcsXCJ1c2FnZVwiOlwiYWN
jZXNzXCIsXCJ2ZXJcIjpcIjEuMFwifSIsImV4cCI6MTY3MTcxMzU2MSwiaWF0IjoxN
jcxNzEzMjYxLCJqdGkiOiJkMWIyMDFjMzdiZGE2Njk0OWYzNmM1OTkzMzY4MmUxODM4
NTQwMWVlIn0.AbDCVEiLlzJ4t8m4dhtvapRzcYu_lz5zwKwasjlKxUcw2Mz3wYlgYcoF
g74v22xrX-BugWsEkIIDXnEctCbSrFBLfz4jYwMvhIyYu6KOIsW8qtm6fibFCkb_qRMr
AekMTUpeJxUJ8rnsZkXRh1vyzY2efJBHKSB5yBteOESryj1Nw1_kPV3evxhvLuOnaAp_
ewVDJniSM3AdLtW6yh_eAiuIMT4CeUju8ZPEdyUFOycT2B1JKUWbMchJqwZ8shpZPwHNH
0jTeGvvCp-gQqnCwffj_TxfD3UB1SL5y634eQ-zHTIO3IuUTA-uZVU6dioYRoM_zbE9NW
22FYNkZhFALg","refresh_token":"eyJjdHkiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.
eyJpc3MiOiJpZHMuYXV0b2JvdC5jdnAiLCJzdWIiOiJ7XCJpZHNfaWRcIjpcImlkcy5
hdXRvYm90LmN2cFwiLFwiY2xpZW50X2lkXCI6XCJiZWRiYzU1ZWU4NjRiOTljOGY1NDA
4ODZiMjNhZTM3YzUxODk0MDdlXCIsXCJ0b2tlblwiOlwiZTE0ZDQyM2NhNTIzZmQ5MzRk
ZDc4NDA2YzUyNmY2YzJiNTJiMWRjMFwiLFwiZXhwaXJ5XCI6MTY3MTcyMDQ2MTc0Nyxc
InVzYWdlXCI6XCJyZWZyZXNoXCIsXCJ2ZXJcIjpcIjEuMFwifSIsImV4cCI6MTY3MTcy
MDQ2MSwiaWF0IjoxNjcxNzEzMjYxLCJqdGkiOiJlMTRkNDIzY2E1MjNmZDkzNGRkNzg
0MDZjNTI2ZjZjMmI1MmIxZGMwIn0.XlFitxdlNE0KKyD9uUIF_KHQNv0AR-JO7V9Ncl9G24
yuK66U-BGYXrK1h67larnVPmpDeDRm-g5C5ApLXTx-MT0RuhQZPc6hU6TBpyKkvk0FhYyf2
LU48j0seI5XuvS3_i_vDQxPY_Q6TXeaANBYjcgsNAHKoXvIO0K3YaZOUsx1yeVkPIFeCl8H3
iJgXCD5gOF4OUK_g8lda7-92ARiqIAFtobwYqa-a-ramXyXncG81ihFNL7ngXC6V50hTC
zOduZYGvFxTGaLV753GAErrLNyKiKSm--txpoiBH5rf7w3JaJE9G98B64nHVhTm8nm4BysEV
gF3UNLhcNb0C0Vtw","expires_in":300,"user_id":"sjefferson","realm":
"finesse.com","user_principal":"sjefferson@finesse.com"} The response also contains the token expiry time in seconds. Note In a Unified CCX deployment, the username, loginName, and loginId can be
                            used interchangeably for the Finesse REST API calls. | Note | In a Unified CCX deployment, the username, loginName, and loginId can be
                            used interchangeably for the Finesse REST API calls. |
| Note | In a Unified CCX deployment, the username, loginName, and loginId can be
                            used interchangeably for the Finesse REST API calls. |
| Step 5 | This step is for Unified CCE deployments only. In a Unified CCE deployment, the user_id obtained from the IdS token can be either the loginName or the peripheralId (loginId). The Finesse REST APIs can only accept the loginId. Use the User—Get User Id from loginName API to get the loginId from the user_id of the IdS token. Example: Code Snippet https://finesse1.xyz.com/finesse/api/User/sjefferson Example Response: Code Snippet < User > < dialogs > /finesse/api/User/1001002/Dialogs </ dialogs > < extension > </ extension > < firstName > AGENT </ firstName > < lastName > 98411 </ lastName > < loginId > 98411 </ loginId > < loginName > sjefferson </ loginName > < mediaType > 1 </ mediaType > < pendingState > </ pendingState > < reasonCodeId > -1 </ reasonCodeId > < roles > < role > Agent </ role > </ roles > < settings > < wrapUpOnIncoming > OPTIONAL </ wrapUpOnIncoming > </ settings > < state > LOGOUT </ state > < stateChangeTime > </ stateChangeTime > < teamId > 5000 </ teamId > < teamName > FunctionalAgents </ teamName > < uri > /finesse/api/User/sjefferson </ uri > < wrapUpTimer > 30 </ wrapUpTimer > </ User > |
| Step 6 | Get the loginId from the loginId field. All subsequent Finesse REST API requests must use the loginId from the
                        <User> response, instead of the username/user_id/loginName. Example: To login the agent sjefferson using the Finesse REST API,
                        you must use the loginId of 98411. Code Snippet Code Snippet - 1 https://finesse1.xyz.com/finesse/api/User/98411 < User > < state > LOGIN </ state > < extension > 98411 </ extension > </ User > |
| Step 7 | To avoid the authentication and authorization flow again, the access token must be refreshed before the expiry time. Use the Single Sign-On—Refresh Existing Access Token with the return_user query parameter set to yes to refresh the user's access token. The username must be provided in a cookie or a URL query parameter with a key of cc_username. The value is a URL encoded username, which can be the loginName or peripheralId for whom the token is requested. Example Response: Code Snippet {"token":"eyJjdHkiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3M
iOiJpZHMuYXV0b2JvdC5jdnAiLCJzdWIiOiJ7XCJzY29wZVwiOltcImNjY19vbnB
yZW1fYXBwc1wiXSxcInJ0XCI6XCI4MmY1M2RhZGMwMWM2ODlkMGJiZjMyN2Q1MGI1
MmQyZjAzNmQzM2M3XCIsXCJ1c2VyX2lkXCI6XCJzamVmZmVyc29uXCIsXCJyZWFsb
VwiOlwiZmluZXNzZS5jb21cIixcInVwblwiOlwic2plZmZlcnNvbkBmaW5lc3NlL
mNvbVwiLFwiaWRzX2lkXCI6XCJpZHMuYXV0b2JvdC5jdnBcIixcImNsaWVudF9pZF
wiOlwiYmVkYmM1NWVlODY0Yjk5YzhmNTQwODg2YjIzYWUzN2M1MTg5NDA3ZVwiLF
widG9rZW5cIjpcIjk1OGQyODM1ODRmOGU2MDc5NjBlYzcyNjc4Nzk5NjE3YjA1Y
zMyOTNcIixcImV4cGlyeVwiOjE2NzE3MTM2MDEwNjQsXCJ1c2FnZVwiOlwiYWNjZXN
zXCIsXCJ2ZXJcIjpcIjEuMFwifSIsImV4cCI6MTY3MTcxMzYwMSwiaWF0IjoxNjcxN
zEzMzAxLCJqdGkiOiI5NThkMjgzNTg0ZjhlNjA3OTYwZWM3MjY3ODc5OTYxN2IwNWM
zMjkzIn0.aT0vf5GWKgfx1xUxZy4l4OS8yI4ACqmPZeOtNd6ZbToRqngOCsZJqMZ
tnmUBhXAOfBzeJjjYQOY2h74QQo88Bs4YZSc5WrWAnuUibI7cLhWYn8erb9fxB_
OD6FSIehWBzv3-S3mJiVJEnQ91FnhOv9JjocZDFxGVDGj3BwTU5o75DhIYtJd_G_RG
jFtRYIa6Jq8PThC-sfFBQD0P0AnViycLgKGQ7kpzEHvIUBsvyAzuCAfWzAQ_uK9ME
mjANCvni7aeFsEohVSKzG-pbECC4_rWCvZmLlm9qHL8KXzjF7ZybchmRZbl_sN3
fBxciLsYifbdwkhe5U1k8J_P9TdmtQ","expires_in":300,"user_id":"sjefferson",
"realm":"finesse.com","user_principal":"sjefferson@finesse.com"} |

| Note | If the system's authentication mode is SSO, then you can skip step 2. |
|---|---|

| Note | You must use browser components that allow redirections and IdP form submissions. You cannot use Postman or AJAX for the Single Sign-On APIs. |
|---|---|

| Note | In a Unified CCX deployment, the username, loginName, and loginId can be
                            used interchangeably for the Finesse REST API calls. |
|---|---|