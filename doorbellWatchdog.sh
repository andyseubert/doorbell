#!/bin/bash
if pgrep door >/dev/null 2>&1
then
  /opt/doorbell/doorBellListener.py &
 echo "starting listener"
fi

