---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-aft-1-1-english-verizon-user-guide-user-ver-aftuse-html-d7e3e15ec5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/aft/1_1/english/verizon/user/guide/user_ver/AFTuse.html
retrieved_at: 2026-08-21T15:51:58.109567+00:00
---

ALI Formatting Tool User Guide for Verizon

# ALI Formatting Tool User Guide for Verizon

Chapter: Using the ALI Formatting Tool

## Chapter: Using the ALI Formatting Tool

## Using the ALI Formatting Tool

This section provides information about how to use the ALI Formatting Tool (AFT):

• Using the ALI Formatting Tool Interface

• Using AFT to Generate a Formatted ALI File

## Using the ALI Formatting Tool Interface

To familiarize yourself with the AFT interface, select the pull-down menus from the AFT main menu to see the options. Hold your mouse over each AFT icon to view the icon description in the tool tip box.

These topics will help you become familiar with the AFT interface:

• ALI Formatting Tool Fields

• Using the Tool Bar and Icons

### ALI Formatting Tool Fields

You can edit the following fields using AFT:

• The header and trailer fields. The ALI Formatting Tool (AFT) displays all the ALI record data in the ALI tab. The ALI file consists of one header record and one trailer record only; there is not an individual header and trailer record for each ELIN record.

• The Function/Transaction Code field. Refer to the "Using the ALI Formatting Tool for Verizon" for more information.

• Any service provider-specific fields. Refer to the "Using the ALI Formatting Tool for Verizon" for more information.

You cannot edit the following fields using AFT:

• The ALI records fields that you configure and edit through Cisco Emergency Responder (Cisco ER). They are disabled (greyed out) in AFT.

• The record count field. This trailer field cannot be edited in AFT because AFT calculates this number internally based on the number of records selected to export.

Related Topics

• Using the Tool Bar and Icons

• Before You Generate Files

• Generating a Formatted ALI File

### Using the Tool Bar and Icons

Use Table 3-1 to learn how you use the AFT interface to perform the main AFT tasks.

Use the "Generating a Formatted ALI File" section for a step-by-step procedure about putting the tasks together and generating reformatted ALI files.

Table 3-1 Using the AFT Interface

Give a NENA file as input to AFT

Use one of these methods:

• Click the File Open icon .

• Select Menu > File > Open (Ctrl+O) .

If the NENA files are on the Master CER server and AFT is installed on the Standby CER server, you can use the Open Window Dialog box to browse to a shared Master CER folder.

Go to a specific ELIN number

1. Select Menu > File > Go to ELIN (Ctrl+E) .

2. Enter the ELIN number.

If the ELIN is present, it is selected in the tree and the ALI tab is populated with data for that record.

If it is an invalid record number, a message displays with the valid range of numbers.

Go to a specific record

1. Select Menu > File > Go to Record Number (Ctrl+R) .

2. Enter the record number.

If the record number is valid, that record is selected in the tree and the ALI tab is populated with data for that record.

If it is an invalid record number, a message displays with the valid range of numbers.

View ALI details for an ELIN/Select an ELIN to edit its ALI fields

Click on the ELIN in the tree.

This highlights the ELIN and populates its details in the right pane of the window.

You can then edit the ALI records by entering new values in the ALI editable fields.

Undo record change/Redo record change

Use one of these methods:

• Click the Undo/Redo icon.

• Select Menu > Edit > Undo record/Redo record change (Ctrl+Z/Ctrl+Y) .

The Undo/Redo option remembers the last 20 record changes.

Cut/Copy/Paste record input

Use one of these methods:

• Click the Cut/Copy/Paste icon.

• Select Menu > Edit > Cut/Copy/Paste (Ctrl+X/Ctrl+C/Ctrl+V) .

Select ALI records to be exported to your service provider

In the tree, click in the ELIN check box. Use one of the following options:

• Select all ELINs in the tree by checking the root node of the tree.

• Select all ELINs with a specific area code by checking the Area Code in the tree. For example, checking the 408 check box will select all the numbers in the 408 area code.

• Select all ELINs with a specific City Code by checking the City Code in the tree. For example, clicking on 228 will also select 228-9333 and 228-5672.

• Select an individual ELIN by checking the 4-digit directory number, for example, 9933.

Check marks will indicate the ELINs that are selected.

Generate Formatted File

Use one of the following methods:

• Click the Generate Formatted File icon.

