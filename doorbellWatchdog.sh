#!/bin/bash
PID=$(pgrep door)

if [[ -z "$PID" ]]; then
  /opt/doorbell/doorBellListener.py & 
fi
unset PID
