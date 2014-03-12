doorbell
========

raspberry pi is your doorbell

prepare raspberry
----

    sudo apt-get install -y python
    sudo apt-get install -y git
    sudo apt-get install -y python-rpi.gpio
    
* plug the doorbell button between GPIO pin 2 and GND
* add computer hostnames to listeners.txt - these will receive the ring signal
* add to rc.local 


    python /opt/path/to/doorbell/bootalert.py
    python /opt/path/to/doorbell/doorBellListener.py

install on windows
----
* place the .wav file in the public users music folder
* put the doorbellservice.exe file somewhere you like
* configure **dbWatchdog.ps1**
 * configure the correct path to the doorbellservice.exe
 * the default location is
  * e:\scripts\doorbell\doorbell\dist\DoorBellService.exe
* make the dbWatchdog.ps1 file into a scheduled task to run every minute 
* put the client.py file on your raspberry pi
 * _git clone https://github.com/andyseubert/doorbell_
* to ring the doorbell sound on the windows client run
<code>ringer.py hostname</code>


