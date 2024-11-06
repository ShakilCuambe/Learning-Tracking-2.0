from turtle import Screen, Turtle
import pandas
screen = Screen()
turtle = Turtle()
screen.title("50 statess")
image = "blank_states_img.gif"
screen.addshape(image)
# choice = screen.textinput(title="Guess the US state", prompt="Whats another state name??").title()
turtle.shape(image)
count = 0

data = pandas.read_csv("50_states.csv")
# dict = data.to_dict(orient='list')
states = data["state"].to_list()
states_copy = states
# print(states)
x_cords = data["x"].to_list()
y_cords = data["y"].to_list()
certos_list = []
error_list = []
game_on = True


def complete_the_challenge(state, x_cor, y_cor):
    timmy = Turtle()
    timmy.hideturtle()
    timmy.penup()
    timmy.speed("fastest")
    timmy.goto(x=x_cor, y=y_cor)  # Move the score display to the top
    # timmy.hideturtle()
    # timmy.clear()

    timmy.write(arg=state, move=False, align="center", font=('Arial', 12, 'normal'))

while len(certos_list) < 50:
    choice = screen.textinput(title=f"{len(certos_list)}/50 correct",
                              prompt="Whats another state name??").title()
    state_data = data[data["state"] == choice]

    if choice == "Exit":
        break

    if choice in states:
        state_data = data[data["state"] == choice]
        # count += 1
        certos_list.append(choice)
        complete_the_challenge(choice, state_data.x.item(), state_data.y.item())
    #  
        states.remove(choice)   

for x in states_copy:
    if x not in certos_list:
        error_list.append(x)

error = pandas.DataFrame(error_list)
error.to_csv("errors_dados.csv")

screen.mainloop()
