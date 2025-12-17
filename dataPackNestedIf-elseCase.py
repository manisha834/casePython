# Write a Python program using only if, elif, and nested if-else statements (no loops allowed).
# Create a menu-based program for NTC Data Packs.
# MAIN MENU
# 1) All Time Data Pack
# 2) Recurring Pack
# 3) SMS Pack
# 4) Unlimited Facebook / YouTube Pack
# Task Requirements:
# 1.Display the main menu.
# 2.Ask the user to enter a choice (1–4).
# 3.Based on the selected option, display the corresponding sub-menu:

# If the user selects 1 → All Time Data Pack
# 1) 1GB @ Rs 30 - 1 Day
# 2) 4GB @ Rs 99 - 1 Day
# 3) 5GB @ Rs 109 - 7 Days
# 4) 12GB @ Rs 199 - 7 Days
# If the user selects 2 → Recurring Pack
# 1) 700MB / Day @ Rs 299 – 28 Daysoption
# 2) 1.5GB / Day @ Rs 599 -28 Days
# If the user selects 3 → SMS Pack
# 1) 200 SMS @ Rs 35 - 1 Day
# 2) 200 SMS @ Rs 60 - 7 Days
# 3) 500MB @ Rs 150 - 28 Days
# If the user selects 4 → Unlimited Facebook / YouTube Pack
# 1) Unlimited Facebook @ Rs 55 - 3 Days
# 2) Unlimited YouTube @ Rs 55 - 3 Days

# 4.After showing the sub-menu, ask the user to select an offer number.
# 5.If the selected offer is an MB pack, display:
# MB Pack is selected
# 6.If the selected offer is from the Unlimited Facebook / YouTube Pack, display:
# This offer is selected
# 7.If the user enters an invalid main choice or sub-choice, display:
# Invalid choice

print("1) All Time Data Pack\n","2) Recurring Pack\n","3) SMS Pack\n","4) Unlimited Facebook/Youtube Pack\n")
choice=int(input("Enter your choice from 1 to 4"))
if choice==1:
    print("1) 1GB @ Rs 30 - 1 Day\n","2) 4GB @ Rs 99 - 1 Day\n","3) 5GB @ Rs 109 - 7 Days\n","4) 12GB @ Rs 199 - 7 Days\n")
    option=int(input("Enter the option from 1 to 4"))
    if option==1:
        print("1GB pack for 1 day is selected")
    elif option==2:
        print("4GB pack for 1 day is selected")
    elif option==3:
        print("5GB data pack for 7 days is selected")    
    elif option==4:
        print("12GB data pack for 7 days is selected")   
    else:
        print("Invalid choice")  
elif choice==2:
    print("1) 700MB /Day @ Rs 299- 28 days option\n","2) 1.5GB /Day @ Rs 599 - 28 Days\n")
    option=int(input("Enter the option from 1 to 2"))
    if option==1:
        print("700MB data pack for 28 days is selected")
    elif option==2:
        print("1.5GB pack for 28 days is selected")
    else:
        print("Invalid choice")
elif choice==3:
    print("1) 200SMS @ Rs 35 - 1 Day\n","2) 200SMS @ Rs 60 - 7Days\n","3) 500MB @ Rs 150 - 28 Days\n")
    option=int(input("Enter the option from 1 to 3"))
    if option==1:
        print("200SMS data pack for 1 day is selected")
    elif option==2:
        print("200SMS data pack for 7 days is selected")
    elif option==3:
        print("500MB data pack for 28 days is selected")    
    else:
        print("Invalid choice")   
elif choice==4:
    print("1) Unlimited Facebook @ Rs 55 - 3 days\n","2) Unlimited Youtube @ Rs 55 - 3 days\n")
    option=int(input("Enter the option from 1 to 2"))
    if option==1:
        print("Unlimited Facebook data pack for 3 days is selected")
    elif option==2:
        print("Unlimited Youtube data pack for 3 days is selected")
    else:
        print("Invalid choice")  
else:
    print("Invalid Choice")                           