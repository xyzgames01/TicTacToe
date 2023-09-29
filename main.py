from guizero import *
import emoji

app = App(title='Tic Tac Toe', height=380, width=295, layout="grid")

x_text = "X"
o_text = "O"
n_text = ""

x_emoji_text = emoji.emojize(':cold_sweat:')
O_emoji_text = emoji.emojize(':O:')

x_turn_text = "It's X's Turn"
o_turn_text = "It's O's Turn"

x_win_text = "X Wins!"
o_win_text = "O Wins!"

game_won = False

player_turn = False

game_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def turn(button_number):
    global player_turn
    button_list[button_number].enabled = False
    if player_turn:
        button_list[button_number].text = o_text
        player_turn = False
        game_list.remove(button_number)
        game_list.insert(button_number, o_text)
    else:
        button_list[button_number].text = x_text
        player_turn = True
        game_list.remove(button_number)
        game_list.insert(button_number, x_text)
    CheckForWin()


def CheckForWin():
    global x_win_text
    global o_win_text
    global game_won

    for i in range(3):
        i = i * 3
        if game_list[i] == x_text:
            if game_list[i + 1] == x_text:
                if game_list[i + 2] == x_text:
                    print("X wins HORIZONTALLY")
                    game_won = True
                    Win(x_win_text)
                    break
        if game_list[i] == o_text:
            if game_list[i + 1] == o_text:
                if game_list[i + 2] == o_text:
                    print("o wins HORIZONTALLY")
                    game_won = True
                    Win(o_win_text)
                    break
    for i in range(3):
        if game_list[i] == x_text:
            if game_list[i + 3] == x_text:
                if game_list[i + 6] == x_text:
                    print("X wins VERTICALLY")
                    game_won = True
                    Win(x_win_text)
                    break
        if game_list[i] == o_text:
            if game_list[i + 3] == o_text:
                if game_list[i + 6] == o_text:
                    print("o wins VERTICALLY")
                    game_won = True
                    Win(o_win_text)
                    break
    for i in range(1):
        if game_list[i] == x_text:
            if game_list[i + 4] == x_text:
                if game_list[i + 8] == x_text:
                    print("X wins DIAGONALLY LEFT")
                    game_won = True
                    Win(x_win_text)
                    break
        if game_list[i] == o_text:
            if game_list[i + 4] == o_text:
                if game_list[i + 8] == o_text:
                    print("o wins DIAGONALLY LEFT")
                    game_won = True
                    Win(o_win_text)
                    break
        if game_list[i + 2] == x_text:
            if game_list[i + 4] == x_text:
                if game_list[i + 6] == x_text:
                    print("X wins DIAGONALLY RIGHT")
                    game_won = True
                    Win(x_win_text)
                    break
        if game_list[i + 2] == o_text:
            if game_list[i + 4] == o_text:
                if game_list[i + 6] == o_text:
                    print("o wins DIAGONALLY RIGHT")
                    game_won = True
                    Win(o_win_text)
                    break
    for i in range(9):
        if game_list[i] == "O" or game_list[i] == "X":
            if game_won is False and i == 8:
                Win("Tie")
        else:
            break


def Win(player):
    global game_text
    for i in button_list:
        i.enabled = False
    game_text.value = player


def ResetGame():
    global game_list
    global player_turn
    global game_text
    global game_won
    game_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player_turn = False
    game_won = False
    game_text.value = x_turn_text
    for i in button_list:
        i.enabled = True
        i.text = n_text


button1 = PushButton(app, text=n_text, align="left", grid=[0, 0], width=10, height=4, command=turn, args=[0])
button2 = PushButton(app, text=n_text, align="left", grid=[1, 0], width=10, height=4, command=turn, args=[1])
button3 = PushButton(app, text=n_text, align="left", grid=[2, 0], width=10, height=4, command=turn, args=[2])
button4 = PushButton(app, text=n_text, align="left", grid=[0, 1], width=10, height=4, command=turn, args=[3])
button5 = PushButton(app, text=n_text, align="left", grid=[1, 1], width=10, height=4, command=turn, args=[4])
button6 = PushButton(app, text=n_text, align="left", grid=[2, 1], width=10, height=4, command=turn, args=[5])
button7 = PushButton(app, text=n_text, align="left", grid=[0, 2], width=10, height=4, command=turn, args=[6])
button8 = PushButton(app, text=n_text, align="left", grid=[1, 2], width=10, height=4, command=turn, args=[7])
button9 = PushButton(app, text=n_text, align="left", grid=[2, 2], width=10, height=4, command=turn, args=[8])

reset_button = PushButton(app, text="Reset", align="left", grid=[1, 3], width=10, height=4, command=ResetGame)

game_text = Text(app, text=x_turn_text, grid=[1, 4])

button_list = [button1, button2, button3, button4, button5, button6, button7, button8, button9]


def main():
    app.display()


if __name__ == '__main__':
    main()
