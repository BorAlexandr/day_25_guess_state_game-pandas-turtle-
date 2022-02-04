import pandas
import turtle
from inscription import Inscriptions

screen = turtle.Screen()
screen.title("U.S. States Game")

top_image = "blank_states_img.gif"
screen.addshape(top_image)
turtle.shape(top_image)

data_states = pandas.read_csv("50_states.csv")

current_states = []


# user_answer = screen.textinput(title=f"{len(current_states)}/50 states correct",
#                                prompt="What's another state's name").title()


while len(current_states) < 50:
    user_answer = screen.textinput(title=f"{len(current_states)}/50 states correct",
                                   prompt="What's another state's name").title()
    if user_answer == "Exit":
        break
    elif user_answer in data_states["state"].to_list():
        x, y = data_states[data_states.state == user_answer].x, data_states[data_states.state == user_answer].y
        inscription = Inscriptions(user_answer, x, y)
        current_states.append(user_answer)


all_states = set(data_states["state"].to_list())
all_states.difference_update(set(current_states))

not_guessed_state = pandas.DataFrame(all_states, columns=["state"]).to_csv("not_guessed_state.csv")












