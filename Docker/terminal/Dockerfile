FROM python:latest

COPY terminal.py ./

CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"