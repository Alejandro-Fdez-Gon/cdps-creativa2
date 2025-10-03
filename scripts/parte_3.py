from subprocess import call
import os

def crear_dir(file):
    try:
        os.mkdir(file)
    except FileExistsError:
        pass

def web():    
    crear_dir("./parte_3/web")
    
    if os.path.exists("./parte_3/web/Dockerfile"):
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
        fout.write('CMD [\"python3\", \"productpage.py\", \"9080\"]\n')
        fout.close()
        call(["mv", "-f", "copia.txt", "./parte_3/web/Dockerfile"])

def details():
    crear_dir("./parte_3/details")
    call(["cp", "parte_1/practica_creativa2/bookinfo/src/details/details.rb", "parte_3/details"]) 

    if os.path.exists("./parte_3/details/Dockerfile"):
        pass
    else:
        # Creamos el archivo Dockerfile.
        fout = open("copia.txt", 'w')
        fout.write('FROM ruby:2.7.1-slim\n')
        fout.write('COPY details.rb /opt/microservices/details.rb\n')
        fout.write('ENV SERVICE_VERSION v1\n')
        fout.write('ENV ENABLE_EXTERNAL_BOOK_SERVICE true\n')
        fout.write('EXPOSE 9080\n')
        fout.write('CMD [\"ruby\", \"/opt/microservices/details.rb\", \"9080\"]\n')
        fout.close()
        call(["mv", "-f", "copia.txt", "./parte_3/details/Dockerfile"])

def ratings():
    crear_dir("./parte_3/ratings")  
    call(["cp", "parte_1/practica_creativa2/bookinfo/src/ratings/package.json", "parte_3/ratings"])
    call(["cp", "parte_1/practica_creativa2/bookinfo/src/ratings/ratings.js", "parte_3/ratings"])

    if os.path.exists("./parte_3/ratings/Dockerfile"):
        pass
    else:
        # Creamos el archivo Dockerfile.
        fout = open("copia.txt", 'w')
        fout.write('FROM node:12.18.1-slim\n')
        fout.write('COPY package.json /opt/microservices/package.json\n')
        fout.write('COPY ratings.js /opt/microservices/ratings.js\n')
        fout.write('WORKDIR /opt/microservices\n')
        fout.write('RUN npm install\n')
        fout.write('ENV SERVICE_VERSION v1\n')
        fout.write('EXPOSE 9080\n')
        fout.write('CMD [\"node\", \"ratings.js\", \"9080\"]\n')
        fout.close()
        call(["mv", "-f", "copia.txt", "./parte_3/ratings/Dockerfile"])

def yaml():
    if os.path.exists("./parte_3/docker-compose-v1.yaml"):
        pass
    else:
        # Creamos el docker-compose.yaml.
        f1 = open("v1.txt", 'w')
        f1.write('version: "3"\n')
        f1.write('\nservices:\n')
        f1.write('  web:\n')
        f1.write('    build: ./web\n    image: 42/productpage\n    container_name: 42-productpage\n    ports:\n      - "9080:9080"\n')
        f1.write('\n  details:\n')
        f1.write('    build: ./details\n    image: 42/details\n    container_name: 42-details\n')
        f1.write('\n  ratings:\n')
        f1.write('    build: ./ratings\n    image: 42/ratings\n    container_name: 42-ratings\n')
        f1.write('\n  reviews:\n')
        f1.write('    build: ../parte_1/practica_creativa2/bookinfo/src/reviews/reviews-wlpcfg\n    image: 42/reviews_v1\n    container_name: 42-reviews-v1\n    environment:\n      - ENABLE_RATINGS=false\n      - SERVICE_VERSION=v1\n      - STAR_COLOR=black\n')
        f1.close()

        if os.path.exists("./parte_3/docker-compose-v2.yaml") and os.path.exists("./parte_3/docker-compose-v3.yaml"):
            pass
        else:
            f1 = open("v1.txt", 'r')
            f2 = open("v2.txt", 'w')
            f3 = open("v3.txt", 'w')
            for line in f1:
                if "reviews_v1" in line:
                    f2.write("    image: 42/reviews_v2\n")
                    f3.write("    image: 42/reviews_v3\n")
                elif "reviews-v1" in line:
                    f2.write("    container_name: 42-reviews-v2\n")
                    f3.write("    container_name: 42-reviews-v3\n")                
                elif "ENABLE_RATINGS" in line:
                    f2.write("      - ENABLE_RATINGS=true\n")
                    f3.write("      - ENABLE_RATINGS=true\n")
                elif "SERVICE_VERSION" in line:
                    f2.write("      - SERVICE_VERSION=v2\n")
                    f3.write("      - SERVICE_VERSION=v3\n")
                elif "STAR_COLOR" in line:
                    f2.write(line)
                    f3.write("      - STAR_COLOR=red\n")
                else:
                    f2.write(line)
                    f3.write(line)
            f1.close()
            f2.close()
            f3.close()       

        call(["mv", "-f", "v1.txt", "./parte_3/docker-compose-v1.yaml"])
        call(["mv", "-f", "v2.txt", "./parte_3/docker-compose-v2.yaml"])
        call(["mv", "-f", "v3.txt", "./parte_3/docker-compose-v3.yaml"])


def compose():
    try:
        # Creamos la carpeta referente al apartado 2.
        os.mkdir("./parte_3")
    except FileExistsError:
        pass
    
    # Creamos los Dockerfile de cada contenedor
    web()
    details()
    ratings()

    # Creamos el docker-compose.yaml.
    yaml()

def run(version):
    call(["sudo", "docker", "rm", "42-productpage"])
    call(["sudo", "docker-compose", "-f", "./parte_3/docker-compose-"+ version +".yaml", "build"])
    call(["sudo", "docker-compose", "-f", "./parte_3/docker-compose-"+ version +".yaml", "up"])