# SSN Validator Test Plan

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
|TC1|456-98-8974|The SSN is valid
|TC2|000-89-7321|The SSN is not valid
|TC3|456-78932-1|The SSN is not valid
|TC4|789546-987456-798|The SSN is too long.
|TC5|666-88-8999|The SSN is not valid
|TC6|906-88-8999|The SSN is not valid
|TC7|667-00-8999|The SSN is not valid
|TC8|766-881-8999|The SSN is valid
|TC9|676-44-8999|The SSN is valid
|TC10|676-44-0000|The SSN is not valid