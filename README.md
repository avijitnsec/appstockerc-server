This repository provides steps and tools to deploy Asynchronous Scheduler using RabbitMQ And Dramatiq

<br/>
<br/>
<br/>
<br/>
<br/>

# Prerequisites

## Setup RabbitMQ

install docker in deployment environment  \
docker run -d --hostname my-rabbit --name scheduler-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management \
validate rabbitmq at <IP>:15672 as a management user (guest:guest)

<br/>
<br/>

## Start the Scheduler

<br/>
Build the Docker image
docker build -t scheduler --file Dockerfile .


