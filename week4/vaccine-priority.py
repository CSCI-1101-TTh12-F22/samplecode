
## Option #1: Ask all questions in advance
## then use and and or operators

healthcare = input("Are you a healthcare worker? y or n ")
covidface = input("Are you a covid facing? y or n ")
assistedliving = input("Do you live in an assisted living facility? y or n ")
age = int(input("What is your age? "))
comorbidity = int(input("How many comorbidities do you have? "))
essential = input("Are you an essential worker? y or n ")

phase = -1
if (healthcare == "y" and covidface == "y") or (age > 65 and assistedliving == "y"):
    phase = 1
elif age > 75 or (healthcare == "y" and covidface == "n"):
    phase = 2
elif age > 65 or comorbidity == 2 or (essential == "y" and comorbidity == 1):
    phase = 3
else:
    phase = 4

print("You are in phase {}".format(phase))


## Option #2: Have nested if statements.
## Only ask questions if you need to know the answer!
phase = -1
healthcare = input("Are you a healthcase worker? (y or n) ")
if healthcare == "y":
    covidfacing = input("Are you covid facing? (y or n) " )
    if covidfacing == "y":
        phase = 1
    else:
        phase = 2
else:
    age = int(input("What is your age? "))
    if age > 75:
        assistedliving = input("Do you live in assisted living? ")
        if assistedliving == "y":
            phase = 1
        else:
            phase = 2
    elif age > 65:
        assistedliving = input("Do you live in assisted living? ")
        if assistedliving == "y":
            phase = 1
        else:
            phase = 3
    else:
        comorb = int(input("How many comorbidities do you have? "))
        if comorb >= 2:
            phase = 3
        elif comorb == 1:
            essential = input("Are you an essential worker? ")
            if essential == "y":
                phase = 3
            else:
                phase = 4

print("You are in phase {}".format(phase))

                     

        
            
            
        
            










    
