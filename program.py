import random
import sys
sys.path.append('..')
from pacman import play, move_ghosts
from ui import ui_print, ui_msg_lost ,ui_level ,ui_msg_win ,ui_msg_hit ,ui_shap
import keyboard
import time
from apscheduler.schedulers.background import BackgroundScheduler

sys.path.append('..')
# Y -> our hero
# G -> ghosts
# P -> pills
# . -> empty spaces
# | and - -> walls
#Q -> ghosts on pills
shape=[" @ -> our hero",
       " G -> ghosts",
       " P -> pills",
       " . -> empty spaces",
       " | and - -> walls",
       " Q -> ghosts on pills"]
MAP = [
    "|--------------------------------|",
    "|....|G.......||..........|...P..|",
    "|..||.PP..P......|....|||.P...|..|",
    "|.|......|.P...|.........||......|",
    "|.......|...P................GG..|",
    "|...||....|.P..............|.....|",
    "|..G.G......@...|............||..|",
    "|..G.G....|.....|.............|..|",
    "|......||......GG.....||......|..|",
    "|--------------------------------|"
]

def update():
    global MAP
    map_new = []
    for line in MAP:
        line = line.replace("P", ".")
        line = line.replace("Q", "G")
        i=random.randint(1,len(line)-2)
        if line[i] ==".":
            line=line[:i]+"P"+line[i+1:]
        map_new.append(line)
    MAP = map_new
    return MAP
level= ui_level()
ui_shap(shape)
ui_print(MAP)
list1=[]
start_time=time.time()
sched = BackgroundScheduler()

sched.add_job(update, 'interval', seconds=10)
sched.start()

def pressed_keys(e):
    # every 10 seconds remove pills and insret new pills
    for key in keyboard._pressed_events.values():
        if key.name != "esc":
            valid_key, pacman_alive,pills = play(MAP, key.name)
            if pills:
                list1.append(1)
            if (not pacman_alive):
                end_time=time.time()
                ui_msg_lost(len(list1),end_time-start_time)
            else:
                pacman_was_hit = move_ghosts(MAP, level)
                if pacman_was_hit:
                    end_time=time.time()
                    ui_msg_hit(len(list1),end_time-start_time)
                else:
                    ui_print(MAP)


keyboard.hook(pressed_keys)  # it enables the hook
keyboard.wait('esc')  # it tells that wait until escape is pressed . when you press escape code will continue here.
sched.shutdown()
print('end of program')





