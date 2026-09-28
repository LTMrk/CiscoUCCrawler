---
doc_id: developer-cisco-com-site-user-data-services-learn-how-to-configure-http-sessions-625d334ed6
source_url: https://developer.cisco.com/site/user-data-services/learn/how-to/configure-http-sessions/
retrieved_at: 2026-09-01T17:35:06.881162+00:00
---

# How to Properly Configure HTTP Sessions

This example code demonstrates how to configure your HTTP library for proper session management. Samples for popular Java libraries and Python are provided.

## 1. Java

1.1. Apache CXF

Always pass the same object instance to ClientProxy.getClient(Object) so that you get the same client instance back.

# Code

```
Client client = ClientProxy. getClient (port);
  client.getRequestContext().put(org.apache.cxf.message.Message. MAINTAIN_SESSION , Boolean. TRUE );

  HTTPConduit http = (HTTPConduit) client.getConduit();
  http.getAuthorization().setUserName(johndoeUser);
  http.getAuthorization().setPassword(johndoePassword);
```

1.2 AXIS2

Use the same ServiceClient instance throughout your code. A singleton pattern is appropriate (but not necessary).

# Code

```
ServiceClient client = new ServiceClient();
  client.getOptions().setManageSession(true);
```

1.3 Apache HTTP Client (4.2.1)

Use the same DefaultHttpClient instance (or whatever http client instance you create) for all of the connections in each thread. A singleton pattern is appropriate, but not necessary.

# Code

```
TrustStrategy trustStrategy = new TrustSelfSignedStrategy();
  X509HostnameVerifier hostnameVerifier = new AllowAllHostnameVerifier();
  ClientConnectionManager connection = null;
  
  try {
  SSLSocketFactory sslSf = new SSLSocketFactory(trustStrategy, hostnameVerifier);
      PlainSocketFactory psf = new PlainSocketFactory();
  
      Scheme http = new Scheme("http", 8080, psf);
      Scheme https = new Scheme("https", 8443, sslSf);
  
      SchemeRegistry schemeRegistry = new SchemeRegistry();
      schemeRegistry.register(http);
      schemeRegistry.register(https);
      connection = new PoolingClientConnectionManager(schemeRegistry);
  
  } catch (Exception e) {
      System.out.println("Unable to set up multiple scheme support in HttpClient connection manager.");
  }
  
  DefaultHttpClient client = new DefaultHttpClient(connection);
  
  List<String> authPrefs = new ArrayList<String>();
  authPrefs.add(AuthPolicy.BASIC);
  
  client.getParams().setParameter(AuthPNames.PROXY_AUTH_PREF, authPrefs);
  client.getParams().setParameter(ClientPNames.COOKIE_POLICY, CookiePolicy.BROWSER_COMPATIBILITY);
```

## 2. Python

Use the same opener instance throughout your code.

# Code

```
import urllib2
  # Create an OpenerDirector with support for Basic HTTP Authentication...
  auth_handler = urllib2.HTTPBasicAuthHandler()
  auth_handler.add_password(realm='Cisco Web Services Realm',
          uri='https://10.89.x.x:8443/cucm-uds/user',
          user='johndoe',
          passwd='54321')
  opener = urllib2.build_opener(auth_handler)
  # ...and install it globally so it can be used with urlopen.
  urllib2.install_opener(opener)
  urllib2.urlopen('http://10.89.x.x/cucm-uds/user/johndoe')
```

New to UDS? Checkout these steps to get started.

Get Started

Visit the UDS Developer Forums to ask questions and interact with other developers.

Forums