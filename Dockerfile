FROM ubuntu:20.10 AS base

WORKDIR /app/
RUN apt update -y && apt -y install python3 && apt -y install pip

RUN pip install -U pymoo && pip install -U numpy && pip install -U pylint

COPY . .
WORKDIR /app/src/
CMD ["python3", "wrapper.py", "test1.wcard", "2"]  
### test ###

<<<<<<< HEAD
#Eventually the parameters passed into the wrapper class should be more extensive than just the problem card name.
CMD ["python3", "Wrapper.py", "test1.wcard", "2"]   
#CMD ["python3", "wrapper.py", "test1.wcard", "2","cost"]
=======
>>>>>>> 0c3eed5d92a3c126ccb8af5acaca3680e5066fb9

### Command to start environment w/ database:
#$ docker run -d -p 3306:3306 --name test \
# -e MYSQL_ROOT_PASSWORD=supersecret capstone-project

#NOTE: may have to play around with port number to get it to work

#Eventually the parameters passed into the wrapper class should be more extensive than just the problem card name.
 