import turtle
import pandas
import textturtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
text_man = textturtle.Text()

game_is_on = True
counter = 0
state_list = []
game_title = "Guess the State"
while game_is_on:
    answer_state = screen.textinput(title=game_title, prompt="What's another state's name?").title()
    data = pandas.read_csv("50_states.csv")
    # print(answer_state)
    if answer_state in data["state"].values and not answer_state in state_list:
        # print(data[data.state == answer_state])
        state_list.append(answer_state)
        counter += 1
        game_title = f"{counter}/50 States Correct"
        df = data.set_index("state")
        # print(df.loc[answer_state, "x"])
        text_man.write_text(answer_state, df.loc[answer_state, "x"], df.loc[answer_state, "y"])
        if counter == 50:
            game_is_on = False
    else:
        print("OOPS try again")
    if answer_state == "Exit":
        missing_states = [state for state in data.state.to_list() if state not in state_list ]
        # for state in data.state.to_list():
        #     if state not in state_list:
        #         missing_states.append(state)
        #
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break





