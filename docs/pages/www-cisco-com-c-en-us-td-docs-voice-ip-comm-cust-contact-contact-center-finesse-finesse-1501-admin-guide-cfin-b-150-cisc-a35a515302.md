---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-finesse-finesse-1501-admin-guide-cfin-b-150-cisc-a35a515302
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/finesse/finesse_1501/admin/guide/cfin_b_150_cisco-finesse-administration-guide/cfin_m_150_manage-phone-books.html
retrieved_at: 2026-08-21T12:04:36.027893+00:00
---

Cisco Finesse Administration Guide, Release 15.0(1)

# Cisco Finesse Administration Guide, Release 15.0(1)

Updated: December 12, 2025

Chapter: Manage Phone Books

## Chapter: Manage Phone Books

# Manage Phone Books

## Phone Books and Contacts

Finesse supports the following number of phone books:

10 global phone books

300 team phone books

The system supports a total of 50,000 contacts. The total number of contacts per agent across all phone books is limited to
                              6000.

Use the Manage Phone Books gadget to view, add, edit, or delete phone books and phone book contacts. Click the Name or Assign
                              To headers to sort the phone books in ascending or descending order. Click the last Name, First Name, Number, or Note headers
                              to sort the contacts in ascending or descending order.

The following table describes the fields on the Manage Phone Books gadget:

Field

Explanation

Name

The name of the phone book. It must be unique, and can be a maximum of 64 alphanumeric characters.

Assign To

Indicates if the phone book is global (All Users) or team (Teams).

Last Name

The last name of a contact. The last name can be a maximum of 128 characters. This field is optional.

First Name

The first name of a contact. The first name can be a maximum of 128 characters. This field is optional.

Number

The phone number for the contact. The phone number can be 1-32 characters long and cannot be blank.

Optional text that describes the contact. The note can be a maximum of 128 characters.

Actions on the Manage Phone Books gadget:

New: Add a new phone book or contact

Edit: Edit an existing phone book or contact

Delete: Delete a phone book or contact

Refresh: Reload the list of phone books or contacts from the server

Import: Import a list of contacts to the phone book

Export: Export a list of contacts from the phone book

## Add Phone Book

Step 1

In the Manage Phone Books gadget, click New .

Step 2

In the Name field, enter a name for the phone book.

Phone book names can be a maximum of 64 characters.

Step 3

From the Assign To drop-down, select All Users if the phone book is global or Teams if the phone book is available to specified teams.

Step 4

Click Save .

## Edit Phone Book

Step 1

In the Manage Phone Books gadget, select the phone book you want to edit.

Step 2

Click Edit .

Step 3

In the Name field, enter the new name for the phone book. If you want to change who can access the phone book, in the Assign To drop-down, choose All Users or Teams .

Step 4

Click Save .

If you change the Assign To field from Teams to All Users, click Yes to confirm the change.

## Delete Phone Book

Step 1

In the Manage Phone Books gadget, select the phone book that you want to delete.

Step 2

Click Delete .

Step 3

Click Yes to confirm the deletion of the selected phone book.

## Import Contacts

The Import function allows you to replace all the contacts in a phone book with a new list of contacts, or to populate a new
                              phone book with contacts.

The import list must be in the specified comma separated values (CSV) format, and can contain a maximum of 6000 contacts.
                              Import lists that contain more than 6000 contacts are rejected with an error message.

The CSV file contains the fields described in the following table:

Field

Max Length

Can Be Blank?

Permitted Characters

First Name

128

Yes

Alphanumeric characters

The CSV file that contains the contacts to import must use Latin encoding.

Last Name

128

Yes

Phone Number

32

No

Notes

128

Yes

The following is an example of a phone book CSV file:

```
"First Name","Last Name","Phone Number","Notes"
"Amanda","Cohen","6511234",""
"Nicholas","Knight","612-555-1228","Sales"
"Natalie","Lambert","952-555-9876","Benefits"
"Joseph","Stonetree","651-555-7612","Manager"
```

A phone book CSV file must conform to this format and include the headers in the first line. During import, the file is scanned
                              for illegal characters. If any are found, they are replaced with question marks.

Exported CSV files always show each field enclosed in double quotes to ensure that any commas or double quotes that are part
                                          of the actual filed data are not mistaken for field delimiters. If your data does not include these characters, you can omit
                                          the double quotes in files you prepare for importing.

Step 1

In the Manage Phone Books gadget, select the phone book into which you want to import a list of contacts.

Step 2

Click Import .

Step 3

Click Browse and navigate to the location of the CSV file containing the contacts you want to import.

The CSV file must use Latin encoding.

Step 4

Click OK .

## Export Contacts

The Export function allows you to extract a list of contacts from an existing phone book. The exported list is saved in CSV
                              format.

Step 1

In the Manage Phone Books gadget, select the phone book that contains the contacts you want to export.

Step 2

Click Export .

Step 3

Click Open to open the CSV file in Excel, or click the Save drop-down list and choose Save , Save as , or Save and open .

Step 4

A message appears that gives you the option to view the downloaded file, open the folder into which the download was saved, view the Internet Explorer View Downloads window, or dismiss the message without viewing the file.

Step 5

A message appears that gives you the option to view the downloaded file, open the folder into which the download was saved, view the Internet Explorer View Downloads window, or dismiss the message without viewing the file.

## Add Contact

Step 1

In the Manage Phone Books gadget, select the phone book to which you want to add a contact.

The List of Contacts for <phone book name> area appears.

Step 2

Click New .

Step 3

Complete the fields. The First Name, Last Name, and Note fields are optional and have a maximum length of 128 characters.
                                       The Number field is required and has a maximum length of 32 characters.

