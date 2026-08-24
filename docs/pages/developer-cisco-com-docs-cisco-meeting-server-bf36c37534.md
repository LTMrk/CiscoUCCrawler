---
doc_id: developer-cisco-com-docs-cisco-meeting-server-bf36c37534
source_url: https://developer.cisco.com/docs/cisco-meeting-server/
retrieved_at: 2026-08-24T22:11:52.064181+00:00
---

# REST Primer Guide

##### Table of Contents

## Overview

This document covers the basics of a REST API, and provides a brief introduction to Cisco Meeting Server APIs concepts.

## Introduction to API

An Application Programming Interface (API) for a website is code that allows two software programs to communicate with each another. An API exposes functionality to another application.

### Web services

The popularity of web, paved the way for more interconnected services. Typically connectivity is preferred over an open network rather than as a direct connection. HTTP is the preferred protocol to send and receive messages, and to define a client-server behavior. Web Services provide programming interfaces between two systems to communicate via HTTP methods.

## Introduction to REST APIs

REST stands for "Representational State Transfer". REST is centered around the HTTP request and response model. A RESTful API uses HTTP requests to GET, PUT, POST and DELETE data.

### RESTful Design

By definition, a RESTful design is a set of principles. It states that an interface must have the following five design elements for a rich application in order to offer a wide range of functionality:

- A client-server model

- Stateless - this means that every HTTP request happens in complete isolation. When the client makes an HTTP request, it includes all information necessary for the server to fulfill that request. The server never relies on information from previous requests.

- Compatibility with caching

- Layered system

- Uniform interface

Items 2-4 are significant as they ensure a successful design function across potentially complex networks that are common today. For example, load balancing, proxies.

### Key features of REST API

A RESTful Web API should have the following features:

- Accessible via a base URI http://<anyserver.cisco.com>/api/v1

- Support known internet media types such as JSON, XML.

- Support standard HTTP methods: GET, PUT, POST, DELETE

### Basics of a REST request

A basic REST command will have the following elements regardless of the tool/client used:

- Address - Defines the location of the API object you want to work on.

- HTTP command - Specifies the type of action you want to perform

- Payload - Any headers and data to be sent

- Response - The response from the server.

#### REST API request

To construct a request, you need the following information for the API endpoint you are calling.

- Methods - GET, POST, PUT, DELETE

- URL and parameters - The URL for the endpoint you are calling with any parameters as applicable.

- Authentication - Types such as HTTP, basic or tokens

- Headers - If the API requires headers

- Request body - JSON or XML data

The Cisco Meeting API Reference Documentation lists all of the publicly available API methods and provides the details on how to make each request.

#### Response

The response from server may include the following items:

- HTTP Status code - used to return the status of the request such as  success or error. See List of Status codes here

- Content - The response received from the server for the request are typically in JSON or XML formats.

## Cisco Meeting Server API

Cisco Meeting Server provides a rich set of API to interact with the application. The Meeting Server APIs are designed as a hierarchy of objects, similar to a directory structure. Example: Each configured coSpace exists as a node in this tree, and all of the users who are members of the coSpace exist as nodes “beneath” the coSpace object’s node. If there are 100 coSpaces configured on the Meeting server, conceptually there would be 100 nodes directly beneath /coSpaces in the hierarchy.

Note: A space is a persistent virtual meeting room that a group of users can use at any time for calling and chatting. Within Cisco Meeting Server API a "coSpace" is the same as a "space".

The API uses HTTPS as a transport mechanism. To use the API, a connection has to be enabled using HTTPS through the same TCP ports as used by the Cisco Meeting Server Web Admin interface.

A visual representation of how we communicate with Cisco Meeting Server.

Use Cisco Meeting Server's API commands via a HTTP client of your choice (Example: POSTMAN, POSTER).  The commands are sent to the server, which for Meeting Server is the Web Admin Service. There, the REST API interface works internally with the Cisco Meeting Server to process the requests, and return the response back through the Web server as a XML response to the HTTP client.

## Cisco Meeting Server APIs key features:

Key items of an API request are:

### Objects

An object refers to information returned by an API, For example, in Meeting Server, object is a space, a user, or a call. An objects consists of Attributes .

