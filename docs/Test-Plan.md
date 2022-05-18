# SSN Validator Test Plan

## Requirements
The application must validate that the Social Security Number accomplishes with these points:
* It should have 9 digits.
* It should be divided into 3 parts by hyphen (-).  
    * The first part should have 3 digits and should not be 000, 666, or between 900 and 999.
    * The second part should have 2 digits and it should be from 01 to 99.
    * The third part should have 4 digits and it should be from 0001 to 9999.
    
## Acceptance criteria:
* The application shows the user a SSN valid criteria.
* The application tells the user if the number given exceed 11 characters (including separators {-}).
* The application prints messages to the user to notify him of its current state.
* The application valides whether a SSN is or not valid.
* Validated a SSN, the application lets the user decide if he wants to validate another SSN.

## Test strategy
For this opportunity, we will be using the Pytest framework to do automated unit-testing, so the framework prints the result of the listed testcases. To exec the unit tests, all we have to do is:
1. Open a system terminal.
2. Change the directory to he project's.
3. Type this in the console:
    > pytest -v
4. Hit the enter key.

## Test cases
| Code         | Input     | Expected output |
|--------------|-----------|------------|
|TC1|456-98-8974|True
|TC2|000-89-7321|False
|TC3|456-78932-1|False
|TC4|676-44-0000|False
|TC5|666-88-8999|False
|TC6|906-88-8999|False
|TC7|667-00-8999|False
|TC8|766-81-8999|True
|TC9|676-44-8999|True