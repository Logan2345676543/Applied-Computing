import random
answer1 = ("Absolutely!")
answer2 = ("No way Pedro!")
answer3 = ("Go for it tiger.")
answer4 = ("ion know bro.")
answer5 = ("Do it, you wont.")
print("Welcome to the Magic 8 ball game-use it to answer your questions...")
question = input("Ask me for any advice and I'll help you out. Type in your question and then press enter for an answer. ")
print("shaking... \n" *4)
choice = random.randint(1,5)
if choice == 1:
           answer=answer1
elif choice == 2:
           answer=answer2
elif choice == 3:
           answer=answer4
elif choice == 4:
           answer=answer5
else:
           answer=answer3
print(answer)