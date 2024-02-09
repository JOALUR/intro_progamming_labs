#option 1
def option_one():
    print("Try these 10 ways to cut 500 calories every day: ")
    print(" * Swap your snack.")
    print(" * Cut one high-calorie treat.")
    print(" * DO NOT drink your calories.")
    print(" * Make low-calorie subsitutions.")
    print(" * Ask for a doggie bag.")
    print(" * Just say 'no' to fried food.")
    print(" * Build a thinner pizza.")
    print(" * Use a smaller plate.")
    print(" * Avoid alchohol.")
    print("Sourse: US National Library of Medicine.\n")
    
#option 2
def option_two():
    try:
        #user start weight
        start_weight = float(input("Please enter starting weight in pound (>=100): "))
        
        if start_weight < 100:
            print("Error: Weight must be at least 100 pounds.")
            return

        #month/weight display
        print("-------------------")
        print("Month     Weight")
        print("-------------------")
        
        #months 1-6
        for month in range(1,7):
            expected_weight = start_weight - (month * 4)
            print(f"  {month}      {expected_weight} lb.")
            
    except ValueError:
        print("Error: Invalid input. Please enter a valid weight")
        
    print()

#beginning display and options    
while True:
    print("500 Less a Day Makes the Weight Go Away...")
    print("\nChoose one of the following options:")
    print("    1. Display '10 ways to cut 500 calories' guidline.")
    print("    2. Generate next semester expected weight table.")
    print("    3. Quit")
    
    try: 
        user_choice = int(input("Option: "))
        
        if user_choice == 1:
            option_one()
        elif user_choice == 2:
            option_two()
        elif user_choice == 3:
            print("Good Bye!\n")
            break
        else:
            print("Error: Invalid choice. Please select a valid option.")
            
        
    except ValueError:
        print("Error: Invalid input. Please enter a valid choice.\n")
        
    

    
    





    
    
        
