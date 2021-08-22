FROM ubuntu:20.10 AS base

#We actually do not need to give the builder part to the client. We only need to give the CarlSat executable
#This would obviously neccessitate changes to the dockerfile in later stages of development.
FROM base as builder        
WORKDIR /app/src/

RUN apt update -y && apt -y install clang-11 lldb-11 lld-11 && apt -y install clang && apt -y install util-linux

RUN apt update -y && apt -y install wget && apt -y install unzip && apt -y install make


RUN wget https://github.com/JBontes/CarlSAT_2021/archive/refs/heads/main.zip

RUN ls main.zip | xargs -n1 unzip
RUN rm main.zip


WORKDIR /app/src/CarlSAT_2021-main/
RUN make clean && make



FROM base as exec
WORKDIR /app/
RUN apt update -y && apt -y install python3 && apt -y install pip

RUN pip install -U pymoo && pip install -U numpy

COPY --from=builder /app/src/CarlSAT_2021-main/CarlSAT .

#We will eventually be copying in a folder of wcards I imagine.
COPY --from=builder /app/src/CarlSAT_2021-main/test1.wcard .

COPY . .
#Eventually the parameters passed into the wrapper class should be more extensive than just the problem card name.
CMD ["python3", "src/wrapper.py", "test1.wcard", "2"]   



