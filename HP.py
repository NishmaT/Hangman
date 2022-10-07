import random
import turtle
import time

print("Hi,Welcome to Game")
name = input("Enter your name:")
print("Hello " + name + "! Best of Luck!")
time.sleep(3)
print("Let's start...")
words= ['happy','joy','rainbow','blue','water','smile','game','plant','funny']
selected_word=random.choice(words)
print("Its a",len(selected_word),"letter word " )
guesses=[]
for i in range(0,len(selected_word)):
    guesses.append("__")
print(guesses)
wrong_guesses=0
correct_guesses=0
t = turtle.Turtle()
t.penup()
t.goto((0,0))
t.penup()
t.goto((0,100))
t.pendown()
t.goto((0,125))
t.goto((75,125))
t.goto((75,-100))
t.penup()
t.goto((0,0))
while wrong_guesses<6 and "__" in guesses:
    letter=input("Enter a letter: ")
    if letter in selected_word:
        res = [i for i in range(len(selected_word)) if selected_word.startswith(letter, i)]
        for k in res:
            guesses[k]=letter
        print(guesses)
    else:
        print("You guessed it wrong!")
        wrong_guesses=wrong_guesses+1
        if wrong_guesses==1:
            t.pendown()
            r = 50
            t.circle(r)
            
        elif wrong_guesses==2:
            x=(0,-50)
            t.pendown()
            t.goto(x)
        elif wrong_guesses==3:
            x=(0,-50)
            t.goto((-25,-75))
            t.goto(x)
        elif wrong_guesses==4:
            x=(0,-50)
            t.goto((25,-75))
            t.goto(x)
        elif wrong_guesses==5:
            t.goto((0,-25))
            t.goto((25,-15))
        else:
            t.goto((0,-25))
            t.goto((-25,-15))
            t.hideturtle()
            
print("The word is ",selected_word,"!")