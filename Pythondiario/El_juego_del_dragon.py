import os
os.system('cls')
import random, time, sys


"""En este juego, el jugador se encuentra en una tierra llena de dragones.
 Los dragones viven en sus caves y en ellas guardan sus tesoros. Algunos dragones son buenos y compartirán su tesoro,
   otros dragones son codiciosos y hambrientos y se comerán a cualquiera que pise su cave.
 El jugador se encuentra frente a las dos caves, una con un dragón amable y otra con un dragón hambriento.
 El jugador tiene que elegir a cual cave entrar, sin saber de ante mano donde esta uno u el otro."""

#! /usr/bin/env python
# -*- coding: utf-8 -*-


#Reino del Dragon....


text = """Estamos en una tierra llena de dragones.  .  .
Delante nuestro hay dos cuevas.
En una una el dragón que la habita es amigable y compartirá el tesoro contigo....
en la otra hay un dragón muy codicioso y malvado y te comerá si te ve  .  .  .
"""

def intro():

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)

    print ("\n")

def start ():
    intro()
    choose_cave(0)
   


def raw_input():
   return input()

def choose_cave(punts):
    cave = ""
    print ("¿A qué cueva quieres entrar? 1 o 2?", end=' ')
    cave = raw_input()
    
    if cave != "1" and cave != "2":
        print("\nSólo se puede elegir 1 o 2, intente de nuevo\n")
        choose_cave(punts)
    else:
      check_cave(cave, punts)



def start_again():
    print("Quieres jugar de nuevo? (si o no)", end=' ')
    again = raw_input()
    if again == ("s") or again == ("si"):
  
     choose_cave(0)
 
    else:
       print("Fin del juego")
       return

def check_cave(cave, score):
    
    print ("Te acercas a la cueva...")
    time.sleep(1)
    print ("Esta oscuro y tenebroso...")
    time.sleep(1)
    print ("Un gran dragón salta delante tuyo, abre su boca y...")
    print ("")
    time.sleep(2)
   
    random_cave = random.randint (1, 2)
    random_cave=str(random_cave)
   
    if  cave == random_cave: 
        print ("Te entrega el tesoro...")
        score +=100
        choose_cave(score)
    else:
        print ("El dragon te come de un bocado....")
        print(f"Has ganado {score} puntos")
        start_again()

start()


   


   



