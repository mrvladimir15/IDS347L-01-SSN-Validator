# SSN Validator User Manual

## How to use it?

### Starting the application
When the application is executed (as the [README.md](https://github.com/mrvladimir15/IDS347L-01-SSN-Validator/blob/main/README.md) file suggests), the program will show:
* The user's terminal will be shown.
* A welcome message to the user.
* Criteria for a valid SSN.
* Message asking for a input indicatig the SSN to validate.

### Using the application
In order to use the application, the main program will notify the user when to give it the SSN to validate (as the *Starting the application* section shows). When the message is displayed, all user has to do in enter the Social Security Number that he wants to validate via his keyboard.
> **QUICK REMINDER**: the Social Security Number is 555-55-5555. To learn more about the SSN format, check the [README.md](https://github.com/mrvladimir15/IDS347L-01-SSN-Validator/blob/main/README.md) file.  

### Showing the output and closing the application
The application shows in the console the result of the SSN. If the SSN is valid, the console will print "The SSN is valid"; in the opposite case, it will print "The SSN is not valid".  
> In case the **input exceeds 11 characters** (including separator {-}), the application will show "The SSN is too long".
Validated the SSN number, the program will ask the user if he wants to validate another SSN or not. Answer the question with '0' if you want to close the app; if you want to validate another SSN, then, answer with '1'.