• Go to Menu > Tools and click Generate Formatted File (Ctrl+G) .

AFT generates an ALI file in a format that your service provider can read.

Perform a bulk update to the ALI files

1. Use one of these methods:

– Click the Bulk Update icon.

– Select Menu > Tools > Bulk Update (Ctrl+B) .

AFT displays the bulk update form.

2. Select one of the following options:

– To apply the changes to all records, click the first tab, Apply All .

– To apply the changes to one area code, click the second tab, Apply by Area Code .

– To apply the change to one area code and one city code, click the third tab, Apply by Area Code and City Code .

The bulk update feature saves the changes automatically.

Save updates to the ALI file

Select Menu > Tools > Save Record (Ctrl+S) .

The new value is saved and displayed in the interface.

If you modify an ALI record but do not save the changes, an alert asks if you want to save the changes.

Close AFT

Select Menu > File > Exit .

If you try to close AFT without saving changes, AFT asks if you want to generate a formatted file.

Related Topics

• ALI Formatting Tool Fields

• Using AFT to Generate a Formatted ALI File

## Using AFT to Generate a Formatted ALI File

Use the following topics to generate a formatted ALI file:

• Before You Generate Files

• Generating a Formatted ALI File

### Before You Generate Files

Make sure you have completed the following tasks before you begin to use AFT to generate an exported file:

• You have installed, set up and used Cisco Emergency Responder (Cisco ER) to configure ERLs with the ELIN and ALI information and to generate a NENA file. For information on performing these tasks, refer to the Cisco Emergency Responder Administration Guide .

• You have successfully installed, launched and tested AFT. See "Installing the ALI Formatting Tool,"

• You understand which specific information you modify for your service provider. For details, see "Using the ALI Formatting Tool for Verizon."

### Generating a Formatted ALI File

To use AFT to generate a formatted file, perform the following steps:

Step 1 Provide a NENA file generated by Cisco Emergency Responder (Cisco ER) as input to AFT in one of these ways:

• Select Menu > File > Open (Ctrl+O) and browse to select the file name.

• Use the File Open icon and enter the file name.

Tip If the NENA files are on the Master Cisco ER server and AFT is installed on the Standby Cisco ER server, you can use the Open Window Dialog box to browse to a shared Master Cisco ER folder.

AFT displays all the ELINs from the NENA file in a tree box in the left side of the page by the Area Code, City Code and 4-digit directory number.

Step 2 To view details of the ALI files, click on an ELIN in the tree.

This highlights the ELIN and populates its details in the right pane of the window.

Step 3 Edit the ALI fields by entering new values in the editable fields.

Step 4 Save any changes that you made to the ALI file:

Select Menu > Tools > Save Record (Ctrl+S) .

Step 5 Select the ELINs that you want to export to the service provider by clicking in the corresponding check boxes in the tree.

• To select all ELINs in the tree, check the root node of the tree.

• To select all ELINs with a specific area code, click in the Area Code check box in the tree. For example, clicking the 408 check box will select all the numbers in the 408 area code. All the 408 numbers display check marks.

• To select all ELINs with a specific City Code, click in the City Code check box. For example, selecting 228 will also select 228-9333 and 228-5672.

• To select an individual ELIN, click in the 4-digit check box, for example, 9933

Check marks will indicate the ELINs that are selected.

Step 6 Update the service provider-fields in AFT:

For details about the service provider-specific information required, see "Using the ALI Formatting Tool for Verizon."

Step 7 At this point, if the service provider-specific field is common for many ELIN records (for example, if all the ELIN records share the same Private Switch Code), you can use AFT's Bulk Update feature:

a. Select Menu > Tools  >  Bulk Update (Ctrl+B) or the Bulk Update icon.

AFT displays the bulk update form.

b. Select one of the following options:

– To apply the changes to all records, click the first tab: Apply All .

– To apply the changes to one area code, click the second tab: Apply by Area Code .

– To apply the changes to one area code and one city code, click the third tab: Apply by Area Code and City Code .

Step 8 Generate a formatted file in one of these way:

• Go to Menu > Tools and click Generate Formatted File (Ctrl+G) .

• From the Tool Bar, click the Generate Formatted File icon.

AFT generates an ALI file in a format specific to your service provider and prompts you for a location to save it.

Step 9 Enter a location where you want to store the formatted file.

