---
doc_id: developer-cisco-com-docs-finesse-javascript-library-9eb841f386
source_url: https://developer.cisco.com/docs/finesse/javascript-library/
retrieved_at: 2026-08-25T21:02:09.378155+00:00
---

# JavaScript Library

## Without Finesse JavaScript library

In the absence of the Finesse JavaScript library, the following code would be needed to pull the User details after the login process is completed.

Make a GET call to the server to get the details of this agent.

Example—GET

Code Snippet

```
$.ajax({
    url: 'finesse/api/User/1001001' // where 1001001 is the username or id of the logged in agent.
    type: 'GET',
    success: function(response){
        // here response is an xml containing all the relevant information regarding the User 1001001 which can be used
        // for example response can be < User > < id > 1001001 </ id > < state > NOT_READY </ state > </ User > // Need to parse the response and make it usable
    },
    error: function(err){
        // Something went wrong while fetching user data, show an error dialog to the user may be.
    },
});
```

Make a PUT call to the server to change the state of this agent.

Example—PUT

Code Snippet

```
$.ajax({
    url: 'finesse/api/User/1001001' // where 1001001 is the username/id through which the agent logged in.
    type: 'PUT',
    data: ' < User > < state > READY </ state > </ User > '
    success: function(response){
        // Do something once the user state has been changed successfully.
    },
    error: function(err){
        // Something went wrong while fetching user data, show an error dialog to the user may be.
    },
});
```

REST operations such as POST and DELETE can also be performed on the User API to get the desired result.

## With Finesse JavaScript library

In the presence of the Finesse JavaScript library, the following code would be needed to pull the User details, where the User object is under the namespace finesse.restservices.User .

Make a GET all on the User API. The GET call in the above example is made using the jQuery OpenAjax API, where the onLoad is equivalent to the success option of the jQuery OpenAjax call.

Example—onLoad, onChange, and on Error

Code Snippet

```
var _user = new finesse.restservices.User({
    id: '1001001',
    onLoad: function(user){
        // Do something on the successful fetch(GET) of user object
    },
    onChange: function(user){
        // Do something on the successful update(PUT) of object
        // can do user.getState() or user.getTeamName()
    }
    onError: function(err){
        // Something went wrong while fetching user data, show an error dialog to the user may be.
    }
});
```

The onChange is equivalent to the success option in PUT jQuery OpenAjax call made to modify the state of the User in the second example. Similarly, there are other handlers such as onAdd used for POST request and onDelete used for DELETE requests which are supported by User object as well as other Finesse JavaScript objects.

Update the state of the User using the setState() provided by finesse.restservices.User.

Code Snippet

```
_user.setState('READY');
```

The above example triggers a state change for the User, which is equivalent to make a PUT request, which in turn triggers the onChange handler attached to the User object.

All the handlers (GET, PUT, POST, DELETE, ERROR) can be attached to the object during initialization. Initialization of a JavaScript object triggers a GET request, the response of which is used to populate the JavaScript object. There are APIs available within the JavaScript object to create, update, and delete certain compositions (in the JavaScript object itself) that internally trigger PUT, POST, and DELETE REST API request respectively.

To put this into perspective, the Finesse JavaScript REST API objects try to encapsulate the low-level request or response handling at the client-side and provide with APIs which are easy to use, maintain and improve the readability of the code.