FROM ubuntu:20.10 AS base

WORKDIR /app/


### test ###
FROM mysql as DB


WORKDIR /app/

RUN apt update -y && apt -y install python3 && apt-get -y install python3-pip 

RUN pip3 install -U pymoo && pip3 install -U numpy && pip3 install -U mysql-connector-python 


RUN apt update -y && apt -y install python3
RUN apt -y install python3-pip
RUN pip3 install -U pymoo && pip3 install -U numpy
ENV MYSQL_DATABASE hyperopt
ADD ./sqlscripts/ /docker-entrypoint-initdb.d/ 
COPY . .

#NOTE: may have to play around with port number to get it to work

#Eventually the parameters passed into the wrapper class should be more extensive than just the problem card name.
