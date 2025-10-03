import sys
from subprocess import call

def indiv(file):
    try:
        call(["sudo", "rm", "-rf", file])
    except FileNotFoundError:
        pass

def total():

    indiv("parte_1")
    indiv("parte_2")
    indiv("parte_3")

    if len(sys.argv) > 2 and sys.argv[2] == "all":
        # Borramos todos los archivos creados durante la practica.
        indiv("./scripts")
        indiv("creativa_2.zip")
        indiv("creativa_2.pdf")
        indiv("creativa_2.py")

            
