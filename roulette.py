print("Roulette Wheel Colors App ...")
#roulette wheel color wording



while True:
    try:
        roulette = int(input("Please enter pocket number (0-36): "))
        #roulette variable
        
        if 0 <= roulette <= 36:    
    
            if roulette == 0:
                print("The Color of the Wheel Pocket is Green")
            
    
            elif 1 <= roulette <= 10:
        
                if roulette % 2 == 0:
                    print("The Color of the Wheel Pocket is Black") 
                else:
                    print("The Color of the Wheel Pocket is Red")
        
    
            elif 11 <= roulette <= 18:
                if roulette % 2 == 0:
                    print("The Color of the Wheel Pocket is Red")
                else:
                    print("The Color of the Wheel Pocket is Black")
        
        
            elif 19 <= roulette <= 28:
                if roulette % 2 ==0:
                    print("The Color of the Wheel Pocket is Black")
                else:
                    print("The Color of the Wheel Pocket is Red")
        
            elif 29 <= roulette <= 36:
                if roulette % 2 == 0:
                    print("The Color of the Wheel Pocket is Red")
                else:
                    print("The Color of the Wheel Pocket is Black")
                    
            break #exits loop when numbers valid
         
        else:
            print("Error ... Invalid Pocket. Try Again! Enter a number (0-36).")
            
            
    except ValueError:
        print("Error ... Invalid Pocket. Pick a number (0-36).")
    
                
