FROM ubuntu:20.10 AS base

WORKDIR /app/src/

RUN apt update -y && apt -y install clang-11 lldb-11 lld-11 && apt -y install clang && apt -y install util-linux

<<<<<<< HEAD
COPY . .
WORKDIR /app/src/
CMD ["python3", "wrapper.py", "test1.wcard", "2"]  
### test ###


### Command to start environment w/ database:
#$ docker run -d -p 3306:3306 --name test \
# -e MYSQL_ROOT_PASSWORD=supersecret capstone-project
=======
RUN apt update -y && apt -y install wget && apt -y install unzip && apt -y install make


RUN wget https://github.com/JBontes/CarlSAT_2021/archive/refs/heads/main.zip

RUN ls main.zip | xargs -n1 unzip
RUN rm main.zip


WORKDIR /app/src/CarlSAT_2021-main/
RUN make clean && make

### test ###
FROM ubuntu/mysql as DB


WORKDIR /app/

RUN apt update -y && apt -y install python3 && apt -y install python3-pip &&  apt -y install libc6

RUN pip3 install -U pymoo && pip3 install -U numpy && pip3 install -U mysql-connector-python 


RUN apt update -y && apt -y install python3
RUN apt -y install python3-pip
RUN pip3 install -U pymoo && pip3 install -U numpy
ENV MYSQL_DATABASE hyperopt
ADD ./sqlscripts/ /docker-entrypoint-initdb.d/ 
COPY . .
>>>>>>> 547eb52539cfc7cb3438cf75d165b484e4331b0b

#NOTE: may have to play around with port number to get it to work

#Eventually the parameters passed into the wrapper class should be more extensive than just the problem card name.
<<<<<<< HEAD
 
=======
>>>>>>> 547eb52539cfc7cb3438cf75d165b484e4331b0b
