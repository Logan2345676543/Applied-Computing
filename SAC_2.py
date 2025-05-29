#starting count at 0
attendence_amount = 0
#ask how may students in the class
students = int(input("Enter the amount of students in the class? "))
#ask how many periods during the week
periods = int(input("Enter total number of periods held in the week (1 to 5): "))
#ensuring that it is between 1 and 5
while periods <1 or periods >5:
    periods = int(input("Please eneter a number between 1 and 5: "))
    
#going through each student    
for i in range(students):
    name = input(f"\nEnter name for student {i + 1}: ")
    attendence_amount = 0
    attendence_record = ""
#each students attendence
    for j in range(periods):
        attendence = input(f"Enter attendence for {name}, P/A for period {j + 1}: ").upper()
        if attendence == "P":
            attendence_amount += 1
        attendence_record += attendence
#working out percentage       
        percentage = (attendence_amount / periods)*100
#Show how many times they were present
        print(f"{name}: {attendence_amount} periods present ({percentage:.0f}%)", end="")
    if percentage < 75:
        print(" - Warning low attendence")
    else:
        print()
   
print("\nData written to file.")