FROM ubuntu:20.10 AS base


### test ###
FROM mysql as DB

WORKDIR /app/
RUN apt update -y && apt -y install python3 && apt-get -y install pip

RUN pip install -U pymoo && pip install -U numpy

COPY . .
ENV MYSQL_DATABASE company
COPY ./sqlScripts/ /docker-entrypoint-initdb.d/ 
### Command to start environment w/ database:
#$ docker run -d -p 3306:3306 --name test \
# -e MYSQL_ROOT_PASSWORD=pw

#NOTE: may have to play around with port number to get it to work

#Eventually the parameters passed into the wrapper class should be more extensive than just the problem card name.
#CMD ["python3", "wrapper.py", "test1.wcard", "2"]   