Step 10 Using the service provider's preferred method of transmitting files, send the ALI file to your service provider so they can update their E911 database with the ELINs from the AFT ALI file.

Tip Be sure to keep a copy of the AFT ALI file for your records. This will be helpful if the service providers reports errors; you can make any required changes to the file without having to re-do all the AFT formatting changes.

Step 11 Your service provider returns the status of the ALI files.

• If your service provider reports that there are no errors, you can continue using AFT to generate more formatted records or you can quit the program.

• If your service provider reports that there are ALI errors, perform the following steps:

– Make corrections to the formatted file that you sent to the service provider. All the error codes for the service providers are defined in the ALI format documentation for that service provider. Refer to their documentation to determine the errors in your file and correct the errors using AFT.

Note If an error occurs in fields that cannot be edited using AFT, you must use CER to correct the fields. Then use AFT to generate the file again.

– Send the corrected file to your service provider. Again, be sure to keep a copy of your corrected file for your records.

– Repeat this process until your service provider can read the formatted files and can use them to update their ELIN records.

Related Topics

• Using the Tool Bar and Icons

• "Troubleshooting the ALI Formatting Tool"

• "Using the ALI Formatting Tool for Verizon"

| Task | Procedure | Notes |
|---|---|---|
| Give a NENA file as input to AFT | Use one of these methods: • Click the File Open icon . • Select Menu > File > Open (Ctrl+O) . | If the NENA files are on the Master CER server and AFT is installed on the Standby CER server, you can use the Open Window Dialog box to browse to a shared Master CER folder. |
| Go to a specific ELIN number | 1. Select Menu > File > Go to ELIN (Ctrl+E) . 2. Enter the ELIN number. | If the ELIN is present, it is selected in the tree and the ALI tab is populated with data for that record. If it is an invalid record number, a message displays with the valid range of numbers. |
| Go to a specific record | 1. Select Menu > File > Go to Record Number (Ctrl+R) . 2. Enter the record number. | If the record number is valid, that record is selected in the tree and the ALI tab is populated with data for that record. If it is an invalid record number, a message displays with the valid range of numbers. |
| View ALI details for an ELIN/Select an ELIN to edit its ALI fields | Click on the ELIN in the tree. | This highlights the ELIN and populates its details in the right pane of the window. You can then edit the ALI records by entering new values in the ALI editable fields. |
| Undo record change/Redo record change | Use one of these methods: • Click the Undo/Redo icon. • Select Menu > Edit > Undo record/Redo record change (Ctrl+Z/Ctrl+Y) . | The Undo/Redo option remembers the last 20 record changes. |
| Cut/Copy/Paste record input | Use one of these methods: • Click the Cut/Copy/Paste icon. • Select Menu > Edit > Cut/Copy/Paste (Ctrl+X/Ctrl+C/Ctrl+V) . |  |
| Select ALI records to be exported to your service provider | In the tree, click in the ELIN check box. Use one of the following options: • Select all ELINs in the tree by checking the root node of the tree. • Select all ELINs with a specific area code by checking the Area Code in the tree. For example, checking the 408 check box will select all the numbers in the 408 area code. • Select all ELINs with a specific City Code by checking the City Code in the tree. For example, clicking on 228 will also select 228-9333 and 228-5672. • Select an individual ELIN by checking the 4-digit directory number, for example, 9933. | Check marks will indicate the ELINs that are selected. |
| Generate Formatted File | Use one of the following methods: • Click the Generate Formatted File icon. • Go to Menu > Tools and click Generate Formatted File (Ctrl+G) . | AFT generates an ALI file in a format that your service provider can read. |
| Perform a bulk update to the ALI files | 1. Use one of these methods: – Click the Bulk Update icon. – Select Menu > Tools > Bulk Update (Ctrl+B) . AFT displays the bulk update form. 2. Select one of the following options: – To apply the changes to all records, click the first tab, Apply All . – To apply the changes to one area code, click the second tab, Apply by Area Code . – To apply the change to one area code and one city code, click the third tab, Apply by Area Code and City Code . | The bulk update feature saves the changes automatically. |
| Save updates to the ALI file | Select Menu > Tools > Save Record (Ctrl+S) . | The new value is saved and displayed in the interface. If you modify an ALI record but do not save the changes, an alert asks if you want to save the changes. |
| Close AFT | Select Menu > File > Exit . | If you try to close AFT without saving changes, AFT asks if you want to generate a formatted file. |