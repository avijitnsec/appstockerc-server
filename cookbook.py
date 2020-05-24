import dramatiq
import sys

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from dramatiq.brokers.rabbitmq import RabbitmqBroker


rabbitmq_broker = RabbitmqBroker()
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor
def print_current_date():
    print(datetime.now())


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(
        print_current_date,
        CronTrigger.from_crontab("* * * * *"),
    )
    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()