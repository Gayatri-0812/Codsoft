print("Welcome to the python quiz!")
print("RULE NO. 1: +1 for correct answer")
print("RULE NO. 2: PASSING MARKS(50% OR 5 CORRECT QUESTIONS)")
name = input("What is your name? ")
playing = input( name  + " do you want to play the quiz?(yes/no) ")
score = 0



if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play")

answer = input("Who Painted Monalisa? ")
if answer.lower() == "Leonardo da Vinci":
    print("Correct!")
    score += 1 
    
else:
    print("Incorrect!")
    

answer = input("What is the correct extension for python file? ")
if answer.lower() == ".py":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")
    

answer = input("Which animal is known as the 'Ship of the Dessert'? ")
if answer == "Camel":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")
  
    
answer = input("Which character is used to give single-line comments in python? ")
if answer == "#":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")

answer = input("What is the capital of France? ")
if answer == "Paris":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")

answer = input("How many sides does a pentagon have? ")
if answer.lower() == "5":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")
    
answer = input("What is truncation division operator in python? ")
if answer == "//":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")
    
answer = input("Which is the most sensitive organ in our body? ")
if answer.lower() == "Skin":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")

answer = input("Name of the longest river in the world? ")
if answer == "Nile":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")
    
answer = input("What is the capital of Argentina? ")
if answer.lower() == "Buenos Aires":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")


    







print("Thank you for taking the quiz!")

if (score>=5):
    print("Congratulations! You have successfully passed the quiz.")
else:
    print("Better luck next time.")

print(name + " you got " + str(score) + "/10 questions correct." )
print("Accuracy: " + str((score/10) * 100) + " %")