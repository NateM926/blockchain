from cc.tasks import refill_addresses_queue

def celery(self):
    a = refill_addresses_queue.delay()
    return a