Every object has a unique GUID style ID.

Example: <coSpace id=`3eef25b-2bc6-48ca-8378-dc9823c602>

An object is referenced with the path to it. Typically, an API will have a number of endpoints grouped under the same Object. In this case, you describe both the object and the individual endpoints.

### Attributes

Attributes cannot be added or removed.

Example: The name or alias to a space.

#### Example of Objects and Attributes

### Parameters

Parameters are options you can pass during an API request (such as specifying the response format or the amount returned) to influence the response.

### Web address

An object is referenced with a path to locate it.

### API organization

The API itself is designed as a hierarchy of objects, like a trees with roots.  The objects are organized into collections.  You can query a collection to see all its objects. The hierarchy goes down multiple levels. Typically an object can be a sub-set of other objects.

Example: A GET to /coSpaces would list the two objects space1 and space2 .

Note : See the Cisco Meeting Server API reference for more information on APIs.

### Configuration

The Cisco Meeting Server API is not open. To use the Cisco Meeting Server API you need to follow these steps:

- Connect via HTTPS via the same TCP ports as you would use to access the Web Admin Interface - which is typically 443.

- Enter your credentials to login to MMP.

- Configure a new 'api' user with a username and password, Set them using the MMP command user: add <username> (api).

This command creates a new api user and prompts for a password for the user which must be entered twice to ensure that the intended password is configured.

Note that MMP users with either the 'admin' or 'api' role can access the API. See the MMP Command Reference Guide for details.

On first login, the user will be asked to configure a new password. You must provide these credentials in order to use the API.

To use the API, the API user supplies the configured username and password to the Meeting Server.

### Authorization

The Authorization is a simple HTTP Basic Authentication at the connection level. Credentials are protected by the HTTPS connection.

### API methods

REST API design allows standard HTTP commands to perform actions:

#### GET

Use GET methods to retrieve information. This performs the ‘read’ action. You can retrieve an object at individual level or collection level.

Example 1: Retrieve information for an individual space. To retrieve a particular coSpaces's detail specify the unique ID of the coSpaces.

GET https://cms.dcloud.cisco.com:445/api/v1/coSpaces/ID

Example 2: Retrieve information for all spaces

If you do not know the ID of a space, you can list all the 'cospace' objects by doing a GET on a collection level as follows:

GET https://cms.dcloud.cisco.com:445/api/v1/coSpaces

#### POST

Use POST methods to create new objects; for example, to create a new space or dial plan rule. To create, use a POST to the parent location of an object.

POST https://cms.anyserver.cisco.com:445/api/v1/coSpaces/

You can also enter the parameters for the new object at the same time.

Note: The new object will have an ID assigned automatically and will appear in the LOCATION header in the response.

#### PUT

Use PUT methods to modify existing objects; for example, changing the name of an existing space, muting a specific call leg or changing the layout. To modify, send a PUT request to the object's location with the parameters in the request.

PUT https://cms.anyserver.cisco.com:445/api/v1/coSpaces/ID

#### DELETE

Use DELETE to delete an object in the tree.

Note: You can delete objects, not attributes.

Example: To delete a particular space, specify the unique ID:

DELETE https://cms.dcloud.cisco.com:445/api/v1/coSpaces/ID

## Summary of Cisco Meeting Server API requests

A Cisco Meeting Server's API request should have the following items:

- Address : https://anyserver:port/api/v1/<object path>

- Methods : GET, PUT, POST, DELETE

- Payload : Name and Value pairs

- Response : Based on the request specified, the API returns objects formatted as XML. (Example: 200 OK or 400 Bad request)

## HTTP Clients

There are tools that helps to interact directly with a REST API. You can choose an HTTP client of your choice based on the platform you are using. Listed below are a few examples:

### POSTMAN

POSTMAN is an extension of Google Chrome, available on macOS and Microsoft Windows.

The above example shows a GET request to retrieve available spaces on the Server.

### PowerShell

Windows PowerShell is available in every Windows installation. This is very useful in an instance where you cannot install a client.

### Other tool suggestions

- CURL - Command Line tool for Windows and macOS.

- PAW for macOS.

Next