import turtle
import pandas
screen = turtle.Screen()
screen.title("US State Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = list(data.state)
guessed_state = []
score = 0
missing_state = []
while guessed_state != 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another States Name ").title()
    if answer_state == "Exit":
        for state in state_list:
            if state not in guessed_state:
                missing_state.append(state)
        data_missing_state = pandas.DataFrame(missing_state)
        data_missing_state.to_csv("Missing States.csv")
        break
    if answer_state in state_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        score += 1
