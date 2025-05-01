# Input distance
distance = int(input("How many kms is you house from school: "))
# Input if they walk to school yes/no
is_walk_input = input("Do you walk to school? (yes/no): ")
# Put into lowercase and compare
is_walk_input = is_walk_input.lower() == "no"
# if further than 5kms
if is_walk_input:
    if distance <= 5:
        print("you should walk")
    else:
        print("That is long")
# If do walk
else:
    print("That is a short distance")