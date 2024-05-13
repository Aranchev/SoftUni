while True:                             #! while True: creates an infinite loop that keeps taking user input
    a = float(input())                    
    
    if a < 0:
        print("Negative number!")   
        break  #? --------------------> Until...
    
    b = a * 2
    print(f"Result: {b:.2f}")