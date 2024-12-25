import turtle
import pandas as pd

FONT = ("Arial", 8 , "bold")
GAME_OVER_FONT = ("Arial", 24 , "bold")
GAME_OVER_LIST_FONT = ("Arial", 18, "normal")

#Screen Commands
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Turtle Commands
t = turtle.Turtle()
t.hideturtle()
t.penup()

#Read csv file using pandas and convert them into a list of lowercase states
data = pd.read_csv("50_states.csv")
data_list = data["state"].to_list()

x_list = data["x"].to_list()
y_list = data["y"].to_list()

states_list = []
for country in data_list:
    lowercase = country.lower()
    states_list.append(lowercase)

#Start Game
game_is_on = True
score = 0
previous_answers = []

while game_is_on:

    #Prompts user for input, gives feedback for certain answers
    if score == 0:
        user_answer = screen.textinput(title="Guess the States!", prompt="Guess a state name?\nIf you do decide to give up type 'g' :)").lower()

    elif user_answer not in states_list and user_answer not in previous_answers and score != 0:
        user_answer = screen.textinput(title=f"{score}/50 States Correct", prompt="That is not a state, try again!").lower()

    else:
        user_answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").lower()

    #check for repeat guesses
    while user_answer in previous_answers:
        user_answer = screen.textinput(title=f"{score}/50 States Correct", prompt="You have already guessed that, try again!").lower()

    #Check if guess is among 50 guesses
    if user_answer in states_list:

        #Show answer on the map
        index = states_list.index(user_answer)
        t.goto(x_list[index], y_list[index])
        t.write(arg=user_answer, align="center", font=FONT)

        #Remove previous guesses
        states_list.remove(user_answer)
        x_list.remove(x_list[index])
        y_list.remove(y_list[index])

        #If guess is correct, add it into a list of correct previous guesses
        previous_answers.append(user_answer)

        #Increase score
        score += 1

    #Give up prompt
    if user_answer == "g":
        screen.clear()
        t.goto(0, 300)
        t.write(arg="GAME OVER", align="center", font=GAME_OVER_FONT)
        t.goto(0, 260)
        t.write(arg=f"Below is a list of states you didn't manage to guess", align="center", font=GAME_OVER_LIST_FONT)
        t.goto(0, 180)
        t.write(arg=f"{states_list[0:15]}\n{states_list[15:30]}\n{states_list[30:45]}\n{states_list[45:50]}", align="center", font=("Arial", 10, "normal"))
        game_is_on = False

    #win condition
    if score == 50:
        screen.clear()
        t.goto(0, 300)
        t.write(arg="YOU GUESSED ALL THE STATES! GOOD JOB!", align="center", font=GAME_OVER_FONT)
        game_is_on = False

screen.exitonclick()