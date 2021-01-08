import signalfx
import time
from random import randrange
import logging
import sys
import os

client = signalfx.SignalFx(api_endpoint=os.getenv("API_ENDPOINT"),
        ingest_endpoint=os.getenv("INGEST_ENDPOINT"),
        stream_endpoint=os.getenv("STREAM_ENDPOINT"))

ingest = client.ingest(os.getenv("ORG_TOKEN"))
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

try:
    while True:
        ingest.send(
            gauges=[{
                'metric': 'dirtydog.python.testingestgauge',
                'value': randrange(5, 900),
                'timestamp': int(time.time()*1000) }],
            counters=[{
                'metric': 'dirtydog.python.testingestcounter',
                'value': randrange(1,10),
                'timestamp': int(time.time()*1000) }],
            cumulative_counters=[{
                'metric': 'dirtydog.python.testingestccounter',
                'value': int(randrange(1,1000)),
                'timestamp': int(time.time()*1000) }]
            )
        ingest.stop()
        time.sleep(10)
except KeyboardInterrupt:
    pass
