doorbell
========

raspberry pi is your doorbell

prepare raspberry
----
<code>
    sudo apt-get install -y python git python-rpi.gpio
</code>    
* the doorbell button goes to a solid state relay which is connected on its NO terminals to the buttonPin and GND
* add computer hostnames to listeners.txt - these will receive the ring signal
* add to rc.local 

<code>
    /opt/doorbell/bootalert.py
    /opt/doorbell/doorBellListener.py
    /opt/doorbell/unlockDoor.py
</code>

* add to crontab

     * * * * * /opt/doorbell/doorbellWatchdog.sh

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


install on raspberry to be the ringer
----
 * install as per "prepare raspberry" 
 * git clone into /opt/doorbell
 * add to rc.local /opt/doorbell/RingerPi.py &
 * make sure the audio is working. I found this page helpful http://computers.tutsplus.com/articles/using-a-usb-audio-device-with-a-raspberry-pi--mac-55876
