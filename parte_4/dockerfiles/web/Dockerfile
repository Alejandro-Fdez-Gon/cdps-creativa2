FROM python:3.8.10
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y git && apt-get install -y python3-pip
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git
ENV GROUP_NUMBER '42'
WORKDIR practica_creativa2/bookinfo/src/productpage
RUN sed -i "s/1.26.5/1.24/" ./requirements.txt
RUN sed -i "s/Simple Bookstore App/$GROUP_NUMBER/" ./templates/productpage.html
RUN pip3 install -r requirements.txt
EXPOSE 9080
CMD ["python3", "productpage.py", "9080"]
