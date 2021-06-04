
def ui_level():
    while True:
        level=input("give me a level (easy,normal):\n").lower()
        if level=="easy" or level=="normal" or level=="hard":
            return level
            False
        else:
            pass

def ui_print(map):
    for row in map:
        for column in row:
            print(column, end='')

        print("")
    print("            new")


def ui_shap(shape):
    for row in shape:
        print(row)

def ui_msg_lost(pill,time):
    print("Pacman died!")
    print("your pills are",pill,"and your time is",time)
def ui_msg_win(pill,time):
    print("You won the game!")
    print("your pills are", pill,"and your time is",time)
def ui_msg_hit(pill,time):
    print("Pacman hited!")
    print("your pills are", pill,"and your time is",time)