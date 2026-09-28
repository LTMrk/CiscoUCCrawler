---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-searching-and-sorting-html-fce3d7b9db
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_searching-and-sorting.html
retrieved_at: 2026-08-17T03:47:27.659670+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Searching and Sorting

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Searching and Sorting

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- Searching and Sorting

Links to Other API pages: Cisco_Unity_Connection_APIs

## Searching

The general format of a search
                           		query is:

```
query=(column [is | startswith] value)
```

For example, to find all users that have an alias starting with the
                           		letter "a," the query would be:

```
query=(alias startswith a)
```

The full URL, including escaping spaces as %20, would be:

```
GET http://<connection-server>/vmrest/users?query=(alias%20startswith%20a)
```

(For more information about escaping spaces, see the (RFC for URIs.)

## Sorting

Sorting is similar to searching.
                           		The general format of a sort is:

```
sort=(column [asc | desc])
```

For example, to sort users by alias, the sort would be:

```
sort=(alias asc)
```

The full URL would be:

```
GET http://<connection-server>/vmrest/users?sort=(alias%20asc)
```

Note that spaces must be escaped in the URL as %20 (standard URL escape
                           		code for space).

## Constraints on the
                        	 Allowed Values in Search Queries and Sorts

Note the following constraints on the allowed values in the queries and
                           		sorts, based on database performance requirements:

- Sorts can support only a
                                 		  single column.

- Sorts can specify only a
                                 		  column that is indexed.

- Queries can support only an
                                 		  indexed column or a boolean column.

- Queries can specify more
                                 		  than one column only if all columns belong to a single compound index. (Note:
                                 		  the ability to specify more than one column is not yet implemented; at this
                                 		  time, only single criteria queries are allowed.)

- When both a query and a sort
                                 		  are specified, the sort column must be one of the columns in the query.

- Queries can use only two
                                 		  conditions: "is" and "startswith".