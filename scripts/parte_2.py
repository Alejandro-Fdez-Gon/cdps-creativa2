from subprocess import call
import os

def image():
    try:
        # Creamos la carpeta referente al apartado 2.
        os.mkdir("./parte_2")
    except FileExistsError:
        pass

    if os.path.exists("./parte_2/Dockerfile"):
        pass
    else:
        # Creamos el archivo Dockerfile.
        fout = open("copia.txt", 'w')
        fout.write('FROM python:3.8.10\n')
        fout.write('RUN apt-get -y update && apt-get -y upgrade\n')
        fout.write('RUN apt-get install -y git && apt-get install -y python3-pip\n')
        fout.write('RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git\n')
        fout.write('ENV GROUP_NUMBER \'42\'\n')
        fout.write('WORKDIR practica_creativa2/bookinfo/src/productpage\n')
        fout.write('RUN sed -i "s/1.26.5/1.24/" ./requirements.txt\n')
        fout.write('RUN sed -i "s/Simple Bookstore App/$GROUP_NUMBER/" ./templates/productpage.html\n')
        fout.write('RUN pip3 install -r requirements.txt\n')
        fout.write('EXPOSE 9080\n')
        fout.write('CMD [\"python3\", \"productpage_monolith.py\", \"9080\"]\n')
        fout.close()
        call(["mv", "-f", "copia.txt", "./parte_2/Dockerfile"])

    call(["sudo", "docker", "rm", "42-productpage"])
    call(["sudo", "docker", "build", "-t", "42/productpage", "./parte_2"])
    call(["sudo", "docker", "run", "-tp", "9080:9080", "--name", "42-productpage", "42/productpage"])

