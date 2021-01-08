# SignalFx-Python-Instrumentation
SignalFx-Python Manual instrumentation - Send your metrics to SignalFx using Python

I wrote this python instrumentation based on the documentation provided here https://github.com/signalfx/signalfx-python

Installation

Install python3

$ sudo apt install python3 python-pip

To install with pip:

$ pip install signalfx

To install from source:

$ git clone https://github.com/signalfx/signalfx-python.git
$ cd signalfx-python/
$ pip install -e .

$ git clone https://github.com/rydersean/SignalFx-Python-Instrumentation.git
1. Add your org token to the setup.sh file
2. Uncomment ingest environment variable based on if you want to send to OTEL Collector, SignalFx SmartAgent or SignalFx Ingest directly
2. $ source setup.sh
3. $ python SignalFx-Python-Metrics.py
4. Watch your terminal for debug info
