import re

# Function to validate SSN
def validateSSN(userString):
    mainRegex = "^(?!000|666|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0000)\\d{4}$"
    rgx = re.compile(mainRegex)
    
    if re.search(rgx, userString):
        return True
    else:
        return False
    
if __name__ == "__main__":
    validado = True
    print("Welcome to the SSN Validator!")
    
    while validado == True:
        # User input
        userInput = input("Insert the SSN: ")
        
        if len(userInput) == 11:
            result = validateSSN(userInput)
            
            # Validate SSN
            if result == True:
                print("The SSN is valid")
            else:
                print("The SSN is not valid")
            
        else:
            print("The SSN is not the correct. SSN total lenght is 11 (including hyphens)")
        
        # Ask if the user wants to validate another SSN
        ans = int(input("Do you want to validate another SSN? 0 = false; 1 = yes: "))
        
        if ans == 0:
            validado = False
        elif ans != 1:
            print("Insert a valid response")