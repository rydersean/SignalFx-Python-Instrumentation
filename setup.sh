#Uncomment INGEST_ENDPOINT depending on if you want to use OTEL Collector, SignalFx Smart Agent or direct to SignalFx Ingest Endpoint
#export INGEST_ENDPOINT=http://0.0.0.0:9943 #OTEL Collector
#export INGEST_ENDPOINT=https://ingest.us0.signalfx.com #SFX Ingest
export INGEST_ENDPOINT=http://localhost:9080 #SignalFx SmartAgent on localhost
export API_ENDPOINT=https://api.us0.signalfx.com
export STREAM_ENDPOINT=https://stream.us0.signalfx.com
export ORG_TOKEN=ENTER_YOUR_ORG_TOKEN_HERE
