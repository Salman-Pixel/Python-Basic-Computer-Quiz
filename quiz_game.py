print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    print("Aight mate! Goodbye...")
    quit()

    
print("Alright! Let's play :) ")
score = 0
questions = 0

answer = input("What does the CPU stand for? ").lower()
questions += 1
if answer == "central processing unit":
    print("Correct!")
    score += 3
else:
    print("Incorrect :|")
    
answer = input("What does the GPU stand for? ").lower()
questions += 1
if answer == "graphics processing unit":
    print("Correct!")
    score += 3
else:
    print("Incorrect :|")
    
answer = input("What does IBM stand for? ").lower()
questions += 1
if answer == "international business machine":
    print("Correct!")
    score += 5
else:
    print("Incorrect :|")
    
answer = input("What does the RAM stand for? ").lower()
questions += 1
if answer == "random access memory":
    print("Correct!")
    score += 2
else:
    print("Incorrect :|")
    
answer = input("What does the ROM stand for? ").lower()
questions += 1
if answer == "read only memory":
    print("Correct!")
    score += 2
else:
    print("Incorrect :|")
    
print(f"You got {score} out of {questions} questions correct!")
print(f"Your percentage is {(score/questions * 100)}%")

