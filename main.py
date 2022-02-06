#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font

import time
from random import randint
from math import sqrt


# Objects (1)
ev3 = EV3Brick()
ev3.screen.print("Lädt/Loading")
ll=Motor(Port.A)
mm=Motor(Port.B)
rr=Motor(Port.C)
auto=TouchSensor(Port.S1)
ok=TouchSensor(Port.S2)
voice=False
voiceconfig={"language": "de", "voice": "f1", "speed": 120, "pitch": 50, "volume": 60}
printconfig={"ySide": int(Font('Lucida', 12).height/2), "xSide": int(Font('Lucida', 12).width), "xText": Font('Lucida', 12).width, "yText": Font('Lucida', 12).height, "maxwidth": int(ev3.screen.width/Font('Lucida', 12).width-2), "maxheight": int(ev3.screen.width/Font('Lucida', 12).height-1)}
# Leanders Texte "texte" einlesen
d=open("de.txt", "r"); dd=d.read(); exec(dd); d.close()


# Definitions (2)
def read_texte():
    d=open(voiceconfig["language"] +".txt", "r"); r=d.read(); exec(r); d.close()
def buffer():
    while not (Button.CENTER in ev3.buttons.pressed()):
        pass
    wait(500)
def time_ms():
    fds=time.time()
    return int(fds*1000)
def showwait(texte=["", ""]):
    ev3.screen.clear()
    for text in texte:
        output_(text)
    output_("[CENTER]", pos=(50, 110))
    buffer()
def highscore():
    # Leanderboard und so nehmen!
    buffer()
def output():
    emph=0
    while not (Button.CENTER in ev3.buttons.pressed()):
        ev3.screen.clear()
        for i in range(0, len(texte[5])):
            if emph==i:
                output_(text=texte[5][i], pos=(30, 5+23*i), text_color=Color.WHITE, background_color=Color.BLACK)
            else:
                output_(text=texte[5][i], pos=(30, 5+23*i), text_color=Color.BLACK, background_color=Color.WHITE)
            while not ((Button.UP in ev3.buttons.pressed()) or (Button.DOWN in ev3.buttons.pressed())):
                pass
            if (Button.DOWN in ev3.buttons.pressed()):
                emph=(emph+1)%len(texte[5]); wait(200); ev3.screen.clear(); continue
            elif (Button.UP in ev3.buttons.pressed()):
                emph=(emph-1)%len(texte[5]); wait(200); ev3.screen.clear(); continue
    if emph<2:
        voiceconfig["language"]="de"
        ev3.speaker.set_volume(voiceconfig["volume"])
        ev3.speaker.set_speech_options(voiceconfig["language"], voiceconfig["voice"], voiceconfig["speed"], voiceconfig["pitch"])
    else:
        voiceconfig["language"]="de"
        ev3.speaker.set_volume(voiceconfig["volume"])
        ev3.speaker.set_speech_options(voiceconfig["language"], voiceconfig["voice"], voiceconfig["speed"], voiceconfig["pitch"])
    if emph%2==0:
        voice=True
    else:
        voice=False
    read_texte(); wait(500)
def highscore_():
    # hier das zeugs zum überschreiben, namen festlegen etc machen
    buffer()
def output_(text="default", pos=(5, 60), text_color=Color.BLACK, background_color=Color.WHITE):
    if voice==True:
        ev3.speaker.say(text)
        if print_==False:
            return
    ev3.screen.set_font(Font('Lucida', 9))
    ev3.screen.draw_text(x=pos[0], y=pos[1], text=text, text_color=text_color, background_color=background_color)


# Begrüßung (3)
ev3.screen.clear()
showwait([texte[0][0]])
buffer()


# Menü (4)
emph=0
while not (Button.CENTER in ev3.buttons.pressed()):
    wait(200)
    ev3.screen.clear()
    for i in range(0, len(texte[2])):
        if emph==i:
            output_(text=texte[2][i], pos=(30, 15+23*i), text_color=Color.WHITE, background_color=Color.BLACK)
        else:
            output_(text=texte[2][i], pos=(30, 15+23*i), text_color=Color.BLACK, background_color=Color.WHITE)
    while not ((Button.RIGHT in ev3.buttons.pressed()) or (Button.LEFT in ev3.buttons.pressed()) or (Button.UP in ev3.buttons.pressed()) or (Button.DOWN in ev3.buttons.pressed()) or (Button.CENTER in ev3.buttons.pressed())):
        pass
    if (Button.DOWN in ev3.buttons.pressed()):
        emph=(emph+1)%len(texte[2])
        continue
    elif (Button.UP in ev3.buttons.pressed()):
        emph=(emph-1)%len(texte[2])
        continue
    elif (Button.RIGHT in ev3.buttons.pressed()) or (Button.LEFT in ev3.buttons.pressed()):
        if (emph==0) or (emph==1):
            for text in texte[3+emph]:
                showwait([text])
            emph=0
            continue
        elif emph==2:
            output()
            emph=0
            continue
        elif emph==3:
            emph=0
            # leanders ding
            continue


# Hauptprogramm (5)
## Die Durchschnittsgeschwindigkeit d ist die Wurzel der Zeit plus 200, die seit nn verstrichen ist.
## ges=(l, m, r) soll das Geschwindigkeitstupel sein; l=randint(1, d), m=randint(d/2, 2d), r=(d-(l+m)/3)*3
wait(500)
ev3.speaker.beep()
startv=-200
d=200
ges=[startv, startv, startv]
timetoreset=randint(1, 5)
run_=True
nn=time_ms()
while run_==True:
    ll.run(-(int(ges[randint(0, 1)])))
    mm.run(-(int(ges[randint(0, 2)])))
    rr.run(-(int(ges[randint(1, 2)])))
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
showwait(["Du hast verloren! Das Auto ist gegen ein Hindernis gedonnert..."])
buffer()
showwait(["Aber lass uns doch mal schauen, ob du vielleicht den Highscore geknackt hast!"])
while not (Button.CENTER in ev3.buttons.pressed()):
    pass
# Leanders Programmteil einfügen