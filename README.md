doorbell
========

raspberry pi is your doorbell

* place the .wav file in the public users music folder
* put the doorbellservice.exe file somewhere you like
* make the dbWatchdog.ps1 file into a scheduled task once you configure the correct path in it to the doorbellservice.exe
 * the default location is
* e:\scripts\doorbell\doorbell\dist\DoorBellService.exe
* put the client.py file on your raspberry pi
* to ring the doorbell sound on the windows client run
<code>client.py hostname</code>

