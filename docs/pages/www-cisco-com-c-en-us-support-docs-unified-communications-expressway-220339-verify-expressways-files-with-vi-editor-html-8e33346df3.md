---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-expressway-220339-verify-expressways-files-with-vi-editor-html-8e33346df3
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/expressway/220339-verify-expressways-files-with-vi-editor.html
retrieved_at: 2026-08-16T15:43:48.603297+00:00
---

Verify Expressways Files with Vi Editor

# Verify Expressways Files with Vi Editor

### Download Options

Updated: April 3, 2023

Document ID: 220339

Contents

## Contents

## Introduction

This document describes the steps to access and edit a file with VI Editor on Expressways and another alternative with WinSCP software.

## Prerequisites

### Requirements

- Basic knowledge on Expressway.

- Expressway default configuration.

- WinSCP installed on PC.

### Components Used

- Expressway-C server on version X14.0.3.

- Windows 10 PC.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

### Basic Linux Commands

You can run commands to perform various tasks, from package installation, to user management, and file manipulation.

pwd command : Use the pwd command to find the path of your current directory.

cd command : To navigate through the Linux files and directories, use the cd command.

ls command : The ls command lists files and directories within a system. Run it without a flag or parameter to show the current directory content.

cat command: It lists, combines, and writes file content to the standard output. To run the cat command, type cat , followed by the file name and its extension.

There are several commands available, but they are out of the scope of this document.

## Vi Editor Basics

The Vi Editor tool is an interactive tool as it displays changes made in the file on the screen while you edit the file. In Vi Editor , you can insert, edit, or remove a word as the cursor moves throughout the file.

The Vi Editor has two modes:

- Command Mode : In Command Mode, actions are taken on the file. The Vi Editor starts in Command Mode. Here, the typed words act as commands in Vi Editor. To pass a command, you need to be in Command Mode.

- Insert Mode : In Insert Mode, is possible to insert text into the file. The Esc key takes you to the Command Mode from the Insert Mode.

By default, the Vi Editor starts in Command Mode . To enter text, you need to be in Insert Mode , just type the letter i to change to the Insert Mode.

### How to Use Vi Editor

In order to open a file with Vi Editor , you must know the directory path first. For the purpose of this article, a file named test-vi is created, the path is /tandberg/etc . Please see the image, with the steps to find the path and move to a specific directory. Make sure to access the Expressway by Secure Shell (SSH), and use the root account.

### Access a File

Once you navigate to the correct directory, run the command vi <file-name> to open it. By default Vi Editor is in the Command Mode :

Press Enter to access the file with the Vi Editor . The output shows the information within the file and allows you to modify it, if needed.

If you need it to delete or add text, type the letter i to enter the Insert Mode . Notice that in the lower left corner, the file name changed to the word INSERT .

In Insert mode , it is possible now to make any modifications as needed. For example:

### How to Save a File with Vi Editor

Once a file is ready to be saved, change back to the Command Mode by the use of the ESC key. Here are two different ways to Save and Quit .

Command: ZZ

Make sure the Command Mode is enabled. In this case, press ZZ ., which is the command to save and quit the file at the same time.

Command : wq

Make sure Command Mode is enabled. Whatever you type while in Command Mode , it can be seen in the lower left corner.

Afterwards, press Enter . The Expressway Linux prompt is now available.

Note : The q! command allows you to quit Vi Editor without the need to save the changes made.

## WinSCP Basics

WinSCP is an open source, free SFTP client, FTP client, WebDAV client, S3 client, and SCP client for Windows. Its main function is file transfer between a local and a remote computer. Beyond this, WinSCP offers script and basic file manager functionality.

### How to Use WinSCP Text Editor

Access the Expressway with the WinSCP application with root credentials.

WinSCP allows you to navigate in Expressway as if it is a Windows folder in any Windows PC. This image shows files on path /tandberg/etc where the test-vi file is stored.

Double-click, or right-click > Edit > Edit to open an internal editor, which allows you to edit the file and save it at the same time.

This image shows the same file output, with a new line: test line 6 added by the use of the WinSCP editor.

File with new line can be saved by the use of the same WinSCP text editor.

## Verify

### How to Check Changes on Files

The use of the Vi Editor is one way, but there is another Linux command that can be used. The command only allows you to print the content of a file onto the standard output stream.

Run the cat test-vi command on the same directory as the file.

Note : Path can also be added to the cat command instead. To navigate to the directory, use the cd command . For example: cat /tandberg/etc/test-vi .

## Additional Resources

Basic Linux Commands

Basic Vi Commands

### Revision History

1.0

04-Apr-2023

Initial Release

### Contributed by Cisco Engineers

Jefferson Andres Madriz Castro

TAC

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 04-Apr-2023 | Initial Release |