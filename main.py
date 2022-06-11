from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.bgpic('blank_states_img.gif')

# game_is_on = True

states_df = pandas.read_csv('50_states.csv')
correct = 0
guessed = []


def end_game():
    states_not_guessed = []
    for state in states_df["state"].tolist():
        if state not in guessed:
            states_not_guessed.append(state)

    states_not_guessed_df = pandas.DataFrame({"States": states_not_guessed})
    states_not_guessed_df.to_csv("states_to_learn.csv")


while correct < 50:
    user_input = screen.textinput(title=f"{correct}/50 States Correct", prompt="Whats' another state name?").title()
    if user_input == "Exit":
        end_game()
        break

    if user_input in guessed:
        continue

    guessed.append(user_input)
    input_df = states_df[states_df["state"] == user_input]
    if not input_df.empty:
        correct += 1
        x_axis = input_df.x.item()
        y_axis = input_df.y.item()
        write = Turtle()
        write.hideturtle()
        write.penup()
        write.goto(x=x_axis, y=y_axis)
        write.write(user_input)
