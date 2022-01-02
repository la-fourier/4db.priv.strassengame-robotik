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


# Objects (1)
ev3 = EV3Brick()
ll=Motor(Port.A)
mm=Motor(Port.B)
rr=Motor(Port.C)
auto=TouchSensor(Port.S1)


# Definitions (2)
def time_ms():
    fds=time.time()
    return int(fds*1000)
def showwait(texte=["", ""]):
    ev3.screen.clear()
    for text in texte:
        ev3.screen.print(text)
    while not (Button.CENTER in ev3.buttons.pressed()):
        pass
    wait(500)
def highscore():
    while not (Button.CENTER in ev3.buttons.pressed()):
        pass
    wait(500)
def output():
    while not (Button.CENTER in ev3.buttons.pressed()):
        pass
    wait(500)


# Begrüßung (3)
wait(500)
ev3.screen.draw_text(x=10, y=10, text="Willkommen! Du willst spielen? Dann bist du hier genau richtig! Drücke den Mittleren Knopf, um fortzufahren. ")
while not (Button.CENTER in ev3.buttons.pressed()):
    pass


# Menü (4)
emph=0
wait(500)
args=["Anleitung >>", "Credits >>", "Output >>", "Highscore >>"]
args_=[["Bei diesem Spiel geht es darum, mit dem Auto möglichst lange den Hindernissen auszuweichen.",
    "Das alleine wäre ja langweilig, doch währrend dem Spiel verändert sich deine Geschwindigkeit!",
    "Mit der Zeit wechselt die Geschwindigkeit öfter, schneller und zufälliger!",
    "Durch einen Druck auf die Mittlere Bricktaste kannst du das Spiel unterbrechen, durch einen zweiten Druck beenden.",
    "Lenken kannst du mit dem Lenkrad, aber jetzt viel Spass dir!"],
    [["Robotik-F Wirsberg-Gymnasium",
    "Erich, Leander, David",
    "Moritz, Luca, Johannes",
    "Herr Keßelring"]]]
while not (Button.CENTER in ev3.buttons.pressed()):
    ev3.screen.clear()
    for i in range(0, len(args)):
        if emph==i:
            ev3.screen.draw_text(x=30, y=5+23*i, text=args[i], text_color=Color.WHITE, background_color=Color.BLACK)
        else:
            ev3.screen.draw_text(x=30, y=5+23*i, text=args[i], text_color=Color.BLACK, background_color=Color.WHITE)
    while not ((Button.RIGHT in ev3.buttons.pressed()) or (Button.LEFT in ev3.buttons.pressed()) or (Button.UP in ev3.buttons.pressed()) or (Button.DOWN in ev3.buttons.pressed()) or (Button.CENTER in ev3.buttons.pressed())):
        pass
    if (Button.DOWN in ev3.buttons.pressed()):
        emph=(emph+1)%len(args)
        wait(500)
        ev3.screen.clear()
        continue
    elif (Button.UP in ev3.buttons.pressed()):
        emph=(emph-1)%len(args)
        wait(500)
        ev3.screen.clear()
        continue
    elif (Button.RIGHT in ev3.buttons.pressed()) or (Button.LEFT in ev3.buttons.pressed()):
        if (emph==0) or (emph==1):
            for a in args_[emph]:
                wait(500)
                if emph==0:
                    showwait(texte=[a])
                elif emph==1:
                    showwait(texte=a)
        elif emph==2:
            wait(500)
            output()
        elif emph==3:
            #Datei einlesen, in eine Liste namens highscore schreiben, schließen und alle anzeigen
            highscore=["1292", "1232"]
            wait(500)
            showwait(texte=highscore)
        continue
ev3.speaker.beep()
startv=-200
## Die Durchschnittsgeschwindigkeit d ist die Wurzel der Zeit plus 200, die seit nn verstrichen ist.
## ges=(l, m, r) soll das Geschwindigkeitstupel sein; l=randint(1, d), m=randint(d/2, 2d), r=(d-(l+m)/3)*3
d=200
ges=[startv, startv, startv]
timetoreset=randint(1, 5)


# Hauptprogramm (5)
wait(500)
run_=True
nn=time_ms()
while run_==True:
    ll.run(int(ges[randint(0, 1)]))
    mm.run(int(ges[randint(0, 2)]))
    rr.run(int(ges[randint(1, 2)]))
    foo=int(time_ms()-nn)
    if auto.pressed()==True:
        run_=False
        ll.hold()
        mm.hold()
        rr.hold()
    while int(time_ms()-nn)%timetoreset!=0:
        if (Button.CENTER in ev3.buttons.pressed()):
            b=time_ms()
            ll.hold()
            mm.hold()
            rr.hold()
            ev3.screen.clear()
            ev3.screen.print("Spiel unterbrochen!")
            ev3.screen.print("CENTER zum Fortfahren")
            wait(500)
            while not (Button.CENTER in ev3.buttons.pressed()):
                pass
            wait(500)
            a=time_ms()
            nn=nn+(a-b)
        foo=int(time_ms()-nn)
        ev3.screen.print(str(foo))
        wait(10)
        ev3.screen.clear()
    d=int(sqrt(int(time_ms()-nn)))+200
    ges[0]=randint(1, int(d))
    ges[1]=randint(int(d/2), int(2*d))
    ges[2]=(int(d)-(int(ges[0])+int(ges[1]))/3)*3
    timetoreset=randint(1, 5)

# Programmende (6)
ev3.screen.print("Du hast verloren! Das Auto ist gegen ein Hindernis gedonnert...")
ev3.speaker.say("I say it just because Master Johannes wants so")
wait(1000)
while not (Button.CENTER in ev3.buttons.pressed()):
    pass
wait(1000)
ev3.screen.print("Aber lass uns doch mal schauen, ob du vielleicht den Highscore geknackt hast!")
while not (Button.CENTER in ev3.buttons.pressed()):
    pass