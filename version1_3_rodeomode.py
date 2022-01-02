#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time

from random import randint

from math import sqrt

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
ll=Motor(Port.A)
mm=Motor(Port.B)
rr=Motor(Port.C)
auto=TouchSensor(Port.S1)

def time_ms():
    fds=time.time()
    return int(fds*1000)

# Write your program here.

#Begrüßung
ev3.screen.draw_text(x=10, y=10, text="Willkommen! Du willst spielen? Dann bist du hier genau richtig! Drücke den Mittleren Knopf, um fortzufahren. ")
while not (Button.CENTER in ev3.buttons.pressed()):
            pass

print("Teil 1 ist erfolgreich abgelaufen. ")


#Menü
ev3.screen.clear()
emph=0
emphy=0
i=0
wait(1000)
args=[[["Start", "Anleitung >>", "Modus >>", "Highscore >>", "Credits >>"],
    ["Start", "Anleitung >>", "Modus >>", "Highscore >>", "Credits >>"],
    ["Start", "Anleitung >>", "Modus >>", "Highscore >>", "Credits >>"],
    ["Start", "Anleitung >>", "Modus >>", "Highscore >>", "Credits >>"],
    ["Start", "Anleitung >>", "Modus >>", "Highscore >>", "Credits >>"]],
    
    [["", "", "", "", "", ""],
    ["Bei diesem Spiel geht es darum, mit dem Auto möglichst lange den Hindernissen auszuweichen.",
    "Das alleine wäre ja langweilig, doch währrend dem Spiel verändert sich deine Geschwindigkeit!",
    "Mit der Zeit wechselt die Geschwindigkeit öfter, schneller und zufälliger!",
    "Durch einen Druck auf die Mittlere Bricktaste kannst du das Spiel unterbrechen, durch einen zweiten Druck beenden.",
    "Lenken kannst du mit dem Lenkrad, aber jetzt viel Spass dir!"],
    ["Unendlichmodus", "Level 1", "Level 2", "Level 3", "level 4"],
    ["", "", "", "", "", "", "", "", "", "", ""],
    ["Robotik-F Wirsberg-Gymnasium", "Erich, Leander, David", "Moritz, Luca, Johannes", "Herr Keßelring"]]]
while not (Button.CENTER in ev3.buttons.pressed()):
    for i in range(0, len(args[emphy])):
        print("emph= " +str(emph) + "  emphy= " +str(emphy) + "  i= " +str(i))
        if emph==i:
            ev3.screen.draw_text(x=40, y=10+23*i, text=args[emphy][emph][i], text_color=Color.WHITE, background_color=Color.BLACK)
        else:
            ev3.screen.draw_text(x=40, y=10+23*i, text=args[emphy][emph][i], text_color=Color.BLACK, background_color=Color.WHITE)
        i=(1+i)%len(args[emphy][emph])
    print()
    while not ((Button.RIGHT in ev3.buttons.pressed()) or (Button.LEFT in ev3.buttons.pressed()) or (Button.UP in ev3.buttons.pressed()) or (Button.DOWN in ev3.buttons.pressed()) or (Button.CENTER in ev3.buttons.pressed())):
        pass
    if (Button.DOWN in ev3.buttons.pressed()):
        emph=(emph+1)%len(args[emphy])
        wait(200)
        ev3.screen.clear()
        continue
    elif (Button.UP in ev3.buttons.pressed()):
        emph=(emph-1)%len(args[emphy])
        wait(200)
        ev3.screen.clear()
        continue
    elif (Button.RIGHT in ev3.buttons.pressed()):
        emphy=(emphy+1)%2
        wait(200)
        emph=0
        i=0
        ev3.screen.clear()
        continue
    elif (Button.LEFT in ev3.buttons.pressed()):
        emphy=(emphy-1)%2
        wait(200)
        emph=0
        i=0
        ev3.screen.clear()
        continue
    ev3.screen.clear()

nn=time_ms()
ev3.speaker.beep()
startv=-200
## Die Durchschnittsgeschwindigkeit d ist die Wurzel der Zeit plus 200, die seit nn verstrichen ist.
## ges=(l, m, r) soll das Geschwindigkeitstupel sein; l=randint(1, d), m=randint(d/2, 2d), r=(d-(l+m)/3)*3
d=200
ges=[startv, startv, startv]
timetoreset=randint(1, 5)
#Hauptprogramm
break_=False
run_=True
while run_==True:
    while break_==False:
        ll.run(int(ges[randint(0, 1)]))
        mm.run(int(ges[randint(0, 2)]))
        rr.run(int(ges[randint(1, 2)]))
        foo=int(time_ms()-nn)
        ev3.screen.print(str(foo))
        wait(10)
        ev3.screen.clear()
        if auto.pressed()==True:
            run_=False
            break_=True
            ll.hold()
            mm.hold()
            rr.hold()
        while int(time_ms()-nn)%timetoreset!=0:
            pass
        d=int(sqrt(int(time_ms()-nn)))+200
        ges[0]=randint(1, int(d))
        ges[1]=randint(int(d/2), int(2*d))
        ges[2]=(int(d)-(int(ges[0])+int(ges[1]))/3)*3
        timetoreset=randint(1, 5)

#Programmende
ev3.screen.print("Du hast verloren! Das Auto ist gegen ein Hindernis gedonnert...")
ev3.speaker.say("I say it just because Master Johannes wants so")
wait(1000)