---
doc_id: developer-cisco-com-site-hcs-learn-fulfillment-ws-sample-b31bb35c1a
source_url: https://developer.cisco.com/site/hcs/learn/fulfillment-ws-sample/
retrieved_at: 2026-09-08T03:51:27.962169+00:00
---

Download the Code

# How to ... Create an HCS Fulfillment APIs Client Application

This sample application demonstrates how to create an HCS Fulfillment web service consumer client using the Apache CFX framework. The CFX framework can be used generate stub classes from the Cisco HCM-F WSDLs.

You can then use these generated classes to connect to the Cisco HCM-F interfaces. You can download the code for this example. The following article walks through how to generate the consumer classes and how to create a web client that performs the following tasks:

- Configure default credentials

- Configure a Unified Communications Domain Manager

- Configure a Unified Operations Manager

- Configure a UCSManager

- Configure a vCenter

- Synchronize all service providers

# Before You begin

To complete this exercise, you will need access to the following tools.

- Access to an HCS deployment

- HCS Admin username and password

- The Apache CFX framework ( http://cxf.apache.org )

# Download and Install the CXF Framework

- Go to http://cxf.apache.org and download and install CFX.

- After, you have downloaded CFX, you may need to set up your environment to use CFX. You can do so by entering the following on the command line. Use the version of CFX that corresponds to the version you downloaded.

?

1

2

3

4

5

6

7

< strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" >

< table class = "tablesorter" cellpadding = "0" cellspacing = "0" >

< tbody >

< tr >

< td style = "border-right-color:#6ce26c;
                                                        border-right-width:thick; border-left-style:none;
                                                        border-bottom-style:none; border-top-style:none
                                                        " >< span style = "color:#999;" >1</ span >

</ td >

< td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none; " >  $   < span style = "color:#f952ac;" >export</ span >  CXF_HOME=/Your_CXF_Download_Location/apache-cxf-2.X.X/</ td ></ tr ></ tbody ></ table ></ strong >

# Generating the consumer classes

In this example, we will use the CFX framework to generate classes from the HCS Fulfillment API WSDLs. We will then use these generated classes to call the APIs.

## Get the WSDL's

For this application, we need get the following wsdl's from the HCS deployment.

Shared Data Repository WSDL

https://your-hcs-box.example.com:8443/HCSWebServiceInterface/SharedDataRepositoryWebService?wsdl

Fulfillment WSDL

https://your-hcs-box.example.com:8443/HCSWebServiceInterface/Fulfillment WebService?wsdl

HCS License Manager WSDL

https://your-hcs-box.example.com:8443/HCSWebServiceInterface/HCSLicenseManagerWebService?wsdl

Service Inventory WSDL

https://your-hcs-box.example.com:8443/HCSWebServiceInterface/ServiceInventoryWebService?wsdl

- Create a directory for your project.

- Create a directory inside of your project directory for the wsdl files.

- Save all of the wsdl files in the wsdl directory.

?

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

< strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" >

< table class = "tablesorter" cellpadding = "0" cellspacing = "0" >

< tbody >

< tr >

< td style = "width:
                                                        10px; border-right-color:#6ce26c; border-right-width:thick;
                                                        border-left-style: none; border-bottom-style:none;
                                                        border-top-style:none " >< span style = "color:#999;" >1</ span >

< span style = "color:#999;" >2</ span >

< span style = "color:#999;" >3</ span >

< span style = "color:#999;" >4</ span >

< span style = "color:#999;" >5</ span >

< span style = "color:#999;" >6</ span >

</ td >

< td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $
                                                        < span style = "color:#f952ac;" >pwd</ span >

/home/alice

$
                                                    < span style = "color:#f952ac;" >mkdir</ span >
                                                    myProject

$
                                                    < span style = "color:#f952ac;" >cd</ span > myProject

$
                                                    < span style = "color:#f952ac;" >mkdir</ span >
                                                    wsdl

$
                                                    < span style = "color:#f952ac;" >cd</ span > wsdl</ td ></ tr ></ tbody ></ table ></ strong >

## Generate the Classes

We will also create a directory for the compiled business logic class files.

?

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

< strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" >

< table class = "tablesorter" cellpadding = "0" cellspacing = "0" >

< tbody >

< tr >

< td style = "width:
                                                        10px; border-right-color:#6ce26c; border-right-width:thick;
                                                        border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none " >< span style = "color:#999;" >1</ span >

< span style = "color:#999;" >2</ span >

< span style = "color:#999;" >3</ span >

< span style = "color:#999;" >4</ span >

< span style = "color:#999;" >5</ span >

</ td >

< td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $< span style = "color:#f952ac;" > pwd</ span >

/home/alice/myProject

$< span style = "color:#f952ac;" > mkdir</ span >
                                                    autogen

$< span style = "color:#f952ac;" > mkdir</ span >
                                                    autogen/src

$< span style = "color:#f952ac;" > mkdir</ span >
                                                    autogen/build</ td ></ tr ></ tbody ></ table ></ strong >

We will also create a directory for the compiled business logic class files.

?

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

< strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" >

< table class = "tablesorter" cellpadding = "0" cellspacing = "0" >

< tbody >

< tr >

< td style = "width:
                                                        10px; border-right-color:#6ce26c; border-right-width:thick;
                                                        border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none " >< span style = "color:#999;" >1</ span >

< span style = "color:#999;" >2</ span >

< span style = "color:#999;" >3</ span >

</ td >

< td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $< span style = "color:#f952ac;" > pwd</ span >

/home/alice/myProject

$< span style = "color:#f952ac;" > mkdir</ span >
                                                    build</ td ></ tr ></ tbody ></ table ></ strong >

Next, we will use wsdl2java to generate the classes.

You may hit a java.lang.OutOfMemoryError while generating the code. To fix this you will need to increase the maximum heap size of wsdl2java. To increase the heap size do the following:

- open /Your_CXF_Download_Location/apache-cxf-2.X.X/bin/wsdl2java in an text editor.

- Change $JAVA_HOME/bin/java -Xmx128M <SNIP>

- to $JAVA_HOME/bin/java -Xmx256M <SNIP>

- Close and save the wsdl2java file.

Run the following commands to generate the stub classes. These commands make take a few minutes to complete. After they have finished, you should see the generated classes in the autogen/src and autogen/build directories.

?

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

< strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" >

< table class = "tablesorter" cellpadding = "0" cellspacing = "0" >

< tbody >

< tr >

< td style = "border-right-color:#6ce26c;
                                                        border-right-width:thick; border-left-style:none;
                                                        border-bottom-style:none; border-top-style:none
                                                        " >< span style = "color:#999;" >1</ span >

< span style = "color:#999;" >2</ span >

< span style = "color:#999;" >3</ span >

< span style = "color:#999;" >4</ span >

< span style = "color:#999;" >5</ span >

< span style = "color:#999;" >6</ span >

</ td >

< td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $
                                                        < span style = "color:#f952ac;" >pwd</ span >

/home/alice/myProject

$
                                                    /Your_CXF_Download_Location/apache-cxf-2.X.X/bin/wsdl2java -classdir
                                                    autogen/build/ -d autogen/src/ -compile
                                                    ./wsdl/SharedDataRepositoryWebService.wsdl

$
                                                    /Your_CXF_Download_Location/apache-cxf-2.X.X/bin/wsdl2java -classdir
                                                    autogen/build/ -d autogen/src/ -compile
                                                    ./wsdl/FulfillmentWebService.wsdl

$
                                                    /Your_CXF_Download_Location/apache-cxf-2.X.X/bin/wsdl2java -classdir
                                                    autogen/build/ -d autogen/src/ -compile
                                                    ./wsdl/ServiceInventoryWebService.wsdl

$
                                                    /Your_CXF_Download_Location/apache-cxf-2.X.X/bin/wsdl2java -classdir
                                                    autogen/build/ -d autogen/src/ -compile
                                                    ./wsdl/HCSLicenseManagerWebService.wsdl</ td ></ tr ></ tbody ></ table ></ strong >

# Create the Web Client

Next, we will add the code that connects to the HCS Web Services and uses some of the APIs.

## Create a directory for the source files

First, we will create a directory to contain our business logic source.

?

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

< strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" >

< table class = "tablesorter" cellpadding = "0" cellspacing = "0" >

< tbody >

< tr >

< td style = "width:
                                                        10px; border-right-color:#6ce26c; border-right-width:thick;
                                                        border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none " >< span style = "color:#999;" >1</ span >

< span style = "color:#999;" >2</ span >

< span style = "color:#999;" >3</ span >

< span style = "color:#999;" >4</ span >

< span style = "color:#999;" >5</ span >

</ td >

< td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $
                                                        < span style = "color:#f952ac;" >pwd</ span >

/home/alice/myProject

$
                                                    < span style = "color:#f952ac;" >mkdir</ span >
                                                    src

$
                                                    < span style = "color:#f952ac;" >mkdir</ span >
                                                    src/com

$
                                                    < span style = "color:#f952ac;" >mkdir</ span >
                                                    src/com/example

</ td ></ tr ></ tbody ></ table ></ strong >

?

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

< strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" >

< table class = "tablesorter" cellpadding = "0" cellspacing = "0" >

< tbody >

< tr >

< td style = "width:
                                                        10px; border-right-color:#6ce26c; border-right-width:thick;
                                                        border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none " >< span style = "color:#999;" >1</ span >

< span style = "color:#999;" >2</ span >

< span style = "color:#999;" >3</ span >

</ td >

< td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $
                                                        < span style = "color:#f952ac;" >pwd</ span >

/home/alice/myProject

$
                                                    < span style = "color:#f952ac;" >mkdir</ span >
                                                    build

</ td ></ tr ></ tbody ></ table ></ strong >

## Create a Connector

To complete the web client, we are going to create three classes. You can download these sample classes .

- HCSConnector.java - a simple base connector client that helps you connect to the HCM-F SOAP Interface. Handles setting up the remote host, credentials, logging and certificate management. You should store this file as /home/alice/myProject/src/com/example/HCSConnector.java .

- HCSConnectorImpl.java - extends the HCSConnector base client and implements a version specific HCM-F Connector. Uses settings from the base class and the CXF autogenerated stubs to connect to the HCM-F SOAP interface. You should store this file as /home/alice/myProject/src/com/example/HCSConnectorImpl.java .

- WorkflowHCSWebClient.java - uses the version specific connector and automates a sample workflow. You should store this file as /home/alice/myProject/src/com/example/WorkflowHCSWebClient.java .

## Using the HCS APIs

The WorkflowHCSWebClient.java demonstrates how to implement the following workflow:

- Configure default credentials

- Configure a Unified Communications Domain Manager

- Configure a Unified Operations Manager

- Configure a UCSManager

- Configure a vCenter

- Synchronize all service providers

You can see the code that performs this workflow in the following segment.

?

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

44

45

46

47

48

49

50

51

52

53

54

55

56

57

58

59

60

61

62

63

64

65

66

67

68

69

70

71

72

73

74

75

76

< strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" >

< table class = "tablesorter" cellpadding = "0" cellspacing = "0" >

< tbody >

< tr >

< td style = "border-right-color:#6ce26c;
                                                        border-right-width:thick; border-left-style:none;
                                                        border-bottom-style:none; border-top-style:none
                                                        " >< span style = "color:#999;" >1</ span >

< span style = "color:#999;" >2</ span >

< span style = "color:#999;" >3</ span >

< span style = "color:#999;" >4</ span >

< span style = "color:#999;" >5</ span >

< span style = "color:#999;" >6</ span >

< span style = "color:#999;" >7</ span >

< span style = "color:#999;" >8</ span >

< span style = "color:#999;" >9</ span >

< span style = "color:#999;" >10</ span >

< span style = "color:#999;" >11</ span >

< span style = "color:#999;" >12</ span >

< span style = "color:#999;" >13</ span >

< span style = "color:#999;" >14</ span >

< span style = "color:#999;" >15</ span >

< span style = "color:#999;" >16</ span >

< span style = "color:#999;" >17</ span >

< span style = "color:#999;" >18</ span >

< span style = "color:#999;" >19</ span >

< span style = "color:#999;" >20</ span >

< span style = "color:#999;" >21</ span >

< span style = "color:#999;" >22</ span >

< span style = "color:#999;" >23</ span >

< span style = "color:#999;" >24</ span >

< span style = "color:#999;" >25</ span >

< span style = "color:#999;" >26</ span >

< span style = "color:#999;" >27</ span >

< span style = "color:#999;" >28</ span >

< span style = "color:#999;" >29</ span >

< span style = "color:#999;" >30</ span >

< span style = "color:#999;" >31</ span >

< span style = "color:#999;" >32</ span >

< span style = "color:#999;" >33</ span >

< span style = "color:#999;" >34</ span >

< span style = "color:#999;" >35</ span >

</ td >

< td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > < span style = "color:#009;" >public void</ span >
                                                        doSampleWorkFlow () < span style = "color:#009;" >throws</ span >
                                                        NBIException, com.cisco.hcs.nbi.ws.fulfillment.v9_0.NBIException
                                                        {

ServiceProvider
                                                    serviceProvider = getServiceProvider();

KID
                                                    serviceProviderKID = serviceProvider.getPk();

ManagementNetwork
                                                    managementNetwork = getManagementNetwork(serviceProviderKID);

< span style = "color:#38a963;" >//Step 1: Configure Default Credentials</ span >

configureDefaultCredentials(serviceProviderKID);

< span style = "color:#38a963;" >//Step 2: Configure a
                                                    CUCDM</ span >

configureCUCDM(managementNetwork);

< span style = "color:#38a963;" >//Step 3: Configure a
                                                    CUOM</ span >

configureCUOM(managementNetwork);

< span style = "color:#38a963;" >//Step 4: Configure a Data
                                                    Center</ span >

configureDataCenter(serviceProviderKID);

< span style = "color:#38a963;" >//Wait for user input before kicking of
                                                    manual sync</ span >

< span style = "color:#38a963;" >//of all service
                                                    providers</ span >

System.out.println(< span style = "color:#009;" >"Press any key to trigger sync of all
                                                    configured service providers."</ span >);

< span style = "color:#009;" >new</ span > Scanner(System.in).nextLine();

< span style = "color:#38a963;" >//Step 5: Kick off a sync of all Service
                                                    Providers</ span >

< span style = "color:#38a963;" >//</ span >

< span style = "color:#38a963;" >//Use the Fulfillment web client to kick
                                                    of CUCDM sync on HCS Server</ span >

< span style = "color:#38a963;" >//</ span >

< span style = "color:#38a963;" >//NOTE: passing in a null list, syncs all
                                                    configured service providers</ span >

fulfillmentWebService.syncListOfServiceProviders(< span style = "color:#009;" >null</ span >);

}

</ td ></ tr ></ tbody ></ table ></ strong >

# Build the web client

The sample code download includes an ant build.xml file that you can use to build this project.

The build.xml file performs the following tasks:

- Compile the autogenerated code stubs.

- Archive all the autogenerated code and class files into a jar file (call this jar file "HCSWebClientGeneratedClasses.jar").

- Compile the business logic class files.

- Archive the business logic code and the class files into a jar file. (This jar file will depend on the HCSWebClientGeneratedClasses.jar, and will be called WorkflowHCSWebClient.jar.)

- Archive the downloaded WSDL files.

- Use the main class of WorkflowHCSWebClient as the class that is executed when the jar is run.

You can store the build.xml file from the sample code download in /home/alice/myProject/build.xml .

Be sure to set your CXF_HOME environment variable as follows:

?

1

2

3

4

5

6

7

8

< strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" >

< table class = "tablesorter" cellpadding = "0" cellspacing = "0" >

< tbody >

< tr >

< td style = "border-right-color:#6ce26c;
                                                        border-right-width:thick; border-left-style:none;
                                                        border-bottom-style:none; border-top-style:none
                                                        " >< span style = "color:#999;" >1</ span >

</ td >

< td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $ 
                                                        < span style = "color:#f952ac;" >export</ span >
                                                        CXF_HOME=/Your_CXF_Download_Location/apache-cxf-2.X.X/

</ td ></ tr ></ tbody ></ table ></ strong >

You can build the client as follows:

?

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

< strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" >

< table class = "tablesorter" cellpadding = "0" cellspacing = "0" >

< tbody >

< tr >

< td style = "width:
                                                        10px; border-right-color:#6ce26c; border-right-width:thick;
                                                        border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none " >< span style = "color:#999;" >1</ span >

< span style = "color:#999;" >2</ span >

< span style = "color:#999;" >3</ span >

</ td >

< td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $ 
                                                        < span style = "color:#f952ac;" >pwd</ span >

/home/alice/myProject

$
                                                    ant all

</ td ></ tr ></ tbody ></ table ></ strong >

# Run the web client

To run the web client, use the following command. Enter the appropriate server address, username and password for your system.

?

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

< strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" >

< table class = "tablesorter" cellpadding = "0" cellspacing = "0" >

< tbody >

< tr >

< td style = "border-right-color:#6ce26c;
                                                        border-right-width:thick; border-left-style:none;
                                                        border-bottom-style:none; border-top-style:none
                                                        " >< span style = "color:#999;" >1</ span >

< span style = "color:#999;" >2</ span >

< span style = "color:#999;" >3</ span >

</ td >

< td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $ 
                                                        < span style = "color:#f952ac;" >pwd</ span >

/home/alice/myProject

$
                                                    java -Dhcs=< span style = "color:#09F;" >"my-hcs-box"</ span >
                                                    -Dusername=< span style = "color:#09F;" >"my_username"</ span >
                                                    -Dpassword=< span style = "color:#09F;" >"my_password"</ span > -jar
                                                    ./jar/WorkflowHCSWebClient.jar

</ td ></ tr ></ tbody ></ table ></ strong >

| 1 2 3 4 5 6 7 | < strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" > < table class = "tablesorter" cellpadding = "0" cellspacing = "0" > < tbody > < tr > < td style = "border-right-color:#6ce26c;
                                                        border-right-width:thick; border-left-style:none;
                                                        border-bottom-style:none; border-top-style:none
                                                        " >< span style = "color:#999;" >1</ span > </ td > < td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none; " >  $   < span style = "color:#f952ac;" >export</ span >  CXF_HOME=/Your_CXF_Download_Location/apache-cxf-2.X.X/</ td ></ tr ></ tbody ></ table ></ strong > |
|---|---|

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 | < strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" > < table class = "tablesorter" cellpadding = "0" cellspacing = "0" > < tbody > < tr > < td style = "width:
                                                        10px; border-right-color:#6ce26c; border-right-width:thick;
                                                        border-left-style: none; border-bottom-style:none;
                                                        border-top-style:none " >< span style = "color:#999;" >1</ span > < span style = "color:#999;" >2</ span > < span style = "color:#999;" >3</ span > < span style = "color:#999;" >4</ span > < span style = "color:#999;" >5</ span > < span style = "color:#999;" >6</ span > </ td > < td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $
                                                        < span style = "color:#f952ac;" >pwd</ span > /home/alice $
                                                    < span style = "color:#f952ac;" >mkdir</ span >
                                                    myProject $
                                                    < span style = "color:#f952ac;" >cd</ span > myProject $
                                                    < span style = "color:#f952ac;" >mkdir</ span >
                                                    wsdl $
                                                    < span style = "color:#f952ac;" >cd</ span > wsdl</ td ></ tr ></ tbody ></ table ></ strong > |
|---|---|

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 | < strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" > < table class = "tablesorter" cellpadding = "0" cellspacing = "0" > < tbody > < tr > < td style = "width:
                                                        10px; border-right-color:#6ce26c; border-right-width:thick;
                                                        border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none " >< span style = "color:#999;" >1</ span > < span style = "color:#999;" >2</ span > < span style = "color:#999;" >3</ span > < span style = "color:#999;" >4</ span > < span style = "color:#999;" >5</ span > </ td > < td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $< span style = "color:#f952ac;" > pwd</ span > /home/alice/myProject $< span style = "color:#f952ac;" > mkdir</ span >
                                                    autogen $< span style = "color:#f952ac;" > mkdir</ span >
                                                    autogen/src $< span style = "color:#f952ac;" > mkdir</ span >
                                                    autogen/build</ td ></ tr ></ tbody ></ table ></ strong > |
|---|---|

| 1 2 3 4 5 6 7 8 9 10 11 | < strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" > < table class = "tablesorter" cellpadding = "0" cellspacing = "0" > < tbody > < tr > < td style = "width:
                                                        10px; border-right-color:#6ce26c; border-right-width:thick;
                                                        border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none " >< span style = "color:#999;" >1</ span > < span style = "color:#999;" >2</ span > < span style = "color:#999;" >3</ span > </ td > < td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $< span style = "color:#f952ac;" > pwd</ span > /home/alice/myProject $< span style = "color:#f952ac;" > mkdir</ span >
                                                    build</ td ></ tr ></ tbody ></ table ></ strong > |
|---|---|

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 | < strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" > < table class = "tablesorter" cellpadding = "0" cellspacing = "0" > < tbody > < tr > < td style = "border-right-color:#6ce26c;
                                                        border-right-width:thick; border-left-style:none;
                                                        border-bottom-style:none; border-top-style:none
                                                        " >< span style = "color:#999;" >1</ span > < span style = "color:#999;" >2</ span > < span style = "color:#999;" >3</ span > < span style = "color:#999;" >4</ span > < span style = "color:#999;" >5</ span > < span style = "color:#999;" >6</ span > </ td > < td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $
                                                        < span style = "color:#f952ac;" >pwd</ span > /home/alice/myProject $
                                                    /Your_CXF_Download_Location/apache-cxf-2.X.X/bin/wsdl2java -classdir
                                                    autogen/build/ -d autogen/src/ -compile
                                                    ./wsdl/SharedDataRepositoryWebService.wsdl $
                                                    /Your_CXF_Download_Location/apache-cxf-2.X.X/bin/wsdl2java -classdir
                                                    autogen/build/ -d autogen/src/ -compile
                                                    ./wsdl/FulfillmentWebService.wsdl $
                                                    /Your_CXF_Download_Location/apache-cxf-2.X.X/bin/wsdl2java -classdir
                                                    autogen/build/ -d autogen/src/ -compile
                                                    ./wsdl/ServiceInventoryWebService.wsdl $
                                                    /Your_CXF_Download_Location/apache-cxf-2.X.X/bin/wsdl2java -classdir
                                                    autogen/build/ -d autogen/src/ -compile
                                                    ./wsdl/HCSLicenseManagerWebService.wsdl</ td ></ tr ></ tbody ></ table ></ strong > |
|---|---|

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 | < strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" > < table class = "tablesorter" cellpadding = "0" cellspacing = "0" > < tbody > < tr > < td style = "width:
                                                        10px; border-right-color:#6ce26c; border-right-width:thick;
                                                        border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none " >< span style = "color:#999;" >1</ span > < span style = "color:#999;" >2</ span > < span style = "color:#999;" >3</ span > < span style = "color:#999;" >4</ span > < span style = "color:#999;" >5</ span > </ td > < td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $
                                                        < span style = "color:#f952ac;" >pwd</ span > /home/alice/myProject $
                                                    < span style = "color:#f952ac;" >mkdir</ span >
                                                    src $
                                                    < span style = "color:#f952ac;" >mkdir</ span >
                                                    src/com $
                                                    < span style = "color:#f952ac;" >mkdir</ span >
                                                    src/com/example </ td ></ tr ></ tbody ></ table ></ strong > |
|---|---|

| 1 2 3 4 5 6 7 8 9 10 11 12 | < strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" > < table class = "tablesorter" cellpadding = "0" cellspacing = "0" > < tbody > < tr > < td style = "width:
                                                        10px; border-right-color:#6ce26c; border-right-width:thick;
                                                        border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none " >< span style = "color:#999;" >1</ span > < span style = "color:#999;" >2</ span > < span style = "color:#999;" >3</ span > </ td > < td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $
                                                        < span style = "color:#f952ac;" >pwd</ span > /home/alice/myProject $
                                                    < span style = "color:#f952ac;" >mkdir</ span >
                                                    build </ td ></ tr ></ tbody ></ table ></ strong > |
|---|---|

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 | < strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" > < table class = "tablesorter" cellpadding = "0" cellspacing = "0" > < tbody > < tr > < td style = "border-right-color:#6ce26c;
                                                        border-right-width:thick; border-left-style:none;
                                                        border-bottom-style:none; border-top-style:none
                                                        " >< span style = "color:#999;" >1</ span > < span style = "color:#999;" >2</ span > < span style = "color:#999;" >3</ span > < span style = "color:#999;" >4</ span > < span style = "color:#999;" >5</ span > < span style = "color:#999;" >6</ span > < span style = "color:#999;" >7</ span > < span style = "color:#999;" >8</ span > < span style = "color:#999;" >9</ span > < span style = "color:#999;" >10</ span > < span style = "color:#999;" >11</ span > < span style = "color:#999;" >12</ span > < span style = "color:#999;" >13</ span > < span style = "color:#999;" >14</ span > < span style = "color:#999;" >15</ span > < span style = "color:#999;" >16</ span > < span style = "color:#999;" >17</ span > < span style = "color:#999;" >18</ span > < span style = "color:#999;" >19</ span > < span style = "color:#999;" >20</ span > < span style = "color:#999;" >21</ span > < span style = "color:#999;" >22</ span > < span style = "color:#999;" >23</ span > < span style = "color:#999;" >24</ span > < span style = "color:#999;" >25</ span > < span style = "color:#999;" >26</ span > < span style = "color:#999;" >27</ span > < span style = "color:#999;" >28</ span > < span style = "color:#999;" >29</ span > < span style = "color:#999;" >30</ span > < span style = "color:#999;" >31</ span > < span style = "color:#999;" >32</ span > < span style = "color:#999;" >33</ span > < span style = "color:#999;" >34</ span > < span style = "color:#999;" >35</ span > </ td > < td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > < span style = "color:#009;" >public void</ span >
                                                        doSampleWorkFlow () < span style = "color:#009;" >throws</ span >
                                                        NBIException, com.cisco.hcs.nbi.ws.fulfillment.v9_0.NBIException
                                                        { ServiceProvider
                                                    serviceProvider = getServiceProvider(); KID
                                                    serviceProviderKID = serviceProvider.getPk(); ManagementNetwork
                                                    managementNetwork = getManagementNetwork(serviceProviderKID); < span style = "color:#38a963;" >//Step 1: Configure Default Credentials</ span > configureDefaultCredentials(serviceProviderKID); < span style = "color:#38a963;" >//Step 2: Configure a
                                                    CUCDM</ span > configureCUCDM(managementNetwork); < span style = "color:#38a963;" >//Step 3: Configure a
                                                    CUOM</ span > configureCUOM(managementNetwork); < span style = "color:#38a963;" >//Step 4: Configure a Data
                                                    Center</ span > configureDataCenter(serviceProviderKID); < span style = "color:#38a963;" >//Wait for user input before kicking of
                                                    manual sync</ span > < span style = "color:#38a963;" >//of all service
                                                    providers</ span > System.out.println(< span style = "color:#009;" >"Press any key to trigger sync of all
                                                    configured service providers."</ span >); < span style = "color:#009;" >new</ span > Scanner(System.in).nextLine(); < span style = "color:#38a963;" >//Step 5: Kick off a sync of all Service
                                                    Providers</ span > < span style = "color:#38a963;" >//</ span > < span style = "color:#38a963;" >//Use the Fulfillment web client to kick
                                                    of CUCDM sync on HCS Server</ span > < span style = "color:#38a963;" >//</ span > < span style = "color:#38a963;" >//NOTE: passing in a null list, syncs all
                                                    configured service providers</ span > fulfillmentWebService.syncListOfServiceProviders(< span style = "color:#009;" >null</ span >); } </ td ></ tr ></ tbody ></ table ></ strong > |
|---|---|

| 1 2 3 4 5 6 7 8 | < strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" > < table class = "tablesorter" cellpadding = "0" cellspacing = "0" > < tbody > < tr > < td style = "border-right-color:#6ce26c;
                                                        border-right-width:thick; border-left-style:none;
                                                        border-bottom-style:none; border-top-style:none
                                                        " >< span style = "color:#999;" >1</ span > </ td > < td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $ 
                                                        < span style = "color:#f952ac;" >export</ span >
                                                        CXF_HOME=/Your_CXF_Download_Location/apache-cxf-2.X.X/ </ td ></ tr ></ tbody ></ table ></ strong > |
|---|---|

| 1 2 3 4 5 6 7 8 9 10 11 12 | < strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" > < table class = "tablesorter" cellpadding = "0" cellspacing = "0" > < tbody > < tr > < td style = "width:
                                                        10px; border-right-color:#6ce26c; border-right-width:thick;
                                                        border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none " >< span style = "color:#999;" >1</ span > < span style = "color:#999;" >2</ span > < span style = "color:#999;" >3</ span > </ td > < td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $ 
                                                        < span style = "color:#f952ac;" >pwd</ span > /home/alice/myProject $
                                                    ant all </ td ></ tr ></ tbody ></ table ></ strong > |
|---|---|

| 1 2 3 4 5 6 7 8 9 10 11 12 | < strong style = "font:'Courier
                                                    New', Courier, monospace; font-size:14px;" > < table class = "tablesorter" cellpadding = "0" cellspacing = "0" > < tbody > < tr > < td style = "border-right-color:#6ce26c;
                                                        border-right-width:thick; border-left-style:none;
                                                        border-bottom-style:none; border-top-style:none
                                                        " >< span style = "color:#999;" >1</ span > < span style = "color:#999;" >2</ span > < span style = "color:#999;" >3</ span > </ td > < td style = "border-right-style:
                                                        none; border-left-style:none; border-bottom-style:none;
                                                        border-top-style:none;" > $ 
                                                        < span style = "color:#f952ac;" >pwd</ span > /home/alice/myProject $
                                                    java -Dhcs=< span style = "color:#09F;" >"my-hcs-box"</ span >
                                                    -Dusername=< span style = "color:#09F;" >"my_username"</ span >
                                                    -Dpassword=< span style = "color:#09F;" >"my_password"</ span > -jar
                                                    ./jar/WorkflowHCSWebClient.jar </ td ></ tr ></ tbody ></ table ></ strong > |
|---|---|