#!/usr/bin/python
import time
from time import sleep
import datetime
import os
import sys
import subprocess
from subprocess import Popen
import pynma
p = pynma.PyNMA( "12842c4d5f6061eb9543674248c3518edda9dd83343ebe19" )
application="alertpi boot"
event="DoorBell OnBoot"
description="doorbell just turned on"
priority=2

p.push(application, event, description)
subprocess.Popen([sys.executable, "/opt/doorbell/sendsms.py BootedUpJustNow" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)


