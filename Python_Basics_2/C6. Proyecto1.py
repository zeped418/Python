#Proyecto de python - Juego de lógica

import random

opciones=("piedra", "papel", "tijera")

win_comp=0
win_user=0
ronda=1



while True:
  
  print("\n")
  print("*"*15)
  print("Round " + str(ronda))
  print("Computadora: ", win_comp)
  print("Humano: ", win_user)
  print("*"*15)
  
  # opción del usuario
  user = input("\n 🤖 Eige piedra, papel o tijera  =>  ")
  user = user.lower()

  if not user in opciones:
    print("Opcion no valida")
    continue
  
  computer=random.choice(opciones)

  print("\n La computadora eligió ", computer, "\n")
  #igual es ==, si es = solo es asignación
  
  if user == computer:
    print("Es un empate!")
    #versión con piedra
  elif user == "piedra":
    if computer == "tijera":
      print("Piedra vence a la tijera")
      print("Usuario victorioso")
      win_user += 1
    else:
      print("Papel gana a la piedra")
      print("Computadora wins")
      win_comp += 1
    #versión con papel
  elif user == "papel":
    if computer =="tijera":
      print("computadora venció")
      print("tijeras cortan papel")
      win_comp += 1
    else:
      print("Papel vence a la piedra")
      print("Usuario ha vencido a la maquina")
      win_user += 1
  elif user=="tijera":
    if computer=="papel":
      print("Usuario ganó")
      print("tijera mocha al papel")
      win_user += 1
    else:
      print("Piedra gana a tijera")
      print("Usuario pierde")
      win_comp += 1
  
  if win_user==3:
    print("La humanidad vence a la tecnología 🏆")
    break
  if win_comp==3:
    print("La maquina vence al humano 🐱‍🚀")
    break
  ronda=ronda+1