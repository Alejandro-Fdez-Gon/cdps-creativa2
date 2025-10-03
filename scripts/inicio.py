from subprocess import call
import os

def actualizar():
    # Actualizamos los paquetes.
    call(["sudo", "apt-get", "-y", "update"])
    call(["sudo", "apt-get", "-y", "upgrade"])

    # Instalamos PIP.
    call(["sudo", "apt-get", "install", "-y", "python3-pip"])

    # Instalamos docker y docker-compose.
    call(["sudo", "apt-get", "install", "-y", "docker.io"])
    call(["sudo", "apt-get", "install", "-y", "docker-compose"])


def previo(github, productpage):
    try:
        # Creamos la carpeta referente al apartado 1.
        os.mkdir("./parte_1")
    except FileExistsError:
        pass
    
    # Descargamos el repositorio
    call(["git", "clone", github, "./parte_1/practica_creativa2"])

    # Modificacion requierements.txt
    fin = open(productpage + "requirements.txt", 'r')
    fout = open("copia.txt", 'w')
    for line in fin:
        if 'urllib3' in line:
            fout.write('urllib3==1.24\n')
        else:
            fout.write(line)  
    fin.close()
    fout.close()
    call(["rm", "-f", productpage + "requirements.txt"])
    call(["mv", "-f", "copia.txt", productpage + "requirements.txt"])

    # Instalamos las dependencias
    call(["pip3", "install", "-r", productpage + "requirements.txt"])

    # Modificamos el titulo de la pagina web.
    group_number = os.getenv('GROUP_NUMBER')
    fin = open(productpage + "templates/productpage.html", "r")
    fout = open("copia.txt", 'w')
    for line in fin:
        if "{% block title %}Simple Bookstore App{% endblock %}" in line:
            fout.write("{% block title %}"+group_number+"{% endblock %}")
        else:
            fout.write(line)
    fin.close()
    fout.close()
    call(["rm", productpage + "templates/productpage.html"])
    call(["mv", "copia.txt", productpage + "templates/productpage.html"])