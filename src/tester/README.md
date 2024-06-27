# Test service
test service with python


## Responsibility

- Waits for a new test-request message on rabbit-mq
- Test that simulation's api
- Measure response time of each simulation
- Calculate the score of a simulation
- Store the results of that on mysql and influx

## Observation

this app only use logs as observation and metrics are not configured yet.

### Logger

logger config is in `conf/logger.json`. and json formatter class for python logs is in `core/logger.py`.
logs are handled by queue-handler with sends logging messages to a queue and let other handlers do there job in another thread.
in this way we have a very better performance.  

other handlers with are do there job on the queue are:
- syslog
- stdout
- stderr
- file-json

syslog is used to send the logs to local-7. in this way we could use **Promtail** to push the logs to **Loki** and do our observation from grafana.

file-json is a `RotatingFileHandler` with save the logs as json(using our manual formatter class in `core.logger.MyJSONFormatter`) in `/logs`.


## Env:

|ENV            |Required   |default        |
|-----------    |  :-----:  |---------------|
|`DB_URL`       |True       |               |
|`RABBITMQ_URL` |False      |`rabbitmq`     |
|`TEST_QUEUE`   |False      |`Test_Queue`   |
