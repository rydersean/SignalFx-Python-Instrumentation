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
counter=3

try:
    while True:
        ingest.send(
            gauges=[{
                'metric': 'dirtydog.python.testingestgauge',
                'value': randrange(5, 900),
                'timestamp': int(time.time()*1000) }],
            counters=[{
                'metric': 'dirtydog.python.testingestcounter',
                'value': counter,
                'timestamp': int(time.time()*1000) }],
            cumulative_counters=[{
                'metric': 'dirtydog.python.testingestccounter',
                'value': counter+1,
                'timestamp': int(time.time()*1000) }]
            )
        ingest.stop()
        counter=counter+3
        time.sleep(10)
        
except KeyboardInterrupt:
    pass
