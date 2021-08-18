FROM ubuntu:20.10 AS base


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
RUN pip install -U pymoo

COPY --from=builder /app/src/CarlSAT_2021-main/CarlSAT .
COPY --from=builder /app/src/CarlSAT_2021-main/test1.wcard .
COPY . .
CMD ["python3", "src/wrapper.py", "test1.wcard", "2"]


