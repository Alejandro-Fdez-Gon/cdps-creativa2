from subprocess import call
import os
import sys
from scripts import inicio, parte_1, parte_2, parte_3, destroy

# Variables globales.
github = "https://github.com/CDPS-ETSIT/practica_creativa2.git"
productpage = "./parte_1/practica_creativa2/bookinfo/src/productpage/"
puerto = '4000'
os.environ['GROUP_NUMBER'] = '42'

# Esqueleto del codigo.
if len(sys.argv) < 2:
    # Paso previo.
    inicio.actualizar()
    inicio.previo(github, productpage)
    exit()

elif sys.argv[1] == "1":
    # Primera parte.
    parte_1.mod_port(puerto, productpage)
    parte_1.arranque(puerto, productpage)

elif sys.argv[1] == "2":
    # Segunda parte.
    parte_2.image()

elif sys.argv[1] == "3":
    # Tercera parte.
    if len(sys.argv) == 2:
        parte_3.compose()
    elif len(sys.argv) == 3:
        if sys.argv[2] == "v1" or sys.argv[2] == "v2" or sys.argv[2] == "v3":
            parte_3.run(sys.argv[2])    
        else:
            print("Version equivocada")

elif sys.argv[1] == "destroy":
    # Modulo de borrado de archivos.
    destroy.total()

else:
    # Valores introducidos incorrectos.
    print("Error: Te equivocaste al llamar al script, vuelva a probar.")
    


