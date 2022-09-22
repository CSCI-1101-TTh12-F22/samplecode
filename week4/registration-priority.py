year = int(input("What year will you graduate? "))
major = input("Are you a CS major? ")

# seniors = 2023
# juniors = 2024
# soph = 2025
# freshman = 2026

###priority = -1
##if year == 2023 and major=="yes":
##    priority = 1
##elif year == 2024 and major == "yes":
##    priority = 2
##elif year == 2023:
##    priority = 3
##elif year == 2025 and major == "yes":
##    priority = 4
##elif year == 2024:
##    priority = 5
##else:
##    priority = 6
##
##print(f'Your priority is {priority}!')
##

priority = -1
if year == 2023:
    if major == "yes":
        priority = 1
    else:
        priority = 3
elif year == 2024:
    if major == "yes":
        priority = 2
    else:
        priority = 5
elif year == 2025:
    if major == "yes":
        priority = 4
    else:
        priority = 6
else:
    priority = 6

print(priority)


    
