attendence_amount = 0
students = int(input("Enter the amount of students in the class? "))
periods = int(input("Enter total number of periods held in the week (1 to 5): "))
while periods <1 or periods >5:
    periods = int(input("Please eneter a number between 1 and 5: "))
    
for i in range(students):
    name = input(f"Enter name for student {i + 1}: ")
    for j in range(periods):
        attendence = input(f"Enter attendence for {name}, P/A for period {j + 1}: ")
print("Attendance report:")
if attendence == "P":
    attendence_amount 
print(attendence_amount)