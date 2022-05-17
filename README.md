# IDS347L-01-SSN-Validator
 
## Generals
### Description
This application has, as general purpose, validate whether a Social Security Number (SSN) number is or not valid, according to the following criteria:
* It should have 9 digits.
* It should be divided into 3 parts by hyphen (-).  
    * The first part should have 3 digits and should not be 000, 666, or between 900 and 999.
    * The second part should have 2 digits and it should be from 01 to 99.
    * The third part should have 4 digits and it should be from 0001 to 9999.

## Project documentation
 * [User manual](https://github.com/mrvladimir15/IDS347L-01-SSN-Validator/blob/main/docs/user-manual.md). Redirects to the user manual, where a detailed use description can be found, indicating how to operate the application and how this last will answer to the user.
 * [Test Plan](https://github.com/mrvladimir15/IDS347L-01-SSN-Validator/blob/main/docs/Test-Plan.md). Redirects to the application's test plan, a document that indicates how will be the path to test the whole application and confirm that it accomplishes the given requirements.

## Required software
To run the application and execute the test cases using PyTest there is some software required:  
### PYTHON 3.9:
1. Open the terminal. 
2. In the terminal, type:
    > $ sudo apt install python 3.9
3. Verify the installation by typing this in the terminal:
    > python 3.9 --version

### PYTEST:
1. Open the terminal.
2. In the terminal, type:
    > pip install -U pytest
3. Verify that the installation is correct by checking that we have installed the latest version.
    > $ pytest --version


## How to install
In order to install the application in Ubuntu, follow the next steps:  
1. Open the terminal.  
2. In the terminal, type:
    > ./{installing root} $ git clone https://github.com/mrvladimir15/IDS347L-01-SSN-Validator

## How to run
To run the application:
1. Open the terminal.
2. Place the project installation directory in the console.
3. In the console, type:
    > python SSNValidator.py