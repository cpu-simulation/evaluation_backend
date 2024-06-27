# Rest service

rest api service using Django and DRF 

## Responsibility

- Providing endpoint for frontend to access teams data
- Admin panel (separation of concerns? nah it's just an mvp) 
- push message to rabbit-mq

<!-- ## How to use -->
<!--  -->
<!-- ### Docker -->
<!--  -->
<!-- use docker to create and run image\ -->
<!-- 1.create docker image\ -->
<!-- `docker build -t rest-service .` -->
<!--  -->

## Observation

### Logger

of course this app uses logger and you can see the configurations in `rest/logger.json`,`rest/settings.py` as configuration and json formatter class at `rest/logger.py`.

I failed to configure `queue_handler` in logger as i did for test service.
but who cares. no one even reads this doc.
but if you think you can configure that, do not hesitate. you know how to contribute. 

this app has syslog output for logs too. so you can use **grafana LOKI** for logs 

this service also uses **DRF_API_LOGGER**. if you ask me, it's not needed but nice to have

### Prometheus
unfortunately this feature is not configured yet.\
or configured and i've forgotten to update this doc.\
but come back and ask me for this feature when ever you could pronounce "Prometheus".

## Env

|ENV            |Required   |default        |
|-----------    |  :-----:  |---------------|
|`SECRET_KEY`   |True       |               |
|`DEBUG`        |False      |`True`         |
|`MYSQL_HOST`   |False      |`mysql`        |
|`MYSQL_DB`     |True       |               |
|`MYSQL_USER`   |True       |               |
|`MYSQL_PASSWORD`|True       |               |
|`MYSQL_PORT`   |False      |`3306`         |


## Volume

log files??