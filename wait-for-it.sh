#!/usr/bin/env bash
set -e

echo "Starting wait-for-it script"
echo "Arguments: $@"

TIMEOUT=15
WAITFORIT_CMD="nc -z"

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 host port [timeout] [command... to run after success]"
    exit 1
fi

HOST="$1"
PORT="$2"
shift 2  # Shift the arguments to skip the host and port

if [ "$1" ]; then
    TIMEOUT="$1"
    shift 1  # Shift to skip the timeout
fi

echo "Waiting for $HOST:$PORT for up to $TIMEOUT seconds..."
for i in $(seq 1 $TIMEOUT); do
    if $WAITFORIT_CMD "$HOST" "$PORT" >/dev/null 2>&1; then
        echo "$HOST:$PORT is available."
        if [ "$#" -gt 0 ]; then
            echo "Executing command: $@"
            exec "$@"
        fi
        exit 0
    fi
    sleep 1
done

echo "Timeout waiting for $HOST:$PORT"
exit 1
