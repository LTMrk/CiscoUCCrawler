---
doc_id: developer-cisco-com-site-webdialer-learn-sample-apps-html-sample-app-65e4ba786e
source_url: https://developer.cisco.com/site/webdialer/learn/sample-apps/html-sample-app/
retrieved_at: 2026-09-01T17:49:52.911224+00:00
---

# HTML Sample App

The HTML interface of Cisco WebDialer allows you to incorporate simple click-to-dial (C2D)
                    functionality to your corporate directory web pages or in any other application using Cisco Unified
                    Communication Manager (Unified CM) phones. It is easy and straight-forward with most of the details
                    managed by the Cisco WebDialer service. Some configurations need to be modified on the server but
                    Cluster services are automatic and do not have to be programmed by the developer.

To get started with using Cisco WebDialer, let's look at an HTML request for a simple
                    example.

Example Scenario: How to click-to-dial an extension from a web page.

Follow the below steps to ensure your enviornment is configured for this sample app:

- Make sure the Cisco WebDialer Service is running on the Unified CM server

- Verify you have a provisioned phone/device

- Follow the steps to add a valid username and password

- Ensure Unified CM server is in the HTML code

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

< html >

< head >

< meta http-equiv = Content -Type content = "text/html;
                                                charset=windows-1252" >

< title >

WebDialer HTML Example

</ title >

<script>

function launchWebDialerWindow(
                                            url ) {

webdialer=window.open( url, "webdialer" , "status=no,
                                            width=420, height=300, scrollbars=no, resizable=yes, toolbar=no" );

}

function launchWebDialerServlet(
                                            destination ) {

url = ' https://cucm3.kpiint.com:8443/webdialer/Webdialer?destination= ' + escape(destination);

launchWebDialerWindow( url );

}

</script>

</ head >

< body lang = EN -US>

< div class = Section1 >

< p class = MsoNormal >

Sample WebDialer HTML Application

</ p >

</ p >

Make sure the Web Dialer Service is running on
                                            the Unified CM server , that you have a provisioned phone/device,

and that you have added a valid user name,
                                            password, and server in the HTML code.

</ p >

</ p >

</ p >

</ p >

Click the
                                            number below to call Bill Smith's phone.

</ p >

</ p >

</ p >

</ p >

Bill
                                            Smith Ext.

< TD >

< A href = "javascript:launchWebDialerServlet('1002')" >

1002

</ A >

</ TD >

</ div >

</ body >

</ html >

You can copy and paste the above code into a text file with the extension HTML.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 | < html > < head > < meta http-equiv = Content -Type content = "text/html;
                                                charset=windows-1252" > < title > WebDialer HTML Example </ title > <script> function launchWebDialerWindow(
                                            url ) { webdialer=window.open( url, "webdialer" , "status=no,
                                            width=420, height=300, scrollbars=no, resizable=yes, toolbar=no" ); } function launchWebDialerServlet(
                                            destination ) { url = ' https://cucm3.kpiint.com:8443/webdialer/Webdialer?destination= ' + escape(destination); launchWebDialerWindow( url ); } </script> </ head > < body lang = EN -US> < div class = Section1 > < p class = MsoNormal > Sample WebDialer HTML Application </ p > </ p > Make sure the Web Dialer Service is running on
                                            the Unified CM server , that you have a provisioned phone/device, and that you have added a valid user name,
                                            password, and server in the HTML code. </ p > </ p > </ p > </ p > Click the
                                            number below to call Bill Smith's phone. </ p > </ p > </ p > </ p > Bill
                                            Smith Ext. < TD > < A href = "javascript:launchWebDialerServlet('1002')" > 1002 </ A > </ TD > </ div > </ body > </ html > |
|---|---|