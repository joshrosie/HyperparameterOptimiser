FROM ubuntu:20.10 AS base

WORKDIR /app/
RUN apt update -y && apt -y install python3 && apt -y install pip

RUN pip install -U pymoo && pip install -U numpy

COPY . .
#RUN cd src/ && ls
WORKDIR /app/src/

#Eventually the parameters passed into the wrapper class should be more extensive than just the problem card name.
CMD ["python3", "wrapper.py", "test1.wcard", "2"]   



