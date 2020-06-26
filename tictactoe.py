import random
def eleccion_jug(opcion,tablero,choices):
	"""Con la opción recibida se ubica en el tablero
	(Int,list 2D,list 1D)->list 2D,list 1D"""
	if opcion<3:
		tablero[0][opcion] = "o"
		choices.remove(opcion)
	elif opcion<6:
		tablero[1][opcion-3] = "o"
		choices.remove(opcion)
	elif opcion<9:
		tablero[2][opcion-6] = "o"
		choices.remove(opcion)
	return tablero,choices
def eleccion_jug2(opcion,tablero,choices):
	"""Con la opción recibida se ubica en el tablero
	(Int,list 2D,list 1D)->list 2D,list 1D"""
	if opcion<3:
		tablero[0][opcion] = "x"
		choices.remove(opcion)
	elif opcion<6:
		tablero[1][opcion-3] = "x"
		choices.remove(opcion)
	elif opcion<9:
		tablero[2][opcion-6] = "x"
		choices.remove(opcion)
	return tablero,choices
def eleccion_consola(tablero,choices):
	"""Elige una opción y la ubica en el tablero
	(list 2D,list 1D)->list 2D,list 1D"""
	opcionia = random.choice(choices)
	if opcionia<3:
		tablero[0][opcionia] = "x"
		choices.remove(opcionia)
	elif opcionia<6:
		tablero[1][opcionia-3] = "x"
		choices.remove(opcionia)
	elif opcionia<9:
		tablero[2][opcionia-6] = "x"
		choices.remove(opcionia)
	return tablero,choices
def ganador(tablero,ganar,winner):
	for i in range(3):
		if tablero[i] == ["o","o","o"]:
			ganar = True
			winner = "jugador"
		elif tablero[i] == ["x","x","x"]:
			ganar = True
			winner = "ordenador"			
		elif tablero[0][i]=="x" and tablero[1][i]=="x" and tablero[2][i]=="x":
			ganar = True
			winner = "ordenador"
		elif tablero[0][i]=="o" and tablero[1][i]=="o" and tablero[2][i]=="o":
			ganar = True
			winner = "jugador"
	if tablero[0][0]=="x" and tablero[1][1]=="x" and tablero[2][2]=="x":
		ganar = True
		winner = "ordenador"
	elif tablero[0][0]=="o" and tablero[1][1]=="o" and tablero[2][2]=="o":
		ganar = True
		winner = "jugador"
	elif tablero[0][2]=="x" and tablero[1][1]=="x" and tablero[2][0]=="x":
		ganar = True
		winner = "ordenador"
	elif tablero[0][2]=="o" and tablero[1][1]=="o" and tablero[2][0]=="o":
		ganar = True
		winner = "jugador"
	return ganar,winner
def ganador2p(tablero,ganar,winner,name1,name2):
	for i in range(3):
		if tablero[i] == ["o","o","o"]:
			ganar = True
			winner = name1
		elif tablero[i] == ["x","x","x"]:
			ganar = True
			winner = name2			
		elif tablero[0][i]=="x" and tablero[1][i]=="x" and tablero[2][i]=="x":
			ganar = True
			winner = name2
		elif tablero[0][i]=="o" and tablero[1][i]=="o" and tablero[2][i]=="o":
			ganar = True
			winner = name1
	if tablero[0][0]=="x" and tablero[1][1]=="x" and tablero[2][2]=="x":
		ganar = True
		winner = name2
	elif tablero[0][0]=="o" and tablero[1][1]=="o" and tablero[2][2]=="o":
		ganar = True
		winner = name1
	elif tablero[0][2]=="x" and tablero[1][1]=="x" and tablero[2][0]=="x":
		ganar = True
		winner = name2
	elif tablero[0][2]=="o" and tablero[1][1]=="o" and tablero[2][0]=="o":
		ganar = True
		winner = name1			
	return ganar,winner
def imprimir(tablero):
	for i in range(3):
		print(tablero[i][0],"|",tablero[i][1],"|",tablero[i][2])
def main():
	winner = " "
	tablero = [[0,1,2],[3,4,5],[6,7,8]]
	ganar = False
	choices = [0,1,2,3,4,5,6,7,8]
	print("Bienvenido a Tic Tac Toe, si desea jugar contra la máquina escriba P\nsi desea hacer una partida de dos jugadores escriba C\nsi ve esta línea de nuevo, por favor ingrese una opción válida ")
	des = input("").lower()
	if des == "p":
		imprimir(tablero)
		while ganar == False:
			opcion = int(input("Digite la opción "))
			tablero,choices = eleccion_jug(opcion,tablero,choices)
			tablero,choices = eleccion_consola(tablero,choices)
			imprimir(tablero)
			ganar,winner = ganador(tablero,ganar,winner)
		print("El ganador de la partida es el " + winner)
	elif des == "r":
		name1 = input("Digite el nombre del jugador 1 ")
		name2 = input("Digite el nombre del jugador 1")
		imprimir(tablero)
		while ganar == False:
			opcion = int(input("Digite la opción",name1))
			tablero,choices = eleccion_jug(opcion,tablero,choices)
			opcion = int(input("Digite la opción",name2))
			tablero,choices = eleccion_jug2(opcion,tablero,choices)
			imprimir(tablero)
			ganar,winner = ganador2p(tablero,ganar,winner)
		print("El ganador de la partida es",winner)
	else:
		main()
main()