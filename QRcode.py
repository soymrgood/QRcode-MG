#!/usr/bin/python

# IMPORTANDO LOS MODULOS
import os, time, subprocess
from colorama import Fore, Back, Style, init
init()

##################################################################
# By: Mr. Good                                                   #
# Canal de YouTube: https://www.youtube.com/c/MrGoodCanalOficial #
# Soy el creador de esta herramienta :v compartela               #  
#                                                                #
# Este script esta hecho con el fin de poder crear codigos QR    #
# pueden camuflar enlaces phishing :)                            #
##################################################################

os.system("clear")
os.system("bash .QRcode.sh")

# MENU
print (Fore.WHITE + Style.BRIGHT + "\n(1)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT + " Crear codigo QR" + Style.RESET_ALL)

print (Fore.WHITE + Style.BRIGHT + "(0)" + Style.RESET_ALL + Fore.CYAN + Style.BRIGHT + " ->" + Style.RESET_ALL + Fore.RED + Style.BRIGHT + " Exit" + Style.RESET_ALL)


opcion = int(input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL))

# CONDICIONALES
if opcion == 0:
	os.system("clear")
	
	
elif opcion == 1:
	print(Fore.YELLOW + Style.BRIGHT + "\n Introduce la URL que deseas convertir a codigo QR: " + Style.RESET_ALL)
	qr = input(Fore.WHITE + Style.BRIGHT + "\n>> " + Style.RESET_ALL)
	os.system('clear')
	print('')
	os.system("curl qrcode.show/"+qr)
else:
	print(Fore.RED + "Opcion incorrecta, vuelve a intentarlo." + Style.RESET_ALL)
