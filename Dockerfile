FROM ubuntu:latest

RUN apt-get update -y && apt-get install python3 python3-pip -y
RUN pip3 install flask tinydb
