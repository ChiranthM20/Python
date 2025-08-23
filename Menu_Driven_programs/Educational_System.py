print("\n***Educational System***")

print("\n1. Add student details\n2. Display student details\n3. Exit")

student = {}

while(True):
    
    choice = int(input("\nEnter your choice : "))
    

    if choice == 1:
        name = input("\nEnter student's name : ")
        age = int(input("\nEnter student's age : "))
        student[name]=age
        print(f"\n{name} is {age} years old")
    
    elif choice == 2:
        if not student:
            print("\nNo student details available")
        else:
            print("\n--- Student Details ---")
            for name, age in student.items():
                print(f"Name: {name}, Age: {age}")
            
    
    elif choice == 3:
        print("\nExitting...")
        break

    else:
        print("\nInvalid choice! Please try again")

          
          
          

        
        
         