Step 4

Click Save .

## Edit Contact

Step 1

In the Manage Phone Books gadget, select the phone book that contains the contact you want to edit.

The List of Contacts for <phone book name> area appears.

Step 2

Select the contact you want to edit.

Step 3

Click Edit .

Step 4

Edit the fields that you want to change. The First Name, Last Name, and Note fields are optional and have a maximum of 128
                                       characters. The Number field is required and has a maximum of 32 characters.

Step 5

Click Save .

## Delete Contact

Step 1

In the Manage Phone Books gadget, select the phone book that contains the contact you want to delete.

The List of Contacts for <phone book name> area appears.

Step 2

Select the contact that you want to delete.

Step 3

Click Delete .

Step 4

Click Yes to confirm the deletion of the selected contact.

| Field | Explanation |
|---|---|
| Name | The name of the phone book. It must be unique, and can be a maximum of 64 alphanumeric characters. |
| Assign To | Indicates if the phone book is global (All Users) or team (Teams). |
| Last Name | The last name of a contact. The last name can be a maximum of 128 characters. This field is optional. |
| First Name | The first name of a contact. The first name can be a maximum of 128 characters. This field is optional. |
| Number | The phone number for the contact. The phone number can be 1-32 characters long and cannot be blank. |
| Note | Optional text that describes the contact. The note can be a maximum of 128 characters. |

| Step 1 | In the Manage Phone Books gadget, click New . |
|---|---|
| Step 2 | In the Name field, enter a name for the phone book. Note Phone book names can be a maximum of 64 characters. | Note | Phone book names can be a maximum of 64 characters. |
| Note | Phone book names can be a maximum of 64 characters. |
| Step 3 | From the Assign To drop-down, select All Users if the phone book is global or Teams if the phone book is available to specified teams. |
| Step 4 | Click Save . |

| Note | Phone book names can be a maximum of 64 characters. |
|---|---|

| Step 1 | In the Manage Phone Books gadget, select the phone book you want to edit. |
|---|---|
| Step 2 | Click Edit . |
| Step 3 | In the Name field, enter the new name for the phone book. If you want to change who can access the phone book, in the Assign To drop-down, choose All Users or Teams . |
| Step 4 | Click Save . If you change the Assign To field from Teams to All Users, click Yes to confirm the change. |

| Step 1 | In the Manage Phone Books gadget, select the phone book that you want to delete. |
|---|---|
| Step 2 | Click Delete . |
| Step 3 | Click Yes to confirm the deletion of the selected phone book. |

| Field | Max Length | Can Be Blank? | Permitted Characters |
|---|---|---|---|
| First Name | 128 | Yes | Alphanumeric characters Note The CSV file that contains the contacts to import must use Latin encoding. | Note | The CSV file that contains the contacts to import must use Latin encoding. |
| Note | The CSV file that contains the contacts to import must use Latin encoding. |
| Last Name | 128 | Yes |
| Phone Number | 32 | No |
| Notes | 128 | Yes |

| Note | The CSV file that contains the contacts to import must use Latin encoding. |
|---|---|

| Note | Exported CSV files always show each field enclosed in double quotes to ensure that any commas or double quotes that are part
                                          of the actual filed data are not mistaken for field delimiters. If your data does not include these characters, you can omit
                                          the double quotes in files you prepare for importing. |
|---|---|

| Step 1 | In the Manage Phone Books gadget, select the phone book into which you want to import a list of contacts. |
|---|---|
| Step 2 | Click Import . |
| Step 3 | Click Browse and navigate to the location of the CSV file containing the contacts you want to import. Note The CSV file must use Latin encoding. | Note | The CSV file must use Latin encoding. |
| Note | The CSV file must use Latin encoding. |
| Step 4 | Click OK . |

| Note | The CSV file must use Latin encoding. |
|---|---|

| Step 1 | In the Manage Phone Books gadget, select the phone book that contains the contacts you want to export. |
|---|---|
| Step 2 | Click Export . |
| Step 3 | Click Open to open the CSV file in Excel, or click the Save drop-down list and choose Save , Save as , or Save and open . |
| Step 4 | A message appears that gives you the option to view the downloaded file, open the folder into which the download was saved, view the Internet Explorer View Downloads window, or dismiss the message without viewing the file. |
| Step 5 | A message appears that gives you the option to view the downloaded file, open the folder into which the download was saved, view the Internet Explorer View Downloads window, or dismiss the message without viewing the file. |

| Step 1 | In the Manage Phone Books gadget, select the phone book to which you want to add a contact. The List of Contacts for <phone book name> area appears. |
|---|---|
| Step 2 | Click New . |
| Step 3 | Complete the fields. The First Name, Last Name, and Note fields are optional and have a maximum length of 128 characters.
                                       The Number field is required and has a maximum length of 32 characters. |
| Step 4 | Click Save . |

| Step 1 | In the Manage Phone Books gadget, select the phone book that contains the contact you want to edit. The List of Contacts for <phone book name> area appears. |
|---|---|
| Step 2 | Select the contact you want to edit. |
| Step 3 | Click Edit . |
| Step 4 | Edit the fields that you want to change. The First Name, Last Name, and Note fields are optional and have a maximum of 128
                                       characters. The Number field is required and has a maximum of 32 characters. |
| Step 5 | Click Save . |

| Step 1 | In the Manage Phone Books gadget, select the phone book that contains the contact you want to delete. The List of Contacts for <phone book name> area appears. |
|---|---|
| Step 2 | Select the contact that you want to delete. |
| Step 3 | Click Delete . |
| Step 4 | Click Yes to confirm the deletion of the selected contact. |