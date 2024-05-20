# Phone Number Cleanup Script
This is a Python script written for cleaning up clients' phone numbers. The CSV file has been extracted from the database, which contains the clients' phone numbers. It checks for the correct number of digits in the phone number columns and flags entries that do not have exactly 10 digits. It performs the following steps:

## Define the Columns:

The script assumes there are three phone number columns named Phone (1) (Cleaned), Phone (2) (Cleaned), and Phone (3) (Cleaned).

## Load the CSV File:

The script loads the CSV file into a Pandas DataFrame. The file is assumed to be named Phone_Numbers.csv.

## Add a New Column:

A new column, Number Of Digits, is created in the DataFrame and initialized with 0.

## Check Phone Number Columns:

The script iterates through the phone number columns and counts the number of digits in each cell.
If a cell contains a phone number with less or more than 10 digits, the corresponding entry in the Number Of Digits column is set to 1.

## Save the Updated DataFrame:

The script saves the updated DataFrame back to a new CSV file named Checked_Phone_Numbers.csv.
